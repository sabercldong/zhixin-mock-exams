"""八题正式独立核验。数值路线回到原方程/界面，不仅回代最后公式。"""
from pathlib import Path
import contextlib,io,json,math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.special import ellipk
import preflight_physics
ROOT=Path(__file__).resolve().parents[1]
def main():
    with contextlib.redirect_stdout(io.StringIO()):
        preflight_physics.main()
    report=json.loads((ROOT/'build/preflight-physics.json').read_text())
    # 01: 对电流和速度的一阶耦合方程直接积分。
    G,m,L,w,U=2.,3.,.04,1.7,.8
    A=G*U/(w*(G*G-m*L*w*w))
    def motor(t,y):
        x,v,I=y
        return [v,G*I/m,(U*math.cos(w*t)-G*v)/L]
    sol=solve_ivp(motor,(0,10),[0,A*w,0],rtol=1e-11,atol=1e-12,max_step=.01)
    err=max(abs(sol.y[0]-A*np.sin(w*sol.t)))
    assert err<1e-9
    report['01']['independent_ODE_position_error']=float(err)
    # 02: 直接boost光子四矢量，反冲系统mass-shell独立构造。
    M,M0,beta=1.05,1.,.3
    results=[]
    for MC in np.linspace(M0,M,21):
        k=(M*M-MC*MC)/(2*M)
        EC=math.sqrt(MC*MC+k*k)
        assert abs(k+EC-M)<1e-12
        for angle in np.linspace(0,math.pi,13):
            # c=1, boost沿x；光子(p_x,p_y,E)
            px,py=k*math.cos(angle),k*math.sin(angle)
            gam=1/math.sqrt(1-beta*beta)
            E=gam*(k+beta*px);xp=gam*(px+beta*k)
            assert abs(E*E-xp*xp-py*py)<1e-12
            results.append(E)
    endpoint=(M*M-M0*M0)/(2*M)
    assert abs(max(results)-endpoint*math.sqrt((1+beta)/(1-beta)))<1e-12
    report['02']['boost_mass_shell_cases']=len(results)
    # 03: 四条真实坐标轨迹反向投影，并用二阶导数核对SHO。
    t=np.linspace(0,2*math.pi,1001)
    cases=[(np.cos(t),np.sin(t),np.cos(t),np.cos(t-math.pi/4)),
           (np.cos(t),.7*np.sin(t),np.cos(t),(np.cos(t)+.7*np.sin(t))/math.sqrt(2)),
           (np.cos(t),math.sqrt(2)*np.cos(2*t)-np.cos(t),np.cos(t),np.cos(2*t)),
           (np.sin(t),math.sqrt(2)*np.sin(2*t)-np.sin(t),np.sin(t),np.sin(2*t))]
    errors=[]
    for x,y,expected_x,expected_u in cases:
        errors.append(float(max(abs((x+y)/math.sqrt(2)-expected_u))))
        assert max(abs(x-expected_x))<1e-12
    assert max(errors)<1e-12
    report['03']['independent_reverse_projection_residuals']=errors
    # 04: 用原收支函数求根；检验稳定、变式和温标。
    TH,k,P=313.15,173.,130.5550897199396
    fun=lambda T:k*(TH-T)-P*T/(TH-T)
    root=brentq(fun,1e-6,TH-1e-6)
    assert abs(root-298.15)<1e-8
    assert fun(root-1)>0 and fun(root+1)<0
    COP=root/(TH-root)
    assert abs(P*COP+P-P*TH/(TH-root))<1e-9
    report['04']['independent_root_K']=root
    report['04']['variant_eta04_power_W']=P/.4
    report['04']['variant_max_difference_K']=math.sqrt(500*298.15/173)
    # 05: 球面交点和向量反射；收敛到薄面近轴系数。
    def reflect(P,V,C):
        D=P-C
        aa=V@V;bb=2*(D@V);cc=D@D-1
        roots=np.roots([aa,bb,cc])
        dist=min(float(r.real) for r in roots if abs(r.imag)<1e-8 and r.real>1e-9)
        Q=P+dist*V;normal=Q-C
        normal/=np.linalg.norm(normal)
        return Q,V-2*(V@normal)*normal
    def ghost(p,alpha):
        h=p+2*alpha
        P=np.array([0.,h]);V=np.array([1.,alpha-h])
        P,V=reflect(P,V,np.array([4.,0.]))
        P,V=reflect(P,V,np.array([-1.,0.]))
        y4=P[1]+(3-P[0])*V[1]/V[0]
        out=V[1]/V[0]-y4
        return y4+2*out
    coefficients=[]
    for eps in [1e-5,2e-6,4e-7]:
        cp=(ghost(eps,0)-ghost(-eps,0))/(2*eps)
        ca=(ghost(0,eps)-ghost(0,-eps))/(2*eps)
        coefficients.append(dict(epsilon=eps,height_coefficient=cp,angle_coefficient=ca))
    assert abs(coefficients[-1]['height_coefficient']-56)<1e-7
    assert abs(coefficients[-1]['angle_coefficient']-33)<1e-7
    report['05']['exact_sphere_reflection_paraxial_convergence']=coefficients
    # 06: 在矢量空间直接差分张力矢量，核对摩擦圆盘。
    theta0=2*math.pi/3
    angle=np.linspace(0,theta0,40001)
    tangent=np.stack((-np.sin(angle),np.cos(angle)),axis=1)
    Ta=np.sin(np.minimum(angle,math.pi/2))
    Tb=np.sin(np.maximum(angle-math.pi/6,0))
    force_norms=[]
    for T in [Ta,Tb]:
        derivative=np.gradient(T[:,None]*tangent,angle,axis=0)
        norms=np.linalg.norm(derivative,axis=1)
        assert max(norms)<1+1e-6 and abs(T[-1]-1)<1e-12
        force_norms.append(float(max(norms)))
    assert max(abs(Ta-Tb))>.4
    report['06']['vector_friction_maxima']=force_norms
    report['06']['qualification']='最大静力载荷，不声称加载历程唯一；30°仅指定分布的平台角。'
    # 07: 面积律给E(t)，对椭圆Cartesian坐标求加速度。
    a,e,mu=2.,.6,1.
    b=a*math.sqrt(1-e*e);n=math.sqrt(mu/a**3)
    errors=[]
    for E in np.linspace(0,2*math.pi,101):
        pos=np.array([a*math.cos(E)-a*e,b*math.sin(E)])
        Ep=n/(1-e*math.cos(E))
        Epp=-e*math.sin(E)*Ep*Ep/(1-e*math.cos(E))
        acc=np.array([-a*math.cos(E),-b*math.sin(E)])*Ep**2+np.array([-a*math.sin(E),b*math.cos(E)])*Epp
        expected=-mu*pos/np.linalg.norm(pos)**3
        errors.append(float(np.linalg.norm(acc-expected)))
    assert max(errors)<1e-12
    report['07']['Cartesian_area_law_acceleration_error']=max(errors)
    # 08: 直接二阶ODE返回与临界显式解、带漂移例子。
    def cylinder(wc,wz,end):
        def ode(t,Y):
            phi,rate,z,vz=Y
            return [rate,wc*vz*math.cos(phi),vz,-wc*rate*math.cos(phi)]
        return solve_ivp(ode,(0,end),[0,1,0,wz],rtol=2e-12,atol=2e-13,max_step=.01)
    periods=[4*ellipk(.25),4/1.5*ellipk(4/9)]
    returns=[]
    for wc,T,expected_phi in zip([.5,1.5],periods,[2*math.pi,0]):
        Y=cylinder(wc,0,T).y[:,-1]
        err=max(abs(Y-np.array([expected_phi,1,0,0])))
        assert err<1e-8
        returns.append(dict(wc=wc,period_s=float(T),return_error=float(err)))
    sol=cylinder(1,0,5);phi,rate,z,vz=sol.y
    assert max(abs(np.sin(phi)-np.tanh(sol.t)))<1e-9
    assert max(abs(z+np.log(np.cosh(sol.t))))<1e-9
    drift=cylinder(.5,.2,20)
    assert min(drift.y[1])>0 and min(drift.y[3])<0
    report['08']['independent_closed_returns']=returns
    report['08']['critical_explicit_z_error']=float(max(abs(z+np.log(np.cosh(sol.t)))))
    report['08']['drift_example_has_axial_reversal']=True
    for q,data in report.items():
        data['status']='passed'
        data['method_note']='数值/几何核验和解析适用条件同时成立；不宣称检验覆盖所有可能模型。'
        (ROOT/'build'/f'question{q}-verification.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print('8题原方程、反向投影、向量静力及独立光路核验均通过。')
if __name__=='__main__':main()
