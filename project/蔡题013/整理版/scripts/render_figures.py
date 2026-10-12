"""编译分题TikZ合集并保存独立矢量图；不把生成预览当已审读。"""
from pathlib import Path
import argparse,subprocess
import fitz
ROOT=Path(__file__).resolve().parents[1]
COMPILER=Path('/Users/dongxingxi/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py')
NAMES={'01': ['statement-01', 'geometry-01', 'method-01', 'derivation-01', 'check-01'], '02': ['statement-02', 'geometry-02', 'method-02', 'derivation-02', 'check-02'], '03': ['statement-03', 'geometry-03', 'method-03', 'derivation-03', 'check-03'], '04': ['statement-04', 'geometry-04', 'method-04', 'derivation-04', 'check-04'], '05': ['statement-05', 'geometry-05', 'method-05', 'derivation-05', 'check-05'], '06': ['statement-06', 'geometry-06', 'method-06', 'derivation-06', 'check-06'], '07': ['statement-07', 'geometry-07', 'method-07', 'derivation-07', 'check-07'], '08': ['statement-08', 'geometry-08', 'method-08', 'derivation-08', 'check-08']}

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
