---
name: challenge-plan
description: Adversarially stress-test a completed implementation plan before execution through independent review lenses, anonymized cross-review, and an evidence-weighted readiness verdict. Use after plan-work when a plan has costly assumptions, shared boundaries, migrations, novel architecture, broad blast radius, or the user asks for a council, pressure test, red-team review, or adversarial plan review.
---

# Challenge Plan

Stress-test a completed plan before implementation. Operate read-only unless the user explicitly asks to revise the plan.

Be adversarial without manufacturing objections. Retain only challenges with concrete evidence, credible impact, and a useful plan amendment. A council member may report no material finding.

## Council Lenses

Convene these five independent advisors:

1. **Reuse Scout**

   Look for existing project code, platform primitives, framework features, libraries, services, or established patterns that could replace planned custom work. Compare adoption and invention on fit, integration cost, maintenance, security, licensing, lock-in, and operational burden. Do not recommend a dependency merely because one exists.

2. **Outcome Guardian**

   Trace every major commitment to the project's stated goals, user outcome, scope, non-goals, and acceptance signals. Flag work that is locally sensible but strategically irrelevant, gold-plated, contradictory, or unlikely to change the intended outcome.

3. **Alternative Architect**

   Produce at least one materially different implementation path when a credible one exists. Prefer smaller surfaces, deletions, reversible steps, progressive migration, and established local patterns. Compare alternatives on complexity, coupling, reversibility, delivery risk, and verifiability; do not offer style-only rewrites.

4. **Failure Modeler**

   Test the plan against boundary inputs, state transitions, partial failure, retries and idempotency, concurrency and ordering, permissions, external dependency failure, migration and backward compatibility, rollback and recovery, and realistic scale. Prioritize failure modes that change architecture, scope, sequence, or verification rather than listing every imaginable edge case.

5. **Evidence and Delivery Auditor**

   Challenge the plan's evidence, assumptions, dependencies, ownership, sequencing, integration points, rollout, observability, rollback, and verification. Identify claims that need a cheap discriminator, steps too large to teach anything before commitment, and outcomes with no convincing proof of completion.

Add one narrowly defined specialist only when project evidence shows material security, privacy, accessibility, compliance, performance, data-integrity, or operational risk. Do not add a specialist for generic thoroughness.

## Workflow

1. Establish the review packet.

   Identify the exact completed plan and read the sources needed to judge it: project canon, stated goals, relevant code and dependency manifests, tests, prior probes, architecture constraints, and the plan's evidence and assumptions. If no reviewable plan exists, stop and recommend `$plan-work`.

   Give every advisor the same neutral packet: plan text or path, goal, constraints, supporting sources, and known unknowns. Separate observed facts from plan claims.

   Completion criterion: every advisor can inspect the same plan, intent, and evidence without reconstructing missing context.

2. Run independent adversarial passes.

   Dispatch the five advisors as separate subagents, in parallel where capacity permits. When capacity requires batches, preserve independence by withholding every other advisor's output until all first passes finish.

   Tell each advisor to stay inside its assigned lens and return at most three material findings. Require each finding to include:

   - the challenged plan claim or omission;
   - concrete evidence or a clearly labeled unproven assumption;
   - the credible consequence;
   - the smallest useful plan amendment or discriminator.

   Do not ask advisors to be balanced, reach consensus, rewrite the entire plan, or fill a criticism quota.

   Completion criterion: all default lenses ran independently, and every proposed finding is falsifiable or tied to observable project evidence.

3. Run anonymized cross-review.

   Start a second pass with every first-pass advisor, including any specialist. Remove role names, label the first-pass responses `A`, `B`, and so on, and randomize their order separately for each reviewer. Give every reviewer the complete set without revealing authorship. Ask:

   1. Which finding is best supported and most consequential?
   2. Which finding is weakest, duplicated, or merely preference?
   3. Which disagreement must be resolved before implementation?
   4. What material concern, if any, did every response miss?

   Keep peer reviews concise. Their purpose is to test the findings, not create a second pile of unranked commentary. Wait for every reviewer before synthesis.

   Completion criterion: every first-pass advisor completed peer review, every challenge faced independent scrutiny, and newly introduced concerns meet the same evidence and impact standard.

4. Synthesize by evidence, not votes.

   Act as chair. Reconcile overlapping findings, inspect disputed evidence when cheap, and reject speculative or low-impact objections. A strong minority finding outweighs shallow consensus.

   Assign each surviving amendment one level:

   - `Blocker`: implementation should not start until resolved.
   - `Material`: amend the plan before execution.
   - `Watch`: carry the risk and its verification into execution.

   Choose one verdict:

   - `Ready`: no blocker or material amendment remains.
   - `Revise`: the approach remains sound, but material plan edits are required.
   - `Replan`: the goal, premise, or implementation approach needs fundamental reconsideration.

   Completion criterion: the verdict follows from surviving evidence, every required amendment names its target in the plan, and the result does not smuggle rejected challenges back in as vague caution.

5. Hand off one next move.

   Recommend `$do-work` when the plan is ready, `$plan-work` when amendments or replanning are needed, or `$shape-work` when the council uncovered a user-owned product decision. Do not invoke the next skill automatically.

   If the user asks to revise the plan, apply only accepted amendments, preserve the original scope ledger, and rerun the plan's traceability check.

   Completion criterion: the user receives one unambiguous next action and knows which risks were resolved, retained, or rejected.

## Output Format

```md
# Plan Challenge: <plan name>

## Verdict
<Ready | Revise | Replan> — <short rationale>

## Required Amendments
- <Blocker | Material>: <plan target, evidence, impact, and exact amendment>

## Risks To Carry
- <Watch item and execution-time verification>

## Council Disagreements
- <surviving tension and how it was resolved or why it remains open>

## Rejected Challenges
- <plausible objection rejected for weak evidence, duplication, or low impact>

## Confirmed Strengths
- <important plan choices that survived adversarial review>

## Next Move
<one action>
```

Omit empty sections. Keep individual advisor transcripts out of the main result unless the user asks for them.
