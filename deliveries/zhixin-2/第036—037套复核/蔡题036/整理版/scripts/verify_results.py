"""Independent arithmetic, constraint, integration and sign checks for set 036."""
from math import sqrt, pi, sin, cos, sinh, asinh, exp, log, isclose

def near(a, b, rel=1e-9, abs_tol=1e-10):
    assert isclose(a, b, rel_tol=rel, abs_tol=abs_tol), (a, b)

def simpson(f, a, b, n=10000):
    h = (b-a)/n
    return h/3*(f(a)+f(b)+4*sum(f(a+i*h) for i in range(1,n,2))
                +2*sum(f(a+i*h) for i in range(2,n,2)))

def ring_difference(rho, z, n=20000):
    # Dimensionless Ke*lambda=a=1; subtract origin before integration.
    return 2*pi/n*sum(1/sqrt(1+rho*rho+z*z-2*rho*cos(2*pi*(i+.5)/n))-1
                      for i in range(n))

def q1():
    eps = .001
    near(ring_difference(eps,0)/eps**2,pi/2,rel=2e-6)
    near(ring_difference(0,eps)/eps**2,-pi,rel=2e-6)
    s=.02
    cone=ring_difference(s*sqrt(2/3),s/sqrt(3))
    assert cone<0
    near(cone/s**4,-7*pi/24,rel=.002)
    assert 3/8-15/8*(2/3)+105/64*(2/3)**2<0
    print("Q1 PASS: transverse/axial curvature and k=2 quartic instability")

def q2():
    a=sqrt(3)*.75
    V=(a-1)/4
    H=sqrt(3-(3-a)**2)/4
    w=2*V
    D=2*H/w*asinh(V/H)
    D_num=2*simpson(lambda s:H/sqrt(H*H+w*w*s*s),0,.5)
    near(D,D_num)
    near(D,0.896087202987,abs_tol=1e-11)
    assert format(D,".3g")=="0.896"
    near(H*H+(.5-V)**2,3/16)
    near(.5+2*V,sqrt(3)*.75/2)
    assert 0<V<.125 and 0<D<1
    # Compare slope ratio across all feasible V.
    lo=.5-sqrt(3)/4
    for i in range(1001):
        v=lo+(V-lo)*i/1000
        hv=sqrt(max(0,3/16-(.5-v)**2))
        assert hv/v<=H/V+1e-10
    h=(sqrt(H*H+V*V)-H)/w
    print(f"Q2 PASS: D/l={D:.12f}, tan(alpha)={H/V:.12f}, h/l={h:.12f}")

def q3():
    na=(sqrt(3)/2,.5); nb=(-sqrt(3)/2,.5); nc=(0,-1)
    acc=[6/11,3/11,2/11]; normals=[na,nb,nc]
    center=(sqrt(3)/11,9/11)
    for n,a,speed2 in zip(normals,acc,[0,0,1]):
        near(a-sum(x*y for x,y in zip(center,n)),speed2)
    for j in (0,1):
        near(sum(m*a*n[j] for m,a,n in zip([1,2,3],acc,normals)),0)
    near(sqrt(sum(x*x for x in center)),2*sqrt(21)/11)
    for delta in (0,.1,1,10,100):
        den=4*delta*delta+24*delta+33
        ax=3*sqrt(3)/den; ay=(12*delta+27)/den
        av=[(6*delta+18)/den,(6*delta+9)/den,(4*delta*delta+12*delta+6)/den]
        for j,co in enumerate((ax,ay)):
            near(delta*co+sum(m*a*n[j] for m,a,n in zip([1,2,3],av,normals)),0)
    print("Q3 PASS: 3 radial constraints and zero total force")

def q4():
    E,R,rs,L,tb=12.,7.,3.,2.,.8
    tau=L*(R+rs)/(R*rs); inf=E/rs
    il=lambda t:inf*(1-exp(-t/tau))
    ir=lambda t:E/(R+rs)*exp(-t/tau)
    i0=il(tb); Q0=L*i0*i0/2
    q0=simpson(il,0,tb); q1=simpson(ir,0,tb)
    W=E*(q0+q1)
    heat=simpson(lambda t:rs*(il(t)+ir(t))**2+R*ir(t)**2,0,tb)
    near(q1,L*i0/R); near(heat,W-Q0)
    near(simpson(lambda t:R*i0*i0*exp(-2*R*t/L),0,20*L/R),Q0,rel=1e-8)
    print("Q4 PASS: charge and full on/off energy budgets")

def q5():
    B,r,E,R,k,m=1.,.02,1.5,2.,1e-6,.05
    K=B*r*r/2; I=m*r*r/2
    near(-K*(3000*2*pi/60),-.06283185307179587)
    n=E/K*60/(2*pi)
    near(K*E/(I*R),E*B/(m*R))
    steady=K*E/(K*K+k*R)
    load=K*E/(2*R)
    om=(K*E-R*load)/(K*K+k*R)
    near(om,steady/2)
    current=(E-K*om)/R
    near(E*current,R*current**2+k*om**2+load*om)
    power=lambda q:q*(K*E-R*q)/(K*K+k*R)
    assert power(load)>power(load*.99) and power(load)>power(load*1.01)
    print(f"Q5 PASS: voltage=-62.8319 mV, nmax={n:.9f} r/min; power optimum")

def q6():
    for d in [.01,.2,.5,.6,.99]:
        l=1.
        roots=[-sqrt(l*d),l-sqrt(l*(l-d)),sqrt(l*d),l+sqrt(l*(l-d))]
        assert len(set(round(a,12) for a in roots))==4
        for a in roots:
            sigma=1 if a>0 else -1
            u=abs(a); v=sigma*(l-a); f=1/(1/u+1/v)
            near(f,sigma*a*(l-a)/l)
            near((d-a)**2,f*f)
            assert u>0
        assert roots[0]<0<roots[1]<d<roots[2]<l<roots[3]
    print("Q6 PASS: all four roots, real-object signs and focus locations")

def q7():
    gam=5/3; p=.75
    TL=p**((gam-1)/gam)
    nL=2*p**(1/gam); nR=3-nL
    TR=1.5/nR
    near(nL*TL,1.5); near(nR*TR,1.5)
    near(nL*TL+nR*TR,3)
    near(TL,(nL/2)**(gam-1))
    assert TL<1<TR and nL>nR
    print(f"Q7 PASS: nL/nR={nL/nR:.12f}, TL/T0={TL:.12f}, TR/T0={TR:.12f}")

def q8():
    v=u=.5
    vin=(v+u)/(1+v*u)
    vout=(-vin-u)/(1+vin*u)
    w=-vout
    near(w,13/14)
    dc=v/(v+u); dr=dc*(1-u/w)
    near(dc,.5); near(dr,3/13)
    pin=v/sqrt(1-v*v); pout=-w/sqrt(1-w*w)
    dp=pout-pin
    F=dp/dc
    de=1/sqrt(1-w*w)-1/sqrt(1-v*v)
    near(F,-32*sqrt(3)/9)
    near(F*(-u),16*sqrt(3)/9)
    near(de/dc,F*(-u))
    # Direct event coordinates for a train of balls while the racket is ahead.
    ts=[(20+v*n)/(v+u) for n in range(6)]
    rs=[t+(20-u*t)/w for t in ts]
    for a,b in zip(rs,rs[1:]): near(b-a,dr)
    print("Q8 PASS: Lorentz reflection, event intervals, impulse and energy")

def extensions():
    # Weak hardening oscillator period from the energy integral.
    beta=.05; amp=.1
    period=4*simpson(lambda theta:
        (1+beta*amp**2/2*(1+sin(theta)**2))**(-.5),0,pi/2)
    approx=2*pi*(1-3*beta*amp**2/8)
    near(period,approx,rel=1e-7)
    near(sqrt(3)*asinh(1/sqrt(3)),sqrt(3)*log(3)/2)
    for b in (.01,.1,1.,10.):
        x=1-sqrt(b/(1+b))
        efficiency=lambda t:t*(1-(1+b)*t)/(1-t)
        near(efficiency(x),(sqrt(1+b)-sqrt(b))**2)
        assert efficiency(x)>efficiency(x*.999)
    for v,u in ((.2,.1),(.5,.5),(.8,.7)):
        energy=1/sqrt(1-v*v); p=energy*v; gamma2=1/(1-u*u)
        eout=gamma2*((1+u*u)*energy+2*u*p)
        pout=-gamma2*((1+u*u)*p+2*u*energy)
        near(eout-energy,-u*(pout-p))
    print("Extensions PASS: amplitude correction, friction boundary, finite ring mass, efficiency and 4-momentum")

if __name__=="__main__":
    for check in (q1,q2,q3,q4,q5,q6,q7,q8):
        check()
    extensions()
    print("All 8 independent checks passed.")
