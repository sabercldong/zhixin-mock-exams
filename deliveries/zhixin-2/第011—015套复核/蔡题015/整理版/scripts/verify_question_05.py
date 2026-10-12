"""Independent Q5 geometry and dynamics checks; conditional model, not source/PDF acceptance."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,math
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.optimize import root,brentq
from numpy.polynomial.legendre import leggauss

ROOT=Path(__file__).resolve().parents[1]
SYMBOLIC=[];NUMERIC=[]
def identity(name,actual,expected=0):
    residual=sp.simplify(actual-expected)
    assert residual==0,(name,residual)
    SYMBOLIC.append({"name":name,"residual":str(residual)})
def close(name,value,expected,tol=3e-6):
    value=float(value);expected=float(expected)
    err=abs(value-expected)/max(abs(expected),1.)
    assert np.isfinite(value) and err<tol,(name,value,expected,err)
    NUMERIC.append({"name":name,"value":value,"expected":expected,"normalized_error":err,"tolerance":tol})
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def exact_symbolic():
    r,g,m=sp.symbols("r g m",positive=True)
    d1,d2,v,u,w=sp.symbols("d1 d2 v u w",real=True)
    rt=sp.sqrt
    A=sp.Matrix([3*r*(-sp.cos(d1)/rt(3)-rt(sp.Rational(2,3))*sp.sin(d1)),
                 rt(6)*r*(-sp.sin(d1)/rt(3)+rt(sp.Rational(2,3))*sp.cos(d1)),0])
    B=sp.Matrix([3*r*(sp.cos(d2)/rt(3)-rt(sp.Rational(2,3))*sp.sin(d2)),
                 rt(6)*r*(sp.sin(d2)/rt(3)+rt(sp.Rational(2,3))*sp.cos(d2)),0])
    P=sp.Matrix([u,-r+v,w])
    AP=P-A;BP=P-B
    l1=rt(AP.dot(AP));l2=rt(BP.dot(BP))
    E=sp.Matrix([AP.dot(A.diff(d1)),BP.dot(B.diff(d2)),l1+l2-4*rt(3)*r])
    q=sp.Matrix([d1,d2,v]);base={d1:0,d2:0,v:0,u:0,w:0}
    at=lambda expr:sp.simplify(expr.subs(base))
    identity("ring A abscissa",at(A[0]),-rt(3)*r)
    identity("ring A ordinate",at(A[1]),2*r)
    identity("equilibrium normal A",at(E[0]))
    identity("equilibrium normal B",at(E[1]))
    identity("fixed total string equilibrium",at(E[2]))
    t=A.diff(d1);tt=A.diff(d1,2)
    speed=at(rt(t.dot(t)))
    cross=at(rt(t.cross(tt).dot(t.cross(tt))))
    rho=sp.simplify(speed**3/cross)
    identity("ellipse curvature from parametric derivatives",rho,16*r/(3*rt(3)))
    ell=at(l1)
    identity("straight segment length",ell,2*rt(3)*r)
    identity("bead beyond osculating center",ell-rho,2*r/(3*rt(3)))
    normal=at(AP/ell)
    O=sp.simplify(at(A)+rho*normal)
    identity("left osculating center x",O[0],-r/(3*rt(3)))
    identity("osculating center y",O[1],-2*r/3)
    ae=ell-rho;ce=-O[0]
    be=sp.simplify(rt(ae**2-ce**2));Re=sp.simplify(ae**2/be)
    identity("local auxiliary ellipse semiminor",be,r/3)
    identity("local bottom equals bead position",O[1]-be,-r)
    identity("local trajectory radius",Re,4*r/9)
    J=at(E.jacobian(q))
    assert sp.simplify(J.det())!=0
    qu=sp.simplify(-J.inv()*at(E.diff(u)))
    qw=sp.simplify(-J.inv()*at(E.diff(w)))
    identity("left ring parameter slope",qu[0],rt(6)/r)
    identity("right ring parameter slope",qu[1],rt(6)/r)
    identity("first order vertical bead shift",qu[2])
    for i in range(3):identity(f"out of plane first order ring/height {i}",qw[i])
    def second(input_var,first):
        terms=[]
        for e in E:
            qq=at(sp.hessian(e,list(q)))
            mixed=at(sp.Matrix([sp.diff(e,input_var,qi) for qi in q]))
            terms.append(sp.simplify(at(sp.diff(e,input_var,2))+2*(mixed.T*first)[0]+(first.T*qq*first)[0]))
        return sp.simplify(-J.inv()*sp.Matrix(terms))
    quu=second(u,qu);qww=second(w,qw)
    identity("exact implicit in-plane height curvature",quu[2],9/(4*r))
    identity("exact implicit out-plane height curvature",qww[2],1/(3*r))
    mixed=[]
    for e in E:
        eq=at(sp.Matrix([sp.diff(e,w,qi) for qi in q]))
        mixed.append(sp.simplify(at(sp.diff(e,u,w))+(eq.T*qu)[0]))
    quw=sp.simplify(-J.inv()*sp.Matrix(mixed))
    identity("mixed height curvature vanishes",quw[2])
    T0=m*g/rt(3)
    identity("positive equal tensions vertical balance",T0*(2*rt(3)/2),m*g)
    identity("period squared",4*sp.pi**2*Re/g,16*sp.pi**2*r/(9*g))
    qdot_scale=at(rt(t.dot(t)))*qu[0]
    identity("ring arc slope",qdot_scale,4*rt(3))
    # Full configuration with finite ring degrees: the ideal constraint reduction is singular.
    fyy=at(E[2].diff(v))
    fdd=at(E[2].diff(d1,2))
    unrestricted_ydd=sp.simplify(-fdd/fyy)
    identity("finite-ring-coordinate potential curvature (not ideal normal branch)",unrestricted_ydd,-r/6)
    return {"jacobian_determinant":str(sp.factor(J.det())),
            "first_derivative":list(map(str,qu)),
            "second_inplane":list(map(str,quu)),
            "second_outplane":list(map(str,qww)),
            "conditional_model":"Inextensible massless string; ideal negligible-mass rings; in-plane branch for handwritten single period."}

def numerical_branch(a,b,x,z=0.):
    c=math.sqrt(a*a-b*b);d=math.sqrt(a*a+c*c)
    theta0=np.array([math.acos(-c/a),math.acos(c/a),-c*c/a])
    def values(q):
        th1,th2,y=q
        A=np.array([a*math.cos(th1),b*math.sin(th1),0.])
        B=np.array([a*math.cos(th2),b*math.sin(th2),0.])
        t1=np.array([-a*math.sin(th1),b*math.cos(th1),0.])
        t2=np.array([-a*math.sin(th2),b*math.cos(th2),0.])
        tt1=np.array([-a*math.cos(th1),-b*math.sin(th1),0.])
        tt2=np.array([-a*math.cos(th2),-b*math.sin(th2),0.])
        P=np.array([x,y,z]);v1=P-A;v2=P-B
        l1=np.linalg.norm(v1);l2=np.linalg.norm(v2)
        G1=v1@t1;G2=v2@t2
        F=np.array([G1,G2,l1+l2-2*d])
        J=np.array([[-t1@t1+v1@tt1,0.,t1[1]],
                    [0.,-t2@t2+v2@tt2,t2[1]],
                    [-G1/l1,-G2/l2,v1[1]/l1+v2[1]/l2]])
        Eu=np.array([t1[0],t2[0],v1[0]/l1+v2[0]/l2])
        return F,J,Eu,A,B,v1/l1,v2/l2,l1,l2
    result=root(lambda q:values(q)[0],theta0,jac=lambda q:values(q)[1],tol=1e-11)
    state=values(result.x)
    assert np.linalg.norm(state[0])<2e-11,(result.message,state[0])
    qx=-np.linalg.solve(state[1],state[2])
    return result.x,qx,state

def period_from_original_normal_constraints(amplitude,n=48):
    nodes,weights=leggauss(n)
    ymax=numerical_branch(3.,math.sqrt(6),amplitude)[0][2]
    total=0.
    for node,weight in zip(nodes,weights):
        phi=(node+1)*math.pi/4;x=amplitude*math.sin(phi)
        q,qx,state=numerical_branch(3.,math.sqrt(6),x)
        gap=ymax-q[2]
        assert gap>0,(amplitude,x,gap)
        integrand=amplitude*math.cos(phi)*math.sqrt(1+qx[2]**2)/math.sqrt(2*gap)
        total+=weight*integrand
    return total*math.pi # four times integral with dphi=pi/4

def high_precision_energy_period(amplitude,n=32):
    """Same nonlinear source constraints at 50 digits; avoid subtractive loss near turning point."""
    with mp.workdps(50):
        amp=mp.mpf(str(amplitude));a=mp.mpf(3);b=mp.sqrt(6)
        t1base=mp.acos(-1/mp.sqrt(3));t2base=mp.acos(1/mp.sqrt(3))
        def state(x):
            def eq(t1,t2,y):
                ax=a*mp.cos(t1);ay=b*mp.sin(t1)
                bx=a*mp.cos(t2);by=b*mp.sin(t2)
                dx1=x-ax;dy1=y-ay;dx2=x-bx;dy2=y-by
                return (dx1*(-a*mp.sin(t1))+dy1*b*mp.cos(t1),
                        dx2*(-a*mp.sin(t2))+dy2*b*mp.cos(t2),
                        mp.sqrt(dx1*dx1+dy1*dy1)+mp.sqrt(dx2*dx2+dy2*dy2)-4*mp.sqrt(3))
            t1,t2,y=mp.findroot(eq,(t1base+mp.sqrt(6)*x,t2base+mp.sqrt(6)*x,
                                   -1+mp.mpf(9)*x*x/8),tol=mp.mpf("1e-42"))
            ax=a*mp.cos(t1);ay=b*mp.sin(t1);bx=a*mp.cos(t2);by=b*mp.sin(t2)
            l1=mp.sqrt((x-ax)**2+(y-ay)**2);l2=mp.sqrt((x-bx)**2+(y-by)**2)
            fx=(x-ax)/l1+(x-bx)/l2;fy=(y-ay)/l1+(y-by)/l2
            return y,-fx/fy # envelope derivative: the two stationary ring contributions vanish
        ymax=state(amp)[0];nodes,weights=leggauss(n);total=mp.mpf(0)
        for node,weight in zip(nodes,weights):
            phi=(mp.mpf(str(node))+1)*mp.pi/4
            x=amp*mp.sin(phi);y,yp=state(x)
            total+=mp.mpf(str(weight))*amp*mp.cos(phi)*mp.sqrt(1+yp**2)/mp.sqrt(2*(ymax-y))
        return float(mp.pi*total)

def main():
    symbolic_summary=exact_symbolic()
    for a,b in [(3.,math.sqrt(6)),(4.,math.sqrt(12)),(2.5,1.4),(5.,3.)]:
        c=math.sqrt(a*a-b*b);d=math.sqrt(a*a+c*c)
        R=d*d*c**4/a**5
        h=2e-4
        def yy(x,z=0.):return numerical_branch(a,b,x,z)[0][2]
        y0=yy(0.)
        H1=(yy(h)+yy(-h)-2*y0)/h**2
        H2=(yy(2*h)+yy(-2*h)-2*y0)/(2*h)**2
        close(f"exact-ring constraints x curvature a={a}",(4*H1-H2)/3,1/R)
        Z1=(yy(0,h)+yy(0,-h)-2*y0)/h**2
        Z2=(yy(0,2*h)+yy(0,-2*h)-2*y0)/(2*h)**2
        close(f"exact-ring constraints z curvature a={a}",(4*Z1-Z2)/3,1/a)
        for x,z in [(-.002,0.),(.002,0.),(0.,.002),(.001,.001),(-.001,-.001)]:
            q,qx,state=numerical_branch(a,b,x,z)
            close(f"fixed-length a={a} x={x} z={z}",state[7]+state[8],2*d,2e-11)
            close(f"ring A tangential residual a={a} x={x} z={z}",state[0][0],0,2e-11)
            close(f"ring B tangential residual a={a} x={x} z={z}",state[0][1],0,2e-11)
            nsum=-(state[5]+state[6])
            assert nsum[1]>0 # tensile support, not compressive rods
        th=math.acos(c/a)
        t=np.array([-a*math.sin(th),b*math.cos(th)])
        tt=np.array([-a*math.cos(th),-b*math.sin(th)])
        rho=np.linalg.norm(t)**3/abs(np.linalg.det(np.column_stack([t,tt])))
        close(f"parametric curvature a={a}",rho,b*b*d**3/a**4,1e-12)
    # Direct horizontal restoring force from the original string directions.
    for h in [.0002,.0004,.0008]:
        slopes=[]
        for x in [h,2*h]:
            q,qx,state=numerical_branch(3.,math.sqrt(6),x)
            nsum=-(state[5]+state[6])
            force_x=nsum[0]/nsum[1] # mg=1
            slopes.append(-force_x/x)
        close(f"actual string restoring-force slope h={h}",(4*slopes[0]-slopes[1])/3,9/4)
    periods={}
    for amp in [.001,.002,.004]:
        periods[str(amp)]=period_from_original_normal_constraints(amp)
    extrap=(4*periods["0.001"]-periods["0.002"])/3
    close("independent energy integral original nonlinear branch",extrap,4*math.pi/3,3e-6)
    close("energy integral quadrature 32/48 convergence",period_from_original_normal_constraints(.002,32),periods["0.002"],3e-6)
    hp_periods={str(amp):high_precision_energy_period(amp) for amp in [.0005,.001,.002]}
    close("50-digit source constraints quadrature 32/48",high_precision_energy_period(.002,48),hp_periods["0.002"],1e-11)
    close("50-digit independent zero-amplitude period extrapolation",(4*hp_periods["0.0005"]-hp_periods["0.001"])/3,4*math.pi/3,1e-9)
    close("double/50-digit independent nonlinear period",periods["0.002"],hp_periods["0.002"],3e-6)
    # Ring pinning is a separate variant: exact ellipse from fixed two focal endpoints.
    a,b=3.,math.sqrt(6);c=math.sqrt(3);d=2*math.sqrt(3);yA=2.
    for x in [-.1,-.02,0.,.02,.1]:
        f=lambda y:math.hypot(x+c,y-yA)+math.hypot(x-c,y-yA)-2*d
        y=brentq(f,-6.,yA-1e-4,xtol=1e-13)
        close(f"fixed rings exact ellipse y at {x}",y,yA-3*math.sqrt(1-x*x/d**2),1e-12)
    close("changed axes a=4,b=sqrt12 radius",20*16/4**5,5/16,1e-12)
    r=.12;g=9.8;m=.15;uamp=.002
    values={"r_m":r,"g_m_s2":g,"mass_kg":m,"bead_amplitude_m":uamp,
            "inplane_period_s":2*math.pi*math.sqrt(4*r/(9*g)),
            "outplane_period_s":2*math.pi*math.sqrt(3*r/g),
            "tension_N":m*g/math.sqrt(3),
            "ring_arc_amplitude_m":4*math.sqrt(3)*uamp,
            "bead_acceleration_amplitude_m_s2":9*g/(4*r)*uamp,
            "energy_J":.5*m*9*g/(4*r)*uamp*uamp}
    close("normal mode frequency ratio squared",((3*math.sqrt(3)/2)**2),27/4,1e-12)
    original={"paper":sha(ROOT.parent/"试卷.pdf"),"answers":sha(ROOT.parent/"答案.pdf")}
    report={"paper":"015","question":5,
            "stage":"independent preverification only, not full source or figure/PDF acceptance",
            "created_utc":datetime.now(timezone.utc).isoformat(),
            "originals":original,
            "detail_manifest_sha256":sha(ROOT/"preview/originals/question-05-detail-manifest.json"),
            "script_sha256":sha(Path(__file__)),
            "symbolic_checks":SYMBOLIC,"numeric_checks":NUMERIC,
            "symbolic_count":len(SYMBOLIC),"numeric_count":len(NUMERIC),
            "max_normalized_error":max(row["normalized_error"] for row in NUMERIC),
            "symbolic_summary":symbolic_summary,
            "independent_energy_periods_r1_g1":periods,
            "high_precision_energy_periods_r1_g1":hp_periods,
            "numeric_variant":values,"verified_math":True,
            "document_complete":False,"model_condition_resolved":False,
            "question_accepted":False,"set_accepted":False,
            "remaining_model_issues":["原题写伸长的细线而手写采用固定绳长；是否同步改为不可伸长须确认。",
                                      "原题未限定平面内扰动；单一手写周期只覆盖平面内理想无质量环的约束支路。"]}
    path=ROOT/"build/question-05-preverification.json"
    path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:v for k,v in report.items() if k not in ["symbolic_checks","numeric_checks"]},ensure_ascii=False))
if __name__=="__main__":main()
