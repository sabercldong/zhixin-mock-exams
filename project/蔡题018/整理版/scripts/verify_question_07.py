"""太阳透镜小黑球：圆像面积、方向辐亮度与独立球面数值积分。

预核验不等于完整交付；对有限角度仅检验明确的均匀填充方向锥，
不以Gaussian焦距冒充无像差大孔径的全光学模型。
"""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[1]

def sphere_projection_integral(theta,n_nodes=400,n_phi=1440):
    # 真正球面法向n=(sqrt(1-z²)cosφ,sqrt(1-z²)sinφ,z)；
    # dS=b² dz dφ，只对朝向来光的n·k>0面元积分。
    z,weights=np.polynomial.legendre.leggauss(n_nodes)
    phi=(np.arange(n_phi)+.5)*(2*math.pi/n_phi)
    dot=np.sqrt(1-z*z)[:,None]*math.sin(theta)*np.cos(phi)[None,:]+z[:,None]*math.cos(theta)
    return float(np.sum(np.maximum(dot,0).sum(axis=1)*weights)*(2*math.pi/n_phi))

def main():
    Rs,re,r,f,b,sigma,Ts=sp.symbols('Rs re r f b sigma Ts',positive=True)
    a=f*Rs/re
    luminosity=4*sp.pi*Rs**2*sigma*Ts**4
    irradiance_sun=luminosity/(4*sp.pi*re**2)
    lens_power=sp.pi*r*r*irradiance_sun
    image_irradiance=sp.simplify(lens_power/(sp.pi*a*a))
    assert image_irradiance==sigma*Ts**4*r*r/f**2
    tb_four=sp.simplify(sp.pi*b*b*image_irradiance/(4*sp.pi*b*b*sigma))
    assert tb_four==Ts**4*r*r/(4*f*f)
    handwritten_four=Ts**4*r*r/(16*f*f)
    assert sp.simplify(tb_four/handwritten_four)==4
    alpha,theta,phi=sp.symbols('alpha theta phi',positive=True)
    # Lambert出射度和球面的正入射积分分别从积分求出。
    hemisphere=sp.integrate(sp.cos(theta)*sp.sin(theta),(theta,0,sp.pi/2))*2*sp.pi
    assert hemisphere==sp.pi
    sphere_projection=sp.integrate(sp.cos(theta)*b*b*sp.sin(theta),(theta,0,sp.pi/2))*2*sp.pi
    assert sphere_projection==sp.pi*b*b
    omega=sp.integrate(sp.sin(theta),(theta,0,alpha))*2*sp.pi
    cone_fraction=sp.simplify(omega/(4*sp.pi))
    assert cone_fraction==(1-sp.cos(alpha))/2
    assert sp.limit(cone_fraction/alpha**2,alpha,0)==sp.Rational(1,4)
    assert sp.series(cone_fraction,alpha,0,6).removeO()==alpha**2/4-alpha**4/48
    # 从输入方向逐个积分球面朝光区域，数值不预置πb²。
    direction_checks=[]
    for direction in [0.,.1,.4,.8,1.2,math.pi/2,2.,math.pi]:
        actual=sphere_projection_integral(direction)
        error=abs(actual-math.pi)/math.pi
        assert error<1e-5,(direction,error)
        direction_checks.append(dict(direction_radians=direction,projection_integral=actual,
                                     relative_error=error))
    # 再逐方向对实际光锥求积；此处数值球面积分独立于圆像推导。
    x,w=np.polynomial.legendre.leggauss(24)
    cone_checks=[]
    for opening in [.03,.1,.3,.7,1.2,1.55]:
        directions=(x+1)*opening/2
        measured=sum(weight*sphere_projection_integral(float(t),200,720)*math.sin(t)
                     for t,weight in zip(directions,w))*opening/2*2*math.pi
        expected=math.pi*2*math.pi*(1-math.cos(opening))
        error=abs(measured-expected)/expected
        assert error<3e-5,(opening,error)
        # 对单位球与L_S=σTs⁴/π，入射除以完整出射4πσTs⁴。
        measured_temp_four=measured/(4*math.pi*math.pi)
        temp_four=(1-math.cos(opening))/2
        assert abs(measured_temp_four-temp_four)/temp_four<3e-5
        cone_checks.append(dict(cone_half_angle=opening,numerical_surface_and_direction_integral=measured,
                               relative_error=error,TB_over_TS=measured_temp_four**.25,
                               exact_filled_cone_temperature_ratio=temp_four**.25))
    # 纯近轴数据与精确理想方向锥，不声称大角Gaussian成像精确。
    paraxial=[]
    for aperture_ratio in [.001,.01,.03,.1]:
        opening=math.atan(aperture_ratio)
        exact=((1-math.cos(opening))/2)**.25
        small=math.sqrt(aperture_ratio/2)
        hand=.5*math.sqrt(aperture_ratio)
        assert abs(small/hand-math.sqrt(2))<1e-12
        if aperture_ratio<=.03:assert abs(small/exact-1)<.0002
        paraxial.append(dict(r_over_f=aperture_ratio,paraxial=small,filled_cone=exact,
                             handwritten=hand,paraxial_relative_error=small/exact-1))
    # 有非零冷背景的灰体/互易交换网络，检查所有权重非负的温度区间。
    weighted=[]
    for Cs in [.1,1.,10.]:
        for Cc in [0.,.3,3.]:
            high=6000.;cold=300.
            ball=((Cs*high**4+Cc*cold**4)/(Cs+Cc))**.25
            assert cold<=ball<=high
            weighted.append(dict(C_BS=Cs,C_BC=Cc,TB=ball))
    # 稳态热机/炉不是被动光学增亮；无电池耗尽，不违背自身状态与熵恒定。
    Ts_value=6000.;Th=2000.;Tc=300.;Qh=200.;eta=.7;TB=7000.
    W=eta*Qh;Qc=Qh-W
    assert eta<=1-Tc/Th and W+Qc==Qh and TB>Ts_value
    engine_entropy_generation=Qc/Tc-Qh/Th
    assert engine_entropy_generation>=0
    sigma_value=5.670374419e-8
    radius=math.sqrt(W/(4*math.pi*sigma_value*TB**4))
    emission=4*math.pi*radius**2*sigma_value*TB**4
    assert abs(emission-W)<1e-12
    # 炉把功转成热的熵产生；这是热边界账，不冒充远场光子熵的精确公式。
    furnace_entropy_generation=W/TB
    assert furnace_entropy_generation>0
    # 全方向覆盖率0..1时，从被动辐亮度界限不可能得到TB>Ts。
    for solid_angle in np.linspace(0,4*math.pi,257):
        ratio=(solid_angle/(4*math.pi))**.25
        assert 0<=ratio<=1
    # 用户已授权在题干补充球形；平薄两面黑物体作为改变形状后的独立对照。
    plate_four=image_irradiance/(2*sigma)
    assert sp.simplify(plate_four/tb_four)==2
    plane_cone=sp.integrate(sp.cos(theta)*sp.sin(theta),(theta,0,alpha))*2*sp.pi
    assert sp.trigsimp(plane_cone-sp.pi*sp.sin(alpha)**2)==0
    assert sp.trigsimp(sp.sin(alpha)**2/(1-sp.cos(alpha))-(1+sp.cos(alpha)))==0
    # 由真实功率ODE求温度扰动系数，不先把指数解作为输入。
    T,TB_symbol,Cb=sp.symbols('T TB Cb',positive=True)
    Pabs=4*sp.pi*b*b*sigma*TB_symbol**4
    rhs=(Pabs-4*sp.pi*b*b*sigma*T**4)/Cb
    assert sp.simplify(rhs.subs(T,TB_symbol))==0
    perturbation_coefficient=sp.diff(rhs,T).subs(T,TB_symbol)
    assert perturbation_coefficient==-16*sp.pi*b*b*sigma*TB_symbol**3/Cb
    # 四个完整带解变式，独立用收支方程计算。
    variants=[]
    exact1=6000*((1-1/math.sqrt(1.01))/2)**.25
    assert abs(exact1-1339.1390023764332)<1e-9
    variants.append(dict(number=1,paraxial=6000*math.sqrt(.1/2),
                         filled_cone=exact1,handwritten=6000*.5*math.sqrt(.1)))
    beta=(1-math.cos(.3))/2
    background_temperature=(beta*6000**4+(1-beta)*300**4)**.25
    assert abs(background_temperature-2319.5923622094024)<1e-9
    variants.append(dict(number=2,beta=beta,temperature=background_temperature))
    sphere_temp=6000*math.sqrt(.05/2)
    plate_temp=6000*((.05)**2/2)**.25
    assert abs(plate_temp/sphere_temp-2**.25)<1e-12
    variants.append(dict(number=3,sphere=sphere_temp,plate=plate_temp,
                         ratio=plate_temp/sphere_temp))
    rad8=math.sqrt(500/(4*math.pi*sigma_value*8000**4))
    rad6=math.sqrt(500/(4*math.pi*sigma_value*6000**4))
    assert abs(rad8-.00041389885774521253)<1e-15
    assert abs(rad6-.0007358201915470445)<1e-15
    assert abs(500/300-1000/1200-5/6)<1e-15
    variants.append(dict(number=4,actual_work=500,entropy_generation=5/6,
                         radius_for_8000=rad8,threshold_radius_for_6000=rad6))
    files=['scripts/verify_question_07.py','drafts/question-07-核验备忘.md',
           'drafts/question-07.md','figures/题07_图稿源文件.tex']
    complete=(ROOT/'drafts/question-07.md').exists()
    if complete:
        source=(ROOT/'drafts/question-07.md').read_text()
        assert source.count('\n## ')==9 and '<!-- question-complete -->' in source
        assert '假设太阳为黑体' in source and '球形' in source and '薄圆片' in source
        question_text=source.split('<!-- question-start -->')[1].split('<!-- question-end -->')[0]
        assert '球形小黑体（修订：补充球形条件）' in question_text
        assert not any(word in source for word in ['形状待确认','原题未明确球形','未补充就保留条件化说明'])
    names=['question-07','image-07','projection-07','cone-07','passive-07','engine-07']
    figures={name:hashlib.sha256((ROOT/f'figures/{name}.pdf').read_bytes()).hexdigest()
             for name in names if (ROOT/f'figures/{name}.pdf').exists()}
    complete=complete and len(figures)==6
    report=dict(question=7,verified_math=True,document_complete=complete,set_accepted=False,
                scope='三问球形修订主解与形状改变后的模型对照；不代表整套验收',
                image_irradiance=str(image_irradiance),TB_fourth_power=str(tb_four),
                handwritten_TB_fourth_power=str(handwritten_four),handwritten_power_error_factor=4,
                filled_cone_temperature_fourth_fraction=str(cone_fraction),
                geometric_conditions=['b远小于太阳像半径','近轴r/f远小于1用于第一式',
                                      '有限角度只给实际均匀填充锥，不将高斯像公式外推',
                                      '忽略暗背景；灰体权重法不冒充任意频率滤光的常数式'],
                independent_sphere_surface_projection=direction_checks,
                independent_surface_and_cone_quadrature=cone_checks,paraxial_comparison=paraxial,
                passive_gray_exchange_examples=weighted,
                variants_checked=variants,
                perturbation_coefficient=str(perturbation_coefficient),
                shape_comparison_fourth_power_factor=str(sp.simplify(plate_four/tb_four)),
                unresolved_critical_condition=None,
                condition_resolution=dict(explicit_human_approval=True,reply='是',
                                          confirmed_date='2026-10-08',shape='sphere',
                                          approved_change='题干补充球形小黑体并注明修订'),
                active_steady_example=dict(Ts=Ts_value,Th=Th,Tc=Tc,TB=TB,Qh=Qh,W=W,Qc=Qc,
                                           efficiency=eta,carnot_bound=1-Tc/Th,ball_radius=radius,
                                           emission_power=emission,
                                           engine_entropy_generation=engine_entropy_generation,
                                           furnace_heat_boundary_entropy_generation=furnace_entropy_generation,
                                           device_state_and_entropy_constant=True),
                figures_sha256=figures,
                source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in files if (ROOT/p).exists()})
    destination='verification-q07.json' if complete else 'verification-q07-preliminary.json'
    (ROOT/'build'/destination).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(question=7,verified_math=True,document_complete=complete,
                         max_projection_error=max(v['relative_error'] for v in direction_checks),
                         max_cone_error=max(v['relative_error'] for v in cone_checks),
                         active_steady_ball_radius=radius),ensure_ascii=False))

if __name__=='__main__':main()
