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
GROUPS={'01':['question','compression','shear','hyperbola','dipole'],'02':['question','parameters','range','anomaly','check'],'03':['question','impulse','relative','steps','check'],'04':['question','metric','hessian','ellipse','check'],'05':['question','branches','dispersion','power','check'],'06':['question','restframe','sunframe','spiral','check'],'07':['question','flow','energy','comparison','check'],'08':['question','laplacian','symmetry','emf','leads']}
NAMES={q:[f'{n}-{q}' for n in ns] for q,ns in GROUPS.items()}
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
 # 两网格的相位差产生莫尔带；图中细纹仅作有限窗口示意。
 grid=''
 for x in np.arange(0,5.01,.25):grid+=f'\\draw[main] ({x:.3f},0)--({x:.3f},3);\n'
 for x in np.arange(-.5,5.01,.25):grid+=f'\\draw[accent!65] ({x:.3f},0)--({x+.45:.3f},3);\n'
 grid+=r'\node[note] at (2.5,-1){蓝色参考纹与红色受力纹；亮暗带取决于相位差累积};'
 compression=r'''\draw[main,thick] (0,0) rectangle (2,3);\draw[accent,thick] (4,0) rectangle (6,2.5);
\foreach \y in {0,.5,1,1.5,2,2.5,3}{\draw[main] (0,\y)--(2,\y);}
\foreach \y in {0,.4167,.8333,1.25,1.6667,2.0833,2.5}{\draw[accent] (4,\y)--(6,\y);}
\draw[arr,accent] (5,3.5)--(5,2.7) node[pos=0,above]{$\Delta p$};
\draw[<->] (-.5,0)--(-.5,3) node[midway,left]{$D$};\draw[<->] (6.5,0)--(6.5,2.5) node[midway,right]{$D-\Delta D$};
\node[above] at (1,3.3){初始 $h$};\node[above] at (5,3.8){受压 $h'=(1-\varepsilon)h$};
\node[note] at (3,-1.2){$\lambda=h(1-\varepsilon)/\varepsilon$；图中应变已放大};'''
 shear=r'''\draw[main,dashed] (0,0) rectangle (4,3);\draw[accent,thick] (0,0)--(4,0)--(5,3)--(1,3)--cycle;
\foreach \x in {.5,1,1.5,2,2.5,3,3.5}{\draw[main!55] (\x,0)--(\x,3);\draw[accent] (\x,0)--(\x+1,3);}
\draw[<->] (0,3.6)--(1,3.6) node[midway,above]{$d$};\draw[<->] (-.6,0)--(-.6,3) node[midway,left]{$H$};
\node[note] at (2.5,-1.3){$u_x(z)=\gamma z$，$\gamma=d/H=\tan\theta$；$\gamma\lambda=h$};'''
 hyp=r'\fill[accent] (-1.5,0) circle (2pt);\fill[accent] (1.5,0) circle (2pt);\node[below] at (-1.5,0){$-\Delta/2$};\node[below] at (1.5,0){$\Delta/2$};\draw[dashed] (-3.5,0)--(3.5,0);'
 for aa in [.3,.7,1.1]:
  yy=np.linspace(-2,2,100);xx=aa*np.sqrt(1+yy*yy/(2.25-aa*aa));hyp+=plot(xx,yy)+plot(-xx,yy)
 hyp+=r'\draw[accent,thick] (0,-2.2)--(0,2.2);\node[note] at (0,-3){$r_--r_+=kr$；中心线为 $k=0$，双曲线需按符号选支};'
 dip=r'\fill[accent] (-1.5,0) circle (2pt);\fill[main] (1.5,0) circle (2pt);\node[below] at (-1.5,0){$+$};\node[below] at (1.5,0){$-$};'
 for d in [np.pi/3,np.pi/2,2*np.pi/3]:
  cy=1.5/np.tan(d);rr=1.5/np.sin(d);angles=np.linspace(np.arctan2(-cy,1.5),np.pi-np.arctan2(-cy,1.5),100)
  dip+=plot(rr*np.cos(angles),cy+rr*np.sin(angles))
 dip+=r'\draw[dashed] (-3,0)--(3,0);\node[note] at (0,-1.8){恒定有向角差的圆弧；等量异号无限长线电荷的电场线};'
 save('01',[grid,compression,shear,hyp,dip])
 s=3200**2/(9.8*6.37e6);a=1/(2-s);e=np.sqrt(1-s);psi=2*np.arcsin(s/(2-s))
 orb=r'\draw[main,thick] (0,0) circle (1.7);\fill (0,0) circle (2pt);\node[right] at (0,0){地心 $O$};'
 t=np.linspace(0,2*np.pi,200);orb+=plot(1.7*a*(np.cos(t)-e),1.7*a*np.sqrt(1-e*e)*np.sin(t),'gray!60,dashed')
 f=np.linspace(np.pi-psi/2,np.pi+psi/2,80);rr=1.7*s/(2-s)/(1+e*np.cos(f));orb+=plot(rr*np.cos(f),rr*np.sin(f),'accent,very thick')
 orb+=r'''\draw[arr] (-3,1)--(-1.66,.15);\node[above] at (-3,1){发射点};\draw[arr] (-3,-1)--(-1.66,-.15);\node[below] at (-3,-1){首次落地};\node[note] at (0,-2.7){椭圆虚线为数学延长；只取地表以上的红色轨道段};'''
 params=flow([r'固定初速\\$s=v_0^2/(gR)$',r'固定半长轴\\$a=R/(2-s)$',r'改变仰角\\$x=\cos^2\alpha$',r'改变偏心率\\$e^2=1-s(2-s)x$'],r'经纬度只定位发射点；球对称且无自转时，方位角任意')
 al=np.linspace(0,np.pi/2,150);xx=np.cos(al)**2;ps=2*np.arctan2(s*np.sqrt(xx*(1-xx)),1-s*xx)
 ran=axes(6,3.5,r'$\alpha/\mathrm{deg}$',r'$\Psi/\mathrm{deg}$');ran+=plot(np.degrees(al)/18,np.degrees(ps)/4)
 opt=np.degrees(np.arctan(e));ran+=f'\\fill[accent] ({opt/18:.4f},{np.degrees(psi)/4:.4f}) circle (2pt);\n'
 ran+=r'\node[above] at (2.36,2.7){$42.437^\circ$};\node[below] at (5,0){$90$};\node[note] at (2.5,-1.2){唯一内部最大值；两端中心角均为零};'
 ano=r'''\draw[main,thick] (0,0) ellipse (3 and 1.6);\fill[accent] (-2.538,0) circle (2pt);\node[below right] at (-2.538,-.3){地心焦点};\draw[dashed] (0,0) circle (3);
\draw[accent,thick] (-2.3,1.03)--(-2.538,0)--(-2.3,-1.03);\node[left] at (-3,0){远点};\node[right] at (2.9,1.1){辅助圆};\node[note] at (0,-4){偏近点角区间 $[\pi-\eta,\pi+\eta]$\\焦点扫面积含 $\eta+e\sin\eta$；本图为参数示意};'''
 save('02',[orb,params,ran,ano,flow([r'最佳角\\$\alpha_*=42.437^\circ$',r'最大中心角\\$\Psi=10.2518^\circ$',r'开普勒时间\\$t_f=510.30\,\mathrm s$',r'独立检查\\首次回到 $r=R$'],r'平抛极限：$\alpha_*\to45^\circ$，$t_f\to\sqrt2v_0/g$')])
 bounce=r'''\draw[main,thick] (0,0) rectangle (6,.2);\node[below] at (3,0){木板质量 $m$，长度 $l$};\draw[main,thick] (-.2,3) rectangle (.2,3.4);\draw[arr,accent] (.3,3.2)--(1.6,3.2) node[midway,above]{$v_0$};\draw[<->] (-.8,.2)--(-.8,3.2) node[midway,left]{$h$};\draw[dashed] (0,3.2)..controls (1.2,3.2) and(2.2,2)..(2.8,.2);\node[right] at (4,2){$\mu=1/2$};\node[note] at (3,-1.2){首次飞行 $t_0$；以后竖直反弹间隔 $2t_0$};'''
 imp=flow([r'竖直冲量\\$J_N=2mu$',r'切向上限\\$J_T\le2\mu mu$',r'实际切向冲量\\$\min(2\mu mu,mw/2)$',r'速度差更新\\$w_{\rm after}=\max(w-4\mu u,0)$'],r'共速时截断最大摩擦冲量，不能继续造成人为反向')
 rel=axes(6,4,'$j$','$w_j$');j=np.arange(4);rel+=plot(j*1.4,np.array([10,6,2,0])*.3,'accent,thick');
 for x,y in zip(j*1.4,np.array([10,6,2,0])*.3):rel+=f'\\fill[accent] ({x},{y}) circle (2pt);\n'
 rel+=r'\node[below] at (4.2,0){$3$};\node[left] at (0,3){$10$};\node[note] at (2.5,-1.2){示例 $u=2$、$v_0=10$：速度差 $10,6,2,0$};'
 steps=axes(6,4,'碰撞次数','$s$');steps+=plot([0,1.5,3,4.5],[0,1.2,2.64,3.12],'main,thick')+r'''\node[above] at (1.5,1.2){$2.0$};\node[above] at (3,2.64){$4.4$};\node[above] at (4.5,3.12){$5.2$};\node[below] at (1.5,0){$1$};\node[below] at (3,0){$2$};\node[below] at (4.5,0){$3$};\node[note] at (2.5,-1.2){先计初次路程，再累加 $w_j(2u/g)$；停滑后相对位置固定};'''
 save('03',[bounce,imp,rel,steps,flow([r'初次路程\\$s_0=v_0u/g$',r'后续速度差\\$w_j=(v_0-2ju)_+$',r'有限等差和\\$N=\lceil v_0/(2u)\rceil$',r'长度条件\\$l\ge s_{\max}$'],r'例 $g=10,h=.2,v_0=10$ 得 $l\ge5.20\,\mathrm m$')])
 tri=r'''\draw[main,thick] (0,3)--(-2.598,-1.5)--(2.598,-1.5)--cycle;
\foreach \x/\y/\lab in {0/3/A,-2.598/-1.5/B,2.598/-1.5/C}{\fill (\x,\y) circle (2pt);\node[above] at (\x,\y){$\lab$};\draw[dashed] (0,0)--(\x,\y);}
\fill[accent] (.6,.8) circle (3pt);\node[right] at (.6,.8){$M$};\fill (0,0) circle (2pt);\node[left] at (0,0){$O$};\draw[arr,accent] (0,0)--(.6,.8);\node[left] at (.1,.6){$\mathbf q$};\node[below] at (0,-1.6){$L$};\node[note] at (0,-2.8){每孔桌下悬挂质量 $m$；$OA=L/\sqrt3$};'''
 met=flow([r'绳长约束\\$h_i=\ell_i-r_i$',r'速度投影\\$\dot r_i=-\mathbf n_i\cdot\dot{\mathbf q}$',r'投影平方和\\$\sum\dot r_i^2=3|\dot{\mathbf q}|^2/2$',r'有效质量\\$M_*=M+3m/2$'],r'约束消去自由度，但不消去悬挂物的动能')
 hes=r'\draw[arr] (0,0)--(6,0) node[right]{$q$};\draw[arr] (2.6,0)--(2.6,4) node[above]{$U-U_0$};\node[below] at (2.6,0){$0$};';xx=np.linspace(-2,2,90);hes+=plot(xx+2.6,xx**2*.7)+r'\node[note] at (2.5,-1.2){二阶势能 $k_*|\mathbf q|^2/2$；两个方向的Hessian相同};'
 ell=r'\draw[arr] (-2.5,0)--(2.8,0) node[right]{$x$};\draw[arr] (0,-1.5)--(0,1.8) node[above]{$y$};'
 tt=np.linspace(0,2*np.pi,180);ell+=plot(2*np.cos(tt),1.1*np.sin(tt))+r'\draw[arr,accent] (2,0)--(2,.65) node[right]{$v_0$};\node[note] at (0,-2.5){$x=\Delta x\cos\omega t$，$y=(v_0/\omega)\sin\omega t$\\原点位于椭圆中心，初速度沿 $y$ 方向};'
 save('04',[tri,met,hes,ell,flow([r'回复系数\\$k_*=3\sqrt3mg/(2L)$',r'线性惯量\\$M_*=M+3m/2$',r'共同频率\\$\omega^2=k_*/M_*$',r'绳绷紧检查\\$\omega^2q_{\max}<g$'],r'二维等频只在小振幅线性模型中成立')])
 circ=r'''\draw (0,0)--(7,0);\node[left] at (0,0){地};\draw (0,0)--(0,3);\node[left] at (0,3){$U_0$};'''
 for j in range(3):
  x=j*2
  circ+=f'\\draw ( {x},3)--({x+.25},3);\\draw[decorate,decoration={{coil,aspect=.5,segment length=4pt,amplitude=3pt}}] ({x+.25},3)--({x+1.6},3);\\draw ({x+1.6},3)--({x+2},3);\n'
  circ+=f'\\draw ({x+2},3)--({x+2},1.6);\\draw[thick] ({x+1.7},1.6)--({x+2.3},1.6);\\draw[thick] ({x+1.7},1.35)--({x+2.3},1.35);\\draw ({x+2},1.35)--({x+2},0);\n'
  circ+=f'\\node[above] at ({x+1},3.2){{$L$}};\\node[right] at ({x+2.3},1.5){{$C$}};\\fill ({x+2},3) circle (2pt);\\node[above] at ({x+2},3.25){{$U_{j+1}$}};\n'
 circ+=r'\draw (6,3)--(7,3) node[right]{$\cdots$};\node[note] at (3.5,-1.2){源端记节点0；节点 $n$ 右边仍是一整节输入阻抗 $Z$};'
 branch=flow([r'自相似方程\\$Z^2-i\omega LZ-L/C=0$',r'通带选支\\$\operatorname{Re}Z>0$',r'阻带选支\\$|\rho|<1$',r'辐射边界\\无穷远无入射波'],r'形式二次根必须以被动性与空间有界性选择')
 kd=np.linspace(0,np.pi,100);disp=axes(6,4,'$k$',r'$\omega\sqrt{LC}$');disp+=plot(kd*1.6,2*np.sin(kd/2)*1.5)
 disp+=r'\node[below] at (5.027,0){$\pi$};\node[left] at (0,3){$2$};\draw[dashed] (0,3)--(5.4,3);\node[note] at (2.5,-1.2){$\omega\sqrt{LC}=2\sin(k/2)$；带边群速度趋零};'
 tt=np.linspace(0,2*np.pi,150);powfig=r'\draw[arr] (0,1.4)--(7,1.4) node[right]{$\omega t$};\draw[arr] (0,0)--(0,4) node[above]{$P_n$};';pp=np.cos(tt)*np.cos(tt-np.pi/6);powfig+=plot(tt,pp*2+1.4,'accent,thick')+r'\draw[dashed] (0,1.4)--(6.3,1.4);\node[left] at (0,1.4){$0$};\node[note] at (3,-1.2){示例 $k=\pi/3$、$n=0$；瞬时可反向，平均仍为正};'
 save('05',[circ,branch,disp,powfig,flow([r'电压传播\\$U_n=U_0\cos(\omega t-nk)$',r'电流半节延迟\\$I_n\propto\cos(\omega t-nk-k/2)$',r'每节储能\\$\overline{\mathcal W}=CU_0^2/2$',r'平均功率\\$\overline P=\overline{\mathcal W}v_g/a_0$'],r'阻带纯无功、平均功率零；带边形式解不能视为有限储能')])
 dust=r'''\fill[accent!40] (0,0) circle (.65);\node at (0,0){太阳};\draw[main,dashed] (0,0) circle (2.6);\fill[main] (2.6,0) circle (3pt);\node[right] at (2.8,0){灰尘};\draw[arr,accent] (2.6,0)--(2.6,1.2) node[right]{$v$};\draw[arr,main] (.8,0)--(2.3,0) node[midway,above]{光};\node[note] at (0,-3.6){吸收截面 $\pi r_d^2$；热平衡再辐射保持近似恒定质量};'''
 rest=r'''\fill[main] (0,0) circle (3pt);\draw[arr,accent] (-3,.7)--(-.3,.05) node[midway,above]{入射光};\draw[arr] (0,0)--(0,1.6) node[above]{$\hat t$};\draw[arr,accent] (0,0)--(0,-1.2) node[below]{切向阻力};\foreach \th in {0,45,90,135,180,225,270,315}{\draw[arr,main!60] (\th:.35)--(\th:1.1);}\node[note] at (0,-2.5){灰尘静止系：光行差角 $v/c$，出射总动量零};'''
 sun=flow([r'径向吸收\\切向入射动量零',r'静止系再辐射\\$\mathbf p_{\rm rest}=0$',r'低速变换\\$\dot{\mathbf p}_{\rm em}=P\mathbf v/c^2$',r'太阳系阻力\\$f_2=Pv/c^2=f_1$'],r'两个参考系在描述同一个净力，不叠加为双倍')
 spir=axes(6,4,r'$t/(R_0^2/2A)$','归一化值');tt=np.linspace(0,.95,100);spir+=plot(tt*5,np.sqrt(1-tt)*3,'accent,thick')+plot(tt*5,(1-tt)*3,'main,dashed')
 spir+=r'\node[right] at (4.5,2){实线 $R/R_0$};\node[right] at (5.3,1){虚线 $R^2/R_0^2$};\node[note] at (2.5,-1.2){$R^2=R_0^2-2A_{\rm PR}t$；半径本身非线性下降};'
 save('06',[dust,rest,sun,spir,flow([r'阻力\\$f=Pv/c^2$',r'圆轨道能量\\$E=-\mu_{\rm eff}m_d/(2R)$',r'收缩率\\$\dot R=-L_sr_d^2/(2m_dc^2R)$',r'适用检查\\$v/c\ll1,\ |\dot R|/v\ll1$'],r'若 $\beta_{\rm rad}\ge1$，束缚近圆轨道假设不成立')])
 vessel=r'''\draw[main,thick] (0,0) rectangle (7,2.6);\draw[very thick] (3.5,0)--(3.5,1.1);\draw[very thick] (3.5,1.5)--(3.5,2.6);\draw[very thick] (6.5,0)--(6.5,2.6);\draw (6.5,1.3)--(8,1.3);\draw[arr,accent] (8,1.3)--(7.1,1.3) node[pos=0,above]{$2p_0S$};\node at (1.7,1.6){左腔 $V_0$};\node at (1.7,.8){$p_0,T_0$};\node at (5,1.6){右腔 $V_0$};\node at (5,.8){$2p_0,T_0$};\draw[arr,accent] (4.1,1.3)--(2.9,1.3);\node[note] at (3.5,-1.2){固定绝热带孔隔板，右活塞慢移；有物质流动就有入口焓};'''
 fl=flow([r'右腔恒压出流\\$dU_R=-p\,dV_R+C_PT_Rdn_R$',r'右温保持\\$T_R=T_0$',r'左腔固定体积填充\\$dU_L=C_PT_0d\nu$',r'压力平衡\\$\nu_f=n_0/\gamma$'],r'整体相加时入口与出口焓相消，只剩外界活塞功')
 en=flow([r'初始内能\\$U_i=3(C_V/\mathcal R)p_0V_0$',r'外界正功\\$W=2p_0(1-\alpha)V_0$',r'末内能\\$U_f=2(C_V/\mathcal R)p_0V_0(1+\alpha)$',r'终体积比例\\$\alpha=1-1/(2\gamma)$'],r'不得把未知比热直接代成 $\alpha=3/4$')
 nu=np.linspace(0,1/1.4,90);comp=axes(6,4,r'$\nu/n_0$',r'$T/T_0$');comp+=plot(nu*6,(1+1.4*nu)/(1+nu)*2,'accent,thick')+plot(nu*6,np.ones_like(nu)*2,'main,dashed')
 comp+=r'\node[right] at (4.3,2.5){左温};\node[right] at (4.3,1.8){右温};\node[left] at (0,2){$1$};\node[note] at (2.5,-1.2){示例 $\gamma=7/5$；末左温 $7T_0/6$，右温 $T_0$};'
 save('07',[vessel,fl,en,comp,flow([r'一般终值\\$T_L=2\gamma T_0/(\gamma+1)$',r'右腔终值\\$T_R=T_0$',r'总量守恒\\$n_L+n_R=3n_0$',r'全局能量\\$\Delta U=W_{\rm in}$'],r'压力均衡终点与更长时间的共同温度要分开')])
 import itertools
 vs=sorted(set(itertools.permutations((1,1,0)))|set(itertools.permutations((1,-1,0)))|set(itertools.permutations((-1,-1,0))))
 es=[(i,j) for i in range(12) for j in range(i+1,12) if sum((vs[i][k]-vs[j][k])**2 for k in range(3))==2]
 xy=[(1.5*(x+.55*y),1.5*(z+.35*y)) for x,y,z in vs];net=''
 for i,j in es:net+=plot([xy[i][0],xy[j][0]],[xy[i][1],xy[j][1]],'main')
 for i,(x,y) in enumerate(xy):net+=f'\\fill ({x},{y}) circle (2pt);\n'
 for v,lab,anchor in [((1,0,1),'A','above'),((0,1,1),'B','above right'),((1,0,-1),'C','below')]:
  x,y=xy[vs.index(v)];net+=f'\\fill[accent] ({x},{y}) circle (3pt);\\node[{anchor}] at ({x},{y}){{$ {lab} $}};\n'
 net+=r'\node[note] at (0,-3){立方八面体：12顶点、24棱、14面；每棱1欧\\线段为三维网络投影，投影交叉处不新增节点};'
 lap=flow([r'坐标生成邻接\\$|\mathbf v_i-\mathbf v_j|^2=2$',r'每点度数4\\$L_{ii}=4,\ L_{ij}=-1$',r'试验电流\\$\mathbf b=\mathbf e_A-\mathbf e_D$',r'端点电阻\\$R_{AD}=(\phi_A-\phi_D)/I$'],r'固定汇点电势与伪逆法独立求解全部节点')
 sym=flow([r'全部棱等价\\24条相同类型',r'Foster恒等式\\$\sum R_{ij}/R_e=11$',r'相邻电阻\\$R_{AB}=11/24\,\Omega$',r'方形对角\\$R_{AC}=7/12\,\Omega$'],r'只允许按保持源汇边界的对称并点；对角结果须另解节点方程')
 em=flow([r'直棱感应电动势\\$\mathcal E_{ij}=-\dot{\mathbf B}\cdot(\mathbf r_i\times\mathbf r_j)/2$',r'邻位置求和\\$\sum_{j\sim i}\mathbf r_j=2\mathbf r_i$',r'节点驱动和零\\$\sum\mathcal E_{ij}=0$',r'节点保守电势\\$\phi_i=\text{同一常数}$'],r'节点零差不阻止回路感应环流')
 leads=r'''\fill[accent] (0,2) circle (3pt);\fill[accent] (0,-1) circle (3pt);\node[left] at (0,2){$A$};\node[left] at (0,-1){$C$};\draw[arr,main] (0,2)--(0,-1);\draw[arr,accent] (0,2)..controls(3,2) and(3,-1)..(0,-1);\node[right] at (2.4,.5){路径2};\node[left] at (0,.5){路径1};\node[note] at (1.3,-2.3){两路径读数差 $=-\dot{\mathbf B}\cdot\mathbf S$\\保守节点差为零，直线 $A\to C$ 积分为 $-al^2/4$};'''
 save('08',[net,lap,sym,em,leads])
 # 同步图名索引，独立源包可从本脚本重建40图。
 p=ROOT/'scripts/render_figures.py';txt=p.read_text();txt=re.sub(r'NAMES=.*?\n\ndef main',f'NAMES={NAMES!r}\n\ndef main',txt,flags=re.S);p.write_text(txt)
 print(NAMES)
if __name__=='__main__':main()
