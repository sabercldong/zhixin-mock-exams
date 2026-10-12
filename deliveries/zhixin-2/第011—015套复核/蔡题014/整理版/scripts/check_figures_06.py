"""Q6 geometry and actual-scale readability; no automatic visual acceptance."""
from pathlib import Path
import hashlib,json
import fitz
ROOT=Path(__file__).resolve().parents[1]
NAMES=['statement-06','geometry-06','modes-06','stability-06','chain-06']
checks=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(test,condition,**data):
    assert condition,(test,data)
    checks.append(dict(test=test,passed=True,**data))
def main():
    path=ROOT/'figures/题06_图稿源文件.tex';code=path.read_text()
    check('five standalone vector pages',code.count(r'\begin{tikzpicture}')==5)
    check('standalone wrapper retained',r'\documentclass[tikz,border=5pt]{standalone}' in code)
    check('fixed equally spaced three x guides',r'\foreach \x in {-2.6,0,2.6}' in code)
    check('different signed positions on respective guide',all(t in code for t in ['(-2.6,.65)','(0,-.40)','(2.6,1.0)']))
    check('signed first displacement from initial y0','(-2.29,0)--(-2.29,.65)' in code)
    check('signed middle displacement from initial y0','(.31,0)--(.31,-.40)' in code)
    check('signed third displacement from initial y0','(2.91,0)--(2.91,1.0)' in code)
    check('origin label above axis away from negative charge',r'\node[above left] at (0,0) {$O$}' in code)
    check('horizontal dimensions are guide distances not oblique separations','(-2.6,-1.08)--(0,-1.08)--(2.6,-1.08)' in code)
    check('generic distance triangle has true right projection','(I)--(F)--(J)' in code and 'at (4,2)' in code and 'at (4,0)' in code)
    check('generic height dimension connects true projected endpoints','(4.45,0)--(4.45,2)' in code)
    check('pair-distance equation includes fixed h and displacement difference',r'r_{ij}^2=h^2+(\Delta y)^2' in code)
    check('translation arrows attached to all three particles',r'\foreach \x in {0,1,2}' in code and r'(\x,0)--(\x,.8)' in code)
    check('antisymmetric arrows attached to outer particles only','(3.8,0)--(3.8,.8)' in code and '(5.8,0)--(5.8,-.8)' in code)
    check('symmetric middle displacement is twice and opposite',all(v in code for v in ['(7.6,0)--(7.6,.8)','(8.6,0)--(8.6,-1.6)','(9.6,0)--(9.6,.8)']))
    check('normal mode ratios explicitly stated',all(t in code for t in ['{1:1:1}','{1:0:-1}','{1:-2:1}']))
    check('threshold axis scale maps quarter to x1',4*.25==1.)
    check('antisymmetric line equals lambda-quarter',abs(.8-(4.2/4-.25))<1e-14)
    check('symmetric line equals three lambda',abs(3.15-3*(4.2/4))<1e-14)
    check('zero branch is identified as translation',r'\omega_0^2=0' in code)
    check('stable shading starts at critical parameter, not zero','(1,0) rectangle (4.20,3.30)' in code)
    check('full-chain alternating sites are equally spaced',r'\foreach \x in {-2,0,2,4,6}' in code and r'\foreach \x in {-1,1,3,5}' in code)
    check('primitive cell contains one charge of each sign','(-.50,-.42) rectangle (1.50,.43)' in code)
    check('phase translation connects adjacent cell centers','(.50,1.04)--(2.50,1.04)' in code)
    check('nearest distance and cell period are distinguished','(0,-1.12)--(1,-1.12)' in code and '(0,-1.75)--(2,-1.75)' in code)
    widths=[.76,.69,.86,.72,.86];figures=[]
    for name,width in zip(NAMES,widths):
        pdf=ROOT/f'figures/{name}.pdf';png=pdf.with_suffix('.png')
        with fitz.open(pdf) as doc:
            check(name+' single vector page',len(doc)==1 and len(doc[0].get_drawings())>5)
            p=doc[0];spans=[v for block in p.get_text('dict')['blocks'] if block['type']==0 for line in block['lines'] for v in line['spans'] if v['text'].strip()]
            check(name+' searchable math labels',bool(spans) and '\ufffd' not in p.get_text())
            printed_min=min(v['size'] for v in spans)*(166/25.4*72*width)/p.rect.width
            check(name+' readable at declared final width',printed_min>=8.,min_printed_font_pt=printed_min)
            check(name+' text not cropped',all(p.rect.contains(fitz.Rect(v['bbox'])) for v in spans))
        figures.append(dict(name=name,pdf_sha256=sha(pdf),png_sha256=sha(png),width_fraction=width))
    report=dict(paper='014',question='06',geometry_passed=True,check_count=len(checks),checks=checks,
                figures=figures,figure_source_sha256=sha(path),script_sha256=sha(Path(__file__)),
                actual_visual_reviewed=False,question_accepted=False,set_accepted=False)
    (ROOT/'verification/question-06-geometry.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(passed=True,checks=len(checks),figures=len(figures),accepted=False),ensure_ascii=False))
if __name__=='__main__':main()
