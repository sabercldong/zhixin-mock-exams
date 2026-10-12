"""真实三维动量旋转椭球的投影线稿，非二维椭圆加标签。"""
from pathlib import Path
import math
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
A,a,b=.9,.65,.46
view=np.array([.30,-.55,.77942286]);view/=np.linalg.norm(view)
right=np.cross(np.array([0.,0.,1.]),view);right/=np.linalg.norm(right)
up=np.cross(view,right);scale=2.35
def project(p):return np.array([p@right,p@up])*scale
def point(t,f):return np.array([A+a*math.cos(t),b*math.sin(t)*math.cos(f),b*math.sin(t)*math.sin(f)])
def line(p,q,style):
    u,v=project(p),project(q)
    return f'\\draw[{style}] ({u[0]:.6f},{u[1]:.6f})--({v[0]:.6f},{v[1]:.6f});'
lines=[]
for phi in np.linspace(0.,2*math.pi,12,endpoint=False):
    ts=np.linspace(.001,math.pi-.001,85)
    for t0,t1 in zip(ts,ts[1:]):
        mid=point((t0+t1)/2,phi);normal=(mid-np.array([A,0,0]))/np.array([a*a,b*b,b*b])
        style='field!65,thin' if normal@view>=0 else 'field!30,dashed,thin'
        lines.append(line(point(t0,phi),point(t1,phi),style))
for t in [math.pi/4,math.pi/2,3*math.pi/4]:
    fs=np.linspace(0,2*math.pi,181)
    for f0,f1 in zip(fs,fs[1:]):
        mid=point(t,(f0+f1)/2);normal=(mid-np.array([A,0,0]))/np.array([a*a,b*b,b*b])
        style='field!65,thin' if normal@view>=0 else 'field!30,dashed,thin'
        lines.append(line(point(t,f0),point(t,f1),style))
origin=np.zeros(3);axes=[(np.array([1.95,0,0]),'p_x','right'),(np.array([0,.82,0]),'p_y','below left'),(np.array([0,0,.82]),'p_z','above')]
for end,label,anchor in axes:
    lines.append(line(origin,end,'vec,gray'))
    x,y=project(end);lines.append(f'\\node[{anchor}] at ({x:.6f},{y:.6f}) {{$'+label+'$};')
u=.35;v=math.sqrt(1-u*u);phi=math.pi/5
plus=np.array([A+a*u,b*v*math.cos(phi),b*v*math.sin(phi)])
minus=np.array([A-a*u,-plus[1],-plus[2]])
for p,label,anchor,col in [(plus,r'\boldsymbol p_+','above right','force'),(minus,r'\boldsymbol p_-','below right','ink')]:
    lines.append(line(origin,p,'vec,'+col));x,y=project(p)
    lines.append(f'\\fill[{col}] ({x:.6f},{y:.6f}) circle (1.4pt) node[{anchor},fill=white,inner sep=1pt] {{$'+label+'$};')
lines.append(line(plus,minus,'gray,dashed'))
x,y=project(np.array([A,0,0]));lines.append(f'\\fill[ink] ({x:.6f},{y:.6f}) circle (1.2pt) node[below,fill=white,inner sep=1pt] {{$A$}};')
lines.append(r'\node[below left] at (0,0) {$O_p$};')
(ROOT/'figures/momentum-08-space.tex').write_text('\n'.join(lines)+'\n')
print('三维线稿',len(lines),'条绘图语句；示意轴比不对应实测质量。')
