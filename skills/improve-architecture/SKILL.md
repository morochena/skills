---
name: improve-architecture
description: Establish, audit, and improve a repository's architectural consistency without imposing a universal architecture. Use when the user explicitly invokes $improve-architecture, asks to document how a codebase is structured, wants docs/architecture.md created or updated, requests an architecture audit, wants inconsistently applied patterns identified, or asks for a concrete refactoring roadmap grounded in the repository's own philosophy and framework conventions.
---

# Improve Architecture

## Overview

Make the repository's architectural intent explicit, compare the implementation with that intent, and produce an evidence-based remediation report. Optimize for lower cognitive load and consistent decisions rather than pattern purity.

When the user asks to improve or document the architecture, use write mode and write the architecture documentation and audit report. When the user asks only to assess, review, or explain, use dry-run mode: remain read-only and present the candidate contract and findings in chat. Do not refactor production code unless the user separately authorizes implementation.

## Principles

- Treat architecture as a response to this system's constraints, not a catalog of fashionable patterns.
- Prefer the repository's explicit decisions and established framework conventions over imported opinions.
- Minimize the complexity required to understand, change, test, and operate the system.
- Value consistent dependency direction, boundaries, naming, and placement more than superficial uniformity.
- Distinguish an accidental inconsistency from a justified local exception.
- Preserve useful framework defaults. Do not recreate Rails, Django, Laravel, or another opinionated framework inside a parallel home-grown architecture.
- Recommend a new abstraction only when it removes more cognitive load than it introduces.
- Treat duplication as evidence to investigate, not automatic proof that an abstraction is needed.

## Workflow

### 1. Establish scope and evidence

Read repository instructions and inspect the project before asking questions. First classify it as a runtime application, library/package, documentation or configuration repository, infrastructure repository, monorepo, or a combination. Inventory the boundaries that matter for that repository type.

For runtime applications, inspect:

- application and package boundaries;
- entry points and delivery mechanisms;
- dependency manifests and framework configuration;
- representative business workflows;
- domain or business logic placement;
- persistence and external-service boundaries;
- tests and test organization;
- architectural decision records, engineering docs, and relevant canon.

For libraries, packages, documentation, configuration, and infrastructure repositories, replace application-centric concepts with their equivalents. Inspect public interfaces, artifact or package isolation, metadata and schemas, generation or deployment flow, cross-package references, compatibility guarantees, and validation boundaries as applicable.

Use evidence in this order:

1. User-stated constraints and decisions
2. Explicit architecture documentation and accepted decision records
3. Opinionated framework conventions the project has adopted
4. Dependency direction and runtime behavior in the code
5. Recurring repository patterns

Do not mistake a frequently repeated accident for deliberate architecture. Note contradictions between these evidence sources. Classify each candidate rule in working notes:

- `Established`: stated by the user or an accepted canonical source.
- `Inferred`: supported by at least two independent kinds of evidence, such as a framework convention plus recurring code, without material counterexamples.
- `Proposed`: a potentially useful direction that still requires a maintainer decision.

Never create a non-conformance finding against a proposed rule.

For a large repository, inspect at least one end-to-end path through every major application or bounded area, then use targeted searches to test whether the observed pattern holds elsewhere. Record what the audit covered and what it did not.

### 2. Establish the architecture contract

Choose the contract path explicitly:

1. Honor a path specified by the user or an existing architecture-specific repository convention.
2. If the repository has a broader canon system but no settled architecture path, record the location as an open decision in dry-run mode. In write mode, ask the user to choose before creating a competing canonical file unless their request already names the path.
3. Otherwise, use `docs/architecture.md`.

If the document does not exist, build a candidate contract from established and inferred rules before auditing. In write mode, create it. In dry-run mode, present it in chat without modifying files. Describe the system that maintainers intend to have, but do not invent certainty. Put proposed rules and unresolved choices in `Open Questions`; do not phrase them as current requirements.

If the document exists, read it as the contract under validation. Check whether it is internally coherent and still matches current dependencies, framework choices, and accepted decisions. Do not silently rewrite it merely to make existing code appear compliant; report documentation drift when the document is stale or ambiguous.

Keep `docs/architecture.md` durable and concise. Include only applicable sections:

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

Make rules testable. Prefer "controllers translate HTTP input and call application services" over "keep controllers thin." Include short concrete repository examples where they clarify placement or dependency direction.

### 3. Audit conformance

Trace dependencies and representative behavior across boundaries. Look for:

- business rules placed in delivery, persistence, view, or transport code contrary to the contract;
- dependency direction violations and circular dependencies;
- parallel patterns solving the same class of problem without a documented reason;
- framework conventions followed in one area and bypassed in another;
- domain concepts represented inconsistently across modules;
- boundaries that leak persistence, transport, vendor, or infrastructure details;
- abstractions whose indirection costs more than they clarify;
- shared modules that have become unrelated dependency magnets;
- tests coupled to implementation details or unable to exercise business behavior at the intended boundary;
- obsolete compatibility layers, incomplete migrations, and abandoned architectural seams;
- documented rules that are too vague to apply consistently.

For every suspected issue, inspect enough call sites and history or tests, when useful, to distinguish a violation from an intentional exception. Do not report stylistic preference as architectural non-conformance.

### 4. Write the audit report

Use `docs/architecture-audit.md` unless the user specifies another path. In write mode, write the report there. In dry-run mode, present the report in chat without modifying files. Keep transient observations out of the architecture contract.

Use this structure:

```md
# Architecture Audit

## Executive Summary
## Contract and Scope
## What Is Consistent
## Findings
### ARCH-001: <concise title>
- Severity: High | Medium | Low
- Status: Confirmed | Probable | Needs decision
- Principle: <established or inferred rule from the architecture contract>
- Rule Source: Established | Inferred
- Evidence: <paths, symbols, and behavior>
- Impact: <maintenance, correctness, delivery, or operational cost>
- Recommendation: <specific target state>
- Sequence: <prerequisites and safe migration order>
- Verification: <how to know the inconsistency is resolved>

## Cross-Cutting Refactoring Order
## Accepted Exceptions
## Open Decisions
## Audit Coverage and Residual Risk
```

Order findings by architectural leverage and risk, not by ease of cleanup. Group repeated instances under one finding rather than producing a long lint-style list. Cite concrete paths and symbols; include line numbers only when they are stable and useful.

Use severity consistently:

- `High`: The inconsistency creates a credible correctness, security, data, availability, or system-wide change-safety risk.
- `Medium`: The inconsistency recurs across a meaningful boundary, creates competing patterns, breaks package or deployment expectations, or materially raises change cost.
- `Low`: The inconsistency is localized and creates limited cognitive or maintenance cost without a broader risk.

Recommendations must state a target state and an incremental migration path. Call out changes that should be performed together so a partial refactor does not create a third competing pattern.

### 5. Reconcile the result

Before finishing:

- verify every finding maps to an established or inferred architecture rule;
- remove findings based only on personal taste;
- move concerns based on proposed rules into open decisions rather than findings;
- identify accepted exceptions rather than forcing false uniformity;
- make the report's refactoring order compatible with dependency and migration constraints;
- run relevant documentation checks or repository validation;
- summarize files written, major conclusions, audit coverage, and unresolved decisions.

If implementation is authorized, agree on the findings in scope before changing production code. Apply the roadmap incrementally and update both documents as decisions become durable.
