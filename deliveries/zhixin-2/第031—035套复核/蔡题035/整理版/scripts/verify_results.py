"""Independent numerical/constraint checks for every question of set 035."""
from math import sqrt, sin, cos, asin, exp, pi, isclose
from fractions import Fraction
import json

def near(a,b,rel=1e-8,abs_tol=1e-9):
    assert isclose(a,b,rel_tol=rel,abs_tol=abs_tol),(a,b)

def bisect(f,a,b):
    assert f(a)*f(b)<=0
    for _ in range(90):
        c=(a+b)/2
        if f(a)*f(c)<=0:b=c
        else:a=c
    return (a+b)/2

def integrate(f,a,b,eps=1e-8):
    def simp(a,b,fa,fb,fc):return (b-a)*(fa+4*fc+fb)/6
    fa,fb,fc=f(a),f(b),f((a+b)/2)
    whole=simp(a,b,fa,fb,fc)
    def go(a,b,fa,fb,fc,old,tol,depth):
        c=(a+b)/2; fl=f((a+c)/2); fr=f((c+b)/2)
        left=simp(a,c,fa,fc,fl); right=simp(c,b,fc,fb,fr)
        if depth==0 or abs(left+right-old)<15*tol:
            return left+right+(left+right-old)/15
        return go(a,c,fa,fc,fl,left,tol/2,depth-1)+go(c,b,fc,fb,fr,right,tol/2,depth-1)
    return go(a,b,fa,fb,fc,whole,eps,26)

def q1():
    a,c,v=3.,1.,2.
    for u in (.2,.8,1.,1.4,2.3):
        ts=[a*j/(u*1000) for j in range(1001)]
        times=[t+(a-u*t)/c for t in ts]
        near(min(times),a/max(c,u))
        if u<c:assert times[0]<times[-1]
        elif u>c:assert times[-1]<times[0]
        else:
            for t in times:near(t,a/c)
        for t in ts[::50]:
            for dx in (-2,-.4,0,.4,2):
                T=t+sqrt((a-u*t)**2+dx**2)/c
                assert T>=a/max(c,u)-1e-10
    return {"critical_case":"all first-arrival positions checked"}

def q2():
    cv,cp=2.5,3.5
    qf=cv/(cv+cp)
    near(cv/cp,5/7);near(qf,5/12)
    for frac in [0,.2,.5,.8,1]:
        q=qf*frac
        TL=1+q/cv; TR=1+(1-q)/cp
        # nR=p0=V0=T0=Q0=1; total work = right volume change.
        near(cv*(TL-1+TR-1)+(TR-1),1)
    q=qf/2
    near((1-q)/cp-q/cv,1/7)
    return {"dU1":5/7,"dU2":5/12,"temperature_factor":1/7}

def q3():
    # Direct RK4 integration in ground-frame velocity, with position relative to drift.
    m,k,b,g=1.7,1.3,.9,2.1
    D=k*k+b*b
    vx,vy=m*g*b/D,-m*g*k/D
    expected=(-2*m*m*g*k*b/D**2,m*m*g*(k*k-b*b)/D**2)
    z=[0.,0.,0.,0.]
    def fun(y):return [(-k*y[0]-b*y[1])/m,(b*y[0]-k*y[1]-m*g)/m,y[0]-vx,y[1]-vy]
    h=.003
    for _ in range(16000):
        a=fun(z)
        bb=fun([v+h*t/2 for v,t in zip(z,a)])
        cc=fun([v+h*t/2 for v,t in zip(z,bb)])
        dd=fun([v+h*t for v,t in zip(z,cc)])
        z=[v+h*(a0+2*b0+2*c0+d0)/6 for v,a0,b0,c0,d0 in zip(z,a,bb,cc,dd)]
    near(z[0],vx);near(z[1],vy)
    near(z[2],expected[0]);near(z[3],expected[1])
    near(sqrt(z[2]**2+z[3]**2),m*m*g/D)
    return {"relative_displacement":z[2:],"method":"RK4, independent ODE integration"}

def q4():
    G,ME,MM,r,RE,RM,rho=6.67e-11,5.98e24,7.35e22,3.84e8,6.37e6,1.74e6,10.
    om=2*pi/(27.3*86400);xc=r*MM/(ME+MM);a=RE;b=r-RM
    f=lambda x:-G*ME/x**2+G*MM/(r-x)**2+om**2*(x-xc)
    H=lambda x:G*ME/x+G*MM/(r-x)+om**2*(x-xc)**2/2
    L=bisect(f,a,b)
    net=integrate(lambda t:f(t*1e8)*1e8,a/1e8,b/1e8,eps=.01)
    left=integrate(lambda t:f(t*1e8)*1e8,a/1e8,L/1e8,eps=.01)
    near(net,H(b)-H(a),rel=1e-10)
    near(left,H(L)-H(a),rel=1e-10)
    M=-rho*net/f(b);p=-rho*left; pend=-rho*net
    near(rho*net+M*f(b),0,abs_tol=1e-6)
    assert p>pend>0
    near(p,6.0954927010e8,rel=1e-10)
    for j in range(101):
        x=a+(b-a)*j/100
        assert rho*(H(a)-H(x))<=p+1e-3
    return {"M0_kg":M,"rL_m":L,"pmax_Pa":p,"pend_Pa":pend}

def q5():
    m,g,h,L,k=70.,10.,90.,30.,35.
    de=m*g/k; A=h-L-de; om=sqrt(k/m);v1=sqrt(2*g*L)
    near(.5*k*(h-L)**2,m*g*h)
    near((k*(h-L)-m*g)/m,2*g)
    near(A*om,sqrt(2*g*L+g*de))
    t1=sqrt(2*L/g);t2=(pi/2+pi/6)/om
    near(-de*cos(om*t2)+v1/om*sin(om*t2),A)
    near(de*om*sin(om*t2)+v1*cos(om*t2),0)
    # Time integral after z=A sin(theta) substitution.
    numeric=integrate(lambda theta:1/om,-pi/6,pi/2)
    near(numeric,t2)
    return {"L":L,"k":k,"vmax":A*om,"omega":om,"A":A,"time":t1+t2}

def q6():
    # Units c=1: independently boost both incoming particle energies/momenta.
    for m,M,Ti in [(4.,197.,.001),(4.,197.,20.),(1.,1.,3.),(1.,2.,1000.)]:
        E=m+Ti;p=sqrt(Ti*(Ti+2*m))
        beta=p/(E+M);gam=1/sqrt(1-beta*beta)
        e1=gam*(E-beta*p);p1=gam*(p-beta*E)
        e2=gam*M;p2=-gam*beta*M
        near(p1+p2,0,abs_tol=1e-8)
        near(e1*e1-p1*p1,m*m,rel=1e-8)
        near(e2*e2-p2*p2,M*M,rel=1e-8)
        est=e1+e2
        near(est,sqrt((m+M)**2+2*M*Ti))
        avail=2*M*Ti/(est+m+M)
        near(avail,est-m-M,abs_tol=1e-8)
        assert 0<avail<=Ti
    return {"checks":"individual Lorentz boosts, invariants, positive available energy"}

def q7():
    n=1.3
    beta=bisect(lambda b:4*asin(n*sin(b))-2*b-pi/2,0,asin(1/n)-1e-12)
    bp=asin(n*sin(beta))
    E=(-cos(beta),-sin(beta));v=(cos(beta-bp),sin(beta-bp))
    dot=lambda a,b:a[0]*b[0]+a[1]*b[1]
    H=tuple(E[i]-2*dot(E,v)*v[i] for i in range(2))
    vr=tuple(v[i]-2*dot(v,H)*H[i] for i in range(2))
    Q=tuple(H[i]-2*dot(H,vr)*vr[i] for i in range(2))
    near(Q[0],sin(beta));near(Q[1],cos(beta))
    near(H[0],1/sqrt(2));near(H[1],-1/sqrt(2))
    # Exit tangential component after refraction into water must match +y.
    tangent=(-Q[1],Q[0])
    near(dot(vr,tangent),n*dot((0.,1.),tangent))
    factor=1/sqrt(2)+sin(beta)
    diameters=[2*N*488e-9*.3/(.036*factor) for N in (8,8.5,9)]
    assert pi-2*asin(1/n)<pi/2
    near(diameters[1]*1e6,59.6873375261)
    return {"beta_deg":beta*180/pi,"geometric_factor":factor,
            "diameter_um":[d*1e6 for d in diameters],"ray_exit":Q}

def solve(A,b):
    n=len(b);a=[[Fraction(v) for v in row]+[Fraction(b[i])] for i,row in enumerate(A)]
    for col in range(n):
        pivot=next(i for i in range(col,n) if a[i][col])
        a[col],a[pivot]=a[pivot],a[col]
        v=a[col][col];a[col]=[x/v for x in a[col]]
        for i in range(n):
            if i!=col:
                factor=a[i][col];a[i]=[x-factor*y for x,y in zip(a[i],a[col])]
    return [row[-1] for row in a]

def q8():
    edges=[(i,(i+d)%7) for i in range(7) for d in (1,2)]
    assert len({tuple(sorted(e)) for e in edges})==14
    L=[[0]*7 for _ in range(7)]
    for i,j in edges:
        L[i][i]+=1;L[j][j]+=1;L[i][j]-=1;L[j][i]-=1
    answers=[]
    for sink,expected in [(1,Fraction(38,91)),(2,Fraction(40,91)),(3,Fraction(48,91))]:
        keep=[i for i in range(7) if i!=sink]
        z=solve([[L[i][j] for j in keep] for i in keep],[int(i==0) for i in keep])
        V=[Fraction(0)]*7
        for i,v in zip(keep,z):V[i]=v
        assert V[0]==expected
        for i in range(7):
            assert sum(L[i][j]*V[j] for j in range(7))==int(i==0)-int(i==sink)
        assert sum((V[i]-V[j])**2 for i,j in edges)==expected
        spectral=sum(2*(1-cos(2*pi*k*sink/7))/
                     (4-2*cos(2*pi*k/7)-2*cos(4*pi*k/7))
                     for k in range(1,7))/7
        near(spectral,float(expected))
        answers.append({"R":str(expected),"V":[str(v) for v in V]})
    return answers

if __name__=="__main__":
    result={}
    for i,fun in enumerate((q1,q2,q3,q4,q5,q6,q7,q8),1):
        result[str(i)]=fun()
        print("Q",i,"PASS",json.dumps(result[str(i)],ensure_ascii=False))
    print("All eight question checks passed.")
