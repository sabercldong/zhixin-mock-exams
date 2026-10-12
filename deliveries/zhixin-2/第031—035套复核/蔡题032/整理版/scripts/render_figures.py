"""逐题编译保留的 TikZ，导出矢量 PDF 和 Obsidian PNG。"""
from pathlib import Path
import os, sys
import argparse
import subprocess
import fitz

ROOT=Path(__file__).resolve().parents[1]
_candidates=sorted(Path.home().glob('.codex/plugins/cache/openai-bundled/latex/*/scripts/compile_latex.py'))
COMPILER=Path(os.environ['CODEX_LATEX_COMPILER']) if os.environ.get('CODEX_LATEX_COMPILER') else (_candidates[-1] if _candidates else None)
assert COMPILER is not None and COMPILER.is_file(), 'Set CODEX_LATEX_COMPILER to compile_latex.py'
NAMES={'01':['question-01','nets-01','optimization-01','volume-01'],
       '02':['question-02','impulses-02','optimization-02','geometry-02','flight-02'],
       '03':['question-03','currents-03','rest-03','modified-03','port-03'],
       '04':['question-04','energy-04','composition-04'],
       '05':['question-05','meshes-05','capacitor-05','heating-05'],
       '06':['question-06','events-06','timeline-06'],
       '07':['question-07','paths-07','series-07','reflectance-07'],
       '08':['question-08','circulation-08','forces-08']}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('questions',nargs='*')
    args=parser.parse_args()
    for q in args.questions or NAMES:
        source=ROOT/'figures'/f'题{q}_图稿源文件.tex'
        result=subprocess.run([sys.executable,str(COMPILER),str(source),'--compiler','texlive','--engine','xelatex'],cwd=source.parent,capture_output=True,text=True)
        assert result.returncode==0,(source,result.stdout,result.stderr)
        doc=fitz.open(source.with_suffix('.pdf'));names=NAMES[q]
        assert len(doc)==len(names),(q,len(doc),names)
        for i,name in enumerate(names):
            path=source.parent/f'{name}.pdf'
            if path.exists(): path.unlink()
            single=fitz.open();single.insert_pdf(doc,from_page=i,to_page=i);single.save(path);single.close()
            doc[i].get_pixmap(matrix=fitz.Matrix(2.5,2.5),alpha=False).save(path.with_suffix('.png'))
            subprocess.run(['qpdf','--check',str(path)],check=True,capture_output=True)
        print(q,','.join(names),flush=True)

if __name__=='__main__':main()
