---
name: do-work
description: Coordinate, integrate, and verify implementation from a settled plan.
---

# Do Work

Act as coordinator and final integrator. Delegate independent streams when useful and allowed; keep architectural judgment, shared interfaces, and final verification centralized.

Use the current workspace. Create a branch or worktree only when the user requests that isolation.

## Implementation Standard

- Write for the next maintainer: explicit names, straightforward control flow, and one level of abstraction at a time.
- Minimize conceptual complexity before line count.
- Introduce abstractions when they remove proven complexity or extend an established local pattern.
- Let verification effort follow behavioral risk and regression cost.

## Workflow

1. Establish the implementation ledger.

   Read the user's plan, `docs/plans/<slug>.md`, or the settled chat context. Record the goal, non-goals, acceptance signals, and every plan item. Route unresolved product decisions to `$shape-work` and missing execution structure to `$plan-work` before implementation.

   Completion criterion: every intended outcome is represented in the ledger, and no material product or design decision is being guessed.

2. Inspect the repo.

   Read relevant canon, existing patterns, tests, package commands, and affected modules. Identify pre-existing user changes that overlap the work.

   Completion criterion: each plan item has a grounded implementation location, a verification path, and a safe relationship to existing changes.

3. Assign implementation streams.

   Give each stream one owner, narrow context, expected outputs, likely files, and verification. Delegate independent modules, separate research, isolated test work, stable frontend/backend slices, and reviewable mechanical changes when worker agents are available. Keep overlapping files, shared interfaces, migrations, architecture boundaries, and design-sensitive changes with the coordinator.

   Completion criterion: every ledger item has one owner; delegated streams are independent; integration-sensitive decisions have one coordinating owner.

4. Integrate continuously.

   Implement coordinator-owned work and review each delegated result before relying on it. Reconcile interfaces, behavior, style, naming, and abstractions as streams land.

   Completion criterion: every ledger item is implemented, explicitly user-deferred, or blocked with evidence; the combined change reads as one coherent implementation.

5. Verify behavior.

   Run the closest relevant checks for each changed behavior and broader checks at integration boundaries. When a check is unavailable or disproportionately expensive, run the highest-signal substitute and explain the gap.

   Completion criterion: every changed behavior has a passing check or an explicit verification gap; integration checks cover every changed shared boundary.

6. Clean up.

   Remove temporary instrumentation and artifacts created during this run. Leave pre-existing plans and documentation cleanup to the user; recommend `$canonize` when durable facts should enter `docs/canon/`.

   Completion criterion: the final diff contains only intentional implementation, tests, and authorized documentation changes.

7. Report.

   Summarize completed ledger items, user-deferred or blocked work, files changed, checks run, verification gaps, and residual risk.

   Completion criterion: the user can account for every original plan item and judge the implementation's remaining risk.
