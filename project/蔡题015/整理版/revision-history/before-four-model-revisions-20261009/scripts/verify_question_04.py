"""015 Q4: independent circuit, mechanics, thermal and solved-variant checks."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.optimize import brentq
from scipy.integrate import quad,solve_ivp

ROOT=Path(__file__).resolve().parents[1]
symbolic,numeric=[],[]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def exact(name,expr):
    residual=sp.simplify(expr)
    assert residual==0,(name,residual)
    symbolic.append({"name":name,"residual":str(residual)})
def close(name,value,expected,tol=2e-9):
    error=abs(value-expected)/max(1,abs(expected))
    assert error<=tol,(name,value,expected,error)
    numeric.append({"name":name,"value":float(value),"expected":float(expected),"normalized_error":float(error)})
def free_z(T,x,p=1e5,S=.0012,V=.001,k=1e4,Tref=300):
    a=k/(p*S);b=S/V
    lo=max(-x,-V/S)+1e-12
    return brentq(lambda z:Tref*(1+a*(x+z))*(1+b*z)-T,lo,.01,xtol=1e-15)
def main():
    e,r,Rh,Rs=sp.symbols("e r Rh Rs",positive=True)
    Req=Rh*Rs/(Rh+Rs)
    U=e*Req/(r+Req)
    Ph=e**2*Rh/(r+Rh)**2
    Pl=U**2/Rh
    exact("closed node-current sum",(e-U)/r-U/Rh-U/Rs)
    exact("closed low heating-power form",Pl-e**2*Rh*Rs**2/(r*(Rh+Rs)+Rh*Rs)**2)
    exact("closed chemical and all resistor power",e*(e-U)/r-((e-U)/r)**2*r-U**2/Rh-U**2/Rs)
    Uh=e*Rh/(r+Rh)
    exact("open chemical and all resistor power",e**2/(r+Rh)-e**2*r/(r+Rh)**2-Uh**2/Rh)
    exact("ideal voltage source has no shunt regulation",Pl.subs(r,0)-Ph.subs(r,0))
    exact("equal resistors heating ratio", (Pl/Ph).subs(Rs,Rh)-(r+Rh)**2/(2*r+Rh)**2)
    exact("original high heating",Ph.subs({e:15,r:1,Rh:4})-36)
    exact("original low heating",Pl.subs({e:15,r:1,Rh:4,Rs:4})-25)
    p,S,V,k,Tref,x,z,T,G,C=sp.symbols("p S V k Tref x z T G C",positive=True)
    a=k/(p*S);b=S/V
    pm=p+k*(x+z)/S
    Tfree=Tref*(1+a*(x+z))*(1+b*z)
    exact("free piston force",pm*S-p*S-k*(x+z))
    exact("actual ideal gas and piston equation",pm*(V+S*z)-p*V*Tfree/Tref)
    exact("contact threshold volume is fixed",Tfree.subs(z,0)-Tref*(1+a*x))
    exact("rod/piston quadratic expansion",Tfree/Tref-(1+a*x+(a+b+a*b*x)*z+a*b*z*z))
    exact("free temperature slope",sp.diff(Tfree,z)-Tref*(a+b+a*b*x+2*a*b*z))
    xstar=p*S/k*(T/Tref-1)
    exact("threshold displacement inverse",Tref*(1+a*xstar)-T)
    Nh=p*S*(T/Tref-1)-k*x
    exact("optional hard-stop reaction vanishes at threshold",Nh.subs(x,xstar))
    L,H=sp.symbols("L H",positive=True)
    d=(H-G*(T-Tref))/(H-L)
    exact("relay average heat balance",d*L+(1-d)*H-G*(T-Tref))
    eta=sp.symbols("eta",nonnegative=True)
    xgap=p*S/k*(T/(Tref*(1+eta))-1)
    exact("variant fixed contact volume",Tref*(1+a*xgap)*(1+eta)-T)
    work=sp.integrate((p+k*(x+z)/S)*S,z)
    exact("free piston gas work equals ambient plus spring change",sp.diff(work,z)-sp.diff(p*S*z+sp.Rational(1,2)*k*(x+z)**2,z))
    tau,t=sp.symbols("tau t",positive=True)
    Teq=sp.symbols("Teq",positive=True)
    Ti=sp.symbols("Ti",positive=True)
    sol=Teq+(Ti-Teq)*sp.exp(-G*t/C)
    exact("fixed-state thermal ODE",C*sp.diff(sol,t)-G*(Teq-sol))
    # SI dimensional identities, not numerical unit labels only.
    from sympy.physics.units import meter,kelvin,pascal,newton,joule,watt,convert_to
    exact("SI kx/S is pressure",convert_to((newton/meter)*meter/meter**2,pascal)-pascal)
    exact("SI displacement scale pS/k",convert_to(pascal*meter**2/(newton/meter),meter)-meter)
    exact("SI heat-loss power",convert_to((watt/kelvin)*kelvin,watt)-watt)
    exact("SI p dV is work",convert_to(pascal*meter**3,joule)-joule)

    rng=np.random.default_rng(1504)
    # Independent simultaneous Kirchhoff equations for voltage, total current, branch currents.
    for j in range(18):
        ev=float(rng.uniform(8,24));rv=float(rng.uniform(.3,3))
        hv=float(rng.uniform(2,8));sv=float(rng.uniform(2,12))
        mat=np.array([[1,rv,0,0],[0,1,-1,-1],[1,0,-hv,0],[1,0,0,-sv]],float)
        uv,it,ih,is_=np.linalg.solve(mat,np.array([ev,0,0,0],float))
        req=hv*sv/(hv+sv)
        low=ev**2*hv*sv**2/(rv*(hv+sv)+hv*sv)**2
        high=ev**2*hv/(rv+hv)**2
        close(f"node {j+1} heater power",ih*ih*hv,low)
        close(f"node {j+1} terminal voltage",uv,ev-rv*it)
        close(f"node {j+1} full power budget",ih*ih*hv+is_*is_*sv+it*it*rv,ev*it)
        assert high>low>0
    # Actual mechanical residual roots; coordinates never silently identified.
    for j,xv in enumerate(np.linspace(0,.003,13)):
        Tv=325 if xv<=.001 else (300*(1+1e4*xv/(1e5*.0012)) if xv<.00144 else 336)
        zv=free_z(Tv,xv)
        pv=1e5+1e4*(xv+zv)/.0012
        close(f"piston {j+1} actual pV",pv*(.001+.0012*zv)/Tv,1e5*.001/300)
        close(f"piston {j+1} force residual",pv*.0012,1e5*.0012+1e4*(xv+zv))
        if xv<=.001: assert zv>=-2e-12
        elif xv<.00144: close(f"piston {j+1} relay location",zv,0)
        else: assert zv<=2e-12
        assert .001+.0012*zv>0 and xv+zv>=-2e-12
    close("original low equilibrium",300+25,325)
    close("original high equilibrium",300+36,336)
    close("critical rod travel m",brentq(lambda q:300*(1+1e4*q/(1e5*.0012))-325,0,.002),.001)
    close("330 K rod travel m",brentq(lambda q:300*(1+1e4*q/(1e5*.0012))-330,0,.002),.0012)
    close("upper rod travel m",brentq(lambda q:300*(1+1e4*q/(1e5*.0012))-336,0,.002),.00144)
    close("325 K free piston rise",free_z(325,0),.0009846574719986243)
    # Integrate actual free-state gas work, comparing independent spring energy differences.
    for j in range(8):
        xv=float(rng.uniform(.0002,.002));t1=float(rng.uniform(315,325));t2=t1+float(rng.uniform(1,8))
        z1,z2=free_z(t1,xv),free_z(t2,xv)
        w=quad(lambda q:(1e5+1e4*(xv+q)/.0012)*.0012,z1,z2,epsabs=1e-13)[0]
        de=1e5*.0012*(z2-z1)+.5*1e4*((xv+z2)**2-(xv+z1)**2)
        close(f"gas-work {j+1} ambient plus spring",w,de)
        for q in [z1,z2]:
            deriv=300*(1e4/(1e5*.0012)*(1+.0012*q/.001)+(1+1e4*(xv+q)/(1e5*.0012))*.0012/.001)
            ce=(1e5*.001/(8.314462618*300))*3*8.314462618+(1e5+1e4*(xv+q)/.0012)*.0012/deriv
            assert ce>0
    # ODE event times versus independently separated-variable logarithms.
    # Constant C is an explicitly added variant, not a source-given heat capacity.
    for j in range(6):
        cv=15+3*j;gv=1+.08*j;tl=325;th=336;ts=329+.15*j;hh=.1+.03*j
        low,high=ts-hh,ts+hh
        event_c=lambda t,y:y[0]-low
        event_c.terminal=True;event_c.direction=-1
        cool=solve_ivp(lambda t,y:[gv*(tl-y[0])/cv],[0,100],[high],events=event_c,rtol=2e-12,atol=2e-12,max_step=.01)
        tc=float(cool.t_events[0][0])
        close(f"hysteresis {j+1} cooling event",tc,cv/gv*math.log((high-tl)/(low-tl)),tol=2e-8)
        event_h=lambda t,y:y[0]-high
        event_h.terminal=True;event_h.direction=1
        heat=solve_ivp(lambda t,y:[gv*(th-y[0])/cv],[0,100],[low],events=event_h,rtol=2e-12,atol=2e-12,max_step=.01)
        tht=float(heat.t_events[0][0])
        close(f"hysteresis {j+1} heating event",tht,cv/gv*math.log((th-low)/(th-high)),tol=2e-8)
    tc=15*math.log(5.1/4.9);tht=15*math.log(6.1/5.9)
    close("variant 3 cooling seconds",tc,.6000800192056225)
    close("variant 3 heating seconds",tht,.5000463040138756)
    close("variant 3 closed fraction",tc/(tc+tht),.5454646494136237)
    # Other complete variants and environmental distinctions.
    var1low=15**2*4*8**2/(1*(4+8)+4*8)**2
    close("variant 1 low heat",var1low,3600/121)
    close("variant 1 closed fraction",brentq(lambda d:d*var1low+(1-d)*36-30,0,1),121/126)
    close("variant 2 environment changed closed fraction",brentq(lambda d:d*25+(1-d)*36-35,0,1),1/11)
    close("variant 2 lower displacement",(.0012*1e5/1e4)*(320/300-1),.0008)
    close("variant 2 upper displacement",(.0012*1e5/1e4)*(331/300-1),.00124)
    for j,target in enumerate([325,330,336]):
        eps=.0012
        xx=brentq(lambda q:300*(1+1e4*q/(1e5*.0012))*(1+eps)-target,0,.002)
        close(f"variant 4 fixed-volume target {j+1}",xx,(1e5*.0012/1e4)*(target/(300*(1+eps))-1))
    close("variant 4 330 K travel cm",(1e5*.0012/1e4)*(330/(300*(1+.0012))-1)*100,.11841789852177376)
    for j,target in enumerate(np.linspace(325,336,12)):
        dv=brentq(lambda d:d*25+(1-d)*36-(target-300),0,1)
        close(f"relay average balance {j+1}",dv*25+(1-dv)*36,target-300)
        assert 0<=dv<=1
    manuscript=ROOT/"drafts/question-04.md"
    report={"paper":"015","question":4,"stage":"independent source/math preverification; no figure or PDF acceptance",
            "created_utc":datetime.now(timezone.utc).isoformat(),"symbolic_checks":symbolic,
            "numeric_checks":numeric,"symbolic_count":len(symbolic),"numeric_count":len(numeric),
            "max_normalized_error":max(v["normalized_error"] for v in numeric),
            "verified_math":True,"document_complete":False,"question_accepted":False,"set_accepted":False,
            "scope":"negligible initial gap and ideal quasi-static threshold model; finite-gap/hysteresis variants explicitly separate",
            "source_sha256":sha(manuscript) if manuscript.exists() else None,
            "script_sha256":sha(Path(__file__)),"originals":{"paper":sha(ROOT.parent/"试卷.pdf"),"answers":sha(ROOT.parent/"答案.pdf")},
            "detail_manifest_sha256":sha(ROOT/"preview/originals/question-04-detail-manifest.json")}
    (ROOT/"build/question-04-preverification.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({k:report[k] for k in ["symbolic_count","numeric_count","max_normalized_error","document_complete","question_accepted"]}))
if __name__=="__main__": main()
