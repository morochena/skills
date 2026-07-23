# Preservation Model

Use this reference when normalizing canon or marking preserved documents.

## Canonical homes

Use a coherent existing convention when one exists. Otherwise use:

```txt
docs/canon/language.md
docs/canon/product.md
docs/canon/trajectory.md
docs/canon/system.md
docs/canon/engineering.md
```

- `language.md`: domain and product terms, roles, business concepts, and naming boundaries.
- `product.md`: North Star, current product, product boundaries, and non-negotiables.
- `trajectory.md`: current directional themes, directional boundaries, and a review rule that keeps backlog material in temporary planning.
- `system.md`: durable architectural intent, runtime boundaries, authorization rules, invariants, and tradeoffs that source structure cannot explain safely.
- `engineering.md`: non-obvious engineering constraints, naming boundaries, testing intent, and conventions whose rationale is not mechanically discoverable.

Do not create every file by default. Create a canonical home only when durable content needs it.

Use code, configuration, schemas, and tests as the authority for mechanically discoverable or enforceable behavior. Generated views may summarize those sources but do not create intent. Use canon for vocabulary, product intent, invariants, boundaries, non-goals, and rationale that executable sources cannot express safely.

Do not mirror module trees, routes, schemas, commands, dependency lists, or test inventories in canon. Omit them or point to the stable executable source. When a constraint can be enforced at reasonable cost, prefer a type, test, lint rule, schema, or configuration check and keep only its non-derivable intent in canon.

Write canon in present tense as specific, compact, source-grounded current intent. Convert decision history into current constraints, represent uncertainty explicitly, and keep each durable meaning in one prose or executable home.

Use this read order when the files exist: `language.md`, `product.md`, `trajectory.md`, `system.md`, then `engineering.md`.

## Canon metadata

Use this metadata when the repository has no stronger convention:

```md
---
status: canonical
last_reviewed: YYYY-MM-DD
scope: project
---
```

Update `last_reviewed` only after verifying or changing the file.

## Preserved status

Prefer frontmatter when the file already has frontmatter or the repository commonly uses it. Preserve existing fields and add or update:

```md
---
status: temporary
canonical: false
last_reviewed: YYYY-MM-DD
---
```

Use `status: stale` for stale material.

When frontmatter would conflict with repository style, add the first visible note:

```md
> Status: temporary, non-canonical. Preserved for reference; current intent belongs in `docs/canon/`, and current mechanics belong in executable sources.
```

Use `stale` in the note for stale material. The marker must identify the exact classification rather than merely saying the document is non-canonical.
