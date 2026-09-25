# HLS-DSE V22 — AI-Controlled Research Project

V22 reorganizes V21 into independent canonical reports while preserving V21 in full.

## Reports
R01 Research Master
R02 Research Program & Phases
R03 Experimental Methodology
R04 System & Software Architecture
R05 Related Work & Literature Evidence
R06 Study Specifications
R07 Research Extensions
R08 Historical Archive

## AI Control
`AI_CONTROL/` contains the system contract, no-guessing policy, permissions,
plugin/tool/skill policies, isolation, change control, evidence policy, reporting policy,
stop conditions, and escalation rules.

## Core rule
No AI-generated estimate may be silently promoted to measured evidence.

## Execution
Read MASTER → AI_CONTROL → active Study contract → execute → scan → register evidence → report → update state.

## Timing accounting
Every applicable evaluation records HLS, synthesis, P&R, bitstream generation, FPGA programming, initialization, execution, and total elapsed time. Missing timing is UNKNOWN, never estimated.

## Plotting
Every Study has isolated `plots/code`, `plots/generated`, and `plots/manifests` directories. Plot scripts are separate from experiment execution and are traceable to their source evidence.

## Pragma Space and Candidate Generation

The framework separates user-defined pragma-space constraints from automatically generated concrete candidates. Candidate generation is versioned and provenance-tracked; automatic generation does not silently expand the declared search space.

## V22.5.1 Literature-gap and external-baseline layer

The project now includes S09 External Baseline Reproduction and a formal Research Gap Register. External results are separated into literature-reported, reproduced, our-measured, and oracle/reference evidence. Direct comparisons require normalized benchmark, pragma space, device, tool version, constraints, metric stage, and evaluation budget.

## V23.1 Fixed Device and Vivado/Vitis Artifact Isolation

The reference target is fixed to **XC7Z020CLG484**.

All Vivado/Vitis outputs are isolated under:

`runs/<STUDY_ID>/<RUN_ID>/`

Vivado and Vitis never share mutable workspaces across Studies. XSA, bitstream, ELF, BOOT artifacts, reports, logs, and measurements are tied to the Run manifest and SHA-256 provenance. Completed Runs are immutable.

See:
- `contracts/DEVICE_REFERENCE_CONTRACT.yaml`
- `contracts/HARDWARE_PLATFORM_CONTRACT.yaml`
- `contracts/ARTIFACT_AND_RUN_MANAGEMENT_CONTRACT.yaml`
- `runs/_TEMPLATE/`
