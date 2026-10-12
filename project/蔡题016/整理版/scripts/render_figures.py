"""016 TikZ collections and vector single figures; rendering is not review."""
from pathlib import Path
import argparse,subprocess
import fitz
ROOT=Path(__file__).resolve().parents[1]
COMPILER=Path('/Users/dongxingxi/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py')
NAMES={
    '01':['question-01','velocity-01','reflection-01','minimum-01','escape-01','downstream-01'],
    '02':['question-02','space-02','vectors-02','circles-02','quadrupole-02'],
    '03':['question-03','unfold-03','forces-03','rings-03','asymmetric-03'],
    '04':['question-04','inertia-04','motion-04','forces-04','contact-04','block-04'],
    '05':['question-05','forces-05','circuit-05','motion-05','modes-05','energy-05'],
    '06':['question-06','exchange-06','impulse-06','energy-06','count-06','crossings-06'],
    '07':['question-07','geometry-07','angles-07','path-07','phasors-07','peak-07'],
    '08':['question-08','frames-08','pressure-08','events-08','fourforce-08','limits-08'],
}
def main():
    parser=argparse.ArgumentParser();parser.add_argument('questions',nargs='*');args=parser.parse_args()
    for q in args.questions or NAMES:
        path=ROOT/f'figures/题{q}_图稿源文件.tex'
        run=subprocess.run(['python3',str(COMPILER),str(path),'--compiler','texlive','--engine','xelatex'],cwd=path.parent,capture_output=True,text=True)
        assert run.returncode==0,run.stdout+run.stderr
        log=path.with_suffix('.log').read_text(errors='replace')
        assert not any(s in log for s in ['Overfull','Missing character','Undefined control sequence','! '])
        subprocess.run(['qpdf','--check',str(path.with_suffix('.pdf'))],capture_output=True,check=True)
        with fitz.open(path.with_suffix('.pdf')) as doc:
            assert len(doc)==len(NAMES[q])
            for i,name in enumerate(NAMES[q]):
                dest=ROOT/f'figures/{name}.pdf'
                with fitz.open() as single:single.insert_pdf(doc,from_page=i,to_page=i);single.save(dest)
                doc[i].get_pixmap(matrix=fitz.Matrix(2.5,2.5),alpha=False).save(dest.with_suffix('.png'))
                subprocess.run(['qpdf','--check',str(dest)],capture_output=True,check=True)
        print(q,NAMES[q],flush=True)
if __name__=='__main__':main()
