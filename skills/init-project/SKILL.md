---
name: init-project
description: Create or revise AGENTS.md when a project needs durable agent instructions or an explicit lifecycle policy.
disable-model-invocation: true
---

# Initialize Project

Create compact project instructions that preserve choices an agent cannot infer safely from the repository. Treat `$init-project` as an explicit setup command.

## Instruction Scope

Read applicable repository instructions. Inspect root documentation, build metadata, and test configuration only as needed to establish project facts and commands.

Preserve existing user rules unless the request or settled conversation authorizes their revision. Apply authorized changes in place without asking for the same permission again. Report any unresolved conflict that affects the requested result.

## Lifecycle

Record exactly one value:

- `pre-release`: no released product or external user depends on current behavior or stored data.
- `released`: users or external consumers can depend on current behavior, interfaces, or stored data.

Lifecycle is a user-owned fact. Use the request or existing instructions. If neither establishes it, ask one focused question before writing a lifecycle or compatibility policy. Continue independent inspection while the answer is pending. Do not infer lifecycle from version numbers or deployment files.

## Write the Instructions

Read [references/agents-policy.md](references/agents-policy.md) for the compact default policy. Select the confirmed lifecycle clause and adapt the verification guidance to known project commands and risks.

Include product precedent or architectural durability rules when the user requests them or existing project decisions establish them. Retain adopted rules unless their revision is authorized. Do not add a mandatory research phase or a general ban on temporary production designs to every project.

Use [references/verification-depth.md](references/verification-depth.md) only when feature maturity or expected change would materially affect test investment, or the user requests that model. Keep detailed classifications out of the default instructions. Do not remove an existing classification policy without authorization.

Add only durable, source-grounded project constraints. Link to authoritative code, configuration, and documents with a condition for reading each source. Omit copied inventories, generic coding advice, unverified commands, and rules that require reading all project documents before every edit.

Create nested `AGENTS.md` files only when a subproject needs different rules. State their scope and avoid repeating inherited instructions.

## Completion

- The applicable instruction chain has one confirmed lifecycle and a matching compatibility policy.
- Project facts and commands have sources; existing rules are preserved or changed within the user's authorization.
- Verification matches behavioral risk, reuses valid results, and retains required coverage for high-consequence behavior.
- Report changed files, selected policies, and unresolved decisions. Continue other work already authorized by the user.
