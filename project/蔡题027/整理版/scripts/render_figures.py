"""逐题编译TikZ并拆分矢量PDF及居中笔记所用PNG。"""
from pathlib import Path
import argparse, subprocess, fitz
ROOT=Path(__file__).resolve().parents[1]
COMPILER=Path('/Users/dongxingxi/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py')
NAMES={
    "01": [
        "question-01",
        "geometry-01",
        "materials-01",
        "accelerations-01"
    ],
    "02": [
        "question-02",
        "velocities-02",
        "forces-02",
        "magnetic-02"
    ],
    "03": [
        "question-03",
        "reflection-03",
        "displacement-03",
        "potential-03"
    ],
    "04": [
        "question-04",
        "nodes-04",
        "currents-04",
        "reduced-04"
    ],
    "05": [
        "question-05",
        "reflection-05",
        "rays-05",
        "apparent-05"
    ],
    "06": [
        "question-06",
        "droplet-06",
        "energy-06",
        "balance-06"
    ],
    "07": [
        "question-07",
        "sequence-07",
        "transfer-07"
    ],
    "08": [
        "question-08",
        "symmetry-08",
        "reduced-08",
        "recursion-08"
    ]
}
def main():
    parser=argparse.ArgumentParser();parser.add_argument('questions',nargs='*');args=parser.parse_args()
    for q in args.questions or NAMES:
        source=ROOT/'figures'/f'题{q}_图稿源文件.tex'
        result=subprocess.run(['python3',str(COMPILER),str(source),'--compiler','texlive','--engine','xelatex'],cwd=source.parent,capture_output=True,text=True)
        assert result.returncode==0,(source,result.stdout,result.stderr)
        doc=fitz.open(source.with_suffix('.pdf'));names=NAMES[q]
        assert len(doc)==len(names),(q,len(doc),names)
        for i,name in enumerate(names):
            path=source.parent/f'{name}.pdf'
            single=fitz.open();single.insert_pdf(doc,from_page=i,to_page=i);single.save(path);single.close()
            doc[i].get_pixmap(matrix=fitz.Matrix(2.5,2.5),alpha=False).save(path.with_suffix('.png'))
            subprocess.run(['qpdf','--check',str(path)],check=True,capture_output=True)
        print(q,','.join(names),flush=True)
if __name__=='__main__':main()

