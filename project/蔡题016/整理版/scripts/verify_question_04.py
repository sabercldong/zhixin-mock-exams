"""016 Q4: source integral, signed Newton systems, actual tangent geometry and LP.

Only the release instant has a vertical string. Finite-time checks use the
moving tangency to a fixed table slot, not a falsely permanent a_A=r*beta.
"""
from pathlib import Path
import argparse,hashlib,json,math,subprocess
import numpy as np
import sympy as sp
from scipy.integrate import quad,solve_ivp
from scipy.optimize import linprog

ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def tangent_geometry(x,R,r):
    q=np.array([r-x,-R]);dist=np.linalg.norm(q)
    u=math.atan2(q[1],q[0])+math.acos(r/dist)
    e=np.array([math.cos(u),math.sin(u)])
    straight=math.sqrt(dist*dist-r*r)
    direction=(q-r*e)/straight
    return straight-r*u, -direction[0], direction

def tangent_second(x,R,r):
    step=R*1e-5
    return (tangent_geometry(x+step,R,r)[1]-
            tangent_geometry(x-step,R,r)[1])/(2*step)

def release_matrix(n,m,R,r,g,rolling):
    # Unknown [a_O, beta(clockwise), T, f_B(right), a_A(down), N_B].
    I=m*R*R/2
    A=np.array([[m,0,0,-1,0,0],
       [0,I,-r,R,0,0],[0,0,1,0,n*m,0],
       [0,-r,0,0,1,0],[0,0,-1,0,0,1],
       [1,-R if rolling else 0,0,0,0,0]],float)
    b=np.array([0,0,n*m*g,0,m*g,0],float)
    sol=np.linalg.solve(A,b)
    assert np.linalg.norm(A@sol-b)<1e-10
    return sol

def static_lp(n,k,rho,ell,muB,muD,muC=None):
    # m=g=R=1; unknown T,N_B,f_B,P,f_D,N_D,M_D,q_C.
    # q_C upward on spool, f_D signed right; M_D=N_D*x_D.
    Aeq=np.array([[1,0,0,0,0,0,0,0],
       [0,0,1,-1,0,0,0,0],[0,1,0,0,0,0,0,1],
       [-rho,0,1,0,0,0,0,1],[0,0,0,1,1,0,0,0],
       [0,0,0,0,0,1,0,-1],[0,0,0,-1,0,0,1,0]],float)
    beq=np.array([n,0,1+n,0,0,k,k*ell/2],float)
    Aub=[[0,-muB,1,0,0,0,0,0],[0,-muB,-1,0,0,0,0,0],
         [0,0,0,0,1,-muD,0,0],[0,0,0,0,-1,-muD,0,0],
         [0,0,0,0,0,-ell,1,0]]
    bounds=[(0,None),(0,None),(None,None),(0,None),
            (None,None),(0,None),(0,None),(0,0)]
    if muC is not None:
        bounds[-1]=(None,None)
        Aub.extend([[0,0,0,-muC,0,0,0,1],[0,0,0,-muC,0,0,0,-1]])
    return linprog(np.zeros(8),A_ub=np.array(Aub),b_ub=np.zeros(len(Aub)),
                   A_eq=Aeq,b_eq=beq,bounds=bounds,method='highs')

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--complete',action='store_true')
    args=parser.parse_args()
    m,R,r,n,g,s=sp.symbols('m R r n g s',positive=True)
    mass=sp.integrate(2*m*s/R**2,(s,0,R))
    I=sp.integrate(2*m*s**3/R**2,(s,0,R))
    assert sp.simplify(mass-m)==0
    assert sp.simplify(I-m*R**2/2)==0
    D=3*R**2+2*n*r**2
    a2=2*n*r**2*g/D;ao2=2*n*R*r*g/D
    T=3*n*R**2*m*g/D;f=2*n*R*r*m*g/D
    NB=m*g+T
    assert sp.simplify(n*m*g-T-n*m*a2)==0
    assert sp.simplify(I*a2/r-(T*r-f*R))==0
    assert sp.simplify((I+m*R**2)*a2/r-T*r)==0
    assert sp.simplify(f/NB-2*n*R*r/(3*(n+1)*R**2+2*n*r**2))==0
    source_integrals=[];release=[];motions=[]
    for mv,Rv in [(.4,.06),(1.2,.1),(2.3,.25)]:
        rho=mv/(math.pi*Rv**2)
        massnum=quad(lambda t:2*math.pi*rho*t,0,Rv)[0]
        inertia=quad(lambda t:2*math.pi*rho*t**3,0,Rv)[0]
        assert abs(massnum-mv)<1e-12 and abs(inertia-mv*Rv**2/2)<1e-12
        source_integrals.append(dict(m=mv,R=Rv,mass_integral=massnum,I_integral=inertia))
    for nv in [.2,1,4]:
        for ratio in [.2,.5,.8]:
            mv,Rv,gv=1.2,.1,9.8;rv=ratio*Rv
            for rolling in [False,True]:
                sol=release_matrix(nv,mv,Rv,rv,gv,rolling)
                denom=(3 if rolling else 1)*Rv**2+2*nv*rv**2
                expectedA=2*nv*rv**2*gv/denom
                assert abs(sol[4]-expectedA)<1e-11
                assert sol[2]>0 and sol[5]>0
                if rolling:
                    assert sol[3]>0 and abs(sol[0]-Rv/rv*sol[4])<1e-11
                    assert abs(sol[3]/sol[5]-2*nv*ratio/(3*(nv+1)+2*nv*ratio**2))<1e-12
                else:assert abs(sol[0])+abs(sol[3])<1e-12
                # Initial tangent line genuinely at x=r, not x=R.
                ell,Lx,td=tangent_geometry(0,Rv,rv)
                assert abs(ell-Rv)<1e-14 and abs(Lx)<1e-14
                assert np.linalg.norm(td-np.array([0,-1]))<1e-14
                assert abs(tangent_second(0,Rv,rv)-1/Rv)<1e-7/Rv
                release.append(dict(n=nv,r_over_R=ratio,rolling=rolling,
                    a_O=sol[0],beta=sol[1],T=sol[2],f_B=sol[3],a_A=sol[4],
                    N_B=sol[5],mu_required=sol[3]/sol[5],
                    exact_tangent_initial_Lx=Lx))
                Iv=mv*Rv*Rv/2;M=nv*mv
                if rolling:
                    def ode(t,y):
                        phi,w=y;x=Rv*phi
                        _,lx,_=tangent_geometry(x,Rv,rv)
                        lxx=tangent_second(x,Rv,rv)
                        qp=rv-Rv*lx;qpp=-Rv**2*lxx
                        beta=M*(gv-qpp*w*w)*qp/(Iv+mv*Rv**2+M*qp**2)
                        return [w,beta]
                    result=solve_ivp(ode,[0,1e-4],[0,0],rtol=2e-10,atol=1e-13)
                    phi,w=result.y[:,-1];x=Rv*phi
                    ell1,lx,_=tangent_geometry(x,Rv,rv)
                    yp=rv-Rv*lx;yy=rv*phi-(ell1-Rv)
                    energy=.5*(Iv+mv*Rv**2)*w*w+.5*M*(yp*w)**2-M*gv*yy
                    computed_acc=2*yy/1e-8
                else:
                    def ode(t,y):
                        x,phi,v,w=y;_,lx,_=tangent_geometry(x,Rv,rv)
                        lxx=tangent_second(x,Rv,rv)
                        tension=M*(gv+lxx*v*v)/(1+M*rv*rv/Iv+M*lx*lx/mv)
                        return [v,w,-tension*lx/mv,rv*tension/Iv]
                    result=solve_ivp(ode,[0,1e-4],[0,0,0,0],rtol=2e-10,atol=1e-13)
                    x,phi,v,w=result.y[:,-1];ell1,lx,_=tangent_geometry(x,Rv,rv)
                    yy=rv*phi-(ell1-Rv);vy=rv*w-lx*v
                    energy=.5*mv*v*v+.5*Iv*w*w+.5*M*vy*vy-M*gv*yy
                    computed_acc=2*yy/1e-8
                assert result.success and abs(energy)<2e-12
                assert abs(computed_acc/sol[4]-1)<5e-6
                motions.append(dict(n=nv,r_over_R=ratio,rolling=rolling,
                    actual_tangent_constraint_initial_acceleration=computed_acc,
                    energy_residual=energy,interval_seconds=1e-4))
    statics=[];impossible=[]
    for nv in [.3,1,3]:
        for ratio in [.2,.5,.8]:
            for kv in [.8,2]:
                bmin=nv*ratio/(1+nv);dmin=nv*ratio/kv;lmin=2*nv*ratio/kv
                for factors in [(1.1,1.1,1.1),(1,1,1),(.9,1.1,1.1),
                                (1.1,.9,1.1),(1.1,1.1,.9)]:
                    muB,muD,ell=bmin*factors[0],dmin*factors[1],lmin*factors[2]
                    res=static_lp(nv,kv,ratio,ell,muB,muD)
                    expected=all(t>=1 for t in factors)
                    assert res.success==expected,(nv,kv,ratio,factors,res.message)
                    statics.append(dict(n=nv,k=kv,r_over_R=ratio,mu_B=muB,
                        mu_D=muD,l_over_R=ell,LP_feasible=bool(res.success)))
                for muc in [.1,1,1e4]:
                    res=static_lp(nv,kv,ratio,100,0,1e4,muC=muc)
                    assert not res.success
                    impossible.append(dict(n=nv,k=kv,r_over_R=ratio,mu_C=muc,
                        LP_feasible=False,smooth_floor_no_static_equilibrium=True))
    variant1={}
    for rolling in [False,True]:
        val=release_matrix(1,.4,.06,.02,9.8,rolling)
        variant1['rolling' if rolling else 'smooth']=dict(
            zip(['a_O','beta','T','f_B','a_A','N_B'],val.tolist()),
            mu_required=val[3]/val[5])
    var2=static_lp(3,2,.4,1.4,.31,.61)
    assert var2.success
    assert not static_lp(3,2,.4,1.4,.31,.55).success
    nmax=18/19
    assert abs(release_matrix(nmax,1,1,.5,1,True)[3]/
               release_matrix(nmax,1,1,.5,1,True)[5]-.15)<1e-12
    assert release_matrix(1,1,1,.5,1,True)[3]/release_matrix(1,1,1,.5,1,True)[5]>.15
    static_bound=5/3
    assert static_lp(static_bound,2,.4,1.2,.25,.5).success
    assert not static_lp(static_bound+1e-3,2,.4,1.2,.25,.5).success
    sources={'scripts/verify_question_04.py':sha(Path(__file__))}
    figures={}
    if args.complete:
        subprocess.run(['python3',str(ROOT/'scripts/check_projected_question_04.py')],check=True)
        geometry_path=ROOT/'build/projected-geometry-q04.json'
        geometry=json.loads(geometry_path.read_text());assert geometry['passed']
        sources['scripts/check_projected_question_04.py']=sha(ROOT/'scripts/check_projected_question_04.py')
        sources['build/projected-geometry-q04.json']=sha(geometry_path)
        source=ROOT/'drafts/question-04.md';text=source.read_text()
        assert '<!-- question-complete -->' in text and text.count('\n## ')==9
        for name in ['question-04','inertia-04','motion-04','forces-04','contact-04','block-04']:
            file=ROOT/f'figures/{name}.pdf';assert file.exists();figures[name]=sha(file)
        sources['drafts/question-04.md']=sha(source)
        sources['figures/题04_图稿源文件.tex']=sha(ROOT/'figures/题04_图稿源文件.tex')
    result=dict(question=4,verified_math=True,document_complete=args.complete,set_accepted=False,
        scope='release-instant Newton equations; finite-time moving tangency checked separately',
        mass_and_inertia_source_integrals=source_integrals,
        signed_Newton_release_systems=release,actual_tangent_ODE_checks=motions,
        static_contact_LP_checks=statics,smooth_B_impossibility_LP_checks=impossible,
        solved_variants=dict(numerical_release=variant1,
            static_numeric=dict(LP_solution=var2.x.tolist(),
                mu_B_min=.3,mu_D_min=.6,l_min_metres=.06,
                given_mu_D_point55_fails=True),
            rolling_mass_ratio_limit=nmax,static_mass_ratio_limit=static_bound),
        source_sha256=sources,figures_sha256=figures,
        originals_sha256={name:sha(ROOT.parent/name) for name in ['试卷.pdf','答案.pdf']})
    path=ROOT/('build/verification-q04.json' if args.complete else 'build/verification-q04-preliminary.json')
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(question=4,verified_math=True,document_complete=args.complete,
        release_systems=len(release),actual_geometry_ODEs=len(motions),
        static_LPs=len(statics),impossibility_LPs=len(impossible),variants=result['solved_variants']),ensure_ascii=False))
if __name__=='__main__':main()
