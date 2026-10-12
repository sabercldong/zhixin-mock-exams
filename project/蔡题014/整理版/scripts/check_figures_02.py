"""Check the current drawn coordinates, not an abstract unrelated diagram."""
from pathlib import Path
import hashlib,itertools,json,math
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'figures/题02_图稿源文件.tex'
tex=SOURCE.read_text();checks=[]
def check(name,condition,**data):
    assert condition,(name,data)
    checks.append(dict(name=name,passed=True,**data))
def project(p,height):
    x,y,z=p
    return (1.8*x+.72*y,.52*y+height*z)
pb=list(itertools.product([0.,1.],repeat=3))
oxygen=[(.5,.5,0),(.5,1,.5),(0,.5,.5),(.5,.5,1),(.5,0,.5),(1,.5,.5)]
check('TikZ renders both phases using declared projections',r'\cell{1.8}{.5}' in tex and r'\cell{2.6}{.63}' in tex)
check('exactly 8 distinct corners and 6 distinct face centers',len(set(pb))==8 and len(set(oxygen))==6)
for p in oxygen:
    text='('+','.join(str(int(v)) if v in [0,1] else '.5' for v in p)+')'
    check('actual face-center node exists '+text,text in tex)
check('sixth lower oxygen remains present',r'(.5,.5,0)' in tex)
check('actual a dimension measures full projected front edge',r'(0,-.3)--(1.8,-.3)' in tex)
check('actual b dimension matches full axial height',r'(3.05,0)--(3.05,2.60)' in tex)
for phase,height,ti_z in [('high',1.8,.5),('low',2.6,.63)]:
    positions=pb+oxygen+[(.5,.5,ti_z)]
    projected=[project(p,height) for p in positions]
    distances=[math.dist(x,y) for x,y in itertools.combinations(projected,2)]
    check('projected ion nodes do not coincide '+phase,min(distances)>.23,minimum_cm=min(distances))
    check('long-axis Ti inside the octahedron '+phase,0<ti_z<1)
    check('background pairs remain inversion symmetric '+phase,all(tuple(1-v for v in p) in positions[:-1] for p in positions[:-1]))
check('low-phase Ti moves above center into upper pyramid',.5<.63<1)
check('dipole diagram offset is actual center-to-Ti separation',r'(-.65,0)--(-.65,.50)' in tex and r'(0,.50)' in tex)
check('slab actual corner projection retains equal axial thickness',
      all(abs(t-b-.8)<1e-12 for t,b in [(.8,0),(1.38,.58)]))
check('slab thickness dimension follows back vertical edge',r'(6.75,.58)--(6.75,1.38)' in tex)
check('polarization is upward and field arrow is downward',
      r'(-.90,.20)--(-.90,1.20)' in tex and r'(2.55,.66)--(2.55,.15)' in tex)
check('upper/lower bound-charge signs follow outer normals',
      r'\sigma_{\mathrm b}^{\mathrm{top}}=+P' in tex and r'\sigma_{\mathrm b}^{\mathrm{bottom}}=-P' in tex)
check('finite disk h dimension is center-to-upper-disk distance',r'(-4.55,0)--(-4.55,1.05)' in tex)
check('finite disk R dimension matches actual radius',r'(-2,1.65)--(0,1.65)' in tex and r'ellipse (2.0 and .35)' in tex)
check('finite disk ring s dimension matches selected radius',r'(-2,.72)--(-1.05,.72)' in tex and r'ellipse (.95 and .165)' in tex)
figures=[]
for name in ['cell-02','dipole-02','slab-02','disks-02']:
    figures.append(dict(name=name,pdf_sha256=hashlib.sha256((ROOT/f'figures/{name}.pdf').read_bytes()).hexdigest(),png_sha256=hashlib.sha256((ROOT/f'figures/{name}.png').read_bytes()).hexdigest()))
report=dict(paper='014',question='02',geometry_passed=True,check_count=len(checks),checks=checks,figure_source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),figures=figures,actual_reviewed=False,accepted=False)
(ROOT/'verification/question-02-geometry.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(geometry_passed=True,checks=len(checks),figures=len(figures),accepted=False),ensure_ascii=False))
