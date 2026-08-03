# AGENTS.md Policy Blocks

Use these blocks when `$init-project` creates or updates root project instructions. Select one lifecycle clause. Keep the verification policy for both lifecycle values.

## Project Profile

- Lifecycle: `<pre-release | released>`

### Pre-release Compatibility

Use when `Lifecycle` is `pre-release`:

- Do not preserve backward compatibility. Remove obsolete paths instead of adding compatibility layers, fallbacks, aliases, dual writes, or migrations.
- Prefer the clean target design over a staged transition. Replace old interfaces and update all in-repository callers in the same change.
- Do not preserve development-only data unless the user asks for it.

### Released Compatibility

Use when `Lifecycle` is `released`:

- Preserve externally visible behavior and user data by default.
- Do not remove or change a public interface without an explicit compatibility, migration, or rollout decision.
- When a compatibility layer or migration is necessary, define its owner, removal condition, and safe transition path. Do not keep it indefinitely by default.

## Product Precedent

Before you design a product, interaction, or workflow solution, study how established products solve the same problem. Use proven patterns, terms, and conventions as the default. Create a new approach only when project constraints or a clear product benefit justify the difference.

State which products or patterns informed the design and which parts you adopted. If you depart from an established pattern, state the reason. Skip this study for local maintenance work and for work that already has a settled design.

## Architectural Durability

Make production architecture decisions for the intended long-term design. Do not accept a stopgap that only works for now and is meant to be replaced later.

Choose the simplest design that can remain in place. Long-term design does not mean speculative abstractions, unused extension points, or features outside the current scope.

When uncertainty blocks a durable decision, use a disposable probe outside the production path and remove it after it answers the question. Do not let probe structure become production architecture. A released system can require migration stages, but each stage must move directly toward the target design and have an explicit removal condition.

## Feature Maturity And Verification

Before implementation of a new or changed feature, classify it on both axes:

- Baked level: `1` (unbaked), `2` (moderately baked), or `3` (very baked).
- Churn: `high`, `medium`, or `low`.

Baked level sets test depth:

- Level 1 — unbaked: The behavior is exploratory or unsettled. Do not add durable automated regression tests for it. Use only the minimum smoke check, type check, manual check, or disposable probe needed to show that the slice works.
- Level 2 — moderately baked: The main contract is settled, but details can change. Add a small number of high-level contract or integration tests for the stable behavior and critical failure path. Avoid exhaustive variants and tests of internal structure.
- Level 3 — very baked: The behavior is stable and its regression cost matters. Add broad regression coverage for main paths, important edge cases, failure and recovery behavior, and integration boundaries.

Churn sets test coupling:

- High churn: Test only stable observable behavior and established boundaries. Avoid snapshots, call-count assertions, and implementation-detail tests.
- Medium churn: Test public behavior and the main integration seams. Use focused unit tests where the units are stable.
- Low churn: Add detailed tests when they improve regression detection and remain clear to maintain.

Use baked level to decide how much to test. Use churn to decide where to test. When the signals differ, apply both. For example, a very baked feature with high implementation churn needs broad coverage at stable external boundaries, not broad coverage of its internals.

Treat the two axes as independent. Never use stable behavior as proof of low churn. Never use frequent code changes as proof that behavior is unbaked.

These classifications do not remove the need to verify a change. They control durable regression investment. Always test established behavior whose failure can affect security, permissions, money, user data, data integrity, or irreversible side effects. Keep tests already required by an accepted specification or regression contract.

State the selected baked level and churn, with a short reason, in the implementation ledger or plan. If the classification is not supplied, infer it from settled project evidence. Ask the user only when the choice would materially change scope, risk, or acceptance.
