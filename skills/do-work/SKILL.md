---
name: do-work
description: Implement settled intent or a coordination plan through small working slices, continuous integration, and risk-matched verification.
disable-model-invocation: true
---

# Do Work

Implement settled intent through the smallest useful working slices. Act as coordinator and final integrator when real parallel streams exist; keep architectural judgment, shared interfaces, and final verification centralized.

Continue until the full requested scope and required checks are complete, or a concrete blocker prevents dependent work. Complete independent authorized work before reporting a blocker. Do not stop after the first slice or ask again for permission already supplied by the request or settled conversation. Existing authorization does not cover extra scope or external actions.

Use the current workspace. Create a branch or worktree only when the user requests that isolation.

## Implementation Standard

- Write for the next maintainer: explicit names, straightforward control flow, and one level of abstraction at a time.
- Minimize conceptual complexity before line count.
- Introduce abstractions when they remove proven complexity or extend an established local pattern.
- Let verification effort follow behavioral risk and regression cost.

## Workflow

1. Establish the implementation ledger.

   Read the user's request, settled chat context, or coordination plan. Track the goal, non-goals, acceptance signals, and every intended outcome. Show a ledger only when it helps the user assess scope or make a decision. Ask only for unresolved material product decisions; a separate `$shape-work` invocation is optional.

   Add a plan only when implementation reveals real parallel coordination, migration order, shared-interface ownership, a costly commitment, or a cross-session handoff. Do not require a separate `$plan-work` invocation to continue authorized work.

2. Inspect the repo.

   Read relevant canon, existing patterns, tests, package commands, and affected modules. Identify pre-existing user changes that overlap the work. Inspect existing coverage before adding tests; add tests only for meaningful gaps or required behavior.

   When the work changes a user-facing surface, look for an existing project-local `verify-*` skill in the repository's skill root. If it covers the surface, read its applicable feature files and add those user paths to the verification work. Do not create or maintain a verifier inside `$do-work`.

3. Build the first evidence-producing slice.

   Choose the smallest end-to-end slice that can run, render, or otherwise expose real behavior. When technical feasibility remains uncertain, use a disposable probe or narrow harness before committing production structure. Apply what the result teaches, and do not let throwaway structure enter the product without review. For a purely mechanical change where slicing adds no signal, use the smallest coherent batch instead.

4. Assign implementation streams.

   Create streams only where independence improves delivery. Give each stream one owner, narrow context, expected outputs, likely files, and verification. Delegate independent modules, separate research, isolated test work, stable frontend/backend slices, and reviewable mechanical changes when worker agents are available. Keep overlapping files, shared interfaces, migrations, architecture boundaries, and design-sensitive changes with the coordinator.

5. Integrate and verify continuously.

   Implement coordinator-owned work and review each delegated result before relying on it. After each meaningful slice, run the closest relevant check and use the result to refine the next slice. Reconcile interfaces, behavior, style, naming, and abstractions as streams land.

6. Verify the integrated behavior.

   Check changed integration boundaries and use the highest-signal end-to-end path appropriate to the change. Reuse passing results from this run when they cover the final code and relevant environment. When a matching project-local verifier exists, run its doctor check and the feature recipes affected by the change unless valid results already cover them. Follow its isolation, evidence, and cleanup rules. Do not run unrelated mapped features.

   Complete required checks. Once relevant checks pass, stop verification. Repeat checks only when changes to code, dependencies, or the environment invalidate their results, or a failure or unresolved concern justifies another run. Expand coverage only for an uncovered risk, failure, or explicit requirement.

   Treat this verifier use as part of `$do-work`; it does not start `$create-verification-skill` or `$maintain-verification-skill`. When a check is unavailable or disproportionately expensive, run the best substitute and explain the gap.

7. Clean up.

   Remove temporary instrumentation and artifacts created during this run. Leave pre-existing plans and documentation cleanup to the user; recommend `$canonize` when durable facts should enter `docs/canon/`.

8. Report.

   For a small change, report the result, verification, and any unresolved issue in a short paragraph. For larger work, add the scope and file details needed to assess completion. Always disclose user-deferred or blocked outcomes and material verification gaps or residual risk. Omit empty categories and do not reproduce the ledger by default.

## Completion

- Every requested outcome is implemented, explicitly user-deferred, or blocked with evidence. Complete independent authorized work before reporting a blocker.
- Required checks cover the final code and changed integration boundaries. Disclose any unavailable check or remaining risk.
- The diff contains intentional implementation, tests, and authorized documentation changes. Remove temporary artifacts and report the result concisely.
