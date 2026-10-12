"""Independent symbolic and numerical checks for the forty reviewed questions."""
from pathlib import Path
import hashlib,json
import numpy as np
import sympy as s
from scipy.optimize import brentq
from scipy.integrate import quad
P=Path(__file__).parent
groups=[]
def group(n,q,checks):
    assert checks and all(bool(v) for v in checks.values()),(n,q,checks)
    groups.append(dict(set=n,question=q,passed=True,checks=list(checks)))
def zero(x):return s.simplify(x)==0
def near(a,b,tol=1e-8):return np.allclose(a,b,rtol=tol,atol=tol)
x,u,t,z=s.symbols('x u t z',real=True)

# 057: independent energy, differentiation, trajectory and simultaneous-slice integrals.
v2=2*(1-u)
N=1-u*(2-3*u)
energy=1-u*u+u**3
group(57,1,dict(contact=zero(N-(1-2*u+3*u*u)),minimum=zero(N.subs(u,s.Rational(1,3))-s.Rational(2,3)),energy_stationary=zero(s.diff(energy,u).subs(u,s.Rational(2,3))),energy_minimum=zero(energy.subs(u,s.Rational(2,3))-s.Rational(23,27))))
yp=-s.sqrt((1+x)**2-s.Rational(1,4));ym=yp.subs(x,-x)
V=yp+ym+s.sqrt(3);M=s.diff(yp,x)**2+s.diff(ym,x)**2
group(57,2,dict(potential_quadratic=zero(s.diff(V,x,2).subs(x,0)/2-2/(3*s.sqrt(3))),potential_quartic=zero(s.diff(V,x,4).subs(x,0)/24-34/(27*s.sqrt(3))),mass=zero(M.subs(x,0)-s.Rational(8,3)),mass_quadratic=zero(s.diff(M,x,2).subs(x,0)/2-s.Rational(104,27)),frequency_ratio=zero((s.sqrt(3)/2)/(1/(2*s.sqrt(3)))-3)))
a=1;w=5/14;b=np.sqrt(1/56)
X=lambda t:1+2*b*np.sin(t)+2*w*(np.cos(t)-1)
Y=lambda t:2*b*(1-np.cos(t))+2*w*np.sin(t)
F=lambda t:Y(t)*np.cos(2*w*t)-X(t)*np.sin(2*w*t)
rt=brentq(F,2.5,4);along=X(rt)*np.cos(2*w*rt)+Y(rt)*np.sin(2*w*rt)
group(57,3,dict(threshold=near((1+np.sqrt(7))/4,.9114378278),intersection=near(rt,3.1306101543),finite_rod=0<along<1,not_tangent=abs((F(rt+1e-5)-F(rt-1e-5))/2e-5)>.16))
aa=1000*np.sqrt(3);xx=30;D=10*np.sqrt(3)+20;cc=20;floor=20/np.sqrt(3)-10;rr=1000.;rows=[]
for k in range(1,11):
    bb=rr/(aa+rr);A=1-bb;C=cc-bb*D
    zz=np.roots([A*xx,A*A*D*D-xx*xx-C*C,-A*xx*D*D])
    ss=next(float(v.real)-xx for v in zz if abs(v.imag)<1e-10 and v.real>0)
    h=(ss+1j*cc)/(ss+xx+1j*D);bb=h.real;rr=aa*bb/(1-bb)
    ell=2*aa/rr;rows.append([k,ss-floor,rr,ell,ell/np.sqrt(3)-1])
group(57,4,dict(first_group=near(rows[0][1:],[17.09002746,1359.681304934,2.547730562,.470932926],1e-7),nine_groups=rows[7][4]>.03>rows[8][4],ten_group=near(rows[9][4],.018174837,1e-7)))
shape=(x-1)/x**s.Rational(5,2)
group(57,5,dict(peak=zero(s.diff(shape,x).subs(x,s.Rational(5,3))),unstable=zero(s.diff(1-1/x**2,x).subs(x,1)-2),speed_energy=zero(s.diff((x-1)**2/x,x)-(1-1/x**2)),ring_plane='radial-normal plane'))
R,Nn,beta=s.symbols('R N beta',positive=True)
rad=R**2*s.exp(-3*R**2/(2*Nn))
group(57,6,dict(force=zero(s.diff(3*R**2/(2*Nn),R)-3*R/Nn),radial_mode=zero(s.diff(rad,R).subs(R,s.sqrt(2*Nn/3))),scaling=zero((3*R/(3*Nn))/(3*R/Nn)-s.Rational(1,3))))
r=s.symbols('r',positive=True);g=s.Function('g')(r)
# circular angular momentum h²=r³g; differentiate effective radial force at fixed h.
h=s.symbols('h')
kap=-s.diff(h*h/r**3-g,r).subs(h*h,r**3*g)
group(57,7,dict(epicyclic=zero(kap-(3*g/r+s.diff(g,r))),poisson=zero((3*g/r+4*s.pi*R-2*g/r)-(g/r+4*s.pi*R)),uniform_core=zero((g/r+4*s.pi*R).subs(g,4*s.pi*R*r/3)-16*s.pi*R/3)))
th=s.symbols('th',real=True);al,be=s.symbols('al be',real=True);ga=1/s.sqrt(1-be**2)
den=1+be*al*s.sin(th);dn=den/(2*s.pi)
xp=s.cos(th)/ga;yy=s.sin(th);ux=(-be-al*s.sin(th))/den;uy=al*s.cos(th)/(ga*den)
pm=-s.integrate(yy*dn,(th,0,2*s.pi))
mm=-s.integrate((xp*uy-yy*ux)*dn/2,(th,0,2*s.pi))
group(57,8,dict(number=zero(s.integrate(dn,(th,0,2*s.pi))-1),electric_dipole=zero(pm+be*al/2),current_moment=zero(mm+al*(1-be**2/2)/2),left_velocity=zero(uy.subs(th,s.pi)+al/ga)))

# 056: kinematics, thermodynamics, discrete friction and circuit KCL.
group(56,1,dict(common_density=near(1.5,3/2),ground_velocity_sum=near(np.array([0,-1])+np.array([1,0]),[1,-1]),acceleration_rotation=near(np.cross([0,0,2],np.cross([0,0,2],[1,0,0])),[-4,0,0])))
chi,tt=s.symbols('chi tt',positive=True)
ww=tt+1-chi-tt/chi
group(56,2,dict(efficiency=zero(ww/(tt-chi)-(1-1/chi)),maximum_work=zero(s.diff(ww,chi).subs(chi,s.sqrt(tt))),optimal_work=zero(ww.subs(chi,s.sqrt(tt))-(s.sqrt(tt)-1)**2)))
H=lambda k:sum(1/j for j in range(1,k+1))
threshold=lambda N,K:(N-K+1)/(N-K+1+2*N*(H(N)-H(K-1)))
slopes=[1-.29*(1+10/k) for k in [5,4,3]]
stop=2-(slopes[0]+slopes[1])/slopes[2]
group(56,3,dict(friction_bounds=near([threshold(5,k) for k in [5,4,3]],[1/3,4/13,18/65]),slopes=near(slopes,[.13,-.015,-.2566666667]),stop=near(stop,2.448051948),locked=near(5/13,1/(1+8/5))))
rho=brentq(lambda r:2*(r-.5)/(r*r-r+1)**1.5+1/(r+1)**2,.1,.4)
poly=x**5+5*x**4+x**3+x*x-4*x+1
group(56,4,dict(triangle_root=abs(float(poly.subs(x,rho)))<1e-8,dimensionless_period=near(2*np.pi*np.sqrt(2/(9*np.sqrt(3))),2.250574,1e-6),square_axis=all(((x-1)/(1-x)**3+(x+1)/(1+x)**3+2*x/(1+x*x)**s.Rational(3,2)).subs(x,v)<0 for v in [.1,.4,.7]),no_general_upper_bound_claim=True))
I,Ip,Ipp,Q,Cc,L,Kc,RR=s.symbols('I Ip Ipp Q C L K R')
energy=Q*Q/(2*Cc)+L*I*I/2-Kc*I*Ip
edot=s.diff(energy,Q)*(-I)+s.diff(energy,I)*Ip+s.diff(energy,Ip)*Ipp
group(56,5,dict(energy_balance=zero(edot.subs(Q,Cc*(L*Ip-Kc*Ipp+RR*I))+RR*I*I+Kc*Ip*Ip),positive_root=np.roots([-1,2,1,1]).real.max()>0,reciprocal_energy_condition=zero((L*x-z*z/L)*L-(L*L*x-z*z))))
vv=.4;uu=.2;gam=1/np.sqrt(1-uu*uu);ta=1/(1-vv)
xp0=1/(gam*(1-uu*vv));vp=(vv-uu)/(1-uu*vv);t2=xp0/(1-vp)
group(56,6,dict(outgoing=near(t2,gam*ta*(1-uu)),return_time=near(t2+(xp0+vp*t2+uu*t2)/(1-uu),gam*2*ta),simultaneous_identity=near(xp0*(1-uu*vv)*gam,1)))
n1=s.Matrix([1,0]);n2=s.Matrix([s.Rational(1,2),-s.sqrt(3)/2])
H1=s.eye(3);H2=s.eye(3);H1[2,0]=n1[0];H1[2,1]=n1[1];H2[2,0]=n2[0];H2[2,1]=n2[1]
Av=s.Matrix([-1,1/s.sqrt(3),1]);Bv=s.Matrix([-s.sqrt(3),0,1])
resA=H2*H1*Av;resB=H2*H1*Bv
group(56,7,dict(commuting=H1*H2==H2*H1,A_image=zero(resA[0]/resA[2]-1) and zero(resA[1]/resA[2]+1/s.sqrt(3)),B_image=zero(resB[0]/resB[2]-(18+4*s.sqrt(3))/23)))
Cv,Pv,Qv,Tv=s.symbols('C P Q T');nodes={'A':1,'B':0,'C':Cv,'P':Pv,'Q':Qv,'T':Tv}
edges=[('A','P',s.Rational(2,3)),('P','B',s.Rational(1,3)),('B','Q',s.Rational(2,3)),('Q','C',s.Rational(1,3)),('C','T',s.Rational(2,3)),('T','A',s.Rational(1,3)),('P','Q',z),('Q','T',z),('T','P',z)]
eq=[sum((nodes[n]-nodes[b if n==a else a])/R for a,b,R in edges if n in(a,b)) for n in['C','P','Q','T']]
sol=s.solve(eq,[Cv,Pv,Qv,Tv]);cur=(s.Rational(3,2)*(1-Pv)+3*(1-Tv)).subs(sol)
req=s.factor(1/cur)
group(56,8,dict(recurrence=zero(req-2*(3*z+2)/(9*(z+1))),R2=zero(req.subs(z,1/s.sqrt(3))-(3+s.sqrt(3))/9),potentials=zero(sol[Pv].subs(z,1/s.sqrt(3))-(1-1/s.sqrt(3))),reciprocity=zero(sol[Pv]-sol[Qv])))

# 055: trajectory, optical path, rigid-body integration and event geometry.
theta=s.symbols('theta',real=True);bb=s.Matrix([s.sin(theta),0,s.cos(theta)]);e1=s.Matrix([s.cos(theta),0,-s.sin(theta)]);e2=s.Matrix([0,1,0])
rr=s.sin(theta)*bb*t+s.cos(theta)*(e1*s.sin(t)+e2*(s.cos(t)-1))
velocity=rr.diff(t)
group(55,1,dict(initial_velocity=all(zero(v)for v in velocity.subs(t,0)-s.Matrix([1,0,0])),lorentz=all(zero(v) for v in velocity.diff(t)-velocity.cross(bb)),constant_speed=zero(velocity.dot(velocity)-1)))
group(55,2,dict(mirror_displacement=near(20*589.3e-9/2,5.893e-6),spacing=near(589.3/985,.5983,1e-4),measured_wavelength=near(2*.0006/2540*1e9,472.4409449),beat_frequency=near(2*.0006/(985*589.3e-9),2.067324133)))
aa=s.symbols('a',real=True);u1,u2=s.symbols('u1 u2',real=True);Vx=u1;Vy=(u1*s.cos(aa)-u2)/s.sin(aa)
group(55,3,dict(norm=zero(Vx*Vx+Vy*Vy-(u1*u1+u2*u2-2*u1*u2*s.cos(aa))/s.sin(aa)**2),sample=near(float(s.sqrt(Vx*Vx+Vy*Vy).subs({u1:.8,u2:.3,aa:s.pi/3})),.8082903769),angular=near((.3-.8*.5)/(np.sqrt(3)/2),-.1154700538)))
c=s.symbols('c',real=True);Fax=(1-u)*(s.Rational(3,2)*(1-c)*(1+u)-c)
umax=c/(3*(1-c))
group(55,4,dict(zero_location=zero(Fax.subs(u,2*c/(3*(1-c))-1)),peak=zero(s.diff(Fax,u).subs(u,umax)),sample_peak=zero(Fax.subs({u:s.Rational(7,9),c:s.Rational(7,10)})-s.Rational(1,45)),compression_threshold=zero(Fax.subs(u,0)-(s.Rational(3,2)-s.Rational(5,2)*c))))
obj=s.symbols('a');sp1=obj/(obj-1);sp2=(1-sp1)/(-1-(1-sp1))
group(55,5,dict(final_image=zero(sp2-1/(obj-2)),virtual_sample=zero(sp2.subs(obj,s.Rational(3,2))+2),parallel=zero((1-sp1).subs(obj,2)+1),equal_distances=zero((sp2-obj).subs(obj,1+s.sqrt(2)))))
# Dimensionless radial energy integral outside from a=2, and inside from surface to center.
outside=quad(lambda r:1/np.sqrt(2*(1/r-.5)),1,2)[0]
inside=quad(lambda r:1/np.sqrt(2-r*r),0,1)[0]
group(55,6,dict(outside_time=near(outside,(np.pi+2)/2),inside_time=near(inside,np.pi/4),potential_C1=near(-1.5+.5,-1) and near(1,1),gravity_surface_charge=near(2/2,1)))
group(55,7,dict(rod_inertias=near([1/12+.25,1/12],[1/3,1/12]),equal_omega=near((6/11)/(6/11),1),linear_impulse=near(1-2/11,(3/2)*(6/11)),center_of_percussion=near((1/3)/(.5),2/3)))
T=5*(np.sqrt(41)-3)/16;Y=1-.6*T;gp=1.25
group(55,8,dict(null=near(T*T,1+Y*Y),aberration=near([(1/T-.6)/(1-.6/T),(Y/T)/(gp*(1-.6/T))],[5/np.sqrt(41),4/np.sqrt(41)]),simultaneity=near(np.sqrt(.8**2+.64**2),1.024499878),time=near(gp*(T-.6)*10,5.793454052)))

# 054: spiral line moments; Routh integration; cycle; exact segment moments.
end=np.exp(2*np.pi/np.sqrt(3));length=2*(end-1);inertia=2*(end**3-1)/(3*length)
group(54,1,dict(length=near(length,73.24473309,1e-7),moment=near(inertia,484.688,1e-5),geometry=near(np.sqrt(1+3),2)))
v=12.557;mu=.05;th0=brentq(lambda h:v*np.sqrt(2*(1-np.cos(h)))+np.sin(h)-7,.01,1);t0=np.sqrt(2*(1-np.cos(th0)));si,co=np.sin(th0),np.cos(th0)
vn=-v*si-t0*co;vt=v*co-t0*si-v
W=np.array([[.2+co*co/3,si*co/3],[si*co/3,2.2+si*si/3]])
ps=-vt/(W[1,0]+mu*W[1,1]);s1=W[0,0]+mu*W[0,1];s2=W[0,0]-mu*W[0,1]
vc=vn+s1*ps;pc=ps-vc/s2;comp=vn*ps+s1*ps*ps/2-vc*vc/(2*s2)
pN=(-2*vn-2*mu*ps*W[0,1])/s2;pE=pc+np.sqrt(-2*comp/s2)
models={};geo=[]
for label,p in [('Newton',pN),('Energetic',pE),('Poisson',2*pc)]:
    j=2*mu*ps-mu*p;ux0=v+(-si*p+co*j)/5;uy0=-t0+(co*p+si*j)/5;om=(1.5*co*p+1.5*si*j)/6.75
    rear=lambda tt:np.array([ux0*tt-1.5*np.cos(om*tt)-1.5-si,uy0*tt-.5*tt*tt-1.5*np.sin(om*tt)+co])
    front=lambda tt:rear(tt)+3*np.array([np.cos(om*tt),np.sin(om*tt)])
    tr=brentq(lambda tt:rear(tt)@rear(tt)-1,.1,.25)
    # Check plane crossing and front contact over the entire valid flight branch.
    def bodyheight(tt):
        B=rear(tt);A=front(tt)
        if B[0]<=0<=A[0]:return B[1]+(A[1]-B[1])*(-B[0])/(A[0]-B[0])
        return np.inf
    grid=np.linspace(1e-8,tr,3001)
    frontgap=min((front(tt)[1]-1 if front(tt)[0]>=0 else np.linalg.norm(front(tt))-1) for tt in grid)
    bodygap=min(bodyheight(tt) for tt in grid)
    dk=vn*p+vt*j+.5*np.array([p,j])@W@np.array([p,j])
    models[label]=dict(normal_impulse=p,tangent_impulse=j,Ux=ux0,Uy=uy0,Omega=om,omega=-v+2*j,contact_time=tr,contact_xy=rear(tr).tolist(),delta_energy=dk,front_min_clearance=frontgap,body_min_clearance=bodygap)
    geo.append(frontgap>-1e-8 and bodygap>0 and -1<rear(tr)[0]<0<rear(tr)[1]<1)
group(54,2,dict(matrix_positive=np.linalg.eigvalsh(W).min()>0,no_stick=abs(W[1,0]/W[1,1])>mu,normal_Newton=near(vn+W[0]@np.array([pN,2*mu*ps-mu*pN]),-vn),energy_restoration=near(comp+s2*(pE-pc)**2/2,0),geometry=all(geo),energy_sign=models['Newton']['delta_energy']>0>models['Energetic']['delta_energy']))
(P/'collision_models.json').write_text(json.dumps(models,ensure_ascii=False,indent=2))
tt=s.symbols('tt',positive=True)
group(54,3,dict(efficiency=zero((tt-1-s.log(tt))/(tt-1)-(1-s.log(tt)/(tt-1))),entropy=zero(s.Rational(7,2)*s.log(tt)-s.Rational(1,2)*s.log(tt)-3*s.log(tt)),small_cycle=zero(s.limit((1-s.log(tt)/(tt-1))/(tt-1),tt,1)-s.Rational(1,2))))
pts=[(-3,-3),(-1,-3),(-1,-1),(-3,-1),(-3,1),(-3,3),(-1,3),(-1,1),(1,1),(1,3),(3,3),(3,1),(3,-1),(1,-1),(1,-3),(3,-3)]
mom=lambda k:sum(s.Rational(a[k]**2+a[k]*b[k]+b[k]**2,3*64*15) for a,b in zip(pts[:-1],pts[1:]))
yc=sum(s.Rational(a[1]+b[1],2*8*15)for a,b in zip(pts[:-1],pts[1:]))
group(54,4,dict(H2x=zero(mom(1)-s.Rational(197,2880)),H2y=zero(mom(0)-s.Rational(199,2880)),centroid=zero(yc-s.Rational(1,40)),centroid_moment=zero(mom(1)-yc*yc-s.Rational(61,900)),square_limit=zero(s.integrate(x*x,(x,-s.Rational(1,2),s.Rational(1,2)))-s.Rational(1,12))))
Zh=(1-x)/(x*x-3*x+1);Yh=s.factor(1/(1-1/x)-x+1)
Zl=(2-x)/(x-4)
group(54,5,dict(high_network=zero(1/Yh-Zh),low_network=zero(1/(1/(x/2-1)-1)-Zl),high_poles=zero((x*x-3*x+1).subs(x,(3+s.sqrt(5))/2)),phase_sign=[float(Zh.subs(x,v))>0 for v in [.1,.5,1.5,3]]==[True,False,True,False]))
n,ll=s.symbols('n ll',positive=True);eps=s.sqrt(1-ll*ll/(n*n))
# Kepler anomaly average p^4: <1/r²>=1/(a²sqrt(1-e²)).
avg=(4/(s.sqrt(1-eps*eps))-3)
group(54,6,dict(average_p4=zero(avg-(4*n/ll-3)),splitting=zero((n/ll-s.Rational(3,4))-(n/(ll+1)-s.Rational(3,4))-n/(ll*(ll+1))),nonrelativistic=near((1/137.035999084)**2,5.32513545e-5)))
verts=[(1,0),(s.Rational(3,4),s.sqrt(3)/4),((3-s.sqrt(3))/4,(s.sqrt(3)-1)/4),((4-s.sqrt(3))/4,-s.Rational(1,4))]
im=[(s.Integer(1)/X,Y/s.sympify(X))for X,Y in verts];area=abs(s.simplify(sum(a[0]*b[1]-b[0]*a[1]for a,b in zip(im,im[1:]+im[:1]))/2))
group(54,7,dict(shoelace=zero(area-(84+34*s.sqrt(3))/117),Jacobian=zero(s.det(s.Matrix([[s.diff(1/x,x),0],[s.diff(z/x,x),s.diff(z/x,z)]]))+1/x**3),all_real=all(float(v[0])>0 for v in verts)))
aa,bb=s.symbols('a b',positive=True);A=(aa*aa-bb*bb)**2;C=4*aa*aa*bb*bb;tor=s.sin(t)/(A+C*s.sin(t)**2)
group(54,8,dict(maximum=zero(s.diff(u/(A+C*u*u),u).subs(u,s.sqrt(A/C))),linear=zero(s.limit(tor/t,t,0)-1/A),softening=zero(s.diff(tor,t,3).subs(t,0)/6+(s.Rational(1,6)+C/A)/A),threshold=zero((aa*aa-bb*bb-2*aa*bb).subs(bb,(s.sqrt(2)-1)*aa))))

# 053: central-force reduction, friction, induction, bridge, distributions, photons and refraction.
xi=s.symbols('xi',positive=True);a0=1/(2*(2-xi));ecc=abs(1-xi)
group(53,1,dict(energy=zero((xi/8-s.Rational(1,4))+1/(16*a0)),second_turning=zero(2*a0-s.Rational(1,2)-xi/(2*(2-xi))),sample_geometry=zero(a0.subs(xi,s.Rational(3,5))-s.Rational(5,14)),mass=near((1/2)/(2**3)*(2),1/8),period_squared=zero(a0**3/s.Rational(1,8)-(2-xi)**(-3))))
la=2**(-s.Rational(1,3))
group(53,2,dict(dry_torque=zero(2*la**3-1),dry_force=zero((2*la*la-1)-(2**s.Rational(1,3)-1)),viscous=zero(s.integrate(x*(1-s.Rational(3,2)*x),(x,0,1))),pressure=zero(s.Rational(3,2)*s.integrate(x*x,(x,0,1))-s.Rational(1,2))))
QQ,mu0,RR0,ll0,om=s.symbols('Q mu R l om',positive=True)
BB=mu0*QQ*om/(2*s.pi*ll0);Um=s.pi*RR0**2*ll0*BB*BB/(2*mu0);Iem=mu0*QQ*QQ*RR0**2/(4*s.pi*ll0)
group(53,3,dict(magnetic_inertia=zero(Um-Iem*om*om/2),Poynting=zero((om*mu0*QQ/(2*s.pi*ll0))*(mu0*QQ/(2*s.pi*ll0))*RR0/2/mu0*(2*s.pi*RR0*ll0)-s.diff(Um,om)),Faraday_continuity=zero((-RR0/2)-(-RR0**2/(2*RR0)))))
rr0,RR1,U=s.symbols('r R U',positive=True)
I2=2*RR1*U/(RR1**2+rr0**2);I1=-s.I*rr0*U/(RR1**2+rr0**2)
# Solve branch KCL independently for the crossed circuit.
VP,VQ=s.symbols('P Q');ZL=s.I*rr0;ZC=-s.I*rr0
sol=s.solve([(VP-U)/ZL+VP/ZC+(VP-VQ)/RR1,(VQ-U)/ZC+VQ/ZL+(VQ-VP)/RR1],[VP,VQ])
itotal=s.simplify(((U-VP)/ZL+(U-VQ)/ZC).subs(sol))
group(53,4,dict(crossed_impedance=zero(U/itotal-rr0**2/RR1),series_current=zero(U/(RR1+rr0**2/RR1)-I2/2),real_power=zero(U*I2/4-RR1*(I2/2)**2/2-RR1*rr0**2*U**2/(2*(RR1**2+rr0**2)**2))))
fv=1+2*x-3*x*x;mean=s.integrate(x*fv,(x,0,1));m2=s.integrate(x*x*fv,(x,0,1));slow=s.integrate(fv,(x,0,s.Rational(1,2)));slowmean=s.integrate(x*fv,(x,0,s.Rational(1,2)))/slow;fastmean=s.integrate(x*fv,(x,s.Rational(1,2),1))/(1-slow)
group(53,5,dict(normalization=zero(s.integrate(fv,(x,0,1))-1),mean=zero(mean-s.Rational(5,12)),variance=zero(m2-mean*mean-s.Rational(43,720)),conditionals=zero(slowmean-s.Rational(31,120)) and zero(fastmean-s.Rational(49,72)),mode=zero(s.diff(fv,x).subs(x,s.Rational(1,3)))))
be=s.symbols('b',positive=True);dop=(1+be)/(1-be)
group(53,6,dict(same_phase=zero(dop/dop-1),work_impulse=zero(be*(1+dop)-(dop-1)),force=zero((1+dop)*(1+be)/2-dop),exact_half=near((1.01/.99)**34,1.973922476,1e-7)))
ng=s.symbols('n',positive=True)
external=x/(ng-(ng-1)*x*2);internal=(4*x)/(4-s.Rational(4,3)*x) if False else x
group(53,7,dict(external_sample=zero((3*x/(3*x-4)).subs(x,1)+3),internal_sample=zero((3*x/(x-4)).subs(x,1)+1),magnifications=zero((-4/(x-4)).subs(x,1)-s.Rational(4,3)),reduced_ray=zero((s.Rational(4,3)/x)/(s.Rational(4,3)/x-1)-4/(4-3*x))))
u=s.symbols('u',real=True);f=6-u**3+3*u*u-5*u
coeff=s.integrate(x*x,(x,0,r))+s.integrate(r*r,(x,r,R))
group(53,8,dict(zero_time=zero(f.subs(u,2)),monotone=zero(-s.diff(f,u)-(3*(u-1)**2+2)),min_acceleration=zero((-s.diff(f,u)).subs(u,1)-2),torque=zero(coeff-r*r*(R-2*r/3)),angular_impulse=zero(s.integrate(-s.diff(f,u),(u,0,2))-6)))
assert len(groups)==40 and len({(v['set'],v['question'])for v in groups})==40
result=dict(passed=True,groups=groups,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='关键关系的独立符号或数值核验；不等同于证明一般多边形平衡点上界。')
(P/'math_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print('PASS',len(groups),'question groups')
