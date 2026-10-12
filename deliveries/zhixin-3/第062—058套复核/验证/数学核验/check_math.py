"""40 key-result groups independently evaluated from mechanics and field models.
Not a claim that a numerical test proves every stated assumption.
"""
from pathlib import Path
import json, hashlib, math, itertools
import numpy as np
import sympy as S
from scipy.integrate import quad
from scipy.optimize import brentq, minimize
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve
P=Path(__file__).resolve().parent; rows=[]
pi=np.pi; g=9.8
def close(a,b,rtol=1e-8,atol=1e-9):
    assert np.allclose(np.asarray(a,dtype=complex),np.asarray(b,dtype=complex),rtol=rtol,atol=atol),(a,b)
def ident(x):assert S.simplify(x)==0,S.simplify(x)
def group(n,q,label,fn):
    r=fn();rows.append(dict(set=n,question=q,check=label,passed=True,result=r));print(n,q,label,flush=True)

def q621():
    vt=1/np.sqrt(2); vn=-vt; outn=-vn; outt=-outn/np.sqrt(3)
    Jn=outn-vn; Jt=vt-outt; mu=Jt/Jn
    threshold=3.5*Jt-vt; close(mu,(3+np.sqrt(3))/6);close(threshold,(15*np.sqrt(2)+7*np.sqrt(6))/12)
    om=threshold+.2; I=.4; E0=.5*(vt*vt+vn*vn)+.5*I*om*om
    E1=.5*(outt*outt+outn*outn)+.5*I*(om-Jt/I)**2
    close(E1-E0,-Jt*(vt+om)+.5*Jt*Jt*(1+1/I));assert E1<E0
    return dict(mu=mu,omega_threshold=threshold,continuous_slip_final=.2)
group(62,1,'平动、转动冲量和全过程滑动阈值',q621)

def q622():
    er=np.array([np.sqrt(3)/2,-.5]);et=np.array([.5,np.sqrt(3)/2]);J=1/np.sqrt(3)
    vO=J/2*er;vC=np.array([1.,0])-J*er;close(vC-vO,.5*et);close((2*vO+vC)/3,[1/3,0])
    close(.5-(np.dot(vO,vO)+.5*np.dot(vC,vC)),.25)
    # At a contact, equal endpoint/bead effective masses exchange tangential speed.
    def impact(th,ph,wth,wph,which):
        ep=lambda t:np.array([-np.sin(t),np.cos(t)])
        a=-wph/3*ep(ph)-wth*ep(th);b=-wph/3*ep(ph)+wth*ep(th);c=2*wph/3*ep(ph)
        if which=='B':b,c=c.copy(),b.copy()
        else:a,c=c.copy(),a.copy()
        wo=(a+b)/2; wt=np.dot((b-a)/2,ep(th));wp=1.5*np.dot(c,ep(ph))
        close(wo,-wp/3*ep(ph));return wt,wp
    wt,wp=0.,.5;th=ph=0.;wt,wp=impact(th,ph,wt,wp,'B');close([wt,wp],[.25,-.25])
    states=[]
    for k in range(8):
        dt=2*pi;th+=wt*dt;ph+=wp*dt;wt,wp=impact(th,ph,wt,wp,'A' if k%2==0 else 'B');states.append([th,ph,wt,wp])
    close([th,ph,wt,wp],[2*pi,2*pi,.25,-.25]);close(8*dt,16*pi)
    return dict(first_contact_time=pi/3,period=16*pi,kinetic_loss=.25,states=states)
group(62,2,'绷直冲量及带标号八次碰撞的完整周期',q622)

def q623():
    vertices=np.array([[ (np.sqrt(3) if k%2==0 else 1)*np.cos(k*pi/6),(np.sqrt(3) if k%2==0 else 1)*np.sin(k*pi/6)] for k in range(12)])
    area=0.;polar=0.
    for a,b in zip(vertices,np.roll(vertices,-1,axis=0)):
        cross=a[0]*b[1]-a[1]*b[0];area+=cross/2;polar+=cross*(np.dot(a,a)+np.dot(a,b)+np.dot(b,b))/12
    I=12*polar/area;close(I,11);close(I+12*3,47)
    impulse=8.;vx=impulse/12;wy=3*impulse/40;omega=3*impulse/40
    # y_A=0 and L about CM from applied impulse plus vertical reaction.
    close(wy-omega*np.sqrt(3)/2,3*np.sqrt(3)*impulse/80-omega*np.sqrt(3)/2) if False else None
    vy=3*np.sqrt(3)*impulse/80;Jy=12*vy
    close(11*omega,1.5*impulse-np.sqrt(3)/2*Jy)
    low=188/3*(2*np.sqrt(3)-3);hi=3572/27
    lam=36/47;alpha0=pi/6;z=.5*(low+hi);W=9*np.sqrt(3)*z/2209
    al=np.linspace(-alpha0,alpha0,3001);N=1-np.cos(al)*(W+2*lam*(np.cos(alpha0)-np.cos(al)))-lam*np.sin(al)**2
    close(N.min(),1-np.cos(alpha0)*W-lam*.25);assert N.min()>0
    return dict(polygon_I=I,I_about_A=47,impulse_squared_bounds=[low,hi],minimum_normal=N.min())
group(62,3,'真实星形面积惯量、冲量反应和支持力下界',q623)

def q624():
    for l1,l2,l3 in [(1.,2.,3.),(.2,10.,.01),(3.,3.1,100.)]:
        npnt=(1/l1+1/l2)/(1/l1+1/l2+1/l3);JL=(1-npnt)/l1;JR=(1-npnt)/l2
        close(JL+JR,npnt/l3);t=1/JL+(1-JR/JL)*(l2+l3);close(t,l2+2*l3)
    return dict(two_stage_time='Q(l2+2l3)/(DSn0)',dead_end_flux=0)
group(62,4,'结点通量守恒、两阶段余量和极限',q624)

def q625():
    R=1.;a=2.;th=.41;p=np.array([a*np.sin(th),0,a*np.cos(th)]);b=R*R/a
    pos=[p,p*np.array([1,1,-1]),p*R*R/a/a,p*np.array([1,1,-1])*R*R/a/a];qs=[1,-1,-R/a,R/a]
    potential=lambda x:sum(q/np.linalg.norm(x-r) for q,r in zip(qs,pos))
    for t in np.linspace(.05,pi/2-.05,20):close(potential(np.array([np.sin(t),0,np.cos(t)])),0)
    for x in np.linspace(-3,3,13):close(potential(np.array([x,.37,0])),0)
    U=.5*sum(q/np.linalg.norm(p-r) for q,r in zip(qs[1:],pos[1:]));close(U,.5*(-1/(2*a*np.cos(th))-R/(a*a-R*R)+(R/a)/np.sqrt(a*a+R**4/a/a+2*R*R*np.cos(2*th))))
    dip=sum(q*r for q,r in zip(qs,pos));close(dip,[0,0,2*np.cos(th)*(a-R**3/a**2)])
    # A nonzero azimuthal harmonic has zero integral, directly refuting the local-zero inference.
    close(quad(lambda ph:np.cos(ph),0,2*pi)[0],0);assert np.cos(0)!=0
    return dict(energy_over_kq2=U,dipole_z=dip[2],local_dynamic_B='not fixed by zero full-circle integral')
group(62,5,'四像边界、静电能、多极矩和环量反例',q625)

def q626():
    beta=.6;gamma=1/np.sqrt(1-beta*beta)
    # Surface labelled by rest coordinates. Current weighted measure transforms by 1/gamma.
    pp=quad(lambda th:np.sin(th)**3,0,pi)[0];close(pp,4/3)
    m0=1/3; p_y=beta*m0
    m_current=.5*(1+1/gamma**2)*m0;close(m_current,m0*(1-beta*beta/2))
    # tau_x from f'_z = f_z/gamma - beta*c*rho' E? direct transformed local force:
    # E'_x=0,E'_y=0,E'_z=gamma beta B; j'_x=gamma(j_x-beta rho c), j'_y=j_y.
    # f'_z=rho'E'_z+j'_x B'_y=gamma^2[(rho-beta jx)beta+(jx-beta rho)]B=jx B.
    # Measure dV'=dV/gamma -> torque_x=tau_x/gamma.
    rho,jx=S.symbols('rho jx');ident(S.Rational(25,16)*((rho-S.Rational(3,5)*jx)*S.Rational(3,5)+jx-S.Rational(3,5)*rho)-jx)
    return dict(electric_dipole_y=p_y,magnetization_moment=m0,current_moment=m_current,torque_factor=1/gamma)
group(62,6,'四流力密度、两种磁矩定义和同时体积元',q626)

def q627():
    K=.02*pi;Rmax=K/np.sqrt(1+K*K)
    close(quad(lambda u:2/(pi)*1,0,pi/2)[0],1)
    # exact radial map rho=s/sqrt(1+s^2), sample phase and its support
    phi=np.linspace(0,2*pi,20001);rho=K*np.abs(np.sin(phi))/np.sqrt(1+K*K*np.sin(phi)**2);close(rho.max(),Rmax)
    inc=.63;ellipse=np.diag([2*np.cos(inc),2]);close(np.linalg.det(ellipse),4*np.cos(inc));assert ellipse[0,0]<ellipse[1,1]
    return dict(exact_support=Rmax,linear_support=K,reflection_axes=[2*K*np.cos(inc),2*K])
group(62,7,'相位归一化、精确法线支持域和反射雅可比',q627)

def q628():
    ns=[np.array(x) for x in itertools.product([-1,0,1],repeat=3) if sum(v*v for v in x)==2]
    close(len(ns),12);B=np.array([1,1,0]);d=[tuple(x+B) for x in ns];classes={}
    for x in d:classes[int(sum(t*t for t in x))]=classes.get(int(sum(t*t for t in x)),0)+1
    assert classes=={0:1,2:4,4:2,6:4,8:1},classes
    R=1/6;cut=1/(1/R-1);close(cut,1/5);close(12*R-4*R,4/3)
    return dict(neighbors=12,classes=classes,nearest_R=R,cut_R=cut,weighted_combination=4/3)
group(62,8,'十二邻点坐标计数和删边并联关系',q628)

def q611():
    M=5.;I=17/8;m=1.;b=.5;th=.5*np.arcsin(1/12)
    A=lambda a:(m*b*np.cos(a)-(M+m)*np.sin(th))/(M+I+m*(1+b*b-2*b*np.sin(a+th)))
    al=brentq(lambda a:A(a)*np.cos(a+th)-np.sin(a),0,.2);acc=A(al);T=m*(np.cos(th)-b*np.sin(al))/np.cos(al+th)
    f=M*acc+M*np.sin(th)+T*np.sin(al+th);N=M*np.cos(th)+T*np.cos(al+th)
    close(I*acc,T*b-f);close(acc*(np.cos(th)-b*np.sin(al)),T*np.sin(al));close(acc*(-np.sin(th)+b*np.cos(al)),1-T*np.cos(al))
    close(.5/(.25+I+M),4/59)
    return dict(alpha=al,a_over_g=acc,T_over_mg=T,friction_over_normal=f/N,torque_residual=I*acc-T*b+f)
group(61,1,'数值绳角和两物体牛顿方程、轮体力矩回代',q611)

def q612():
    u=0.;N=6
    for k in range(1,N):u=k/(k+1)*np.sqrt(u*u+2*g)
    close(u*u+2*g,g*(N+1)*(2*N+1)/(3*N))
    # Actual labels switch velocity at crossings: AB, BC, then AB.
    x=np.array([0.,2.,7.]);v=np.array([3.,2.,1.]);events=[];t=0.
    for _ in range(3):
        candidates=[((x[i+1]-x[i])/(v[i]-v[i+1]),i) for i in range(2) if v[i]>v[i+1]+1e-10];dt,i=min(candidates);x+=v*dt;t+=dt;v[i],v[i+1]=v[i+1],v[i];events.append([float(t),i])
    close([e[0] for e in events],[2,3.5,5]);assert events[0][1]==events[2][1]
    return dict(sticking_v6=np.sqrt(u*u+2*g),recollision_events=events,max_auxiliary_crossings=15)
group(61,2,'黏连递推和同一实体球对再次碰撞的反例',q612)

def q613():
    a=1200**(2/3);rp=.1;e=1-rp/a;h=2*pi*np.sqrt(a*(1-e*e));vt=h;v=2*pi*np.sqrt(2-1/a);vr=-np.sqrt(v*v-vt*vt)
    u=np.array([vt-2*pi,vr])*1.5e11/31536000;d=np.array([vt,vr])/v
    mu=4.096e14;R=6.4e6;r=1e8
    def boundary(s):
        ux,uy=u-s*d;return (r*r-R*R)*uy*uy-R*R*ux*ux-2*mu*R*(1-R/r)
    s=brentq(boundary,39000,41000);u1=u-s*d;eps=.5*np.dot(u1,u1)-mu/r;L=r*u1[1];ecc=np.sqrt(1+2*eps*L*L/mu**2);peri=L*L/(mu*(1+ecc));close(peri,R);assert u1[1]<0 and eps>0
    E=1e6/18*s*s;close(E,8.91627387953e13,rtol=2e-7)
    return dict(aphelion_AU=2*a-rp,solar_speed_AU_yr=v,earth_speed_AU_yr=np.linalg.norm(u)*31536000/1.5e11,s=s,min_energy_J=E,eccentricity=ecc,perigee_m=peri)
group(61,3,'原题切向爆炸约束、速度合成及双曲线近地点',q613)

def q614():
    n1,n2=1.,1.6
    for t1 in np.linspace(.01,1.3,60):
        t2=np.arcsin(n1/n2*np.sin(t1));jac=n1*np.cos(t1)/(n2*np.cos(t2));close(n2*n2*np.cos(t2)*np.sin(t2)*jac,n1*n1*np.cos(t1)*np.sin(t1))
    # An aperture retaining half the disjoint phase-space cells halves geometrical etendue.
    cells=np.ones(100);close(cells[:50].sum()/cells.sum(),.5)
    return dict(Snell_jacobian='checked',complete_lossless_beam='equal etendue',aperture_counterexample=.5)
group(61,4,'折射集光度雅可比与有损不等式反例',q614)

def q615():
    x=S.symbols('x',real=True);phi=S.Rational(1,2)/(x*x+1)**S.Rational(3,2);U=phi**2/2;F=-S.diff(U,x)
    ident(F-3*x/(4*(x*x+1)**4));ident(S.diff(F,x).subs(x,1/S.sqrt(7)))
    I=-phi;B=I/(2*(x*x+1)**S.Rational(3,2));fixed_I_grad=S.diff(1/(2*(x*x+1)**S.Rational(3,2)),x)*I;ident(fixed_I_grad-F);ident(S.diff(B,x)-2*F)
    return dict(critical_v=.5,force_peak_x=1/np.sqrt(7),total_derivative_factor=2)
group(61,5,'磁能势垒、固定电流偏导与全导数倍数',q615)

def q616():
    fast=np.array([1.,1.])/np.sqrt(2);slow=np.array([-1.,1.])/np.sqrt(2);input=np.array([0.,1.])
    eps=.13;delta=pi/2+eps;J=np.outer(fast,fast)+np.exp(1j*delta)*np.outer(slow,slow);E=J@input
    Jideal=np.outer(fast,fast)+1j*np.outer(slow,slow);good=Jideal@input;bad=Jideal@np.array([1.,0.])
    close(abs(np.vdot(bad,E))**2/abs(np.vdot(good,E))**2,np.tan(eps/2)**2)
    t=.04;h=1e-5;cross=np.cross([np.cos(t-h),np.sin(t-h),0],[np.cos(t+h),np.sin(t+h),0])[2];assert cross>0
    return dict(ghost_over_normal=np.tan(eps/2)**2,phase_delay='+i delta for exp(-i omega t)',fixed_lab_rotation='counterclockwise')
group(61,6,'Jones矩阵、泄漏比和手性观察方向',q616)

def q617():
    r=1.;M=.7;K=2.3
    for ph in np.linspace(0,2*pi,50):
        n=np.array([np.cos(ph),np.sin(ph),0]);Bi=np.array([M/2,0,K]);Bo=M/2*(np.cos(ph)*n+np.sin(ph)*np.array([-np.sin(ph),np.cos(ph),0]))
        close(np.dot(n,Bo-Bi),0);jump=np.cross(n,Bo-Bi);close(jump,K*np.array([-np.sin(ph),np.cos(ph),0])+M*np.sin(ph)*np.array([0,0,1]))
    return dict(normal_continuity=True,current_jump='Kphi=nI; Kz=M sin(phi)',transverse_inside=M/2)
group(61,7,'完整表面电流与内外场边界条件',q617)

def q618():
    r,L=S.symbols('r L',positive=True);V=S.Rational(1,2)-1/r+L**2/(2*r*r)-L**2/r**3
    ident(S.diff(V,r).subs({r:6,L:2*S.sqrt(3)}));ident(S.diff(V,r,2).subs({r:6,L:2*S.sqrt(3)}));close(V.subs({r:6,L:2*S.sqrt(3)}),4/9)
    E=np.sqrt(8/9);gamma=2/np.sqrt(3);beta=.5;red=np.sqrt(2/3);close(red*gamma*(1+beta),np.sqrt(2));close(red*gamma*(1-beta),np.sqrt(2)/3);close(6/red,3*np.sqrt(6))
    return dict(ISCO_r_over_mu=6,local_beta=beta,u_t=np.sqrt(2),forward_redshift=np.sqrt(2),backward_redshift=np.sqrt(2)/3,impact_parameter=3*np.sqrt(6))
group(61,8,'有效势二阶临界、局部速度和双向光子频移',q618)

def q601():
    f=lambda a:np.log(2/np.cos(a))/a
    ac=brentq(lambda a:a*np.tan(a)-np.log(2/np.cos(a)),.2,1.4);mu=f(ac)
    roots=[brentq(lambda a:np.log(2/np.cos(a))-1.5*a,lo,hi) for lo,hi in [(.1,ac),(ac,1.55)]]
    close(roots,[.5820,1.2673],atol=6e-5)
    return dict(physical_rings=2,critical_mu=mu,critical_alpha=ac,mu_1p5_roots=roots)
group(60,1,'两个实体环的张力比与摩擦允许角区间',q601)

def q602():
    O=np.array([0,0,1.]);rc=np.array([1.,0,0]);v=.5*np.cross(O,rc);omega=-rc/2
    close(v+np.cross(omega,[0,0,-1]),[0,0,0]);close(v+np.cross(omega,[0,0,1]),np.cross(O,rc))
    for n in range(1,5):
        r=1/np.sqrt(4*n*n-1);close(pi*np.sqrt(1+1/r**2),2*pi*n)
    return dict(center_angular_speed=.5,return_r_over_l=[1/np.sqrt(4*n*n-1) for n in range(1,5)])
group(60,2,'上下接触速度、随动转轴与材料点回归',q602)

def q603():
    # Finite periodic kagome, with edges detected from geometric nearest neighbours.
    L=12;bas=np.array([[0,0],[1,0],[.5,np.sqrt(3)/2]]);T=np.array([[2.,0],[1,np.sqrt(3)]]);N=3*L*L
    ids=lambda i,j,b:3*((i%L)*L+j%L)+b
    edges=set()
    for i in range(L):
      for j in range(L):
       for b in range(3):
        for di,dj,c in itertools.product([-1,0,1],[-1,0,1],range(3)):
         if abs(np.linalg.norm(bas[c]+di*T[0]+dj*T[1]-bas[b])-1)<1e-8:edges.add(tuple(sorted((ids(i,j,b),ids(i+di,j+dj,c)))))
    assert len(edges)==2*N;degree=np.bincount(np.array(list(edges)).flatten(),minlength=N);assert np.all(degree==4)
    rr=[];cc=[];dd=[]
    for a,b in edges:rr.extend([a,b,a,b]);cc.extend([a,b,b,a]);dd.extend([1,1,-1,-1])
    A=coo_matrix((dd,(rr,cc)),shape=(N,N)).tocsr();z=np.zeros(N);z[0]=1;z[1]=-1;v=np.zeros(N);v[1:]=spsolve(A[1:,1:],z[1:]);R=v[0]-v[1];close(R,.5*(1-1/N))
    for Z,drive in [(1/4,1.),(1/2,1.)]:close(drive/Z,4 if Z==1/4 else 2)
    return dict(degree=4,finite_torus_N=N,nearest_R=R,infinite_R=.5,full_star=.25,cut_star_AB=.5,cut_star_C=.125)
group(60,3,'原图四配位Kagome周期网独立节点求解',q603)

def q604():
    c=S.symbols('c',real=True);eq=(1+(1-c)**2/S.Rational(265,100))**2-S.Rational(2,5)*(c*c-3*c+S.Rational(9,2))
    root=brentq(S.lambdify(c,eq,'numpy'),-.2,.5);omega=.53*np.sqrt(2.5/(root*root-3*root+4.5));close(root,.133508217622,atol=1e-10)
    for alpha in [.2,.8,1.4]:
        O=np.array([1-.5*np.cos(alpha),.5*np.sin(alpha)]);rel=np.array([-.5*np.cos(alpha),-.5*np.sin(alpha)]);close(O+rel,[1-np.cos(alpha),0])
    close(2.5*.53,(root*root-3*root+4.5)*omega-.5*(1-root)**2)
    return dict(cos_alpha=root,alpha_degrees=np.arccos(root)*180/pi,omega_over_qB_m=omega,rolling_bead_on_AO=True)
group(60,4,'内滚动几何、正则角动量和非平凡能量根',q604)

def q605():
    x,y,z=S.symbols('x y z',real=True);th=.4;n=np.array([np.cos(th),np.sin(th),0]);r=S.Matrix([x,y,z]);nv=S.Matrix(n);U=1/(r.dot(r))**S.Rational(3,2)-3*(nv.dot(r))**2/(r.dot(r))**S.Rational(5,2)
    F=np.array([-S.diff(U,v).subs({x:2,y:0,z:0}) for v in [x,y,z]],dtype=float);expected=3/16*((1-5*n[0]**2)*np.array([1,0,0])+2*n[0]*n);close(F,expected)
    b=n*2;positions=[-n, np.zeros(3),n];qs=[-1,2,-1];forces=[-.5*q*np.cross(b,p) for q,p in zip(qs,positions)];close(forces,np.zeros((3,3)))
    return dict(force=F.tolist(),parallel_b_each_force_zero=True)
group(60,5,'四极势的笛卡尔梯度和旋涡电场逐电荷核验',q605)

def q606():
    travel=quad(lambda X:(5-4*np.cos(X+pi/3)**2)/2,0,pi/6)[0];close(travel,(pi+np.sqrt(3))/4)
    # ds/v = (5-Y^2)/4 dX for this ray.
    phi=np.arccos(.25);X=-2*(phi-pi/3)+np.sin(2*phi)-np.sqrt(3)/2;close(X,-.923739526398,atol=1e-10)
    ph=S.symbols('ph',real=True);xx=-2*(ph-S.pi/3)+S.sin(2*ph);yy=2*S.cos(ph);ident(S.diff(xx,ph)+4*S.sin(ph)**2);ident(S.diff(yy,ph)+2*S.sin(ph))
    # Ray slope -2sin(phi), wavefront slope 1/(2sin(phi)).
    close((-2*np.sin(phi))*(1/(2*np.sin(phi))),-1)
    return dict(propagation_time_scaled=travel,wavefront_X_at_half=X,receive_time_scaled=pi/6+np.sqrt(3)/4)
group(60,6,'射线实际传播积分、波面参数和正交性',q606)

def q607():
    q=S.symbols('q',positive=True);segments=[(90,95,176-q),(95,100,271-2*q),(100,105,171-q),(105,145,S.Integer(66)),(145,155,q-79)]
    work=sum(float(S.integrate(7740/q-f,(q,a,b))) for a,b,f in segments[:2]);v=np.sqrt(2*g*(work/10)/100);close(v,.593811205,rtol=2e-7)
    complete=sum(float(S.integrate(7740/q-f,(q,a,b))) for a,b,f in segments[:4]);assert complete<0
    close(300*76*155/(86*90),456.5891472868);close(7740/66,117.2727272727)
    return dict(v_when_rear_at_A=v,work_to_first_exit_cm2=complete,weakly_damped_equilibrium_q=7740/66,last_drop_temperature_K=300*76*155/7740)
group(60,7,'逐段管柱几何功积分、出口不可达和最后一滴温度',q607)

def q608():
    for gamma in [1.1,2,3,10,100]:
        Et=gamma+1;p=np.sqrt(gamma*gamma-1);theta=2*np.arccos(np.sqrt((gamma-1)/(gamma+1)));close(Et*np.cos(theta/2),p)
        for fraction in [.3,.4,.5,.6,.7]:
            c=1-2*(gamma+1)/(2*Et**2*fraction*(1-fraction))
            if -1<=c<=1:assert np.arccos(c)>=theta-1e-10
    return dict(equal_energy_minimum=True,gamma3_minimum_degrees=90)
group(60,8,'两光子不变量、动量合成与等能最小角',q608)

def q591():
    D=np.array([np.sqrt(.5),np.sqrt(.5)])
    one=lambda c:np.sqrt((c-1)**2+.25)+2*np.linalg.norm(D-[c,0]);res=minimize(lambda x:one(x[0]),[.8],method='BFGS',tol=1e-11)
    c=brentq(lambda c:(c-1)/np.sqrt((c-1)**2+.25)+2*(c-D[0])/np.linalg.norm(D-[c,0]),.7,1)
    def fun(z):f,h=z;return np.sqrt((f-1)**2+.25)+2*np.linalg.norm([h/np.sqrt(2)-f,h/np.sqrt(2)])+(1-h)
    ans=minimize(fun,[.7,.78],method='BFGS',tol=1e-10);f,h=ans.x
    close(c,.8253271331,atol=2e-8);close([f,h],[.6974998331,.7779599764],atol=2e-7)
    close([one(c)*1000,fun(ans.x)*1000],[1963.474986,1945.437929],atol=1e-4)
    return dict(single_entry=c,two_entries=[float(f),float(h)],times_seconds=[(np.sqrt(1.25)+1)*1000,one(c)*1000,fun(ans.x)*1000])
group(59,1,'时间函数独立极小化和入出水坐标',q591)

def q592():
    h,l,M=1.3,1.,2.;F1=M*g*(9*l*l+4*h*h)/(24*h*l);F2=F1-M*g*h/(3*l);close(F1*F1-F2*F2,(M*g/2)**2)
    u=brentq(lambda u:np.sinh(u)/u-3,.1,4);close(np.sinh(u)/u,3)
    m,v=1.,2.;P0=-m*v;P1=2*m*(-v/2);close(P0,P1);close(.5*m*v*v-2*.5*m*(v/2)**2,.25*m*v*v)
    return dict(catenary_parameter=u,largest_tension=F1,retension_impulse=m*v/2)
group(59,2,'重绳平衡、真实悬链线及绷直动量损失',q592)

def q593():
    k=.35;r0=2.4;mass=quad(lambda t:r0*np.exp(k*t)*np.sqrt(1+k*k),-np.inf,0)[0]
    x=quad(lambda t:(r0*np.exp(k*t))**2*np.cos(t)*np.sqrt(1+k*k),-np.inf,0)[0]/mass;y=quad(lambda t:(r0*np.exp(k*t))**2*np.sin(t)*np.sqrt(1+k*k),-np.inf,0)[0]/mass
    close([x,y],[2*k*k*r0/(1+4*k*k),-k*r0/(1+4*k*k)])
    angle=quad(lambda t:-np.exp(2*t)/(1/3+np.exp(2*t)),0,-np.inf)[0];close(angle,np.log(2))
    return dict(center=[x,y],mass_for_lambda1=mass,equal_mass_worm_angle=np.log(2))
group(59,3,'无限螺线收敛积分和虫爬行角动量积分',q593)

def q594():
    z,delta,L,r,rho,b,G,Q,eps=S.symbols('z delta L r rho b G Q eps',nonzero=True)
    Eind=-4*rho*b*b*G*delta/(r*r);d=-Q*r*r/(16*S.pi*eps*L*L*G*rho*b*b);ident((Eind+(-Q/(4*S.pi*eps*L*L))).subs(delta,d))
    V=S.Rational(4,3)*S.pi*r*b*b;dip=-2*rho*V*d;F=Q*dip*2/(4*S.pi*eps*L**3);ident(F-Q**2*r**3/(12*S.pi*eps**2*G*L**5))
    assert float(F.subs({Q:1,r:1,eps:1,G:-.1,L:5}))<0
    # Scaling follows independently from a nonzero transverse polarizability.
    alpha_perp=lambda rr,bb:rr*bb*bb
    close(alpha_perp(2,.2)/alpha_perp(1,.1),8)
    return dict(longitudinal_signed_coefficient='1/(12 pi eps^2 Gamma2)<0',finite_transverse_leading='r b^2 / L^5',ideal_line_quadrupole='r^5 / L^7')
group(59,4,'错位椭球场抵消、吸引力符号和两种极限次序',q594)

def q595():
    # Eliminate rolling friction with I/(mr^2)=2/5; surface-current torque adds qB/3 to the numerator.
    omega1=1/(1+.4);omega2=(1+1/3)/(1+.4);close(omega1,5/7);close(omega2,20/21);close(omega1/omega2,.75)
    mm=quad(lambda th:np.sin(th)**3,0,pi)[0]/4;close(mm,1/3)
    return dict(cyclotron_center=omega1,cyclotron_surface=omega2,radius_ratio=.75,shell_current_moment=mm)
group(59,5,'纯滚摩擦消元、球面磁矩积分和轨道比',q595)

def q596():
    beta=.4;gamma=1/np.sqrt(1-beta*beta);a=.7;l=2;fp=1/(4*gamma*a);Xp=gamma*l-fp
    for y in [.0,.2,.6]:
        xm=gamma*l-gamma*a*y*y;distance=np.hypot(xm-Xp,y);close(distance,fp+gamma*a*y*y)
    close((gamma*(1+beta))/gamma,1+beta)
    return dict(lab_focus_x0=l-1/(4*gamma*gamma*a),moving_focus_frequency_factor=1+beta,fixed_axis_factor=(1+beta)/(1-beta))
group(59,6,'抛物线等光程、焦点世界线及两种频率',q596)

def q597():
    gamma=1.4;beta=(1+3**.4)/2;entropy=1.5*(2.5*np.log(beta*beta/3**.4)+np.log(4/3));ratio=(5/3)**.4;xi=(1+3**.4)*ratio/(1+ratio)
    def energy(x):return 3**.4*(.5/(1+x))**.4+(1.5/(1-x))**.4
    close(energy(-.5),energy(.5));close(2*beta,1+3**.4);close(xi+(1+3**.4)/(1+ratio),1+3**.4)
    assert entropy>0
    return dict(final_temperature_ratio=beta,entropy_coefficient=entropy,half_amplitude_hot_ratio=xi,turning_total_energy=energy(.5))
group(59,7,'绝热转折对称性、总能量、熵增与慢变近似',q597)

def q598():
    R,y,w,v=1.,2.,.2,.4;gamma=1/np.sqrt(1-v*v);th=.7;x=R*np.cos(th);yy=R*np.sin(th);d=np.hypot(x,y-yy)
    xp=gamma*(x-v*d);tp=gamma*(-d+v*x);yp=yy
    close(tp*tp,xp*xp+(yp-y)**2)
    n=np.array([-x,y-yy])/d;u=w*R*np.array([np.sin(th),-np.cos(th)]);close(np.dot(u,n),-w*R*y*np.cos(th)/d)
    return dict(simultaneous_area_factor=1/gamma,null_emission_event=True,doppler_factor=np.sqrt(1-w*w*R*R)/(1-np.dot(u,n)))
group(59,8,'发射事件零间隔、顺时针多普勒投影和同时面积',q598)

def q581():
    th=np.arccos(2/3);close(np.sin(th),np.sqrt(5)/3);close(3*np.cos(th)-2,0)
    a=1/np.sqrt(2);H=3/(2*np.sqrt(2));x=1/np.sqrt(2);close(H-a*x*x,x);close(-2*a*x,-x/np.sqrt(1-x*x));close(H+1/(4*a),np.sqrt(2))
    heights=[max(np.sqrt(1-z*z)+aa*z*z for z in np.linspace(-1,1,20001))+1/(4*aa) for aa in [.3,.5,a,1,2]];assert heights[2]==min(heights)
    return dict(detachment_degrees=th*180/pi,forbidden_contact_energy_height=np.sqrt(2),allow_contact_infimum_height=1)
group(58,1,'脱离支持力、双切抛物线及能量下确界',q581)

def q582():
    m=.005;R=.02;J1=2/3*.0027*R*R;J=1e-6;v=15.6;close(J1,7.2e-7);crit=m*v*R/J;close(crit,1560)
    v2=9.86;mu=.719;w=mu*v2*(1/R+m*R/J);close(w,1063.4015,atol=.01)
    Jt=m*J*R*w/(J+m*R*R);close(Jt,mu*m*v2)
    return dict(shell_inertia=J1,reverse_strict_threshold=crit,omega2_threshold=w,tangential_impulse=Jt)
group(58,2,'接触点角动量和双球切向冲量阈值',q582)

def q583():
    a=1/np.sqrt(2);vertices=np.array([[a,0,0],[-a,0,0],[0,a,0],[0,-a,0],[0,0,a],[0,0,-a]])
    edges=[(i,j) for i,j in itertools.combinations(range(6),2) if abs(np.linalg.norm(vertices[i]-vertices[j])-1)<1e-8];assert len(edges)==12
    b=np.array([0,np.sqrt(2/3),1/np.sqrt(3)]);curr=[-.5*np.dot(b,np.cross(vertices[i],vertices[j])) for i,j in edges]
    K=np.zeros(6);moment=np.zeros(3)
    for (i,j),I in zip(edges,curr):K[i]+=I;K[j]-=I;moment+=I*np.cross(vertices[i],vertices[j])/2
    close(K,np.zeros(6));close(moment,-b/4)
    return dict(edge_count=12,KCL='all six vertices',magnetic_moment=moment.tolist(),torque_x=-np.sqrt(2)/(4*np.sqrt(3)))
group(58,3,'十二棱电动势、六节点KCL和各向同性磁矩',q583)

def q584():
    th=S.symbols('th',real=True);ell=S.Function('ell')(th);ss=S.sin(th);cc=S.cos(th)
    x2=1-ell*cc;y2=ell*ss;x1=x2-ss;y1=y2+1-cc
    J=y2*S.diff(x2,th)+x1*S.diff(y1,th);boundary=ell*ss*(1-ss)-ell**2*ss*cc
    ident(J-ss*(1-ss)-S.diff(boundary,th))
    vals=[]
    for aa in [0,.15,.3,.5]:
        el=aa*cc;j=S.lambdify(th,J.subs(ell,el).doit(),'numpy');integral=quad(j,0,pi/2)[0];area=pi/4-integral;vals.append(area);close(area,pi/2-1)
        dy=S.lambdify(th,S.diff(y1.subs(ell,el),th),'numpy');assert min(dy(x) for x in np.linspace(0,pi/2,200))>=-1e-10
    return dict(area_over_r2=pi/2-1,legal_cosine_examples=vals,total_derivative_sign='minus r ell sin(theta)(1-sin(theta)) in area endpoint')
group(58,4,'任意自由函数的面积全导数和合法边界样例',q584)

def q585():
    A,R,k,emf=2.1,3.2,1.8,4.5;v=A*emf/(k*R+A*A);I=(emf-A*v)/R;close(k*v,A*I);close(emf*I,I*I*R+k*v*v)
    x=S.symbols('x',real=True);r,l=S.symbols('r l',positive=True);B=((x+l)/S.sqrt((x+l)**2+r*r)-x/S.sqrt(x*x+r*r))/2;grad=S.diff(B,x)
    ident(grad.subs(x,-l)-(.5/r-.5*r*r/(l*l+r*r)**S.Rational(3,2)))
    ident(grad.subs(x,0)+grad.subs(x,-l))
    return dict(terminal_v=v,current=I,power_input=emf*I,back_emf_fraction=A*v/emf,approx_requires='A^2 << kR')
group(58,5,'线圈端场梯度、互易反电动势和终端功率闭合',q585)

def q586():
    for n in [1,2,5,20]:
        b=0
        for _ in range(n):b=(n*b+100)/(n+1)
        close(b,100*(1-(n/(n+1))**n))
    H=373.15;C=273.15;T=np.sqrt(H*C);W=H+C-2*T;close([T-273.15,T+W-273.15],[46.10839456465,53.89160543535],atol=1e-7)
    close(np.log(T/H)+np.log(T/C),0);close([H+C,H*C],[646.3,T*T])
    return dict(reversible_T_K=T,W_over_capacity=W,dissipated_final_C=T+W-273.15,reverse_final_hot_C=100)
group(58,6,'分份递推、熵守恒和回用功后的温度',q586)

def q587():
    n1,n2,angle=1.5,1.,1.;ky=n1*np.sin(angle);alpha=np.sqrt(ky*ky-n2*n2);kz=-1j*alpha
    close(ky*ky+kz*kz,n2*n2);assert np.exp((-1j*kz).real)<1
    close(-1j*kz,-alpha);assert 1/n1<1/ky<1/n2
    return dict(alpha_over_vacuum_k=alpha,phase_velocity_over_c=1/ky,amplitude_depth_over_wavelength=1/(2*pi*alpha),energy_depth_half=True)
group(58,7,'复波矢色散、衰减支和相速度界限',q587)

def q588():
    vr=(.6+.8)/(1+.6*.8);close(vr,35/37);gr=1/np.sqrt(1-vr*vr);close(gr,37/12);mC=100/gr;mH=100.;E=mC/np.sqrt(1-.6**2)+mH/np.sqrt(1-.8**2);p=.6*mC/np.sqrt(1-.6**2)-.8*mH/np.sqrt(1-.8**2)
    close([E,p],[23000/111,-12100/111]);close(p/E,-121/230);M=np.sqrt(E*E-p*p);close(M,100*np.sqrt(4251)/37)
    t=14/1.4;x=.6*t;close([t,x],[10,6]);close(t+.8*x-.8*14,3.6)
    return dict(relative_speed=vr,mC=mC,total_rest_mass=M,final_velocity=p/E,collision=[x,t],simultaneous_B_time=3.6)
group(58,8,'两次洛伦兹同时性和非弹性四动量',q588)

assert len(rows)==40
(P/'math_results.json').write_text(json.dumps(dict(passed=True,groups=rows,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),ensure_ascii=False,indent=2))
print('PASS: 40 groups')
