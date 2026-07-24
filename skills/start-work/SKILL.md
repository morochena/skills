---
name: start-work
description: Route work by intent, uncertainty, reversibility, coordination, and risk to direct action, evidence-producing shaping, planning, or specialized workflows.
---

# Start Work

Act as a router, not an orchestrator. Inspect only enough local context to choose a branch, then recommend one immediate move. Another user-invoked skill starts only when the user invokes it.

## Workflow

1. Ground the routing decision.

   Read the task and inspect only the repository facts needed to distinguish intent, dominant uncertainty, reversibility, coordination, and risk. Ask the user only for a decision, priority, constraint, or missing intent that cannot be discovered locally.

   Completion criterion: the routing decision depends on known facts rather than assumptions about the repository.

2. Route specialized intent first.

   Use the first matching branch:

   - Explore an idea without committing to requirements: recommend `$brainblast`.
   - Diagnose broken, flaky, slow, or surprising behavior: recommend `$debug-work`.
   - Adversarially stress-test a completed plan before implementation: recommend `$challenge-plan`.
   - Review an existing change: recommend `$review-work`.
   - Establish or audit repository architecture: recommend `$improve-architecture`.
   - Normalize canon and remove planning sediment: recommend `$canonize`.
   - Normalize canon while preserving and marking sediment: recommend `$canonize-mark`.
   - Implement settled intent or execute a coordination plan: recommend `$do-work`.

   Completion criterion: a specialized branch wins whenever the user's primary intent matches it, regardless of task size.

3. Route ordinary delivery work.

   When no specialized branch matches, choose the first applicable route:

   - When a user-owned product or design decision could materially change behavior, scope, architecture, or acceptance, recommend `$shape-work`.
   - When a cheap reversible artifact can answer the dominant uncertainty, recommend `$shape-work` if the evidence informs a user-owned decision; recommend `$do-work` if intent is settled and the uncertainty is technical. Useful probes include wireframes, scripts, focused tests, traces, benchmarks, contracts, and narrow working slices.
   - When intent is settled, feedback is quick, and no shared boundary needs coordination, act directly for clear local work or recommend `$do-work`.
   - When parallel lanes, migrations, shared interfaces, costly or irreversible commitments, or cross-session handoff require durable coordination, recommend `$plan-work`.

   Task size may reveal coordination or risk, but never triggers planning by itself.

   Completion criterion: the recommendation targets the actual uncertainty or coordination cost and uses the cheapest safe way to produce evidence.

4. Recommend one immediate move.

   State the recommendation, the evidence for it, and the first action. Mention likely later skills only as orientation, not as an automatically started sequence. Include canon, verification, parallelism, or workspace-isolation notes only when they affect the immediate choice.

   Completion criterion: the user receives one unambiguous next action and can invoke it without interpreting a multi-step process.
