"""完整静力优化、两种运动分支的独立三维检查与模型限制证据。"""
from pathlib import Path
import contextlib
import io
import json
import math
import re
import numpy as np
from scipy.optimize import brentq
import verify_question02_static as static

ROOT=Path(__file__).resolve().parents[1]
U=np.ones(3)/math.sqrt(3)
T=np.array([0.,1.,-1.])/math.sqrt(2)
POSITIONS=-np.eye(3)


def check(reactions,radius,W,lam,F,mass,acceleration,inertia,alpha,mu):
    force=reactions.sum(axis=0)-W*U-mass*acceleration
    torque=np.cross(radius*POSITIONS,reactions).sum(axis=0)+lam*radius*F*T-inertia*alpha
    cone=[mu*reactions[i,i]-np.linalg.norm(np.delete(reactions[i],i)) for i in range(3)]
    residual=max(np.max(abs(force)),np.max(abs(torque)))/(1+W+abs(lam*radius*F))
    assert residual<1e-12,(force,torque)
    assert min(cone)>-1e-10 and min(np.diag(reactions))>=-1e-10,(cone,reactions)
    return float(residual)


def roll_reactions(q,beta,W=1.,mass=1.,radius=1.):
    w=W/math.sqrt(3)
    inertia=beta*mass*radius*radius
    # 解平动和转动的2x2线性系统，不调用正文的闭式加速度。
    # 2f-ma=w; sqrt(2)f+sqrt(2)I*a/r^2=qW.
    f,a=np.linalg.solve(np.array([[2.,-mass],[math.sqrt(2),math.sqrt(2)*inertia/radius**2]]),
                        np.array([w,q*W]))
    s=f*f/w;normal=w+s
    reactions=np.array([[0.,0.,0.],[f,normal,-s],[f,-s,normal]])
    return reactions,a,math.hypot(f,s)/normal,inertia


def main():
    with contextlib.redirect_stdout(io.StringIO()):static.main()
    diagnostic=json.loads((ROOT/'build/question02-static-diagnostic.json').read_text())
    rng=np.random.default_rng(3402)
    max_roll=max_spin=0.
    max_velocity=0.
    for _ in range(300):
        lam=rng.uniform(.45,.95);q=rng.uniform(1/math.sqrt(6)+1e-6,lam-1e-6)
        G=rng.uniform(.5,4.);F=q*G/(lam-q);W=G+F
        radius=rng.uniform(.2,3.);mass=rng.uniform(.5,4.);beta=rng.uniform(.1,1.)
        reactions,a,need,inertia=roll_reactions(q,beta,W,mass,radius)
        mu=(1+need)/2
        alpha=np.array([0.,a/radius,-a/radius])
        max_roll=max(max_roll,check(reactions,radius,W,lam,F,mass,np.array([a,0.,0.]),inertia,alpha,mu))
        v=rng.uniform(.1,4.);omega=np.array([0.,v/radius,-v/radius])
        velocities=np.array([v,0.,0.])+np.cross(omega,radius*POSITIONS)
        assert np.max(abs(velocities[1:]))<1e-12 and velocities[0,0]>0
        max_velocity=max(max_velocity,float(np.max(abs(velocities[1:]))))
    for _ in range(300):
        mu=rng.uniform(0,.5);lam=rng.uniform(.45,.95)
        # 由三点受力线性方程直接解法向力，再计算阻力矩。
        normals=np.linalg.solve(np.array([[1.,2*mu],[-mu/math.sqrt(2),1.]]),np.ones(2)/math.sqrt(3))
        P,N=normals;p=mu*P;f=mu*N
        contacts=np.array([[P,-p/math.sqrt(2),-p/math.sqrt(2)],[f,N,0.],[f,0.,N]])
        kd=-float(np.dot(np.cross(POSITIONS,contacts).sum(axis=0),T))
        q=rng.uniform(kd+1e-6,lam-1e-6);F=q/(lam-q);W=1+F
        reactions=contacts*W;inertia=rng.uniform(.1,2.)
        actual_torque=np.cross(POSITIONS,reactions).sum(axis=0)+lam*F*T
        alpha=actual_torque/inertia
        assert np.dot(alpha,T)>0
        max_spin=max(max_spin,check(reactions,1.,W,lam,F,1.,np.zeros(3),inertia,alpha,mu))
        velocities=np.cross(T,POSITIONS)
        for i in range(3):
            tangent=reactions[i].copy();tangent[i]=0
            assert np.linalg.norm(np.cross(tangent,velocities[i]))<1e-10
            assert np.dot(tangent,velocities[i])<=0
    # 变式的最大q由原始受力系统计算摩擦需求，再数值求根。
    variations=[]
    mu=.46;lam=.6
    for beta in [.4,2/3]:
        root=brentq(lambda q:roll_reactions(q,beta)[2]-mu,1/math.sqrt(6),lam,xtol=1e-14)
        c=mu/math.sqrt(1-mu*mu)
        predicted=(1+(1+2*beta)*(2*c-1))/math.sqrt(6)
        assert abs(root-predicted)<1e-12
        variations.append(dict(beta=beta,q_max_numerical=root,force_upper_over_G=root/(lam-root)))
    # 高摩擦静力自锁：构造原始三维反力，凸组合取得给定有限力矩。
    W=1.;w=W/math.sqrt(3);mu=.8;P=50.;p=mu*P;f=(w-P)/2;s=f*f/(w+p/math.sqrt(2));N=w+p/math.sqrt(2)+s
    large=np.array([[P,-p/math.sqrt(2),-p/math.sqrt(2)],[f,N,-s],[f,-s,N]])
    capacity=-float(np.dot(np.cross(POSITIONS,large).sum(axis=0),T))
    q=.9;mix=q/capacity;reactions=mix*large+(1-mix)*np.eye(3)*w
    residual_self=check(reactions,1.,W,1.,q,1.,np.zeros(3),1.,np.zeros(3),mu)
    # 几何检查读取实际题图的半径与边长定义。
    source=(ROOT/'figures/题02_图稿源文件.tex').read_text()
    radius=float(re.search(r'\\def\\rad\{([\d.]+)\}',source).group(1))
    side=float(re.search(r'\\def\\L\{([\d.]+)\}',source).group(1))
    assert 2*radius<side
    C=np.ones(3)*radius;points=C+radius*POSITIONS
    midpoint=(points[1]+points[2])/2
    assert abs(np.linalg.norm(C-midpoint)-radius/math.sqrt(2))<1e-12
    assert abs(np.dot(C-midpoint,points[1]-points[2]))<1e-12
    assert np.max(abs(np.linalg.norm(points-C,axis=1)-radius))<1e-12
    # 正式答案是有条件的模式可行性与“不唯一”的证明，不宣称唯一真实运动。
    report=dict(status='pass',static_optimization_cases=len(diagnostic['rows']),
                static_max_residual=max(row['equality_residual'] for row in diagnostic['rows']),
                rolling_cases=300,spin_cases=300,max_rolling_residual=max_roll,
                max_spin_residual=max_spin,max_no_slip_velocity_residual=max_velocity,
                two_mode_counterexample=diagnostic['instantaneous_two_mode_counterexample'],
                variation_root_checks=variations,self_locking_residual=residual_self,
                diagram_geometry='pass',
                answer_scope='静力承载与两种瞬时模式的可行条件；证明原题不足以选择唯一分支。')
    (ROOT/'build/question02-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
