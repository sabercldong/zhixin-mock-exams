"""生成旋转椭球的空间投影线稿，按表面法向判别前后可见线。"""
from pathlib import Path
import math
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
view=np.array([.25,-.65,math.sqrt(1-.25**2-.65**2)])
right=(np.array([1.,0.,0.])-view[0]*view)/math.sqrt(1-view[0]**2)
up=np.cross(view,right);scale=.55

def projection(point):return scale*np.array([point@right,point@up])
def texpoint(point):
    x,y=projection(point);return f'({x:.5f},{y:.5f})'
def surface(t,phi):return np.array([5*math.cos(t),4*math.sin(t)*math.cos(phi),4*math.sin(t)*math.sin(phi)])

def main():
    pieces=[]
    for phi in np.linspace(0,math.pi,4,endpoint=False):
        for j in range(240):
            t=2*math.pi*j/240;next_t=2*math.pi*(j+1)/240
            p=surface(t,phi);q=surface(next_t,phi)
            normal=(p+q)/2/np.array([25.,16.,16.]);front=normal@view>=0
            style='gray!60,line width=.35pt' if front else 'gray!45,dashed,line width=.25pt'
            pieces.append(f'\\draw[{style}] {texpoint(p)}--{texpoint(q)};')
    for t in [math.pi/6,math.pi/2,5*math.pi/6]:
        for j in range(180):
            phi=2*math.pi*j/180;next_phi=2*math.pi*(j+1)/180
            p=surface(t,phi);q=surface(t,next_phi)
            normal=(p+q)/2/np.array([25.,16.,16.]);front=normal@view>=0
            style='gray!60,line width=.35pt' if front else 'gray!45,dashed,line width=.25pt'
            pieces.append(f'\\draw[{style}] {texpoint(p)}--{texpoint(q)};')
    # 两端只在近顶点帽区域镀银；可见线为蓝色，隐藏线虚线。
    for phi in np.linspace(0,2*math.pi,16,endpoint=False):
        for start in [0.,math.pi-.21]:
            for j in range(12):
                t=start+.21*j/12;next_t=start+.21*(j+1)/12
                p=surface(t,phi);q=surface(next_t,phi);normal=(p+q)/2/np.array([25.,16.,16.])
                style='field,thick' if normal@view>=0 else 'field!50,dashed,thin'
                pieces.append(f'\\draw[{style}] {texpoint(p)}--{texpoint(q)};')
    (ROOT/'figures'/'question-07-space.tex').write_text('% Explicit prolate spheroid projection, a=5 b=4.\n'+'\n'.join(pieces)+'\n')
    print(dict(path=str(ROOT/'figures'/'question-07-space.tex'),segments=len(pieces),axis_projection=right[0],camera=view.tolist()))

if __name__=='__main__':main()
