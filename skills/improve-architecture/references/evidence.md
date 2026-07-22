# Architecture Evidence

Use this reference to select evidence and coverage for the repository under audit.

## Repository-type inventory

For runtime applications, inspect:

- application and package boundaries;
- entry points and delivery mechanisms;
- dependency manifests and framework configuration;
- representative business workflows;
- business logic placement;
- persistence and external-service boundaries;
- tests and test organization;
- accepted architecture records, engineering documentation, and canon.

For libraries and packages, inspect public interfaces, compatibility guarantees, package isolation, dependency direction, release artifacts, examples, and validation boundaries.

For documentation or configuration repositories, inspect schemas, generation flow, reference ownership, validation, and consumer boundaries.

For infrastructure repositories, inspect deployment units, state boundaries, provider dependencies, environment promotion, secrets, rollback paths, and validation.

For monorepos, identify each application or package boundary, shared packages, dependency constraints, build orchestration, and cross-package contracts.

## Evidence precedence

Use evidence in this order:

1. User-stated constraints and decisions.
2. Explicit architecture documentation and accepted decision records.
3. Adopted framework conventions.
4. Dependency direction and runtime behavior.
5. Recurring repository patterns.

A repeated pattern is evidence, not proof of intent. Record contradictions between stronger and weaker sources.

## Rule confidence

- `Established`: stated by the user or an accepted canonical source.
- `Inferred`: supported by at least two independent kinds of evidence without material counterexamples.
- `Proposed`: a potentially useful direction that still requires a maintainer decision.

Base conformance findings only on established or inferred rules. Route proposed rules to open decisions.

## Coverage

For a large repository, inspect at least one end-to-end path through every major application or bounded area, then use targeted searches to test whether each observed pattern holds elsewhere. Record inspected paths, sampled areas, excluded areas, and residual risk.
