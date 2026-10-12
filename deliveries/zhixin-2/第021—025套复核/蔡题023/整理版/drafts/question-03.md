# 第 3 题

<!-- question-start -->
在垂直纸面向里的匀强磁场中，有两个质量均为 $m$ 的点电荷 $A$、$B$，初始间距为 $L$，电荷均为 $+q$，初始静止。考虑两者间静电作用，静电常数为 $K$，不考虑相对论效应。

（1）磁感应强度为 $B$ 时，求之后两粒子的最大间距。

（2）另从相同的静止初态出发，将 $B$ 粒子的电荷改为 $-q$。要求两粒子不发生碰撞，求磁场最小值 $B_0$。

（3）在异号电荷情形，磁感应强度取 $B_1>B_0$，求之后两粒子的最近距离 $l_0$。

数值参数：$B=2.41\times10^{-2}\,\mathrm T$、$L=7.21\,\mathrm m$、$m=1.97\times10^{-11}\,\mathrm{kg}$、$K=8.98\times10^9\,\mathrm{N\,m^2\,C^{-2}}$、$B_1=1.58\,\mathrm T$。数值表中的小写长度标识统一为初始间距 $L$；电荷大小保留为 $q>0$。

![图 3-1　两粒子的初始位置及垂直纸面向里的磁场。](../figures/question-03.png)
<!-- question-end -->

## 一、题型定位

同号和异号电荷都属于两体电磁动力学，但它们的对称性不同。同号时质心静止，连接两粒子的相对位置矢量会转动；异号时两粒子沿同一横向方向偏转，质心移动，而间距沿固定方向变化。

解答要分别消去不需要的运动自由度，把总能量化为关于间距的一维有效势。最大或最小距离是径向速度为零的位置，不等于粒子总速度为零。对防碰撞阈值还须检查重根是否在有限时间达到。

## 二、知识点

两个质量相同的粒子总动能可分解为
$$
T=m|\dot{\boldsymbol R}|^2+\frac m4|\dot{\boldsymbol r}|^2,
$$
其中 $\boldsymbol R=(\boldsymbol r_A+\boldsymbol r_B)/2$，$\boldsymbol r=\boldsymbol r_B-\boldsymbol r_A$。约化质量为 $m/2$；相对运动动能前面的系数是 $m/4$，不是 $m/2$。

磁力不做功，静电势能为 $Kq_Aq_B/r$。普通机械角动量在磁场中未必守恒，但角向运动方程可以积分得到包含磁场项的守恒量。根的判定必须兼顾初态可达性、能量和运动时间。

## 三、物理图像

同号电荷从静止开始互相排斥，间距先增加。随着横向速度出现，磁力改变轨迹，使相对位置矢量旋转；向外运动会遇到有效磁势垒，最大距离有限。

异号电荷从静止开始接近。虽然两者 $x$ 方向速度相反，但电荷也相反，因此磁力的 $y$ 分量同向，质心向 $+y$ 移动。共同的 $y$ 速度产生相反的 $x$ 向磁力，抵抗静电吸引。防碰撞靠的是这种耦合，不是两粒子各自绕固定圆心运行。

## 四、解题入口

统一取 $\boldsymbol B=-B\boldsymbol e_z$，初始两粒子在 $x=\mp L/2$，质心在原点。磁力的平面分量为
$$
q_i\boldsymbol v_i\times(-B\boldsymbol e_z)
=q_iB(-v_{iy},v_{ix}).
$$
同号先证明质心静止，再积分相对角向方程；异号使用 $\boldsymbol r_A=(-r/2,Y)$、$\boldsymbol r_B=(r/2,Y)$，先积分质心纵向速度。两种情形最后都用总能量确定距离转折点，但不能共用同一个角动量式。

## 五、解析

（1）写出完整两粒子方程和能量。

令 $r=|\boldsymbol r_B-\boldsymbol r_A|$，则
$$
\begin{aligned}
m\ddot{\boldsymbol r}_A
&=Kq_Aq_B\frac{\boldsymbol r_A-\boldsymbol r_B}{r^3}
+q_AB\,\boldsymbol e_z\times\dot{\boldsymbol r}_A,\\
m\ddot{\boldsymbol r}_B
&=Kq_Aq_B\frac{\boldsymbol r_B-\boldsymbol r_A}{r^3}
+q_BB\,\boldsymbol e_z\times\dot{\boldsymbol r}_B.
\end{aligned}
$$
初始速度为零，故守恒总能量为
$$
\frac m2(v_A^2+v_B^2)+\frac{Kq_Aq_B}{r}
=\frac{Kq_Aq_B}{L}.
$$
磁力项点乘各自速度均为零，静电力对两者所做总功等于静电势能减少量。这是后面能量式的依据。

（2）同号时证明质心固定。

取 $q_A=q_B=q$，两式相加：
$$
2m\ddot{\boldsymbol R}
=2qB\,\boldsymbol e_z\times\dot{\boldsymbol R}.
$$
这是质心速度在匀强磁场中旋转的方程。初始 $\dot{\boldsymbol R}=0$，唯一解为 $\dot{\boldsymbol R}=0$，因此 $\boldsymbol R=0$ 始终成立。两粒子位置互为相反数，各自距质心为 $r/2$。

两式相减得到相对运动方程：
$$
m\ddot{\boldsymbol r}
=qB\,\boldsymbol e_z\times\dot{\boldsymbol r}
+\frac{2Kq^2}{r^3}\boldsymbol r.
$$
静电项的系数为两粒子加速度之差，所以是 $2Kq^2$，不能只保留单个粒子的库仑力。

（3）积分同号相对角向运动。

令 $\boldsymbol r=r\boldsymbol e_r(\varphi)$，定义 $\omega=qB/m>0$。相对速度为
$$
\dot{\boldsymbol r}=\dot r\boldsymbol e_r+r\dot\varphi\boldsymbol e_\varphi.
$$
由 $\boldsymbol e_z\times\boldsymbol e_r=\boldsymbol e_\varphi$、$\boldsymbol e_z\times\boldsymbol e_\varphi=-\boldsymbol e_r$，得到
$$
\begin{aligned}
\ddot r-r\dot\varphi^2
&=-\omega r\dot\varphi+\frac{2Kq^2}{mr^2},\\
r\ddot\varphi+2\dot r\dot\varphi&=\omega\dot r.
\end{aligned}
$$
第二式乘 $r$ 后，左端是乘积的导数：
$$
\frac d{dt}(r^2\dot\varphi)=\omega r\dot r
=\frac\omega2\frac d{dt}(r^2).
$$
积分并代入 $r(0)=L$、$\dot\varphi(0)=0$：
$$
\boxed{
r^2\dot\varphi=\frac\omega2(r^2-L^2),\qquad
\dot\varphi=\frac{qB}{2m}\left(1-\frac{L^2}{r^2}\right).
}
$$
当 $r>L$ 时 $\dot\varphi>0$，连接矢量逆时针转动，与初始向外速度受磁力向上偏转的方向一致。

图 3-2 中相对速度被分成 $\dot r$ 与 $r\dot\varphi$ 两部分。最大间距时只要求第一部分为零，第二部分通常仍不为零。

![图 3-2　同号电荷的相对径向运动与角向运动。](../figures/orbit-03.png)

（4）消去角速度，构造同号径向有效势。

质心固定，总动能为
$$
T=\frac m4\left(\dot r^2+r^2\dot\varphi^2\right).
$$
把第（3）步角速度代入能量：
$$
\boxed{
\frac m4\dot r^2
+\frac{q^2B^2}{16m}\frac{(r^2-L^2)^2}{r^2}
+\frac{Kq^2}{r}
=\frac{Kq^2}{L}.
}
$$
第二项来自相对运动的角向动能，不是磁力做功产生的势能。因为角向自由度已被消去，它在径向方程中起有效势的作用。

初始径向加速度为 $2Kq^2/(mL^2)>0$，故运动从 $r=L$ 向外开始。转折点除去初始 $L$ 后，还应存在一个 $r_{\max}>L$。

（5）逐步化简最大间距方程。

在 $r=r_{\max}$ 处取 $\dot r=0$：
$$
\frac{B^2}{16m}\frac{(r^2-L^2)^2}{r^2}
=K\left(\frac1L-\frac1r\right).
$$
约去两边共同的 $q^2$ 后，使用
$$
r^2-L^2=(r-L)(r+L),\qquad
\frac1L-\frac1r=\frac{r-L}{Lr}.
$$
对于所求非初始转折点 $r>L$，可约去 $r-L$：
$$
\frac{B^2}{16m}\frac{(r-L)(r+L)^2}{r^2}
=\frac K{Lr}.
$$
交叉相乘得到
$$
\boxed{B^2L(r-L)(r+L)^2=16Km\,r,\qquad r>L.}
$$
令 $x=r/L$、$\chi=16Km/(B^2L^3)$，方程为
$$
\begin{aligned}
(x-1)(x+1)^2&=\chi x,\\
\boxed{x^3+x^2-(1+\chi)x-1=0,\qquad x>1.}
\end{aligned}
$$
初始根 $r=L$ 在约分时已剔除；不能把它当作最大距离答案。

（6）证明所需根唯一并计算数值。

把方程写成 $h(x)=\chi$：
$$
h(x)=\frac{(x-1)(x+1)^2}{x}
=x^2+x-1-\frac1x.
$$
在 $x>1$，
$$
h'(x)=2x+1+\frac1{x^2}>0.
$$
又 $h(1)=0$，$h(x)\to+\infty$，所以任意 $\chi>0$ 都有且只有一个大于一的根。无需为了“显式”而写很长的三次根式；单调方程加清晰的数值求根已经给出唯一答案。

先逐项代入：
$$
\begin{aligned}
Km&=(8.98\times10^9)(1.97\times10^{-11})
=0.176906,\\
L^3&=(7.21)^3=374.805361\,\mathrm{m^3},\\
\chi&=\frac{16(0.176906)}
{(2.41\times10^{-2})^2(374.805361)}
\simeq13.00237437.
\end{aligned}
$$
解单调方程得到 $x\simeq3.314975196$，故
$$
\boxed{r_{\max}\simeq23.90097\,\mathrm m\approx23.9\,\mathrm m.}
$$

（7）异号时建立正确的运动对称性。

改为 $q_A=+q$、$q_B=-q$。初始两粒子受到相反的 $x$ 向吸引力，其 $x$ 向速度相反；磁力的 $y$ 分量却同向。由对称性及完整方程，可以保持
$$
\boldsymbol r_A=\left(-\frac r2,Y\right),\qquad
\boldsymbol r_B=\left(\frac r2,Y\right),
$$
直到发生碰撞或转折。这里 $r>0$ 是两粒子间距，连接方向仍沿 $x$，但质心 $Y$ 不再固定。

代入两粒子的 $x$、$y$ 方程：
$$
\boxed{
\ddot r=\frac{2qB}{m}\dot Y-\frac{2Kq^2}{mr^2},\qquad
\ddot Y=-\frac{qB}{2m}\dot r.
}
$$
图 3-3 中两个粒子的共同 $y$ 速度正是第二式积分后的量；下面不能把它丢掉，也不能用同号的相对角速度代替。

![图 3-3　异号电荷的间距变化及共同横向运动。](../figures/center-03.png)

（8）积分质心速度并求异号径向能量。

利用初始 $\dot Y(0)=0$、$r(0)=L$，
$$
\boxed{\dot Y=\frac{qB}{2m}(L-r).}
$$
代入第一式也可得到
$$
\ddot r=\frac{q^2B^2}{m^2}(L-r)-\frac{2Kq^2}{mr^2}.
$$
静电吸引使 $r$ 减小，而共同横向速度所产生的磁力项抵抗这一减小。

两粒子的速度平方相同，为 $\dot r^2/4+\dot Y^2$，所以
$$
T=\frac m4\dot r^2+m\dot Y^2.
$$
静电势能为 $-Kq^2/r$，初始总能量为 $-Kq^2/L$。于是
$$
\boxed{
\frac m4\dot r^2
+\frac{q^2B^2}{4m}(L-r)^2
-\frac{Kq^2}{r}
=-\frac{Kq^2}{L}.
}
$$
径向有效势为
$$
U_{\rm eff}(r)
=\frac{q^2B^2}{4m}(L-r)^2-\frac{Kq^2}{r}.
$$
第一项是被消去的质心动能；它的来源不同于同号的角向动能，系数也不同。

（9）求防碰撞阈值，不遗漏根的可达性。

初始 $\ddot r(0)=-2Kq^2/(mL^2)<0$，故间距先减小。把能量式解出径向速度平方：
$$
\begin{aligned}
\dot r^2
&=\frac{4Kq^2}{m}\left(\frac1r-\frac1L\right)
-\frac{q^2B^2}{m^2}(L-r)^2\\
&=\frac{q^2}{m^2}(L-r)
\left[\frac{4Km}{Lr}-B^2(L-r)\right].
\end{aligned}
$$
在 $0<r<L$ 的非初始转折点，必须满足
$$
B^2r(L-r)=\frac{4Km}{L}.
$$
左端的二次函数在 $r=L/2$ 最大：
$$
r(L-r)=\frac{L^2}{4}-\left(r-\frac L2\right)^2
\leq\frac{L^2}{4}.
$$
因此出现转折根的必要且充分条件为
$$
B^2\frac{L^2}{4}\geq\frac{4Km}{L},
$$
即
$$
\boxed{B\geq B_0=4\sqrt{\frac{Km}{L^3}}.}
$$
图 3-4 按 $r(L-r)$ 的最大值展示阈值。超过阈值有两个候选根，但从 $r=L$ 向内运动首先遇到较大的根。

![图 3-4　异号电荷的转折条件与防碰撞阈值。](../figures/barrier-03.png)

（10）检查阈值等号为何足以“不碰撞”。

当 $B=B_0$，两根重合在 $r=L/2$，径向速度平方化为
$$
\dot r^2
=\frac{q^2B_0^2}{m^2}\frac{L-r}{r}
\left(r-\frac L2\right)^2.
$$
从外侧接近 $L/2$ 时，取向内运动的负根：
$$
\dot r
=-\frac{qB_0}{m}
\sqrt{\frac{L-r}{r}}\left(r-\frac L2\right).
$$
令 $\delta=r-L/2>0$，在 $\delta\to0$ 时，
$$
\dot\delta\simeq-\frac{qB_0}{m}\delta,
\qquad
\delta\propto e^{-qB_0t/m}.
$$
因此达到重根所需时间无限，粒子渐近接近间距 $L/2$，并不继续穿越到零。由于本问只要求“不发生碰撞”，等号满足要求，$B_0$ 确实是可取得的最小磁场。若问“有限时间反射并周期往返”，则必须取 $B>B_0$，两个要求不同。

若 $B<B_0$，括号在整个 $0<r<L$ 内为正，不存在阻止接近的禁区；接近零时 $\dot r^2\sim4Kq^2/(mr)$，碰撞剩余时间的积分 $\int_0^\varepsilon\sqrt r\,dr$ 有限。因此低于阈值确会发生点粒子模型中的碰撞。

（11）求强于阈值时的最近距离。

将转折条件改写为
$$
r^2-Lr+\frac{4Km}{B_1^2L}=0.
$$
使用求根公式：
$$
r_\pm
=\frac L2\left[1\pm
\sqrt{1-\frac{16Km}{B_1^2L^3}}\right]
=\frac L2\left[1\pm\sqrt{1-\frac{B_0^2}{B_1^2}}\right].
$$
$B_1>B_0$ 保证根号为实数且非零。由于初态 $r=L$，首先遇到的转折点是 $r_+$，所以
$$
\boxed{
l_0=r_+
=\frac L2\left(1+\sqrt{1-\frac{B_0^2}{B_1^2}}\right).
}
$$
可达性也可由因式分解检查：
$$
\dot r^2
=\frac{q^2B_1^2}{m^2}\frac{L-r}{r}
(r-r_+)(r-r_-).
$$
在 $r_-<r<r_+$ 内右端为负，该区域不可达。因此较小的 $r_-$ 不是本初态的最近距离；它属于被禁区隔开的另一支可能运动。

图 3-5 的较大根分支位于 $L/2<l_0<L$，从阈值处向 $L$ 逼近。后续数值选根依据这一初态分支，而非仅选较小的正根。

![图 3-5　最近距离的外侧可达分支及强场极限。](../figures/roots-03.png)

<!-- KEEP_STUDENT_START -->
（12）逐项代入阈值和最近距离。

由已计算的 $Km$、$L^3$，
$$
B_0=4\sqrt{\frac{0.176906}{374.805361}}
\simeq0.0869017207\,\mathrm T.
$$
再计算
$$
\left(\frac{B_0}{B_1}\right)^2
=\left(\frac{0.0869017207}{1.58}\right)^2
\simeq3.02581\times10^{-3}.
$$
把它代入较大根，得到
$$
\boxed{l_0\simeq7.20454309\,\mathrm m\approx7.20\,\mathrm m.}
$$
这个值接近初始距离 $7.21\,\mathrm m$，而不是接近零，符合强磁场阻止接近的物理趋势。

（13）量纲、极限及电荷大小检查。

$Km/L^3$ 的量纲为 $\mathrm T^2$，因此 $B_0$ 具有正确磁感应强度量纲。相同电荷大小同时出现在库仑势能和磁耦合项中，消元时共同因子 $q^2$ 消去，所以这些距离和阈值不依赖 $q$；运动时间仍依赖 $q$，不能据此声称完整运动与电荷无关。

当 $B_1\downarrow B_0$，$l_0\to L/2$；当 $B_1\to\infty$，令 $\epsilon=B_0^2/B_1^2\ll1$，用
$$
\sqrt{1-\epsilon}=1-\frac\epsilon2+O(\epsilon^2)
$$
得到
$$
l_0=L\left[1-\frac{B_0^2}{4B_1^2}
+O(B_1^{-4})\right].
$$
同号在 $B\to0$ 时，$\chi\to\infty$，最大距离无限；在很强磁场时 $x\to1^+$。两种趋势分别符合没有磁束缚时的库仑排斥和强磁场约束。

最终结果为同号单调三次方程的唯一 $x>1$ 根、异号最小场 $B_0$ 和异号最近距离的较大根。三者来自两种不同的运动对称性，必须分开推导。

<!-- KEEP_STUDENT_END -->

## 六、关键洞察

异号问题的磁势垒其实是质心动能。粒子被磁场整体侧向带走，侧向动能越大，留给相对径向运动的能量越少；这解释了磁场不做功却能防止碰撞。

同号问题也可用约化质量 $\mu_r=m/2$、相对有效电荷 $q_r=q/2$ 表示：
$$
\mu_r\ddot{\boldsymbol r}
=q_r\dot{\boldsymbol r}\times\boldsymbol B
+\frac{Kq^2}{r^3}\boldsymbol r.
$$
但这个等效电荷仅针对相对运动方程，不能拿它计算原粒子的实际电量。用对称规范 $\boldsymbol A=\boldsymbol B\times\boldsymbol r/2$ 可获得相对角向正则动量，和解析的角向积分一致。

阈值重根是分离轨道。在异号情形 $B=B_0$、$r=L/2$ 时，共同速度为 $\dot Y=qB_0L/(4m)$；对每个粒子，$x$ 向静电吸引与磁力正好平衡。两粒子保持间距并匀速横向运动。阈值轨道从静止初态渐近趋向该运动状态，解释了其无限接近时间。

## 七、易错点

把同号质心固定的结论用到异号；把异号磁力方向画成相反而漏掉电荷变号；用单粒子动能代替两粒子总动能；约化质量差一个二；把最大间距误判为两粒子都瞬时静止；认为普通角动量守恒而漏掉磁场项。

二次方程中最常见错误是选较小正根作为最近距离。根的大小本身不是筛选规则，初态可达支才是。防碰撞阈值等号也不能只靠判别式，须检查是否有限时间越过重根。

## 八、课堂讲解建议

先让学生分别画同号排斥和异号吸引后的初速度与磁力，借此判断质心是否运动。板书两种总动能分解，强调每个被消去的自由度仍贡献能量。

最大距离推导保留初始根的因子，先写“所求根大于L”再约分。最近距离推导同时画两根和禁区，让学生从初始L沿允许区找到第一转折点。

最后用全两粒子运动方程的数值轨迹对照有效势结果，突出独立验证对象是完整模型，而不是把最终公式再代回自身。阈值用指数渐近说明“不碰撞”和“有限时间反射”的差别。

## 九、变式训练

（1）异号情形取 $B_1=2B_0$，求最近距离以及此时质心速度。

解：根号为 $\sqrt{1-1/4}=\sqrt3/2$，故
$$
l_0=\frac L4(2+\sqrt3),\qquad
\dot Y_{\rm turn}
=\frac{qB_1}{2m}(L-l_0)
=\frac{qB_0L}{4m}(2-\sqrt3).
$$
转折时径向速度零，但共同横向速度非零；总动能仍为 $m\dot Y_{\rm turn}^2$，不能置零。

（2）同号情形要求最大间距恰为 $2L$，求磁场。

解：把 $r=2L$ 代入已剔除初始根的方程：
$$
B^2L\cdot L\cdot(3L)^2=16Km(2L).
$$
因此 $9B^2L^4=32KmL$，得到
$$
B=\sqrt{\frac{32Km}{9L^3}}
=\frac{\sqrt2}{3}B_0.
$$
这里 $B_0$ 只是同一组参数构成的磁场尺度，并不把同号题改成异号防碰撞题。代入 $x=2$ 得 $h(2)=9/2$，与 $\chi=16Km/(B^2L^3)=9/2$ 一致。

（3）异号电荷取$B=B_0(1+\epsilon)$，$0<\epsilon\ll1$，求最近间距对磁场变化的敏感性。

解：由$d_{\min}/L=[1+\sqrt{1-(B_0/B)^2}]/2$展开，
$$\frac{d_{\min}}L=\frac12+\sqrt{\frac{\epsilon}2}+O(\epsilon^{3/2}),\qquad
\frac{d d_{\min}}{dB}=\frac{LB_0^2}{2B^3\sqrt{1-B_0^2/B^2}}.$$
导数在临界点右侧发散，故线性误差传播不能跨过$B=B_0$。阈值处双根对应无限时间逼近，不能把$d=L/2$当成有限时刻反弹点；质心运动也没有因此停止。

（4）求强磁场下同号电荷最大间距的增量，以及异号电荷最近间距的减量。

解：同号方程$B^2L(r-L)(r+L)^2=16Km r$，令$r=L+\Delta$，保留最低阶得
$$\Delta=\frac{4Km}{B^2L^2}+O(B^{-4}).$$
异号公式展开得$L-d_{\min}=LB_0^2/(4B^2)+O(B^{-4})$；代入$B_0^2=16Km/L^3$，两者首项相同。这里$K$沿用原问的相互作用常数，不能将其再乘一次电荷平方。展开要求上述增减量远小于$L$。
