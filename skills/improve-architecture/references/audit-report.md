# Architecture Audit Report

Use this reference to structure and prioritize conformance findings.

## Report structure

Use `docs/architecture-audit.md` unless the user specifies another path.

```md
# Architecture Audit

## Executive Summary
## Contract and Scope
## What Is Consistent
## Findings
### ARCH-001: <concise title>
- Severity: High | Medium | Low
- Status: Confirmed | Probable | Needs decision
- Principle: <established or inferred contract rule>
- Rule Source: Established | Inferred
- Evidence: <paths, symbols, and behavior>
- Impact: <maintenance, correctness, delivery, or operational cost>
- Recommendation: <specific target state>
- Sequence: <prerequisites and safe migration order>
- Verification: <observable completion test>

## Cross-Cutting Refactoring Order
## Accepted Exceptions
## Open Decisions
## Audit Coverage and Residual Risk
```

## Severity

- `High`: credible correctness, security, data, availability, or system-wide change-safety risk.
- `Medium`: recurring boundary inconsistency, competing patterns, broken package or deployment expectations, or material change cost.
- `Low`: localized cognitive or maintenance cost without broader risk.

## Finding quality

Order findings by architectural leverage and risk. Group repeated instances under one root finding. Cite concrete paths and symbols; use line numbers only when stable and useful.

Each recommendation states a target state and incremental migration path. Identify changes that must move together so partial remediation cannot create another competing pattern.
