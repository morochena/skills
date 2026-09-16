# Verification Depth

Use this model when feature maturity or expected change materially affects durable test investment, or the user requests these classifications. Apply it to the affected feature, not the entire project.

## Independent Axes

**Baked level** measures how settled the intended behavior is. It controls coverage depth:

- `1` — exploratory: use the minimum smoke check, type check, manual check, or disposable probe needed to prove the slice works. Defer durable regression tests for unsettled behavior unless required below.
- `2` — partly settled: protect stable contracts and critical failure paths with a small number of contract or integration tests.
- `3` — settled: cover important main paths, edge cases, failures, recovery, and affected integration boundaries.

**Churn** measures how likely the code or behavior is to change soon. It controls test coupling:

- `high`: test stable observable behavior and established boundaries. Avoid snapshots, call-count assertions, and tests of internal structure.
- `medium`: test public behavior and integration boundaries. Use unit tests where the units are stable.
- `low`: add detailed tests where they improve regression detection and remain clear to maintain.

Do not infer one axis from the other. Settled behavior can have an implementation that changes frequently; unsettled behavior can remain unchanged for a long time.

## Apply the Model

Inspect existing coverage and add tests only for meaningful gaps or explicit requirements. These classifications never remove required checks or coverage for security, permissions, money, user data, data integrity, or irreversible effects. Preserve accepted regression contracts.

Infer classifications from settled project evidence. State them briefly when they change the verification choice. Ask the user only if a missing decision would materially change scope, risk, or acceptance. Record a durable feature default only when the user has confirmed it.
