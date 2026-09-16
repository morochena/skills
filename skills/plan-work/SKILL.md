---
name: plan-work
description: Plan work that needs coordination across shared interfaces, migrations, parallel streams, or costly commitments. Review and refine the plan before execution.
disable-model-invocation: true
---

# Plan Work

Coordinate settled work with real dependencies, shared ownership, migration order, costly commitments, or handoff needs. Task size alone does not require a plan.

## Scope and Authorization

For a planning-only request, return the refined plan without implementing it. When the user also requests implementation, continue through implementation and required checks once the plan is ready. Do not ask for approval already supplied by the request or settled conversation. This continuation does not invoke another skill or authorize extra scope or external actions.

When no coordination is needed, keep any requested plan brief. Implement directly if authorized; otherwise recommend direct work or `$do-work`. Ask only for an unresolved material decision or missing authorization that affects the next action. Continue independent authorized work while waiting.

## Build the Plan

Read only the code, canon, tests, and prior results needed to establish affected boundaries and intent. Run a cheap non-destructive check or disposable probe when a technical assumption could change the plan. Separate observed evidence from unproven assumptions, and name a useful check for each material assumption.

Record the goal, constraints, non-goals, acceptance signals, and every requested outcome. Mark user-chosen deferrals explicitly. Do not silently reduce scope to make the plan easier to execute.

For each outcome, identify its implementation location, dependencies, and verification. Create independent work streams only when they help. Each stream needs an owner, required context, likely files, expected output, and checks. Keep sequential work on the critical path.

Give one coordinator ownership of shared interfaces, overlapping files, migrations, architecture decisions, and final integration. State what makes each dependent step ready to start. Use the current workspace; propose branches or worktrees only when the user requests isolation or likely conflicts justify asking.

Keep the plan in chat unless coordination must survive the current execution context. For a durable plan, write `docs/plans/<slug>.md` with:

```md
---
status: temporary
owner: plan-work
created: YYYY-MM-DD
cleanup: absorb-with-canonize
---
```

## Review and Refine

Read [references/adversarial-review.md](references/adversarial-review.md) when reviewing the draft. Apply the standard review once. Use deep independent review only for a listed high-consequence commitment with a material evidence gap.

Apply accepted amendments to the plan and check that every requested outcome still has an owner, execution path, and verification method. Resolve material findings before affected implementation. Do not add another review workflow by default.

## Deliver or Execute

For a planning-only request, return one refined plan. Use headings that help the reader find scope, evidence, assumptions, execution order, ownership, and verification. Link canon only where the plan needs it, with a reason to read each file. Omit empty sections and separate review transcripts.

For an authorized implementation request, carry out the plan in useful working slices. Follow repository instructions and relevant verification guidance. Fix failures caused by the change, complete required checks, and clean up temporary artifacts. Reuse valid check results; repeat or expand checks only for invalidated results, failures, or uncovered risks. Do not stop after the first slice or merely recommend another skill.

Report the result, checks, and any user-deferred or blocked outcome. When implementation is not requested, recommend one next move. If a material user decision blocks work, state that exact decision and complete any independent authorized work.

## Completion

- Every requested outcome is covered or explicitly deferred by the user; facts and assumptions remain distinct.
- The plan identifies dependencies, one owner for each shared boundary, and a verification method for each outcome.
- Accepted review findings are resolved in the plan; remaining risks have a named check or decision.
- A planning-only request ends with a usable plan. An implementation request ends with verified work or a precise blocker and completed independent work.
