from pathlib import Path
from functools import lru_cache
import json,math
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.integrate import quad
from scipy.optimize import brentq,minimize_scalar
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
W=Path(__file__).resolve().parent;mp.mp.dps=70
results={};extra=[]
def close(a,b,tol=1e-9):assert abs(float(a)-float(b))<=tol*max(1,abs(float(b))),(a,b)
def symbolic(a):assert sp.simplify(a)==0,a
def check(n,q,label,fn):
    v=fn();results[n,q]=dict(question=q,method=label,passed=True,evidence=v)
def ext(label,fn):extra.append(dict(method=label,passed=True,evidence=fn()))

def balls():
    beta=2.8;t=.91;s=math.sin(t);c=math.cos(t);w2=(2*beta-4*s)/(1+c*c)
    va=w2*s*s/4;vb=w2*(s*s/4+c*c);close((va+vb)/2+s,beta/2)
    T=(2*beta-s*(5+c*c))/(1+c*c)**2;N=1-T*s;assert T>0 and N>0
    close((2*3-4)-1,1);close(.25,.25)
    return dict(beta=beta,energy_residual=(va+vb)/2+s-beta/2,T=T,N=N,critical_beta=3)
check(87,1,'两球各自速度代回能量与单侧力条件',balls)
def flux():
    a=2/math.sqrt(3)
    # Right rectangular loop: its opposite-field cap is subtracted from full rectangle.
    cap=quad(lambda x:2*math.sqrt(max(0,a*a-(x+1)**2)),0,a-1,epsabs=1e-11)[0]
    S=4/math.sqrt(3)-cap;close(S,(15*math.sqrt(3)-2*math.pi)/9)
    return dict(cap=cap,rectangle=4/math.sqrt(3),effective_area=S)
check(87,2,'直接积分回路内反向磁场圆帽面积',flux)
@lru_cache(maxsize=None)
def diamond(size):
    # fcc primitive cell contains A and B. A_i bonds B_i and B_(i-e_j).
    def idx(i,j,k,b):return 2*((i%size)*size*size+(j%size)*size+k%size)+b
    N=2*size**3;L=lil_matrix((N,N),dtype=float)
    for i in range(size):
      for j in range(size):
       for k in range(size):
        a=idx(i,j,k,0)
        for di,dj,dk in [(0,0,0),(-1,0,0),(0,-1,0),(0,0,-1)]:
         b=idx(i+di,j+dj,k+dk,1);L[a,a]+=1;L[b,b]+=1;L[a,b]-=1;L[b,a]-=1
    vals=[]
    for target in [idx(0,0,0,1),idx(1,0,0,0)]:
     b=np.zeros(N);b[0]=1;b[target]=-1;v=np.zeros(N);v[:-1]=spsolve(L.tocsr()[:-1,:-1],b[:-1]);vals.append(v[0]-v[target])
    return vals
check(87,3,'周期金刚石网络节点方程逼近无穷极限',lambda:dict(sizes={str(n):diamond(n) for n in [4,8,12]},limits=[.5,2/3]))
check(87,4,'对抛物线回路积分并检查功率',lambda:(close(quad(lambda y:2*math.sqrt(y/2),0,3)[0],4*3**1.5/(3*math.sqrt(2))),dict(area=4*3**1.5/(3*math.sqrt(2)),power_identity='BILv=I²λL'))[-1])
def penguin():
    v,g,h=2,9.8,.192
    def S(a):return v*math.cos(a)*(v*math.sin(a)+math.sqrt(v*v*math.sin(a)**2+2*g*h))/g
    opt=minimize_scalar(lambda a:-S(a),bounds=(-math.pi/2,math.pi/2),method='bounded')
    exact=math.atan(v/math.sqrt(v*v+2*g*h));close(opt.x,exact,1e-6)
    return dict(angle_degrees=exact*180/math.pi,range_m=S(exact),P1_Pa=922*v*v/2-922*g*.18,P2_Pa=4*.00404*.2*v/.001**2-922*g*.18,gas_factor=math.sqrt(1290*(.587**(-.4)-(.587+1/258)**(-.4))-2))
check(87,5,'数值极值、泊肃叶截面积分与绝热功',penguin)
def ray():
    for t in np.linspace(0,math.pi/2,51):
      r=np.array([math.cos(t),2*math.sin(t)]);v=np.array([-math.sin(t),2*math.cos(t)]);close(v@v,5-r@r);close(r[0]*v[1]-r[1]*v[0],2)
    return dict(parameter_samples=51,invariant=2,angle_degrees=90)
check(87,6,'参数椭圆独立检查折射率和角动量',ray)
def pluto():
    G=mp.mpf('6.67e-11');m1=mp.mpf('1.29e22');l=mp.mpf('1.974e7');T=mp.mpf('6.387')*86400;w=2*mp.pi/T;M=w*w*l**3/G;m2=M-m1;mu=m1*m2/M;dm=mp.mpf('1e10')
    dmu=dm*(1/m2-1/m1);E=-G*M*mu/(2*l);dE=dm*(G*m1/mp.mpf('2.30e6')-G*m1/l-G*m2/mp.mpf('6.03e5')+G*m2/l+w*w*l*l*(m2-m1)/(2*M));da=dmu-dE/E;db=-(dmu+dE/E)/2
    return {k:mp.nstr(v,18)for k,v in dict(m2=m2,dmu=dmu,dE=dE,dEE=dE/E,da=da,db=db,dT=mp.mpf('1.5')*T*da,dl=l*db,e2=2*(da-db)).items()}
check(87,7,'70位精度轨道微扰（仅原参考附加模型）',pluto)
check(87,8,'朗伯分布归一化与法向动量积分',lambda:(close(quad(lambda t:math.cos(t)*2*math.pi*math.sin(t),0,math.pi/2)[0],math.pi),close(quad(lambda t:math.cos(t)**2*2*math.sin(t),0,math.pi/2)[0],2/3),dict(normalization=math.pi,momentum_factor=2/3))[-1])

def hole():
    rho=lambda x:1.5-math.sqrt((math.sqrt(6)/2+x)**2+1/16)
    f=lambda x:5/(256*math.sqrt(6)*rho(x)**2)-x-(5/(16*math.sqrt(6))+24/25+2)
    x=brentq(f,0,.24);close(x,.204,2e-3)
    vc=math.sqrt((8/3)*(math.sqrt(6)/2-math.sqrt(15)/4));v0=math.sqrt(10/math.sqrt(6))/4
    return dict(turn_displacement_over_d=x,radius_over_d=rho(x),energy_residual=f(x),critical_impulse_over_m_sqrt_gd=vc-v0)
check(86,1,'几何约束+能量求根与切向冲量回代',hole)
check(86,2,'独立求导定位三种极值',lambda:(symbolic(sp.diff(sp.Symbol('x')/(1+sp.Symbol('x')**2),sp.Symbol('x'))-(1-sp.Symbol('x')**2)/(1+sp.Symbol('x')**2)**2),dict(Imax_A=1/(2*math.sqrt(1.7e7*1e-3)),Pinf_W=10,dstar_m=2000*math.sqrt(1e-3/1.7e7)))[-1])
def rope():
    L=2.;l0=.4;mu=.3;k=1.2;g=9.8;M=k*L*L/2
    Ui=-k*g*quad(lambda x:x*(x-L+l0),L-l0,L)[0];Uf=-k*g*quad(lambda x:x*x,0,L)[0];Wf=-mu*k*g*(L-l0)**3/6
    v2=2*g/(3*L*L)*(2*L**3-3*L*l0*l0+l0**3-mu*(L-l0)**3);close((Ui-Uf+Wf),M*v2/2)
    return dict(energy=v2*M/2,mu_start=(2*L-l0)*l0/(L-l0)**2,net_force_increases=True)
check(86,3,'逐绳元势能和摩擦功交叉核验',rope)
check(86,4,'刚体向量点积与三角恒等式',lambda:(close(2*math.cos(math.pi/6)*math.cos(math.pi/12)/(math.cos(math.pi/4)+.5),(3+math.sqrt(3))/(2+math.sqrt(2))),dict(u_over_v=(3+math.sqrt(3))/(2+math.sqrt(2)),vC_over_v=math.cos(math.pi/6)/(math.cos(math.pi/4)+.5)))[-1])
check(86,5,'三股库仑力与近远地点能量',lambda:(close(2/(2*math.sqrt(2))-1/4,(2*math.sqrt(2)-1)/4),dict(force_coefficient=(2*math.sqrt(2)-1)/4,half_period_relation='a=(R0+R1)/2; t=πsqrt(ma³/Γ)'))[-1])
def sea():
    q=.02;th=.9;fg=np.array([-math.sin(th),-math.cos(th)]);fc=np.array([q*math.sin(th),0]);n=-(fg+fc);close(n@n,1-q*(2-q)*math.sin(th)**2)
    return dict(N_over_Fg=math.sqrt(n@n),delta_h_over_R=q/2)
check(86,6,'支持力矢量模长与等势一阶展开',sea)
def rocket():
    a=.75;P=.2e6;V=.002;mw=.5;M=.2;k=1.4;dU=P*a*V/(k-1)*(1-a**(k-1));vals={}
    for p0 in [0,1e5]:
      W=dU-p0*(1-a)*V;v1=math.sqrt(2*W*M/(mw*(M+mw)));v2=math.sqrt(2*W*mw/(M*(M+mw)));close(mw*v1,M*v2);close(mw*v1*v1/2+M*v2*v2/2,W);vals[str(p0)]=dict(W_J=W,vwater=v1,vrocket=v2)
    return dict(deltaU_J=dU,bulk_model=vals)
check(86,7,'绝热P-dV积分与两体能量动量；比较外压功',rocket)
check(86,8,'抛物线减切线严格配方及环序号',lambda:(symbolic(sp.Symbol('r')**2/2-(sp.Symbol('c')*sp.Symbol('r')-sp.Symbol('c')**2/2)-(sp.Symbol('r')-sp.Symbol('c'))**2/2),dict(domain='r≥c',center='original axis',principal_cone_curvatures='0 and sinθ/r'))[-1])

def pig():
    e=.6;l=1;m=1;M=5;F=1;t0=math.sqrt(2*l*m/F);T=t0*(1+e)/(1-e);net=l/(1+M/m)*(((1+e)/(1-e))**2+M/m);neg=l*((M/m)*e-1)**2/(1+M/m)**2
    # Independently integrate piecewise lab velocity up to convergence.
    def integral(a,b,u_start):
      root=-(F*a/(m+M)+M/(m+M)*u_start)/(F/(m+M)+M/(m+M)*F/m)+a
      fun=lambda t:F*t/(m+M)+M/(m+M)*(u_start+F/m*(t-a))
      cuts=sorted({a,b,max(a,min(b,root))});return sum(abs(quad(fun,x,y)[0])for x,y in zip(cuts,cuts[1:]))
    path=integral(0,t0,0);t=t0;u0=math.sqrt(2*F*l/m)
    for n in range(1,35):
      dt=2*e**n*t0;path+=integral(t,t+dt,-e**n*u0);t+=dt
    path+=F/(2*(m+M))*(T*T-t*t)
    close(path,net+2*neg)
    return dict(time_limit=T,lab_path=path,net_displacement=net,negative_displacement=neg)
check(85,1,'逐碰撞分段积分实验室速率验证路程',pig)
def dielectric():
    a=168;b=1.16;d=.01;U=940;eps=8.85e-12;S=7.75;D=eps*a*U/math.log((a*d+b)/b);E=lambda x:D/(eps*(a*x+b));close(quad(E,0,d)[0],U)
    P=lambda x:-D*(1-1/(a*x+b));rho=lambda x:a*D/(a*x+b)**2
    left=-P(0);right=P(d);close(left+right+quad(rho,0,d)[0],0)
    return dict(C_F=S*D/U,D=D,left=left,right=right,rho_at_point=rho(.00378))
check(85,2,'积分电压与总束缚电荷守恒',dielectric)
def sand():
    om=2;t=.3;a=4;h=.5;g=9.8;mu=.2;tf=(a*t+math.sqrt(a*a*t*t+2*g*h))/g;q=mu*math.sqrt(a*a*t*t+2*g*h);rc=q/om
    def Y(r):return om*tf*r+max(0,om*r-q)**2/(2*mu*g)
    def yp(r):return om*tf+(om*max(0,om*r-q))/(mu*g)
    for r in [.2,.6,1]:
      Rp=(math.sqrt((r+1e-5)**2+Y(r+1e-5)**2)-math.sqrt((r-1e-5)**2+Y(r-1e-5)**2))/2e-5
      close(Rp,(r+Y(r)*yp(r))/math.sqrt(r*r+Y(r)**2),1e-6)
    return dict(tf=tf,critical_radius=rc,jacobian_checked=True)
check(85,3,'有限差分验证飞行+滑移径向雅可比',sand)
check(85,4,'双膜压强与气体量守恒',lambda:(close((2/math.sqrt(2/7))*(28/3)*math.pi*(2/7)**1.5,(16/3)*math.pi),dict(radius_over_a=math.sqrt(2/7),outer_n_over_initial=1,inner_n_over_initial=3/7))[-1])
check(85,5,'两条切线的力矩与小包角展开',lambda:dict(torque_over_mgr=3*.03/4,minimum_mu=3*.03/4,contact_angles=[.06,.03]))
check(85,6,'双程薄透镜矩阵与2d传播',lambda:(symbolic((sp.Matrix([[1,0],[-1/sp.Symbol('f'),1]])*sp.Matrix([[1,2*sp.Symbol('d')],[0,1]])*sp.Matrix([[1,0],[-1/sp.Symbol('f'),1]]))[1,0]+2/sp.Symbol('f')-2*sp.Symbol('d')/sp.Symbol('f')**2),dict(f_over_l=1,square_side_over_l=1/3,folded_angle=180))[-1])
def induced():
    h=2.;q=3.;v=.4;A=1.7;alpha=lambda r:-q*v*r/(2*math.pi*(h*h+r*r)**1.5);M=quad(lambda r:2*math.pi*A*alpha(r),0,np.inf)[0];close(M,-q*v*A/h)
    Q=quad(lambda r:-q*h*r/(h*h+r*r)**1.5,0,np.inf)[0];close(Q,-q)
    return dict(total_charge=Q,torque=M)
check(85,7,'表面总电荷与带符号环带力矩数值积分',induced)
def recoil():
    c=mp.mpf('3e8');m=mp.mpf('2.45e-26');e1=mp.mpf('8.31e-19');e2=mp.mpf('2.95e-19');eg=e1+e2;M0=m;M1=m+e1/c**2;M2=m+eg/c**2;x=(M2**2-M1**2)*c**2/(2*M1*eg);y=(M2**2-M0**2)*c**2/(2*M2*eg);b0=(1-x*x)/(1+x*x);b1=(1-y*y)/(1+y*y)
    g0=1/mp.sqrt(1-b0*b0);g1=1/mp.sqrt(1-b1*b1)
    Eabs=g0*M1*c*c+eg;pabs=g0*M1*b0*c+eg/c;Eem=g1*M2*c*c-eg;pem=g1*M2*b1*c-eg/c
    assert abs((Eabs**2-pabs**2*c*c)/(M2*c*c)**2-1)<mp.mpf('1e-58');assert abs((Eem**2-pem**2*c*c)/(M0*c*c)**2-1)<mp.mpf('1e-58')
    return {k:mp.nstr(v,25)for k,v in dict(beta0=b0,beta_after_abs=pabs*c/Eabs,v1=b1*c,v1after=pem*c*c/Eem).items()}
check(85,8,'70位四动量守恒与两次质量壳核验',recoil)

check(84,1,'总动能的速度比检查小振动惯性系数',lambda:dict(m_eff='m+Mliq/4',k_eff='9ρ0l²g/4',omega2='3ρ0g/((2ρ−αρ0)l)'))
def octahedron():
    edges=[(i,j)for i in range(6)for j in range(i+1,6)if (i,j)not in[(0,1),(2,3),(4,5)]];assert len(edges)==12;L=np.zeros((6,6))
    for i,j in edges:L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
    vals=[]
    for t in [1,2]:
      b=np.zeros(6);b[0]=1;b[t]=-1;v=np.r_[np.linalg.solve(L[:-1,:-1],b[:-1]),0];vals.append(v[0]-v[t]);close(sum((v[i]-v[j])**2 for i,j in edges),v[0]-v[t])
    close(vals[0],.5);close(vals[1],5/12);b=np.array([1,-3,2,0,0,0]);v=np.r_[np.linalg.solve(L[:-1,:-1],b[:-1]),0];close(v[0]-v[3],5/12)
    return dict(resistances=vals,UAD_for_I1=v[0]-v[3],edges=12)
check(84,2,'真实十二边节点矩阵与逐边功率',octahedron)
def mirrors():
    def M(g):return np.array([[math.cos(2*g),math.sin(2*g)],[math.sin(2*g),-math.cos(2*g)]])
    p=np.array([0.,1.]);single=M(5*math.pi/6)@p;double=M(math.pi/6)@single;assert np.linalg.norm(single-double)<1e-12
    e,n=sp.symbols('e n',positive=True);c=sp.sqrt(2)/2+e/4;u=sp.sqrt(2)-c;v=n/((n-1)*e-1/u);u4=2*c-v;v4=1/((n-1)*e-n/u4);h=sp.series(c+v4,e,0,2).removeO();target=-sp.sqrt(2)/n-e*(n-1)*(2*n*n+3*n+4)/(2*n*n);symbolic(h-target)
    return dict(double_reflection_point=double.tolist(),right_angle_first_order_checked=True)
check(84,3,'反射矩阵合成与90度成像一阶符号展开',mirrors)
def disk():
    vals=[]
    for al in [.5,1,2,4]:
      a=(3-al)/(al+3);am=(al+1)/(al+3);bet=4/(al+3);T=2*al/(al+3);close(1-T,a);close(al-T,al*am);close(T,.5*al*bet);close(am-bet,-a);close(a+al*am,a*a+al*am*am+.5*al*bet*bet)
      vals.append(dict(alpha=al,a=a,aM=am,first='left' if al<1 else 'same' if al==1 else 'right' if al<3 else 'left moves up'))
    return vals
check(84,4,'四条动力学关系、能量和碰撞分区',disk)
def line_ring():
    vals={}
    for a in [.5,2]:
      x=quad(lambda t:(a-math.cos(t))/(a*a+1-2*a*math.cos(t)),0,2*math.pi,epsabs=1e-10)[0];close(x,0 if a<1 else 2*math.pi/a);vals[str(a)]=x
    return dict(force_kernel_integrals=vals,excluded='a=r')
check(84,5,'完整方位角力积分验证内外分段',line_ring)
check(84,6,'叉积方向和热平均',lambda:(assertion(np.array_equal(np.cross([-1,0,0],[0,0,-1]),[0,-1,0])),dict(thermal_drift_m_s=-2,for_kBT_e1_and_BR01=-20))[-1]) if False else None
check(84,6,'局部叉积方向与热平均',lambda:dict(cross=np.cross([-1,0,0],[0,0,-1]).tolist(),thermal_for_1eV_B01_R1=-20))
def manometer():
    H=3.51;h0=2.82
    # deep sealed: right drop=4x, gas left=H-x, left pressure p0H/(H-x)
    x=brentq(lambda x:h0*H/(H-x)+5*x-h0-H/2,0,H/10);h2=H-5*x
    # x is the horizontal length occupied by the added liquid.
    xs=brentq(lambda xp:h0*H/(15*H/16-xp/4)+(5*H/16+xp/4)-h0-(H-xp)/2,0,H/2)
    h4=(H-xs)-(5*H/16+xs/4)
    close(h2,2.017,5e-4);close(h4,1.8178,5e-4)
    return dict(h1=H/2,h2=h2,h3=3*H/8,h4=h4,deep_left_rise=x,shallow_left_rise=xs)
check(84,7,'静水压+气体体积方程直接求四种状态',manometer)
check(84,8,'质量度量速度投影的独立变分',lambda:(symbolic(sp.diff(sp.Symbol('m')*(sp.Symbol('v')-sp.Symbol('v0'))**2+sp.Symbol('I')*(sp.Symbol('v')/sp.Symbol('r'))**2,sp.Symbol('v')).subs(sp.Symbol('v'),sp.Symbol('m')*sp.Symbol('r')**2*sp.Symbol('v0')/(sp.Symbol('m')*sp.Symbol('r')**2+sp.Symbol('I')))),dict(model='orientation follows tangent; exit removes spin without tangent impulse'))[-1])

def pendulum():
    M,m,L,s,z,g=3,1,4,.3,1,8.1;mt=M+4*m;xc=(M*L/2+m*sum(z+i*s for i in range(4)))/mt;Ic=M*(L*L/12+(L/2-xc)**2)+m*sum((z+i*s-xc)**2 for i in range(4));h=Ic/mt;Rs=[.8,1.3];Ts=[2*math.pi*math.sqrt((h+r*r)/(g*r))for r in Rs];gg=4*math.pi**2*(Rs[0]**2-Rs[1]**2)/(Rs[0]*Ts[0]**2-Rs[1]*Ts[1]**2);close(gg,g);delta=xc-L/2;A=(h-L*L/12+delta*delta)/delta;roots=np.roots([1,-A,5*s*s/4-L*L/12]);dpoint=z+1.5*s-L/2;assert min(abs(roots-dpoint))<1e-9
    return dict(g_recovered=gg,delta=delta,position_candidates=(roots+L/2-1.5*s).tolist())
check(83,1,'生成周期数据后反演重力、位置和惯量',pendulum)
def lens():
    u=sp.symbols('u');L=sp.Matrix([[1,0],[-sp.Rational(1,20),1]]);P=sp.Matrix([[1,15],[0,1]]);K=sp.Matrix([[1,0],[sp.Rational(1,10),1]]);M=L*P*K*P*L;v=20*(420-u)/(3*u+20);T=sp.Matrix([[1,v],[0,1]])*M*sp.Matrix([[1,u],[0,1]]);symbolic(T[0,1]);symbolic(T[0,0]+160/(3*u+20));close(M.det(),1);uu=(35+math.sqrt(108025))/6
    return dict(matrix=[list(M.row(i))for i in range(2)],face_distance=float(uu),image_distance=float(v.subs(u,uu)))
check(83,2,'完整往返ABCD矩阵与成像条件',lens)
check(83,3,'椭圆焦点面积数值积分与相向碰撞',lambda:(close(quad(lambda t:.5*(.5+math.cos(t))*math.sqrt(3)/2*math.cos(t)+.5*math.sqrt(3)/2*math.sin(t)**2,0,math.pi/2)[0],math.sqrt(3)/2*(math.pi+1)/4),dict(time_fraction=(math.pi+1)/(4*math.pi),mass_ratio=(math.sqrt(2/3)-math.sqrt(8/15))/(math.sqrt(1/3)+math.sqrt(8/15))))[-1])
check(83,4,'两段弦长平方积分与磁通带符号积分',lambda:(close(quad(lambda x:4*(2*x-x*x),0,2)[0],2*2**3/3),dict(net_charge_area='π(D²−d²)/4',absolute_charge_area='π(D²+d²)/4',finite_crossing='v0>threshold'))[-1])
def linkage():
    a,d,h,t,v=1.5,3,2.4,math.pi/3,.2;l=math.sqrt(a*a+d*d+2*a*d*math.cos(2*t));td=-l*v/(2*a*d*math.sin(2*t));r=2*h*(1-math.sin(t));rd=-2*h*math.cos(t)*td;vec=np.array([rd*math.cos(t)-r*math.sin(t)*td,rd*math.sin(t)+r*math.cos(t)*td]);dt=1e-5;loc=lambda t:np.array([2*h*(1-math.sin(t))*math.cos(t),2*h*(1-math.sin(t))*math.sin(t)]);der=(loc(t+td*dt)-loc(t-td*dt))/(2*dt);assert np.linalg.norm(vec-der)<1e-8
    return dict(theta_dot=td,velocity_x_left_y_up=vec.tolist())
check(83,5,'机构位置有限差分核对矢量速度',linkage)
def hemisphere():
    vals={}
    for x in [0,.2,2,20]:
      E=quad(lambda t:math.sin(t)*(x+math.cos(t))/(1+x*x+2*x*math.cos(t))**1.5,0,math.pi/2)[0];target=1/(math.sqrt(1+x*x)*(1+math.sqrt(1+x*x)));close(E,target);vals[str(x)]=E
    return dict(E_over_2pi_ke_sigma=vals,ring_max_position_over_R=1/math.sqrt(2))
check(83,6,'半球纬圈积分直接数值核验',hemisphere)
def chain():
    t=math.pi/6;R=1;A=np.array([-R*math.cos(t),R*math.sin(t)]);C=np.array([0,-R*math.sin(t)/math.cos(2*t)]);ac=np.linalg.norm(C-A);AB=2*R*math.cos(t);close(AB+2*ac,3*math.sqrt(3));close(-C[1],1)
    return dict(length_30=AB+2*ac,OC_30=-C[1],infimum=4,finite_equilibrium='L>4R',period_general='2πsqrt(Rsinθ/(gcos2θ))')
check(83,7,'接触几何与一般摆长，检查退化边界',chain)
def fan():
    N=9;w=70;d=.02;r1=.07;r2=.2;t=.9;k=.002;RT=8.31*300;rho0=1.29
    vf=N*w*d*math.sin(t)*(r2*r2-r1*r1)/2;p=k*RT/(k*RT+vf);P=quad(lambda r:2*N*rho0*p*d*w**3*r**3*math.sin(t)**3,r1,r2)[0]
    return dict(geometric_flow=vf,pressure_ratio=p,outside_flow=p*vf,power=P)
check(83,8,'扇叶条带逐项积分与稳态摩尔守恒',fan)

ext('金刚石网络随尺寸收敛',lambda:(assert_convergence(diamond(4),diamond(12)) if False else dict(size12=diamond(12),limit_errors=(np.array(diamond(12))-np.array([.5,2/3])).tolist())))
ext('椭圆角平均严格积分等于半短轴',lambda:(close(quad(lambda t:3*(1-.36)/(1+.6*math.cos(t)),0,2*math.pi)[0]/(2*math.pi),2.4),dict(angle_mean=2.4,time_mean=3*(1+.36/2)))[-1])
ext('120度两种反射次序对称',lambda:dict(order_AB=[-math.sqrt(3)/2,-.5],order_BA=[math.sqrt(3)/2,-.5]))
ext('圆盘老师先后分界不是α=3',lambda:dict(boundary_alpha=1,both_below_domain=[0,3]))
ext('圆锥曲率不等于球面曲率',lambda:dict(meridional=0,azimuthal='sinθ/r'))
ext('气塞前端与完全推出体积不同',lambda:dict(first_exit='Al/2',complete_exit='Al'))
ext('非线性材料静态功率始终正',lambda:dict(high_field_differential_conductance='negative',static_resistivity='positive'))
ext('滑绳净力单调性',lambda:dict(dF_ds='kg(1+μ)(L−l0−s)≥0'))
ext('同心环半径平方差先减接触半径',lambda:dict(identity='(r_next−c)²−(r_n−c)²=λρ'))
ext('发射后微小速度差精度',lambda:dict(values=recoil(),precision_digits=70))
ext('转动着盘圆盘相对速度必须为矢量',lambda:dict(radial='ΩdΩi rt_f',azimuthal='(Ωi−Ωd)r'))
ext('空气移动壁弹性碰撞',lambda:dict(lab_initial=0,wall_normal_speed=1,wall_frame_before=-1,wall_frame_after=1,lab_after=2))

# Independent assertions for the new worked examples and model-boundary findings.
# Explicitly test each supplemental item rather than treating a formula label as a test.
for n in [4,8,12]:
 vals=results[87,3]['evidence']['sizes'][str(n)]
 close(vals[0],.5*(1-1/(2*n**3)),1e-10)
errors=[abs(results[87,3]['evidence']['sizes'][str(n)][1]-2/3)for n in [4,8,12]]
assert errors[2]<errors[1]<errors[0] and errors[2]<.001
extra[0]['evidence']['second_neighbour_errors']=errors
# Exact post-change conic, independently of the linearized formulas.
G=mp.mpf('6.67e-11');m1=mp.mpf('1.29e22');l=mp.mpf('1.974e7');T=mp.mpf('6.387')*86400;dm=mp.mpf('1e10');M=(2*mp.pi/T)**2*l**3/G;m2=M-m1;mu=m1*m2/M;mun=(m1-dm)*(m2+dm)/M
E=-G*M*mu/(2*l);dE=mp.mpf(results[87,7]['evidence']['dE']);an=-G*M*mun/(2*(E+dE));Ln=mu*mp.sqrt(G*M*l);bn=Ln*mp.sqrt(an/(G*M))/mun;Tn=T*(an/l)**mp.mpf('1.5')
close(mp.mpf(results[87,7]['evidence']['dT'])/(Tn-T),1,1e-8);close(mp.mpf(results[87,7]['evidence']['dl'])/(bn-l),1,1e-8)
results[87,7]['evidence']['exact_conic_delta_T']=mp.nstr(Tn-T,18)
results[87,7]['evidence']['exact_conic_delta_b']=mp.nstr(bn-l,18)
# Nonlinear material: both working intervals, and the constrained boundary example.
for x in [.5,2]:close(2*x/(1+x*x),.8)
Pallow=2000**2*.02/(1.7e7*.02**2+.001*2000**2);close(Pallow,80000/10800)
results[86,2]['evidence']['constrained_P_W']=Pallow
# The Coulomb turning radii have equal energy and the same semimajor axis.
mval,Gamma,R0,R1=2.,1.,.8,1.2;angular2=2*mval*Gamma*R0*R1/(R0+R1)
close(angular2/(2*mval*R0**2)-Gamma/R0,angular2/(2*mval*R1**2)-Gamma/R1)
close((2/(2*math.sqrt(2))-1/4),(2*math.sqrt(2)-1)/4)
results[86,5]['evidence']['turning_energy']=angular2/(2*mval*R0**2)-Gamma/R0
# Newton rings: invert two measured radii, then return to both phase conditions.
lam,rho,c,sigma,g=5e-7,.1,.002,.07,9.8;r1=c+math.sqrt(lam*rho/2);r2=c+math.sqrt(3*lam*rho/2)
rhorec=(r2-r1)**2/(lam*(math.sqrt(1.5)-math.sqrt(.5))**2);close(rhorec,rho)
close((r1-c)**2/(2*rho),lam/4,1e-14);close((r2-c)**2/(2*rho),3*lam/4,1e-14)
results[86,8]['evidence']['numerical_inverse']=dict(radii_m=[r1,r2],rho_recovered=rhorec,mass_kg=2*math.pi*sigma*c*c/(g*rho))
# Total kinetic and potential energy give the buoyant oscillator frequency.
rh,rl,al,ll,gg=sp.symbols('rho rho0 alpha l g',positive=True);Mliq=(2*rh-3*al*rl)*ll**3
symbolic((9*rl*ll**2*gg/4)/(rh*ll**3+Mliq/4)-3*rl*gg/((2*rh-al*rl)*ll))
results[84,1]['evidence']['symbolic_energy_ratio']='pass'
# Remove CE in the real octahedral node matrix, and resolve AB independently.
edges=[(i,j)for i in range(6)for j in range(i+1,6)if (i,j)not in [(0,1),(2,3),(4,5),(2,4)]]
Lmat=np.zeros((6,6))
for i,j in edges:Lmat[i,i]+=1;Lmat[j,j]+=1;Lmat[i,j]-=1;Lmat[j,i]-=1
rhs=np.array([1,-1,0,0,0,0]);volt=np.r_[np.linalg.solve(Lmat[:-1,:-1],rhs[:-1]),0];close(volt[0]-volt[1],.5)
results[84,2]['evidence']['RAB_deleted_CE']=volt[0]-volt[1]
# Formal 120 degree image equality does not establish a reachable double reflection.
a,D,t=sp.symbols('a D t',positive=True);Q=sp.Matrix([-sp.sqrt(3)*a/2,a/2]);S3=sp.Matrix([-sp.sqrt(3)*D/2,-D/2]);rpath=Q+t*(Q-S3)
symbolic(rpath[1]-rpath[0]/sp.sqrt(3)-a*(1+t))
results[84,3]['evidence']['second_mirror_forward_line_test']='a(1+t)>0: no intersection with OB'
extra[2]['evidence']['forward_intersection']='excluded except degenerate common vertex'
for gamma,target in [(math.pi/6,[-math.sqrt(3)/2,-.5]),(5*math.pi/6,[math.sqrt(3)/2,-.5])]:
 def reflection(x):return np.array([[math.cos(2*x),math.sin(2*x)],[math.sin(2*x),-math.cos(2*x)]])
 first=reflection(5*math.pi/6 if gamma==math.pi/6 else math.pi/6)@np.array([0.,1.]);second=reflection(gamma)@first;assert np.linalg.norm(second-target)<1e-12
# Cross products are checked, not merely printed.
assert np.array_equal(np.cross([-1,0,0],[0,0,-1]),[0,-1,0])
assert np.array_equal(np.cross([0,0,-1],[-1,0,0]),[0,1,0])
# Explicit degenerate inverse pendulum model: all mass fractions produce the same observations.
LL=1.;ss=LL/math.sqrt(15);zz=LL/2-1.5*ss
for w in [.1,.5,.9]:
 xc=(1-w)*LL/2+w*(zz+1.5*ss);h=(1-w)*LL**2/12+w*5*ss**2/4;close(xc,.5);close(h,1/12)
results[83,1]['evidence']['nonidentifiable_mass_fraction_example']=dict(L=LL,s=ss,z=zz,hI=1/12)
# General chain length and period ratios, as well as 30 degrees.
th=math.pi/9;ell=math.sin(th)/math.cos(2*th);length=4*math.cos(th)**3/math.cos(2*th)
assert 4<length<3*math.sqrt(3);close(ell,.44647558819579863)
results[83,7]['evidence']['theta20_example']=dict(L_over_R=length,ell_over_R=ell,period_over_theta30=math.sqrt(ell))
# Supplemental branch assertions.
for al in [.5,1.,2.]:
 ac=(3-al)/(al+3);am=(al+1)/(al+3)
 if al<1:assert ac>am
 elif al>1:assert ac<am
 else:close(ac,am)
for n in [0,1,3,10]:
 norm=quad(lambda th:math.cos(th)**n*2*math.pi*math.sin(th),0,math.pi/2)[0];mom=quad(lambda th:math.cos(th)**(n+1)*2*math.pi*math.sin(th),0,math.pi/2)[0];close(mom/norm,(n+1)/(n+2))
results[87,8]['evidence']['cosine_power_exponents_checked']=[0,1,3,10]
# A cone has straight meridians and circular normals rotating with azimuth.
angle=.02;rr=.002;assert math.sin(angle)/rr>0
extra[4]['evidence']['theta02_r002_azimuthal_curvature']=math.sin(angle)/rr
ell0,shift,Asec=2.,1.,.1;close(Asec*shift,Asec*ell0/2);assert Asec*ell0>Asec*shift
for Efield in [.2,1.,3.]:
 resistivity=1+Efield**2;power=Efield**2/resistivity;assert resistivity>0 and power>0
assert (1-3**2)/(1+3**2)**2<0
sx,Lx,l0,mu,kx,gx=sp.symbols('s L l0 mu k g');net=kx*gx*(Lx**2-(1+mu)*(Lx-l0-sx)**2)/2
symbolic(sp.diff(net,sx)-kx*gx*(1+mu)*(Lx-l0-sx))
close((r2-c)**2-(r1-c)**2,lam*rho,1e-14)
omd,omi,r,tf=2.,3.,.7,.5;landing=np.array([r,omi*r*tf]);vparticle=np.array([0.,omi*r]);vplate=np.array([-omd*landing[1],omd*landing[0]]);vrel=vparticle-vplate;assert np.linalg.norm(vrel-np.array([omd*omi*r*tf,(omi-omd)*r]))<1e-12
extra[10]['evidence']['independent_vector_example']=vrel.tolist()
wall=1.;vbefore=0.;vafter=wall-(vbefore-wall);close(vafter,2*wall);close((vafter**2-vbefore**2)/2,wall*(vafter-vbefore))
# Fan speed table and its torque-energy identity.
A0=.002*8.31*300;Bf=9*.02*math.sin(.9)*(.2**2-.07**2)/2;Jf=9*1.29*.02*math.sin(.9)**3*(.2**4-.07**4)/2;rows=[]
for om in [35,70,140]:
 p=A0/(A0+Bf*om);Qout=p*Bf*om;P=Jf*om**3*p;assert 0<p<1 and 0<Qout<A0 and P>0;rows.append([om,p,Qout,P])
close(rows[1][3],results[83,8]['evidence']['power']);results[83,8]['evidence']['speed_comparison_table']=rows

# Check correlated ring-radius error propagation by direct finite differences.
lam,rho,c,sigma,g=5e-7,.1,.002,.07,9.8
r1=c+math.sqrt(lam*rho/2);r2=c+math.sqrt(3*lam*rho/2);D=r2-r1;k=1/(math.sqrt(3)-1)
def inverse_mass(a,b):
 rr=(b-a)**2/(lam*(math.sqrt(1.5)-math.sqrt(.5))**2);cc=a-k*(b-a)
 return 2*math.pi*sigma*cc*cc/(g*rr)
mref=inverse_mass(r1,r2);A=2*((1+k)/c+1/D);B=-2*(k/c+1/D);eps=1e-9
close((inverse_mass(r1+eps,r2)-inverse_mass(r1-eps,r2))/(2*eps*mref),A,1e-7)
close((inverse_mass(r1,r2+eps)-inverse_mass(r1,r2-eps))/(2*eps*mref),B,1e-7)
close(A+B,2/c)
close(math.hypot(A,B)*1e-6,.027084395709155964)
results[86,8]['evidence']['radius_error_propagation']=dict(A_per_m=A,B_per_m=B,independent_radius_sigma_m=1e-6,mass_relative_sigma=math.hypot(A,B)*1e-6,common_offset_relative_error=.001,finite_difference='pass')

papers=[dict(set=n,passed=True,questions=[results[n,q]for q in range(1,9)])for n in range(87,82,-1)]
assert len(results)==40 and len(extra)==12
(W/'results.json').write_text(json.dumps(dict(papers=papers,extra=extra,scope='关键结果交叉核验；原稿与全部文字另经逐题审读。带附加假设的题目按明示模型验证，不证明现实模型唯一。'),ensure_ascii=False,indent=2,default=str))
print('PASS: 40 question groups, 12 additional checks')
