---
name: canonize
description: Canonize project documentation and remove planning sediment. Use when the user wants to create, update, normalize, audit, or clean durable project docs; delete ADRs, plans, specs, milestones, roadmaps, proposals, or stale docs after extracting active constraints; maintain docs/canon/language.md, product.md, trajectory.md, system.md, and engineering.md; update agent adapters when present; or separate product trajectory from backlog.
---

# Canonize

Maintain a small, trusted canon for a codebase. Canon captures durable product truth, domain language, system shape, and engineering rules that should guide future agent sessions.

Canon lives in `docs/canon/` by default. Root agent files such as `AGENTS.md`, `CLAUDE.md`, and `CONTEXT.md` are adapters: they help specific agent ecosystems find the canon, but they do not own it.

The skill turns scattered notes into present-tense constraints. ADRs are source material, not canon. Preserve historical decision logs only when the user explicitly asks for history to remain.

## Workflow

1. Inspect the repo's existing instructions and docs.

   Read root agent docs first: `AGENTS.md`, `CLAUDE.md`, `README.md`, `CONTEXT.md`, `CONTEXT-MAP.md`, and `docs/` indexes when present. Then inspect source structure, package files, routes, tests, and configuration only as needed to ground doc claims.

   Exclude generated tool state, vendored package docs, dependency checkouts, build output, and nested project docs unless the user asks to canonize that nested project.

   Completion criterion: every broad claim you plan to write has a source in the repo or is marked uncertain, and out-of-scope docs are not rewritten or deleted.

2. Classify documentation.

   Classify relevant markdown as:

   - `canonical`: maintained current truth future agents should trust.
   - `adapter`: agent consumption wiring, such as `AGENTS.md`, `CLAUDE.md`, root `CONTEXT.md`, `CONTEXT-MAP.md`, or `docs/agents/domain.md`.
   - `protected-reference`: maintained operational reference, such as deployment setup, integration setup, issue tracker configuration, contribution policy, security policy, or license text.
   - `temporary`: active plans, drafts, specs, ADRs, handoffs, investigation notes, proposals, or issue work.
   - `stale`: old planning, ADRs, or generated docs whose active constraints are obsolete or already rewritten into canon.
   - `unknown`: possibly useful, but not source-grounded enough to canonize.

   Classify ADRs, decision records, plans, specs, milestones, spikes, proposals, and handoffs as planning sediment even when repo instructions mention them or a directory name sounds official.

   Completion criterion: every relevant root or `docs/` markdown file you touched, referenced, or relied on has a classification, and every ADR-like file is classified as canonizable sediment unless the user explicitly requested preservation.

3. Normalize the canon set.

   Prefer an existing `docs/canon/` convention when it is coherent. Otherwise use this layout:

   ```txt
   docs/canon/language.md
   docs/canon/product.md
   docs/canon/trajectory.md
   docs/canon/system.md
   docs/canon/engineering.md
   ```

   For larger or multi-domain repos, add only what the structure proves necessary, such as `docs/canon/<context>/language.md` or `docs/canon/<context>/system.md`.

   Completion criterion: language canon lives in `docs/canon/language.md`, each durable meaning has one canonical home, and no root file is required for canon.

4. Rewrite sediment into canon.

   Convert history, deliberation, and wishes into active truth:

   - "We chose Clerk after comparing auth providers" -> "The app uses Clerk for authentication."
   - "We moved billing logic out of components because it got messy" -> "Billing rules belong in the billing domain layer. UI components display billing state but do not calculate billing eligibility."
   - "Maybe add team analytics later" -> omit it, unless it can be rewritten as a current trajectory theme grounded by active work.

   Convert ADRs into current constraints, not decision history:

   - "ADR 0012: We chose local repository checkouts over GitHub API ingestion" -> "Repository file ingestion uses local checkouts. GitHub may provide links or credentials, but it is not the primary file ingestion path."
   - "Superseded by ADR 0022" -> keep only the current rule from ADR 0022 and remove both historical record files when fully absorbed.

   Completion criterion: canon is present tense, compact, source-grounded, and free of planning language except for the constrained trajectory rules below.

5. Update adapters.

   Update existing adapters so they point at the canon read order instead of owning canon. Create a new adapter only when repo convention clearly expects one or the user asks for one.

   If root `CONTEXT.md` exists for legacy workflow compatibility, keep it as a compact adapter or mirror of `docs/canon/language.md`. When both files exist, `docs/canon/language.md` owns the language canon.

   Completion criterion: adapters make `docs/canon/` easy to consume, do not duplicate canon at length, and do not point to deleted docs.

6. Remove non-canon docs.

   Delete temporary and stale markdown artifacts after any durable facts have been rewritten into canon. This is the default cleanup behavior for planning sediment.

   Delete ADRs and decision-record directories by default, including `docs/adr/**`, `docs/adrs/**`, and `docs/decisions/**`, after their active constraints are represented in `docs/canon/*`.

   Preserve protected docs: root agent instructions, root README files, licenses, security policies, contribution guides, canonical docs, maintained operational references, adapters, source files, tests, generated tool state, and out-of-scope nested project docs. Preserve `unknown` docs and report why they were not canonized.

   Completion criterion: every temporary or stale doc is removed or reported as unknown; every ADR-like file is removed unless the user explicitly requested preserved history; none can silently steer future implementation through canon links, adapter links, or ambiguous status.

7. Self-check references.

   Search canon and adapters for paths and titles of deleted docs. Remove or rewrite stale references so future agents cannot follow a deleted planning artifact.

   Completion criterion: no deleted doc path is still referenced from canon or adapter docs.

8. Report the result.

   Summarize changed canon files, adapter changes, non-canon artifacts removed, protected or unknown docs left in place, deleted-reference cleanup, and facts left uncertain.

   Completion criterion: the user can tell what is trusted canon now and what still needs human judgment.

## Canon Files

`docs/canon/language.md` is language canon:

- Domain terms
- Product terms
- User roles
- Business concepts
- Terms with codebase-specific meaning
- Avoided terms and naming boundaries

`docs/canon/product.md` is product canon:

- North Star
- Current Product
- Product Boundaries
- Non-Negotiables

`docs/canon/trajectory.md` is product trajectory:

- Active Direction
- Directional Boundaries
- Review Rule

`docs/canon/system.md` is the current system model:

- Application architecture
- Major modules
- Data flow
- Runtime boundaries
- External services
- Persistence model
- Auth and permission model
- Important invariants

`docs/canon/engineering.md` is engineering canon:

- Code organization conventions
- Testing strategy
- API conventions
- UI conventions
- Error handling conventions
- Naming conventions
- Dependency rules
- Common commands

Use a header on canon files when the repo has no stronger convention:

```md
---
status: canonical
last_reviewed: YYYY-MM-DD
scope: project
---
```

Update `last_reviewed` only when you actually verify or change the file.

## Product Trajectory

Always create or update `docs/canon/trajectory.md`. Product direction lives there, not in `docs/canon/product.md`.

`docs/canon/product.md` owns the North Star, current product, product boundaries, and non-negotiables. `docs/canon/trajectory.md` owns active direction. If product.md already has a `Current Direction` section, move that content into trajectory.md and leave product.md focused on current product truth.

Trajectory contains:

- The 1-3 active product themes guiding work
- Directional boundaries: what the active direction does not imply
- A review rule that tells future agents to remove backlog-like content

Trajectory does not contain:

- Task lists
- Feature backlogs
- Dates unless externally committed
- Speculative features
- Abandoned ideas
- "Maybe" sections
- Implementation notes

Phrase future-leaning ideas as current direction or boundaries. If a sentence says "may", "maybe", "future", or "later", rewrite it into active direction or remove it unless it defines a boundary.

Rewrite desired features as direction, not instructions:

```md
# Product Trajectory

## Active Direction

The product is moving toward small-team collaboration. Near-term work should make shared ownership, visibility, and handoff clearer.

This does not imply building a full enterprise workspace model.

## Review Rule

If this document starts looking like a backlog, delete the backlog and keep only the direction.
```

Completion criterion: `docs/canon/trajectory.md` exists, contains active direction rather than a backlog, and product.md no longer carries a competing `Current Direction` section.

## Writing Rules

Canon is:

- Present tense
- Current-state oriented
- Specific
- Source-grounded
- Compact
- Free of speculation
- Free of decision-history prose

Prefer active constraints:

```md
Mutations use server actions by default. Use API routes when an endpoint must support non-React clients.
```

Avoid historical rationale in canon:

```md
We decided to use server actions after comparing them with API routes.
```

## Agent Consumption Rule

Agents should read canon before broad implementation work:

1. `docs/canon/language.md`
2. `docs/canon/product.md`
3. `docs/canon/trajectory.md`
4. `docs/canon/system.md`
5. `docs/canon/engineering.md`

Adapters such as `AGENTS.md`, `CLAUDE.md`, root `CONTEXT.md`, `CONTEXT-MAP.md`, and `docs/agents/domain.md` may mirror or point to this order for specific agent ecosystems.

Treat other markdown as non-canonical unless canon or repo instructions explicitly point to it.

## Success Criteria

The skill is working when:

- The repo has fewer docs and fewer trusted docs.
- Canon is stable across future agent sessions.
- Language canon lives in `docs/canon/language.md`.
- Product trajectory lives in `docs/canon/trajectory.md`.
- Adapters point at canon rather than owning canon.
- Agents use the same product and domain language as the codebase.
- Stale plans are removed by default and cannot steer implementation.
- Important decisions survive as current constraints, not historical artifacts.
- No deleted doc path is still referenced from canon or adapters.
