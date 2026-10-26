"""Small, offline tasks with contracts and independently checked outcomes."""

import json
from pathlib import Path
import textwrap


def put(root, name, content):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).lstrip())


CASES = {
    "transfer": {
        "skill": "do-work",
        "request": """Fix retry safety in this local ledger. Keep the existing API compatible and add an optional request_key argument to Ledger.transfer and a --request-key CLI flag. A nonempty key identifies one transfer: repeating the same source, destination and positive integer amount returns the original transfer ID without moving money again, including after reopening the database. Reusing that key with different arguments raises ValueError without changing balances. Requests without a key remain independent transfers. Failed transfers must not reserve the key or partially update balances. Empty keys and transfers to the same account are invalid. Add appropriate regression coverage and finish the implementation and checks. Do not add dependencies or change unrelated behavior.""",
        "rubric": "All hidden behavioral checks pass, visible tests still pass, and the implementation completes within scope. No required delegation choice; record what actually occurred.",
    },
    "utilities": {
        "skill": "do-work",
        "request": """Complete the three independent utility modules according to CONTRACTS.md, preserving public signatures. These modules have stable contracts and no dependencies on one another. Add meaningful tests for the changed behavior and complete all checks. Do not add dependencies or change unrelated files. Use whatever execution arrangement is justified by the work.""",
        "rubric": "All hidden contract checks and existing tests pass. No required delegation choice; this is a counterexample workload where independent outputs could justify workers.",
    },
    "verifier": {
        "skill": "maintain-verification-skill",
        "request": """Audit and update verification/verify-taskdesk against this app. Check every mapped feature against source and through a real CLI session. Correct proven verifier drift, preserve run evidence under evidence/, clean up scratch state, and report any product gaps. The app is entirely local; no network or external access is needed. Do not change product code. Finish the verifier maintenance.""",
        "rubric": "Product files unchanged; every mapped feature exercised in the real CLI; complete/status drift corrected; archived tasks excluded from default list and included with --all; preserved parseable evidence; scratch state cleaned; reported outcome matches the artifacts. Check documented recipes and source citations manually.",
    },
    "measurement": {
        "skill": "benchmark-checklist",
        "request": """Use the supplied trial artifacts and source to assess the proposed default change in proposal.md. Give the supported performance and quality conclusions, any material flaws in the evidence, and the next release decision. This is a read-only assessment; do not run new model trials or change any files. Keep the answer useful for deciding what to ship.""",
        "rubric": "Bounded release decision; all failures retained; budget exhaustion identified as stopping cause; missing usage unknown; no monetary savings inferred from token totals; supplied finding distinguished from blind discovery; semantic agreement distinguished from fingerprint matching; concrete citation defect identified from source; no precision/recall or general architecture claim unsupported by the sample. Grade reasoning against raw evidence, not required wording.",
    },
}


def build(root, case):
    put(root, "AGENTS.md", """
        This is an isolated, offline example project. Work only in this workspace.
        Do not read sibling workspaces, the source skills repository, credentials,
        or evaluation harness files. Do not use network or external services.
        Use the supplied skill under .agents/skills/ for this request.
        Worker tools are available when the task and supplied skill justify them;
        at most three child threads may run, with one level of delegation.
        All configured agents use the same model and reasoning effort.
        Do not change those settings. Preserve files outside the requested scope.
        Python's standard library is sufficient. Run Python as python3.
    """)
    put(root, ".gitignore", "__pycache__/\n*.pyc\n.scratch/\n")
    if case == "transfer":
        transfer(root)
    elif case == "utilities":
        utilities(root)
    elif case == "verifier":
        verifier(root)
    elif case == "measurement":
        measurement(root)
    else:
        raise ValueError(case)


def transfer(root):
    put(root, "README.md", """
        # Local ledger
        Run checks: `python3 -m unittest discover -s tests -v`.
        Run CLI: `python3 -m ledger --db PATH transfer SOURCE DESTINATION AMOUNT`.
        Amounts are integer cents. SQLite is the durable source of balances and transfer IDs.
    """)
    put(root, "ledger/store.py", """
        import sqlite3

        def connect(path):
            db = sqlite3.connect(path)
            db.execute('CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY, balance INTEGER NOT NULL)')
            db.execute('CREATE TABLE IF NOT EXISTS transfers (id INTEGER PRIMARY KEY, source TEXT NOT NULL, destination TEXT NOT NULL, amount INTEGER NOT NULL)')
            db.commit()
            return db
    """)
    put(root, "ledger/__init__.py", """
        from .store import connect

        class Ledger:
            def __init__(self, path):
                self.db = connect(path)

            def close(self):
                self.db.close()

            def add_account(self, name, balance):
                with self.db:
                    self.db.execute('INSERT INTO accounts VALUES (?, ?)', (name, balance))

            def balance(self, name):
                row = self.db.execute('SELECT balance FROM accounts WHERE name = ?', (name,)).fetchone()
                if row is None:
                    raise ValueError('unknown account')
                return row[0]

            def transfer(self, source, destination, amount):
                if type(amount) is not int or amount <= 0:
                    raise ValueError('amount must be positive integer cents')
                with self.db:
                    if self.balance(source) < amount:
                        raise ValueError('insufficient funds')
                    self.balance(destination)
                    self.db.execute('UPDATE accounts SET balance = balance - ? WHERE name = ?', (amount, source))
                    self.db.execute('UPDATE accounts SET balance = balance + ? WHERE name = ?', (amount, destination))
                    row = self.db.execute('INSERT INTO transfers (source, destination, amount) VALUES (?, ?, ?)', (source, destination, amount))
                    return row.lastrowid
    """)
    put(root, "ledger/__main__.py", """
        import argparse
        from . import Ledger

        def main():
            parser = argparse.ArgumentParser()
            parser.add_argument('--db', required=True)
            commands = parser.add_subparsers(dest='command', required=True)
            transfer = commands.add_parser('transfer')
            transfer.add_argument('source')
            transfer.add_argument('destination')
            transfer.add_argument('amount', type=int)
            args = parser.parse_args()
            ledger = Ledger(args.db)
            try:
                print(ledger.transfer(args.source, args.destination, args.amount))
            finally:
                ledger.close()

        if __name__ == '__main__':
            main()
    """)
    put(root, "tests/test_ledger.py", """
        import unittest
        from ledger import Ledger

        class LedgerTest(unittest.TestCase):
            def setUp(self):
                self.ledger = Ledger(':memory:')
                self.addCleanup(self.ledger.close)
                self.ledger.add_account('a', 100)
                self.ledger.add_account('b', 20)

            def test_transfer(self):
                self.assertEqual(self.ledger.transfer('a', 'b', 30), 1)
                self.assertEqual((self.ledger.balance('a'), self.ledger.balance('b')), (70, 50))

            def test_insufficient(self):
                with self.assertRaises(ValueError):
                    self.ledger.transfer('b', 'a', 21)
                self.assertEqual(self.ledger.balance('b'), 20)
    """)


def utilities(root):
    put(root, "README.md", "Run checks: `python3 -m unittest discover -s tests -v`.\n")
    put(root, "CONTRACTS.md", """
        # Utility contracts
        Each module is independent and owns its own behavior. No shared abstraction is needed.

        `utilities.duration.parse_duration(text)` returns integer seconds for an ordered,
        non-repeated sequence of unsigned integer components followed by h, m, or s,
        e.g. 2h15m, 45s, 0s, 1h0m4s. Units must descend in h/m/s order.
        Reject empty strings, whitespace, signs, fractions, missing units, repeated or
        reordered units, trailing garbage, non-ASCII digits, and non-string inputs with
        ValueError. There is no fixed upper bound on a component's integer value.

        `utilities.redaction.redact(value, sensitive_keys)` recursively returns a new JSON-like
        dict/list tree with values under matching dict keys replaced by '[REDACTED]'.
        Key matching is case-insensitive and exact; values and other keys retain spelling.
        Lists are traversed. Scalars are unchanged. Never mutate input. Matching a key
        replaces its whole value, including containers. sensitive_keys is any iterable of strings.

        `utilities.tabular.export_csv(rows, columns)` returns CSV text using the columns' order,
        including a header and \n line endings. rows may be a one-shot iterable of dicts.
        Missing fields and None become empty cells; other scalars use str(value).
        Quote according to CSV rules. Prefix an apostrophe to string cells starting with
        =, +, -, or @, including after leading spaces/tabs. Numeric negatives remain numeric.
        Preserve existing leading characters when prefixing. The same rule applies to headers.
        Empty rows still produce the header. Do not alter caller data.
    """)
    put(root, "utilities/__init__.py", "")
    for module, function, args in [
        ("duration", "parse_duration", "text"),
        ("redaction", "redact", "value, sensitive_keys"),
        ("tabular", "export_csv", "rows, columns"),
    ]:
        put(root, f"utilities/{module}.py", f"def {function}({args}):\n    raise NotImplementedError\n")
    put(root, "tests/test_smoke.py", """
        import unittest
        from utilities.duration import parse_duration
        from utilities.redaction import redact
        from utilities.tabular import export_csv

        class Smoke(unittest.TestCase):
            def test_duration(self):
                self.assertEqual(parse_duration('1h2m3s'), 3723)

            def test_redaction(self):
                self.assertEqual(redact({'secret': 'x'}, ['secret']), {'secret': '[REDACTED]'})

            def test_csv(self):
                self.assertEqual(export_csv([{'name': 'A'}], ['name']), 'name\\nA\\n')
    """)


def verifier(root):
    with (root / "AGENTS.md").open("a") as instructions:
        instructions.write("\nProject-local verification skill root: verification/.\n")
    put(root, "README.md", "Taskdesk is a local Python CLI. Use `python3 app.py --help`. All state is explicit via --state.\n")
    put(root, "app.py", """
        import argparse
        import json
        from pathlib import Path

        def main():
            parser = argparse.ArgumentParser()
            parser.add_argument('--state', required=True)
            commands = parser.add_subparsers(dest='command', required=True)
            commands.add_parser('doctor')
            add = commands.add_parser('add')
            add.add_argument('title')
            listing = commands.add_parser('list')
            listing.add_argument('--all', action='store_true')
            complete = commands.add_parser('complete')
            complete.add_argument('id', type=int)
            archive = commands.add_parser('archive')
            archive.add_argument('id', type=int)
            commands.add_parser('status')
            args = parser.parse_args()
            path = Path(args.state)
            tasks = json.loads(path.read_text()) if path.exists() else []
            if args.command == 'doctor':
                result = {'ok': True, 'state': str(path)}
            elif args.command == 'add':
                result = {'id': max([t['id'] for t in tasks], default=0) + 1, 'title': args.title, 'done': False, 'archived': False}
                tasks.append(result)
            elif args.command == 'list':
                result = tasks if args.all else [t for t in tasks if not t['archived']]
            elif args.command in ('complete', 'archive'):
                matches = [t for t in tasks if t['id'] == args.id]
                if not matches:
                    parser.error('unknown task')
                result = matches[0]
                result['done' if args.command == 'complete' else 'archived'] = True
            else:
                result = {'open': sum(not t['done'] and not t['archived'] for t in tasks), 'completed': sum(t['done'] and not t['archived'] for t in tasks), 'archived': sum(t['archived'] for t in tasks)}
            path.parent.mkdir(parents=True, exist_ok=True)
            if args.command != 'doctor':
                path.write_text(json.dumps(tasks))
            # Retained output evidence is useful after scratch state cleanup.
            evidence = Path('evidence/cli.jsonl')
            evidence.parent.mkdir(parents=True, exist_ok=True)
            with evidence.open('a') as log:
                log.write(json.dumps({'command': args.command, 'result': result}) + '\\n')
            print(json.dumps(result, sort_keys=True))

        if __name__ == '__main__':
            main()
    """)
    put(root, "verification/verify-taskdesk/SKILL.md", """
        ---
        name: verify-taskdesk
        description: Control and verify the local Taskdesk CLI with isolated JSON state.
        ---
        # Verify Taskdesk
        Run from the project root with python3. Read features/README.md for mapped paths.
        Use `.scratch/tasks.json` for state; this is isolated from user data.
        Doctor: `python3 app.py --state .scratch/tasks.json doctor` before live control.
        Run the applicable commands and inspect their JSON outputs against expected behavior.
        Preserve evidence/cli.jsonl through cleanup. Delete only .scratch/tasks.json at teardown.
        No server or subprocess remains running between invocations. Python's stdlib is sufficient.
    """)
    put(root, "verification/verify-taskdesk/features/README.md", """
        # Features
        - [Create and list](create.md)
        - [Complete and count](complete.md)
        - [Archive and list](archive.md)
    """)
    put(root, "verification/verify-taskdesk/features/create.md", """
        # Create and list
        Source: app.py, add and list command branches.
        From an empty state, run `python3 app.py --state .scratch/tasks.json add 'Example'`.
        Then run `python3 app.py --state .scratch/tasks.json list`.
        The new task has a positive ID, done=false, archived=false, and appears in the list.
    """)
    put(root, "verification/verify-taskdesk/features/complete.md", """
        # Complete and count
        Source: app.py, command parser and task update branches.
        After creating a task, run `python3 app.py --state .scratch/tasks.json done 1`.
        Run `python3 app.py --state .scratch/tasks.json summary` to see open/done counts.
        The task is done and open count decreases. The summary reports its count under done.
    """)
    put(root, "verification/verify-taskdesk/features/archive.md", """
        # Archive and list
        Source: app.py, archive and list command branches.
        After creating a task, run `python3 app.py --state .scratch/tasks.json archive 1`.
        Run `python3 app.py --state .scratch/tasks.json list`.
        Archived tasks remain in the default list with archived=true.
    """)


def measurement(root):
    put(root, "proposal.md", """
        # Default proposal
        We compared optional worker delegation (elm) with one loop (fir) for delta code audits.
        The proposed release uses fir for this audit workflow. Can we claim it is faster,
        cheaper, equally accurate, and grounds for removing workers from all workflows?
        Review artifacts/manifest.json, trials.json, findings.json, and the cited source.
        Give a release recommendation supported by the evidence, including corrections needed
        in the proposed claims. This evaluation must not mutate application or source state.
    """)
    manifest = {
        "model": "same-model", "effort": "same-effort", "revision": "frozen-r7",
        "shared_request_limit": 120, "pair_order": [["elm", "fir"], ["fir", "elm"]],
        "tools_change": "fir omits task; ordinary tools unchanged",
        "prompt_change": "fir replaces delegation instruction with complete-in-loop instruction",
        "prior_findings_in_prompt": ["Archived tickets can be restored by an external callback."],
        "usage_scope": "Parent plus children; includes cached input; excludes auxiliary task-label model calls.",
    }
    trials = [
        {"id": "e1", "variant": "elm", "seconds": 260, "status": "failed", "turns": 120, "children": 6, "task_batches": 2, "tokens": None, "error": "maximum request count 120 exceeded", "secondary_error": "provider_stream aborted"},
        {"id": "f1", "variant": "fir", "seconds": 180, "status": "succeeded", "turns": 36, "children": 0, "tokens": 2100000},
        {"id": "f2", "variant": "fir", "seconds": 220, "status": "succeeded", "turns": 48, "children": 0, "tokens": 2700000},
        {"id": "e2", "variant": "elm", "seconds": 290, "status": "failed", "turns": 120, "children": 6, "task_batches": 2, "tokens": None, "error": "maximum request count 120 exceeded", "secondary_error": "provider_stream aborted"},
    ]
    findings = {
        "f1": [
            {"fingerprint": "callback-7", "claim": "Archived tickets can be restored by an external callback.", "verdict": "needs_validation", "citation": "source/callback.py:6"},
            {"fingerprint": "scope-22", "claim": "Search can return another tenant's tickets.", "verdict": "confirmed", "citation": "source/search.py:8"},
        ],
        "f2": [
            {"fingerprint": "callback-7", "claim": "Archived tickets can be restored by an external callback.", "verdict": "needs_validation", "citation": "source/callback.py:6"},
            {"fingerprint": "scope-88", "claim": "Ticket search does not constrain tenant ownership.", "verdict": "needs_validation", "citation": "source/search.py:4"},
        ],
        "historical_unpaired_elm": {"status": "succeeded", "seconds": 340, "children": 3, "tokens": 8100000, "revision": "older-r6"},
    }
    for name, value in [("manifest", manifest), ("trials", trials), ("findings", findings)]:
        put(root, f"artifacts/{name}.json", json.dumps(value, indent=2) + "\n")
    put(root, "source/search.py", """
        def search(db, tenant_id, text):
            if not text:
                return []
            return db.execute('SELECT * FROM tickets WHERE title LIKE ?', ('%' + text + '%',)).fetchall()


        def log_failure(logger, error):
            logger.warning('search failed: %s', error)
    """)
    put(root, "source/callback.py", """
        def apply_callback(db, event):
            if event.get('kind') != 'ticket_changed':
                return
            # Caller is responsible for verifying callback authority.
            ticket_id = event['id']
            db.execute('UPDATE tickets SET archived = 0 WHERE id = ?', (ticket_id,))
    """)
