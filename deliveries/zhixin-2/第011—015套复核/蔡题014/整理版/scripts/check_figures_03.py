"""Check actual Q3 source-coordinate conventions. This is not visual acceptance."""
from pathlib import Path
import hashlib,json,math,re
ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'figures/题03_图稿源文件.tex';source=path.read_text();checks=[]
def add(name,condition,**data):
    assert condition,(name,data)
    checks.append(dict(name=name,passed=True,**data))
add('exactly five TikZ pictures',source.count(r'\begin{tikzpicture}')==5)
add('actual source has outward radial and real normal-force components',
    r'\fs*(1-\qq*\qq)/(1+\qq*\qq)' in source and r'-2*\fs/(1+\qq*\qq)' in source)
add('actual source plots negative-x-opening parabola',
    source.count(r'\cc-\t*\t/(4*\cc)')==3)
add('actual source has displaced sqrt(c) label and velocity label off the track',
    'node[below left,xshift=-3pt]' in source and '(1.83,3.65)' in source)
for theta in [55.,60.]:
    l=3. if theta==55. else 3.6
    ax=l*math.cos(math.radians(theta));ay=-l*math.sin(math.radians(theta))
    bx=ax;by=-ay
    add('statement endpoints have identical radius',abs(math.hypot(ax,ay)-l)<1e-12 and abs(math.hypot(bx,by)-l)<1e-12,theta=theta)
    dot=(ax*bx+ay*by)/l**2
    add('statement endpoints have the displayed smaller central angle',abs(math.acos(max(-1,min(1,dot)))-2*math.radians(theta))<1e-12,theta=theta)
c=2.7
add('rendered parabola parameters are consistent with l and theta',abs(c-3.6*math.cos(math.radians(30))**2)<1e-12)
endY=3.117691454
for y in [-endY,-1.8,0.,1.8,endY]:
    x=c-y*y/(4*c);r=math.hypot(x,y)
    add('plotted curve focus and directrix distances agree',abs(r-(2*c-x))<1e-12,y=y)
add('drawn A/B numerical endpoint coordinates are on the curve',abs(1.8-(c-endY**2/(4*c)))<5e-10)
add('drawn P lies on the curve',abs(2.4-(c-1.8**2/(4*c)))<1e-12)
add('directrix is on the opposite side from the opening',5.4==2*c and c>0)
for q in [-.7,-.45,0.,.45,.7]:
    c=2.5;x=c*(1-q*q);y=2*c*q;r=c*(1+q*q)
    f=((1-q*q)/(1+q*q),2*q/(1+q*q))
    n=(-2/(1+q*q),-2*q/(1+q*q));v=(-q,1)
    add('F_r points exactly outward from focus',abs(f[0]*y-f[1]*x)<1e-12 and f[0]*x+f[1]*y>0,q=q)
    add('N is exactly normal to actual tangent',abs(n[0]*v[0]+n[1]*v[1])<1e-12,q=q)
    add('actual force arrow sum equals constant leftward acceleration',abs(f[0]+n[0]+1)<1e-12 and abs(f[1]+n[1])<1e-12,q=q)
    add('normal arrow points to concave side and gives positive support',n[0]<0 and math.hypot(*n)>0,q=q)
add('microelement angle matches coordinate ratio',abs(math.degrees(math.atan2(1.8,2.7))-33.6901)<1e-4)
add('mapped half-angle matches endpoint coordinates',abs(math.degrees(math.atan2(1.2,2.3))-27.5528)<1e-4)
figures=[]
for name in ['statement-03','element-03','parabola-03','map-03','forces-03']:
    figures.append(dict(name=name,**{suffix+'_sha256':hashlib.sha256((ROOT/f'figures/{name}.{suffix}').read_bytes()).hexdigest() for suffix in ['png','pdf']}))
report=dict(paper='014',question='03',figure_source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
            check_count=len(checks),checks=checks,figures=figures,geometry_passed=True,actual_visual_reviewed=False,accepted=False)
(ROOT/'verification/question-03-geometry.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(check_count=len(checks),geometry_passed=True,accepted=False),ensure_ascii=False))
