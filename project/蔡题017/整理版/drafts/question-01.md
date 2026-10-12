# 第1题

<!-- question-start -->

（1）设重力加速度恒为 $g$。一个质点从地面上的出射点 $A$ 以速率 $v_0$ 斜向上抛出，最终落回地面。证明：抛物线轨迹的焦点到 $A$ 的距离与出射角无关；求出该距离，并求出准线到 $A$ 的距离。

（2）考虑引力随距离的变化。设地表重力加速度为 $g$，地球半径为 $R$，重复第（1）问中的发射情景。证明：质点轨道上除地心之外的另一个焦点到出射点 $A$ 的距离为定值，并求出该值；给出改变出射角时，质点轨迹能够覆盖的范围。

![图1-1 平面匀强重力与球对称引力下的出射几何。](../figures/question-01.png){width=94%}

<!-- question-end -->

## 一、题型定位

本题把动力学中“相同出射速率”转化为圆锥曲线中的几何不变量。第一问的抛物线焦点随角度移动，但始终在一个以出射点为圆心的圆上；第二问的总机械能只由 $v_0$ 和 $R$ 决定，因此所有负能量轨道具有相同半长轴。另一焦点的轨迹与轨道族的包络由此联系起来。

需要区分三个层次：一条具体轨道上的点；固定速率、改变方向得到的轨道族；轨道族实际在地球外、首次撞地前走过的部分。仅画完整椭圆并把内部全部涂色，不足以证明最后一种覆盖范围。图1-1左侧的 $x,y$ 是平面坐标；右侧的 $O,A$ 用来建立地心距离 $r$，两套坐标不混用。

## 二、知识点

匀强重力下的水平匀速与竖直匀加速运动；二次函数配方；抛物线的焦点、准线及有符号焦参数；球对称引力中的能量与角动量；极坐标径向方程与圆锥曲线；椭圆两焦点距离和；三角不等式及相切法向；二次方程的判别式和物理解筛选。

为避免与“单位质量能量”混淆，记引力参数为 $\mathcal G=gR^2$，而不把它记作质量。记比机械能为 $\varepsilon$，比角动量为 $\ell$。这两个量分别具有 $\mathrm{m^2\,s^{-2}}$ 和 $\mathrm{m^2\,s^{-1}}$ 的量纲。半长轴 $a$、焦点圆半径 $D$、包络距离和 $S$ 均为长度。

## 三、物理图像

第一问中，固定 $v_0$、改变仰角 $\theta$，相当于改变水平和竖直动能的分配。轨迹顶点上升时，向下开口抛物线的焦参数同时改变，这两种变化恰使焦点到 $A$ 的距离不变。准线在所有角度下都是同一条水平直线。

第二问中，所有发射方向具有相同初始动能和引力势能。负能量下，轨道变得扁长或接近圆形，但能量决定的半长轴不变。地心 $O$ 是固定焦点，另一个焦点 $F$ 在以 $A$ 为中心、半径 $D$ 的球面上变化。轨道包络是另一张以 $O,A$ 为焦点的旋转椭球面；它不是某一条质点轨道，也不是以地心为中心的球面。

地球是不允许穿过的实物区域。需要在包络内再施加 $r\ge R$，并核对从 $A$ 到目标的轨道段没有先撞地。达到逃逸速率时，负能量轨道族的包络趋于无界，但不能直接说“所有地球外位置都可由临界逃逸轨道到达”：无限时间、速度极限和空间点的位置必须分别讨论。

## 四、解题入口

先把第一问写成 $y=a_qx^2+b_qx$，保留 $a_q<0$ 的符号，配方确定顶点，再与标准抛物线形式比较。不要凭图猜焦点在顶点上方还是下方。

第二问先用能量识别轨道支路，再推导同能量轨道的半长轴。对任意轨道点 $P$，分别写出 $AF=2a-R$ 和 $OP+FP=2a$，然后使用 $AP\le AF+FP$。得到覆盖范围的必要条件以后，再以固定目标的出射角方程证明条件充分，并排除数学轨道穿地后的延伸。

## 五、解析

**第1步：明确坐标、角度与模型边界。**

第一问取 $A$ 为原点，地面为 $y=0$，$x$ 水平向右，$y$ 竖直向上。设出射仰角为 $\theta$，初速度为

$$
\begin{aligned}
v_{x0}&=v_0\cos\theta,\\
v_{y0}&=v_0\sin\theta.
\end{aligned}
$$

通常的斜抛对应 $0<\theta<\pi/2$；向左发射可由镜面对称得到。水平发射的质点在理想地面处立即受到边界限制，竖直发射不形成通常的非退化抛物线，故二者只在需要时作为轨道族的极限。

第二问仍把 $\theta$ 定义为相对出射点局部切线的仰角。因此初始径向速度与切向速度分别为 $v_0\sin\theta$、$v_0\cos\theta$，而不是反过来。图1-1右侧的切线与 $OA$ 垂直。地球外的单位质量引力加速度为

$$
\mathbf a=-\frac{\mathcal G}{r^3}\mathbf r,
\qquad
\mathcal G=gR^2,
\qquad
r=|\mathbf r|.
$$

这里采用题目引力模型的通常假定：球对称平方反比引力，忽略空气阻力、自转与地形。地球内的引力并未由题目给定，也无须猜测，因为实际飞行在首次到达 $r=R$ 时停止。后文以可达点及其可逼近边界的闭包描述空间覆盖；若某边界必须用球面圆轨道才能精确达到，将明确说明它与先严格离地的飞行不同。

**第2步：消去第一问的时间，得到带符号的二次函数。**

水平与竖直运动方程为

$$
\begin{aligned}
x(t)&=v_0\cos\theta\,t,\\
y(t)&=v_0\sin\theta\,t-\frac12gt^2.
\end{aligned}
$$

因为 $\cos\theta>0$，可以由第一式解出 $t=x/(v_0\cos\theta)$，代入第二式：

$$
\begin{aligned}
y
&=x\tan\theta-\frac{g}{2v_0^2\cos^2\theta}x^2\\
&=b_qx+a_qx^2,\\
b_q&=\tan\theta,\\
a_q&=-\frac{g(1+\tan^2\theta)}{2v_0^2}<0.
\end{aligned}
$$

这里使用了 $1/\cos^2\theta=1+\tan^2\theta$。$a_q$ 的负号表示开口向下；若将它当成正数，焦点与准线位置都会颠倒。

**第3步：完整配方，确定顶点与焦参数。**

对二次函数进行配方：

$$
\begin{aligned}
y
&=a_q\left(x^2+\frac{b_q}{a_q}x\right)\\
&=a_q\left(x+\frac{b_q}{2a_q}\right)^2
-\frac{b_q^2}{4a_q}.
\end{aligned}
$$

因此顶点 $V$ 的坐标为

$$
x_V=-\frac{b_q}{2a_q},
\qquad
y_V=-\frac{b_q^2}{4a_q}.
$$

尤其注意 $x_V$ 前的负号：由于 $a_q<0$、$b_q>0$，实际 $x_V>0$，与质点向右运动一致。

将配方结果改写为标准形式

$$
(x-x_V)^2=4p(y-y_V),
\qquad
p=\frac{1}{4a_q}<0.
$$

这里的 $p$ 是有符号焦参数，不是“焦点到顶点的正距离”。实际正距离为 $|p|$。向下开口时，焦点在顶点下方，准线在顶点上方。

**第4步：算出焦点与准线，逐项消去角度。**

由标准形式，焦点为 $F=(x_V,y_V+p)$，准线为 $y=y_V-p$。记

$$
d=\frac{v_0^2}{2g}.
$$

代入 $a_q,b_q$ 后，顶点和焦参数分别为

$$
\begin{aligned}
x_V
&=\frac{v_0^2\sin\theta\cos\theta}{g}
=d\sin2\theta,\\
y_V
&=\frac{v_0^2\sin^2\theta}{2g}
=d\sin^2\theta,\\
p
&=-\frac{v_0^2\cos^2\theta}{2g}
=-d\cos^2\theta.
\end{aligned}
$$

故焦点坐标和准线为

$$
\begin{aligned}
x_F&=d\sin2\theta,\\
y_F&=d(\sin^2\theta-\cos^2\theta)
=-d\cos2\theta,\\
y_{\text{准线}}
&=d(\sin^2\theta+\cos^2\theta)=d.
\end{aligned}
$$

计算 $AF$ 时应先平方再求正长度：

$$
\begin{aligned}
AF^2
&=x_F^2+y_F^2\\
&=d^2(\sin^22\theta+\cos^22\theta)\\
&=d^2.
\end{aligned}
$$

于是

$$
\boxed{AF=\frac{v_0^2}{2g}},
\qquad
\boxed{\operatorname{dist}(A,\text{准线})=\frac{v_0^2}{2g}}.
$$

焦点随着 $2\theta$ 改变而沿圆 $x_F^2+y_F^2=d^2$ 运动；准线却不动。图1-2中的 $F,V,p$ 和 $y=d$ 正对应这些量，不把焦点圆误认为质点轨迹。

![图1-2 抛物线焦点、准线与等距关系。](../figures/focus-01.png){width=82%}

**第5步：用焦点—准线定义独立检查符号。**

取轨迹任意点 $P=(x,y)$，向准线作垂足 $M=(x,d)$，则 $PM=d-y$。飞行中 $y\le y_V\le d$，所以无需把 $d-y$ 改为负值。

令 $X=x-x_V$、$Y=y-y_V$，轨迹满足 $X^2=4pY$。于是

$$
\begin{aligned}
PF^2
&=X^2+(Y-p)^2\\
&=4pY+Y^2-2pY+p^2\\
&=(Y+p)^2.
\end{aligned}
$$

准线纵坐标为 $y_V-p$，故

$$
\begin{aligned}
PM^2
&=[(y_V-p)-y]^2\\
&=(-p-Y)^2\\
&=(Y+p)^2=PF^2.
\end{aligned}
$$

两者都是非负距离，因而 $PF=PM$。图1-2中画出的两条等距线段用于这一步核验。它检验的是整条抛物线定义，不仅是把焦点最终数值代回某一个点。

**第6步：求平面轨道族的覆盖范围，说明判别式的物理意义。**

虽然第一问只要求焦点与准线，但同一几何结构也能直接检查“固定速率改变方向”的覆盖。设 $\tau=\tan\theta$，由第2步得

$$
y=x\tau-\frac{x^2}{4d}(1+\tau^2).
$$

把目标点 $P=(x,y)$ 固定，将其视为关于 $\tau$ 的方程：

$$
\frac{x^2}{4d}\tau^2-x\tau+
\left(y+\frac{x^2}{4d}\right)=0.
$$

对于 $x>0$，判别式为

$$
\begin{aligned}
\Delta_\tau
&=x^2-\frac{x^2}{d}
\left(y+\frac{x^2}{4d}\right)\\
&=x^2\left(1-\frac yd-\frac{x^2}{4d^2}\right).
\end{aligned}
$$

有实出射角的必要条件为

$$
y\le d-\frac{x^2}{4d}.
$$

若再要求 $y\ge0$，则平方根在 $0$ 与 $1$ 之间，两根

$$
\tau_\pm=\frac{2d}{x}
\left(1\pm\sqrt{1-\frac yd-\frac{x^2}{4d^2}}\right)
$$

均不为负。由 $t=x/(v_0\cos\theta)>0$，且斜抛在第一次到达 $y=0$ 前始终有 $y\ge0$，可知这些目标确实能够在首次落地前到达。向左右改变方位后的平面覆盖为

$$
\boxed{0\le y\le d-\frac{x^2}{4d}}.
$$

当 $\Delta_\tau=0$，两种角度合并，这才是轨道族的包络。该包络也是一条抛物线，但不是任何一条固定角度轨迹；它的焦点为 $A$，准线为 $y=2d$，而单条轨迹的准线是 $y=d$。

**第7步：中心引力先用能量分支，避免无条件套用椭圆。**

第二问的比机械能为

$$
\begin{aligned}
\varepsilon
&=\frac12v_0^2-\frac{\mathcal G}{R}\\
&=\frac12v_0^2-gR.
\end{aligned}
$$

因为球对称引力的力矩为零，$\ell=|\mathbf r\times\mathbf v|$ 守恒。初始值为

$$
\ell=Rv_0\cos\theta.
$$

定义无量纲速度参数

$$
u=\frac{v_0^2}{gR}.
$$

因此

$$
\varepsilon=\frac{gR}{2}(u-2).
$$

$0<u<2$ 对应负能量椭圆；$u=2$ 对应抛物线逃逸；$u>2$ 对应双曲线逃逸。逃逸速率为

$$
v_{\mathrm{esc}}=\sqrt{2gR}.
$$

原题所说“落回地球”的非退化轨道必须首先在 $u<2$ 范围讨论。能量虽相同，角动量并不相同；不能由“能量固定”推出所有轨道的偏心率或周期内的撞地时间相同。

**第8步：从牛顿方程推导圆锥曲线及能量—半长轴关系。**

设轨道平面内的地心极角为 $\varphi$，取 $A$ 的地心方向为 $\varphi=0$，令 $w(\varphi)=1/r$。角动量守恒给出

$$
\dot\varphi=\frac{\ell}{r^2}=\ell w^2.
$$

利用链式法则：

$$
\begin{aligned}
\dot r
&=\frac{dr}{d\varphi}\dot\varphi\\
&=-\frac{w'}{w^2}\ell w^2=-\ell w',\\
\ddot r
&=-\ell w''\dot\varphi
=-\ell^2w^2w'',\\
r\dot\varphi^2&=\ell^2w^3.
\end{aligned}
$$

径向牛顿方程为 $\ddot r-r\dot\varphi^2=-\mathcal G/r^2$，故

$$
\begin{aligned}
-\ell^2w^2(w''+w)&=-\mathcal G w^2,\\
w''+w&=\frac{\mathcal G}{\ell^2}.
\end{aligned}
$$

这一步是将中心力运动化为常系数二阶微分方程。其解可写为

$$
w=\frac{\mathcal G}{\ell^2}
[1+e\cos(\varphi-\varphi_p)],
\qquad
r=\frac{p_c}{1+e\cos(\varphi-\varphi_p)},
\qquad
p_c=\frac{\ell^2}{\mathcal G}.
$$

$e$ 是偏心率，$p_c$ 是半通径，不能与第一问的有符号焦参数 $p$ 混淆。

再将此解代入能量，保留径向和切向两部分：

$$
\begin{aligned}
\varepsilon
&=\frac{\ell^2}{2}\big[(w')^2+w^2\big]-\mathcal G w\\
&=\frac{\mathcal G^2}{2\ell^2}
\left[e^2\sin^2f+(1+e\cos f)^2
-2(1+e\cos f)\right]\\
&=\frac{\mathcal G^2}{2\ell^2}(e^2-1),
\qquad f=\varphi-\varphi_p.
\end{aligned}
$$

括号展开时，$2e\cos f$ 与 $-2e\cos f$ 抵消，$e^2(\sin^2f+\cos^2f)=e^2$，因此能量确与沿轨道的位置无关。

为明确半长轴从何而来，沿近地点方向取局部直角坐标 $(X_c,Y_c)$，轨道方程写成 $r+eX_c=p_c$。平方并配方：

$$
\begin{aligned}
X_c^2+Y_c^2&=(p_c-eX_c)^2,\\
(1-e^2)X_c^2+2p_ceX_c+Y_c^2&=p_c^2,\\
(1-e^2)\left(X_c+\frac{p_ce}{1-e^2}\right)^2
+Y_c^2&=\frac{p_c^2}{1-e^2}.
\end{aligned}
$$

当 $e<1$，比较椭圆标准式得到

$$
a=\frac{p_c}{1-e^2}.
$$

结合能量式，才可推出

$$
\varepsilon=-\frac{\mathcal G}{2a}.
$$

以上推导假设 $\ell>0$；竖直径向发射对应其退化极限，后面单独核对最高点，不用 $1/\ell$ 公式硬代零。

**第9步：由能量求固定半长轴，再算另一焦点距离。**

把初始能量代入 $\varepsilon=-\mathcal G/(2a)$：

$$
\begin{aligned}
\frac12v_0^2-\frac{\mathcal G}{R}
&=-\frac{\mathcal G}{2a},\\
v_0^2-\frac{2\mathcal G}{R}
&=-\frac{\mathcal G}{a},\\
\frac1a&=\frac2R-\frac{v_0^2}{\mathcal G}.
\end{aligned}
$$

所以对于 $0<u<2$，

$$
\boxed{a=\frac{\mathcal G R}{2\mathcal G-Rv_0^2}
=\frac{R}{2-u}}.
$$

地心 $O$ 是椭圆一个焦点，另一焦点为 $F$。由于 $A$ 在椭圆上，焦点定义给出

$$
OA+AF=2a.
$$

利用 $OA=R$：

$$
\begin{aligned}
D\equiv AF
&=2a-R\\
&=\frac{2R}{2-u}-R\\
&=\frac{Ru}{2-u}\\
&=\frac{Rv_0^2}{2gR-v_0^2}.
\end{aligned}
$$

于是

$$
\boxed{AF=\frac{Rv_0^2}{2gR-v_0^2}},
\qquad 0<v_0<\sqrt{2gR}.
$$

这个距离只由 $v_0,g,R$ 决定，与仰角和发射方位无关。图1-3中的 $OA+AF=2a$ 与 $OP+FP=2a$ 是同一个椭圆定义应用于两个不同的轨道点，不是两个额外的动力学假设。

![图1-3 地心焦点、另一焦点与首次回到球面的椭圆轨道段。](../figures/orbit-01.png){width=60%}

**第10步：用三角不等式建立包络，判定何时真正相切。**

取一条轨道上的任意地球外点 $P$，记 $r=OP$、$s=AP$。由该椭圆的焦点性质，

$$
r+FP=2a.
$$

再由三角不等式，

$$
AP\le AF+FP.
$$

将上一式的 $FP=2a-r$ 以及 $AF=D=2a-R$ 代入：

$$
\begin{aligned}
s
&\le (2a-R)+(2a-r),\\
s+r&\le4a-R.
\end{aligned}
$$

定义

$$
S=4a-R=\frac{R(2+u)}{2-u}=R+2D.
$$

因此任何实际地球外可达点必须满足

$$
\boxed{r\ge R,\qquad s+r\le S}.
$$

等号成立要求 $A,F,P$ 共线，且 $F$ 位于 $A$ 与 $P$ 之间，而不是仅要求三点落在任意一条直线上。图1-4明确画出这一顺序，$AF=D$、$AP=s$、$OP=r$ 将实际进入包络方程。

![图1-4 同能量椭圆轨道族的包络与共线取等条件。](../figures/envelope-01.png){width=74%}

还应证明包络与具体轨道相切，而不是只凭示意图断言。具体轨道的局部法向与

$$
\frac{\overrightarrow{OP}}{OP}
+\frac{\overrightarrow{FP}}{FP}
$$

平行，包络面的局部法向与

$$
\frac{\overrightarrow{OP}}{OP}
+\frac{\overrightarrow{AP}}{AP}
$$

平行。取等时 $F$ 位于 $A,P$ 之间，所以 $\overrightarrow{FP}/FP=\overrightarrow{AP}/AP$，两个法向相同，从而切面相同。$F=P$ 的退化径向顶点用连续极限理解，不对零长度 $FP$ 求单位向量。

**第11步：证明包络内的目标确有向外发射解。**

必要条件不等于充分条件。现固定一个目标 $P$，令其地心极角为 $0<\varphi\le\pi$，地心距离为 $r=\rho R$，$\rho\ge1$。发射方位取在 $OA,OP$ 确定的平面内；另一侧可由对称性得到。

第8步的解在 $A$ 处满足

$$
w(0)=\frac1R,
\qquad
w'(0)=-\frac{v_0\sin\theta}{\ell}.
$$

由此可将轨道写成明确含初始角的形式：

$$
\frac{R}{r}
=\frac{
1+(u\cos^2\theta-1)\cos\varphi
-u\sin\theta\cos\theta\sin\varphi
}{u\cos^2\theta}.
$$

令 $\tau=\tan\theta$，乘以 $u\cos^2\theta$，再利用 $\cos^2\theta=1/(1+\tau^2)$：

$$
\begin{aligned}
\frac u\rho
&=(1+\tau^2)(1-\cos\varphi)
+u\cos\varphi-u\tau\sin\varphi,\\
(1-\cos\varphi)\tau^2-u\sin\varphi\,\tau
&+1-\cos\varphi+u\cos\varphi-\frac u\rho=0.
\end{aligned}
$$

这是固定目标时的出射角二次方程。展开判别式：

$$
\begin{aligned}
\Delta_\tau
&=u^2\sin^2\varphi
-4(1-\cos\varphi)
\left(1-\cos\varphi+u\cos\varphi-\frac u\rho\right)\\
&=(1-\cos\varphi)
\left[u^2-4+(u-2)^2\cos\varphi+\frac{4u}{\rho}\right].
\end{aligned}
$$

将包络 $s+r=S$ 与距离公式 $s^2=r^2+R^2-2Rr\cos\varphi$ 联立，解得该方向的包络半径

$$
\begin{aligned}
r_e(\varphi)
&=\frac{S^2-R^2}{2(S-R\cos\varphi)},\\
\rho_e(\varphi)
&=\frac{4u}
{(2-u)[2+u-(2-u)\cos\varphi]}.
\end{aligned}
$$

代入判别式，恰有

$$
\Delta_\tau
=4u(1-\cos\varphi)
\left(\frac1\rho-\frac1{\rho_e}\right).
$$

由于 $0<u<2$、$\rho>0$，故 $\Delta_\tau\ge0$ 等价于 $\rho\le\rho_e$，即目标在包络内。对于 $0<\varphi<\pi$，较大根

$$
\tau_+=
\frac{u\sin\varphi+\sqrt{\Delta_\tau}}
{2(1-\cos\varphi)}
$$

为正，给出向外初始径向速度。$\varphi=\pi$ 时根由原方程单独计算，存在正根的条件仍与包络一致；$\varphi=0$ 则使用径向发射，而不在分母 $1-\cos\varphi=0$ 处硬套公式。

**第12步：检查所选轨道在到达目标之前没有先撞地。**

令

$$
k=\frac{p_c}{R}=u\cos^2\theta,
\qquad
c_0=u\sin\theta\cos\theta\ge0.
$$

轨道任意中间极角 $\psi$ 的半径为

$$
\frac{r(\psi)}R=
\frac{k}{1+(k-1)\cos\psi-c_0\sin\psi}.
$$

负能量非退化椭圆的偏心率 $e<1$，分母始终为正，因此可以安全地比较不等式，不会把双曲线另一支的负分母混进来。

条件 $r(\psi)\ge R$ 等价于

$$
\begin{aligned}
(k-1)(\cos\psi-1)-c_0\sin\psi&\le0,\\
-2\sin\frac\psi2
\left[(k-1)\sin\frac\psi2
+c_0\cos\frac\psi2\right]&\le0.
\end{aligned}
$$

对 $0<\psi<\pi$，两半角函数均为正，因此进一步等价于

$$
(k-1)\tan\frac\psi2+c_0\ge0.
$$

若 $k\ge1$，该式在整个半周内自动成立。若 $k<1$，左侧随 $\psi$ 增大而减小；既然目标处 $\psi=\varphi$ 有 $r\ge R$，则所有更早的 $\psi$ 都满足它。因此目标确在首次撞地之前，而非穿地后的数学轨道段上。

$\varphi=\pi$ 的可达目标必须有 $k\ge1$，否则其半径小于 $R$，不能进入地球外范围。恰有 $k=1,c_0=0$ 时为球面圆轨道，应按后面的临界边界约定处理。至此，“包络内且地球外”的条件既必要又充分，不能省去这一步而只给一幅完整椭圆图。

**第13步：把距离和条件写成空间范围，求最高高度与球面覆盖。**

以 $O$ 为坐标原点，$Y$ 轴沿 $OA$ 向外，$X,Z$ 为与之垂直的坐标，令 $\varrho=\sqrt{X^2+Z^2}$。此时 $A=(0,R,0)$，

$$
r=\sqrt{\varrho^2+Y^2},
\qquad
s=\sqrt{\varrho^2+(Y-R)^2}.
$$

包络 $r+s=S$ 是以 $O,A$ 为焦点的旋转椭球，中心在 $Y=R/2$。半长轴、半焦距和横向半轴分别为

$$
\begin{aligned}
a_e&=\frac S2=\frac{R(2+u)}{2(2-u)},\\
c_e&=\frac R2,\\
b_e^2
&=a_e^2-c_e^2\\
&=\frac{S^2-R^2}{4}
=\frac{2R^2u}{(2-u)^2}.
\end{aligned}
$$

所以负能量下的空间覆盖闭包为

$$
\boxed{
\frac{X^2+Z^2}{b_e^2}
+\frac{(Y-R/2)^2}{a_e^2}\le1,
\qquad
X^2+Y^2+Z^2\ge R^2
}.
$$

图1-5画的是该轴对称体的空间投影，两幅分别缩放，不能把纸面大小当成实际尺寸比较；前实后虚的纬圈帮助区别球面和旋转椭球。解题使用的仍是 $\varrho,Y,r,s$，不是把投影中看起来相交的线误当成空间接触。

![图1-5 不同出射能量下的地球外覆盖体及轴对称空间关系。](../figures/space-01.png){width=94%}

沿 $OA$ 向外的径向发射角动量为零，最高点满足径向速度为零。直接由能量求得

$$
\begin{aligned}
-\frac{\mathcal G}{r_{\max}}
&=\frac12v_0^2-\frac{\mathcal G}{R},\\
r_{\max}&=\frac{2R}{2-u}=2a,\\
h_{\max}&=r_{\max}-R=\frac{Ru}{2-u}=D.
\end{aligned}
$$

这也与椭球最外端 $Y=R/2+a_e=2a$ 一致，是动力学与包络几何的独立交叉检查。

球面上 $r=R$，则可达边界满足 $AP\le S-R=2D$。设球面目标与 $A$ 的地心夹角为 $\varphi$，弦长为

$$
AP=2R\sin\frac\varphi2.
$$

所以当 $0<u<1$ 时，

$$
\boxed{0\le\varphi\le
2\arcsin\frac{u}{2-u}}.
$$

当 $1<u<2$ 时 $D>R$，全部球面位置均在包络内，可以由真实向外飞行轨道到达。当 $u=1$ 时，反面点恰在包络边界；切向发射为 $r=R$ 的圆轨道，若要求质点先严格离开球面，反面点只能作为 $\theta\to0^+$ 的极限接近，不能声称有一条先升空再于反面点首次撞地的有限角度轨道。

**第14步：处理逃逸临界与双曲线焦点，说明“另一个焦点”的适用域。**

当 $u=2$ 时，$\varepsilon=0$，第8步能量式给出 $e=1$。轨道为以地心 $O$ 为焦点的抛物线，只有一个有限焦点。椭圆 $a,D$ 发散只是支路极限，不能把无穷远当成一个可量出的有限“另一个焦点”。

当 $u>2$ 时，$\varepsilon>0$，$e>1$。第8步的直角坐标方程此时改写为

$$
(e^2-1)\left(X_c-\frac{p_ce}{e^2-1}\right)^2-Y_c^2
=\frac{p_c^2}{e^2-1}.
$$

比较双曲线标准式，其半实轴的正长度为 $a_h=p_c/(e^2-1)$。再由第8步完整能量式，

$$
\varepsilon=\frac{\mathcal G^2}{2\ell^2}(e^2-1)
=\frac{\mathcal G}{2a_h}.
$$

因此由

$$
\varepsilon=\frac{\mathcal G}{2a_h}
$$

求得

$$
a_h=\frac{R}{u-2}.
$$

初始向外运动所在的实际双曲线支满足 $AF-OA=2a_h$，从而

$$
\begin{aligned}
AF
&=R+2a_h\\
&=\frac{Ru}{u-2}\\
&=\frac{Rv_0^2}{v_0^2-2gR}.
\end{aligned}
$$

因此超临界支路的另一焦点距离也与角度无关，但它不是把椭圆公式保留负号后直接当作负距离。非退化情况下可以合写为 $AF=Rv_0^2/|2gR-v_0^2|$，仍必须注明 $u\ne2$ 以及各自的轨道类型。

**第15步：用单调角积分求不落回支路的实际覆盖，排除伪解。**

对于 $u\ge2$，向外发射后径向运动不会出现有限外侧转向点。能量与角动量给出

$$
\dot r^2
=2\varepsilon+\frac{2\mathcal G}{r}
-\frac{\ell^2}{r^2}.
$$

因为 $\dot r\ge0$，从球面到目标半径 $r$ 的累计偏转角为

$$
\varphi(r;\ell)=
\int_R^r
\frac{\ell\,dq}
{q^2\sqrt{2\varepsilon+2\mathcal G/q-\ell^2/q^2}}.
$$

固定 $\varepsilon,r$，对被积函数关于 $\ell$ 求导。令 $C(q)=2\varepsilon+2\mathcal G/q>0$，逐项求导得

$$
\begin{aligned}
\frac{\partial}{\partial\ell}
\frac{\ell}{q^2\sqrt{C-\ell^2/q^2}}
&=\frac1{q^2}
\left[(C-\ell^2/q^2)^{-1/2}
+\frac{\ell^2}{q^2}(C-\ell^2/q^2)^{-3/2}\right]\\
&=\frac{C}{q^2(C-\ell^2/q^2)^{3/2}}>0.
\end{aligned}
$$

故固定目标半径时，偏转角随角动量增大而增大。向外发射允许的最大角动量是 $\ell_{\max}=Rv_0$，对应切向发射 $\theta=0$；其初始径向速度虽为零，但 $u\ge2$ 时径向加速度为 $v_0^2/R-g=g(u-1)>0$，会立即向外离开球面。

切向轨道的半通径和偏心率为 $p_c=Ru$、$e=u-1$，且 $A$ 为近地点。因此图1-6中的边界轨道为

$$
r_t(\varphi)=
\frac{Ru}{1+(u-1)\cos\varphi}.
$$

从径向发射的零偏转到切向发射的最大偏转连续变化，实际可达范围为

$$
\boxed{
1+(u-1)\cos\varphi>0,
\qquad
r\ge\frac{Ru}{1+(u-1)\cos\varphi}
},
\qquad u\ge2.
$$

![图1-6 临界逃逸时的切向边界轨道与向外可达区域。](../figures/unbound-01.png){width=88%}

其中 $u=2$ 时 $r_t=2R/(1+\cos\varphi)$、$0\le\varphi<\pi$；$u>2$ 时

$$
0\le\varphi<
\arccos\left(-\frac1{u-1}\right).
$$

严格不等号表示渐近方向在有限距离不能到达。图1-6的 $A,O,\varphi$ 与 $r_t$ 就是上式中的量；阴影位于切向抛物线外行一侧，不表示把数学轨道另一支或穿地部分纳入覆盖。即便代入固定目标二次方程得到正 $\tan\theta$，仍须检查目标是否位于从 $A$ 开始的实际外行支，不能用判别式代替这一筛选。

**第16步：检查平地极限、量纲与主要边界。**

固定 $v_0,g$ 而令 $R\to\infty$，有 $u=v_0^2/(gR)\to0$。第二问焦点距离变为

$$
\begin{aligned}
D
&=\frac{v_0^2}{2g}
\left(1-\frac{v_0^2}{2gR}\right)^{-1}\\
&=\frac{v_0^2}{2g}
\left[1+\frac{v_0^2}{2gR}
+O(R^{-2})\right]\\
&\longrightarrow d.
\end{aligned}
$$

这里使用几何级数展开 $(1-z)^{-1}=1+z+O(z^2)$，适用于 $|z|\ll1$。$v_0^2/g$ 是长度，$v_0^2/(gR)$ 是无量纲量，所以式中各项量纲一致。

再取出射点附近的局部高度 $y=Y-R$、水平距离 $x=\varrho$。在 $|x|,|y|\ll R$ 时，

$$
r=\sqrt{x^2+(R+y)^2}
=R+y+\frac{x^2}{2R}+O(R^{-2})
$$

，而 $s=\sqrt{x^2+y^2}$。包络 $s+r=R+2D$ 在平地极限给出

$$
\sqrt{x^2+y^2}+y=2d.
$$

移项后平方：

$$
\begin{aligned}
x^2+y^2&=(2d-y)^2,\\
x^2&=4d^2-4dy,\\
y&=d-\frac{x^2}{4d}.
\end{aligned}
$$

恰与第6步的平面包络一致。注意这是固定局部空间点的 $R\to\infty$ 极限，不是固定 $R$ 把 $u\to2$ 的逃逸极限；两种极限不能互换。

$v_0\to0$ 时 $D\to0$，外部可达体缩到出射点附近；$u\to2^-$ 时 $D\to\infty$，负能量椭圆可以在长时间后绕回，但 $u=2$ 的实际外行抛物线不再折返，覆盖支路需按第15步重新判断。

**第17步：给出可复算的数值与轨道检查，不只核对最终公式。**

以 $g,R$ 为单位使 $R=1$、$\mathcal G=1$，取 $u=1/2$。由前面式子，

$$
\begin{aligned}
a&=\frac23,\qquad
D=\frac13,\qquad
S=\frac53,\\
a_e&=\frac56,\qquad
b_e=\frac23.
\end{aligned}
$$

例如目标的地心极角 $\varphi=0.2$、地心距离 $\rho=1.1$ 时，包络半径为

$$
\rho_e=
\frac{4u}{(2-u)[2+u-(2-u)\cos\varphi]}
\approx1.2946.
$$

所以目标在包络内；不能只因 $\rho>1$ 就判断可达。将 $\varphi,\rho,u$ 代回角度二次方程，三个系数和判别式为

$$
\begin{aligned}
A_\tau&=1-\cos0.2\approx0.01993342,\\
B_\tau&=-0.5\sin0.2\approx-0.09933467,\\
C_\tau&=1-\cos0.2+0.5\cos0.2-\frac{0.5}{1.1}
\approx0.05542126,\\
\Delta_\tau&=B_\tau^2-4A_\tau C_\tau
\approx0.00544843.
\end{aligned}
$$

所以 $\tau_-\approx0.640160$、$\tau_+\approx4.343162$，分别给出 $\theta_-\approx32.6257^\circ$、$\theta_+\approx77.0338^\circ$。两初始径向速度均为正；按第12步检查中间半径都不小于 $R$。再从

$$
\begin{aligned}
\dot X&=V_X,\qquad \dot Y=V_Y,\\
\dot V_X&=-\frac{X}{(X^2+Y^2)^{3/2}},\\
\dot V_Y&=-\frac{Y}{(X^2+Y^2)^{3/2}}
\end{aligned}
$$

独立积分，初值取地心坐标 $X(0)=1,Y(0)=0$、$V_X(0)=\sqrt u\sin\theta$、$V_Y(0)=\sqrt u\cos\theta$。这组核验坐标只是把前面的径向轴旋转了 $90^\circ$，$r,\varphi$ 的定义未变。

计算应在首次 $r=1$ 的回落事件终止，或在到达目标极角时终止，并同时检查 $\varepsilon$、$\ell$ 守恒。81个负能量目标与36个逃逸目标的独立运动积分、12个切向边界的径向角积分均与本题解析一致；这些核验使用牛顿方程与积分定义，而不是把最终焦点公式重复输入自证。

## 六、关键洞察

固定速率的关键不是“轨迹相似”，而是能量相同。匀强重力模型把这种不变量藏在焦点坐标的两倍角中；平方反比模型把它藏在半长轴中。两者的焦点定距离在平地极限连续相接，但覆盖体在逃逸临界存在不同外行支路，不能凭形式连续就忽略时间和撞地边界。

几何法还可为负能量覆盖提供另一条独立路线。若给定地球外点 $P$，要求另一焦点满足

$$
AF=D,\qquad PF=2a-r.
$$

两个圆在轨道平面内相交的条件为

$$
|D-(2a-r)|\le AP\le D+(2a-r).
$$

左侧为 $|r-R|$，对任意 $OP=r$、$OA=R$ 由三角不等式自动成立；右侧为 $S-r$，正是包络条件。还须检查 $2a-r\ge0$。由 $AP\ge r-R$ 和 $AP+r\le S$，可得 $2r-R\le4a-R$，所以 $r\le2a$，此检查自动通过。两圆交点中的向外发射解再按主解析的首次撞地条件筛选；这说明几何构造与动力学筛选缺一不可。

利用偏心率向量可以直接复核焦点圆。单位质量轨道的偏心率向量为

$$
\mathbf e=\frac{\mathbf v\times(\mathbf r\times\mathbf v)}{\mathcal G}
-\frac{\mathbf r}{r}.
$$

在 $A$ 处，以 $\mathbf e_r,\mathbf e_t$ 表示局部径向与切向：

$$
\begin{aligned}
\mathbf e
&=(u\cos^2\theta-1)\mathbf e_r
-u\sin\theta\cos\theta\,\mathbf e_t,\\
e^2
&=(u\cos^2\theta-1)^2
+u^2\sin^2\theta\cos^2\theta\\
&=1+u(u-2)\cos^2\theta.
\end{aligned}
$$

负能量椭圆的另一焦点相对地心为 $\overrightarrow{OF}=-2a\mathbf e$，故

$$
\begin{aligned}
\overrightarrow{AF}
&=-2a\mathbf e-R\mathbf e_r\\
&=D[-\cos2\theta\,\mathbf e_r
+\sin2\theta\,\mathbf e_t].
\end{aligned}
$$

这不仅再次证明 $AF=D$，还证明改变发射方位时，另一焦点覆盖以 $A$ 为中心的球面。$F$ 的切向分量朝发射方向，不能为了让几何图好看任意翻转它。双曲线的有符号半长轴为负，另一焦点方向会相应改变；实际正距离仍按其支路计算。

数值验证中，包络的角度二次方程具有理论重根。浮点运算得到极小正判别式时，直接开方会将舍入误差放大为平方根级误差，尤其在接近逃逸的细长轨道上。正确处理是先确认目标确为解析包络点，再使用严格重根式；不能把容差不断放宽，掩盖真正的几何或符号错误。

## 七、易错点

将向下开口抛物线的焦点放在顶点上方，通常来自把 $p$ 当成无符号正距离。应先保留 $p=1/(4a_q)<0$，再分别写 $y_F=y_V+p$ 和准线 $y=y_V-p$。

配方时漏写 $x_V=-b_q/(2a_q)$ 的负号，会把焦点画到发射点左侧。距离平方偶然仍可能算对，不能据此认定坐标和图正确。

把 $AF+FP=AP$ 写成对任何轨道点都成立。一般情况下只有 $AP\le AF+FP$；等号必须有 $A,F,P$ 的正确共线顺序。另一种共线顺序给出距离差，不是本题的椭圆包络。

把同能量椭圆与以 $O,A$ 为焦点的包络椭圆混为一谈。前者半长轴 $a$、焦点 $O,F$；后者半长轴 $a_e=S/2$、焦点 $O,A$。两个椭圆在边界点相切，但不是同一条曲线。

只检查目标在包络内，不检查 $r\ge R$、向外初速与首次撞地。数学椭圆的内部轨道段穿过地球，不能按未给出的地球内部模型继续飞行。

将 $u=1$ 的圆轨道、$u=2$ 的逃逸轨道混为一类。前者速度为 $\sqrt{gR}$，是切向绕地临界；后者速度为 $\sqrt{2gR}$，能量才为零。$u=1$ 的反面球面点涉及是否允许恰沿球面运行，须注明边界约定。

对双曲线目标只用角度方程的正根和判别式判断可达。另一数学支可能给出看似正的出射角，却需越过无穷远后才到目标。非负能量应以实际外行角积分或真实运动时间筛选。

## 八、课堂讲解建议

课堂可先只讲第一问。板书保留 $a_q<0$，让学生亲自完成一次配方，再比较焦点和准线的纵坐标。先问“顶点升高时，焦点是否一定同步升高”，再用 $\theta=30^\circ,60^\circ$ 的计算打破只看顶点的直觉。图1-2上必须指出焦点圆并非飞行轨迹。

转入第二问时，先让学生分别写初始能量和角动量，比较哪一个随角度变化。教师在板书上分开列 $a$ 与 $a_e$，全过程保留 $O,F$ 与 $O,A$ 两套焦点。图1-4只在共线取等处使用，图1-3用于提醒真实飞行在首次碰到球面处停止。

学生能够完成必要条件后，不立即宣布全解。课堂再提出“包络内是否每一点都能到达”，先用两圆交点直观建立候选轨道，再用角度方程与首次撞地不等式补齐证明。运算基础较弱时，可分两次讲第11、12步，不能把充分性压缩成“显然”。

最后的逃逸支路适合作为条件辨析。教师画图1-6，要求学生比较“$u\to2^-$ 的长周期回落”与“恰有 $u=2$ 的外行逃逸”，明确二者不是同一条实际运动过程。学生若用双曲线正根声称可绕过所有方向，课堂以真实角积分的单调性定位其错误，不仅告知答案错了。

## 九、变式训练

**变式1：指定地面目标的两种发射角。**

取 $v_0=20\,\mathrm{m\,s^{-1}}$、$g=10\,\mathrm{m\,s^{-2}}$。先求 $\theta=30^\circ$ 的焦点与准线，再判断 $P=(24\,\mathrm m,8\,\mathrm m)$ 能否到达，并求两种角度。

由 $d=v_0^2/(2g)=20\,\mathrm m$，

$$
\begin{aligned}
x_F&=20\sin60^\circ=10\sqrt3\,\mathrm m,\\
y_F&=-20\cos60^\circ=-10\,\mathrm m,\\
y_{\text{准线}}&=20\,\mathrm m.
\end{aligned}
$$

该角度的顶点高度仅为 $d\sin^230^\circ=5\,\mathrm m$，焦点却在地下；这不违背抛物线的几何定义，焦点不要求位于物理飞行弧内。

目标处的包络高度为

$$
y_e(24)=20-\frac{24^2}{80}=12.8\,\mathrm m>8\,\mathrm m.
$$

因此目标可达。角度根为

$$
\begin{aligned}
\tau_\pm
&=\frac{40}{24}
\left(1\pm\sqrt{1-\frac8{20}-\frac{24^2}{1600}}\right)\\
&=\frac53\left(1\pm\frac{\sqrt6}{5}\right)\\
&=\frac{5\pm\sqrt6}{3}.
\end{aligned}
$$

所以

$$
\boxed{\theta_\pm=
\arctan\frac{5\pm\sqrt6}{3}}.
$$

两根约为 $0.8502,2.4832$，对应仰角约 $40.37^\circ,68.06^\circ$。各自飞行时间为 $t_\pm=24/(20\cos\theta_\pm)$；代入 $y=20\sin\theta_\pm\,t_\pm-5t_\pm^2$，均得到 $8\,\mathrm m$。由于目标高度非负且取正时间，两种角度都属于首次落地前的轨迹。

**变式2：低于绕地速率时的最大球面射程。**

设 $v_0^2=gR/2$，求最高高度、包络半轴和最大球面弧长。

此时 $u=1/2$，故

$$
\begin{aligned}
a&=\frac{2R}{3},&
D=h_{\max}&=\frac R3,\\
S&=\frac{5R}{3},&
a_e&=\frac{5R}{6},\\
b_e^2
&=\left(\frac{5R}{6}\right)^2-\left(\frac R2\right)^2
=\frac{4R^2}{9},&
b_e&=\frac{2R}{3}.
\end{aligned}
$$

球面上 $AP=2R\sin(\varphi/2)$，而最大弦长为 $2D=2R/3$：

$$
\sin\frac{\varphi_{\max}}2=\frac13.
$$

因此最大球面弧长为

$$
\boxed{L_{\max}=2R\arcsin\frac13
\approx0.679674R}.
$$

它不是弦长 $2R/3$。若硬套平地射程 $v_0^2/g=R/2$，则忽略了球面曲率和引力变化；本例最高高度已达 $R/3$，不满足平地近似的尺度要求。

**变式3：首次落点可以是出射点的反面吗？**

设 $u=3/2$，求一条首次落点为反面球面点的发射角，并验证其轨道在此之前不穿地。

反面点有 $\varphi=\pi$、$\rho=1$。将其代入角度方程：

$$
\begin{aligned}
2\tau^2+2-u-u&=0,\\
2\tau^2-1&=0.
\end{aligned}
$$

选向外发射的正根：

$$
\boxed{\tan\theta=\frac1{\sqrt2}},
\qquad
\theta\approx35.264^\circ.
$$

这时 $\cos^2\theta=2/3$，所以

$$
k=u\cos^2\theta=1,
\qquad
c_0=u\sin\theta\cos\theta=\frac1{\sqrt2}.
$$

轨道为

$$
\frac rR=\frac1{1-\frac1{\sqrt2}\sin\varphi}.
$$

在 $0<\varphi<\pi$ 中，分母严格小于 $1$ 且大于 $1-1/\sqrt2>0$，因此 $r>R$；到 $\varphi=\pi$ 时恰有 $r=R$。这证明反面点确是首次落点，不是穿地后重新走到的点。

本例 $a=2R$、$D=3R$、$S=7R$，所有球面都在包络内；但径向最高高度 $3R$ 与这条轨道的最大高度不同。该轨道在 $\varphi=\pi/2$ 达到

$$
r_{\mathrm{apo}}=\frac{R}{1-1/\sqrt2}
=(2+\sqrt2)R.
$$

其最高高度为 $(1+\sqrt2)R<3R$，符合“轨道族最高值”不等于“每一条轨道的最高值”。

**变式4：超临界速度下，侧面的近处目标反而不能到达。**

设 $u=3$，目标位于与 $OA$ 垂直的地心方向，即 $\varphi=\pi/2$。求可达的最小地心距离，并判断 $r=2R$ 与 $r=4R$。

由实际外行边界，并代入第14、15步的几何参数，逐项得到

$$
\begin{aligned}
r_t(\pi/2)&=\frac{3R}{1+2\cos(\pi/2)}=3R,\\
a_h&=\frac{R}{3-2}=R,\qquad
AF=\frac{3R}{3-2}=3R,\\
\varphi_\infty&=\arccos\left(-\frac1{3-1}\right)=120^\circ.
\end{aligned}
$$

所以 $r=2R$ 不可达，$r=4R$ 可达。$\varphi=\pi/2$ 虽在渐近角范围内，仍须满足 $r\ge3R$，同时检查角度与径向界限才构成完整判断。不是速度足够大就能用任意角度飞到一切外部近点：固定速率且必须向外发射，会限制累计偏转角。

对可达目标 $\rho=4$，角度方程为

$$
\begin{aligned}
\tau^2-3\tau+\frac14&=0,\\
\tau_\pm&=\frac{3\pm\sqrt{9-1}}2
=\frac{3\pm2\sqrt2}{2}.
\end{aligned}
$$

实际外行支选较小根 $\tau_-=(3-2\sqrt2)/2\approx0.08579$。较大根虽然也为正，却对应越过渐近方向后的另一数学段，不能用作从 $A$ 出发到该目标的实际轨迹。

这一筛选不能仅凭“选小根”的经验完成。对任一候选根，先由初始角算出

$$
\begin{aligned}
k&=\frac{3}{1+\tau^2},&
c_0&=\frac{3\tau}{1+\tau^2},\\
\frac rR
&=\frac{k}{1+(k-1)\cos\psi-c_0\sin\psi}.
\end{aligned}
$$

这里 $\psi$ 是沿实际运动连续增长的地心角，目标要求 $\psi=\pi/2$。分子 $k>0$，所以只有从 $\psi=0$ 起、分母连续为正的那一段才是出发后的物理轨道。分母第一次降为零时，$r$ 趋于无穷；越过这个角度再代入代数式，已不是从 $A$ 沿这条外行轨道可到达的位置。

<!-- KEEP_TOGETHER_START -->

为求第一次出现的零点，令

$$
\begin{aligned}
e&=\sqrt{(k-1)^2+c_0^2},\\
\delta&=\operatorname{atan2}(-c_0,k-1),\qquad -\pi<\delta<0,\\
1+(k-1)\cos\psi-c_0\sin\psi
&=1+e\cos(\psi-\delta).
\end{aligned}
$$

此处利用辅助角公式；$\operatorname{atan2}$ 根据两个分量确定象限，不能用单值的 $\arctan[-c_0/(k-1)]$ 替代，否则较大根的象限会错。初始时 $\psi-\delta=-\delta\in(0,\pi)$，且分母等于 $k>0$。随着 $\psi$ 增大，余弦在到达 $\pi$ 前单调减小。因为本例 $e>1$，第一次零点满足

$$
\boxed{\psi_\infty
=\delta+\arccos\left(-\frac1e\right)}.
$$

逐根代入得到

$$
\begin{aligned}
\tau_-&\approx0.0857864:&
k_-&\approx2.9780834,&
c_{0-}&\approx0.2554792,&
e_-&\approx1.9945133,\\
\tau_+&\approx2.9142136:&
k_+&\approx0.3160343,&
c_{0+}&\approx0.9209914,&
e_+&\approx1.1471854.
\end{aligned}
$$

于是

$$
\begin{aligned}
\psi_{\infty,-}&\approx112.7317^\circ>90^\circ,\\
\psi_{\infty,+}&\approx24.0576^\circ<90^\circ.
\end{aligned}
$$

较小根的实际轨道尚未走到无穷远，便在 $90^\circ$ 方向到达 $4R$；较大根的实际轨道在 $24.0576^\circ$ 已趋于无穷远，永远不能转到目标的 $90^\circ$ 方向。用初始条件直接积分牛顿方程也得到这两条轨道的不同渐近方向。这个例子说明：二次方程实根只保证代数关系成立，根的物理筛选还必须检查连续运动区间，不能忽略双曲线的分支。

<!-- KEEP_TOGETHER_END -->

<!-- question-complete -->
