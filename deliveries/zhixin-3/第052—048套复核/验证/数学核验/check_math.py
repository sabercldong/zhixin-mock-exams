from pathlib import Path
import json,hashlib
import numpy as np
import sympy as s
from scipy.integrate import quad
from scipy.optimize import brentq
P=Path(__file__).parent;groups=[]
def near(a,b,tol=1e-7):return np.allclose(a,b,rtol=tol,atol=tol)
def zero(a):return s.simplify(a)==0
def group(n,q,c):
 assert all(bool(v)for v in c.values()),(n,q,c)
 groups.append(dict(set=n,question=q,passed=all(bool(v)for v in c.values()),checks=list(c)))
x,t,y=s.symbols('x t y',real=True);r=s.symbols('r',positive=True)
# 052
rho1,rho2,H,S,A,g=s.symbols('rho1 rho2 H S A g',positive=True)
group(52,1,dict(partial_cover=zero(s.diff(rho1*(H-x)+rho2*x,x)-(rho2-rho1)),finite_vessel=zero((A/(A-S))*(1-S/A)-1),period_limit=near(np.sqrt(1-.01),.994987437)))
mu=469.;mc=138.;lam=197.32698/mc;eps=2.22/(mc*mc/(2*mu));root=brentq(lambda x:(1-x)/(x*x*(1+x))-eps,.3,.999);gg=mc*mc/(2*mu)*lam*2*np.exp(root)/(root*(1+root));C=mu*gg*lam/(197.32698**2)
group(52,2,dict(bound_root=near(root,.8527017802),coupling=near(gg,86.2211284),only_n1_bound=1<2*C/np.e<4,stability_polynomial=1+root-root**2>0))
phi=s.symbols('phi',real=True);X=phi+s.sin(phi);Y=1-s.cos(phi);ds=2*s.cos(phi/2)
group(52,3,dict(cycloid_arclength=zero(s.diff(X,phi)**2+s.diff(Y,phi)**2-ds**2),tautochrone=zero((4*s.sin(phi/2))**2-8*Y),Abel_halfwidth=near(quad(lambda u:1/np.sqrt(u*(1-u)),0,1)[0],np.pi)))
I,L,D=s.symbols('I L D',positive=True);If=I-D/L;K=I*D-D*D/(2*L)
group(52,4,dict(isolated_energy=zero(L*(I**2-If**2)/2-K),reach=zero(K.subs(D,2*L*I)),interior_equilibrium=zero(s.diff((s.Rational(1,2)-s.cos(x))**2,x).subs(x,s.pi/3))))
theta=brentq(lambda t:10*np.tan(t)-100*(.15+.25*.05*np.sin(t)),.01,1.5);wx=-10*(.1/.05+np.sin(theta))*np.cos(theta);wy=10*(np.cos(theta)**2-.1/.05*np.sin(theta))
group(52,5,dict(tilt=near(theta*180/np.pi,58.092733),angular_velocity=near([wx,wy],[-15.05777,-14.18448],1e-6),uniqueness=10-100*.05/4>0))
a,dd=s.symbols('a dd',real=True);phase=s.cos(a-dd)-s.cos(a)
group(52,6,dict(grazing_linear=zero(s.diff(phase,dd).subs(dd,0)-s.sin(a)),grazing_quadratic=zero(s.diff(phase,dd,2).subs(dd,0)+s.cos(a)),allowed_order=abs(np.cos(.1)+.001)<=1))
c=2.998e8;v=c*(5.2e-6+6.24e-5);Pbin=3.44*365.25*86400;ra=v*8.5*3600/2;rb=v*(25.08-8.5)*3600/2;sep=v*Pbin/(2*np.pi);M=4*np.pi*np.pi*sep**3/(6.67e-11*Pbin**2);lightyear=c*365.25*86400;lum=4*np.pi*(125*lightyear)**2*2.38e-9;planet=np.sqrt(lum/(16*np.pi*5.67e-8*300**4))
group(52,7,dict(radii=near([ra,rb],[310077144.,604832829.12]),photometric_ratio=near(np.sqrt(.04/.153),.51130999),central_mismatch=abs(ra/rb-np.sqrt(.04/.153))>.001,orbital_mass=near(M,2.156213e30,2e-5),planet_radiation=near(planet/sep,3.843,1e-3)))
alpha,n,l=s.symbols('alpha n l',positive=True);DE=-alpha**4/(2*n**4)*(n/l-s.Rational(3,4))
group(52,8,dict(circular_shift=zero(DE.subs(l,n)+alpha**4/(8*n**4)),n2_splitting=zero((alpha**2/8)/abs(DE.subs({n:2,l:1})-DE.subs({n:2,l:2}))-4/alpha**2),time_average=near(quad(lambda u:1/(1-.6*np.cos(u)),0,2*np.pi)[0]/(2*np.pi),1/.8)))
# 051
r1,r2,d=s.symbols('r1 r2 d',positive=True);delta=r2-r1;length=2*s.sqrt(d*d-delta*delta)+s.pi*(r1+r2)+2*delta*s.asin(delta/d)
group(51,1,dict(belt_derivative=zero(s.diff(length,r1)-(s.pi-2*s.asin(delta/d))),symmetry=zero(length-length.xreplace({r1:r2,r2:r1})),cone_sum=zero((5-x)+(5+x)-10)))
eta=4/(3*np.pi);j=.5-eta**2;rho=2/np.pi*(np.arccos(5/13)-(5/13)*(12/13));T2=2*np.pi*np.sqrt(j/eta);m=1e-4;kap=m/(1+m);jump=2*np.sqrt(kap/j)*np.arctan(np.sqrt(kap/(j+kap*eta**2)))*eta*np.sqrt(j/(j+kap*eta**2));lead=2*m*eta/j;inc=4*m/(eta)*.5/j
group(51,2,dict(density=near(rho,.522652,1e-5),inertia=near(j,.3198734513),sway_period=near(T2,5.454746,1e-6),fast_map=near(jump,lead,1e-6),cycles=near(.01/inc,6.7879,1e-5)))
mm=s.symbols('mm',positive=True);Z=(s.cosh(mm*x)-1)/mm
group(51,3,dict(full_curve_even=zero(Z-Z.subs(x,-x)),tangent=zero(s.diff(Z,x)-s.sinh(mm*x)),selflock=near(np.log(np.tan(np.arctan(np.exp(-.6*np.pi/2)))),-.6*np.pi/2)))
qc=(1-np.sqrt(23/27))/2;q=1/81;dis=1-27*q*(1-q);nus=np.sort([(1+np.sqrt(dis))/2,(1-np.sqrt(dis))/2]);B=np.array([[0,0,1,0],[0,0,0,1],[.75,3*np.sqrt(3)/4*(1-2*qc),0,2],[3*np.sqrt(3)/4*(1-2*qc),2.25,-2,0]])
group(51,4,dict(critical=near(qc,.0385208965),earth_modes=near(nus,[.0904936061,.9095063939]),critical_defect=np.linalg.matrix_rank(B-1j/np.sqrt(2)*np.eye(4),tol=1e-7)==3))
verts=[s.Matrix([1/s.sqrt(3),0,-1/(2*s.sqrt(6))]),s.Matrix([-1/(2*s.sqrt(3)),s.Rational(1,2),-1/(2*s.sqrt(6))]),s.Matrix([-1/(2*s.sqrt(3)),-s.Rational(1,2),-1/(2*s.sqrt(6))]),s.Matrix([0,0,s.sqrt(6)/4])]
group(51,5,dict(node_sources=all(sum((verts[i].cross(verts[j])for j in range(4)if j!=i),s.zeros(3,1))==s.zeros(3,1)for i in range(4)),AD_emf=zero(-verts[0].cross(verts[3])[1]/2-s.sqrt(2)/8),AB_power=zero((s.Rational(2,256)+s.Rational(6,2304))/2-s.Rational(1,192))))
group(51,6,dict(heat_segments=near([2.5*(2-1),3.5*(4-2),2.5*(1-4)+(1-4)/2], [2.5,7,-9]),efficiency=near(.5/(2.5+7),1/19),triangle_area=near(.5*(2-1)*(2-1),.5)))
# Curvature and independent ray reflection at explicit P,Q.
X=s.cos(x)**3;Y=s.sin(x)**3;num=s.diff(X,x)*s.diff(Y,x,2)-s.diff(Y,x)*s.diff(X,x,2);P1=np.array([-(2/3)**1.5,-(1/3)**1.5]);Q1=P1*np.array([1,-1]);T=np.array([1,-np.sqrt(1/2)]);T=T/np.linalg.norm(T);vi=P1/np.linalg.norm(P1);vo=2*T*np.dot(vi,T)-vi;target=(Q1-P1)/np.linalg.norm(Q1-P1)
group(51,7,dict(curvature_numerator=zero(num+9*s.sin(x)**2*s.cos(x)**2),reflection=near(vo,target),emission=near(np.degrees(np.arctan2(P1[1],P1[0]))%360,199.4712206),separation=near(2*.6,3*.4)))
p=2000;hc=6.62607015e-34*2.99792458e8;dn=.001
group(51,8,dict(strict_modes=sum(1 for n in range(1,p+2)if n<p)==1999,sum_modes=sum(range(1,p))==p*(p-1)/2,finite_force=near(hc*p*(p-1)/(8*dn**2),9.9272632e-14,1e-19)))
# 050
f=quad(lambda v:v/(1+v)**2,0,1)[0];rc=.1*1.29*.01/(2000*f)
group(50,1,dict(variable_speed_integral=near(f,np.log(2)-.5),cylinder=near(rc*1e6,3.339,1e-3),sphere=near(.75*rc*1e6,2.504,1e-3)))
R,LL=s.symbols('R LL',positive=True);d2=R*R-LL*LL/4;K=d2+LL*LL/12;xx=d2/K
group(50,2,dict(effective_inertia=zero(K-(R*R-LL*LL/6)),support_vector=zero(s.diff(s.sqrt(s.cos(t)**2+(1-xx)**2*s.sin(t)**2)-(1+xx*t*t),t,2).subs(t,0)/2-(-2*xx+xx*xx/2)),force_sum=zero(-(s.Rational(1,2)+xx)+(s.Rational(1,2)+xx))))
ri=.9;ro=2.;rh=(ro*ro-ri*ri)/(2*ri);cc=np.sqrt(ro*ro+rh*rh)
group(50,3,dict(grazing_geometry=near(cc,ri+rh),global_flux_continuity=near(-.5*3*ri**2,-.5*(3*ri**2+2*(ri**2-ri**2))),straight_center_field=near(-(ro*ro-ri*ri)/ri**2,-3.9382716049)))
group(50,4,dict(contact_geometry=near(np.sqrt(2*1.2*.4-.4**2)**2+(1.2-.4)**2,1.2**2),collision_threshold=near((2*1.2*np.sqrt(10*.4)/(2*1.2-.4))**2,5.76),threshold_zero_speed=near(5.76*(2*1.2-.4)**2/(4*1.2**2)-10*.4,0)))
Dmat=np.diag([1,2,1]);vv=np.array([1,1,-3]);group(50,5,dict(volume_constraint=near(np.dot([1,2,1],vv),0),positive_energy=vv@Dmat@vv>0,equal_modes=near(np.linalg.eigvalsh(np.eye(2)),[1,1])))
a=.7;fint=quad(lambda u:np.exp(-u*u),0,a)[0];cnt=.5-fint/np.sqrt(np.pi)+(1-np.exp(-a*a))/(2*np.sqrt(np.pi)*a);direct=quad(lambda u:np.exp(-u*u)*min(u/a,1)/np.sqrt(np.pi),0,np.inf)[0]
group(50,6,dict(wall_collision_fraction=near(cnt,direct),short_time=near(.5-quad(lambda u:np.exp(-u*u),0,100)[0]/np.sqrt(np.pi)+(1-np.exp(-10000))/(200*np.sqrt(np.pi)),1/(200*np.sqrt(np.pi))),long_time=0<cnt<.5))
# Transfer matrix from object plane through L1 to L2.
T=lambda d:np.array([[1.,d],[0,1.]]);Lens=lambda f:np.array([[1.,0],[-1/f,1.]]);M=T(3)@Lens(1.5)@T(6)
group(50,7,dict(transfer=near(M,[[-1,-3],[-2/3,-3]]),extreme_visible=near(-(-1.5)-2*(-.5),2.5),ray_max=near(M@np.array([2.5,-2/3]),[-.5,1/3]),bright_center=near(M@np.array([1,-1/6]),[-.5,-1/6])))
ss=.5;lam=.1;del0=(1-ss*ss-np.sqrt((1-ss*ss)**2-2*ss*ss*lam))/ss;dx=lam+ss*del0+.5*del0**2
proper=quad(lambda u:np.sqrt(1-u*u),0,ss)[0]
group(50,8,dict(simultaneity=near(del0,ss*dx),proper_time=near(proper,(np.arcsin(ss)+ss*np.sqrt(1-ss*ss))/2),finite_event=ss+del0<1,domain_limit=near(((1-ss)**2*(ss+2)/(2*ss)),.625)))
# 049: full rectangle sweep, not just corner-radius heuristics.
AA=np.sqrt(41);BB=np.sqrt(26);d=(AA+BB-np.sqrt(18-(AA-BB)**2))/2;a=AA-d;b=BB-d;IC=np.array([-a,d+b]);boundary=[]
for u in np.linspace(-1,4,120):boundary.extend([[u,-5],[u,-3]])
for v in np.linspace(-5,-3,120):boundary.extend([[-1,v],[4,v]])
car=np.array(boundary);bad=False
for th in np.linspace(0,np.pi/2,1801):
 rot=np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]]);pos=car@rot.T+IC
 bad|= bool(np.any((pos[:,1]<-1e-8)|(pos[:,0]>d+1e-8)|((pos[:,0]<-1e-8)&(pos[:,1]>d+1e-8))))
group(49,1,dict(Ackermann=near(5/3-1,2/3),offset_constraint=near(a*a+b*b,9),full_boundary_sweep=not bad,counterexample=d<np.sqrt(41)))
N=100;rr=.1;W=lambda n:np.log(N/(rr*N+(1-rr)*n))+np.log(n/(rr*n+1-rr));opt=brentq(lambda n:(W(n+.001)-W(n-.001))/.002,2,50)
group(49,2,dict(optimal_stage=near(opt,10,1e-5),global_grid=max(W(n)for n in np.linspace(1,100,10001))<=W(10)+1e-8,required_mass_ratio=near(((.9*np.exp(2))/(1-.1*np.exp(2)))**2,648.70,1e-3)))
group(49,3,dict(lab_velocities=near([1/(.5)+1/(.5),-1/(.5)+1/(1.5)],[4,-4/3]),moving_frame=near([4-1,-4/3-1],[3,-7/3]),height_ratio=near((9-49/9)/(16-16/9),.25)))
A=.25;B=1+np.sqrt(3)/4;mucrit=A*B/(1+B*B);jn=2*(1+B*B)/(1+A*A+B*B);jt=-2*A*B/(1+A*A+B*B);w=A*jn+B*jt;vy=-1+jn;vx=jt
group(49,4,dict(sticking=near(vx+B*w,0),normal_restitution=near(vy+A*w,1),energy=near(vx*vx+vy*vy+w*w,1),critical=0<mucrit<.5))
group(49,5,dict(reflection_composition=near(72-(-72-18),18+144),formal_group_order=len({(144*k)%360 for k in range(5)})==5,branch_centers=near([72-72,144-144,216-216,288-288],[0,0,0,0]),visibility_not_claimed=True))
group(49,6,dict(parallel_edges=near(np.array([13/3,10/3])-np.array([5,5]),-np.array([2,5])/3),net_efficiency=near((10/3)/5,2/3),second_cycle=near(np.array([5,5])+10/3,[25/3,25/3]),entropy_closure=near(3*(1/3),1)))
kr=brentq(lambda k:np.log(k)-k*(-3*np.pi/2),.01,.5)
group(49,7,dict(spiral_parameter=near(kr,.27441,1e-4),curvature=zero(s.diff(s.exp(t)*s.cos(t),t)**2+s.diff(s.exp(t)*s.sin(t),t)**2-2*s.exp(2*t)),center_identity=near(np.array([1,0])+np.sqrt(1+.3**2)*np.array([-1,.3])/np.sqrt(1+.3**2),[0,.3])))
group(49,8,dict(near_far=zero((1-s.sqrt(1-l*l/n/n))+(1+s.sqrt(1-l*l/n/n))-2),eccentricity=zero(1-(1-l*l/n/n)-l*l/n/n),splitting=zero(DE.subs(l,1)-DE.subs(l,2)+alpha**4/(4*n**3))))
# 048
beta,theta=s.symbols('beta theta',real=True);nn=s.Matrix([-s.sin(beta),0,s.cos(beta)]);er=s.Matrix([s.cos(beta)*s.cos(theta),s.sin(theta),s.sin(beta)*s.cos(theta)]);F=s.Matrix([0,0,1])
group(48,1,dict(perpendicular=zero(er.dot(nn)),restoring_torque=zero(er.cross(F).dot(nn)+s.sin(beta)*s.sin(theta)),front_force=near((2*.5),1)))
vperp,Bz=s.symbols('vp Bz',positive=True);energy=s.Symbol('energy');mag=vperp*vperp/(2*Bz)
group(48,2,dict(adiabatic_perp=zero((2*mag*Bz)-vperp*vperp),mirror_ratio=near(1/.5**2,4),strict_boundary=quad(lambda z:1/np.sqrt(max(1e-30,1-(1-.5*(1-z)**2))),0,.999)[0]>5))
group(48,3,dict(fixed_free_shape=zero(s.sin(s.pi*t/2).subs(t,0)),free_shear=zero(s.diff(s.sin(s.pi*t/2),t).subs(t,1)),torsion_free_both=zero(s.diff(s.cos(s.pi*t),t).subs(t,0))and zero(s.diff(s.cos(s.pi*t),t).subs(t,1))))
T=1.95;Tc=4.48;B0=.144;mu0=1.25e-6;Bc=B0*(1-T*T/Tc**2);der=-2*B0*T/Tc**2;formal=-mu0*Bc*der;si=-Bc*der/mu0
group(48,4,dict(formal_value=near(formal,4.082432778265912e-9,1e-14),SI_density=near(si,2612.756978090183,1e-6),max_entropy_shape=zero(s.diff(t*(1-t*t),t).subs(t,1/s.sqrt(3)))))
group(48,5,dict(magnetic_force=zero(-s.diff((2-s.cos(t))**2/2,t)-(2-s.cos(t))*(-s.sin(t))),stiffness=zero(s.diff((2-s.cos(t))**2/2,t,2).subs(t,0)-1),zero_current_quartic=zero(s.diff((1-s.cos(t))**2/2,t,4).subs(t,0)/24-s.Rational(1,8))))
z2=(np.sqrt(3)-1)/2;z4=(np.sqrt(2)-1)/2
# Finite-network KCL, with transverse C4 edges and longitudinal resistance 1.
Nf=40;nnodes=4*(Nf+1);lap=np.zeros((nnodes,nnodes))
for k in range(Nf+1):
 for i in range(4):
  for j in [((i+1)%4)+4*k]+([i+4*(k+1)]if k<Nf else []):
   h=i+4*k;lap[h,h]+=1;lap[j,j]+=1;lap[h,j]-=1;lap[j,h]-=1
curr=np.zeros(nnodes);curr[0]=1;curr[2]=-1;pot=np.linalg.lstsq(lap,curr,rcond=None)[0];curr2=np.zeros(nnodes);curr2[0]=1;curr2[1]=-1;pot2=np.linalg.lstsq(lap,curr2,rcond=None)[0];rac=pot2[0]-pot2[1]
group(48,6,dict(network_diagonal=near(pot[0]-pot[2],2*z2),network_adjacent=near(rac,z2+z4),ladder_fixedpoint=near(z2,1/(2+1/(1+z2)))))
eta=.003;vmax=np.sqrt(1-(1+eta)**(-2));integral=4*quad(lambda ph:np.sqrt(2*eta)*np.cos(ph)/np.sqrt(1-(1+eta*np.cos(ph)**2)**(-2)),0,np.pi/2)[0]
group(48,7,dict(period_expansion=near(integral/(2*np.pi),1+3*eta/8,3e-6),speed_correction=near(vmax/np.sqrt(2*eta),1-3*eta/4,7e-6)))
mu=.6;th=.9;phase=lambda th:2*np.arctan(np.sqrt(np.sin(th)**2-mu*mu)/np.cos(th));diff=(phase(th+1e-6)-phase(th-1e-6))/2e-6
group(48,8,dict(phase_derivative=near(diff,2*np.sin(th)/np.sqrt(np.sin(th)**2-mu*mu)),positive_shift=diff/np.cos(th)>0,unit_modulus=near(abs((np.cos(th)+1j*np.sqrt(np.sin(th)**2-mu*mu))/(np.cos(th)-1j*np.sqrt(np.sin(th)**2-mu*mu))),1)))
assert len(groups)==40
out=dict(passed=all(g['passed']for g in groups),groups=groups,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),note='核对列出的关键关系；不声称自动证明完整解析，也不证明第049套道路全局最优或双镜实际可见性。')
(P/'math_results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print('values',ra,rb,rho,T2,jump,lead,rc,kr,formal,si);print('passed',sum(g['passed']for g in groups))
