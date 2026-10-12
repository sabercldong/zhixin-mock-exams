# 第5题

<!-- question-start -->

空间中存在沿 $+z$ 方向的匀强磁场 $\boldsymbol B=B_0\boldsymbol e_z$。两个电子的电荷均为 $-q$，质量均为 $m$，在 $x$—$y$ 平面内运动。只考虑两个电子之间的静电作用及外磁场的洛伦兹力，不考虑相对论效应。

（1）初始时两个电子相距 $l$，速度大小均为 $v_0$，方向相反。此后两个电子均保持匀速圆周运动。求各参数必须满足的条件，并讨论轨道的稳定性。

（2）初始时一个电子静止，另一个电子的初速度大小为 $v_0$；此后两个电子的距离始终保持为 $l$。求两个电子质心的轨道形态，以及初始运动电子第一次速度为零的时间。

图5-1分别表示两问与恒定距离相容的初始速度方向；磁场沿纸面法向向外。

![图5-1 两问的初始位置、速度及垂直于运动平面的磁场。](../figures/question-05.png){width=88%}

<!-- question-end -->

## 一、题型定位

这是均匀磁场中的两体动力学问题。相同的电荷质量比使质心运动与相对运动能够严格分离：内力在质心方程中抵消，却在相对方程中加倍。圆轨道条件由向内磁力、向外静电斥力和向心加速度共同决定，不是普通的单电子回旋半径公式。

第（1）问中的 $v_0$ 是每个电子的速率；第（2）问中的 $v_0$ 是唯一初始运动电子的速率。两问虽然使用同一个字母，但在相同的 $l$ 和同一角速度分支下，后一速率是前一速率的两倍。先区分质心速度、相对速度与绕质心速度，才能避免错误的因子 $2$。

## 二、知识点

带负电荷粒子的洛伦兹力方向；两等质量粒子的质心和相对坐标；圆周运动的向心加速度；两电子间距与各自轨道半径的区别；正则角动量守恒；径向微扰时切向速度随半径变化；线性恢复力与径向稳定性；均匀磁场中质心回旋运动；两个等模旋转速度矢量的相消；首个零速时刻与瞬时静止的区别。

记库仑常量为 $k_e=1/(4\pi\varepsilon_0)$。采用 $q>0$、$B_0>0$，定义正的回旋角频率

$$
\Omega=\frac{qB_0}{m}>0.
$$

从 $+z$ 方向看向运动平面，逆时针为正角方向。题设只保留库仑力和给定磁场力，因此不存在阻尼、辐射反作用或外部约束力。稳定性首先应在题设的平面运动模型内讨论，不能暗中更换为不受限制的三维运动。

## 三、物理图像

两个电子同号相斥。若它们围绕静止质心作共同圆周运动，磁力必须向内，并且大于向外的库仑力；剩余向内合力才提供向心加速度。由此允许两种正角速度：一支较慢，磁力的大部分用于平衡斥力；另一支较快，更接近单粒子的回旋运动。

检验稳定性时，不能把轨道半径增大而切向速度仍保持不变。磁场对运动电子有力矩，径向移动时切向速度按照正则角动量守恒改变。把这种变化代回真实径向受力，才能判断两支是否具有回复趋势。

第（2）问的质心并不静止。每个电子的速度由“质心的回旋速度”和“绕质心旋转的速度”相加而成。初始运动电子的两部分速度开始同向，后来由于两种角速度不同而逐渐转开；两部分模长相等且首次反向时，总速度为零。

## 四、解题入口

第（1）问先取轨道半径 $\rho_0=l/2$，写向心方向的牛顿方程，再将速率换成角速度 $\omega=2v_0/l$。所得二次方程同时给出两个角速度分支与轨道存在条件。稳定性另作守恒约束下的微扰，不能仅凭二次方程有两个根就猜测一稳一不稳。

第（2）问先相加两个电子的牛顿方程，得到质心回旋频率 $\Omega$；再相减得到相对方程。恒定间距使相对角速度 $\omega$ 恒定，且此时 $\omega=v_0/l$。最后以两旋转速度的相位差判断首个零速时刻。

以下先完成第（1）问，再处理第（2）问；角速度的上下分支始终使用一致的下标。

## 五、解析

**第1步：固定电子编号、坐标与负电荷的磁力方向。**

取初始连线沿 $x$ 轴，电子 $1$ 在右侧，电子 $2$ 在左侧。对平面向量定义

$$
J(v_x,v_y)=(-v_y,v_x).
$$

<!-- KEEP_TOGETHER_START -->

$J$ 把向量逆时针转过 $90^\circ$。由于

$$
\begin{aligned}
\boldsymbol v\times\boldsymbol e_z&=(v_y,-v_x)=-J\boldsymbol v,\\
(-q)\boldsymbol v\times\boldsymbol B
&=qB_0J\boldsymbol v=m\Omega J\boldsymbol v,
\end{aligned}
$$

<!-- KEEP_TOGETHER_END -->

电子位于右侧、向上运动时，磁力向左；位于左侧、向下运动时，磁力向右。这与共同逆时针圆周运动需要的向心方向一致。若换成顺时针，磁力和斥力都向外，不能提供共同圆轨道的向心合力。

这里的 $q$ 是电荷量的正值，电子的电荷才是 $-q$；不能在定义 $\Omega$ 时再多放一个负号。

**第2步：证明第（1）问的质心静止，辨认共同圆心。**

记电子的位置为 $\boldsymbol r_1,\boldsymbol r_2$，速度为 $\boldsymbol v_1,\boldsymbol v_2$，质心位置与速度分别为

$$
\boldsymbol R_c=\frac{\boldsymbol r_1+\boldsymbol r_2}{2},
\qquad
\boldsymbol V_c=\frac{\boldsymbol v_1+\boldsymbol v_2}{2}.
$$

两电子的库仑力等大反向。相加牛顿方程得

$$
\begin{aligned}
m(\dot{\boldsymbol v}_1+\dot{\boldsymbol v}_2)
&=m\Omega J(\boldsymbol v_1+\boldsymbol v_2),\\
\dot{\boldsymbol V}_c&=\Omega J\boldsymbol V_c.
\end{aligned}
$$

第（1）问初速度等大反向，因此 $\boldsymbol V_c(0)=0$。这个线性方程的解始终为 $\boldsymbol V_c(t)=0$，质心固定。取质心为 $O$，则始终有 $\boldsymbol r_2=-\boldsymbol r_1$。

对匀速圆轨道，加速度与磁力都沿该圆的径向，因而剩余库仑力也必须沿该圆的径向。库仑力方向又沿 $\boldsymbol r_1-\boldsymbol r_2=2\boldsymbol r_1$；两个径向方向在整个圆周上重合，只能使圆心位于 $O$。故两电子在同一个圆上相隔半周，各自半径均为

$$
\rho_0=\frac l2.
$$

初始速度必须垂直于两电子连线，并按前述逆时针方向取向。这是圆周运动条件的一部分，不是任意一对等大反向初速度都能成立。

**第3步：用真实的向心受力建立圆轨道方程。**

如图5-2，电子 $1$ 在右侧时，$qB_0v_0$ 向左，库仑斥力 $k_eq^2/l^2$ 向右。图中的 $l$ 是两电子间距，$\rho_0$ 才是向心加速度中的半径。

![图5-2 同圆反向位置的两电子与径向向内、向外两种力。](../figures/force-05.png){width=60%}

取向内为这一式的正方向：

$$
\begin{aligned}
qB_0v_0-\frac{k_eq^2}{l^2}
&=\frac{mv_0^2}{\rho_0}
=\frac{2mv_0^2}{l},\\
\frac{2m}{l}v_0^2-qB_0v_0+\frac{k_eq^2}{l^2}&=0.
\end{aligned}
$$

右边是 $m$ 乘向心加速度，左边两种真实力的合力提供这一加速度。只写 $qB_0v_0=mv_0^2/\rho_0$ 会遗漏两电子间的斥力。

也可立即检查，任意可行根都满足

$$
qB_0v_0-\frac{k_eq^2}{l^2}
=\frac{2mv_0^2}{l}>0.
$$

所以磁力确实比斥力大，而不是相互完全抵消。

**第4步：完整解出速率的两个正根。**

先除以 $2m/l$，再配方：

$$
\begin{aligned}
v_0^2-\frac{qB_0l}{2m}v_0+\frac{k_eq^2}{2ml}&=0,\\
\left(v_0-\frac{qB_0l}{4m}\right)^2
&=\left(\frac{qB_0l}{4m}\right)^2-\frac{k_eq^2}{2ml}.
\end{aligned}
$$

因此

$$
\boxed{
v_{0,\pm}^{(1)}
=\frac{qB_0l}{4m}
\pm\sqrt{\left(\frac{qB_0l}{4m}\right)^2-\frac{k_eq^2}{2ml}}
}.
$$

上标 $(1)$ 仅用于提醒这是第（1）问的每个电子速率。根号里的第二项为正，因此只要判别式非负，根号就严格小于 $qB_0l/(4m)$；两个根都为正，不能把减号根误删成负速率。

两个根对应不同的运动状态，而不是一个顺时针、一个逆时针状态。两者均按同一逆时针方向运动。

**第5步：求判别式条件，逐项消去电荷量。**

存在实数圆轨道的必要条件为

$$
\begin{aligned}
\frac{q^2B_0^2l^2}{16m^2}
-\frac{k_eq^2}{2ml}&\geq0,\\
B_0^2l^2-\frac{8k_em}{l}&\geq0,\\
B_0^2l^3&\geq8k_em.
\end{aligned}
$$

第二行是把第一行乘以 $16m^2/q^2$，第三行再乘以正数 $l$，不改变不等号。故

$$
\boxed{
l\geq l_c,\qquad
l_c=2\left(\frac{k_em}{B_0^2}\right)^{1/3}
}.
$$

等价地，在给定 $l$ 时，磁场必须满足

$$
B_0\geq B_c=\sqrt{\frac{8k_em}{l^3}}.
$$

临界长度与 $q$ 无关，是因为斥力含 $q^2$，而磁力与速率共同形成的判别式也含同一个 $q^2$。这不表示运动速率与 $q$ 无关；速率仍与 $q$ 成正比。

判别式为零时两个圆轨道分支合并，只有一个圆轨道角速度值；接下来还须单独检验其稳定性。

**第6步：改用角速度，并固定上下分支的含义。**

定义

$$
C=\frac{2k_eq^2}{m},
\qquad
D=\sqrt{\frac{\Omega^2}{4}-\frac{C}{l^3}}.
$$

第（1）问中每个电子的圆周速率为 $v_0=\omega l/2$。代回第3步的方程：

$$
\begin{aligned}
qB_0\frac{\omega l}{2}-\frac{k_eq^2}{l^2}
&=m\frac{\omega^2l}{2},\\
\omega^2-\Omega\omega+\frac{C}{l^3}&=0.
\end{aligned}
$$

故

$$
\boxed{\omega_\pm=\frac{\Omega}{2}\pm D}.
$$

对有限的 $l$、非零的 $q$，有

$$
0\leq D<\frac{\Omega}{2},
\qquad
0<\omega_-\leq\frac{\Omega}{2}
\leq\omega_+<\Omega.
$$

若 $l=l_c$，则 $D=0$、$\omega_+=\omega_-=\Omega/2$。若 $l>l_c$，两个不等分支都存在。后续任何含 $\pm$ 的式子，都要与 $\omega_\pm$ 的定义相联系。

**第7步：明确稳定性扰动不能把切向速度固定住。**

考察某一圆轨道 $\rho_0=l/2$，让两电子仍关于 $O$ 对称，但半径发生小的径向变化。图5-3把扰动后的半径写为 $\rho=\rho_0(1+x)$，其中 $x$ 是无量纲微扰；图中切向速度 $v(x)$ 随半径变化。

![图5-3 对称径向微扰、切向速度与三项径向受力。](../figures/radial-05.png){width=86%}

对电子 $1$，库仑力沿径向，对 $O$ 无力矩。洛伦兹力却在存在径向速度时含切向分量。把平面极坐标速度写成

$$
\boldsymbol v=\dot\rho\,\boldsymbol e_\rho
+\rho\dot\theta\,\boldsymbol e_\theta,
$$

则磁力为

$$
m\Omega J\boldsymbol v
=m\Omega\dot\rho\,\boldsymbol e_\theta
-m\Omega\rho\dot\theta\,\boldsymbol e_\rho.
$$

切向牛顿方程因此是

$$
m(\rho\ddot\theta+2\dot\rho\dot\theta)
=m\Omega\dot\rho.
$$

必须使用这一切向方程，才能知道扰动后 $v=\rho\dot\theta$ 如何改变。

**第8步：从切向方程推导正则角动量守恒。**

把前式乘以 $\rho$，整理为两个全导数：

$$
\begin{aligned}
\rho^2\ddot\theta+2\rho\dot\rho\dot\theta
-\Omega\rho\dot\rho&=0,\\
\frac{\mathrm d}{\mathrm dt}
\left(\rho^2\dot\theta-\frac{\Omega}{2}\rho^2\right)&=0.
\end{aligned}
$$

乘以 $m$，并用 $v=\rho\dot\theta$、$m\Omega=qB_0$，得到

$$
m\rho v-\frac{qB_0}{2}\rho^2=\text{常量}.
$$

机械角动量 $m\rho v$ 本身不守恒；与磁场项结合后的量才守恒。磁场沿 $+z$、电子电荷为负时，这里是减号。

初始圆轨道给出守恒常量 $m\rho_0v_0-m\Omega\rho_0^2/2$。于是

$$
\begin{aligned}
\rho v-\frac{\Omega}{2}\rho^2
&=\rho_0v_0-\frac{\Omega}{2}\rho_0^2,\\
v(\rho)&=\frac{\rho_0v_0}{\rho}
+\frac{\Omega}{2}\frac{\rho^2-\rho_0^2}{\rho}.
\end{aligned}
$$

这就是图5-3中 $v(x)$ 的来源，并没有把单粒子回旋半径公式套进双粒子问题。

**第9步：保留微扰速度的全部一阶变化。**

令 $\rho=\rho_0(1+x)$。由第8步：

$$
\begin{aligned}
v(x)
&=\frac{1}{1+x}
\left[v_0+\frac{\Omega\rho_0}{2}
\bigl((1+x)^2-1\bigr)\right],\\
&=\frac{1}{1+x}
\left[v_0+\Omega\rho_0x
+\frac{\Omega\rho_0}{2}x^2\right].
\end{aligned}
$$

此处用 $(1+x)^{-1}=1-x+O(x^2)$，得到

$$
v(x)=v_0+(\Omega\rho_0-v_0)x+O(x^2).
$$

记

$$
a_v=\Omega\rho_0-v_0.
$$

$a_v$ 的单位仍是速度，不是加速度。即使 $v_0$ 为较慢分支，扰动时也要保留 $\Omega\rho_0x$；遗漏这个磁力矩贡献会改变稳定性判断。

<!-- KEEP_TOGETHER_START -->

**第10步：正确建立径向扰动的方程，而非另加一项真实离心力。**

极坐标径向加速度为 $\ddot\rho-\rho\dot\theta^2$。两电子间距现在是 $2\rho$，所以径向牛顿方程为

$$
m\left(\ddot\rho-\frac{v^2}{\rho}\right)
=\frac{k_eq^2}{(2\rho)^2}-m\Omega v.
$$

<!-- KEEP_TOGETHER_END -->

移项可写成

$$
m\ddot\rho
=\frac{mv^2}{\rho}
+\frac{k_eq^2}{4\rho^2}
-m\Omega v.
$$

右边前三项组合是求径向加速度的表达式；$mv^2/\rho$ 来自坐标加速度的移项，并不是在惯性系额外施加给电子的一种相互作用。代入 $\rho=\rho_0(1+x)$、$2\rho_0=l$：

$$
F_{\rm out}(x)
=\frac{mv(x)^2}{\rho_0(1+x)}
+\frac{k_eq^2}{l^2(1+x)^2}
-m\Omega v(x).
$$

这里 $F_{\rm out}$ 表示 $m\ddot\rho$ 的右端。圆轨道上 $F_{\rm out}(0)=0$；若一阶项与 $x$ 异号，才构成径向回复趋势。

**第11步：逐项展开径向表达式，不能漏掉库仑项。**

由第9步，平方速度、逆半径和逆距离平方分别为

$$
\begin{aligned}
v(x)^2&=v_0^2+2v_0a_vx+O(x^2),\\
(1+x)^{-1}&=1-x+O(x^2),\\
(1+x)^{-2}&=1-2x+O(x^2).
\end{aligned}
$$

所以

$$
\begin{aligned}
F_{\rm out}(x)
={}&\left(\frac{mv_0^2}{\rho_0}
+\frac{k_eq^2}{l^2}-m\Omega v_0\right)\\
&+\left[
\frac m{\rho_0}(2v_0a_v-v_0^2)
-\frac{2k_eq^2}{l^2}-m\Omega a_v
\right]x+O(x^2).
\end{aligned}
$$

第一行由圆轨道方程严格等于零。对一阶系数，使用

$$
v_0=\omega\rho_0,\quad
a_v=(\Omega-\omega)\rho_0,\quad
\frac{k_eq^2}{l^2}
=m\rho_0(\Omega\omega-\omega^2).
$$

最后一式就是第3步的圆轨道平衡关系，使用前要保留其符号。逐项代入：

$$
\begin{aligned}
\frac{F_{\rm out}(x)}{m\rho_0}
={}&\bigl[
2\omega(\Omega-\omega)-\omega^2
-2(\Omega\omega-\omega^2)
-\Omega(\Omega-\omega)
\bigr]x+O(x^2)\\
={}&\bigl[
2\Omega\omega-3\omega^2
-2\Omega\omega+2\omega^2
-\Omega^2+\Omega\omega
\bigr]x+O(x^2)\\
={}&-\bigl(\Omega^2-\Omega\omega+\omega^2\bigr)x
+O(x^2).
\end{aligned}
$$

磁力、几何项、库仑项的一阶变化都参与最后的系数。不能只根据 $\Omega-2\omega$ 的符号判断，否则会错误地把较慢分支判成不稳定。

**第12步：给出两支与临界圆轨道的平面稳定性。**

因为 $\ddot\rho=\rho_0\ddot x$，一阶径向方程为

$$
\ddot x+\kappa^2x=0,
\qquad
\kappa^2=\Omega^2-\Omega\omega+\omega^2.
$$

完成平方，或利用圆轨道关系，均可检查其正值：

$$
\begin{aligned}
\kappa^2
&=\left(\omega-\frac{\Omega}{2}\right)^2
+\frac{3\Omega^2}{4}>0,\\
&=\Omega^2-\frac{C}{l^3}
\geq\frac{3\Omega^2}{4}.
\end{aligned}
$$

故

$$
\boxed{\text{两支圆轨道在题设平面内均为径向、轨道稳定。}}
$$

同一个 $l$ 的两支有相同的 $\kappa$，尽管圆周角速度 $\omega_+$、$\omega_-$ 不同。在临界点 $l=l_c$，$\kappa=\sqrt3\,\Omega/2$，仍不为零；两个代数根合并不等于径向回复力消失。

这里的稳定允许相位漂移：稍改初值可能使邻近轨道的角速度略变，长期相位不必与未扰动解完全一致。径向微扰却不会指数发散，轨道到相应圆轨道的距离保持小。无阻尼模型也不会自行衰减回原轨道。

量纲上，$C$ 为长度三次方除以时间平方，$C/l^3$、$\Omega^2$、$\kappa^2$ 均为时间的负二次方；上述恢复系数具备正确的频率量纲。

**第13步：转入第（2）问，严格分离质心与相对运动。**

沿用电子 $1$ 为初始运动者，选取

$$
\begin{aligned}
\boldsymbol r_1(0)&=\left(\frac l2,0\right),&
\boldsymbol r_2(0)&=\left(-\frac l2,0\right),\\
\boldsymbol v_1(0)&=(0,v_0),&
\boldsymbol v_2(0)&=(0,0).
\end{aligned}
$$

这些方向由恒定间距要求确定：$\mathrm d|\boldsymbol r_1-\boldsymbol r_2|^2/\mathrm dt=0$ 使初始相对速度垂直于连线；允许的定距旋向仍为逆时针。

记相对位置为 $\boldsymbol R=\boldsymbol r_1-\boldsymbol r_2$。两个电子的牛顿方程分别为

$$
\begin{aligned}
m\ddot{\boldsymbol r}_1
&=\frac{k_eq^2}{R^3}\boldsymbol R
+m\Omega J\dot{\boldsymbol r}_1,\\
m\ddot{\boldsymbol r}_2
&=-\frac{k_eq^2}{R^3}\boldsymbol R
+m\Omega J\dot{\boldsymbol r}_2.
\end{aligned}
$$

两式相加、相减，分别得到

$$
\boxed{
\ddot{\boldsymbol R}_c=\Omega J\dot{\boldsymbol R}_c,
\qquad
\ddot{\boldsymbol R}=\Omega J\dot{\boldsymbol R}
+\frac{C}{R^3}\boldsymbol R
}.
$$

内力在前式消失，在后式出现系数 $2$。两电子的绝对运动不是单纯的绕固定质心圆周运动，不能在此令 $\boldsymbol R_c$ 不动。

**第14步：由恒定间距证明相对角速度恒定，并求初速条件。**

写 $\boldsymbol R=R\boldsymbol e_r$，其切向方程为

$$
R\ddot\theta+2\dot R\dot\theta=\Omega\dot R.
$$

题设 $R=l$ 恒定，故 $\dot R=0$，进一步得 $\ddot\theta=0$。记恒定相对角速度为 $\omega$，则

$$
\boldsymbol R(t)=l(\cos\omega t,\sin\omega t).
$$

相对径向方程给出

$$
-\omega^2l=-\Omega\omega l+\frac{C}{l^2},
$$

仍为 $\omega^2-\Omega\omega+C/l^3=0$。但初始相对速度为

$$
\dot{\boldsymbol R}(0)
=\boldsymbol v_1(0)-\boldsymbol v_2(0)
=v_0\boldsymbol e_y.
$$

故此问中 $\omega l=v_0$，不是 $\omega l/2=v_0$。于是允许的初速为

$$
\boxed{
v_{0,\pm}^{(2)}
=l\left(\frac{\Omega}{2}\pm D\right)
=2v_{0,\pm}^{(1)}
}.
$$

定距运动也要求 $l\geq l_c$。如果任意选取一个 $v_0$ 而不满足这个条件，恒定间距这个前提就不能实现。

**第15步：积分质心速度，明确圆心、半径、频率和旋向。**

图5-4区分质心绕固定圆心的运动与电子绕运动质心的旋转。设 $a_c=v_0/(2\Omega)$，质心初始位于 $O$，它的圆心为 $G=(-a_c,0)$，不是电子间的运动中点。图中的 $M$ 表示当前质心；其位置向量为 $\boldsymbol R_c(t)=\overrightarrow{OM(t)}$，不要把这个位置向量与质心圆的半径混淆。

图中的实线小圆表示质心轨道；虚线大圆只表示以当前质心为中心、半径为 $l/2$ 的相对位置关系，不是任一电子在固定坐标中的完整轨迹。橙色连线的中点是当前质心，两端分别是电子 $1,2$，不能把固定圆心 $G$ 与这个运动中点混为一谈。

![图5-4 质心回旋圆及以运动质心为中点的两电子连线。](../figures/com-05.png){width=56%}

对图中的 $M(t)$，第13步质心方程的分量为

$$
\dot V_{c,x}=-\Omega V_{c,y},
\qquad
\dot V_{c,y}=\Omega V_{c,x}.
$$

初始 $\boldsymbol V_c(0)=(0,v_0/2)$，解为

$$
\boldsymbol V_c(t)
=\frac{v_0}{2}(-\sin\Omega t,\cos\Omega t).
$$

逐分量从 $0$ 积分到 $t$：

$$
\begin{aligned}
X_c(t)&=-\frac{v_0}{2}\int_0^t\sin\Omega t'\,\mathrm dt'
=\frac{v_0}{2\Omega}(\cos\Omega t-1),\\
Y_c(t)&=\frac{v_0}{2}\int_0^t\cos\Omega t'\,\mathrm dt'
=\frac{v_0}{2\Omega}\sin\Omega t.
\end{aligned}
$$

常数 $-1$ 来自初始 $X_c(0)=0$，不能删去后改变圆心。消去时间：

$$
\left(X_c+\frac{v_0}{2\Omega}\right)^2+Y_c^2
=\left(\frac{v_0}{2\Omega}\right)^2.
$$

故

$$
\boxed{
\text{质心作逆时针匀速圆周运动，}\quad
R_c=\frac{v_0}{2\Omega}=\frac{mv_0}{2qB_0},
\quad T_c=\frac{2\pi}{\Omega}
}.
$$

圆心位置依赖坐标原点，但半径、频率与旋向不依赖这一选择。库仑力不改变质心回旋频率。

**第16步：写出绕质心的位置和速度，说明两个角速度的来源。**

由质心与相对坐标的定义：

$$
\begin{aligned}
\boldsymbol r_1(t)&=\boldsymbol R_c(t)+\frac l2(\cos\omega t,\sin\omega t),\\
\boldsymbol r_2(t)&=\boldsymbol R_c(t)-\frac l2(\cos\omega t,\sin\omega t).
\end{aligned}
$$

电子间连线长度始终为 $l$，但其中点按第15步的圆运动移动。每个电子的绝对轨迹一般是两个不同频率圆运动的叠加，而不是围绕 $G$ 的单个圆。

定义单位切向量

$$
\boldsymbol e_\phi(\alpha)=(-\sin\alpha,\cos\alpha).
$$

对上面两位置式求导，并使用 $\omega l=v_0$：

$$
\begin{aligned}
\boldsymbol v_1(t)&=\frac{v_0}{2}
\left[\boldsymbol e_\phi(\Omega t)+\boldsymbol e_\phi(\omega t)\right],\\
\boldsymbol v_2(t)&=\frac{v_0}{2}
\left[\boldsymbol e_\phi(\Omega t)-\boldsymbol e_\phi(\omega t)\right].
\end{aligned}
$$

回代 $t=0$，立即得到 $\boldsymbol v_1(0)=v_0\boldsymbol e_y$、$\boldsymbol v_2(0)=0$，确认编号和两个系数正确。绕质心速度的模为 $\omega l/2=v_0/2$，与质心速度模相同，这才使速度相消有可能发生。

**第17步：利用等模矢量相消，求第一次零速时间。**

图5-5中两速度矢量分别以 $\Omega$、$\omega$ 旋转。它们初始同向，第一次反向时相位差为 $\pi$；不需要等待两个运动各完成整数周。

![图5-5 初始运动电子的两个等模速度分量与首次相消。](../figures/velocity-05.png){width=86%}

两单位切向量的点积为 $\cos[(\Omega-\omega)t]$，所以

$$
\begin{aligned}
|\boldsymbol v_1(t)|^2
&=\frac{v_0^2}{4}
\left(1+1+2\cos[(\Omega-\omega)t]\right)\\
&=v_0^2\cos^2\left(\frac{\Omega-\omega}{2}t\right).
\end{aligned}
$$

使用恒等式 $1+\cos\alpha=2\cos^2(\alpha/2)$。由第6步，$0<\omega<\Omega$，故相位差随时间正向增加。全部零速时刻为

$$
(\Omega-\omega)t=(2n+1)\pi,
\qquad n=0,1,2,\ldots.
$$

第一次对应 $n=0$，因此

$$
\boxed{t_*=\frac{\pi}{\Omega-\omega}}.
$$

如果直接用相消矢量判断，也得到同一条件；速度模平方的推导则额外证明在 $0<t<t_*$ 内没有遗漏更早的零点。

**第18步：绑定分支符号，完成边界和物理检查。**

将 $\omega_\pm=\Omega/2\pm D$ 代入，注意减号会反转根号前的符号：

$$
\boxed{
t_{*,+}=\frac{\pi}{\Omega/2-D},
\qquad
t_{*,-}=\frac{\pi}{\Omega/2+D}
}.
$$

因此较快相对旋转支的首次停止反而更晚，因为它与质心角速度 $\Omega$ 的差更小。两个时间均为正，单位均为时间。

临界条件 $D=0$ 时，两支合并，$t_*=2\pi/\Omega$。当保持 $B_0$ 不变并使 $l$ 很大，较慢支 $\omega_-\to0$，$t_{*,-}\to\pi/\Omega$；较快支 $\omega_+\to\Omega$，$t_{*,+}\to\infty$。这些只是经典模型的形式极限，实际应用仍须检查速率远小于光速。

首次停止时 $\boldsymbol e_\phi(\omega t_*)=-\boldsymbol e_\phi(\Omega t_*)$，于是

$$
|\boldsymbol v_2(t_*)|=v_0.
$$

而电子 $1$ 此刻的磁力为零，库仑斥力仍非零：

$$
\ddot{\boldsymbol r}_1(t_*)
=\frac{k_eq^2}{ml^3}\boldsymbol R(t_*)\neq0.
$$

所以它只是瞬时静止，随后马上继续运动。两电子速度在此刻发生角色交换，但静电力不会消失。

## 六、关键洞察

第（1）问的两个圆轨道分支并非“一个稳定、一个不稳定”。它们在同一个 $l$ 上具有相同的径向频率，区别主要在旋转方向一致时角速度的大小，以及正则角动量的正负。用有效势能可以进一步检验一般平面微扰，而不限于第7步选取的固定守恒量微扰。

令相对距离为 $R$，约化质量为 $\mu=m/2$。相对角运动满足

$$
\frac{\mathrm d}{\mathrm dt}
\left[R^2\left(\dot\theta-\frac{\Omega}{2}\right)\right]=0.
$$

记单位约化质量的正则角动量为 $j$，则

$$
j=R^2\left(\dot\theta-\frac{\Omega}{2}\right),
\qquad
\dot\theta=\frac{\Omega}{2}+\frac j{R^2}.
$$

$j$ 可以为正、负或零；它与第8步单电子守恒量相差固定倍数，不要由于名字相同就直接混用数值。相对径向方程为

$$
\begin{aligned}
\ddot R
&=R(\dot\theta^2-\Omega\dot\theta)+\frac C{R^2}\\
&=-\frac{\Omega^2R}{4}+\frac{j^2}{R^3}+\frac C{R^2}.
\end{aligned}
$$

中间的交叉项相消：

$$
\left(\frac\Omega2+\frac j{R^2}\right)^2
-\Omega\left(\frac\Omega2+\frac j{R^2}\right)
=-\frac{\Omega^2}{4}+\frac{j^2}{R^4}.
$$

故单位约化质量的有效势能是

$$
U_{\rm eff}(R)
=\frac{\Omega^2R^2}{8}+\frac{j^2}{2R^2}+\frac C R.
$$

逐项求负导数便得到上面的径向方程。库仑势能项是正的 $C/R$，因为相同电荷相斥。该有效势能不是全部实际势能，而是固定正则角动量后的一维径向描述。

其二阶导数为

$$
U_{\rm eff}''(R)
=\frac{\Omega^2}{4}+\frac{3j^2}{R^4}+\frac{2C}{R^3}>0.
$$

而 $R\to0^+$ 与 $R\to\infty$ 时，$U_{\rm eff}$ 都趋于正无穷，故每个 $j$ 都有唯一稳定径向最低点。在指定圆轨道 $R=l$ 上，

$$
j=l^2\left(\omega-\frac\Omega2\right),
$$

代入二阶导数，并用 $C/l^3=\Omega\omega-\omega^2$：

$$
\begin{aligned}
U_{\rm eff}''(l)
&=\frac{\Omega^2}{4}
+3\left(\omega-\frac\Omega2\right)^2
+2(\Omega\omega-\omega^2)\\
&=\Omega^2-\Omega\omega+\omega^2=\kappa^2.
\end{aligned}
$$

这是对径向受力逐项展开的独立能量核验。较小的初值变化使 $j$ 和径向能量连续变化，轨道仍在邻近最低点附近作有界径向运动；质心初速度的微扰又只产生有界回旋运动。因此平面内的轨道稳定结论不只依赖完全对称的某一种特殊扰动。

还可检验旋转坐标的全部平面线性模式。随圆轨道以 $\omega$ 旋转，令相对位置微扰的径向、切向分量为 $\xi,\eta$，设

$$
s=\frac C{l^3}=\Omega\omega-\omega^2,\qquad
\gamma=\Omega-2\omega.
$$

为说明两个耦合项的来源，设 $Q(t)$ 为转过 $\omega t$ 的二维旋转矩阵：

$$
Q(t)=
\begin{pmatrix}
\cos\omega t&-\sin\omega t\\
\sin\omega t&\cos\omega t
\end{pmatrix}.
$$

令 $\boldsymbol R=Q(t)\boldsymbol u$。逐项求矩阵元素的导数可得 $\dot Q=\omega JQ$，且 $J^2=-I$，其中 $I$ 是二维单位矩阵。逐次求位置向量的导数：

$$
\begin{aligned}
\dot{\boldsymbol R}
&=Q(\dot{\boldsymbol u}+\omega J\boldsymbol u),\\
\ddot{\boldsymbol R}
&=Q(\ddot{\boldsymbol u}+2\omega J\dot{\boldsymbol u}
-\omega^2\boldsymbol u).
\end{aligned}
$$

把它们代入第13步的相对牛顿方程，左乘 $Q^{-1}$。旋转不改变向量长度，且 $JQ=QJ$，所以

$$
\begin{aligned}
\ddot{\boldsymbol u}+2\omega J\dot{\boldsymbol u}
-\omega^2\boldsymbol u
&=\Omega J\dot{\boldsymbol u}
-\Omega\omega\boldsymbol u+\frac C{u^3}\boldsymbol u,\\
\ddot{\boldsymbol u}
&=(\Omega-2\omega)J\dot{\boldsymbol u}
+(\omega^2-\Omega\omega)\boldsymbol u
+\frac C{u^3}\boldsymbol u.
\end{aligned}
$$

在该旋转坐标中，未扰动相对位置为 $\boldsymbol u_0=(l,0)$。写 $\boldsymbol u=(l+\xi,\eta)$，常数项由圆轨道平衡抵消。库仑矢量的导数不能用一个标量系数同时替代两个方向：

记 $u=|\boldsymbol u|$；下面的 $\delta_{ij}$ 在 $i=j$ 时为 $1$，在 $i\neq j$ 时为 $0$，$i,j$ 分别标记两个平面分量。

$$
\begin{aligned}
\frac{\partial}{\partial u_j}
\left(\frac{u_i}{u^3}\right)
&=\frac{\delta_{ij}}{u^3}-\frac{3u_iu_j}{u^5},\\
\left.\frac{\partial(\boldsymbol u/u^3)}
{\partial\boldsymbol u}\right|_{(l,0)}
&=\frac1{l^3}
\begin{pmatrix}-2&0\\0&1\end{pmatrix}.
\end{aligned}
$$

库仑项的线性变化为 $(-2s\xi,s\eta)$，而 $(\omega^2-\Omega\omega)(\xi,\eta)=-s(\xi,\eta)$；两者相加为 $(-3s\xi,0)$。又有 $J(\dot\xi,\dot\eta)=(-\dot\eta,\dot\xi)$，故两个分量方程是

$$
\ddot\xi=-3s\xi-\gamma\dot\eta,
\qquad
\ddot\eta=\gamma\dot\xi.
$$

代入 $\xi,\eta\propto e^{\lambda t}$：

$$
\begin{aligned}
(\lambda^2+3s)\xi+\gamma\lambda\eta&=0,\\
-\gamma\lambda\xi+\lambda^2\eta&=0.
\end{aligned}
$$

行列式条件为

$$
\lambda^2(\lambda^2+3s+\gamma^2)
=\lambda^2(\lambda^2+\kappa^2)=0.
$$

非零特征根是纯虚的 $\pm i\kappa$。零特征根允许相位改变及邻近圆轨道参数改变，不能把由此导致的长期相位差说成径向指数不稳定。

题设限定运动在平面内非常重要。若放开相对轴向位移 $\zeta$，磁场不提供沿 $z$ 的回复力，线性相对方程为

$$
\ddot\zeta=\frac C{l^3}\zeta.
$$

它有增长解 $\zeta\propto e^{\sqrt{C/l^3}\,t}$，说明不受限制的三维模型不同于题设的平面模型。这个范围辨析不改变本题所问的平面稳定结论。

## 七、易错点

把 $l$ 当成每个电子的圆周半径，导致向心加速度少一个因子 $2$。第（1）问必须先用质心静止和对称性确定 $\rho_0=l/2$。

将负电荷的磁力方向画反。对于 $+z$ 磁场，右侧电子向上运动时磁力向左，共同旋转是逆时针；两个角速度分支不是两种相反旋向。

只保留磁力而忽略两电子的库仑斥力，或者把向心力当成第三种真实力。应按图5-2写磁力减斥力，再等于向心加速度对应的 $m$。

径向扰动后固定切向速度，或错误地保持机械角动量不变。图5-3所需守恒量是 $m\rho v-qB_0\rho^2/2$；磁力矩正是微扰速度中 $\Omega\rho_0x$ 的来源。

一阶化简时遗漏 $-2k_eq^2x/l^2$ 或弄错磁力变化的符号，会把慢速支误判为不稳定。正确系数是 $-m\rho_0\kappa^2$，对两支都为负。

把圆轨道判别式为零当成稳定性临界。判别式判断指定 $l$ 是否存在圆轨道；径向稳定性则由另一个二阶导数或线性恢复系数判断，两者不同。

把“稳定”理解为微扰自行衰减，或者所有未来时刻的角位置都与主问解相同。无阻尼的径向振动会持续存在，微小频率变化也可造成相位漂移；这些不等于轨道径向发散。

第（2）问仍写 $\omega=2v_0/l$，是把两问的初始速度混用。应先写 $\dot{\boldsymbol R}(0)=\boldsymbol v_1(0)-\boldsymbol v_2(0)$，再由相对距离得到 $\omega=v_0/l$。

质心运动半径用 $mv_0/(qB_0)$ 会大一倍，因为质心初速只有 $v_0/2$。积分时遗漏位置常数又会把圆心错放到初始质心处。

在 $t_*=\pi/(\Omega-\omega)$ 中照抄 $\omega$ 的根号符号，使快支、慢支停时交换。应分开写 $t_{*,+}$ 与 $t_{*,-}$，并用“角速度越接近 $\Omega$，相消越慢”检验。

把首次速度为零等同于最终停止。此时磁力虽为零，库仑斥力却仍在，电子立即获得非零加速度；也不能把电子 $2$ 的初始零速误当成电子 $1$ 的首次零速。

## 八、课堂讲解建议

课堂先在图5-1确定电子编号、磁场向外和两问的初始速度。教师让学生分别计算两问的质心初速度与相对初速度，板书同时保留 $0,v_0/2$ 和 $2v_0,v_0$，避免后续仅靠记忆区分因子 $2$。

讲圆轨道时，在图5-2先标向内磁力和向外斥力，再确定半径是 $l/2$。教师可先让学生判断磁力必须大于斥力，然后列方程、配方并讨论两个正根，不直接告知哪个分支更快。

讲稳定性时，课堂先问“半径略变，切向速度是否仍为原值”。教师从图5-3的径向速度产生切向磁力讲起，再从切向牛顿方程推出守恒量。板书把径向一阶变化分成几何、库仑、磁力三列，全部代入后才合并，尤其检查慢速支的回复系数。

课堂可用有效势能作第二条验证路线，强调“代数根合并”和“势能二阶导数为零”不是同一件事。教师不宜仅用结论性的稳定、不稳定标签，要让学生指出到底是哪一个小量有界，哪一个相位允许漂移。

讲第（2）问时，在图5-4区分固定圆心 $G$、初始质心 $O$、当前质心 $M$ 和相对连线。教师先完成质心速度积分，再加上绕质心速度；课堂用图5-5演示两个等长箭头从同向转到反向，最后以模平方证明没有更早的零点。

结束时让学生逐项回代初值、检查两停时的根号符号，并分析瞬时静止后的加速度。板书留出临界点和大间距两个极限，但同时提醒非相对论速率约束，避免把形式极限误当成任意真实电子实验都可实现。

## 九、变式训练

**变式1：间距是临界间距的两倍时，比较两支圆轨道。**

保持 $m,q,B_0$ 不变，取 $l=2l_c$。求 $\omega_\pm/\Omega$、第（1）问两个速率、两支径向小振动频率，并写第（2）问的首次停止时间。

由临界关系 $C/l_c^3=\Omega^2/4$：

$$
\frac C{l^3}
=\frac{C}{8l_c^3}=\frac{\Omega^2}{32}.
$$

因而

$$
\begin{aligned}
D&=\frac\Omega2\sqrt{1-\frac18}
=\frac\Omega2\sqrt{\frac78},\\
\frac{\omega_\pm}{\Omega}
&=\frac{1\pm\sqrt{7/8}}2,\\
v_{0,\pm}^{(1)}
&=\frac{\Omega l}{4}\left(1\pm\sqrt{\frac78}\right).
\end{aligned}
$$

两支径向频率均为

$$
\boxed{\kappa=\Omega\sqrt{\frac{31}{32}}}.
$$

第（2）问的初速为 $2v_{0,\pm}^{(1)}$，对应

$$
\boxed{
t_{*,+}=\frac{2\pi}{\Omega(1-\sqrt{7/8})},
\qquad
t_{*,-}=\frac{2\pi}{\Omega(1+\sqrt{7/8})}
}.
$$

分母都是正数。将较慢根取极限，停时接近 $\pi/\Omega$；较快根更接近 $\Omega$，停时明显更长。径向频率相同不代表圆周运动或停时相同。

<!-- KEEP_TOGETHER_START -->

**变式2：用给定电子参数检验速度、长度与时间量级。**

给定

$$
\begin{aligned}
m&=9.1093837139\times10^{-31}\,\mathrm{kg},\\
q&=1.602176634\times10^{-19}\,\mathrm C,\\
k_e&=8.9875517923\times10^9\,\mathrm{N\,m^2\,C^{-2}},\\
B_0&=1.00\,\mathrm T,\qquad l=1.00\times10^{-6}\,\mathrm m.
\end{aligned}
$$

求两问允许速率、质心半径、首次停时，并检验非相对论近似。以下额外给定 $c=2.99792458\times10^8\,\mathrm{m\,s^{-1}}$。

<!-- KEEP_TOGETHER_END -->

先算基本参数：

$$
\begin{aligned}
\Omega
&=\frac{(1.602176634\times10^{-19})(1.00)}
{9.1093837139\times10^{-31}}
\approx1.7588200084\times10^{11}\,\mathrm{s^{-1}},\\
l_c
&=2\left[
\frac{(8.9875517923\times10^9)(9.1093837139\times10^{-31})}
{(1.00)^2}
\right]^{1/3}\\
&\approx4.0309442941\times10^{-7}\,\mathrm m.
\end{aligned}
$$

题给 $l>l_c$，所以两根存在。为了避免电荷量数量级掩盖判断，可先算无量纲组合

$$
\frac{C}{\Omega^2l^3}
=\frac{2k_em}{B_0^2l^3}
\approx0.0163742,
$$

它小于 $1/4$。代入二次根式，得到

$$
\begin{aligned}
\omega_-&\approx2.9286962327\times10^9\,\mathrm{s^{-1}},\\
\omega_+&\approx1.7295330461\times10^{11}\,\mathrm{s^{-1}}.
\end{aligned}
$$

第（1）问每个电子速率为 $\omega_\pm l/2$：

$$
v_{0,-}^{(1)}\approx1464.35\,\mathrm{m\,s^{-1}},
\qquad
v_{0,+}^{(1)}\approx86476.65\,\mathrm{m\,s^{-1}}.
$$

第（2）问只有一个电子初始运动，所以其速率为 $\omega_\pm l$：

$$
v_{0,-}^{(2)}\approx2928.70\,\mathrm{m\,s^{-1}},
\qquad
v_{0,+}^{(2)}\approx172953.30\,\mathrm{m\,s^{-1}}.
$$

相应质心半径为

$$
\begin{aligned}
R_{c,-}
&=\frac{\omega_-l}{2\Omega}
\approx8.32574\times10^{-9}\,\mathrm m,\\
R_{c,+}
&=\frac{\omega_+l}{2\Omega}
\approx4.91674\times10^{-7}\,\mathrm m.
\end{aligned}
$$

首停时按分支分别代入：

$$
\begin{aligned}
t_{*,-}
&=\frac{\pi}{1.7588200084\times10^{11}-2.9286962327\times10^9}
\approx1.81644\times10^{-11}\,\mathrm s,\\
t_{*,+}
&=\frac{\pi}{1.7588200084\times10^{11}-1.7295330461\times10^{11}}
\approx1.07269\times10^{-9}\,\mathrm s.
\end{aligned}
$$

较快支的分母是两相近角速度之差，数值计算必须保留足够有效数字，不能先把 $\omega_+$ 取成 $\Omega$ 再作减法。若需更稳健地求这个小分母，可利用两根乘积：

$$
\Omega-\omega_+=\omega_-=\frac{C/l^3}{\omega_+}.
$$

最大初速与光速之比约为 $5.77\times10^{-4}$，非相对论速率条件满足；这只核对题设的经典速度近似，不意味着已加入题外的辐射或量子模型。两支径向频率都约为 $1.74436\times10^{11}\,\mathrm{s^{-1}}$。

**变式3：两个电子初始都运动时，是否还能出现零速？**

取初始位置仍为 $(l/2,0)$、$(-l/2,0)$，但初速度改成 $a\boldsymbol e_y$、$b\boldsymbol e_y$，其中 $a>b\geq0$。求保持间距 $l$ 的条件，并判断电子 $1$ 是否能再次瞬时停止。

质心初速度与相对初速度分别为

$$
\boldsymbol V_c(0)=\frac{a+b}{2}\boldsymbol e_y,
\qquad
\dot{\boldsymbol R}(0)=(a-b)\boldsymbol e_y.
$$

因此恒距条件为

$$
\omega=\frac{a-b}{l}\in\{\omega_-,\omega_+\},
\qquad l\geq l_c.
$$

和 $a+b$ 只决定质心运动幅度，并不进入相对圆轨道方程；差 $a-b$ 才决定相对角速度。电子 $1$ 速度为

$$
\boldsymbol v_1(t)
=\frac{a+b}{2}\boldsymbol e_\phi(\Omega t)
+\frac{a-b}{2}\boldsymbol e_\phi(\omega t).
$$

将模平方展开：

$$
\begin{aligned}
|\boldsymbol v_1(t)|^2
&=\frac{(a+b)^2+(a-b)^2}{4}
+\frac{a^2-b^2}{2}\cos[(\Omega-\omega)t]\\
&=\frac{a^2+b^2}{2}
+\frac{a^2-b^2}{2}\cos[(\Omega-\omega)t].
\end{aligned}
$$

因为 $a^2-b^2>0$，最小值在相位差为奇数倍 $\pi$ 时取得：

$$
\min|\boldsymbol v_1|^2
=\frac{a^2+b^2-a^2+b^2}{2}=b^2.
$$

所以 $b>0$ 时电子 $1$ 永远不能零速；$b=0$ 时才回到本题的首停时。等模矢量是精确相消的必要条件，不能把本题的相位差条件机械套给两个不等模分量。

此刻电子 $2$ 的最大速率为 $a$，而初始速率为 $b$；两粒子在相位差 $\pi$ 时交换速率大小。整个过程中库仑势能因间距不变而固定，总动能也保持不变，可再用 $a^2+b^2$ 检查。

**变式4：临界场附近分支合并，径向恢复频率是否也消失？**

固定 $l,m,q$，令临界场为 $B_c=\sqrt{8k_em/l^3}$，并取 $B_0=B_c(1+\epsilon)$，其中 $0<\epsilon\ll1$。定义 $\Omega_c=qB_c/m$。求两个角速度分支的首要分裂量、径向频率及两个首次停止时间的首要变化。

由临界条件 $C/l^3=\Omega_c^2/4$，而 $\Omega=\Omega_c(1+\epsilon)$：

$$
\begin{aligned}
D
&=\sqrt{\frac{\Omega_c^2}{4}(1+\epsilon)^2-\frac{\Omega_c^2}{4}}\\
&=\frac{\Omega_c}{2}\sqrt{2\epsilon+\epsilon^2}.
\end{aligned}
$$

因此精确两根为

$$
\omega_\pm
=\frac{\Omega_c}{2}
\left(1+\epsilon\pm\sqrt{2\epsilon+\epsilon^2}\right).
$$

使用 $\sqrt{2\epsilon+\epsilon^2}
=\sqrt{2\epsilon}\,[1+\epsilon/4+O(\epsilon^2)]$：

$$
\omega_\pm
=\frac{\Omega_c}{2}
\left[1\pm\sqrt{2\epsilon}+\epsilon
+O(\epsilon^{3/2})\right].
$$

分支分裂的首要量为 $\omega_+-\omega_-=\Omega_c\sqrt{2\epsilon}+O(\epsilon^{3/2})$，它是 $\sqrt\epsilon$ 级，不是 $\epsilon$ 级。临界附近对参数的灵敏度较大。

径向频率却为

$$
\begin{aligned}
\kappa^2
&=\Omega^2-\frac C{l^3}
=\Omega_c^2\left(\frac34+2\epsilon+\epsilon^2\right),\\
\kappa
&=\frac{\sqrt3\,\Omega_c}{2}
\left[1+\frac43\epsilon+O(\epsilon^2)\right].
\end{aligned}
$$

$\epsilon\to0^+$ 时径向频率仍趋于 $\sqrt3\,\Omega_c/2$，没有软化至零；两根合并与径向失稳是不同的判断。

最后，首停时的精确式为

$$
t_{*,\pm}
=\frac{2\pi}{\Omega_c}
\frac1{1+\epsilon\mp\sqrt{2\epsilon+\epsilon^2}}.
$$

<!-- KEEP_TOGETHER_START -->

令分母偏离 $1$ 的量为 $h=\epsilon\mp\sqrt{2\epsilon+\epsilon^2}$。展开 $(1+h)^{-1}=1-h+h^2+O(h^3)$，并保留到 $\epsilon$：

$$
\boxed{
t_{*,\pm}
=\frac{2\pi}{\Omega_c}
\left[1\pm\sqrt{2\epsilon}+\epsilon
+O(\epsilon^{3/2})\right]
}.
$$

平方项贡献 $2\epsilon$，与一次项中的 $-\epsilon$ 合成 $+\epsilon$；若只保留线性倒数而漏掉 $h^2$，便会弄错二阶项。较快支停时增加、较慢支停时减少，均回到临界值 $2\pi/\Omega_c$。

<!-- KEEP_TOGETHER_END -->

这里还有一个精确的有理化核验：两种分母的乘积为

$$
(1+\epsilon)^2-(2\epsilon+\epsilon^2)=1.
$$

因此可直接把精确停时写成

$$
t_{*,\pm}
=\frac{2\pi}{\Omega_c}
\left(1+\epsilon\pm\sqrt{2\epsilon+\epsilon^2}\right).
$$

它与上述展开一致，且不需要在数值上相减两个接近的量。这种有理化与变式2中利用两根乘积求小根的思想相同。

<!-- question-complete -->
