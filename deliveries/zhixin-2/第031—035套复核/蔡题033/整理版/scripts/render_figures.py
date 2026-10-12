"""编译保留的TikZ源文件，按固定对应关系导出单图PDF及PNG。"""
from pathlib import Path
import os, sys
import subprocess
import fitz

ROOT=Path(__file__).resolve().parents[1]
_candidates=sorted(Path.home().glob('.codex/plugins/cache/openai-bundled/latex/*/scripts/compile_latex.py'))
COMPILER=Path(os.environ['CODEX_LATEX_COMPILER']) if os.environ.get('CODEX_LATEX_COMPILER') else (_candidates[-1] if _candidates else None)
assert COMPILER is not None and COMPILER.is_file(), 'Set CODEX_LATEX_COMPILER to compile_latex.py'
NAMES={
    '01':['question-01','solution-01'],
    '02':['question-02','solution-02'],
    '03':['question-03','planar-03','spatial-03'],
    '04':['question-04','solution-04'],
    '05':['question-05','solution-05'],
    '06':['question-06','solution-06'],
    '07':['question-07','layers-07','triangle-07'],
    '08':['solution-08','levels-08'],
}


def main():
    for q,names in NAMES.items():
        source=ROOT/'figures'/f'题{q}_图稿源文件.tex'
        built=subprocess.run([sys.executable,str(COMPILER),str(source),'--compiler','texlive','--engine','xelatex'],
                             cwd=source.parent,text=True,capture_output=True)
        assert built.returncode==0,(source,built.stdout,built.stderr)
        doc=fitz.open(source.with_suffix('.pdf'))
        assert len(doc)==len(names),(q,len(doc),names)
        for i,name in enumerate(names):
            pdf=source.parent/f'{name}.pdf'
            if pdf.exists(): pdf.unlink()
            single=fitz.open();single.insert_pdf(doc,from_page=i,to_page=i)
            single.save(pdf);single.close()
            doc[i].get_pixmap(matrix=fitz.Matrix(2.5,2.5),alpha=False).save(source.parent/f'{name}.png')
            subprocess.run(['qpdf','--check',str(pdf)],check=True,capture_output=True)
        print(q,','.join(names),flush=True)


if __name__=='__main__':main()
