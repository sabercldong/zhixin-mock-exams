"""第025套独立预核验，保留模型歧义而不伪造答案。"""
from pathlib import Path
import json
import math
import numpy as np
from scipy.integrate import solve_ivp, quad

ROOT = Path(__file__).resolve().parents[1]

def main():
    report = {}
    # 动圈互易耦合：g*v是反电动势，g*I是安培力。
    coupling, mass, inductance, frequency, voltage = 2., 3., .04, 1.7, .8
    denominator = coupling**2 - mass*inductance*frequency**2
    X = coupling*voltage/(frequency*denominator)
    t = np.linspace(0, 4, 200)
    x = X*np.sin(frequency*t)
    velocity = frequency*X*np.cos(frequency*t)
    current = -mass*frequency**2*x/coupling
    derivative = -mass*frequency**3*X*np.cos(frequency*t)/coupling
    residual = inductance*derivative + coupling*velocity - voltage*np.cos(frequency*t)
    assert np.max(np.abs(residual)) < 1e-12
    report['01'] = dict(status='preflight_pass_with_explicit_models',
                        circuit_residual=float(np.max(np.abs(residual))),
                        missing_conditions=['无阻力不产生吸引性的稳定态','未给回复力','自感是否忽略需注明'])
    # 辐射端点：以总反冲系统不变质量的下界计算，而非忽略反冲。
    M, recoil = 1.05, 1.
    endpoint = (M*M-recoil*recoil)/(2*M)
    inferred = endpoint + math.sqrt(endpoint*endpoint+recoil*recoil)
    assert abs(inferred-M)<1e-12
    recoil_energy = math.sqrt(recoil*recoil+endpoint*endpoint)
    assert abs(endpoint+recoil_energy-M)<1e-12
    beta=.3;doppler=math.sqrt((1+beta)/(1-beta))
    report['02']=dict(status='preflight_pass',rest_endpoint=endpoint,recovered_mass=inferred,
                       forward_doppler=doppler,naive_mass=doppler*endpoint+math.sqrt((doppler*endpoint)**2+recoil**2))
    # 两个独立方向的简谐投影，经可逆斜坐标变换构造四类轨迹。
    samples=np.linspace(0,2*math.pi,1001)
    x=np.cos(samples);u=np.cos(2*samples);y=math.sqrt(2)*u-x
    parabola=math.sqrt(2)*(2*x*x-1)-x
    assert np.max(np.abs(y-parabola))<1e-12
    x8=np.sin(samples);u8=np.sin(2*samples);y8=math.sqrt(2)*u8-x8
    assert np.max(np.abs((x8+y8)/math.sqrt(2)-u8))<1e-12
    report['03']=dict(status='preflight_pass',possible_shape_classes=['圆','抛物线弧','椭圆','八字形'],
                       condition='不要求两简谐投影同频；图示表示形状类别，不能擅加共同平衡点与固定频率。')
    # Carnot制冷与漏热稳定根。
    k,TH,TL=173.,313.15,298.15
    P=k*(TH-TL)**2/TL
    delta=(math.sqrt(P*P+4*k*P*TH)-P)/(2*k)
    assert abs(TH-delta-TL)<1e-12
    report['04']=dict(status='preflight_pass',electrical_power_W=P,cooling_power_W=k*(TH-TL),
                       COP=TL/(TH-TL),lowest_temperature_K=TH-delta)
    # 透镜/反射面逐界面光线传播，反射时改用沿传播方向的局部斜率。
    def ray(p,a):
        h=p+2*a;s=a-h
        y2=h+3*s
        direct=y2+2*(s-y2)
        s+=2*y2;y3=y2+3*s
        s+=2*y3;y4=y3+3*s
        s-=y4;ghost=y4+2*s
        return direct,ghost
    cases=[]
    for p0,a0 in [(.001,.002),(-.001,.002),(.002,0.),(0.,.003)]:
        direct,ghost=ray(p0,a0)
        assert abs(direct+a0)<1e-12 and abs(ghost-(56*p0+33*a0))<1e-12
        cases.append(dict(aperture_height=p0,incident_angle=a0,direct=direct,ghost=ghost))
    report['05']=dict(status='preflight_pass',index=1.5,image_distance_over_f=2.,
                       ghost_diameter_over_D=56.,ghost_center_over_f_alpha=33.,rays=cases,
                       qualification='双凸表面反射从空气侧观察均为凸面反射；须检查多次传播的近轴范围和截光。')
    # 曲绳平面静摩擦是向量约束，不是只取切向摩擦，更不是柱面欧拉绳公式。
    theta=2*math.pi/3
    a=np.linspace(0,theta,10001)
    profile_A=np.sin(np.minimum(a,math.pi/2))
    slope_A=np.where(a<math.pi/2,np.cos(a),0.)
    offset=theta-math.pi/2
    profile_B=np.sin(np.maximum(a-offset,0.))
    slope_B=np.where(a>offset,np.cos(a-offset),0.)
    assert np.max(profile_A**2+slope_A**2)<1+1e-12
    assert np.max(profile_B**2+slope_B**2)<1+1e-12
    assert abs(profile_A[-1]-1)<1e-12 and abs(profile_B[-1]-1)<1e-12
    report['06']=dict(status='preflight_pass_with_nonuniqueness',
                       maximum_static_force_over_mu_m_g=1/theta,
                       two_distinct_admissible_static_profiles=True,
                       plateau_angle_of_profile_A_degrees=30.,
                       issue='同一最大拉力存在不同静力张力分布；静力饱和与实际滑动分界不等价。')
    # 椭圆几何与极坐标动力学分开核验。
    ecc=.6;semimajor=2.;b=semimajor*math.sqrt(1-ecc*ecc);l=semimajor*(1-ecc*ecc)
    geometry=[]
    for E in np.linspace(.1,math.pi-.1,10):
        position=np.array([semimajor*math.cos(E),b*math.sin(E)])
        focus=np.array([semimajor*ecc,0.]);other=-focus
        rvec=position-focus;rpvec=position-other
        r=np.linalg.norm(rvec);rp=np.linalg.norm(rpvec)
        cosine=math.sqrt((1+np.dot(rvec,rpvec)/(r*rp))/2)
        rho=(semimajor**2*math.sin(E)**2+b*b*math.cos(E)**2)**1.5/(semimajor*b)
        assert abs(1/r+1/rp-2*cosine*cosine/l)<1e-12
        assert abs(rho-l/cosine**3)<1e-12
        geometry.append(dict(eccentric_anomaly=E,r=r,other_r=rp,curvature_radius=rho))
    report['07']=dict(status='preflight_pass',semilatus_rectum=l,geometry=geometry)
    # 受约束Lorentz力ODE，不重复能量公式作自证。
    def ode(t,state,wc):
        phi,rate,z,vz=state
        return [rate,wc*vz*math.cos(phi),vz,-wc*rate*math.cos(phi)]
    cases=[]
    for wc,wz,wphi in [(0.3,.6,1.),(1.5,0.,1.),(.5,0.,1.),(1.,0.,1.),(-.3,.6,1.)]:
        sol=solve_ivp(lambda t,y:ode(t,y,wc),(0,30),[0,wphi,0,wz],rtol=2e-11,atol=2e-12,max_step=.02)
        phi,rate,z,vz=sol.y
        momentum_residual=np.max(np.abs(vz-(wz-wc*np.sin(phi))))
        energy_residual=np.max(np.abs(rate**2+vz**2-(wphi**2+wz**2)))
        assert momentum_residual<2e-9 and energy_residual<2e-9
        cases.append(dict(wc=wc,wz=wz,wphi=wphi,momentum_residual=float(momentum_residual),energy_residual=float(energy_residual)))
    report['08']=dict(status='preflight_pass',ODE_cases=cases,
                       winding_bound='abs(wc)<sqrt(wz^2+wphi^2)-abs(wz)',
                       closed_if_wz_zero='abs(wc)!=abs(wphi)',
                       qualification='非零横向磁场通常不产生等螺距圆柱螺旋线；需区分绕轴运动、轴向反向及闭合振荡。')
    directory=ROOT/'build';directory.mkdir(exist_ok=True)
    (directory/'preflight-physics.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
