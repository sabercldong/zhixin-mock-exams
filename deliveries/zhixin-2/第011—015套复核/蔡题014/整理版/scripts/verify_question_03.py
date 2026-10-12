"""Initial Q3 checks: variational equation, metric flattening, real reaction and quadrature.
No source draft/figure/PDF acceptance is asserted by this computation.
"""
from pathlib import Path
import argparse,hashlib,json,math
import sympy as s
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('--full',action='store_true');args=parser.parse_args()
r,rp,rpp,c,l,g=s.symbols('r rp rpp c l g',positive=True,real=True)
phi=s.symbols('phi',real=True)
q=s.symbols('q',real=True)
checks=[]
def zero(name,expr):
    residual=s.trigsimp(s.simplify(expr))
    assert residual==0,(name,residual)
    checks.append(dict(name=name,passed=True))
F=s.sqrt(r*r+rp*rp)/s.sqrt(r)
F_r=s.diff(F,r);F_rp=s.diff(F,rp)
EL=s.simplify(F_r-(s.diff(F_rp,r)*rp+s.diff(F_rp,rp)*rpp))
zero('Euler-Lagrange residual exactly reduces to hand-written ODE',
     EL-(r*r+3*rp*rp-2*r*rpp)*s.sqrt(r)/(2*(r*r+rp*rp)**s.Rational(3,2)))
zero('Beltrami first integral derived directly from F',
     F-rp*F_rp-r**s.Rational(3,2)/s.sqrt(r*r+rp*rp))
rstar=c/s.cos(phi/2)**2
dr=s.diff(rstar,phi);ddr=s.diff(rstar,phi,2)
zero('parabola satisfies the actual second-order variational equation',rstar*rstar+3*dr*dr-2*rstar*ddr)
zero('first integral on the parabola after squaring',
     rstar**3/(rstar*rstar+dr*dr)-c)
zero('both inbound and outbound radius derivative magnitude',dr**2-rstar**2*(rstar/c-1))
x=s.trigsimp(rstar*s.cos(phi));y=s.trigsimp(rstar*s.sin(phi))
zero('Cartesian focus-directrix relation r+x=2c',rstar+x-2*c)
zero('Cartesian parabola equivalent to polar result',y*y-4*c*(c-x))
X=s.sqrt(r)*s.cos(phi/2);Z=s.sqrt(r)*s.sin(phi/2)
zero('square-root metric radial coefficient',s.diff(X,r)**2+s.diff(Z,r)**2-1/(4*r))
zero('square-root metric angular coefficient',s.diff(X,phi)**2+s.diff(Z,phi)**2-r/4)
zero('square-root metric cross coefficient',s.diff(X,r)*s.diff(X,phi)+s.diff(Z,r)*s.diff(Z,phi))
# Real particle motion uses the constrained parabola, not optical auxiliary momentum.
xq=c*(1-q*q);yq=2*c*q;rq=c*(1+q*q)
zero('actual radius from Cartesian coordinates',xq*xq+yq*yq-rq*rq)
ydot=s.sqrt(2*g*c)
xdot=-q*ydot
zero('real trajectory speed equals sqrt(2gr)',xdot*xdot+ydot*ydot-2*g*rq)
normal=s.Matrix([-1,-q])/s.sqrt(1+q*q)
gravity=g*s.Matrix([xq,yq])/rq
actual_acc=s.Matrix([-g,0])
reaction=s.simplify(actual_acc-gravity)
zero('constraint reaction equals positive normal scalar',
     (reaction-2*g/s.sqrt(1+q*q)*normal).norm()**2)
zero('normal reaction does no mechanical work',reaction.dot(s.Matrix([xdot,ydot])))
zero('trajectory curvature and speed give centripetal acceleration',
     2*g*rq/(2*c*(1+q*q)**s.Rational(3,2))-g/s.sqrt(1+q*q))
zero('radial potential gives outward constant force',-s.diff(-g*r,r)-g)
# Endpoint and elapsed-time checks on the ordinary smaller central angle.
theta=s.symbols('theta',positive=True,real=True)
cend=l*s.cos(theta/2)**2
zero('parabola passes through both prescribed endpoints',rstar.subs({phi:theta,c:cend})-l)
# Ordinary smaller central angle: 0 < theta <= pi/2, hence cos(theta/2)>0.
time_residual=s.simplify(2*l*s.sin(theta)/s.sqrt(2*g*cend)-2*s.sqrt(2*l/g)*s.sin(theta/2))
time_residual=s.refine(time_residual,s.Q.positive(s.cos(theta/2)))
zero('time from linear y motion matches square-root chord on allowed angular domain',time_residual)
numeric=[]
def add(name,measured,expected,scale=1.,**data):
    error=abs(measured-expected)/max(scale,abs(expected),1e-30)
    assert error<2e-9,(name,measured,expected,error)
    numeric.append(dict(name=name,measured=measured,expected=expected,error=error,passed=True,**data))
for theta0 in [.03,.2,.5,1.,1.4,math.pi/2]:
    leng=2.3;gg=4.7;cc=leng*math.cos(theta0/2)**2
    def radius(t):return cc/math.cos(t/2)**2
    def rprime(t):return radius(t)*math.tan(t/2)
    integral,err=quad(lambda t:math.hypot(radius(t),rprime(t))/math.sqrt(2*gg*radius(t)),-theta0,theta0,epsabs=1e-12,epsrel=1e-12)
    expected=2*math.sqrt(2*leng/gg)*math.sin(theta0/2)
    add('independent polar arc-length time integral',integral,expected,theta=theta0)
    # Nonstationary smooth competitors keep exactly the same two endpoint radii.
    for strength in [-.20,-.05,.05,.25,1.]:
        def competitor(t):
            f=1+strength*math.cos(math.pi*t/(2*theta0))**2
            fp=-strength*math.pi/(2*theta0)*math.sin(math.pi*t/theta0)
            rr=radius(t)*f;rrp=rprime(t)*f+radius(t)*fp
            return math.hypot(rr,rrp)/math.sqrt(2*gg*rr)
        value,_=quad(competitor,-theta0,theta0,epsabs=1e-11,epsrel=1e-11)
        assert value>=expected-1e-10,(theta0,strength,value,expected)
        numeric.append(dict(name='endpoint-preserving inward/outward path is not faster',theta=theta0,strength=strength,time=value,optimal=expected,passed=True))
    # Real motion is solved from dy/dt, independently of the polar integral.
    final_y=leng*math.sin(theta0);speed_y=math.sqrt(2*gg*cc)
    flight=2*final_y/speed_y
    add('elapsed time from actual real-particle trajectory',flight,expected,theta=theta0)
    for fraction in [.0,.1,.5,.9,1.]:
        yy=-final_y+fraction*flight*speed_y
        xx=cc-yy*yy/(4*cc);rr=math.hypot(xx,yy)
        vx=-yy*speed_y/(2*cc);vy=speed_y
        add('actual kinetic energy plus outward potential is zero',.5*(vx*vx+vy*vy)-gg*rr,0,scale=gg*leng,theta=theta0,fraction=fraction)
        force_x=-gg-gg*xx/rr;force_y=-gg*yy/rr
        add('constraint force does no work along actual motion',force_x*vx+force_y*vy,0,scale=gg*math.sqrt(2*gg*leng),theta=theta0,fraction=fraction)
        assert force_x<0
    # The circular competitor retains r=l but has a longer optical length.
    circle_time=2*theta0*leng/math.sqrt(2*gg*leng)
    assert circle_time>=expected
    numeric.append(dict(name='circular arc is no faster',theta=theta0,time=circle_time,optimal=expected,passed=True))
if args.full:
    # Additional manuscript steps and solved variants, independent of the earlier 18/108.
    C=s.symbols('C',real=True);uu=C*r**3-r*r
    zero('second partial derivative in slope is strictly positive expression',
         s.diff(F,rp,2)-r**s.Rational(3,2)/(r*r+rp*rp)**s.Rational(3,2))
    zero('integrating-factor solution solves reduced ODE',s.diff(uu,r)-3*uu/r-r)
    zero('reduced integrating factor product derivative',s.diff(uu*r**-3,r)-r**-2)
    z=s.symbols('z',positive=True);ww=C*z**s.Rational(3,2)-z
    zero('hand-written alternative z=r^2 reduction',z+3*ww-2*z*s.diff(ww,z))
    zero('real curvature from Cartesian first and second derivatives',
         s.Rational(1,2)/c/(1+q*q)**s.Rational(3,2)-1/(2*c*(1+q*q)**s.Rational(3,2)))
    zero('radial force has negative projection on concave-side normal',
         gravity.dot(normal)+g/s.sqrt(1+q*q))
    zero('actual constraint torque is g*y per unit mass',
         xq*reaction[1]-yq*reaction[0]-g*yq)
    real_L=xq*ydot-yq*xdot
    zero('real angular momentum is not conserved: time derivative equals torque',
         s.diff(real_L,q)*ydot/(2*c)-g*yq)
    zero('small-angle closest-radius expansion to fourth order',
         s.series(cend/l,theta,0,6).removeO()-(1-theta**2/4+theta**4/48))
    zero('small-angle time ratio expansion to fourth order',
         s.series(2*s.sin(theta/2)/theta,theta,0,6).removeO()-(1-theta**2/24+theta**4/1920))
    zero('small-angle absolute time expansion through fifth order',
         s.series(2*s.sin(theta/2),theta,0,7).removeO()-(theta-theta**3/24+theta**5/1920))
    zero('endpoint speed components have exactly the specified magnitude',
         (s.sqrt(2*g*l)*s.sin(theta/2))**2+(s.sqrt(2*g*l)*s.cos(theta/2))**2-2*g*l)
    zero('endpoint dimensionless q is the half-angle tangent',
         l*s.sin(theta)/(2*cend)-s.tan(theta/2))
    # Auxiliary attractive particle is deliberately not the real constrained particle.
    a,mu,J,e=s.symbols('a mu J e',positive=True);paux=J*J/(mu*a);rpaux=paux/(1+e)
    zero('auxiliary periapsis energy fixes eccentricity without assuming a parabola',
         J*J/(2*mu*rpaux*rpaux)-a/rpaux-mu*a*a/(2*J*J)*(e*e-1))
    rho=mu*a/J**2*(1+e*s.cos(phi))
    zero('auxiliary Binet equation',s.diff(rho,phi,2)+rho-mu*a/J**2)
    zero('auxiliary near-radius c equals p/2 at zero energy',paux/2-J**2/(2*mu*a))
    ra,rb=s.symbols('ra rb',positive=True);beta=s.symbols('beta',real=True)
    wa=s.Matrix([s.sqrt(ra),0]);wb=s.Matrix([s.sqrt(rb)*s.cos(beta/2),s.sqrt(rb)*s.sin(beta/2)])
    delta=wb-wa;D2=ra+rb-2*s.sqrt(ra*rb)*s.cos(beta/2)
    zero('unequal radii Euclidean squared distance',delta.dot(delta)-D2)
    nw=s.Matrix([delta[1],-delta[0]])/s.sqrt(D2)
    zero('unequal radii line normal has unit length',nw.dot(nw)-1)
    hh=s.sqrt(ra*rb)*s.sin(beta/2)/s.sqrt(D2)
    zero('unequal radii line offset from origin',nw.dot(wa)-hh)
    tt=(ra-s.sqrt(ra*rb)*s.cos(beta/2))/D2
    zero('unequal radii foot parameter satisfies perpendicularity',(wa+tt*delta).dot(delta))
    zero('unequal radii complete-line minimum radius equals h^2',
         s.expand_trig(((wa+tt*delta).dot(wa+tt*delta)-hh*hh).subs(beta,2*phi)))
    Om=s.symbols('Omega',positive=True);u=s.symbols('u',real=True)
    zero('linear radial force comes from its stated potential',-s.diff(-Om**2*r*r/2,r)-Om**2*r)
    zero('linear radial force logarithmic radial metric',s.diff(l*s.exp(u),u)/(l*s.exp(u))-1)
    zero('linear radial force circular support supplies inward net force',2*Om**2*l-Om**2*l-Om**2*l)
    # Explicit physical-unit conversions do not use source-code length as content.
    from sympy.physics.units import meter,second,newton,kilogram,convert_to
    zero('time result has SI seconds',convert_to(s.sqrt(meter/(meter/second**2)),second)-second)
    zero('reaction magnitude has SI force',convert_to(kilogram*meter/second**2,newton)-newton)
    for ra0,rb0,beta0 in [(2.,2.,1.2),(.03,10.,.05),(10.,.03,.05),(1.,4.,math.pi),(4.,1.,2.8),(1.,1.,math.pi)]:
        wa0=(math.sqrt(ra0),0.);wb0=(math.sqrt(rb0)*math.cos(beta0/2),math.sqrt(rb0)*math.sin(beta0/2))
        dx,dy=wb0[0]-wa0[0],wb0[1]-wa0[1];d2=dx*dx+dy*dy;dist=math.sqrt(d2);gg=3.4
        foot=-(wa0[0]*dx+wa0[1]*dy)/d2;clamped=min(1.,max(0.,foot))
        def sample(t):
            xx=wa0[0]+t*dx;yy=wa0[1]+t*dy
            rr=xx*xx+yy*yy;rrp=2*(xx*dx+yy*dy)
            phip=2*(xx*dy-yy*dx)/rr
            return math.hypot(rrp,rr*phip)/math.sqrt(2*gg*rr)
        travel,_=quad(sample,0,1,epsabs=1e-12,epsrel=1e-12)
        add('unequal radii actual polar time integral vs mapped line',travel,math.sqrt(2/gg)*dist,ra=ra0,rb=rb0,beta=beta0)
        minr=(wa0[0]+clamped*dx)**2+(wa0[1]+clamped*dy)**2
        h0=math.sqrt(ra0*rb0)*math.sin(beta0/2)/dist
        expected=h0*h0 if 0<=foot<=1 else min(ra0,rb0)
        add('unequal-radii segment minimum uses clamped foot',minr,expected,ra=ra0,rb=rb0,beta=beta0,foot=foot)
        for t in [0.,.25,.5,.75,1.]:
            wx=wa0[0]+t*dx;wy=wa0[1]+t*dy
            radius=wx*wx+wy*wy;phase=2*math.atan2(wy,wx)
            gamma=math.atan2(-dx,dy)
            add('unequal-radii reconstructed rotated parabola satisfies its equation',
                radius*(1+math.cos(phase-2*gamma)),2*h0*h0,ra=ra0,rb=rb0,beta=beta0,t=t)
    # True nonplanar test paths are compared with angle-progress compression.
    for theta0 in [.3,.8,1.3,math.pi/2]:
        for amplitude in [.2,.6]:
            leng=2.;gg=3.;cc=leng*math.cos(theta0/2)**2
            def sphere_speed(t):
                tilt=amplitude*math.cos(math.pi*t/(2*theta0))
                tiltprime=-amplitude*math.pi/(2*theta0)*math.sin(math.pi*t/(2*theta0))
                return math.hypot(tiltprime,math.cos(tilt))
            total,_=quad(sphere_speed,-theta0,theta0,epsabs=1e-12,epsrel=1e-12)
            ratio=2*theta0/total;assert ratio<=1+1e-12
            def time_integrand(t,compress):
                rr=cc/math.cos(t/2)**2;rrp=rr*math.tan(t/2)
                angular=sphere_speed(t)*(ratio if compress else 1.)
                return math.hypot(rrp,rr*angular)/math.sqrt(2*gg*rr)
            original,_=quad(lambda t:time_integrand(t,False),-theta0,theta0,epsabs=1e-11)
            compressed,_=quad(lambda t:time_integrand(t,True),-theta0,theta0,epsabs=1e-11)
            lower=2*math.sqrt(2*leng/gg)*math.sin(theta0/2)
            assert original+1e-11>=compressed and compressed+1e-11>=lower
            numeric.append(dict(name='nonplanar actual angular compression does not increase time',theta=theta0,amplitude=amplitude,
                                original=original,compressed=compressed,global_minimum=lower,passed=True))
    for theta0 in [.02,.1,.4,1.,math.pi/2]:
        leng=2.;om=.7
        circular=2*theta0/om
        for strength in [-.2,.2,.8]:
            # A direct nonconstant-radius competitor for the linear-force variant.
            def integrand(t):
                radial_log=strength*math.cos(math.pi*t/(2*theta0))**2
                derivative=-strength*math.pi/(2*theta0)*math.sin(math.pi*t/theta0)
                rr=leng*math.exp(radial_log);rrp=rr*derivative
                return math.hypot(rrp,rr)/(om*rr)
            value,_=quad(integrand,-theta0,theta0,epsabs=1e-11)
            assert value>=circular-1e-11
            numeric.append(dict(name='linear-force direct time integral: circle is no slower',theta=theta0,strength=strength,time=value,circular=circular,passed=True))
    for theta0 in [.005,.01,.025]:
        ratio=2*math.sin(theta0/2)/theta0
        approx=1-theta0**2/24+theta0**4/1920
        add('small-angle time ratio verified numerically',ratio,approx,theta=theta0)
report=dict(paper='014',question='03',scope=('full current manuscript mathematics and solved variants; PDF acceptance separate' if args.full else 'initial math and actual source reading only; no finished question or PDF'),
            symbolic_checks=checks,symbolic_count=len(checks),numeric_count=len(numeric),numerical_checks=numeric,
            math_passed=True,question_accepted=False,set_accepted=False,
            source_sha256={name:hashlib.sha256((ROOT.parent/name).read_bytes()).hexdigest() for name in ['试卷.pdf','答案.pdf']},
            script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            result=dict(closest_radius='l*cos(theta0/2)^2',polar='r=l*cos(theta0/2)^2/cos(phi/2)^2',
                        time='2*sqrt(2*l/g)*sin(theta0/2)',normal_reaction='2*m*g/sqrt(1+q^2)'),
            pending=['完整九模块与手写Snell/Euler-Lagrange代数补全','平面轨道/微元/最短路/受力图','分题工作PDF与实际审读'])
if args.full:
    report.update(draft_sha256=hashlib.sha256((ROOT/'drafts/question-03.md').read_bytes()).hexdigest(),
                  figure_source_sha256=hashlib.sha256((ROOT/'figures/题03_图稿源文件.tex').read_bytes()).hexdigest(),
                  model_authorization_required=False,
                  pending=['实际图稿及工作PDF审读；分题验收与整套完成分开'])
dest=ROOT/('verification/question-03-math.json' if args.full else 'verification/question-03-initial-math.json')
dest.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(symbolic_count=len(checks),numeric_count=len(numeric),math_passed=True,question_accepted=False),ensure_ascii=False))
