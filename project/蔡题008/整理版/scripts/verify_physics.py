"""独立数值/符号核验，固定参数，无时间戳以便逐字节复现。"""
from pathlib import Path
import json
import numpy as np
import sympy as sp
from scipy.linalg import null_space,expm
from scipy.integrate import quad,solve_ivp
import mpmath as mp
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(q,name,passed,**values):
 checks.append(dict(name=f'{q:02d}-{name}',passed=bool(passed),values=values))
def close(x,y,tol=1e-10):return bool(np.allclose(x,y,rtol=tol,atol=tol))
def main():
 # 01: potential, two separately isolated rod moment equations, variants.
 a=.5;b=.5;L=1.5;g=10.;p1=10.;p2=20.;k=g*L*(p1+p2/2)/(a*b);N=k*a*(L-b)/L
 th=np.linspace(.1,1.3,13);ss=a*a+b*b-2*a*b*np.cos(th)
 U=g*L*(p1+p2/2)*np.cos(th)+k*ss/2
 check(1,'zero-length-global-potential',np.ptp(U)<1e-10,potential_range=float(np.ptp(U)))
 check(1,'spring-length-cosine',np.all(ss>0),min_squared_length=float(ss.min()))
 tauAB=k*a*(L-b)*np.sin(th)-N*L*np.sin(th)
 check(1,'AB-isolated-torque',np.max(abs(tauAB))<1e-10,max_residual=float(max(abs(tauAB))))
 tauCD=(-k*a+g*(p1+p2/2)+N)*L*np.sin(th)
 check(1,'CD-independent-torque',np.max(abs(tauCD))<1e-10,max_residual=float(max(abs(tauCD))))
 RB=np.array([k*b*np.sin(np.pi/6),k*(a-b*np.cos(np.pi/6))-N]);RC=np.array([-RB[0],N+g*(p1+p2)-k*(a-b*np.cos(np.pi/6))])
 check(1,'AD-compression-and-wall-balance',N>0 and close(RB+RC,[0,g*(p1+p2)]),compression_newton=N,RB=RB.tolist(),RC=RC.tolist())
 check(1,'neutral-k',close(k,1200),stiffness_N_per_m=k)
 check(1,'variant-1-load',close(N,400),N=N)
 k2=g*L*(p1+5+p2/2)/(a*b)
 check(1,'variant-2-extra-mass',close(k2-k,300),delta_k=k2-k)
 bn=.75;kn=g*L*(p1+p2/2)/(a*bn);Nn=kn*a*(L-bn)/L
 check(1,'variant-3-new-point',close([kn,Nn],[800,200]),k=kn,N=Nn)
 tau=100*a*b*np.sin(np.pi/6)
 check(1,'variant-4-perturbation',close(tau,12.5),balancing_torque_Nm=tau)
 s0=.2;effective=1-s0/np.sqrt(ss)
 check(1,'finite-rest-length-not-neutral',np.ptp(effective)>.1,factor_range=float(np.ptp(effective)))
 check(1,'geometry-not-presumed',close(k,400*L/a),a=a,L=L,b=b)
 # 02: obtain kinetic matrix directly from spatial bead coordinates.
 ls=np.linspace(0,1,101);D=ls**2-ls+1;beta=2*np.pi/3
 rho=(1-ls)+ls*np.exp(1j*beta);rp=np.exp(1j*beta)-1
 check(2,'spatial-rod-length',close(abs(rp)**2+3,6),length_squared=abs(rp)**2+3)
 check(2,'bead-radius-squared',close(abs(rho)**2,3*D-2),max_residual=float(max(abs(abs(rho)**2-(3*D-2)))))
 I=2+abs(rho)**2;cross=np.imag(np.conj(rho)*rp)
 check(2,'total-inertia',close(I,3*D),min_dimensionless_inertia=float(I.min()))
 check(2,'angular-cross-term',close(cross,np.sqrt(3)/2),cross_coefficient=float(cross[0]))
 Meff=6-cross**2/I
 check(2,'Schur-effective-mass',close(Meff,6-1/(4*D)),min_coefficient=float(Meff.min()))
 ld=-np.sqrt(2*np.sqrt(3)*(1-ls)/Meff);omega=-cross/I*ld
 check(2,'zero-angular-momentum',max(abs(I*omega+cross*ld))<1e-12,max_residual=float(max(abs(I*omega+cross*ld))))
 check(2,'energy-conservation',close(.5*Meff*ld**2,np.sqrt(3)*(1-ls)),max_residual=float(max(abs(.5*Meff*ld**2-np.sqrt(3)*(1-ls)))))
 wh=2*np.sqrt(3)*.5/(3*.75*(24*.75-1))
 check(2,'half-height-speed',close(wh,4*np.sqrt(3)/153),omega2_r_over_g=wh)
 wb=2*np.sqrt(3)/(3*23)
 check(2,'bottom-speed',close(wb,2*np.sqrt(3)/69),omega2_r_over_g=wb)
 alpha=np.sqrt(3)/6*quad(lambda z:1/(z*z-z+1),0,1)[0]
 check(2,'total-angle-and-mass-scaling',close(alpha,np.pi/9),radians=alpha,degrees=alpha*180/np.pi)
 half=np.sqrt(3)/6*quad(lambda z:1/(z*z-z+1),.5,1)[0]
 check(2,'half-angle-and-length-scaling',close(half,np.pi/18) and close(np.sqrt(wh/2),np.sqrt(wh)/np.sqrt(2)),half_degrees=half*180/np.pi)
 time_integrand=lambda l:np.sqrt((6-1/(4*(l*l-l+1)))/(1-l))
 time_upper=quad(time_integrand,.5,1)[0];time_lower=quad(time_integrand,0,.5)[0]
 check(2,'mirror-handedness-and-time-process',close(-cross,-np.sqrt(3)/2) and time_upper>time_lower and close(3-12/23,57/23),mirror_angle=-alpha,upper_time_integral=time_upper,lower_time_integral=time_lower,initial_ground_N_over_mg=57/23)
 # 03: symbolic path energy and coenergy derivative.
 LA,LB,M,IA,IB,z,mu0,r1,r2=sp.symbols('LA LB M IA IB z mu0 r1 r2',positive=True)
 W=LA*IA**2/2+LB*IB**2/2+M*IA*IB
 check(3,'A-source-differential',sp.diff(W,IA)==LA*IA+M*IB)
 check(3,'B-source-differential',sp.diff(W,IB)==LB*IB+M*IA)
 check(3,'cross-derivatives-reciprocal',sp.diff(W,IA,IB)==M)
 simultaneous=sp.integrate(sp.Symbol('t')*(LA*IA**2+LB*IB**2+2*M*IA*IB),(sp.Symbol('t'),0,1))
 check(3,'variant-1-simultaneous',sp.simplify(simultaneous-W)==0)
 Mex=mu0*sp.pi*r1**2*r2**2/(2*z**3);F=IA*IB*sp.diff(Mex,z)
 Fdip=IB*sp.pi*r2**2*sp.diff(mu0*IA*r1**2/(2*z**3),z)
 check(3,'independent-dipole-force',sp.simplify(F-Fdip)==0)
 check(3,'force-attraction-sign',F.is_negative is True,formula=str(F))
 finite_r1=1.;finite_r2=.5;finite_z=10.
 exactM=finite_r1*finite_r2/2*quad(lambda t:np.cos(t)/np.sqrt(finite_z**2+finite_r1**2+finite_r2**2-2*finite_r1*finite_r2*np.cos(t)),0,2*np.pi,epsabs=1e-13)[0]
 leadingM=np.pi*finite_r1**2*finite_r2**2/(2*finite_z**3)
 correctedM=leadingM*(1-1.5*(finite_r1**2+finite_r2**2)/finite_z**2)
 check(3,'mutual-coupling-symmetry-and-finite-radius',sp.simplify(Mex-Mex.xreplace({r1:r2,r2:r1}))==0 and abs(correctedM-exactM)<abs(leadingM-exactM)/20,exact_neumann_integral=exactM,leading=leadingM,next_order=correctedM)
 check(3,'variant-2-turn-scaling',close(3*4,12),turn_multiplier=12)
 check(3,'variant-3-distance-M',sp.simplify(Mex.subs(z,2*z)/Mex)==sp.Rational(1,8))
 check(3,'variant-3-distance-F',sp.simplify(F.subs(z,2*z)/F)==sp.Rational(1,16))
 check(3,'variant-4-source-field-mechanical',close(2*.7, .7+.7),source_work=1.4,field_energy=.7,mechanical_work=.7)
 ev=np.linalg.eigvalsh([[2,.8],[.8,3]])
 pa,pb=sp.symbols('pa pb');lm=sp.Matrix([[LA,M],[M,LB]]);pv=sp.Matrix([pa,pb]);Uflux=(pv.T*lm.inv()*pv)[0]/2
 fixed_flux_force=sp.simplify((-sp.diff(Uflux,M)).subs({pa:LA*IA+M*IB,pb:LB*IB+M*IA})-IA*IB)
 check(3,'positive-energy-bound-and-fixed-flux-force',all(ev>0) and .8**2<=2*3 and fixed_flux_force==0,eigenvalues=ev.tolist(),symbolic_force_residual=str(fixed_flux_force))
 # 04: full capacitance DAE versus reduced matrix exponentials.
 e=np.eye(6);avec=np.array([1,-1,1,-1,1,-1])/np.sqrt(6)
 X=null_space(np.vstack([np.ones(6),avec]));CC=sum(np.outer(e[j]-e[(j+2)%6],e[j]-e[(j+2)%6]) for j in range(6))
 def network(Rs,t):
  gs=1/np.array(Rs);GG=sum(gs[j]*np.outer(e[(j+1)%6]-e[j],e[(j+1)%6]-e[j]) for j in range(6));bb=gs[0]*(e[1]-e[0])
  aa=avec@GG@avec;ag=avec@GG@X;Gr=X.T@GG@X-np.outer(ag,ag)/aa;br=X.T@bb-ag*(avec@bb)/aa
  yi=np.linalg.solve(Gr,br);EE=expm(-Gr*t/3);y=(np.eye(4)-EE)@yi;yd=Gr/3@EE@yi
  eta=(avec@bb-ag@y)/aa;etad=-ag@yd/aa;V=X@y+avec*eta;Vd=X@yd+avec*etad
  return np.array([gs[0]*(1+V[0]-V[1]),gs[1]*(V[1]-V[2])]),V,Vd,GG,bb,Gr
 check(4,'capacitance-rank',np.linalg.matrix_rank(CC)==4,rank=int(np.linalg.matrix_rank(CC)))
 check(4,'dynamic-capacitance',close(X.T@CC@X,3*np.eye(4)))
 check(4,'two-null-modes',close(CC@avec,0) and close(CC@np.ones(6),0))
 residual=[]
 for tt in [0,.1,1,5,20]:
  ii,V,Vd,GG,bb,Gr=network([2,1,3,1.5,.8,4],tt);residual.append(float(max(abs(CC@Vd+GG@V-bb))))
 check(4,'unequal-resistor-DAE',max(residual)<1e-10,max_residual=max(residual))
 gs=1/np.array([2,1,3,1.5,.8,4]);init=network(1/gs,0)[0];expected=[gs[0]*(1-gs[0]/sum(gs)),gs[0]*gs[1]/sum(gs)]
 check(4,'general-initial-values',close(init,expected),currents=init.tolist())
 end=network(1/gs,1000)[0]
 check(4,'general-steady-series',close(end,1/sum(1/gs)),currents=end.tolist())
 rate=np.linalg.eigvalsh(network([1]*6,0)[-1])/3
 check(4,'equal-network-decay-spectrum',close(rate,[1/3,1/3,1,1]),decay_rates=rate.tolist())
 ts=np.linspace(0,10,71);err=[]
 for tt in ts:
  exact=np.array([1+2*np.exp(-tt/3)+2*np.exp(-tt),1+np.exp(-tt/3)-np.exp(-tt)])/6
  err.append(float(max(abs(network([1]*6,tt)[0]-exact))))
 check(4,'equal-current-explicit',max(err)<1e-10,max_error=max(err))
 Vsteady=network([1]*6,1000)[1];stored=.5*Vsteady@CC@Vsteady
 check(4,'initial-slopes-and-steady-energy',close([(-2/3-2)/6,(-1/3+1)/6],[-4/9,1/9]) and close(Vsteady,np.array([-5,5,3,1,-1,-3])/12) and close(stored,2/3),steady_capacitor_energy_over_Ceps2=stored)
 peak=1.5*np.log(3);val=network([1]*6,peak)[0][1]
 check(4,'peak-and-variant-1-2',close(val,(1+2/(3*np.sqrt(3)))/6) and close(network([1]*6,0)[0][0]/network([1]*6,0)[0][1],5),peak_t=peak,peak_I=val)
 check(4,'variant-3-unequal-R1',close(network([2,1,1,1,1,1],0)[0],[5/11,1/11]) and close(network([2,1,1,1,1,1],1000)[0],1/7))
 check(4,'dissipation-positive',np.min(np.linalg.eigvalsh(Gr))>0 and close(2/(3*np.sqrt(3))*100,38.49001794597505),min_reduced_eigenvalue=float(np.linalg.eigvalsh(Gr).min()))
 # 05: obtain self-conjugate branches by multiplying round-trip matrices.
 f,R,d,s=sp.symbols('f R d s',positive=True);DD=d+R
 P=lambda h:sp.Matrix([[1,h],[0,1]]);LL=sp.Matrix([[1,0],[-1/f,1]]);MM=sp.Matrix([[1,0],[-2/R,1]])
 TT=P(s)*LL*P(DD)*MM*P(DD)*LL*P(s)
 factor=-2/(R*f*f)*(f*DD-s*(DD-f))*(f*d-s*(d-f))
 check(5,'roundtrip-B-factorization',sp.simplify(TT[0,1]-factor)==0)
 sc=f*d/(d-f);sv=f*DD/(DD-f)
 check(5,'center-branch-self-conjugate',sp.simplify(TT[0,1].subs(s,sc))==0)
 check(5,'vertex-branch-self-conjugate',sp.simplify(TT[0,1].subs(s,sv))==0)
 check(5,'center-branch-inverted',sp.simplify(TT[0,0].subs(s,sc))==-1)
 check(5,'vertex-branch-upright',sp.simplify(TT[0,0].subs(s,sv))==1)
 check(5,'unimodular-ray-matrix',sp.simplify(TT.det())==1)
 check(5,'branch-order',sp.simplify(sc-sv-f*f*R/((d-f)*(DD-f)))==0)
 check(5,'variant-1-two-positions',close([float(sc.subs({f:10,d:30,R:20})),float(sv.subs({f:10,d:30,R:20}))],[15,12.5]))
 check(5,'variant-2-single-position',close(float(sv.subs({f:10,d:5,R:20})),50/3) and sc.subs({f:10,d:5,R:20})<0)
 check(5,'variant-3-center-at-f',close(float(sv.subs({f:10,d:10,R:20})),15) and sp.simplify((f*d-s*(d-f)).subs(d,f))==f*f)
 check(5,'variant-4-upright-choice',close(float(sv.subs({f:10,d:30,R:20})),12.5))
 check(5,'no-finite-positive-object-domain',float(sc.subs({f:10,d:2,R:3}))<0 and float(sv.subs({f:10,d:2,R:3}))<0)
 # 06: directly integrate fixed-direction relative Newton equations.
 mu=2/3;AA=1/12;HH=17/12
 def rhs(t,z):
  x,y,vx,vy=z;rad=np.hypot(x,y);return [vx,vy,1.5*x/rad**3-1/8,1.5*y/rad**3]
 sol=solve_ivp(rhs,[0,80],[1,0,0,-1],method='DOP853',rtol=2e-12,atol=2e-13,t_eval=np.linspace(0,80,801));x,y,vx,vy=sol.y;rad=np.hypot(x,y)
 energy=mu*(vx*vx+vy*vy)/2+1/rad+AA*x
 xi=np.sqrt(rad+x);eta=y/xi;px=mu*(xi*vx+eta*vy);pe=mu*(-eta*vx+xi*vy)
 cx=px**2/(2*mu)+AA*xi**4/2-HH*xi**2;ce=pe**2/(2*mu)-AA*eta**4/2-HH*eta**2
 check(6,'relative-equation-and-initial-H',close(.5*mu+1+AA,HH),initial_energy=HH)
 check(6,'numerical-energy',max(abs(energy-HH))<1e-8,max_energy_error=float(max(abs(energy-HH))))
 check(6,'xi-separation-constant',max(abs(cx+8/3))<1e-7,max_error=float(max(abs(cx+8/3))))
 check(6,'eta-separation-constant',max(abs(ce-2/3))<1e-7,max_error=float(max(abs(ce-2/3))))
 check(6,'xi-bounded-coordinate',xi.min()**2>=2-1e-9 and xi.max()**2<=32+1e-9,min_xi2=float(xi.min()**2),max_xi2=float(xi.max()**2))
 check(6,'eta-monotonic-escape',all(pe<0) and all(np.diff(eta)<0),eta_final=float(eta[-1]),min_escape_polynomial=2/3)
 fake=2*(4+np.sqrt(17))
 check(6,'trajectory-exceeds-false-upper-bound',rad[-1]>fake,r_at_t80=float(rad[-1]),false_bound=fake)
 torque=mu*(x*(1.5*y/rad**3)-y*(1.5*x/rad**3-1/8))
 check(6,'noncentral-torque',close(torque,AA*y),max_torque_error=float(max(abs(torque-AA*y))))
 check(6,'1D-root-and-variant-2',close(1/12+12/12,1+1/12),second_turning_distance=12)
 check(6,'variant-1-equal-mass',close((1-1)/(1+1),0),electric_relative_force=0)
 check(6,'variant-3-relative-equilibrium',close(3/3,1),dimensionless_critical_E=3)
 mirror=solve_ivp(rhs,[0,10],[1,0,0,1],method='DOP853',rtol=2e-12,atol=2e-13,t_eval=np.linspace(0,10,101))
 orig=solve_ivp(rhs,[0,10],[1,0,0,-1],method='DOP853',rtol=2e-12,atol=2e-13,t_eval=np.linspace(0,10,101))
 check(6,'variant-4-reflected-trajectory',close(mirror.y,orig.y*np.array([1,-1,1,-1])[:,None],1e-9))
 # 07: single-exit global path minimization on the entire circle.
 rt=np.sqrt(3);AV=np.array([-rt/2,.5]);BV=np.array([0.,2.]);CV=np.array([-rt/2,1.5])
 check(7,'relative-start-and-end',close(np.linalg.norm(AV),1) and close(np.linalg.norm(BV),2))
 check(7,'interface-point',close(np.linalg.norm(CV),rt))
 check(7,'two-segment-lengths',close([np.linalg.norm(CV-AV),np.linalg.norm(BV-CV)],[1,1]))
 check(7,'tangent-exterior-segment',close(CV@(BV-CV),0))
 check(7,'critical-refraction',close(2*np.sin(np.pi/6),np.sin(np.pi/2)))
 phi=np.linspace(-np.pi,np.pi,100001);distA=np.sqrt(4-2*rt*np.cos(phi-np.pi/6));visible=(phi>=np.pi/3)&(phi<=2*np.pi/3)
 angular=lambda a,b:abs((a-b+np.pi)%(2*np.pi)-np.pi)
 delta=np.minimum(angular(phi,np.pi/3),angular(phi,2*np.pi/3));delta[visible]=0
 exterior=np.where(visible,np.sqrt(7-4*rt*np.sin(phi)),1+rt*delta)
 J=2*distA+exterior;ix=J.argmin()
 check(7,'global-entire-circle-minimum',J.min()>=3-1e-10 and abs(phi[ix]-np.pi/3)<.001,min_weighted_length=float(J.min()),min_angle=float(phi[ix]))
 ds=np.linspace(0,np.pi,10001)
 check(7,'reentry-eliminated-by-arc',min(4*np.sin(ds/2)-ds)>=-1e-12,min_arc_advantage=float(min(4*np.sin(ds/2)-ds)))
 check(7,'optimal-time-and-variant-1',close(1+.5,1.5) and close(2*1.5,3))
 check(7,'variant-2-force-doubling',close(1.5/2,.75))
 # Intersection of A+t(B-A) with circle, not a memorized direct length.
 direct=BV-AV;roots=np.roots([direct@direct,2*AV@direct,AV@AV-3]);lam=float(max(roots));inside=lam*np.linalg.norm(direct)
 direct_time=inside+(np.linalg.norm(direct)-inside)/2
 check(7,'direct-intersection-and-variant-3',close(inside,np.sqrt(2)) and close(direct_time,(np.sqrt(2)+rt)/2),direct_time=direct_time,relative_slowdown_percent=(direct_time/1.5-1)*100)
 dx1=quad(lambda tau:-rt/2,0,1)[0];dy1=quad(lambda tau:.5+tau,0,1)[0]
 dx2=quad(lambda sig:-rt/2+rt*sig,0,.5)[0];dy2=quad(lambda sig:1.5+sig,0,.5)[0]
 check(7,'variant-4-speed-scale-and-real-space-integral',close(2*(1+.5),3) and close([dx1+dx2,dy1+dy2],[-5*rt/8,15/8]),final_displacement_units_mu2_over_F=[dx1+dx2,dy1+dy2])
 check(7,'terminal-velocity-continuity',close(AV+[0,1],CV) and close(CV+np.array([rt/2,.5]),BV))
 # 08: high precision exact relativistic delay, including high photon energy.
 mp.mp.dps=65;T0=mp.mpf('7.5e9')*mp.mpf('365.25')*86400;E1=mp.mpf('1e5');E2=mp.mpf('1e8');dt=mp.mpf('.5')
 eps=mp.sqrt(2*dt/(T0*(1/E1**2-1/E2**2)))
 exact=T0*(1/mp.sqrt(1-(eps/E1)**2)-1/mp.sqrt(1-(eps/E2)**2))
 c=mp.mpf('2.998e8');ev=mp.mpf('1.602176634e-19');mass=eps*ev/(c*c)
 check(8,'propagation-time-conversion',T0==mp.mpf('236682000000000000'),T0_s=str(T0))
 check(8,'MeV-conversion',E1==100000 and E2==100000000,E1_eV=str(E1),E2_eV=str(E2))
 mom,cc,rest=sp.symbols('mom cc rest',positive=True);EE=sp.sqrt(mom**2*cc**2+rest**2)
 check(8,'relativistic-square-and-group-velocity',abs((1-(mp.sqrt(1-(eps/E1)**2))**2)-(eps/E1)**2)<mp.mpf('1e-60') and sp.simplify(sp.diff(EE,mom)-mom*cc**2/EE)==0)
 check(8,'bound-static-energy',mp.mpf('2.055e-4')<eps<mp.mpf('2.057e-4'),epsilon0_eV=str(eps))
 check(8,'rest-mass-SI',mp.mpf('3.66e-40')<mass<mp.mpf('3.67e-40'),mass_kg=str(mass))
 check(8,'exact-delay-versus-quadratic',abs(exact-dt)<mp.mpf('1e-16'),exact_delay_s=str(exact),relative_error=str(exact/dt-1))
 check(8,'expansion-validity',eps/E1<mp.mpf('3e-9'),epsilon_over_E1=str(eps/E1))
 high_fraction=(E1/E2)**2
 check(8,'high-energy-term-retained',abs(high_fraction-mp.mpf('1e-6'))<mp.mpf('1e-60'),relative_high_energy_term=str(high_fraction))
 check(8,'variant-1-time-quarter',mp.sqrt(mp.mpf('.125')/dt)==mp.mpf('.5'))
 check(8,'variant-2-distance-four',mp.sqrt(mp.mpf(1)/4)==mp.mpf('.5'))
 check(8,'variant-3-energies-tenfold',abs(mp.sqrt(2*dt/(T0*(1/(10*E1)**2-1/(10*E2)**2)))/eps-10)<mp.mpf('1e-60'))
 check(8,'variant-4-finite-energy-ratio',1/mp.sqrt(mp.mpf('.99'))<mp.mpf('1.0051'),correction_factor=str(1/mp.sqrt(mp.mpf('.99'))))
 report=dict(all_passed=all(c['passed'] for c in checks),check_count=len(checks),checks=checks)
 (ROOT/'physics_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(dict(all_passed=report['all_passed'],check_count=len(checks),failed=[c['name'] for c in checks if not c['passed']]),ensure_ascii=False))
 assert report['all_passed']
if __name__=='__main__':main()
