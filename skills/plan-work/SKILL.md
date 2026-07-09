---
name: plan-work
description: Create an implementation plan optimized for one coordinating agent session and parallel worker-agent execution when available. Use when the user explicitly invokes $plan-work, wants to decompose medium/large work, needs blocking edges and independent streams identified, or wants a plan that guards against accidental V1 shrinkage before $do-work.
---

# Plan Work

## Overview

Turn clarified intent into a plan that a single coordinating agent session can execute, using worker agents for independent streams when the platform supports them. The plan should make the work easier to do, not create ceremony for its own sake.

Default to chat-only plans for small and medium work. For large work, write a temporary plan to `docs/plans/<slug>.md` so it can survive the chat and later be absorbed or removed by `$canonize`.

## Planning Principles

- Preserve full intended scope unless the user explicitly chooses to defer work.
- Optimize for readable code and low cognitive load.
- Prefer simple, explicit implementation over clever abstractions.
- Make parallelism visible, but keep integration-sensitive judgment with the coordinator.
- Tailor verification to risk and iteration cost.
- Avoid test-first planning unless the user asks or the problem genuinely benefits from it.

## Workflow

1. Read context.

   Read relevant canon, the current code shape, and any prior shaping notes. If requirements are still fuzzy, stop and recommend `$shape-work`.

2. Define scope.

   State the goal, non-goals, and any constraints. Add a `Full-Scope Check` that says what must not be silently deferred.

3. Find parallel lanes.

   Decompose the work into independent streams. For each stream, list likely files/modules, required context, output expectations, and verification.

4. Identify blocking edges.

   Separate work that can start immediately from work that depends on decisions, shared interfaces, migrations, generated types, design choices, or another stream's output.

5. Keep integration central.

   Mark integration points the main coordinator should own or review closely. Avoid giving worker agents mutually incompatible authority over the same interfaces.

6. Choose artifact size.

   Keep the plan in chat for small/medium work. For large work, create `docs/plans/<slug>.md` with this frontmatter:

   ```md
   ---
   status: temporary
   owner: plan-work
   created: YYYY-MM-DD
   cleanup: absorb-with-canonize
   ---
   ```

## Output Format

Use this format in chat or in `docs/plans/<slug>.md`:

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

## Parallelism Rules

Assume one agent session coordinates the work. Plan for worker agents inside the current workspace by default when the platform supports them.

Do not plan branches or worktrees unless the user explicitly asks. If file conflicts look likely, note that worktrees may be worth asking about, but keep the default low-ceremony.
