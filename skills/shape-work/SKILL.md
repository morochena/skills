---
name: shape-work
description: Resolve material decisions until fuzzy product or engineering work is ready to plan or build.
---

# Shape Work

Run a readiness interview: discover repository facts locally, reserve product judgment for the user, and resolve one material decision at a time.

Shape work in chat first. Write to canon only when a durable term or constraint has clearly settled.

## Workflow

1. Orient.

   Read existing canon when present, especially `docs/canon/language.md`. Inspect the codebase for facts that bear on the user's idea.

   Completion criterion: discoverable codebase facts are separated from user-owned decisions, priorities, and constraints.

2. Establish the readiness ledger.

   Track the intended outcome, in-scope behavior, explicit non-goals, acceptance signals, domain terms, constraints, and unresolved product or design decisions. Preserve the user's full intended scope unless they choose a deferral.

   Completion criterion: every known requirement or concern has one place in the ledger, and silent scope shrinkage would be visible.

3. Interview one decision at a time.

   Select the highest-leverage unresolved decision. Offer only viable, mutually exclusive options, put the recommendation first, explain the material tradeoff of each, and wait for the user's choice. Use one focused open question when honest options do not yet exist.

   Completion criterion for each turn: exactly one user-owned decision is presented, the recommendation is explicit, and the answer can update the readiness ledger without reinterpretation.

4. Sharpen language.

   Challenge overloaded or vague terms. If a term conflicts with existing canon, surface the conflict and ask which meaning should win.

   Completion criterion: every term that changes scope, behavior, ownership, or acceptance has one settled meaning or is listed as an unresolved blocker.

5. Capture settled canon.

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

6. Test readiness.

   Review the ledger after each answer. Continue the interview while an unresolved user decision could materially change scope, behavior, architecture, or acceptance. When ready, summarize settled decisions, explicit non-goals, acceptance signals, canon updates, and remaining implementation questions.

   Completion criterion: product intent can be planned or built without guessing; every remaining open question is either implementation-discoverable or explicitly non-blocking. Recommend `$plan-work` for coordinated work and direct implementation for clear local work.

## Decision Prompts

Use the environment's native structured-choice prompt when it is available and permitted. Otherwise use consistently lettered options so the user can answer with one character. Keep one decision per prompt and make accepting or revisiting the recommendation an explicit choice.

## Canon Boundaries

Write durable domain terms, product terms, roles, business concepts, and naming boundaries to `docs/canon/language.md`. Keep brainstorming, plans, issue work, rationale, decision logs, and unconfirmed guesses in temporary context.

Use `$canonize` later to absorb or remove temporary planning artifacts.
