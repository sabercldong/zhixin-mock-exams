from pathlib import Path
import math,re
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
PRE=r'''\documentclass[multi=tikzpicture,border=9pt]{standalone}
\usepackage[UTF8]{ctex}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,patterns}
\definecolor{main}{HTML}{17365D}
\definecolor{accent}{HTML}{AC3931}
\tikzset{every picture/.style={font=\small,line width=.75pt},>={Stealth[length=2mm]},arr/.style={->},box/.style={draw=main,rounded corners=2pt,fill=main!4,text width=3.6cm,minimum height=1cm,align=center},note/.style={align=center,text width=9cm}}
\begin{document}
'''
NAMES={f'{i:02d}':[f'{n}-{i:02d}' for n in ['statement','geometry','method','derivation','check']] for i in range(1,9)}
def save(q,figs):
 assert len(figs)==5
 (ROOT/f'figures/题{q:02d}_图稿源文件.tex').write_text(PRE+''.join('\n\\begin{tikzpicture}\n'+s+'\n\\end{tikzpicture}\n' for s in figs)+'\\end{document}\n')
def plot(x,y,style='main,thick'):
 return '\\draw['+style+'] '+' -- '.join(f'({a:.5f},{b:.5f})' for a,b in zip(x,y))+';\n'
def axes(xlabel,ylabel,x=6,y=4):
 return f'\\draw[arr] (0,0)--({x},0) node[right]{{{xlabel}}};\\draw[arr] (0,0)--(0,{y}) node[above]{{{ylabel}}};\n'
def flow(labels,note):
 s=''
 for i,(x,y) in enumerate([(0,0),(5,0),(5,-2.3),(0,-2.3)]):s+=f'\\node[box] (n{i}) at ({x},{y}) {{{labels[i]}}};\n'
 return s+r'\draw[arr] (n0)--(n1);\draw[arr] (n1)--(n2);\draw[arr] (n2)--(n3);'+'\n'+r'\node[note] at (2.5,-4.1) {'+note+'};'
def circuit():
 return r'''\draw[main,thick] (0,0)--(0,1.25);\draw[main,thick] (0,1.65)--(0,3)--(1.5,3);\draw[main,thick] (-.35,1.65)--(.35,1.65);\draw[main,thick] (-.2,1.25)--(.2,1.25);\node[left] at (0,1.5){$U_0$};\draw[main,thick] (1.5,2.8) rectangle (2.5,3.2);\node[above] at (2,3.2){$R_1$};\draw[main,thick] (2.5,3)--(5,3);\fill (3.5,3) circle (2pt);\draw[main,thick] (5,2.8) rectangle (6,3.2);\node[above] at (5.5,3.2){$R_2$};\draw[main,thick] (6,3)--(7.5,3)--(7.5,1.7);\draw[main,thick] (3.5,3)--(3.5,1.7);\foreach \x/\lab in {3.5/C_1,7.5/C_2}{\draw[main,thick] (\x-.35,1.7)--(\x+.35,1.7);\draw[main,thick] (\x-.35,1.3)--(\x+.35,1.3);\draw[main,thick] (\x,1.3)--(\x,0);\node[right] at (\x+.4,1.5){$\lab$};}\draw[main,thick] (0,0)--(7.5,0);'''
def main():
 (ROOT/'figures').mkdir(parents=True,exist_ok=True)
 s=r'''\draw[arr] (-3,0)--(4,0) node[right]{$x$};\draw[arr] (0,-2.5)--(0,3) node[above]{$y$};\draw[main,dashed,thick] (0,0) circle (1.8);\foreach \x/\y in {-0.6/0.6,0.6/0.6,-0.6/-0.6,0.6/-0.6}{\node at (\x,\y){$\otimes$};}\node at (.9,.95){$j$};\node[above] at (-2.3,1.4){$I\otimes$};\fill[accent] (-2.3,1.4) circle (3pt);\draw[arr,accent] (-2.3,1.4)--(-1.25,.76);\draw[<->] (0,-2.1)--(1.8,-2.1) node[midway,below]{$r$};\node[note] at (.5,-3.3){同向电流吸引；导线横向受力指向圆心};'''
 x=np.linspace(0,4,160);f=np.where(x<=1,x,1/np.maximum(x,.001));g=axes(r'$\rho/r$',r'$F/(\kappa r)$')+plot(x*1.3,f*3)
 g+=r'\draw[dashed] (1.3,0)--(1.3,3);\node[below] at (1.3,0){$1$};\node[left] at (0,3){$1$};\node[note] at (2.7,-1.2){内区线性，外区反比；边界力连续};'
 m=flow([r'场与给定电流\\$F_{\rho}<0$',r'外区守恒\\$J=m\rho_0v_0$',r'最近点条件\\$U_{\rm eff}(r)\ge E$',r'速度下限\\$v_0\ge v_{0c}$'],r'总能量和角动量必须同时使用；等号触边')
 v=np.sqrt(2*np.log(2)/3);xs=np.linspace(.55,2.5,200);ue=np.where(xs<=1,.5*(xs**2-1),np.log(xs))+.5*(2*v)**2/xs**2
 d=axes(r'$\rho/r$',r'$U_{\rm eff}/(\kappa r^2)$')+plot(xs*2,ue*1.8)
 E=.5*v*v+np.log(2);d+=plot([1.1,5],[E*1.8,E*1.8],'accent,dashed')
 d+=r'\node[below] at (2,0){$1$};\node[below] at (4,0){$2$};\node[note] at (2.8,-1.2){临界轨道在两转折点 $r$ 与 $\rho_0=2r$ 之间};'
 t=np.linspace(0,np.pi/4,80);ch=r'''\draw[main,dashed] (0,0) circle (2);\draw[arr] (-2.6,0)--(2.8,0);\draw[arr] (0,-2.4)--(0,2.6);'''
 ch+=plot(2*(-np.cos(t)+np.sin(t)),2*np.sqrt(2)*np.sin(t),'accent,thick')
 ch+=r'\fill (-2,0) circle (2pt);\fill (0,2) circle (2pt);\draw[arr,accent] (-2,0)--(-1.5,.707);\node[above left] at (-2,0){$(-r,0)$};\node[above right] at (0,2){$(0,r)$};\node[note] at (0,-3.4){$v_1=\sqrt3\omega r$：$\alpha=54.7356^\circ$，$\omega t_e=\pi/4$};'
 save(1,[s,g,m,d,ch])
 s=r'''\draw[main,thick] (0,-2)--(0,2);\draw[main,thick] (3,-2)--(3,2);\draw[arr,main] (0,-1)--(0,1) node[left]{$+v_0$};\draw[arr,accent] (3,1)--(3,-1) node[right]{$-v_0$};\draw[<->] (0,2.4)--(3,2.4) node[midway,above]{$d$};\draw[arr] (4,0)--(6,0) node[midway,above]{$S':V$};\node[note] at (2.5,-3.2){示例：两空间轨迹平行，粒子沿相反方向运动};'''
 g=r'''\draw[arr] (0,0)--(4,0) node[right]{$x'$};\draw[arr] (0,-3)--(0,3) node[above]{$y'$};\draw[arr,main,thick] (0,0)--(-2,2) node[above]{$\mathbf u_1'$};\draw[arr,accent,thick] (0,0)--(-2,-2) node[below]{$\mathbf u_2'$};\draw ( -.35,.35)--(-.7,0)--(-.35,-.35);\node[note] at (.5,-4){$\theta=90^\circ$ 时，直角条件 $V=v_0/\sqrt{1+v_0^2/c^2}$};'''
 m=flow([r'反向速度\\$\mathbf u_2=-\mathbf u_1$',r'完整变换\\纵向与横向',r"欧氏内积\\$\mathbf u_1'\cdot\mathbf u_2'=0$",r'非退化检查\\$\sin\theta\ne0$'],r'同向同速的两粒子在所有惯性系仍有相同速度')
 th=np.linspace(0,np.pi/2,160);y=1/np.sqrt(1+.36*np.sin(th)**2);d=axes(r'$\theta$',r'$|V|/v_0$')+plot(th*3,y*3)
 d+=r'\node[left] at (0,3){$1$};\node[below] at (4.71,0){$\pi/2$};\node[note] at (2.8,-1.2){$v_0=0.6c$；$\theta=0$ 的形式极限含静止粒子，须排除};'
 ch=r'''\draw[main,thick] (-2,-2)--(2,2);\draw[accent,thick] (-2,2)--(2,-2);\fill (0,0) circle (3pt);\node[right] at (.3,0){空间交点};\node[main] at (-2.3,-2.6){经过时刻 $t_1'$};\node[accent] at (2.1,-2.6){经过时刻 $t_2'$};\node[note] at (0,-3.8){$t_2'-t_1'=d/(\gamma_VV)\ne0$；空间交点不是碰撞事件};'''
 save(2,[s,g,m,d,ch])
 c=1/np.sqrt(3);b=np.sqrt(2/3);x=.3;y=-b*np.sqrt(1-x*x)
 s=r'''\draw[main,thick] (-2.3094,0)--(1.2,-3.1155)--(2.3094,0);\fill (-2.3094,0) circle (2pt);\fill (2.3094,0) circle (2pt);\node[above] at (-2.3094,0){$A$};\node[above] at (2.3094,0){$B$};\draw[main] (1.2,-2.8655) circle (.25);\draw[arr] (1.2,-2.8655)--(1.2,-4.1) node[right]{$mg$};\draw[arr,accent] (1.2,-2.8655)--(2.4,-2.8655) node[above]{$x>0$};\draw[dashed] (0,.3)--(0,-3.5);\node[note] at (0,-5.1){$|AC|+|CB|=2a$；图中绳折点为小轮近似接触位置};'''
 g='';xx=np.linspace(-1,1,200);g+=plot(xx*4,-b*np.sqrt(1-xx*xx)*4,'gray!45')
 xx=np.linspace(-c,c,180);g+=plot(xx*4,-b*np.sqrt(1-xx*xx)*4,'main,thick')
 g+=r'\draw (-4,0)--(4,0);\fill (-2.3094,0) circle (2pt);\fill (2.3094,0) circle (2pt);\node[above] at (-2.3094,0){$-c_f$};\node[above] at (2.3094,0){$c_f$};\node[note] at (0,-4.7){蓝色：两侧正张力可平衡区；灰色：数学椭圆其他部分};'
 m=flow([r'总长不变\\椭圆折点',r'两力分量\\$T_1,T_2$',r'接触张力比\\$\ln(T_2/T_1)$',r'包角条件\\$\mu\phi\ge\ln(T_2/T_1)$'],r'驱动转矩 $r(T_1-T_2)$；右移时需顺时针驱动')
 xs=np.linspace(0,.56,160);ys=b*np.sqrt(1-xs*xs);d1=1+xs/np.sqrt(3);d2=1-xs/np.sqrt(3);T1=d1*(c-xs)/(2*c*ys);T2=d2*(c+xs)/(2*c*ys)
 d=axes(r'$x/a$',r'$T/(mg)$')+plot(xs*9,T1*3)+plot(xs*9,T2*3,'accent,thick')
 d+=r'\node[main] at (4,.6){$T_1$};\node[accent] at (4,3.3){$T_2$};\node[note] at (2.8,-1.2){最低点张力相等；右侧 $T_2>T_1$};'
 phi=np.arccos((c+xs)/d1)+np.arccos((c-xs)/d2);mus=np.log(T2/T1)/phi
 ch=axes(r'$x/a$',r'$\mu_{\min}$')+plot(xs*9,mus*1.7)
 ch+=r'\node[below] at (5.04,0){$0.56$};\node[note] at (2.8,-1.2){$x=0.3a$ 时 $\mu_{\min}=0.410127$；接近焦点时发散};'
 save(3,[s,g,m,d,ch])
 s=circuit()+r'\node[note] at (3.7,-1.4){原题 $R_1=R_2=R$，$C_1=C_2=C$；初态均无电荷};'
 g=circuit()+r'\draw[arr,accent] (.7,3.5)--(1.3,3.5) node[above]{$i_L$};\draw[arr,accent] (4.2,3.5)--(4.8,3.5) node[above]{$i_R$};\node[note] at (3.7,-1.4){左电流 $i_L=\dot q_1+\dot q_2$；右电流 $i_R=\dot q_2$};'
 m=flow([r'电源功\\$2CU_0^2$',r'末态储能\\$CU_0^2$',r'总热量\\$CU_0^2$',r'分支需瞬态\\方程乘 $\dot q_2$ 积分'],r'总热量由末态决定，分配不能仅看电阻是否相同')
 a=(3-np.sqrt(5))/2;bb=(3+np.sqrt(5))/2;t=np.linspace(0,10,200);u2=1-(bb*np.exp(-a*t)-a*np.exp(-bb*t))/(bb-a);u2p=(np.exp(-a*t)-np.exp(-bb*t))/(bb-a);u1=u2+u2p
 d=axes(r'$t/(RC)$',r'$V_i/U_0$')+plot(t*.5,u1*3)+plot(t*.5,u2*3,'accent,thick')
 d+=r'\node[left] at (0,3){$1$};\node[main] at (2,2.85){节点1};\node[accent] at (3,2.25){节点2};\node[note] at (2.8,-1.2){两个衰减模式；节点1先升压，右支初电流为零};'
 ch=r'''\draw[arr] (0,0)--(6,0);\fill[main!25] (.6,0) rectangle (2,3.3333);\draw[main] (.6,0) rectangle (2,3.3333);\fill[accent!25] (3.3,0) rectangle (4.7,.6667);\draw[accent] (3.3,0) rectangle (4.7,.6667);\node[above] at (1.3,3.3333){$5/6$};\node[above] at (4,.6667){$1/6$};\node[below] at (1.3,0){左电阻};\node[below] at (4,0){右电阻};\node[note] at (2.8,-1.4){单位 $CU_0^2$；独立瞬态积分恢复 $5:1$};'''
 save(4,[s,g,m,d,ch])
 d12=3**(-1/3);d13=2**(-1/3);x3=(d12*d12+d13*d13-1)/(2*d12);y3=np.sqrt(d13*d13-x3*x3);pts=np.array([[0,0],[d12,0],[x3,y3]])*5
 s=plot([pts[0,0],pts[1,0],pts[2,0],pts[0,0]],[pts[0,1],pts[1,1],pts[2,1],pts[0,1]])
 for i,(x,y) in enumerate(pts):s+=f'\\fill[accent] ({x},{y}) circle (3pt);\\node[above left] at ({x},{y}){{$Q_{i+1},m_{i+1}$}};\n'
 s+=r'\node[note] at (1.6,-1.4){对边比 $d_{23}:d_{31}:d_{12}=1:2^{-1/3}:3^{-1/3}$};'
 cm=pts.mean(axis=0);g=s.split(r'\node[note]')[0]+f'\\fill ({cm[0]},{cm[1]}) circle (2pt);\\node[right] at ({cm[0]},{cm[1]}){{$O$}};'
 for x,y in pts:
  xx=cm[0]+1.35*(x-cm[0]);yy=cm[1]+1.35*(y-cm[1]);g+=f'\\draw[arr,accent] ({x},{y})--({xx},{yy});\n'
 g+=r'\node[note] at (1.5,-1.6){示意取等质量：加速度沿质量质心径向向外；电荷比 $1:2:3$};'
 m=flow([r'质量质心\\$\sum m_i\mathbf r_i=0$',r'横向系数消去\\非共线基独立',r'构型条件\\$\eta_i d_{jk}^3=\Gamma$',r'全过程\\$\ddot s=A/s^2$'],r'另有任意共线初态分支，不要求上述非共线边长比')
 d=''
 for scale,sty in [(1,'gray!60'),(1.5,'main'),(2,'accent')]:
  p=cm+(pts-cm)*scale;d+=plot([p[0,0],p[1,0],p[2,0],p[0,0]],[p[0,1],p[1,1],p[2,1],p[0,1]],sty)
 d+=r'\node[note] at (1.5,-2.3){相同边长比，不同尺度；无整体旋转，各粒子沿固定射线};'
 x=np.linspace(1,5,140);ch=axes(r'$s$',r'$\dot s/\sqrt{2A}$')+plot((x-1)*1.2,np.sqrt(1-1/x)*3)
 ch+=r'\node[below] at (0,0){$1$};\node[below] at (4.8,0){$5$};\node[left] at (0,3){$1$};\node[note] at (2.7,-1.3){膨胀由静止开始，逐渐趋于恒定尺度速度；不是初始匀速};'
 save(5,[s,g,m,d,ch])
 s=r'''\draw[main,thick] (-3,0)--(3,0);\fill (0,0) circle (2pt);\node[above right] at (.2,.1){孔 $O$};\draw[main,thick] (-2,0)--(0,0)--(0,-2.7);\fill[accent] (-2,0) circle (4pt);\node[above] at (-2,0){$A:m$};\fill[accent] (0,-2.7) circle (4pt);\node[right] at (0,-2.7){$B:\lambda m$};\draw[arr] (-2,0)--(-2,1) node[left]{$\omega_0l_0$};\draw[<->] (-2,-.4)--(0,-.4) node[midway,below]{$l_0$};\node[note] at (0,-4){初态 $\lambda g=\omega_0^2l_0$，下球静止};'''
 g=r'''\draw[main,thick] (-3,0)--(3,0);\draw[main,thick] (-1.5,0)--(0,0)--(0,-3);\fill[accent] (-1.5,0) circle (3pt);\fill[accent] (0,-3) circle (4pt);\node[right] at (0,-3){$3\lambda m$};\draw[arr,accent] (1,-1.7)--(1,-2.8) node[right]{下降};\draw[arr] (-1.5,.4)--(-.7,.4) node[above]{$\rho$ 减小};\node[note] at (0,-4.3){新增重物：旧转轴 $O$ 不变，角动量守恒，切向速度增大};'''
 m=flow([r'原平衡\\$\lambda g=\omega_0^2l_0$',r'守恒轴区分\\$J_O$ 或 $J_P$',r'完整能量\\两球径向动能',r'转折点\\径向速度同时为零'],r'最大位移可精确求；大质量近似主要影响时间尺度')
 d=r'''\draw[main,thick] (-3,0)--(2,0);\draw[main,thick] (-2.5,0)--(-1.25,0)--(0,0)--(0,-2.5);\fill (0,0) circle (3pt);\node[above] at (0,0){$O$};\fill[main] (-1.25,0) circle (3pt);\node[below] at (-1.25,0){钉子 $P$};\fill[accent] (-2.5,0) circle (4pt);\node[above] at (-2.5,0){$A$};\draw[arr] (-2.5,0)--(-2.5,1.3) node[left]{$v_t$ 不变};\draw[main,dashed] (-1.25,0) circle (1.25);\fill[accent] (0,-2.5) circle (4pt);\draw[arr,accent] (.7,-2.5)--(.7,-1.3) node[right]{先向上};\node[note] at (-.8,-4){新半径 $R_0=l_0/2$，新角动量 $J_P=m v_tR_0$};'''
 x=np.linspace(.3,1.5,160);ch=axes(r'$\rho/l_0$ 或 $R/l_0$',r'$U_{\rm eff}$',6,6)
 ch+=plot(x*3,(.5/x**2+3*x)*.8)+plot(x*3,(.125/x**2+x)*2,'accent,thick')
 ch+=r'\node[main] at (3.7,4.8){新增质量};\node[accent] at (4.2,2.4){钉子支点};\node[note] at (2.8,-1.2){蓝：最近半径 $l_0/2$；红：最大上升 $(\sqrt5-1)l_0/4$\\两曲线仅示各自有效势形状，归一化系数不同};'
 save(6,[s,g,m,d,ch])
 s=r'''\draw[dashed] (-2,0)--(8,0);\foreach \x/\lab in {0/L_1,5/L_2}{\draw[main,<->,thick] (\x,-1.5)--(\x,1.5);\node[above] at (\x,1.5){$\lab$};}\fill[accent] (-2,0) circle (3pt);\node[below] at (-2,0){点源};\draw[<->] (0,2.2)--(5,2.2) node[midway,above]{$L=25\,\mathrm{cm}$};\draw[<->] (-2,-2)--(0,-2) node[midway,below]{$l_1=10\,\mathrm{cm}$};\draw[<->] (5,-2)--(6,-2) node[midway,below]{$l_2=5\,\mathrm{cm}$};\node[note] at (3,-3.4){第一束右侧平行；第二束由左侧平行入射并聚焦};'''
 g=r'''\draw[dashed] (-3,0)--(7,0);\draw[main,<->,thick] (0,-1.2)--(0,1.2);\draw[main,<->,thick] (5,-1.2)--(5,1.2);\fill (-2,0) circle (2pt);\foreach \h in {1,-1}{\draw[accent,thick] (-2,0)--(0,\h)--(4.2,0)--(5,-.1905*\h)--(7,-.1905*\h);}\node[above] at (2.5,1.5){短焦距组};\node[note] at (2,-2.5){第一束在两镜间形成实际交叉点；$L-f_2>0$};'''
 m=flow([r'第一项观测\\$D+l_1C=0$',r'第二项观测\\$A+l_2C=0$',r'矩阵行列式\\$AD-LC=1$',r'二次反演\\$l_1l_2C^2-LC-1=0$'],r'两个 $C$ 根都需回代；本题两个焦距组合均为正')
 d=r'''\draw[dashed] (-3.5,0)--(7,0);\draw[main,<->,thick] (0,-1.2)--(0,1.2);\draw[main,<->,thick] (5,-1.2)--(5,1.2);\foreach \h in {1,-1}{\draw[accent,thick] (-3,\h)--(0,\h)--(5,.1861*\h)--(6,0);\draw[accent,dashed] (5,.1861*\h)--(6.1436,0);}\node[above] at (2,1.6){长焦距组};\node[note] at (2,-2.5){第二镜收到会聚光；虚物在右侧，物距 $L-f_1<0$};'''
 ch=r'''\node[box] at (0,0){短焦距组\\$(6.782161,3.923242)$ cm\\$f_{\rm sys}=-1.861407$ cm};\node[box] at (5,0){长焦距组\\$(30.717839,39.826758)$ cm\\$f_{\rm sys}=26.861407$ cm};\node[note] at (2.5,-2.4){两组均满足外部观测；可增加“镜间是否实际交叉”选解};'''
 save(7,[s,g,m,d,ch])
 s=r'''\draw[main,thick] (0,0) circle (2);\fill[accent] (0,0) circle (3pt);\node[below] at (0,0){核 $+q$};\fill[main] (2,0) circle (3pt);\node[right] at (2,0){电子 $-q$};\draw[arr,accent] (2,0)--(2,1.2) node[right]{$\mathbf v$};\draw[dashed] (0,0)--(2,0) node[midway,below]{$r_0$};\node at (-.7,.7){$B_0\otimes$};\node[note] at (0,-3.3){电子逆时针，等效电流顺时针，核处自生磁场向纸内};'''
 g=r'''\draw[main,thick] (0,0) circle (2);\draw[dashed] (0,0)--(2,0);\fill (2,0) circle (3pt);\draw[arr,main] (2,0)--(3.2,0) node[right]{$\dot r$};\draw[arr,accent] (2,0)--(2,1.4) node[right]{$F_\varphi=qB\dot r$};\node at (0,.35){$B\odot$};\node[note] at (0,-3.2){外场向纸外，径向速度产生切向磁力；$\dot L_z=qBr\dot r$};'''
 m=flow([r'有向机械量\\$L_z=mr^2\dot\varphi$',r'轴向守恒量\\$J=L_z-qBr^2/2$',r'展开动能\\保留 $qBJ/(2m)$',r'能级到一阶\\$E_{n,s}=E_n^0+sn\mu_BB$'],r'求半径时常量项导数为零，求能量时不能删除')
 d=r'''\draw[main,thick] (0,0)--(2,0) node[right]{$E_1^{(0)}$};\draw[main,thick] (0,3)--(2,3) node[right]{$E_2^{(0)}$};\draw[accent,thick] (4,-.25)--(6,-.25);\draw[accent,thick] (4,.25)--(6,.25);\draw[accent,thick] (4,2.5)--(6,2.5);\draw[accent,thick] (4,3.5)--(6,3.5);\draw[arr] (4.5,3.5)--(4.5,.25);\draw[arr] (5.5,2.5)--(5.5,-.25);\node[below] at (1,-.8){无场};\node[below] at (5,-.8){弱场示意};\node[note] at (3,-2){教学圆轨道模型的同绕行方向分支\\$\Delta\nu=\pm\mu_B B/h$；分裂尺度夸大以示意};'''
 ch=r'''\node[box] at (0,0){半径方程\\$J^2=mk r+q^2B^2r^4/4$\\首修正为 $B^2$};\node[box] at (5,0){能量展开\\$qBJ/(2m)$\\已有 $B$ 的首修正};\node[note] at (2.5,-2.5){半径无一阶变化，不等于光谱无一阶变化；保持近似精度一致};'''
 save(8,[s,g,m,d,ch])
 p=ROOT/'scripts/render_figures.py';p.write_text(re.sub(r'^NAMES=.*$',f'NAMES={NAMES!r}',p.read_text(),flags=re.M))
if __name__=='__main__':main()
