# Proportional Plan Review

Use this review inside Plan Work. Refine the draft before returning it. Do not produce a separate review deliverable.

## Standard Review

Review every draft once through these lenses:

1. **Reuse:** Check whether established project code, platform features, or local patterns can replace planned custom work.
2. **Outcome:** Trace each major commitment to the goal, scope, non-goals, and acceptance signals.
3. **Alternative:** Consider a smaller, more reversible path when a materially different credible option exists.
4. **Failure:** Test the plan against relevant partial failure, ordering, permissions, compatibility, rollback, recovery, and realistic scale.
5. **Evidence and delivery:** Challenge unproven assumptions, sequencing, ownership, integration, rollout, observability, and verification.

Retain a concern only when it has concrete evidence or a clearly labeled assumption, a credible effect, and a useful amendment or discriminator. Apply retained amendments directly. Do not fill a criticism quota.

## Deep Review Gate

Run the deep review only when established evidence shows at least one of these signals:

- A destructive or irreversible production data change.
- A breaking public interface or an external cutover whose consumers cannot move together.
- An authentication, authorization, security, or privacy boundary with unresolved correctness evidence.
- A production change without a tested recovery path where failure can cause data loss, loss of access, or a prolonged outage.
- Another named commitment with comparable impact and reversal cost.

The draft must also contain a material evidence gap that can change architecture, scope, sequence, rollback, or recovery. Shared interfaces, ordinary migrations, parallel lanes, task size, broad scope, and new architecture do not activate deep review by themselves. Use the standard review when a small reversible implementation slice can answer the main question.

## Deep Independent Review

When the gate is met:

1. Build one neutral packet with the draft plan, goal, constraints, evidence, assumptions, and relevant project sources.
2. Dispatch the five standard lenses as independent advisors when subagents are available. Add one specialist only when project evidence shows a material security, privacy, accessibility, compliance, performance, data-integrity, or operational risk. Preserve independence until all first passes finish. Ask each advisor for at most three material findings. Each finding must state the challenged claim, evidence or assumption, credible effect, and smallest useful amendment or discriminator.
3. Give every advisor the complete anonymized set of first-pass findings in a different order. Ask each advisor to identify the strongest finding, weak or duplicate findings, unresolved disagreements, and any material concern that all advisors missed. Wait for all cross-reviews before synthesis.
4. Synthesize by evidence. Reject speculative, duplicate, and low-impact findings. Classify retained findings as `Blocker`, `Material`, or `Watch`.
5. Apply `Blocker` and `Material` amendments to the draft. Put each `Watch` item in execution-time verification. Rerun the scope and traceability checks.

If subagents are unavailable, use the five lenses for a structured self-review, then apply the same evidence and amendment rules. State that all passes shared one context and do not provide independent review. Do not simulate separate advisors or anonymized cross-review.

## Result

Return one refined plan. Include `Review Applied` only when it helps execution:

- State `Standard` or `Deep`, and name the deep-review signal when applicable. If deep review used the fallback, always label it `Deep — structured self-review` and disclose the shared-context limitation.
- List material changes that the review made to the plan.
- Record a rejected concern only when it is likely to return during execution.

If review exposes a missing material user decision, state the exact decision and pause only the work that depends on it. Continue independent authorized work. Do not guess the answer or treat a settled decision as missing.
