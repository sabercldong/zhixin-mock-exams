"""Portable current-source build; visual acceptance is recorded separately."""
from pathlib import Path
import os,sys,subprocess,shutil,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
_candidates=sorted((Path.home()/'.codex/plugins/cache/openai-bundled/latex').glob('*/scripts/compile_latex.py'))
COMPILER=Path(os.environ['CODEX_LATEX_COMPILER']) if os.environ.get('CODEX_LATEX_COMPILER') else _candidates[-1]
def run(args):
 result=subprocess.run(args,cwd=ROOT,capture_output=True,text=True)
 name=Path(args[1]).stem
 if name=='compile_latex':name=Path(args[2]).stem+'-compile'
 (ROOT/'build').mkdir(exist_ok=True)
 (ROOT/'build'/f'{name}-output.txt').write_text(result.stdout+result.stderr)
 assert result.returncode==0,(name,(result.stdout+result.stderr)[-4000:])
 print('passed:'+name,flush=True)
def main():
 run([sys.executable,str(ROOT/'scripts/prepare_documents.py'),'--from-drafts'])
 run([sys.executable,str(ROOT/'scripts/build_documents.py')])
 (ROOT/'output').mkdir(exist_ok=True)
 for label in ['试卷','学生详解','教师备课']:
  source=ROOT/'build'/f'蔡题025_{label}.tex'
  run([sys.executable,str(COMPILER),str(source),'--compiler','texlive','--engine','xelatex','--output-directory',str(ROOT/'build')])
  shutil.copy2(source.with_suffix('.pdf'),ROOT/'output'/f'第025套_{label}版.pdf')
 run([sys.executable,str(ROOT/'scripts/quality_check_current.py')])
if __name__=='__main__':main()
