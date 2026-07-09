---
name: brainblast
description: Explore product, feature, architecture, or creative engineering ideas from multiple angles before deciding whether to shape, plan, or build. Use when the user explicitly invokes $brainblast, wants brainstorming grounded in the current product context, asks to explore an idea without committing to implementation, or wants divergent perspectives synthesized into promising directions.
---

# Brainblast

## Overview

Explore an idea without prematurely turning it into a plan. Use product context, canon, and several deliberate lenses to help the user find the most interesting, useful, and practical shape of the idea.

This skill is divergent first and convergent only at the end. Keep it chat-first. Do not edit files, update canon, create plans, or start implementation unless the user explicitly asks.

## Workflow

1. Load product context.

   Read relevant canon when present:

   - `docs/canon/language.md`
   - `docs/canon/product.md`
   - `docs/canon/trajectory.md`
   - `docs/canon/system.md`
   - `docs/canon/engineering.md`

   Inspect the codebase only enough to ground the conversation. Do not over-research before ideating.

2. Restate the idea.

   Put the idea in the product's language. Say what it seems to be about, why it might matter, and what assumptions are already visible.

3. Explore through lenses.

   Generate perspectives from several lenses. Use the relevant ones; skip lenses that do not fit.

   - `User value`: who benefits, what gets easier, what pain disappears.
   - `Product fit`: how it supports or conflicts with the current product direction.
   - `Workflow fit`: where it enters the user's or operator's actual routine.
   - `Implementation shape`: the simplest plausible technical shape.
   - `Complexity risk`: where the idea may become too big, leaky, or clever.
   - `Skeptic pass`: why this might not be worth doing.
   - `Delight pass`: what would make it unusually useful, polished, or memorable.
   - `Weird option`: one non-obvious version that might reveal a better direction.

4. Synthesize.

   Collapse the exploration into a few promising directions. Name the tradeoffs. Avoid pretending there is consensus when there are multiple good paths.

5. Ask what to pull next.

   End by asking which direction the user wants to explore, sharpen, or discard. If the idea is ready to converge, recommend `$shape-work`. If it is ready to execute, recommend `$plan-work`.

## Council Pattern

You may simulate a lightweight council of perspectives, but keep it low ceremony. Do not create named personas unless that helps the user read the tradeoffs.

Prefer this rhythm:

```md
## Idea In Context

## Angles

## Strongest Directions

## Risks And Open Questions

## My Recommendation

## What To Pull Next
```

## Boundaries

- Do not write to `docs/canon/` by default.
- Do not write `docs/plans/` by default.
- Do not start implementation.
- Do not over-index on consensus; productive disagreement is useful.
- Do not force every idea to become work.
- Keep the tone exploratory, candid, and concrete.
