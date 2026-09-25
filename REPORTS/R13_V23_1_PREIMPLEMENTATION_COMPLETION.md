project_version: V23.1
report_id: R13
status: PREIMPLEMENTATION_COMPLETE

# R13 — V23.1 Pre-Implementation Completion

## Purpose

This report freezes the research-program contracts before implementation begins.
The project is ready to start P0 implementation, but no later Phase is authorized.

## Fixed reference

- Device: `xc7z020clg484`
- CPU owns FPGA programming/configuration and invocation.
- FPGA input source is the declared shared-cache path.
- DMA, ACP, direct DDR access, cache level, and coherency remain UNKNOWN until measured.

## Completed hardening

- Study isolation and Run isolation
- Artifact provenance and SHA-256 identity
- Vivado/Vitis output layout
- Benchmark contract
- Measurement contract
- Search algorithm contract
- Memory-path contract
- Concurrency/fairness contract
- Reproduction and baseline contract
- Data-leakage contract
- Cache/reuse contract
- Failure/retry contract
- P1 implementation contract
- P0 exit criteria
- Run template
- Benchmark template
- Preflight configuration
- Baseline registry
- Project validator

## Explicitly not claimed as implemented

The contracts do not mean the following are already measured:

- Vivado synthesis/implementation
- XSA generation
- Vitis platform/application build
- bitstream generation
- FPGA programming time
- cache hit/miss rate
- M_AXI/ACP/DMA behavior
- end-to-end runtime
- power/energy measurements
- external baseline reproduction

These become implementation tasks in the gated phases.

## Gate rule

P0 implementation may begin. P1 and later implementation remain blocked until the corresponding human Gate approval is recorded.


## V23.2 hardening — staged evaluation and provenance

The pre-implementation architecture now explicitly supports staged evaluation. The complete flow remains the scientific reference; a candidate can be stopped before later expensive stages only through an auditable stage decision. Estimates may influence candidate/stage selection, but estimated or predicted values cannot be presented as measured evidence.

Metric provenance is mandatory from evidence creation through reporting. Every numeric metric identifies the producing tool and version, source artifact and SHA-256, source field/measurement, Run, Candidate, benchmark, device, and evidence status.

Implementation remains gated: these contracts and tests are ready, but real Vitis HLS/Vivado/FPGA execution has not been performed by this packaging step.
