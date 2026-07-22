---
name: improve-architecture
description: Establish an architecture contract and audit repository conformance against it.
---

# Improve Architecture

Make architectural intent explicit, compare implementation with that contract, and produce an evidence-based remediation order. Optimize for lower cognitive load and consistent decisions rather than pattern purity.

## Modes

- `write`: when the user asks to improve or document architecture, write the contract and audit report.
- `dry-run`: when the user asks only to assess, review, or explain, remain read-only and present the candidate contract and findings in chat.

Keep production code unchanged until the user separately authorizes selected findings for implementation.

## Principles

- Treat architecture as a response to this system's constraints and adopted framework conventions.
- Prefer explicit repository decisions over imported opinions.
- Optimize dependency direction, boundaries, naming, and placement for consistent change.
- Distinguish accidental inconsistency from a justified local exception.
- Introduce an abstraction only when it removes more cognitive load than it creates.

## Workflow

1. Establish scope and evidence.

   Classify the repository and inspect its instructions, structure, representative behavior, tests, configuration, and architectural material. Before choosing coverage, read [references/evidence.md](references/evidence.md) for repository-type inventories, evidence precedence, rule confidence, and large-repository sampling.

   Completion criterion: every major application or bounded area has representative coverage; the audit records what was inspected and excluded; every candidate rule is labeled `Established`, `Inferred`, or `Proposed` from concrete evidence.

2. Establish the architecture contract.

   Before choosing a contract path or writing rules, read [references/architecture-contract.md](references/architecture-contract.md). Build or validate a concise contract from established and inferred rules. Put proposed rules and unresolved choices in `Open Questions`.

   In write mode, create or update the selected contract. In dry-run mode, present the candidate contract in chat. Report documentation drift when an existing contract conflicts with current dependencies, accepted decisions, or runtime behavior.

   Completion criterion: the contract path is explicit; every normative rule is testable and labeled by evidence strength; proposed rules create no conformance findings.

3. Audit conformance.

   Trace representative behavior and dependencies across the contract's boundaries. Look for misplaced business rules, reversed or circular dependencies, parallel patterns, inconsistent domain representation, leaking infrastructure details, costly indirection, dependency magnets, brittle test boundaries, incomplete migrations, obsolete seams, and rules too vague to apply.

   Inspect enough call sites, tests, history, and counterexamples to distinguish violations from intentional exceptions. Group repeated instances under one architectural issue.

   Completion criterion: every suspected issue is either confirmed against an established or inferred rule, recorded as an accepted exception, moved to an open decision, or discarded with contrary evidence.

4. Produce the audit report.

   Before writing findings, read [references/audit-report.md](references/audit-report.md) for the report schema, severity definitions, ordering, and remediation requirements. Write `docs/architecture-audit.md` in write mode unless the user names another path; present the same structure in chat in dry-run mode.

   Completion criterion: every finding cites its rule, concrete evidence, impact, target state, safe migration order, and verification; the report states coverage and residual risk.

5. Reconcile the result.

   Verify that every finding maps to an established or inferred rule, proposed concerns live in open decisions, accepted exceptions remain explicit, and the refactoring order respects dependency and migration constraints. Run relevant documentation or repository checks.

   Completion criterion: the contract, findings, exceptions, open decisions, and remediation order agree with one another; the user can select implementation scope without rediscovering the audit.

When implementation is authorized, apply only the selected findings incrementally and keep the contract and audit report synchronized with durable decisions.
