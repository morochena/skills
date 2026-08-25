---
name: maintain-verification-skill
description: Audit and correct a project-local verification skill by checking every mapped feature against source and live user behavior.
license: MIT
disable-model-invocation: true
---

# Maintain Verification Skill

Keep a project-local verification skill and its feature map consistent with the current app. Cover every mapped feature from source and through a live user path. Do not turn every map bullet into a separate terminal task when one controlled state can prove several behaviors.

Use the current workspace. Do not create a branch or pull request unless the user requests one.

## Outcomes

Report one outcome:

- **clean:** Every mapped feature has source and live coverage. No useful correction is necessary.
- **changed:** One coherent working-tree change contains proven corrections to the verification skill, its map, or its owned helpers.
- **blocked:** Coverage could not finish, or a proven correction could not be applied safely. State the exact blocker.

## Edit Scope

Edit only the target verification skill directory: its `SKILL.md`, `agents/`, `features/`, and owned helper files. Do not edit product code. Treat behavior that differs from the map as one of these cases:

- Documentation drift: correct the map.
- Harness gap: correct the skill or an owned helper.
- Product gap: report it and do not hide it with a documentation change.

## Workflow

1. Locate the target.

   Search established project-local skill roots for a `verify-*` skill with launch, doctor, control, evidence, cleanup, and feature-map instructions. Include `.agents/skills/` in the search when the repository has no other configured root.

   If several candidates exist and the request does not identify one, ask which one to maintain. If no candidate exists, stop and recommend `$create-verification-skill`.

   Completion criterion: exactly one target directory and one feature map are in scope.

2. Check index hygiene.

   Read `features/README.md` and list its sibling feature files. Correct missing, extra, duplicate, and dead index entries. Do not add a generated inventory.

   Completion criterion: every feature file has one index entry, and every index entry resolves to one feature file.

3. Run the source pass.

   Explain how each mapped feature works from current source. Identify its source entry points, likely map drift, and one concise live-check recipe.

   When worker agents are available, give them independent read-only feature reviews in parallel. Use one feature per worker when useful, or use bounded batches when feature count exceeds useful concurrency. Workers must not control the app or edit files. Require this return shape from each worker: feature summary, source entry points, likely drift or none, and one live-check recipe.

   The coordinator must receive a source result for every feature. Merge overlapping recipes into as few app states as practical. Check cited drift before editing. Sweep recent user-facing source changes for a feature missing from the map, and require a concrete source path before adding it.

   Completion criterion: every mapped feature has source evidence, and every proposed addition or correction has a concrete source path.

4. Run the live pass.

   The coordinator owns all live control. Follow the target skill's launch model. Use one long-lived, isolated instance for a server or UI when the skill permits it. Use a fresh isolated session for each short-lived CLI or TUI control run.

   Exercise every mapped feature at least once. Maintain these rules during the pass:

   - Run doctor before the first control action, for each fresh session, and after any surprising failure. If doctor cannot see a bad UI state, reset to a known state or relaunch.
   - Preserve captured evidence through all cleanup steps and confirm it at the documented location.
   - Remove failed-run residue as soon as it is no longer useful. Do not stop an unrelated or user-owned instance.
   - When the doctor instruction has drifted, correct it within edit scope, restart only what the correction invalidated, and retry once.
   - Mark a path `verified-unreachable` only when you record the route that you tried and the concrete missing prerequisite, such as authentication, entitlement, platform, or external state.

   Run final teardown after the last control action and after all correction checks. Preserve evidence.

   Completion criterion: every feature is live-verified or has a precise unreachable result, the target leaves no owned process or scratch state, and evidence remains.

5. Triage and correct drift.

   Correct user-path descriptions that no longer match the app. Correct a control recipe or owned helper when the app works but the verifier cannot control it. Report broken product behavior as a product gap.

   Document the invocation of each changed helper, make executable helpers executable, and run every changed control or doctor path again before handoff.

   Completion criterion: every edit is supported by source and a live result, and no product-code change is in the diff.

6. Report the outcome.

   Keep concise run notes in a scratch location. Do not commit the notes. Report the outcome, features covered, unreachable prerequisites, confirmed drift, product gaps, files changed, checks run, and remaining risk.

   For a clean or blocked outcome, do not create an empty change. For a changed outcome, re-read each changed file and leave one coherent diff. Create a branch, commit, or pull request only when the user requests it.

   Completion criterion: the user can distinguish source coverage, live coverage, corrections, product gaps, and blockers.
