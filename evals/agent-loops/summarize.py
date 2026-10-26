#!/usr/bin/env python3
"""Summarize measurements without treating automated checks as full review."""

import argparse
import json
from pathlib import Path
import statistics


def distribution(values):
    return {'count': len(values), 'median': statistics.median(values), 'minimum': min(values), 'maximum': max(values)} if values else None


def summarize(output):
    results = json.loads((output / 'results.json').read_text())
    notes_path = output / 'measurement-notes.json'
    notes = json.loads(notes_path.read_text()) if notes_path.exists() else []
    excluded = {trial for note in notes if note.get('type') == 'verifier_harness_confound' for trial in note['affected_trials']}
    groups = {}
    for result in results:
        group = groups.setdefault(result['case'], {}).setdefault(result['variant'], [])
        group.append(result)
    summary = {'trials': len(results), 'cases': {}, 'notes': [
        'Automated checks are not a complete quality verdict; verifier recipes and measurement reasoning need review.',
        'Report latency and usage separately from correctness. Missing usage is unknown, not zero.',
        'Session token totals include cached input and are not invoiced cost.',
        'This selected sample cannot establish statistical equivalence or a general architecture winner.',
    ]}
    for case, variants in groups.items():
        summary['cases'][case] = {}
        for variant, trials in variants.items():
            summary['cases'][case][variant] = {
                'attempts': len(trials),
                'process_completions': sum(t['exit_code'] == 0 and not t['timed_out'] for t in trials),
                'automated_passes': sum(t['outcomes']['automated_pass'] for t in trials),
                'wall_seconds_all_attempts': distribution([t['elapsed_seconds'] for t in trials]),
                'tokens_reported': distribution([t['usage_sum']['total_tokens'] for t in trials if t.get('usage_sum') and t['usage_sum'].get('total_tokens') is not None]),
                'missing_usage_attempts': sum(not t.get('usage_sum') for t in trials),
                'interrupted_usage_attempts': sum(t['timed_out'] or t['exit_code'] != 0 for t in trials),
                'child_sessions': [max(0, t['session_count'] - 1) for t in trials],
                'trials': [t['trial'] for t in trials],
                'excluded_from_performance_inferences': [t['trial'] for t in trials if t['trial'] in excluded],
            }
    return summary


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    print(json.dumps(summarize(args.output), indent=2))
