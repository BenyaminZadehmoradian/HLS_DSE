# AI Artifact Isolation Policy

## Purpose
Prevent cross-Study contamination of Vivado, Vitis, bitstream, XSA, ELF, measurement, and report artifacts.

## Mandatory rules
1. Device reference is `xc7z020clg484` unless a new project version explicitly changes it.
2. Every execution uses `runs/<STUDY_ID>/<RUN_ID>/`.
3. Vivado and Vitis projects are Run-local or reference immutable versioned shared artifacts read-only.
4. XSA, bitstream, ELF, BOOT artifacts and reports receive SHA-256 provenance.
5. `RUN_COMPLETE` is immutable. Corrections create a new Run.
6. Raw tool output is never overwritten by normalized/derived data.
7. Evidence cannot cross Studies without an explicit immutable artifact reference in the manifest.
8. DMA, M_AXI, ACP, cache level/coherency and memory paths are not inferred; they must be declared and measured.
9. Every Run belongs to exactly one Study and has a unique RUN_ID. Its layout is the canonical `run_layout` of
   `contracts/ARTIFACT_AND_RUN_MANAGEMENT_CONTRACT.yaml`; the manifest records the command, environment and
   input hashes, and `logs/` holds stdout/stderr.
10. Cross-study reuse requires an explicit dependency recorded in the Study contract.

## Failure condition
If a Run cannot establish Study ID, Run ID, device, tool versions, artifact paths, and hashes, the Run is invalid for measured evidence.
