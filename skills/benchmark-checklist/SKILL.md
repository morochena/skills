---
name: benchmark-checklist
description: Audit performance benchmarks and measured speedup or regression claims for correctness, fair comparison, repeatability, and user-visible relevance. Use when producing or reviewing performance measurements, not for diagnosing slowness without measurements.
license: MIT
disable-model-invocation: true
---

# Benchmark Checklist

Establish what a performance measurement supports before using it to choose an implementation or claim a change improved behavior. Match the effort to the decision and the available evidence.

A measurement audit is read-only by default. Inspect the supplied results and harness; run bounded local checks only within the authorized scope and with isolated state. Report harness defects and missing evidence. An audit does not authorize product changes, production tuning, or load against live services.

When another workflow reads this file as guidance, apply the checks relevant to its performance claim within that workflow's scope. Do not start an unrelated benchmark campaign.

## Workflow

1. Define the claim and measured work.

   State the metric, unit, workload, and comparison the decision depends on. Record the relevant revisions, build mode, dependencies, configuration, environment, data size, and concurrency. Read the harness to establish what the timed region includes and excludes, including setup, warmup, lazy work, and asynchronous completion.

   For an explicitly requested ballpark estimate, one run can suffice if the work and output are verified. Label it as a single observation. Do not turn it into an option ranking or an established regression claim.

2. Verify that the work completed correctly.

   Confirm that the timed path ran the intended code and consumed its result. Count completed operations, failures, timeouts, and retries. Check output correctness or a meaningful invariant, not just output presence. Fast rejection, cached or skipped work, an unconsumed generator, or an unawaited promise can manufacture an apparent speedup. Keep failures visible and explain how they affect the metric.

3. Establish a fair comparison.

   Hold relevant workload and environment conditions constant except for the intended change. Check release versus debug builds, flags, indexes, batching, connection pools, cache state, and resource contention. Use representative supported configurations for each option and disclose meaningful differences. A difference caused by tuning supports a configuration claim, not an inherent advantage of one implementation.

   Identify an overloaded runner or saturated load generator before blaming the system under measurement. When a material comparison condition cannot be controlled, narrow the claim to what was observed or mark the comparison inconclusive.

4. Measure variation.

   For a consequential comparison, repeat runs with consistent warmup and interleave or randomize the sides to reduce order effects. Choose sample count and statistics for the workload, observed noise, and size of the claimed effect. A fixed number of runs is not a universal confidence threshold; tail latency needs enough observations to support the reported percentile.

   Report a central value and spread or suitable uncertainty estimate. Do not pick a winner from a gap the evidence cannot distinguish from noise. Failure to detect a difference does not establish equivalence. Preserve individual results in the existing harness output or temporary notes when they are needed to assess repeatability.

5. Check the explanation and physical limits.

   For a causal claim or optimization decision, seek a measured limiting resource or hot path. Profile separately from reported timings unless profiling overhead is part of the claim. Map the observed limiter to the relevant code, configuration, or load generator. Check claimed throughput against available resources. An end-to-end gain larger than the time spent in the changed piece needs evidence of additional effects, such as reduced contention.

   A repeatable measured difference can be real while its mechanism remains unknown. Report the observed effect when the comparison supports it, and label the causal explanation unproven. Do not invent a bottleneck or require a full profiling exercise for every small measurement.

6. Check relevance and report.

   Relate a microbenchmark to the end-to-end path the user cares about. Measure that path when a broader claim depends on it and the run is practical and authorized. Otherwise keep the claim local and name the missing evidence. Different workloads or a feature absent from the baseline cannot support a direct speedup ratio; use comparable work or an explicit absolute budget.

   Lead with the supported verdict: faster, slower, no measurable difference, or inconclusive. Give the measured values and units, with before and after values for a comparison. Include sample counts, variation, work and error counts, material conditions, and the observed limiter or an explicit unknown. Give the reproducible command and revision or artifact pointers available from the run. Keep the headline short and put detailed samples in supporting evidence. Name the cheapest missing check when the verdict is inconclusive.

## Completion

- Every performance conclusion stays within the evidence for the observed workload and metric. Missing work, output, comparison, or uncertainty evidence is explicit.
- Measured effects remain distinct from causal explanations and end-to-end predictions. Missing evidence limits the verdict rather than being filled by inference.
- The result stays within the requested audit or measurement scope. Preserve useful evidence and remove only scratch processes and state created by this run.
