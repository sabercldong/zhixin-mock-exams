"""生成两相扣圆环的深度排序矢量面片；保留空间坐标、遮挡及绕线。"""
from pathlib import Path
import math
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
R=1.6; minor=.32
view=np.array([-4.,-6.,5.]);view/=np.linalg.norm(view)
right=np.cross(view,[0.,0.,1.]);right/=np.linalg.norm(right)
up=np.cross(right,view)
light=np.array([-.4,-.5,1.]);light/=np.linalg.norm(light)

def surface(phi,theta,coil,radius=minor):
    rho=R+radius*math.cos(theta)
    if coil==1:
        return np.array([rho*math.cos(phi),rho*math.sin(phi),radius*math.sin(theta)])
    return np.array([R+rho*math.cos(phi),-radius*math.sin(theta),rho*math.sin(phi)])

def project(v):
    return (float(v@right),float(v@up))

def point(v):
    x,y=project(v);return f'({x:.5f},{y:.5f})'

def main():
    objects=[]
    for coil,color,n in [(1,'field',18),(2,'force',22)]:
        for i in range(112):
            phi=2*math.pi*i/112;next_phi=2*math.pi*(i+1)/112
            for j in range(24):
                theta=2*math.pi*j/24;next_theta=2*math.pi*(j+1)/24
                vertices=[surface(phi,theta,coil),surface(next_phi,theta,coil),surface(next_phi,next_theta,coil),surface(phi,next_theta,coil)]
                normal=np.cross(vertices[1]-vertices[0],vertices[3]-vertices[0]);normal/=np.linalg.norm(normal)
                shade=int(31+38*(.5+.5*float(normal@light)))
                code=f'\\filldraw[fill={color}!{shade}!white,draw={color}!{shade}!white,line width=.07pt] '+ '--'.join(point(v) for v in vertices)+'--cycle;'
                objects.append((float(np.mean(vertices,axis=0)@view),code))
        # 实际连续螺旋线的代表性画法；示意匝数不替代题目N_i。
        for i in range(1600):
            t=2*math.pi*i/1600;next_t=2*math.pi*(i+1)/1600
            a=surface(t,n*t,coil,minor*1.009);b=surface(next_t,n*next_t,coil,minor*1.009)
            objects.append((float((a+b)@view)/2+.00002,
                            f'\\draw[{color}!85!black,line width=.16pt] {point(a)}--{point(b)};'))
    objects.sort(key=lambda item:item[0])
    target=ROOT/'figures'/'question-05-mesh.tex'
    target.write_text('% Generated from explicit 3D linked torus geometry; far to near.\n'+'\n'.join(code for _,code in objects)+'\n')
    print(dict(mesh_polygons=2*112*24,wire_segments=2*1600,
               minimum_centreline_distance=R,diameter_of_core=2*minor,
               view_direction=view.tolist(),path=str(target)),flush=True)

if __name__=='__main__':main()
