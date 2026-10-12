from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle,Polygon,Rectangle
from scipy.integrate import cumulative_trapezoid
ROOT=Path(__file__).resolve().parent.parent
plt.rcParams.update({'font.family':'STHeiti','font.size':12,'axes.unicode_minus':False,'pdf.fonttype':42,'mathtext.fontset':'stix','axes.spines.top':False,'axes.spines.right':False})
BLUE='#17365D';RED='#BE4D25';GREEN='#347B69'
def fig(n,q,sol=False):
 f,ax=plt.subplots(figsize=(8,3.5)); ax.set_aspect('equal');ax.axis('off');return f,ax
def arrow(a,p,v,c=BLUE,label=None):
 a.annotate('',xy=np.array(p)+v,xytext=p,arrowprops={'arrowstyle':'->','color':c,'lw':1.7})
 if label:a.text(*(np.array(p)+.5*np.array(v)+[.03,.07]),label,color=c)
def save(f,n,q,sol=False):
 d=ROOT/f'蔡题{n:03}'/'figures';d.mkdir(exist_ok=True)
 name=f'{"solution" if sol else "question"}-{q:02}'
 f.tight_layout(pad=1.5);f.savefig(d/(name+'.pdf'));f.savefig(d/(name+'.png'),dpi=150);plt.close(f)
def title(a,t):a.set_title(t,pad=12,color=BLUE)
# 041-1
for sol in [False,True]:
 f,a=fig(41,1,sol);a.add_patch(Rectangle((0,1),4,.23,fc='#D8B892',ec=BLUE));a.add_patch(Rectangle((0,.6),.18,.4,fc='#CBD4DC'));a.add_patch(Rectangle((3.1,.6),.18,.4,fc='#CBD4DC'));a.plot([-.4,4.4],[.6,.6],c='gray');a.text(0,.3,'A 固定');a.text(3,.3,'B 移动');a.plot(2,1.12,'o',c=RED);a.text(1.9,1.45,'重心 C');arrow(a,(3.2,.8),(-.9,0),RED,'F');arrow(a,(2,1.23),(-.8,0),BLUE,'木条向左')
 if sol:arrow(a,(.08,1),(0,.8),GREEN,'$N_A$');arrow(a,(3.18,1),(0,.8),GREEN,'$N_B$');arrow(a,(.4,1.1),(.7,0),RED);arrow(a,(3,1.1),(-.7,0),RED);a.text(.7,-.1,'相对滑动：B 比木条更快；两处摩擦相反')
 else:a.text(.9,-.1,'$x_B=l-x_1$,  $x_C=l/2-u$')
 a.set(xlim=(-.5,4.5),ylim=(-.3,2.2));save(f,41,1,sol)
#041-2
for sol in [False,True]:
 f,a=fig(41,2,sol);a.axhline(0,c='gray');a.axvline(0,c='gray');a.plot(1,0,'o',c=RED);a.text(1.04,.05,'A (+q)');a.plot(0,0,'o',c=BLUE);a.text(-.12,.13,'B (−q)');arrow(a,(0,-.03),(0,-.4),BLUE,'$v_0$');a.text(.4,.05,'$d$')
 if sol:t=np.linspace(0,2*np.pi,500);a.plot(.4+.6*np.cos(t),-np.sin(t)/np.sqrt(5),c=GREEN);a.plot(-.2,0,'o',c=GREEN);a.text(-.5,-.22,'近点 $d/5$');title(a,'组合坐标的椭圆（实际两球仍在各自管内）')
 else:title(a,'相互垂直的无摩擦细管')
 a.set(xlim=(-.65,1.65),ylim=(-.8,.7));save(f,41,2,sol)
#041-3
for sol in [False,True]:
 f,a=fig(41,3,sol);a.plot([-1.5,1.5],[.45,-.45],c='gray');a.add_patch(Circle((0,.3),.3,fill=False,ec=BLUE,lw=2));a.add_patch(Rectangle((-.15,.6),.3,.55,fc='#CBD4DC'));arrow(a,(.5,.3),(.7,-.21),BLUE,'下坡 v')
 if sol:arrow(a,(0,.3),(0,-.8),RED,'Mg');arrow(a,(0,0),(-.65,.195),GREEN,'f');a.text(-1.4,1.25,r'$I\dot\omega=fR-\tau$');a.text(.25,1.15,r'$Ma=Mg\sin\theta-f$')
 else:a.text(-1.4,1.2,'均匀圆柱轮；车体姿态保持');a.text(.6,-.45,r'$\theta=0.8^\circ$')
 a.set(xlim=(-1.6,1.7),ylim=(-.6,1.5));save(f,41,3,sol)
#041-4
C=8.83e6*8.91e6;lam=.7185371258;r1=8.91e6;R=1.27e7;K=lam*9.8*(6.37e6)**2
z=np.linspace(1e-5,1,1000);u=r1+(R-r1)*z*z;T=8.83e6+K*(1/r1-1/u);integ=2*(R-r1)*z*C/(u*np.sqrt((T*u)**2-C*C));ang=cumulative_trapezoid(integ,z,initial=0)
for sol in [False,True]:
 f,a=fig(41,4,sol);a.add_patch(Circle((0,0),6.37,fc='#E5EDF4',ec=BLUE));a.plot(u*np.sin(ang)/1e6,u*np.cos(ang)/1e6,c=GREEN);a.plot(-u*np.sin(ang)/1e6,u*np.cos(ang)/1e6,c=GREEN);ends=[(R*np.sin(ang[-1])/1e6,R*np.cos(ang[-1])/1e6),(-R*np.sin(ang[-1])/1e6,R*np.cos(ang[-1])/1e6)]
 for p in ends:a.plot([0,p[0]],[0,p[1]],c='gray',ls='--');a.plot(*p,'o',c=RED)
 a.text(-1,1,'地球');a.text(.3,8.9,'最低点 $r_1$');a.text(ends[0][0]+.2,ends[0][1],'$F_1$')
 if sol:a.text(-7,15,r'$Tu\sin\alpha=F_2r_1$');a.text(-7,13.5,r'$T(u)=F_2+\lambda gr^2(1/r_1-1/u)$')
 else:title(a,'链形按给定张力重建，非恒重力悬链线')
 a.set(xlim=(-10,10),ylim=(-1,16));save(f,41,4,sol)
#041-5
for sol in [False,True]:
 f,a=fig(41,5,sol);a.plot([0,0,3],[3,0,0],c=BLUE,lw=3);a.scatter([0,0,3],[0,3,0],c=RED);a.text(-.25,-.25,'分束器');a.text(.2,2,'L');a.text(2,.2,'L');arrow(a,(-1,0),(.8,0),RED,'入射');a.text(1,1.6,'往返 N 次')
 if sol:a.text(1.2,2.9,r'$\Delta\phi=4\pi NL\sigma/\lambda$');a.text(1.2,2.35,r'$j=E/(4\pi D^2\Delta t)$')
 else:title(a,'简化双臂干涉仪（非实际设备比例）')
 a.set(xlim=(-1.3,5),ylim=(-.5,3.4));save(f,41,5,sol)
#041-6
f,a=fig(41,6);a.plot([0,0],[-.35,.35],c=RED,lw=3);a.add_patch(Polygon([[1,-.5],[1.2,0],[1,.5],[.8,0]],fc='#DDEAF3',ec=BLUE));a.plot([4,4],[-1,1],c='gray');a.plot([0,1,4],[0,.35,-.4],c=GREEN);a.plot([0,1,4],[0,-.35,.4],c=GREEN);a.text(-.15,.7,'狭缝');a.text(.6,.7,'双棱镜');a.text(3.7,1.1,'屏');a.text(.4,-.8,'h');a.text(2.3,-.8,'L');a.set(xlim=(-.5,4.5),ylim=(-1.2,1.3));save(f,41,6)
f,a=plt.subplots(figsize=(8,3.5));z=np.linspace(0,3,500);a.plot(z,np.abs(np.sinc(z)),c=BLUE);a.axvline(1,c=RED,ls='--');a.set(xlabel=r'$dl\sin\beta/(\lambda D)$',ylabel='调制度 M',ylim=(0,1.1));a.set_title('均匀狭缝且完整照明：首零点在横轴 1');save(f,41,6,True)
#041-7
f,a=fig(41,7);a.plot([-1,1],[0,0],c=BLUE,lw=3);a.scatter([-1,1],[0,0],c=[BLUE,RED],s=90);a.text(-1.3,.2,'−q, m');a.text(.8,.2,'+q, m');a.text(-.2,-.25,'轻杆 l');a.text(-1.4,.9,'均匀 B 指向纸外 ⊙');a.text(.8,.8,r'初始角速度 $\omega_0$');a.set(xlim=(-1.7,1.7),ylim=(-.6,1.3));save(f,41,7)
f,a=plt.subplots(figsize=(8,3.5));th=np.linspace(-np.pi,np.pi,800)
for w in [.7,1.5,2,2.5]:
 y=np.sqrt(np.maximum(w*w-2*(1-np.cos(th)),0));mask=w*w-2*(1-np.cos(th))>=0;a.plot(th,np.where(mask,y,np.nan),label=rf'$\omega_0/\omega_B={w}$');a.plot(th,np.where(mask,-y,np.nan),c=a.lines[-1].get_color())
a.set(xlabel=r'$\theta$',ylabel=r'$L_\theta/(I\omega_B)$');a.legend(fontsize=9,ncol=2);save(f,41,7,True)
#041-8
for sol in [False,True]:
 f,a=fig(41,8,sol)
 if not sol:
  a.plot([0,4],[0,0],c='gray');a.scatter([1,3],[0,0],c=[BLUE,RED],s=120);a.text(.8,.3,'$x_1$');a.text(2.8,.3,'$x_2$');a.text(1.7,.3,'耦合 k');a.text(.05,-.35,'各自另有势能 $kx_i^2/2$');a.set(xlim=(-.3,4.3),ylim=(-.6,1))
 else:
  a.axis('on');a.set_aspect('equal');x=np.linspace(-2,2,100);X,Y=np.meshgrid(x,x);a.contour(X,Y,X*X+Y*Y-X*Y,levels=[.3,1,2,3],colors=BLUE);a.set(xlabel='$x_1$',ylabel='$x_2$');title(a,'联合分布等高线：正相关，ρ=1/2')
 save(f,41,8,sol)
#042-1
for sol in [False,True]:
 f,a=fig(42,1,sol);pts=np.array([[0,0],[2,0],[.7,1.6]]);P=np.array([.8,.5]);a.add_patch(Polygon(pts,fill=False,ec=BLUE));a.plot(*P,'o',c=RED);a.text(P[0]+.05,P[1],'P / 合成重心')
 for i,p in enumerate(pts):a.plot(*p,'s',c=GREEN);a.text(p[0],p[1]-.2,f'{i+1}');a.plot([P[0],p[0]],[P[1],p[1]],c=RED,ls='--')
 if sol:a.text(.3,1.9,r'$\sum G_i=W$,  $\sum G_i(\boldsymbol{r}_i-\boldsymbol{P})=0$')
 else:title(a,'三点支承：秤轮换到三个顶点')
 a.set(xlim=(-.5,2.6),ylim=(-.4,2.3));save(f,42,1,sol)
#042-2
for sol in [False,True]:
 f,a=fig(42,2,sol);a.add_patch(Circle((-.55,0),.18,fc=BLUE));a.add_patch(Circle((.45,0),.22,fc=RED));a.plot(0,0,'+',c='black');a.plot([-.55,.45],[0,0],c='gray',ls='--');a.text(-.75,-.45,r'$29M_\odot$');a.text(.2,-.45,r'$36M_\odot$');arrow(a,(-.55,.2),(0,-.6),BLUE);arrow(a,(.45,-.25),(0,.6),RED)
 if sol:a.text(-1,1,r'$l^3=GM/(2\pi f)^2$');a.text(-1,.65,'题设半径 $r_i=Gm_i/c^2$')
 else:title(a,'牛顿圆轨道估算；质心两侧的半径不同')
 a.set(xlim=(-1.2,1.4),ylim=(-.7,1.3));save(f,42,2,sol)
#042-3
for sol in [False,True]:
 f,a=fig(42,3,sol);a.axhline(2,c=BLUE);a.add_patch(Circle((.5,.4),.16,fill=False,ec=GREEN));a.add_patch(Rectangle((1.8,.2),.22,.4,fc='#DDEAF3',ec=BLUE));a.text(.15,-.1,'可膨胀气泡');a.text(1.4,-.1,'密封刚性瓶');arrow(a,(.5,.6),(0,1),GREEN);arrow(a,(1.91,.6),(0,1),BLUE);a.text(2.35,.7,'深度 h');a.text(.5,2.15,'海面 $p_0$')
 if sol:a.text(.1,1.5,'$V(h)=p(H)V_0/p(h)$');a.text(1.4,1.5,'$V=V_0$')
 a.set(xlim=(-.2,3),ylim=(-.3,2.4));save(f,42,3,sol)
#042-4
for sol in [False,True]:
 f,a=fig(42,4,sol);a.add_patch(Rectangle((1,-.8),.5,1.6,fc='#DDEAF3',ec=BLUE));arrow(a,(-.1,0),(1,0),RED,'线偏振');arrow(a,(1.6,0),(1.2,0),BLUE,'出射');a.text(1.12,-1,'d')
 if sol:a.text(-.1,1.1,r'$\delta=2\pi d(n_1-n_2)/\lambda_0$');a.text(-.1,1.7,'输入与两轴成45°：四分之一波片给圆偏振')
 else:title(a,'双折射薄片：两本征分量相位累积不同')
 a.set(xlim=(-.4,3.4),ylim=(-1.2,1.5));save(f,42,4,sol)
#042-5
for sol in [False,True]:
 f,a=fig(42,5,sol);u=np.linspace(-2.7,2.7,500);Rc=1/12;rr=.05;X=Rc*(u+np.sin(u));Y=Rc*(1-np.cos(u));a.plot(X,Y+rr,c=BLUE,label='圆柱中心轨迹');a.plot(X+rr*np.sin(u/2),Y+rr*(1-np.cos(u/2)),c=RED,label='接触轨道');a.add_patch(Circle((0,rr),rr,fill=False,ec=GREEN));a.set_aspect('equal');a.axis('on');a.set(xlabel='x/a',ylabel='y/a');a.legend(fontsize=10)
 if sol:title(a,'中心摆线与法向偏移后的接触轨道')
 else:title(a,'纯滚动圆柱的等时轨道（r/a=0.05）')
 save(f,42,5,sol)
#042-6
for sol in [False,True]:
 f,a=fig(42,6,sol);t=np.linspace(0,1.4,200);a.plot(np.cos(t),np.sin(t),c=BLUE);arrow(a,(1,0),(0,.35),BLUE,'v');arrow(a,(.18,.98),(-.3,.08),BLUE);arrow(a,(.7,.7),(.3,.3),RED,'向外喷射')
 if sol:a.text(-.35,-.35,r'$m\gamma_v v\,d\theta=u\,dm_0$');a.text(-.35,-.65,r'$m_0/m_1=\exp(\gamma_v v|\theta|/u)$')
 else:title(a,'保持实验室速率，靠横向喷射改变方向')
 a.set(xlim=(-.6,1.6),ylim=(-.9,1.5));save(f,42,6,sol)
#042-7
for sol in [False,True]:
 f,a=fig(42,7,sol);a.plot([-.8,.8],[0,0],c='gray',lw=3);a.plot(0,1.1,'o',c=RED);a.text(.1,1.1,'m, q');arrow(a,(.5,1.2),(0,-.8),BLUE,'E');a.text(-.65,.6,'弹性反弹')
 if sol:a.text(-.6,1.65,r'$J=(4/3)\sqrt{2mF}\,h^{3/2}$');a.text(-.6,-.4,r'$h\propto F^{-1/3}$；$T\propto F^{-2/3}$')
 else:title(a,'匀强场中的一维弹跳：场缓慢变化')
 a.set(xlim=(-1,1.5),ylim=(-.6,2));save(f,42,7,sol)
#042-8
for sol in [False,True]:
 f,a=fig(42,8,sol);a.add_patch(Circle((0,0),1,fill=False,ec=BLUE,lw=2));th=np.pi/3;n=np.array([np.sin(th),np.cos(th)]);a.plot(*n,'o',c=RED);arrow(a,(0,0),(0,1.25),BLUE);a.text(-.62,1.13,"初始 z′");a.plot([0,n[0]],[0,n[1]],c=RED);a.text(.88,.52,'兔子 m');a.plot(0,0,'+',c='black')
 if sol:arrow(a,(0,0),(.4,-.75),GREEN,'旋转轴 a');a.text(-1.3,-1.35,'取 θ=60° 示意；需积分转动轴，不能直接累加角分量')
 else:title(a,'球与兔子：固定球心 / 自由球心两种模型')
 a.set(xlim=(-1.5,1.8),ylim=(-1.55,1.5));save(f,42,8,sol)
print('32 vector figures generated')
