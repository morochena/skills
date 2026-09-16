---
name: create-verification-skill
description: Create and prove a project-local verification skill that controls a web UI, CLI, desktop app, API, mobile app, or library through its real user surface.
license: MIT
---

# Create Verification Skill

Create a project-local `verify-<app>` skill that another agent can use without prior knowledge of the project. Ground every instruction in observed repository behavior and prove the generated skill before handoff.

Use the current workspace. Do not create a branch or pull request unless the user requests one.

## Workflow

1. Locate the output and check for an existing verifier.

   Read applicable repository instructions. Use the established project-local skill root when one exists. Otherwise, use `.agents/skills/`. Write one skill at `<skill-root>/verify-<app>/`; do not create duplicate copies for different agents.

   If a suitable verification skill already exists, stop and recommend `$maintain-verification-skill` unless the user explicitly requested replacement.

2. Interview the repository.

   Discover facts locally. Ask the user only for intent or access that the repository cannot supply.

   - **Surface:** Identify the primary user surface and note other important surfaces.
   - **Launch:** Find the documented local start or build command, required environment, ports, data, authentication, and readiness signal.
   - **Drive:** Prefer an existing Playwright or Cypress harness, PTY helper, command runner, debug interface, or HTTP client. Use a generic browser, PTY, or HTTP method only when the repository has no suitable harness.
   - **Observe:** Identify useful proof, such as screenshots, accessibility snapshots, terminal transcripts, response bodies, logs, exit codes, or persisted state.
   - **Isolate:** Find how to separate ports, data directories, profiles, and sessions. If concurrent instances are not safe, make the generated skill refuse to control an unowned instance.

   Do not write instructions for a checkout that you cannot build or start. Diagnose a broken baseline and report the blocker. You can add clearly named verification scaffolding inside the generated skill, but do not change product code as part of this workflow without separate user authorization.

3. Write the generated skill.

   Create `SKILL.md` with `name: verify-<app>` and a description that names the app, surface, and matching verification work. Create `agents/openai.yaml` with matching interface text. Keep automatic selection enabled by default for the project-local verifier. Add `policy.allow_implicit_invocation: false` only when the user requests an explicit-only verifier. `$do-work` and `$review-work` can also read the verifier as repository guidance when their scope affects a mapped user surface.

   Include these sections with project-specific commands and handles:

   - **Launch:** Give the exact start command, readiness check, and teardown method. For a short-lived CLI or TUI, build once and start each control run in an isolated PTY or terminal session.
   - **Doctor:** Give one read-only check that confirms the correct build, process, port, profile, data directory, and authentication state that matter for this app.
   - **Drive:** Give exact commands and stable selectors from the repository. Prefer roles, accessible names, data attributes, prompt text, route paths, and command flags over coordinates or tab order.
   - **Evidence:** Require the real user path. Capture the action and the result. Confirm important side effects from a second read-only view. Use mocks only at an existing production boundary. Verify what a dry-run or test mode does not change; do not trust its name.
   - **Cleanup:** Stop only processes and sessions that the verification run started. Remove its scratch state and preserve its evidence.
   - **Helpers:** Document the invocation of each owned helper script and make each script executable.

   Do not leave placeholders, invented selectors, untested commands, or hidden setup knowledge.

4. Seed the feature map.

   Read [references/feature-map.md](references/feature-map.md). Create `features/README.md` and one file for each of the three to five most important user-facing features that the repository shows. Use routes, commands, menus, help text, and product documentation as evidence.

   Record every known user entry point for each mapped feature. A successful check of one entry point does not prove the other entry points.

5. Prove the generated skill.

   Run the generated instructions from start to finish:

   1. Launch the app.
   2. Run the doctor check.
   3. Control one mapped feature through a real user path.
   4. Capture the required evidence.
   5. Run cleanup.
   6. Confirm that the evidence still exists.

   After each failed attempt, run the generated cleanup before the next attempt. Fix verification-skill instructions or owned helpers that fail, and repeat the affected checks.

6. Report the result.

   Report the generated skill path, primary surface, control method, feature-map coverage, proof that you ran, and any access or environment gap. Recommend `$maintain-verification-skill` for a later audit; do not suggest a fixed schedule unless the user asks.

## Completion

- The generated skill and feature map contain source-grounded commands, selectors, prerequisites, and observable results, with no hidden setup or placeholders.
- One mapped feature passes the documented launch, doctor, control, evidence, and cleanup path. No owned process or scratch state remains; evidence is preserved.
- Report the verifier path, mapped coverage, actual proof, and any access or verification gap.
