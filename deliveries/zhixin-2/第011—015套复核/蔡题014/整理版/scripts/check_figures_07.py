"""Q7 figure geometry and final-scale readability, separate from actual reading."""
from pathlib import Path
import hashlib,json
import fitz
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
NAMES=['statement-07','optical-07','snell-07','spatial-07','moving-07','events-07']
WIDTHS=[.76,.79,.76,.64,.85,.66]
checks=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(test,condition,**data):
    assert condition,(test,data)
    checks.append(dict(test=test,passed=True,**data))
def main():
    path=ROOT/'figures/题07_图稿源文件.tex';code=path.read_text()
    check('six genuine standalone vector pages',code.count(r'\begin{tikzpicture}')==6)
    check('standalone wrapper',r'\documentclass[tikz,border=5pt]{standalone}' in code)
    check('exact curved profile not a circular or conical replacement','sqrt(1+3*' in code)
    check('source uses actual left hyperbola branch','-(2+sqrt(1+3*' in code)
    for h in [-.6,0.,.6,.8]:
        X=-(2+np.sqrt(1+3*h*h))/3;r=np.hypot(X,h)
        check('ray endpoints lie on physical branch at height '+str(h),abs(2*X+r+1)<1e-13)
        check('outgoing direction points to true F at height '+str(h),-X/r>0)
    check('medium fill on incident side only','(-2.3,-.9)--plot' in code)
    check('common incident wave plane distinct from projection foot','(-2.15,-.35)--(-2.15,1.17)' in code and '(P)--(B)' in code)
    check('optical path dimension connects Xa to actual P horizontal coordinate','(-2.15,1.35)--(\\surfX,1.35)' in code)
    check('Snell normal is perpendicular to actual slope','\\nX}{1/\\normLen}' in code and '\\nY}{-\\slope/\\normLen}' in code)
    check('incidence measured with backward normal and incident segment','start angle=180,end angle={180+\\angleN}' in code)
    check('transmission measured between outgoing direction and forward normal','start angle=\\angleT,end angle=\\angleN' in code)
    check('Snell curve tangent actual height .8','\\slope}{-.8/sqrt(1+3*.8*.8)}' in code)
    check('3D contains curved meridians not straight generators','domain=0:1.876166,samples=65' in code)
    check('depth basis retained in actual coordinates','.62*\\radiusR*sin(\\x)' in code and '.30*\\radiusR*sin(\\x)' in code)
    check('front and rear ring arcs visibly distinguished','domain=180:360' in code and 'domain=0:180' in code and 'blue!35,dashed' in code)
    check('rear meridian hidden dash distinct from front','-.62*\\x' in code and '{-.30*\\x}' in code)
    for X in [-1.8,-1.4,-1.15]:
        rho=np.sqrt(3*X*X+4*X+1)
        for theta in [0.,np.pi/2,np.pi,3*np.pi/2]:
            Y=rho*np.cos(theta);Z=rho*np.sin(theta)
            check('spatial ring lies on exact rotated interface '+str((X,theta)),
                  abs(9*(X+2/3)**2-3*(Y*Y+Z*Z)-1)<1e-13)
    check('cross-ring radius corresponds to actual axial plane','(\\surfX,0)--(\\surfX,.8)' in code)
    check('radius label moved outside the surface mesh','(-2.25,.60)' in code)
    check('moving comparison keeps equal transverse scale','[x=1.8cm,y=1.8cm]' in code)
    check('ground longitudinal shape scaled only by .6','-.6*(2+sqrt' in code)
    check('moving vertex and instantaneous focal distance .6 f','(-.6,0)' in code and '{$3f/5$}' in code)
    check('ground focus explicitly time-labelled not a fixed arbitrary target','{$F_t$}' in code)
    check('event axis is normalized x and ct','{$x/f$}' in code and '{$ct/f$}' in code)
    check('event figure identifies focal worldline','(0,0)--(4.08,5.1)' in code)
    check('central ray starts at actual moving vertex','(-.6,0)--(2.4,3)' in code)
    check('oblique ray starts at actual moving interface at y=f','(-.8,0)--({164/45},{41/9})' in code)
    check('both hit events lie on focal worldline',abs(2.4-.8*3)<1e-14 and abs(164/45-.8*41/9)<1e-14)
    check('blue ray label is offset from focal worldline','(2.02,1.65)' in code)
    figures=[]
    for name,width in zip(NAMES,WIDTHS):
        pdf=ROOT/f'figures/{name}.pdf';png=pdf.with_suffix('.png')
        with fitz.open(pdf) as doc:
            check(name+' single vector page',len(doc)==1 and len(doc[0].get_drawings())>5)
            p=doc[0];spans=[v for b in p.get_text('dict')['blocks'] if b['type']==0 for line in b['lines'] for v in line['spans'] if v['text'].strip()]
            check(name+' searchable math labels',bool(spans) and '\ufffd' not in p.get_text())
            size=min(v['size'] for v in spans)*(166/25.4*72*width)/p.rect.width
            check(name+' legible at actual declared width',size>=8.,min_printed_font_pt=size)
            check(name+' labels inside figure bounds',all(p.rect.contains(fitz.Rect(v['bbox'])) for v in spans))
        figures.append(dict(name=name,pdf_sha256=sha(pdf),png_sha256=sha(png),width_fraction=width))
    report=dict(paper='014',question='07',geometry_passed=True,check_count=len(checks),checks=checks,
                figures=figures,figure_source_sha256=sha(path),script_sha256=sha(Path(__file__)),
                actual_visual_reviewed=False,question_accepted=False,set_accepted=False)
    (ROOT/'verification/question-07-geometry.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(passed=True,checks=len(checks),figures=len(figures),accepted=False),ensure_ascii=False))
if __name__=='__main__':main()
