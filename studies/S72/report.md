---
report_metadata:
  report_id: "S72-SEARCH-ALGORITHM-COST"
  report_type: "STUDY"
  title: "Search Algorithm and End-to-End Cost Comparison"
  project: "HLS-DSE"
  project_version: "V22.9"
  phase_id: "P11"
  phase_name: "Advanced Search & Learning"
  study_id: "S72"
  study_name: "Search Algorithm and End-to-End Cost Comparison"
  status: "PLANNED"
authorship:
  generated_by_ai: true
  ai_model: "GPT-5.6 Luna"
  ai_role: "Research documentation"
  human_researcher: ""
  human_approval_required: true
  human_approval_status: "PENDING"
dates:
  created_date: "2026-09-25"
  last_updated: "2026-09-25"
versioning:
  report_version: "1.0"
  revision: 0
provenance:
  source_studies: []
  source_runs: []
  source_evidence: []
  source_artifacts: []
  source_data_versions: []
  source_scripts: []
  source_plot_scripts: []
reproducibility:
  environment_id: ""
  tool_versions: []
  hardware: []
  random_seeds: []
  commands_or_entrypoints: []
  reproducibility_status: "NOT_RUN"
validation:
  validation_status: "NOT_RUN"
  validation_tests: []
  acceptance_criteria: []
  failed_criteria: []
  known_limitations: []
classification:
  evidence_level: "PLANNED"
  publication_ready: false
---

# S72 — Search Algorithm and End-to-End Cost Comparison

## 1. Executive Summary

This study tests whether the choice of configuration-search algorithm changes not only the final design quality, but also the total cost of obtaining that result. Search computation, HLS/synthesis/P&R/bitstream cost, FPGA programming/configuration, initialization, and benchmark execution are recorded separately.

No search algorithm is assumed to be superior. The study is exploratory and its result may be **CORE**, **SUPPORTING**, **EXTENSION**, or **DROP** after evidence is reviewed.

## 2. Research Question

Under a controlled HLS design space and evaluation budget, how do exhaustive, random, Bayesian, evolutionary, and other search strategies trade off:

- search overhead;
- number and type of expensive evaluations;
- FPGA programming/configuration workload;
- end-to-end wall-clock time; and
- final Pareto/decision quality?

## 3. Experimental Separation

The study must distinguish:

1. **Search time** — computation used by the search algorithm to select/generate candidates.
2. **Evaluation time** — HLS, synthesis, P&R and bitstream generation.
3. **Programming time** — FPGA configuration/programming.
4. **Execution time** — benchmark execution after configuration.
5. **End-to-end time** — the sum of all applicable components.

## 4. Core Formula

\[
T_{end-to-end}=T_{search}+T_{HLS}+T_{SYN}+T_{PNR}+T_{BITSTREAM}+T_{PROGRAM}+T_{INIT}+T_{EXEC}
\]

Every term must be measured or explicitly marked `UNKNOWN`/`NOT_MEASURED`. Missing measurements must never be silently estimated.

## 5. Search Algorithms

Required baseline comparison:

- Exhaustive search when the space is small enough to execute fairly;
- Random search.

Controlled candidate comparisons:

- Bayesian Optimization;
- Evolutionary Search.

Optional extensions are not part of the initial implementation gate: heuristic search, multi-objective variants, RL-guided search, GNN/ML-guided search, and LLM/agentic search.

## 6. Controlled Variables

Benchmark identity, source revision, pragma-space version, candidate legality rules, device, board, package, speed grade, toolchain, clock constraints, correctness tests, objective/constraint definitions, fidelity, random seeds, concurrency/license conditions, and budget definition must be fixed or explicitly recorded.

## 7. Required Results

For every algorithm report:

- candidates generated;
- candidates evaluated;
- search overhead;
- HLS/synthesis/P&R/bitstream counts and times;
- number of programming events;
- programming time;
- benchmark invocations and execution time;
- total wall-clock time;
- hypervolume / decision loss / frontier coverage where applicable;
- time-to-target quality;
- variability across seeds/repetitions.

## 8. Required Plots

All plot code is isolated under `plots/code/` and generated outputs under `plots/generated/`.

1. Quality vs total wall-clock time.
2. Hypervolume vs wall-clock time.
3. Hypervolume vs evaluation budget.
4. Search overhead vs expensive evaluation cost.
5. Evaluation count vs total time.
6. Programming time vs configuration count.
7. End-to-end lifecycle time breakdown.
8. Time-to-target quality.

## 9. Interpretation Rule

A method must not be declared superior from one metric alone. A method with lower evaluation count but higher search overhead, or better QoR but higher lifecycle cost, must be reported as a trade-off.

## 10. Gate Decision

The study can recommend inclusion in the main paper only if the evidence demonstrates a reproducible and decision-relevant trade-off that survives the declared controls. Otherwise the result is retained as supporting evidence, extension material, or a negative result.
