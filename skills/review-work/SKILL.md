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

   When a matching project-local verifier exists, run its doctor check and the affected feature recipes when they use isolated scratch state. Follow its evidence and cleanup rules. Do not run recipes that can affect live services, user data, money, or people without separate authorization. Report stale verifier instructions or unsafe prerequisites as verification gaps; do not correct them inside `$review-work`.

   Look for vague names, mixed abstraction levels, leaky abstractions, costly indirection, hidden control flow, behavior tested through implementation details, and inconsistency with established local patterns.

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
