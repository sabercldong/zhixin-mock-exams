"""八题的独立计算核验；明确区分题设近似、模型限制和严格关系。"""
from pathlib import Path
import json
import math
import numpy as np
from scipy.integrate import quad,solve_ivp
from scipy.special import airy,ai_zeros
from scipy.linalg import eigh_tridiagonal

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'build'
def save(q,details):
    details['status']='pass'
    (DEST/f'question{q:02}-verification.json').write_text(json.dumps(details,ensure_ascii=False,indent=2)+'\n')
    print(f'{q:02} 独立核验通过',flush=True)
def near(a,b,rtol=1e-9,atol=1e-12):
    assert np.allclose(a,b,rtol=rtol,atol=atol),(a,b)
def q1():
    p=1.;h=.5;g=1.
    errors=[]
    for alpha in np.linspace(-.7,.7,19):
        s=-p*np.tan(alpha);z=s*s/(2*p)
        y_contact=s*np.sin(alpha)+z*np.cos(alpha)
        y_mass=h*np.cos(alpha)-y_contact
        analytic=(h-p/2)*np.cos(alpha)+p/(2*np.cos(alpha))
        near(y_mass,analytic)
        errors.append(abs(y_mass-analytic))
    w=math.sqrt(g*(p-h))/h
    def ode(t,Y):
        a,v=Y
        s=-p*np.tan(a);z=p/2*np.tan(a)**2
        D2=s*s+(h-z)**2
        sp=-p/(np.cos(a)**2);zp=p*np.tan(a)/(np.cos(a)**2)
        Dprime=2*s*sp-2*(h-z)*zp
        Hp=-(h-p/2)*np.sin(a)+p/2/np.cos(a)*np.tan(a)
        return [v,-(.5*Dprime*v*v+g*Hp)/D2]
    sol=solve_ivp(ode,[0,10],[.01,0],rtol=1e-11,atol=1e-13,dense_output=True)
    energies=[]
    for a,v in sol.y.T:
        s=-np.tan(a);z=.5*np.tan(a)**2
        energies.append(.5*(s*s+(h-z)**2)*v*v+(h-.5)*np.cos(a)+.5/np.cos(a))
    assert np.ptp(energies)<1e-10
    critical=[(.5*np.cos(a)+.5/np.cos(a)-1) for a in np.linspace(-.7,.7,99)]
    assert min(critical)>-1e-14
    save(1,dict(contact_geometry_error=max(errors),nonlinear_energy_spread=float(np.ptp(energies)),linear_period=2*np.pi/w,
                stable_range='0<h<=p; harmonic requires h<p',critical_case='quartic stable, no nonzero harmonic frequency'))
def q2():
    K=m=r=1.
    work_in=quad(lambda x:K/x**3,2*r,np.inf)[0]
    work_out=quad(lambda x:K/x**3,6*r,np.inf)[0]
    near(2*(work_in-work_out)/m,2/9)
    v=.3
    for stage in range(3):
        u=np.sqrt(v*v+2*work_in/m)
        speeds=[u,0.,0.,0.,0.]
        for j in range(4):
            before=sum(x*x for x in speeds)
            speeds[j],speeds[j+1]=speeds[j+1],speeds[j]
            near(sum(x*x for x in speeds),before)
        v=np.sqrt(speeds[-1]**2-2*work_out/m)
    near(v*v,.3**2+2/3)
    e=.98;a=(1+e)/2
    speeds=[1.,0,0,0,0]
    losses=0.
    for j in range(4):
        u,vv=speeds[j:j+2];before=.5*(u*u+vv*vv)
        va=(1-e)*u/2+(1+e)*vv/2;vb=(1+e)*u/2+(1-e)*vv/2
        near(va+vb,u+vv);near(vb-va,e*(u-vv))
        speeds[j:j+2]=[va,vb];losses+=before-.5*(va*va+vb*vb)
    near(speeds[-1],a**4)
    q=a**8;D=q/4-1/36-.01;star=D/(1-q);y=.1
    for N in range(1,250):
        y=q*y+D
        near(y,q**N*.1+D*(1-q**N)/(1-q))
    save(2,dict(work_in=work_in,work_out=work_out,three_stage_v2=v*v,q=q,D=D,fixed_v2=star,fixed_v=np.sqrt(star),
                note='center-distance force and prescribed four sequential impacts; distant sliding-friction approximation; later recollisions not implied'))
def q3():
    rng=np.random.default_rng(2203)
    maximum=0.
    for u1,u2 in [(3,1),(3,-1),(1,-1),(3,0)]:
        V=np.array([(u1+u2)/2,0,0]);w=abs(u1-u2)/2
        for _ in range(200):
            n=rng.normal(size=3);n/=np.linalg.norm(n)
            a=V+w*n;b=V-w*n
            near(a+b,np.array([u1+u2,0,0]));near(a@a+b@b,u1*u1+u2*u2)
            near(a@b,u1*u2)
            maximum=max(maximum,abs(a@b-u1*u2))
    save(3,dict(max_dot_error=maximum,choices={'A':True,'B':True,'C':False,'D':False},
                same_direction_counterexample_angles_deg=[19.10660535,30.],
                opposite_direction_counterexample_angles_deg=[40.89339465,90.]))
def q4():
    R=.1;a=.003;L=.002;T=.001;mu0=4*np.pi*1e-7;mu=1000*mu0;sigma=5.8e7;N=100;i=.1
    D=(2*np.pi*R-L)/mu+L/mu0
    C=sigma*T*a*a/4;tau=C/D;Binf=N*i/D
    integral=quad(lambda s:-sigma*s*T/2,0,a)[0]
    near(integral,-C)
    sol=solve_ivp(lambda t,Y:[(N*i-D*Y[0])/C],[0,6*tau],[0],rtol=1e-11,atol=1e-13)
    exact=Binf*(1-np.exp(-sol.t/tau))
    assert np.max(abs(exact-sol.y[0]))<1e-11
    Bdot=.4
    heat=quad(lambda s:(sigma*s*s*Bdot*Bdot/4)*2*np.pi*s*T,0,a)[0]
    near(heat,np.pi*sigma*T*a**4*Bdot**2/8)
    save(4,dict(tau=tau,Binf=Binf,half_strip_current_per_Bdot=integral,
                max_ODE_error=float(np.max(abs(exact-sol.y[0]))),heat_integral=heat,
                model_limitation='one-pole equation is stipulated lumped approximation, not exact local Maxwell diffusion',
                tau_over_local_diffusion=tau/(mu0*sigma*a*a),uniform_field_not_automatically_justified=True))
def q5():
    mu0=4*np.pi*1e-7;r=.1;d=.001;l=2;rho=1.7e-8;I0=2
    R=2*np.pi*rho*r/(l*d);L=mu0*np.pi*r*r/l;tau=L/R
    sol=solve_ivp(lambda t,Y:[-R/L*Y[0],R*Y[0]**2],[0,10*tau],[I0,0],rtol=1e-11,atol=1e-13)
    near(sol.y[0,-1],I0*np.exp(-10),rtol=1e-6)
    near(sol.y[1,-1],.5*L*I0**2*(1-np.exp(-20)),rtol=1e-6)
    I=.7;E=rho*I/(l*d);B=mu0*I/l
    near(E*B/mu0*(2*np.pi*r*l),R*I*I)
    save(5,dict(R=R,L=L,tau=tau,energy_error=float(sol.y[1,-1]-.5*L*I0**2*(1-np.exp(-20))),
                skin_to_thickness=np.sqrt(r*d)/d,poynting_outward_power=R*I*I,
                assumptions='nonmagnetic long fixed thin wall, no external drive, quasistatic'))
def q6():
    Ts=5500;lam_s=550;lam_c=400;Tc=Ts*lam_s/lam_c
    lightyear=9.4607304725808e15;dist=1520*lightyear;S=5.17e-13;sigma=5.67e-8
    rc=dist*np.sqrt(S/(sigma*Tc**4));rp=.01*rc;rho=5000.;mp=4*np.pi/3*rp**3*rho
    Mc=2.6e30;G=6.67e-11;c=3e8;K=.5*c*6.9e-10;vp=Mc/mp*K
    Tp=568*86400;R=vp*Tp/(2*np.pi);gp=G*mp/rp**2
    T=Tc*(.9/4)**.25*np.sqrt(rc/R)
    TL=36000;psi=np.pi*TL/Tp
    stheta=np.sqrt(((rc+rp)/R)**2-np.sin(psi)**2)/np.cos(psi)
    theta=np.arcsin(stheta);b=R*np.sin(theta);eta=(rc+rp)/R
    near(np.pi*rp**2/(np.pi*rc**2),1e-4)
    near(sigma*Tc**4*(rc/dist)**2,S)
    near(R*np.sqrt(np.sin(psi)**2+np.sin(theta)**2*np.cos(psi)**2),rc+rp)
    probability=quad(lambda th:.5*np.cos(th),-np.arcsin(eta),np.arcsin(eta))[0];near(probability,eta)
    Rk=(G*(Mc+mp)*Tp**2/(4*np.pi**2))**(1/3);vk=2*np.pi*Rk/Tp
    mdyn=vp**3*Tp/(2*np.pi*G)
    near((1-.1)*sigma*Tc**4*(rc/R)**2*np.pi*rp**2,4*np.pi*rp**2*sigma*T**4)
    save(6,dict(Tc=Tc,distance=dist,rc=rc,rp=rp,mp=mp,vp=vp,R=R,gp=gp,T_global=T,theta=theta,b=b,eta=eta,
                kepler_v=vk,kepler_R=Rk,relative_kepler_speed_difference=vk/vp-1,
                inferred_dynamic_mass=mdyn,input_mass=Mc,
                exact_input_consistency=False,physics_status='given rounded observations not exactly Kepler-consistent; main and cross-check routes not mixed'))
def refract(point,d,n):
    normal=point/np.linalg.norm(point);cosi=d@normal
    tang=n*(d-cosi*normal)
    assert tang@tang<1
    return tang+np.sqrt(1-tang@tang)*normal
def intersection(P1,d1,P2,d2):
    t=np.linalg.solve(np.column_stack([d1,-d2]),P2-P1)
    return P1+t[0]*d1
def ray_pair_direct(S,n,eps):
    rays=[]
    for y in [-eps,eps]:
        P=np.array([np.sqrt(1-y*y),y]);d=P-S;d/=np.linalg.norm(d)
        rays.append((P,refract(P,d,n)))
    return intersection(*rays[0],*rays[1])
def ray_pair_mirror(S,n,eps,final):
    rays=[]
    for y in [-eps,eps]:
        P=np.array([-np.sqrt(1-y*y),y]);d=P-S;d/=np.linalg.norm(d)
        normal=P
        d=d-2*(d@normal)*normal
        if final:
            # second positive intersection of the reflected line with sphere
            distance=-2*(P@d);P=P+distance*d;d=refract(P,d,n)
        rays.append((P,d))
    return intersection(*rays[0],*rays[1])
def q7():
    checks=[]
    for n in [1.,4/3,1.5]:
        y0=1e-5;h1=y0*(n+1)/2;S=np.array([1/(n+1),y0]);eps=2e-5
        direct=ray_pair_direct(S,n,eps)
        intermediate=ray_pair_mirror(S,n,eps,False)
        final=ray_pair_mirror(S,n,eps,True)
        exacts=[np.array([.5,h1]),np.array([-1/(n+3),-2*h1/(n+3)]),np.array([-n/4,-n*h1/2])]
        for actual,expected in zip([direct,intermediate,final],exacts):
            near(actual,expected,rtol=3e-7,atol=3e-8)
        checks.append(dict(n=n,direct=direct.tolist(),mirror=intermediate.tolist(),final=final.tolist(),prediction=[x.tolist() for x in exacts]))
    save(7,dict(exact_surface_vector_raytrace=checks,speed_ratio_actual_eye='-n(n+1)/4',speed_ratio_direct_image='-n/2',
                note='finite paraxial ray errors checked against independently reflected and refracted exact sphere rays'))
def q8():
    h=6.62607015e-34;hbar=h/(2*np.pi);m=1.675e-27;g=10
    ell=(hbar*hbar/(2*m*m*g))**(1/3)
    zeros=-ai_zeros(3)[0];Eexact=m*g*ell*zeros
    # dimensionless Hamiltonian -d²/dx²+x on half-line, Dirichlet ends, x_max=24
    N=4000;dx=24/(N+1);x=dx*np.arange(1,N+1)
    eig=eigh_tridiagonal(2/dx**2+x,-np.ones(N-1)/dx**2,select='i',select_range=(0,2),check_finite=False)[0]
    assert np.max(abs(eig-zeros))<3e-5
    E0=(9*m*g*g*h*h/512)**(1/3);H0=E0/(m*g)
    Ew=(9*m*g*g*h*h/32*(.75)**2)**(1/3)
    for delta in [.25,.75]:
        E=(9*m*g*g*h*h/32*delta**2)**(1/3);H=E/(m*g)
        action=2*quad(lambda s:np.sqrt(max(0,2*m*E*(1-s))),0,1,epsabs=1e-60)[0]*H
        near(action/h,delta,rtol=1e-9)
        freq=g/2*np.sqrt(m/(2*E));near(E/freq/h,1.5*delta)
    save(8,dict(given_model_E0=E0,given_model_H0=H0,WKB_hardwall_H0=Ew/(m*g),Airy_hardwall_H0=ell*zeros[0],
                finite_difference_eigenvalues=eig.tolist(),Airy_zeros=zeros.tolist(),max_eigenvalue_error=float(np.max(abs(eig-zeros))),
                exact_transition_frequency=(Eexact[1]-Eexact[0])/h,
                phase_condition='infinite hard wall Dirichlet => WKB n+3/4; given n+1/4 corresponds different boundary',
                interpretation='H is classical turning height, not an absolute quantum position bound; f is classical correspondence frequency'))
def main():
    DEST.mkdir(exist_ok=True)
    for task in [q1,q2,q3,q4,q5,q6,q7,q8]:task()
if __name__=='__main__':main()

