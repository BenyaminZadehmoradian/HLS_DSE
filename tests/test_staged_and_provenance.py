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


def _kw(**over):
    kw = dict(project_version="V23.2", study_id="S00", run_id="R1", candidate_id="C1", benchmark_id="B1",
              device_part="xc7z020clg484", tool="Vitis HLS", tool_version="2025.2.1", source_artifact="csynth.xml",
              source_artifact_sha256="0" * 64, source_field_or_measurement="latency")
    kw.update(over)
    return kw


def test_advance_past_final_stage_is_rejected():
    with pytest.raises(ValueError):
        make_decision("C1", "R1", "RUNTIME", "ADVANCE", ["DONE"], ["E1"])


def test_unknown_decision_source_is_rejected():
    with pytest.raises(ValueError):
        make_decision("C1", "R1", "HLS", "DROP", ["BAD"], ["E1"], source="GUESS")


def test_decision_ids_are_unique_per_decision():
    a = make_decision("C1", "R1", "HLS", "KEEP", ["X"], ["E1"])
    b = make_decision("C1", "R1", "HLS", "KEEP", ["X"], ["E1"])
    assert a.decision_id != b.decision_id


def test_measured_metric_requires_value_and_known_stage():
    with pytest.raises(ValueError):
        build_metric("M1", "latency", None, "cycles", "MEASURED", "HLS", **_kw())
    with pytest.raises(ValueError):
        build_metric("M1", "latency", 10, "cycles", "MEASURED", "SOMEWHERE", **_kw())


def test_measured_metric_artifact_hash_is_verified(tmp_path):
    import hashlib
    (tmp_path / "csynth.xml").write_text("<latency>10</latency>")
    good = hashlib.sha256(b"<latency>10</latency>").hexdigest()
    m = build_metric("M1", "latency", 10, "cycles", "MEASURED", "HLS", artifact_root=tmp_path,
                     **_kw(source_artifact_sha256=good))
    assert m["provenance"]["source_artifact_sha256"] == good
    with pytest.raises(ValueError):
        build_metric("M1", "latency", 10, "cycles", "MEASURED", "HLS", artifact_root=tmp_path, **_kw())


def test_unknown_metric_cannot_carry_a_value_and_predicted_needs_confidence():
    with pytest.raises(ValueError):
        build_metric("M1", "latency", 3, "cycles", "UNKNOWN", "HLS", **_kw())
    with pytest.raises(ValueError):
        build_metric("M1", "latency", 3, "cycles", "PREDICTED", "HLS", estimator={"estimator_id": "gnn"}, **_kw())
    m = build_metric("M1", "latency", 3, "cycles", "PREDICTED", "HLS",
                     estimator={"estimator_id": "gnn", "confidence": 0.8}, **_kw())
    assert m["status"] == "PREDICTED"
