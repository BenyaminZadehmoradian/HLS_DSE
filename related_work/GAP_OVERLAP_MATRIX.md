# Gap / Overlap Matrix — HLS-DSE V23.2

Generated 2026-09-25 from the 62 papers in `RELATED_WORK_REGISTRY.csv` (repository-derived).
This is an overlap-exposure tool, **not a novelty claim**. Every statement below is `LITERATURE_REPORTED`
evidence from the reviewed papers, or a statement about what those papers report. No HLS-DSE measurement exists yet (P0 not started).

**How cells are built.** "Prior work (YES)" lists papers whose review marked the dimension YES; "PARTIAL" gives a count
(ids in the appendix). Rows marked *keyword screen* use a text match on the review fields and are lower-confidence.
**Overlap risk** is a count heuristic on YES papers (HIGH ≥ 4, MEDIUM 1–3, LOW 0); it says how much prior work
touches the dimension, not whether our planned study differs from it. Coverage is limited to the reviewed set:
a LOW row can mean the literature was not searched deeply for that dimension (UNRESOLVED), not that no work exists.

## 1. Matrix

| Dimension | Prior work (YES) | PARTIAL | Our planned study | Evidence required | Overlap risk |
|---|---|---|---|---|---|
| HLS DSE | RW0001 CRYPTONITE, RW0002 MVSym, RW0006 CMMFO, RW0007 IronManPro, RW0008 HLSFactory, RW0009 HierQoR, RW0010 CollectiveHLS, RW0011 StreamHLS, RW0017 AutoDSE, RW0018 Chimera, RW0019 GNNDSE, RW0020 AutoHLS, RW0021 HARP, RW0022 HGBODSE, RW0023 HLSyn, RW0024 Balor, RW0025 HLPerf, RW0026 TaskTransfer, RW0027 Iceberg, RW0028 LIFT, RW0029 LLMDSE, RW0030 NLPDSE, RW0031 Prometheus, RW0032 Sisyphus, RW0033 FIFOAdvisor, RW0034 MPMLLM4DSE, RW0035 PatternDSE, RW0036 QoRML, RW0037 FADO, RW0042 HLPSDSE, RW0048 HLPow, RW0049 PowerGear, RW0050 EtoEDSE, RW0058 HIPPO, RW0060 HLSToday, RW0062 HLSFactoryAgent | 0 | S72, S75, S55–S58 | Measured search quality vs total wall-clock under a fixed pragma space (S72 protocol). | HIGH |
| Multi-objective DSE | RW0001 CRYPTONITE, RW0006 CMMFO, RW0007 IronManPro, RW0010 CollectiveHLS, RW0015 VOISetBased, RW0018 Chimera, RW0020 AutoHLS, RW0022 HGBODSE, RW0033 FIFOAdvisor, RW0048 HLPow, RW0049 PowerGear, RW0050 EtoEDSE, RW0056 CATransformers, RW0057 CORDOBA, RW0060 HLSToday | 0 | S43–S47, S54, S92 | Measured Pareto fronts with provenance per candidate; front metrics defined before execution. | HIGH |
| Multi-fidelity | RW0006 CMMFO, RW0009 HierQoR, RW0012 MTBO, RW0015 VOISetBased, RW0036 QoRML, RW0045 PLD, RW0058 HIPPO | 1 | S04, S21, S23 | Per-stage measured cost and fidelity error against a full-flow oracle (S04). | HIGH |
| Concurrent evaluation | RW0003 MultiFPGAAlloc, RW0004 EnergyOptAlloc, RW0011 StreamHLS, RW0014 CoopBO, RW0025 HLPerf, RW0031 Prometheus, RW0033 FIFOAdvisor, RW0037 FADO, RW0038 RapidStream2, RW0039 TAPA, RW0040 RapidStreamIR, RW0041 TAPACS, RW0042 HLPSDSE, RW0050 EtoEDSE | 9 | S15, S65, S07 | Joint vs local selection outcomes on the same multi-kernel workload, measured. | HIGH |
| Multi-kernel interaction | RW0011 StreamHLS, RW0025 HLPerf, RW0033 FIFOAdvisor, RW0037 FADO, RW0041 TAPACS, RW0042 HLPSDSE, RW0044 FOS | 28 | S02, S36–S41, S56 | Measured interaction effects (joint minus sum-of-local) with replication. | HIGH |
| Evidence selection | RW0006 CMMFO, RW0012 MTBO, RW0015 VOISetBased, RW0018 Chimera, RW0026 TaskTransfer, RW0029 LLMDSE, RW0042 HLPSDSE, RW0048 HLPow, RW0056 CATransformers | 12 | S05, S20, S22, S67 | Measured decision quality vs evidence spent for adaptive vs fixed policies. | HIGH |
| Decision-centric acquisition | RW0015 VOISetBased, RW0016 VOISystemDesign, RW0020 AutoHLS | 0 | S03, S16, S33 | Measured decision changes caused by acquired evidence (decision-change rate). | MEDIUM |
| Staged evaluation | RW0001 CRYPTONITE, RW0006 CMMFO, RW0020 AutoHLS, RW0030 NLPDSE, RW0035 PatternDSE, RW0038 RapidStream2, RW0042 HLPSDSE, RW0045 PLD, RW0048 HLPow | 25 | S88, S32 | Stage-decision records (STAGE_DECISION_CONTRACT) with measured stop/continue outcomes. | HIGH |
| Early stopping | RW0001 CRYPTONITE, RW0006 CMMFO, RW0029 LLMDSE, RW0030 NLPDSE, RW0050 EtoEDSE, RW0056 CATransformers, RW0057 CORDOBA | 0 | S32, S34, S88 | Measured false-stop rate against full-flow ground truth. | HIGH |
| Cost-aware evaluation | RW0006 CMMFO, RW0009 HierQoR, RW0011 StreamHLS, RW0012 MTBO, RW0015 VOISetBased, RW0030 NLPDSE, RW0031 Prometheus, RW0032 Sisyphus, RW0033 FIFOAdvisor, RW0036 QoRML, RW0038 RapidStream2, RW0045 PLD, RW0046 Bonamy12DPR, RW0049 PowerGear, RW0058 HIPPO | 31 | S06, S20, S72 | Measured tool wall-clock per stage (TIME_MEASUREMENT policy) charged to each decision. | HIGH |
| Pareto stability | RW0057 CORDOBA | 17 | S43–S46 | Replicated runs and seeds; measured front/rank stability. | MEDIUM |
| Physical implementation | RW0006 CMMFO, RW0008 HLSFactory, RW0009 HierQoR, RW0031 Prometheus, RW0036 QoRML, RW0038 RapidStream2, RW0039 TAPA, RW0040 RapidStreamIR, RW0041 TAPACS, RW0042 HLPSDSE, RW0043 DPRSurvey, RW0044 FOS, RW0045 PLD, RW0046 Bonamy12DPR, RW0047 Nafkha17DPR, RW0048 HLPow, RW0049 PowerGear, RW0053 IdleSleep, RW0058 HIPPO, RW0061 TARO | 11 | S78, S59–S61, S81 | Post-route timing/utilization reports as raw artifacts per candidate. | HIGH |
| Lifecycle cost | RW0005 DML, RW0038 RapidStream2, RW0043 DPRSurvey, RW0044 FOS, RW0045 PLD, RW0046 Bonamy12DPR, RW0047 Nafkha17DPR, RW0051 FOCAL, RW0052 GreenFPGA, RW0053 IdleSleep, RW0054 SustHWSpec, RW0056 CATransformers, RW0057 CORDOBA | 8 | S94, S06 | Measured build, programming and invocation costs over a declared lifecycle. | HIGH |
| Configuration/programming | RW0005 DML, RW0038 RapidStream2, RW0043 DPRSurvey, RW0044 FOS, RW0045 PLD, RW0046 Bonamy12DPR, RW0047 Nafkha17DPR, RW0052 GreenFPGA, RW0053 IdleSleep, RW0054 SustHWSpec, RW0056 CATransformers, RW0057 CORDOBA | 2 | S85, S86 | Measured programming time and bitstream size (requires hardware; currently NOT_AVAILABLE). | HIGH |
| CPU–FPGA interaction | RW0002 MVSym, RW0044 FOS, RW0053 IdleSleep | 14 | S83, S84 | Measured end-to-end latency/overlap on hardware (currently NOT_AVAILABLE). | MEDIUM |
| Memory/data movement | RW0003 MultiFPGAAlloc, RW0004 EnergyOptAlloc, RW0030 NLPDSE, RW0031 Prometheus, RW0032 Sisyphus, RW0033 FIFOAdvisor, RW0039 TAPA, RW0041 TAPACS, RW0044 FOS | 32 | S73 | Measured data-movement cost; DMA/ACP/cache remain UNKNOWN_UNTIL_MEASURED. | HIGH |
| Multi-benchmark transfer | RW0009 HierQoR, RW0010 CollectiveHLS, RW0012 MTBO, RW0019 GNNDSE, RW0021 HARP, RW0023 HLSyn, RW0026 TaskTransfer, RW0027 Iceberg, RW0028 LIFT, RW0034 MPMLLM4DSE, RW0048 HLPow, RW0049 PowerGear | 18 | S10, S11, S90, S91 | Held-out benchmark evaluation with leakage controls (DATA_LEAKAGE_CONTRACT). | HIGH |
| Sustainability/energy | RW0002 MVSym, RW0004 EnergyOptAlloc, RW0006 CMMFO, RW0022 HGBODSE, RW0046 Bonamy12DPR, RW0047 Nafkha17DPR, RW0048 HLPow, RW0049 PowerGear, RW0050 EtoEDSE, RW0051 FOCAL, RW0052 GreenFPGA, RW0053 IdleSleep, RW0054 SustHWSpec, RW0055 ASI, RW0056 CATransformers, RW0057 CORDOBA, RW0058 HIPPO | 4 | S19, S20, S96 | Measured power/energy distinguished from estimated power (AI_NO_GUESSING_POLICY). | HIGH |

## 2. Prior-art check (named works)

Legend: Y = YES, P = PARTIAL, N = NO, ? = NOT_REPORTED, - = NOT_APPLICABLE. Columns follow the review dimensions:
J joint (vs local) evaluation · I interactions measured · St staged evaluation · A adaptive evidence acquisition ·
C cost/fidelity modeled · L lifecycle/configuration cost · Ph physical implementation · T multi-benchmark transfer ·
D decision/Pareto stability · E energy/power · CF CPU–FPGA · Me memory/data movement. "Abstract" = reviewed from abstract only.

| Paper | Studies / measures / optimizes (as reported) | J | I | St | A | C | L | Ph | T | D | E | CF | Me | Review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RW0001 CRYPTONITE — CRYPTONITE: Scalable Accelerator Design for Cryptographic Primitives … | Straight-line (loop-free) C code of cryptographic primitives synthesizes via HLS into large, non-scalable hardware and offers no parameterizable constructs for… | P | N | Y | P | P | N | N | N | N | N | N | P | full text |
| RW0002 MVSym — MVSym: Efficient symbiotic exploitation of HLS-kernel multi-versionin… | Resource provisioning in multi-tenant collaborative CPU-FPGA cloud systems with variable resource availability and workloads; the paper exploits multiple HLS-g… | P | ? | P | ? | ? | P | ? | ? | ? | Y | Y | ? | abstract |
| RW0003 MultiFPGAAlloc — Exact and Heuristic Allocation of Multi-kernel Applications to Multi-… | Choosing the number of compute units (CUs) per kernel and allocating them across multiple FPGAs to minimize the pipeline initiation interval of multi-kernel ap… | Y | P | P | N | P | N | P | N | P | N | P | Y | full text |
| RW0004 EnergyOptAlloc — Fast Energy-Optimal Multi-Kernel DNN-like Application Allocation on M… | Finding minimum-power allocations of multi-kernel pipelined DNN-like applications on multi-FPGA platforms for a given throughput (II) constraint, fast enough t… | Y | P | N | N | P | P | P | N | N | Y | P | Y | full text |
| RW0005 DML — DML: Dynamic Partial Reconfiguration With Scalable Task Scheduling fo… | Scheduling heterogeneous tasks from one or multiple applications onto FPGA partially reconfigurable regions in a resource-efficient way while hiding dynamic pa… | P | ? | ? | ? | ? | Y | P | ? | ? | ? | ? | ? | abstract |
| RW0006 CMMFO — Correlated Multi-objective Multi-fidelity Optimization for HLS Direct… | Finding Pareto-optimal HLS directive configurations for power, delay and LUT area when evaluations come from three flow stages (HLS, logic synthesis, implement… | N | P | Y | Y | Y | N | Y | N | P | Y | N | P | full text |
| RW0007 IronManPro — IronMan-Pro: Multiobjective Design Space Exploration in HLS via Reinf… | HLS abstractions hide optimization opportunities, actual RTL quality is hard to predict, and HLS tools do not provide Pareto trade-offs among objectives/constr… | ? | ? | ? | ? | P | ? | P | ? | ? | ? | ? | ? | abstract |
| RW0008 HLSFactory — HLSFactory: A Framework Empowering High-Level Synthesis Datasets for … | Lack of large, standardized, multi-vendor, reproducible and extensible HLS datasets for ML-based QoR prediction and DSE. | - | N | P | N | P | N | Y | P | N | P | N | N | full text |
| RW0009 HierQoR — Hierarchical Source-to-Post-Route QoR Prediction in High-Level Synthe… | Obtaining post-route QoR requires a full C-to-bitstream flow per pragma change; prior predictors estimate post-HLS metrics or require running HLS, and handle p… | N | P | P | N | Y | N | Y | Y | P | N | N | P | full text |
| RW0010 CollectiveHLS — CollectiveHLS: A Collaborative Approach to High-Level Synthesis Desig… | Rapidly proposing latency-optimized, synthesizable HLS directive configurations for unseen applications without per-application QoR models or long meta-heurist… | N | P | P | N | P | N | N | Y | P | N | N | P | full text |
| RW0011 StreamHLS — Stream-HLS: Towards Automatic Dataflow Acceleration | HLS automation frameworks mostly insert pragmas without loop scheduling, target single kernels, lack global DSE, and miss graph-level pipelining (streaming) fo… | Y | Y | P | N | Y | N | N | P | N | N | P | P | full text |
| RW0012 MTBO — Multi-Task Bayesian Optimization | Whether knowledge from previous or related hyperparameter optimizations can be transferred to new tasks to make Bayesian optimization faster (the cold-start pr… | - | P | P | Y | Y | - | - | Y | N | - | - | - | full text |
| RW0013 CMOBOOCE — Constrained Multi-objective Bayesian Optimization through Optimistic … | Sample-efficient multi-objective BO when both objectives and constraints are unknown black-box functions, with theoretical guarantees that existing heuristic/a… | - | - | N | P | N | - | - | N | N | - | - | - | full text |
| RW0014 CoopBO — Bayesian optimization of cooperative components for multi-stage aero-… | Standard BO fails on very high-dimensional, highly constrained multi-component engineering design (multi-stage compressor blades) because of the curse of dimen… | Y | P | N | N | N | - | - | N | N | - | - | - | full text |
| RW0015 VOISetBased — A value of information methodology for multiobjective decisions in qu… | Lack of quantitative methodologies to inform design-maturation and convergence decisions in set-based design (SBD) for complex systems under multiobjective unc… | ? | ? | P | Y | Y | ? | - | ? | P | - | - | - | abstract |
| RW0016 VOISystemDesign — On the value of information in system design: A framework for underst… | How to understand designers' information requirements and design computer-based decision support/information-seeking aids for system design. | - | - | P | P | N | ? | - | - | - | - | - | - | abstract |
| RW0034 MPMLLM4DSE — MPM-LLM4DSE: Reaching the Pareto Frontier in HLS with Multimodal Lear… | GNN-only QoR surrogates miss source-level semantics of pragmas, and generic multi-objective optimizers do not exploit domain knowledge about how pragmas affect… | N | N | N | P | N | N | N | Y | ? | N | N | N | full text |
| RW0025 HLPerf — HLPerf: Demystifying the Performance of HLS-based Graph Neural Networ… | Evaluating the dynamic, input-dependent performance of HLS dataflow architectures (GNN kernels) is too slow via RTL simulation or on-board runs, hindering DSE … | Y | Y | P | N | P | N | P | P | N | N | N | P | full text |
| RW0035 PatternDSE — Pattern-Guided Design Space Exploration for FPGA Accelerator Design | HLS schedule decisions (pipelining, unrolling, tiling, reordering, buffering) create a combinatorial space; generic search wastes synthesis budget on structura… | N | P | Y | N | P | N | N | N | N | N | N | P | full text |
| RW0018 Chimera — Chimera: A Hybrid Machine Learning Driven Multi-Objective Design Spac… | Applying HLS optimization directives to reach expert-level designs requires expertise and many slow HLS runs; DSE must be sample-efficient, multi-objective and… | N | P | N | Y | P | N | N | N | P | N | N | P | full text |
| RW0037 FADO — FADO: Floorplan-Aware Directive Optimization for High-Level Synthesis… | HLS directive DSE for single-die FPGAs ignores per-die resource constraints and die-crossing delays on multi-die FPGAs, while global floorplanning per DSE step… | Y | Y | P | N | P | N | P | N | P | N | N | P | full text |
| RW0022 HGBODSE — HGBO-DSE: Hierarchical GNN and Bayesian Optimization based HLS Design… | Finding Pareto-optimal HLS designs in a vast directive configuration space with accurate post-implementation PPA estimation. | ? | P | ? | P | P | ? | P | ? | ? | Y | ? | P | abstract |

Lifecycle/DFX and energy/sustainability works are covered in the matrix rows above (categories `lifecycle_dfx`,
`energy_sustainability`). Values come from each paper's review; NOT_REPORTED is not the same as NO.

## 3. Unresolved questions

- Paywalled works reviewed from abstract only (MVSym, DML, IronMan-Pro, HGBO-DSE, both VOI papers) have mostly
  NOT_REPORTED dimensions; their overlap on joint evaluation, staged evaluation and adaptive acquisition is UNRESOLVED.
- HLPerf was reviewed from full text but its PDF could not be stored (publisher returned HTTP 403).
- Keyword-screen rows (multi-objective, early stopping) need manual confirmation.
- The reviewed set is not a systematic review; dimensions with few or no YES papers require a targeted literature
  search before any gap is treated as more than a POTENTIAL GAP.
- All potential gaps REQUIRE EXPERIMENTAL VALIDATION; none is established by this matrix.

## 4. Appendix — evidence per dimension

### HLS DSE

Basis: registry category hls_dse/core.

Evidence (review notes of YES papers):

- **RW0001 CRYPTONITE** (2025, IEEE ASAP): Two stages: (1) an e-graph (egg) loop synthesizer using equality saturation plus data-dependence analysis (SVF) and GiNaC-based pattern abstraction to re-roll straight-line code into loops/arrays with preserved equivale…
- **RW0002 MVSym** (2023, Integration, the VLSI Journal): Two symbiotic stages: an HLS-Versioning Optimization Stage selecting a kernel version per request according to a weighted goal (performance/energy/area), followed by a Collaborative Allocation Optimization Stage mapping…
- **RW0006 CMMFO** (2021, DATE): GP-based Bayesian optimization with a non-linear multi-fidelity GP (low-fidelity outputs concatenated as inputs to higher-fidelity GP), correlated multi-output GP across objectives, and a cost-penalized EIPV acquisition…
- **RW0007 IronManPro** (2023, IEEE TCAD): Three components: GPP (GNN-based performance/resource predictor on data-flow graphs), RLMD (RL-based multi-objective DSE engine), CT (code transformer extracting DFGs from HLS C/C++ and emitting synthesizable code with …
- **RW0008 HLSFactory** (2024, MLCAD): Three-stage Python framework: (1) OptDSL frontend expands/samples designs (vendor-specific lowering for AMD/Xilinx and Intel), (2) parallel HLS synthesis and implementation tool flows with fine-grained multiprocessing, …
- **RW0009 HierQoR** (2024, DATE): LLVM/ProGraML CDFG extended with pragma effects (replicated nodes for unrolling, memory-port nodes for partitioning, loop-level IL/II/TC features); hierarchical GNNs: separate local GNNs for pipelined and non-pipelined …
- **RW0010 CollectiveHLS** (2024, ACM TRETS): Offline: LLVM-based source feature extraction and NSGA-II (pop 40, 24 generations) synthesis-based exploration of ~56 applications to build a knowledge base; hierarchical clustering of applications by code features and …
- **RW0011 StreamHLS** (2025, FPGA): MLIR-based framework: dataflow canonicalization and shared-buffer-to-FIFO conversion, an analytical performance model for dataflow designs with FIFO/shared-buffer communication, and MINLP (AMPL + Gurobi) global scheduli…
- **RW0017 AutoDSE** (2022, ACM TODAES): Bottleneck-guided coordinate optimizer: uses Merlin/HLS cycle breakdown to identify critical hierarchy paths and bottleneck type (memory vs compute), orders parameters by impact, tunes them one at a time; design space p…
- **RW0018 Chimera** (2022, arXiv (extended version of IDEAL 2021 p…): Active-learning loop with random-forest latency/resource models plus timeout/error prediction; three point-proposal engines (random, evolutionary, mutational) selected by Thompson sampling; probabilistic 'soft-boundary'…
- **RW0019 GNNDSE** (2022, DAC): ProGraML-based graph (control/data/call flow) extended with pragma nodes; GNN encoder (TransformerConv + Jumping Knowledge + node attention) with MLP heads for validity classification and latency/resource regression; us…
- **RW0020 AutoHLS** (2023, IEEE MWSCAS): Optuna TPE multi-objective Bayesian optimization with a DNN (or 5-qubit variational QNN) decision maker that predicts synthesis failure/resource usage and filters BO samples before running HLS.
- **RW0021 HARP** (2023, ICCAD): HARP: hierarchical graph adding pseudo nodes for high-level (C/LLVM block) structure on top of GNN-DSE's ProGraML-based graph; decoupled program (P) and transformation (T) representations with a neural pragma transforme…
- **RW0022 HGBODSE** (2023, ICFPT): HGP hierarchical GNN predictor with hierarchical pooling estimating post-implementation power, critical-path delay and resource use; TDM tree-structured design-space modeler; BOME multi-objective BO engine with MOTPE-FL…
- **RW0023 HLSyn** (2023, NeurIPS (Datasets and Benchmarks Track)): HLSyn dataset: 42 MachSuite/PolyBench kernels with over 42,000 labeled designs from two tool versions (SDx 'v1' and Vitis 'v2'); benchmark of code/graph encoders (code2vec, CodeT5 variants, GraphCodeBERT, GNN-DSE varian…
- **RW0024 Balor** (2024, ICCAD): ROSE-based graph compiler producing compact HLS-tailored graphs; 'Locations Have Information' annotation that analytically propagates directive (parallelization, pipelining, partitioning, inlining) information onto affe…
- **RW0025 HLPerf** (2024, ACM TRETS): Approximately-cycle-accurate discrete-event simulation (SimPy/PyPy) of dataflow HLS kernels built from HLS C code and pragma-driven pattern models, decoupling performance from functional verification; can also use manua…
- **RW0026 TaskTransfer** (2024, ICCAD): Active-CEM: cross-entropy-method importance sampling over factorized per-pragma distributions, with an inner active-learning loop that selects designs for HLS labeling via K-Means coreset on GNN (HARP) embeddings and fi…
- **RW0027 Iceberg** (2025, ICLAD): LLM-driven generation of diverse synthesizable HLS programs (3000+ released; 214 labeled via AutoDSE), weak labels for unseen configurations from an ensemble of GNNs with MC-dropout, and G-TNP: a HARP GNN encoder feedin…
- **RW0028 LIFT** (2025, arXiv): Fine-tune DeepSeek-Coder 7B (LoRA) with fill-in-the-middle (ILM) formatting, latency-derived sample weights and resampling, plus a structural loss: predicted and ground-truth pragma-annotated code are converted to ProGr…
- **RW0029 LLMDSE** (2025, arXiv): Multi-agent LLM tree search (GPT-4o): Router assigns designs to performance- or resource-oriented Specialists that propose per-parameter updates; Arbitrator (budget-aware) selects proposals; Critic runs the toolchain, p…
- **RW0030 NLPDSE** (2025, ACM TODAES): Analytical latency/resource model parameterized by pragmas, proven to be a latency lower bound under stated hypotheses, encoded as a Non-Linear Program (AMPL + BARON); a lightweight NLP-driven DSE iterates over max arra…
- **RW0031 Prometheus** (2025, ACM TODAES): Prometheus: affine analysis builds a task dataflow graph (fusing statements sharing outputs); a Non-Linear Program (AMPL + Gurobi 11 nonconvex) with multi-level latency model and global/per-SLR resource constraints sele…
- **RW0032 Sisyphus** (2025, FPGA): Builds a legal-by-construction three-level loop template (PoCC/ISCC polyhedral analysis) and formulates an analytical latency/resource model as a Nonlinear Program solved with Gurobi/AMPL; generates C++ with Vitis pragm…
- **RW0033 FIFOAdvisor** (2026, ASP-DAC): Black-box multi-objective optimization with LightningSim incremental trace-based simulation (<1 ms per FIFO configuration) for latency and an analytical BRAM18K usage model; optimizers: random, grouped random, simulated…
- **RW0034 MPMLLM4DSE** (2026, DATE): Multimodal predictor (MPM): Enhanced-CoGNN over ProGraML CDFG fused via multi-head attention and gating with CodeBERT-c embeddings of pragma-annotated source; LLM4DSE uses an LLM (GPT-4o / Qwen3-235B) as optimizer with …
- **RW0035 PatternDSE** (2026, ICECCME (arXiv preprint)): Map each kernel to one of five manually defined pattern classes (elementwise, reduction, matvec, gemm, stencil) with compact schedule templates; validate candidates by LLVM execution and HLS C code generation; rank with…
- **RW0036 QoRML** (2018, FCCM): Build a dataset of >1300 C-to-bitstream samples over 65 designs; extract 234 HLS-report features reduced to 87 via correlation filtering and L1 selection; train Lasso, ANN and XGBoost regression (LUT/FF/DSP/BRAM) and cl…
- **RW0037 FADO** (2023, FPGA): Formulates as multi-choice multi-dimensional bin-packing; iterative latency-bottleneck-guided greedy directive search with incremental floorplan legalization (worst-fit online packing, best-fit-decreasing offline re-pac…
- **RW0042 HLPSDSE** (2025, ICCAD): Iterative, metric-guided DSE organized as a finite-state machine of six actions; after each place-and-route, extracts physical metrics (per-slot utilization, congestion windows, critical-path distribution, slot-crossing…
- **RW0048 HLPow** (2020, ASP-DAC): Automated feature construction from HLS reports/IR (resources, performance, scaling factors, operator-level switching activity from IR simulation; 256 features) and ML power models (linear, SVM, tree ensembles/GBDT, MLP…
- **RW0049 PowerGear** (2022, DATE): Graph construction from HLS IR/FSMD (buffer insertion, datapath merging, graph trimming, edge annotation with switching activity from instrumented IR execution); heterogeneous edge-centric GNN (HEC-GNN) that aggregates …
- **RW0050 EtoEDSE** (2024, IEEE TCAD): EtoE-DSE: end-to-end pathfinding (EPF) and worst-case latency estimation; frequency-based design space segmentation and energy/area Pareto pruning of alternatives (FDSS); latency-constrained segmented GA optimization (L…
- **RW0058 HIPPO** (2025, ICCAD): LLVM/ProGraML-derived hierarchy-preserving CDFG (HP-CDFG) with embedded unroll/partition effects and switching activity from instrumented software execution; analytical linear power models at operation level and GNNs (P…
- **RW0060 HLSToday** (2022, ACM TRETS): Survey of successful HLS deployments (deep learning, video transcoding, graph processing, genome sequencing) and discussion of challenges: clock frequency (AutoBridge floorplanning+pipelining), directive complexity and …
- **RW0062 HLSFactoryAgent** (2026, OSCAR Workshop @ ISCA (arXiv)): Paper-scraping/indexing scripts (DBLP, IEEE Xplore, Crossref/ACM) to find candidate HLS papers (2,517), human curation, then a Pi-framework LLM agent in Docker (Clang, file tools, Bash) that identifies kernels, copies d…

### Multi-objective DSE

Basis: text match /multi-?objective|pareto/ on method, metrics, main_result (keyword screen, lower confidence).

Evidence (review notes of YES papers):

- **RW0001 CRYPTONITE** (2025, IEEE ASAP): Two stages: (1) an e-graph (egg) loop synthesizer using equality saturation plus data-dependence analysis (SVF) and GiNaC-based pattern abstraction to re-roll straight-line code into loops/arrays with preserved equivale…
- **RW0006 CMMFO** (2021, DATE): GP-based Bayesian optimization with a non-linear multi-fidelity GP (low-fidelity outputs concatenated as inputs to higher-fidelity GP), correlated multi-output GP across objectives, and a cost-penalized EIPV acquisition…
- **RW0007 IronManPro** (2023, IEEE TCAD): Three components: GPP (GNN-based performance/resource predictor on data-flow graphs), RLMD (RL-based multi-objective DSE engine), CT (code transformer extracting DFGs from HLS C/C++ and emitting synthesizable code with …
- **RW0010 CollectiveHLS** (2024, ACM TRETS): Offline: LLVM-based source feature extraction and NSGA-II (pop 40, 24 generations) synthesis-based exploration of ~56 applications to build a knowledge base; hierarchical clustering of applications by code features and …
- **RW0015 VOISetBased** (2021, Systems Engineering (Wiley/INCOSE) 24(6…): Value-of-information methodology using Bayesian decision models: a framework integrating VOI into SBD, a multiobjective VOI method assessing a higher-resolution model's ability to reduce uncertainty, and comparison of m…
- **RW0018 Chimera** (2022, arXiv (extended version of IDEAL 2021 p…): Active-learning loop with random-forest latency/resource models plus timeout/error prediction; three point-proposal engines (random, evolutionary, mutational) selected by Thompson sampling; probabilistic 'soft-boundary'…
- **RW0020 AutoHLS** (2023, IEEE MWSCAS): Optuna TPE multi-objective Bayesian optimization with a DNN (or 5-qubit variational QNN) decision maker that predicts synthesis failure/resource usage and filters BO samples before running HLS.
- **RW0022 HGBODSE** (2023, ICFPT): HGP hierarchical GNN predictor with hierarchical pooling estimating post-implementation power, critical-path delay and resource use; TDM tree-structured design-space modeler; BOME multi-objective BO engine with MOTPE-FL…
- **RW0033 FIFOAdvisor** (2026, ASP-DAC): Black-box multi-objective optimization with LightningSim incremental trace-based simulation (<1 ms per FIFO configuration) for latency and an analytical BRAM18K usage model; optimizers: random, grouped random, simulated…
- **RW0048 HLPow** (2020, ASP-DAC): Automated feature construction from HLS reports/IR (resources, performance, scaling factors, operator-level switching activity from IR simulation; 256 features) and ML power models (linear, SVM, tree ensembles/GBDT, MLP…
- **RW0049 PowerGear** (2022, DATE): Graph construction from HLS IR/FSMD (buffer insertion, datapath merging, graph trimming, edge annotation with switching activity from instrumented IR execution); heterogeneous edge-centric GNN (HEC-GNN) that aggregates …
- **RW0050 EtoEDSE** (2024, IEEE TCAD): EtoE-DSE: end-to-end pathfinding (EPF) and worst-case latency estimation; frequency-based design space segmentation and energy/area Pareto pruning of alternatives (FDSS); latency-constrained segmented GA optimization (L…
- **RW0056 CATransformers** (2025, NeurIPS): Multi-objective Bayesian optimization (Ax/BoTorch qNEHVI) over joint model-hardware space with an ML evaluator (importance pruning + brief fine-tuning as accuracy proxy) and a hardware estimator (Accelergy, Sunstone) pl…
- **RW0057 CORDOBA** (2025, HPCA): Define and justify tCDP (total carbon x delay); sweep design space via an ML-accelerator simulator plus an updated ACT carbon model; derive tCDP-optimal designs and Pareto fronts across operational use, prune designs su…
- **RW0060 HLSToday** (2022, ACM TRETS): Survey of successful HLS deployments (deep learning, video transcoding, graph processing, genome sequencing) and discussion of challenges: clock frequency (AutoBridge floorplanning+pipelining), directive complexity and …

### Multi-fidelity

Basis: category multifidelity/core AND `cost_or_fidelity_modeled`.

Evidence (review notes of YES papers):

- **RW0006 CMMFO** (2021, DATE): Non-linear multi-fidelity GP plus acquisition penalty proportional to T_impl/T_i stage runtime.
- **RW0009 HierQoR** (2024, DATE): Predicts high-fidelity post-route QoR from source to avoid HLS+implementation cost
- **RW0012 MTBO** (2013, NeurIPS (NIPS 2013)): Evaluation cost c_t(x) modeled by multi-task GP on log cost; information gain per unit cost.
- **RW0015 VOISetBased** (2021, Systems Engineering (Wiley/INCOSE) 24(6…): Compares high-resolution models given usage cost and information value (abstract).
- **RW0036 QoRML** (2018, FCCM): Explicitly models the gap between low-fidelity HLS estimates and high-fidelity implementation results
- **RW0045 PLD** (2022, ASPLOS): Compile time vs performance trade-off quantified per level.
- **RW0058 HIPPO** (2025, ICCAD): Pre-HLS model positioned as a cheap substitute for full EDA flow + measurement; measurement noise modeled

PARTIAL: RW0027 Iceberg

### Concurrent evaluation

Basis: review dimension `local_vs_joint_evaluation`.

Evidence (review notes of YES papers):

- **RW0003 MultiFPGAAlloc** (2019, DAC): All kernels' CU counts and placements are optimized jointly under shared per-FPGA constraints.
- **RW0004 EnergyOptAlloc** (2022, IEEE TCAD): All kernels' CU counts, placements, and FPGA frequencies optimized jointly.
- **RW0011 StreamHLS** (2025, FPGA): All kernels (nodes) of a multi-kernel application scheduled jointly under a global DSP budget
- **RW0014 CoopBO** (2025, Structural and Multidisciplinary Optimi…): Component subproblems optimized separately but every high-fidelity evaluation is of the full coupled multi-stage system.
- **RW0025 HLPerf** (2024, ACM TRETS): Simulates the whole dataflow pipeline of interconnected kernels jointly to identify bottleneck stages.
- **RW0031 Prometheus** (2025, ACM TODAES): All tasks/statements of a program optimized jointly in one NLP including per-SLR placement
- **RW0033 FIFOAdvisor** (2026, ASP-DAC): All FIFOs of a multi-task dataflow design are sized jointly with whole-design latency
- **RW0037 FADO** (2023, FPGA): Multiple dataflow and non-dataflow kernels in one design co-optimized under shared per-die resource constraints.
- **RW0038 RapidStream2** (2023, ACM TRETS): Entire multi-module dataflow design implemented with coordinated islands
- **RW0039 TAPA** (2023, ACM TRETS): All tasks of the dataflow design floorplanned and pipelined jointly
- **RW0040 RapidStreamIR** (2024, ICCAD): Entire hierarchical design partitioned and floorplanned jointly
- **RW0041 TAPACS** (2024, ASPLOS): All tasks partitioned jointly across FPGAs and slots
- **RW0042 HLPSDSE** (2025, ICCAD): Whole multi-module accelerator is floorplanned and implemented jointly
- **RW0050 EtoEDSE** (2024, IEEE TCAD): Component alternatives combined and evaluated at system level under EtoE latency.

PARTIAL: RW0001 CRYPTONITE, RW0002 MVSym, RW0005 DML, RW0044 FOS, RW0045 PLD, RW0054 SustHWSpec, RW0056 CATransformers, RW0057 CORDOBA, RW0061 TARO

### Multi-kernel interaction

Basis: review dimension `interactions_measured`.

Evidence (review notes of YES papers):

- **RW0011 StreamHLS** (2025, FPGA): Graph-level pipelining interactions between producer/consumer nodes modeled and ablated (Opt2-Opt5)
- **RW0025 HLPerf** (2024, ACM TRETS): Inter-kernel FIFO/stall interactions and input-dependent bottlenecks are modelled and shown to differ between regular vs power-law graphs.
- **RW0033 FIFOAdvisor** (2026, ASP-DAC): Inter-task FIFO effects (stalls, deadlocks) captured via simulation
- **RW0037 FADO** (2023, FPGA): Cross-kernel resource contention per slot, die-crossing timing, and latency bottleneck across functions explicitly modeled.
- **RW0041 TAPACS** (2024, ASPLOS): Inter-task communication cost across dies/FPGAs modeled and measured
- **RW0042 HLPSDSE** (2025, ICCAD): Physical interactions between modules (congestion, crossings, SLL use) measured from post-route results
- **RW0044 FOS** (2020, ACM TRETS): Measured co-execution effects, e.g., memory-bank contention in Mandelbrot x Sobel scenarios.

PARTIAL: RW0003 MultiFPGAAlloc, RW0004 EnergyOptAlloc, RW0006 CMMFO, RW0009 HierQoR, RW0010 CollectiveHLS, RW0012 MTBO, RW0014 CoopBO, RW0017 AutoDSE, RW0018 Chimera, RW0019 GNNDSE, RW0021 HARP, RW0022 HGBODSE, RW0024 Balor, RW0026 TaskTransfer, RW0029 LLMDSE, RW0030 NLPDSE, RW0031 Prometheus, RW0032 Sisyphus, RW0035 PatternDSE, RW0038 RapidStream2, RW0039 TAPA, RW0040 RapidStreamIR, RW0045 PLD, RW0050 EtoEDSE, RW0053 IdleSleep, RW0055 ASI, RW0056 CATransformers, RW0058 HIPPO

### Evidence selection

Basis: review dimension `adaptive_evidence_acquisition`.

Evidence (review notes of YES papers):

- **RW0006 CMMFO** (2021, DATE): Per iteration selects (configuration, fidelity) pair maximizing penalized EIPV.
- **RW0012 MTBO** (2013, NeurIPS (NIPS 2013)): Cost-sensitive multi-task entropy search chooses which task/fold to query; fast CV chooses which fold.
- **RW0015 VOISetBased** (2021, Systems Engineering (Wiley/INCOSE) 24(6…): VOI decides whether/which higher-resolution model to use (abstract).
- **RW0018 Chimera** (2022, arXiv (extended version of IDEAL 2021 p…): Active learning with probabilistic evaluation and Thompson-sampling switching between proposal engines.
- **RW0026 TaskTransfer** (2024, ICCAD): Active learning (coreset) selects which designs to synthesize each CEM iteration
- **RW0029 LLMDSE** (2025, arXiv): LLM agents choose which designs to synthesize next based on feedback and remaining budget
- **RW0042 HLPSDSE** (2025, ICCAD): Metrics from prior implementations guide the next parameter choices
- **RW0048 HLPow** (2020, ASP-DAC): SDR-guided sampling selects which design points to run through HLS.
- **RW0056 CATransformers** (2025, NeurIPS): Bayesian optimization (qNEHVI) chooses configurations to evaluate over 100 trials.

PARTIAL: RW0001 CRYPTONITE, RW0013 CMOBOOCE, RW0016 VOISystemDesign, RW0017 AutoDSE, RW0019 GNNDSE, RW0020 AutoHLS, RW0022 HGBODSE, RW0030 NLPDSE, RW0031 Prometheus, RW0033 FIFOAdvisor, RW0034 MPMLLM4DSE, RW0049 PowerGear

### Decision-centric acquisition

Basis: text match /value of information|decision/ AND adaptive acquisition YES/PARTIAL.

Evidence (review notes of YES papers):

- **RW0015 VOISetBased** (2021, Systems Engineering (Wiley/INCOSE) 24(6…): Value-of-information methodology using Bayesian decision models: a framework integrating VOI into SBD, a multiobjective VOI method assessing a higher-resolution model's ability to reduce uncertainty, and comparison of m…
- **RW0016 VOISystemDesign** (1986, Information Processing & Management 22(…): Conceptual framework: defines the value of information by three attributes (reduction of uncertainty, task relevance, appropriateness of form) and combines them with characterizations of design stages/tasks and approach…
- **RW0020 AutoHLS** (2023, IEEE MWSCAS): Optuna TPE multi-objective Bayesian optimization with a DNN (or 5-qubit variational QNN) decision maker that predicts synthesis failure/resource usage and filters BO samples before running HLS.

### Staged evaluation

Basis: review dimension `staged_evaluation`.

Evidence (review notes of YES papers):

- **RW0001 CRYPTONITE** (2025, IEEE ASAP): Analytical QoR estimator prunes candidates before HLS synthesis; Pareto feedback loop.
- **RW0006 CMMFO** (2021, DATE): Three fidelities (HLS, Synth, Impl); each candidate run only up to chosen fidelity h.
- **RW0020 AutoHLS** (2023, IEEE MWSCAS): ML failure/resource predictor screens BO samples before full HLS synthesis.
- **RW0030 NLPDSE** (2025, ACM TODAES): NLP lower bound used to rank/prune before HLS synthesis
- **RW0035 PatternDSE** (2026, ICECCME (arXiv preprint)): LLVM execution check -> HLS C codegen check -> estimator ranking -> Vitis HLS on top-k.
- **RW0038 RapidStream2** (2023, ACM TRETS): Multi-phase flow: partition/floorplan, parallel island implementation, stitching/partial routing
- **RW0042 HLPSDSE** (2025, ICCAD): FSM of ordered actions; each stage builds on best result of the previous
- **RW0045 PLD** (2022, ASPLOS): -O0 / -O1 / -O3 levels provide progressively slower but higher-quality compile paths.
- **RW0048 HLPow** (2020, ASP-DAC): HLS runs + learned power model replace RTL implementation/measurement for most points.

PARTIAL: RW0002 MVSym, RW0003 MultiFPGAAlloc, RW0008 HLSFactory, RW0009 HierQoR, RW0010 CollectiveHLS, RW0011 StreamHLS, RW0012 MTBO, RW0015 VOISetBased, RW0016 VOISystemDesign, RW0019 GNNDSE, RW0021 HARP, RW0025 HLPerf, RW0026 TaskTransfer, RW0029 LLMDSE, RW0031 Prometheus, RW0036 QoRML, RW0037 FADO, RW0039 TAPA, RW0040 RapidStreamIR, RW0041 TAPACS, RW0049 PowerGear, RW0050 EtoEDSE, RW0056 CATransformers, RW0058 HIPPO, RW0062 HLSFactoryAgent

### Early stopping

Basis: text match /early[- ]?stop|early termination|prun/ on method, evaluation_method (keyword screen, lower confidence).

Evidence (review notes of YES papers):

- **RW0001 CRYPTONITE** (2025, IEEE ASAP): Two stages: (1) an e-graph (egg) loop synthesizer using equality saturation plus data-dependence analysis (SVF) and GiNaC-based pattern abstraction to re-roll straight-line code into loops/arrays with preserved equivale…
- **RW0006 CMMFO** (2021, DATE): GP-based Bayesian optimization with a non-linear multi-fidelity GP (low-fidelity outputs concatenated as inputs to higher-fidelity GP), correlated multi-output GP across objectives, and a cost-penalized EIPV acquisition…
- **RW0029 LLMDSE** (2025, arXiv): Multi-agent LLM tree search (GPT-4o): Router assigns designs to performance- or resource-oriented Specialists that propose per-parameter updates; Arbitrator (budget-aware) selects proposals; Critic runs the toolchain, p…
- **RW0030 NLPDSE** (2025, ACM TODAES): Analytical latency/resource model parameterized by pragmas, proven to be a latency lower bound under stated hypotheses, encoded as a Non-Linear Program (AMPL + BARON); a lightweight NLP-driven DSE iterates over max arra…
- **RW0050 EtoEDSE** (2024, IEEE TCAD): EtoE-DSE: end-to-end pathfinding (EPF) and worst-case latency estimation; frequency-based design space segmentation and energy/area Pareto pruning of alternatives (FDSS); latency-constrained segmented GA optimization (L…
- **RW0056 CATransformers** (2025, NeurIPS): Multi-objective Bayesian optimization (Ax/BoTorch qNEHVI) over joint model-hardware space with an ML evaluator (importance pruning + brief fine-tuning as accuracy proxy) and a hardware estimator (Accelergy, Sunstone) pl…
- **RW0057 CORDOBA** (2025, HPCA): Define and justify tCDP (total carbon x delay); sweep design space via an ML-accelerator simulator plus an updated ACT carbon model; derive tCDP-optimal designs and Pareto fronts across operational use, prune designs su…

### Cost-aware evaluation

Basis: review dimension `cost_or_fidelity_modeled`.

Evidence (review notes of YES papers):

- **RW0006 CMMFO** (2021, DATE): Non-linear multi-fidelity GP plus acquisition penalty proportional to T_impl/T_i stage runtime.
- **RW0009 HierQoR** (2024, DATE): Predicts high-fidelity post-route QoR from source to avoid HLS+implementation cost
- **RW0011 StreamHLS** (2025, FPGA): Analytical dataflow performance model validated vs RTL simulation
- **RW0012 MTBO** (2013, NeurIPS (NIPS 2013)): Evaluation cost c_t(x) modeled by multi-task GP on log cost; information gain per unit cost.
- **RW0015 VOISetBased** (2021, Systems Engineering (Wiley/INCOSE) 24(6…): Compares high-resolution models given usage cost and information value (abstract).
- **RW0030 NLPDSE** (2025, ACM TODAES): Analytical lower-bound model versus expensive HLS runs; bound tightness evaluated
- **RW0031 Prometheus** (2025, ACM TODAES): Analytical latency/resource cost model in NLP
- **RW0032 Sisyphus** (2025, FPGA): Analytical latency/resource model embedded in NLP; prediction error reported
- **RW0033 FIFOAdvisor** (2026, ASP-DAC): Cheap simulator vs co-simulation runtime quantified
- **RW0036 QoRML** (2018, FCCM): Explicitly models the gap between low-fidelity HLS estimates and high-fidelity implementation results
- **RW0038 RapidStream2** (2023, ACM TRETS): Compile-time cost is the primary optimized quantity and is profiled
- **RW0045 PLD** (2022, ASPLOS): Compile time vs performance trade-off quantified per level.
- **RW0046 Bonamy12DPR** (2012, ReConFig): Three model granularities with accuracy/complexity trade-off.
- **RW0049 PowerGear** (2022, DATE): Cheap post-HLS model substitutes for implementation, simulation and measurement; runtime compared
- **RW0058 HIPPO** (2025, ICCAD): Pre-HLS model positioned as a cheap substitute for full EDA flow + measurement; measurement noise modeled

PARTIAL: RW0001 CRYPTONITE, RW0003 MultiFPGAAlloc, RW0004 EnergyOptAlloc, RW0007 IronManPro, RW0008 HLSFactory, RW0010 CollectiveHLS, RW0017 AutoDSE, RW0018 Chimera, RW0019 GNNDSE, RW0020 AutoHLS, RW0021 HARP, RW0022 HGBODSE, RW0024 Balor, RW0025 HLPerf, RW0026 TaskTransfer, RW0027 Iceberg, RW0029 LLMDSE, RW0035 PatternDSE, RW0037 FADO, RW0039 TAPA, RW0040 RapidStreamIR, RW0041 TAPACS, RW0042 HLPSDSE, RW0043 DPRSurvey, RW0044 FOS, RW0048 HLPow, RW0051 FOCAL, RW0053 IdleSleep, RW0056 CATransformers, RW0057 CORDOBA, RW0062 HLSFactoryAgent

### Pareto stability

Basis: review dimension `decision_or_pareto_stability`.

Evidence (review notes of YES papers):

- **RW0057 CORDOBA** (2025, HPCA): Optimal design robustness across lifetime and carbon-intensity uncertainty analysed.

PARTIAL: RW0003 MultiFPGAAlloc, RW0006 CMMFO, RW0009 HierQoR, RW0010 CollectiveHLS, RW0015 VOISetBased, RW0018 Chimera, RW0026 TaskTransfer, RW0033 FIFOAdvisor, RW0037 FADO, RW0049 PowerGear, RW0050 EtoEDSE, RW0051 FOCAL, RW0052 GreenFPGA, RW0053 IdleSleep, RW0054 SustHWSpec, RW0055 ASI, RW0056 CATransformers

### Physical implementation

Basis: review dimension `physical_implementation`.

Evidence (review notes of YES papers):

- **RW0006 CMMFO** (2021, DATE): Implementation-stage (place-and-route) reports are the highest fidelity in the loop; illegal P&R designs penalized.
- **RW0008 HLSFactory** (2024, MLCAD): Vivado implementation (placed-and-routed) reports collected for datasets.
- **RW0009 HierQoR** (2024, DATE): Resource labels and exact Pareto sets from post-route implementation
- **RW0031 Prometheus** (2025, ACM TODAES): Bitstreams generated and run on board, including 3-SLR designs
- **RW0036 QoRML** (2018, FCCM): Labels are post-implementation (place and route) resource and timing
- **RW0038 RapidStream2** (2023, ACM TRETS): Full place-and-route and bitstreams
- **RW0039 TAPA** (2023, ACM TRETS): All results post place-and-route
- **RW0040 RapidStreamIR** (2024, ICCAD): Post-route frequencies reported
- **RW0041 TAPACS** (2024, ASPLOS): Full implementation and on-board runs
- **RW0042 HLPSDSE** (2025, ICCAD): Every candidate is placed and routed
- **RW0043 DPRSurvey** (2018, ACM Computing Surveys): Floorplanning, PR region shaping, bitstream generation discussed.
- **RW0044 FOS** (2020, ACM TRETS): Relocatable PR bitstreams built and run on boards.
- **RW0045 PLD** (2022, ASPLOS): Full place & route and bitstream per page; on-board execution.
- **RW0046 Bonamy12DPR** (2012, ReConFig): Real bitstreams on hardware.
- **RW0047 Nafkha17DPR** (2016, ISWCS): Real partial bitstreams on hardware.
- **RW0048 HLPow** (2020, ASP-DAC): Training/ground-truth power from implemented designs measured on board.
- **RW0049 PowerGear** (2022, DATE): Labels from implemented bitstreams measured on board
- **RW0053 IdleSleep** (2024, ARCS (LNCS 14842)): Real bitstreams on hardware.
- **RW0058 HIPPO** (2025, ICCAD): Labels from placed-and-routed bitstreams measured on board
- **RW0061 TARO** (2023, IEEE TCAD): Post-PnR resources and frequency reported

PARTIAL: RW0003 MultiFPGAAlloc, RW0004 EnergyOptAlloc, RW0005 DML, RW0007 IronManPro, RW0022 HGBODSE, RW0025 HLPerf, RW0032 Sisyphus, RW0037 FADO, RW0054 SustHWSpec, RW0057 CORDOBA, RW0060 HLSToday

### Lifecycle cost

Basis: review dimension `lifecycle_or_configuration_cost`.

Evidence (review notes of YES papers):

- **RW0005 DML** (2022, IEEE Transactions on Computers): DPR latency explicitly considered and hidden by the scheduler (abstract).
- **RW0038 RapidStream2** (2023, ACM TRETS): Uses partial reconfiguration (DFX) and pre-built shells; partial bitstreams per island
- **RW0043 DPRSurvey** (2018, ACM Computing Surveys): Central topic: reconfiguration time, bitstream size/compression, controller throughput, PR tool runtime.
- **RW0044 FOS** (2020, ACM TRETS): Compile time, component update/re-initialisation latency and PR swap latency quantified (Table 5).
- **RW0045 PLD** (2022, ASPLOS): Compile/turnaround cost is the core subject; partial bitstream loading used.
- **RW0046 Bonamy12DPR** (2012, ReConFig): Reconfiguration energy/time is the subject.
- **RW0047 Nafkha17DPR** (2016, ISWCS): Reconfiguration time/power overhead measured.
- **RW0051 FOCAL** (2024, ASPLOS): Embodied vs operational footprint weighting; accelerator usage amortization.
- **RW0052 GreenFPGA** (2024, DAC): Full lifecycle CFP including reconfiguration/app-development/configuration time.
- **RW0053 IdleSleep** (2024, ARCS (LNCS 14842)): Configuration energy and on/off vs idle lifecycle central.
- **RW0054 SustHWSpec** (2024, ICCAD): Embodied footprint amortization via reconfiguration across kernels.
- **RW0056 CATransformers** (2025, NeurIPS): Embodied manufacturing carbon plus operational carbon over a 3-year lifetime.
- **RW0057 CORDOBA** (2025, HPCA): Embodied vs operational carbon over hardware lifetime is central.

PARTIAL: RW0002 MVSym, RW0004 EnergyOptAlloc, RW0021 HARP, RW0023 HLSyn, RW0026 TaskTransfer, RW0028 LIFT, RW0055 ASI, RW0059 SustGap

### Configuration/programming

Basis: lifecycle/configuration cost AND category lifecycle_dfx.

Evidence (review notes of YES papers):

- **RW0005 DML** (2022, IEEE Transactions on Computers): Doing More with Less (DML): an ILP-based scheduler that maps tasks to reconfigurable regions over time, hiding DPR latency, with IP-level pipelining/parallelization within batches and strategies for co-running multiple …
- **RW0038 RapidStream2** (2023, ACM TRETS): Partition the device into islands and floorplan the latency-insensitive design; insert anchor registers on inter-island nets; implement islands in parallel. RapidStream 1.0 stitches islands with RapidWright and resolves…
- **RW0043 DPRSurvey** (2018, ACM Computing Surveys): Literature survey; covers PR architectures, vendor and academic design flows (incl. HLS-to-PR bridges), overhead reduction (partitioning, floorplanning, bitstream compression, reconfiguration controllers), runtime manag…
- **RW0044 FOS** (2020, ACM TRETS): Modular development flow (shell, accelerators, drivers, runtime compiled in isolation with fixed interfaces), relocatable PR regions with bitstream manipulation (BitMan), JSON descriptors, and a resource-elastic schedul…
- **RW0045 PLD** (2022, ASPLOS): Partition the FPGA into DFX pages with a packet-switched linking network (BFT); compile each operator separately with Vitis HLS + Vivado using abstract shell; load partial bitstreams and configure links at runtime; same…
- **RW0046 Bonamy12DPR** (2012, ReConFig): Measure FPGA core power during DPR steps (CompactFlash read, xps_hw_icap writes) and derive coarse-, medium- and fine-grained power models with different accuracy/complexity.
- **RW0047 Nafkha17DPR** (2016, ISWCS): Custom ICAP32 DMA controller for high-throughput internal reconfiguration; measure VCCINT via shunt resistors, AD620 amplifiers and oscilloscope; compare full JTAG, partial JTAG and partial ICAP reconfiguration.
- **RW0052 GreenFPGA** (2024, DAC): GreenFPGA tool: embodied CFP models (design, manufacturing/packaging from ACT/ECO-CHIP data, EOL/recycling) plus deployment CFP (operational energy x carbon intensity, application development including FE/BE and per-dev…
- **RW0053 IdleSleep** (2024, ARCS (LNCS 14842)): Measure configuration stages and tune parameters; propose Idle-Waiting strategy with analytical model of executable workload items; reduce idle power by disabling clock reference/IOs and lowering VCCINT/VCCAUX; Python s…
- **RW0054 SustHWSpec** (2024, ICCAD): Abstract analytical model deriving the critical DSA count (CDC) above which a reconfigurable fabric is more sustainable; populate with synthesized CGRA (8x8 PE, UMC 40 nm, Morpher mapping) and Aladdin-modeled iso-perfor…
- **RW0056 CATransformers** (2025, NeurIPS): Multi-objective Bayesian optimization (Ax/BoTorch qNEHVI) over joint model-hardware space with an ML evaluator (importance pruning + brief fine-tuning as accuracy proxy) and a hardware estimator (Accelergy, Sunstone) pl…
- **RW0057 CORDOBA** (2025, HPCA): Define and justify tCDP (total carbon x delay); sweep design space via an ML-accelerator simulator plus an updated ACT carbon model; derive tCDP-optimal designs and Pareto fronts across operational use, prune designs su…

PARTIAL: RW0002 MVSym, RW0004 EnergyOptAlloc

### CPU–FPGA interaction

Basis: review dimension `cpu_fpga_interaction`.

Evidence (review notes of YES papers):

- **RW0002 MVSym** (2023, Integration, the VLSI Journal): Collaborative CPU-FPGA allocation is core.
- **RW0044 FOS** (2020, ACM TRETS): Linux/ARM host runtime and drivers manage accelerators; offloading scenarios.
- **RW0053 IdleSleep** (2024, ARCS (LNCS 14842)): MCU-FPGA SPI configuration and offloading.

PARTIAL: RW0003 MultiFPGAAlloc, RW0004 EnergyOptAlloc, RW0011 StreamHLS, RW0017 AutoDSE, RW0031 Prometheus, RW0038 RapidStream2, RW0039 TAPA, RW0040 RapidStreamIR, RW0041 TAPACS, RW0043 DPRSurvey, RW0045 PLD, RW0046 Bonamy12DPR, RW0047 Nafkha17DPR, RW0060 HLSToday

### Memory/data movement

Basis: review dimension `memory_data_movement`.

Evidence (review notes of YES papers):

- **RW0003 MultiFPGAAlloc** (2019, DAC): Per-FPGA DRAM bandwidth constraint in the model.
- **RW0004 EnergyOptAlloc** (2022, IEEE TCAD): DDR bandwidth, PCIe transfer time and input data replication modeled.
- **RW0030 NLPDSE** (2025, ACM TODAES): Off-chip to on-chip transfer, tiling/caching and burst width modeled
- **RW0031 Prometheus** (2025, ACM TODAES): Off-chip transfers, tiling, reuse, bit width, double buffering modeled
- **RW0032 Sisyphus** (2025, FPGA): Models off-chip/on-chip transfers, tiling for on-chip caching, burst width
- **RW0033 FIFOAdvisor** (2026, ASP-DAC): FIFO buffering/BRAM memory usage is the optimized quantity
- **RW0039 TAPA** (2023, ACM TRETS): HBM/DDR channel binding and memory interface optimizations
- **RW0041 TAPACS** (2024, ASPLOS): HBM channel allocation and inter-FPGA data volumes analyzed
- **RW0044 FOS** (2020, ACM TRETS): AXI port throughput characterized; memory contention observed.

PARTIAL: RW0001 CRYPTONITE, RW0006 CMMFO, RW0009 HierQoR, RW0010 CollectiveHLS, RW0011 StreamHLS, RW0017 AutoDSE, RW0018 Chimera, RW0022 HGBODSE, RW0024 Balor, RW0025 HLPerf, RW0035 PatternDSE, RW0036 QoRML, RW0037 FADO, RW0038 RapidStream2, RW0040 RapidStreamIR, RW0042 HLPSDSE, RW0043 DPRSurvey, RW0045 PLD, RW0046 Bonamy12DPR, RW0047 Nafkha17DPR, RW0048 HLPow, RW0049 PowerGear, RW0050 EtoEDSE, RW0051 FOCAL, RW0053 IdleSleep, RW0054 SustHWSpec, RW0055 ASI, RW0056 CATransformers, RW0057 CORDOBA, RW0058 HIPPO, RW0060 HLSToday, RW0061 TARO

### Multi-benchmark transfer

Basis: review dimension `multi_benchmark_transfer`.

Evidence (review notes of YES papers):

- **RW0009 HierQoR** (2024, DATE): DSE on four unseen applications
- **RW0010 CollectiveHLS** (2024, ACM TRETS): Core idea: transfer directive knowledge across applications; leave-one-out and knowledge-base ablation (Sec. 5.8).
- **RW0012 MTBO** (2013, NeurIPS (NIPS 2013)): Transfer across datasets (USPS->MNIST, CIFAR-10->SVHN/STL-10, shifted Branin).
- **RW0019 GNNDSE** (2022, DAC): Generalization to 4 unseen PolyBench kernels
- **RW0021 HARP** (2023, ICCAD): Transfer from SDx 2018.3 to Vitis 2020.2
- **RW0023 HLSyn** (2023, NeurIPS (Datasets and Benchmarks Track)): Held-out kernels with zero-shot and few-shot adaptation
- **RW0026 TaskTransfer** (2024, ICCAD): Transfer across toolchain versions and across programs (domain transfer)
- **RW0027 Iceberg** (2025, ICLAD): Few-shot adaptation to unseen HLSyn and real-world programs
- **RW0028 LIFT** (2025, arXiv): Unseen kernels and tool-version shift
- **RW0034 MPMLLM4DSE** (2026, DATE): Predictor trained on 15 kernels and tested on 6 unseen kernels.
- **RW0048 HLPow** (2020, ASP-DAC): Power model trained on 15 apps and tested on 7 unseen PolyBench apps.
- **RW0049 PowerGear** (2022, DATE): Leave-one-application-out transfer

PARTIAL: RW0008 HLSFactory, RW0011 StreamHLS, RW0024 Balor, RW0025 HLPerf, RW0029 LLMDSE, RW0030 NLPDSE, RW0031 Prometheus, RW0032 Sisyphus, RW0033 FIFOAdvisor, RW0036 QoRML, RW0038 RapidStream2, RW0039 TAPA, RW0040 RapidStreamIR, RW0041 TAPACS, RW0042 HLPSDSE, RW0056 CATransformers, RW0058 HIPPO, RW0061 TARO

### Sustainability/energy

Basis: review dimension `energy_or_power`.

Evidence (review notes of YES papers):

- **RW0002 MVSym** (2023, Integration, the VLSI Journal): Energy is a primary metric (RAPL/uProf for CPU).
- **RW0004 EnergyOptAlloc** (2022, IEEE TCAD): Objective is total power (static+dynamic), estimated.
- **RW0006 CMMFO** (2021, DATE): Power is one of three objectives (tool-reported).
- **RW0022 HGBODSE** (2023, ICFPT): Power is a predicted/optimized objective (PPA).
- **RW0046 Bonamy12DPR** (2012, ReConFig): Measured.
- **RW0047 Nafkha17DPR** (2016, ISWCS): Measured.
- **RW0048 HLPow** (2020, ASP-DAC): Power is the modeled objective with latency-power Pareto DSE.
- **RW0049 PowerGear** (2022, DATE): Total and dynamic power predicted and optimized
- **RW0050 EtoEDSE** (2024, IEEE TCAD): Energy is a primary objective (weighted 2:1 over area in fitness).
- **RW0051 FOCAL** (2024, ASPLOS): Energy and power are operational proxies.
- **RW0052 GreenFPGA** (2024, DAC): Operational energy from TDP and duty cycle.
- **RW0053 IdleSleep** (2024, ARCS (LNCS 14842)): Measured.
- **RW0054 SustHWSpec** (2024, ICCAD): Energy from synthesis/Aladdin.
- **RW0055 ASI** (2025, IEEE CAL): McPAT power.
- **RW0056 CATransformers** (2025, NeurIPS): Energy and carbon are objectives.
- **RW0057 CORDOBA** (2025, HPCA): Energy/operational carbon from simulator.
- **RW0058 HIPPO** (2025, ICCAD): Dynamic and total power are the prediction targets

PARTIAL: RW0008 HLSFactory, RW0043 DPRSurvey, RW0059 SustGap, RW0060 HLSToday
