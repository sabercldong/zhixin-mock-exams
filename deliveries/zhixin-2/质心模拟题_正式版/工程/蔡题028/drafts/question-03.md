# 第 3 题

两个质量均为 $m$ 的质点由长度为 $l$ 的刚性轻杆连接。初始时下端质点位于 $(0,0)$，上端质点位于 $(0,l)$，杆沿 $y$ 轴。给上端质点一个沿 $+x$ 方向的初速度 $v_0$，下端初速度为零。此后各质点受到线性阻力

$$\boldsymbol f=-k\boldsymbol v,\qquad k>0.$$

求初始上端质点停下时的位置 $(x_1,y_1)$。运动仅按题设的平面内线性阻力模型处理。

![图 3-1　两质点、刚性轻杆及初始位置和速度。](../figures/question-03.png)

## 一、题型定位

线性阻尼下刚体的质心运动与转动分离。两个质点的阻力系数与质量相同，使总阻力只依赖质心速度，而阻力矩只依赖角速度。最终位置需要同时积分质心平移与杆的转角。

## 二、知识点

质心定理；内力抵消；关于质心的角动量定理；刚体速度分解；指数衰减的微分方程及无穷时间积分；参数方程；瞬时速度为零与永久静止的区别。

## 三、物理图像

初态既不是纯平移，也不是绕下端的固定轴转动。质心向右运动，杆相对于质心顺时针转动；平动速度与角速度以同一个时间尺度衰减。最终总转角可以很大，甚至超过半周。因此题目中的“上端”是对初始质点的编号，不表示它在整个运动中始终位于另一质点上方。

## 四、解题入口

设两个质点相对于质心的位置为 $\boldsymbol r_1$、$\boldsymbol r_2$，先用 $\boldsymbol r_1+\boldsymbol r_2=0$ 求总阻力，再求关于质心的阻力矩。令 $\phi$ 表示从初始竖直方向顺时针转过的角度。求出 $X_C(t)$ 与 $\phi(t)$ 后，通过几何关系还原上端坐标。

## 五、解析

（1）模型边界及初始速度的相容性。

题设阻力作用在每个质点上，不作用在无质量的轻杆上。平面内没有另给重力或其他外力，因此 $y$ 是平面坐标，而不是必须加入重力加速度的竖直高度。若把该图解释成重力不可忽略的竖直面，质心便不会停在固定位置，需另改模型。

上端、下端的初速度差为 $(v_0,0)$，与初始杆方向垂直，满足刚杆两端距离不变的初始约束，不需要再给下端一个任意补偿速度。

总质量为 $2m$，初始质心位置、速度为

$$\boldsymbol R_C(0)=\left(0,\frac l2\right),\qquad
\boldsymbol V_C(0)=\frac12(v_0,0).$$

关于质心的转动惯量为

$$I_C=m\left(\frac l2\right)^2
+m\left(\frac l2\right)^2=\frac12ml^2.$$

（2）求初始角速度，不能把下端当作固定轴。

图 3-2 中，质心平动速度为 $v_0/2$，转动使初始上端再获得向右的 $v_0/2$，使下端获得向左的 $v_0/2$；二者与质心速度相加，正好恢复上端 $v_0$、下端零的初态。

![图 3-2　质心平移与两端相对质心的转动速度分解。](../figures/velocities-03.png)

设逆时针有符号角速度为 $\Omega$，上端相对质心位置为 $(0,l/2)$。于是

$$\begin{aligned}
\boldsymbol v_1(0)
&=\boldsymbol V_C(0)+\Omega_0\boldsymbol e_z
\times\left(0,\frac l2\right),\\
v_0&=\frac{v_0}{2}-\Omega_0\frac l2,\\
\Omega_0&=-\frac{v_0}{l}.
\end{aligned}$$

顺时针转角速度为 $\dot\phi=-\Omega$，所以 $\dot\phi(0)=v_0/l$。

（3）求质心运动方程。

两个质点的速度相加为 $2\boldsymbol V_C$，故总外力为

$$\begin{aligned}
\boldsymbol f_1+\boldsymbol f_2
&=-k(\boldsymbol v_1+\boldsymbol v_2)\\
&=-2k\boldsymbol V_C.
\end{aligned}$$

杆内力一对一抵消。由质心定理

$$2m\frac{\mathrm d\boldsymbol V_C}{\mathrm dt}
=-2k\boldsymbol V_C.$$

定义阻尼时间

$$\tau=\frac mk.$$

分离变量并利用初值：

$$\begin{aligned}
\frac{\mathrm dV_{Cx}}{V_{Cx}}&=-\frac{\mathrm dt}{\tau},\\
\ln\frac{V_{Cx}(t)}{v_0/2}&=-\frac t\tau,\\
V_{Cx}(t)&=\frac{v_0}{2}e^{-t/\tau},\\
V_{Cy}(t)&=0.
\end{aligned}$$

对速度从 $0$ 到 $t$ 积分：

$$\begin{aligned}
X_C(t)
&=\frac{v_0}{2}\int_0^t e^{-t'/\tau}\,\mathrm dt'\\
&=\frac{v_0\tau}{2}\left(1-e^{-t/\tau}\right),\\
Y_C(t)&=\frac l2.
\end{aligned}$$

这里积分变量 $t'$ 与上限 $t$ 区分，指数积分产生时间因子 $\tau$，不能漏掉它。

（4）求关于质心的阻力矩。

各质点速度分解为

$$\boldsymbol v_i=\boldsymbol V_C+
\Omega\boldsymbol e_z\times\boldsymbol r_i.$$

阻力矩之和为

$$\begin{aligned}
\boldsymbol{\mathcal T}_C
&=\sum_i\boldsymbol r_i\times(-k\boldsymbol v_i)\\
&=-k\left(\sum_i\boldsymbol r_i\right)\times\boldsymbol V_C
-k\sum_i\boldsymbol r_i\times
(\Omega\boldsymbol e_z\times\boldsymbol r_i).
\end{aligned}$$

第一项因 $\sum_i\boldsymbol r_i=0$ 而消失。平面运动中第二项的 $z$ 分量为 $-k\Omega\sum_i r_i^2$，因此

$$\mathcal T_{Cz}=-k\Omega\frac{l^2}{2}.$$

杆内力沿杆方向，对质心无力矩。于是

$$\begin{aligned}
\frac12ml^2\dot\Omega&=-\frac12kl^2\Omega,\\
\dot\Omega&=-\frac{k}{m}\Omega,\\
\Omega(t)&=-\frac{v_0}{l}e^{-t/\tau}.
\end{aligned}$$

转动与质心平动具有相同的衰减因子，原因是两个质点均满足相同的阻力系数与质量之比 $k/m$。

（5）积分得到杆的转角。

定义无量纲总转角参数

$$\Phi=\frac{v_0\tau}{l}=\frac{mv_0}{kl}.$$

因 $\phi(0)=0$，

$$\begin{aligned}
\phi(t)
&=\int_0^t(-\Omega(t'))\,\mathrm dt'\\
&=\frac{v_0\tau}{l}\left(1-e^{-t/\tau}\right)\\
&=\Phi\left(1-e^{-t/\tau}\right).
\end{aligned}$$

角度按弧度计，$\Phi$ 是纯数。角速度最终趋于零，累积转角则趋于 $\Phi$。

（6）由几何关系恢复质点坐标。

图 3-3 中，上端相对于质心的向量从初始 $+y$ 方向顺时针转过 $\phi$，因此横分量为正的 $(l/2)\sin\phi$，纵分量为 $(l/2)\cos\phi$。

![图 3-3　顺时针转角、质心坐标及两端位置关系。](../figures/rotation-03.png)

完整位置函数为

$$\begin{aligned}
x_1(t)
&=\frac{v_0\tau}{2}(1-e^{-t/\tau})
+\frac l2\sin\!\left[\Phi(1-e^{-t/\tau})\right],\\
y_1(t)
&=\frac l2+\frac l2\cos\!\left[\Phi(1-e^{-t/\tau})\right].
\end{aligned}$$

下端坐标只需把相对质心的两个分量取反：

$$x_2=X_C-\frac l2\sin\phi,\qquad
y_2=\frac l2-\frac l2\cos\phi.$$

两端位置差始终满足

$$(x_1-x_2)^2+(y_1-y_2)^2
=l^2(\sin^2\phi+\cos^2\phi)=l^2,$$

这是一项直接的刚杆约束检查。

（7）最终静止位置是无穷时间极限。

若“停下”指系统耗散后的最终状态，则取 $t\to\infty$，指数因子趋于零。于是

$$\boxed{\begin{aligned}
x_{1,\infty}
&=\frac{mv_0}{2k}
+\frac l2\sin\left(\frac{mv_0}{kl}\right),\\
y_{1,\infty}
&=\frac l2\left[1+\cos\left(\frac{mv_0}{kl}\right)\right].
\end{aligned}}$$

线性阻力使速度指数衰减，除特殊的单个质点瞬时零速外，整个系统在任意有限时间仍有非零质心速度。这里的“最终静止”严格说是渐近极限，不是某个有限截止时刻。

（8）单独核查上端的有限时间瞬时停顿。

直接对位置函数求导，利用 $l\dot\phi=v_0e^{-t/\tau}$，有

$$\begin{aligned}
v_{1x}
&=\frac{v_0}{2}e^{-t/\tau}(1+\cos\phi),\\
v_{1y}
&=-\frac{v_0}{2}e^{-t/\tau}\sin\phi,\\
|\boldsymbol v_1|
&=v_0e^{-t/\tau}\left|\cos\frac\phi2\right|.
\end{aligned}$$

在有限时间内 $e^{-t/\tau}>0$，因此上端瞬时速度为零的条件不是阻尼指数消失，而是

$$\phi=(2n+1)\pi,\qquad n=0,1,2,\ldots$$

并要求 $(2n+1)\pi<\Phi$，该角度才能在有限时间达到。

若 $\Phi>\pi$，第一次瞬时停顿发生在

$$\begin{aligned}
\Phi(1-e^{-t_*/\tau})&=\pi,\\
e^{-t_*/\tau}&=1-\frac{\pi}{\Phi},\\
t_*&=-\tau\ln\left(1-\frac{\pi}{\Phi}\right).
\end{aligned}$$

此时 $X_C=l\pi/2$、$\sin\pi=0$、$\cos\pi=-1$，所以

$$\boxed{(x_1,y_1)_{\text{首次瞬时零速}}
=\left(\frac{\pi l}{2},0\right)}.$$

若 $0<\Phi<\pi$，不存在有限时间的上端零速点；若 $\Phi=\pi$，第一次零速仅在最终极限达到。一般的第 $n$ 个瞬时零速点为 $((2n+1)\pi l/2,0)$，只保留满足角度范围的整数 $n$。

（9）为什么瞬时零速不等于停在那里。

利用 $\dot\phi>0$ 及 $\ddot\phi=-\dot\phi/\tau$，在 $\phi=\pi$ 时，对 $v_{1y}=-(l/2)\dot\phi\sin\phi$ 求导：

$$\begin{aligned}
a_{1y}
&=-\frac l2\left(\ddot\phi\sin\phi
+\dot\phi^2\cos\phi\right)\\
&=\frac l2\dot\phi^2>0.
\end{aligned}$$

上端虽瞬时速度为零，但此时杆仍转动，下端仍运动，杆内力使上端立即向上加速。因此该位置不应代替最终静止坐标。题目若专门问“第一次速度为零”，才使用上一小步的分段答案。

（10）消去时间，检查整个轨迹。

由于 $X_C=l\phi/2$，上端轨迹可写成

$$\boxed{x_1=\frac l2(\phi+\sin\phi),\qquad
y_1=\frac l2(1+\cos\phi),\quad0\leq\phi<\Phi.}$$

图 3-4 中，轨迹在 $\phi=\pi$ 处有尖点；若总转角未超过 $\pi$，实际运动只截取尖点之前的一段。阻尼参数只决定走到哪里和走得多快，不改变这条参数曲线的形状。

![图 3-4　上端轨迹及瞬时零速尖点，示意总转角大于半周。](../figures/path-03.png)

<!-- KEEP_STUDENT_START -->

（11）能量衰减与小参数检查。

初始平动、转动动能分别为

$$K_{C0}=\frac12(2m)\left(\frac{v_0}{2}\right)^2
=\frac14mv_0^2,\qquad
K_{\Omega0}=\frac12I_C\left(\frac{v_0}{l}\right)^2
=\frac14mv_0^2.$$

所以总动能为

$$K(t)=\frac12mv_0^2e^{-2t/\tau}.$$

阻力功率为 $-k(v_1^2+v_2^2)$。由速度分解，$v_1^2+v_2^2=v_0^2e^{-2t/\tau}$，于是

$$\frac{\mathrm dK}{\mathrm dt}
=-kv_0^2e^{-2t/\tau},$$

与上式求导完全一致。

当 $\Phi\ll1$，利用 $\sin\Phi=\Phi-\Phi^3/6+\cdots$、$\cos\Phi=1-\Phi^2/2+\cdots$，

$$\begin{aligned}
x_{1,\infty}
&=l\Phi-\frac{l\Phi^3}{12}+O(l\Phi^5),\\
y_{1,\infty}
&=l-\frac{l\Phi^2}{4}+O(l\Phi^4).
\end{aligned}$$

上端主要沿初速方向移动，纵向变化为二阶小量，符合初态。$v_0=0$ 时恢复 $(0,l)$。当 $k\to0^+$，终态距离一般不收敛；无阻力系统本来就不会最终停下，不能把此极限误当有限停止位置。

<!-- KEEP_STUDENT_END -->

<!-- KEEP_STUDENT_START -->

（12）求杆内力，核对瞬时零速时的加速度来源。

设 $\boldsymbol e=(\sin\phi,\cos\phi)$ 指向质心到初始上端的方向，杆的拉力大小为 $T_{\rm rod}$。两端受力方程为

$$m\dot{\boldsymbol v}_1=-k\boldsymbol v_1-T_{\rm rod}\boldsymbol e,\qquad
m\dot{\boldsymbol v}_2=-k\boldsymbol v_2+T_{\rm rod}\boldsymbol e.$$

杆长固定使相对速度垂直于 $\boldsymbol e$。两端相对位置为 $l\boldsymbol e$，对其长度平方求两次时间导数：

$$\begin{aligned}
(\boldsymbol v_1-\boldsymbol v_2)^2
+l\boldsymbol e\cdot(\dot{\boldsymbol v}_1-\dot{\boldsymbol v}_2)&=0,\\
|\boldsymbol v_1-\boldsymbol v_2|^2
-\frac{2l}{m}T_{\rm rod}&=0,\\
T_{\rm rod}&=\frac{m}{2l}|\boldsymbol v_1-\boldsymbol v_2|^2
=\frac{ml}{2}\dot\phi^2.
\end{aligned}$$

相减的阻力项在杆方向投影为零，不是阻力本身消失。当 $\phi=\pi$ 时，上端位于质心下方，杆拉力向上；其速度为零，阻力也为零，所以 $a_{1y}=T_{\rm rod}/m=l\dot\phi^2/2>0$，正好恢复前面的运动学求导结果。拉力随 $e^{-2t/\tau}$ 衰减，只有在终态极限才趋于零。这条逐质点受力路线与质心—转动路线相互独立。

<!-- KEEP_STUDENT_END -->

## 六、关键洞察

等质量、等阻力系数使质心平移与绕质心转动以同一指数衰减，因此 $X_C/\phi=l/2$ 恒定。上端轨迹对应半径 $l/2$ 的摆线形式，但轻杆并未真的在地面上滚动；这是一种运动学等效，不能据此添加地面支持力。

最终位置与第一次瞬时零速位置属于两个不同问题。对 $\Phi>\pi$，首次零速位置与 $v_0$、$k$ 都无关，而最终位置仍依赖这些参数。这个差异可用于检查是否把“停止”含混地理解成一种状态。

## 七、易错点

把下端看成固定轴，会错误地让质心沿圆周运动。仅积分上端所受阻力、忽略杆内力，会错误地得到直线运动。杆内力对整体合力和质心力矩抵消，不代表它对单个质点没有作用。

转角从 $+y$ 顺时针计时，坐标应为 $(\sin\phi,\cos\phi)$，不是未经说明的 $(\cos\phi,\sin\phi)$。指数阻尼的系统没有普通的有限“整体停下时刻”；当上端速度瞬时为零时，还需检查角速度与加速度。

## 八、课堂讲解建议

先让学生把初始两端速度分解成质心速度与相对转动速度，确认下端静止只是平移、转动相消。板书分别求合力和合力矩，解释为什么平移项在力矩中消失、杆内力也不产生质心力矩。

在得到最终坐标后，继续求上端速度，比较终态和轨迹尖点的条件。课堂可选 $\Phi=\pi/2$、$\Phi=\pi$、$\Phi=3\pi/2$ 三种参数，让学生从图中判断哪些情况有有限时间瞬时零速，而不是给所有参数套同一个“第一次停下”的答案。

<!-- KEEP_TOGETHER_START -->

## 九、变式训练

变式一：初始上端速度仍为 $v_0$，下端改为沿 $+x$ 的速度 $u_0$。求最终上端坐标。阻力与其余条件不变。

解：初始质心速度为 $(v_0+u_0)/2$，顺时针角速度为 $(v_0-u_0)/l$。两个阻尼方程仍具有相同时间常数 $\tau=m/k$。因此

$$X_{C,\infty}=\frac{\tau(v_0+u_0)}2,\qquad
\phi_\infty=\frac{\tau(v_0-u_0)}l.$$

代入几何关系：

$$\boxed{\begin{aligned}
x_{1,\infty}
&=\frac{\tau(v_0+u_0)}2
+\frac l2\sin\left[\frac{\tau(v_0-u_0)}l\right],\\
y_{1,\infty}
&=\frac l2\left\{1+\cos\left[\frac{\tau(v_0-u_0)}l\right]\right\}.
\end{aligned}}$$

若 $u_0=v_0$，杆只平移，结果为 $(\tau v_0,l)$；若 $u_0=-v_0$，质心不动，杆只转动。两种极限分别检验平移项和转角项。一般瞬时零速不再必然出现摆线尖点，因为此时 $X_C/\phi$ 不一定为 $l/2$。

<!-- KEEP_TOGETHER_END -->

变式二：令总累积顺时针转角$\Phi=7\pi/2$，求初始上端质点在有限时间内零速的次数、时刻及坐标。

解：上端零速要求$\phi=(2j+1)\pi<\Phi$。只有$\pi,3\pi$两次。由$\phi=\Phi(1-e^{-t/\tau})$，时刻分别为$\tau\ln(7/5)$和$\tau\ln7$；坐标分别为$(\pi l/2,0)$、$(3\pi l/2,0)$。杆的角速度此时仍非零，所以这是轨迹尖点处的瞬时零速，之后质点重新运动。

变式三：求系统机械能随时间的变化，并求损失初始机械能75%时的质心位移和转角。

解：平动与角速度均乘$e^{-t/\tau}$，惯量不变，故$K(t)=K(0)e^{-2t/\tau}$，初值$K(0)=mv_0^2/2$。剩余25%时$e^{-t/\tau}=1/2$、$t=\tau\ln2$。此时质心右移$v_0\tau/4$，杆转角为$\Phi/2$。耗散功率为$k(|\boldsymbol v_1|^2+|\boldsymbol v_2|^2)=2K/\tau$，与能量导数相符。

变式四：若测得最终杆方向与初始相同，能否唯一反推出阻力系数$k$？已知$m,v_0,l$，只观察杆方向而不测位移。

解：同向要求$\Phi=2\pi n$，$n$为正整数，因此$k=mv_0/(2\pi nl)$有无穷多个候选。方向只确定转角模$2\pi$，不能确定整周数。若再测最终质心位移$X_{C\infty}=mv_0/(2k)=\pi nl$，即可确定$n$并恢复$k$；完整上端坐标的横向位移也给出同一信息。
