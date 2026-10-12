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
NAMES = {
    '01':['question-01','force-01','flux-01','phases-01','coupling-01'],
    '02':['question-02','recoil-02','doppler-02'],
    '03':['question-03','coordinates-03','samefreq-03','parabola-03','eight-03'],
    '04':['question-04','balance-04','steady-04'],
    '05':['question-05','direct-05','reflection-05','ghost-05','aperture-05'],
    '06':['question-06','element-06','tension-06','profiles-06'],
    '07':['question-07','vertices-07','geometry-07','curvature-07'],
    '08':['question-08','basis-08','unwrapped-08','potential-08','closed-08','separatrix-08'],
}

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
