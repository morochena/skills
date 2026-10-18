---
name: review-work
description: Run a findings-first review of implementation correctness, scope, risk, readability, and verification.
disable-model-invocation: true
---

# Review Work

Lead with actionable findings. Keep summaries secondary and operate read-only unless the user explicitly requests fixes.

## Review Priority

Prioritize issues in this order:

1. Correctness bugs and regressions
2. Scope mismatches, including accidental V1 shrinkage
3. Security, data safety, and privacy risks
4. Performance, reliability, and operational risks
5. Test gaps where missing coverage creates real risk
6. Complexity, readability, naming, and abstraction leakage
7. UI polish, accessibility, and interaction rough edges

## Workflow

1. Establish the review target.

   Use the user's specified base, branch, PR, plan, or file list. If no target is specified, inspect the working tree diff, including untracked files that belong to the change.

2. Read intent.

   Read the request, issue, chat context, canon, acceptance tests, prototypes, or other observed artifacts needed to know what the change was supposed to do.

   When the change affects a user-facing surface, look for an existing project-local `verify-*` skill in the repository's skill root. If it covers the surface, read the applicable feature files as review evidence. Do not create, repair, or maintain the verifier during a read-only review.

3. Trace affected behavior.

   Review the diff, affected call paths, state transitions, data boundaries, user-visible behavior, and relevant tests. Run focused checks that distinguish a suspected issue from a harmless pattern.

   Look beyond symbol references when safety depends on a serialized shape, persisted state, dependency version or patch, scheduling order, feature flag, or downstream consumer. Identify the few assumptions that make the change safe and use the cheapest isolated check of the real behavior that can refute them. Mark an assumption unproven when the evidence stops short; do not alter the reviewed files or run unsafe probes to complete a read-only review.

   When a matching project-local verifier exists, run its doctor check and the affected feature recipes when they use isolated scratch state. Follow its evidence and cleanup rules. Do not run recipes that can affect live services, user data, money, or people without separate authorization. Report stale verifier instructions or unsafe prerequisites as verification gaps; do not correct them inside `$review-work`.

   Assess important tests against two counterfactuals: would an incorrect result, missing effect, or duplicate effect fail the test, and would a behavior-preserving internal refactor keep it passing? Derive expected results from the contract. An assertion about a request to an external service can be behavioral; an assertion about which private helper ran usually is not. Use a mutation in an isolated copy only when it safely resolves a real coverage question, and leave the reviewed files unchanged.

   Look for vague names, mixed abstraction levels, leaky abstractions, costly indirection, hidden control flow, and inconsistency with established local patterns. Assess reader load through both the layers a reader must trace and the mutable state they must remember. Neither line count nor a single caller establishes a problem on its own.

   When a performance claim affects the review verdict, check correct completed work, comparable conditions, and run-to-run variation. If installed, read [../benchmark-checklist/SKILL.md](../benchmark-checklist/SKILL.md) for detailed guidance within this review's scope.

4. Validate and prioritize findings.

   Keep only issues with concrete evidence and a credible impact. Treat personal taste and optional rewrites as non-findings. Group repeated instances under one root finding.

5. Report findings first.

   Use severity labels:

   - `P0`: Blocks release or risks data/security.
   - `P1`: Likely bug, regression, or serious mismatch.
   - `P2`: Important quality, maintainability, or test risk.
   - `P3`: Minor polish or optional improvement.

   Report in this order: findings, open questions, short summary, and verification. Attach each finding to the tightest stable file and line range available.

6. State residual risk.

   Name unreviewed surfaces, unrun checks, uncertain assumptions, and the checks that would add confidence.

## Completion

- The change set and intended behavior are grounded in the request and repository evidence.
- Findings state evidence, impact, and the smallest useful correction, ordered by severity. Group repeated instances under one cause; state when no actionable finding remains.
- Report verification gaps and unreviewed surfaces. Keep the review read-only unless fixes are authorized.
