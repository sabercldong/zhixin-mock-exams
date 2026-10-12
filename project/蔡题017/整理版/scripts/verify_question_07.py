"""017 Q7: independently timed real fields, optical ODEs and exhaustive branch tests."""
from pathlib import Path
import hashlib,json,math
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def e(a):return np.array([math.cos(a),math.sin(a)])
def q(a):return np.array([-math.sin(a),math.cos(a)])
def wave(a,delta):
    u,w=e(a),q(a)
    return np.outer(u,u)+np.exp(-1j*delta)*np.outer(w,w)
def intensity(F,t):return float(abs(e(t)@F)**2)
def real_wave(C,S,a,phase_e,phase_o):
    # Actual cosine/sine coefficients on each material axis; keep both absolute phases.
    u,w=e(a),q(a)
    ce,se=float(u@C),float(u@S)
    co,so=float(w@C),float(w@S)
    def advanced(c,s,phi):return c*math.cos(phi)+s*math.sin(phi),s*math.cos(phi)-c*math.sin(phi)
    ue,ve=advanced(ce,se,-phase_e);uo,vo=advanced(co,so,-phase_o)
    return ue*u+uo*w,ve*u+vo*w
def sampled(C,S,t):
    times=np.arange(4096)*2*math.pi/4096
    field=np.outer(C,np.cos(times))+np.outer(S,np.sin(times))
    incident=.5
    total=np.mean(np.sum(field*field,axis=0))/incident
    passed=np.mean((e(t)@field)**2)/incident
    rejected=np.mean((q(t)@field)**2)/incident
    return float(total),float(passed),float(rejected)
def real_chain(plates,t):
    C=np.array([1.,0.]);S=np.zeros(2)
    for a,d,base in plates:C,S=real_wave(C,S,a,base+d,base)
    return sampled(C,S,t)
def ode_wave(F,a,delta,base=7.3):
    u,w=e(a),q(a)
    K=(base+delta)*np.outer(u,u)+base*np.outer(w,w)
    sol=solve_ivp(lambda z,f:1j*K@f,[0.,1.],np.array(F,dtype=complex),
        method='DOP853',rtol=8e-12,atol=8e-13)
    return sol.y[:,-1]
def circularity(F):return float(2*np.imag(np.conjugate(F[0])*F[1]))
def distance_axis(a,b):return abs(math.sin(a-b))
def classify(a,b,t):
    # Nonparallel target only; two complete families with physical axes modulo pi.
    A=distance_axis(a,b)<2e-6 and abs(math.sin(2*a-t))<2e-6
    B=abs(math.cos(2*a))<2e-6 and abs(math.sin(a+b-t))<2e-6
    return 'same-axis' if A else 'circular' if B else None
def main():
    a,b,t,d=sp.symbols('a b t d',real=True)
    es=lambda z:sp.Matrix([sp.cos(z),sp.sin(z)])
    qs=lambda z:sp.Matrix([-sp.sin(z),sp.cos(z)])
    W=lambda z,phase:es(z)*es(z).T+sp.exp(-sp.I*phase)*qs(z)*qs(z).T
    H=W(a,sp.pi)
    assert all(sp.trigsimp(x)==0 for x in H*es(0)-es(2*a))
    Q1=W(a,sp.pi/2);Q2=W(b,sp.pi/2)
    F=(Q2*Q1*es(0)).applyfunc(sp.expand_complex)
    real=sp.cos(a-b)*es(a+b)
    imag=-sp.sin(a-b)*es(sp.pi/2-(a-b))
    assert all(sp.trigsimp(sp.re(F[i])-real[i],method='fu')==0 for i in range(2))
    assert all(sp.trigsimp(sp.im(F[i])-imag[i],method='fu')==0 for i in range(2))
    Ar=(qs(t).T*F)[0]
    assert sp.trigsimp(sp.re(Ar)-sp.cos(a-b)*sp.sin(a+b-t),method='fu')==0
    assert sp.trigsimp(sp.im(Ar)+sp.sin(a-b)*sp.cos(a-b+t),method='fu')==0
    stokes=sp.trigsimp(2*sp.im(sp.conjugate(F[0])*F[1]),method='fu')
    assert sp.trigsimp(stokes+sp.cos(2*a)*sp.sin(2*(a-b)),method='fu')==0
    assert sp.trigsimp((sp.cos(a-b)**2+sp.sin(a-b)**2)-1)==0
    ratio=sp.sin(2*a)**2/4
    assert sp.trigsimp(sp.diff(ratio,a)-sp.sin(4*a)/2)==0
    assert sp.trigsimp(sp.diff(ratio,a,2)-2*sp.cos(4*a))==0
    rng=np.random.default_rng(1707)
    # Malus law independently by time averaged real projections, including signs.
    polarizers=[]
    for angle in [0,math.pi/6,math.pi/4,math.pi/3,math.pi/2,3*math.pi/4,-math.pi/5]:
        C=math.cos(angle)*e(angle);S=np.zeros(2)
        total,passed,rejected=sampled(C,S,math.pi/2)
        exact=.25*math.sin(2*angle)**2
        assert abs(passed-exact)<2e-14
        polarizers.append(dict(theta=angle,ratio=passed,total_before_P2=total))
    arbitrary=[]
    for j in range(24):
        a0=float(rng.uniform(-math.pi,math.pi));b0=float(rng.uniform(-math.pi,math.pi))
        t0=float(rng.uniform(-math.pi,math.pi));d0=float(rng.uniform(-3*math.pi,3*math.pi))
        phases=[(a0,d0,3.1+j*.1)]
        F0=wave(a0,d0)@e(0)
        total,passed,rejected=real_chain(phases,t0)
        assert abs(total-1)<3e-14 and abs(passed-intensity(F0,t0))<3e-14
        assert abs(passed+rejected-1)<3e-14
        phases=[(a0,math.pi/2,3.1),(b0,math.pi/2,5.7)]
        total2,passed2,rejected2=real_chain(phases,t0)
        F2=wave(b0,math.pi/2)@wave(a0,math.pi/2)@e(0)
        reject_formula=(math.cos(a0-b0)**2*math.sin(a0+b0-t0)**2+
            math.sin(a0-b0)**2*math.cos(a0-b0+t0)**2)
        assert abs(total2-1)<3e-14 and abs(passed2-intensity(F2,t0))<3e-14
        assert abs(rejected2-reject_formula)<3e-14
        assert abs(circularity(F2)+math.cos(2*a0)*math.sin(2*(a0-b0)))<3e-14
        arbitrary.append(dict(theta3=a0,second_axis=b0,target=t0,retardation=d0,
            real_field_single_ratio=passed,real_field_two_ratio=passed2,
            norm_and_rejection_checked=True))
    optical_odes=[]
    for j in range(10):
        a0=float(rng.uniform(-math.pi,math.pi));b0=float(rng.uniform(-math.pi,math.pi))
        d0=float(rng.uniform(-2*math.pi,2*math.pi));base=3+j
        actual=ode_wave(e(0),a0,d0,base)
        expected=np.exp(1j*(base+d0))*(wave(a0,d0)@e(0))
        err=float(np.max(abs(actual-expected)));assert err<2e-9
        actual2=ode_wave(ode_wave(e(0),a0,math.pi/2,base),b0,math.pi/2,base+1)
        expect2=np.exp(1j*(2*base+1+math.pi))*(wave(b0,math.pi/2)@wave(a0,math.pi/2)@e(0))
        err2=float(np.max(abs(actual2-expect2)));assert err2<3e-9
        optical_odes.append(dict(single_ODE_error=err,two_ODE_error=err2))
    families=[]
    for tv in [.19,math.pi/6,math.pi/3,math.pi/2,2.4]:
        for sign in [1,-1]:
            for typ,av,bv in [
                ('same-axis',tv/2,tv/2),
                ('same-axis-shift',tv/2+math.pi/2,tv/2+math.pi/2),
                ('circular-positive',math.pi/4,tv-math.pi/4),
                ('circular-negative',-math.pi/4,tv+math.pi/4)]:
                total,passed,rejected=real_chain([(av,sign*math.pi/2,4.),(bv,sign*math.pi/2,6.)],tv)
                assert abs(passed-1)<3e-14 and rejected<3e-28
                families.append(dict(theta2=tv,family=typ,delta_sign=sign,axes=[av,bv],ratio=passed))
    # Independent search of the two real rejection equations; classify all roots, not just sample families.
    roots=[]
    for tv in [.19,math.pi/6,math.pi/3,math.pi/2,2.4]:
        discovered=[]
        def residual(v):
            # Actual physical optical matrix only, not analytical branch equations.
            Fv=wave(v[1],math.pi/2)@wave(v[0],math.pi/2)@e(0)
            z=q(tv)@Fv
            return [z.real,z.imag]
        for av in np.linspace(.03,math.pi-.03,7):
            for bv in np.linspace(.07,math.pi-.07,7):
                sol=least_squares(residual,[av,bv],xtol=1e-13,ftol=1e-13,gtol=1e-13,max_nfev=100)
                if np.linalg.norm(sol.fun)>1e-8:continue
                aa,bb=np.mod(sol.x,math.pi)
                typ=classify(aa,bb,tv)
                if typ is None:
                    # At a crossed target the two families coincide, so rejection has a quadratic zero.
                    # Refine the actual complex optical product; a tiny residual alone is not a tight angle bound.
                    with mp.workdps(65):
                        target=mp.pi/2 if abs(tv-math.pi/2)<1e-14 else mp.mpf(str(tv))
                        def actual_high_precision(ax,bx):
                            def plate(z):
                                u=mp.matrix([mp.cos(z),mp.sin(z)])
                                w=mp.matrix([-mp.sin(z),mp.cos(z)])
                                return u*u.T-mp.j*w*w.T
                            fv=plate(bx)*plate(ax)*mp.matrix([1,0])
                            value=-mp.sin(target)*fv[0]+mp.cos(target)*fv[1]
                            return mp.re(value),mp.im(value)
                        refined=mp.findroot(actual_high_precision,(mp.mpf(str(aa)),mp.mpf(str(bb))),
                            tol=mp.mpf('1e-44'),maxsteps=120)
                        aa,bb=float(refined[0])%math.pi,float(refined[1])%math.pi
                    typ=classify(aa,bb,tv)
                assert typ is not None,(tv,aa,bb,sol.fun)
                if not any(distance_axis(aa,x['axes'][0])<2e-6 and distance_axis(bb,x['axes'][1])<2e-6 for x in discovered):
                    discovered.append(dict(axes=[float(aa),float(bb)],family=typ))
        assert len(discovered)==(2 if abs(tv-math.pi/2)<1e-14 else 4)
        roots.append(dict(theta2=tv,independent_roots=discovered))
    half_cases=[]
    for tv in [.19,math.pi/6,math.pi/3,math.pi/2,2.4]:
        for sign in [1,-1]:
            for order in [1,3,5]:
                for axis_shift in [0,math.pi/2]:
                    av=tv/2+axis_shift
                    total,passed,rejected=real_chain([(av,sign*order*math.pi,5.)],tv)
                    assert abs(passed-1)<3e-14 and rejected<1e-27
                    half_cases.append(dict(target=tv,axis=av,signed_half_order=sign*order,ratio=passed))
    loci=[]
    for av in [math.pi/6,math.pi/4]:
        actual=wave(av,math.pi/2)@e(0)
        ts=np.arange(61)*2*math.pi/61
        field=np.outer(actual.real,np.cos(ts))+np.outer(actual.imag,np.sin(ts))
        if av==math.pi/6:
            drawn=np.vstack([.75*np.cos(ts)-.25*np.sin(ts),.433012702*(np.cos(ts)+np.sin(ts))])
        else:drawn=np.vstack([.5*np.cos(ts)-.5*np.sin(ts),.5*np.cos(ts)+.5*np.sin(ts)])
        error=float(np.max(abs(field-drawn)));assert error<3.1e-10
        loci.append(dict(first_axis=av,current_TikZ_locus_error=error))
    degenerates=[]
    for av in [.0,.14,math.pi/4,.91,math.pi/2]:
        bv=av+math.pi/2
        Fv=wave(bv,math.pi/2)@wave(av,math.pi/2)@e(0)
        assert intensity(Fv,0)>1-2e-14
        degenerates.append(dict(orthogonal_quarter_axes=[av,bv],parallel_analyzer_ratio=intensity(Fv,0),
            crossed_analyzer_ratio=intensity(Fv,math.pi/2)))
    # Exact numerical variants and axis/thickness tolerances from actual field propagation.
    theta=math.pi/3;lam=632.8e-9;dn=.01;lhalf=lam/(2*dn)
    err_axis=math.pi/180;err_delta=5*math.pi/180
    errvals={}
    for label,eps,eta in [('axis_only',err_axis,0),('retardation_only',0,err_delta),('both',err_axis,err_delta)]:
        beta=theta/2+eps
        got=real_chain([(beta,math.pi+eta,4.3)],theta)[1]
        A=math.cos(beta)*math.sin(beta-theta);B=math.sin(beta)*math.cos(beta-theta)
        exact=1-(A+B)**2+4*A*B*math.sin(eta/2)**2
        assert abs(got-exact)<2e-14
        errvals[label]=got
    quarters=[]
    for aa,bb in [(math.pi/12,math.pi/12),(7*math.pi/12,7*math.pi/12),
        (math.pi/4,-math.pi/12),(-math.pi/4,5*math.pi/12)]:
        got=real_chain([(aa,math.pi/2,4.3),(bb,math.pi/2,2.7)],math.pi/6)[1]
        assert abs(got-1)<2e-14
        quarters.append(dict(axes_deg=[math.degrees(aa)%180,math.degrees(bb)%180],ratio=got))
    spectra=[]
    for factor in [.9,1.,1.1]:
        phase=math.pi/factor
        got=real_chain([(math.pi/4,phase,9.)],math.pi/2)[1]
        pair=real_chain([(math.pi/4,phase/2,6.),(math.pi/4,phase/2,7.)],math.pi/2)[1]
        orth=real_chain([(math.pi/4,phase/2,6.),(3*math.pi/4,phase/2,7.)],math.pi/2)[1]
        assert abs(got-math.sin(phase/2)**2)<2e-14 and abs(pair-got)<2e-14 and orth<3e-28
        spectra.append(dict(lambda_over_lambda0=factor,half_wave_ratio=got,
            same_axis_quarter_pair=pair,orthogonal_axes_quarter_pair=orth))
    assert abs(lhalf-31.64e-6)<1e-18
    names=['question-07','malus-07','axes-07','half-07','quarter-07','branches-07']
    sources=['scripts/verify_question_07.py','drafts/question-07.md','figures/题07_图稿源文件.tex']
    complete=all((ROOT/p).exists() for p in sources) and all((ROOT/f'figures/{n}.{ext}').exists() for n in names for ext in ['pdf','png'])
    if complete:
        text=(ROOT/'drafts/question-07.md').read_text()
        modules=['题型定位','知识点','物理图像','解题入口','解析','关键洞察','易错点','课堂讲解建议','变式训练']
        assert [s.split('、',1)[1] for s in text.splitlines() if s.startswith('## ')]==modules
        assert text.count('<!-- question-complete -->')==1
        assert all(text.count(f'../figures/{n}.png')==1 for n in names)
    report=dict(question=7,verified_math=True,document_complete=complete,set_accepted=False,
        scope='real periodic fields, optical propagation ODE and independent root search, not visual acceptance',
        symbolic_field_and_rejection_identities_verified=True,polarizer_time_averages=polarizers,
        arbitrary_real_field_cases=arbitrary,actual_optical_ODE_cases=optical_odes,
        full_transmission_family_checks=families,independent_quarter_roots=roots,
        signed_half_wave_and_axis_checks=half_cases,actual_field_figure_locus_checks=loci,
        parallel_target_degenerate_checks=degenerates,
        numerical_variants=dict(half_wave_thickness_m=lhalf,quarter_wave_thickness_m=lhalf/2,
            axis_and_retardation_error_ratios=errvals,quarter_target_30deg=quarters,wavelength_spectrum=spectra),
        handwritten_notes=['Malus double projection route and half-wave rotation are correct',
            'keep the real wave decomposition of both quarter plates with its relative projection signs',
            'the first-plate input components both use beta1, not beta2 in the second input component',
            'two same-oriented quarter plates are a half-wave plate; orthogonal material axes cancel',
            'the handwritten two-quarter solution lists representative families only; complete angles modulo pi and the negative-45-degree circular branch',
            'the stated nonzero analyzer angle is understood physically modulo pi; parallel-target degeneracy is separately derived'],
        assumptions=['ideal lossless plates, ideal polarizers, normal incidence, monochromatic light',
            'I1 means after P1, not before P1; I1>0',
            'angle axes are unoriented lines modulo pi; material extraordinary and ordinary axes remain distinguished',
            'both quarter plates have the same signed retardation fixed by lprime*(ne-no)=lambda/4',
            'complex phase convention explicit; global phase ignored, relative phases retained'],
        dimensions=dict(retardation='2 pi times dimensionless refractive-index difference times length/wavelength',
            intensity_ratios='dimensionless',waveplate_thickness='length',passed=True),
        source_sha256={p:sha(ROOT/p) for p in sources if (ROOT/p).exists()},
        figures_sha256={n:sha(ROOT/f'figures/{n}.pdf') for n in names} if complete else {},
        originals_sha256={p.name:sha(p) for p in ROOT.parent.glob('*.pdf')})
    out='verification-q07.json' if complete else 'verification-q07-preliminary.json'
    (ROOT/'build'/out).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(verified_math=True,document_complete=complete,
        timed_field_cases=len(arbitrary),optical_ODE_cases=len(optical_odes),family_cases=len(families),
        independent_search_targets=len(roots),numerical_variants=report['numerical_variants']),ensure_ascii=False))
if __name__=='__main__':main()
