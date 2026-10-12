"""第027套独立物理核验；通过仅表示所列数学与物理检查，不代表文档已完成。"""
from pathlib import Path
import json, math
import numpy as np
from scipy.integrate import solve_ivp, quad
import preflight_physics as pf

ROOT=Path(__file__).resolve().parents[1]
results={}
for q,item in pf.record.items():
    results[q]={"status":"pass","preflight":item,
                "scope":"原题模型及异常结论已计算核验；正式稿和PDF另行验收。"}

magnetic=[]
for mp,k in [(0.1,.02),(1.,.2),(10.,.3)]:
    m=l=g=1.;M=m+mp;theta_i=math.pi/2-.01;si=math.sin(theta_i)
    initial=[l*math.cos(theta_i),l*si,0.,0.,0.,0.]
    def rhs(t,y):
        e=np.array([y[0]-y[2],y[1]])/l
        rel=np.array([y[3]-y[5],y[4]])
        thdot=(e[0]*rel[1]-e[1]*rel[0])/l
        T=(np.dot(rel,rel)/l-g*e[1]+k/m*(l*thdot-e[1]*y[5]))/(1/m+e[0]**2/mp)
        return [y[3],y[4],y[5],(k*y[4]-T*e[0])/m,
                -k*y[3]/m-T*e[1]/m-g,T*e[0]/mp]
    def end(t,y):return y[1]
    end.terminal=True;end.direction=-1
    sol=solve_ivp(rhs,[0,50],initial,events=end,rtol=2e-11,atol=2e-13,max_step=.006,dense_output=True)
    assert len(sol.t_events[0])==1
    err_v=[];err_p=[];err_E=[];err_l=[];normal=[]
    for y in sol.sol(np.linspace(0,sol.t[-1],501)).T:
        e=np.array([y[0]-y[2],y[1]])/l
        rel=np.array([y[3]-y[5],y[4]])
        s=e[1];D=1-m/M*s*s
        expected=(2*g*l*(si-s)-k*k*l*l/(m*M)*(si-s)**2)/D
        Px=m*y[3]+mp*y[5]
        E=.5*m*(y[3]**2+y[4]**2)+.5*mp*y[5]**2+m*g*y[1]
        thdot=(e[0]*rel[1]-e[1]*rel[0])/l
        T=(np.dot(rel,rel)/l-g*s+k/m*(l*thdot-s*y[5]))/(1/m+e[0]**2/mp)
        N=mp*g+k*y[5]-T*s
        err_v.append(abs(np.dot(rel,rel)-expected))
        err_p.append(abs(Px-k*l*s+k*l*si))
        err_E.append(abs(E-m*g*l*si))
        err_l.append(abs(np.dot(e,e)-1));normal.append(N)
    assert max(err_v)<2e-7 and max(err_p)<2e-8 and max(err_E)<2e-8 and max(err_l)<2e-8
    assert min(normal)>0
    magnetic.append(dict(mprime=mp,qB=k,speed_squared_error=max(err_v),
                         conserved_momentum_error=max(err_p),energy_error=max(err_E),
                         rod_length_error=max(err_l),minimum_support=min(normal)))
results["02"]["magnetic_real_force_ODE"]=magnetic

# 垂足反射展开的点序与下界：三个非等边锐角三角形。
geometries=[]
for d,p,h in [(4,1.5,2.5),(3,1.1,1.7),(5,2.8,3.6)]:
    a=d-p;LF=p*p+h*h;LD=a*a+h*h
    A=np.array([d*p*p/LF,d*p*h/LF]);C=np.array([d*h*h/LD,d*a*h/LD])
    B=np.array([p,0.]);B1=np.array([p*(p*p-h*h)/LF,2*p*p*h/LF])
    B2=np.array([d+a*(h*h-a*a)/LD,2*a*a*h/LD])
    W=np.array([p*a+h*h,h*(a-p)])
    errors=[np.linalg.norm(A-B1-p/LF*W),
            np.linalg.norm(B2-C-a/LD*W),
            np.linalg.norm(C-A-d*(h*h-p*a)/(LF*LD)*W)]
    assert h*h>p*a and max(errors)<1e-12
    P=np.linalg.norm(A-B)+np.linalg.norm(B-C)+np.linalg.norm(C-A)
    sine_E=d*h/math.sqrt(LF*LD)
    assert abs(P-2*h*sine_E)<1e-12
    geometries.append(dict(vertices=[d,p,h],max_point_order_error=max(errors),perimeter=P))
results["03"]["orthic_reflection_checks"]=geometries
I2=quad(lambda psi:1/math.sqrt(1+math.sin(psi)**2),0,math.pi/2,
        epsabs=1e-12,epsrel=1e-12)[0]
assert abs(I2*16/3-pf.record["03"]["small_amplitude_coefficient"])<1e-9
results["03"]["regularized_period_integral"]=I2

# 光线微束逐线追迹，独立核验局部像公式的极限；不将三维严格点像强加给折射族。
def exiting_line(a,n):
    source=np.array([1.,1.]);H=np.array([a,1-a]);d=(H-source)/np.linalg.norm(H-source)
    normal=np.array([-1.,-1.])/math.sqrt(2);tangent=np.array([1.,-1.])/math.sqrt(2)
    st=np.dot(d,tangent)/n;inside=normal*math.sqrt(1-st*st)+tangent*st
    Q=H-H[0]/inside[0]*inside
    assert Q[1]>0 and abs(n*inside[1])<1
    out=np.array([-math.sqrt(1-n*n*inside[1]**2),n*inside[1]])
    return Q,out
local_checks=[]
for eps in [.01,.005,.001]:
    Qm,dm=exiting_line(.2-eps,1.5);Qp,dp=exiting_line(.2+eps,1.5)
    k=np.linalg.solve(np.column_stack([dm,-dp]),Qp-Qm)[0]
    image=Qm+k*dm
    error=np.linalg.norm(image-np.array([.6423618607125966,1.231557682006689]))
    local_checks.append(dict(half_parameter_width=eps,intersection=image.tolist(),error=error))
assert local_checks[-1]['error']<2e-5
assert all(local_checks[i]['error']>local_checks[i+1]['error'] for i in range(2))
results['05']['local_image_by_neighbor_ray_intersections']=local_checks

# 首次事件由双向正能量光子构成辐射，并核验变式的允许散热比例。
e=pf.loss1;d=2/3;h=.5;gamma_target=1+(1-h)*e
target_p=math.sqrt(gamma_target**2-1);pr=d-target_p
forward=(h*e+pr)/2;backward=(h*e-pr)/2
assert forward>=0 and backward>=0
assert abs(pf.gam0+1-pf.gam1-gamma_target-forward-backward)<1e-14
assert abs(pf.u0-pf.u0/2-target_p-forward+backward)<1e-14
num=2*e+e*e-d*d
hlo=num/(2*e*(1+e+d));hhi=num/(2*e*(1+e-d))
for hv in np.linspace(0,1,1001):
    pc=math.sqrt((1+(1-hv)*e)**2-1)
    permitted=abs(d-pc)<=hv*e+1e-12
    assert permitted==(hlo-1e-12<=hv<=hhi+1e-12)
results['07']['first_event_four_momentum']=dict(forward_photon_energy_over_mc2=forward,
    backward_photon_energy_over_mc2=backward,allowed_heat_fraction=[hlo,hhi])

for q,item in results.items():
    (ROOT/"build"/f"question{q}-verification.json").write_text(
        json.dumps(item,ensure_ascii=False,indent=2)+"\n")
    print(q,item["status"],flush=True)
