"""Behavioral checks kept outside each agent workspace until its run ends."""

import csv
import importlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


def checks(root, case):
    sys.path.insert(0, str(root))

    class Transfer(unittest.TestCase):
        def setUp(self):
            self.scratch = tempfile.TemporaryDirectory()
            self.addCleanup(self.scratch.cleanup)
            self.path = str(Path(self.scratch.name) / 'db.sqlite')
            self.ledger = importlib.import_module('ledger').Ledger(self.path)
            self.addCleanup(lambda: self.ledger.close())
            self.ledger.add_account('a', 100)
            self.ledger.add_account('b', 20)
            self.ledger.add_account('c', 0)

        def balances(self):
            return tuple(self.ledger.balance(n) for n in ['a', 'b', 'c'])

        def test_replay_after_reopen(self):
            first = self.ledger.transfer('a', 'b', 30, request_key='req-1')
            self.ledger.close()
            self.ledger = importlib.import_module('ledger').Ledger(self.path)
            self.assertEqual(self.ledger.transfer('a', 'b', 30, request_key='req-1'), first)
            self.assertEqual(self.balances(), (70, 50, 0))

        def test_conflicts_have_no_effect(self):
            self.ledger.transfer('a', 'b', 10, request_key='x')
            for arguments in [('a', 'b', 11), ('a', 'c', 10), ('b', 'a', 10)]:
                with self.assertRaises(ValueError):
                    self.ledger.transfer(*arguments, request_key='x')
            self.assertEqual(self.balances(), (90, 30, 0))

        def test_failure_does_not_claim_key(self):
            with self.assertRaises(ValueError):
                self.ledger.transfer('c', 'b', 10, request_key='later')
            self.ledger.transfer('a', 'c', 10)
            self.ledger.transfer('c', 'b', 10, request_key='later')
            self.assertEqual(self.balances(), (90, 30, 0))

        def test_unknown_destination_rolls_back(self):
            with self.assertRaises(ValueError):
                self.ledger.transfer('a', 'missing', 10, request_key='q')
            self.assertEqual(self.balances(), (100, 20, 0))
            self.ledger.transfer('a', 'b', 10, request_key='q')
            self.assertEqual(self.balances(), (90, 30, 0))

        def test_legacy_transfers_are_independent(self):
            self.assertNotEqual(self.ledger.transfer('a', 'b', 10), self.ledger.transfer('a', 'b', 10))
            self.assertEqual(self.balances(), (80, 40, 0))

        def test_invalid_inputs_have_no_effect(self):
            for amount in [0, -1, True, 1.1, '1']:
                with self.assertRaises(ValueError):
                    self.ledger.transfer('a', 'b', amount, request_key='bad')
            with self.assertRaises(ValueError):
                self.ledger.transfer('a', 'a', 1, request_key='self')
            with self.assertRaises(ValueError):
                self.ledger.transfer('a', 'b', 1, request_key='')
            self.assertEqual(self.balances(), (100, 20, 0))

        def test_cli_replay(self):
            command = [sys.executable, '-m', 'ledger', '--db', self.path, 'transfer', 'a', 'b', '7', '--request-key', 'cli']
            one = subprocess.run(command, cwd=root, capture_output=True, text=True, timeout=10)
            two = subprocess.run(command, cwd=root, capture_output=True, text=True, timeout=10)
            self.assertEqual((one.returncode, two.returncode), (0, 0), one.stderr + two.stderr)
            self.assertEqual(one.stdout, two.stdout)
            self.assertEqual(self.balances(), (93, 27, 0))

    class Utilities(unittest.TestCase):
        def test_duration_valid(self):
            parse = importlib.import_module('utilities.duration').parse_duration
            for source, expected in [('0s', 0), ('2h15m', 8100), ('45s', 45), ('1h0m4s', 3604), ('999m', 59940)]:
                self.assertEqual(parse(source), expected)

        def test_duration_invalid(self):
            parse = importlib.import_module('utilities.duration').parse_duration
            for source in ['', ' ', '1m2h', '1s1s', '1h2h', '-1s', '+1s', '1.5h', '1h ', ' 1h', '1H', '1', '1hfoo', '١s', 3, None]:
                with self.subTest(source=source), self.assertRaises(ValueError):
                    parse(source)

        def test_redaction_nested(self):
            redact = importlib.import_module('utilities.redaction').redact
            source = {'Token': {'nested': 'secret'}, 'rows': [{'TOKEN': 'x', 'name': 'A'}, ['x', {'token': 'z'}]], 'token_suffix': 'keep'}
            before = json.loads(json.dumps(source))
            result = redact(source, iter(['token']))
            self.assertEqual(result, {'Token': '[REDACTED]', 'rows': [{'TOKEN': '[REDACTED]', 'name': 'A'}, ['x', {'token': '[REDACTED]'}]], 'token_suffix': 'keep'})
            self.assertEqual(source, before)

        def test_redaction_new_containers(self):
            redact = importlib.import_module('utilities.redaction').redact
            source = {'rows': [{'x': 3}], 'ok': None}
            result = redact(source, [])
            result['rows'][0]['x'] = 4
            self.assertEqual(source['rows'][0]['x'], 3)
            self.assertEqual(redact(5, ['x']), 5)

        def test_csv_roundtrip_and_formula_protection(self):
            export = importlib.import_module('utilities.tabular').export_csv
            rows = [{'name': 'A, B', 'formula': '  =2+3', 'amount': -5}, {'name': 'quoted "line"\nnext', 'formula': '@SUM(A1)', 'amount': None}]
            before = json.loads(json.dumps(rows))
            result = export(iter(rows), ['name', 'formula', 'amount', 'missing'])
            self.assertEqual(list(csv.reader(io.StringIO(result))), [['name', 'formula', 'amount', 'missing'], ['A, B', "'  =2+3", '-5', ''], ['quoted "line"\nnext', "'@SUM(A1)", '', '']])
            self.assertEqual(rows, before)
            self.assertNotIn('\r', result)

        def test_csv_empty_and_headers(self):
            export = importlib.import_module('utilities.tabular').export_csv
            self.assertEqual(export(iter([]), ['=header', 'x']), "'=header,x\n")
            self.assertEqual(list(csv.reader(io.StringIO(export([{'x': '\t-1'}], ['x'])))), [['x'], ["'\t-1"]])

    suite = unittest.defaultTestLoader.loadTestsFromTestCase({'transfer': Transfer, 'utilities': Utilities}[case])
    stream = io.StringIO()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    return {'passed': result.wasSuccessful(), 'tests': result.testsRun, 'failures': len(result.failures), 'errors': len(result.errors), 'log': stream.getvalue()}


if __name__ == '__main__':
    print(json.dumps(checks(Path(sys.argv[1]), sys.argv[2]), indent=2))
