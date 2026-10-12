"""独立模型核验；全运动方程、轨道积分、离散波动算子，不只回代答案。"""
from pathlib import Path
import json, math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.linalg import eigh_tridiagonal

ROOT=Path(__file__).resolve().parents[1]
def save(q,data):
    data={'status':'pass',**data}
    (ROOT/'build').mkdir(exist_ok=True)
    (ROOT/'build'/f'question{q:02}-verification.json').write_text(
        json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(f'第{q}题：'+data['method'],flush=True)

def q1():
    phi=np.array([np.pi/3,np.pi,5*np.pi/3])
    pos=np.column_stack([np.cos(phi),np.sin(phi)])
    D=[np.array([[1.,0.,-y],[0.,1.,x]]) for x,y in pos]
    stiffness=sum(d.T@d for d in D)
    err=0.; checks=0
    for s in [.01,.3,1.,1.7]:
        for theta in np.linspace(0,2*np.pi,721)[:-1]:
            external=np.array([np.sin(theta),-np.cos(theta),-s])
            deformation=np.linalg.solve(stiffness,external)
            f=np.array([-d@deformation for d in D])
            ref=(np.array([-np.sin(theta),np.cos(theta)])+s*np.column_stack([-np.sin(phi),np.cos(phi)]))/3
            err=max(err,float(np.max(abs(f-ref))))
            assert np.argmax(np.linalg.norm(f,axis=1))==np.argmax(np.cos(theta-phi)) or np.isclose(
                np.max(np.cos(theta-phi)),np.cos(theta-phi)[np.argmax(np.linalg.norm(f,axis=1))])
            checks+=1
    assert err<2e-15
    pair=np.array([[np.sqrt(3)/2,.5],[-np.sqrt(3)/2,-.5],[0,0]])
    assert np.linalg.norm(pair.sum(axis=0))<1e-15
    assert abs(np.sum(pos[:,0]*pair[:,1]-pos[:,1]*pair[:,0]))<1e-15
    save(1,dict(method='刚体接触刚度矩阵直接求解与自平衡力反例',parameter_cases=checks,
                maximum_component_error=err,unique_regions_require_equal_tangential_stiffness=True))

def q2():
    b0=80.; beta=.01
    def field(r):
        x,y,z=r
        return b0*np.array([-beta*z*x,-beta*z*y,1+beta*z*z])
    def rhs(t,s):
        return np.r_[s[3:],np.cross(s[3:],field(s[:3]))]
    sol=solve_ivp(rhs,(0,32),[0,0,0,1,0,.4],method='DOP853',
                  rtol=3e-10,atol=1e-12,max_step=.025,dense_output=True)
    t=np.linspace(0,32,5001);state=sol.sol(t).T
    bs=np.array([field(s[:3]) for s in state]);bn=np.linalg.norm(bs,axis=1)
    v=state[:,3:];v2=np.sum(v*v,axis=1)
    parallel=np.sum(v*bs,axis=1)/bn
    mu=(v2-parallel**2)/(2*bn)
    drift=float(np.max(abs(mu/mu[0]-1)))
    predicted=.4/np.sqrt(beta);zmax=float(state[:,2].max())
    assert drift<.003 and abs(zmax-predicted)/predicted<.003
    assert np.max(abs(v2-v2[0]))<1e-6
    # 端点缺口为一次与二次幂的时间积分具有不同收敛性。
    linear=[2*(1-np.sqrt(e)) for e in [1e-2,1e-4,1e-6]]
    quadratic=[-np.log(e) for e in [1e-2,1e-4,1e-6]]
    assert linear[-1]<2 and quadratic[-1]>quadratic[0]*2
    save(2,dict(method='满足散度零的轴对称场中直接积分三维洛伦兹方程',
                adiabatic_moment_relative_variation=drift,z_turn_numeric=zmax,z_turn_adiabatic=predicted,
                kinetic_energy_error=float(np.max(abs(v2-v2[0]))),
                equality_requires_endpoint_time_test=True))

def particle_ode(B,sign):
    def rhs(t,s):
        a,b,va,vb=s[:2],s[2:4],s[4:6],s[6:8]
        d=a-b;r=np.linalg.norm(d)
        ca=sign*d/r**3
        return np.r_[va,vb,ca+B*np.array([-va[1],va[0]]),
                     -ca+sign*B*np.array([-vb[1],vb[0]])]
    return rhs
def q3():
    init=[-.5,0,.5,0,0,0,0,0]
    results={}
    for sign,b in [(1,1.),(-1,6.)]:
        def turn(t,s):
            s=np.asarray(s);r=s[2:4]-s[:2];return float(np.dot(r,s[6:8]-s[4:6]))
        turn.direction=-1 if sign==1 else 1
        turn.terminal=True
        sol=solve_ivp(particle_ode(b,sign),(0,30),init,events=turn,
                      method='DOP853',rtol=2e-11,atol=2e-13,max_step=.01)
        assert len(sol.t_events[0])==1
        last=sol.y_events[0][0];rad=float(np.linalg.norm(last[2:4]-last[:2]))
        reference=brentq(lambda x:x*x+x-1-1/x-16/b**2,1,20) if sign==1 else .5*(1+np.sqrt(1-16/b**2))
        assert abs(rad-reference)<1e-9
        r=np.linalg.norm(sol.y[2:4]-sol.y[:2],axis=0)
        energy=.5*np.sum(sol.y[4:]**2,axis=0)+sign/r
        assert np.max(abs(energy-sign))<1e-9
        results['like' if sign==1 else 'unlike']=dict(
            turning_distance_numeric=rad,turning_distance_formula=float(reference),
            event_time=float(sol.t_events[0][0]),energy_error=float(np.max(abs(energy-sign))))
    # 临界轨道短时直接积分，检查其在外侧接近而非穿越重根。
    threshold=solve_ivp(particle_ode(4.,-1),(0,2),init,method='DOP853',rtol=1e-12,atol=1e-14,max_step=.002)
    rad=np.linalg.norm(threshold.y[2:4]-threshold.y[:2],axis=0)
    assert rad.min()>.5 and rad[-1]<.51
    K=8.98e9;m=1.97e-11;L=7.21;B=.0241;B1=1.58
    chi=16*K*m/(B*B*L**3)
    x=brentq(lambda x:x*x+x-1-1/x-chi,1,10)
    B0=4*np.sqrt(K*m/L**3)
    nearest=.5*L*(1+np.sqrt(1-(B0/B1)**2))
    save(3,dict(method='全两粒子平面运动方程的独立转折事件积分',orbits=results,
                actual_parameters=dict(chi=float(chi),maximum_distance=float(x*L),
                B0=float(B0),nearest_distance=float(nearest)),
                critical_distance_at_scaled_t2=float(rad[-1])))

def q4():
    G=6.67e-11;MS=1.99e30;RE=1.5e11;RM=5.79e10
    mu=G*MS;a=(RE+RM)/2
    r=RM/RE
    def rhs(t,s):
        return np.r_[s[2:],-s[:2]/np.linalg.norm(s[:2])**3]
    def end(t,s):return s[1]
    end.direction=-1;end.terminal=True
    va_scaled=np.sqrt(2*r/(1+r))
    sol=solve_ivp(rhs,(0,10),[1,0,0,va_scaled],events=end,
                  method='DOP853',rtol=1e-12,atol=1e-14,max_step=.01)
    last=sol.y_events[0][0]
    assert abs(np.linalg.norm(last[:2])-r)<1e-10
    va=np.sqrt(mu/RE)*va_scaled;vp=np.linalg.norm(last[2:])*np.sqrt(mu/RE)
    vE=np.sqrt(mu/RE);vM=np.sqrt(mu/RM)
    infE=vE-va;infM=vp-vM
    dvE=np.sqrt(infE**2+2*G*5.97e24/6.37e6)
    dvM=np.sqrt(infM**2+2*G*3.30e23/2.44e6)
    ratio=np.exp((dvE+dvM)/3000)
    periodhalf=float(sol.t_events[0][0])*np.sqrt(RE**3/mu)
    assert abs(periodhalf-np.pi*np.sqrt(a**3/mu))<.01
    save(4,dict(method='日心二体轨道直接积分至另一端点并匹配两行星近场能量',
                vE=float(vE),vM=float(vM),va=float(va),vp=float(vp),
                v_inf_E=float(infE),v_inf_M=float(infM),delta_v_E=float(dvE),delta_v_M=float(dvM),
                mass_ratio=float(ratio),transfer_days=float(periodhalf/86400),
                exhaust4000_ratio=float(np.exp((dvE+dvM)/4000))))

def q5():
    mu0=4*np.pi*1e-7;A=.1;N=100;I=10;d=.001
    reluctance=(.998/(1800*mu0)+2*d/mu0)/A
    flux=N*I/reluctance;B=flux/A
    # 固定磁通，移动铁块使两铜间隙均增加 y；铁芯实体长度固定。
    def energy(y):
        return (flux/A)**2/(2*1800*mu0)*A*.998+(flux/A)**2/(2*mu0)*A*2*(d+y)
    dy=1e-6;force=(energy(dy)-energy(-dy))/(2*dy)
    assert abs(force-A*B**2/mu0)/force<1e-10
    Aw=np.pi*.002**2;l0=140;lbound=100*(1.4+2*np.pi*.002)
    values=dict(B=float(B),force=float(force),mass_at_g9_8=float(force/9.8),
                wire_area=float(Aw),thin_wire_length=l0,finite_radius_length_lower_bound=float(lbound),
                thin_wire_resistance=float(2e-8*l0/Aw),thin_wire_power=float(100*2e-8*l0/Aw),
                thin_wire_mass=float(8000*Aw*l0),power_lower_bound=float(100*2e-8*lbound/Aw),
                mass_lower_bound=float(8000*Aw*lbound))
    save(5,dict(method='串联磁路与固定磁通场能的双间隙虚位移独立核验',values=values,
                winding_layout_missing_actual_power_not_unique=True))

def q6():
    gamma=1.4;alpha=2.
    def rhs(t,s):return [s[1],alpha*(1+s[0])**(-gamma)-1]
    def peak(t,s):return alpha*(1+s[0])**(-gamma)-1
    peak.direction=-1
    def turn(t,s):return s[1]
    turn.direction=-1;turn.terminal=True
    sol=solve_ivp(rhs,(0,10),[0,0],events=[peak,turn],method='DOP853',
                  rtol=2e-12,atol=1e-14,max_step=.005)
    hpeak,vpeak=sol.y_events[0][0];hmax=sol.y_events[1][0][0]
    e=lambda h:alpha/(gamma-1)*(1-(1+h)**(1-gamma))-h
    positive_root=brentq(e,alpha**(1/gamma)-1,alpha/(gamma-1))
    assert abs(hmax-positive_root)<1e-10
    assert abs(hpeak-(alpha**(1/gamma)-1))<1e-10
    assert abs(vpeak**2-2*e(hpeak))<1e-10
    errors=.5*sol.y[1]**2-np.array([e(h) for h in sol.y[0]])
    assert np.max(abs(errors))<1e-10
    save(6,dict(method='活塞完整二阶动力学方程独立积分，检出合力零与速度零两事件',
                alpha=alpha,h_velocity_max=float(hpeak),h_max=float(hmax),
                v_max_scaled=float(vpeak),energy_error=float(np.max(abs(errors))),
                filling_temperature_ratio=3.5/2.5))

def q7():
    # 闭端Dirichlet，开端Neumann；质量集总离散波动算子，无输入频率答案。
    n=600;L=.05;c=330.;dx=L/n
    diagonal=np.full(n,2.);off=np.full(n-1,-1.);off[-1]=-np.sqrt(2.)
    eigen=eigh_tridiagonal(diagonal,off,select='i',select_range=(0,2))[0]/dx**2
    numeric=c*np.sqrt(eigen)/(2*np.pi)
    exact=np.array([1,3,5])*c/(4*L)
    error=float(np.max(abs(numeric/exact-1)))
    assert error<1e-5
    save(7,dict(method='闭端固定、开端零压力对应离散波动算子的前三个本征值',
                grid_intervals=n,frequencies_numeric=numeric.tolist(),
                frequencies_ideal=exact.tolist(),maximum_relative_error=error,
                ideal_fundamental_not_unique_actual_blowing_sound=True))

def q8():
    checks=[]
    for A,v0 in [(1.,0.),(-1.,0.),(1.,.3),(-1.,.3)]:
        w0=v0/np.sqrt(1-v0*v0);gamma0=1/np.sqrt(1-v0*v0)
        def rhs(t,s):
            v=s[0];return [A*(1-v*v)**1.5,v,np.sqrt(1-v*v)]
        t=np.linspace(0,3,1001)
        sol=solve_ivp(rhs,(0,3),[v0,1,0],t_eval=t,method='DOP853',rtol=1e-12,atol=1e-14,max_step=.01)
        w=w0+A*t
        v=w/np.sqrt(1+w*w)
        x=1+(np.sqrt(1+w*w)-gamma0)/A
        tau=(np.arcsinh(w)-np.arcsinh(w0))/A
        err=float(np.max(abs(sol.y-np.array([v,x,tau]))))
        assert err<1e-10
        p=sol.y[0]/np.sqrt(1-sol.y[0]**2)
        force=np.gradient(p,t)
        assert np.max(abs(force-A))<1e-8
        assert np.all(np.diff(sol.y[2])>0)
        checks.append(dict(A=A,v0=v0,maximum_state_error=err,
                           force_error=float(np.max(abs(force-A)))))
    save(8,dict(method='坐标加速度、速度、固有时的联合数值积分及动量差分',
                branches=checks,initial_velocity_and_time_definition_require_explicit_conditions=True))

def main():
    for fn in (q1,q2,q3,q4,q5,q6,q7,q8):fn()
if __name__=='__main__':main()
