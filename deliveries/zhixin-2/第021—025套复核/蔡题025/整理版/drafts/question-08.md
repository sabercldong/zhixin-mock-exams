# 第 8 题

<!-- question-start -->
质量为 $m$、电荷量为 $q$的粒子被光滑约束限制在半径为 $R_0$的圆柱面上运动，圆柱轴沿 $z$方向。空间存在均匀磁场

$$\boldsymbol B=B\boldsymbol e_x.$$

使用柱坐标，径向和圆周方向的单位矢量为

$$\boldsymbol e_s=\cos\phi\,\boldsymbol e_x+\sin\phi\,\boldsymbol e_y,\qquad
\boldsymbol e_\phi=-\sin\phi\,\boldsymbol e_x+\cos\phi\,\boldsymbol e_y,$$

位置为 $\boldsymbol r=R_0\boldsymbol e_s+z\boldsymbol e_z$。定义带符号的 $\omega_c=qB/m$。

（a）由牛顿定律求 $\phi,z,\dot\phi,\dot z,\ddot\phi,\ddot z$满足的两个运动方程。

（b）已知 $\phi(0)=0$、$\dot z(0)=R_0\omega_z$，求 $\dot z$与 $\phi$的关系。

（c）再给 $\dot\phi(0)=\omega_\phi$：

（i）证明 $\dot\phi^2+\omega_c^2\sin^2\phi-2\omega_c\omega_z\sin\phi-\omega_\phi^2=0$。

（ii）若 $\omega_z,\omega_\phi$均非零，求能使粒子按螺旋线运动的 $\omega_c$条件。

（iii）若 $\omega_\phi\ne0$、$\omega_z=0$，求粒子轨迹闭合所需的 $\omega_c$条件。

模型约定：约束只施加径向力且可以维持粒子在柱面上，不考虑脱离和摩擦。“螺旋线”若严格指等螺距曲线，与连续绕轴但螺距可变的曲线不同；解析分别讨论，不用同一条件代替两种定义。

![图 8-1　真实圆柱面、横向磁场、柱坐标及初始速度分量。](../figures/question-08.png)
<!-- question-end -->

## 一、题型定位

曲面约束中的洛伦兹力与一维有效势运动。粒子虽然只有两个自由度，但其空间速度和磁场不能用平面示意替代。洛伦兹力将圆周速度和轴向速度耦合，径向约束承担维持柱面的任务。

## 二、知识点

旋转单位矢量；柱坐标速度与加速度；洛伦兹力叉乘；约束力不做功；第一积分；能量守恒；有效势与转向点；绕轴运动、振荡和分离轨道；闭合曲线；椭圆积分周期。

$\omega_c$随电荷正负改变符号。分类条件常依赖 $|\omega_c|$，但实际轴向运动方向依赖其符号，不能在运动方程里提前将它换成正数。

## 三、物理图像

横向磁场相对粒子的径向、圆周方向的分量随 $\phi$变化。轴向速度产生圆周洛伦兹力，圆周速度又产生轴向洛伦兹力，所以一般既不是匀速绕圈，也不是匀速沿轴移动。

把柱面沿母线剪开并展开，横坐标为 $R_0\phi$、纵坐标为 $z$。严格等螺距螺旋线应在展开图上成为直线；一般绕轴轨迹则是斜率随位置改变的曲线。原柱面的可见前后边界和展开坐标是两种互补图像，不能把展开图误认为空间中的平面轨迹。

## 四、解题入口

先对基矢求导，保留径向加速度 $-R_0\dot\phi^2$。将磁场展开到 $\boldsymbol e_s,\boldsymbol e_\phi,\boldsymbol e_z$，逐项叉乘，只把切向和轴向分量用于两条运动方程。

轴向方程先积分一次得到 $\dot z=R_0(\omega_z-\omega_c\sin\phi)$，再用不做功得到能量第一积分。之后用 $\dot\phi^2$能否为零来区分连续绕轴与转向；闭合性还要检查一段角运动周期内轴向位移是否为零。

## 五、解析

（1）先求随位置旋转的基矢导数。

由基矢定义，对时间求导：

$$\begin{aligned}
\dot{\boldsymbol e}_s
&=\dot\phi(-\sin\phi\,\boldsymbol e_x
          +\cos\phi\,\boldsymbol e_y)
=\dot\phi\,\boldsymbol e_\phi,\\
\dot{\boldsymbol e}_\phi
&=\dot\phi(-\cos\phi\,\boldsymbol e_x
          -\sin\phi\,\boldsymbol e_y)
=-\dot\phi\,\boldsymbol e_s.
\end{aligned}$$

半径恒定，所以

$$\boldsymbol v=R_0\dot\phi\,\boldsymbol e_\phi+\dot z\,\boldsymbol e_z.$$

再求导，既要导系数也要导单位矢量：

$$\begin{aligned}
\boldsymbol a
&=R_0\ddot\phi\,\boldsymbol e_\phi
  +R_0\dot\phi\,\dot{\boldsymbol e}_\phi
  +\ddot z\,\boldsymbol e_z\\
&=-R_0\dot\phi^2\,\boldsymbol e_s
  +R_0\ddot\phi\,\boldsymbol e_\phi
  +\ddot z\,\boldsymbol e_z.
\end{aligned}$$

半径不变并不意味着径向加速度为零；第一项正是维持柱面运动的向心加速度。

（2）展开磁场并逐项作叉乘。

反变换为

$$\boldsymbol e_x=\cos\phi\,\boldsymbol e_s-\sin\phi\,\boldsymbol e_\phi,$$

因此

$$\boldsymbol B=B(\cos\phi\,\boldsymbol e_s-\sin\phi\,\boldsymbol e_\phi).$$

使用右手基底 $(\boldsymbol e_s,\boldsymbol e_\phi,\boldsymbol e_z)$，有 $\boldsymbol e_\phi\times\boldsymbol e_s=-\boldsymbol e_z$、$\boldsymbol e_z\times\boldsymbol e_s=\boldsymbol e_\phi$、$\boldsymbol e_z\times\boldsymbol e_\phi=-\boldsymbol e_s$。逐项相乘：

$$\begin{aligned}
q\boldsymbol v\times\boldsymbol B
={}&-qBR_0\dot\phi\cos\phi\,\boldsymbol e_z\\
&+qB\dot z\cos\phi\,\boldsymbol e_\phi\\
&+qB\dot z\sin\phi\,\boldsymbol e_s.
\end{aligned}$$

图 8-2 以横截面显示当地基底，磁场分解中的圆周分量是 $-B\sin\phi$。此负号与叉乘中的另一个负号相乘后，径向洛伦兹力为正的 $qB\dot z\sin\phi$。

![图 8-2　柱面横截面的当地基底与磁场的径向、圆周分解。](../figures/basis-08.png)

（3）写两条运动方程及径向约束力。

设约束力为 $N\boldsymbol e_s$，$N$带正负号。切向、轴向的牛顿第二定律分别为

$$mR_0\ddot\phi=qB\dot z\cos\phi,\qquad
m\ddot z=-qBR_0\dot\phi\cos\phi.$$

除以相应系数，得第（a）问：

$$\boxed{\ddot\phi=\frac{\omega_c}{R_0}\dot z\cos\phi,\qquad
\ddot z=-R_0\omega_c\dot\phi\cos\phi.}$$

径向方程另给

$$-mR_0\dot\phi^2=N+qB\dot z\sin\phi,$$

即 $N=-mR_0\dot\phi^2-qB\dot z\sin\phi$。这不增加新的自由度，而是确定约束所需的径向力。若圆柱接触只能推不能拉，就要另检验这一力是否可实现；当前题目采用保持在柱面的双向理想约束。

（4）先积分轴向方程，使用初始条件。

因为 $d(\sin\phi)/dt=\dot\phi\cos\phi$，轴向方程可写成

$$\frac{d}{dt}\left(\dot z+R_0\omega_c\sin\phi\right)=0.$$

括号内为常量。代入 $\phi(0)=0$、$\dot z(0)=R_0\omega_z$，得到

$$\boxed{\dot z=R_0(\omega_z-\omega_c\sin\phi).}$$

这是第（b）问。它在角运动转向处同样成立，因为推导没有除以 $\dot\phi$，也没有要求 $\phi$单调。

（5）由不做功取得能量积分。

洛伦兹力总与速度垂直，径向约束也与柱面切向速度垂直，因此

$$\frac{d}{dt}\left[\frac12m(R_0^2\dot\phi^2+\dot z^2)\right]=0.$$

用初态确定常量，并除以 $mR_0^2/2$：

$$\dot\phi^2+\frac{\dot z^2}{R_0^2}
=\omega_\phi^2+\omega_z^2.$$

代入轴向第一积分：

$$\dot\phi^2+(\omega_z-\omega_c\sin\phi)^2
=\omega_\phi^2+\omega_z^2.$$

展开平方、消去两边的 $\omega_z^2$：

$$\boxed{\dot\phi^2+\omega_c^2\sin^2\phi
-2\omega_c\omega_z\sin\phi-\omega_\phi^2=0.}$$

这完成第（c）（i）问。加号来自轴向速度的平方，交叉项的负号来自第一积分中的减号。

也可用两条二阶方程直接检验：$d(\dot\phi^2+\dot z^2/R_0^2)/dt$中的两项分别为 $2\omega_c\dot\phi\dot z\cos\phi/R_0$和它的相反数，严格抵消。这与数值积分二阶运动方程的能量残差检查独立对应。

（6）明确严格螺旋线与一般绕轴运动。

严格圆柱螺旋线写作 $z-z_0=p\phi$，其中 $p$为固定非零螺距参数。如果粒子速率恒定，则

$$v^2=(R_0^2+p^2)\dot\phi^2$$

要求非零 $\dot\phi$恒定，进而 $\dot z=p\dot\phi$也恒定。但轴向方程要求

$$0=\ddot z=-R_0\omega_c\dot\phi\cos\phi.$$

一条不断绕轴的轨道会经过各种 $\phi$，$\cos\phi$不可能始终为零。所以在 $\omega_\phi,\omega_z$均非零时，严格等螺距螺旋线需要

$$\boxed{\omega_c=0.}$$

此时 $\phi=\omega_\phi t$、$z=z_0+R_0\omega_z t$，螺距每转为 $2\pi R_0\omega_z/\omega_\phi$，确实恒定。

若题意把“螺旋线”宽泛地用作连续绕轴并沿轴漂移的轨迹，则应改用下一段的绕轴条件。不能仅从图上像螺旋就忽略螺距是否恒定。

（7）求完整绕轴而不转向的条件。

记 $\Omega=\sqrt{\omega_\phi^2+\omega_z^2}>0$，有

$$\dot\phi^2=Q(\phi)
=\Omega^2-(\omega_z-\omega_c\sin\phi)^2.$$

完整绕轴要求所有角度均可到达且 $\dot\phi$不为零，即 $\min_\phi Q(\phi)>0$。因 $\sin\phi$遍历 $[-1,1]$，

$$\max_\phi|\omega_z-\omega_c\sin\phi|
=|\omega_z|+|\omega_c|.$$

所以

$$\Omega>|\omega_z|+|\omega_c|,$$

等价于

$$\boxed{|\omega_c|<
\sqrt{\omega_z^2+\omega_\phi^2}-|\omega_z|.}$$

右侧因 $\omega_\phi\ne0$而严格为正。若 $\omega_c$固定为有符号数，其允许区间是 $-C<\omega_c<C$，其中 $C=\sqrt{\omega_z^2+\omega_\phi^2}-|\omega_z|$。

等号不能包含。此时某角度处 $Q$的零点位于正弦极值，靠近该点 $Q$按角偏差平方趋零，积分 $dt=d\phi/\sqrt Q$发散，粒子无限接近该角度，却不会在有限时间完成一圈。

图 8-3 将符合严格不等式的空间绕轴轨迹与展开曲线并列。后面的局部螺距公式使用的是图中展开横坐标 $R_0\phi$，不是空间直线距离。

![图 8-3　连续绕轴的三维轨迹及柱面展开后变化的局部螺距。](../figures/unwrapped-08.png)

令 $\varepsilon=\operatorname{sgn}\omega_\phi$。在持续绕轴时，

$$\frac{dz}{d\phi}
=\frac{R_0(\omega_z-\omega_c\sin\phi)}
{\varepsilon\sqrt{\Omega^2-(\omega_z-\omega_c\sin\phi)^2}}.$$

通常它随 $\phi$变化，进一步说明这不是严格等螺距的螺旋线。

（8）轴向是否总向同一个方向。

由 $\dot z=R_0(\omega_z-\omega_c\sin\phi)$，若希望轴向速度始终与初始 $\omega_z$同号且不为零，需要

$$|\omega_c|<|\omega_z|.$$

等号时会在某角度暂时轴向速度为零，但通常不反向；大于这个值，则完整绕轴轨迹中可能出现局部轴向反向。这个条件与绕轴条件不同，不能互相替代。

然而即使有局部反向，在连续绕轴的一周内轴向净位移仍与 $\omega_z$同号。令

$$f(s)=\frac{s}{\sqrt{\Omega^2-s^2}},\qquad |s|<\Omega.$$

它为奇函数且严格递增。一周的轴向位移为

$$\Delta z=R_0\int_0^{2\pi}
f(\omega_z-\omega_c\sin\phi)\,d\phi.$$

此式对逆向绕轴也成立：积分方向与 $1/\varepsilon$的符号互相抵消。将 $\sin\phi=s$与 $-s$对应的贡献配对：

$$f(\omega_z-\omega_cs)+f(\omega_z+\omega_cs).$$

当 $\omega_z>0$时，$\omega_z+\omega_cs>-\omega_z+\omega_cs$，单调性给

$$f(\omega_z+\omega_cs)>-f(\omega_z-\omega_cs),$$

所以每一对贡献为正；$\omega_z<0$时同理为负。由此得到非零轴向净漂移，而不是只看某一瞬时 $\dot z$。

（9）用有效势确定允许区间。

将角运动写成

$$\frac12\dot\phi^2+V_{\rm eff}(\phi)=E_{\rm eff},\qquad
V_{\rm eff}=\frac12(\omega_z-\omega_c\sin\phi)^2,\quad
E_{\rm eff}=\frac12\Omega^2.$$

这只是将真实动能分配改写成一维形式；有效势不表示磁场对粒子做功。允许区满足 $V_{\rm eff}\le E_{\rm eff}$，等号处是候选转向点。

图 8-4 专门展示 $\omega_z=0$的三类情形。低于势垒时角度往返，高于势垒时角度旋转，恰在势垒顶时形成无限时间才能到达的分离轨道。

![图 8-4　零初始轴向速度时的有效势、转向点与分离能量。](../figures/potential-08.png)

（10）$\omega_z=0$、较弱磁场时轨迹也能闭合。

此时

$$\dot\phi^2=\omega_\phi^2-\omega_c^2\sin^2\phi,\qquad
\dot z=-R_0\omega_c\sin\phi.$$

若 $|\omega_c|<|\omega_\phi|$，角度完整绕轴。在一圈内

$$\Delta z=-\frac{R_0\omega_c}{\varepsilon}
\int_0^{2\pi}
\frac{\sin\phi\,d\phi}
{\sqrt{\omega_\phi^2-\omega_c^2\sin^2\phi}}=0.$$

原因是将 $\phi$换成 $\phi+\pi$，分母相同、分子相反，两个半周期积分抵消。完成一圈后 $\phi$增加或减少 $2\pi$，空间位置、$\dot\phi$和 $\dot z$均恢复，故真实空间轨迹闭合。

若 $\omega_c=0$，则 $z=z_0$，粒子沿圆周运动，也属于闭合轨迹。不能因为题目讨论磁场就将这个边界例子无故排除。

令 $k=|\omega_c/\omega_\phi|<1$，一圈所需时间为

$$T_{\rm rot}
=\frac4{|\omega_\phi|}
\int_0^{\pi/2}\frac{d\phi}{\sqrt{1-k^2\sin^2\phi}}
=\frac4{|\omega_\phi|}K(k),$$

其中 $K(k)$为第一类完全椭圆积分。$k\to0$时 $K(0)=\pi/2$，恢复圆周周期 $2\pi/|\omega_\phi|$。

（11）较强磁场时的往返闭合轨迹。

若 $|\omega_c|>|\omega_\phi|$，令

$$k=\frac{|\omega_\phi|}{|\omega_c|}<1,\qquad
\phi_m=\arcsin k.$$

从初始 $\phi=0$出发，粒子被限制在 $-\phi_m\le\phi\le\phi_m$，在端点 $\dot\phi=0$，随后角运动反向。

转向点不是平衡点，因为 $\sin\phi_m\ne0$且 $\cos\phi_m>0$；二阶方程给出指向允许区的角加速度，粒子可以在有限时间转向。完整振荡对称地经过正、负角区，$\dot z=-R_0\omega_c\sin\phi$为奇函数，两半周期轴向位移相反，因此总轴向位移为零。

图 8-5 同时画出弱场的一圈闭合曲线与强场的局部往返闭合曲线。后者只占圆柱的一部分角区，但并非平面上的线段；它在空间中具有轴向高度变化。

![图 8-5　弱场绕轴闭合曲线与强场有限角区往返闭合曲线。](../figures/closed-08.png)

振荡周期先写成四倍四分之一周期：

$$T_{\rm lib}=4\int_0^{\phi_m}
\frac{d\phi}{\sqrt{\omega_\phi^2-\omega_c^2\sin^2\phi}}.$$

令 $\sin\phi=k\sin\psi$，则

$$\cos\phi\,d\phi=k\cos\psi\,d\psi,$$

而分母为 $|\omega_\phi|\cos\psi$。因此

$$\begin{aligned}
T_{\rm lib}
&=\frac4{|\omega_c|}
\int_0^{\pi/2}\frac{d\psi}{\sqrt{1-k^2\sin^2\psi}}\\
&=\frac4{|\omega_c|}K(k).
\end{aligned}$$

这一周期证明转向发生在有限时间，并与直接积分二阶运动方程获得的返回时刻一致。

（12）临界等号处为什么不闭合。

若 $|\omega_c|=|\omega_\phi|\ne0$，则

$$\dot\phi^2=\omega_\phi^2\cos^2\phi.$$

从零角出发会接近 $\phi=\varepsilon\pi/2$。时间积分含 $\int d\phi/\cos\phi$，在端点对数发散。到达这一角度所需时间无穷大，而 $\dot z$趋于非零常量，所以轴向位置持续远离，轨迹不能闭合。

图 8-6 表示这一分离情形：角度趋向有限值，轴向位移却不受限。它不同于两端都能在有限时间转向的强场往返轨迹。

![图 8-6　临界磁场下角度渐近、轴向持续远离的非闭合分离轨道。](../figures/separatrix-08.png)

综合第（c）（iii）问：

$$\boxed{\omega_z=0,\ \omega_\phi\ne0:\quad
\text{轨迹闭合当且仅当 }|\omega_c|\ne|\omega_\phi|.}$$

弱场完整绕轴、强场局部往返，都可以闭合；只有临界等号对应非闭合分离轨道。只给 $|\omega_c|>|\omega_\phi|$会漏掉整个弱场闭合分支。

（13）给出临界轨道的显式解，核对渐近判断。

以 $\omega_c=\omega_\phi=\omega>0$、$\omega_z=0$、$z(0)=z_0$为例。在初始允许区 $\dot\phi=\omega\cos\phi$。设 $s=\sin\phi$，则

$$\dot s=\cos\phi\dot\phi
=\omega(1-s^2).$$

分离变量并用 $s(0)=0$，得到 $s=\tanh(\omega t)$。所以

$$\sin\phi=\tanh\omega t,\qquad
\cos\phi=\operatorname{sech}\omega t.$$

轴向速度 $\dot z=-R_0\omega\tanh\omega t$，积分为

$$z-z_0=-R_0\ln\cosh\omega t.$$

真实空间轨道为

$$\boxed{x=R_0\operatorname{sech}\omega t,\quad
y=R_0\tanh\omega t,\quad
z=z_0-R_0\ln\cosh\omega t.}$$

它满足 $x^2+y^2=R_0^2$，初始圆周速度为 $R_0\omega$，初始轴向速度为零。$t\to\infty$时 $x\to0$、$y\to R_0$，但 $z\to-\infty$，不能称为闭合。直接求导回代两条二阶方程也成立。

（14）最终分类、量纲与极限检查。

两条运动方程中，$\omega_c\dot z/R_0$和 $R_0\omega_c\dot\phi$分别具有 $\mathrm{s^{-2}}$与 $\mathrm{m/s^2}$量纲。第一积分中的每一项都是 $\mathrm{s^{-2}}$，没有少乘或多乘半径。

当 $q=0$或 $B=0$，$\omega_c=0$，两条加速度均为零，得到等螺距螺旋线；当同时 $\omega_z=0$，它退化成闭合圆周。改变电荷符号并保留初态时，轴向耦合方向改变，但零初始轴向速度的旋转/振荡阈值只含绝对值，不变。

非零 $\omega_z$时应分别报告：严格等螺距需要 $\omega_c=0$；连续完整绕轴需要上述严格不等式；轴向始终不反向还需 $|\omega_c|\le|\omega_z|$，若要求速度处处非零则取严格小于。

零 $\omega_z$时应分别报告：弱场旋转闭合、强场振荡闭合、临界分离不闭合。所有这些判断都来自角运动的允许区和轴向净位移，而不是只看能量式能否有实数根。

## 六、关键洞察

磁场不做功，并不意味着速度各分量不变。这里总速率恒定，但圆周与轴向动能可以交换。有效势来自将轴向动能代入守恒式，不应被解释成磁力的真实势能。

闭合曲线与角度是否完整绕轴不是同一问题。弱场可以每圈回到同一高度，强场可以在一个有限角区绕出闭合回路；临界时角度停在渐近边界，轴向仍向远处运动。这三者必须同时检查位置与速度的返回。

轴向第一积分还可由平移对称性理解。选矢势 $\boldsymbol A=By\,\boldsymbol e_z$，则 $\nabla\times\boldsymbol A=B\boldsymbol e_x$。广义动量 $p_z=m\dot z+qBy=m\dot z+qBR_0\sin\phi$守恒，恢复同一个 $\dot z$关系。这是独立的对称性视角，不需要重做叉乘积分。

## 七、易错点

单位矢量不求导，漏掉向心加速度；将 $\boldsymbol B$误认为始终沿径向；叉乘顺序交换却不变号；把带符号的 $\omega_c$提前换为正数；能量式遗漏轴向动能；过转向点继续固定 $\dot\phi$平方根的正号；把等号也收入完整绕轴区间；只承认强场闭合，漏掉弱场的一周轴向抵消；用平面波线替代柱面空间轨迹。

尤其不能由 $\dot\phi=0$直接断言粒子静止。转向处通常仍有轴向速度，并有非零角加速度；只有同时检查所有分量才能判断运动状态。

## 八、课堂讲解建议

让学生先在真实柱面上找当地径向和圆周方向，再把均匀横向磁场投影，板书三项叉乘的来源。推完轴向积分后，要求学生说明为什么洛伦兹力不做功却能改变 $\dot z$。

分类时先展示展开图，区分等螺距直线和变螺距曲线；再用有效势比较越过势垒、两侧转向和无限时间接近势垒顶。讲闭合性时让学生同时核对角位置、轴向位移和速度返回，不能只观察空间曲线“看起来绕了一圈”。

## 九、变式训练

变式一：取 $\omega_\phi=1\,\mathrm{s^{-1}}$、$\omega_z=0.2\,\mathrm{s^{-1}}$、$\omega_c=0.5\,\mathrm{s^{-1}}$。判断是否完整绕轴、轴向是否局部反向以及轨迹是否闭合。

完整解答：绕轴阈值为 $\sqrt{1.04}-0.2\approx0.81980390\,\mathrm{s^{-1}}$，大于 $0.5$，所以完整绕轴。最小角速度平方为

$$Q_{\min}=1.04-(0.2+0.5)^2=0.55\,\mathrm{s^{-2}}>0.$$

轴向速度为 $R_0(0.2-0.5\sin\phi)$，在 $\sin\phi=0.4$处变号，存在局部反向。但一周净轴向位移为正，因为 $\omega_z>0$，按主解析的奇函数配对证明每对贡献为正。因此不会在每一周回到同一高度，不是闭合轨迹，也不是严格等螺距螺旋线。

变式二：$\omega_z=0$、$\omega_\phi=1\,\mathrm{s^{-1}}$，分别取 $\omega_c=0.5\,\mathrm{s^{-1}}$与 $1.5\,\mathrm{s^{-1}}$。求闭合轨迹的周期表达式和较强场的最大角度。

完整解答：第一种属于弱场旋转，$k=0.5$，

$$T_1=4K(0.5)\,\mathrm s\approx6.74300142\,\mathrm s.$$

第二种属于强场振荡，$k=2/3$，

$$\phi_m=\arcsin(2/3)\approx41.81031490^\circ,\qquad
T_2=\frac{4}{1.5}K(2/3)\,\mathrm s
\approx4.82577999\,\mathrm s.$$

两者都在上述周期后回到初始空间位置和速度，轴向净位移为零。周期数值由椭圆积分计算，并以二阶运动方程直接积分的回返结果交叉检查；若将第二个周期错用弱场公式，会得到没有实数意义的积分参数。

（3）取初始角速度$p=\omega_\phi>0$、轴向参数$z=\omega_z$，磁场较弱。求完整绕行一圈的轴向位移至二阶。

解：用$c=\omega_c$，主问积分给
$$\Delta Z=R\int_0^{2\pi}\frac{z-c\sin\phi}{\sqrt{p^2+2cz\sin\phi-c^2\sin^2\phi}}\,d\phi.$$
展开并利用$\int\sin\phi\,d\phi=0$、$\int\sin^2\phi\,d\phi=\pi$，得
$$\Delta Z=\frac{2\pi Rz}{p}\left[1+\frac{3c^2}{4p^2}\left(1+\frac{z^2}{p^2}\right)+O(c^4)\right].$$
整圈积分对$c$为偶函数，一阶修正消失；局部螺距仍随角度改变。展开要求远离转向阈值，且$|cz|/p^2,c^2/p^2$足够小。

（4）求圆柱的有向径向反力，并用纯初始绕行说明双侧约束为何必要。

解：向外为正，磁力径向分量$qB\dot Z\sin\phi$，径向加速度$-R\dot\phi^2$，故
$$N_r=-mR[p^2+3cz\sin\phi-2c^2\sin^2\phi].$$
$z=0,|c|>|p|$时在转向点$\sin\phi=p/|c|$或其符号对应根，$\dot\phi=0$，反力为$+mRp^2$；初始则为$-mRp^2$。反力会换向，单侧表面接触不能保证全过程按此轨迹运动。双侧径向约束的反力始终垂直速度，不做功。
