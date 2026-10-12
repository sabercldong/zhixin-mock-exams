"""编译分题TikZ合集并保存独立矢量图；不把生成预览当已审读。"""
from pathlib import Path
import argparse,subprocess
import fitz
ROOT=Path(__file__).resolve().parents[1]
import os
_configured=os.environ.get('CODEX_LATEX_COMPILER')
_candidates=sorted((Path.home()/'.codex/plugins/cache/openai-bundled/latex').glob('*/scripts/compile_latex.py'))
COMPILER=Path(_configured) if _configured else (_candidates[-1] if _candidates else Path('compile_latex.py'))
NAMES={'01': ['question-01', 'forces-01', 'contacts-01', 'threshold-01', 'phase-01'], '02': ['question-02', 'impulse-02', 'section-02', 'moment-02', 'diagram-02'], '03': ['question-03', 'normal-03', 'spot-03', 'optimum-03', 'vector-03'], '04': ['question-04', 'fields-04', 'velocity-04', 'energy-04', 'barrier-04'], '05': ['question-05', 'directions-05', 'circuit-05', 'head-05', 'power-05'], '06': ['question-06', 'pulse-06', 'frames-06', 'photon-06', 'recoil-06'], '07': ['question-07', 'initial-07', 'modes-07', 'charge-07', 'voltage-07'], '08': ['question-08', 'joint-08', 'support-08', 'cut-08', 'series-08']}

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
