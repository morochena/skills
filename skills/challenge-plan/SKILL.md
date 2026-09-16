---
name: challenge-plan
description: Stress-test an existing plan when the user explicitly requests an adversarial review, pressure test, red-team review, or council.
disable-model-invocation: true
---

# Challenge Plan

Stress-test a completed plan before implementation. Operate read-only unless the user explicitly asks to revise the plan.

Plan Work already includes proportional review during plan creation. This skill provides a separate review through independent lenses and anonymized cross-review.

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

2. Run independent adversarial passes.

   Dispatch the five advisors as separate subagents, in parallel where capacity permits. When capacity requires batches, preserve independence by withholding every other advisor's output until all first passes finish.

   Tell each advisor to stay inside its assigned lens and return at most three material findings. Require each finding to include:

   - the challenged plan claim or omission;
   - concrete evidence or a clearly labeled unproven assumption;
   - the credible consequence;
   - the smallest useful plan amendment or discriminator.

   Do not ask advisors to be balanced, reach consensus, rewrite the entire plan, or fill a criticism quota.

3. Run anonymized cross-review.

   Start a second pass with every first-pass advisor, including any specialist. Remove role names, label the first-pass responses `A`, `B`, and so on, and randomize their order separately for each reviewer. Give every reviewer the complete set without revealing authorship. Ask:

   1. Which finding is best supported and most consequential?
   2. Which finding is weakest, duplicated, or merely preference?
   3. Which disagreement must be resolved before implementation?
   4. What material concern, if any, did every response miss?

   Keep peer reviews concise. Their purpose is to test the findings, not create a second pile of unranked commentary. Wait for every reviewer before synthesis.

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

5. Hand off one next move.

   Recommend `$do-work` when the plan is ready, `$plan-work` when amendments or replanning are needed, or `$shape-work` when the council uncovered a user-owned product decision. Do not invoke the next skill automatically.

   If the user asks to revise the plan, apply only accepted amendments, preserve the original scope ledger, and rerun the plan's traceability check.

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

## Completion

- All council members complete independent review and anonymized cross-review of the same plan and evidence.
- The verdict follows from supported findings; each required amendment identifies its plan target, consequence, and useful correction.
- Report one next action and remaining risks. Revise the plan only when authorized, preserving its full scope.
