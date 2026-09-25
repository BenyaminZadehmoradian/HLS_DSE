# AI TIME MEASUREMENT POLICY

## Purpose
Every executable HLS-DSE evaluation must account for the time spent producing,
configuring, and executing the evaluated design. Timing values must be measured
from execution instrumentation whenever the corresponding stage is actually run.

## Required timing categories

- `t_hls_s`: HLS / C-to-RTL or equivalent HLS processing time
- `t_synthesis_s`: RTL synthesis time
- `t_pnr_s`: placement and routing / implementation time
- `t_bitstream_s`: bitstream generation/export time
- `t_program_s`: physical FPGA programming/configuration time
- `t_init_s`: board/application/kernel initialization time
- `t_execution_s`: benchmark/kernel execution time
- `t_total_s`: wall-clock total for the declared evaluation boundary

## Critical distinction

Bitstream generation is NOT FPGA programming time.

```text
HLS
  -> synthesis
  -> P&R
  -> bitstream generation
  -> FPGA programming/configuration
  -> initialization
  -> benchmark execution
```

Each stage must be separately recorded when applicable.

## Programming frequency

The run record must also record:

- `n_program`
- `n_bitstream_build`
- `n_invocation`

This permits lifecycle accounting such as:

`T_lifecycle = T_build + N_program * T_program + N_invocation * T_execution`

The exact lifecycle equation used by a Study must be declared in that Study's contract.

## No estimation rule

If a timing value was not measured, it must be:

`UNKNOWN` / `NOT_MEASURED`

and must not be replaced by an AI estimate.

## Provenance

Every timing value must identify:

- run_id
- study_id
- evaluation_id
- start timestamp
- end timestamp or measured duration
- command/process
- environment fingerprint
- source log/artifact
- measurement method
- status: measured / derived / unknown

## Comparison rule

When comparing DSE methods, report both:

1. number and type of expensive evaluations, and
2. actual elapsed execution cost.

A reduction in evaluation count must not automatically be described as a reduction
in wall-clock cost.
