---
name: shape-work
description: Resolve material product or design decisions through grounded conversation or cheap reversible probes until work is ready to build or coordinate.
---

# Shape Work

Discover repository facts locally, reserve product judgment for the user, and resolve one material decision at a time. Use conversation when it supplies enough evidence; create the smallest reversible probe when seeing or running something would sharpen the decision.

Keep prose in chat. Keep probes disposable unless the user asks to preserve them or later execution needs them. Write to canon only when a durable term or constraint has clearly settled.

## Workflow

1. Orient.

   Read existing canon when present, especially `docs/canon/language.md`. Inspect the codebase for facts that bear on the user's idea.

   Completion criterion: discoverable codebase facts are separated from user-owned decisions, priorities, and constraints.

2. Establish the readiness ledger.

   Track the intended outcome, in-scope behavior, explicit non-goals, acceptance signals, domain terms, constraints, and unresolved product or design decisions. Preserve the user's full intended scope unless they choose a deferral.

   Completion criterion: every known requirement or concern has one place in the ledger, and silent scope shrinkage would be visible.

3. Choose the next decision and evidence source.

   Select the highest-leverage unresolved decision. Decide whether repository inspection, conversation, or a working probe can best reduce its uncertainty.

   Use a probe when it is cheap, reversible, and materially more informative than prose:

   - For UI or interactions, create a runnable wireframe, render it, interact with it, and inspect screenshots or console behavior when useful.
   - For logic or state, create a focused script, test harness, fixture, or simulation and inspect its output.
   - For APIs or data, exercise a request/response example, schema, contract test, or mocked integration.
   - For performance, run a narrow benchmark, trace, or measurement.

   Avoid probes whose cost, destructive effect, security exposure, or production impact exceeds the decision they inform. Keep temporary artifacts outside production paths when practical and identify anything that must survive the shaping session.

   Completion criterion: the next decision has a concrete evidence source, and any probe has an explicit question it can answer.

4. Produce evidence or ask.

   Run and inspect the chosen probe before drawing conclusions. Report what it demonstrates and what it cannot demonstrate. When a probe would add little, offer only viable, mutually exclusive options, put the recommendation first, and explain the material tradeoff of each. Use one focused open question when honest options do not yet exist.

   Completion criterion for each turn: exactly one user-owned decision is presented, the recommendation is explicit, and the evidence is observable rather than hypothetical.

5. Sharpen language.

   Challenge overloaded or vague terms. If a term conflicts with existing canon, surface the conflict and ask which meaning should win.

   Completion criterion: every term that changes scope, behavior, ownership, or acceptance has one settled meaning or is listed as an unresolved blocker.

6. Capture settled canon.

   Update `docs/canon/language.md` when domain language becomes durable. Use present tense, compact wording, and project vocabulary. Keep unsettled ideas and implementation planning in the readiness ledger rather than canon.

   Create `docs/canon/language.md` only when there is settled language to capture. Use this header when no local convention exists:

   ```md
   ---
   status: canonical
   last_reviewed: YYYY-MM-DD
   scope: project
   ---
   ```

   Completion criterion: each canon edit records only a settled durable meaning and preserves the repository's existing canon conventions.

7. Test readiness.

   Review the ledger after each answer. Continue while an unresolved user decision could materially change scope, behavior, architecture, or acceptance. When ready, remove disposable probes that later work does not need, identify any preserved artifact and why it remains, then summarize settled decisions, explicit non-goals, acceptance signals, canon updates, and remaining implementation questions.

   Completion criterion: product intent can be built without guessing; every remaining open question is either implementation-discoverable or explicitly non-blocking. Recommend `$plan-work` only for durable coordination, migration order, shared boundaries, or costly commitments; otherwise recommend direct implementation or `$do-work`.

## Decision Prompts

Use the environment's native structured-choice prompt when it is available and permitted. Otherwise use consistently lettered options so the user can answer with one character. Keep one decision per prompt and make accepting or revisiting the recommendation an explicit choice.

## Canon Boundaries

Write durable domain terms, product terms, roles, business concepts, and naming boundaries to `docs/canon/language.md`. Keep brainstorming, plans, issue work, rationale, decision logs, probe output, and unconfirmed guesses in temporary context.

Use `$canonize` later to absorb or remove temporary planning artifacts.
