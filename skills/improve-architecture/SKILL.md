---
name: improve-architecture
description: Assess, document, or improve repository architecture through observed evidence, concise durable intent, bounded remediation, and executable guardrails.
---

# Improve Architecture

Make architectural intent explicit, compare implementation with that contract, and improve selected boundaries with evidence. Optimize for lower cognitive load and consistent decisions rather than pattern purity.

## Modes

- `assess`: when the user asks to assess, review, audit, or explain, remain read-only and report in chat.
- `document`: when the user asks to document architecture, write or update the concise contract. Keep audit findings in chat unless the user requests a report or a remediation program needs durable handoff.
- `improve`: when the user asks to improve, refactor, or enforce architecture, implement the selected bounded finding and add an executable guardrail when practical.

When an improve request does not select a boundary or finding, establish the evidence, present the highest-leverage choices, and get that material scope decision before changing production structure.

## Principles

- Treat architecture as a response to this system's constraints and adopted framework conventions.
- Prefer explicit repository decisions over imported opinions.
- Treat code, configuration, schemas, dependency graphs, and tests as primary evidence of current mechanics.
- Preserve intent and non-derivable constraints in prose; enforce testable boundaries in code, configuration, or tests when practical.
- Optimize dependency direction, boundaries, naming, and placement for consistent change.
- Distinguish accidental inconsistency from a justified local exception.
- Introduce an abstraction only when it removes more cognitive load than it creates.

## Workflow

1. Establish scope and evidence.

   Classify the repository and inspect its instructions, structure, representative behavior, tests, configuration, and architectural material. Run focused dependency queries, static checks, tests, traces, or other non-destructive probes when they can replace speculation with observed behavior. Before choosing coverage, read [references/evidence.md](references/evidence.md) for repository-type inventories, evidence precedence, rule confidence, and large-repository sampling.

   Completion criterion: every major application or bounded area has representative coverage; the assessment records what was inspected and excluded; every candidate rule is labeled `Established`, `Inferred`, or `Proposed` from concrete evidence.

2. Establish the architecture contract.

   Before choosing a contract path or writing rules, read [references/architecture-contract.md](references/architecture-contract.md). Build or validate a concise contract from established and inferred rules. Put proposed rules and unresolved choices in `Open Questions`.

   In `document` mode, create or update the selected contract. In `assess` mode, present the candidate contract in chat. In `improve` mode, update the contract only when the selected change alters durable intent. Report documentation drift when an existing contract conflicts with current dependencies, accepted decisions, or runtime behavior.

   Completion criterion: the contract path is explicit; every normative rule is testable and labeled by evidence strength; proposed rules create no conformance findings.

3. Test conformance.

   Trace representative behavior and dependencies across the contract's boundaries. Look for misplaced business rules, reversed or circular dependencies, parallel patterns, inconsistent domain representation, leaking infrastructure details, costly indirection, dependency magnets, brittle test boundaries, incomplete migrations, obsolete seams, and rules too vague to apply.

   Inspect enough call sites, tests, history, and counterexamples to distinguish violations from intentional exceptions. When cheap, turn a suspected violation into a reproducible dependency query, architecture test, lint rule, type check, or focused behavioral test. Group repeated instances under one architectural issue.

   Completion criterion: every suspected issue is confirmed by observable evidence against an established or inferred rule, recorded as an accepted exception, moved to an open decision, or discarded with contrary evidence.

4. Produce the mode-specific result.

   Before reporting findings, read [references/audit-report.md](references/audit-report.md) for the finding schema, severity definitions, ordering, and remediation requirements.

   - In `assess` mode, present findings in chat.
   - In `document` mode, write the contract and keep findings in chat unless a durable audit was requested or is necessary for a cross-session remediation program.
   - In `improve` mode, implement only the selected finding, verify it incrementally, and add an executable boundary check when its value exceeds its maintenance cost.

   Completion criterion: every reported or implemented finding cites its rule, concrete evidence, impact, target state, safe migration order, and verification; every production change is within the selected scope.

5. Reconcile the result.

   Verify that every finding maps to an established or inferred rule, proposed concerns live in open decisions, accepted exceptions remain explicit, and any refactoring order respects dependency and migration constraints. Run the original conformance signal, relevant regression checks, and documentation checks for changed durable intent.

   Completion criterion: executable behavior, contract, findings, exceptions, open decisions, and remediation order agree; the user can distinguish observed improvement from remaining proposals.
