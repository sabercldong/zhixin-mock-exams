from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle,Polygon,Arc
ROOT=Path(__file__).resolve().parent.parent
plt.rcParams.update({'font.family':'STHeiti','font.size':11,'axes.unicode_minus':False,'pdf.fonttype':42,'mathtext.fontset':'stix','axes.spines.top':False,'axes.spines.right':False})
B='#17365D';R='#BE4D25';G='#347B69'
def canvas(k=1):
 f,a=plt.subplots(1,k,figsize=(8,3.5));aa=np.atleast_1d(a)
 for ax in aa:ax.set_aspect('equal');ax.axis('off')
 return f,aa
def arrow(a,p,v,c=B,label=None,offset=(.02,.06)):
 p=np.asarray(p);v=np.asarray(v);a.annotate('',xy=p+v,xytext=p,arrowprops={'arrowstyle':'->','color':c,'lw':1.6})
 if label:a.text(*(p+.5*v+offset),label,color=c,fontsize=10)
def save(f,n,q,sol=False):
 d=ROOT/f'蔡题{n:03}'/'figures';name=f'{"solution" if sol else "question"}-{q:02}'
 f.tight_layout(pad=1.2);f.savefig(d/(name+'.pdf'));f.savefig(d/(name+'.png'),dpi=150);plt.close(f)
# Correct 30-degree half angle and actual circle-section geometry.
f,axs=canvas(2)
for ax in axs:
 A=np.array([-.5,0]);O=np.array([.5,0]);P=np.array([0,-np.sqrt(3)/2]);ax.plot([-.5,.5],[0,0],c='gray');ax.plot([-.5,0,.5],[0,P[1],0],c=B);ax.plot([0,0],[0,P[1]],c='gray',ls='--');ax.scatter([-.5,.5,0],[0,0,P[1]],c=[G,B,R]);ax.text(-.65,.06,'A');ax.text(.52,.04,'O');ax.text(-.04,.05,'C');ax.text(.04,P[1]-.06,'B');ax.set(xlim=(-.9,.9),ylim=(-1.2,.25))
axs[0].text(-.8,.15,r'$AC=CO=R/2$');axs[0].text(.08,-.4,r'$CB=\sqrt{3} R/2$');axs[0].set_title('最低点截面：两半径均为 R')
ax=axs[1];P=(0,-np.sqrt(3)/2);arrow(ax,P,(-.25,np.sqrt(3)/4),R,'T',(-.16,.02));arrow(ax,P,(.25,np.sqrt(3)/4),G,'N');arrow(ax,P,(0,-.25),B,'mg',(.13,-.08));ax.add_patch(Arc(P,.5,.5,theta1=90,theta2=120,ec=R));ax.text(-.13,-.48,'30°');ax.set_title('两支持力夹角60°；与竖直各30°');save(f,38,1,True)
# Four paraxial surfaces, matched to reduced-angle ray matrices.
for sol in (False,True):
 f,axs=canvas();a=axs[0];r1=1;r2=.65;gap=.5 if sol else 0;centre2=1+gap+r2
 for c,r in ((0,r1),(centre2,r2)):a.add_patch(Circle((c,0),r,fc='#E5EDF4',ec=B));a.text(c-.1,.4,'n=2')
 a.axhline(0,c='gray',lw=.7)
 for sign in (-1,1):
  y=.16*sign
  if sol:
   q=y/2; y2=y+(q-y)*r1; q2=q-y-y2; y3=y2+q2*gap; y4=y3+(q2-y3/r2)*r2; q4=q2-y3/r2-y4/r2
   xs=[-3,-1,1,1+gap,centre2+r2,centre2+r2+.8];ys=[0,y,y2,y3,y4,y4+q4*.8]
  else:xs=[-2,-1,1,1,centre2+r2,centre2+r2+.8];ys=[y,y,0,0,-r2*y,-r2*y]
  a.plot(xs,ys,c=R,lw=1.6);arrow(a,(xs[-2],ys[-2]),(.5,0),R)
 if sol:a.plot(-3,0,'o',c=G);a.text(-3,-.45,'物点 u=3r1');a.text(1.12,.16,'中间像');a.text(.4,-1.25,r'$\Delta=r_1^2/(u-r_1)$')
 else:a.text(-1.7,-1.25,'两球相切，出射平行；横向倍率 −r2/r1')
 a.set(xlim=((-3.4 if sol else -2.4),4),ylim=(-1.4,1.3));save(f,38,4,sol)
# Rolling friction and acceleration have the same direction.
f,axs=canvas(2);a,b=axs;a.add_patch(Circle((0,1),1,fill=False,ec=B));a.plot([-1.6,1.6],[0,0],c='gray');arrow(a,(-.1,0),(-.8,0),R,'f');arrow(a,(0,1),(-.8,0),G,'a');a.add_patch(Arc((0,1),1.4,1.4,theta1=20,theta2=145,ec=R));arrow(a,(-.58,1.4),(-.08,-.1),R);a.text(.65,1.8,'正力矩');a.text(-1.3,-.6,r'$I_{\rm eff}=3mr^2/2$');a.set(xlim=(-1.7,1.7),ylim=(-.7,2.5));a.set_title('纯滚动：摩擦推动质心')
b.axis('on');b.set_aspect('auto');theta=np.linspace(0,np.pi/2,200);b.plot(theta,1-.75*np.sin(theta),c=B);b.set(xlabel=r'$\theta$',ylabel=r'$I/I_0$');b.set_title(r'示例 $C_B/(LI_0)=0.75$');save(f,38,5,True)
# Actual bisector reflection branches, not arbitrary arches.
f,axs=canvas(2);a,b=axs;t=np.linspace(0,2*np.pi,600);x=.75
circle=np.linspace(0,2*np.pi,300);a.plot(np.cos(circle),np.sin(circle),c=B);a.plot(x*np.cos(circle),x*np.sin(circle),c='gray',ls='--');a.plot(x,0,'o',c=R);a.text(x+.03,0,'A');a.plot(0,0,'+',c=B);a.text(0,-.13,'O');q=1.8;a.plot(x*np.cos(q),x*np.sin(q),'o',c=G);a.text(x*np.cos(q)-.15,x*np.sin(q),'B');a.set(xlim=(-1.15,1.15),ylim=(-1.15,1.15));a.set_title('A与B轨道均距圆心0.75r')
b.axis('on');b.set_aspect('auto');tau=[np.ones_like(t)/3,np.ones_like(t)*7/3,np.ones_like(t)*8/3,4*x*np.abs(np.sin(t/2))*2/3, (2*np.sqrt(1+x*x-2*x*np.cos(t/2))+2*x*np.abs(np.sin(t/2)))*2/3,(2*np.sqrt(1+x*x+2*x*np.cos(t/2))+2*x*np.abs(np.sin(t/2)))*2/3]
for i,y in enumerate(tau):b.plot(t/(2*np.pi),y,label=str(i+1))
b.set(xlabel='t/T',ylabel='延迟 / s',ylim=(0,3.2));b.legend(ncol=3,fontsize=9);b.set_title('5、6为两个可追踪驻值分支');save(f,38,7)
f,axs=canvas(2);a,b=axs;phi=1.8;A=np.array([x,0]);Q=x*np.array([np.cos(phi),np.sin(phi)])
for psi,c in ((phi/2,R),(phi/2+np.pi,G)):
 P=np.array([np.cos(psi),np.sin(psi)]);a.plot(*np.array([A,P,Q,A]).T,c=c);a.plot(*P,'o',c=c)
a.plot(np.cos(circle),np.sin(circle),c=B);a.scatter(*np.array([A,Q]).T,c=[R,G]);a.text(*(A+[.03,.03]),'A');a.text(*(Q+[-.15,.05]),'B');a.set(xlim=(-1.15,1.15),ylim=(-1.15,1.15));a.set_title('反射点位于角平分径线两端')
b.axis('on');b.set_aspect('auto');b.plot(t/(2*np.pi),tau[4],c=R,label='5');b.plot(t/(2*np.pi),tau[5],c=G,label='6');b.axhline(8/3,c='gray',ls='--');b.set(xlabel='t/T',ylabel='延迟 / s',ylim=(0,3.2));b.legend();b.set_title('更多驻点可存在；图示不穷举回波');save(f,38,7,True)
# Force arrows at landing must point in the forward direction.
f,axs=canvas();a=axs[0];t=np.linspace(0,1,200);a.plot(3*t,4*t*(1-t),c=B);a.plot([-.3,3.7],[0,0],c='gray');arrow(a,(0,0),(.55,.8),B,'u');arrow(a,(3,0),(.55,-.6),B,'u′');arrow(a,(3,0),(0,.7),G,'I_N');arrow(a,(3,.03),(.7,0),R,'I_f');a.text(.5,1.3,r'$k\Delta x=I_f\leq\mu mg\tau$');a.set(xlim=(-.5,4),ylim=(-.7,1.6));a.set_title('向前摩擦冲量补回飞行中的水平阻力损失');save(f,39,1,True)
# Halo: Snell-consistent rays through nonparallel faces of a 60-degree prism.
for sol in (False,True):
 f,axs=canvas(2 if sol else 1);a=axs[0];a.add_patch(Polygon([[0,0],[1.5,1.5*np.sqrt(3)],[3,0]],fc='#E5EDF4',ec=B));y=.9;P=np.array([y/np.sqrt(3),y]);Q=np.array([3-y/np.sqrt(3),y]);alpha=np.arcsin(1.309/2)-np.pi/6;vin=np.array([np.cos(alpha),np.sin(alpha)]);vout=np.array([np.cos(alpha),-np.sin(alpha)]);a.plot(*np.array([P-1.1*vin,P,Q,Q+1.1*vout]).T,c=R,lw=2)
 for p,angle in ((P,-np.pi/6),(Q,np.pi/6)):
  d=.55*np.array([np.cos(angle),np.sin(angle)]);a.plot(*np.array([p-d,p+d]).T,c='gray',ls='--')
 arrow(a,P-1.05*vin,.45*vin,R);arrow(a,Q+.25*vout,.4*vout,R);a.text(1.35,2.1,'60°');a.text(.9,.68,'内部 r1=r2=30°');a.text(.8,-.45,r'$\delta_{\min}=2\arcsin(n/2)-\pi/3$');a.set(xlim=(-.8,3.8),ylim=(-.6,2.8));a.set_title('六角冰晶通道的等效60°棱镜')
 if sol:
  a=axs[1];a.plot([0,0],[-.8,.8],c=B,lw=3);a.plot([2,2],[-.8,.8],c='gray',ls='--');a.plot([2.7,2.7],[-.8,.8],c='gray')
  for s in (-1,1):a.plot([-1,0,2,2.7],[.6*s,.6*s,0,-.21*s],c=R)
  a.text(-.2,1,'镜头 D');a.text(1.8,.9,'焦面 f');a.text(2.5,1.1,'底片 v');a.text(-.6,-1.1,r'$r=v\tan\theta_0+D(v-f)/(2f)$');a.set(xlim=(-1.1,3.2),ylim=(-1.25,1.3));a.set_title('底片在太阳焦面之后')
 save(f,39,4,sol)
# Endpoint impulse and velocity attach to actual arc endpoints, along actual tangents.
for sol in (False,True):
 f,axs=canvas();a=axs[0];angles=np.linspace(.25,2.65,10 if sol else 300);pts=np.c_[np.cos(angles),np.sin(angles)];a.plot(*pts.T,c=B)
 if sol:a.scatter(*pts.T,c=B,s=18)
 # Increasing arclength from first to last: pull first away, final moves toward previous.
 tang0=np.array([-np.sin(angles[0]),np.cos(angles[0])]);tang1=np.array([-np.sin(angles[-1]),np.cos(angles[-1])]);arrow(a,pts[0],-.6*tang0,R,'J');arrow(a,pts[-1],-.45*tang1,G,'v_end')
 if sol:
  j=4;e=pts[j+1]-pts[j];e=e/np.linalg.norm(e);arrow(a,pts[j],.25*e,R,'I_j');arrow(a,pts[j+1],-.25*e,G)
 a.text(-.8,-.35,r'$v_{\rm end}=J\Theta/(m\sinh\Theta)$');a.set(xlim=(-1.5,1.6),ylim=(-.7,1.45));a.set_title('绳的弧线与端点切向冲量；Θ为总转角');save(f,39,7,sol)
# Cube: field points from the positive face to the negative face.
f,axs=canvas(2);a,b=axs
pts=np.array([[i+.35*k,j+.25*k] for k in (0,1) for j in (0,1) for i in (0,1)])
for i,p in enumerate(pts):
 for j,q in enumerate(pts):
  if j>i and sum(abs(np.array([i%2,(i//2)%2,i//4])-np.array([j%2,(j//2)%2,j//4])))==1:a.plot(*np.array([p,q]).T,c='gray')
 a.scatter(*p,c=R if i%2==0 else B);a.text(*(p+[.03,.04]),'+' if i%2==0 else '−',c=R if i%2==0 else B)
arrow(a,(.4,.55),(.7,0),G,'E_max');a.set(xlim=(-.2,1.6),ylim=(-.25,1.5));a.set_title('左面四正，右面四负：合场向右')
b.axis('on');b.set_aspect('auto');b.bar([0,4,8,12,16],[8,24,24,8,6],width=2,color=B);b.set(xlabel=r'$|U|^2$',ylabel='配置数');b.set_xticks([0,4,8,12,16]);b.set_title('全部70种配置');save(f,40,1,True)
# Highest-point Euler term shown separately; lowest-point directions in rotated axes.
f,axs=canvas(2);a,b=axs
for ax in axs:ax.set(xlim=(-1.5,1.6),ylim=(-1.1,1.35))
a.plot([0,0],[1,-.15],c='gray');a.plot(0,-.15,'o',c=B);a.text(.05,-.12,'P_H');arrow(a,(0,-.15),(0,-.6),R,r'$(l\alpha_0+\omega^2r)e_t$');arrow(a,(0,-.15),(.7,0),G,r'$\alpha_0r e_r$',(.02,.15));a.set_title('最高位置：欧拉项沿摆臂');a.text(-1.4,1,r'$a_H^2=(l\alpha_0+\omega^2r)^2+(\alpha_0r)^2$')
b.plot(0,0,'o',c=B);b.text(.05,.08,'P_L');arrow(b,(0,0),(0,.65),R,r'$-\Omega^2l e_r$',(.05,0));arrow(b,(0,0),(.7,0),G,r'$(\Omega^2+\omega^2)r e_t$',(-.35,-.25));b.set_title('最低位置前视图最左点：科里奥利项为零');b.text(-1.4,1,r'$\rho_L=-r e_t,\quad v_{rel}\parallel e_k$');save(f,40,2,True)
# Both candidate equilibria require opposite laboratory current orientations.
f,axs=canvas();a=axs[0];a.axis('on');a.set_aspect('auto');z=np.r_[np.linspace(-3,-.3,300),np.nan,np.linspace(.3,3,300)];a.plot(z,1/z**2,c=B);a.axhline(1,c='gray');a.scatter([-1,1],[1,1],c=[R,G]);a.text(-2.9,2.2,'负侧：I_s>0，不稳定');a.text(.9,2.2,'正侧：I_s<0，稳定');a.set(xlabel='z/a',ylabel='向上磁力 / mg',ylim=(0,3));a.set_title('两半轴分别选电流方向；同一绕向仅有一侧平衡');save(f,40,3,True)
# Proper and lab periods: two speeds, same proper time per turn.
f,axs=canvas();a=axs[0]
for y,g in ((.9,1.4),(.2,2.5)):
 a.plot([0,g],[y,y],c=B,lw=2);a.plot([0,0],[y-.08,y+.08],c=B);a.plot([g,g],[y-.08,y+.08],c=B);a.text(.1,y+.12,f'实验室：γ={g}，一圈时间 γT0')
a.plot([0,1],[-.6,-.6],c=R,lw=2);a.text(.1,-.45,'粒子固有时间：T0=2πm/(eB)，两种速度相同');a.set(xlim=(-.2,3),ylim=(-1,.0+1.3));a.set_title('每圈固有时间与速度无关');save(f,40,6,True)
# Hohmann ellipse: Sun is at a focus, endpoints +r_E and -r_M.
for sol in (False,True):
 f,axs=canvas(2 if sol else 1);a=axs[0];rE=1;rM=.387;aa=(rE+rM)/2;bb=np.sqrt(rE*rM);c=(rE-rM)/2;t=np.linspace(0,2*np.pi,500)
 for r in (rE,rM):a.plot(r*np.cos(t),r*np.sin(t),c='gray')
 a.plot(c+aa*np.cos(t),bb*np.sin(t),c=B,lw=2);a.plot(0,0,'o',c=R);a.text(.03,-.12,'太阳 / 焦点');a.scatter([1,-rM],[0,0],c=[B,G]);a.text(.85,-.15,'地球');a.text(-.65,-.15,'水星');a.plot(c,0,'+',c='gray');a.text(c,.13,'椭圆中心');arrow(a,(1,0),(0,.35),B,'v_E');arrow(a,(-rM,0),(0,-.45),G,'v_p');a.set(xlim=(-1.1,1.25),ylim=(-1.15,1.2));a.set_title('日心转移椭圆：长轴端点位于两圆轨道')
 if sol:
  a=axs[1];a.add_patch(Circle((0,0),.45,fc='#DDEAF3',ec=B));a.plot([-1,-.6,-.45], [.6,.35,0],c=R);arrow(a,(-.45,0),(.45,0),R,'u_s');a.text(-.3,-.1,'水星');a.text(-1.1,1,r'$u_s^2=u_\infty^2+2\mu_M/R_M$');a.text(-1.1,-.8,'软着陆：制动到零；捕获圆轨道另减圆轨道速率');a.set(xlim=(-1.3,1.5),ylim=(-1,1.2));a.set_title('近水星引力加速与制动')
 save(f,40,8,sol)
# Add required nonunique ODE sketch to question 041-7.
f,axs=canvas(2);a,b=axs;a.axis('on');a.set_aspect('auto');xx=np.linspace(-1,5,300)
for C in (0,1.5):a.plot(xx,np.maximum(xx-C,0)**4/256,label=f'C={C}')
a.axhline(0,c=G,lw=2,label='零解');a.set(xlabel='x',ylabel='y',ylim=(-.05,2.5));a.legend(fontsize=8);a.set_title(r"$y'=y^{3/4}$：零解与等待后增长")
b.plot([-1,1],[0,0],c=B,lw=3);b.scatter([-1,1],[0,0],c=[B,R]);b.text(-1.3,.25,'−q,m');b.text(.7,.25,'+q,m');b.text(-1.3,.8,'B 指向纸外 ⊙');b.text(-.1,-.3,'轻杆 l');b.set(xlim=(-1.6,1.6),ylim=(-.6,1.1));b.set_title('磁偶极子初态 θ=0');save(f,41,7)
# Equilateral support geometry in both versions.
for sol in (False,True):
 f,axs=canvas();a=axs[0];pts=np.array([[0,0],[2,0],[1,np.sqrt(3)]]);P=np.array([1,.5]);a.add_patch(Polygon(pts,fill=False,ec=B));a.plot(*P,'o',c=R);a.text(*(P+[.06,.05]),'P / 合成重心')
 for i,p in enumerate(pts):a.plot(*p,'s',c=G);a.text(*(p+[.02,-.18]),str(i+1));a.plot(*np.array([P,p]).T,c='gray',ls='--')
 if sol:a.text(-.2,2.05,r'$G_i/W=\lambda_i$，三个重心坐标之和为1')
 a.set(xlim=(-.6,2.7),ylim=(-.4,2.4));a.set_title('等边三角钢板，秤轮换到三个顶点');save(f,42,1,sol)
# Adiabatic phase-space area, scaled so equal areas are visible.
f,axs=plt.subplots(figsize=(8,3.5));z=np.linspace(0,1,400)
for force,c in ((1,B),(2,R)):
 h=force**(-1/3);zz=z*h;p=np.sqrt(2*force*(h-zz));axs.plot(zz,p,c=c,label=f'F/F0={force}');axs.plot(zz,-p,c=c);axs.plot([0,0],[-p[0],p[0]],c=c)
axs.set(xlabel='z/h0',ylabel='p / √(mF0h0)');axs.legend();axs.set_title('场加强：最高点下降，动量范围扩大，闭合面积不变');save(f,42,7,True)
# Axis-return condition represented by quantitative final tilt, avoiding a fixed-axis cartoon.
f,a=plt.subplots(figsize=(8,3.5));theta=np.linspace(0,np.pi/2,700)
for k,c,label in ((2.5,B,'球心固定'),(1.25,R,'球心自由')):
 lam=np.sqrt(1+k*(k+2)*np.sin(theta)**2);A=k*np.cos(theta)*np.sin(theta);C=-1-k*np.sin(theta)**2;zz=C*C/lam**2+A*A/lam**2*np.cos(2*np.pi*lam);tilt=np.arccos(np.clip(zz,-1,1));a.plot(np.degrees(theta),np.degrees(tilt),c=c,label=label)
a.set(xlabel='初始 θ / °',ylabel='兔子一圈后球轴倾角 / °');a.legend();a.set_title('实验室规定兔子圆轨迹：轴返回的非退化零点不同');save(f,42,8,True)
print('Rebuilt 25 corrected vector diagrams')

# Numerical paraxial ray tracing of the mirror-unfolded return system.
f,axs=canvas();a=axs[0];l=1.;f1=1.2;f2=.8;h=f2*l*(2*l-3*f1)/(f1*f2-3*f1*l-f2*l+2*l*l)
xs=np.array([0,l,3*l,3*l+2*h,5*l+2*h,6*l+2*h]);fs=[f1,f2,f2,f1]
for slope in (-.11,.11):
 y=0.;v=slope;ys=[y]
 for i in range(1,len(xs)):
  y+=v*(xs[i]-xs[i-1]);ys.append(y)
  if i<5:v-=y/fs[i-1]
 a.plot(xs,ys,c=R,lw=1.8)
for xx,name in zip(xs[1:5],['L1','L2','L2′','L1′']):
 a.plot([xx,xx],[-.35,.35],c=B);a.text(xx-.08,.43,name)
mirror=3*l+h;a.plot([mirror,mirror],[-.6,.6],c='gray',ls='--');a.text(mirror-.65,.69,'镜面展开线')
a.scatter([xs[0],xs[-1]],[0,0],c=G);a.text(-.1,-.25,'S');a.text(xs[-1]-.1,-.25,'S′')
a.text(.2,-.8,r'$M_{12}=0,\quad h^\prime=\frac{f_2l(2l-3f_1)}{f_1f_2-3f_1l-f_2l+2l^2}$')
a.set(xlim=(-.5,8.4),ylim=(-1.,.95));a.set_title('展开后的真实傍轴光线；示例 f1=1.2l、f2=0.8l');save(f,40,5,True)
# Correct impedance labels: crossing branches have no electrical junction.
f,axs=canvas();a=axs[0];pts={1:np.array([-2.,0]),2:np.array([2.,0]),3:np.array([0.,1.5]),0:np.array([0.,-1.5])}
for i,j,lab,pos in [(1,2,'R',(-1.,.1)),(0,3,'R',(.12,-.6)),(1,3,'−iR',(-1.15,.9)),(2,3,'iR',(1.,.9)),(1,0,'iR',(-1.2,-.9)),(2,0,'−iR',(1.,-.9))]:
 a.plot(*np.array([pts[i],pts[j]]).T,c=B);a.text(*pos,lab,fontsize=12,bbox=dict(fc='white',ec='none',pad=1))
for i,p in pts.items():
 a.add_patch(Circle(p,.18,fc='white',ec=B,zorder=5));a.text(*p,str(i),ha='center',va='center',zorder=6)
a.text(-2.,-2.1,r'$V_3-V_0=i(V_1-V_2),\quad Z_{\rm eq}=R/2$')
a.set(xlim=(-2.5,2.5),ylim=(-2.4,2.));a.set_title('六条棱的等效电路；交叉处不相连');save(f,39,5,True)
