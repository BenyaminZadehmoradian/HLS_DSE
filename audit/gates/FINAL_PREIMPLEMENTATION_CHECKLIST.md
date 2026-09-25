# Final Pre-Implementation Checklist — V23.1

## Governance
- [x] Canonical project version = V23.1
- [x] Reference device = xc7z020clg484
- [x] P0 is the only active phase
- [x] Human gate required
- [x] Automatic advancement disabled
- [x] Future implementation blocked

## Scientific contracts
- [x] Research program and independent Studies
- [x] Benchmark contract
- [x] Search algorithm contract
- [x] Measurement contract
- [x] Statistics contract
- [x] Failure/retry contract
- [x] Memory-path contract
- [x] Concurrency/fairness contract
- [x] Reproduction contract
- [x] Data-leakage contract
- [x] Cache/reuse contract
- [x] External baseline contract

## Hardware/software provenance
- [x] Device identity
- [x] Vivado/Vitis isolation
- [x] XSA provenance
- [x] Bitstream provenance
- [x] ELF provenance
- [x] Run manifest
- [x] SHA-256 artifact identity
- [x] Immutable completed Run rule

## Data integrity
- [x] Raw / normalized / derived separation
- [x] Measured evidence cannot exist before real execution
- [x] Benchmark correctness contract
- [x] Failure taxonomy
- [x] Retry policy
- [x] Dataset leakage policy

## Implementation readiness
- [x] Run template
- [x] Benchmark template
- [x] Preflight configuration
- [x] Environment scanner scaffold
- [x] Project validator
- [x] CLI status/validation commands
- [x] P1 implementation contract
- [x] P0/P1 exit criteria

## Verification performed on this package
- [x] `python scripts/validate_project.py` → errors=0, warnings=0
- [x] `python -m pytest -q` → 1 passed
- [x] CLI project validation → PASS
- [x] CLI state reporting → PASS

## Explicitly deferred to implementation
- [ ] Actual Vivado run
- [ ] Actual Vitis run
- [ ] Actual XSA generation
- [ ] Actual bitstream generation
- [ ] Actual FPGA programming
- [ ] Actual CPU–FPGA memory characterization
- [ ] Actual runtime measurement
- [ ] Actual power/energy measurement
- [ ] External baseline reproduction

These are not missing project definitions; they are implementation/evidence tasks and must remain gated.
