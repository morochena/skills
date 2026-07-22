---
name: debug-work
description: Run a red-to-green diagnosis loop for broken, flaky, slow, or surprising behavior.
---

# Debug Work

Establish a trustworthy red signal, explain it, then turn it green or brief the unresolved decision with evidence.

## Workflow

1. Define the claim.

   State the observed behavior, expected behavior, affected surface, and known reproduction path. Discover missing technical facts locally; ask one focused question only when a user-only detail blocks the investigation.

   Completion criterion: the claim distinguishes expected from observed behavior and identifies the smallest surface that can prove the difference.

2. Establish red.

   Inspect relevant code, logs, tests, recent changes, configuration, and canon. Run the smallest command, test, measurement, or manual path that reliably exposes the behavior. When full reproduction is expensive, establish a narrower proxy signal.

   Completion criterion: a repeatable red signal exists, or the report states exactly what prevented reproduction and what narrower evidence was established.

3. Localize the fault.

   Trace the red signal across the relevant boundaries: input, state, data model, side effect, render path, network call, cache, concurrency, environment, or dependency. For performance work, measure where time or resources are spent. For UI work, inspect rendered behavior when possible.

   Completion criterion: the failing boundary is narrow enough to form falsifiable hypotheses, and the evidence rules out unrelated layers.

4. Falsify hypotheses.

   Test one hypothesis at a time with targeted instrumentation, temporary logging, focused tests, measurements, or code reading. Prefer the simplest explanation that accounts for all observed evidence.

   Completion criterion: one hypothesis explains the red signal and predicts a confirming change, or every remaining hypothesis and missing discriminator is reported.

5. Resolve or brief.

   When resolution is authorized and the diagnosis is conclusive, implement the smallest readable change at the localized boundary. When resolution needs a product decision or larger design, produce a concise brief and recommend `$shape-work` or `$plan-work`.

   Completion criterion: the change follows from the diagnosis without unrelated rewriting, or the brief identifies the exact decision that prevents a safe fix.

6. Turn the signal green.

   Re-run the red signal and the highest-signal regression checks. Add a test when it protects meaningful behavior or a likely recurrence. Remove temporary instrumentation unless it is useful permanent observability.

   Completion criterion: the original red signal is green, relevant regression checks pass, and every unrun check or residual uncertainty is explicit.

7. Report the diagnosis.

   Explain the cause, decisive evidence, fix or recommended fix, and verification.

   Completion criterion: the user can distinguish what was observed, what was inferred, what changed, and what remains uncertain.

For flaky behavior, investigate state, time, ordering, isolation, and environment before widening the search.
