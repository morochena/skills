---
name: shape-work
description: Clarify fuzzy engineering, product, architecture, or domain work before planning or implementation. Use when the user explicitly invokes $shape-work, wants an interview, needs requirements sharpened, needs domain language settled in docs/canon/language.md, or is preparing medium/large work for $plan-work.
---

# Shape Work

## Overview

Interview the user until the work is clear enough to plan or build. Resolve one decision at a time, recommend an answer for each question, and look up codebase facts instead of asking the user to restate them.

Shape work in chat first. Write to canon only when a durable term or constraint has clearly settled.

## Workflow

1. Orient.

   Read existing canon when present, especially `docs/canon/language.md`. Inspect the codebase for facts that bear on the user's idea.

2. Name the outcome.

   Establish what done means. Watch for accidental scope shrinkage: if the user wants the full thing now, do not quietly turn it into a smaller V1.

3. Interview one decision at a time.

   Ask one question, include the recommended answer, and wait. Do not ask a questionnaire. Do not answer for the user on product or design decisions.

4. Sharpen language.

   Challenge overloaded or vague terms. If a term conflicts with existing canon, surface the conflict and ask which meaning should win.

5. Capture settled canon.

   Update `docs/canon/language.md` during the interview when domain language becomes settled. Use present tense, compact wording, and project vocabulary. Do not record unsettled ideas, implementation notes, or planning chatter.

   Create `docs/canon/language.md` only when there is settled language to capture. Use this header when no local convention exists:

   ```md
   ---
   status: canonical
   last_reviewed: YYYY-MM-DD
   scope: project
   ---
   ```

6. Stop at shared understanding.

   End with a concise summary of the settled decisions, open questions, canon updates, and the recommended next step, usually `$plan-work`.

## Canon Boundaries

Write to `docs/canon/language.md` for:

- Domain terms
- Product terms
- User roles
- Business concepts
- Naming boundaries
- Terms to avoid

Do not write to canon for:

- Brainstorming
- Temporary implementation plans
- Issue checklists
- Historical rationale
- ADR-style decision logs
- Guesses that have not been confirmed

Use `$canonize` later to absorb or remove temporary planning artifacts.
