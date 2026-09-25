import pytest
from hlsdse.staged import make_decision, validate_stage_decision
from hlsdse.provenance import build_metric


def test_stage_advance_requires_correct_next_stage():
    d = make_decision("C1", "R1", "HLS", "ADVANCE", ["PROMISING"], ["E1"])
    assert d.next_stage == "SYNTHESIS"


def test_estimated_metric_cannot_be_measured_without_artifact():
    with pytest.raises(ValueError):
        build_metric("M1","timing",1.2,"ns","MEASURED","HLS",
                     project_version="V23.2",study_id="S00",run_id="R1",candidate_id="C1",
                     benchmark_id="B1",device_part="xc7z020clg484",tool="Vitis HLS",
                     tool_version="2025.2.1",source_artifact="",source_artifact_sha256="0"*64,
                     source_field_or_measurement="timing")


def test_derived_metric_requires_inputs():
    with pytest.raises(ValueError):
        build_metric("M2","total",2,"s","DERIVED","RUNTIME",
                     project_version="V23.2",study_id="S00",run_id="R1",candidate_id="C1",
                     benchmark_id="B1",device_part="xc7z020clg484",tool="derived",
                     tool_version="1",source_artifact="",source_artifact_sha256="0"*64,
                     source_field_or_measurement="sum")
