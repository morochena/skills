---
name: start-work
description: Route work by intent, uncertainty, reversibility, coordination, and risk to direct action, evidence-producing shaping, planning, or specialized workflows.
disable-model-invocation: true
---

# Start Work

Inspect only enough local context to choose the smallest useful workflow. For a routing-only request, recommend one immediate move. When the user has also requested implementation, do clear, local, reversible work directly if intent is settled and no shared boundary needs coordination. Stay within the authorized scope. Another user-invoked skill starts only when the user invokes it; direct work does not require another skill call.

## Workflow

1. Ground the routing decision.

   Read the task and inspect only the repository facts needed to distinguish intent, dominant uncertainty, reversibility, coordination, and risk. Ask the user only for a decision, priority, constraint, or missing intent that cannot be discovered locally.

   Completion criterion: the routing decision depends on known facts rather than assumptions about the repository.

2. Route specialized intent first.

   Use the first matching branch:

   - Initialize or revise repository agent instructions: recommend `$init-project`.
   - Explore an idea without committing to requirements: recommend `$brainblast`.
   - Diagnose broken, flaky, slow, or surprising behavior: recommend `$debug-work`.
   - Create a project-local way to control and prove real app behavior: recommend `$create-verification-skill`.
   - Audit or correct an existing project-local verification skill: recommend `$maintain-verification-skill`.
   - Adversarially stress-test a completed plan before implementation: recommend `$challenge-plan`.
   - Review an existing change: recommend `$review-work`.
   - Establish or audit repository architecture: recommend `$improve-architecture`.
   - Normalize canon and remove planning sediment: recommend `$canonize`.
   - Normalize canon while preserving and marking sediment: recommend `$canonize-mark`.
   - Implement settled intent or execute a coordination plan: do authorized work directly when it meets the conditions above; otherwise recommend `$do-work`.

   Completion criterion: a specialized branch wins whenever the user's primary intent matches it, regardless of task size.

3. Route ordinary delivery work.

   When no specialized branch matches, choose the first applicable route:

   - When a user-owned product or design decision could materially change behavior, scope, architecture, or acceptance, recommend `$shape-work`.
   - When a cheap reversible artifact can answer the dominant uncertainty, recommend `$shape-work` if the evidence informs a user-owned decision; recommend `$do-work` if intent is settled and the uncertainty is technical. Useful probes include wireframes, scripts, focused tests, traces, benchmarks, contracts, and narrow working slices.
   - When intent is settled, feedback is quick, and no shared boundary needs coordination, do clear local work directly if implementation is authorized. For a routing-only request, recommend direct work or `$do-work`.
   - When parallel lanes, migrations, shared interfaces, costly or irreversible commitments, or cross-session handoff require durable coordination, recommend `$plan-work`.

   Task size may reveal coordination or risk, but never triggers planning by itself.

   Completion criterion: the recommendation targets the actual uncertainty or coordination cost and uses the cheapest safe way to produce evidence.

4. Report the result or recommend one immediate move.

   After direct work, state the result, verification, and any unresolved issue. Otherwise, state the recommendation, the evidence for it, and the first action. Mention likely later skills only as orientation, not as an automatically started sequence. Include canon, verification, parallelism, or workspace-isolation notes only when they affect the immediate choice.

   Completion criterion: the user receives a verified result with any gaps stated, or one unambiguous next action.
