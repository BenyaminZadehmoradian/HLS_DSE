import argparse, json, runpy
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
    au=sub.add_parser('authorize', help='decide (and log) a control request; executes nothing')
    au.add_argument('--action',required=True); au.add_argument('--phase',required=True); au.add_argument('--study',required=True)
    au.add_argument('--environment',default=None); au.add_argument('--approval',default=None); au.add_argument('--actor',required=True)
    tr=sub.add_parser('transition', help='canonical phase-state transition (PHASE_CONTROL transition table)')
    tr.add_argument('--to',required=True,dest='to_state'); tr.add_argument('--approval',required=True)
    tr.add_argument('--actor',required=True); tr.add_argument('--reason',required=True)
    pb=sub.add_parser('publish', help='validate, scan, commit and push per AI_CONTROL/AUTO_PUSH_POLICY.yaml (no force/skip flags)')
    pb.add_argument('-m','--message',required=True); pb.add_argument('--reason',required=True); pb.add_argument('--actor',required=True)
    pb.add_argument('--path',action='append',dest='paths',help='restrict to these changed paths (repeatable)')
    pb.add_argument('--provenance',default='{}',help='JSON: phase, study, run_id, environment_id when applicable')
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
        runpy.run_path(str(root/'scripts/validate_project.py'), run_name='__main__')
    elif args.cmd=='status':
        state=json.loads('{}') if False else None
        import yaml
        data=yaml.safe_load((root/'RESEARCH_STATE.yaml').read_text())
        for k in ['project_version','current_phase','current_study','status','p1_authorized','human_gate_required']:
            print(f'{k}={data.get(k)}')
    elif args.cmd=='publish':
        from .publish import automatic_publish
        e=automatic_publish(root, args.message, reason=args.reason, actor=args.actor,
                            provenance=json.loads(args.provenance), paths=args.paths)
        print(json.dumps(e, indent=2, sort_keys=True))
        raise SystemExit({'PUSHED':0,'NO_CHANGES':0,'COMMITTED_NOT_PUSHED':4,'COMMITTED_PUSH_FAILED':5}.get(e['result'],3))
    elif args.cmd=='scan-environment':
        runpy.run_path(str(root/'scripts/p0_preflight.py'), run_name='__main__')
    elif args.cmd=='authorize':
        from .control import authorize
        d=authorize(args.action, args.phase, args.study, args.environment, actor=args.actor, caller='cli:authorize',
                    approval_id=args.approval, root=root)
        print(json.dumps(d.__dict__, indent=2, sort_keys=True))
        raise SystemExit(0 if d.allowed else 1)
    elif args.cmd=='transition':
        from .control import transition, ControlError
        try:
            rec=transition(args.to_state, approval_id=args.approval, actor=args.actor, reason=args.reason, root=root)
        except ControlError as e:
            print(f'TRANSITION DENIED: {e.code}: {e.detail}'); raise SystemExit(1)
        print(json.dumps(rec, indent=2, sort_keys=True))
