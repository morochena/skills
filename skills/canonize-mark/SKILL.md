---
name: canonize-mark
description: Canonize durable non-derivable project intent while preserving and visibly marking planning sediment in place.
disable-model-invocation: true
---

# Canonize Mark

Preserve non-canonical documents while making their status unmistakable. Let code, configuration, schemas, and tests own mechanically discoverable truth. Normalize durable intent, reconcile active constraints, and mark planning sediment in place so future agents can distinguish it from trusted truth.

## Workflow

1. Inventory and classify the documentation surface.

   Read repository instructions, root documentation, `docs/` indexes, and every relevant in-scope Markdown file. Inspect source and configuration only as needed to ground documentation claims. Exclude generated tool state, vendored documentation, dependency checkouts, build output, and nested projects outside the requested scope.

   Classify every in-scope document:

   - `canonical`: maintained current truth future agents should trust.
   - `adapter`: agent-specific wiring that points to canon.
   - `protected-reference`: maintained operational, contribution, security, policy, or license material.
   - `temporary`: active plans, drafts, specs, ADRs, handoffs, investigations, or proposals.
   - `stale`: obsolete planning or generated documentation whose active constraints are obsolete or already absorbed.
   - `unknown`: potentially useful material that cannot yet be classified or source-grounded.

   Treat ADR and decision-record files as temporary or stale source material in preservation mode.

   For each candidate claim, identify whether its proper authority is executable—code, configuration, schema, test, or generated output—or prose canon.

2. Normalize canon and reconcile active constraints.

   Before editing canon or status markers, read [references/preservation-model.md](references/preservation-model.md) for canonical homes, writing rules, and marking formats. Prefer a coherent existing `docs/canon/` convention; otherwise use the model in that reference.

   Preserve vocabulary, intent, invariants, boundaries, non-goals, and rationale that executable sources cannot express safely. Remove mechanically discoverable duplication from canon or replace it with a stable pointer to its source.

   When a temporary document names a constraint that should be enforced in code, configuration, schema, or tests, verify the existing enforcement. Preserve an established normative constraint as intent and report any enforcement gap instead of claiming that implementation conforms. Treat an unaccepted constraint as an unresolved decision.

3. Update adapters and authority links.

   Make existing adapters link to relevant canon with a use condition for each file. Point authoritative links only to canon, protected references, or stable executable sources. When an unknown document could otherwise appear authoritative, identify it as unknown and non-authoritative in the nearest maintained index or adapter without presenting it as guidance. Keep adapters compact and preserve the repository's existing agent ecosystems.

4. Mark planning sediment in place.

   Preserve each temporary or stale document at its current path and retain its content and existing metadata. Add or update the repository-appropriate status marker from the preservation reference. Preserve `unknown` documents without modification and report them for human judgment.

5. Reconcile the preserved documentation surface.

   Verify status markers, canonical ownership, executable authority, adapter links, and references among maintained documentation. Make canon the destination for non-derivable intent and executable sources the destination for mechanics while leaving preserved material available as explicitly non-authoritative context.

6. Report the result.

   Summarize changed canon files, adapter changes, temporary and stale documents marked, protected and unknown documents left intact, authority-link cleanup, and facts requiring human judgment.

## Completion

- Each durable meaning has one authoritative home, and active constraints are reconciled with source.
- Temporary and stale documents retain their content with accurate non-canonical markers. Protected material remains intact and unknown documents remain unmodified.
- Adapters and maintained links identify valid authoritative sources and when to read them. Report unresolved facts and enforcement gaps.
