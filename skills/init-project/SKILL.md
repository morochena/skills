---
name: init-project
description: Create or update a repository AGENTS.md with explicit lifecycle, compatibility, product precedent, long-term architecture, feature maturity, churn, and risk-matched verification rules. Use when initializing agent instructions for a project, replacing a generic AGENTS.md, or making project development conventions durable.
---

# Initialize Project

Create compact project instructions that preserve choices an agent cannot infer safely from the repository. Treat `$init-project` as an explicit setup command.

## Workflow

1. Inspect the instruction scope.

   Find every applicable `AGENTS.md` and repository instruction file. Read the root documentation, build metadata, and test configuration only as needed to identify established commands and conventions. Treat existing instructions as user-owned content. Update them in place; do not replace, weaken, or duplicate them.

   Completion criterion: the target instruction scope, existing rules, and any conflicts are known.

2. Establish the lifecycle.

   Use exactly one lifecycle value:

   - `pre-release`: no released product or external user depends on current behavior or stored data.
   - `released`: users or external consumers can depend on current behavior, interfaces, or stored data.

   Treat lifecycle as a user-owned fact. Never infer it from a version number, deployment file, or incomplete repository. If the user did not supply it and existing instructions do not state it, ask one focused question before writing.

   Completion criterion: one lifecycle value is confirmed and any conflicting compatibility rule is resolved.

3. Establish the verification model.

   Define baked level and churn as separate per-change classifications:

   - Baked level measures how settled the intended behavior is. It controls the amount of durable regression coverage.
   - Churn measures how likely the code or behavior is to change soon. It controls where tests attach and how closely they couple to the implementation.

   Do not infer either classification from the other. Stable behavior can have a high-churn implementation, and unsettled behavior can sit unchanged for a long time. Do not assign one baked level or churn value to the whole project. Require the implementing agent to classify each new or changed feature before choosing its verification strategy. Distinguish durable automated tests from temporary probes, smoke checks, type checks, and other evidence that an exploratory slice runs.

   Completion criterion: the instructions prevent both premature test maintenance and unverified implementation.

4. Write the project instructions.

   Read [references/agents-policy.md](references/agents-policy.md). Add its project profile, product precedent, architectural durability, and verification policies to the root `AGENTS.md`. Select only the confirmed lifecycle clause. Adapt headings to a clear existing structure, but preserve the policy meanings.

   Add other repository-specific rules only when they are durable, source-grounded, and useful to an agent. Prefer pointers to authoritative code or configuration over copied inventories. Do not add generic coding advice, speculative architecture, discoverable file lists, or unverified commands.

   Add a feature-specific maturity or churn value only when the user confirms that it is a durable default. If only one value is known, record only that value. Never derive churn from baked level or baked level from churn.

   Create a nested `AGENTS.md` only when a subproject needs different rules. State its scope and do not repeat inherited root rules.

   Completion criterion: the applicable instructions contain one explicit lifecycle flag, one matching compatibility policy, the product precedent rule, the architectural durability rule, and the complete maturity-based verification policy without conflicting or speculative guidance.

5. Check the result.

   Re-read the final instruction chain from root to the affected scope. Confirm that:

   - lifecycle is explicit and has one value;
   - compatibility guidance matches lifecycle;
   - product design starts from relevant established patterns;
   - production architecture fits the intended long-term design;
   - no stopgap remains that is meant to be replaced later;
   - baked level controls test depth;
   - churn controls test coupling;
   - high-consequence behavior still receives necessary coverage;
   - existing user instructions remain intact unless the user approved a change; and
   - every added project fact has a source.

   Report the selected lifecycle, the product precedent rule, the architectural durability rule, the verification policy, the files changed, and any rule that still needs a user decision.

   Completion criterion: another agent can choose a compatible implementation and proportionate verification strategy without guessing about project maturity.
