---
name: debug-work
description: Diagnose broken, flaky, slow, or surprising behavior through reproduction, localization, hypothesis testing, and pragmatic fixes. Use when the user explicitly invokes $debug-work, reports a bug or performance regression, wants triage-style investigation without issue-tracker ceremony, or needs a verified diagnosis before implementation.
---

# Debug Work

## Overview

Debug behavior before rewriting it. The goal is to reproduce, localize, explain, and then fix or brief the fix with evidence.

This is not an issue-tracker triage workflow. Avoid labels, state machines, and ceremony unless the user explicitly asks for tracker work.

## Workflow

1. State the claim.

   Write the observed behavior, expected behavior, affected surface, and any known reproduction steps. If a key reproduction detail is missing and cannot be discovered locally, ask one specific question.

2. Gather facts.

   Inspect relevant code, logs, tests, recent changes, configuration, and canon. Look up codebase facts instead of asking the user.

3. Reproduce or narrow.

   Run the smallest command, test, or manual path that can confirm the behavior. If full reproduction is expensive, find a narrower signal.

4. Localize.

   Trace from symptom to boundary: input, state, data model, side effect, render path, network call, cache, concurrency, environment, or dependency. Prefer evidence over vibes.

5. Test hypotheses.

   Make one hypothesis at a time. Use targeted instrumentation, temporary logging, focused tests, or code reading to falsify it.

6. Fix or brief.

   If the fix is clear and the user asked for resolution, implement the smallest readable fix. If the fix needs a decision or larger design, produce a concise brief and recommend `$shape-work` or `$plan-work`.

7. Verify.

   Re-run the reproduction and the most relevant regression checks. Add a test only when it protects meaningful behavior or prevents likely recurrence.

8. Report.

   Explain the cause, the evidence, the fix or recommended fix, and what was verified.

## Debugging Taste

- Prefer boring explanations over clever ones.
- Do not rewrite large areas before locating the fault.
- Keep temporary instrumentation out of the final diff unless it is useful permanent observability.
- Treat flaky bugs as state, time, ordering, isolation, or environment problems until proven otherwise.
- Treat performance bugs as measurement problems first, implementation problems second.
- For UI bugs, inspect the rendered behavior when possible instead of trusting code shape alone.
