"""重建核验、单图与三版本，沿用教师主文件生成学生核心和试卷。"""
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
    if result.returncode:
        print((result.stdout+result.stderr)[-4500:],flush=True)
        raise RuntimeError(f'{name} failed: {result.returncode}')
    print('通过：'+name,flush=True)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--from-drafts',action='store_true')
    args=parser.parse_args()
    for q in range(1,9):
        runtime=str(SCIENTIFIC_PYTHON) if q==2 else sys.executable
        run([runtime,str(ROOT/'scripts'/f'verify_question{q:02}.py')])
    run([sys.executable,str(ROOT/'scripts/render_figures.py')])
    prepare=[sys.executable,str(ROOT/'scripts/prepare_documents.py')]
    if args.from_drafts:prepare.append('--from-drafts')
    run(prepare)
    run([sys.executable,str(ROOT/'scripts/build_documents.py')])
    (ROOT/'output').mkdir(exist_ok=True)
    for label in ('试卷','学生详解','教师备课'):
        source=ROOT/'build'/f'蔡题034_{label}.tex'
        run([sys.executable,str(COMPILER),str(source),'--compiler','texlive','--engine','xelatex',
             '--output-directory',str(ROOT/'build')])
        shutil.copy2(source.with_suffix('.pdf'),ROOT/'output'/f'第034套_{label}版.pdf')
    run([sys.executable,str(ROOT/'scripts/quality_check.py')])
    run([sys.executable,str(ROOT/'scripts/visual_audit.py')])


if __name__=='__main__':main()
