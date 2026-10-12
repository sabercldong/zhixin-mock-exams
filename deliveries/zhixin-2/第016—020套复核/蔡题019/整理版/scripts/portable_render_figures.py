"""Compile current TikZ sources and split figures according to figure_map.json."""
from pathlib import Path
import os,json,subprocess,sys
import fitz
ROOT=Path(__file__).resolve().parents[1]
candidates=sorted((Path.home()/'.codex/plugins/cache/openai-bundled/latex').glob('*/scripts/compile_latex.py'))
COMPILER=Path(os.environ['CODEX_LATEX_COMPILER']) if os.environ.get('CODEX_LATEX_COMPILER') else candidates[-1]
NAMES=json.loads((ROOT/'figure_map.json').read_text())
SCALE=2.5
for q,names in NAMES.items():
 p=ROOT/f'figures/题{q}_图稿源文件.tex'
 run=subprocess.run([sys.executable,str(COMPILER),str(p),'--compiler','texlive','--engine','xelatex'],cwd=p.parent,capture_output=True,text=True)
 assert run.returncode==0,run.stdout+run.stderr
 log=p.with_suffix('.log').read_text(errors='replace')
 assert not any(t in log for t in ['Overfull','Missing character','Undefined control sequence','! ']),q
 with fitz.open(p.with_suffix('.pdf')) as d:
  assert len(d)==len(names),(q,len(d),len(names))
  for i,name in enumerate(names):
   target=ROOT/f'figures/{name}.pdf'
   if target.exists():target.unlink()
   with fitz.open() as one:one.insert_pdf(d,from_page=i,to_page=i);one.save(target)
   d[i].get_pixmap(matrix=fitz.Matrix(SCALE,SCALE),alpha=False).save(target.with_suffix('.png'))
 print(q,len(names),flush=True)
