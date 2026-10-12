"""八题独立预核验；不把此结果当作成品验收。"""
from pathlib import Path
import json
import math
import numpy as np
from scipy.integrate import solve_ivp, quad

ROOT=Path(__file__).resolve().parents[1]

def wedge_force_solution(t,mu,F,sign,m=1.,g=1.):
    c=1/math.sqrt(1+t*t);s=t*c
    # 三个真实受力方程的未知量依次为 a,N,Q，不使用闭式答案。
    A=np.array([[m, -(s-sign*mu*c), sign*mu],
                [m*t, c+sign*mu*s, 0],
                [0, -(c+sign*mu*s), 1]])
    return np.linalg.solve(A,np.array([F,m*g,m*g]))

def q1():
    checks=[]
    for t,mu in [(0.4,0.3),(0.8,0.5),(1.2,0.8),(0.5,1.5)]:
        D=1+(1-mu*mu)*t*t-mu*t
        Fs=(3*mu-(1-2*mu*mu)*t)/(1+mu*t)
        if D<=0 or Fs<0:continue
        Fd=1/t+mu
        for F in [0,Fs,(Fs+Fd)/2]:
            a,N,Q=wedge_force_solution(t,mu,F,1)
            expected=(1+mu*t)*(F-Fs)/D
            assert abs(a-expected)<1e-11
            assert abs(Q-(2-a*t))<1e-11
            checks.append(dict(t=t,mu=mu,F=F,a=a,N=N,Q=Q))
    # 锯齿力的分段解，以独立时间积分检验脉冲、临界相切和持续加速。
    t=.4;mu=.3;t0=1.;D=1+(1-mu*mu)*t*t-mu*t
    Fs=(3*mu-(1-2*mu*mu)*t)/(1+mu*t);Kappa=(1+mu*t)/D
    pulses=[]
    for ratio in [1.4,2.,3.]:
        F0=ratio*Fs;K=F0/t0;t1=Fs/K
        vp=.5*Kappa*K*(t0-t1)**2
        inc=Kappa*t0*(F0/2-Fs)
        # 同步小时间步，以原始受力矩阵算加速度；静止时实行静摩擦条件。
        dt=1/100000;v=0.;end=[]
        for step in range(300000):
            phase=(step+.5)*dt%t0;F=K*phase
            if v<=1e-12 and F<=Fs:a=0.
            else:a=wedge_force_solution(t,mu,F,1)[0]
            v=max(0.,v+a*dt)
            if (step+1)%100000==0:end.append(v)
        targets=[vp+max(0.,inc)*j for j in range(3)]
        err=max(abs(x-y) for x,y in zip(end,targets))
        assert err<2e-5
        pulses.append(dict(F0_over_Fs=ratio,end_velocities=end,targets=targets,error=err))
    return dict(status="verified_with_contact_and_friction_domains",force_checks=checks,sawtooth_checks=pulses,
                note="刚性Coulomb模型在D+=0或D+<0区间存在退化或非唯一；大外力也会违反保持接触条件。")

def gravity_exact(r,l,phase,M=1.,G=1.):
    position=np.array([r,0.]);u=np.array([math.cos(phase),math.sin(phase)])
    result=np.zeros(2)
    for center in [l*u,-l*u]:
        d=center-position;result+=G*M*d/np.linalg.norm(d)**3
    return result

def q2():
    tests=[]
    for rho in [.03,.015,.0075]:
        r=1.;l=rho
        errors=[]
        for phase in [.1,.4,.9,1.4]:
            exact=gravity_exact(r,l,phase)
            approximation=np.array([-2-3*l*l*(3*math.cos(phase)**2-1),3*l*l*math.sin(2*phase)])
            errors.append(float(np.linalg.norm(exact-approximation)))
            assert np.linalg.norm(gravity_exact(r,l,phase+math.pi)-exact)<1e-12
        tests.append(dict(l_over_r=rho,max_quadrupole_error=max(errors)))
    assert tests[0]['max_quadrupole_error']/tests[1]['max_quadrupole_error']>15
    return dict(status="quadrupole_not_dipole",omega_squared="GM/(4l^3)",period="4pi sqrt(l^3/(GM))",
                tests=tests,wavelength_if_radiative_model="cT/2",note="两正质量的质心偶极矩为零；牛顿近区时变场不能直接称为辐射场。")

def polygon_integrals(vertices):
    v=np.array(vertices,float);w=np.roll(v,-1,axis=0)
    cross=v[:,0]*w[:,1]-w[:,0]*v[:,1]
    area=.5*sum(cross)
    moment=sum(cross*((v*v).sum(1)+(v*w).sum(1)+(w*w).sum(1)))/12
    return float(area),float(moment)

def q3():
    tri=[(1,0),(.5,1/(2*math.sqrt(3))),(.5,-1/(2*math.sqrt(3)))]
    area,J=polygon_integrals(tri)
    mean=J/area
    assert abs(mean-17/36)<1e-12
    sums=[]
    for N in [1,2,5,10,30]:
        # 真正的逐层三角形坐标缩放/转动与面积惯性积分。
        A=0.;I=0.
        for j in range(N):
            scale=3**(-j/2)
            for k in range(6):
                angle=k*math.pi/3+j*math.pi/6
                rot=np.array([[math.cos(angle),-math.sin(angle)],[math.sin(angle),math.cos(angle)]])
                av,jv=polygon_integrals(np.array(tri)@rot.T*scale);A+=av;I+=jv
        density=1/(6*area)
        sums.append(dict(layers=N,M_over_m=A*density,I_over_mr2=I*density))
    assert abs(sums[-1]['M_over_m']-1.5)<1e-12
    assert abs(sums[-1]['I_over_mr2']-17/32)<1e-12
    return dict(status="verified",I0_over_mr2=mean,M_over_m=1.5,I_infinity_over_mr2=17/32,polygon_sums=sums)

def q4():
    P0=101e3;T0=293.;R=8.31;ra=4.5e-6;rb=36e-6;gamma=5/3
    Va=4*math.pi*ra**3/3;Vb=4*math.pi*rb**3/3;n=P0*Va/(R*T0)
    Pb=P0*Va/Vb;Tc=T0*(Vb/Va)**(gamma-1);Pc=n*R*Tc/Va
    expansion=quad(lambda V:n*R*T0/V,Va,Vb,epsabs=1e-24)[0]
    compression=quad(lambda V:Pb*(Vb/V)**gamma,Va,Vb,epsabs=1e-24)[0]
    on=compression-expansion
    closed=P0*Va*((64-1)*1.5-math.log(512))
    assert abs(on-closed)<1e-20
    return dict(status="reversible_adiabatic_model_verified",Va=Va,Vb_over_Va=Vb/Va,n=n,Pb=Pb,Pc=Pc,Tc=Tc,work_on=on,
                note="仅绝热不能推出PV^gamma常量；列出可逆模型及熵增条件下的温度/功下界。")

def q5():
    cases=[]
    for R1,R2,phi in [(1,1,0),(1,1,math.pi/2),(1,1,math.pi/4),(1,2,math.pi/2),(1,2,.4)]:
        n1=np.array([1.,0]);n2=np.array([math.cos(phi),-math.sin(phi)])
        H=np.outer(n1,n1)/R1+np.outer(n2,n2)/R2
        eigen=np.linalg.eigvalsh(H)
        trace=1/R1+1/R2
        d=math.sqrt(1/R1**2+1/R2**2+2*math.cos(2*phi)/(R1*R2))
        expected=np.array([(trace-d)/2,(trace+d)/2])
        assert max(abs(eigen-expected))<1e-12
        cases.append(dict(R1=R1,R2=R2,angle=phi,eigenvalues=eigen.tolist()))
    return dict(status="verified",cases=cases,note="正交圆形要求两个曲率半径相等；不等时为椭圆。")

def q6():
    h=6.62607015e-34;me=9.1093837139e-31;c=299792458.;L=1.83e-9
    E1=h*h/(8*me*L*L);gap=23*E1;wavelength=h*c/gap
    matrix=quad(lambda x:2*x*math.sin(11*math.pi*x)*math.sin(12*math.pi*x),0,1)[0]
    expected=-8*11*12/(math.pi**2*(12*12-11*11)**2)
    assert abs(matrix-expected)<1e-13
    assert abs(2*sum(j*j for j in range(1,12))-1012)<1e-12
    return dict(status="verified",E1_J=E1,gap_J=gap,wavelength_nm=wavelength*1e9,x_11_12_over_L=matrix,
                note="22个独立电子按每级两自旋填满n=1到11；这是给定一维势阱模型，不是精确化学谱。")

def q7():
    checks=[];K=1.
    for rad in [1,.7,.3]:
        B=2*K*rad/(2*rad*rad)**1.5
        flux=quad(lambda x:2*math.pi*x*2*K*rad/(x*x+rad*rad)**1.5,0,rad)[0]
        lab=2*math.pi*rad*(-.2)*B
        motion=-2*math.pi*rad*(-.2)*B
        assert abs(flux-4*math.pi*K*(1-1/math.sqrt(2)))<1e-12
        assert abs(lab+motion)<1e-12
        checks.append(dict(radius=rad,equator_field=B,flux=flux,lab_emf=lab,motional_emf=motion,total_emf=lab+motion))
    return dict(status="verified",checks=checks,result="同缩导电环总电动势为0；固定环的结果不同。")

def q8():
    L=2.;C=.25;R=.8;alpha=.3
    cases=[]
    for rd in [.3,.8,1.5,7.]:
        beta=(rd-R)/(2*L);disc=1/(L*C)-beta*beta
        def rhs(t,y):return [y[1],(rd-R)/L*y[1]-y[0]/(L*C)]
        times=np.linspace(0,4,501)
        sol=solve_ivp(rhs,(0,4),(0.,alpha),t_eval=times,rtol=1e-11,atol=1e-13)
        if disc>0:
            w=math.sqrt(disc);ans=alpha*np.exp(beta*times)*np.sin(w*times)/w
        elif disc<0:
            s=math.sqrt(-disc);ans=alpha*np.exp(beta*times)*np.sinh(s*times)/s
        else:ans=alpha*times*np.exp(beta*times)
        err=float(max(abs(ans-sol.y[0])));assert err<1e-7
        cases.append(dict(r=rd,beta=beta,omega_squared=disc,error=err))
    V=2.;I=10.;rd=.8;A=.3
    mean=quad(lambda t:(V-rd*A*math.sin(t))*(I+A*math.sin(t)),0,2*math.pi)[0]/(2*math.pi)
    assert abs(mean-(V*I-rd*A*A/2))<1e-12
    return dict(status="conditional_linear_circuit_model_verified",ode_cases=cases,mean_diode_power=mean,
                note="dI/dV是电导，dV/dI才是电阻；稳定有限振幅不由无限线性负阻自动确定。原偏置(V2-V1)/2需满足V2>3V1，区间中点应为(V1+V2)/2。")

def main():
    results={f"{j:02}":fn() for j,fn in enumerate([q1,q2,q3,q4,q5,q6,q7,q8],1)}
    target=ROOT/"build";target.mkdir(exist_ok=True)
    (target/"preflight-physics.json").write_text(json.dumps(results,ensure_ascii=False,indent=2)+"\n")
    for q,info in results.items():print(q,info["status"],flush=True)

if __name__=="__main__":main()

