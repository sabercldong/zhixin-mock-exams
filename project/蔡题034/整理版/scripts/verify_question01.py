"""Independent event-by-event check for set034 question1 (not full-set acceptance)."""
from math import sin,cos,tan,atan,log,ceil,sqrt,isclose,pi
from pathlib import Path
import json

def formula(v0,alpha,e,mu,g=9.8):
    U,w=v0*cos(alpha),v0*sin(alpha)
    K=mu*(1+e)/(1-e)
    if U>=K*w-1e-13*v0:
        return (U+mu*w)**2/(2*mu*g),None
    z=1-U/(K*w)
    n=max(1,ceil(log(z)/log(e)))
    # Correct round-off at exact equality; retain the defining inequalities.
    while n>1 and U-K*w*(1-e**(n-1))<=1e-13*v0:n-=1
    while U-K*w*(1-e**n)>1e-13*v0:n+=1
    s=e**n
    D=2*w/g*((U-K*w)*(1-s)/(1-e)+K*w*(1-s*s)/(1-e*e))
    C=(1+e-2*s)/(1-e)
    assert isclose((U+mu*w)**2/(2*mu*g)-D,
                   (U-mu*C*w)**2/(2*mu*g),rel_tol=1e-9,abs_tol=1e-8)
    return D,n

def event(v0,alpha,e,mu,g=9.8):
    ux,vy=v0*cos(alpha),v0*sin(alpha)
    x=0.
    count=0
    while vy>1e-13*v0 and ux>0:
        x+=ux*(2*vy/g)
        normal_impulse_per_mass=(1+e)*vy
        ux=max(0.,ux-mu*normal_impulse_per_mass)
        vy*=e
        count+=1
        assert count<20000
    if ux>0:x+=ux*ux/(2*mu*g)
    return x

if __name__=="__main__":
    count=0
    for e in [.05,.25,.5,.8,.97]:
        for mu in [.04,.15,.3,.6,.95]:
            for deg in [2,8,16.69924423399,30,45,60,80,88]:
                a=deg*pi/180
                d,n=formula(12.3,a,e,mu)
                numerical=event(12.3,a,e,mu)
                assert isclose(d,numerical,rel_tol=1e-9,abs_tol=1e-8),(e,mu,deg,d,numerical,n)
                count+=1
            K=mu*(1+e)/(1-e)
            for n in [1,2,3,8]:
                a=atan(1/(K*(1-e**n)))
                d,found=formula(12.3,a,e,mu)
                assert found==n,(e,mu,n,found)
                assert isclose(d,event(12.3,a,e,mu),rel_tol=1e-9,abs_tol=1e-8)
                count+=1
    result={"question":1,"event_checks":count,"status":"PASS",
            "sample30":formula(1,pi/6,.5,.3,g=1)[0],
            "sample60":formula(1,pi/3,.5,.3,g=1)[0],
            "optimal_example":formula(1,atan(.3),.5,.3,g=1)[0]}
    dest=Path(__file__).resolve().parents[1]/"build"
    dest.mkdir(exist_ok=True)
    (dest/"question01-verification.json").write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print(json.dumps(result,ensure_ascii=False,indent=2))

