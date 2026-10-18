---
name: debug-work
description: Run a red-to-green diagnosis loop for broken, flaky, slow, or surprising behavior.
disable-model-invocation: true
---

# Debug Work

Establish a trustworthy red signal, explain it, then turn it green or brief the unresolved decision with evidence.

## Workflow

1. Define the claim.

   State the observed behavior, expected behavior, affected surface, and known reproduction path. Discover missing technical facts locally; ask one focused question only when a user-only detail blocks the investigation.

2. Establish red.

   Inspect relevant code, logs, tests, recent changes, configuration, and canon. Run the smallest command, test, measurement, or manual path that reliably exposes the behavior. When full reproduction is expensive, establish a narrower proxy signal.

3. Localize the fault.

   Trace the red signal across the relevant boundaries: input, state, data model, side effect, render path, network call, cache, concurrency, environment, or dependency. For performance work, measure where time or resources are spent. For UI work, inspect rendered behavior when possible.

4. Falsify hypotheses.

   Test one hypothesis at a time with targeted instrumentation, temporary logging, focused tests, measurements, or code reading. Prefer the simplest explanation that accounts for all observed evidence.

   After two attempted fixes that share a premise fail the same signal, state that premise and test it before another fix relies on it. Choose an observation that would differ if the premise were false. If it cannot yet be tested, name the evidence gap and seek a discriminating measurement instead of layering on another speculative patch.

   When a performance comparison drives the diagnosis, check correct completed work, comparable conditions, and run-to-run variation. If installed, read [../benchmark-checklist/SKILL.md](../benchmark-checklist/SKILL.md) for detailed measurement guidance within this workflow.

5. Resolve or brief.

   Before adding a guard, retry, or fallback, determine whether the triggering state is legitimate. Handle a legitimate state at the responsible boundary; otherwise trace the invalid state to its producer. Preserve necessary containment while correcting the cause.

   When resolution is authorized and the diagnosis is conclusive, implement the smallest readable change at the localized boundary. When resolution needs a product decision, produce a concise brief and recommend `$shape-work`. Recommend `$plan-work` only when the diagnosed fix creates durable coordination, migration order, shared-interface ownership, or a costly commitment.

6. Turn the signal green.

   Re-run the red signal and the highest-signal regression checks. Add a test when it protects meaningful behavior or a likely recurrence. Remove temporary instrumentation unless it is useful permanent observability.

7. Report the diagnosis.

   Explain the cause, decisive evidence, fix or recommended fix, and verification.

For flaky behavior, investigate state, time, ordering, isolation, and environment before widening the search.

## Completion

- The diagnosis distinguishes observed behavior from inference and identifies decisive evidence or a precise reproduction gap.
- An authorized fix makes the original signal pass, covers relevant regression risk, and leaves no unrelated edits or temporary instrumentation.
- Report the cause, result, checks, and unresolved decisions or verification gaps.
