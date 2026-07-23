---
name: do-work
description: Implement settled intent or a coordination plan through small working slices, continuous integration, and risk-matched verification.
---

# Do Work

Implement settled intent through the smallest useful working slices. Act as coordinator and final integrator when real parallel streams exist; keep architectural judgment, shared interfaces, and final verification centralized.

Use the current workspace. Create a branch or worktree only when the user requests that isolation.

## Implementation Standard

- Write for the next maintainer: explicit names, straightforward control flow, and one level of abstraction at a time.
- Minimize conceptual complexity before line count.
- Introduce abstractions when they remove proven complexity or extend an established local pattern.
- Let verification effort follow behavioral risk and regression cost.

## Workflow

1. Establish the implementation ledger.

   Read the user's request, settled chat context, or coordination plan. Record the goal, non-goals, acceptance signals, and every intended outcome. Route unresolved user-owned product decisions to `$shape-work`.

   Do not return to `$plan-work` merely because execution structure was not written in advance. Use it only when implementation reveals real parallel coordination, migration order, shared-interface ownership, a costly commitment, or a cross-session handoff.

   Completion criterion: every intended outcome is represented in the ledger, and no material product or design decision is being guessed.

2. Inspect the repo.

   Read relevant canon, existing patterns, tests, package commands, and affected modules. Identify pre-existing user changes that overlap the work.

   Completion criterion: each intended outcome has a grounded implementation location, a verification path, and a safe relationship to existing changes.

3. Build the first evidence-producing slice.

   Choose the smallest end-to-end slice that can run, render, or otherwise expose real behavior. When technical feasibility remains uncertain, use a disposable probe or narrow harness before committing production structure. Apply what the result teaches, and do not let throwaway structure enter the product without review. For a purely mechanical change where slicing adds no signal, use the smallest coherent batch instead.

   Completion criterion: the first slice or probe produces observable evidence about behavior, integration, or feasibility and informs the remaining implementation.

4. Assign implementation streams.

   Create streams only where independence improves delivery. Give each stream one owner, narrow context, expected outputs, likely files, and verification. Delegate independent modules, separate research, isolated test work, stable frontend/backend slices, and reviewable mechanical changes when worker agents are available. Keep overlapping files, shared interfaces, migrations, architecture boundaries, and design-sensitive changes with the coordinator.

   Completion criterion: every ledger item has one owner; delegated streams are independent; integration-sensitive decisions have one coordinating owner.

5. Integrate and verify continuously.

   Implement coordinator-owned work and review each delegated result before relying on it. After each meaningful slice, run the closest relevant check and use the result to refine the next slice. Reconcile interfaces, behavior, style, naming, and abstractions as streams land.

   Completion criterion: every ledger item is implemented, explicitly user-deferred, or blocked with evidence; each meaningful slice has a passing signal or an explicit verification gap; the combined change reads as one coherent implementation.

6. Verify the integrated behavior.

   Run broader checks at integration boundaries and the highest-signal end-to-end path available. When a check is unavailable or disproportionately expensive, run the best substitute and explain the gap.

   Completion criterion: every changed behavior has a passing check or an explicit verification gap, and integration checks cover every changed shared boundary.

7. Clean up.

   Remove temporary instrumentation and artifacts created during this run. Leave pre-existing plans and documentation cleanup to the user; recommend `$canonize` when durable facts should enter `docs/canon/`.

   Completion criterion: the final diff contains only intentional implementation, tests, and authorized documentation changes.

8. Report.

   Summarize completed outcomes, user-deferred or blocked work, files changed, checks run, verification gaps, and residual risk.

   Completion criterion: the user can account for every intended outcome and judge the implementation's remaining risk.
