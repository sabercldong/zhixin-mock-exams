"""编译分题TikZ合集并保存独立矢量图；不把生成预览当已审读。"""
from pathlib import Path
import argparse,subprocess
import fitz
ROOT=Path(__file__).resolve().parents[1]
COMPILER=Path('/Users/dongxingxi/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py')
NAMES={'01': ['question-01', 'retarded-01', 'frames-01', 'branches-01', 'rate-01'], '02': ['question-02', 'impulse-02', 'envelope-02', 'coverage-02', 'probability-02'], '03': ['question-03', 'energy-03', 'catenary-03', 'spacing-03', 'hexagon-03'], '04': ['question-04', 'gradient-04', 'diffusion-04', 'drift-04', 'time-04'], '05': ['question-05', 'recursion-05', 'roots-05', 'decay-05', 'limits-05'], '06': ['question-06', 'angular-06', 'velocity-06', 'acceleration-06', 'constraint-06'], '07': ['question-07', 'image-07', 'flight-07', 'frequency-07', 'double-07'], '08': ['question-08', 'field-08', 'parallel-08', 'radial-08', 'comparison-08']}

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
