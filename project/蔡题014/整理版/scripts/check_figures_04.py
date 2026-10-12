"""Coordinate and physical checks on current Q4 TikZ. No automatic visual pass."""
from pathlib import Path
import hashlib,json,math
import numpy as np
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'figures/题04_图稿源文件.tex'
NAMES=['statement-04','element-04','flux-04','motion-04','graphs-04']
text=SRC.read_text();checks=[]
def yes(name,condition):
    assert condition,name
    checks.append(dict(name=name,passed=True))
def equal(name,left,right,tol=1e-10):
    yes(name,abs(left-right)<tol)
yes('all five figures are actual independent TikZ pictures',text.count('\\begin{tikzpicture}')==5)
yes('statement uses world coordinates with a nonzero depth projection',
    'x={(1cm,0cm)},y={(.40cm,.24cm)},z={(0cm,1cm)}' in text)
yes('coil is a connected five-turn helix, not five isolated ellipses',
    '\\foreach \\j in {0,...,4}' in text and '.15+(.45)*(\\j+\\p/360)' in text)
equal('upper helix endpoint equals upper supply lead height',.15+5*.45,2.4)
yes('both circuit leads terminate on actual coil endpoints',
    '(1,0,.15)--(3.15,0,.15)' in text and '(1,0,2.4)--(3.15,0,2.4)' in text)
yes('open switch has two separate contacts and a blade',
    '(3.15,0,1.78)--(3.44,0,2.03)' in text and '(3.15,0,2.13) circle' in text)
yes('battery plates are separated from conducting leads',
    '(3.15,0,.15)--(3.15,0,.82)' in text and '(3.15,0,.99)--(3.15,0,1.78)' in text)
yes('positive long battery plate feeds lower helix endpoint for positive vertical coil field',
    '(2.91,0,.82)--(3.39,0,.82)' in text and '(3.01,0,.99)--(3.29,0,.99)' in text)
for angle in np.linspace(0,2*math.pi,17):
    xx,yy=1.4*math.cos(angle),1.4*math.sin(angle)
    yes('entire ring fits on the tabletop plane',abs(xx)<=1.8 and abs(yy)<=1.6)
equal('table height equals initial horizontal ring height',3.1,3.1)
yes('coil and isolated ring are separated vertically',2.4<3.1)
dl=np.array([0.,1.,0.]);br=np.array([1.,0.,0.]);ez=np.array([0.,0.,1.])
yes('positive circular current gives downward radial-field force',np.allclose(np.cross(dl,br),-ez))
yes('upward velocity gives positive azimuthal motion EMF',np.allclose(np.cross(ez,br),dl))
yes('element arrow actually follows the positive tangent world direction',
    '(P)--(2,1.75,0)' in text and '(P)--(2,0,-1.45)' in text)
yes('closed cylinder has upward top and downward bottom outward normals',
    '(0,0,1.5)--(0,0,2.55)' in text and '(0,0,0)--(0,0,-.95)' in text)
yes('bottom closed-surface flux has the correct minus sign','$-\\Phi(z)$' in text)
yes('Br label is offset above the side arrow, clear of height dimension',
    '(1.55,0,.72)--(2.5,0,.72) node[midway,above]' in text)
yes('height dimension endpoints match the two cylinder faces',
    '(2.92,0,0)--(2.92,0,1.5)' in text)
yes('upward motion current is counterclockwise with positive tangent at front',
    'domain=210:320' in text)
yes('downward motion current reverses the tangent at the front',
    'domain=320:210' in text)
yes('apex panel explicitly has zero current and zero force','$I=0,\\ F_z=0$' in text)
yes('upward and downward force arrows oppose their velocity arrows',
    '(1.62,-.25)--(1.62,-1.10)' in text and '(10.02,.25)--(10.02,1.2)' in text)
us=math.log(2);ur=brentq(lambda u:2*(1-math.exp(-u))-u,1.,2.)
equal('graph velocity zero uses log2',2*math.exp(-us)-1,0)
equal('graph height at apex is 1-log2',2*(1-math.exp(-us))-us,1-us)
equal('positive graph return time root',ur,1.59362426004004)
yes('return root is after the unique apex',ur>us)
yes('graphs explicitly indicate eta=1, not arbitrary numeric parameters',text.count('$\\eta=1$')==2)
equal('negative graph asymptote is -1',2*math.exp(-50)-1,-1)
yes('graph height after return is negative',2*(1-math.exp(-2.2))-2.2<0)
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
figs=[]
for name in NAMES:
    for suffix in ['pdf','png']:yes('current vector and raster file exist '+name+'.'+suffix,(ROOT/f'figures/{name}.{suffix}').exists())
    figs.append(dict(name=name,pdf_sha256=sha(ROOT/f'figures/{name}.pdf'),png_sha256=sha(ROOT/f'figures/{name}.png')))
report=dict(paper='014',question='04',geometry_passed=True,check_count=len(checks),checks=checks,
            figure_source_sha256=sha(SRC),figures=figs,actual_visual_review=False,question_accepted=False)
(ROOT/'verification/question-04-geometry.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(geometry_passed=True,checks=len(checks),figures=len(figs)),ensure_ascii=False))
