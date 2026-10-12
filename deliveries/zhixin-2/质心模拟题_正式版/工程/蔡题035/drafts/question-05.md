# 第 5 题

<!-- question-start -->
一名质量 $m=70\ \mathrm{kg}$ 的蹦极者从高出水面 $h=90\ \mathrm m$ 的平台由静止竖直下落。其脚上系有原长为 $L$、劲度系数为 $k$ 的理想弹性绳，另一端固定在平台。弹性绳伸长时服从胡克定律，松弛时不施力。

到达水面时，人的速度恰为零，加速度大小为 $a_0=2g$。取 $g=10\ \mathrm{m/s^2}$，人的身高、绳的质量、空气阻力及其他能量损失均忽略。

1. 求 $L$ 和 $k$。
2. 求人静止悬挂时弹性绳的伸长量。
3. 求下降过程中的最大速率 $v_{\max}$。
4. 求弹性绳张紧阶段相对于平衡位置的简谐运动振幅 $A$ 和角频率 $\omega$。
5. 求从平台下落至水面所需时间 $t$。

![图 5-1　平台、绳原长位置、平衡位置与最低点。](../figures/question-05.png)

<!-- question-end -->

## 一、题型定位

松绳自由落体与张紧后弹性振动的分段运动。先利用最低点能量和加速度两个独立条件反求弹性参数，再用平衡位置确定最大速率，最后以速度连续条件确定简谐阶段的初相位。

## 二、知识点

- 弹性绳只能提供拉力，松弛阶段不能套用弹簧简谐方程。
- 从静止到最低点的机械能守恒。
- 最低点速度为零，但加速度一般不为零。
- 弹性力与重力平衡位置对应速度极大位置。
- 以平衡位置为原点的简谐运动及初相位筛选。
- 分段运动的时间相加和交界处位置、速度连续。

## 三、物理图像

取从平台竖直向下为正方向，人的下降距离为 $y$。当 $0\leq y<L$ 时绳松弛，只有重力。当 $y\geq L$ 时，绳伸长量为 $\delta=y-L$，向上拉力大小为 $k\delta$。

运动中有四个不能混同的位置：平台 $y=0$、绳刚张紧的 $y=L$、合力为零的 $y=y_e$、到达水面的最低点 $y=h$。最低点是速度为零的位置；平衡位置是加速度为零的位置，两者不同。

## 四、解题入口

最低点的伸长量 $\delta_{\max}=h-L$ 同时出现在弹性势能和拉力中。先用它代替 $L$，列能量方程及最低点受力方程，便可消去 $k$。求时间时再回到两段运动，不能把整个 $90\ \mathrm m$ 都视作自由落体或简谐运动。

## 五、解析

（1）确定最低点加速度方向。

人在水面处速度恰为零，此前一直向下，此处为下落转折点。在继续服从题设力学模型的情况下，后续速度将向上，所以最低点加速度向上。按向下为正的约定，

$$
a(h)=-2g.
$$

对张紧绳，牛顿第二定律为

$$
ma=mg-k(y-L).
$$

在 $y=h$ 处代入：

$$
-2mg=mg-k(h-L),
$$

所以

$$
k(h-L)=3mg.
$$

这不是 $k(h-L)=2mg$，因为绳的拉力除了提供向上的合力，还必须抵消向下的重力。

（2）最低点能量方程及参数求解。

以平台处的重力势能为零，人的重力势能为 $-mgy$。从平台静止下落到水面，初末动能均为零，弹性绳初态未伸长。因此

$$
mgh=\frac12k(h-L)^2.
$$

令 $\delta_{\max}=h-L>0$，两条方程写成

$$
k\delta_{\max}=3mg,\qquad
\frac12k\delta_{\max}^2=mgh.
$$

第二式除以第一式：

$$
\frac{\frac12k\delta_{\max}^2}{k\delta_{\max}}
=\frac{mgh}{3mg}.
$$

约去共同因子得

$$
\frac12\delta_{\max}=\frac h3,
\qquad
\delta_{\max}=\frac{2h}{3}=60\ \mathrm m.
$$

因此

$$
\boxed{L=h-\delta_{\max}=30\ \mathrm m.}
$$

再由最低点拉力条件，

$$
\begin{aligned}
k&=\frac{3mg}{\delta_{\max}}\\
&=\frac{3\times70\times10}{60}\ \mathrm{N/m}\\
&=\boxed{35\ \mathrm{N/m}}.
\end{aligned}
$$

检查弹性势能：

$$
\frac12k\delta_{\max}^2
=\frac12\times35\times60^2
=63000\ \mathrm J,
$$

而重力势能减少 $mgh=70\times10\times90=63000\ \mathrm J$，完全一致。

（3）静止悬挂时的伸长量。

人静止悬挂时合力为零，所以

$$
mg=k\delta_e.
$$

因此

$$
\boxed{\delta_e=\frac{mg}{k}=20\ \mathrm m.}
$$

平衡位置的下降距离为

$$
y_e=L+\delta_e=50\ \mathrm m.
$$

题目求的是伸长量 $\delta_e=20\ \mathrm m$，不是绳的总长度 $50\ \mathrm m$。两者在图 5-2 中分别标示。

![图 5-2　分段加速度、平衡位置与张紧阶段的相位关系。](../figures/solution-05.png)

（4）为什么最大速率出现在平衡位置？

绳未张紧时 $a=g>0$，人向下的速率不断增加。张紧后，

$$
a(y)=g-\frac{k}{m}(y-L).
$$

在 $L<y<y_e$，拉力小于重力，故 $a>0$，向下速率仍增加。在 $y_e<y<h$，拉力大于重力，故 $a<0$，向下速率减小。因此 $y=y_e$ 是整个下降过程的最大速率位置。

能量方程可写为

$$
\frac12mv^2=mgy-\frac12k(y-L)^2
\qquad(y\geq L).
$$

对 $y$ 求导也可验证：

$$
m v\frac{\mathrm dv}{\mathrm dy}=mg-k(y-L).
$$

在 $v>0$ 的下落区间，速率的驻点满足右侧为零，即 $y=y_e$。右侧随 $y$ 严格减小，因此该驻点为最大值。

代入 $y_e=L+\delta_e$：

$$
\frac12mv_{\max}^2
=mg(L+\delta_e)-\frac12k\delta_e^2.
$$

由 $k\delta_e=mg$，有 $k\delta_e^2=mg\delta_e$，因此

$$
\begin{aligned}
\frac12mv_{\max}^2
&=mgL+\frac12mg\delta_e,\\
v_{\max}^2
&=2gL+g\delta_e.
\end{aligned}
$$

代入数值：

$$
v_{\max}^2=2\times10\times30+10\times20=800\ \mathrm{m^2/s^2}.
$$

所以

$$
\boxed{v_{\max}=20\sqrt2\ \mathrm{m/s}\approx28.3\ \mathrm{m/s}.}
$$

（5）张紧阶段化为简谐运动。

以平衡位置为原点，仍取向下为正，定义

$$
z=y-y_e=y-L-\delta_e.
$$

因为 $y=z+L+\delta_e$，所以

$$
\begin{aligned}
m\ddot z
&=mg-k(z+\delta_e)\\
&=(mg-k\delta_e)-kz\\
&=-kz.
\end{aligned}
$$

利用平衡关系消去常量项，得到

$$
\ddot z+\omega^2z=0,
\qquad
\boxed{\omega=\sqrt{\frac{k}{m}}
=\sqrt{\frac{35}{70}}\ \mathrm{s^{-1}}
=\frac1{\sqrt2}\ \mathrm{s^{-1}}.}
$$

最低点位于

$$
z_{\max}=h-y_e=90-50=40\ \mathrm m,
$$

且速度为零，所以简谐阶段的振幅为

$$
\boxed{A=40\ \mathrm m.}
$$

振幅是相对平衡位置的最大偏离，不是弹性绳最大伸长量 $60\ \mathrm m$。同时

$$
A\omega=40\frac1{\sqrt2}=20\sqrt2\ \mathrm{m/s},
$$

与独立能量法得到的最大速率一致。

（6）自由落体阶段的时间和交界速度。

绳从松弛变为恰好张紧时下降距离为 $L$。由

$$
L=\frac12gt_1^2,
$$

取正时间根：

$$
t_1=\sqrt{\frac{2L}{g}}
=\sqrt6\ \mathrm s
\approx2.44949\ \mathrm s.
$$

此刻速度向下，大小为

$$
v_1=gt_1=\sqrt{2gL}=10\sqrt6\ \mathrm{m/s}.
$$

绳刚开始伸长时弹性力从零连续增大，没有冲量，速度不会突变。这个 $v_1$ 就是简谐阶段的初速度。

（7）利用初相位求从张紧到最低点的时间。

把简谐阶段开始时重新记为 $s=0$。此时

$$
z(0)=L-y_e=-20\ \mathrm m,\qquad
\dot z(0)=10\sqrt6\ \mathrm{m/s}>0.
$$

采用

$$
z(s)=A\sin(\omega s+\varphi),
\qquad
\dot z(s)=A\omega\cos(\omega s+\varphi).
$$

由初始位置，

$$
\sin\varphi=\frac{-20}{40}=-\frac12.
$$

仅由正弦值可以得到多个相位，必须用初速度方向筛选。因为 $\dot z(0)>0$，所以 $\cos\varphi>0$，初相位应取第四象限代表值

$$
\varphi=-\frac{\pi}{6}.
$$

核对速度：

$$
A\omega\cos\varphi
=\frac{40}{\sqrt2}\frac{\sqrt3}{2}
=10\sqrt6\ \mathrm{m/s},
$$

与自由落体末速度一致。

第一次到达最低点时 $z=A$，相位首次到达 $\pi/2$，因此

$$
\begin{aligned}
\omega t_2-\frac{\pi}{6}&=\frac{\pi}{2},\\
\omega t_2&=\frac{2\pi}{3},\\
t_2&=\frac{2\pi}{3\omega}
=\frac{2\sqrt2\pi}{3}\ \mathrm s.
\end{aligned}
$$

这段相位变化是 $2\pi/3$，不是从平衡位置到极端位置的 $\pi/2$。所以不能直接使用简谐周期的四分之一。

总时间为

$$
\begin{aligned}
t&=t_1+t_2\\
&=\sqrt6+\frac{2\sqrt2\pi}{3}\ \mathrm s\\
&\approx2.44949+2.96192\ \mathrm s\\
&=\boxed{5.41\ \mathrm s}.
\end{aligned}
$$

（8）用时间积分独立复核简谐段。

以平衡位置为原点，机械能关系写为

$$
v^2=\omega^2(A^2-z^2).
$$

在第一次下落过程中 $v=\dot z>0$，所以

$$
\mathrm dt=\frac{\mathrm dz}{\omega\sqrt{A^2-z^2}}.
$$

由 $z=-20$ 到 $z=40$ 积分：

$$
\begin{aligned}
t_2
&=\frac1\omega\int_{-20}^{40}
\frac{\mathrm dz}{\sqrt{40^2-z^2}}\\
&=\frac1\omega
\left[\arcsin\frac z{40}\right]_{-20}^{40}\\
&=\frac1\omega\left(\frac\pi2+\frac\pi6\right)
=\frac{2\pi}{3\omega}.
\end{aligned}
$$

这里使用标准代换 $z=A\sin\theta$；最低点处根号趋于零，但积分是收敛的，因此到达转折点所需时间有限。

（9）简谐公式的适用区间。

绳张紧要求 $y\geq L$，也就是

$$
z\geq-\delta_e=-20\ \mathrm m.
$$

如果把幅度 $40\ \mathrm m$ 的正弦运动延伸一整周期，它会到达 $z=-40\ \mathrm m$，对应 $y=10\ \mathrm m<L$。此时绳早已松弛，不能继续提供向下的“弹性推力”，所以完整运动不是一整段简谐运动。

本题第（4）问的 $A,\omega$ 表征张紧阶段。下落至最低点所经过的全部张紧区间满足 $z\geq-20\ \mathrm m$，所以前面的时间计算有效。若继续研究回弹，必须在再次到达 $y=L$ 时切换回重力自由运动方程。

还需解释最低点处 $1/v$ 趋于无穷为何不导致时间无穷。令距最低点的位移差为 $\varepsilon=A-z>0$，则

$$
\begin{aligned}
A^2-z^2&=(A-z)(A+z)=\varepsilon(2A-\varepsilon),\\
v&=\omega\sqrt{\varepsilon(2A-\varepsilon)}
\simeq\omega\sqrt{2A\varepsilon}.
\end{aligned}
$$

最后一式只用于 $\varepsilon\ll A$ 的局部检验。距最低点还有 $\varepsilon_0$ 时，剩余时间近似为

$$
\Delta t\simeq\frac1{\omega\sqrt{2A}}
\int_0^{\varepsilon_0}\frac{\mathrm d\varepsilon}{\sqrt\varepsilon}
=\frac{\sqrt{2\varepsilon_0/A}}{\omega}.
$$

根号奇点的积分仍然有限，并且随 $\varepsilon_0\to0$ 而趋于零。反过来写成 $\varepsilon\simeq A\omega^2(\Delta t)^2/2$，再用 $A\omega^2=20\ \mathrm{m/s^2}=2g$，就得到最低点附近在向上加速度 $2g$ 作用下的局部二次运动规律。它同时核对了积分的收敛性、简谐参数和题给最低点加速度，不需要将速度为零误解为“人永远到不了最低点”。

本题是忽略人体尺寸、绳质量、耗散和材料非线性的理想模型，给出的参数不能用于实际蹦极装备或安全设计。

## 六、关键洞察

本题最低点的能量条件与力条件分别约束“总能量积累”和“局部瞬时加速度”。它们缺一不可：只知道最低点位置，可以用多组 $L,k$ 达到同一位置；再指定最低点加速度才能唯一确定。

把最低点向上加速度一般化为 $a_0=\alpha g$，仍从静止下落高度 $h$，则

$$
k\delta_{\max}=(1+\alpha)mg,\qquad
\frac12k\delta_{\max}^2=mgh.
$$

消元得到

$$
\begin{aligned}
\delta_{\max}&=\frac{2h}{1+\alpha},\\
L&=\frac{\alpha-1}{\alpha+1}h,\\
k&=\frac{(1+\alpha)^2mg}{2h}.
\end{aligned}
$$

弹性绳原长非负要求 $\alpha\geq1$。这一限制由初始松绳、重力供能和最低点条件共同确定。

对应平衡伸长与振幅为

$$
\delta_e=\frac{2h}{(1+\alpha)^2},
\qquad
A=\delta_{\max}-\delta_e
=\frac{2h\alpha}{(1+\alpha)^2}.
$$

代入 $\alpha=2$、$h=90\ \mathrm m$，立即恢复 $\delta_e=20\ \mathrm m$ 和 $A=40\ \mathrm m$。参数公式还说明，提高最低点向上加速度要求，会使原长增大、劲度系数增大；必须重新计算整个运动，不能只改变最低点受力。

## 七、易错点

- 把最低点加速度方向误取为向下，从而写错拉力。
- 把绳的伸长量、总长和人相对平衡位置的位移混用。
- 认为绳一张紧就开始减速；实际上张紧后还要继续加速至平衡位置。
- 将最大伸长 $60\ \mathrm m$ 当作振幅。
- 只由初始位置选相位，漏掉初速度方向，得到错误的时间支。
- 将张紧段一律取四分之一周期。
- 把松绳阶段也套进弹簧简谐方程，得到不存在的弹性推力。

## 八、课堂讲解建议

先让学生在同一条竖直线上标出 $0,L,y_e,h$，并写明每一段加速度正负，再计算参数。课堂中不要先给相位角，应由张紧时的 $z(0)$ 和 $\dot z(0)$ 共同确定。

完成时间后，用相位圆和定积分各核查一次。板书最后画出“只截取正弦曲线中绳保持张紧的部分”，帮助学生区分数学延拓与实际运动。

## 九、变式训练

变式一：在相同无耗散模型中，假设人到达最低点后立即回弹且不受水作用，求返回平台的时间和完整往返周期。

回弹过程与下落过程时间反演对称。从最低点到绳重新松弛处所需时间仍为 $t_2$，到达 $y=L$ 时速度向上，大小仍为 $v_1=\sqrt{2gL}$。之后绳松弛，人在重力作用下继续上升：

$$
\Delta y_{\mathrm{rise}}=\frac{v_1^2}{2g}=L.
$$

因此恰好回到平台高度，速度为零；松绳上升时间为

$$
t_3=\frac{v_1}{g}=\sqrt{\frac{2L}{g}}=t_1.
$$

从平台出发又回到平台的完整周期为

$$
\boxed{
T_{\mathrm{whole}}=2(t_1+t_2)
=2\sqrt6+\frac{4\sqrt2\pi}{3}
\approx10.82\ \mathrm s.
}
$$

而把绳误作可压缩弹簧得到的完整简谐周期为 $2\pi/\omega=2\sqrt2\pi\approx8.89\ \mathrm s$，两者不同。差别来自上方松绳区的真实运动，不是相位选择或数值舍入误差。

这里的时间反演对称也可以直接用积分验证。回弹的张紧段仍满足同一能量关系，但速度取负支，因而

$$
\begin{aligned}
t_{\mathrm{return,taut}}
&=\int_A^{-\delta_e}
\frac{\mathrm dz}{-\omega\sqrt{A^2-z^2}}\\
&=\frac1\omega\int_{-\delta_e}^{A}
\frac{\mathrm dz}{\sqrt{A^2-z^2}}=t_2.
\end{aligned}
$$

积分上下限和速度的负号同时改变，时间仍为正。松绳上升段速度满足 $v=-\sqrt{2gy}$，所以

$$
t_{\mathrm{return,free}}
=\int_L^0\frac{\mathrm dy}{-\sqrt{2gy}}
=\left[\sqrt{\frac{2y}{g}}\right]_0^L=t_1.
$$

这两式分别验证张紧段和松弛段的返回时间，而不是把整段返回过程误作同一个简谐周期的一部分。只有绳无耗散、空气阻力忽略且最低点不受水的冲击时，往返能量和时间才有这种对称性；一旦存在耗散，返回高度、相位及运动周期都需要重新计算。

变式二：在无耗散、绳只受拉的模型中，把最低点向上加速度要求改为 $3g$，质量 $70\,\mathrm{kg}$、下降高度 $90\,\mathrm m$、$g=10\,\mathrm{m/s^2}$ 不变。求绳原长和劲度系数。

解：最低点 $k\delta=4mg$，从平台到最低点能量守恒给 $k\delta^2/2=mgh$。两式相除得 $\delta=h/2=45\,\mathrm m$，故

$$
L=h-\delta=45\,\mathrm m,\qquad
k=\frac{4mg}{\delta}=\frac{560}{9}\,\mathrm{N/m}.
$$

原长为正、初态绳松弛，与模型一致。提高最低点加速度同时改变了原长与劲度，不能保持原 $k=35\,\mathrm{N/m}$。

变式三：保持原绳 $L=30\,\mathrm m,k=35\,\mathrm{N/m}$，将人的质量增为 $140\,\mathrm{kg}$，假定下方没有水面或其他阻挡。求最低点下降高度及最大速率。

解：从静止到最低点有 $k\delta^2/2=mg(L+\delta)$，取正根 $\delta=mg/k+\sqrt{(mg/k)^2+2mgL/k}$。这里 $mg/k=40\,\mathrm m$，所以

$$
h_{\min}=L+\delta=70+20\sqrt{10}\,\mathrm m\approx133.246\,\mathrm m.
$$

最大速度在张力等于重力处 $\delta=mg/k$，能量给 $v_{\max}^2=2gL+mg^2/k=1000\,\mathrm{m^2/s^2}$，故 $v_{\max}=10\sqrt{10}\,\mathrm{m/s}$。这个最低点已低于原水面，故必须明确移除水面条件。

变式四：质量、原长保持本题值，劲度增为四倍，即 $k'=140\,\mathrm{N/m}$，仍假定下方无阻挡。求最低点和最低点向上加速度。

解：$mg/k'=5\,\mathrm m$。同一能量二次方程给 $\delta'=5+\sqrt{25+300}=5+5\sqrt{13}\,\mathrm m$，故下降高度 $h'=35+5\sqrt{13}\approx53.0278\,\mathrm m$。最低点受力给

$$
a_{\rm up}=\frac{k'\delta'}m-g=10\sqrt{13}\,\mathrm{m/s^2}\approx36.0555\,\mathrm{m/s^2}.
$$

更硬的绳使最低点升高，但加速度增大；两者由能量与受力两条不同条件共同决定。
