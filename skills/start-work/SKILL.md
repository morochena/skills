---
name: start-work
description: Route a task to the smallest useful workflow.
---

# Start Work

Act as a router, not an orchestrator. Inspect only enough local context to choose a branch, then recommend one immediate move. Another user-invoked skill starts only when the user invokes it.

## Workflow

1. Ground the routing decision.

   Read the task and inspect only the repository facts needed to distinguish intent, clarity, size, and risk. Ask the user only for a decision, priority, constraint, or missing intent that cannot be discovered locally.

   Completion criterion: the routing decision depends on known facts rather than assumptions about the repository.

2. Route specialized intent first.

   Use the first matching branch:

   - Explore an idea without committing to requirements: recommend `$brainblast`.
   - Diagnose broken, flaky, slow, or surprising behavior: recommend `$debug-work`.
   - Review an existing change: recommend `$review-work`.
   - Establish or audit repository architecture: recommend `$improve-architecture`.
   - Normalize canon and remove planning sediment: recommend `$canonize`.
   - Normalize canon while preserving and marking sediment: recommend `$canonize-mark`.
   - Execute a settled implementation plan: recommend `$do-work`.

   Completion criterion: a specialized branch wins whenever the user's primary intent matches it, regardless of task size.

3. Size ordinary delivery work.

   When no specialized branch matches, classify the work:

   - `trivial`: clear, local, and low-risk; act directly when action was requested.
   - `small`: mostly clear with a short assumption check; use a brief chat plan, then act directly.
   - `medium`: several files, domain terms, or design choices; recommend `$shape-work` when intent is unresolved, otherwise `$plan-work`.
   - `large`: multiple areas, blocking edges, migrations, or parallel lanes; recommend `$shape-work` when intent is unresolved, otherwise `$plan-work`.

   Completion criterion: size reflects coordination and uncertainty, not merely line count; the recommendation is the smallest workflow that covers both.

4. Recommend one immediate move.

   State the recommendation, the evidence for it, and the first action. Mention likely later skills only as orientation, not as an automatically started sequence. Include canon, verification, parallelism, or workspace-isolation notes only when they affect the immediate choice.

   Completion criterion: the user receives one unambiguous next action and can invoke it without interpreting a multi-step process.
