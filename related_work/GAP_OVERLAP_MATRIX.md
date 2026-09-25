# Gap / Overlap Matrix — HLS-DSE V23.2 (corrected 2026-09-25)

Built from the **canonical** Related Work set only: 6 CORE and
30 SUPPORTING papers. The 6 HOLD papers were reviewed from the
abstract only and appear as NOT REVIEWED. ADJACENT and EXCLUDED papers (`EXCLUSION_REGISTER.csv`) are not used.

This matrix exposes overlap. **It makes no novelty claim**, and the collection is **not a systematic review**.
An empty cell means: *No directly matching work identified in the current reviewed collection. Additional systematic search required.* It does not mean that no prior work exists.

Status vocabulary:
- `KNOWN PRIOR ART`: at least one canonical paper reports the dimension (YES) and is classified PRIOR ART.
- `PARTIAL OVERLAP`: canonical papers report the dimension (YES) in a different setting.
- `POTENTIAL OVERLAP`: only PARTIAL evidence exists.
- `POTENTIAL GAP`: nothing matches in the reviewed collection; additional search is required.
- `UNRESOLVED`: evidence exists only in HOLD papers.
- `NOT REVIEWED`: HOLD papers that may be relevant.

## 1. Dimension matrix

| Dimension | Status | Canonical papers reporting it (YES) | PARTIAL (count) | NOT REVIEWED (HOLD, YES/PARTIAL/NOT_REPORTED) | Our Studies | Evidence required from us |
|---|---|---|---|---|---|---|
| Multi-kernel / concurrent joint evaluation | PARTIAL OVERLAP | RW0003 MultiFPGAAlloc, RW0004 EnergyOptAlloc, RW0011 StreamHLS, RW0014 CoopBO, RW0031 Prometheus, RW0033 FIFOAdvisor, RW0037 FADO, RW0042 HLPSDSE, RW0050 EtoEDSE | 4 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0015 VOISetBased, RW0022 HGBODSE | S07, S15, S65, S66 | Measured joint vs local selection outcomes on the same multi-kernel workload. |
| Measured multi-kernel interaction | PARTIAL OVERLAP | RW0011 StreamHLS, RW0033 FIFOAdvisor, RW0037 FADO, RW0042 HLPSDSE, RW0044 FOS | 19 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0015 VOISetBased, RW0022 HGBODSE | S02, S36–S42, S56 | Measured interaction effect (joint minus composed-local) with replication. |
| Evidence selection (adaptive acquisition) | KNOWN PRIOR ART | RW0006 CMMFO, RW0012 MTBO, RW0018 Chimera, RW0026 TaskTransfer, RW0042 HLPSDSE, RW0048 HLPow | 8 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0015 VOISetBased, RW0016 VOISystemDesign, RW0022 HGBODSE | S05, S20, S22, S67 | Measured decision quality per unit of evidence cost, adaptive vs fixed policies. |
| Multi-fidelity / cost-aware evaluation | KNOWN PRIOR ART | RW0006 CMMFO, RW0009 HierQoR, RW0011 StreamHLS, RW0012 MTBO, RW0030 NLPDSE, RW0031 Prometheus, RW0032 Sisyphus, RW0033 FIFOAdvisor, RW0036 QoRML, RW0045 PLD, RW0046 Bonamy12DPR | 19 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0015 VOISetBased, RW0022 HGBODSE | S04, S06, S21, S23 | Measured per-stage tool cost and fidelity error against a full-flow oracle. |
| Staged evaluation | KNOWN PRIOR ART | RW0001 CRYPTONITE, RW0006 CMMFO, RW0020 AutoHLS, RW0030 NLPDSE, RW0035 PatternDSE, RW0042 HLPSDSE, RW0045 PLD, RW0048 HLPow | 13 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0015 VOISetBased, RW0016 VOISystemDesign, RW0022 HGBODSE | S88, S32 | Stage-decision records with measured stop/continue outcomes (false-stop rate). |
| Decision / Pareto stability | PARTIAL OVERLAP | RW0057 CORDOBA | 11 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0015 VOISetBased, RW0022 HGBODSE | S43–S46, S92 | Replicated runs/seeds with measured front and rank stability. |
| Physical implementation | KNOWN PRIOR ART | RW0006 CMMFO, RW0008 HLSFactory, RW0009 HierQoR, RW0031 Prometheus, RW0036 QoRML, RW0042 HLPSDSE, RW0043 DPRSurvey, RW0044 FOS, RW0045 PLD, RW0046 Bonamy12DPR, RW0047 Nafkha17DPR, RW0048 HLPow, RW0053 IdleSleep | 5 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0022 HGBODSE | S59–S61, S78, S81 | Post-route reports as raw artifacts per candidate. |
| Lifecycle / configuration cost | PARTIAL OVERLAP | RW0043 DPRSurvey, RW0044 FOS, RW0045 PLD, RW0046 Bonamy12DPR, RW0047 Nafkha17DPR, RW0052 GreenFPGA, RW0053 IdleSleep, RW0057 CORDOBA | 4 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0015 VOISetBased, RW0016 VOISystemDesign, RW0022 HGBODSE | S85, S86, S94 | Measured build, programming and invocation cost (programming needs hardware: NOT_AVAILABLE). |
| Multi-benchmark transfer | KNOWN PRIOR ART | RW0009 HierQoR, RW0010 CollectiveHLS, RW0012 MTBO, RW0019 GNNDSE, RW0021 HARP, RW0023 HLSyn, RW0026 TaskTransfer, RW0048 HLPow | 8 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0015 VOISetBased, RW0022 HGBODSE | S10, S11, S90 | Held-out benchmark evaluation under the data-leakage contract. |
| Power / energy | KNOWN PRIOR ART | RW0004 EnergyOptAlloc, RW0006 CMMFO, RW0046 Bonamy12DPR, RW0047 Nafkha17DPR, RW0048 HLPow, RW0050 EtoEDSE, RW0052 GreenFPGA, RW0053 IdleSleep, RW0057 CORDOBA | 2 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0022 HGBODSE | S19, S20 | Measured power/energy kept separate from estimates. |
| CPU–FPGA interaction | PARTIAL OVERLAP | RW0044 FOS, RW0053 IdleSleep | 9 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0022 HGBODSE | S83, S84 | Measured end-to-end latency/overlap (hardware NOT_AVAILABLE). |
| Memory / data movement | KNOWN PRIOR ART | RW0003 MultiFPGAAlloc, RW0004 EnergyOptAlloc, RW0030 NLPDSE, RW0031 Prometheus, RW0032 Sisyphus, RW0033 FIFOAdvisor, RW0044 FOS | 19 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0022 HGBODSE | S73 | Measured data movement; DMA/ACP/cache stay UNKNOWN_UNTIL_MEASURED. |

## 2. Prior-art boundary check

Labels: `PRIOR ART`, `PARTIAL OVERLAP`, `METHOD FOUNDATIONAL`, `RELEVANT BUT DIFFERENT`, `UNRESOLVED`. The purpose is to
prevent false novelty claims, not to establish novelty.

| Topic | Papers (label) | Boundary note |
|---|---|---|
| Multi-fidelity HLS DSE | RW0006 CMMFO (PRIOR ART); RW0009 HierQoR (METHOD FOUNDATIONAL); RW0036 QoRML (METHOD FOUNDATIONAL) | CMMFO selects configuration and fidelity jointly with a cost-penalized acquisition, but optimizes each benchmark independently (joint evaluation: NO). |
| Multi-task BO | RW0012 MTBO (METHOD FOUNDATIONAL); RW0026 TaskTransfer (PARTIAL OVERLAP) | Cross-task evidence sharing exists; TaskTransfer transfers across HLS programs but runs DSE per program. |
| Cost-aware BO | RW0006 CMMFO (PRIOR ART); RW0012 MTBO (METHOD FOUNDATIONAL) | Cost-weighted acquisition is established. |
| Value of information | RW0015 VOISetBased (UNRESOLVED); RW0016 VOISystemDesign (UNRESOLVED) | Both VOI papers are HOLD (abstract only). No HLS-specific VOI paper was identified in the current collection; additional systematic search required. |
| Constrained MOBO | RW0013 CMOBOOCE (METHOD FOUNDATIONAL) | Optimistic constraint estimation for multi-objective BO. |
| Feasibility-aware acquisition | RW0013 CMOBOOCE (METHOD FOUNDATIONAL); RW0014 CoopBO (METHOD FOUNDATIONAL); RW0018 Chimera (PARTIAL OVERLAP) | Probability-of-feasibility and timeout/error prediction exist; stage-specific HLS feasibility semantics were not found. |
| Joint / concurrent multi-kernel optimization | RW0011 StreamHLS (PARTIAL OVERLAP); RW0031 Prometheus (PARTIAL OVERLAP); RW0037 FADO (PARTIAL OVERLAP); RW0033 FIFOAdvisor (PARTIAL OVERLAP); RW0050 EtoEDSE (PARTIAL OVERLAP); RW0003 MultiFPGAAlloc (RELEVANT BUT DIFFERENT); RW0001 CRYPTONITE (RELEVANT BUT DIFFERENT); RW0002 MVSym (UNRESOLVED) | These optimize kernels of ONE design jointly under shared resources (analytical models or heuristics). Whether any selects evidence jointly across concurrently deployed benchmarks: none identified in the current collection. |
| Multi-benchmark transfer | RW0026 TaskTransfer (PARTIAL OVERLAP); RW0019 GNNDSE (PRIOR ART); RW0021 HARP (METHOD FOUNDATIONAL); RW0023 HLSyn (METHOD FOUNDATIONAL) | Cross-program surrogate generalization is established. |
| Physical-aware HLS DSE | RW0037 FADO (PARTIAL OVERLAP); RW0042 HLPSDSE (RELEVANT BUT DIFFERENT); RW0036 QoRML (METHOD FOUNDATIONAL) | Floorplan-aware and post-route-in-the-loop DSE exist. |
| Configuration / DFX-aware optimization | RW0045 PLD (RELEVANT BUT DIFFERENT); RW0044 FOS (RELEVANT BUT DIFFERENT); RW0043 DPRSurvey (METHOD FOUNDATIONAL); RW0053 IdleSleep (RELEVANT BUT DIFFERENT); RW0005 DML (UNRESOLVED) | Reconfiguration and compile cost are measured; configuration strategy as a DSE decision variable was not found in the current collection. |
| CPU/FPGA runtime optimization | RW0044 FOS (RELEVANT BUT DIFFERENT); RW0053 IdleSleep (RELEVANT BUT DIFFERENT); RW0002 MVSym (UNRESOLVED) | Runtime systems exist; MVSym needs its full text. |
| Evidence reuse / caching | RW0026 TaskTransfer (PARTIAL OVERLAP); RW0012 MTBO (METHOD FOUNDATIONAL) | Model-level transfer exists. Reuse of cached tool results across decisions: no directly matching work identified in the current reviewed collection; additional systematic search required. |
| Staged evaluation | RW0006 CMMFO (PARTIAL OVERLAP); RW0020 AutoHLS (PARTIAL OVERLAP); RW0035 PatternDSE (PARTIAL OVERLAP); RW0030 NLPDSE (PARTIAL OVERLAP); RW0045 PLD (RELEVANT BUT DIFFERENT) | Pruning and fidelity-staged evaluation exist. |
| Early stopping | — | Early termination of an in-progress tool run was not verified in any review (the earlier keyword screen was not reliable). No directly matching work identified in the current reviewed collection; additional systematic search required. |

## 3. Corrections relative to the 6a08f53 version

- Built from CORE + SUPPORTING only. The earlier version counted ADJACENT and later-excluded papers.
- The "Overlap risk" count heuristic was removed and replaced by the status vocabulary above.
- The keyword-screen rows ("Multi-objective DSE", "Early stopping", "Decision-centric acquisition") were removed.
  They produced unverified matches. Early stopping is now stated as not verified.
- Empty cells now carry the systematic-search caveat instead of implying absence of prior work.

## 4. Appendix — evidence per dimension (canonical papers, YES)

### Multi-kernel / concurrent joint evaluation

- **RW0003 MultiFPGAAlloc** (SUPPORTING): All kernels' CU counts and placements are optimized jointly under shared per-FPGA constraints.
- **RW0004 EnergyOptAlloc** (SUPPORTING): All kernels' CU counts, placements, and FPGA frequencies optimized jointly.
- **RW0011 StreamHLS** (CORE): All kernels (nodes) of a multi-kernel application scheduled jointly under a global DSP budget
- **RW0014 CoopBO** (SUPPORTING): Component subproblems optimized separately but every high-fidelity evaluation is of the full coupled multi-stage system.
- **RW0031 Prometheus** (CORE): All tasks/statements of a program optimized jointly in one NLP including per-SLR placement
- **RW0033 FIFOAdvisor** (CORE): All FIFOs of a multi-task dataflow design are sized jointly with whole-design latency
- **RW0037 FADO** (CORE): Multiple dataflow and non-dataflow kernels in one design co-optimized under shared per-die resource constraints.
- **RW0042 HLPSDSE** (SUPPORTING): Whole multi-module accelerator is floorplanned and implemented jointly
- **RW0050 EtoEDSE** (CORE): Component alternatives combined and evaluated at system level under EtoE latency.

### Measured multi-kernel interaction

- **RW0011 StreamHLS** (CORE): Graph-level pipelining interactions between producer/consumer nodes modeled and ablated (Opt2-Opt5)
- **RW0033 FIFOAdvisor** (CORE): Inter-task FIFO effects (stalls, deadlocks) captured via simulation
- **RW0037 FADO** (CORE): Cross-kernel resource contention per slot, die-crossing timing, and latency bottleneck across functions explicitly modeled.
- **RW0042 HLPSDSE** (SUPPORTING): Physical interactions between modules (congestion, crossings, SLL use) measured from post-route results
- **RW0044 FOS** (SUPPORTING): Measured co-execution effects, e.g., memory-bank contention in Mandelbrot x Sobel scenarios.

### Evidence selection (adaptive acquisition)

- **RW0006 CMMFO** (CORE): Per iteration selects (configuration, fidelity) pair maximizing penalized EIPV.
- **RW0012 MTBO** (SUPPORTING): Cost-sensitive multi-task entropy search chooses which task/fold to query; fast CV chooses which fold.
- **RW0018 Chimera** (SUPPORTING): Active learning with probabilistic evaluation and Thompson-sampling switching between proposal engines.
- **RW0026 TaskTransfer** (SUPPORTING): Active learning (coreset) selects which designs to synthesize each CEM iteration
- **RW0042 HLPSDSE** (SUPPORTING): Metrics from prior implementations guide the next parameter choices
- **RW0048 HLPow** (SUPPORTING): SDR-guided sampling selects which design points to run through HLS.

### Multi-fidelity / cost-aware evaluation

- **RW0006 CMMFO** (CORE): Non-linear multi-fidelity GP plus acquisition penalty proportional to T_impl/T_i stage runtime.
- **RW0009 HierQoR** (SUPPORTING): Predicts high-fidelity post-route QoR from source to avoid HLS+implementation cost
- **RW0011 StreamHLS** (CORE): Analytical dataflow performance model validated vs RTL simulation
- **RW0012 MTBO** (SUPPORTING): Evaluation cost c_t(x) modeled by multi-task GP on log cost; information gain per unit cost.
- **RW0030 NLPDSE** (SUPPORTING): Analytical lower-bound model versus expensive HLS runs; bound tightness evaluated
- **RW0031 Prometheus** (CORE): Analytical latency/resource cost model in NLP
- **RW0032 Sisyphus** (SUPPORTING): Analytical latency/resource model embedded in NLP; prediction error reported
- **RW0033 FIFOAdvisor** (CORE): Cheap simulator vs co-simulation runtime quantified
- **RW0036 QoRML** (SUPPORTING): Explicitly models the gap between low-fidelity HLS estimates and high-fidelity implementation results
- **RW0045 PLD** (SUPPORTING): Compile time vs performance trade-off quantified per level.
- **RW0046 Bonamy12DPR** (SUPPORTING): Three model granularities with accuracy/complexity trade-off.

### Staged evaluation

- **RW0001 CRYPTONITE** (SUPPORTING): Analytical QoR estimator prunes candidates before HLS synthesis; Pareto feedback loop.
- **RW0006 CMMFO** (CORE): Three fidelities (HLS, Synth, Impl); each candidate run only up to chosen fidelity h.
- **RW0020 AutoHLS** (SUPPORTING): ML failure/resource predictor screens BO samples before full HLS synthesis.
- **RW0030 NLPDSE** (SUPPORTING): NLP lower bound used to rank/prune before HLS synthesis
- **RW0035 PatternDSE** (SUPPORTING): LLVM execution check -> HLS C codegen check -> estimator ranking -> Vitis HLS on top-k.
- **RW0042 HLPSDSE** (SUPPORTING): FSM of ordered actions; each stage builds on best result of the previous
- **RW0045 PLD** (SUPPORTING): -O0 / -O1 / -O3 levels provide progressively slower but higher-quality compile paths.
- **RW0048 HLPow** (SUPPORTING): HLS runs + learned power model replace RTL implementation/measurement for most points.

### Decision / Pareto stability

- **RW0057 CORDOBA** (SUPPORTING): Optimal design robustness across lifetime and carbon-intensity uncertainty analysed.

### Physical implementation

- **RW0006 CMMFO** (CORE): Implementation-stage (place-and-route) reports are the highest fidelity in the loop; illegal P&R designs penalized.
- **RW0008 HLSFactory** (SUPPORTING): Vivado implementation (placed-and-routed) reports collected for datasets.
- **RW0009 HierQoR** (SUPPORTING): Resource labels and exact Pareto sets from post-route implementation
- **RW0031 Prometheus** (CORE): Bitstreams generated and run on board, including 3-SLR designs
- **RW0036 QoRML** (SUPPORTING): Labels are post-implementation (place and route) resource and timing
- **RW0042 HLPSDSE** (SUPPORTING): Every candidate is placed and routed
- **RW0043 DPRSurvey** (SUPPORTING): Floorplanning, PR region shaping, bitstream generation discussed.
- **RW0044 FOS** (SUPPORTING): Relocatable PR bitstreams built and run on boards.
- **RW0045 PLD** (SUPPORTING): Full place & route and bitstream per page; on-board execution.
- **RW0046 Bonamy12DPR** (SUPPORTING): Real bitstreams on hardware.
- **RW0047 Nafkha17DPR** (SUPPORTING): Real partial bitstreams on hardware.
- **RW0048 HLPow** (SUPPORTING): Training/ground-truth power from implemented designs measured on board.
- **RW0053 IdleSleep** (SUPPORTING): Real bitstreams on hardware.

### Lifecycle / configuration cost

- **RW0043 DPRSurvey** (SUPPORTING): Central topic: reconfiguration time, bitstream size/compression, controller throughput, PR tool runtime.
- **RW0044 FOS** (SUPPORTING): Compile time, component update/re-initialisation latency and PR swap latency quantified (Table 5).
- **RW0045 PLD** (SUPPORTING): Compile/turnaround cost is the core subject; partial bitstream loading used.
- **RW0046 Bonamy12DPR** (SUPPORTING): Reconfiguration energy/time is the subject.
- **RW0047 Nafkha17DPR** (SUPPORTING): Reconfiguration time/power overhead measured.
- **RW0052 GreenFPGA** (SUPPORTING): Full lifecycle CFP including reconfiguration/app-development/configuration time.
- **RW0053 IdleSleep** (SUPPORTING): Configuration energy and on/off vs idle lifecycle central.
- **RW0057 CORDOBA** (SUPPORTING): Embodied vs operational carbon over hardware lifetime is central.

### Multi-benchmark transfer

- **RW0009 HierQoR** (SUPPORTING): DSE on four unseen applications
- **RW0010 CollectiveHLS** (SUPPORTING): Core idea: transfer directive knowledge across applications; leave-one-out and knowledge-base ablation (Sec. 5.8).
- **RW0012 MTBO** (SUPPORTING): Transfer across datasets (USPS->MNIST, CIFAR-10->SVHN/STL-10, shifted Branin).
- **RW0019 GNNDSE** (SUPPORTING): Generalization to 4 unseen PolyBench kernels
- **RW0021 HARP** (SUPPORTING): Transfer from SDx 2018.3 to Vitis 2020.2
- **RW0023 HLSyn** (SUPPORTING): Held-out kernels with zero-shot and few-shot adaptation
- **RW0026 TaskTransfer** (SUPPORTING): Transfer across toolchain versions and across programs (domain transfer)
- **RW0048 HLPow** (SUPPORTING): Power model trained on 15 apps and tested on 7 unseen PolyBench apps.

### Power / energy

- **RW0004 EnergyOptAlloc** (SUPPORTING): Objective is total power (static+dynamic), estimated.
- **RW0006 CMMFO** (CORE): Power is one of three objectives (tool-reported).
- **RW0046 Bonamy12DPR** (SUPPORTING): Measured.
- **RW0047 Nafkha17DPR** (SUPPORTING): Measured.
- **RW0048 HLPow** (SUPPORTING): Power is the modeled objective with latency-power Pareto DSE.
- **RW0050 EtoEDSE** (CORE): Energy is a primary objective (weighted 2:1 over area in fitness).
- **RW0052 GreenFPGA** (SUPPORTING): Operational energy from TDP and duty cycle.
- **RW0053 IdleSleep** (SUPPORTING): Measured.
- **RW0057 CORDOBA** (SUPPORTING): Energy/operational carbon from simulator.

### CPU–FPGA interaction

- **RW0044 FOS** (SUPPORTING): Linux/ARM host runtime and drivers manage accelerators; offloading scenarios.
- **RW0053 IdleSleep** (SUPPORTING): MCU-FPGA SPI configuration and offloading.

### Memory / data movement

- **RW0003 MultiFPGAAlloc** (SUPPORTING): Per-FPGA DRAM bandwidth constraint in the model.
- **RW0004 EnergyOptAlloc** (SUPPORTING): DDR bandwidth, PCIe transfer time and input data replication modeled.
- **RW0030 NLPDSE** (SUPPORTING): Off-chip to on-chip transfer, tiling/caching and burst width modeled
- **RW0031 Prometheus** (CORE): Off-chip transfers, tiling, reuse, bit width, double buffering modeled
- **RW0032 Sisyphus** (SUPPORTING): Models off-chip/on-chip transfers, tiling for on-chip caching, burst width
- **RW0033 FIFOAdvisor** (CORE): FIFO buffering/BRAM memory usage is the optimized quantity
- **RW0044 FOS** (SUPPORTING): AXI port throughput characterized; memory contention observed.

## 5. Addendum 2026-09-25 — web-search additions (HOLD, abstract-only; not used in the matrix above)

The matrix above is built from canonical papers only and is unchanged. The web search added 23 HOLD papers
(RW0063–RW0085). They do not change any status cell until their full text is reviewed, but they move three
prior-art boundaries that any claim must respect:

| Boundary | HOLD papers | Consequence |
|---|---|---|
| Compositional (local-Pareto-first) system-level HLS DSE is an established line | RW0064 CompSLD12 (DATE 2012), RW0063 COSMOS (TECS 2017), RW0065 PGDSE (ASP-DAC 2023), with RW0050 EtoEDSE | "Joint vs local" is not a new framing; what remains open is an oracle test of the compositional assumption (S97) and measured residuals (S98). |
| Value-of-information / multi-information-source acquisition exists as a method | RW0066 MISO (NeurIPS 2017), RW0067 MISCBO, RW0068 CBOMIS, RW0069 CMFBO; decision-domain refinement in hardware DSE: RW0070 Fovea | The acquisition rule of S99 must be positioned as an application/extension of these, not as a new VOI method. |
| Co-residence changes runtime on FPGA SoCs | RW0075, RW0076, RW0077 (Zynq-7000 traces), RW0078 (XC7Z020 ACP/HP) | Runtime joint≠local is documented; using it inside an HLS DSE decision (S100) is not found in the collection. Hardware required. |

Search-algorithm comparison (S72) gains further prior art: RW0071 SoberDSE, RW0072 Prospector, RW0073 KuangMOBO.
No paper in the collection was found that (a) reports a kernel's post-route QoR alone vs co-resident, or (b) uses a
local-vs-joint choice as an acquisition decision. This remains a statement about the current collection, not a
novelty claim; the systematic review RW0083 is the next source to check.
