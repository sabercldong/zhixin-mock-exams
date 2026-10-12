"""编译分题TikZ合集并保存独立矢量图；不把生成预览当已审读。"""
from pathlib import Path
import argparse,subprocess
import fitz
ROOT=Path(__file__).resolve().parents[1]
COMPILER=Path('/Users/dongxingxi/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py')
NAMES={'01': ['question-01', 'compression-01', 'shear-01', 'hyperbola-01', 'dipole-01'], '02': ['question-02', 'parameters-02', 'range-02', 'anomaly-02', 'check-02'], '03': ['question-03', 'impulse-03', 'relative-03', 'steps-03', 'check-03'], '04': ['question-04', 'metric-04', 'hessian-04', 'ellipse-04', 'check-04'], '05': ['question-05', 'branches-05', 'dispersion-05', 'power-05', 'check-05'], '06': ['question-06', 'restframe-06', 'sunframe-06', 'spiral-06', 'check-06'], '07': ['question-07', 'flow-07', 'energy-07', 'comparison-07', 'check-07'], '08': ['question-08', 'laplacian-08', 'symmetry-08', 'emf-08', 'leads-08']}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('questions',nargs='*');args=parser.parse_args()
    for q in args.questions or NAMES:
        path=ROOT/f'figures/题{q}_图稿源文件.tex'
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
