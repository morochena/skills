# Default Project Policy

Use the confirmed lifecycle clause and concise verification guidance. Adapt them to established project rules. Do not copy these authoring instructions into `AGENTS.md`.

## Project Profile

- Lifecycle: `<pre-release | released>`

### Pre-release Compatibility

- Prefer the target design and update affected in-repository callers together. Remove obsolete paths instead of adding compatibility layers for development-only behavior.
- Preserve development data when the user requests it or an established project rule requires it.

### Released Compatibility

- Preserve externally visible behavior and user data unless the user has authorized a specific compatibility, migration, or rollout decision.
- Give a required transition an owner, a safe migration path, and a removal condition for temporary compatibility code.

## Verification

- Match checks and durable test coverage to changed behavior and regression cost. Inspect existing coverage before adding tests. Use temporary probes for unsettled behavior when they provide the needed evidence.
- Keep required coverage for security, permissions, money, user data, data integrity, and irreversible effects. Preserve accepted regression contracts.
- Complete required checks. Reuse passing results that cover the final code and environment. Repeat or expand checks only when a change invalidates a result, a failure occurs, or a material risk remains uncovered.

Add exact local check commands only after confirming them. State that local checks may run and retry without further approval only when their use of disposable state and lack of production effects are established facts.

## Optional Project Rules

Include these only when requested or established by project decisions. Preserve existing adopted meanings unless the user authorizes a change.

- **Product precedent:** For unresolved product or interaction design, consult relevant established patterns and explain material departures. Skip research for settled designs and local maintenance.
- **Architectural durability:** Choose a simple design that fits the intended architecture. Use a disposable probe for unresolved feasibility. Give any necessary temporary production stage an explicit target and removal condition.

For projects that need a detailed test investment model, use [verification-depth.md](verification-depth.md). Load it only when maturity or expected change affects the verification decision.
