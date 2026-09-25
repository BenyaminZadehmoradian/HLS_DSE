import argparse, json, subprocess
from pathlib import Path
from .pragma_space import generate_cartesian

def main():
    p=argparse.ArgumentParser(prog='hlsdse')
    sub=p.add_subparsers(dest='cmd',required=True)
    g=sub.add_parser('generate-candidates'); g.add_argument('space_json'); g.add_argument('benchmark_id'); g.add_argument('--out',required=True)
    a=sub.add_parser('validate-config'); a.add_argument('path')
    sub.add_parser('validate-project')
    sub.add_parser('status')
    sub.add_parser('scan-environment')
    args=p.parse_args()
    root=Path(__file__).resolve().parents[2]
    if args.cmd=='generate-candidates':
        space=json.loads(Path(args.space_json).read_text())
        rows=[{'candidate_id':c.candidate_id,'benchmark_id':c.benchmark_id,'pragma_config':c.pragma_config,'generator':c.generator} for c in generate_cartesian(space,args.benchmark_id)]
        Path(args.out).write_text(json.dumps(rows,indent=2),encoding='utf-8')
        print(len(rows))
    elif args.cmd=='validate-config':
        print('CONFIG_PRESENT', Path(args.path).exists())
    elif args.cmd=='validate-project':
        cp=subprocess.run([__import__('sys').executable, str(root/'scripts/validate_project.py')], text=True)
        raise SystemExit(cp.returncode)
    elif args.cmd=='status':
        state=json.loads('{}') if False else None
        import yaml
        data=yaml.safe_load((root/'RESEARCH_STATE.yaml').read_text())
        for k in ['project_version','current_phase','current_study','status','p1_authorized','human_gate_required']:
            print(f'{k}={data.get(k)}')
    elif args.cmd=='scan-environment':
        cp=subprocess.run([__import__('sys').executable, str(root/'scripts/p0_preflight.py')], text=True)
        raise SystemExit(cp.returncode)
