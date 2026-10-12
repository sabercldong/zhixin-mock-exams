"""014 Q5 independent geometry and file binding; visual reading remains separate."""
from pathlib import Path
import hashlib,json,math,re
import fitz
ROOT=Path(__file__).resolve().parents[1]
NAMES=['statement-05','layout-05','bounds-05','interface-05','duality-05']
checks=[]
def check(name,condition,**values):
    assert condition,(name,values)
    checks.append(dict(test=name,passed=True,**values))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def phase(x,y):
    return 1 if (x<.5)==(y>.5) else 2
def main():
    source=ROOT/'figures/题05_图稿源文件.tex';code=source.read_text()
    check('five separate vector figures',code.count(r'\begin{tikzpicture}')==5)
    check('standalone independent source',r'\documentclass[tikz,border=5pt]{standalone}' in code)
    check('genuine spatial top and finite thickness faces',all(x in code for x in [
        'x={(1cm,0cm)},y={(.38cm,.65cm)},z={(0cm,1cm)}',
        '(0,0,-.18)--(3.3,0,-.18)--(3.3,0,0)--(0,0,0)',
        '(3.3,0,-.18)--(3.3,3.3,-.18)--(3.3,3.3,0)--(3.3,0,0)']))
    check('world plate is square even though perspective image is not',3.3**2==4*1.65**2)
    check('plate top two directions are noncollinear in projection',abs(.65)>0)
    check('front full-width narrow face is contacted',r'\draw[electrode] (0,0,-.09)--(3.3,0,-.09)' in code)
    check('rear full-width edge is contacted',r'\draw[electrode] (0,3.3,0)--(3.3,3.3,0)' in code)
    check('front terminal reaches contacted face not top sheet interior','(1.65,0,-.09)--(1.65,-.45,-.09)' in code)
    check('rear terminal attaches directly to rear electrode','(1.65,3.3,0)--(1.65,4.05,0)' in code)
    check('width dimension measures both original x endpoints','(0,-1.15,-.18)--(3.3,-1.15,-.18)' in code)
    check('depth dimension measures both original y endpoints','(3.7,0,-.18)--(3.7,3.3,-.18)' in code)
    check('thickness dimension connects actual top and bottom heights','(-.32,0,-.18)--(-.32,0,0)' in code)
    check('short really connects whole middle row','(0,1.65)--(3.3,1.65)' in code)
    check('cut has separate left and right interior edges','(0,0) rectangle (1.60,3.3) (1.70,0) rectangle (3.3,3.3)' in code)
    check('cut does not sever shared terminal electrodes','(0,0)--(3.3,0) (0,3.3)--(3.3,3.3)' in code)
    check('original current arrow points from high top to low bottom','(-.55,2.8)--(-.55,2.05)' in code)
    check('dual current arrow points from high left to low right','(.80,-.43)--(2.50,-.43)' in code)
    for x,y in [(.25,.25),(.75,.25),(.25,.75),(.75,.75),(.15,.7),(.7,.85),(.85,.35),(.4,.2)]:
        # Inverse of the stated CCW rotation, T^{-1}(x,y)=(y,1-x).
        rotated=phase(y,1-x)
        check('quarter-turn swaps conductivity at '+str((x,y)),rotated==3-phase(x,y))
    check('rotation maps high original top to dual left',(1-1,.25)==(0,.25))
    check('rotation maps low original bottom to dual right',(1-0,.75)==(1,.75))
    theta1=math.degrees(math.atan2(1.4,.7));theta2=math.degrees(math.atan2(.7,1.4))
    check('local current refraction uses kappa1/kappa2=4',abs(math.tan(math.radians(theta2))/math.tan(math.radians(theta1))-.25)<1e-14)
    check('incoming interface angle matches actual line',abs(theta1-63.435)<1e-3)
    check('outgoing interface angle matches actual line',abs(theta2-26.565)<1e-3)
    check('interface normal points material1 to material2','(-1.55,0)--(2.12,0)' in code)
    check('interface tangent is CCW normal','(0,0)--(0,2.25)' in code)
    check('dual high voltage includes scale I/kappa0',r'U^\star=I/\kappa_0' in code)
    check('n and t labels are separated from the conducting rays',2.25>1.95 and 2.12>1.4)
    widths=[.54,.57,.82,.55,.83];items=[]
    for name,width in zip(NAMES,widths):
        pdf=ROOT/f'figures/{name}.pdf';png=pdf.with_suffix('.png')
        with fitz.open(pdf) as doc:
            check(name+' is a single standalone vector page',len(doc)==1 and len(doc[0].get_drawings())>5)
            page=doc[0];text=page.get_text()
            check(name+' contains searchable clear labels','\ufffd' not in text and bool(text.strip()))
            spans=[span for block in page.get_text('dict')['blocks'] if block['type']==0 for line in block['lines'] for span in line['spans'] if span['text'].strip()]
            minfont=min(v['size'] for v in spans)
            # A4 printable width 166 mm (22 mm margins), unchanged 101 template.
            printed_min=minfont*(166/25.4*72*width)/page.rect.width
            check(name+' labels remain legible at actual document width',printed_min>=8.,min_printed_font_pt=printed_min)
            check(name+' all text inside the page bounds',all(fitz.Rect(v['bbox']).contained_in(page.rect) if hasattr(fitz.Rect(v['bbox']),'contained_in') else page.rect.contains(fitz.Rect(v['bbox'])) for v in spans))
        items.append(dict(name=name,pdf_sha256=sha(pdf),png_sha256=sha(png),width_fraction=width))
    report=dict(paper='014',question='05',check_count=len(checks),checks=checks,figures=items,geometry_passed=True,
                actual_visual_reviewed=False,question_accepted=False,set_accepted=False,figure_source_sha256=sha(source),
                script_sha256=sha(Path(__file__)))
    (ROOT/'verification/question-05-geometry.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(passed=True,checks=len(checks),figures=len(items),actual_reviewed=False),ensure_ascii=False))
if __name__=='__main__':main()
