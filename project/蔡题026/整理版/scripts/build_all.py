"""从可编辑教师主文件重建图稿、三版本及严格技术验收。"""
from pathlib import Path
import argparse
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
COMPILER=Path('/Users/dongxingxi/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py')
SCIENTIFIC_PYTHON=Path('/Users/dongxingxi/.local/share/uv/tools/docling/bin/python')

def run(args):
    result=subprocess.run(args,cwd=ROOT,text=True,capture_output=True)
    name=Path(args[1]).stem
    if name=='compile_latex':name=Path(args[2]).stem+'-compile'
    (ROOT/'build').mkdir(exist_ok=True)
    (ROOT/'build'/f'{name}-output.txt').write_text(result.stdout+result.stderr)
    assert result.returncode==0,(name,(result.stdout+result.stderr)[-5000:])
    print('通过：'+name,flush=True)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--from-drafts',action='store_true');args=parser.parse_args()
    run([str(SCIENTIFIC_PYTHON),str(ROOT/'scripts/verify_physics.py')])
    run([sys.executable,str(ROOT/'scripts/render_figures.py')])
    prepare=[sys.executable,str(ROOT/'scripts/prepare_documents.py')]
    if args.from_drafts:prepare.append('--from-drafts')
    run(prepare)
    run([sys.executable,str(ROOT/'scripts/build_documents.py')])
    (ROOT/'output').mkdir(exist_ok=True)
    for label in ['试卷','学生详解','教师备课']:
        source=ROOT/'build'/f'蔡题026_{label}.tex'
        run([sys.executable,str(COMPILER),str(source),'--compiler','texlive','--engine','xelatex','--output-directory',str(ROOT/'build')])
        shutil.copy2(source.with_suffix('.pdf'),ROOT/'output'/f'第026套_{label}版.pdf')
    run([sys.executable,str(ROOT/'scripts/quality_check.py')])
    run([sys.executable,str(ROOT/'scripts/visual_audit.py')])

if __name__=='__main__':main()
