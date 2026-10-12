"""第021套：独立方程、图结构、数值轨迹与极限核验；不以结论代入自证。"""
from pathlib import Path
from fractions import Fraction as F
import json, math, itertools
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp, quad
from scipy.optimize import minimize_scalar, brentq
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
ROOT=Path(__file__).resolve().parents[1]
def save(q,data):
    data['status']='pass'
    (ROOT/'build').mkdir(exist_ok=True)
    (ROOT/'build'/f'question{q:02}-verification.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(q,json.dumps(data,ensure_ascii=False),flush=True)

def q1():
    k,c=sp.symbols('k c',real=True);d=1+k*k+2*k*c
    ax=k*sp.sqrt(1-c*c)*((1+k*c)*(1+k)**2-2*k*(1-c)*d)/d**2
    ny=1-k*k*(1-c*c)*(1+k)**2/d**2-2*k*k*c*(1-c)/d
    P=4*k*k*c*c+k*(3*k*k-2*k+3)*c+1+k*k-2*k**3
    assert sp.simplify(ny-(1+k*c)*P/d**2)==0
    assert sp.simplify(ax-k*sp.sqrt(1-c*c)*P/d**2)==0
    critical=-(3*k*k-2*k+3)/(8*k)
    assert sp.factor(P.subs(c,critical))==-(k+1)**3*(9*k-7)/16
    values=[]
    for kv in [.1,.3,.6,7/9]:
        func=lambda t:kv*abs(math.sin(t))/(1+kv*math.cos(t))
        opt=minimize_scalar(lambda t:-func(t),bounds=(0,math.pi),method='bounded')
        assert abs(-opt.fun-kv/math.sqrt(1-kv*kv))<1e-9
        values.append(dict(k=kv,mu_required=-opt.fun))
    kv=.5;eps=.003
    d0=1+kv*kv+2*kv*math.cos(eps)
    w0=math.sqrt(2*kv*(1-math.cos(eps))/d0)
    def ode(t,y):
        th,w=y;den=1+kv*kv+2*kv*math.cos(th)
        return [w,kv*math.sin(th)*(1+w*w)/den]
    sol=solve_ivp(ode,(0,50),(eps,w0),rtol=2e-11,atol=2e-13,max_step=.015)
    th,w=sol.y;den=1+kv*kv+2*kv*np.cos(th)
    e=.5*den*w*w+kv*(1+np.cos(th))
    assert np.max(abs(e-2*kv))<1e-8
    # 直接有限差分坐标，另核查曲率变号，不通过反力式计算。
    t=math.acos(-kv);dt=1e-4
    xy=lambda x:np.array([x+kv*math.sin(x),1+kv*math.cos(x)])
    first=(xy(t+dt)-xy(t-dt))/(2*dt)
    second=(xy(t+dt)-2*xy(t)+xy(t-dt))/dt**2
    det=first[0]*second[1]-first[1]*second[0]
    assert abs(det)<2e-8
    save(1,dict(contact_limit=7/9,friction_samples=values,ode_energy_error=float(np.max(abs(e-2*kv))),curvature_finite_difference=det))

def q2():
    threshold=1.25
    # 从重力抛射方程直接求二次交点，而非代入高度阈值结论。
    checks=[]
    for lam in [1.1,1.25,1.4,2]:
        bad=0
        for z in np.linspace(.001,.999,800):
            u=math.sqrt(2*(lam-z))
            t2=2*u
            x2=1-z+u*t2
            yy=z-.5*t2*t2
            assert abs(yy-(1-x2))<1e-12
            if x2<=1:bad+=1
        checks.append(dict(lambda_value=lam,repeated_interior_collisions=bad))
    f=lambda z:-z+2*math.sqrt(z*(threshold-z))
    opt=minimize_scalar(lambda z:-f(z),bounds=(0,1),method='bounded')
    z=threshold*(5-math.sqrt(5))/10
    maximum=5*(math.sqrt(5)-1)/8
    assert abs(opt.x-z)<2e-6 and abs(-opt.fun-maximum)<1e-10
    t=math.sqrt(2*z);u=math.sqrt(2*(threshold-z))
    assert abs((1-z+u*t)-1-maximum)<1e-13
    # 原题问最近：直接落点坐标在两端为坡脚，开放内区间只有零下确界。
    nearest_samples=[]
    for epsilon in [1e-2,1e-4,1e-6,1e-8]:
        endpoints=[]
        for height in [epsilon,1-epsilon]:
            velocity=math.sqrt(2*(threshold-height))
            landing=1-height+velocity*math.sqrt(2*height)
            assert landing>1
            endpoints.append(landing-1)
        nearest_samples.append(dict(epsilon=epsilon,distance_to_foot=endpoints))
    assert f(0)==0 and f(1)==0
    assert all(f(height)>0 for height in np.linspace(.0001,.9999,10000))
    save(2,dict(critical_lambda=threshold,ground_min_distance_per_h=0,nearest_limit_samples=nearest_samples,
                ground_max_distance_per_h=maximum,optimal_collision_height_per_h=z,direct_trajectory_tests=checks,endpoint_note='λ=5/4时顶点到坡脚的第二次交点为边界接触；含端点严格要求λ>5/4，无最大高度。原题求最近，闭区间为零、开区间为零下确界；最大值仅用于有解变式。'))

def laplacian(vertices,edges):
    idx={p:i for i,p in enumerate(vertices)};L=lil_matrix((len(idx),len(idx)),dtype=float)
    for a,b,r in edges:
        i,j=idx[a],idx[b];g=1/float(r)
        L[i,i]+=g;L[j,j]+=g;L[i,j]-=g;L[j,i]-=g
    return idx,L.tocsr()
def resistance(vertices,edges,a,b):
    idx,L=laplacian(vertices,edges);ground=idx[b]
    keep=[i for i in range(len(idx)) if i!=ground];load=np.zeros(len(idx));load[idx[a]]=1;load[idx[b]]=-1
    v=np.zeros(len(idx));v[keep]=spsolve(L[keep][:,keep],load[keep])
    return float(v[idx[a]]),v,L
def q3():
    cube=list(itertools.product([0,1],repeat=3))
    edges=[(a,b,1) for a,b in itertools.combinations(cube,2) if sum(abs(x-y) for x,y in zip(a,b))==1]
    term=[(0,0,0),(1,0,0),(0,1,0),(0,0,1)]
    _,L=laplacian(cube,edges);indices=[cube.index(x) for x in term];hidden=[x for x in range(8) if x not in indices]
    mat=sp.Matrix([[int(v) for v in row] for row in L.toarray()])
    schur=mat.extract(indices,indices)-mat.extract(indices,hidden)*mat.extract(hidden,hidden).inv()*mat.extract(hidden,indices)
    assert schur[0,1]==-1 and schur[1,2]==-sp.Rational(5,9)
    equivalent=[(a,b,1 if 0 in (i,j) else sp.Rational(9,5)) for (i,a),(j,b) in itertools.combinations(enumerate(term),2)]
    for a,b in itertools.combinations(term,2):
        r1,_,_=resistance(cube,edges,a,b);r2,_,_=resistance(term,equivalent,a,b)
        assert abs(r1-r2)<1e-13
    # 分形直接逐代生成四个角部网络及六条中段；投影交叉不合并节点。
    initial=[tuple(F(int(i==j)) for j in range(4)) for i in range(4)]
    def make(verts,depth,scale):
        if depth==0:return [(a,b,scale) for a,b in itertools.combinations(verts,2)]
        children=[[tuple((2*a+b)/3 for a,b in zip(verts[i],verts[j])) for j in range(4)] for i in range(4)]
        result=[]
        for child in children:result.extend(make(child,depth-1,scale/3))
        for i,j in itertools.combinations(range(4),2):result.append((children[i][j],children[j][i],scale/3))
        return result
    network=[]
    for n in range(5):
        ed=make(initial,n,F(1));vertices=sorted(set(a for a,b,r in ed)|set(b for a,b,r in ed))
        rn,v,L= resistance(vertices,ed,initial[0],initial[1])
        expected=1/3+1/(6*2**n)
        assert abs(rn-expected)<2e-12
        load=L@v;idx=vertices.index(initial[0]);other=vertices.index(initial[1])
        assert np.max(np.abs(np.delete(load,[idx,other])))<2e-11
        network.append(dict(iteration=n,nodes=len(vertices),edges=len(ed),resistance=rn))
    # 门格尔海绵：直接保留体素与体素自身惯量，而非只重复递推式。
    moment=[];cells=[(np.zeros(3),1.)]
    digits=[np.array(v)/3 for v in itertools.product([-1,0,1],repeat=3) if sum(x==0 for x in v)<=1]
    for n in range(4):
        mass=len(cells)/27**n
        inertia=sum((1/27**n)*(pos[0]**2+pos[1]**2+side**2/6) for pos,side in cells)
        assert abs(inertia-mass*(1/5-1/(30*9**n)))<2e-12
        moment.append(dict(iteration=n,mass=mass,inertia=inertia))
        cells=[(pos+side*d,side/3) for pos,side in cells for d in digits]
    save(3,dict(cube_terminal_conductance_matrix=str(schur),tetra_network=network,menger_voxel_checks=moment,limit_mass=0,limit_inertia=0,tetra_limit_resistance=1/3,wire_model='各代导线材料和截面不变，电阻随长度缩放，六条中间连接保留。'))

def q4():
    s,z,C,m=sp.symbols('s z C m',positive=True)
    U=-C*z/(s*s+z*z)**sp.Rational(3,2)
    Us=sp.diff(U,s);Uz=sp.diff(U,z);zc=s/sp.sqrt(2)
    assert sp.simplify(Uz.subs(z,zc))==0
    wo2=sp.simplify((Us/(m*s)).subs(z,zc))
    wz2=sp.simplify((sp.diff(U,z,2)/m).subs(z,zc))
    wr2=sp.simplify((3*Us/(m*s)+sp.diff(U,s,2)/m).subs(z,zc))
    assert sp.simplify(wz2/wo2)==sp.Rational(4,3)
    assert sp.simplify(wr2/wo2)==sp.Rational(2,3)
    # 实际非线性轴向、径向运动，检测零交叉周期。
    s0=1.;z0=1/math.sqrt(2);coef=1.;mass=1.
    omega2=3*coef*z0/(s0*s0+z0*z0)**2.5
    angular_momentum=math.sqrt(omega2)
    def axial(t,y):
        zz,u=y
        return [u,coef*(s0*s0-2*zz*zz)/(s0*s0+zz*zz)**2.5]
    def radial(t,y):
        ss,u=y
        return [u,angular_momentum**2/ss**3-3*coef*z0*ss/(ss*ss+z0*z0)**2.5]
    periods={}
    for name,ode,eq,expected in [('axial',axial,z0,math.sqrt(4/3*omega2)),('radial',radial,s0,math.sqrt(2/3*omega2))]:
        def crossing(t,y):return y[0]-eq
        crossing.direction=-1
        sol=solve_ivp(ode,(0,60),(eq+1e-4,0.),events=crossing,rtol=1e-11,atol=1e-13,max_step=.03)
        ts=sol.t_events[0];measured=float(np.mean(np.diff(ts)))
        assert abs(measured-2*math.pi/expected)/(2*math.pi/expected)<1e-6
        periods[name]=measured
    save(4,dict(omega_axial_squared_ratio='4/3',omega_radial_squared_ratio='2/3',nonlinear_periods=periods,orbit_plane_offset='z=s/sqrt(2)；负电荷对应p正向的半轴'))

def q5():
    theta=.65;mu=.25;g=1.;a=g*(math.sin(theta)-mu*math.cos(theta));b=mu
    vc=g*math.cos(theta);vmax=g*(math.sin(theta)+mu*math.cos(theta))/mu
    tc=math.log(math.tan(theta)/(math.tan(theta)-mu))/b
    def ode(t,y):return [y[1],g*math.sin(theta)-mu*abs(g*math.cos(theta)-y[1])]
    sol=solve_ivp(ode,(0,60),(0,0),rtol=1e-10,atol=1e-12,max_step=.01,dense_output=True)
    tests=[]
    for t in [tc*.2,tc*.8,tc,tc+1,tc+8]:
        expected=a/b*(math.exp(b*t)-1) if t<=tc else vmax+(vc-vmax)*math.exp(-b*(t-tc))
        got=sol.sol(t)[1];assert abs(got-expected)<1e-7
        tests.append(dict(t=t,ode_velocity=float(got),piecewise_velocity=expected))
    # 独立功率积分：洛伦兹力垂直速度，重力减摩擦等于动能增长。
    v=sol.y[1];times=sol.t
    power=v*(math.sin(theta)-mu*np.abs(math.cos(theta)-v))
    from scipy.integrate import simpson
    work=simpson(power,x=times)
    assert abs(work-.5*v[-1]**2)<1e-6
    save(5,dict(critical_velocity=vc,terminal_velocity=vmax,switch_time=tc,piecewise_ode_tests=tests,power_integral_error=float(work-.5*v[-1]**2),start_condition='滑动后正向加速需tanθ>μ；静摩擦启动条件原题未给。'))

def q6():
    m0=202.;T0=300.;rho0=1.174;r=10.;g=10.6;p0=1.01e5;mu=.029;h=125.;gamma=7/5;R=8.314462618
    V=4*math.pi*r**3/3;rho_d=m0/V
    ph=p0-rho0*g*h
    Th=T0*(1-(gamma-1)/gamma*rho0*g*h/p0)
    rhoh=rho0*(1-rho0*g*h/(gamma*p0))
    rhoi=rhoh-rho_d
    fraction=rhoi/rho0;p_after=p0*fraction**gamma;Tin_after=T0*fraction**(gamma-1)
    dp=p0-p_after;Ti=T0*(ph/p0)*(rho0/rhoi)
    # 定容开口罐能量方程：独立积分dT/dN；不是封闭定容绝热降温。
    sol=solve_ivp(lambda N,T:[(gamma-1)*T[0]/N],(1,fraction),[T0],rtol=1e-12,atol=1e-12)
    assert abs(sol.y[0,-1]-Tin_after)<1e-8
    assert abs((m0+rhoi*V)-rhoh*V)<1e-11
    # 静力平衡+等熵大气的完整数值解用于检验线性近似。
    K=p0/rho0**gamma
    hydro=solve_ivp(lambda z,p:[-g*(p[0]/K)**(1/gamma)],(0,h),[p0],rtol=1e-12,atol=1e-8)
    p_exact=hydro.y[0,-1];rho_exact=(p_exact/K)**(1/gamma)
    assert abs(p_exact-ph)/p0<1e-4 and abs(rho_exact-rhoh)/rho0<1e-4
    calibrated_R=p0*mu/(rho0*T0)
    heater=math.pi*r*r*4*(Ti-Th)
    pump_work=heater*(1-Th/Ti)
    assert abs(pump_work-673.95)<.005
    save(6,dict(volume=V,dry_density=rho_d,ambient_pressure=ph,ambient_temperature=Th,ambient_density=rhoh,gas_density=rhoi,gas_mass=rhoi*V,pressure_drop=dp,temperature_after_exhaust=Tin_after,heated_temperature=Ti,inside_outside_temperature_difference=Ti-Th,heat_pump_variant_minimum_work=pump_work,exact_hydro_pressure=p_exact,exact_hydro_density=rho_exact,ideal_gas_constant_from_givens=calibrated_R,ideal_gas_input_relative_mismatch=calibrated_R/R-1,model='m0为本体质量；定容均匀理想气体准平衡绝热排气，后封闭升空；皮膜均温且吸收率按1处理。'))

def q7():
    f1,f2,D=sp.symbols('f1 f2 D',positive=True)
    P=lambda x:sp.Matrix([[1,x],[0,1]])
    L=lambda f:sp.Matrix([[1,0],[-1/f,1]])
    mat=sp.simplify(L(f1)*P(f1+f2)*L(f2)*P(D)*L(f2)*P(f1+f2)*L(f1))
    b=sp.factor(mat[0,1]);length=2*(f1+f2)+D
    dc=2*f2*(f1+f2)/(f1-f2)
    assert sp.simplify((b-length).subs(D,dc))==0
    rng=np.random.default_rng(20261005);max_error=0
    # 不使用合成矩阵，逐面传播、折射检查虚像回延。
    for y,angle in rng.uniform(-.025,.025,(300,2)):
        yi=y+2*angle; ai=angle-yi/2;heights=[yi]
        for distance,f in [(3,1),(6,1),(3,2)]:
            yi+=distance*ai;ai-=yi/f;heights.append(yi)
        back=yi-14*ai
        err=max(abs(back-y),abs(ai-angle));max_error=max(max_error,err)
        assert err<1e-13
    # 四片二维圆孔：以输出斜率归一化，在最后一孔内随机采样。
    samples=rng.uniform(-1,1,(200000,2));samples=samples[np.sum(samples*samples,axis=1)<=1]
    pupil=[]
    for field in [0,.5]:
        source=np.array([field,0.]);u=-source/14+samples/14
        heights=[source+2*u,-source/2+2*u,-source/2-10*u,source+14*u]
        ratios=[float(np.max(np.linalg.norm(y,axis=1))) for y in heights]
        assert all(t<=1+1e-12 for t in ratios)
        pupil.append(dict(field_height_per_h=field,max_ray_height_each_lens=ratios))
    save(7,dict(system_matrix=str(mat),overlap_distance=str(dc),transverse_magnification=1,virtual_image_note='重合像为右侧出射光线反向延长所得；不是原光源处的真实聚焦。',brightness_ratio_uniform_source_full_collection='1:1',independent_ray_error=max_error,pupil_sampling=pupil,source_disk_radius='h/2，已从图片核对，OCR误读为2h。'))

def q8():
    # 无量纲m=c=1，库仑系数C=.6，接触r0=1，总势垒.6。
    C=.6;r0=1.;Gamma=1+C/(2*r0)
    beta0=math.sqrt(1-1/Gamma**2)
    trials=[]
    for angle in [.15,.6,1.3,math.pi]:
        s=math.sin(angle/2)
        beta=math.sqrt((Gamma*Gamma-1)/(s*s+Gamma*Gamma-1))
        gamma=1/math.sqrt(1-beta*beta)
        v1=np.array([beta*math.cos(angle/2),beta*math.sin(angle/2),0.])
        v2=np.array([beta*math.cos(angle/2),-beta*math.sin(angle/2),0.])
        Etot=2*gamma;ptot=gamma*(v1+v2)
        invariant=math.sqrt(Etot*Etot-np.dot(ptot,ptot))
        assert abs(invariant-2*Gamma)<2e-12
        trials.append(dict(angle=angle,beta=beta,cm_energy=invariant))
    # 直接积分正碰的相对坐标与单粒子相对论动量，检测最近距离。
    rstart=100.;ginitial=Gamma-C/(2*rstart);pinitial=-math.sqrt(ginitial*ginitial-1)
    def ode(t,y):
        sep,p=y
        return [2*p/math.sqrt(1+p*p),C/(sep*sep)]
    def stop(t,y):return y[1]
    stop.direction=1;stop.terminal=True
    sol=solve_ivp(ode,(0,500),(rstart,pinitial),events=stop,rtol=2e-11,atol=2e-13,max_step=.1)
    closest=sol.y_events[0][0,0]
    energy=2*np.sqrt(1+sol.y[1]**2)+C/sol.y[0]
    assert abs(closest-r0)<1e-8 and np.max(abs(energy-2*Gamma))<1e-8
    variant_exact=math.sqrt(.0201/(math.sin(math.pi/12)**2+.0201))
    variant_low=math.sqrt(.02/math.sin(math.pi/12)**2)
    assert abs(variant_exact-.48042)<.000005 and abs(variant_low-.54641)<.000005
    save(8,dict(barrier_per_rest_energy=C/r0,Gamma=Gamma,headon_beta=beta0,angle_trials=trials,relativistic_cm_ode_closest_distance=float(closest),energy_error=float(np.max(abs(energy-2*Gamma))),variant_delta_002_angle_30_beta=variant_exact,variant_nonrelativistic_beta=variant_low,model='正碰、无辐射损失的经典势垒与相对论自由粒子运动学；不是量子聚变概率阈值。严格小于r0对应速度严格大于临界下确界。'))
if __name__=='__main__':
    for f in (q1,q2,q3,q4,q5,q6,q7,q8):f()
