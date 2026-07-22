# Architecture Contract

Use this reference to choose the contract path and create or validate its contents.

## Path selection

Choose the path in this order:

1. Use the path specified by the user.
2. Use an established architecture-specific repository convention.
3. When a broader canon system exists without a settled architecture home, treat the location as an open decision in dry-run mode and ask the user before writing a competing canonical file.
4. Otherwise use `docs/architecture.md`.

## Contract construction

When no contract exists, build it from established and inferred rules before auditing conformance. When one exists, validate its internal coherence and its fit with current dependencies, framework choices, accepted decisions, and runtime behavior.

Express uncertainty through evidence labels and `Open Questions`. Preserve useful framework defaults instead of recreating an opinionated framework inside a parallel architecture.

Use only applicable sections:

```md
# Architecture

## Design Philosophy
## System Context
## Applications and Major Boundaries
## Dependency Direction
## Business Logic
## Data and External Services
## Cross-Cutting Concerns
## Framework Conventions
## Testing Boundaries
## Exceptions and Tradeoffs
## Changing the Architecture
## Open Questions
```

Make each rule testable. Prefer:

> Controllers translate HTTP input and call application services.

over:

> Keep controllers thin.

Use short repository examples when they clarify placement or dependency direction. Keep transient audit observations in the audit report rather than the durable contract.
