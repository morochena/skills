#!/usr/bin/env python3
"""Run frozen old/new skills on offline tasks; preserve every attempt."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time

from fixtures import CASES, build


REPO = Path(__file__).resolve().parents[2]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(root):
    return {str(p.relative_to(root)): sha(p) for p in sorted(root.rglob('*')) if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts}


def metrics(home):
    sessions = []
    tools = {}
    for path in sorted(home.glob('sessions/**/*.jsonl')):
        last_usage = None
        meta = {}
        contexts = set()
        requests = 0
        for line in path.read_text().splitlines():
            event = json.loads(line)
            payload = event.get('payload', {})
            if event.get('type') == 'session_meta':
                meta = {k: payload.get(k) for k in ['id', 'source', 'forked_from_id', 'thread_source']}
            elif event.get('type') == 'turn_context':
                contexts.add((payload.get('model'), payload.get('effort')))
            elif event.get('type') == 'event_msg' and payload.get('type') == 'token_count' and payload.get('info'):
                last_usage = payload['info']['total_token_usage']
            elif event.get('type') == 'response_item' and payload.get('type') in ['function_call', 'custom_tool_call']:
                name = payload.get('name', 'unknown')
                tools[name] = tools.get(name, 0) + 1
            elif event.get('type') == 'response_item' and payload.get('type') == 'message' and payload.get('role') == 'assistant':
                requests += 1
        sessions.append({**meta, 'usage': last_usage, 'models': sorted(contexts), 'assistant_messages': requests})
    usage = {}
    for session in sessions:
        if session['usage']:
            for key, value in session['usage'].items():
                usage[key] = usage.get(key, 0) + value
    return {'sessions': sessions, 'session_count': len(sessions), 'usage_sum': usage or None, 'tools': tools}


def outcomes(directory, case, before):
    workspace = directory / 'workspace'
    after = inventory(workspace)
    changed = sorted(k for k in set(before) | set(after) if before.get(k) != after.get(k))
    result = {'changed_files': changed}
    if case in ['transfer', 'utilities']:
        hidden = subprocess.run([sys.executable, str(Path(__file__).with_name('check_outcomes.py')), str(workspace), case], capture_output=True, text=True, timeout=60)
        result['hidden'] = json.loads(hidden.stdout) if hidden.returncode == 0 else {'passed': False, 'error': hidden.stderr}
        visible = subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'], cwd=workspace, capture_output=True, text=True, timeout=60)
        result['visible'] = {'passed': visible.returncode == 0, 'log': visible.stdout + visible.stderr}
        result['scope_ok'] = all(p == 'README.md' or (p.startswith(('ledger/', 'tests/')) if case == 'transfer' else p.startswith(('utilities/', 'tests/'))) for p in changed)
        result['automated_pass'] = result['hidden']['passed'] and result['visible']['passed'] and result['scope_ok']
    elif case == 'verifier':
        evidence_path = workspace / 'evidence/cli.jsonl'
        evidence = [json.loads(line) for line in evidence_path.read_text().splitlines()] if evidence_path.exists() else []
        commands = sorted({item['command'] for item in evidence})
        result.update({
            'scope_ok': all(p.startswith(('verification/verify-taskdesk/', 'evidence/', '.scratch/')) for p in changed),
            'product_unchanged': before['app.py'] == after.get('app.py'),
            'commands': commands,
            'live_complete': set(['doctor', 'add', 'list', 'complete', 'archive', 'status']).issubset(commands),
            'scratch_clean': not (workspace / '.scratch/tasks.json').exists(),
            'evidence_records': len(evidence),
            'corrections_applied': all('verification/verify-taskdesk/features/' + name in changed for name in ['complete.md', 'archive.md']),
            'manual_review_required': True,
        })
        result['automated_pass'] = result['scope_ok'] and result['product_unchanged'] and result['live_complete'] and result['scratch_clean'] and result['corrections_applied']
    else:
        result.update({'scope_ok': not changed, 'automated_pass': not changed, 'manual_review_required': True})
    return result


def run_trial(output, snapshot, case, variant, repetition, ordinal, args, config):
    name = f'trial-{ordinal:02d}'
    directory = output / 'trials' / name
    workspace = directory / 'workspace'
    workspace.mkdir(parents=True)
    build(workspace, case)
    base_digest = inventory(workspace)
    for path in snapshot.iterdir():
        if path.is_dir():
            shutil.copytree(path, workspace / '.agents/skills' / path.name, dirs_exist_ok=True)
    before = inventory(workspace)
    subprocess.run(['git', 'init', '-q', str(workspace)], check=True)
    subprocess.run(['git', '-C', str(workspace), 'add', '.'], check=True)
    subprocess.run(['git', '-C', str(workspace), '-c', 'user.name=Skill Eval', '-c', 'user.email=eval@example.invalid', 'commit', '-qm', 'Frozen fixture'], check=True)
    home = directory / 'runtime'
    home.mkdir()
    actual_home = Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex')))
    for filename in ['auth.json', 'models_cache.json']:
        if (actual_home / filename).exists():
            (home / filename).symlink_to(actual_home / filename)
    (home / 'config.toml').write_text(config)
    skill = CASES[case]['skill']
    prompt = f'Use ${skill} at .agents/skills/{skill}/SKILL.md to complete this request.\n\n{CASES[case]["request"]}\n'
    (directory / 'prompt.txt').write_text(prompt)
    command = ['codex', '--no-daemon', '-a', 'never', 'exec', '--json', '--sandbox', 'workspace-write', '-C', str(workspace), '-o', str(directory / 'answer.md'), '-']
    environment = os.environ.copy()
    environment['CODEX_HOME'] = str(home)
    start = time.monotonic()
    print(json.dumps({'event': 'start', 'trial': name, 'case': case, 'variant': variant, 'repetition': repetition}), flush=True)
    with (directory / 'events.jsonl').open('w') as events, (directory / 'stderr.txt').open('w') as errors:
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=events, stderr=errors, env=environment, text=True, start_new_session=True)
        (directory / 'process.json').write_text(json.dumps({'pid': process.pid, 'started': time.time()}))
        timed_out = False
        try:
            process.communicate(prompt, timeout=args.timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
    elapsed = time.monotonic() - start
    result = {'trial': name, 'case': case, 'variant': variant, 'repetition': repetition, 'elapsed_seconds': elapsed, 'exit_code': process.returncode, 'timed_out': timed_out, 'fixture_hashes': base_digest, **metrics(home)}
    result['outcomes'] = outcomes(directory, case, before)
    # Authentication is only linked while the run needs it; never copy credentials to artifacts.
    for filename in ['auth.json', 'models_cache.json']:
        (home / filename).unlink(missing_ok=True)
    (directory / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'event': 'finish', 'trial': name, 'case': case, 'variant': variant, 'seconds': round(elapsed, 2), 'exit_code': process.returncode, 'timed_out': timed_out, 'automated_pass': result['outcomes']['automated_pass'], 'sessions': result['session_count'], 'tokens': (result['usage_sum'] or {}).get('total_tokens'), 'tools': result['tools']}), flush=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--baseline', default='HEAD')
    parser.add_argument('--repeats', type=int, default=2)
    parser.add_argument('--timeout', type=int, default=300)
    parser.add_argument('--case', choices=CASES, action='append')
    args = parser.parse_args()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    old = output / 'snapshots/before'
    new = output / 'snapshots/updated'
    old.mkdir(parents=True)
    new.mkdir()
    revision = subprocess.check_output(['git', '-C', str(REPO), 'rev-parse', args.baseline], text=True).strip()
    files = subprocess.check_output(['git', '-C', str(REPO), 'ls-tree', '-r', '--name-only', revision, 'skills'], text=True).splitlines()
    for filename in files:
        destination = old / Path(filename).relative_to('skills')
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(subprocess.check_output(['git', '-C', str(REPO), 'show', f'{revision}:{filename}']))
    shutil.copytree(REPO / 'skills', new, dirs_exist_ok=True)
    config = '''model = "gpt-6.1-sol"
model_reasoning_effort = "xhigh"
suppress_unstable_features_warning = true
[features]
apps = false
plugins = false
memories = false
multi_agent = true
skip_host_skill_discovery = true
[skills.bundled]
enabled = false
[agents]
enabled = true
max_concurrent_threads_per_session = 3
max_depth = 1
default_subagent_model = "gpt-6.1-sol"
default_subagent_reasoning_effort = "xhigh"
'''
    cases = args.case or list(CASES)
    manifest = {'started_utc': datetime.now(timezone.utc).isoformat(), 'baseline_revision': revision, 'cli_version': subprocess.check_output(['codex', '--version'], text=True).strip(), 'config': config, 'repeats': args.repeats, 'timeout_seconds': args.timeout, 'concurrent_trials': 1, 'cases': {name: CASES[name] for name in cases}, 'skill_hashes': {'before': inventory(old), 'updated': inventory(new)}, 'harness_hashes': inventory(Path(__file__).parent), 'decision_rule': 'Retain the revised default if meaningful output quality and scope do not regress; report latency and usage separately. Do not infer a universal speedup from a small selected sample. Make only follow-up edits supported by observed failures or ambiguous instructions.'}
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    results = []
    for repetition in range(1, args.repeats + 1):
        for index, case in enumerate(cases):
            variants = ['before', 'updated'] if (repetition + index) % 2 else ['updated', 'before']
            for variant in variants:
                result = run_trial(output, {'before': old, 'updated': new}[variant], case, variant, repetition, len(results) + 1, args, config)
                results.append(result)
                (output / 'results.json').write_text(json.dumps(results, indent=2) + '\n')
    print(json.dumps({'event': 'complete', 'trials': len(results), 'output': str(output)}), flush=True)


if __name__ == '__main__':
    main()
