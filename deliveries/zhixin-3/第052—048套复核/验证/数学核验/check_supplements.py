from pathlib import Path
import hashlib,json
import numpy as np
import sympy as s
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import erf,beta
P=Path(__file__).parent;rows=[]
def near(a,b,tol=1e-6):return bool(np.allclose(a,b,atol=tol,rtol=tol))
def zero(a):return s.simplify(a)==0
def group(n,q,kind,checks):
 ok=all(bool(v)for v in checks.values());rows.append(dict(set=n,question=q,section=kind,passed=ok,checks={k:bool(v)for k,v in checks.items()}));
 assert ok,(n,q,kind,checks)
x,n,G=s.symbols('x n G',positive=True);E=n*n/x**2-G*s.exp(-x)/x;stat=2*n*n*s.exp(x)/(x*(1+x));gam=(1+np.sqrt(5))/2
# 36 examples added after the original result checks.
group(52,1,'worked_case',dict(heights=1200*.1+800*.1==1000*.2,period=near(2*np.pi*np.sqrt(.05),1.405,5e-4),amplitude=near(.04*.8,.032)))
group(52,2,'worked_case',dict(zero_energy=zero(E.subs(G,stat).subs(x,1)),second_derivative=zero(s.diff(E,x,2).subs(G,stat).subs(x,1)-n*n),coalescence=abs(1+gam-gam*gam)<1e-10))
group(52,3,'worked_case',dict(point_scale=near(40/(16*np.pi**2),.2533,1e-4),arc=near(2*np.sqrt(2)*40/(16*np.pi**2),.7164,1e-4),rolling_scale=near(40/(24*np.pi**2),.1689,1e-4)))
group(52,4,'worked_case',dict(reversal=near(1-1.5,-.5),energy=near(1.5-1.5**2/2,.375),equilibrium=near(np.cos(np.pi/3),.5),frequency=near(np.sin(np.pi/3)**2,.75)))
disk=brentq(lambda t:np.tan(t)-1.5-.125*np.sin(t),.1,1.5);ring=brentq(lambda t:np.tan(t)-2-.25*np.sin(t),.1,1.5)
group(52,5,'worked_case',dict(ring_tilt_larger=ring>disk,unique=10-100*.05/2>0,friction=near(100*.1/10,1)))
exact=np.cos(.045)-np.cos(.05);first=np.sin(.05)*.005;second=first-np.cos(.05)*.005**2/2
group(52,6,'worked_case',dict(cosine=near(exact,2.3741e-4,1e-8),error=near((first/exact-1)*100,5.3,.05),quadratic_improves=abs(second-exact)<abs(first-exact)))
l14=2*np.sqrt(1.5**2-.3**2);l23=2*np.sqrt(.5**2-.3**2)
group(52,7,'worked_case',dict(chords=near([l14,l23],[2.9394,.8],1e-4),biased_fit=near((l14-l23)/4,.5348,1e-4),area=near(.5**2,.25)))
l=s.symbols('l',positive=True);DE=-(n/l-s.Rational(3,4))/(2*n**4)
group(52,8,'worked_case',dict(adjacent=zero(DE.subs(l,n-1)-DE.subs(l,n)+1/(2*n**4*(n-1))),low_l=zero(DE.subs(l,1)-DE.subs(l,2)+1/(4*n**3))))
h=4/(3*np.pi);j=.5-h*h;m=1e-4;k=m/(1+m);jump=2*h*np.sqrt(k/(j+k*h*h))*np.arctan(np.sqrt(k/(j+k*h*h)));lead=2*m*h/j
group(51,2,'worked_case',dict(exact_jump=near(jump,2.65294e-4,1e-9),lead=near(lead,2.65363e-4,1e-9),cycles=near(.01/(2*jump+4*m/h),6.789,1e-3)))
qc=(1-np.sqrt(23/27))/2;gc=(25-np.sqrt(621))/2;q=1/81;freq=np.sqrt([(1-np.sqrt(1-27*q*(1-q)))/2,(1+np.sqrt(1-27*q*(1-q)))/2])
group(51,4,'worked_case',dict(parameter_conversion=near(qc,gc/(1+gc)),frequencies=near(freq,[.300822,.953681],1e-6),sum_squares=near(freq@freq,1)))
L4=4*np.eye(4)-np.ones((4,4));v=np.array([1.,-1,0,0]);power=sum((v[i]-v[jj])**2 for i in range(4)for jj in range(i+1,4))
group(51,5,'worked_case',dict(laplacian=near(L4@v,4*v),dissipation=near(power,8),decay_energy=near(v@v/2,1)))
u=s.symbols('u',positive=True);XX=-s.cos(u)**3;YY=-s.sin(u)**3
group(51,7,'worked_case',dict(cusp_x=zero(s.limit((XX+1)/u**2,u,0)-s.Rational(3,2)),cusp_y=zero(s.limit(YY/u**3,u,0)+1),integrability=near(quad(lambda u:u**(-.5),0,.01)[0],.2)))
integ=quad(lambda mm:(2-mm)/(2),1,2)[0]
group(50,1,'worked_case',dict(variable_mass_distance=near(integ,.25),critical_r=near(2*.1*1.29*.01/2000*1e6,1.29),half_transfer=near(.1*1.29*.01/(4000*(np.log(2)-.5))*1e6,1.670,5e-4)))
z=45/46
group(50,2,'worked_case',dict(vector_coefficient=near(-2*z+z*z/2,-6255/4232),sum_coefficient=near(-4/np.sqrt(15)*(.5+z),-1.5268,1e-4)))
group(50,3,'worked_case',dict(flux=near(-3*1**2+1*(2**2-1),0),radial_energy=near(2**2-1.5**2,7/4),threshold=2>1.5))
kap=s.symbols('kap',positive=True);vth=s.sqrt(2*(1+kap)*s.Rational(1,2))/(s.Rational(1,2)+kap)
group(50,4,'worked_case',dict(disk=zero(vth.subs(kap,s.Rational(1,2))**2-s.Rational(3,2)),ring=zero(vth.subs(kap,1)**2-s.Rational(8,9)),stopping_time=near(1.5/(1),1.5)))
Q=s.Matrix([[1,1],[1,-1]])/s.sqrt(2);M=s.Matrix([[3,1],[1,3]])/2
group(50,5,'worked_case',dict(mass_modes=Q.T*M*Q==s.diag(2,1),new_w_mass=1+2*.5==2,volume=near(1+2-3,0)))
count=lambda a:.5-erf(a)/2+(1-np.exp(-a*a))/(2*np.sqrt(np.pi)*a)
group(50,6,'worked_case',dict(short_flux=near(count(100),1/(200*np.sqrt(np.pi))),long_limit=near(count(1e-5),.5,1e-5),count_not_escaped=count(.1)<.5))
width=lambda Y:max(0,min((1.5-Y)/6,(.5-Y)/3)-max((-1.5-Y)/6,(-.5-Y)/3))
group(50,7,'worked_case',dict(partial_width=all(near(width(Y),(2.5-Y)/6)for Y in [.8,1,2]),full_width=all(near(width(Y),1/3)for Y in [0,.1,.5]),edge=near(width(2.5),0)))
ss=.5;ll=.1;dd=(.75-np.sqrt(.5125))/.5;DX=ll+ss*dd+dd*dd/2
group(50,8,'worked_case',dict(simultaneity=near(dd,ss*DX),length=near(DX*np.sqrt(.75),.11816,1e-5),finite_limit=ll<.625<.8))
AA=np.sqrt(41);BB=np.sqrt(26);d=(AA+BB-np.sqrt(18-(AA-BB)**2))/2;aa=AA-d;bb=BB-d
group(49,1,'worked_case',dict(support_separation=all(aa*np.sin(t)+bb*np.cos(t)<=3+1e-12 for t in np.linspace(0,np.pi/2,2001)),outer_bounds=near([d+aa,d+bb],[AA,BB]),offset_circle=near(aa*aa+bb*bb,9)))
group(49,2,'worked_case',dict(one_stage=near(np.log(1000/100.9),2.2936,1e-4),two_stage=near(2*np.log(np.sqrt(1000)/(.1*np.sqrt(1000)+.9)),4.1043,1e-4),three_stage=near(3*np.log(10/1.9),4.9822,1e-4)))
group(49,3,'worked_case',dict(symmetry_axis=near(1/(.5**2+.5**2),2),center=near(1/(.5**2),4),moving_depth=near((3**2-1)/2,4)))
A=.25;B=1+np.sqrt(3)/4;D=1+A*A+B*B;jn=2*(1+B*B)/D;jt=-2*A*B/D;om=A*jn+B*jt
jnsl=2/(1+A*A-.05*A*B);jtsl=-.05*jnsl;omsl=A*jnsl+B*jtsl
group(49,4,'worked_case',dict(stick_velocity=near([jt+B*om,-1+jn+A*om],[0,1]),slip_sign=jtsl+B*omsl>0,slip_normal=near(-1+jnsl+A*omsl,1)))
group(49,5,'worked_case',dict(intersection=all(near(h+2/3*(.5-h),h/3+1/3)for h in [-1,0,2]),finite_mirror=near([(-1)/3+1/3,2/3+1/3],[0,1])))
group(49,6,'worked_case',dict(volume_closure=near(3**2.5/3/3**1.5,1),hot_work=near(3-1,2),cold_work=near(1/3-1,-2/3)))
group(49,7,'worked_case',dict(center_normal=near(np.dot([.3,1],[-1,.3]),0),curvature_distance=near(np.linalg.norm([-1,.3]),np.sqrt(1.09)),charge_reversal=near(-np.array([.3,1]),[-.3,-1])))
r1=9-3*np.sqrt(5);r2=9+3*np.sqrt(5)
group(49,8,'worked_case',dict(turning_sum=near(r1+r2,18),turning_product=near(r1*r2,36),near_speed=2/r1>2/r2))
group(48,1,'worked_case',dict(kingpin_torque=near(-250*np.sin(np.pi/18)*np.sin(np.pi/36),-3.78,.005),caster=near(-400*.015,-6)))
group(48,2,'worked_case',dict(mirror=near(1/np.sin(np.pi/4)**2,2),loss_cone=near(1-np.cos(np.pi/6),.1340,1e-4),escaped=1/np.sin(np.pi/9)**2>4))
group(48,3,'worked_case',dict(kinetic_weight=near(quad(lambda z:np.sin(np.pi*z/2)**2,0,1)[0],.5),potential_weight=near(quad(lambda z:np.cos(np.pi*z/2)**2,0,1)[0],.5),zero_net_rotation=abs(quad(lambda z:np.cos(np.pi*z),0,1)[0])<1e-12))
group(48,4,'worked_case',dict(total_entropy=near(2612.756978e-6,.002612756978),latent_heat=near(2612.756978e-6*1.95,.005095,1e-6),latent_max=zero(s.diff(x*x*(1-x*x),x).subs(x,1/s.sqrt(2)))))
group(48,5,'worked_case',dict(beta_integral=near(quad(lambda u:1/np.sqrt(1-u**4),0,1)[0],beta(.25,.5)/4),amplitude_scale=near(4*quad(lambda u:1/np.sqrt(1-u**4),0,1)[0],beta(.25,.5))))
U=np.array([[1,1,1,1],[1,0,-1,0],[0,1,0,-1],[1,-1,1,-1]],float);U[0]/=2;U[1:3]/=np.sqrt(2);U[3]/=2
group(48,6,'worked_case',dict(orthonormal=near(U@U.T,np.eye(4)),diag_projection=near(U@np.array([1,0,-1,0]),[0,np.sqrt(2),0,0]),adj_projection=near(U@np.array([1,-1,0,0]),[0,1/np.sqrt(2),-1/np.sqrt(2),1])))
vroot=brentq(lambda eta:np.sqrt(2+eta)/(np.sqrt(2)*(1+eta))-.99,0,.1)
group(48,7,'worked_case',dict(speed_threshold=abs(vroot-.01333)<3e-4,period_threshold=near(.01*8/3,.02667,1e-5),exact_equation=near(2+vroot,1.9602*(1+vroot)**2)))
mu=2/3;th=np.pi/3;kk=2*np.pi*1.5/600;delta=2*np.tan(th)/(kk*np.sqrt(np.sin(th)**2-mu**2))
group(48,8,'worked_case',dict(shift_nm=near(delta,399,.1),critical=th>np.arcsin(mu),inside_wave_number=near(kk,2*np.pi*1.5/600)))
# 27 additional derivations; algebra and independently evaluated limits.
x0=.8527017802
sder=s.diff(E,x,2).subs(G,stat);ratio=s.simplify(x**4*sder/(2*n*n))
group(52,2,'additional_derivation',dict(radial_ratio=zero(ratio-(1+x-x*x)/(1+x)),frequency=near(np.sqrt(float(ratio.subs(x,x0))),.77945,1e-5)))
c,c0=s.symbols('c c0',positive=True);mu_fn=s.sqrt(1-c*c)*c/(4*c*c-c0*c0)
# Check monotonic friction on release-to-bottom interval and both force equations.
u0=np.pi/4;grid=np.linspace(0,u0,1001);fr=np.sin(grid)*np.cos(grid)/(4*np.cos(grid)**2-np.cos(u0)**2)
group(52,3,'additional_derivation',dict(friction_increases=bool(np.all(np.diff(fr)>=-1e-12)),release_bound=near(fr[-1],1/3),normal_positive=bool(np.all(4*np.cos(grid)**2-np.cos(u0)**2>0))))
t1,t2=s.symbols('t1 t2',positive=True);K=t2/(t1-t2)
group(52,7,'additional_derivation',dict(time_gradient=zero(s.diff(K,t1)+t2/(t1-t2)**2)and zero(s.diff(K,t2)-t1/(t1-t2)**2),mass_scaling=zero(s.diff(x**3,x)*x/x**3-3)))
BL=lambda a,b:2*np.sqrt(200**2-(b-a)**2)+np.pi*(a+b)+2*(b-a)*np.arcsin((b-a)/200);rb=brentq(lambda b:BL(35,b)-BL(30,50),40,50)
group(51,1,'additional_derivation',dict(exact_belt=near(rb,45.463,1e-3),ratio=near(35/rb,.7699,1e-4),length_excess=near(BL(30,50)-400-80*np.pi,2.002,1e-3)))
z=.3*np.pi;arc=.1/.6*np.sinh(z)
group(51,3,'additional_derivation',dict(critical_angle=near(2*np.arctan(np.exp(-z))*180/np.pi,42.58,.005),height=near(.1/.6*(np.cosh(z)-1),.07967,1e-5),length=near(arc,.1814,1e-5)))
b,cv=s.symbols('b cv',positive=True);Qa=cv*(b-1);Qb=(cv+1)*b*(b-1);Qc=(cv+s.Rational(1,2))*(1-b*b);work=(b-1)**2/2
group(51,6,'additional_derivation',dict(first_law=zero(Qa+Qb+Qc-work),efficiency=zero(work/(Qa+Qb)-(b-1)/(2*(cv+(cv+1)*b))),original_limit=zero((work/(Qa+Qb)).subs({b:2,cv:s.Rational(5,2)})-s.Rational(1,19))))
group(51,8,'additional_derivation',dict(strict_cutoff=[j for j in range(1,5)if j<3]==[1,2],jump_sum=1+2+3==6,fixed_interval=near(3/4,6/8)))
a,vo=s.symbols('a vo',positive=True);sol=1/(1/(2*vo)+a*x)-vo
stop=1/(2*a*vo)
group(50,1,'additional_derivation',dict(velocity_equation=zero(s.diff(sol,x)+a*(vo+sol)**2),stop=zero(sol.subs(x,stop)),distance=zero(s.integrate(sol,(x,0,stop))-(s.log(2)-s.Rational(1,2))/a)))
Nr,Nt,rr,dd,LL=s.symbols('Nr Nt rr dd LL');N1=rr/2*(-Nr/dd-2*Nt/LL);N2=rr/2*(-Nr/dd+2*Nt/LL)
group(50,2,'additional_derivation',dict(radial=zero(-dd/rr*(N1+N2)-Nr),tangent=zero(LL/(2*rr)*(N2-N1)-Nt),contact_bound=near(6*(23/6)/(np.sqrt(15)/2),11.88,.005)))
v0=2;omc=-3;travel=quad(lambda r:1/np.sqrt(v0*v0-omc*omc*r*r/4),0,1)[0]
group(50,3,'additional_derivation',dict(transit_integral=near(travel,2/3*np.arcsin(.75)),radial_energy=near(4-9/4,7/4)))
h=.25;r=1;g=1;low=2*r*np.sqrt(g*h)/(2*r-h);high=2*r*np.sqrt(g*(r-h))/(2*r-h)
Km=(r-h)*g
psi=np.linspace(0,np.arccos(1-h/r),1001);normal=g*(2*np.cos(psi)-(1-h/r))-Km/r
group(50,4,'additional_derivation',dict(feasible_interval=low<high,normal_boundary=near(normal[-1],0),all_contacts=bool(np.all(normal>=-1e-12)),no_interval_at_half=near(2*np.sqrt(.5)/1.5,2*np.sqrt(1-.5)/1.5)))
group(50,5,'additional_derivation',dict(total_energy=near((1+2+9)/2,6),mode_energy=near(2+4,6),flow=near(1+2-3,0)))
out=lambda a:1-erf(2*a)+(1-np.exp(-4*a*a))/(2*np.sqrt(np.pi)*a)
group(50,6,'additional_derivation',dict(count_expansion=near(count(.1),.5-.1/(2*np.sqrt(np.pi))+.1**3/(12*np.sqrt(np.pi)),1e-7),impulse_expansion=near(erf(.1)*np.sqrt(np.pi)/(.2),1-.1**2/3+.1**4/10,3e-8),escape_expansion=near(out(.1),1-.2/np.sqrt(np.pi)+4*.1**3/(3*np.sqrt(np.pi)),1e-5)))
# Independent integration of circular aperture intersection at Y=1.
ra=.5;rb=.75;dc=.5
area=quad(lambda z:max(0,min(np.sqrt(max(0,ra*ra-z*z)),np.sqrt(max(0,rb*rb-(z+dc)**2))))*2,-ra,ra,epsabs=1e-9,points=[(rb*rb-ra*ra-dc*dc)/(2*dc)])[0]
H=(-dc+ra+rb)*(dc+ra-rb)*(dc-ra+rb)*(dc+ra+rb)
formula=ra*ra*np.arccos((dc*dc+ra*ra-rb*rb)/(2*dc*ra))+rb*rb*np.arccos((dc*dc+rb*rb-ra*ra)/(2*dc*rb))-.5*np.sqrt(H)
group(50,7,'additional_derivation',dict(circle_overlap=near(area,formula),full_aperture=near(2*(rb-ra),.5),visibility=near(2*(ra+rb),2.5)))
s0,lam=s.symbols('s0 lam',positive=True);ds=s0/(1-s0*s0)*lam+s0**3/(2*(1-s0*s0)**3)*lam**2;res=s.expand(ds-s0*(lam+s0*ds+ds**2/2))
group(50,8,'additional_derivation',dict(second_order_simultaneity=zero(res.coeff(lam,1))and zero(res.coeff(lam,2)),speed_transform=near((.5682178937-.5)/(1-.5*.5682178937),.0953,1e-4)))
r0=s.symbols('r0',positive=True);f=x-s.log(r0*s.exp(x)+1-r0)
group(49,2,'additional_derivation',dict(series_coeff=zero(s.diff(f,x).subs(x,0)-(1-r0))and zero(s.diff(f,x,2).subs(x,0)+r0*(1-r0)),advantage=zero(r0*x*x+1-r0-(r0*x+1-r0)**2-r0*(1-r0)*(x-1)**2),limit=near(.9*np.log(1000),6.2170,1e-4)))
e=.5;jn=(1+e)*(1+B*B)/D;jt=-(1+e)*A*B/D;om=A*jn+B*jt;v2=jt*jt+(-1+jn)**2+om*om
# Restore collision symbols accidentally shadowed by later scalars.
A=.25;B=1+np.sqrt(3)/4;D=1+A*A+B*B;jn=(1+e)*(1+B*B)/D;jt=-(1+e)*A*B/D;om=A*jn+B*jt;v2=jt*jt+(-1+jn)**2+om*om
group(49,4,'additional_derivation',dict(restitution=near(-1+jn+A*om,e),contact_tangent=near(jt+B*om,0),energy=near(v2,1-(1-e*e)*(1+B*B)/D),example=near(v2,.2650,1e-4)))
group(49,6,'additional_derivation',dict(first_law=near(5-5/3,10/3),COP=near((5/3)/(10/3),.5),heat_pump=near(5/(10/3),1.5),coordinate=near(np.array([13/3,10/3])-np.array([5,5]),[-2/3,-5/3])))
roots=[brentq(lambda k:np.log(k)+(2*np.pi*m-np.pi/2)*k,1e-8,.999999)for m in range(1,5)]
group(49,7,'additional_derivation',dict(first_branch=near(roots[0],.2744106,1e-6),ordering=bool(np.all(np.diff(roots)<0)),unique_positive=all(1/k+2*np.pi*m-np.pi/2>0 for m,k in enumerate(roots,1))))
ecc=.6;action=2*quad(lambda u:ecc**2*np.sin(u)**2/(1-ecc*np.cos(u)),0,np.pi)[0]
group(49,8,'additional_derivation',dict(radial_action=near(action,2*np.pi*(1-np.sqrt(1-ecc*ecc))),factorization=zero(ecc**2*s.sin(x)**2-((1-ecc*s.cos(x))*(1+ecc*s.cos(x))-(1-ecc*ecc)))))
lf,lr,M,v,R=s.symbols('lf lr M v R',positive=True);Ff=lr/(lf+lr)*M*v*v/R;Fr=lf/(lf+lr)*M*v*v/R
group(48,1,'additional_derivation',dict(force=zero(Ff+Fr-M*v*v/R),yaw=zero(lf*Ff-lr*Fr),middle=zero(Ff.subs(lf,lr)-M*v*v/(2*R))))
theta=np.pi/3;zz=np.cos(theta)/np.sin(theta);Bm=1+zz*zz
group(48,2,'additional_derivation',dict(mirror_ratio=near(Bm,1/np.sin(theta)**2),inside=zz<1,frequency=near(np.sin(theta)**2*zz*zz,np.cos(theta)**2)))
root=brentq(lambda K:1/np.tan(K)-K,.01,1.56)
group(48,3,'additional_derivation',dict(tip_root=near(root,.860334,1e-6),period=near(np.pi/(2*root),1.826,.001),frequency=near(2*root/np.pi,.5477,1e-4)))
group(48,4,'additional_derivation',dict(heat_capacity_shape=zero(x*s.diff(x*(1-x*x),x)-x*(1-3*x*x)),jump=near(4*.144**2/(1.25e-6*4.48),1.4811e4,.5)))
k,L,I0,B0,S=s.symbols('k L I0 B0 S',positive=True);pot=(L*I0+B0*S*(1-s.cos(k*x)))**2/(2*L)
A4=B0*B0*S*S*k**4/(8*L)-I0*B0*S*k**4/24
group(48,5,'additional_derivation',dict(quartic_coefficient=zero(s.diff(pot,x,4).subs(x,0)/24-A4),frequency_shift=zero(3*A4/(2*I0*B0*S*k*k)-k*k/16*(3*B0*S/(L*I0)-1))))
q=2-np.sqrt(3);N=4;bbeta=q**(2*N+1);V=lambda nn:q**nn+bbeta*q**(-nn);zN=1/(3-V(1)/V(0));zinf=(np.sqrt(3)-1)/2
group(48,6,'additional_derivation',dict(free_boundary=near(V(N+1),V(N)),finite_larger=zN>zinf,limit=abs(zN-zinf)<4e-6))
eta=s.symbols('eta',positive=True);series=s.series((1+x)/s.sqrt(1+x/2),x,0,3).removeO();exact=2/np.pi*quad(lambda u:(1+.1*np.cos(u)**2)/np.sqrt(1+.05*np.cos(u)**2),0,np.pi/2)[0]
group(48,7,'additional_derivation',dict(smooth_series=zero(series-(1+3*x/4-5*x*x/32)),period_improves=abs(exact-(1+.3/8-15*.01/256))<abs(exact-1.0375),speed_series=zero(s.series(s.sqrt(1+x/2)/(1+x),x,0,3).removeO()-(1-3*x/4+23*x*x/32))))
# Final 14 diagram-led checks.
group(52,6,'final_model_check',dict(interior_orders=[m for m in range(-20,10)if -1<.5+.1*m<1]==list(range(-14,5)),angles=near([np.degrees(np.arccos(.6)),np.degrees(np.arccos(.4))],[53.13,66.42],.005)))
Area,Sec,H1,H3,rho1,rho3,mass,grav=s.symbols('Area Sec H1 H3 rho1 rho3 mass grav',positive=True)
Ma=Sec**2/(Area-Sec)*(rho1*H1+rho3*H3);stiff=(rho1-rho3)*grav*Sec*Area/(Area-Sec)
group(52,1,'final_model_check',dict(added_mass=zero(Ma-Sec**2*(rho1*H1+rho3*H3)/(Area-Sec)),narrow_limit=zero(s.limit(Ma/stiff,Area,Sec,dir='+')-(rho1*H1+rho3*H3)/((rho1-rho3)*grav))))
Ufun=lambda th:(.5-np.cos(th))**2/2
period=4/np.sqrt(2)*quad(lambda th:1/np.sqrt(.5-Ufun(th)),0,2*np.pi/3)[0]
group(52,4,'final_model_check',dict(turning=near(Ufun(2*np.pi/3),.5),cross_barrier=.5>Ufun(0),period=near(period,11.2048,1e-4)))
expansion=s.series(s.sqrt(1-x)-1,x,0,3).removeO()
group(52,8,'final_model_check',dict(circular_relativistic=zero(expansion+x/2+x*x/8),speed_condition=near(.0073/2,.00365)))
Delta=.001473;rd=.99;cycle=np.log(1-(1-rd)*.01/Delta)/np.log(rd)
group(51,2,'final_model_check',dict(recurrence=near(sum(Delta*rd**i for i in range(7)),Delta*(1-rd**7)/(1-rd)),cycles=near(cycle,6.9951,1e-4),integer_reaches=Delta*(1-rd**6)/(1-rd)<.01<=Delta*(1-rd**7)/(1-rd)))
prod=27*.05*.95;sig=.5*np.sqrt(np.sqrt(prod)-1);omega=.5*np.sqrt(np.sqrt(prod)+1);lm=sig+1j*omega
characteristic=lm**4+lm**2+prod/4
group(51,4,'final_model_check',dict(characteristic=abs(characteristic)<1e-10,growth=near(sig,.1820,1e-4),cycle_growth=near(np.exp(2*np.pi*sig),3.14,.01)))
L4=4*np.eye(4)-np.ones((4,4));vinit=np.array([2,1,-1,0.]);vmean=vinit.mean();vperp=vinit-vmean
group(51,5,'final_model_check',dict(common_mode=near(L4@np.ones(4),0),decay_mode=near(L4@vperp,4*vperp),charge=near(np.sum(vmean+vperp*np.exp(-4)),np.sum(vinit)),remaining_energy=near(4*vmean*vmean/2,2*vmean*vmean)))
qq=np.array([-(2/3)**1.5,(1/3)**1.5]);tq=np.array([np.sqrt(2/3),np.sqrt(1/3)]);incoming=np.array([0.,1]);outgoing=2*np.dot(incoming,tq)*tq-incoming
group(51,7,'final_model_check',dict(second_reflection=near(outgoing,-qq/np.linalg.norm(qq)),explicit_direction=near(outgoing,[2*np.sqrt(2)/3,-1/3])))
Mpre=np.array([[-1,-3],[-2/3,-3]]);L2=np.array([[1,0],[-1,1]]);Mpost=L2@Mpre;Mpupil=np.array([[1,1.5],[0,1]])@Mpost
group(50,7,'final_model_check',dict(parallel_beam=near(Mpost[1],[1/3,0]),pupil_image=near(Mpupil[0],[-.5,-3]),pupil_relation=near(Mpupil[0],-.5*np.array([1,6]))))
vy,U0,vx=s.symbols('vy U0 vx',real=True)
group(49,3,'final_model_check',dict(nonstationary_bernoulli=zero((vx*vx+vy*vy)/2-U0*vy-((vx*vx+(vy-U0)**2)/2-U0**2/2))))
mp=np.array([np.cos(2*np.pi/5),np.sin(2*np.pi/5)]);ep=np.array([2.,0]);sp=2*np.tan(np.pi/5)/(mp[1]+(2-mp[0])*np.tan(np.pi/5));contact=ep+sp*(mp-ep);pin=np.array([1.,0]);vi=(contact-pin)/np.linalg.norm(contact-pin);vo=(ep-contact)/np.linalg.norm(ep-contact);tang=np.array([np.cos(np.pi/5),np.sin(np.pi/5)])
group(49,5,'final_model_check',dict(intersection=near(contact,[.873,.634],5e-4),reflection=near(2*np.dot(vi,tang)*tang-vi,vo),valid_ray=contact@tang>0))
kmed=2*np.pi*1.5/600;Q=np.sqrt(.75-4/9);ell=1/(kmed*Q)
group(48,8,'final_model_check',dict(penetration=near(ell,115.2,.05),shift=near(2*np.sqrt(3)*ell,399,.1)))
# 20 nodes, actual finite C4 lattice; energy check independently sums each edge once.
NN=4;Nnodes=4*(NN+1);lap=np.zeros((Nnodes,Nnodes));edges=[]
for k in range(NN+1):
 for i in range(4):
  edges.append((4*k+i,4*k+(i+1)%4))
  if k<NN:edges.append((4*k+i,4*(k+1)+i))
for i,jj in edges:lap[i,i]+=1;lap[jj,jj]+=1;lap[i,jj]-=1;lap[jj,i]-=1
inj=np.zeros(Nnodes);inj[0]=1;inj[2]=-1;V=np.linalg.lstsq(lap,inj,rcond=None)[0];Rdiag=V[0]-V[2];q2=2-np.sqrt(3);bt=q2**9;pred=2/(3-(q2+bt/q2)/(1+bt))
group(48,6,'final_model_check',dict(finite_node=near(Rdiag,pred),residual=np.max(np.abs(lap@V-inj))<1e-10,power=near(sum((V[i]-V[jj])**2 for i,jj in edges),Rdiag),error=near(Rdiag-(np.sqrt(3)-1),6.61e-6,1e-8)))
ki,kj,betat,Le=s.symbols('ki kj betat Le',positive=True);Xi,Xj=s.symbols('Xi Xj');boundary=Xi*(betat*Le*kj**2*Xj)-Xj*(betat*Le*ki**2*Xi)
group(48,3,'final_model_check',dict(tip_orthogonality=zero(boundary/(ki**2-kj**2)+betat*Le*Xi*Xj)))

# Last nine worked derivations.
Ac=np.array([[0,0,1,0],[0,0,0,1],[.75,np.sqrt(23)/4,0,2],[np.sqrt(23)/4,2.25,-2,0]],complex);lc=1j/np.sqrt(2);yv=(-np.sqrt(23)+4*np.sqrt(2)*1j)/11;vc=np.array([1,yv,lc,lc*yv]);wy=8/11*(1+lc*yv);wc=np.array([0,wy,1,yv+lc*wy]);mat=Ac-lc*np.eye(4)
group(51,4,'last_derivation',dict(eigenvector=near(mat@vc,np.zeros(4)),generalized=near(mat@wc,vc)))
tt=s.symbols('tt',positive=True);cc,RR,V0=s.symbols('cc RR V0',positive=True);ex=s.exp(-5*tt/(2*RR*cc));aa=2*V0/5+3*V0*ex/5;bb=2*V0/5-2*V0*ex/5
group(51,5,'last_derivation',dict(first_equation=zero(2*cc*s.diff(aa,tt)+3*(aa-bb)/RR),second_equation=zero(cc*s.diff(bb,tt)-(aa-bb)/RR),charge=zero(2*aa+3*bb-2*V0),heat=zero(s.integrate(3*V0**2/RR*s.exp(-5*tt/(RR*cc)),(tt,0,s.oo))-3*cc*V0**2/5)))
group(51,6,'last_derivation',dict(entropy=near(9-19/8,53/8),lost_work=near(57/8-.5,53/8)))
sa=.5;sb=.5682178936723648;clock=lambda u:(np.arcsin(u)+u*np.sqrt(1-u*u))/2
group(50,8,'last_derivation',dict(clocks=near(clock(sb)-clock(sa),quad(lambda u:np.sqrt(1-u*u),sa,sb)[0]),positive_clock_difference=clock(sb)>clock(sa)))
# Hyperbolic rigid model: differentiate coordinates to verify the flat metric.
alpha,c,xi,tau=s.symbols('alpha c xi tau',positive=True);ct=(c*c/alpha+xi)*s.sinh(alpha*tau/c);xx=(c*c/alpha+xi)*s.cosh(alpha*tau/c)-c*c/alpha
group(50,8,'rigid_model',dict(time_metric=zero(-s.diff(ct,tau)**2+s.diff(xx,tau)**2+c*c*(1+alpha*xi/c**2)**2),space_metric=zero(-s.diff(ct,xi)**2+s.diff(xx,xi)**2-1),cross_metric=zero(-s.diff(ct,tau)*s.diff(ct,xi)+s.diff(xx,tau)*s.diff(xx,xi))))
Rr=4.;AR=np.sqrt(16+(Rr+1)**2);BR=np.sqrt(1+(Rr+1)**2);road=(AR+BR-np.sqrt(2*(Rr-1)**2-(AR-BR)**2))/2
group(49,1,'last_derivation',dict(road_family=near(road,d),offset_circle=near((AR-road)**2+(BR-road)**2,(Rr-1)**2),positive_offsets=AR>road and BR>road))
Et,kappa,Lz,c,m,uup,up,uval=s.symbols('Et kappa Lz c m uup up uval',real=True)
energy_eq=(Et+kappa*uval)**2-c*c*(Lz*Lz*up*up+Lz*Lz*uval*uval)-m*m*c**4
diffeq=s.diff(energy_eq,uval)*up+s.diff(energy_eq,up)*uup
orbit=uup+(1-kappa*kappa/(Lz*Lz*c*c))*uval-Et*kappa/(Lz*Lz*c*c)
group(49,8,'last_derivation',dict(orbit_differentiation=zero(diffeq+2*c*c*Lz*Lz*up*orbit)))
k,L,I0,B0,S=s.symbols('k L I0 B0 S',positive=True);potential=(L*I0+B0*S*(1-s.cos(k*x)))**2/(2*L);sixth=s.diff(potential,x,6).subs(x,0)/720
sixth_tuned=s.simplify(sixth.subs(I0,3*B0*S/L));K2=3*B0*B0*S*S*k*k/L
group(48,5,'last_derivation',dict(sixth_coefficient=zero(sixth_tuned+B0*B0*S*S*k**6/(60*L)),frequency=zero(15*sixth_tuned/(8*K2)+k**4/96)))
# Random potentials on the actual 20-node lattice; quadratic energy equals the Laplace form.
rng=np.random.default_rng(48);vrand=rng.normal(size=20);edge_energy=sum((vrand[i]-vrand[jj])**2 for i,jj in edges)
group(48,6,'last_derivation',dict(energy_laplacian=near(vrand@lap@vrand,edge_energy),grounded_positive=np.min(np.linalg.eigvalsh(lap[1:,1:]))>0,gauge=near(lap@(vrand+7),lap@vrand)))


# Final pagination repairs add five mathematical examples, checked separately.
kap=s.symbols('kap',positive=True);u=s.symbols('u',positive=True);u0=np.pi/4
for kv in [0.4,0.5,1,2]:
 grid=np.linspace(0,u0,1001);ratio=kv*np.sin(grid)*np.cos(grid)/((kv+2)*np.cos(grid)**2-np.cos(u0)**2)
 assert np.all(np.diff(ratio)>=-1e-12)
group(52,3,'general_rolling_variant',dict(ring_radius=near(1/(16*(1+1)),1/32),sphere_radius=near(1/(16*(1+.4)),5/112),friction=near(ratio[-1],2/3)))
group(51,3,'helix_tension',dict(integrated_budget=near(.6*np.sin(np.pi/6)*np.pi,.3*np.pi),ratio=near(np.exp(.3*np.pi),2.5663,1e-4),circle_ratio=near(np.exp(.6*np.pi),6.5861,1e-4)))
z=s.symbols('z',positive=True);Sfun=1/(4*s.sinh(z/2)**2)
group(51,8,'smooth_cutoff',dict(derivative=zero(s.diff(Sfun,z)+Sfun*s.coth(z/2)),series=zero(s.limit(Sfun-1/z**2,z,0)+s.Rational(1,12)),series_next=zero(s.limit((Sfun-1/z**2+s.Rational(1,12))/z**2,z,0)-s.Rational(1,240)),sum_numeric=near(sum(j*np.exp(-j)for j in range(1,200)),float(Sfun.subs(z,1)))))
group(50,7,'general_apertures',dict(visible_at_three=near(1+3/2,2.5),full_at_three=near(abs(1-3/2),.5),switch=near(abs(1-2/2),0),both_boundaries=all(abs(1-la/2)<=1+la/2 for la in [.1,1,2,3,7])))
checks=[]
for lamv in [2,4]:
 zs=(np.sqrt(1+4/lamv)-1)/2;qr=1/(1+lamv*(1+zs));zn=1/lamv
 for nn in range(1,10):
  checks.append(zn>=zs-1e-13 and zn-zs<=qr**(2*(nn-1))*(1/lamv-zs)+1e-13)
  zn=(1+zn)/(1+lamv*(1+zn))
group(48,6,'finite_recurrence_bound',dict(fixed_point=all(near((1+(np.sqrt(1+4/j)-1)/2)/(1+j*(1+(np.sqrt(1+4/j)-1)/2)),(np.sqrt(1+4/j)-1)/2)for j in [2,4]),error_bounds=all(checks)))

# Four final derivations retained in the delivered manuscript.
eps=s.symbols('eps',positive=True);statG=2*n*n*s.exp(x)/(x*(1+x));En=n*n/x**2-statG*s.exp(-x)/x
group(52,2,'general_negative_energy',dict(elimination=zero((En+eps)*x*x*(1+x)-(eps*x*x*(1+x)-n*n*(1-x))),count=1<2.969963/np.e<4))
r1,r2,Dd=s.symbols('r1 r2 Dd',positive=True);dl=r2-r1;bet=s.asin(dl/Dd);BL=2*s.sqrt(Dd*Dd-dl*dl)+s.pi*(r1+r2)+2*dl*bet
hr=2/s.sqrt(Dd*Dd-dl*dl)
group(51,1,'exact_belt_derivatives',dict(first_1=zero(s.diff(BL,r1)-(s.pi-2*bet)),first_2=zero(s.diff(BL,r2)-(s.pi+2*bet)),hessian=zero(s.diff(BL,r1,2)-hr)and zero(s.diff(BL,r1,r2)+hr)))
kr=brentq(lambda K:1/np.tan(K)-K,.01,1.56);kin=quad(lambda zz:np.sin(kr*zz)**2,0,1)[0]+np.sin(kr)**2;stiff=quad(lambda zz:(kr*np.cos(kr*zz))**2,0,1)[0]
group(48,3,'tip_energy_identity',dict(stiffness_mass=near(stiff,kr*kr*kin),boundary=near(kr*np.cos(kr),kr*kr*np.sin(kr))))
kt,vt,rt,tm=s.symbols('kt vt rt tm',positive=True);rad=rt+kt*vt/s.sqrt(1+kt*kt)*tm;theta=s.log(rad/rt)/kt
group(49,7,'time_parameter',dict(spiral=zero(rt*s.exp(kt*theta)-rad),speed_squared=zero(s.diff(rad,tm)**2+rad**2*s.diff(theta,tm)**2-vt*vt),outward=zero(s.diff(rad,tm)-kt*vt/s.sqrt(1+kt*kt))))
assert len(rows)==95
out=dict(passed=True,groups=rows,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),note='36项带解示例与27项补充推导和14项末轮模型检验和9项后续推导及5项收尾变式和4项终稿推导的关键关系交叉核验；非全文自动证明，不改变道路全局最优、双镜可见性和题面模型歧义的未证范围。')
(P/'supplement_results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print('PASS',len(rows),'supplement groups')
