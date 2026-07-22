---
name: plan-work
description: Plan implementation as parallel lanes, critical paths, integration points, and verifiable scope.
---

# Plan Work

Turn settled intent into an executable plan for one coordinating agent session and independent worker streams where supported.

Default to chat-only plans for small and medium work. For large work, write a temporary plan to `docs/plans/<slug>.md` so it can survive the chat and later be absorbed or removed by `$canonize`.

## Workflow

1. Read context.

   Read relevant canon, the current code shape, and prior shaping notes. Route unresolved product or design decisions to `$shape-work` before planning implementation.

   Completion criterion: the outcome, material constraints, and remaining user decisions are known; implementation can proceed without inventing product intent.

2. Establish the scope ledger.

   State the goal, constraints, non-goals, and every intended outcome. Record user-chosen deferrals explicitly in a `Full-Scope Check`.

   Completion criterion: every requested outcome is in scope, a named non-goal, or an explicit user deferral.

3. Design parallel lanes.

   Decompose the ledger into independent streams. For each stream, list likely files or modules, required context, expected outputs, and verification.

   Completion criterion: every scope item belongs to one stream, and each stream can be executed from the context and outputs stated in the plan.

4. Map the critical path.

   Identify decisions, shared interfaces, migrations, generated types, design dependencies, and stream outputs that block later work. Separate immediately runnable lanes from dependent lanes.

   Completion criterion: every dependency has a prerequisite, downstream consumer, and point at which it becomes unblocked.

5. Assign integration ownership.

   Give one coordinator ownership of shared interfaces, overlapping files, migrations, architecture-sensitive choices, and final integration. Use the current workspace; propose branches or worktrees only when the user requests isolation or likely conflicts justify asking.

   Completion criterion: every integration point has one owner, and no streams have incompatible authority over the same boundary.

6. Prove traceability.

   Cross-check the scope ledger against streams, blocking edges, integration points, and verification.

   Completion criterion: every scope item maps to one implementation stream and one verification method; every blocking edge and shared boundary appears in the execution order.

7. Choose artifact size.

   Keep the plan in chat for small/medium work. For large work, create `docs/plans/<slug>.md` with this frontmatter:

   ```md
   ---
   status: temporary
   owner: plan-work
   created: YYYY-MM-DD
   cleanup: absorb-with-canonize
   ---
   ```

   Completion criterion: the plan lives in the smallest artifact that will remain available for the expected execution window.

## Output Format

Use the applicable sections from this format; omit empty ceremony:

```md
# <Plan Name>

## Goal

## Scope

## Non-Goals

## Canon To Read

## Parallel Work Streams

## Blocking Edges

## Integration Points

## Verification Strategy

## Full-Scope Check

## Coordinator Notes
```

The plan is complete when another agent can account for the entire scope, start every unblocked lane, recognize every dependency, integrate through one owner, and verify each outcome without rediscovering intent.
