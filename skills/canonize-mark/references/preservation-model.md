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
- `system.md`: current architecture, modules, data flow, runtime boundaries, services, persistence, authorization, and invariants.
- `engineering.md`: code organization, testing, APIs, UI, errors, naming, dependencies, and common commands.

Write canon in present tense as specific, compact, source-grounded current state. Convert decision history into current constraints, represent uncertainty explicitly, and keep each durable meaning in one canonical home.

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
> Status: temporary, non-canonical. Preserved for reference; current implementation guidance belongs in `docs/canon/`.
```

Use `stale` in the note for stale material. The marker must identify the exact classification rather than merely saying the document is non-canonical.
