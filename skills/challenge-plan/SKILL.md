---
name: challenge-plan
description: Stress-test an existing plan when the user requests an adversarial review, pressure test, red-team review, or council.
disable-model-invocation: true
---

# Challenge Plan

Challenge a completed plan against the user's intent and consequential uncertainties. Operate read-only unless the user explicitly asks to revise the plan. Do not manufacture objections or perform a fixed number of review passes.

## Workflow

1. Establish the target and purpose.

   Identify the plan, the requested focus, intended outcomes, relevant constraints, and evidence needed to evaluate it. If there is no reviewable plan, explain what is missing and recommend `$plan-work`. If the user names no focus, identify the few assumptions or failure modes that could materially change the approach, sequencing, recovery, or acceptance.

2. Test consequential claims.

   Trace intended outcomes back to the request to catch omitted workflows or misinterpreted requirements. For material uncertainties, prefer a safe, isolated probe, contract check, rehearsal, or examination of real behavior over speculation. Do not run unsafe probes or mutate reviewed files during a read-only challenge. Consider failure, security, accessibility, usability, operational, and maintainability concerns where relevant, including concerns a test alone may not settle.

   Where a consequential question remains uncertain and a shared blind spot could be costly, seek focused independent scrutiny when available and authorized. Supply the specific question, evidence, and constraints; ask for the smallest useful discriminator or amendment. Respect an explicitly requested council, subject to available delegation and authorization, but do not require a fixed number of advisors or anonymized cross-review. If independent scrutiny is unavailable, state that limitation rather than simulating it.

3. Synthesize and report.

   Keep concerns grounded in evidence or a clearly labeled assumption, a credible effect, and a useful amendment or check. Reject duplicate, speculative, or low-impact objections. Say when no material concern was found; absence of a finding is not proof of correctness.

   Give a `Ready`, `Revise`, or `Replan` verdict, followed by the material findings, recommended checks or amendments, evidence used, and consequential gaps. Record unresolved user-owned decisions. Recommend `$do-work` when ready, `$plan-work` for material revisions, or `$shape-work` for unresolved product decisions; do not invoke the next skill automatically.

## Completion

- The plan and intended outcomes are grounded in relevant evidence.
- Material concerns name their impact and an actionable amendment or discriminator.
- The verdict distinguishes verified behavior from assumptions and states consequential gaps.
