---
name: canonize
description: Canonize durable non-derivable project intent and remove planning sediment after active constraints are reconciled with executable sources.
---

# Canonize

Maintain a small, trusted canon in `docs/canon/`. Let code, configuration, schemas, and tests own mechanically discoverable truth. Treat root agent files as adapters and ADRs, plans, specs, proposals, and handoffs as source material whose active constraints must be reconciled before removal.

Use `$canonize-mark` when the user wants non-canonical documents preserved in place.

## Workflow

1. Inventory and classify the documentation surface.

   Read repository instructions, root documentation, `docs/` indexes, and every relevant in-scope Markdown file. Inspect source structure, package files, routes, tests, and configuration only as needed to ground documentation claims. Exclude generated tool state, vendored documentation, dependency checkouts, build output, and nested projects outside the requested scope.

   Classify every in-scope document:

   - `canonical`: maintained current truth future agents should trust.
   - `adapter`: agent-specific wiring that points to canon.
   - `protected-reference`: maintained operational, contribution, security, policy, or license material.
   - `temporary`: active plans, drafts, specs, ADRs, handoffs, investigations, or proposals.
   - `stale`: obsolete planning or generated documentation whose active constraints are obsolete or already absorbed.
   - `unknown`: potentially useful material that cannot yet be classified or source-grounded.

   Treat ADR and decision-record files as temporary or stale source material unless the user explicitly requests historical preservation.

   For each candidate claim, identify whether its proper authority is executable—code, configuration, schema, test, or generated output—or prose canon.

   Completion criterion: every relevant root or `docs/` Markdown file has one classification; every candidate claim has an authoritative home, repository source, or uncertainty marker; every excluded file is accounted for by an explicit scope rule.

2. Normalize the canon model.

   Before creating or restructuring canon files, read [references/canon-model.md](references/canon-model.md) for file ownership, trajectory rules, writing rules, metadata, and adapter consumption order. Prefer a coherent existing `docs/canon/` convention; otherwise use the model in that reference.

   Completion criterion: language canon lives in `docs/canon/language.md`, each durable meaning has one prose or executable home, product truth and trajectory do not compete, and no root adapter is required to own canon.

3. Reconcile active constraints.

   Preserve vocabulary, intent, invariants, boundaries, non-goals, and rationale that executable sources cannot express safely. Remove mechanically discoverable duplication from canon or replace it with a stable pointer to its source.

   When a temporary document names a constraint that should be enforced in code, configuration, schema, or tests, verify the existing enforcement. Preserve an established normative constraint as intent and report any enforcement gap instead of claiming that implementation conforms. Treat an unaccepted constraint as an unresolved decision.

   Completion criterion: every temporary or stale document has been checked for durable intent and active constraints; each meaning has one authoritative home; canon contains non-derivable current intent rather than repository inventory or planning history.

4. Update adapters.

   Make existing adapters point to the canon read order. Create an adapter only when repository convention or the user requires one. Keep legacy `CONTEXT.md` files compact; `docs/canon/language.md` remains the owner of language canon.

   Completion criterion: every adapter points to existing canonical files or authoritative executable sources, duplicates no canon at length, and contains no authoritative link to temporary, stale, or unknown material.

5. Remove absorbed sediment.

   For each document classified `temporary` or `stale`, verify that its active constraints were reconciled with their authoritative prose or executable home, then remove the exact file and any now-empty ADR or decision-record directory. Preserve canonical files, adapters, protected references, source files, tests, generated tool state, out-of-scope nested projects, and `unknown` documents. Report every preserved unknown.

   Completion criterion: every temporary or stale document is removed after reconciliation; every unknown and protected document remains; no removed document can continue steering implementation through an authoritative link.

6. Reconcile references and canon ownership.

   Search maintained documentation and adapters for the paths and titles of removed files. Rewrite stale links, remove competing canonical statements, and verify the canon file metadata and ownership rules from the reference.

   Completion criterion: no removed path or title remains as a live reference; every durable meaning has one prose or executable owner; every canonical file changed in this run was genuinely reviewed.

7. Report the result.

   Summarize changed canon files, adapter changes, removed sediment, protected and unknown documents left in place, reference cleanup, and facts requiring human judgment.

   Completion criterion: the user can account for every in-scope document and distinguish trusted canon from preserved uncertainty.
