"""第026套的独立计算核验；不将数值通过等同于PDF验收。"""
from pathlib import Path
import json
import math
import numpy as np
from scipy.integrate import quad, solve_ivp
import preflight_physics as pf

ROOT=Path(__file__).resolve().parents[1]
results={}
for q,fn in enumerate([pf.q1,pf.q2,pf.q3,pf.q4,pf.q5,pf.q6,pf.q7,pf.q8],1):
    results[f"{q:02}"]={"status":"pass","independent_preflight":fn(),
        "scope":"所列模型与计算已核验；题干、图文和PDF分别验收。"}

# 两摩擦系数变式由真实受力矩阵核验，不复用同系数闭式。
cases=[]
for xi,muG,nu in [(.4,0,.7),(.8,.25,.5),(1.2,.3,.4)]:
    co=1/math.sqrt(1+xi*xi);si=xi*co
    for sig in [-1,1]:
        F=.8
        A=np.array([[1,-(si-sig*nu*co),sig*muG],
                    [xi,co+sig*nu*si,0],[0,-(co+sig*nu*si),1]])
        a,N,Q=np.linalg.solve(A,[F,1,1])
        D=1+(1-muG*nu)*xi*xi-sig*muG*xi
        expected=((1+sig*nu*xi)*F+(1-2*muG*nu)*xi-sig*(nu+2*muG))/D
        assert abs(a-expected)<1e-12
        cases.append(dict(xi=xi,ground_mu=muG,contact_mu=nu,sigma=sig,error=abs(a-expected)))
results["01"]["different_friction_matrix"]=cases

# 不等质量双星：真实向量源叠加核验二阶和三阶势。
cases=[]
eta=.2;l=.02
for r in [1.,2.]:
    for psi in [.2,.6,1.1]:
        u=np.array([math.cos(psi),math.sin(psi)])
        pos=np.array([r,0.])
        M1=1+eta;M2=1-eta;a1=(1-eta)*l;a2=(1+eta)*l
        exact=-M1/np.linalg.norm(pos-a1*u)-M2/np.linalg.norm(pos+a2*u)
        c=math.cos(psi)
        phi2=-2/r-l*l*(1-eta*eta)*(3*c*c-1)/r**3
        P3=(5*c**3-3*c)/2
        phi3=phi2+4*eta*(1-eta*eta)*l**3/r**4*P3
        assert abs(phi3-exact)<3e-7
        cases.append(dict(r=r,phase=psi,third_order_error=abs(phi3-exact)))
results["02"]["unequal_mass_exact_potential"]=cases

# 对二维三角域直接作条积分，核对面积、质心和惯量。
area=quad(lambda x:2*(1-x)/math.sqrt(3),.5,1,epsabs=1e-13)[0]
xmoment=quad(lambda x:2*x*(1-x)/math.sqrt(3),.5,1,epsabs=1e-13)[0]
J=quad(lambda x:2*x*x*(1-x)/math.sqrt(3)+2*(1-x)**3/(9*math.sqrt(3)),.5,1,epsabs=1e-13)[0]
assert abs(xmoment/area-2/3)<1e-12 and abs(J/area-17/36)<1e-12
assert 3**(-4)>.01 and 3**(-5)<.01 and 9**(-2)>.01 and 9**(-3)<.01
results["03"]["slice_integrals"]=dict(area=area,centroid_x=xmoment/area,polar_moment_over_mass=J/area,
    minimum_layers_mass_one_percent=5,minimum_layers_inertia_one_percent=3)

info=results["04"]["independent_preflight"]
pv=101e3*info["Va"]
Qab=pv*math.log(512);Qca=-94.5*pv
assert abs(info["work_on"]+Qab+Qca)<1e-20
assert abs(512**(.4)-12.125732532083186)<1e-10
for gamma in [1.2,1.4,5/3]:
    x=512
    W=pv*((x**(gamma-1)-1)/(gamma-1)-math.log(x))
    assert W>0
results["04"]["heat_balance"]=dict(Qab=Qab,Qca=Qca,cycle_residual=info["work_on"]+Qab+Qca)

cases=[]
for phi in [.25,math.pi/6,math.pi/3,math.pi/2]:
    R=1.
    for u,v in [(1.,0.),(0.,1.),(.4,.8)]:
        x=u*math.cos(phi/2)+v*math.sin(phi/2)
        y=-u*math.sin(phi/2)+v*math.cos(phi/2)
        original=x*x+(x*math.cos(phi)-y*math.sin(phi))**2
        principal=(1+math.cos(phi))*u*u+(1-math.cos(phi))*v*v
        assert abs(original-principal)<1e-12
    cases.append(dict(phi=phi,axis_ratio=1/math.tan(phi/2)))
results["05"]["rotated_geometry"]=cases

info=results["06"]["independent_preflight"]
assert abs(info["gap_J"]/1.602176634e-19-2.58254762113293)<1e-12
assert abs(info["wavelength_nm"]*23/25-441.6780609393186)<1e-10
results["06"]["unit_and_filling_checks"]=dict(ground_energy_over_E1=1012,
    pi_electrons=22,occupied_spatial_levels=11,first_empty_level=12,
    corrected_structure_pi_centres=22,chain_carbon_vertices=18,ring_carbon_vertices=12,methyl_carbons=10)

cases=[]
K=1.;a=-.2
for R,b,s in [(1.,1.,1.),(.7,1.,0.),(.4,.6,2.)]:
    bdot=s*a*b/R
    emf=4*math.pi*K*(a*b*b-R*b*bdot)/(b*b+R*R)**1.5
    def flux(dt):
        rt=R+a*dt;bt=b+bdot*dt
        return quad(lambda x:2*math.pi*x*2*K*rt/(x*x+rt*rt)**1.5,0,bt,epsabs=1e-12)[0]
    h=1e-5;fd=-(flux(h)-flux(-h))/(2*h)
    assert abs(emf-fd)<1e-8
    cases.append(dict(R=R,b=b,scaling_exponent=s,emf=emf,finite_difference_emf=fd,error=abs(emf-fd)))
results["07"]["moving_boundary_numerical_integral"]=cases

# 重根以真实ODE积分验证；初始电荷回到未求导KVL核验。
L=2.;C=.25;R=.8;alpha=.3;omega0=1/math.sqrt(L*C)
r=R+2*math.sqrt(L/C)
def rhs(t,y):return [y[1],(r-R)/L*y[1]-y[0]/(L*C)]
t=np.linspace(0,2,201)
sol=solve_ivp(rhs,[0,2],[0,alpha],t_eval=t,rtol=1e-12,atol=1e-14)
expected=alpha*t*np.exp(omega0*t)
assert max(abs(sol.y[0]-expected))<1e-9
q0=-L*C*alpha
assert abs(L*alpha+q0/C)<1e-14
R=20.;r=R;V=3.;Vb=7.;I=(Vb-V)/R;ihat=.01
pd=quad(lambda t:(V-r*ihat*math.sin(t))*(I+ihat*math.sin(t)),0,2*math.pi)[0]/(2*math.pi)
pr=quad(lambda t:R*(I+ihat*math.sin(t))**2,0,2*math.pi)[0]/(2*math.pi)
assert abs(pd-.599)<1e-12 and abs(pr-.801)<1e-12 and abs(pd+pr-Vb*I)<1e-12
results["08"]["critical_and_power_checks"]=dict(critical_root_ODE_error=float(max(abs(sol.y[0]-expected))),
    initial_charge=q0,diode_mean_power=pd,resistor_mean_power=pr,source_power=Vb*I)

(ROOT/"build").mkdir(exist_ok=True)
for q,item in results.items():
    (ROOT/"build"/f"question{q}-verification.json").write_text(json.dumps(item,ensure_ascii=False,indent=2)+"\n")
    print(q,item["status"],flush=True)
