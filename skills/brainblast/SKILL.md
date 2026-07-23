---
name: brainblast
description: Diverge through grounded lenses, then converge on promising product or engineering directions.
---

# Brainblast

Diverge before converging. Keep the exploration in chat and hand off to another skill only after the user chooses a direction.

## Workflow

1. Ground the idea.

   Read relevant canon when present, especially:

   - `docs/canon/language.md`
   - `docs/canon/product.md`
   - `docs/canon/trajectory.md`
   - `docs/canon/system.md`
   - `docs/canon/engineering.md`

   Inspect enough of the codebase to separate product facts from assumptions. Stop once further inspection would not materially change the exploration.

   Completion criterion: every fact used to constrain the idea is source-grounded, and every remaining uncertainty is labeled as an assumption.

2. Frame the idea.

   Restate the idea in the product's language. Name the beneficiary, the problem or opportunity, why it might matter, and the visible assumptions.

   Completion criterion: the framing is concrete enough that the user can correct the premise before divergence begins.

3. Diverge through lenses.

   Explore every materially relevant lens:

   - `User value`: who benefits, what gets easier, what pain disappears.
   - `Product fit`: how it supports or conflicts with the current product direction.
   - `Workflow fit`: where it enters the user's or operator's actual routine.
   - `Implementation shape`: the simplest plausible technical shape.
   - `Complexity risk`: where the idea may become too big, leaky, or clever.
   - `Skeptic pass`: why this might not be worth doing.
   - `Delight pass`: what would make it unusually useful, polished, or memorable.
   - `Weird option`: one non-obvious version that might reveal a better direction.

   Completion criterion: each relevant lens contributes a distinct observation or is explicitly marked inapplicable; the skeptic and weird-option lenses are included unless they genuinely do not fit.

4. Converge on directions.

   Synthesize a small set of genuinely distinct directions. For each, name its value, tradeoffs, assumptions, and simplest plausible shape. Preserve meaningful disagreement between viable directions.

   Completion criterion: the directions are distinguishable by a material choice, and the user can compare their consequences.

5. Ask what to pull next.

   Recommend the strongest direction while keeping alternatives visible. Ask one focused question about what to explore, sharpen, or discard. Recommend `$shape-work` when material decisions remain, `$do-work` when intent is settled and execution is clear, and `$plan-work` only when durable coordination or a costly commitment requires it.

   Completion criterion: the response ends with one clear recommendation and one user choice, without creating files or starting implementation.

## Output Shape

```md
## Idea In Context

## Angles

## Strongest Directions

## Risks And Open Questions

## My Recommendation

## What To Pull Next
```
