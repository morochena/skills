# Agent loop comparison

Run the committed skills and the current working-tree skills on the same offline
tasks. Each trial has a fresh workspace and Codex home. Both variants can use
workers; the task does not force a delegation decision. The only varied input is
the skill package. No production application, user data, publication, or external
service is involved.

```sh
python3 evals/agent-loops/run.py --output /tmp/skills-loop-comparison --repeats 2
```

The output directory must not already exist. Use `--baseline REF` to select the
old skills, `--case transfer` to select a case, and `--timeout SECONDS` to bound
each attempt. Run from a machine with a working, signed-in `codex` CLI. The
runner pins the locally configured model used for the initial comparison:
`gpt-6.1-sol`, `xhigh`, with the same defaults for children. Review that choice
before reusing the harness on another account or model configuration.

To add the separate, later no-worker control for the utility task after the
primary comparison finishes:

```sh
python3 evals/agent-loops/single_loop_control.py /tmp/skills-loop-comparison
python3 evals/agent-loops/summarize.py /tmp/skills-loop-comparison
python3 evals/agent-loops/review_packet.py /tmp/skills-loop-comparison
```

The control uses the frozen updated snapshot with worker tools disabled. It is
unpaired and runs later, so retain the order and caching limitations. The review
packet omits variant identity, timing, usage, and skill instructions; keep its
mapping outside the reviewer's workspace.

The verifier fixture uses `verification/verify-taskdesk`, an explicitly configured
project-local root. The initial 2026-10-24 experiment used `.agents/skills`, which
the workspace-write sandbox protected from edits. Those four blocked attempts
remain in the evidence and are excluded from skill performance conclusions.
`writable_verifier.py OUTPUT` reruns both frozen versions twice in the corrected
fixture for that historical experiment. A fresh run already uses the writable
root and does not need this recovery cohort. The grader requires actual feature
file changes as well as live coverage; process exit alone is insufficient.

Trials run sequentially. Pair order alternates across tasks and reverses on the
second repetition. Each attempt records process wall time, exit status, timeout,
actual tool calls, child sessions, output, changes, and available session usage.
Limits allow three concurrent child threads and one level of delegation. This
CLI does not reproduce Ultra Magnus's shared model-request limit; conclusions
about that limit must come from its own experiment.

The cases are deliberately small examples, not a representative coding benchmark:

| Case | Skill | Work and quality evidence |
| --- | --- | --- |
| `transfer` | `do-work` | Retry safety across a SQLite store, service, and CLI. Hidden checks cover durable replay, conflicts, failed-request recovery, legacy behavior, validation, and CLI integration. |
| `utilities` | `do-work` | Three independent modules with stable contracts. Hidden checks cover parser validation, recursive redaction without mutation, and CSV behavior. |
| `verifier` | `maintain-verification-skill` | Correct a verifier against a real local CLI. Check source scope, live command evidence, corrected recipes, and scratch cleanup. |
| `measurement` | `benchmark-checklist` | Assess a supplied agent comparison against raw results and source. Review the answer for supported conclusions, failure accounting, usage limits, semantic findings, and citation accuracy. |

Requests and quality rubrics are frozen in `manifest.json` before execution.
Hidden behavioral checks stay outside the agent workspace until it finishes.
Verifier recipes and measurement reasoning also need artifact review; automated
checks alone are not a quality verdict. Review outputs without variant labels or
latency and usage measurements when practical.

The output retains both snapshots, all trials, prompts, event streams, final
answers, and results. Usage is the sum of the last reported cumulative counters
for each retained session. Preserve per-session values so aggregation can be
audited. Cached input is included in total input; do not add it again. Missing
usage remains unknown, and tokens are not invoiced cost. The runtime may omit
usage for a failed or interrupted attempt.
The last retained counter from an interrupted run can exclude its unfinished
model call; treat it as partial reported usage, not a complete attempt total.

Authentication is linked from the existing Codex home only while a trial runs;
it is never copied into the results. If interrupted, inspect the current trial's
`process.json` before stopping only that owned process group and removing its
runtime authentication links. Raw runtime logs can contain account metadata;
keep them local. Publish only a reviewed, sanitized summary and useful evidence.

Use the result to choose a default for these tasks and conditions. A small,
selected sample cannot establish a universal architecture winner, statistical
equivalence, a monetary saving, or performance on larger repositories. Keep
failures and regressions visible. Make further skill edits only when the
observed behavior supports them.
