# Gap / Overlap Matrix — HLS-DSE V23.2 (corrected 2026-09-25)

Built from the **canonical** Related Work set only: 11 CORE and
39 SUPPORTING papers (14 of them added by full-text review on 2026-09-25). HOLD papers were reviewed from the
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
| Multi-kernel / concurrent joint evaluation | PARTIAL OVERLAP | RW0003 MultiFPGAAlloc, RW0004 EnergyOptAlloc, RW0011 StreamHLS, RW0014 CoopBO, RW0031 Prometheus, RW0033 FIFOAdvisor, RW0037 FADO, RW0042 HLPSDSE, RW0050 EtoEDSE, RW0080 FADO2 | 8 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0015 VOISetBased, RW0022 HGBODSE | S07, S15, S65, S66 | Measured joint vs local selection outcomes on the same multi-kernel workload. |
| Measured multi-kernel interaction | PARTIAL OVERLAP | RW0011 StreamHLS, RW0033 FIFOAdvisor, RW0037 FADO, RW0042 HLPSDSE, RW0044 FOS | 21 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0015 VOISetBased, RW0022 HGBODSE | S02, S36–S42, S56 | Measured interaction effect (joint minus composed-local) with replication. |
| Evidence selection (adaptive acquisition) | KNOWN PRIOR ART | RW0006 CMMFO, RW0012 MTBO, RW0018 Chimera, RW0026 TaskTransfer, RW0042 HLPSDSE, RW0048 HLPow, RW0066 MISO, RW0068 CBOMIS, RW0069 CMFBO, RW0072 Prospector, RW0081 CMMFOJ, RW0085 ASPO | 12 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0015 VOISetBased, RW0016 VOISystemDesign, RW0022 HGBODSE | S05, S20, S22, S67 | Measured decision quality per unit of evidence cost, adaptive vs fixed policies. |
| Multi-fidelity / cost-aware evaluation | KNOWN PRIOR ART | RW0006 CMMFO, RW0009 HierQoR, RW0011 StreamHLS, RW0012 MTBO, RW0030 NLPDSE, RW0031 Prometheus, RW0032 Sisyphus, RW0033 FIFOAdvisor, RW0036 QoRML, RW0045 PLD, RW0046 Bonamy12DPR, RW0066 MISO, RW0068 CBOMIS, RW0069 CMFBO, RW0070 Fovea, RW0081 CMMFOJ | 24 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0015 VOISetBased, RW0022 HGBODSE | S04, S06, S21, S23 | Measured per-stage tool cost and fidelity error against a full-flow oracle. |
| Staged evaluation | KNOWN PRIOR ART | RW0001 CRYPTONITE, RW0006 CMMFO, RW0020 AutoHLS, RW0030 NLPDSE, RW0035 PatternDSE, RW0042 HLPSDSE, RW0045 PLD, RW0048 HLPow, RW0070 Fovea, RW0081 CMMFOJ | 20 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0015 VOISetBased, RW0016 VOISystemDesign, RW0022 HGBODSE | S88, S32 | Stage-decision records with measured stop/continue outcomes (false-stop rate). |
| Decision / Pareto stability | PARTIAL OVERLAP | RW0057 CORDOBA, RW0070 Fovea | 14 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0015 VOISetBased, RW0022 HGBODSE | S43–S46, S92 | Replicated runs/seeds with measured front and rank stability. |
| Physical implementation | KNOWN PRIOR ART | RW0006 CMMFO, RW0008 HLSFactory, RW0009 HierQoR, RW0031 Prometheus, RW0036 QoRML, RW0042 HLPSDSE, RW0043 DPRSurvey, RW0044 FOS, RW0045 PLD, RW0046 Bonamy12DPR, RW0047 Nafkha17DPR, RW0048 HLPow, RW0053 IdleSleep, RW0072 Prospector, RW0079 ZyCAP, RW0080 FADO2, RW0081 CMMFOJ, RW0084 SeedTiming | 7 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0022 HGBODSE | S59–S61, S78, S81 | Post-route reports as raw artifacts per candidate. |
| Lifecycle / configuration cost | PARTIAL OVERLAP | RW0043 DPRSurvey, RW0044 FOS, RW0045 PLD, RW0046 Bonamy12DPR, RW0047 Nafkha17DPR, RW0052 GreenFPGA, RW0053 IdleSleep, RW0057 CORDOBA, RW0079 ZyCAP | 6 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0015 VOISetBased, RW0016 VOISystemDesign, RW0022 HGBODSE | S85, S86, S94 | Measured build, programming and invocation cost (programming needs hardware: NOT_AVAILABLE). |
| Multi-benchmark transfer | KNOWN PRIOR ART | RW0009 HierQoR, RW0010 CollectiveHLS, RW0012 MTBO, RW0019 GNNDSE, RW0021 HARP, RW0023 HLSyn, RW0026 TaskTransfer, RW0048 HLPow, RW0071 SoberDSE | 13 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0015 VOISetBased, RW0022 HGBODSE | S10, S11, S90 | Held-out benchmark evaluation under the data-leakage contract. |
| Power / energy | KNOWN PRIOR ART | RW0004 EnergyOptAlloc, RW0006 CMMFO, RW0046 Bonamy12DPR, RW0047 Nafkha17DPR, RW0048 HLPow, RW0050 EtoEDSE, RW0052 GreenFPGA, RW0053 IdleSleep, RW0057 CORDOBA, RW0065 PGDSE | 4 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0022 HGBODSE | S19, S20 | Measured power/energy kept separate from estimates. |
| CPU–FPGA interaction | PARTIAL OVERLAP | RW0044 FOS, RW0053 IdleSleep, RW0079 ZyCAP | 10 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0022 HGBODSE | S83, S84 | Measured end-to-end latency/overlap (hardware NOT_AVAILABLE). |
| Memory / data movement | KNOWN PRIOR ART | RW0003 MultiFPGAAlloc, RW0004 EnergyOptAlloc, RW0030 NLPDSE, RW0031 Prometheus, RW0032 Sisyphus, RW0033 FIFOAdvisor, RW0044 FOS, RW0063 COSMOS | 27 | RW0002 MVSym, RW0005 DML, RW0007 IronManPro, RW0022 HGBODSE | S73 | Measured data movement; DMA/ACP/cache stay UNKNOWN_UNTIL_MEASURED. |

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
- **RW0080 FADO2** (CORE, full text 2026-09-25): directives for all kernels co-selected under shared per-slot constraints; whole design synthesized and implemented

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
- **RW0066 MISO** (SUPPORTING, full text 2026-09-25): cost-sensitive knowledge gradient over (source, design), Eq. 1
- **RW0068 CBOMIS** (SUPPORTING, full text 2026-09-25): constrained max-value entropy search / source cost in a trust region
- **RW0069 CMFBO** (SUPPORTING, full text 2026-09-25): heuristic cost-scaled constrained EI-style
- **RW0072 Prospector** (SUPPORTING, full text 2026-09-25): multi-objective BO with PESMO
- **RW0081 CMMFOJ** (CORE, full text 2026-09-25): per-stage cost-penalized EIPV, argmax over (x, stage)
- **RW0085 ASPO** (SUPPORTING, full text 2026-09-25): cost-aware EI divided by lambda(t)*c_hat(x) plus constraint-aware optimisation (cooling ineffective as written)

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
- **RW0066 MISO** (SUPPORTING, full text 2026-09-25): per-source cost, noise and discrepancy GP
- **RW0068 CBOMIS** (SUPPORTING, full text 2026-09-25): lambda(x,l), discrepancy GP, rho-based variance correction
- **RW0069 CMFBO** (SUPPORTING, full text 2026-09-25): see registry row and note for the evidence
- **RW0070 Fovea** (SUPPORTING, full text 2026-09-25): ~4000x cost gap, disagreement bound, full runtime accounting
- **RW0081 CMMFOJ** (CORE, full text 2026-09-25): rho_i = T_impl/T_i and non-linear multi-fidelity GP

### Staged evaluation

- **RW0001 CRYPTONITE** (SUPPORTING): Analytical QoR estimator prunes candidates before HLS synthesis; Pareto feedback loop.
- **RW0006 CMMFO** (CORE): Three fidelities (HLS, Synth, Impl); each candidate run only up to chosen fidelity h.
- **RW0020 AutoHLS** (SUPPORTING): ML failure/resource predictor screens BO samples before full HLS synthesis.
- **RW0030 NLPDSE** (SUPPORTING): NLP lower bound used to rank/prune before HLS synthesis
- **RW0035 PatternDSE** (SUPPORTING): LLVM execution check -> HLS C codegen check -> estimator ranking -> Vitis HLS on top-k.
- **RW0042 HLPSDSE** (SUPPORTING): FSM of ordered actions; each stage builds on best result of the previous
- **RW0045 PLD** (SUPPORTING): -O0 / -O1 / -O3 levels provide progressively slower but higher-quality compile paths.
- **RW0048 HLPow** (SUPPORTING): HLS runs + learned power model replace RTL implementation/measurement for most points.
- **RW0070 Fovea** (SUPPORTING, full text 2026-09-25): formulation, analytical screening, calibration, reference evaluation
- **RW0081 CMMFOJ** (CORE, full text 2026-09-25): hls/syn/impl stages, run up to a selected stage h

### Decision / Pareto stability

- **RW0057 CORDOBA** (SUPPORTING): Optimal design robustness across lifetime and carbon-intensity uncertainty analysed.
- **RW0070 Fovea** (SUPPORTING, full text 2026-09-25): exact recovery over 20 calibration draws per pair

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
- **RW0072 Prospector** (SUPPORTING, full text 2026-09-25): place-and-route per evaluated design
- **RW0079 ZyCAP** (SUPPORTING, full text 2026-09-25): measured on ZedBoard with a PR floorplan
- **RW0080 FADO2** (CORE, full text 2026-09-25): SLR floorplan in the loop; post-implementation Fmax on U250
- **RW0081 CMMFOJ** (CORE, full text 2026-09-25): Vivado implementation reports at the impl stage on VC707
- **RW0084 SeedTiming** (SUPPORTING, full text 2026-09-25): post-route STA over 30 place-and-route seeds

### Lifecycle / configuration cost

- **RW0043 DPRSurvey** (SUPPORTING): Central topic: reconfiguration time, bitstream size/compression, controller throughput, PR tool runtime.
- **RW0044 FOS** (SUPPORTING): Compile time, component update/re-initialisation latency and PR swap latency quantified (Table 5).
- **RW0045 PLD** (SUPPORTING): Compile/turnaround cost is the core subject; partial bitstream loading used.
- **RW0046 Bonamy12DPR** (SUPPORTING): Reconfiguration energy/time is the subject.
- **RW0047 Nafkha17DPR** (SUPPORTING): Reconfiguration time/power overhead measured.
- **RW0052 GreenFPGA** (SUPPORTING): Full lifecycle CFP including reconfiguration/app-development/configuration time.
- **RW0053 IdleSleep** (SUPPORTING): Configuration energy and on/off vs idle lifecycle central.
- **RW0057 CORDOBA** (SUPPORTING): Embodied vs operational carbon over hardware lifetime is central.
- **RW0079 ZyCAP** (SUPPORTING, full text 2026-09-25): reconfiguration throughput, bitstream sizes, caching/prefetch, blocking vs overlapped (Tables I-II, Fig. 5)

### Multi-benchmark transfer

- **RW0009 HierQoR** (SUPPORTING): DSE on four unseen applications
- **RW0010 CollectiveHLS** (SUPPORTING): Core idea: transfer directive knowledge across applications; leave-one-out and knowledge-base ablation (Sec. 5.8).
- **RW0012 MTBO** (SUPPORTING): Transfer across datasets (USPS->MNIST, CIFAR-10->SVHN/STL-10, shifted Branin).
- **RW0019 GNNDSE** (SUPPORTING): Generalization to 4 unseen PolyBench kernels
- **RW0021 HARP** (SUPPORTING): Transfer from SDx 2018.3 to Vitis 2020.2
- **RW0023 HLSyn** (SUPPORTING): Held-out kernels with zero-shot and few-shot adaptation
- **RW0026 TaskTransfer** (SUPPORTING): Transfer across toolchain versions and across programs (domain transfer)
- **RW0048 HLPow** (SUPPORTING): Power model trained on 15 apps and tested on 7 unseen PolyBench apps.
- **RW0071 SoberDSE** (SUPPORTING, full text 2026-09-25): disjoint training (20) and inference (9) kernels

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
- **RW0065 PGDSE** (CORE, full text 2026-09-25): primary objective via frequency-scaled power x time model

### CPU–FPGA interaction

- **RW0044 FOS** (SUPPORTING): Linux/ARM host runtime and drivers manage accelerators; offloading scenarios.
- **RW0053 IdleSleep** (SUPPORTING): MCU-FPGA SPI configuration and offloading.
- **RW0079 ZyCAP** (SUPPORTING, full text 2026-09-25): PS-PL interfaces, processor blocking vs overlap, 140 ns access latency

### Memory / data movement

- **RW0003 MultiFPGAAlloc** (SUPPORTING): Per-FPGA DRAM bandwidth constraint in the model.
- **RW0004 EnergyOptAlloc** (SUPPORTING): DDR bandwidth, PCIe transfer time and input data replication modeled.
- **RW0030 NLPDSE** (SUPPORTING): Off-chip to on-chip transfer, tiling/caching and burst width modeled
- **RW0031 Prometheus** (CORE): Off-chip transfers, tiling, reuse, bit width, double buffering modeled
- **RW0032 Sisyphus** (SUPPORTING): Models off-chip/on-chip transfers, tiling for on-chip caching, burst width
- **RW0033 FIFOAdvisor** (CORE): FIFO buffering/BRAM memory usage is the optimized quantity
- **RW0044 FOS** (SUPPORTING): AXI port throughput characterized; memory contention observed.
- **RW0063 COSMOS** (CORE, full text 2026-09-25): datapath/PLM co-design is central; interconnect bandwidth fixed

## 5. Addendum 2026-09-25 — web-search additions

23 papers were added from a web search (RW0063–RW0085). **14 were then reviewed in full text** and entered the
canonical set (their YES dimensions are merged into §1 and §4 above); the other 9 remain HOLD (abstract only; for 4 of
them no legitimate open copy was found). Full-text findings that move prior-art boundaries:

| Boundary | Papers (full text) | What the full text shows | Consequence |
|---|---|---|---|
| Compositional (local-first) system-level HLS DSE | RW0064 CompSLD12, RW0063 COSMOS, RW0065 PGDSE (all CORE) | Per-component dominance/Pareto pruning plus additive or TMG composition (sum of areas; throughput from cycle time). None of the three ever synthesizes or implements the composed system; their accuracy numbers (1–13% mismatch, "ADRS 0") compare composed plans with composed results. PG-DSE's "lossless pruning" is verified against exhaustive search on one 27-alternative synthetic system only. | The compositional assumption is prior art **and untested against joint evidence** → S97. |
| Joint co-resident directive optimization with implementation | RW0080 FADO 2.0 (CORE) | Additive per-slot resources + max/sum latency; slot cap had to be tightened 70%→65% because summed HLS QoR still failed placement/routing; implementation failures in Table 6; single runs, ~9% Fmax differences. | Strongest published sign that composed-local ≠ joint post-route, never quantified → S98. |
| Stage-selective (multi-fidelity) HLS evidence acquisition | RW0081 CMMFO journal (CORE), with RW0006 | Cost-penalized EIPV over (configuration, hls/syn/impl stage) for single kernels; normalized ADRS 0.34 (DCGP). | Stage selection is prior art; S99's new element must be local-vs-joint across co-resident kernels. |
| Multi-information-source VOI | RW0066 MISO, RW0068 CBOMIS, RW0069 CMFBO (SUPPORTING) | Cost-normalized knowledge gradient with additive source discrepancy f(l,x)=f(0,x)+δ_l(x) (MISO); constrained entropy search with correlation-based variance inflation (CBOMIS). All single-objective; none handles one evaluation informing several components, Pareto targets, or crashed runs. | Method foundation for S99; the gaps listed are what S99 must add. |
| Decision-domain cross-fidelity refinement in hardware DSE | RW0070 Fovea (SUPPORTING) | Reference evaluation only inside a domain guaranteed to contain the reference optimum if the measured disagreement bound holds; 1400/1400 exact recoveries; single objective, one-shot. | Direct precedent for "buy expensive evidence only if it can change the decision"; S99 needs the Pareto/multi-kernel version and S98 must report worst-case residuals. |
| Search-algorithm comparison | RW0071 SoberDSE, RW0072 Prospector (SUPPORTING) | SoberDSE's "no algorithm dominates" rests on single runs on a GNN surrogate with a self-referential reference set; Prospector: PESMO BO 1.74x closer to exhaustive fronts on small single-kernel spaces. | S72 remains supporting; it must rank algorithms at equal budget, with seeds, against the S04 oracle. |
| Tool noise and configuration cost | RW0084 SeedTiming, RW0079 ZyCAP, RW0085 ASPO (SUPPORTING) | 30 seeds → ~8% peak-to-peak Fmax on 20 nm UltraScale (internally inconsistent statistics); ZedBoard PCAP 128 MB/s, ICAP-DMA 382 MB/s, full xc7z020 bitstream 4,045,564 B; checkpoint reuse saves 20–33% per synthesis. | S81 must measure its own noise floor on xc7z020; configuration time (ms) is negligible next to build time (min–h). |

Still true after the full-text review: no paper in the collection reports a kernel's post-route QoR alone vs
co-resident, or uses a local-vs-joint choice as an acquisition decision. This is a statement about the current
collection, not a novelty claim; the remaining HOLD papers and the systematic review RW0083 still need checking.
