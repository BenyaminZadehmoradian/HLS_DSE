# S73 — Memory-system and data-movement cost

## Status
PLANNED — no execution is authorized by this document.

## Research question
Does the memory-system and data-movement cost dimension materially change HLS-DSE decisions under controlled conditions?

## Hypothesis
The effect, if present, must be measured rather than assumed.

## Scope
This Study is independent. It may become CORE, SUPPORTING, EXTENSION, DROP, or NEGATIVE_RESULT only after evidence.

## Architecture
Default CPU programs/configures the FPGA; FPGA receives input data through the shared-cache path. Any DMA, DDR, cache hierarchy, coherence, or return-path detail must be explicitly declared.

## Required evidence
- raw tool/hardware artifacts
- normalized evidence records
- timing measurements
- configuration/workload provenance
- seed/repetition information where applicable
- failure taxonomy

## No-guessing rule
Missing measurements are `UNKNOWN/NOT_MEASURED`; they are never estimated and presented as measured.

## Decision rule
The Study is retained only if it produces reproducible evidence with a meaningful effect, decision impact, or scientifically useful negative result.
