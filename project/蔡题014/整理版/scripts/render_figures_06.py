"""Render Q6 constrained charges, pair geometry, internal modes, threshold and periodic cell.
Rendering itself never asserts actual visual reading or question acceptance.
"""
from pathlib import Path
import hashlib,json,subprocess
import fitz
ROOT=Path(__file__).resolve().parents[1]
COMPILER=Path('/Users/dongxingxi/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py')
NAMES=['statement-06','geometry-06','modes-06','stability-06','chain-06']
def main():
    path=ROOT/'figures/题06_图稿源文件.tex'
    run=subprocess.run(['python3',str(COMPILER),str(path),'--compiler','texlive','--engine','xelatex'],cwd=path.parent,capture_output=True,text=True)
    (path.parent/'题06_编译记录.txt').write_text(run.stdout+run.stderr)
    assert run.returncode==0,run.stdout+run.stderr
    log=path.with_suffix('.log').read_text(errors='replace')
    warnings=[line for line in log.splitlines() if any(x in line for x in ['Overfull','Underfull','Missing character','Undefined control sequence','! ','Warning:'])]
    assert not warnings,warnings
    subprocess.run(['qpdf','--check',str(path.with_suffix('.pdf'))],capture_output=True,check=True)
    items=[]
    with fitz.open(path.with_suffix('.pdf')) as doc:
        assert len(doc)==len(NAMES)
        for i,name in enumerate(NAMES):
            dest=ROOT/f'figures/{name}.pdf'
            with fitz.open() as single:
                single.insert_pdf(doc,from_page=i,to_page=i);single.save(dest)
            doc[i].get_pixmap(matrix=fitz.Matrix(2.8,2.8),alpha=False).save(dest.with_suffix('.png'))
            subprocess.run(['qpdf','--check',str(dest)],capture_output=True,check=True)
            items.append(dict(name=name,pdf_sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),png_sha256=hashlib.sha256(dest.with_suffix('.png').read_bytes()).hexdigest()))
    (ROOT/'preview/figure-build-q06.json').write_text(json.dumps(dict(source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),figures=items,layout_warnings=warnings,actual_reviewed=False,accepted=False),ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(figures=len(items),warnings=warnings,accepted=False),ensure_ascii=False))
if __name__=='__main__':main()

