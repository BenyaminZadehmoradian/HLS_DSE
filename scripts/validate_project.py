from pathlib import Path
import json, yaml, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]; warnings=[]

def load_yaml(p):
    try: return yaml.safe_load(p.read_text(encoding='utf-8')) or {}
    except Exception as e: errors.append(f'YAML {p}: {e}'); return {}

def require(path, label=None):
    if not path.exists(): errors.append(f'Missing required {label or path}: {path}')

state=load_yaml(ROOT/'RESEARCH_STATE.yaml')
expected_version = state.get('project_version')
expected_source = state.get('canonical_source')
if not expected_version: errors.append('Missing project_version')
if not expected_source: errors.append('Missing canonical_source')
if expected_source and not (ROOT/expected_source).exists(): errors.append('Canonical source file missing')
# Phase/state machine, P1 authorization, active_environment, approval artifacts, transition provenance and
# AI_CONTROL policy consistency: the same checks the runtime control plane (hlsdse.control) enforces.
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT/'src'))
from hlsdse.control import repository_control_errors
errors.extend(f'CONTROL: {e}' for e in repository_control_errors(ROOT))
for name in ['CONTROL_PLANE_POLICY.yaml','PHASE_CONTROL.yaml','AUTO_PUSH_POLICY.yaml','AI_EXECUTION_POLICY.yaml','AI_SCOPE_POLICY.yaml']:
    require(ROOT/'AI_CONTROL'/name, 'AI_CONTROL policy')
if state.get('fixed_reference_device') != 'xc7z020clg484': errors.append('Reference device must be xc7z020clg484')

registry=load_yaml(ROOT/'contracts/STUDY_ID_REGISTRY.yaml')
for sid in ['S00','S01','S09','S71']:
    if sid not in registry.get('reserved',{}): errors.append(f'Missing registry entry {sid}')

ids={}
for p in (ROOT/'studies').glob('S*/CONTRACT.yaml'):
    d=load_yaml(p); sid=d.get('study_id')
    if sid: ids.setdefault(sid,[]).append(str(p))
for sid,paths in ids.items():
    if len(paths)>1: errors.append(f'Duplicate study_id {sid}: {paths}')

s71=load_yaml(ROOT/'studies/S71/CONTRACT.yaml')
if not s71 or s71.get('study_id')!='S71': errors.append('S71 contract invalid')
s09=load_yaml(ROOT/'studies/S09/CONTRACT.yaml')
if s09 and s09.get('status')!='ARCHIVED_ID_COLLISION': errors.append('S09 must be archived')

required_contracts=[
'DEVICE_REFERENCE_CONTRACT.yaml','HARDWARE_PLATFORM_CONTRACT.yaml','ARTIFACT_AND_RUN_MANAGEMENT_CONTRACT.yaml',
'BENCHMARK_CONTRACT.yaml','STATISTICS_CONTRACT.yaml','SEARCH_ALGORITHM_CONTRACT.yaml','MEASUREMENT_CONTRACT.yaml',
'MEMORY_PATH_CONTRACT.yaml','CONCURRENCY_FAIRNESS_CONTRACT.yaml','REPRODUCTION_CONTRACT.yaml','DATA_LEAKAGE_CONTRACT.yaml',
'CACHE_CONTRACT.yaml','FAILURE_AND_RETRY_CONTRACT.yaml','P1_IMPLEMENTATION_CONTRACT.yaml','EXTERNAL_BASELINE_CONTRACT.yaml',
'STAGED_EVALUATION_CONTRACT.yaml','STAGE_DECISION_CONTRACT.yaml','METRIC_PROVENANCE_CONTRACT.yaml']
for name in required_contracts: require(ROOT/'contracts'/name, 'contract')

for p in [ROOT/'schemas/METRIC_PROVENANCE_SCHEMA.json',ROOT/'schemas/STAGE_DECISION_SCHEMA.json',ROOT/'experiments/EVIDENCE_RECORD_SCHEMA.json',ROOT/'experiments/RUN_MANIFEST_SCHEMA.json',ROOT/'experiments/PRAGMA_CANDIDATE_SCHEMA.json',ROOT/'schemas/STUDY_RUN_SCHEMA.json']:
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: errors.append(f'JSON {p}: {e}')

if not (ROOT/'runs/_TEMPLATE/manifest.yaml').exists(): errors.append('Missing runs/_TEMPLATE/manifest.yaml')
if not (ROOT/'benchmarks/templates/BENCHMARK_TEMPLATE.yaml').exists(): errors.append('Missing benchmark template')
if not (ROOT/'configs/preflight/default.yaml').exists(): errors.append('Missing preflight config')
if not (ROOT/'audit/gates/P0_EXIT_CRITERIA.md').exists(): errors.append('Missing P0 exit criteria')

for p in (ROOT/'evidence/measured').rglob('*'):
    if p.is_file(): warnings.append(f'Unexpected measured evidence before P0: {p}')

# Reports must identify the current version; historical/archived reports may be exempt.
for p in (ROOT/'REPORTS').glob('*.md'):
    txt=p.read_text(encoding='utf-8')
    if 'project_version:' not in txt and 'Historical' not in txt: warnings.append(f'Report metadata missing: {p}')

artifact=load_yaml(ROOT/'contracts/ARTIFACT_AND_RUN_MANAGEMENT_CONTRACT.yaml')
if artifact.get('reference_device',{}).get('part') != 'xc7z020clg484': errors.append('Artifact contract reference device mismatch')

hardware=load_yaml(ROOT/'contracts/HARDWARE_PLATFORM_CONTRACT.yaml')
if hardware.get('reference_device',{}).get('part') != 'xc7z020clg484': errors.append('Hardware contract reference device mismatch')

print(f'errors={len(errors)} warnings={len(warnings)}')
for x in errors: print('ERROR:',x)
for x in warnings: print('WARNING:',x)
sys.exit(1 if errors else 0)
