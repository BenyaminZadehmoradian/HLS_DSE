# HLS-DSE V22.8 — Implementation Ready

This release is the canonical handoff point into implementation. It does not claim that experiments have been executed or validated.

## First action
Run only:

```bash
./scripts/p0_gate_check.sh
```

Then inspect the generated validation output. If P0 passes, a human must explicitly approve the P0 Gate before P1 implementation becomes legal.

## Core additions
- canonical project/version state
- immutable Study ID registry; external baseline reproduction is S71
- benchmark contract
- device/toolchain contract
- metric contract
- correctness contract
- failure taxonomy and retry policy
- statistics pre-registration contract
- multi-dimensional budget contract
- evidence/run schemas
- executable candidate generator, legality hook, provenance, evidence store, and command runner
- P0/P1 executable contracts
- external baseline reproduction infrastructure
- CSV as export/view, not source of truth
- strict phase gating remains active
