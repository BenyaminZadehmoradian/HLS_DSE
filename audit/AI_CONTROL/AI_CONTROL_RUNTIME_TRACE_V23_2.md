# AI_CONTROL Runtime Trace — V23.2 (post-implementation, P0/S00)

**Source:** `evidence/control_probe_results.json`. It was produced by `evidence/control_probe.py` on 2026-09-25T17:16:41Z,
with base HEAD `f6b111a`.
- **Repositories:** synthetic throwaway git repositories built by `tests/control_harness.py`.
- **Approvals:** synthetic fixtures (approver `SYNTHETIC_TEST_FIXTURE`).
- **Tools:** mock scripts only.
- **Real repository:** not written.

The pre-implementation trace, "no AI_CONTROL check; implicit ALLOW; tool reached", is preserved at commit `d2a8523`.

## Trace 1: unauthorized P0 research request → DENY (scenario A)

```text
request_id        = 00c2f436-64ae-4e5a-ba31-e8bcc09cee4d
request           = run_authorized([<mock>, --probe], action=research_hls_runs, phase=P0, study=S00, environment=None)
policy            = AI_CONTROL/CONTROL_PLANE_POLICY.yaml 1.0 → action research_hls_runs → category HLS (gated)
state             = P0 / S00 / IMPLEMENTING (canonical transition record present), p1_authorized=false
approval          = G0-P0-S00-001 (valid, committed, unexpired)
scope             = research_hls_runs ∈ forbidden
decision          = DENY  OUT_OF_SCOPE: research_hls_runs is forbidden by G0-P0-S00-001
executor          = NOT CALLED (executor_called=false; spy saw 0 calls; mock marker absent)
log               = DECISION record appended (request_id matches)
```

## Trace 2: launcher gate → DENY (scenario K)

```text
request_id        = 2117faab-b07f-4ac7-bd3f-0d929dd62798
invocation        = bin/vivado -mode batch -source mock.tcl   (PATH: gate dir first, mock tool behind it)
path              = bin/vivado → tool_gate.sh → /usr/bin/python3 -E -B → hlsdse.control.tool_gate_main
classification    = tool identity vivado → research_vivado_runs (not a -version/-help query)
environment       = ENV-2025.2.1-XC7Z020-1 (from the launcher environment)
decision          = DENY  OUT_OF_SCOPE: research_vivado_runs is forbidden by G0-P0-S00-001
exit              = 126, "HLSDSE_CONTROL_DENY: …" on stderr; mock vivado NOT reached
```

**Real launcher check (no tool executed):** `run_in_env.sh bash -c 'command -v …'` resolves `vivado`, `vitis`,
`vitis-run`, `v++`, `vitis_hls` and `xsct` to the gate shims in `environments/xilinx_2025_2_1/bin/`.

## Trace 3: direct state write → DENY (scenario L)

```text
request_id        = 69f77783-908a-40ba-be5e-b09f3a2f69da
state             = PLANNED → IMPLEMENTING written directly into RESEARCH_STATE.yaml and PHASE_CONTROL.yaml
decision          = DENY  STATE_PROVENANCE_INVALID: P0 IMPLEMENTING has no matching canonical transition record
transitions       = IMPLEMENTING→GATE_REVIEW: INVALID_TRANSITION;  P0→P1: PHASE_ADVANCE_FORBIDDEN
```

## Trace 4: direct executor → refused (scenario J)

```text
_execute(decision_from_authorize(), argv)  → ExecutionDenied (decision not issued for execution)
flow.run_command(..., action=research_vivado_runs) → run.status=DENIED (OUT_OF_SCOPE); mock vivado NOT reached
```

The probe's spy counts the attempted `_execute` call (`executor_calls_observed: 1`). The executor refused it before
starting any process, so the marker is absent.

## Trace 5: positive mock → ALLOW (scenario POS)

```text
request_id        = 1d80913c-05a0-43f6-8e77-96b9e483b17b
request           = action=control_plane_implementation, phase=P0, study=S00, environment=None
approval          = G0-P0-S00-001 (flat scope layout, same as the real artifact)
decision          = ALLOW  AUTHORIZED
executor          = CALLED once; mock_control_step ran (marker written); executor_returncode=0
tool              = mock only; no HLS, Vivado or Vitis binary resolved or executed
```

## Summary

| Set | Result |
|---|---|
| Scenarios (A–N + POS) | 15/15 PASS |
| Fail-closed cases | 13/13 PASS |

**Real tools executed:** 0.
