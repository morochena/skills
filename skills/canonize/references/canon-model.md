# Canon Model

Use this reference when creating, restructuring, or verifying project canon.

## Canon ownership

Use a coherent existing convention when one exists. Otherwise use:

```txt
docs/canon/language.md
docs/canon/product.md
docs/canon/trajectory.md
docs/canon/system.md
docs/canon/engineering.md
```

For a large or multi-domain repository, add a context-specific canon file only when the repository structure proves that another canonical home is necessary.

- `language.md`: domain and product terms, roles, business concepts, codebase-specific meanings, and naming boundaries.
- `product.md`: North Star, current product, product boundaries, and non-negotiables.
- `trajectory.md`: current directional themes, directional boundaries, and the rule for reviewing trajectory.
- `system.md`: current architecture, modules, data flow, runtime boundaries, services, persistence, authorization, and invariants.
- `engineering.md`: code organization, testing, APIs, UI, errors, naming, dependencies, and common commands.

Use this metadata when the repository has no stronger convention:

```md
---
status: canonical
last_reviewed: YYYY-MM-DD
scope: project
---
```

Update `last_reviewed` only after verifying or changing the file.

## Product trajectory

Keep current product truth in `product.md` and active direction in `trajectory.md`. Move any competing `Current Direction` section out of `product.md`.

Trajectory contains only:

- one to three active product themes;
- boundaries that limit what those themes imply;
- a review rule that removes backlog-like content.

Express future-leaning ideas as current direction or boundaries. Omit task lists, feature backlogs, uncommitted dates, speculative features, abandoned ideas, and implementation notes.

Example:

```md
# Product Trajectory

## Active Direction

The product is moving toward small-team collaboration. Near-term work should make shared ownership, visibility, and handoff clearer.

This direction stops short of a full enterprise workspace model.

## Review Rule

Keep active direction and boundaries here; move executable work into temporary planning.
```

## Canon writing

Write canon in present tense as specific, compact, source-grounded current state. State active constraints rather than decision history.

```md
Mutations use server actions by default. API routes serve endpoints that must support non-React clients.
```

Represent uncertainty explicitly instead of converting a wish or weak inference into truth. Each meaning has one canonical home; adapters and protected references may point to it rather than restate it.

## Agent consumption

Use this read order when the files exist:

1. `docs/canon/language.md`
2. `docs/canon/product.md`
3. `docs/canon/trajectory.md`
4. `docs/canon/system.md`
5. `docs/canon/engineering.md`

Adapters such as `AGENTS.md`, `CLAUDE.md`, root `CONTEXT.md`, `CONTEXT-MAP.md`, and `docs/agents/domain.md` may point to this order. Other Markdown becomes authoritative only when canon or repository instructions identify it as such.
