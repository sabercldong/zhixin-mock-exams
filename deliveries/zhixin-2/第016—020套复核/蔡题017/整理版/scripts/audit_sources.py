"""复用源稿检查规则，017按当前已完整编写的题逐一审查，不伪造八题完成。"""
from pathlib import Path
import argparse,importlib.util,json
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'scripts/audit_rules_shared.py'
spec=importlib.util.spec_from_file_location('audit_rules020',SOURCE)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);module.ROOT=ROOT
MODULES,BANNED,metrics,inspect=module.MODULES,module.BANNED,module.metrics,module.inspect
def main():
    parser=argparse.ArgumentParser();parser.add_argument('questions',nargs='*');args=parser.parse_args()
    questions=args.questions or ['01']
    rows=[inspect(q) for q in questions]
    for q,row in zip(questions,rows):
        for rel in [f'drafts/question-{q}.md',f'figures/题{q}_图稿源文件.tex']:
            if (ROOT/rel).exists():
                raw=(ROOT/rel).read_bytes()
                controls=sorted(set(v for v in raw if v<32 and v not in [9,10]))
                if controls:row['issues'].append('raw_control_character:'+rel+':'+str(controls))
    report=dict(scope='已完整写出的分题源稿，不代表整套验收',questions=rows,passed=all(not r['issues'] for r in rows))
    (ROOT/'build').mkdir(exist_ok=True)
    (ROOT/'build/source-quality.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    for q,row in zip(questions,rows):
        single=dict(scope=report['scope'],questions=[row],passed=not row['issues'])
        (ROOT/f'build/source-quality-q{q}.json').write_text(json.dumps(single,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False));assert report['passed']
if __name__=='__main__':main()
