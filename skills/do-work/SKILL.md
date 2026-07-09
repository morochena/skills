---
name: do-work
description: Implement planned engineering work with one agent session coordinating worker agents where useful and available. Use when the user explicitly invokes $do-work, asks to execute a plan, wants parallel implementation in the current workspace, or wants implementation guided by simplicity, readability, pragmatic verification, and low ceremony.
---

# Do Work

## Overview

Execute the work with the main agent session acting as coordinator and final integrator. Use worker agents for independent streams when available, but keep architectural judgment, shared interfaces, and final verification centralized.

Use the current workspace by default. Do not create branches or worktrees unless the user explicitly asks.

## Engineering Taste

- Code is communication with future readers.
- Minimize complexity before minimizing lines.
- Prefer explicit names, straightforward control flow, and single-level methods.
- Extract abstractions only when they remove real complexity or match an existing local pattern.
- Repeat code when DRY would make the system leakier or harder to read.
- Add tests where risk, behavior, or regression cost justifies them. Do not perform TDD by default.

## Workflow

1. Load the plan.

   Read the user's plan, `docs/plans/<slug>.md`, or the chat context. If the work is fuzzy, stop and recommend `$shape-work` or `$plan-work`.

2. Inspect the repo.

   Read relevant canon, existing patterns, tests, package commands, and affected modules. Protect unrelated user changes.

3. Assign streams.

   If multi-agent tools are available, send independent streams to worker agents with narrow prompts, raw task context, expected outputs, and verification requirements. Keep overlapping files, shared interfaces, migrations, and design-sensitive changes in the main session.

   If worker agents are not available, execute the streams sequentially and say so.

4. Integrate continuously.

   Review each worker-agent result before relying on it. Normalize style, naming, and abstractions so the final implementation reads like one coherent change.

5. Verify pragmatically.

   Run targeted checks for each stream when cheap enough. Run broader checks at integration points and at the end. If full verification is slow, explain the tradeoff and run the highest-signal checks first.

6. Clean up.

   Remove temporary files and generated planning sediment unless the user asked to keep them. Recommend `$canonize` when durable facts should be absorbed into `docs/canon/`.

7. Report.

   Summarize what changed, which checks ran, what remains risky, and any follow-up that is genuinely useful.

## Sub-Agent Rules

Use worker agents to parallelize:

- Independent modules
- Research against local code
- Test updates for separate behavior
- UI and backend slices with a stable contract
- Mechanical changes that can be reviewed after

Do not outsource:

- Product decisions
- Architecture boundaries
- Shared public interfaces without coordinator review
- Conflict-prone edits in the same files
- Final integration or final verification
