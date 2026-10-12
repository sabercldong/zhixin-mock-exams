"""复用源稿检查规则，019按当前已完整编写的题逐一审查，不伪造八题完成。"""
from pathlib import Path
import argparse,importlib.util,json
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parents[1]/'蔡题020/整理版/scripts/audit_sources.py'
spec=importlib.util.spec_from_file_location('audit_rules020',SOURCE)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);module.ROOT=ROOT
MODULES,BANNED,metrics,inspect=module.MODULES,module.BANNED,module.metrics,module.inspect
def main():
    parser=argparse.ArgumentParser();parser.add_argument('questions',nargs='*');args=parser.parse_args()
    rows=[inspect(q) for q in args.questions or ['01']]
    report=dict(scope='已完整写出的分题源稿，不代表整套验收',questions=rows,passed=all(not r['issues'] for r in rows))
    (ROOT/'build').mkdir(exist_ok=True)
    (ROOT/'build/source-quality.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False));assert report['passed']
if __name__=='__main__':main()
