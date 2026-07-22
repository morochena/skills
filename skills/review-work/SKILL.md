---
name: review-work
description: Run a findings-first review of implementation correctness, scope, risk, readability, and verification.
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

   Use the user's specified base, branch, PR, plan, or file list. If no target is specified, inspect the working tree diff.

   Completion criterion: the exact change set and comparison base are known, including untracked files that belong to the change.

2. Read intent.

   Read the plan, issue, chat context, or canon needed to know what the change was supposed to do.

   Completion criterion: every intended outcome and explicit non-goal has a source; missing intent is recorded as an open question rather than guessed.

3. Trace affected behavior.

   Review the diff, affected call paths, state transitions, data boundaries, user-visible behavior, and relevant tests. Run focused checks that distinguish a suspected issue from a harmless pattern.

   Look for vague names, mixed abstraction levels, leaky abstractions, costly indirection, hidden control flow, behavior tested through implementation details, and inconsistency with established local patterns.

   Completion criterion: every changed behavior has been traced through its meaningful callers, effects, and tests, and every applicable review priority has been considered.

4. Validate and prioritize findings.

   Keep only issues with concrete evidence and a credible impact. Treat personal taste and optional rewrites as non-findings. Group repeated instances under one root finding.

   Completion criterion: every retained finding states the broken or risky behavior, evidence, impact, and smallest useful remediation.

5. Report findings first.

   Use severity labels:

   - `P0`: Blocks release or risks data/security.
   - `P1`: Likely bug, regression, or serious mismatch.
   - `P2`: Important quality, maintainability, or test risk.
   - `P3`: Minor polish or optional improvement.

   Report in this order: findings, open questions, short summary, and verification. Attach each finding to the tightest stable file and line range available.

   Completion criterion: findings are ordered by severity and leverage; the absence of findings is stated explicitly when no actionable issue remains.

6. State residual risk.

   Name unreviewed surfaces, unrun checks, uncertain assumptions, and the checks that would add confidence.

   Completion criterion: the user can distinguish verified safety from remaining uncertainty.
