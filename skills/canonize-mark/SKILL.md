---
name: canonize-mark
description: Canonize project documentation in preservation mode. Use when the user wants to create, update, normalize, or audit durable project docs while leaving ADRs, plans, specs, milestones, roadmaps, proposals, temporary docs, or stale docs in place; mark planning sediment instead of deleting it; maintain docs/canon/language.md and docs/canon/* with conservative cleanup; update agent adapters when present.
---

# Canonize Mark

Preserve non-canonical docs while making their status explicit. This is the conservative variant of `canonize`: it normalizes durable canon, then marks ADRs, temporary docs, and stale docs in place so they cannot silently steer future agents.

## Workflow

1. Load the canon rules.

   Read the sibling skill at `../canonize/SKILL.md`, then follow its inspection, classification, canon layout, adapter, product trajectory, writing, and reporting rules.

   Completion criterion: you can classify the repo's relevant markdown as `canonical`, `adapter`, `protected-reference`, `temporary`, `stale`, or `unknown` using the same rules as `canonize`.

2. Apply the preservation override.

   Replace `canonize`'s removal step with this behavior:

   - Keep `temporary`, `stale`, and `unknown` docs in their current paths, including ADR and decision-record directories.
   - Rewrite durable facts from those docs into canon before marking them.
   - Add or update status metadata so the file's non-canonical status is visible.
   - Remove canon links that make non-canon files look authoritative.
   - Keep adapters as adapters that point at `docs/canon/`; do not turn preserved sediment into agent-consumption wiring.
   - Preserve existing frontmatter fields and document content unless a narrow edit is needed to mark status.

   Completion criterion: every temporary or stale doc remains in place and carries an explicit non-canonical status, including every ADR-like file.

3. Mark non-canon docs.

   Prefer frontmatter when the file already has frontmatter or the repo commonly uses it:

   ```md
   ---
   status: temporary
   canonical: false
   last_reviewed: YYYY-MM-DD
   ---
   ```

   For stale docs:

   ```md
   ---
   status: stale
   canonical: false
   last_reviewed: YYYY-MM-DD
   ---
   ```

   When adding frontmatter would clash with the repo's style, add a first visible note instead:

   ```md
   > Status: temporary, non-canonical. This file is preserved for reference and should not guide implementation unless promoted into canon.
   ```

   Completion criterion: a future agent can tell at a glance that the file is not canon or a protected decision constraint.

4. Report the result.

   Summarize changed canon files, adapter changes, ADRs marked temporary or stale, other docs marked temporary or stale, unknown docs left unmodified, and any facts that still need human judgment.

   Completion criterion: the user can tell what is trusted canon and which preserved docs are non-canonical.

## Success Criteria

The skill is working when:

- Canon is stable across future agent sessions.
- Language canon lives in `docs/canon/language.md`.
- Adapters point at canon rather than owning canon.
- ADRs, temporary docs, and stale docs remain available but clearly non-canonical.
- Stale plans cannot steer implementation.
- Important decisions survive as current constraints, not historical artifacts.
