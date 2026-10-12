"""逐题编译TikZ，单图PDF和PNG同时保留；不代替实际审图。"""
from pathlib import Path
import argparse
import subprocess
import fitz

ROOT = Path(__file__).resolve().parents[1]
import os
_candidates=sorted((Path.home()/'.codex/plugins/cache/openai-bundled/latex').glob('*/scripts/compile_latex.py'))
COMPILER=Path(os.environ['CODEX_LATEX_COMPILER']) if os.environ.get('CODEX_LATEX_COMPILER') else _candidates[-1]
assert COMPILER.is_file()
NAMES = {'01':['question-01','geometry-01','forces-01','trajectory-01'],'02':['question-02','collision-02','second-02','range-02'],'03':['question-03','moments-03','cube-03','star-03','tetra-03','reduction-03'],'04':['question-04','field-04','axial-04','radial-04'],'05':['question-05','forces-05','normal-05','velocity-05'],'06':['question-06','atmosphere-06','exhaust-06','balance-06','engine-06'],'07':['question-07','train-07','ray-07','pupil-07'],'08':['question-08','barrier-08','cm-08','relativity-08']}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('questions',nargs='*');args=parser.parse_args()
    for q in args.questions or NAMES:
        source=ROOT/'figures'/f'题{q}_图稿源文件.tex'
        result=subprocess.run(['python3',str(COMPILER),str(source),'--compiler','texlive','--engine','xelatex'],
                              cwd=source.parent,capture_output=True,text=True)
        assert result.returncode==0,(source,result.stdout,result.stderr)
        bad=[line for line in source.with_suffix('.log').read_text(errors='replace').splitlines()
             if any(word in line for word in ['Missing character','Overfull','Undefined control sequence'])]
        assert not bad,(q,bad)
        with fitz.open(source.with_suffix('.pdf')) as doc:
            assert len(doc)==len(NAMES[q]),(q,len(doc),NAMES[q])
            for i,name in enumerate(NAMES[q]):
                dest=source.parent/f'{name}.pdf'
                if dest.exists():dest.unlink()
                with fitz.open() as single:
                    single.insert_pdf(doc,from_page=i,to_page=i);single.save(dest)
                doc[i].get_pixmap(matrix=fitz.Matrix(2.5,2.5),alpha=False).save(dest.with_suffix('.png'))
                subprocess.run(['qpdf','--check',str(dest)],check=True,capture_output=True)
        print(q,','.join(NAMES[q]),flush=True)

if __name__=='__main__':main()
