---
name: shape-work
description: Resolve material product or design decisions through grounded conversation or cheap reversible probes until work is ready to build or coordinate.
disable-model-invocation: true
---

# Shape Work

Discover repository facts locally, reserve product judgment for the user, and resolve one material decision at a time. Use conversation when it supplies enough evidence; create the smallest reversible probe when seeing or running something would sharpen the decision.

Keep prose in chat. Keep probes disposable unless the user asks to preserve them or later execution needs them. Write to canon only when a durable term or constraint has clearly settled.

For a shaping-only request, stop when intent is ready. When the user also requests implementation, continue with that authorized work once material decisions are settled. Do not require another skill invocation or repeat an approval already supplied by the user.

## Workflow

1. Orient.

   Read canon only where its subject affects the idea; use `docs/canon/language.md` when terms need clarification. Inspect the codebase for relevant facts.

2. Establish the readiness ledger.

   Track the intended outcome, in-scope behavior, explicit non-goals, acceptance signals, domain terms, constraints, and unresolved product or design decisions. Preserve the user's full intended scope unless they choose a deferral.

3. Choose the next decision and evidence source.

   Select the highest-leverage unresolved decision. If no material user decision remains, proceed to capture settled canon and test readiness without another question. Otherwise, decide whether repository inspection, conversation, or a working probe can best reduce its uncertainty.

   Use a probe when it is cheap, reversible, and materially more informative than prose:

   - For UI or interactions, create a runnable wireframe, render it, interact with it, and inspect screenshots or console behavior when useful.
   - For logic or state, create a focused script, test harness, fixture, or simulation and inspect its output.
   - For APIs or data, exercise a request/response example, schema, contract test, or mocked integration.
   - For performance, run a narrow benchmark, trace, or measurement.

   Avoid probes whose cost, destructive effect, security exposure, or production impact exceeds the decision they inform. Keep temporary artifacts outside production paths when practical and identify anything that must survive the shaping session.

4. Produce evidence or ask.

   Run and inspect the chosen probe before drawing conclusions. Report what it demonstrates and what it cannot demonstrate. Ask only when a material user decision remains unresolved by the request and settled context. When a probe would add little, offer only viable, mutually exclusive options, put the recommendation first, and explain the material tradeoff of each. Use one focused open question when honest options do not yet exist.

   While an answer is pending, continue authorized repository checks or other work that does not depend on it. Wait for the answer before work that depends on the decision; elapsed time does not settle it.

5. Sharpen language.

   Challenge overloaded or vague terms. If a term conflicts with existing canon, surface the conflict and ask which meaning should win.

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

7. Test readiness.

   Review the ledger after each answer. Continue while an unresolved user decision could materially change scope, behavior, architecture, or acceptance. When ready, remove disposable probes that later work does not need, identify any preserved artifact and why it remains, then summarize settled decisions, explicit non-goals, acceptance signals, canon updates, and remaining implementation questions.

   Continue authorized implementation when ready. For a shaping-only request, recommend `$plan-work` only for real coordination or costly commitments; otherwise recommend direct implementation or `$do-work`.

## Decision Prompts

Use the environment's native structured-choice prompt when it is available and permitted. Otherwise use consistently lettered options so the user can answer with one character. Keep one decision per prompt and make accepting or revisiting the recommendation an explicit choice.

## Canon Boundaries

Write durable domain terms, product terms, roles, business concepts, and naming boundaries to `docs/canon/language.md`. Keep brainstorming, plans, issue work, rationale, decision logs, probe output, and unconfirmed guesses in temporary context.

Use `$canonize` later to absorb or remove temporary planning artifacts.

## Completion

- Preserve the full requested scope and settled decisions. Present at most one unresolved material user decision at a time.
- Keep evidence, assumptions, and user choices distinct. Canon edits contain only settled durable meanings; remove unneeded probes and identify retained artifacts.
- When intent is ready, state acceptance signals and remaining implementation questions. Continue authorized implementation, or recommend one next move for a shaping-only request.
