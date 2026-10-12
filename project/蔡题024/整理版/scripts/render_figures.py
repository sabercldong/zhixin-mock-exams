"""逐题编译TikZ，单图PDF和PNG同时保留；不代替实际审图。"""
from pathlib import Path
import argparse
import subprocess
import fitz

ROOT = Path(__file__).resolve().parents[1]
COMPILER = Path('/Users/dongxingxi/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py')
NAMES = {
    '01':['question-01','opposite-01','rates-01','endpoints-01'],
    '02':['question-02','force-02','series-02','taper-02','weight-02'],
    '03':['question-03','equivalent-03','discrete-03'],
    '04':['question-04','force-04','induction-04','stability-04','oscillation-04'],
    '05':['question-05','inside-05','images-05','force-05','zeros-05'],
    '06':['question-06','kinetic-06','diffraction-06'],
    '07':['question-07','vectors-07','correlation-07','fringes-07'],
    '08':['question-08','boundary-08','cells-08','shell-08'],
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
                with fitz.open() as single:
                    single.insert_pdf(doc,from_page=i,to_page=i);single.save(dest)
                doc[i].get_pixmap(matrix=fitz.Matrix(2.5,2.5),alpha=False).save(dest.with_suffix('.png'))
                subprocess.run(['qpdf','--check',str(dest)],check=True,capture_output=True)
        print(q,','.join(NAMES[q]),flush=True)

if __name__=='__main__':main()

