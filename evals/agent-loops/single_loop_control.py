#!/usr/bin/env python3
"""Append an explicitly separated no-worker control to a completed comparison."""

import argparse
import json
from pathlib import Path

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
    assert len(results) == len(manifest['cases']) * manifest['repeats'] * 2, 'Finish the primary comparison first.'
    config = manifest['config'].replace('multi_agent = true', 'multi_agent = false').replace('[agents]\nenabled = true', '[agents]\nenabled = false')
    control_manifest = {
        'case': 'utilities', 'variant': 'updated_single_loop_control', 'repeats': args.repeats,
        'config': config, 'harness_hashes': inventory(Path(__file__).parent),
        'purpose': 'Check whether actual delegation on the independent utility task adds value. Use the frozen updated skill snapshot and the same task; disable worker tools only. These later, unpaired control runs have an order/cache confound and are not part of the primary before/updated comparison.',
    }
    path = output / 'control-manifest.json'
    assert not path.exists(), 'Control already exists; do not silently replace attempts.'
    path.write_text(json.dumps(control_manifest, indent=2) + '\n')
    for repetition in range(1, args.repeats + 1):
        result = run_trial(output, output / 'snapshots/updated', 'utilities', 'updated_single_loop_control', repetition, len(results) + 1, args, config)
        results.append(result)
        (output / 'results.json').write_text(json.dumps(results, indent=2) + '\n')


if __name__ == '__main__':
    main()
