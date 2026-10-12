from pathlib import Path
import math,re
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
PRE=r'''\documentclass[multi=tikzpicture,border=9pt]{standalone}
\usepackage[UTF8]{ctex}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,patterns,decorations.pathmorphing}
\definecolor{main}{HTML}{17365D}
\definecolor{accent}{HTML}{AC3931}
\tikzset{every picture/.style={font=\small,line width=.75pt},
>={Stealth[length=2mm]},arr/.style={->},
box/.style={draw=main,rounded corners=2pt,fill=main!4,text width=3.6cm,minimum height=1cm,align=center},
note/.style={align=center,text width=9cm}}
\begin{document}
'''
GROUPS={'01': ['question', 'retarded', 'frames', 'branches', 'rate'], '02': ['question', 'impulse', 'envelope', 'coverage', 'probability'], '03': ['question', 'energy', 'catenary', 'spacing', 'hexagon'], '04': ['question', 'gradient', 'diffusion', 'drift', 'time'], '05': ['question', 'recursion', 'roots', 'decay', 'limits'], '06': ['question', 'angular', 'velocity', 'acceleration', 'constraint'], '07': ['question', 'image', 'flight', 'frequency', 'double'], '08': ['question', 'field', 'parallel', 'radial', 'comparison']}
NAMES={q:[f"{n}-{q}" for n in ns] for q,ns in GROUPS.items()}
def save(q,figs):
 assert len(figs)==5
 (ROOT/f'figures/题{q}_图稿源文件.tex').write_text(PRE+''.join('\n\\begin{tikzpicture}\n'+s+'\n\\end{tikzpicture}\n' for s in figs)+'\\end{document}\n')
def line(x,y):return ' -- '.join(f'({a:.5f},{b:.5f})' for a,b in zip(x,y))
def plot(x,y,style='main,thick'):return '\\draw['+style+'] '+line(x,y)+';\n'
def axes(xmax=6,ymax=4,xlabel='$x$',ylabel='$y$'):
 return f'\\draw[arr] (0,0)--({xmax},0) node[right]{{{xlabel}}};\n\\draw[arr] (0,0)--(0,{ymax}) node[above]{{{ylabel}}};\n'
def flow(labels,note):
 s=''
 for i,(x,y) in enumerate([(0,0),(5,0),(5,-2.3),(0,-2.3)]):s+=f'\\node[box] (n{i}) at ({x},{y}) {{{labels[i]}}};\n'
 return s+r'\draw[arr] (n0)--(n1);\draw[arr] (n1)--(n2);\draw[arr] (n2)--(n3);'+'\n'+r'\node[note] at (2.5,-4.1) {'+note+'};'
def main():
 (ROOT/'figures').mkdir(parents=True,exist_ok=True)
 lamp=r'''\draw[thick] (-.5,0)--(6,0);\draw[main,thick] (0,0)--(0,3);\fill[accent] (0,3) circle (3pt);\node[left] at (0,1.5){$h$};\draw[main,thick] (2,0)--(2,1.5);\node[right] at (2,1.4){$l=h/2$};\draw[arr,accent] (2.2,.5)--(3.4,.5) node[midway,above]{$v$};\draw[dashed] (0,3)--(4,0);\node[below] at (0,0){灯柱};\node[below] at (2,0){脚 $X$};\node[below] at (4,0){瞬时影界 $2X$};\node[note] at (2.5,-1.3){虚线仅为忽略光行时的相似三角形};'''
 retard=r'''\draw[thick] (-.5,0)--(6,0);\fill (0,3) circle (3pt);\draw[accent,thick] (0,3)--(4,0);\draw[main,thick] (2,0)--(2,1.5);\draw[main,dashed] (3,0)--(3,1.5);\node[above] at (1.8,2){遮挡时刻};\node[above right] at (3,1.5){到达时刻};\node[below] at (4,0){$q$};\draw[arr] (2,.3)--(3,.3);\node[note] at (2.5,-1.2){头部横坐标 $q/2$ 属于过去；脚 $X$ 属于现在};'''
 frames=flow([r'地面同时距离\\$X=h/2$',r'地面影长\\$|q-X|=0.138086h$',r'人系同时距离\\$D=h/2$',r'近端人系影长\\$|s|=0.115912h$'],r'两问是不同脚事件；同一事件满足 $X=\gamma D$')
 branch=axes(6,4,'$s/h$','$D/h$');ss=np.linspace(-2.5,.5,220);dd=ss+.6*np.sqrt(1+4*ss**2);branch+=plot((ss+2.5)*1.8,dd*2.8);branch+=r'\draw[accent,dashed] (0,1.4)--(5.4,1.4);\node[right] at (5.4,1.4){$D/h=0.5$};\node[below] at (4.5,0){$0$};\node[note] at (2.7,-1.2){同一同时切片可有近端和远端两个迟滞解};'
 rates=flow([r'有向坐标\\$s<0$',r'求导\\$\dot D=v$',r'近端速度\\$\dot s=0.823047c$',r'距离导数\\$\dot L=-\dot s$'],r'取绝对值的时机：先求有向导数，再判断长度增减')
 save('01',[lamp,retard,frames,branch,rates])
 pen=r'''\draw[arr] (-.5,0)--(5,0) node[right]{$x$};\draw[arr] (0,-2)--(0,3) node[above]{$z$};\draw[main,very thick] (0,1.8)--(4,1.8);\fill[accent] (2,1.8) circle (3pt);\draw[arr,accent] (2,1.5)--(2,.4) node[right]{$V=v_0/2$};\draw[arr] (2.7,2.4) arc (40:150:.8);\node[above] at (3.4,1.8){$\omega=v_0/l$};\draw[dashed] (2,-1.5)--(2,2.7);\node[note] at (2,-3){局部下落：质心匀速向下，笔绕质心逆时针转动};'''
 impulse=r'''\draw[main,very thick] (0,0)--(5,0);\fill (0,0) circle (3pt);\fill[accent] (2.5,0) circle (3pt);\draw[arr,accent] (5,0)--(5,2) node[right]{$v_0$};\draw[arr] (2.5,0)--(2.5,1) node[left]{$V=v_0/2$};\node[below] at (0,0){冲量期间固定端};\node[note] at (2.5,-1.4){释放后 $I_C=ml^2/12$；平动与转动动能之和保持};'''
 env=''
 for th in np.linspace(-np.pi,np.pi,17):
  xx=.5+np.array([-.5,.5])*np.cos(th);zz=-th*.5+np.array([-.5,.5])*np.sin(th);env+=plot(xx*5,zz*1.8,'gray!40')
 th=np.linspace(-np.pi,np.pi,220);env+=plot((.5+.5*np.cos(th)**2)*5,(-th*.5+.25*np.sin(2*th))*1.8,'accent,thick')+plot((.5-.5*np.cos(th))*5,(-th*.5-.5*np.sin(th))*1.8,'main,thick')
 env+=r'\node[note] at (2.5,-4.2){灰色运动线段；红色内部包络，蓝色端点候选轨迹\\候选曲线需删去被其他时刻覆盖的弧};'
 cover=r'''\draw[main,thick] (0,0) rectangle (1,4.71);\fill[main!30] (0,0) rectangle (1,4.71);\draw[accent,thick] (3,0) rectangle (4,4.71);\fill[accent!35] (3,2.06) rectangle (4,2.65);\node[below] at (.5,-.2){$x=0.2l$};\node[below] at (3.5,-.2){$x=0.8l$};\draw[<->] (4.7,0)--(4.7,4.71) node[midway,right]{$H=\pi l/2$};\node[note] at (2,-1.6){一个周期内的覆盖：左侧为全部，右侧宽度 $2A$};'''
 xs=np.linspace(.001,.999,150);probs=[]
 for xx in xs:
  d=xx-.5;al=np.arccos(2*abs(d));th=np.linspace(-al,al,4001);z=-th/2+d*np.tan(th);probs.append(min(1,(max(z)-min(z))/(np.pi/2)))
 prob=axes(6,3.7,'$x/l$','$P$')+plot(xs*5,np.array(probs)*3)
 prob+=r'\node[left] at (0,3){$1$};\node[below] at (5,0){$1$};\fill[accent] (1,3) circle (2pt);\fill[accent] (4,.37208) circle (2pt);\node[note] at (2.5,-1.3){$P(0.2l)=1$，$P(0.8l)=0.124027$；按扫掠并集计算};'
 save('02',[pen,impulse,env,cover,prob])
 pp=2*np.log(1+np.sqrt(2));xx=np.linspace(-pp/2,pp*1.5,320);phase=np.mod(xx,pp);yy=1-np.cosh(np.minimum(phase,pp-phase));road=plot(xx*2,yy*2,'main,very thick')
 cx=pp;rr=2*np.sqrt(2);road+=plot([cx,cx+rr,cx,cx-rr,cx],[2-rr,2,2+rr,2,2-rr],'accent,thick')
 road+=r'\draw[dashed] (-1.8,2)--(5.4,2);\fill[accent] (1.762747,2) circle (3pt);\node[above right] at (1.762747,2){轴高 $a$};\node[note] at (1.7,-2){槽底接触半径为 $\sqrt2a$；方轮与路面按同一比例绘制};'
 energy=flow([r'槽顶\\$V=a\omega$',r'槽底\\$V=\sqrt2a\omega$',r'总动能\\$K=\frac12(M+2m)V^2$\\$+I\omega^2$',r'同一次运动\\$K$ 保持，$\omega$ 改变'],r'每个位置的 $\omega$ 是瞬时值，不能强行相等')
 cat=axes(6,3.5,'$x/a$','$-f/a$');tt=np.linspace(0,np.log(1+np.sqrt(2)),100);cat+=plot(tt*5,(np.cosh(tt)-1)*6,'accent,thick')+r'\node[note] at (2.5,-1.3){半槽 $f=a[1-\cosh(x/a)]$；弧长 $s=a\sinh(x/a)$};'
 spacing=r'''\draw[<->] (0,2)--(6,2) node[midway,above]{$d=np$};\foreach \x in {0,6}{\draw[main,thick] (\x,0)--(\x+1.4,1.4)--(\x,2.8)--(\x-1.4,1.4)--cycle;\fill[accent] (\x,1.4) circle (2pt);}\node[note] at (3,-1.2){全相位不穿入需 $d\ge2\sqrt2a$；最小整数周期为 $n=2$};'''
 hexag=r'''\draw[arr] (0,0)--(6,0);\draw[main,thick] (0,0)--(3,-3);\draw[accent,thick] (0,0)--(3,-1.732);\node[right] at (3,-3){方轮 $45^\circ$};\node[right] at (3,-1.732){六边形 $30^\circ$};\node[note] at (2.5,-4.5){接触边切换角不同；六边形需要重新截取匹配路面};'''
 save('03',[road,energy,cat,spacing,hexag])
 square=r'''\draw[main,thick] (0,0) rectangle (3,3);\draw[arr] (0,1.5)--(-1,1.5);\draw[arr,accent] (3,1.5)--(4.7,1.5);\draw[arr] (1.5,0)--(1.5,-1);\draw[arr,accent] (1.5,3)--(1.5,4.7);\node at (1.5,1.5){叶片};\node[note] at (1.5,-2.1){对边张力相减；常量背景消去，净力为 $S\nabla\sigma$};'''
 grad=flow([r'边界张力\\$\oint\sigma\mathbf n\,dl$',r'面积梯度\\$\int\nabla\sigma\,dA$',r'线性或二次场\\精确取中心梯度',r'一般非线性场\\小片近似'],r'张力较大的一侧拉力较强；$a>0$ 时糖源吸引叶片')
 hemi=r'''\draw[main,thick] (-3,0)--(3,0) node[right]{水面};\fill[accent] (0,0) circle (3pt);\draw[main] (3,0) arc (0:-180:3);\foreach \a in {210,240,270,300,330}{\draw[arr,accent] (0,0)--(\a:2.6);}\node[note] at (0,-4.2){深水半空间：流过半球面积 $2\pi r^2$，总摩尔率 $J$};'''
 drift=r'''\fill[accent] (0,0) circle (3pt);\node[above] at (0,0){糖源};\draw[main] (4,0) circle (.45);\draw[arr,accent,thick] (3.7,0)--(2.2,0) node[midway,above]{$\mathbf F$};\draw[arr] (4.4,0)--(5.6,0) node[midway,above]{$-k\mathbf v$};\node[note] at (2.5,-1.6){终端漂移：$\dot r=-C/r^2$；张力力与阻力平衡};'''
 times=axes(6,3.7,'$t/t_*$','$r^3/r_1^3$');times+=plot([0,5],[3,0])+r'\draw[accent,dashed] (4.375,0)--(4.375,.375)--(0,.375);\node[below] at (4.375,0){$7/8$};\node[left] at (0,.375){$1/8$};\node[note] at (2.5,-1.4){半径减半所需时间占形式原点时间的 $7/8$};'
 save('04',[square,grad,hemi,drift,times])
 circ=r'\draw (0,0)--(7,0);\draw (0,0)--(0,1.1);\draw (0,1.9)--(0,3);\draw (0,1.5) circle (.4);\node at (0,1.5){$U$};'
 for n in range(3):
  x=2*n;lab=['','2','4'][n];circ+=f'\\draw ({x},3)--({x+.4},3);\\draw[thick] ({x+.4},2.8) rectangle ({x+1.3},3.2);\\node[above] at ({x+.85},3.3){{${lab}R$}};\\draw ({x+1.3},3)--({x+2},3)--({x+2},2.6);\\draw[thick] ({x+1.8},1.8) rectangle ({x+2.2},2.6);\\node[right] at ({x+2.3},2.2){{${lab}R$}};\\draw ({x+2},1.8)--({x+2},1.5);\\draw[decorate,decoration={{coil,segment length=3pt,amplitude=2pt}}] ({x+2},1.5)--({x+2},.4);\\draw ({x+2},.4)--({x+2},0);\\node[right] at ({x+2.3},.9){{${lab}L$}};\n'
 circ+=r'\node[note] at (3.5,-1.2){每级先横向 $2^nR$，再纵向串联 $2^nR$ 与 $2^nL$};'
 recursion=flow([r'首串联元件\\$R$',r'节点纵支路\\$B=R+i\omega L$',r'完整余网\\$2Z$',r'端口递推\\$Z=R+B\parallel2Z$'],r'圈出的余网拓扑不变，但每个阻抗都乘二')
 qq=np.linspace(0,8,120);zp=(3+1j*qq+np.sqrt(17-qq**2+14j*qq))/4;zm=(3+1j*qq-np.sqrt(17-qq**2+14j*qq))/4
 roots=r'\draw[arr] (0,0)--(6,0) node[right]{$\omega L/R$};\draw[arr] (0,-1.3)--(0,3.4) node[above]{$\operatorname{Re}Z/R$};\node[left] at (0,0){$0$};';roots+=plot(qq*.625,zp.real*1.2,'main,thick')+plot(qq*.625,zm.real*1.2,'accent,dashed')
 roots+=r'\node[note] at (2.5,-2.4){蓝线为物理解，红线为负实部的减号根\\横轴为零实部；减号根不是被动输入阻抗};'
 rr=abs(1-1/((3+1j+np.sqrt(16+14j))/4));decay=axes(6,3.7,'级数 $n$','$|U_n|/U_0$');nn=np.arange(8);decay+=plot(nn*.7,rr**nn*3,'accent,thick')+r'\node[note] at (2.5,-1.3){示例 $\omega L/R=1$；电压按 $|\rho|^n$ 衰减};'
 limits=flow([r'低频实部\\$(3+\sqrt{17})R/4$',r'低频感抗\\$\omega L(1+7/\sqrt{17})/4$',r'高频实部\\$5R/2$',r'高频感抗\\$\omega L/2$'],r'有限级反向递推与总耗散和可独立检查解析根')
 save('05',[circ,recursion,roots,decay,limits])
 mechanism=r'''\draw[main,thick] (0,0)--(3,5.196) node[above]{$C$};\draw[main,thick] (0,0)--(5,0);\draw[main,thick] (-1,4)--(2.3094,4);\draw[main,thick] (1.1547,2)--(4.6188,0);\fill (0,0) circle (3pt);\node[below] at (0,0){$O$};\fill[accent] (2.3094,4) circle (3pt);\node[right] at (2.3094,4){$B$};\fill[accent] (1.1547,2) circle (3pt);\node[left] at (1.1547,2){$D$};\node[below] at (4.6188,0){$E$};\draw[arr,accent] (-1,4.5)--(.2,4.5) node[midway,above]{$v$};\node[note] at (2,-1.3){$B$ 沿杆滑动；$D$ 是杆上固定点；$OD=BD$ 仅在图示瞬间};'''
 angular=flow([r'水平约束\\$x_B=b\cot\alpha$',r'一次微分\\$\dot\alpha=-v\sin^2\alpha/b$',r'二次微分\\$\ddot\alpha=2v^2\sin^3\alpha\cos\alpha/b^2$',r'图示方向\\顺时针、逆时针'],r'角速度与角加速度可以方向相反')
 vel=r'''\draw[arr,main,thick] (0,0)--(3,-1.732) node[midway,below]{$\mathbf v_D$};\draw[arr,accent,thick] (3,-1.732)--(4,0) node[midway,right]{$\mathbf v_E-\mathbf v_D$};\draw[arr,thick] (0,0)--(4,0) node[midway,above]{$\mathbf v_E$};\node[note] at (2,-3.2){速度分量按 $v/8$ 归一；相对速度垂直于 $DE$};'''
 acc=r'''\draw[arr,main,thick] (0,0)--(-3,-.577);\node[left] at (-3,-.577){$\mathbf a_D$};\draw[arr,accent,thick] (0,0)--(-3.111,0);\node[above] at (-1.7,0){$\mathbf a_E$ 向左};\node[note] at (-1.5,-2){二阶约束：$(\mathbf a_E-\mathbf a_D)\cdot\mathbf r_{ED}=-|\mathbf v_E-\mathbf v_D|^2$};'''
 con=flow([r'位置定尺寸\\$OD=b/\sqrt3$，$DE=b$',r'求导保常量\\$OD,DE$ 不变',r'输出坐标\\$x_E=d\cos\alpha+\sqrt{\ell^2-d^2\sin^2\alpha}$',r'独立检查\\$V_E=v/2$，$A_E<0$'],r'瞬时中点不能作为任意时刻的中点约束')
 save('06',[mechanism,angular,vel,acc,con])
 wedge=r'''\draw[main,very thick] (0,0)--(6,0);\draw[main,very thick] (0,0)--(3,5.196);\draw[dashed] (0,0)--(5.2,3);\fill[accent] (2.598,1.5) circle (3pt);\draw[arr,accent] (2.598,1.5)--(4.33,2.5) node[midway,above]{$v=u/3$};\node[left] at (0,0){$O$};\node[right] at (.8,.3){$60^\circ$};\node[note] at (2.5,-1.4){沿角平分线远离墙角；两墙一次回声互为镜像};'''
 img=r'''\draw[main,thick] (0,0)--(6,0);\fill[accent] (2.598,1.5) circle (3pt);\node[above] at (2.598,1.5){发射 $S$};\fill[main] (2.598,-1.5) circle (3pt);\node[below] at (2.598,-1.5){像点 $S'$};\fill[accent] (4.2,2.425) circle (3pt);\node[above] at (4.2,2.425){未来接收 $A$};\draw[dashed] (2.598,-1.5)--(4.2,2.425);\draw[accent,thick] (2.598,1.5)--(3.21,0)--(4.2,2.425);\node[note] at (2.5,-2.8){像点对应过去发射位置；实际回声路径在墙面折转};'''
 flight=flow([r'发射半径\\$r$',r'接收半径\\$r+vT$',r'镜像夹角\\$60^\circ$',r'余弦定理\\$(u^2-v^2)T^2$\\$-rvT-r^2=0$'],r'取正时间根；传播期间接收者仍继续向外运动')
 freq=r'''\draw[arr] (0,0)--(7,0);\draw[arr,main] (1,.4)--(1,2);\draw[arr,main] (2,.4)--(2,2);\draw[arr,accent] (4,.4)--(4,2);\draw[arr,accent] (5.4215,.4)--(5.4215,2);\draw[<->] (1,2.4)--(2,2.4) node[midway,above]{$\Delta t_e$};\draw[<->] (4,2.4)--(5.4215,2.4) node[midway,above]{$\Delta t_a$};\node[note] at (3,-1.2){$\Delta t_a=(1+\beta K_1)\Delta t_e$；$f_1/f_0=0.703465$};'''
 double=r'''\draw[main,thick] (0,0)--(4,0);\draw[main,thick] (0,0)--(2,3.464);\fill[accent] (2.598,1.5) circle (3pt);\fill[main] (-2.598,1.5) circle (3pt);\draw[dashed] (0,0)--(-2.598,1.5);\draw[dashed] (0,0)--(2.598,1.5);\draw[accent,thick] (-2.598,1.5)--(4,2.309);\node[note] at (1,-1.4){两次反射镜像方向差 $120^\circ$；$f_2/f_0=0.547066$\\$180^\circ$ 形式路径穿过顶点，须另行指定角点模型};'''
 save('07',[wedge,img,flight,freq,double])
 wheel=r'''\draw[main,thick] (0,2) circle (2);\fill (0,2) circle (2pt);\node[above right] at (0,2){$O$};\draw[accent,very thick] (0,2)--(-2,2);\draw[main,thick] (-3,-2)--(3,-2);\draw[arr,accent] (2,-2)--(.5,-2) node[midway,below]{$I$};\draw[<->] (2.5,-2)--(2.5,0) node[midway,right]{$R$};\draw[<->] (-2.7,-2)--(-2.7,2) node[midway,left]{$2R$};\draw[arr] (-.6,4.5) arc (110:70:2);\node[above] at (0,4.5){顺时针 $\omega$};\node[note] at (0,-3.4){导线到轮缘最低点间隙为 $R$，到轮心为 $2R$};'''
 field=r'''\draw[main,thick] (-3,0)--(3,0);\draw[arr,accent] (1,0)--(-1,0) node[midway,below]{$I$};\foreach \x in {-2,0,2}{\foreach \y in {1,2,3}{\node at (\x,\y){$\otimes$};}}\node[note] at (0,-1.5){导线上方磁场向纸内；$B=\mu_0I/(2\pi d)$};'''
 parallel=r'''\draw[main,very thick] (0,2)--(4,2);\draw[main] (-1,0)--(5,0);\node[below] at (0,2){$O$};\node[below] at (4,2){$P$};\draw[<->] (-.7,0)--(-.7,2) node[midway,left]{$2R$};\draw[arr,accent] (2,2)--(2,1) node[right]{$\mathbf v$};\node at (3,1){$\otimes\ \mathbf B$};\draw[arr] (2,2.3)--(3.5,2.3) node[above]{$\mathbf v\times\mathbf B$};\node[note] at (2,-1.5){磁场沿水平辐条恒定，速度随半径线性增加};'''
 radial=r'''\draw[main,very thick] (0,2)--(0,4);\draw[main] (-3,0)--(3,0);\node[right] at (0,2){$O$};\node[right] at (0,4){$P$};\draw[<->] (-.8,0)--(-.8,2) node[midway,left]{$2R$};\draw[<->] (-.8,2)--(-.8,4) node[midway,left]{$R$};\draw[arr,accent] (0,3)--(1,3) node[above]{$\mathbf v$};\draw[arr] (.3,2.8)--(.3,3.8);\node[note] at (0,-1.4){向上：导线距离为 $2R+r$，动生积分含自然对数};'''
 comp=r'''\draw[arr] (0,0)--(6,0);\foreach \x/\h/\lab in {1/1.89/向上,3/2.5/水平,5/3.86/向下}{\fill[main!20] (\x-.4,0) rectangle (\x+.4,\h);\draw[main] (\x-.4,0) rectangle (\x+.4,\h);\node[below] at (\x,0){\lab};}\node[note] at (3,-1.5){共同系数 $\mu_0I\omega R/(2\pi)$\\系数依次为 $0.189070$、$0.25$、$0.386294$};'''
 save('08',[wheel,field,parallel,radial,comp])
 p=ROOT/'scripts/render_figures.py';src=p.read_text();src=re.sub(r'^NAMES=.*$',f'NAMES={NAMES!r}',src,flags=re.M);p.write_text(src)
if __name__=='__main__':main()
