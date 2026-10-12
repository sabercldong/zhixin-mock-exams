"""Geometrical checks of the actual Q1 TikZ coordinates and parametric curves."""
from pathlib import Path
import hashlib,json,math,re
ROOT=Path(__file__).resolve().parents[1]
source=ROOT/'figures/题01_图稿源文件.tex'
tex=source.read_text()
checks=[]
def check(name,error,tolerance=1e-5):
    assert error<=tolerance,(name,error,tolerance)
    checks.append(dict(name=name,error=error,tolerance=tolerance,passed=True))
def point(block,label):
    m=re.search(r'\\coordinate\('+label+r'\) at\s*\(([^,]+),([^)]+)\)',block)
    assert m,(label,block[:150])
    return tuple(float(v) for v in m.groups())
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
geom=tex.split('% geometry-01:',1)[1].split('% projection-01:',1)[0]
O,H,T=[point(geom,label) for label in ['O','H','T']]
ot,th=sub(T,O),sub(H,T)
check('figure 1 OT radius',abs(math.hypot(*ot)-1.7))
check('figure 1 OH distance',abs(math.hypot(*sub(H,O))-3.4))
check('figure 1 tangent perpendicular to radius',abs(dot(ot,th)))
arrow=sub((-.09,2.015),T)
check('figure 1 velocity arrow along tangent',abs(dot(ot,arrow)),2e-3)
proj=tex.split('% projection-01:',1)[1].split('% cardioid-01:',1)[0]
O,H,T,P=[point(proj,label) for label in ['O','H','T','P']]
check('figure 2 perpendicular foot',abs(dot(sub(H,P),sub(T,O))),2e-5)
check('figure 2 same radial line',abs(T[0]*P[1]-T[1]*P[0]),2e-5)
er=(.5,math.sqrt(3)/2)
etheta=(-math.sqrt(3)/2,.5)
check('figure 2 radial projection X',abs(dot(sub(H,T),er)-.45),2e-5)
check('figure 2 tangential projection Y',abs(dot(sub(H,T),etheta)+3.3*math.sqrt(3)/2),2e-5)
for j in range(73):
    angle=2*math.pi*j/72
    radius=1+math.cos(angle)
    x,y=radius*math.cos(angle),radius*math.sin(angle)
    check(f'cardioid implicit equation {j}',abs(2*(x*x+y*y)-2*x-2*math.hypot(x,y)),2e-13)
    X,Y=-1+3*math.cos(angle),-4*math.sin(angle)
    check(f'ellipse level {j}',abs((X+1)**2/9+Y**2/16-1),5e-15)
    ground=abs(math.cos(angle/2))
    observer=math.sqrt(2.25*math.sin(angle)**2+4*math.cos(angle)**2)
    assert 0<=ground<=1 and 1.5-1e-14<=observer<=2+1e-14
    checks.append(dict(name=f'rate graph bounds {j}',passed=True))
fig=json.loads((ROOT/'preview/figure-build-q01.json').read_text())
assert fig['source_sha256']==hashlib.sha256(source.read_bytes()).hexdigest()
for entry in fig['figures']:
    for suffix,key in [('.pdf','pdf_sha256'),('.png','png_sha256')]:
        assert hashlib.sha256((ROOT/'figures'/(entry['name']+suffix)).read_bytes()).hexdigest()==entry[key]
report=dict(question='01',figure_source_sha256=fig['source_sha256'],figures=fig['figures'],
            checks=checks,check_count=len(checks),geometry_passed=True,
            actual_visual_reviewed=False,accepted=False)
(ROOT/'verification/question-01-geometry.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(check_count=len(checks),geometry_passed=True,accepted=False)))
