# Research Gap Register — Literature Review Update 2026-09-25

This register records gaps identified by reviewing current HLS-DSE, automated pragma, benchmark, multi-fidelity, and multi-application work.

## G01 — External reproduction is now mandatory
HLSFactory provides full-flow dataset generation and artifact evaluation, including pre-generated datasets and versioned vendor-tool environments. Our project therefore needs an explicit reproduction layer rather than only a related-work table.

## G02 — Benchmark/design-space normalization
HLSyn exposes concrete pragma-valued design points and validity labels across tool versions. Our project must map benchmark identity, pragma space, validity, metric semantics, and tool version before comparing results.

## G03 — Automatic pragma generation is prior art
AutoHLS, automatic pragma insertion/NLP work, IronMan-Pro, and Sisyphus already automate pragma selection/transformation. Our pragma-space layer must be infrastructure, not the main novelty claim.

## G04 — Code transformation is a distinct search dimension
Sisyphus jointly considers code transformations, pragma insertion, and tile sizes. If our project permits source transformations, they must be a separately typed design-space dimension; otherwise explicitly exclude them from the core study.

## G05 — Multi-kernel/global optimization already exists
Stream-HLS and earlier multi-dependent-kernel work show that multi-kernel/global optimization is established. Our contribution must remain focused on evidence selection between local and joint evaluation, not merely global optimization.

## G06 — Multi-fidelity optimization is established
Correlated multi-objective multi-fidelity HLS work already exploits multiple fidelity levels. Our distinction must be decision-centric: selecting expensive joint evidence based on expected decision impact, not merely predicting higher-fidelity QoR.

## G07 — Feasibility semantics need standardization
Validity, synthesizability, resource feasibility, implementation success, timing closure, and final deployment feasibility are distinct labels in existing datasets and flows. They must not collapse into one binary field.

## G08 — Tool-version sensitivity must be first-class
HLSFactory's artifact evaluation explicitly spans multiple Vitis/Vivado versions and notes practical nondeterminism. Our environment registry must make tool version and environment part of evidence identity.

## G09 — Reproducibility artifacts are part of the contribution
HLSFactory supplies pre-generated datasets, scripts, figures, and detailed reproduction instructions. Our project should expose machine-readable manifests, commands, seeds, and immutable evidence links for every reported result.

## G10 — Dataset scale and storage need realistic budgeting
HLSFactory reports large storage/time requirements for full dataset regeneration. Our study contracts must budget disk, licenses, wall-clock, and parallelism before scaling experiments.

## G11 — Agentic HLS is an adjacent, rapidly evolving layer
HLSFactory-Agent (2026) automates extraction of standalone HLS designs from repositories. It does not replace our DSE question, but it affects benchmark acquisition and motivates a clean separation between dataset curation and DSE.

## G12 — Recent automated HLS frameworks broaden the baseline set
CollectiveHLS, AutoHLS, IronMan-Pro, Sisyphus, and Stream-HLS should be treated as distinct baseline families rather than one generic 'prior HLS-DSE' category.

## G13 — Direct comparison requires matched evaluation stage
HLS, synthesis, placement/routing, and physical timing are different evidence levels. A method evaluated only at HLS cannot be directly compared with post-route QoR without stage normalization.

## G14 — Search-budget fairness is essential
Reported speedups may use different numbers of evaluations, surrogate calls, or pruning assumptions. Our comparison must report candidate count, expensive evaluations, wall-clock, and lifecycle/programming time where applicable.

## G15 — External baseline failure is itself evidence
When a method cannot be reproduced because of missing code/data, proprietary dependencies, or incompatible tool versions, record the failure rather than silently substituting an implementation.

## G16 — Publication claims need an explicit comparability label
Every external comparison row must be labelled direct reproduction, controlled re-evaluation, or indirect literature comparison.

## G17 — Missing current literature categories
Before final paper submission, re-scan HLS DSE for FIFO sizing, memory/bandwidth optimization, dataflow/global scheduling, agentic HLS, and post-route/physical-aware optimization so that the baseline set remains current.

## G18 — Power/energy measurement remains incomplete
The current project contains a power/energy extension, but it must define actual measurement source, tool, activity assumptions, execution workload, and whether power is estimated or measured before publication claims.

## G19 — The compositional assumption is prior art and untested (2026-09-25)
Compositional system-level HLS DSE (DATE 2012, COSMOS 2017, PG-DSE 2023, EtoE-DSE 2024) prunes components to their
local Pareto fronts. No oracle test of that assumption on co-resident FPGA kernels was found. → S97.

## G20 — Interaction residual across fidelities is unmeasured (2026-09-25)
Published evidence of non-additive behaviour is at RTL simulation (Stream-HLS) and post-route (Prometheus, FADO,
HLPS-DSE), never as "joint minus composed-local" against a noise floor. If the residual is zero at every
fidelity, the local-vs-joint question collapses. → S98 (go/no-go for S99).

## G21 — Local-vs-joint acquisition must build on multi-source VOI (2026-09-25)
Multi-information-source BO (MISO knowledge gradient; constrained multi-source BO) and decision-domain refinement
(Fovea) already exist outside HLS. The contribution can only be their formulation over local/joint sources with an
interaction-residual model, fused feasibility, censored crashes and tool noise. → S99.

## G22 — Runtime co-residence effects are documented but unused in DSE (2026-09-25)
Memory-path interference on FPGA SoCs (up to 10-16x slowdowns; bounded on Zynq-7000) is measured but not fed into
HLS DSE decisions. Requires a physical board (currently NOT_AVAILABLE). → S100.
