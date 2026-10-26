# Comparing Agent Workflows

Use these checks when the measured change affects prompts, skills, delegation, or the agent loop. Apply the main checklist's repeatability and scope rules. A narrow result can justify a local default without establishing the best architecture for every workload.

## Control the Comparison

When isolating delegation, hold the model, reasoning effort, prompt content, source revision, prior findings, tools other than delegation, environment, and limits constant. Record required prompt differences and pin relevant runtime versions. If model selection or another mechanism also changes, describe the result as a comparison of those configurations.

Use fresh equivalent state and interleave or randomize variants. Retain every attempt, including timeouts, budget exhaustion, and partial outputs. Historical successes are useful context; they are not paired controls. A small repeated sample can support a bounded rollout while leaving generalization uncertain.

Observe what happened: delegation enabled is different from delegation used. Record task batches, child count, nesting, tool calls, and the actual stopping reason when available. Check whether child requests consume a shared parent limit. Parallel execution can exhaust the allowance before synthesis; distinguish that from a provider or infrastructure failure.

## Check the Output

Define success and quality criteria before inspecting variant results. Validate output structure, consequential claims, cited locations, severity or confidence, and an appropriate coverage sample. Hide variant identity from the evaluator when practical.

Check task completion separately from process exit. An agent can exit successfully after accurately reporting a blocked task. Confirm the requested artifact or applied change exists; a prepared patch does not complete a request to apply it. Classify permission and harness failures separately before drawing conclusions about the workflow.

Keep completion, correctness, coverage, latency, and usage separate. Matching finding counts or themes does not establish precision or recall. Findings supplied in the prompt cannot demonstrate blind rediscovery. Compare findings by their meaning as well as identifiers: unstable fingerprints can hide agreement. Check that citations support the claim rather than merely pointing to a nearby line.

## Account for the Whole Attempt

Measure wall time through usable final output, including worker startup, handoff, synthesis, verification, and retries relevant to the claim. Report failures and their consumed resources alongside successful-run timings. A failed run is not a faster completed result.

State the scope of each usage counter: parent, children, auxiliary model calls, retries, and cached tokens. Missing usage is unknown, not zero. Reported token volume is not invoiced cost; make a monetary claim only with applicable pricing or billing evidence and sufficient usage detail.

## Bound the Conclusion

Prefer a default for the measured task family and constraints over a universal delegation rule. Preserve cases where independent context, parallel outputs, or independent verification add value. Required execution, credential, and publication boundaries do not need to disappear when reasoning stays in one loop. State what evidence would justify keeping, revising, or reversing the change.
