"""第024套：原几何/积分/矢量场与独立数值核验，不用结论自证。"""
from pathlib import Path
import json
import math
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss

ROOT=Path(__file__).resolve().parents[1]
def save(q,**data):
    data={'status':'passed',**data}
    (ROOT/'build').mkdir(exist_ok=True)
    (ROOT/'build'/f'question{q:02}-verification.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    return data

def derivative(f,t,h=0.0003):
    fm2,fm1,f0,fp1,fp2=[f(t+i*h) for i in [-2,-1,0,1,2]]
    v=(fm2-8*fm1+8*fp1-fp2)/(12*h)
    a=(-fm2+16*fm1-30*f0+16*fp1-fp2)/(12*h*h)
    return v,a

def q1():
    # 两条直线的Cartesian交点，而非极坐标答案的代入。
    def meet(t,opposite):
        if abs(t)<1e-12:return np.array([2/3 if opposite else 2.0,0.0])
        ua=np.array([np.cos(t),np.sin(t)])
        ub=np.array([np.cos(np.pi-2*t),np.sin(np.pi-2*t)]) if opposite else np.array([np.cos(2*t),np.sin(2*t)])
        # A + a*ua = B + r*ub.
        ar=np.linalg.solve(np.column_stack((ua,-ub)),np.array([1.0,0.0]))
        return ar[0]*ua
    result=[]
    for opposite in [False,True]:
        for t in [0,np.pi/4]:
            point=meet(t,opposite);v,a=derivative(lambda x:meet(x,opposite),t)
            expected_r=(1/3 if t==0 else 1) if opposite else 1
            expected_v=(2/3 if t==0 else 2*np.sqrt(5)) if opposite else 2
            expected_a=(4/9 if t==0 else 4*np.sqrt(65)) if opposite else 4
            assert abs(np.linalg.norm(point-[1,0])-expected_r)<1e-9
            assert abs(np.linalg.norm(v)-expected_v)<1e-7
            assert abs(np.linalg.norm(a)-expected_a)<5e-6,(t,opposite,a)
            result.append(dict(opposite=opposite,omega_t=t,r_over_l=expected_r,v_over_l_omega=expected_v,a_over_l_omega_squared=expected_a))
    return save(1,cartesian_line_intersection_and_five_point_derivatives=result,
                qualification='t=0用连续轨迹极限；反向光束初始指向与转动正方向明示。')

def q2():
    # 单位位移时以能量最小的绳段伸长求动滑轮等效刚度。
    k=7.;X=.3;ku=2*k;kl=k
    xu=2*X*kl/(ku+kl);xl=2*X-xu
    energy=.5*ku*xu*xu+.5*kl*xl*xl
    keff=2*energy/X**2
    assert abs(keff-8*k/3)<1e-12
    checks=[]
    for a,b in [(1.,2.),(2.,2.01),(.5,3.)]:
        d=b-a
        compliance=quad(lambda t:1/(a+d*t),0,1)[0]
        closed=math.log(b/a)/d
        stretch=quad(lambda t:quad(lambda v:a+d*v,t,1)[0]/(a+d*t),0,1)[0]
        analytic=(b*b*math.log(b/a)-(b*b-a*a)/2)/(2*d*d)
        assert abs(compliance-closed)<1e-12
        assert abs(stretch-analytic)<1e-10
        checks.append(dict(S1=a,S2=b,dimensionless_compliance=compliance,dimensionless_self_weight_extension=stretch))
    return save(2,pulley_stiffness_over_k=keff/k,short_bar_stiffnesses_over_k=[9,6,3],
                composite_stiffness_over_k=18/11,nonuniform_bar_integrals=checks,
                qualification='第5问应指第4问；密度rho和重力g不能从伸长公式省掉。')

def q3():
    ratios=[1/np.sqrt(30),.2,1/np.sqrt(20)]
    checks=[]
    for r in ratios:
        p=np.arange(1,201)/(1+np.arange(1,201)*r)**2
        assert p[4]>=max(p)-1e-12
        checks.append(dict(r_over_R=float(r),maximizing_N=[int(n+1) for n,v in enumerate(p) if abs(v-max(p))<1e-12]))
    return save(3,integer_scan=checks,closed_interval=[float(1/np.sqrt(30)),float(1/np.sqrt(20))],
                qualification='允许并列最大时闭区间，要求唯一最大时开区间。')

def q4():
    l=2.;a=l/(2*np.sqrt(3));q=.8;b=.3;m=1.;x0=.2
    Q=q/np.sqrt(3)+b*a/(2)*(a*a+x0*x0)**1.5/x0
    n=np.array([-np.sqrt(3)/2,.5]);t=np.array([.5,np.sqrt(3)/2])
    rotations=[np.array([[np.cos(v),-np.sin(v)],[np.sin(v),np.cos(v)]]) for v in [0,2*np.pi/3,4*np.pi/3]]
    def force(x):
        positions=[M@(a*n+x*t) for M in rotations]
        total=0.
        for i,ri in enumerate(positions):
            fi=-q*Q*ri/np.linalg.norm(ri)**3
            for j,rj in enumerate(positions):
                if j!=i:fi+=q*q*(ri-rj)/np.linalg.norm(ri-rj)**3
            ei=-b/2*np.array([-ri[1],ri[0]])
            total+=(fi+q*ei)@(rotations[i]@t)
        return total/3
    assert abs(force(x0))<1e-12
    h=1e-6;slope=(force(x0+h)-force(x0-h))/(2*h)
    omega2=q*(Q-q/np.sqrt(3))*(a*a-2*x0*x0)/(m*(a*a+x0*x0)**2.5)
    assert abs(slope/m+omega2)<1e-9
    period=2*np.pi/np.sqrt(omega2)
    sol=solve_ivp(lambda time,y:[y[1],force(y[0])/m],[0,period],[x0+1e-6,0],rtol=1e-11,atol=1e-13,max_step=period/300)
    assert abs(sol.y[0,-1]-(x0+1e-6))<1e-9
    return save(4,Q_for_example=float(Q),Q0_over_q=float(1/np.sqrt(3)),stable_x_over_l_upper=float(1/(2*np.sqrt(6))),
                cartesian_force_residual=float(force(x0)),small_oscillation_period=float(period),
                qualification='原无场Q0为阈值，严格稳定要求Q>Q0；圆柱磁区中心取重心且涵盖整个槽。')

def sphere_quadrature(n=220):
    u,w=leggauss(n);phi=2*np.pi*np.arange(2*n)/(2*n)
    xx=np.sqrt(1-u[:,None]**2)*np.cos(phi)[None,:]
    yy=np.sqrt(1-u[:,None]**2)*np.sin(phi)[None,:]
    zz=np.broadcast_to(u[:,None],xx.shape)
    points=np.stack([xx,yy,zz],axis=-1).reshape(-1,3)
    weights=np.broadcast_to(w[:,None]*2*np.pi/(2*n),xx.shape).reshape(-1)
    return points,weights

def q5():
    surface,weights=sphere_quadrature()
    A=np.array([2.5,0,0]);B=np.array([0,0,1.5]);P=np.array([.5,.5,.5])
    # 直接积分球面真实感应电荷，不能将外部镜像式伸入导体。
    sigma=np.full(len(surface),(16/15)/(4*np.pi))
    for charge in [A,B]:
        aa=np.linalg.norm(charge)
        sigma-=(aa*aa-1)/(4*np.pi*np.linalg.norm(surface-charge,axis=1)**3)
    diff=P-surface;dist=np.linalg.norm(diff,axis=1)
    ei=np.sum((sigma*weights/dist**3)[:,None]*diff,axis=0)
    vi=np.sum(sigma*weights/dist)
    ext=sum((P-v)/np.linalg.norm(P-v)**3 for v in [A,B])
    expected_vi=16/15-(np.sqrt(2)+np.sqrt(6))/3
    assert np.linalg.norm(ei+ext)<1e-8,(ei,ext)
    assert abs(vi-expected_vi)<1e-8
    assert abs(np.sum(sigma*weights))<1e-9
    d=2.;V=.8
    charge=np.array([0,0,d])
    sig=-(d*d-1)/(4*np.pi*np.linalg.norm(surface-charge,axis=1)**3)+V/(4*np.pi)
    field_z=np.sum(sig*weights*(d-surface[:,2])/np.linalg.norm(charge-surface,axis=1)**3)
    expected=V/d**2-d/(d*d-1)**2
    assert abs(field_z-expected)<1e-9
    root=brentq(lambda u:V-u**3/(u*u-1)**2,1.00001,100)
    return save(5,induced_field_normalized=ei.tolist(),induced_potential_normalized=float(vi),
                direct_surface_integral_field_residual=float(np.linalg.norm(ei+ext)),
                isolated_net_charge_residual=float(np.sum(sigma*weights)),fixed_potential_force_normalized=float(field_z),
                force_zero_example_d_over_R=float(root),
                qualification='第1问电势按孤立初始电中性模型；P在导体内部，外部镜像式不能在P直接求值。')

def q6():
    h=6.62607015e-34;kb=1.380649e-23;u=1.66053906892e-27
    mass=20*u;d=.5e-9;p=h/d;energy=p*p/(2*mass)
    temp=energy/(1.5*kb)
    rms=np.sqrt(3*kb*temp/mass)
    assert abs(h/(mass*rms)/d-1)<1e-14
    # 直接积分Maxwell速度分布的动能，与压力方程/热容路线独立。
    kinetic=quad(lambda v:np.sqrt(2/np.pi)*v**2*np.exp(-v*v/2)*v*v/2,0,np.inf)[0]
    assert abs(kinetic-1.5)<1e-10
    return save(6,characteristic_temperature_K=float(temp),characteristic_speed_m_per_s=float(rms),
                Maxwell_average_energy_over_kBT=kinetic,constants={'h':h,'k_B':kb,'u':u},
                qualification='题设d=lambda特征尺度，动量采用均方根；不是一般衍射唯一温度。')

def q7():
    psi=2*np.pi*np.arange(1024)/1024
    fields=np.column_stack((np.cos(psi),np.sin(psi)))
    results=[]
    for theta in [0,np.pi/6,np.pi/4]:
        axes=[np.array([np.cos(v),np.sin(v)]) for v in [0,theta,2*theta]]
        matrices=[np.outer(v,v) for v in axes]
        arm1=fields@matrices[0]@matrices[2];arm2=fields@matrices[1]@matrices[2]
        intensities=[]
        for delta in [0,np.pi/3,np.pi,2*np.pi]:
            mixed=arm1+np.exp(1j*delta)*arm2
            actual=.25*np.mean(np.sum(abs(mixed)**2,axis=1))
            expected=(np.cos(2*theta)**2+np.cos(theta)**2+2*np.cos(2*theta)*np.cos(theta)**2*np.cos(delta))/8
            assert abs(actual-expected)<1e-12
            intensities.append(float(actual))
        A=(np.cos(2*theta)**2+np.cos(theta)**2)/8
        C=np.cos(2*theta)*np.cos(theta)**2/4
        results.append(dict(theta_degrees=float(theta*180/np.pi),intensities_over_I0=intensities,visibility=float(abs(C)/A)))
    return save(7,random_polarization_direct_projection=results,
                qualification='两臂由同一自然光波前分出；投影后的交叉统计量包含cos(theta)。')

def q8():
    # 三条原点相邻棱自发为零；全部十二棱还产生两两端点约束。
    k=np.array([np.sqrt(2),np.sqrt(3),np.sqrt(5)])
    vals=[]
    for varying in range(3):
        fixed=[j for j in range(3) if j!=varying]
        for aa in [0,1]:
            for bb in [0,1]:
                positions=np.zeros((17,3));positions[:,varying]=np.linspace(0,1,17)
                positions[:,fixed[0]]=aa;positions[:,fixed[1]]=bb
                vals.extend(np.prod(np.sin(positions*k),axis=1).tolist())
    # 远端棱并非自动为零。以下反例使两个分量量子化、第三个连续。
    maxedge=max(abs(v) for v in vals)
    k=np.array([np.pi,2*np.pi,np.sqrt(5)])
    values=[]
    for varying in range(3):
        fixed=[j for j in range(3) if j!=varying]
        for aa in [0,1]:
            for bb in [0,1]:
                positions=np.zeros((17,3));positions[:,varying]=np.linspace(0,1,17)
                positions[:,fixed[0]]=aa;positions[:,fixed[1]]=bb
                values.extend(np.prod(np.sin(positions*k),axis=1).tolist())
    assert max(abs(v) for v in values)<1e-14
    n=40
    pts=np.arange(-n,n+1);x,y,z=np.meshgrid(pts,pts,pts,indexing='ij')
    radii=np.sqrt(x*x+y*y+z*z);mask=radii<=n
    count=int(np.sum(mask));approx=4*np.pi*n**3/3
    assert abs(count/approx-1)<.02
    energy=np.sum(radii[mask]);integral=np.pi*n**4
    assert abs(energy/integral-1)<.02
    return save(8,arbitrary_k_maximum_edge_field=float(maxedge),
                edge_counterexample=[float(v) for v in k],counterexample_edge_residual=float(max(abs(v) for v in values)),
                full_integer_sphere_count=count,continuum_sphere_count=float(approx),shell_energy_relative_error=float(energy/integral-1),
                toy_energy_coefficient_in_h_units=float(8*np.pi),
                qualification='仅棱边条件最多约束两个分量，不能确定三维离散晶格；独立端点边界和角频率关系须补正。')

def main():
    data={str(i):fn() for i,fn in enumerate([q1,q2,q3,q4,q5,q6,q7,q8],1)}
    (ROOT/'build/preflight-physics.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print('八题独立预核验通过；模型限定与原题缺漏须在正式解析保留。')

if __name__=='__main__':
    main()
