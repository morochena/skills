---
name: review-work
description: Review implemented work for correctness, clarity, complexity, readability, abstraction quality, scope fidelity, performance, polish, edge cases, and pragmatic test coverage. Use when the user explicitly invokes $review-work, asks for a review, wants a post-build quality pass, or wants to check whether a change matches the intended plan.
---

# Review Work

## Overview

Review work like a senior engineer who values readable, communicative software. Lead with actionable findings and keep praise or summaries secondary.

This skill is read-only by default. Do not modify files unless the user explicitly asks for fixes.

## Review Axes

Prioritize issues in this order:

1. Correctness bugs and regressions
2. Scope mismatches, including accidental V1 shrinkage
3. Security, data safety, and privacy risks
4. Performance, reliability, and operational risks
5. Test gaps where missing coverage creates real risk
6. Complexity, readability, naming, and abstraction leakage
7. UI polish, accessibility, and interaction rough edges

## Engineering Taste

Look for places where the code fails to communicate:

- Names are vague, abbreviated, or missing domain context.
- Conditionals should be named intermediate variables.
- Methods mix levels of abstraction.
- Abstractions leak details or add more complexity than they remove.
- DRY creates indirection that is harder to understand than duplication.
- Advanced language features hide intent from ordinary maintainers.
- Tests verify implementation details instead of behavior.

## Workflow

1. Establish the review target.

   Use the user's specified base, branch, PR, plan, or file list. If no target is specified, inspect the working tree diff.

2. Read intent.

   Read the plan, issue, chat context, or canon needed to know what the change was supposed to do.

3. Inspect the change.

   Review diffs and affected code paths. Run focused commands only when they materially improve confidence.

4. Report findings first.

   Use severity labels:

   - `P0`: Blocks release or risks data/security.
   - `P1`: Likely bug, regression, or serious mismatch.
   - `P2`: Important quality, maintainability, or test risk.
   - `P3`: Minor polish or optional improvement.

5. Include residual risk.

   Say what you did not verify and which checks would add confidence.

## Output Format

Use this shape:

```md
## Findings

- [P1] <title> - <file:line>
  <why it matters and what to change>

## Open Questions

## Summary

## Verification
```

If there are no findings, say so clearly and name any remaining test gaps or residual risk.
