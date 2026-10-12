"""题设等质量静电双粒子：两条符号路线与独立双粒子Hamilton ODE。

只核验题设的瞬时静电/相对论动量半经典模型，非完整Maxwell或量子基态。
"""
from pathlib import Path
import hashlib,json,math
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[1]

def main():
    m,c,L,A=sp.symbols('m c L A',positive=True)
    beta=sp.symbols('beta',positive=True)
    # 用0<beta<1参数化合法域，避免无根据sqrt化简。
    velocity=c*beta
    momentum=m*c*beta/sp.sqrt(1-beta**2)
    radius=L/momentum
    coupling=2*L*c*beta
    assert sp.simplify(radius*momentum-L)==0
    assert sp.simplify(2*momentum*velocity/radius-coupling/radius**2)==0
    # 动量矢量的时间导数，而不是仅对动量大小求导。
    t,om=sp.symbols('t om',real=True)
    vec=sp.Matrix([-momentum*sp.sin(om*t),momentum*sp.cos(om*t)])
    assert sp.trigsimp(sp.diff(vec,t).dot(sp.diff(vec,t))-momentum**2*om**2)==0
    # 独立固定总角动量的相对Hamiltonian。
    rr,pr=sp.symbols('rr pr',real=True,positive=True)
    root=sp.sqrt(m*m*c**4+c*c*(pr*pr+L*L/rr**2))
    H=2*root-A/rr
    Hcirc=H.subs(pr,0)
    derivative=sp.diff(Hcirc,rr)
    stationary_A=2*c*c*L*L/(rr*sp.sqrt(m*m*c**4+c*c*L*L/rr**2))
    assert sp.simplify(derivative.subs(A,stationary_A))==0
    # 半径代回完整能量的化简在合法域以gamma>1为参数。
    gam=sp.symbols('gam',positive=True)
    # 消去根式平方关系核对能量，不强迫无域的sqrt(1-beta²)为正。
    expected_B=m*c*c/sp.sqrt(1-beta**2)
    assert sp.simplify((m*m*c**4+c*c*L*L/radius**2)-expected_B**2)==0
    energy=2*expected_B-coupling/radius
    assert sp.simplify(energy-2*m*c*c*sp.sqrt(1-beta**2))==0
    Hrr=sp.diff(Hcirc,rr,2).subs(A,stationary_A)
    positive_Hrr=2*m*m*c**6*L*L/(rr**4*(m*m*c**4+c*c*L*L/rr**2)**sp.Rational(3,2))
    # factor先识别正参数平方组合，避免simplify保留sqrt((L²+c²m²r²)²)。
    assert sp.factor(Hrr-positive_Hrr)==0
    Hprpr=sp.diff(H,pr,2).subs(pr,0)
    orbital_squared=(2*c*c*L/(rr**2*sp.sqrt(m*m*c**4+c*c*L*L/rr**2)))**2
    assert sp.factor(Hprpr*Hrr/orbital_squared-m*m*c**4/(m*m*c**4+c*c*L*L/rr**2))==0
    assert sp.series(sp.sqrt(1-beta**2),beta,0,6).removeO()==1-beta**2/2-beta**4/8
    assert sp.limit(Hcirc*rr,rr,0,dir='+')==2*c*L-A
    critical_H=Hcirc.subs(A,2*c*L)
    assert sp.limit(critical_H,rr,0,dir='+')==0
    assert sp.simplify(sp.limit(critical_H/rr,rr,0,dir='+')-m*m*c**3/L)==0
    # 定L能量驻点数值求根，不先用解析半径作初值或方程输入。
    rows=[]
    for n in [1,2,3,7]:
        for relative_coupling in [.01,.25,.75,.995]:
            # normalized m=c=hbar=1; A=2*n*relative_coupling.
            aa=2*n*relative_coupling
            def derivative_numeric(r):
                return aa/r**2-2*n*n/(r**3*math.sqrt(1+n*n/r**2))
            sampled=np.logspace(-5,7,1201)
            bracket=next((lo,hi) for lo,hi in zip(sampled[:-1],sampled[1:])
                         if derivative_numeric(lo)<0<derivative_numeric(hi))
            numerical_radius=brentq(derivative_numeric,*bracket,xtol=1e-13,rtol=1e-14)
            predicted=n*math.sqrt(1-relative_coupling**2)/relative_coupling
            assert abs(numerical_radius/predicted-1)<2e-12
            pp=n/numerical_radius
            vv=pp/math.sqrt(1+pp*pp)
            oo=2*vv/numerical_radius
            # 两粒子独立相空间，共8状态；不把解析轨道当rhs。
            initial=np.array([numerical_radius/2,0,-numerical_radius/2,0,0,pp,0,-pp])
            def rhs(phase,z):
                rp=z[0:2];rm=z[2:4];pplus=z[4:6];pminus=z[6:8]
                delta=rm-rp;separation=np.linalg.norm(delta)
                force=aa*delta/separation**3
                vp=pplus/math.sqrt(1+np.dot(pplus,pplus))
                vm=pminus/math.sqrt(1+np.dot(pminus,pminus))
                return np.concatenate((vp,vm,force,-force))/oo
            sol=solve_ivp(rhs,(0,4*math.pi),initial,method='DOP853',
                          rtol=2e-12,atol=2e-13,max_step=.01)
            assert sol.success
            radii=np.linalg.norm(sol.y[0:2]-sol.y[2:4],axis=0)
            lp=sol.y[0]*sol.y[5]-sol.y[1]*sol.y[4]
            lm=sol.y[2]*sol.y[7]-sol.y[3]*sol.y[6]
            kinetic=np.sqrt(1+(sol.y[4:6]**2).sum(axis=0))+np.sqrt(1+(sol.y[6:8]**2).sum(axis=0))
            energies=kinetic-aa/radii
            separation_error=float(np.max(np.abs(radii/numerical_radius-1)))
            angular_error=float(np.max(np.abs((lp+lm)/n-1)))
            energy_error=float(np.max(np.abs(energies-energies[0])))
            com_error=float(np.max(np.abs(sol.y[0:2]+sol.y[2:4])))
            assert separation_error<2e-8 and angular_error<2e-10 and energy_error<2e-10 and com_error<1e-12
            assert abs(vv-relative_coupling)<1e-12
            assert abs(energies[0]-2*math.sqrt(1-relative_coupling**2))<1e-11
            rows.append(dict(n=n,A=aa,beta=vv,stationary_radius=numerical_radius,
                             radius_relative_error=numerical_radius/predicted-1,
                             ode_separation_relative_error=separation_error,
                             ode_angular_relative_error=angular_error,ode_energy_error=energy_error,
                             ode_center_of_mass_error=com_error))
    # 阈值两侧能量导数逐点检查；等号无正半径驻点。
    threshold=[]
    for aa in [1.9,2.,2.1,3.]:
        vals=[aa/r**2-2/(r**3*math.sqrt(1+1/r**2)) for r in [.0001,.01,.1,1,10,100]]
        if aa>=2:assert all(v>0 for v in vals)
        threshold.append(dict(A=aa,derivatives=vals,positive_circular_orbit_exists=aa<2))
    alpha=7.2973525643e-3
    critical_Z=math.sqrt(2/alpha)
    assert 16<critical_Z<17
    allowed=[Z for Z in range(1,21) if alpha*Z*Z<2]
    assert allowed==list(range(1,17))
    cvalue=299792458.;hbar=6.62607015e-34/(2*math.pi);electron_mass=9.1093837139e-31
    compton=hbar/(electron_mass*cvalue)
    numerical=[]
    for Z in [1,8,16]:
        coupling_ratio=alpha*Z*Z/2
        rvalue=compton*math.sqrt(1-coupling_ratio**2)/coupling_ratio
        classical=compton/coupling_ratio
        numerical.append(dict(Z=Z,beta=coupling_ratio,distance_m=rvalue,
                              one_particle_radius_m=rvalue/2,classical_distance_m=classical,
                              radius_correction=rvalue/classical))
    # 带解变式：激发n、经典修正、能量与径向频率、超过基态阈值但n>1存在。
    variants=[dict(number=1,n=2,Z=1,beta=alpha/4,
                   radius_ratio_to_ground=4*math.sqrt(1-alpha**2/16)/math.sqrt(1-alpha**2/4)),
              dict(number=2,beta=.6,radius_correction=.8,gamma=1.25),
              dict(number=3,beta=.6,total_energy_over_2mc2=.8,
                   binding_energy_over_mc2=.4,radial_over_orbital=.8),
              dict(number=4,Z=20,n_min=2,ground_exists=False,excited_beta=alpha*400/4)]
    assert 1<alpha*400/2<2
    assert variants[-1]['excited_beta']<1
    variants[1]['continuous_Z_for_n1']=math.sqrt(1.2/alpha)
    variants[2]['orbital_frequency_over_mc2_by_nhbar']=2*.6/(.8/.6)
    variants[2]['radial_frequency_over_mc2_by_nhbar']=.8*variants[2]['orbital_frequency_over_mc2_by_nhbar']
    assert abs(variants[2]['orbital_frequency_over_mc2_by_nhbar']-.9)<1e-14
    assert abs(variants[2]['radial_frequency_over_mc2_by_nhbar']-.72)<1e-14
    vv=variants[-1]['excited_beta']
    variants[-1]['excited_radius_m_for_electron_mass']=2*compton*math.sqrt(1-vv*vv)/vv
    assert abs(variants[-1]['excited_radius_m_for_electron_mass']/7.236284691356736e-13-1)<1e-14
    names=['question-08','momentum-08','angular-08','threshold-08','energy-08']
    files=['scripts/verify_question_08.py','drafts/question-08-核验备忘.md','drafts/question-08.md','figures/题08_图稿源文件.tex']
    figs={name:hashlib.sha256((ROOT/f'figures/{name}.pdf').read_bytes()).hexdigest()
          for name in names if (ROOT/f'figures/{name}.pdf').exists()}
    complete=(ROOT/'drafts/question-08.md').exists() and len(figs)==5
    if complete:
        text=(ROOT/'drafts/question-08.md').read_text()
        assert text.count('\n## ')==9 and '<!-- question-complete -->' in text
        assert 'r_0/2' in text and '静电' in text and '严格' in text
    report=dict(question=8,verified_math=True,document_complete=complete,set_accepted=False,
                model_scope='题设瞬时静电+相对论动量+总角动量量子化；非完整电磁/量子理论',
                handwritten_conclusion_correct=True,unresolved_critical_condition=None,
                base_distance='hbar*sqrt(4-alpha**2*Z**4)/(m0*c*alpha*Z**2)',
                strict_condition='0<alpha*Z**2<2; Z positive integer => Z<=16',
                critical_Z=critical_Z,symbolic_independent_routes=['momentum_rotation_and_total_L','fixed_L_Hamiltonian_derivative'],
                independent_numeric_Hamilton_roots_and_two_particle_odes=rows,
                threshold_checks=threshold,numerical_examples=numerical,variants_checked=variants,
                stability_Hrr=str(positive_Hrr),radial_frequency_ratio_squared='1-beta**2',
                figures_sha256=figs,
                source_sha256={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in files if (ROOT/f).exists()})
    destination='verification-q08.json' if complete else 'verification-q08-preliminary.json'
    (ROOT/'build'/destination).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(question=8,verified_math=True,document_complete=complete,
                         independent_odes=len(rows),critical_Z=critical_Z,
                         max_ode_separation_error=max(row['ode_separation_relative_error'] for row in rows),
                         examples=numerical,variants=variants),ensure_ascii=False))

if __name__=='__main__':main()
