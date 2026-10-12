"""第027套原题预核验。异常条件未确认前，不生成或宣称正式交付。"""
from pathlib import Path
import json, math
from fractions import Fraction as F
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'build'; DEST.mkdir(exist_ok=True)
record={}

# 1. 用实际刚体材料点的位置函数差分，不把几何接触点当作固定材料点。
r=1.; om=.7; beta=.2; theta0=math.pi/4
tt=np.array([math.cos(theta0),math.sin(theta0)])
nn=np.array([-math.sin(theta0),math.cos(theta0)])
s0=r*(2+math.cos(theta0))/math.sin(theta0)
def theta(t): return theta0-om*t-beta*t*t/2
def center(t):
    a=theta(t);return np.array([r*(2*math.cos(a)+1)/math.sin(a),2*r])
def cylinder_point(t):
    a=theta(t)
    angle=2/math.sin(a)+1/math.tan(a)+a-(2/math.sin(theta0)+1/math.tan(theta0)+theta0)
    rot=np.array([[math.cos(angle),-math.sin(angle)],[math.sin(angle),math.cos(angle)]])
    return center(t)+rot@(r*nn)
def rod_point(t):
    a=theta(t);return s0*np.array([math.cos(a),math.sin(a)])
def geometric_point(t):
    a=theta(t);return center(t)+r*np.array([-math.sin(a),math.cos(a)])
def derivs(fun,h=2e-4):
    vel=(fun(-2*h)-8*fun(-h)+8*fun(h)-fun(2*h))/(12*h)
    acc=(-fun(2*h)+16*fun(h)-30*fun(0)+16*fun(-h)-fun(-2*h))/(12*h*h)
    return vel,acc
vc,ac=derivs(center);vb,ab=derivs(cylinder_point);vr,ar=derivs(rod_point);vg,ag=derivs(geometric_point)
expected_c=[r*(4+math.sqrt(2))*om, r*((8+3*math.sqrt(2))*om**2+(4+math.sqrt(2))*beta)]
assert abs(vc[0]-expected_c[0])<1e-8 and abs(ac[0]-expected_c[1])<1e-6
assert np.linalg.norm(vb-vr)<1e-8
abt=np.dot(ab,tt);abn=np.dot(ab,nn)
assert abs(abt+s0*om**2)<1e-6
assert abs(abn+r*((12+8*math.sqrt(2))*om**2+(1+2*math.sqrt(2))*beta))<1e-6
record['01']=dict(status='verified',center_velocity=vc.tolist(),center_acceleration=ac.tolist(),
    cylinder_contact_velocity=vb.tolist(),cylinder_contact_acceleration=[float(abt),float(abn)],
    rod_contact_acceleration=[float(np.dot(ar,tt)),float(np.dot(ar,nn))],
    geometric_contact_velocity=vg.tolist(),note='无滑动使两材料点速度相同，不使法向加速度相同。')

# 2. 直接积分上下两个质点受力，轻杆拉力由杆长约束二阶导数求出。
checks=[]
for mp in [.01,.1,1.,10.]:
    m=1.;l=1.;g=1.;M=m+mp;eps=1e-4
    ex=math.sin(eps);ey=math.cos(eps)
    y0=[mp/M*l*ex,l*ey,-m/M*l*ex,0,0,0]
    def rhs(t,y):
        unit=np.array([y[0]-y[2],y[1]])/l
        rel=np.array([y[3]-y[5],y[4]])
        tension=(np.dot(rel,rel)/l-g*unit[1])/(1/m+unit[0]**2/mp)
        return [y[3],y[4],y[5],-tension*unit[0]/m,-tension*unit[1]/m-g,tension*unit[0]/mp]
    def end(t,y): return y[1]
    end.terminal=True;end.direction=-1
    sol=solve_ivp(rhs,[0,50],y0,events=end,rtol=1e-10,atol=1e-12,max_step=.01,dense_output=True)
    assert len(sol.t_events[0])==1
    states=sol.sol(np.linspace(0,sol.t[-1],501));ns=[];errors=[]
    for y in states.T:
        unit=np.array([y[0]-y[2],y[1]])/l;rel=np.array([y[3]-y[5],y[4]])
        ten=(np.dot(rel,rel)/l-g*unit[1])/(1/m+unit[0]**2/mp)
        normal=mp*g-ten*unit[1];s=unit[1];mu=m/M;D=1-mu*s*s
        # 有限初始扰动的精确能量，sin(theta_i)=cos(eps)。
        analytic=mp*g*(D-2*mu*s*(math.cos(eps)-s))/D**2
        ns.append(normal);errors.append(abs(normal-analytic))
    assert min(ns)>0 and max(errors)<2e-7
    checks.append(dict(mprime_over_m=mp,min_normal_force=min(ns),constraint_ODE_error=max(errors)))
record['02']=dict(status='source_conflict',checks=checks,
    exact='N=mprime*g*(1-mu*(2*sin(theta)-sin(theta)^2))/(1-mu*sin(theta)^2)^2, mu=m/(m+mprime)',
    conclusion='所有mprime>0在倒下过程N>0；没有题目预设的正临界质量和唯一theta0。')

# 3. 使用精确绳长、弹性能和周期积分，比较振幅趋零的行为。
def perimeter(u): return 1+math.sqrt(1+u*u+u)+math.sqrt(1+u*u-u)
def potential(u): return .5*(perimeter(u)-3)**2
periods=[]
for amp in [.2,.1,.05]:
    e=potential(amp)
    period=4/math.sqrt(2)*quad(lambda z:amp/math.sqrt(e-potential(amp*z)),0,1,epsabs=1e-7)[0]
    periods.append(dict(amplitude_over_l=amp,period=period,amplitude_times_period=amp*period))
I=quad(lambda x:1/math.sqrt(1-x**4),0,1)[0]
assert abs(periods[-1]['amplitude_times_period']-16*I/3)<.01
record['03']=dict(status='source_conflict',finite_amplitude_periods=periods,
    small_amplitude_coefficient=16*I/3,
    conclusion='原长3l时预张力为零，势能从u^4开始；小振动线性频率为零，T随振幅倒数发散。垂足平衡还要求锐角和绳张紧。')

# 4. 七节点九支路，精确有理数消元。中心O和左边中点等势。
edges4=[(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(6,1),(6,3),(6,5)]
free4=[0,1,2,3,6];fixed4={4:F(0),5:F(1)};matrix4=[]
for vtx in free4:
    row=[F(0)]*6
    for i,j in edges4:
        if vtx not in [i,j]:continue
        other=j if i==vtx else i;row[free4.index(vtx)]+=1
        if other in free4:row[free4.index(other)]-=1
        else:row[-1]+=fixed4[other]
    matrix4.append(row)
for k in range(5):
    pivot=matrix4[k][k];matrix4[k]=[x/pivot for x in matrix4[k]]
    for i in range(5):
        if i==k:continue
        factor=matrix4[i][k];matrix4[i]=[x-factor*y for x,y in zip(matrix4[i],matrix4[k])]
pot4={**fixed4,**dict(zip(free4,[row[-1] for row in matrix4]))}
current4=sum(pot4[5]-pot4[j if i==5 else i] for i,j in edges4 if 5 in [i,j])
assert 1/current4==F(7,10)
record['04']=dict(status='verified',potentials={str(k):str(v) for k,v in pot4.items()},RAB_over_r=str(1/current4),
    node_order='0左下顶点,1左边中点,2顶部,3右边中点,4右下B,5底边中点A,6中心O')

# 5. 三条严格Snell光线，从同一点入射、无内部反射、经左直角边出射。
S=np.array([1.,1.]);ni=1.5;normal=np.array([-1.,-1.])/math.sqrt(2);tangent=np.array([1.,-1.])/math.sqrt(2)
rays=[]
for x in [.1,.2,.3]:
    H=np.array([x,1-x]);v=H-S;v=v/np.linalg.norm(v)
    st=np.dot(v,tangent)/ni;vi=normal*math.sqrt(1-st*st)+tangent*st
    t=-H[0]/vi[0];Q=H+t*vi
    assert Q[1]>0
    st_out=ni*vi[1];assert abs(st_out)<1
    vo=np.array([-math.sqrt(1-st_out**2),st_out])
    rays.append((Q,vo))
intersections=[]
for i,j in [(0,1),(1,2)]:
    p,v=rays[i];q,w=rays[j]
    u=np.linalg.solve(np.column_stack([v,-w]),q-p)[0]
    intersections.append((p+u*v).tolist())
assert np.linalg.norm(np.array(intersections[0])-intersections[1])>.01
record['05']=dict(status='imaging_assumption_needed',n=ni,ray_start_points=[q.tolist() for q,v in rays],
    ray_directions=[v.tolist() for q,v in rays],backward_intersections=intersections,
    conclusion='不同出射光线不严格共点；斜面一次反射像严格位于正方形对角顶点，距离sqrt(2)*l。折射像清单须声明观察方向和近轴近似。')

# 6. 原件两处数值异常分别核算，不偷换饱和蒸汽压。
temperature=290.15;sig=.0728;rad=2e-6;R=8.31;NA=6.02e23;mol_mass=.018;rho=1000;power=20;eta=5e-4;eta2=.003;aperture=.002
E1=3*sig*.001/rad;volume_rate=power*eta*rad/(3*sig)
v=math.sqrt(3*R*temperature/mol_mass);particles=volume_rate*rho/mol_mass*NA*eta2
steady=6*particles/(aperture*v)
branches=[]
for ps in [1.94,1940.]:
    n0=ps*NA/(R*temperature)
    branches.append(dict(saturation_pressure_Pa=ps,n0=n0,relative_humidity_percent=100*steady/n0))
record['06']=dict(status='constant_and_unit_confirmation_needed',pressure_Pa=101000+2*sig/rad,
    energy_1L_J=E1,volume_per_hour_L=volume_rate*3600*1000,speed_m_s=v,steady_density=steady,
    branches=branches,NIST_Antoine_Pa=10**(5.40221-1838.675/(temperature-31.737))*1e5)

# 7. 动量逐次减半，用总能量差；明确热量份额在地面系且剩余全为动能。
u0=4/3;gam0=math.hypot(1,u0);gam1=math.hypot(1,u0/2);gam2=math.hypot(1,u0/4)
loss1=gam0-gam1;loss2=gam1-gam2;gamt=1+loss1/2
beta1=(u0/2)/gam1;betat=math.sqrt(1-gamt**(-2))
ptarget=math.sqrt(gamt*gamt-1);radiation_p=u0/2-ptarget
assert betat>beta1
assert abs(radiation_p)<=loss1/2
record['07']=dict(status='conditional_model_verified',E1_over_E2=loss1/loss2,
    total_energy_J=89*299792458**2*(gam0-1),runner_beta_after_first=beta1,target_beta_after_first=betat,
    collision_count=1,radiation_momentum_over_mc=radiation_p,
    assumption='热量份额按地面系能量；目标静质量不变且剩余全为动能。可由非各向同性辐射满足动量守恒，不称为普通弹性碰撞。')

# 8. 从真实圆弧/方形线段节点组装有限层网络；不以同一个递推公式自证。
def network(layers):
    nodes={};edges=[]
    def node(x,y):
        key=(round(x,12),round(y,12))
        if key not in nodes:nodes[key]=len(nodes)
        return nodes[key]
    def connect(a,b,res):edges.append((a,b,res))
    for j in range(layers):
        radius=2**(-j/2)
        circle=[node(radius*math.cos(k*math.pi/4),radius*math.sin(k*math.pi/4)) for k in range(8)]
        for k in range(8): connect(circle[k],circle[(k+1)%8],math.pi*radius/4)
        for k in [1,3,5,7]:
            nxt=(k+2)%8;th=k*math.pi/4;ph=nxt*math.pi/4
            mid=node(radius*(math.cos(th)+math.cos(ph))/2,radius*(math.sin(th)+math.sin(ph))/2)
            connect(circle[k],mid,radius/math.sqrt(2));connect(mid,circle[nxt],radius/math.sqrt(2))
    A=node(-1,0);B=node(1,0);free=[i for i in range(len(nodes)) if i not in [A,B]]
    index={i:k for k,i in enumerate(free)};mat=np.zeros((len(free),len(free)));rhs=np.zeros(len(free))
    for i,j,res in edges:
        for a,b in [(i,j),(j,i)]:
            if a not in index:continue
            k=index[a];mat[k,k]+=1/res
            if b in index:mat[k,index[b]]-=1/res
            elif b==A:rhs[k]+=1/res
    vals=np.linalg.solve(mat,rhs);V={A:1.,B:0.,**dict(zip(free,vals))}
    current=sum((V[A]-V[j if i==A else i])/res for i,j,res in edges if A in [i,j])
    return 1/current
a=math.pi/4;z1=a+1/(4/math.pi+math.sqrt(2))
root=brentq(lambda z:z-a-1/(4/math.pi+math.sqrt(2)+math.sqrt(2)/(1+z)),a,z1)
seq=[]
for layers in [1,2,5,10,20]:
    val=network(layers);rec=z1
    for j in range(layers-1):rec=a+1/(4/math.pi+math.sqrt(2)+math.sqrt(2)/(1+rec))
    assert abs(val-rec)<2e-9
    seq.append(dict(layers=layers,network_R_over_r=val,recurrence_R_over_r=rec))
assert abs(seq[-1]['network_R_over_r']-root)<1e-9
record['08']=dict(status='verified',R1_over_r=z1,R2_over_r=root,finite_networks=seq)

(DEST/'preflight-physics.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
for q,item in record.items():print(q,item['status'])
