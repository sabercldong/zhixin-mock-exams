"""逐题编译独立TikZ，保留矢量图与笔记PNG；不替代读者审图。"""
from pathlib import Path
import argparse
import subprocess
import fitz

ROOT=Path(__file__).resolve().parents[1]
COMPILER=Path('/Users/dongxingxi/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py')
NAMES={
    "01":["question-01","constraints-01","forces-01","static-01","response-01","force-01","pulses-01"],
    "02":["question-02","field-02","harmonics-02","periods-02"],
    "03":["question-03","geometry-03","integral-03","recursion-03"],
    "04":["question-04","cycle-04","balance-04"],
    "05":["question-05","section-05","axes-05","fringes-05"],
    "06":["question-06","wave-06","levels-06"],
    "07":["question-07","geometry-07","collapse-07","emf-07"],
    "08":["question-08","ac-08","evolution-08","gain-08","power-08"],
}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('questions',nargs='*')
    args=parser.parse_args()
    for q in args.questions or NAMES:
        source=ROOT/'figures'/f'题{q}_图稿源文件.tex'
        result=subprocess.run(
            ['python3',str(COMPILER),str(source),'--compiler','texlive','--engine','xelatex'],
            cwd=source.parent,capture_output=True,text=True)
        assert result.returncode==0,(source,result.stdout,result.stderr)
        log=source.with_suffix('.log').read_text(errors='replace')
        bad=[line for line in log.splitlines() if 'Missing character' in line or 'Overfull' in line]
        assert not bad,(q,bad)
        with fitz.open(source.with_suffix('.pdf')) as doc:
            assert len(doc)==len(NAMES[q]),(q,len(doc),NAMES[q])
            for i,name in enumerate(NAMES[q]):
                path=source.parent/f'{name}.pdf'
                with fitz.open() as single:
                    single.insert_pdf(doc,from_page=i,to_page=i)
                    single.save(path)
                doc[i].get_pixmap(matrix=fitz.Matrix(2.5,2.5),alpha=False).save(path.with_suffix('.png'))
                subprocess.run(['qpdf','--check',str(path)],check=True,capture_output=True)
        print(q,','.join(NAMES[q]),flush=True)

if __name__=='__main__':
    main()
