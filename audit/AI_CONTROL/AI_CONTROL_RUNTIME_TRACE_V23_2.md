# AI_CONTROL Runtime Trace — V23.2

**Source:** `evidence/control_probe_results.json` (probe `evidence/control_probe.py`, HEAD `91f14bb`, run
2026-09-25T16:17:50Z).
- **Tool:** a mock `vivado` shell script called by absolute path. No real HLS, Vivado or Vitis tool was invoked.
- **State:** mutations happened only in a temporary `git archive HEAD` copy. The live `RESEARCH_STATE.yaml` hash was
  unchanged before and after (`562136aff9b2…`).
- **Instrumentation:** a Python audit hook recorded every file opened *inside the executor call*.

## Requested blocking trace: Unauthorized P0 — NOT OBTAINABLE

The audit was asked to show `request → AI_CONTROL → gate → DENY → executor not reached`. No such trace can be
produced, because no code path consults AI_CONTROL. The actual trace:

```text
request_id        = 64c3dcfc-60e4-4faa-a8aa-3953f1d9f155
timestamp_utc     = 2026-09-25T16:17:50.653Z
requested_action  = START_P0: run S00 flow command (<mock>/vivado -mode batch -source synth_mock.tcl)
current_phase     = P0          active_phase_state = PLANNED
current_study     = S00         human_gate_required = true      p1_authorized = false
active_environment = null       authorization record = NONE (no approval artifact exists)

caller            : hlsdse.flow.run_command(RunRecord(study_id='S00', ...), cmd, log)
AI_CONTROL check  : NONE — files opened during call: RESEARCH_STATE.yaml = no; AI_CONTROL/* = none
policy decision   : NONE
gate decision     : NONE
execution decision: implicit ALLOW
tool invocation   : subprocess.run(cmd, shell=True)  →  mock vivado REACHED (marker written)
result            : run.status = SUCCESS
```

## Requested blocking trace: Unauthorized P1 — NOT OBTAINABLE

```text
request_id        = 67ab372c-1e51-4a4c-98ce-4c70d0b06668
timestamp_utc     = 2026-09-25T16:17:50.657Z
requested_action  = run S01 (P1 flow smoke) — p1_authorized = false
AI_CONTROL check  : NONE (0 control files opened)
gate decision     : NONE
tool invocation   : mock vivado REACHED
result            : run.status = SUCCESS
```

Tests C and G mutated the (temporary) state to P1/IMPLEMENTING and P1/RUNNING. The executor still ran. The
validator, run separately afterwards, reported `ERROR: P0 state is not PLANNED`: the violation is detected after
the fact, not prevented.

## Blocking traces that do exist (not AI_CONTROL)

**L1: toolchain environment guard, fail-closed**
```text
request_id  = 3ff67f40-447a-4ad8-95e0-543b80e2c7a9
request     = run_in_env.sh <mock>/vivado -mode batch   (launcher copy with altered pinned vendor hash)
check       = run_in_env.sh: sha256(settings64.sh) == VENDOR_SETTINGS_SHA256
decision    = DENY — "HLSDSE_ENV_ERROR: vendor settings hash mismatch" (exit 3)
executor    = NOT REACHED (no marker)
```
This guard checks the toolchain identity only. With a correct hash, P3 shows the same launcher executing the mock
tool while P0 is unauthorized.

**P1: CLI**
```text
request     = python -m hlsdse start-p0
decision    = argparse error "invalid choice" (exit 2) — the CLI has no execution command at all
executor    = NOT REACHED
```
This is blocking by *absence of a command*, not a policy decision.
