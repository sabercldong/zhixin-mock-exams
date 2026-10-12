# 第1题

<!-- model-revision-authorized: 用户2026-10-10明确回复“四项均按建议修订并注明”；采用共转观察坐标，本分题仍待实际PDF及图稿验收。 -->
<!-- question-start -->

黄俏站在地面上不动，记为质点 $H$。唐鹏记为质点 $T$，坐在半径为 $r$、以恒定角速度 $\omega$ 逆时针旋转的木马上，圆心为 $O$，$OH=l$，$l>r>0$，$\omega>0$。

（1）唐鹏相对木马静止。某时刻，地面上观察到唐鹏的速度恰沿着 $HT$ 连线。求此时黄俏相对唐鹏的速度与加速度，以及唐鹏相对黄俏的速度与加速度。

（2）唐鹏随木马转动，并沿木马径向往复移动，其到圆心的距离为
$$
\rho(t)=\frac r2\left[1+\cos(\omega t)\right].
$$
在 $t=0$ 时，唐鹏与黄俏的距离最小，为 $l-r$。分别写出两位观察者看到对方的轨迹方程。

（3）在第（2）问的运动条件下，求唐鹏相对黄俏，以及黄俏相对唐鹏的速度、加速度随时间的变化。

**修订说明：** 为明确相对运动的测量定义，黄俏的观察坐标方向固定于地面；唐鹏的观察坐标方向随木马以角速度 $\omega$ 转动，径向轴沿 $OT$ 的方向，切向轴沿木马旋转方向。“面向前进方向”指木马的切向，而不是径向移动与旋转运动的合速度方向。$\rho=0$ 时，坐标方向由木马的旋转相位连续定义。相对速度、相对加速度分别指各自观察坐标中相对位置的一阶、二阶时间导数。第（1）问采用连线存在的非退化切线情形 $l>r$。

<!-- question-end -->

## 一、题型定位

本题是“平移与旋转同时存在”的相对运动问题。地面观察者的坐标轴不转动，木马上观察者的坐标轴转动；两人看到的相对速度不一定具有相同大小，加速度也不能直接互相取负。

第（1）问用速度沿切线的几何关系判断瞬时位置，再区分两个观察坐标的导数。第（2）问先写位置，再投影到各自坐标；地面轨迹是心形线，木马旋转坐标中的轨迹是偏心椭圆。第（3）问在相同时间参数下求导，最后用极坐标分量与旋转坐标转换再核验。

若只问同一组地面坐标中两质点的速度之差，答案当然互为相反向量。但本题修订后的模型明确问两个不同方向约定的观察坐标，旋转坐标导数必须计入坐标轴自身的变化；这不是相对运动违背了相互性，而是比较了不同的测量定义。

## 二、知识点

匀速圆周运动的切向速度与向心加速度；从固定基底到旋转基底的投影；极坐标基矢随时间的导数；乘积求导与倍角公式；参数曲线的消参；速度、速率及加速度的区别；旋转坐标中的速度运输定理与加速度运输定理。

设木马转角为 $\theta=\omega t$。固定地面基矢为 $\boldsymbol e_x,\boldsymbol e_y$，随木马转动的单位基矢为
$$
\begin{aligned}
\boldsymbol e_r&=\cos\theta\,\boldsymbol e_x+\sin\theta\,\boldsymbol e_y,\\
\boldsymbol e_\theta&=-\sin\theta\,\boldsymbol e_x+\cos\theta\,\boldsymbol e_y.
\end{aligned}
$$
两基矢长度都是 $1$，彼此垂直，$\boldsymbol e_\theta$ 指向转角增大的切向。它们的时间导数为
$$
\dot{\boldsymbol e}_r=\omega\boldsymbol e_\theta,\qquad
\dot{\boldsymbol e}_\theta=-\omega\boldsymbol e_r.
$$

写出第一式的来由：$\mathrm d(\cos\omega t)/\mathrm dt=-\omega\sin\omega t$，$\mathrm d(\sin\omega t)/\mathrm dt=\omega\cos\omega t$，因而径向基矢的导数恰为 $\omega\boldsymbol e_\theta$。第二式同理，并带有负号。这两个负号决定后面向心项与切向项的符号。

本题中 $r,l,\rho$ 的量纲均为长度，$\omega$ 为时间的倒数。位置公式只含长度，速度公式应含 $\omega$ 乘长度，加速度公式应含 $\omega^2$ 乘长度。量纲检查能排除漏写 $\omega$ 的错误，但不能识别把无量纲系数 $1$ 写成 $2$ 的错误，后者还要用直接求导和特殊时刻核验。

## 三、物理图像

第（1）问的地面速度垂直于 $OT$。速度又沿 $HT$，所以 $HT$ 是木马圆周的切线，三角形 $OTH$ 在 $T$ 处为直角。图1-1画出其中一个切点；另一切点关于 $OH$ 对称。

![图1-1 圆周运动的切向速度与外部观察点的切线关系。](../figures/geometry-01.png){width=68%}

图中的 $r$ 是第（1）问固定半径，不能在该问提前替换成变化半径 $\rho(t)$。图中选择逆时针运动；换成顺时针时，应同时改变角度随时间的方向以及切向基矢，而不是只改某一个速度符号。

第（2）问中，唐鹏不只沿圆周走，还沿径向往复移动。他的实际地面速度由径向速度与切向速度合成，一般并不沿 $\boldsymbol e_\theta$。因此“木马切向坐标”与“始终对准实际速度的坐标”是两种不同模型，不能在计算中混用。

唐鹏观察黄俏时，先作从 $T$ 指向 $H$ 的相对位置向量，再分别投影到 $\boldsymbol e_r,\boldsymbol e_\theta$。如图1-2，坐标原点为 $T$，不是 $O$；$\rho$ 是原点从 $O$ 移出的距离，必须从径向投影中减去。

![图1-2 移动原点处的旋转基矢及相对位置投影。](../figures/projection-01.png){width=66%}

图中的 $P$ 是 $H$ 在径向轴所在直线上的垂足。沿径向轴，$OP$ 的有向投影为 $l\cos\theta$，而 $OT=\rho$，所以 $TP$ 的有向分量是 $X=l\cos\theta-\rho$。图中的 $X$ 尺寸线展示这一相减关系；它是有向坐标，其他相位下可以为负，并不始终等于线段长度的正值。

后续方程使用图中的投影定义
$$
X=(\boldsymbol H-\boldsymbol T)\cdot\boldsymbol e_r,\qquad
Y=(\boldsymbol H-\boldsymbol T)\cdot\boldsymbol e_\theta.
$$
旋转坐标中固定的是两根坐标轴的相对方向，不是它们在地面上的方向。黄俏虽然不动，其坐标 $X,Y$ 仍会改变。

## 四、解题入口

先给“相对”配上完整坐标约定，再写两个质点的位置。地面系取 $O$ 为辅助原点、$OH$ 为 $x_O$ 正轴，黄俏的位置为 $(l,0)$。黄俏自己的观察坐标以 $H$ 为原点，方向与地面辅助轴平行，两者仅相差一个恒定平移。

唐鹏的观察坐标以 $T$ 为原点，基矢随木马旋转。其径向分量不能只写成 $l\cos\theta$，因为唐鹏自己已经位于径向距离 $\rho$ 处；正确分量是 $l\cos\theta-\rho$。切向分量则为 $-l\sin\theta$，其中负号来自切向基矢在固定 $x_O$ 方向上的分量为 $-\sin\theta$。

轨迹方程先保留时间参数，确认起点、方向和周期，再消去参数。速度与加速度从位置求导，不从速率大小求导冒充向量加速度。最后用另一种分解方式检查同一结论，避免位置、速度、加速度一起沿用同一个错误。

## 五、解析

**第1步：建立两种观察坐标，写清位置变量。**

在第（2）、（3）问中，令 $\theta=\omega t$。固定地面坐标中的位置为
$$
\boldsymbol H=l\boldsymbol e_x,\qquad
\boldsymbol T=\rho\boldsymbol e_r.
$$
唐鹏相对黄俏的位置向量，在固定地面基底中展开为
$$
\begin{aligned}
\boldsymbol R_{T/H}
&=\boldsymbol T-\boldsymbol H\\
&=(\rho\cos\theta-l)\boldsymbol e_x
 +\rho\sin\theta\,\boldsymbol e_y.
\end{aligned}
$$
所以以 $H$ 为原点的地面观察坐标为
$$
x_H=\rho\cos\theta-l,\qquad y_H=\rho\sin\theta.
$$

反向相对位置向量确实是 $\boldsymbol H-\boldsymbol T=-\boldsymbol R_{T/H}$。但唐鹏用旋转基底表示它，因此还需作投影：
$$
\begin{aligned}
X&=(l\boldsymbol e_x-\rho\boldsymbol e_r)\cdot\boldsymbol e_r
  =l\cos\theta-\rho,\\
Y&=(l\boldsymbol e_x-\rho\boldsymbol e_r)\cdot\boldsymbol e_\theta
  =-l\sin\theta.
\end{aligned}
$$
计算 $Y$ 时使用 $\boldsymbol e_r\cdot\boldsymbol e_\theta=0$；不是漏掉了 $\rho$ 项，而是该项在切向的投影本来为零。

**第2步：由切线条件确定第（1）问的瞬时位置。**

本步暂取 $\rho=r$ 恒定。地面速度为
$$
\boldsymbol v_{T/H}=r\omega\boldsymbol e_\theta.
$$
“速度沿连线”要求 $\boldsymbol T-\boldsymbol H$ 与 $\boldsymbol e_\theta$ 平行，等价于其径向投影为零：
$$
(\boldsymbol T-\boldsymbol H)\cdot\boldsymbol e_r
=r-l\cos\theta=0.
$$
因此
$$
\cos\theta=\frac rl,\qquad
\sin\theta=\pm\sqrt{1-\frac{r^2}{l^2}}.
$$
因 $l>r$，确实存在两个切点。切线段长可由勾股定理求得：
$$
HT=\sqrt{OH^2-OT^2}=\sqrt{l^2-r^2}.
$$
速度“沿着连线”只说明共线，未指定朝向；两个切点处一个是沿连线靠近黄俏，另一个是沿连线远离黄俏。不能任意把两处都说成“朝向黄俏”。

**第3步：求唐鹏相对黄俏的地面速度与加速度。**

因为黄俏的地面位置恒定，以 $H$ 为原点不会改变导数。$\rho=r$ 时
$$
\begin{aligned}
\boldsymbol v_{T/H}
&=\frac{\mathrm d}{\mathrm dt}
 (r\boldsymbol e_r-l\boldsymbol e_x)
 =r\omega\boldsymbol e_\theta,\\
\boldsymbol a_{T/H}
&=\frac{\mathrm d}{\mathrm dt}
 (r\omega\boldsymbol e_\theta)
 =-r\omega^2\boldsymbol e_r.
\end{aligned}
$$
第一行的速度沿圆周切线，第二行的加速度指向圆心 $O$，不是指向黄俏。第（1）问所求大小为
$$
|\boldsymbol v_{T/H}|=\omega r,\qquad
|\boldsymbol a_{T/H}|=\omega^2r.
$$
即使该时刻速度恰沿 $HT$，加速度方向也不沿 $HT$；切线与半径垂直，二者在该时刻仍垂直。

**第4步：求黄俏在唐鹏旋转坐标中的速度与加速度。**

仍取 $\rho=r$，位置分量为
$$
X=l\cos\theta-r,\qquad Y=-l\sin\theta.
$$
这里 $r$ 为常量，但 $\theta$ 随时间变。逐项求导：
$$
\begin{aligned}
\dot X&=-\omega l\sin\theta,&
\dot Y&=-\omega l\cos\theta,\\
\ddot X&=-\omega^2l\cos\theta,&
\ddot Y&=\omega^2l\sin\theta.
\end{aligned}
$$
因此
$$
\begin{aligned}
|\boldsymbol v^{\,\mathrm{rot}}_{H/T}|
&=\sqrt{\dot X^2+\dot Y^2}
 =\omega l\sqrt{\sin^2\theta+\cos^2\theta}
 =\omega l,\\
|\boldsymbol a^{\,\mathrm{rot}}_{H/T}|
&=\sqrt{\ddot X^2+\ddot Y^2}
 =\omega^2l.
\end{aligned}
$$
这两项不依赖所选切点。若需要切点处的分量，令
$s=\pm\sqrt{1-r^2/l^2}$，代入 $\cos\theta=r/l$：
$$
\begin{aligned}
(\dot X,\dot Y)&=(-\omega ls,-\omega r),\\
(\ddot X,\ddot Y)&=(-\omega^2r,\omega^2ls).
\end{aligned}
$$
这是唐鹏坐标中的分量，不可与地面坐标分量直接逐项比较。

第（1）问的大小汇总为：唐鹏相对黄俏为 $\omega r,\omega^2r$；黄俏在唐鹏旋转坐标中为 $\omega l,\omega^2l$。若唐鹏改用不转动、只平移的坐标轴，则黄俏的速度、加速度会分别是地面唐鹏速度、加速度的反向，大小也改为 $\omega r,\omega^2r$。差异完全来自坐标约定。

**第5步：核实第（2）问的初始相位与最小距离。**

$\rho(0)=r$。由题设最小距离为 $l-r$，可知初始时 $T$ 位于 $O,H$ 之间，即 $\theta(0)=0$，而不是位于 $O$ 的另一侧。由于 $\omega$ 恒定，
$\theta=\omega t$ 与这一初始条件一致。

任意时刻 $0\leq\rho\leq r$。三角不等式给出
$$
HT\geq OH-OT=l-\rho\geq l-r.
$$
在 $\theta=0$ 时，两条不等式同时取等号。因此题设初始时刻确为全周期内的距离最小点，不能只凭图形靠近程度猜测。

**第6步：写出地面观察的完整参数轨迹。**

把变化半径代入第1步的位置公式：
$$
\begin{aligned}
x_H(t)&=\frac r2(1+\cos\theta)\cos\theta-l,\\
y_H(t)&=\frac r2(1+\cos\theta)\sin\theta,\qquad
\theta=\omega t.
\end{aligned}
$$
若使用以圆心 $O$ 为原点的辅助地面坐标，记
$x_O=x_H+l,\ y_O=y_H$，则
$$
x_O=\frac r2(1+\cos\theta)\cos\theta,\qquad
y_O=\frac r2(1+\cos\theta)\sin\theta.
$$

图1-3采用辅助原点 $O$，展示心形线的形状和关键相位；黄俏位于图中固定点 $H$。用图建立方程时，需要把该图的 $x_O$ 减去 $l$ 才得到黄俏原点下的 $x_H$，不能把两种原点的坐标混写。

![图1-3 地面坐标中的心形轨迹及固定观察点。](../figures/cardioid-01.png){width=77%}

这条轨迹的极坐标方程为 $\rho=r(1+\cos\theta)/2$，极点在 $O$。它不是半径为 $r$ 的圆。只有在不发生径向晃动的第（1）问，轨迹才是圆周。

**第7步：给出不含时间参数的地面轨迹关系，并保留正确分支。**

设 $s=\sqrt{(x_H+l)^2+y_H^2}=\rho\geq0$。当 $s>0$ 时，
$\cos\theta=(x_H+l)/s$，代入极坐标方程：
$$
\begin{aligned}
s&=\frac r2\left(1+\frac{x_H+l}{s}\right),\\
2s^2&=rs+r(x_H+l),\\
2\big[(x_H+l)^2+y_H^2\big]-r(x_H+l)
&=r\sqrt{(x_H+l)^2+y_H^2}.
\end{aligned}
$$
在 $s=0$ 的尖点，最后一式仍成立，可连续补入。最后一式是较稳妥的隐式方程，未丢失非负平方根信息。

若再平方，会得到四次关系
$$
\left\{2\big[(x_H+l)^2+y_H^2\big]-r(x_H+l)\right\}^2
=r^2\big[(x_H+l)^2+y_H^2\big].
$$
但平方后的方程必须附加左边大括号内量非负的条件，不能把原方程两边的符号信息随意删除。本题保留参数形式或未平方形式，已经完整描述轨迹，不必为求一个多项式而增加分支筛选负担。

**第8步：写出木马观察坐标中的位置，逐项整理。**

由第1步投影式：
$$
\begin{aligned}
X&=l\cos\theta-\frac r2(1+\cos\theta)\\
 &=\left(l-\frac r2\right)\cos\theta-\frac r2,\\
Y&=-l\sin\theta.
\end{aligned}
$$
为便于后续书写，定义 $A=l-r/2$。这里 $A>0$，因为 $l>r$。于是
$$
X+\frac r2=A\cos\theta,\qquad Y=-l\sin\theta.
$$
分别除以 $A$ 与 $-l$，平方后相加，用
$\cos^2\theta+\sin^2\theta=1$ 消去参数，得到
$$
\boxed{\frac{(X+r/2)^2}{(l-r/2)^2}+\frac{Y^2}{l^2}=1.}
$$

**第9步：解释椭圆中心、半轴和遍历方向。**

图1-4的坐标原点是唐鹏 $T$，椭圆的数学中心却是
$C=(-r/2,0)$。中心不在原点，不等于唐鹏“绕某固定实体圆心”观察黄俏；这只是相对坐标轨迹的中心。

![图1-4 旋转观察坐标中的偏心椭圆及相位方向。](../figures/ellipse-01.png){width=67%}

由图中的横向距离与纵向距离，椭圆横半轴为 $A=l-r/2$，纵半轴为 $l$。在 $\theta=0$ 时，黄俏的旋转坐标为
$(l-r,0)$；当 $\theta$ 稍增，$Y=-l\sin\theta<0$，所以从椭圆右端向下走，按顺时针方向遍历。地面木马逆时针旋转，与观察轨迹顺时针遍历并不矛盾。

四个相位对应的坐标为
$$
\begin{aligned}
\theta=0 &: \quad (X,Y)=(l-r,0),\\
\theta=\pi/2 &: \quad (X,Y)=(-r/2,-l),\\
\theta=\pi &: \quad (X,Y)=(-l,0),\\
\theta=3\pi/2 &: \quad (X,Y)=(-r/2,l).
\end{aligned}
$$
这些位置既核验了偏移量，也核验了 $Y$ 的负号。尤其在 $\theta=\pi$ 时，唐鹏位于 $O$；地面上的黄俏仍距 $O$ 为 $l$，但旋转径向轴指向固定地面负 $x_O$，故其坐标为 $X=-l$。

**第10步：先用倍角公式整理地面位置，降低求导错误风险。**

$\cos^2\theta=(1+\cos2\theta)/2$，
$\sin\theta\cos\theta=\sin2\theta/2$。因而
$$
\begin{aligned}
x_H
&=\frac r2\cos\theta+\frac r2\cos^2\theta-l\\
&=\frac r2\cos\theta+\frac r4+\frac r4\cos2\theta-l,\\
y_H
&=\frac r2\sin\theta+\frac r2\sin\theta\cos\theta\\
&=\frac r2\sin\theta+\frac r4\sin2\theta.
\end{aligned}
$$
这一步没有作小量近似。它把原来的两个乘积改写为独立谐波项，使第二谐波的求导系数能够清楚跟踪。

**第11步：逐项求地面速度，说明第二谐波的系数。**

对 $\cos2\theta=\cos(2\omega t)$ 求导时，链式法则给出
$-2\omega\sin2\theta$；它前面的系数为 $r/4$，两者相乘得到 $-r\omega\sin2\theta/2$，不是 $-r\omega\sin2\theta$。完整过程为
$$
\begin{aligned}
v_{T/H,x}
&=-\frac{r\omega}{2}\sin\theta
  -\frac r4\,2\omega\sin2\theta\\
&=-\frac{r\omega}{2}(\sin\theta+\sin2\theta),\\
v_{T/H,y}
&=\frac{r\omega}{2}\cos\theta
  +\frac r4\,2\omega\cos2\theta\\
&=\frac{r\omega}{2}(\cos\theta+\cos2\theta).
\end{aligned}
$$
位置中 $-l$ 为常量，其导数为零。因此唐鹏相对固定黄俏的地面速度不含 $l$；不是两人距离不影响观察，而是固定原点的平移不改变速度。

**第12步：从速度再求导，得到地面加速度。**

现在第二谐波前面的系数已变为 $r\omega/2$。再求导会再产生因子 $2\omega$，故加速度括号内第二谐波确实带系数 $2$：
$$
\begin{aligned}
a_{T/H,x}
&=-\frac{r\omega}{2}
  \left(\omega\cos\theta+2\omega\cos2\theta\right)\\
&=-\frac{r\omega^2}{2}
  \left(\cos\theta+2\cos2\theta\right),\\
a_{T/H,y}
&=\frac{r\omega}{2}
  \left(-\omega\sin\theta-2\omega\sin2\theta\right)\\
&=-\frac{r\omega^2}{2}
  \left(\sin\theta+2\sin2\theta\right).
\end{aligned}
$$
横、纵分量前面的分母都为 $2$。速度中的第二谐波系数为 $1$、加速度中的第二谐波系数为 $2$，它们处在不同求导层次，不能凭外观一致去统一成同一个数字。

**第13步：不用倍角式，直接以乘积求导复核横向速度。**

从原位置 $x_H=r(1+\cos\theta)\cos\theta/2-l$ 重新计算：
$$
\begin{aligned}
\dot x_H
&=\frac r2\left[
 -\omega\sin\theta\cos\theta
 -(1+\cos\theta)\omega\sin\theta\right]\\
&=-\frac{r\omega}{2}
 \left(\sin\theta+2\sin\theta\cos\theta\right)\\
&=-\frac{r\omega}{2}\left(\sin\theta+\sin2\theta\right).
\end{aligned}
$$
注意中间出现的是 $2\sin\theta\cos\theta=\sin2\theta$，不是
$2\sin2\theta$。两条独立的代数路线在这里给出相同结果。

对 $y_H$ 同样作乘积求导：
$$
\begin{aligned}
\dot y_H
&=\frac{r\omega}{2}
 \left[-\sin^2\theta+(1+\cos\theta)\cos\theta\right]\\
&=\frac{r\omega}{2}
 \left[\cos\theta+\cos^2\theta-\sin^2\theta\right]\\
&=\frac{r\omega}{2}\left(\cos\theta+\cos2\theta\right).
\end{aligned}
$$

**第14步：计算木马旋转观察坐标中的速度与加速度。**

第8步已得 $X=A\cos\theta-r/2,\ Y=-l\sin\theta$。$A$ 为常量，故
$$
\boxed{
\begin{aligned}
\dot X&=-\omega A\sin\theta,\\
\dot Y&=-\omega l\cos\theta,\\
\ddot X&=-\omega^2 A\cos\theta,\\
\ddot Y&=\omega^2 l\sin\theta,
\qquad A=l-\frac r2.
\end{aligned}}
$$
相应的大小为
$$
\begin{aligned}
v^{\,\mathrm{rot}}_{H/T}
&=\omega\sqrt{A^2\sin^2\theta+l^2\cos^2\theta},\\
a^{\,\mathrm{rot}}_{H/T}
&=\omega^2\sqrt{A^2\cos^2\theta+l^2\sin^2\theta}.
\end{aligned}
$$
这两项不是常量；第（1）问圆轨迹中的恒定大小不能直接沿用到第（2）、（3）问的椭圆轨迹。

**第15步：用极坐标速度分解核验第（3）问。**

图1-5左侧把地面速度拆成径向移动和木马切向运动，右侧把地面加速度拆成径向、切向两项。箭头是分量的首尾相接，不是另加外力；本题只做运动学分析。

![图1-5 变化半径运动的速度与加速度分解。](../figures/polar-01.png){width=92%}

按图中的基矢分解，位置为 $\rho\boldsymbol e_r$，求导得到
$$
\begin{aligned}
\boldsymbol v_{T/H}
&=\dot\rho\boldsymbol e_r+\rho\dot{\boldsymbol e}_r\\
&=\dot\rho\boldsymbol e_r+\rho\omega\boldsymbol e_\theta,\\
\dot\rho&=-\frac{r\omega}{2}\sin\theta.
\end{aligned}
$$
径向项投到地面 $x$ 方向为 $-r\omega\sin\theta\cos\theta/2$，
切向项投到同一方向为 $-r\omega(1+\cos\theta)\sin\theta/2$。
两项相加正是第13步的结果。纵向分量也给出第11步的 $v_y$，因而不是另一个速度模型。

**第16步：推导极坐标加速度，追踪因子 $2$ 的物理来源。**

继续对速度向量求导，不能把随时间旋转的基矢当成常量：
$$
\begin{aligned}
\boldsymbol a_{T/H}
&=\ddot\rho\boldsymbol e_r
 +\dot\rho\,\omega\boldsymbol e_\theta
 +\dot\rho\,\omega\boldsymbol e_\theta
 -\rho\omega^2\boldsymbol e_r\\
&=(\ddot\rho-\rho\omega^2)\boldsymbol e_r
  +2\omega\dot\rho\boldsymbol e_\theta,\\
\ddot\rho&=-\frac{r\omega^2}{2}\cos\theta.
\end{aligned}
$$
两项切向贡献分别来自径向速度方向的转动，以及切向速度大小随半径变化；它们相等，所以相加为 $2\omega\dot\rho$。本题 $\dot\omega=0$，否则还会有 $\rho\dot\omega$ 切向项。

代入 $\rho,\dot\rho,\ddot\rho$：
$$
a_r=-\frac{r\omega^2}{2}(1+2\cos\theta),\qquad
a_\theta=-r\omega^2\sin\theta.
$$
再投影到地面坐标：
$$
\begin{aligned}
a_x&=a_r\cos\theta-a_\theta\sin\theta\\
&=-\frac{r\omega^2}{2}
 [\cos\theta+2\cos^2\theta-2\sin^2\theta]\\
&=-\frac{r\omega^2}{2}(\cos\theta+2\cos2\theta),\\
a_y&=a_r\sin\theta+a_\theta\cos\theta\\
&=-\frac{r\omega^2}{2}
 [\sin\theta+4\sin\theta\cos\theta]\\
&=-\frac{r\omega^2}{2}(\sin\theta+2\sin2\theta).
\end{aligned}
$$
与第12步完全一致。图中的 $a_\theta$ 可以为负，此时指向负切向；不能把“切向分量”理解为始终沿运动方向的正分量。

**第17步：求地面速率与加速度大小，区分尖点与椭圆运动。**

极坐标两分量正交，所以
$$
\begin{aligned}
v_{T/H}^2
&=\dot\rho^2+\rho^2\omega^2\\
&=\frac{r^2\omega^2}{4}
 [\sin^2\theta+(1+\cos\theta)^2]\\
&=\frac{r^2\omega^2}{2}(1+\cos\theta)
 =r^2\omega^2\cos^2\frac\theta2.
\end{aligned}
$$
故
$$
v_{T/H}=r\omega\left|\cos\frac\theta2\right|.
$$
平方根必须取非负值，不能删去绝对值而使半个周期的速率成为负数。

加速度大小同理由正交分量求得：
$$
\begin{aligned}
a_{T/H}^2
&=\frac{r^2\omega^4}{4}
 \left[(1+2\cos\theta)^2+4\sin^2\theta\right]\\
&=\frac{r^2\omega^4}{4}(5+4\cos\theta),\\
a_{T/H}&=\frac{r\omega^2}{2}\sqrt{5+4\cos\theta}.
\end{aligned}
$$
括号内最小为 $1$，因此该地面加速度全周期不为零。地面速度在尖点为零，并不意味着地面加速度也为零。

**第18步：检查两个典型相位，避免只检查零项。**

在 $\theta=0$ 时，
$$
\begin{aligned}
\rho&=r,& \dot\rho&=0,& \ddot\rho&=-r\omega^2/2,\\
(v_x,v_y)&=(0,r\omega),&
(a_x,a_y)&=(-3r\omega^2/2,0).
\end{aligned}
$$
这一加速度的径向大小比固定半径圆周运动多出 $r\omega^2/2$，来自正在开始向内的径向晃动。不能仍套用 $r\omega^2$ 作为总加速度。

在 $\theta=\pi/2$ 时，
$$
\begin{aligned}
(v_x,v_y)&=(-r\omega/2,-r\omega/2),\\
(a_x,a_y)&=(r\omega^2,-r\omega^2/2),\\
(\dot X,\dot Y)&=(-\omega A,0),\\
(\ddot X,\ddot Y)&=(0,\omega^2l).
\end{aligned}
$$
这是检查纵向加速度分母的有效时刻，因为 $a_y$ 不为零。若只检查 $\theta=0,\pi$，错误分母乘上零项也会显得“正确”。

**第19步：解释尖点时刻的坐标延拓与速度差异。**

$\theta=\pi$ 时 $\rho=0$，唐鹏到达 $O$，其地面速度为零：
$$
(v_x,v_y)=(0,0),\qquad (a_x,a_y)=(-r\omega^2/2,0).
$$
但旋转坐标中的黄俏并未停止：
$$
(X,Y)=(-l,0),\qquad
(\dot X,\dot Y)=(0,\omega l).
$$
因为唐鹏的观察轴仍随木马转动。若把坐标方向定义为实际合速度方向，则此刻速度为零，朝向没有定义，不能照搬上述平滑椭圆模型。

为避免 $\rho=0$ 时用“从 $O$ 指向 $T$”定义方向的几何不确定性，本题把基矢由木马相位 $\theta$ 定义，并连续通过尖点。这一处理保留了旋转机构提供的方向信息，不是凭空给静止质点添速度。

**第20步：以同一时间参数比较两种观察速率。**

图1-6取 $l=2r$，画出地面唐鹏速率与旋转坐标黄俏速率。横轴都为 $\theta/\pi$，纵轴都以同一个 $r\omega$ 归一化，因而可以直接比较大小。

![图1-6 地面观察与旋转观察速率的对比，示例取 $l=2r$。](../figures/rates-01.png){width=78%}

图中地面曲线在 $\theta=\pi$ 触零，对应心形线尖点；旋转曲线始终在 $1.5$ 与 $2$ 之间，对应
$A/r=1.5,\ l/r=2$。用图中的数值代入第14、17步的速率公式，恰得到这两个范围。该图说明的是不同观察坐标的导数，不是在同一坐标系给同一速度赋予两个互相矛盾的大小。

**第21步：量纲、周期与无径向晃动极限检查。**

所有速度均为长度乘 $\omega$，所有加速度均为长度乘 $\omega^2$；位置、速度、加速度都以 $2\pi/\omega$ 为周期。轨迹消参式两项均无量纲，椭圆式右端为 $1$。

若取消径向晃动而改为 $\rho=r$ 常量，第1步的一般投影式恢复为
$X=l\cos\theta-r,\ Y=-l\sin\theta$，旋转轨迹成为圆心 $(-r,0)$、半径 $l$ 的圆，速率为 $\omega l$；地面轨迹恢复半径 $r$ 的圆，速率为 $\omega r$。这与第（1）问完全一致。

注意不能只在第（2）问某一瞬间取 $\rho=r$，就宣称回到无晃动模型。该瞬间仍有 $\ddot\rho\ne0$，加速度并不相同。恢复固定半径模型必须使 $\rho$ 在一段时间内恒定，即 $\dot\rho=\ddot\rho=0$。

## 六、关键洞察

**洞察1：相对位置互为相反，不保证不同观察坐标的导数互为相反。**

若所有向量都在同一固定地面基底中求导，确有
$\boldsymbol v_{H}-\boldsymbol v_T=-(\boldsymbol v_T-\boldsymbol v_H)$。
但本题唐鹏坐标中的分量包含随时间改变的基矢投影，求导时额外产生基矢转动项。数学上差的是一个旋转变换的导数，而不是牛顿运动学的一条例外。

用旋转矩阵表示坐标变换。令
$$
Q=\begin{pmatrix}\cos\theta&-\sin\theta\\
\sin\theta&\cos\theta\end{pmatrix},\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
$$
$Q$ 把旋转分量映成地面分量，$Q^{\mathsf T}$ 反向投影。
相对旋转坐标列向量 $\boldsymbol R=(X,Y)^{\mathsf T}$ 满足
$$
\boldsymbol R=Q^{\mathsf T}(\boldsymbol H-\boldsymbol T).
$$
由于 $\dot Q=\omega QJ$、$\dot Q^{\mathsf T}=-\omega JQ^{\mathsf T}$，
逐项求导得到
$$
\dot{\boldsymbol R}
=Q^{\mathsf T}(\boldsymbol v_H-\boldsymbol v_T)-\omega J\boldsymbol R.
$$
前一项是两质点实际地面速度之差的投影；后一项才是观察轴转动带来的差别。

**洞察2：由一般运输公式重新核验完整速度、加速度。**

题设 $\boldsymbol v_H=0$，地面唐鹏速度投到旋转基底为
$(\dot\rho,\omega\rho)^{\mathsf T}$。因此
$$
\begin{aligned}
\dot X&=-\dot\rho+\omega Y
 =\frac{r\omega}{2}\sin\theta-\omega l\sin\theta
 =-\omega A\sin\theta,\\
\dot Y&=-\omega\rho-\omega X
 =-\omega(\rho+l\cos\theta-\rho)
 =-\omega l\cos\theta.
\end{aligned}
$$
$X$ 中有原点平移贡献与轴转动贡献，二者在 $Y$ 的导数中恰好消去了 $\rho$，这是相消结果而不是忽略径向移动。

再求导运输式，在 $\omega$ 恒定时得
$$
\ddot{\boldsymbol R}
=Q^{\mathsf T}(\boldsymbol a_H-\boldsymbol a_T)
 -2\omega J\dot{\boldsymbol R}
 +\omega^2\boldsymbol R.
$$
其中 $-2\omega J\dot{\boldsymbol R}$ 是旋转导数的两次交叉贡献，
$+\omega^2\boldsymbol R$ 的正号来自 $J^2=-I$。本题只做运动学转换；若把这些项移到非惯性动力学方程一侧，才会作为科里奥利与离心惯性力出现，不能在此提前把它们叫作真实接触力。

逐分量代入：
$$
\begin{aligned}
\ddot X
&=-\ddot\rho+\omega^2\rho+2\omega\dot Y+\omega^2X\\
&=-\ddot\rho+\omega^2\rho-2\omega^2l\cos\theta
 +\omega^2(l\cos\theta-\rho)\\
&=-\ddot\rho-\omega^2l\cos\theta
 =-\omega^2A\cos\theta,\\
\ddot Y
&=-2\omega\dot\rho-2\omega\dot X+\omega^2Y\\
&=r\omega^2\sin\theta+2\omega^2A\sin\theta
 -\omega^2l\sin\theta\\
&=\omega^2l\sin\theta.
\end{aligned}
$$
直接求导、极坐标分解、运输公式三条路线相互一致，可以分别检查谐波系数、基矢符号和原点移动项。

**洞察3：旋转坐标中的椭圆是一个仿射化的圆参数。**

相对于椭圆中心，令 $U=X+r/2,\ V=Y$，则
$U=A\cos\theta,\ V=-l\sin\theta$。将 $U,V$ 分别除以半轴，
得到 $(U/A,V/l)=(\cos\theta,-\sin\theta)$，它是匀角速率遍历的单位圆。实际椭圆弧长并不是均匀增加，所以“参数角匀速”不等于“沿椭圆匀速”。

对中心坐标再求二阶导数，
$$
\ddot U=-\omega^2U,\qquad \ddot V=-\omega^2V.
$$
因此旋转观察加速度指向数学中心 $C$，大小为
$\omega^2\sqrt{U^2+V^2}$。这与第14步的大小式相同，但不能据此认定黄俏受到了指向 $C$ 的真实弹性力；黄俏在地面静止，曲线及导数出自坐标变换。

**洞察4：真正始终面向合速度会改变轨迹，而不仅改变标签。**

在 $-\pi<\theta<\pi$，用和差化积把地面速度整理为
$$
\begin{aligned}
v_x&=-r\omega\cos\frac\theta2\sin\frac{3\theta}{2},\\
v_y&=r\omega\cos\frac\theta2\cos\frac{3\theta}{2}.
\end{aligned}
$$
这一区间 $\cos(\theta/2)>0$，实际速度方向角为
$\beta=3\theta/2+\pi/2$，其转动速率为 $3\omega/2$，不是 $\omega$。

若一个坐标轴始终沿实际速度，则相对向量要乘以
$Q(\beta)^{\mathsf T}$，而非本题的 $Q(\theta)^{\mathsf T}$。两者相差一个随时间变化的转角，所得轨迹一般不再是第8步的椭圆；尖点处实际速度为零，坐标朝向还会失去定义。这解释了为何必须先明确题干的观察模型，不能用“给图补上前进标签”来掩盖条件差异。

## 七、易错点

把相对速度一律写成互为反向，只在共同固定基底的定义下成立；旋转观察坐标还含轴转动项。检查时应先标记每个向量的基底，不能先算完再凭大小判断哪个答案“像对的”。

以圆心 $O$ 作图后，把图上的 $x_O$ 直接说成黄俏观察坐标，漏掉原点平移 $x_H=x_O-l$。常量平移不影响速度，却会影响轨迹位置和尖点坐标。

写旋转坐标投影时漏减唐鹏本人的径向位置，错误地写成 $X=l\cos\theta$；这样得不到偏心椭圆，也无法恢复第（1）问的圆心偏移。

把 $2\sin\theta\cos\theta$ 误当成 $2\sin2\theta$，使速度的第二谐波系数多一倍。必须先使用 $\sin2\theta=2\sin\theta\cos\theta$，再检查求导所产生的链式因子。

从速度求加速度时混淆两个求导层次，或者把纵向加速度的分母写成 $3$。可用 $\theta=\pi/2$ 使错误项不为零，直接检验；只代入全部正弦项为零的时刻不能发现此类错误。

将速率 $r\omega|\cos(\theta/2)|$ 的导数当成向量加速度。速率导数只描述沿速度方向的加速度分量，还缺少运动方向转动的贡献。

把极坐标基矢视为不变，漏掉向心项或 $2\omega\dot\rho$ 切向项；图1-5中的径向、切向分量对应明确的基矢导数，不能只凭箭头猜系数。

认定地面速度为零时，旋转坐标中的相对速度也必须为零。尖点处的对照已显示：轴继续转动，旋转观察导数可非零。

把第（1）问的切线条件套入第（2）问全部时刻，强迫合速度一直沿两人连线。切线条件只用于第（1）问规定的某个瞬时位置。

## 八、课堂讲解建议

课堂开始先让学生分别描述“用始终朝北的相机看运动的人”和“转动相机看地面上的人”。板书上同时写“原点是谁”与“轴是否转动”，再讨论相对速度。教师应避免仅说“参考系不同”而不交代具体求导定义，因为这种说法仍不能指导学生建立方程。

第一轮让学生只用位置投影完成 $X=l\cos\theta-\rho,\ Y=-l\sin\theta$。可在图1-2上分别指出 $H$ 的径向投影与唐鹏原点的径向位置，解释相减；不要跳到最后椭圆式，再倒过来补一个坐标图。

第二轮在黑板同一列依次写位置、速度、加速度，使 $r/4$ 的第二谐波系数、首次求导产生的 $2\omega$、再次求导产生的 $2\omega$ 各有对应位置。课堂核验宜选 $\theta=\pi/4$ 检查横向速度，选 $\theta=\pi/2$ 检查纵向加速度，不能只在零项处验证。

第三轮利用图1-5做基矢求导。教师可先固定 $\rho$，得到向心项，再允许 $\rho$ 改变，逐一指出两个切向交叉项。这样学生能够理解因子 $2$ 的来源，而不是记忆极坐标加速度公式。

最后使用图1-6比较两条曲线，并让学生解释 $\theta=\pi$ 时各自的测量含义。课堂提问可为：“唐鹏这一瞬间在地面上不动，为什么他转动坐标中的黄俏还在动？”解答应落在“坐标轴仍然转动”，而不是引入黄俏的真实运动或额外受力。若讨论实际身体朝向，应明确它属于另一套模型，不能把身体转向与木马相位混为同一角度。

## 九、变式训练

**变式1：唐鹏采用只平移、不旋转的观察坐标。**

题设运动规律不变，但唐鹏坐标轴始终与固定地面轴平行。求黄俏在该坐标中的轨迹、速度、加速度，并与旋转坐标比较。

完整解答：令唐鹏平移坐标为 $(\xi,\eta)$，则
$$
\begin{aligned}
\xi&=l-\rho\cos\theta=-x_H,\\
\eta&=-\rho\sin\theta=-y_H.
\end{aligned}
$$
反向相对位置在相同基底中的分量恰互为负。因此
$$
\begin{aligned}
\dot\xi&=\frac{r\omega}{2}(\sin\theta+\sin2\theta),\\
\dot\eta&=-\frac{r\omega}{2}(\cos\theta+\cos2\theta),\\
\ddot\xi&=\frac{r\omega^2}{2}(\cos\theta+2\cos2\theta),\\
\ddot\eta&=\frac{r\omega^2}{2}(\sin\theta+2\sin2\theta).
\end{aligned}
$$
平移观察轨迹是地面相对轨迹关于原点的中心反演，并不是旋转观察中的椭圆。速度、加速度大小与地面唐鹏的对应量完全相同。在 $\theta=\pi$ 处，平移坐标观察速度也为零，而共转坐标观察速度为 $\omega l$。两者给出可直接检验的模型区分。

**变式2：径向规律改为 $\rho=a+b\cos\theta$。**

取 $a>b>0$，$l>a+b$，仍用木马共转坐标。求轨迹及相对速度、加速度，并判断椭圆何时退化。

完整解答：首先写一般投影：
$$
X=l\cos\theta-(a+b\cos\theta)=(l-b)\cos\theta-a,\qquad
Y=-l\sin\theta.
$$
因此
$$
\frac{(X+a)^2}{(l-b)^2}+\frac{Y^2}{l^2}=1,
$$
中心为 $(-a,0)$，半轴分别为 $l-b,l$。求导：
$$
\begin{aligned}
\dot X&=-\omega(l-b)\sin\theta,&
\dot Y&=-\omega l\cos\theta,\\
\ddot X&=-\omega^2(l-b)\cos\theta,&
\ddot Y&=\omega^2l\sin\theta.
\end{aligned}
$$
在本变式给定条件下 $l-b>a>0$，椭圆不退化。形式上若放宽几何约束到 $l=b$，横向分量恒为 $-a$，轨迹退化为竖直线段；此时不能再除以 $l-b$ 写椭圆标准式。若 $b=0$，半轴相等，轨迹为中心 $(-a,0)$、半径 $l$ 的圆，对应无径向晃动。

地面速度可由 $\dot\rho=-b\omega\sin\theta$ 写成
$$
\begin{aligned}
v_x&=-\omega\sin\theta(a+2b\cos\theta),\\
v_y&=\omega[a\cos\theta+b(\cos^2\theta-\sin^2\theta)].
\end{aligned}
$$
加速度则先计算 $\ddot\rho=-b\omega^2\cos\theta$，再代入一般极坐标公式：
$$
\begin{aligned}
a_r&=-\omega^2(a+2b\cos\theta),\\
a_\theta&=-2b\omega^2\sin\theta,\\
a_x&=-\omega^2[a\cos\theta+2b\cos2\theta],\\
a_y&=-\omega^2[a\sin\theta+2b\sin2\theta].
\end{aligned}
$$
取 $a=b=r/2$ 即恢复主问题；该极限 $\rho$ 可以为零，但由相位定义的共转基矢仍可连续延拓。

**变式3：求共转坐标中的速率、加速度极值及发生位置。**

仍取主问题 $A=l-r/2$。求黄俏共转观察速率和加速度大小的最大、最小值，不使用对平方根的冗长求导。

完整解答：因为 $0<A<l$，
$$
\begin{aligned}
(v^{\,\mathrm{rot}}_{H/T})^2
&=\omega^2[A^2+(l^2-A^2)\cos^2\theta],\\
(a^{\,\mathrm{rot}}_{H/T})^2
&=\omega^4[A^2+(l^2-A^2)\sin^2\theta].
\end{aligned}
$$
括号中正系数 $l^2-A^2$ 已确定，且 $\sin^2,\cos^2$ 的取值范围为 $[0,1]$。平方根在非负区间单调增加，因此
$$
\begin{aligned}
v_{\min}&=\omega A,& v_{\max}&=\omega l,\\
a_{\min}&=\omega^2 A,& a_{\max}&=\omega^2l.
\end{aligned}
$$
速率最小发生于 $\theta=\pi/2,3\pi/2$，最大于 $\theta=0,\pi$；加速度极值的相位恰相反。速率最小时位于椭圆上下端，加速度最大；速率最大时位于左右端，加速度最小。这里匀速的是参数角，不是弧长速度。

若取图1-6的 $l=2r$，则 $A=3r/2$，共转速率范围为
$[1.5r\omega,2r\omega]$，与图中曲线一致；地面唐鹏速率却在
$[0,r\omega]$ 中变化。两条曲线各有其明确的观察定义。

**变式4：在 $\theta=\pi/4$ 检查横向速度的第二谐波系数。**

取 $r=2\,\mathrm m$，$\omega=1\,\mathrm{s^{-1}}$，只用原位置作乘积求导，计算地面横向速度。

完整解答：这一时刻
$\sin\theta=\cos\theta=\sqrt2/2$，$\sin2\theta=1$。用主解析第13步的原位置导数：
$$
\begin{aligned}
v_x&=-\frac{r\omega}{2}
 \left[\sin\theta\cos\theta+(1+\cos\theta)\sin\theta\right]\\
&=-1\left[\frac12+
 \left(1+\frac{\sqrt2}{2}\right)\frac{\sqrt2}{2}\right]
 \mathrm{m\,s^{-1}}\\
&=-\left(1+\frac{\sqrt2}{2}\right)\mathrm{m\,s^{-1}}
 \approx-1.70710678\,\mathrm{m\,s^{-1}}.
\end{aligned}
$$
若错误地把速度写成
$-r\omega(\sin\theta+2\sin2\theta)/2$，会得到
$-2.70710678\,\mathrm{m\,s^{-1}}$，与原位置差分不符。此检验选择第二谐波不为零的时刻，能够区分两个候选系数；用 $\theta=\pi/2$ 则第二谐波恰为零，无法检查这一错误。

<!-- draft-content-complete: 3个主分问及4个带解变式已写全；模型授权、当前图稿及PDF视觉验收另计，未验收。 -->
