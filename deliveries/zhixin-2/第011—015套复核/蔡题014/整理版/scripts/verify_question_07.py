"""014 Q7: Fermat/Snell branch, aperture and genuine moving-ray event checks."""
from pathlib import Path
import argparse,hashlib,json
import numpy as np
import sympy as s
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[1]
symbolic=[];numerical=[]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def zero(name,expr):
    value=s.simplify(expr)
    assert value==0,(name,value)
    symbolic.append(dict(test=name,passed=True))
def note(name,**values):numerical.append(dict(test=name,passed=True,**values))
def surface(y,f=1.,n=2.):
    return (-n*f-np.sqrt(f*f+(n+1)/(n-1)*y*y))/(n+1)
def run(full=False):
    X,Y,f,n=s.symbols('X Y f n',real=True)
    r=s.symbols('r',positive=True)
    fpos=s.symbols('fpos',positive=True)
    # Algebra is checked without silently replacing a squared root by both signs.
    zero('n2 exact unsquared path expansion',(2*X+f)**2-X*X-Y*Y-(3*X*X+4*f*X+f*f-Y*Y))
    zero('hand hyperbola complete square',
         9*(X+2*f/3)**2-3*Y*Y-f*f-3*(3*X*X+4*f*X+f*f-Y*Y))
    curve=(-2*fpos-s.sqrt(fpos*fpos+3*Y*Y))/3
    zero('physical left branch satisfies squared conic',3*curve**2+4*fpos*curve+fpos**2-Y*Y)
    rhs=-fpos-2*curve
    zero('positive optical distance squared equals geometric distance',rhs**2-curve**2-Y*Y)
    zero('vertex focal distance',curve.subs(Y,0)+fpos)
    zero('exact nonparaxial surface derivative',s.diff(curve,Y)+Y/s.sqrt(fpos**2+3*Y**2))
    zero('paraxial curvature magnitude f',s.diff(curve,Y,2).subs(Y,0)+1/fpos)
    zero('surface sag expansion through quartic',
         s.series(curve,Y,0,6).removeO()+fpos+Y*Y/(2*fpos)-3*Y**4/(8*fpos**3))
    general=(n*n-1)*X*X+2*n*(n-1)*f*X+(n-1)**2*f*f-Y*Y
    zero('general index conic without small-angle approximation',
         (n*X+(n-1)*f)**2-X*X-Y*Y-general)
    zero('general hyperbola centers and axes',
         (n*n-1)*(X+n*f/(n+1))**2-Y*Y-(n-1)*f*f/(n+1)-general)
    general_root=s.sqrt(f*f+(n+1)*Y*Y/(n-1))
    general_curve=-(n*f+general_root)/(n+1)
    general_distance=-(n-1)*f-n*general_curve
    zero('general index derivative keeps correct optical weight',s.diff(general_curve,Y)+Y/((n-1)*general_root))
    zero('general weighted normal denominator',n*general_distance+general_curve-(n-1)*general_root)
    zero('general incidence normalization gives exact critical bound denominator',(n-1)**2*general_root**2+Y**2-((n-1)**2*f*f+n*n*Y*Y))
    # Vector Snell law: tangent dot (n1 incoming - n2 outgoing) must vanish.
    tangent=s.Matrix([-Y/(2*r+X),1])
    incoming=s.Matrix([1,0]);outgoing=s.Matrix([-X/r,-Y/r])
    zero('tangent Fermat equation implies exact vector Snell',
         (2*incoming-outgoing).dot(tangent))
    x,y,t,beta,c=s.symbols('x y t beta c',real=True)
    gamma=s.symbols('gamma',positive=True)
    rest_conic=(X+2*f/3)**2/(f*f/9)-Y*Y/(f*f/3)-1
    transformed=rest_conic.subs({X:gamma*(x-beta*c*t),Y:y})
    zero('Lorentz simultaneity gives moving spatial slice',
         transformed-((x-beta*c*t+2*f/(3*gamma))**2/(f*f/(9*gamma**2))-y*y/(f*f/3)-1))
    zero('beta .8 gamma five thirds',1-s.Rational(4,5)**2-s.Rational(3,5)**2)
    zero('hand moving curve coefficients',
         transformed.subs({beta:s.Rational(4,5),gamma:s.Rational(5,3)})-
         ((x-s.Rational(4,5)*c*t+2*f/5)**2/(f*f/25)-y*y/(f*f/3)-1))
    zero('moving vertex instantaneous focal separation',(-f)/gamma+f/gamma)
    ux,uy=s.symbols('ux uy',real=True)
    boostx=(ux+beta*c)/(1+beta*ux/c)
    boosty=uy/(gamma*(1+beta*ux/c))
    # Substitute the null relation after multiplying out the denominators.
    null=s.factor((boostx**2+boosty**2-c*c)*(1+beta*ux/c)**2)
    zero('velocity boost preserves vacuum speed',
         s.expand(null.subs(uy*uy,c*c-ux*ux)).subs(gamma**(-2),1-beta*beta))
    tau=gamma*(r-beta*X)/c
    outx=(-X/r+beta)*c/(1-beta*X/r)
    outy=-Y*c/(gamma*(r-beta*X))
    zero('actual moving ray hits focus worldline horizontally',
         (X/gamma+outx*tau-beta*c*tau).subs(gamma**(-2),1-beta*beta))
    zero('actual moving ray hits axis at same event',Y+outy*tau)
    zero('moving incident speed thirteen fourteenths',
         ((s.Rational(1,2)+s.Rational(4,5))/(1+s.Rational(1,2)*s.Rational(4,5)))-s.Rational(13,14))
    zero('incident beam catches moving surface',s.Rational(13,14)-s.Rational(4,5)-s.Rational(9,70))
    zero('central future focus event time',s.Rational(5,3)*(1+s.Rational(4,5))-3)
    zero('height f future focus event time',s.Rational(5,3)*(s.Rational(5,3)+s.Rational(4,5)*s.Rational(4,3))-s.Rational(41,9))
    zero('central incident wavefront label',s.Rational(4,5)+2-s.Rational(14,5))
    zero('off axis incident wavefront label',s.Rational(16,15)+s.Rational(8,3)-s.Rational(56,15))
    zero('simultaneous laboratory crossings have unequal incident phases',s.Rational(56,15)-s.Rational(14,5)-s.Rational(14,15))
    zero('same wavefront requires earlier off axis crossing',s.Rational(5,3)*(2+s.Rational(4,5))*(-s.Rational(1,3))+s.Rational(14,9))
    zero('earlier crossing cancels longer flight exactly',-s.Rational(14,9)+s.Rational(41,9)-3)
    zero('rest geometric focal parameter coincides with optical position',s.Rational(1,9)+s.Rational(1,3)-s.Rational(2,3)**2)
    zero('ground geometric focal parameter differs from optical separation',s.Rational(1,25)+s.Rational(1,3)-(2*s.sqrt(21)/15)**2)
    zero('geometric focal mismatch is strictly nonzero in moving slice',s.Rational(1,25)+s.Rational(1,3)-s.Rational(2,5)**2-s.Rational(16,75))
    # Separate geometric construction, Snell angle and refraction-vector checks.
    for nv in [1.25,1.5,2.,3.]:
        for height in [0.,.05,.5,1.,3.,20.]:
            xp=surface(height,n=nv);distance=np.hypot(xp,height)
            path=nv*xp+distance
            path_error=abs(path+(nv-1))
            assert path_error<1e-12
            slope=-height/((nv-1)*np.sqrt(1+(nv+1)/(nv-1)*height**2))
            tangent_num=np.array([slope,1.]);tangent_num/=np.linalg.norm(tangent_num)
            normal=np.array([1.,-slope]);normal/=np.linalg.norm(normal)
            incoming_num=np.array([1.,0.]);output=np.array([-xp,-height])/distance
            residual=abs(np.dot(nv*incoming_num-output,tangent_num))
            sin_i=abs(np.dot(incoming_num,tangent_num));sin_t=abs(np.dot(output,tangent_num))
            assert residual<2e-13 and abs(nv*sin_i-sin_t)<2e-13
            assert sin_i<1/nv and np.dot(output,normal)>0
            # Independently reconstruct transmitted direction from Snell vector.
            tangential=nv*np.dot(incoming_num,tangent_num)
            refracted=tangential*tangent_num+np.sqrt(1-tangential**2)*normal
            direction_error=float(np.linalg.norm(refracted-output))
            assert direction_error<1e-12
            note('exact physical branch equal path and actual refraction vector',
                 refractive_index=nv,height_over_f=height,X_over_f=float(xp),
                 optical_path_error=path_error,snell_residual=residual,
                 incoming_sine=float(sin_i),critical_sine=1/nv,
                 transmitted_direction_error=direction_error)
    for bv in [0.,.3,.6,.8,.95]:
        gv=1/np.sqrt(1-bv*bv)
        for height in [0.,.1,.5,1.,3.]:
            xp=surface(height);distance=np.hypot(xp,height)
            xe=xp/gv;vx=(-xp/distance+bv)/(1-bv*xp/distance)
            vy=-height/distance/(gv*(1-bv*xp/distance))
            expected_time=gv*(distance-bv*xp)
            # Solve a ray/worldline intersection numerically, not substitute
            # only the published final conic or arrival-time formula.
            hit=brentq(lambda elapsed:xe+(vx-bv)*elapsed,0,2*expected_time+1,xtol=1e-12)
            y_error=abs(height+vy*hit)
            conic=((xe+2/(3*gv))**2/(1/(9*gv*gv))-height**2/(1/3)-1)
            assert abs(vx*vx+vy*vy-1)<5e-14
            assert y_error<2e-12 and abs(hit-expected_time)<2e-12
            assert abs(conic)<1e-12
            ui=(.5+bv)/(1+.5*bv)
            assert ui>bv
            note('independent ray intersection with moving optical focus',
                 beta=bv,height_over_f=height,gamma=float(gv),
                 actual_intersection_time_over_f_c=float(hit),
                 analytic_time_error=abs(hit-expected_time),transverse_hit_error=y_error,
                 instantaneous_curve_residual=abs(conic),
                 vacuum_speed_error=abs(vx*vx+vy*vy-1),incident_speed_over_c=ui)
    # A common incident rest wavefront has one arrival event, not merely an
    # intersection of instantaneous straight-ray drawings.
    origin=-5.;start=0.;arrival=2*(surface(0.)-origin)+1
    for height in [0.,.2,.7,1.5,3.]:
        xp=surface(height);dist=np.hypot(xp,height);entry=2*(xp-origin)
        tf=entry+dist
        assert abs(tf-arrival)<2e-13
        labt=(5/3)*tf;labx=.8*labt
        tx=(5/3)*(entry+.8*xp);xx=(5/3)*(xp+.8*entry)
        vx=(-xp/dist+.8)/(1-.8*xp/dist);vy=-height/dist/((5/3)*(1-.8*xp/dist))
        assert abs(xx+vx*(labt-tx)-labx)<2e-13
        assert abs(height+vy*(labt-tx))<2e-13
        note('one incident wavefront transforms to one future focal event',
                 height_over_f=height,rest_arrival_time=tf,lab_arrival_time=labt,
                 lab_arrival_x=labx,interface_event_time=tx)
    fp=.30;hp=.15;xp=surface(hp,fp);rr=np.hypot(xp,hp)
    si=hp/np.sqrt(fp*fp+4*hp*hp)
    note('fully computed finite aperture variant',f_m=fp,height_m=hp,X_m=xp,r_m=rr,
         incidence_degrees=float(np.degrees(np.arcsin(si))),
         refraction_degrees=float(np.degrees(np.arcsin(2*si))),
         exact_sag_m=float(-fp-xp),paraxial_sag_m=hp*hp/(2*fp))
    readings=[]
    for rel in ['preview/originals/paper-03.png','preview/originals/answer-07.png',
                'preview/originals/details/q07-paper.png','preview/originals/details/q07-answer.png']:
        readings.append(dict(path=rel,sha256=sha(ROOT/rel),actual_displayed_and_read=True))
    report=dict(paper='014',question='07',math_passed=True,question_accepted=False,set_accepted=False,
                symbolic_count=len(symbolic),numeric_count=len(numerical),symbolic=symbolic,numerical=numerical,
                source_sha256={name:sha(ROOT.parent/name) for name in ['试卷.pdf','答案.pdf']},
                actual_original_readings=readings,script_sha256=sha(Path(__file__)),
                model_revision='Explicit user approval: index, f and fixed focus in medium rest frame; ground focus moves.',
                caveats=['Squared hyperbola alone is insufficient: retain physical left branch.',
                         'Coordinates X,Y,T denote medium rest frame; x,y,t ground frame.',
                         'No fixed ground focus or ground isotropic c/n assumption is introduced.'])
    if (ROOT/'drafts/question-07.md').exists():report['draft_sha256']=sha(ROOT/'drafts/question-07.md')
    if full:
        report['figure_source_sha256']=sha(ROOT/'figures/题07_图稿源文件.tex')
        report['working_pdf_checks']=json.loads((ROOT/'preview/working-draft-check-q07.json').read_text())
    name='question-07-math.json' if full else 'question-07-initial-math.json'
    (ROOT/'verification'/name).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(passed=True,symbolic=len(symbolic),numeric=len(numerical),question_accepted=False),ensure_ascii=False))
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--full',action='store_true');args=parser.parse_args();run(args.full)
