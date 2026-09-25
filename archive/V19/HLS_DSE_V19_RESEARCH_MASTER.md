<!-- Historical: split verbatim out of REPORTS/R07_Research_Extensions.md (V19 research master). Read-only. Its §27 study map predates contracts/STUDY_ID_REGISTRY.yaml; S07-S27 meanings differ from the registry. -->

# V19 Restored Research Directions

# HLS DSE Research Project — V19
## Complete Research Master: Restored Scope and Deferred Studies

**Status:** Master research scope  
**Purpose:** This document restores all major research directions that were intentionally deferred from the current execution core. Nothing is deleted. The current Core is a scheduling/execution priority, not a deletion of research ideas.

---

# 1. Scope Policy

The project has two layers:

1. **Complete Research Master:** contains every research direction, extension, study, hypothesis, methodology, and previously considered idea.
2. **Execution Core:** identifies what is implemented first and experimentally validated first.

A study marked `DEFERRED`, `EXTENSION`, or `FUTURE` is **not removed**.

No previous research direction should be erased from the master record unless explicitly rejected by experimental evidence or by a future scientific decision.

---

# 2. Current Core

The current primary research thread remains:

> **Interaction- and Feasibility-Aware Selective Evaluation for Concurrent HLS DSE**

Core question:

> Under a fixed expensive-evaluation budget, does selecting between local and joint evidence improve discovery of the global feasible Pareto frontier in concurrent HLS DSE?

Core elements:

- local vs. joint evidence
- metric-specific interaction
- staged feasibility
- decision-changing joint evaluations
- heterogeneous evaluation cost
- selective expensive evaluation
- global feasible Pareto frontier
- Random / Local-only / Independent-composition / Cost-aware / Proposed baselines
- oracle-based evaluation on small spaces
- budget scaling
- reproducibility and evidence provenance

---

# 3. Restored Research Directions

## R01 — GNN-Based QoR Prediction

**Status:** RESTORED / EXTENSION

Use graph representations of HLS programs, CDFGs, IR/FSMD structures, or generated hardware to predict:

- latency
- resource utilization
- timing
- power
- feasibility
- interaction residuals

Potential models:

- GNN
- hierarchical GNN
- graph transformer
- mixture-of-experts

Research role:

- surrogate for expensive evaluation
- candidate ranking
- uncertainty estimation
- interaction prediction
- post-route QoR prediction

Important boundary:

GNN prediction itself is not claimed as novelty. Its role is as a component inside the evidence-selection framework.

---

# 4. LLM / Agentic HLS DSE

**Status:** RESTORED / FUTURE EXTENSION

Potential directions:

- LLM-generated pragma configurations
- LLM-guided candidate generation
- code transformation + pragma insertion
- agentic DSE
- LLM-assisted experiment planning
- LLM-generated hypotheses about interaction
- LLM as a proposal mechanism for unexplored regions

Potential systems to compare with:

- iDSE
- LIFT
- HLSPilot
- ChatHLS
- SAGE-HLS
- MailoHLS
- TimelyHLS
- HLS-Seek
- DAPO
- related LLM/GNN HLS systems

The project must not assume that LLMs improve DSE. They are experimental alternatives.

---

# 5. RL / Reinforcement Learning DSE

**Status:** RESTORED / FUTURE EXTENSION

Possible applications:

- sequential evidence-selection policy
- joint-evaluation scheduling
- candidate generation
- budget allocation
- adaptive fidelity selection
- interaction-aware exploration

Candidate algorithms:

- PPO
- DQN
- contextual bandits
- policy-gradient methods
- constrained RL

Scientific question:

> Can a learned sequential policy select expensive evaluations better than explicit acquisition functions under changing evaluation costs?

RL is not assumed necessary for the core framework.

---

# 6. Meta-DSE / Learning the DSE Strategy

**Status:** RESTORED / EXTENSION

Meta-level optimization can learn:

- which evaluator to invoke
- when to request joint evidence
- which fidelity to use
- which surrogate to trust
- which workload family to transfer from
- how much budget to allocate to exploration vs exploitation

Potential hierarchy:

```text
Workload
   ↓
Candidate generation
   ↓
Local evidence
   ↓
Interaction/uncertainty model
   ↓
Meta-DSE controller
   ↓
Local / Joint / Synthesis / P&R evaluation
   ↓
Global Pareto decision
```

---

# 7. Transfer Learning Across Workloads

**Status:** RESTORED / EXTENSION

Possible transfer directions:

- workload → workload
- kernel → kernel
- FPGA → FPGA
- HLS tool version → tool version
- architecture family → architecture family

Questions:

- How much local calibration is required?
- Does interaction structure transfer?
- Can previous joint evaluations reduce new joint evaluations?
- Does uncertainty remain calibrated after transfer?

Potential methods:

- fine-tuning
- meta-learning
- MAML-like methods
- domain adaptation
- representation transfer
- multi-task learning

---

# 8. Multi-Fidelity Evaluation

**Status:** RESTORED / EXTENSION

Fidelity hierarchy:

```text
Source/static analysis
      ↓
HLS
      ↓
Synthesis
      ↓
Implementation
      ↓
Post-route timing
      ↓
Power estimation / measurement
```

Potential research question:

> Which fidelity should be selected for each candidate and each uncertainty state?

Action can therefore become:

\[
a=(scope,configuration,fidelity)
\]

Examples:

- local + HLS
- local + synthesis
- joint + HLS
- joint + synthesis
- joint + implementation
- joint + post-route

The core local-vs-joint study remains valid as the simplest special case.

---

# 9. Higher-Order Interaction

**Status:** RESTORED / FUTURE

Pairwise interaction:

\[
I_{AB}=Y_{AB}-\hat{Y}_{AB}
\]

Higher-order interaction:

\[
I_{ABC}=Y_{ABC}-\hat{Y}_{ABC}
\]

Possible decomposition:

\[
Y(X)=\sum_i f_i(x_i)
+\sum_{i<j}f_{ij}(x_i,x_j)
+\sum_{i<j<k}f_{ijk}(x_i,x_j,x_k)+\cdots
\]

Research question:

> When does pairwise interaction cease to explain the global feasibility/Pareto behavior?

This is intentionally deferred because its evaluation cost grows combinatorially.

---

# 10. Physical Interaction

**Status:** RESTORED / SECOND-STAGE STUDY

Separate logical and physical interaction.

### Logical interaction

- BRAM contention
- DSP usage
- LUT/FF pressure
- memory bandwidth
- interface contention
- shared resources
- scheduling effects

### Physical interaction

- placement
- routing
- congestion
- timing
- clocking
- floorplan constraints
- SLR/die boundaries
- NoC/interconnect effects

Physical residual:

\[
I^{physical}_m =
Y^{postroute}_{joint,m}
-
\hat{Y}^{logical}_{joint,m}
\]

The physical study should only begin after the logical interaction experiment establishes a meaningful reason to continue.

---

# 11. Partial Reconfiguration / DFX

**Status:** RESTORED / EXTENSION

Potential directions:

- dynamic partial reconfiguration
- PR region allocation
- bitstream loading cost
- configuration switching
- runtime scheduling
- multi-application FPGA
- resource partitioning

Research question:

> How should DSE account for both steady-state concurrent performance and reconfiguration cost?

Potential objective:

\[
T_{total}=T_{configuration}+N\cdot T_{execution}
\]

Potential extended objective set:

- execution time
- reconfiguration time
- energy
- area
- resource utilization
- throughput

This is a separate lifecycle-oriented branch and must not be confused with static concurrent placement.

---

# 12. Lifecycle / Configuration-Aware DSE

**Status:** RESTORED / EXTENSION

Model:

\[
T_{total}=T_{config}+N T_{run}
\]

and potentially:

\[
E_{total}=E_{config}+N E_{run}
\]

Questions:

- When does a more expensive implementation become beneficial over its lifetime?
- When does reconfiguration overhead dominate?
- How does workload frequency change the optimal design?
- How should evaluation budget reflect expected deployment lifetime?

---

# 13. CPU–FPGA Heterogeneous Allocation

**Status:** RESTORED / FUTURE

Candidate actions:

- CPU
- FPGA
- partial FPGA
- heterogeneous CPU+FPGA

Objectives:

- latency
- energy
- throughput
- resource
- communication overhead

Potential model:

\[
T_{total}=T_{compute}+T_{transfer}+T_{synchronization}
\]

This extends the decision space beyond FPGA-only DSE.

---

# 14. DMA / Data-Movement-Aware DSE

**Status:** RESTORED / FUTURE

Potential interactions:

- DMA channels
- AXI bandwidth
- host-device transfers
- memory contention
- buffering
- burst size
- double buffering

Possible objective:

\[
T_{total}=T_{compute}+T_{DMA}+T_{stall}
\]

This can become a major interaction source in multi-kernel systems.

---

# 15. Power / Energy-Aware DSE

**Status:** RESTORED / EXTENSION

Metrics:

- static power
- dynamic power
- total power
- energy
- EDP
- ED²P

Potential formulation:

\[
EDP=E\times T
\]

or

\[
ED^2P=E\times T^2
\]

Potential sources:

- Vivado power analysis
- SAIF
- switching activity
- board-level measurements
- ML-based power estimators

The project should distinguish estimated power from measured power.

---

# 16. Sustainability / Carbon-Aware DSE

**Status:** RESTORED / EXTENSION

Potential metrics:

\[
Carbon=E_{total}\times CI
\]

where \(CI\) is carbon intensity.

Possible boundaries:

- FPGA runtime energy
- development/build energy
- manufacturing embodied carbon
- reconfiguration energy
- datacenter electricity mix

The project must define the system boundary before making sustainability claims.

---

# 17. Energy–Resource Trade-off Studies

**Status:** RESTORED / STUDY FAMILY

Examples:

- resource ↑, power ↓
- resource ↓, power ↑
- latency ↓, energy ↑
- area ↑, energy ↓
- BRAM ↑, DSP ↓
- LUT ↑, timing margin ↑
- replication ↑, voltage/frequency ↓

Each study should specify:

1. benchmark
2. controllable design variable
3. resource measured
4. power/energy measured
5. timing measured
6. mechanism
7. trade-off hypothesis
8. statistical protocol
9. tool chain

---

# 18. No-Joint / Joint-Evidence Certificate

**Status:** RESTORED / RESEARCH HYPOTHESIS

Potential certificate:

> Given current local evidence, uncertainty bounds, feasibility margins, and interaction estimates, joint evaluation is unlikely to change the global decision.

This must be treated as a falsifiable certificate, not an assumed theorem.

Validation:

- certificate prediction
- actual joint result
- false-negative rate
- false-positive rate
- decision loss

---

# 19. Minimum Joint Evidence

**Status:** RESTORED / BENCHMARK-DEPENDENT STUDY

Do not assume a universal minimum.

Instead measure:

\[
B^*_{joint}(\epsilon)
=
\min B
\quad
s.t.
\quad
L(B)\le\epsilon
\]

This quantity is benchmark-, workload-, architecture-, and objective-dependent.

The study asks whether useful empirical thresholds exist, not whether one universal number exists.

---

# 20. Adaptive Interaction Ladder

**Status:** RESTORED / EXTENSION

Potential ladder:

```text
Level 0: local-only
Level 1: joint HLS
Level 2: joint synthesis
Level 3: joint placement
Level 4: joint route
Level 5: timing/power
Level 6: physical measurement
```

The controller can escalate fidelity only when evidence justifies it.

---

# 21. 8-Workload / Large-Scale Benchmarking

**Status:** RESTORED / SCALE STUDY**

Possible progression:

\[
K=2\rightarrow3\rightarrow4\rightarrow8
\]

Measure:

- number of candidate combinations
- joint evaluations
- wall-clock time
- scheduler overhead
- Pareto quality
- interaction density
- scalability

Large K is not required for the first scientific claim but remains a project direction.

---

# 22. Large-Scale Distributed Execution

**Status:** RESTORED / ENGINEERING EXTENSION

Potential components:

- worker pools
- scheduler
- job queues
- resource-aware scheduling
- license-aware scheduling
- retry policy
- cache
- artifact store
- distributed logging
- experiment provenance

This should only be implemented after the scientific workflow is validated.

---

# 23. Advanced Storage / Provenance

**Status:** RESTORED / ENGINEERING EXTENSION

Potential storage:

- SQLite
- Parquet
- JSONL
- content-addressed artifacts
- immutable run manifests
- experiment registry

Required provenance:

- source revision
- HLS version
- synthesis version
- implementation version
- FPGA part
- constraints
- seed
- configuration
- tool options
- environment
- runtime
- artifact hashes

---

# 24. Concurrency and Locking

**Status:** RESTORED / ENGINEERING EXTENSION

Potential problems:

- Vivado project collisions
- temporary directory collisions
- license contention
- shared filesystem race conditions
- artifact overwrites

Potential solution:

- isolated run directories
- run IDs
- process groups
- resource locks
- atomic result publication

Concurrency should be added only when experiments actually require it.

---

# 25. Event Sourcing / Detailed Experiment Logging

**Status:** RESTORED / EXTENSION

Every experiment may generate:

```json
{
  "study_id": "...",
  "run_id": "...",
  "evaluation_id": "...",
  "attempt_id": "...",
  "scope": "local|joint",
  "fidelity": "...",
  "configuration": "...",
  "status": "...",
  "duration_s": 0,
  "tool_version": "...",
  "artifact_hash": "..."
}
```

This supports reproducibility, failure analysis, and automatic report generation.

---

# 26. Meta-Controller Alternatives

**Status:** RESTORED / FUTURE COMPARISON**

Controllers that may later be compared:

- rule-based acquisition
- Bayesian optimization
- contextual bandit
- RL
- GNN policy
- LLM agent
- hybrid controller

The proposed method should not assume that a neural or generative controller is automatically superior.

---

# 27. Research Study Map

| ID | Study | Status |
|---|---|---|
| S00 | Project contract | CORE |
| S01 | Flow smoke test | CORE |
| S02 | Interaction pilot | CORE |
| S03 | Decision relevance | CORE |
| S04 | Oracle benchmark | CORE |
| S05 | Evidence selection | CORE |
| S06 | Budget scaling | CORE |
| S07 | Workload scaling | EXTENSION |
| S08 | Physical interaction | EXTENSION |
| S09 | Multi-fidelity evidence | RESTORED |
| S10 | GNN surrogate | RESTORED |
| S11 | LLM candidate generation | RESTORED |
| S12 | RL/meta-controller | RESTORED |
| S13 | Transfer learning | RESTORED |
| S14 | Higher-order interaction | RESTORED |
| S15 | DFX / PR | RESTORED |
| S16 | Lifecycle-aware optimization | RESTORED |
| S17 | CPU–FPGA allocation | RESTORED |
| S18 | DMA/data movement | RESTORED |
| S19 | Power/energy-aware DSE | RESTORED |
| S20 | Carbon-aware DSE | RESTORED |
| S21 | No-Joint Certificate | RESTORED |
| S22 | Minimum joint evidence | RESTORED |
| S23 | Adaptive fidelity ladder | RESTORED |
| S24 | Large workload scaling | RESTORED |
| S25 | Distributed execution | RESTORED |
| S26 | Provenance/storage | RESTORED |
| S27 | Advanced controller comparison | FUTURE |

---

# 28. What Has NOT Been Deleted

The following are explicitly retained in the master research scope:

- GNN
- GNN surrogate modeling
- hierarchical GNN
- graph transformers
- LLM
- agentic HLS
- RL
- Meta-DSE
- transfer learning
- multi-task learning
- multi-fidelity
- higher-order interaction
- physical interaction
- DFX
- partial reconfiguration
- lifecycle optimization
- configuration energy
- CPU-vs-FPGA
- DMA
- power
- energy
- EDP
- ED²P
- sustainability
- carbon
- No-Joint Certificate
- minimum joint evidence
- adaptive interaction ladder
- 8-workload scaling
- distributed execution
- caching
- provenance
- event logging
- advanced storage
- concurrency
- license-aware scheduling
- alternative learned controllers

---

# 29. Scientific Interpretation

Restoring these studies does **not** mean all of them must appear in the first paper.

The correct hierarchy is:

```text
COMPLETE RESEARCH MASTER
│
├── Core paper
│   ├── S00
│   ├── S01
│   ├── S02
│   ├── S03
│   ├── S04
│   ├── S05
│   └── S06
│
├── Immediate extensions
│   ├── S07
│   ├── S08
│   └── S09
│
├── Advanced research
│   ├── S10–S14
│   ├── S19–S23
│
├── System/lifecycle branch
│   ├── S15–S18
│
└── Engineering/scalability branch
    ├── S24–S27
```

This preserves the entire research program while preventing the first experiment from becoming unmanageably large.

---

# 30. Versioning Rule

Future project versions must never delete a research direction silently.

If a direction is changed, the report should record:

- previous formulation
- reason for change
- new formulation
- affected studies
- whether experiments already exist
- whether old results remain valid

Therefore, V19 is a **restoration**, not a replacement that removes earlier work.

