"""014 Q6: genuine Coulomb Taylor, force integration and full-chain Fourier checks.

This is pre-writing evidence until source, figure and current PDF review are also
complete. No draft or whole-paper acceptance is inferred from a successful run.
"""
from pathlib import Path
import argparse,hashlib,json
import numpy as np
import sympy as s
import mpmath as mp
from scipy.integrate import solve_ivp,quad
ROOT=Path(__file__).resolve().parents[1]
symbolic=[];numerical=[]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def zero(name,expression):
    value=s.simplify(expression)
    assert value==0,(name,value)
    symbolic.append(dict(test=name,passed=True))
def note(name,**values):
    numerical.append(dict(test=name,passed=True,**values))
def energy(y,lam):
    charges=[1.,-lam,1.]
    return sum(charges[i]*charges[j]/np.sqrt((j-i)**2+(y[j]-y[i])**2)
               for i in range(3) for j in range(i+1,3))
def force(y,lam):
    charges=[1.,-lam,1.];f=np.zeros(3)
    for i in range(3):
        for j in range(i+1,3):
            value=charges[i]*charges[j]*(y[i]-y[j])/((j-i)**2+(y[j]-y[i])**2)**1.5
            f[i]+=value;f[j]-=value
    return f
def stiffness(lam):
    return np.array([[lam-.125,-lam,.125],[-lam,2*lam,-lam],[.125,-lam,lam-.125]])
def run(full=False):
    y1,y2,y3,lam,c,m,M,ell,a,b,Y,kt=s.symbols('y1 y2 y3 lam c m M ell a b Y kt',real=True)
    ys=s.Matrix([y1,y2,y3]);L=s.Matrix([[1,-1,0],[-1,2,-1],[0,-1,1]])
    P=s.Matrix([[1,0,-1],[0,0,0],[-1,0,1]])
    B=lam*L-P/8
    U2=c*(lam*((y2-y1)**2+(y3-y2)**2)/2-(y3-y1)**2/16)
    zero('full three-coordinate potential Hessian',(s.hessian(U2,(y1,y2,y3))-c*B).norm())
    z,h=s.symbols('z h',real=True,positive=True)
    zero('pair Taylor includes distance cubed',s.series(1/s.sqrt(h*h+z*z),z,0,4).removeO()-1/h+z*z/(2*h**3))
    for i in range(3):
        zero('translation leaves row sum zero '+str(i),sum(B[i,j] for j in range(3)))
    vectors=[s.Matrix([1,1,1])/s.sqrt(3),s.Matrix([1,0,-1])/s.sqrt(2),
             s.Matrix([1,-2,1])/s.sqrt(6)]
    eigen=[0,lam-s.Rational(1,4),3*lam]
    Q=s.Matrix.hstack(*vectors)
    zero('orthonormal physical normal modes',(Q.T*Q-s.eye(3)).norm())
    for i in range(3):
        zero('actual Hessian eigenvector '+str(i),(B*vectors[i]-eigen[i]*vectors[i]).norm())
    zero('normal mode potential diagonal',(Q.T*B*Q-s.diag(*eigen)).norm())
    v0,va,vs=s.symbols('v0 va vs',real=True)
    zero('kinetic energy normal coordinates',(Q*s.Matrix([v0,va,vs])).dot(Q*s.Matrix([v0,va,vs]))-(v0*v0+va*va+vs*vs))
    hand={y1:(a+b)/s.sqrt(2),y2:-s.sqrt(2)*b,y3:(-a+b)/s.sqrt(2)}
    zero('hand constrained potential includes common c/2',U2.subs(hand)-c*((lam-s.Rational(1,4))*a*a+9*lam*b*b)/2)
    zero('hand kinetic metric is not identity',sum(t*t for t in hand.values())-a*a-3*b*b)
    zero('symmetric physical frequency uses mass 3m',(9*c*lam)/(3*m)-3*c*lam/m)
    cm={y1:Y+(a+b)/s.sqrt(2),y2:Y-s.sqrt(2)*b,y3:Y+(-a+b)/s.sqrt(2)}
    zero('hand variables plus full CM energy',U2.subs(cm)-c*((lam-s.Rational(1,4))*a*a+9*lam*b*b)/2)
    zero('full CM kinetic coefficient is 3m',sum(t*t for t in cm.values())-3*Y*Y-a*a-3*b*b)
    zero('potential independent of COM',s.diff(U2.subs(cm),Y))
    t=s.symbols('t',real=True)
    # Exact forces are differentiated before the small-displacement truncation.
    exact=sum(([1,-lam,1][i]*[1,-lam,1][j])/
              s.sqrt((j-i)**2*ell**2+(ys[j]-ys[i])**2)
              for i in range(3) for j in range(i+1,3))
    for i in range(3):
        for j in range(3):
            val=s.diff(exact,ys[i],ys[j]).subs({y1:0,y2:0,y3:0})
            # ell positive is explicit in the physical distance.
            val=val.subs(s.Abs(ell),ell)
            zero('direct exact Coulomb Hessian '+str(i)+str(j),
                 val-B[i,j]/ell**3)
    ellp=s.symbols('ellp',positive=True)
    line=exact.subs({ell:ellp,y1:a,y2:0,y3:-a,lam:s.Rational(1,4)})
    zero('critical antisymmetric family exact zero energy',line)
    for i in range(3):
        zero('critical family exact force zero '+str(i),
             s.diff(exact,ys[i]).subs({ell:ellp,y1:a,y2:0,y3:-a,lam:s.Rational(1,4)}))
    delta=s.symbols('delta',positive=True)
    anti_force=-s.diff(exact,y1).subs({ell:ellp,y1:a,y2:0,y3:-a,lam:s.Rational(1,4)+delta})
    zero('exact antisymmetric restoring force above critical',anti_force+delta*a/(ellp**2+a**2)**s.Rational(3,2))
    anti_energy=exact.subs({ell:ellp,y1:a,y2:0,y3:-a,lam:s.Rational(1,4)+delta})
    zero('exact two-particle effective energy force factor',-s.diff(anti_energy,a)/2-anti_force)
    zero('cubic relative correction independent of softening parameter',
         s.series((1+a*a/ellp**2)**(-s.Rational(3,2)),a,0,4).removeO()-1+3*a*a/(2*ellp**2))
    z,ph=s.symbols('z ph',real=True)
    sa=s.sqrt(1+z*z);sp=s.sqrt(1+z*z*s.sin(ph)**2)
    zero('rationalized endpoint-free period integrand',
         1/sp-1/sa-z*z*s.cos(ph)**2/((sa+sp)*sa*sp))
    zero('period integrand amplitude expansion',
         s.series(s.sqrt((sa+sp)*sa*sp),z,0,4).removeO()-s.sqrt(2)*(1+3*z*z*(1+s.sin(ph)**2)/8))
    zero('integrated nonlinear period correction nine sixteenths',
         s.integrate(3*(1+s.sin(ph)**2)/8,(ph,0,s.pi/2))*2/s.pi-s.Rational(9,16))
    mass=s.diag(m,M,m);r=s.Matrix([1,-2*m/M,1])
    omega=c*lam*(1/m+2/M)
    zero('unequal middle mass exact symmetric mode',(c*B*r-mass*r*omega).norm())
    zero('unequal middle mass exact antisymmetric mode',(c*B*vectors[1]-mass*vectors[1]*c*(lam-s.Rational(1,4))/m).norm())
    for i in range(3):
        zero('common trap shifts physical eigenvalue '+str(i),
             ((c*B+kt*s.eye(3))*vectors[i]-(c*eigen[i]+kt)*vectors[i]).norm())
    S,G,C=s.symbols('S G C',real=True)
    chain=s.Matrix([[lam*S-G,-lam*C],[-lam*C,lam*S-lam*lam*G]])
    zero('infinite chain Hermitian two-site determinant',
         chain.det()-(lam*lam*(S*S-C*C)-lam*S*(1+lam*lam)*G+lam*lam*G*G))
    zero('infinite chain translational zero at theta 0',(chain.subs({G:0,C:S})*s.Matrix([1,1])).norm())
    qbar=(1-lam)/2;qalt=(1+lam)/2
    zero('even separation average charge product',(1+lam*lam)/2-(qbar*qbar+qalt*qalt))
    zero('odd separation average charge product',-lam-(qbar*qbar-qalt*qalt))
    rng=np.random.default_rng(1406)
    for lamv in [-.5,0.,.1,.25,.3,1.,2.]:
        y=rng.normal(size=3);base=energy(np.zeros(3),lamv)
        coefficient=float(y@stiffness(lamv)@y/2)
        errors=[]
        for eps in [.02,.01,.005]:
            remainder=energy(eps*y,lamv)-base-eps**2*coefficient
            errors.append(abs(remainder))
        assert errors[-1]<errors[0]/120+1e-14
        note('direct pair-energy fourth-order Taylor remainder',lam=lamv,
             amplitudes=[.02,.01,.005],absolute_remainders=errors)
        # Central difference exact forces, not the already derived Hessian.
        step=1e-5;J=np.column_stack([(force(np.eye(3)[j]*step,lamv)-force(-np.eye(3)[j]*step,lamv))/(2*step) for j in range(3)])
        err=float(np.max(abs(J+stiffness(lamv))))
        assert err<1e-8
        note('independent finite difference of actual Coulomb forces',lam=lamv,max_absolute_error=err)
        shift=3.7
        assert abs(energy(y+shift,lamv)-energy(y,lamv))<1e-13
        assert np.max(abs(force(y+shift,lamv)-force(y,lamv)))<1e-13
        note('exact global translation invariance',lam=lamv)
    for lamv in [.26,.5,1.,2.]:
        for vector,freq2 in [(np.array([1.,0.,-1.])/np.sqrt(2),lamv-.25),
                             (np.array([1.,-2.,1.])/np.sqrt(6),3*lamv)]:
            amplitude=1e-5;w=np.sqrt(freq2);duration=6*np.pi/w
            def ode(t,state):
                return np.r_[state[3:],force(state[:3],lamv)]
            times=np.linspace(0,duration,301)
            sol=solve_ivp(ode,(0,duration),np.r_[amplitude*vector,[0.,0.,0.]],
                          t_eval=times,rtol=2e-11,atol=2e-15)
            assert sol.success
            predicted=amplitude*vector[:,None]*np.cos(w*times)
            err=float(np.max(abs(sol.y[:3]-predicted))/amplitude)
            cmerr=float(np.max(abs(sol.y[:3].sum(axis=0))))
            energies=np.array([energy(sol.y[:3,j],lamv)+np.dot(sol.y[3:,j],sol.y[3:,j])/2 for j in range(len(times))])
            eerr=float(np.max(abs(energies-energies[0])))
            assert err<3e-6 and cmerr<1e-12 and eerr<1e-12
            note('actual nonlinear Coulomb trajectory vs linear normal mode',lam=lamv,
                 frequency_squared=float(freq2),relative_amplitude_error=err,
                 COM_error=cmerr,absolute_energy_drift=eerr)
    for av in [-3.,-.5,0.,.5,3.]:
        y=np.array([av,0.,-av])
        assert np.max(abs(force(y,.25)))<1e-14 and abs(energy(y,.25))<1e-14
        note('exact critical free-tilt family, not harmonic guess',tilt=av)
    for lamv in [0.,.1,.25,1.]:
        H=stiffness(lamv);e=np.linalg.eigvalsh(H)
        expected=np.sort([0.,lamv-.25,3*lamv])
        assert np.max(abs(e-expected))<1e-13
        note('direct matrix eigenvalues and instability signs',lam=lamv,eigenvalues=e.tolist())
    for middlev in [.3,1.,3.]:
        for lamv in [.3,1.]:
            D=np.diag([1.,1/np.sqrt(middlev),1.])
            evals=np.linalg.eigvalsh(D@stiffness(lamv)@D)
            expected=np.sort([0.,lamv-.25,lamv*(1+2/middlev)])
            assert np.max(abs(evals-expected))<1e-12
            note('independent generalized mass eigenproblem',middle_mass=middlev,lam=lamv,eigenvalues=evals.tolist())
    for lamv,trap in [(.1,.2),(.25,.1),(1.,.4)]:
        eig=np.linalg.eigvalsh(stiffness(lamv)+trap*np.eye(3))
        expected=np.sort([trap,trap+lamv-.25,trap+3*lamv])
        assert np.max(abs(eig-expected))<1e-13
        note('actual external confinement shifts all modes',lam=lamv,trap=trap,eigenvalues=eig.tolist())
    kval=9e9;q=1e-6;lv=.1;mv=.01;cv=kval*q*q/lv**3
    assert abs(cv-9.)<1e-12
    wa=np.sqrt(cv*(.5-.25)/mv);ws=np.sqrt(cv*3*.5/mv)
    assert abs(wa-15)<1e-12 and abs(ws-30*np.sqrt(1.5))<1e-12
    note('fully evaluated SI variant frequencies',stiffness_N_per_m=cv,
         omega_a=wa,omega_s=ws,period_a=2*np.pi/wa,period_s=2*np.pi/ws)
    for amplitude in [.01,.1,.3]:
        sA=np.sqrt(1+amplitude**2)
        ratio=quad(lambda phi:np.sqrt((sA+np.sqrt(1+amplitude**2*np.sin(phi)**2))*sA*np.sqrt(1+amplitude**2*np.sin(phi)**2)),0,np.pi/2,
                   epsabs=1e-12,epsrel=1e-12)[0]*np.sqrt(2)/np.pi
        for dv in [.0001,.02,.5]:
            def crossing(time,state):return state[0]
            crossing.terminal=True;crossing.direction=-1
            def exact_period_ode(time,state):return np.r_[state[3:],force(state[:3],.25+dv)]
            sol=solve_ivp(exact_period_ode,(0,2*np.pi/np.sqrt(dv)*ratio),
                          [amplitude,0.,-amplitude,0.,0.,0.],events=crossing,
                          rtol=2e-11,atol=2e-13)
            assert sol.success and len(sol.t_events[0])==1
            period=4*sol.t_events[0][0]
            measured=period*np.sqrt(dv)/(2*np.pi)
            err=abs(measured-ratio)
            assert err<3e-9
            correction_error=abs(ratio-1-s.Rational(9,16)*amplitude**2)
            assert float(correction_error)<.2*amplitude**4
            note('genuine three-charge trajectory vs nonlinear energy period',
                 amplitude_over_l=amplitude,delta=dv,period=period,
                 quadrature_period_over_linear=ratio,ODE_period_over_linear=measured,
                 relative_period_error=err,second_order_truncation_error=float(correction_error))
    # Full alternating chain: cross-check Bloch energy against actual pairs on
    # long finite cells. Tail error is bounded by 1/r^3 and explicitly retained.
    cutoff=12000;rr=np.arange(1,cutoff+1,dtype=float)
    odd=2*np.arange(cutoff,dtype=float)+1
    for theta in [.15,.9,2.5,np.pi]:
        Gv=np.sum((1-np.cos(theta*rr))/rr**3)/4
        Cv=2*np.sum(np.cos(theta*odd/2)/odd**3)
        Sv=2*np.sum(1/odd**3)
        for lamv in [.5,1.,2.]:
            mat=np.array([[lamv*Sv-Gv,-lamv*Cv],[-lamv*Cv,lamv*Sv-lamv**2*Gv]])
            v=np.array([.7+.2j,-.3+.6j]);k=theta/2
            # Real pair contributions in gauge y_A=A exp(i n theta),
            # y_B=B exp(i(n+1/2)theta); energy per cell coefficient.
            a0,b0=v
            sameA=-np.sum(abs(a0*(1-np.exp(1j*rr*theta)))**2/(2*rr)**3)
            sameB=-lamv**2*np.sum(abs(b0*(1-np.exp(1j*rr*theta)))**2/(2*rr)**3)
            cross=lamv*np.sum((abs(a0-b0*np.exp(1j*k*odd))**2+
                              abs(a0-b0*np.exp(-1j*k*odd))**2)/odd**3)
            direct=float((sameA+sameB+cross).real)
            matrix=float((np.conj(v)@mat@v).real)
            err=abs(direct-matrix)
            assert err<2e-12
            note('full interaction Bloch matrix vs actual pair energy',theta=theta,lam=lamv,
                 cutoff=cutoff,pair_matrix_error=err,
                 estimated_absolute_kernel_tail_bound=4/cutoff**2)
    # Equal alternating chain H(k)>0: integrate exact logarithmic second
    # derivative and compare independently with the convergent charge sum.
    for k in [.03,.4,1.2,2.2,3.0,np.pi]:
        kernel=float(np.sum((-1.)**(rr+1)*(1-np.cos(rr*k))/rr**3))
        val=quad(lambda u:(k-u)*np.log(2*np.cos(u/2)),0,k,
                 epsabs=2e-12,epsrel=2e-12)[0]
        err=abs(kernel-val)
        # At k=pi all odd terms have the same sign, so the actual tail is
        # O(1/N^2), not an alternating-tail O(1/N^3). Compare with the stated
        # conservative absolute bound, retaining the measured truncation error.
        assert val>0 and err<2/cutoff**2+3e-12,(k,val,kernel,err)
        note('equal-charge full-chain dispersion from exact log integral',wave_number=k,
             H=val,independent_series_error=err,tail_bound=2/cutoff**2)
    # Non-neutral cell: use scaled exact logarithmic integrals at small k.
    # Even near lambda=1 the true negative long-wave trial energy is resolved
    # with high precision, not erased by a finite interaction cutoff.
    mp.mp.dps=100
    for lamstr in ['0.2','0.5','0.8','1.2','2','5']:
        lv=mp.mpf(lamstr);A=(1-lv)**2/4;Bq=(1+lv)**2/4
        logscale=12+(Bq/A)*mp.log(2);kv=mp.exp(-logscale)
        fscaled=mp.quad(lambda zz:(1-zz)*(-mp.log(2*mp.sin(kv*zz/2))),[0,1])
        hscaled=mp.quad(lambda zz:(1-zz)*mp.log(2*mp.cos(kv*zz/2)),[0,1])
        rayleigh=-2*A*fscaled+2*Bq*hscaled
        assert rayleigh<0
        note('non-neutral infinite cell negative long-wave trial, full interactions',
             lam=lamstr,k=str(kv),energy_divided_by_k_squared=str(rayleigh),
             F_divided_by_k_squared=str(fscaled),H_divided_by_k_squared=str(hscaled),
             precision_decimal_digits=100)
    readings=[]
    for name in ['paper-02','answer-07']:
        path=ROOT/f'preview/originals/{name}.png'
        readings.append(dict(path=str(path.relative_to(ROOT)),sha256=sha(path),actual_displayed_and_read=True))
    for name in ['q06-paper','q06-answer-left']:
        path=ROOT/f'preview/originals/details/{name}.png'
        readings.append(dict(path=str(path.relative_to(ROOT)),sha256=sha(path),actual_displayed_and_read=True))
    report=dict(paper='014',question='06',phase='independent physical checks before actual work-PDF acceptance',
                math_passed=True,question_accepted=False,set_accepted=False,
                symbolic_count=len(symbolic),numeric_count=len(numerical),
                symbolic=symbolic,numerical=numerical,actual_original_readings=readings,
                source_sha256={n:sha(ROOT.parent/n) for n in ['试卷.pdf','答案.pdf']},
                script_sha256=sha(Path(__file__)),
                caveats=['Stability is internal relative stability after removing free COM translation.',
                         'Hand alpha,beta quadratic coefficients need c/2 and kinetic metric diag(m,3m).',
                         'Infinite-chain optional has no handwritten solution; independent derivation.',
                         'This program does not accept the draft, figures or current work PDFs.'])
    if (ROOT/'drafts/question-06.md').exists():report['draft_sha256']=sha(ROOT/'drafts/question-06.md')
    if full:
        report['figure_source_sha256']=sha(ROOT/'figures/题06_图稿源文件.tex')
        report['working_pdf_checks']=json.loads((ROOT/'preview/working-draft-check-q06.json').read_text())
    output='question-06-math.json' if full else 'question-06-initial-math.json'
    (ROOT/'verification'/output).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(passed=True,symbolic=len(symbolic),numeric=len(numerical),question_accepted=False),ensure_ascii=False))
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--full',action='store_true')
    run(parser.parse_args().full)
