"""Build TikZ collections and individual vector PDFs; generation is not actual review."""
from pathlib import Path
import argparse,subprocess
import fitz
ROOT=Path(__file__).resolve().parents[1]
import os
_candidates=sorted((Path.home()/'.codex/plugins/cache/openai-bundled/latex').glob('*/scripts/compile_latex.py'))
COMPILER=Path(os.environ['CODEX_LATEX_COMPILER']) if os.environ.get('CODEX_LATEX_COMPILER') else _candidates[-1]
assert COMPILER.is_file()
NAMES={'01':['question-01','focus-01','orbit-01','envelope-01','space-01','unbound-01'],
       '02':['question-02','fields-02','mean-02','sector-02','strength-02'],
       '03':['question-03','torus-03','cylinder-03','cap-03','geometry-03','rupture-03'],
       '04':['question-04','halves-04','longitudinal-04','transverse-04'],
       '05':['question-05','force-05','radial-05','com-05','velocity-05'],
       '06':['question-06','slice-06','temperature-06','entropy-06','wall-06'],
       '07':['question-07','malus-07','axes-07','half-07','quarter-07','branches-07'],
       '08':['question-08','global-08','local-08','capture-08','frames-08','comparison-08']}
def main():
    parser=argparse.ArgumentParser();parser.add_argument('questions',nargs='*');args=parser.parse_args()
    for q in args.questions or NAMES:
        path=ROOT/f'figures/\u9898{q}_\u56fe\u7a3f\u6e90\u6587\u4ef6.tex'
        run=subprocess.run(['python3',str(COMPILER),str(path),'--compiler','texlive','--engine','xelatex'],cwd=path.parent,capture_output=True,text=True)
        assert run.returncode==0,run.stdout+run.stderr
        log=path.with_suffix('.log').read_text(errors='replace')
        assert not any(s in log for s in ['Overfull','Missing character','Undefined control sequence','! '])
        with fitz.open(path.with_suffix('.pdf')) as doc:
            assert len(doc)==len(NAMES[q])
            for i,name in enumerate(NAMES[q]):
                dest=ROOT/f'figures/{name}.pdf'
                with fitz.open() as single:single.insert_pdf(doc,from_page=i,to_page=i);single.save(dest)
                doc[i].get_pixmap(matrix=fitz.Matrix(2.5,2.5),alpha=False).save(dest.with_suffix('.png'))
                subprocess.run(['qpdf','--check',str(dest)],capture_output=True,check=True)
        print(q,NAMES[q],flush=True)
if __name__=='__main__':main()
