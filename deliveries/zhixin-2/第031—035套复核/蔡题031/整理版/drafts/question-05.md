# 第 5 题

一个固定的绝缘光滑细环，半径为$r$。环上有一个质量$m$、电荷量$q$的粒子，初始以速率$v_0$沿图示方向作圆周运动。初始磁场均匀，大小为$B_0$，垂直环面向内，不考虑重力。

（1）磁场缓慢增加到$2B_0$，求粒子的速度。

（2）磁场保持不变，缓慢将细环绕$x$轴转动半圈，求外力所做的功$W$。

两问分别从同一初始状态出发，不把第一问改变磁场后的状态作为第二问的初态。

![图 5-1　初始环面、入纸面磁场与粒子的顺时针初速度。](../figures/question-05.png){width=60%}

## 一、题型定位

这是两个不同机制控制环上带电粒子运动的问题。固定环中改变磁场，会产生感生电场并直接改变粒子动能；固定磁场中转动环，没有实验室中的感生电场，动能变化来自运动约束及外力做功。

两种过程都与穿过环的磁通量变化有关，但不能因此把它们的瞬时受力当作完全相同。固定环的感生切向电场沿周向均匀；转动环的运动电磁作用在不同周向位置并不均匀，需要使用题设慢转条件进行绕环平均。

取$q$为带符号电荷，按图中的顺时针切向规定正速度。首先给出有符号速度，再说明速率应取绝对值。第二问的慢转结果要求粒子绕环运动相对于转环足够快且过程中没有破坏快慢分离；正电荷$q>0$按图运动时满足速度不降至零的条件。

## 二、知识点

- 固定回路的感生电动势为$\oint\boldsymbol E\cdot d\boldsymbol l=-d\Phi_B/dt$。
- 均匀轴向磁场变化时，环上切向感生电场大小与$r\,dB/dt$成正比。
- 洛伦兹磁力$\boldsymbol F_B=q\boldsymbol v\times\boldsymbol B$始终垂直真实速度，不对粒子做功。
- 静止光滑环的约束力不做功，运动光滑环的约束力却可能做功。
- 穿过随环转动的有向面积的磁通量含$\cos\lambda$，半圈后通量符号反转。
- 慢转平均使用$\langle\sin^2\vartheta\rangle=1/2$；这不是说任意瞬间的$\sin^2\vartheta$都等于$1/2$。
- 初末环停止转动时，粒子全部动能由沿环运动速度决定，外力功可用动能变化求得。

## 三、物理图像

初始环在$x$—$y$平面内，$\boldsymbol B=-B_0\boldsymbol e_z$。粒子位于圆周上方时，初速度指向$+x$，故其运动为顺时针。用$w$表示沿这个方向的有符号切向速度，初始$w=v_0>0$。

第一问中环不动，磁场大小$B(t)$增加；顺时针回路的法向为$-z$，所以磁通量为$+\pi r^2B(t)$。磁通增加产生反顺时针的电场，对正电荷沿初运动方向的速度起减小作用。

第二问中磁场不变，环绕固定$x$轴转过$\lambda$，从$0$到$\pi$。原来与磁场同向的环面法向转到反向，磁通量由$+\pi r^2B_0$变为$-\pi r^2B_0$。最终环的几何平面又与初始平面相同，但随环定义的法向及沿环正方向已经翻转。

## 四、解题入口

第一问直接沿固定圆周用法拉第定律：

$$
2\pi rE_\parallel=-\pi r^2\frac{dB}{dt},
\qquad
m\frac{dw}{dt}=qE_\parallel.
$$

第二问先表示缓慢转动时的通量

$$
\Phi_B(\lambda)=\pi r^2B_0\cos\lambda,
$$

再由平均切向运动电磁作用求$w(\lambda)$。求出半圈后的有符号速度后，用静态磁场不做功和初末转动停止条件计算

$$
W=\frac12mw_{\mathrm f}^2-\frac12mv_0^2.
$$

## 五、解析

（1）第一问：固定环的切向感生电场。

选择沿初运动方向，即顺时针的回路积分方向，其右手法向为$-z$。磁场实际方向也为$-z$，故

$$
\Phi_B=\int\boldsymbol B\cdot d\boldsymbol S
=\pi r^2B(t).
\tag{1}
$$

由于磁场均匀并轴对称，环上切向电场在各点的带符号分量相同：

$$
\begin{aligned}
\oint\boldsymbol E\cdot d\boldsymbol l
&=2\pi rE_\parallel\\
&=-\frac{d\Phi_B}{dt}\\
&=-\pi r^2\frac{dB}{dt}.
\end{aligned}
$$

约去$\pi r$，得到

$$
\boxed{
E_\parallel=-\frac r2\frac{dB}{dt}
}.
\tag{2}
$$

如图5-2，$dB/dt>0$时，电场沿逆时针，与顺时针正方向相反。图上的半径$r$对应式（2）的系数，不是粒子速度或其他长度。

![图 5-2　固定环中磁场增强所产生的逆时针切向感生电场。](../figures/faraday-05.png){width=55%}

（2）对切向运动积分，不把磁力当作加速力。

粒子的磁力沿径向；静止环的约束力也仅用于维持圆周运动，没有切向分量。改变切向速度的是电场力，因此

$$
m\frac{dw}{dt}=qE_\parallel
=-\frac{qr}{2}\frac{dB}{dt}.
\tag{3}
$$

将$dt$消去，直接积分磁场变化：

$$
\begin{aligned}
dw&=-\frac{qr}{2m}\,dB,\\
\int_{v_0}^{w_{\mathrm f}}dw
&=-\frac{qr}{2m}\int_{B_0}^{2B_0}dB,\\
w_{\mathrm f}-v_0
&=-\frac{qr}{2m}(2B_0-B_0).
\end{aligned}
$$

故第一问的有符号切向速度为

$$
\boxed{
w_{\mathrm f}^{(1)}
=v_0-\frac{qrB_0}{2m}
}.
\tag{4}
$$

对于正电荷，若$v_0>qrB_0/(2m)$，仍沿原顺时针方向运动，速率就是式（4）的正值；若两者相等，末速为零；若$v_0<qrB_0/(2m)$，最终已经反向，速率应写为

$$
\boxed{
v_{\mathrm{speed}}^{(1)}
=\left|v_0-\frac{qrB_0}{2m}\right|
}.
\tag{5}
$$

负的$w_{\mathrm f}^{(1)}$不是负速率，而是逆时针速度。固定环的感生电场方程在停止和反向时仍成立，不需要为第一问附加“不许速度过零”的假设。

“缓慢”使场变化可以视作准静态感应，不改变从$B_0$到$2B_0$所产生的总切向冲量。只要忽略辐射和其他耗散，式（4）不依赖$B(t)$增加的具体快慢函数。

（3）核对第一问的动能来源和符号。

静止光滑环的约束力与瞬时速度垂直，不做功；磁力也不做功。电场的瞬时功率为

$$
P_E=qE_\parallel w=mw\frac{dw}{dt}
=\frac{d}{dt}\left(\frac12mw^2\right).
$$

因此电场的总功为

$$
\begin{aligned}
W_E
&=\frac12m\left(v_0-\frac{qrB_0}{2m}\right)^2
-\frac12mv_0^2\\
&=-\frac12qrB_0v_0
+\frac{q^2r^2B_0^2}{8m}.
\end{aligned}
\tag{6}
$$

对正电荷，如果最终未反向且速度减小，$W_E<0$。若场增强很大，粒子反向后又被加速，最终动能可能大于初始动能。不能从“初始电场阻碍原运动”推出整个过程的电场总功一定为负。

这个功由改变磁场的外部场源交换，不是静止细环的支撑者做的机械功，也不是洛伦兹磁力的功。

（4）第二问：建立旋转环的空间坐标。

第二问重新从原始$B_0,v_0$开始。设环绕$x$轴缓慢转动角为$\lambda$，环内固定基矢为

$$
\boldsymbol e_1=(1,0,0),\qquad
\boldsymbol e_2=(0,\cos\lambda,\sin\lambda).
\tag{7}
$$

用$\vartheta$表示相对于这组基矢的逆时针周向角，粒子位置为

$$
\boldsymbol r
=r(\cos\vartheta\,\boldsymbol e_1
+\sin\vartheta\,\boldsymbol e_2).
\tag{8}
$$

其周向切向单位矢量为

$$
\boldsymbol e_\vartheta
=(-\sin\vartheta,\cos\vartheta\cos\lambda,
\cos\vartheta\sin\lambda).
$$

顺时针有符号速度仍定义为

$$
w=-r\dot\vartheta.
\tag{9}
$$

图5-3显示环面实际进入空间，而不把半圈转动画成平面内绕中心转动。$x$轴始终固定；法向投影随$\cos\lambda$变化。

![图 5-3　绕固定$x$轴转动时的空间环面、粒子位置与磁场方向。](../figures/rotation-05.png){width=72%}

（5）分开沿环速度和环本身运动速度。

令$\Omega=\dot\lambda$。由于环转动，同一环上材料点的运动速度为

$$
\boldsymbol v_c
=r\Omega(0,-\sin\vartheta\sin\lambda,
\sin\vartheta\cos\lambda).
\tag{10}
$$

粒子的实验室总速度为

$$
\boldsymbol v=r\dot\vartheta\,\boldsymbol e_\vartheta
+\boldsymbol v_c.
\tag{11}
$$

沿环运动的速度部分与$\boldsymbol B$的叉乘不产生沿环切向的磁力；它对应维持圆周方向的作用。转环速度部分则给出

$$
\begin{aligned}
\boldsymbol v_c\times\boldsymbol B
&=rB_0\Omega\sin\vartheta\sin\lambda\,
\boldsymbol e_x,\\
(\boldsymbol v_c\times\boldsymbol B)
\cdot\boldsymbol e_\vartheta
&=-rB_0\Omega\sin^2\vartheta\sin\lambda.
\end{aligned}
\tag{12}
$$

第一式使用$\boldsymbol B=-B_0\boldsymbol e_z$；第二式使用$\boldsymbol e_x\cdot\boldsymbol e_\vartheta=-\sin\vartheta$。两个正弦相乘产生$\sin^2\vartheta$，说明不同周向位置的切向磁作用确实不同。

（6）在慢转条件下平均，再积分到半圈。

完整切向加速度还含转环造成的几何惯性项。按式（8）求两次时间导数，投影到$\boldsymbol e_\vartheta$可得

$$
\ddot\vartheta
=\Omega^2\sin\vartheta\cos\vartheta
-\frac{qB_0}{m}\Omega\sin\lambda\sin^2\vartheta.
\tag{13}
$$

第一项是二阶小量$O(\Omega^2)$；第二项是一阶慢转项$O(\Omega)$。粒子绕环周期远短于转环时间时，在$\lambda$近似不变的一圈内作平均：

$$
\left\langle\sin^2\vartheta\right\rangle=\frac12,
\qquad
\left\langle\sin\vartheta\cos\vartheta\right\rangle=0.
$$

结合$w=-r\dot\vartheta$，主阶慢转方程为

$$
\begin{aligned}
\frac{dw}{dt}
&=\frac{qrB_0}{2m}\Omega\sin\lambda,\\
dw&=\frac{qrB_0}{2m}\sin\lambda\,d\lambda.
\end{aligned}
\tag{14}
$$

从$\lambda=0,w=v_0$积分：

$$
\begin{aligned}
w(\lambda)-v_0
&=\frac{qrB_0}{2m}\int_0^\lambda\sin u\,du\\
&=\frac{qrB_0}{2m}[-\cos u]_0^\lambda\\
&=\frac{qrB_0}{2m}(1-\cos\lambda).
\end{aligned}
\tag{15}
$$

故半圈后

$$
\boxed{
w_{\mathrm f}^{(2)}
=v_0+\frac{qrB_0}{m}
}.
\tag{16}
$$

这是与随环方向一起定义的有符号切向速度。对于图示正电荷，它在慢转全过程中增加，不会中途降到零，快慢分离条件可通过足够小的$\Omega$实现。

（7）从移动回路磁通变化复核平均速度增量。

选择随环的顺时针法向，磁通量为

$$
\Phi_B(\lambda)=\pi r^2B_0\cos\lambda.
\tag{17}
$$

移动回路的运动电动势满足

$$
\begin{aligned}
\oint(\boldsymbol v_c\times\boldsymbol B)
\cdot d\boldsymbol l
&=-\frac{d\Phi_B}{dt}\\
&=\pi r^2B_0\sin\lambda\,\Omega.
\end{aligned}
$$

除以周长得到沿顺时针方向的周向平均运动电磁分量：

$$
\overline E_{\mathrm{mot},\parallel}
=\frac{rB_0}{2}\sin\lambda\,\Omega.
\tag{18}
$$

快绕环粒子在一圈中采样这个平均值，于是$m\,dw/dt=q\overline E_{\mathrm{mot},\parallel}$，恢复式（14）。

图5-4同时画出通量投影$B_0\cos\lambda$和平均速度变化。通量从$B_0$变为$-B_0$，故总变化为$-2B_0$，速度增量是$qrB_0/m$，不是第一问的$-qrB_0/(2m)$。

![图 5-4　慢转半圈的法向磁场投影与正电荷平均切向速度增量。](../figures/flux-05.png){width=76%}

固定磁场意味着实验室$\boldsymbol E=0$。式（18）是随动回路的平均运动电磁作用，不可把它称为实验室中凭空产生的均匀感生电场。这一区分解释了为何最终速度可以用通量算，却仍要用机械外力分析能量来源。

（8）计算外力功，说明运动约束为什么能做功。

光滑环意味着约束力$\boldsymbol N$沿环切向分量为零，即$\boldsymbol N\cdot\boldsymbol e_\vartheta=0$。然而粒子总速度还含$\boldsymbol v_c$，所以

$$
\boldsymbol N\cdot\boldsymbol v
=\boldsymbol N\cdot\boldsymbol v_c
$$

一般不为零。环虽光滑，转动环的外力可以通过运动约束向粒子传递机械能。

磁力功率$(q\boldsymbol v\times\boldsymbol B)\cdot\boldsymbol v=0$，所以粒子动能变化来自约束力功。取缓慢转动且初末环停止转动，环自身初末转动动能相同；外力的净功就是粒子动能的变化。

代入式（16）：

$$
\begin{aligned}
W
&=\frac12m\left(v_0+\frac{qrB_0}{m}\right)^2
-\frac12mv_0^2\\
&=\frac12m
\left(v_0^2+\frac{2qrB_0v_0}{m}
+\frac{q^2r^2B_0^2}{m^2}-v_0^2\right)\\
&=\boxed{
qrB_0v_0+\frac{q^2r^2B_0^2}{2m}
}.
\end{aligned}
\tag{19}
$$

正电荷图示情况$W>0$，转环外力输入能量。这个正功不违反“磁力不做功”；磁场改变了约束反力与速度的关系，机械能仍由外力提供。

（9）检查量纲与两个过程的区别。

量$qBr/m$具有速度量纲：

$$
\left[\frac{qBr}{m}\right]
=\frac{\mathrm C\cdot
(\mathrm{kg\,C^{-1}\,s^{-1}})\cdot\mathrm m}
{\mathrm{kg}}
=\mathrm{m\,s^{-1}}.
$$

式（19）两项均为能量。取$q=0$或$B_0=0$，两个速度改变量和慢转净功均为零，符合无电磁耦合的极限。

第一问改变的是静止环中的真实磁场大小，顺时针通量增加$+\pi r^2B_0$；第二问改变的是静态磁场在随环法向上的投影，通量变化$-2\pi r^2B_0$。因此速度改变量既有相反符号，又有两倍大小，这两个因素都必须保留。

如果$q<0$，式（15）会使顺时针有符号速度减小。若$v_0+qrB_0/m>0$，速度不经过零，慢转平均仍可直接使用，外力功可能为负。若过程中绕环运动趋于停止，则“转得缓慢”不再自动保证平均条件，需要求解式（13）并说明转环时程；不能在这种情形下把平均式当作无条件精确公式。

## 六、关键洞察

判断光滑约束是否做功，要检查约束面是否静止，以及约束力是否垂直于实验室中的总速度。运动约束的法向速度分量是能量交换通道。本题的环约束没有沿环摩擦，仍能够通过转环获得净机械功。

第一问可以由角动量形式复核。选择逆时针周向角$\vartheta$，实验室磁场分量为$B_z=-B$。机械角动量为$L_z=mr^2\dot\vartheta=-mrw$，均匀变磁场使

$$
\frac{d}{dt}
\left(L_z+\frac{qr^2B_z}{2}\right)=0.
$$

因此

$$
-mrw-\frac{qr^2B}{2}
=-mrv_0-\frac{qr^2B_0}{2},
$$

立刻得到$w=v_0-qr(B-B_0)/(2m)$。这条守恒量与法拉第积分一致，但机械角动量$L_z$本身并不守恒，因为感生电场提供切向力矩。

慢转半圈不能把粒子的某一瞬间位置直接代入平均$\sin^2\vartheta=1/2$。完整方程（13）显示了位置相关的细小速度振荡。若转环初末角速度为零，且快慢分离充分，独立数值积分会随转环时间增加趋于式（16），而运动约束的功积分与实际动能变化一致。

## 七、易错点

- 把两问接成同一个连续过程，第二问错误使用第一问的末速度。
- 磁通积分方向与速度正方向不一致，导致第一问的减速号写成加速号。
- 漏掉$2\pi r$与$\pi r^2$之比中的$1/2$。
- 把有符号切向速度当作速率，得到“负速率”而不说明反向。
- 认为磁场变化时只有磁力，遗漏实际产生的感生电场。
- 静态磁场转环时虚构实验室感生电场，或声称磁力直接做了正功。
- 因环光滑就令运动约束功为零，忽略环本身的速度。
- 将慢转平均当成任意转动速度下的精确关系，或忽略绕环速度趋零时的适用限制。

## 八、课堂讲解建议

先固定一套回路方向，让学生自己用右手定则确定法向，再写磁通量。教师应要求第一问先算有符号速度，再讨论是否反向；不能只把答案作为速度大小记忆。

第二问先实际画出$x$轴固定、环面向空间翻转的图，问学生“实验室磁场是否改变”。板书将$\boldsymbol v$分成沿环部分和$\boldsymbol v_c$，从而解释为什么运动约束能做功。平均过程保留$\sin^2\vartheta$到最后一步，帮助学生理解题目“缓慢”的真正用途。

最后把两问的通量变化并列写为$+B_0$和$-2B_0$，检查符号与系数；能量上再区分场源电功与转环机械功。教师可让学生指出“磁力不做功”为什么没有推出“动能不变”。

## 九、变式训练

变式一：在静态磁场中，只将环缓慢转动角$\lambda_f$，初末环停止，正电荷按图运动。求最终平均速度、外力功，并检查$\lambda_f=\pi/2$与$\lambda_f=\pi$。

式（15）给出

$$
w_f=v_0+\Delta w,\qquad
\Delta w=\frac{qrB_0}{2m}(1-\cos\lambda_f).
$$

外力功为

$$
\begin{aligned}
W(\lambda_f)
&=\frac12m(v_0+\Delta w)^2-\frac12mv_0^2\\
&=mv_0\Delta w+\frac12m(\Delta w)^2\\
&=\boxed{
\frac{qrB_0v_0}{2}(1-\cos\lambda_f)
+\frac{q^2r^2B_0^2}{8m}(1-\cos\lambda_f)^2
}.
\end{aligned}
$$

四分之一圈时$\cos(\pi/2)=0$：

$$
w_{\pi/2}=v_0+\frac{qrB_0}{2m},\qquad
W_{\pi/2}=\frac12qrB_0v_0+\frac{q^2r^2B_0^2}{8m}.
$$

半圈时$1-\cos\pi=2$，恢复主问题。外力功不是四分之一圈功简单乘二，因为动能对速度是二次函数，第二个四分之一圈是在已经提高的沿环速度基础上继续输入能量。

小角$\lambda_f\ll1$时，使用$1-\cos\lambda_f=\lambda_f^2/2+O(\lambda_f^4)$：

$$
\Delta w=\frac{qrB_0}{4m}\lambda_f^2+O(\lambda_f^4),
\qquad
W=\frac{qrB_0v_0}{4}\lambda_f^2+O(\lambda_f^4).
$$

变化没有一阶项，与初始法向磁通在$\lambda=0$处取极值一致。这个极限检查能排除把通量投影误写成$B_0\sin\lambda$的错误。

进一步将电荷改为$q=-|q|$，求快慢分离可能失效的临界角。此时慢转预测为

$$
w(\lambda)=v_0-\frac{|q|rB_0}{2m}(1-\cos\lambda).
$$

<!-- KEEP_TOGETHER_START -->

若$|q|rB_0/m<v_0$，半圈结束前仍有$w>0$，运动周期保持有限；若$|q|rB_0/m\ge v_0$，平均结果会达到零。令$w(\lambda_c)=0$，逐项移项得

$$
\begin{aligned}
1-\cos\lambda_c&=\frac{2mv_0}{|q|rB_0},\\
\cos\lambda_c&=1-\frac{2mv_0}{|q|rB_0},\\
\lambda_c&=\arccos\!\left(1-\frac{2mv_0}{|q|rB_0}\right).
\end{aligned}
$$

右端反余弦的自变量在$[-1,1]$内，正好要求$0<v_0\le |q|rB_0/m$。例如$mv_0/(|q|rB_0)=0.7$，则$\cos\lambda_c=-0.4$，临界角约为$113.6^\circ$。

接近此角时，沿环绕行周期$T_{\rm fast}=2\pi r/|w|$增大。若环的转动角速度为$\Omega$，一周中环面改变的角度约为

$$
\Delta\lambda_{\rm one\ cycle}
\simeq\Omega T_{\rm fast}
=\frac{2\pi r\Omega}{|w|}.
$$

平均过程要求该量远小于$1$。在$w$趋零处，即使$\Omega$很小，也不能继续默认粒子已经绕过完整一周并完成位置平均。因此$\lambda_c$是平均解的适用边界，不是可直接跨越的精确停转角；要给出跨越后的速度与功，必须补充转环的时间规律并积分完整运动方程。这里所求的临界角和失效条件均已明确，不能仅把半圈平均速度取绝对值来掩盖这个限制。

<!-- KEEP_TOGETHER_END -->

变式二：环固定，磁场按 $B(t)=B_0+\dot B\,t$ 增大，$q>0$。求粒子首次反向的时间，并说明该时刻的动能。顺时针有向速率初值为 $v_0>0$。

解：法拉第定律给切向电场及方程 $m\dot w=-qr\dot B/2$，不需要慢变近似。积分得 $w=v_0-qr\dot B\,t/(2m)$。当 $\dot B>0$ 时，首次零点为

$$
t_*=\frac{2mv_0}{qr\dot B}.
$$

此时粒子瞬时静止，动能为零；随后 $w<0$，沿逆时针运动。磁力始终不做功，动能变化由感生电场的功提供，至 $t_*$ 该功为 $-mv_0^2/2$。

变式三：环固定，磁场先从 $B_0$ 升至 $B_1$，再以任意时间历程回到 $B_0$。求末速度和全过程感生电场净功；允许中途反向。

解：轴对称感生电场使 $m\,dw=-qr\,dB/2$。沿完整历程积分，$\Delta B=0$，所以 $w_f=v_0$。电场功可直接积为

$$
W_E=\int mw\,dw=\frac m2(w_f^2-v_0^2)=0.
$$

中途速度和能量可以降低到零再增加，不能据此把各段功都取正值。此结论用的是固定环与均匀轴向磁场，不能套到缓慢转动环的另一实验。

变式四：环固定，磁场从 $B_0$ 变为 $B_f$ 后，粒子反向且末动能恰为初动能的四倍。求 $B_f-B_0$ 和电场功，取 $q>0$。

解：四倍动能要求 $|w_f|=2v_0$；反向条件选出 $w_f=-2v_0$。由 $w_f=v_0-qr(B_f-B_0)/(2m)$，得到

$$
B_f-B_0=\frac{6mv_0}{qr},\qquad W_E=\frac32mv_0^2.
$$

若忽略有向速度，会误选同向支线 $w_f=2v_0$。所需场增量的量纲为磁感应强度，电场功等于初末动能差。
