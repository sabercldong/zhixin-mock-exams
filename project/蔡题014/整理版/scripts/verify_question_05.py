"""014 Q5: exact planar duality and independent finite-element conduction checks.

Numerical meshes are approximations, never presented as an exact geometric-mean
proof. Nested energy convergence and each measured error are recorded explicitly.
"""
from pathlib import Path
import argparse, hashlib, json
import numpy as np
import sympy as s
from sympy.physics.units import ampere, volt, meter, ohm, convert_to
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

ROOT=Path(__file__).resolve().parents[1]
symbolic=[]; numerical=[]
def zero(name,expr):
    value=s.simplify(expr)
    assert value==0,(name,value)
    symbolic.append(dict(test=name,passed=True))

def fem(n,k1,k2,width=1.,height=1.,pattern='checker'):
    """Solve div(k grad u)=0 with u=0/1 at bottom/top, natural side insulation.

    Continuous P1 elements, interfaces mesh-aligned; current obtained from actual
    assembled boundary reactions, not inferred from the proposed exact formula.
    """
    assert n%2==0 and min(k1,k2,width,height)>0
    xx,yy=np.meshgrid(np.linspace(0,width,n+1),np.linspace(0,height,n+1))
    xy=np.column_stack([xx.ravel(),yy.ravel()])
    node=np.arange((n+1)**2).reshape(n+1,n+1)
    a=node[:-1,:-1].ravel(); b=node[:-1,1:].ravel()
    c=node[1:,1:].ravel(); e=node[1:,:-1].ravel()
    triangles=np.concatenate([np.column_stack([a,b,c]),np.column_stack([a,c,e])])
    p=xy[triangles]
    twice=(p[:,1,0]-p[:,0,0])*(p[:,2,1]-p[:,0,1])-(p[:,2,0]-p[:,0,0])*(p[:,1,1]-p[:,0,1])
    grad=np.stack([np.column_stack([p[:,1,1]-p[:,2,1],p[:,2,0]-p[:,1,0]]),
                   np.column_stack([p[:,2,1]-p[:,0,1],p[:,0,0]-p[:,2,0]]),
                   np.column_stack([p[:,0,1]-p[:,1,1],p[:,1,0]-p[:,0,0]])],axis=1)/twice[:,None,None]
    centers=p.mean(axis=1)
    left=centers[:,0]<width/2; upper=centers[:,1]>height/2
    first=(left==upper) if pattern=='checker' else (upper if pattern=='series' else left)
    k=np.where(first,k1,k2)
    ke=k[:,None,None]*(twice/2)[:,None,None]*np.einsum('tik,tjk->tij',grad,grad)
    rows=np.broadcast_to(triangles[:,:,None],ke.shape).ravel()
    cols=np.broadcast_to(triangles[:,None,:],ke.shape).ravel()
    K=coo_matrix((ke.ravel(),(rows,cols)),shape=(len(xy),len(xy))).tocsr()
    bottom=node[0]; top=node[-1]; fixed=np.concatenate([bottom,top])
    free=np.setdiff1d(np.arange(len(xy)),fixed)
    u=np.zeros(len(xy));u[top]=1.
    u[free]=spsolve(K[free][:,free],-K[free][:,fixed]@u[fixed])
    reaction=K@u
    conductance=float(reaction[top].sum());energy=float(u@reaction)
    imbalance=float(abs(reaction[top].sum()+reaction[bottom].sum()))
    residual=float(np.max(abs(reaction[free])))
    assert conductance>0 and np.min(u)>-1e-10 and np.max(u)<1+1e-10
    assert abs(energy-conductance)/(1+conductance)<2e-9
    assert imbalance/(1+conductance)<2e-9 and residual/(1+max(k1,k2))<2e-10
    return dict(mesh=n,conductance=conductance,resistance=1/conductance,
                energy=energy,relative_balance=imbalance/(1+conductance),
                scaled_interior_residual=residual/(1+max(k1,k2)))

def run(full):
    x,y=s.symbols('x y',real=True)
    k,k1,k2,k0,U,I,W,H,d,sg1,sg2=s.symbols('k k1 k2 k0 U I W H d sg1 sg2',positive=True,real=True)
    Q=s.Matrix([[0,-1],[1,0]])
    zero('quarter turn is norm preserving',(Q.T*Q-s.eye(2)).norm())
    zero('quarter turn squared reverses vectors',(Q*Q+s.eye(2)).norm())
    Ex,Ey=s.symbols('Ex Ey',real=True)
    E=s.Matrix([Ex,Ey]);J=k*E;Estar=Q*J/k0;Jstar=k0*Q*E
    zero('dual Ohm law including dimensions',(Jstar-(k0**2/k)*Estar).norm())
    zero('inverse transform recovers original E',(-Q*Jstar/k0-E).norm())
    zero('inverse transform recovers original J',(-k0*Q*Estar-J).norm())
    jx=s.Function('Jx')(x,y);jy=s.Function('Jy')(x,y)
    ex=s.Function('Ex')(x,y);ey=s.Function('Ey')(x,y)
    zero('dual curl equals original divergence',s.diff(jx/k0,x)-s.diff(-jy/k0,y)-(s.diff(jx,x)+s.diff(jy,y))/k0)
    zero('dual divergence is minus original curl',s.diff(-k0*ey,x)+s.diff(k0*ex,y)+k0*(s.diff(ey,x)-s.diff(ex,y)))
    Et,Jn=s.symbols('Et Jn',real=True)
    zero('interface dual normal current uses continuous tangential E',(Q*s.Matrix([0,Et]))[0]*k0+k0*Et)
    zero('interface dual tangential E uses continuous normal J',(Q*s.Matrix([Jn,0]))[1]/k0-Jn/k0)
    zero('phase one is changed to phase two',(k0**2/k1-k2).subs(k0,s.sqrt(k1*k2)))
    zero('phase two is changed to phase one',(k0**2/k2-k1).subs(k0,s.sqrt(k1*k2)))
    R=U/I;Rs=(I/k0)/(k0*U)
    zero('finite plate dual terminal resistance product',R*Rs-1/k0**2)
    zero('self-dual positive resistance root',s.sqrt(1/(k1*k2))-1/s.sqrt(k1*k2))
    zero('three-dimensional conductivities converted to sheet values',
         (1/s.sqrt(k1*k2)).subs({k1:d*sg1,k2:d*sg2})-1/(d*s.sqrt(sg1*sg2)))
    lower=2/(k1+k2);exact=1/s.sqrt(k1*k2);upper=(k1+k2)/(2*k1*k2)
    zero('lower difference is nonnegative square',exact-lower-(s.sqrt(k1)-s.sqrt(k2))**2/((k1+k2)*s.sqrt(k1*k2)))
    zero('upper difference is nonnegative square',upper-exact-(s.sqrt(k1)-s.sqrt(k2))**2/(2*k1*k2))
    zero('two modified-circuit bounds have geometric-mean exact R',s.sqrt(lower*upper)-exact)
    zero('uniform potential trial energy equals arithmetic conductance',
         (k1+k2)/2*(U/H)**2*W*H-U**2*W/H*(k1+k2)/2)
    zero('uniform current trial energy equals harmonic resistance',
         (1/k1+1/k2)/2*(I/W)**2*W*H-I**2*H/W*(1/k1+1/k2)/2)
    psi=s.Function('psi')(x,y)
    js=s.Matrix([s.diff(psi,y),-s.diff(psi,x)])
    zero('stream gives divergence-free current',s.diff(js[0],x)+s.diff(js[1],y))
    zero('rotated stream current is gradient',(Q*js-s.Matrix([s.diff(psi,x),s.diff(psi,y)])).norm())
    p,q=s.symbols('p q',real=True)
    # Local values establish the correct refraction and interface signs independently.
    E1=s.Matrix([p/k1,q]);E2=s.Matrix([p/k2,q]);J1=k1*E1;J2=k2*E2
    zero('actual normal current is continuous',J1[0]-J2[0])
    zero('actual tangential E is continuous',E1[1]-E2[1])
    zero('refraction tan ratio is conductivity ratio',J2[1]/J2[0]-k2/k1*J1[1]/J1[0])
    eps,sg=s.symbols('eps sg',real=True,positive=True)
    expansion=s.series(1/s.sqrt(1-eps**2),eps,0,6).removeO()
    zero('complete fourth-order weak contrast expansion',expansion-(1+eps**2/2+3*eps**4/8))
    zero('logarithmic sensitivity of phase one',s.diff(exact,k1)*k1/exact+s.Rational(1,2))
    zero('logarithmic sensitivity of phase two',s.diff(exact,k2)*k2/exact+s.Rational(1,2))
    zero('equal phases reproduce a homogeneous square',exact.subs(k2,k1)-1/k1)
    um=s.symbols('um',real=True)
    zero('added middle short has potential U/2',((k1+k2)*(U-um)-(k1+k2)*um).subs(um,U/2))
    rr=s.symbols('rr',positive=True,real=True)
    zero('alternative fixed terminal voltage normalization',(rr*I-U).subs(rr,U/I))
    zero('alternative fixed terminal current normalization',(U/rr-I).subs(rr,U/I))
    alpha=1/(rr**2*k1*k2)
    zero('rotated inverse kappa has same uniform factor in phase one',1/(rr**2*k2)-alpha*k1)
    zero('rotated inverse kappa has same uniform factor in phase two',1/(rr**2*k1)-alpha*k2)
    zero('uniform factor equals one at positive self-dual root',alpha.subs(rr,exact)-1)
    assert s.limit(exact,k2,0,dir='+')==s.oo
    symbolic.append(dict(test='zero conductivity limit is infinite R, not point-contact conduction',passed=True))
    for n in [8,32,128]:
        row=fem(n,2.,2.,width=1.7,height=.9)
        expected=2*1.7/.9
        assert abs(row['conductance']/expected-1)<2e-10
        numerical.append(dict(test='independent homogeneous rectangle FEM',**row,expected_conductance=expected,passed=True))
    # This is an independent PDE computation. Convergence is explicitly bounded,
    # not hidden by replacing the computed current with sqrt(k1*k2).
    for c1,c2 in [(1.,1.),(2.,1.),(4.,1.),(1.,4.),(.3,1.)]:
        sequence=[fem(n,c1,c2) for n in [16,32,64,128,256]]
        target=np.sqrt(c1*c2)
        errors=[row['conductance']/target-1 for row in sequence]
        assert all(e>-2e-9 for e in errors)
        assert all(sequence[j+1]['conductance']<=sequence[j]['conductance']+2e-9 for j in range(len(sequence)-1))
        assert abs(errors[-1])<.025,(c1,c2,errors)
        for row,error in zip(sequence,errors):
            assert 2*c1*c2/(c1+c2)-2e-9<=row['conductance']<=(c1+c2)/2+2e-9
            numerical.append(dict(test='nested continuous FEM square energy convergence',k1=c1,k2=c2,
                                  **row,exact_conductance=target,relative_discretization_error=float(error),
                                  finite_mesh_not_exact=True,passed=True))
    for pattern in ['series','parallel']:
        for a,b in [(1.,4.),(2.,7.),(.3,1.2)]:
            row=fem(32,a,b,pattern=pattern)
            expected=2*a*b/(a+b) if pattern=='series' else (a+b)/2
            assert abs(row['conductance']/expected-1)<2e-10
            numerical.append(dict(test='same phase fractions, independently solved stripe arrangement',pattern=pattern,
                                  **row,expected_conductance=expected,passed=True))
    for aspect in [.5,2.]:
        row=fem(256,2.,1.,width=aspect,height=1.)
        partner=fem(256,2.,1.,width=1/aspect,height=1.)
        product=row['resistance']*partner['resistance']
        error=abs(product*2-1)
        assert error<.025
        numerical.append(dict(test='independent finite-rectangle dual product, measured mesh error',aspect=aspect,
                              first=row,rotated_aspect=partner,product=product,exact_product=.5,
                              relative_discretization_error=error,finite_mesh_not_exact=True,passed=True))
    resistance=1/(.001*np.sqrt(4e6*1e6))
    current=.001/resistance;power=.001*current
    assert abs(resistance-.0005)<1e-15 and abs(current-2.)<1e-14 and abs(power-.002)<1e-15
    numerical.append(dict(test='fully solved numerical variation with SI conversion',resistance_ohm=resistance,
                          current_ampere=current,power_watt=power,passed=True))
    for delta in [.01,.08,.2]:
        direct=1/np.sqrt(1-delta**2);series=1+delta**2/2+3*delta**4/8
        remainder=direct-series
        assert 0<=remainder<=delta**6
        numerical.append(dict(test='weak-contrast fourth-order expansion remainder',epsilon=delta,
                              exact_normalized=direct,series_normalized=series,remainder=remainder,passed=True))
    # Sheet-current units: (A/m)/(S) = V/m and (S)*(V/m)=A/m.
    dimensions=dict(sheet_conductance='S',sheet_current='A/m',field='V/m',stream='A',resistance='ohm')
    symbolic.append(dict(test='consistent SI units including stream potential and dual constants',passed=True,units=dimensions))
    zero('SI module: sheet conductance from thickness times bulk conductivity',meter/(ohm*meter)-1/ohm)
    zero('SI module: scaled current is an electric field',convert_to((ampere/meter)/(1/ohm),volt/meter)-volt/meter)
    zero('SI module: scaled field is a sheet current',convert_to((1/ohm)*(volt/meter),ampere/meter)-ampere/meter)
    zero('SI module: stream divided by sheet conductance is voltage',convert_to(ampere/(1/ohm),volt)-volt)
    figure=ROOT/'figures/题05_图稿源文件.tex';draft=ROOT/'drafts/question-05.md'
    report=dict(paper='014',question='05',scope='math and independent PDE checks only; not actual visual or whole-set acceptance',
                symbolic_count=len(symbolic),numeric_count=len(numerical),symbolic_checks=symbolic,numerical_checks=numerical,
                math_passed=True,question_accepted=False,set_accepted=False,draft_text_complete=full,
                source_sha256={f:hashlib.sha256((ROOT.parent/f).read_bytes()).hexdigest() for f in ['试卷.pdf','答案.pdf']},
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                actual_source_images={f:hashlib.sha256((ROOT/'preview/originals'/f).read_bytes()).hexdigest() for f in
                    ['paper-02.png','answer-06.png','details/q05-paper.png','details/q05-answer-left.png','details/q05-answer-right.png']},
                figure_source_sha256=hashlib.sha256(figure.read_bytes()).hexdigest() if figure.exists() else None,
                draft_sha256=hashlib.sha256(draft.read_bytes()).hexdigest() if draft.exists() else None,
                independent_route='Finite boundary duality proved directly, separately solved continuous FEM mixed-boundary PDE; strict bounds via energy principles.',
                background_source='A. M. Dykhne, JETP 32 (1971), 63–65, primary journal search result: https://jetp.ras.ru/cgi-bin/e/index/e/32/1/p63?a=list ; full PDF access timed out; not used as a finite-boundary proof.')
    dest=ROOT/('verification/question-05-math.json' if full else 'verification/question-05-initial-math.json')
    dest.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(passed=True,symbolic=len(symbolic),numeric=len(numerical),max_mesh_relative_error=max(
          v.get('relative_discretization_error',0) for v in numerical),math_sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),
          question_accepted=False),ensure_ascii=False))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--full',action='store_true');args=parser.parse_args();run(args.full)
