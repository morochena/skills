---
name: brainblast
description: Diverge through grounded lenses, then converge on promising product or engineering directions.
disable-model-invocation: true
---

# Brainblast

Diverge before converging. Keep the exploration in chat and hand off to another skill only after the user chooses a direction.

## Workflow

1. Ground the idea.

   Read canon only where its subject constrains the idea: language for terms, product for scope, trajectory for direction, system for architecture, or engineering for non-obvious constraints.

   Inspect enough of the codebase to separate product facts from assumptions. Stop once further inspection would not materially change the exploration.

2. Frame the idea.

   Restate the idea in the product's language. Name the beneficiary, the problem or opportunity, why it might matter, and the visible assumptions.

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

4. Converge on directions.

   Synthesize a small set of genuinely distinct directions. For each, name its value, tradeoffs, assumptions, and simplest plausible shape. Preserve meaningful disagreement between viable directions.

5. Ask what to pull next.

   Recommend the strongest direction while keeping alternatives visible. Ask one focused question about what to explore, sharpen, or discard. Recommend `$shape-work` when material decisions remain, `$do-work` when intent is settled and execution is clear, and `$plan-work` only when durable coordination or a costly commitment requires it.

## Output Shape

```md
## Idea In Context

## Angles

## Strongest Directions

## Risks And Open Questions

## My Recommendation

## What To Pull Next
```

## Completion

- Ground the idea in relevant project facts and distinguish assumptions from evidence.
- Present distinct directions with their value, tradeoffs, and simplest plausible form.
- End with a recommendation and one useful user choice. Keep exploration in chat unless the user requests an artifact.
