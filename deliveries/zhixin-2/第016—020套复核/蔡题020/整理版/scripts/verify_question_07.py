"""精确椭圆交点/法向反射追踪，与逐次近轴成像交叉核验。"""
from pathlib import Path
import math,json,hashlib
import numpy as np
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]

def hit_and_reflect(point,direction,a=5.,b=4.):
    d=direction/np.linalg.norm(direction);p=point-np.array([a,0.])
    A=d[0]**2/a**2+d[1]**2/b**2
    B=2*(p[0]*d[0]/a**2+p[1]*d[1]/b**2)
    C=p[0]**2/a**2+p[1]**2/b**2-1
    roots=np.roots([A,B,C]);length=min(float(v.real) for v in roots if abs(v.imag)<1e-10 and v.real>1e-8)
    q=point+length*d;normal=np.array([(q[0]-a)/a**2,q[1]/b**2]);normal/=np.linalg.norm(normal)
    return q,d-2*(d@normal)*normal

def trace(h,offset=1.,a=5.,b=4.):
    c=math.sqrt(a*a-b*b);object_x=a-c-offset
    rays=[]
    for focus in [a-c,a+c]:
        point=np.array([object_x,h]);direction=np.array([focus,0.])-point
        first,out=hit_and_reflect(point,direction,a,b)
        second,out2=hit_and_reflect(first,out,a,b)
        rays.append((second,out2,first,out))
    p,d,_,_=rays[0];q,e,_,_=rays[1]
    st=np.linalg.solve(np.column_stack((d,-e)),q-p)
    image=p+st[0]*d
    return dict(object_x=object_x,image=image.tolist(),magnification=image[1]/h,
                right_hits=[ray[2].tolist() for ray in rays],left_hits=[ray[0].tolist() for ray in rays])

def main():
    a=sp.Rational(5);b=sp.Rational(4);f=b*b/(2*a)
    x=sp.symbols('x');c=sp.sqrt(a*a-b*b);u1=a+c+x
    v1=sp.factor(f*u1/(u1-f));u2=2*a-v1;v2=sp.factor(f*u2/(u2-f))
    magnification=sp.factor(v1*v2/(u1*u2))
    assert v2.subs(x,1)==sp.Rational(1192,597) and magnification.subs(x,1)==sp.Rational(32,597)
    exact=[]
    X=float(v2.subs(x,1));M=float(magnification.subs(x,1))
    for h in [.01,.005,.0025,.00125]:
        row=trace(h);row.update(h=h,position_error=row['image'][0]-X,
                              magnification_error=row['magnification']-M)
        exact.append(row)
    for i in range(1,len(exact)):
        factor=abs(exact[i]['position_error']/exact[i-1]['position_error'])
        assert .20<factor<.30
    assert abs(exact[-1]['position_error'])<1e-4
    # 解析的近轴两族光线独立求交。
    Xg,Yg=sp.symbols('Xg Yg')
    intersection=sp.solve([Yg+16*(Xg-2),Yg-(8-Xg)/112],[Xg,Yg])
    assert intersection=={Xg:sp.Rational(1192,597),Yg:sp.Rational(32,597)}
    # 改变距焦点的距离，用真实曲线反射核验，而非换原公式自证。
    variants=[]
    for offset in [.5,1.,1.5]:
        prediction_X=float(v2.subs(x,offset));prediction_M=float(magnification.subs(x,offset))
        ray=trace(.0005,offset=offset)
        assert abs(ray['image'][0]-prediction_X)<1e-4 and abs(ray['magnification']-prediction_M)<1e-4
        variants.append(dict(distance_left_of_focus=offset,object_x=ray['object_x'],
                             paraxial_image_x=prediction_X,paraxial_magnification=prediction_M,
                             exact_image_x=ray['image'][0],exact_magnification=ray['magnification']))
    # 独立检查一族非焦点入射光线，在近轴像平面上的共同高度。
    bundles=[]
    for height in [.001,.0005]:
        residuals=[]
        for slope_factor in [-1.2,-1.,-.5,-1/7,0.,.2]:
            right_hit,d=hit_and_reflect(np.array([1.,height]),np.array([1.,height*slope_factor]))
            left_hit,out=hit_and_reflect(right_hit,d)
            image_y=left_hit[1]+(X-left_hit[0])*out[1]/out[0]
            residuals.append(image_y-M*height)
        assert max(abs(v) for v in residuals)/height<1e-4
        bundles.append(dict(h=height,nonfocal_slope_factors=[-1.2,-1.,-.5,-1/7,0.,.2],
                            residual_heights_at_paraxial_image_plane=residuals))
    mirror=sp.Matrix([[1,0],[-sp.Rational(5,8),1]])
    propagation=lambda d:sp.Matrix([[1,d],[0,1]])
    system=mirror*propagation(10)*mirror*propagation(9)
    final_matrix=propagation(sp.Rational(1192,597))*system
    assert system==sp.Matrix([[-sp.Rational(21,4),-sp.Rational(149,4)],[sp.Rational(85,32),sp.Rational(597,32)]])
    assert final_matrix[0,1]==0 and final_matrix[0,0]==sp.Rational(32,597) and final_matrix.det()==1
    sphere_f=sp.Rational(5,2);sphere_v1=sphere_f*9/(9-sphere_f);sphere_u2=10-sphere_v1
    sphere_v2=sp.factor(sphere_f*sphere_u2/(sphere_u2-sphere_f));sphere_M=sp.factor(sphere_v1*sphere_v2/(9*sphere_u2))
    # 几何焦点合并后改选任意两条光线，不能继续用两个相同焦点求交。
    sphere_rays=[]
    for slope in [-.0002,.0001]:
        first,d=hit_and_reflect(np.array([1.,.001]),np.array([1.,slope]),a=5.,b=5.)
        second,out=hit_and_reflect(first,d,a=5.,b=5.);sphere_rays.append((second,out))
    p,d=sphere_rays[0];q,e=sphere_rays[1]
    st=np.linalg.solve(np.column_stack((d,-e)),q-p);sphere_image=p+st[0]*d
    assert abs(sphere_image[0]-float(sphere_v2))<1e-5 and abs(sphere_image[1]/.001-float(sphere_M))<1e-5
    sphere=dict(v1=str(sphere_v1),u2=str(sphere_u2),v2=str(sphere_v2),M=str(sphere_M),exact_ray_image=sphere_image.tolist())
    files=['scripts/verify_question_07.py']
    files += [f for f in ['drafts/question-07.md','figures/题07_图稿源文件.tex','scripts/generate_question_07_space.py','figures/question-07-space.tex'] if (ROOT/f).exists()]
    complete=(ROOT/'drafts/question-07.md').exists()
    if complete:
        draft=(ROOT/'drafts/question-07.md').read_text()
        complete=len([line for line in draft.splitlines() if line.startswith('## ')])==9 and 'DRAFT' not in draft
    report=dict(question=7,verified_math=True,document_complete=complete,units='cm',
                first_image_distance=str(v1),final_image_x=str(v2),total_magnification=str(magnification),
                exact_ray_traces=exact,independent_focal_ray_intersection={str(k):str(v) for k,v in intersection.items()},
                variants=variants,arbitrary_ray_bundles=bundles,unfolded_matrix=str(system),image_matrix=str(final_matrix),
                spherical_variant=sphere,source_sha256={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in files})
    (ROOT/'build'/('verification-q07.json' if complete else 'verification-q07-preliminary.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False),flush=True)

if __name__=='__main__':main()
