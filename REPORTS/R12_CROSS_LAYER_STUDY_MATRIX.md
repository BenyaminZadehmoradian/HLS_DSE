---
report_metadata:
  report_id: "R12_CROSS_LAYER_STUDY_MATRIX"
  report_type: "METHODOLOGY"
  title: "Cross-Layer Study Matrix and CPU–FPGA Shared-Cache Architecture"
  project: "HLS-DSE"
  project_version: "V23.0"
  status: "PLANNED"
---

# R12 — Cross-Layer Study Matrix

## 1. Fixed system architecture

The experimental platform is constrained by the following architecture unless a Study explicitly changes and documents it:

```text
                 CPU
                  |
                  | programming / configuration
                  v
            +-----------+
            |   FPGA    |
            | accelerator|
            +-----------+
                  ^
                  |
             shared cache
                  ^
                  |
          system data producer
```

The CPU is the control-plane owner of FPGA programming/configuration and invocation. The FPGA receives its input data from the shared-cache data path. DMA, DDR bypass, cache level, coherence mechanism, and result-return path are **not inferred**; they must be declared and measured when applicable.

## 2. Cross-layer chain

```text
Search Algorithm
      ↓
Search Space
      ↓
Architecture / HLS Directives
      ↓
Memory Architecture
      ↓
HLS
      ↓
Synthesis
      ↓
Placement / Routing / Timing
      ↓
Bitstream
      ↓
CPU Programming / Configuration
      ↓
Shared-Cache Data Availability
      ↓
FPGA Data Consumption
      ↓
CPU–FPGA Synchronization
      ↓
Application Execution
      ↓
Lifecycle Cost
```

A Study may cover only one link or a defined subset. It must not silently generalize from one layer to another.

## 3. Causal dimensions

| Layer | Main variables | Required evidence |
|---|---|---|
| Search | algorithm, seed, candidate order | search trace |
| Search space | legal directives, architecture options | versioned space |
| HLS | cycles, inferred resources | HLS reports |
| Memory | buffers, ports, access pattern | synthesis + runtime |
| Physical | placement, routing, timing | implementation reports |
| Bitstream | size, generation time | artifact metadata |
| Configuration | CPU programming time, count | hardware timing |
| Cache | hit/miss, occupancy, contention | hardware/runtime counters |
| Data path | bytes, wait, transfer/consumption time | runtime instrumentation |
| Runtime | CPU overhead, FPGA execution | synchronized timestamps |
| Lifecycle | invocations, configurations, total cost | workload trace |

## 4. Required distinctions

The project must keep these quantities separate:

- kernel latency vs end-to-end latency;
- search overhead vs evaluation time;
- bitstream generation vs FPGA programming;
- programming time vs initialization time;
- cache access latency vs DMA transfer time;
- cache miss penalty vs FPGA execution time;
- power vs energy vs energy-per-invocation;
- single-run result vs run-to-run variability;
- QoR prediction vs feasibility prediction.

## 5. Decision-changing cross-layer tests

A cross-layer effect is scientifically relevant only if changing the upstream variable changes a downstream DSE decision, subject to measurement uncertainty.

Examples:

1. A pragma changes memory behavior enough to change the selected configuration.
2. A configuration with worse kernel latency wins after CPU programming cost is included.
3. Cache contention changes benchmark ranking.
4. A physical implementation that has similar HLS QoR becomes infeasible after placement/routing.
5. Search algorithm A reaches the same decision quality with lower end-to-end lifecycle cost than algorithm B.

These are hypotheses, not conclusions.

## 6. Architecture-specific mandatory metrics

At minimum, future hardware-backed Studies using this architecture should record:

- `t_search_s`
- `t_hls_s`
- `t_synthesis_s`
- `t_pnr_s`
- `t_bitstream_s`
- `t_program_s`
- `t_init_s`
- `t_cpu_control_s`
- `t_cache_wait_s`
- `t_fpga_data_consumption_s`
- `t_fpga_kernel_s`
- `t_end_to_end_s`
- `n_program`
- `n_invocation`
- `bitstream_size_bytes`
- `cache_hit_rate`
- `cache_miss_rate`
- `cache_bytes_read`
- `cache_bytes_written`
- `contention_wait_s`

Unknown measurements remain `UNKNOWN/NOT_MEASURED`.

## V23.1 Hardware/Artifact Isolation

Reference device: `xc7z020clg484`.

Every cross-layer observation must be traceable to a Study-specific Run containing the Vivado XSA, bitstream, Vitis ELF/software artifact, raw measurements, normalized evidence, and Run manifest. See `contracts/ARTIFACT_AND_RUN_MANAGEMENT_CONTRACT.yaml`.

No Study may overwrite another Study's Vivado/Vitis workspace or measured artifact. A completed Run is immutable.
