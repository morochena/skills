---
name: plan-work
description: Plan durable coordination for parallel work, shared interfaces, migrations, costly commitments, or cross-session handoff from established evidence.
---

# Plan Work

Coordinate settled work that has real blocking edges, shared ownership, migration order, costly commitments, or handoff needs.

A large change alone does not require a plan. When intent is settled and the work is reversible, locally discoverable, and incrementally verifiable, recommend `$do-work` instead.

## Workflow

1. Confirm planning is warranted and choose the artifact.

   Identify the coordination state that must survive: parallel lanes, shared interfaces, migration order, costly or irreversible choices, or cross-session handoff. If none exists, stop and recommend `$do-work`.

   Keep the plan in chat when it will remain available for the execution window. Write `docs/plans/<slug>.md` only when durable coordination requires a file, using:

   ```md
   ---
   status: temporary
   owner: plan-work
   created: YYYY-MM-DD
   cleanup: absorb-with-canonize
   ---
   ```

   Completion criterion: the plan exists because coordination must persist, and it lives in the smallest artifact that can preserve that state.

2. Establish evidence.

   Read relevant canon, current code, tests, prior shaping results, prototypes, logs, traces, and other observed artifacts. Route unresolved user-owned decisions to `$shape-work`. Run the cheapest non-destructive check or disposable probe when a technical assumption could materially change the plan.

   Record:

   - `Evidence Established`: observed facts and artifact results the plan may rely on.
   - `Unproven Assumptions`: remaining claims that could change execution, with the cheapest useful discriminator.

   Completion criterion: the plan distinguishes observed behavior from inference and contains no cheaply testable assumption masquerading as fact.

3. Establish the scope ledger.

   State the goal, constraints, non-goals, and every intended outcome. Record user-chosen deferrals explicitly in a `Full-Scope Check`.

   Completion criterion: every requested outcome is in scope, a named non-goal, or an explicit user deferral.

4. Design work streams.

   Identify independent streams only where independence is real. For each stream, list likely files or modules, required context, expected outputs, and verification. Keep sequential work on the critical path instead of forcing parallel lanes.

   Completion criterion: every scope item belongs to a stream or the critical path, and each independent stream can run from the context and outputs stated in the plan.

5. Map the critical path.

   Identify decisions, shared interfaces, migrations, generated types, design dependencies, and stream outputs that block later work. Separate immediately runnable lanes from dependent lanes.

   Completion criterion: every dependency has a prerequisite, downstream consumer, and point at which it becomes unblocked.

6. Assign integration ownership.

   Give one coordinator ownership of shared interfaces, overlapping files, migrations, architecture-sensitive choices, and final integration. Use the current workspace; propose branches or worktrees only when the user requests isolation or likely conflicts justify asking.

   Completion criterion: every integration point has one owner, and no streams have incompatible authority over the same boundary.

7. Prove traceability.

   Cross-check the scope ledger against streams, blocking edges, integration points, and verification.

   Completion criterion: every scope item maps to one implementation stream or critical-path step and one verification method; every blocking edge and shared boundary appears in the execution order.

## Output Format

Use the applicable sections from this format; omit empty ceremony:

```md
# <Plan Name>

## Goal

## Scope

## Non-Goals

## Evidence Established

## Unproven Assumptions

## Canon To Read

## Work Streams

## Blocking Edges

## Integration Points

## Verification Strategy

## Full-Scope Check

## Coordinator Notes
```

The plan is complete when another agent can distinguish evidence from assumptions, account for the entire scope, start every unblocked stream, recognize every dependency, integrate through one owner, and verify each outcome without rediscovering intent.
