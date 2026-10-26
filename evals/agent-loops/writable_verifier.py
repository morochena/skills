#!/usr/bin/env python3
"""Repeat verifier comparisons in a writable project-local verifier root."""

import argparse
import json
from pathlib import Path

from fixtures import CASES
from run import inventory, run_trial


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    parser.add_argument('--repeats', type=int, default=2)
    parser.add_argument('--timeout', type=int, default=300)
    args = parser.parse_args()
    output = args.output.resolve()
    manifest = json.loads((output / 'manifest.json').read_text())
    results = json.loads((output / 'results.json').read_text())
    path = output / 'writable-verifier-manifest.json'
    assert not path.exists(), 'Do not silently replace attempts.'
    path.write_text(json.dumps({
        'request': CASES['verifier']['request'], 'rubric': CASES['verifier']['rubric'],
        'config': manifest['config'], 'repeats': args.repeats,
        'harness_hashes': inventory(Path(__file__).parent),
        'correction': 'The initial .agents/skills target was protected by the sandbox. Keep all initial attempts as blocked/confounded. This cohort changes the explicit target and configured root to verification/verify-taskdesk for both skill versions; the app and sandbox stay the same. Review actual applied corrections, not just live checks or process exit.',
    }, indent=2) + '\n')
    for repetition in range(1, args.repeats + 1):
        variants = ['before', 'updated'] if repetition % 2 else ['updated', 'before']
        for variant in variants:
            result = run_trial(output, output / 'snapshots' / variant, 'verifier', variant + '_writable_verifier', repetition, len(results) + 1, args, manifest['config'])
            results.append(result)
            (output / 'results.json').write_text(json.dumps(results, indent=2) + '\n')


if __name__ == '__main__':
    main()
