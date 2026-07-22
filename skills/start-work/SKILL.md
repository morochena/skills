---
name: start-work
description: Choose the right personal workflow for engineering or product work. Use when the user explicitly invokes $start-work, asks how to approach a task, starts fuzzy work, wants to decide whether to shape/plan/debug/review/implement/audit architecture, or wants guidance on parallelization, documentation, verification, or worktree ceremony before acting.
---

# Start Work

## Overview

Pick the smallest workflow that will handle the work well. Prefer direct action for clear tasks, shaping for fuzzy decisions, planning for coordination, debugging for broken behavior, review for change quality, and architecture improvement for repository-wide structural consistency.

This skill is a router, not an orchestrator. Recommend the next move and optionally start the first question, but do not silently invoke a larger process unless the user asks.

## Operating Taste

- Optimize for code as communication.
- Minimize complexity and cognitive load.
- Prefer explicit names and boring control flow over clever abstractions.
- Repeat code when deduplication would make the system harder to understand.
- Treat tests as a confidence tool, not a ritual.
- Avoid turning ordinary work into process artifacts.

## Classification

Classify the task into one of these buckets:

- `trivial`: Requirements are clear and the change is small. Recommend direct execution.
- `small`: Requirements are mostly clear, but a short plan or assumption check helps. Recommend a brief plan in chat, then execution.
- `medium`: The work has design choices, domain language, or several files. Recommend `$shape-work` if the idea is fuzzy, otherwise `$plan-work`.
- `large`: The work spans multiple areas, has blocking edges, or benefits from parallel lanes. Recommend `$shape-work` then `$plan-work`; write a temporary plan only when needed.
- `debug`: Something is broken, slow, flaky, or surprising. Recommend `$debug-work`.
- `review`: The user wants critique or a quality pass. Recommend `$review-work`.
- `architecture`: The user wants the repository's architecture documented, audited, or made more consistent. Recommend `$improve-architecture`.

## Decision Rules

Use facts from the repo instead of asking the user. Ask only for decisions, priorities, constraints, or missing intent.

Use `docs/canon/` when broad work depends on domain language, product rules, architecture, or engineering conventions. Read canon in this order when present:

1. `docs/canon/language.md`
2. `docs/canon/product.md`
3. `docs/canon/trajectory.md`
4. `docs/canon/system.md`
5. `docs/canon/engineering.md`

Recommend `docs/plans/<slug>.md` only for large work whose plan needs to survive the chat. Plans are temporary planning sediment and should later be absorbed or removed by `$canonize`.

Use the current workspace by default. Recommend branches or worktrees only when the user explicitly asks, or when likely file conflicts make isolation worth asking about.

## Output Format

Respond with:

```md
## Recommendation
<one clear workflow recommendation>

## Why
<short reasoning>

## Next Step
<the next skill or direct action>

## Notes
<parallelism, canon/docs, verification, or worktree considerations>
```

For obvious trivial work, keep the response brief and move directly into execution if the user asked for action.
