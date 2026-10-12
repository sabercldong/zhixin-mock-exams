# 第4题

<!-- question-start -->

如图4-1所示，在螺线圈上方同轴放置一个水平小铁环，铁环初始静止在水平桌面上，桌面不妨碍铁环向上运动。初始开关断开，随后闭合开关进行跳环实验。

![图4-1 水平导电环、竖直螺线圈与开关电源的空间关系。](../figures/statement-04.png){width=45%}

（1）判断下列说法中正确的选项。

A. 忽略小铁环的自感效应，计入其电阻效应，小铁环可能飞起。

B. 使用直流电源，开关闭合一段时间后，小铁环会落下。

C. 改用正弦交流电源，在稳定状态下，忽略小铁环的自感效应、计入其电阻效应，小铁环可能悬浮。

D. 改用正弦交流电源，小铁环可能悬浮；若只使铁环质量变为原来的 $2$ 倍，为保持原悬浮状态，电源电压应变为原来的 $2$ 倍。

（2）设铁环半径为 $r$，质量为 $m$，电阻为 $R$，自感忽略不计。开关闭合、磁场建立后，环附近磁场的径向分量和穿过环面磁场的竖直面积平均分量分别为 $B_r$ 和 $\bar B_z$。分析铁环此后的运动。

**修订说明：** 为确定第（2）问的启动条件，明确直流磁场从零快速按同一比例建立：$B_r(t)=s(t)B_r$，$\bar B_z(t)=s(t)\bar B_z$，其中 $s$ 从 $0$ 增至 $1$。启动时间足够短，启动阶段铁环位置的变化、重力冲量及运动电动势对启动冲量的修正可忽略。建场完成后的运动采用铁环附近径向磁场局部恒定的近似。$B_r$ 为环上径向场分量，$\bar B_z$ 为环面上的空间平均，不是启动过程的时间平均。按图中向上、向外的场取 $B_r>0$、$\bar B_z>0$。

本题讨论给定电阻、自感参数下的感应电流及其安培力。真实铁磁材料的磁化作用、磁场空间分布远离环后的变化，不由这些参数确定；以下结论属于题设的电磁感应模型，不据此判断真实装置的全部材料效应。交流“稳定悬浮”按一个周期内位置变化可忽略的定高稳态判据讨论；第（2）问另行保留环的机械运动。

<!-- question-end -->

## 一、题型定位

这是电磁感应与竖直动力学的耦合问题，关键在于区分“磁场随时间建立”与“导电环在已建立磁场中运动”两种电动势。两种电动势都能产生电流，但不对应同一种运动效果：快速建场提供向上的初始冲量，建场后的运动感应产生与速度相反的电磁阻力。

第（1）问还考查交流相位。交流磁场不断变化，并不自动意味着平均支持力向上；必须把电流与产生安培力的径向磁场相乘，再对一周期求平均。忽略自感时，定高纯电阻环中的电流与磁场相差四分之一周期，平均升力为零。保留自感后可以出现非零平均升力，但电源电压与升力的关系是平方关系，不是一次关系。

第（2）问的主线是“电磁冲量—初速度—线性阻尼微分方程—速度和位置—上升、转向、下降”。建场阶段不能在积分中把尚未建立的径向磁场替换为最终值；这一步若漏掉，初速度以及后续的最大高度都会错误。

## 二、知识点

闭合环路的正向与环面的法向须符合右手定则。取向上为环面正法向，俯视环时逆时针为正电流方向。外磁通为
$$
\Phi_{\mathrm{ext}}=\int_S\boldsymbol B\cdot\mathrm d\boldsymbol S
=\pi r^2\bar B_z.
$$
固定环的变压器电动势为 $\mathcal E_{\text{变}}=-\partial\Phi_{\mathrm{ext}}/\partial t$；运动环还要计入 $\oint(\boldsymbol v\times\boldsymbol B)\cdot\mathrm d\boldsymbol l$。电流是有正负号的代数量，不能把电动势的绝对值直接当作正电流使用。

安培力微元为
$$
\mathrm d\boldsymbol F=I\,\mathrm d\boldsymbol l\times\boldsymbol B.
$$
本题环上导线沿方位角方向，径向磁场产生竖直力；竖直磁场产生环面内的力，其水平合量因轴对称而相消。穿过环面的磁通不等于负责竖直力的径向场，两者分工不同。

当自感可忽略时，$RI=\mathcal E$。保留自感时则为
$$
L\frac{\mathrm dI}{\mathrm dt}+RI=\mathcal E_{\text{外}}.
$$
后一个方程不能在交流部分删掉，却在直流启动部分暗中保留同样的电流延迟；不同近似需要分别说明。

有线性阻力的竖直运动满足 $m\dot v=-mg-\kappa v$。解一阶线性微分方程时，可用积分因子 $e^{t/\tau}$，其中 $\tau=m/\kappa$。随后对有符号速度积分得到位移，令速度为零求转向时刻，而不是令加速度为零。

能量检查必须计入焦耳热：磁场中的带电粒子磁力不做功，不等于外磁场对整个运动导体不会产生机械阻力。导电环的机械能减少量应与电阻发热相对应。

## 三、物理图像

图4-1中的螺线圈竖直，环水平且与线圈同轴。线圈上端附近的磁力线既有向上的分量，也向外弯曲。建场时向上磁通增加，俯视感应电流为顺时针；顺时针电流在向外的径向场中受向上的安培力。因此环可能离开桌面，而不是靠“环和线圈都通电，所以相互排斥”作没有方向依据的判断。

磁场完成建立后，若环向上运动，环中的运动电流改为逆时针，电磁合力向下；若环向下运动，运动电流改为顺时针，电磁合力向上。两种情形都表现为阻碍运动，而不是永久向上托住环。在最高点，瞬时速度为零，自感忽略时电流和电磁力同时为零，环只有重力，立即开始下降。

交流定高环的图像不同。线圈磁场和环中电流都周期变化，瞬时力也可上下变化。能否悬浮要检查周期平均力是否能平衡重力，以及所讨论高度附近是否存在稳定性；没有指定空间场函数时，不能只由一个平均力数值宣称任意高度都稳定。

本题的 $B_r$ 局部恒定并不表示竖直磁通与高度无关。磁场没有源汇，环上径向磁通向外流出，正对应环面竖直磁通随高度减少。把两个分量都当作处处不变，会一方面计算出运动电动势，另一方面又声称磁通不变，形成自相矛盾。

## 四、解题入口

研究对象取整个铁环，先给电流和竖直速度规定一致的正向。用一个环上微元核对叉积方向，积分得到 $F_z=-2\pi rB_rI$。这样电动势、电流与受力的正负号都能从同一套约定推出，不必在每个阶段重猜方向。

启动阶段保持位置不变，用法拉第定律求电流，再把正在建立的径向场乘进去积分。共同的建场函数 $s(t)$ 使积分成为 $\int_0^1s\,\mathrm ds$，从而确定初速度。后续运动以启动结束为新的 $t=0$，另行建立运动电动势，不能把短暂的建场电流延长到整个运动过程。

得到阻尼方程后，依次求速度、位移、最高点及下降趋势，并以机械能与焦耳热核对。选项判断最后回到两种供电方式：直流没有持续的定高感应升力；纯电阻交流的平均升力为零；有限自感交流有相位修正，但同一几何与频率下升力随电压平方变化。

## 五、解析

**第1步：统一时间原点、场的分量和电流正方向。**

向上取 $z$ 正方向，$v=\dot z$ 是有符号的竖直速度；俯视逆时针为 $I>0$。环半径 $r$ 在运动中不变。为了避免一个字母同时表示两种时间，建场阶段暂用 $t_{\mathrm s}$，持续时间记为 $T_{\mathrm s}$；建场完成后的运动时间记为 $t$，并令此时 $z(0)=0$、$v(0)=v_0$。

在图4-2的环上点 $P$，使用柱坐标单位向量 $\boldsymbol e_r,\boldsymbol e_\varphi,\boldsymbol e_z$。这里 $\boldsymbol e_r$ 指远离线圈轴线的水平径向方向，不是沿磁力线方向；$\boldsymbol e_\varphi$ 沿正电流方向，$\boldsymbol e_z$ 向上。三者满足
$$
\boldsymbol e_r\times\boldsymbol e_\varphi=\boldsymbol e_z,
\qquad
\boldsymbol e_\varphi\times\boldsymbol e_r=-\boldsymbol e_z.
$$

![图4-2 环上微元的方位角正向、径向磁场和竖直安培力。](../figures/element-04.png){width=50%}

后面使用的 $B_r$ 是该环上的径向分量；$\bar B_z$ 是整个环面上竖直分量的面积平均。它们不必大小相等，也不能因为同属一个磁场就互相替代。

**第2步：由环上微元求完整的竖直安培力。**

正向导线元为 $\mathrm d\boldsymbol l=r\,\mathrm d\varphi\,\boldsymbol e_\varphi$。局部磁场写为
$$
\boldsymbol B=B_r\boldsymbol e_r+B_z\boldsymbol e_z.
$$
由叉积逐项得到
$$
\begin{aligned}
\mathrm d\boldsymbol F
&=Ir\,\mathrm d\varphi\,
\boldsymbol e_\varphi\times
(B_r\boldsymbol e_r+B_z\boldsymbol e_z)\\
&=-IrB_r\,\mathrm d\varphi\,\boldsymbol e_z
+IrB_z\,\mathrm d\varphi\,\boldsymbol e_r.
\end{aligned}
$$
第二项是水平径向力，对称环的相对两点方向相反，沿周积分的合量为零。第一项始终沿相同的竖直方向，不能与另一侧相消。因此
$$
\begin{aligned}
F_z&=\int_0^{2\pi}(-IrB_r)\,\mathrm d\varphi\\
&=-2\pi rB_rI.
\end{aligned}
$$
若 $B_r>0$，正电流产生向下的力，负电流产生向上的力。这个带符号公式在启动、上升、下降以及交流分析中都保持不变。

**第3步：固定位置建场时，先求有符号的感应电流。**

启动阶段的位置变化可忽略，外磁通为
$$
\Phi_{\mathrm{ext}}(t_{\mathrm s})
=\pi r^2\bar B_z\,s(t_{\mathrm s}).
$$
环面正法向向上，所以磁通增加为正。法拉第定律给出
$$
\begin{aligned}
\mathcal E_{\text{变}}
&=-\frac{\mathrm d\Phi_{\mathrm{ext}}}{\mathrm dt_{\mathrm s}}\\
&=-\pi r^2\bar B_z\,\dot s,\\
I_{\mathrm s}
&=\frac{\mathcal E_{\text{变}}}{R}
=-\frac{\pi r^2\bar B_z}{R}\dot s.
\end{aligned}
$$
在通常单调建场中，$\dot s>0$、$\bar B_z>0$，所以 $I_{\mathrm s}<0$，即顺时针。这与楞次定律相符：顺时针电流产生向下的自磁场，反抗向上外磁通的增加。

楞次定律反抗的是磁通的变化，不是无条件反抗外磁场。后续外场不再随时间建立，但环运动仍使磁通变化，因此不能认定运动阶段没有电流。

**第4步：保留径向场的建立过程，求向上的启动冲量。**

此时径向场也只有最终值的 $s$ 倍。把第3步的电流代入第2步的受力公式，得到
$$
\begin{aligned}
F_{z,\mathrm s}
&=-2\pi r\,[sB_r]
\left(-\frac{\pi r^2\bar B_z}{R}\dot s\right)\\
&=\frac{2\pi^2r^3B_r\bar B_z}{R}s\dot s.
\end{aligned}
$$
安培力的冲量是力对时间积分，不是把最大力乘一个未给出的“瞬间”。具体计算为
$$
\begin{aligned}
J_z
&=\int_0^{T_{\mathrm s}}F_{z,\mathrm s}\,\mathrm dt_{\mathrm s}\\
&=\frac{2\pi^2r^3B_r\bar B_z}{R}
\int_0^{T_{\mathrm s}}s\dot s\,\mathrm dt_{\mathrm s}\\
&=\frac{2\pi^2r^3B_r\bar B_z}{R}
\int_0^1s\,\mathrm ds\\
&=\frac{2\pi^2r^3B_r\bar B_z}{R}
\left[\frac{s^2}{2}\right]_0^1\\
&=\boxed{\frac{\pi^2r^3B_r\bar B_z}{R}}.
\end{aligned}
$$
这里使用变量代换 $\mathrm ds=\dot s\,\mathrm dt_{\mathrm s}$。积分中保留的 $s$ 产生系数 $1/2$。若错把全过程径向场写成最终 $B_r$，便会把 $\int s\,\mathrm ds$ 错换成 $\int\mathrm ds$，冲量多算一倍。

在题设共同建场模型下，正确启动冲量只取决于起终值，而不取决于 $s(t_{\mathrm s})$ 的具体形状；这不意味着任意不同步的两种场都给出同一个冲量。

**第5步：从冲量求初速度，并说明桌面与快速近似。**

铁环初始静止。启动时间足够短时，重力和桌面支持力的非电磁冲量对有限的向上电磁冲量只有高阶修正。离开桌面后，向上动量近似为 $J_z$，所以
$$
\begin{aligned}
mv_0&=J_z,\\
v_0&=\boxed{\frac{\pi^2r^3B_r\bar B_z}{mR}}.
\end{aligned}
$$
此式使用了 $B_r\bar B_z>0$。若装置把磁场整体反向，两个分量一起变号，乘积不变，仍可得到向上冲量；不能只翻转其中一个符号却保持同一幅场线图。

有限时间内，桌面只能推环向上，不能把已向上加速的环拉回桌面。环尚未离桌时 $N+F_{z,\mathrm s}=mg$，要求 $N\ge0$；当 $F_{z,\mathrm s}>mg$ 时，维持接触需要负支持力，接触即失效。只要建场足够快且幅度足够大，就能满足离桌条件，说明选项A说的“可能飞起”成立。并非任意弱电源、任意慢建场都必然跳起。

若保留非零自感，环电流不能按 $I=\mathcal E/R$ 瞬时响应。本题公式是在自感可忽略的理想模型中求快速但有限的启动，不应把它解释成真实电流可以无条件无限大。

**第6步：用磁通守恒建立竖直磁通与高度的关系。**

建场后外场不再显含时间，但环向上运动时环面磁通会改变。图4-3画出半径同为 $r$、高度相差 $\mathrm dz$ 的薄圆柱。圆柱侧面向外流出的磁通近似为 $2\pi rB_r\,\mathrm dz$，上底与下底竖直磁通之差必须与它相反。

![图4-3 薄圆柱侧面径向磁通与上下环面磁通的对应关系。](../figures/flux-04.png){width=45%}

由 $\nabla\cdot\boldsymbol B=0$，闭合面的磁通和为零：
$$
\begin{aligned}
\Phi_{\mathrm{ext}}(z+\mathrm dz)
-\Phi_{\mathrm{ext}}(z)
+2\pi rB_r\,\mathrm dz&=0,\\
\frac{\mathrm d\Phi_{\mathrm{ext}}}{\mathrm dz}
&=-2\pi rB_r,\\
\pi r^2\frac{\mathrm d\bar B_z}{\mathrm dz}
&=-2\pi rB_r,\\
\frac{\mathrm d\bar B_z}{\mathrm dz}
&=-\frac{2B_r}{r}.
\end{aligned}
$$
这正是图中的场线向外散开时，竖直磁通随高度减小的定量表达。即使环上 $B_r$ 在小范围内近似不变，$\bar B_z$ 仍随高度近似线性变化。题设中的 $\bar B_z$ 是启动位置的值，不能直接沿用为任何高度的相同值。

**第7步：求运动电动势，分别用叉积和磁通变化核对。**

环整体以 $\boldsymbol v=v\boldsymbol e_z$ 平移。因为竖直场与速度平行，不产生 $\boldsymbol v\times\boldsymbol B$；径向场给出
$$
\boldsymbol v\times\boldsymbol B
=vB_r\boldsymbol e_\varphi.
$$
沿正向导线积分，得到
$$
\begin{aligned}
\mathcal E_{\text{动}}
&=\oint(\boldsymbol v\times\boldsymbol B)
\cdot\mathrm d\boldsymbol l\\
&=\int_0^{2\pi}vB_rr\,\mathrm d\varphi\\
&=2\pi rB_rv.
\end{aligned}
$$
另一条核对路线使用第6步：
$$
\begin{aligned}
-\frac{\mathrm d\Phi_{\mathrm{ext}}}{\mathrm dt}
&=-\frac{\mathrm d\Phi_{\mathrm{ext}}}{\mathrm dz}\dot z\\
&=-(-2\pi rB_r)v\\
&=2\pi rB_rv.
\end{aligned}
$$
两条路线所得的大小和符号完全一致。$v>0$ 时电动势为正，$v<0$ 时为负；这是后面电磁力始终阻碍运动的直接原因。

**第8步：把运动电流转成有符号的电磁阻力。**

自感忽略时
$$
I_{\text{动}}=\frac{2\pi rB_r}{R}v.
$$
将此电流代入第2步：
$$
\begin{aligned}
F_{z,\text{动}}
&=-2\pi rB_r\left(\frac{2\pi rB_r}{R}v\right)\\
&=-\frac{4\pi^2r^2B_r^2}{R}v.
\end{aligned}
$$
记
$$
\kappa=\frac{4\pi^2r^2B_r^2}{R}>0,
\qquad F_{z,\text{动}}=-\kappa v.
$$
在图4-4的上升状态中，$v>0$，电磁力向下；下降状态中，$v<0$，电磁力向上。公式中的 $B_r^2$ 说明整体反转外磁场不改变阻尼方向。

![图4-4 上升、最高点和下降时速度、电流与电磁力的方向。](../figures/motion-04.png){width=76%}

最高点不是一个稳定停留点：$v=0$ 使运动电流和电磁力都为零，但重力没有消失。不能把上升阶段向下的阻力延长成全程向下，也不能把下降阶段向上的阻力误写成一个恒定支持力。

**第9步：建立竖直动力学方程及时间常数。**

环已离开桌面，支持力为零。向上的合力为重力与电磁阻力之和，故
$$
\begin{aligned}
m\frac{\mathrm dv}{\mathrm dt}&=-mg-\kappa v,\\
\frac{\mathrm dv}{\mathrm dt}+\frac{\kappa}{m}v&=-g.
\end{aligned}
$$
定义
$$
\boxed{\tau=\frac{m}{\kappa}
=\frac{mR}{4\pi^2r^2B_r^2}},
$$
方程化为
$$
\frac{\mathrm dv}{\mathrm dt}+\frac{v}{\tau}=-g,
\qquad v(0)=v_0.
$$
这里 $\tau$ 的量纲是时间。它不是自感回路的电流衰减时间 $L/R$：主解已经忽略 $L$，当前的指数变化来自质量和运动感应形成的机械阻尼。

**第10步：用积分因子逐行求速度。**

两边同乘 $e^{t/\tau}$，左侧成为乘积的导数：
$$
\begin{aligned}
e^{t/\tau}\frac{\mathrm dv}{\mathrm dt}
+\frac1\tau e^{t/\tau}v
&=-g e^{t/\tau},\\
\frac{\mathrm d}{\mathrm dt}\left(e^{t/\tau}v\right)
&=-g e^{t/\tau}.
\end{aligned}
$$
从 $0$ 到 $t$ 积分，并代入初速度：
$$
\begin{aligned}
e^{t/\tau}v(t)-v_0
&=-g\int_0^t e^{t'/\tau}\,\mathrm dt'\\
&=-g\tau\left(e^{t/\tau}-1\right),\\
e^{t/\tau}v(t)
&=v_0+g\tau-g\tau e^{t/\tau},\\
v(t)&=\boxed{(v_0+g\tau)e^{-t/\tau}-g\tau}.
\end{aligned}
$$
数学技巧是线性方程的积分因子法。积分常数不是凭形式猜出的，已用 $v(0)=v_0$ 确定；指数项的正负也可由 $t=0$ 与初始加速度检查。

**第11步：对有符号速度积分，求竖直位移。**

取启动结束时高度为零，$z(0)=0$。位移为
$$
\begin{aligned}
z(t)
&=\int_0^t v(t')\,\mathrm dt'\\
&=(v_0+g\tau)\int_0^t e^{-t'/\tau}\,\mathrm dt'
-g\tau\int_0^t\mathrm dt'\\
&=(v_0+g\tau)\left[-\tau e^{-t'/\tau}\right]_0^t
-g\tau t\\
&=\boxed{\tau(v_0+g\tau)(1-e^{-t/\tau})-g\tau t.}
\end{aligned}
$$
指数积分带有负号，代入上下限后变为 $1-e^{-t/\tau}$。若把 $-g\tau t$ 漏掉，位移会趋于一个正的有限高度，看似永久悬停；但它的导数已经不是第10步的速度。

这里积分的是 $v$，不是速率 $|v|$。上升时位移增加，下降时位移减少；累计路程另需对 $|v|$ 分段积分。

**第12步：从速度零点求最高点时刻，而非从加速度零点求。**

最高点满足 $v(t_*)=0$。逐项移项得
$$
\begin{aligned}
(v_0+g\tau)e^{-t_*/\tau}&=g\tau,\\
e^{-t_*/\tau}&=\frac{g\tau}{v_0+g\tau},\\
-\frac{t_*}{\tau}
&=-\ln\left(1+\frac{v_0}{g\tau}\right),\\
t_*&=\boxed{\tau\ln\left(1+\frac{v_0}{g\tau}\right)}.
\end{aligned}
$$
当 $v_0>0$ 时，括号大于 $1$，所以 $t_*>0$。速度的导数为
$$
\dot v=-\frac{v_0+g\tau}{\tau}e^{-t/\tau}<0,
$$
因此速度严格递减，只经过一次零点；此前上升，此后下降。最高点的加速度代回动力学方程得 $\dot v(t_*)=-g$，并不为零。

**第13步：完整化简最大上升高度。**

把最高点的指数值代入位移式：
$$
\begin{aligned}
z_{\max}
&=\tau(v_0+g\tau)
\left(1-\frac{g\tau}{v_0+g\tau}\right)-g\tau t_*\\
&=\tau\left[(v_0+g\tau)-g\tau\right]-g\tau t_*\\
&=\tau v_0-g\tau^2\ln\left(1+\frac{v_0}{g\tau}\right).
\end{aligned}
$$
所以
$$
\boxed{z_{\max}
=\tau v_0-g\tau^2\ln\left(1+\frac{v_0}{g\tau}\right)}.
$$
为检查它是否为正，令 $\eta=v_0/(g\tau)>0$，则
$$
z_{\max}=g\tau^2\,[\eta-\ln(1+\eta)].
$$
因为 $\ln(1+\eta)<\eta$，该高度为正。此不等式可直接由
$$
\eta-\ln(1+\eta)
=\int_0^\eta\frac{x}{1+x}\,\mathrm dx>0
$$
看出，不需凭图猜最大高度的符号。

**第14步：描述下降、回到初始高度和局部近似的边界。**

对任意 $t>t_*$，速度为负，环下降。若把局部恒定 $B_r$ 的模型形式上延续，则
$$
v(t)\longrightarrow -g\tau
=-\frac{mgR}{4\pi^2r^2B_r^2}.
$$
这是向下的终端速度：此时向上的电磁阻力平衡重力，但环仍在下降。平衡的是合力，不是把位置固定在某处。

回到启动高度时令 $z(t_{\text{回}})=0$。用 $u=t_{\text{回}}/\tau$、$\eta=v_0/(g\tau)$ 写成
$$
(1+\eta)(1-e^{-u})=u.
$$
此方程显然有 $u=0$，但那只是初始时刻。函数
$$
f(u)=(1+\eta)(1-e^{-u})-u
$$
满足 $f(0)=0$、$f'(0)=\eta>0$、$f''(u)=-(1+\eta)e^{-u}<0$，且 $f(u)\to-\infty$。所以在零根之外恰有一个正根，它位于最高点之后。可用数值求根，不把初始零根当作落回时间。

真实线圈的 $B_r$ 不会在任意高度保持不变。以上定量速度、位移和终端速度是给定局部模型的结果，只有整个所用轨迹留在该近似有效区域时才可应用。若环飞出强场区域，应换用实际 $B_r(z)$；不继续用局部常量去预测无限远处的运动。直流纯电阻环在静止时没有持续感应升力，最终落下的物理判断并不要求真实空间处处存在同一个终端速度。

**第15步：以瞬时功率核对阻力符号和焦耳热。**

在运动阶段，电流为 $I=(2\pi rB_r/R)v$。电阻发热功率为
$$
\begin{aligned}
P_{\mathrm J}
&=RI^2\\
&=R\left(\frac{2\pi rB_r}{R}v\right)^2\\
&=\frac{4\pi^2r^2B_r^2}{R}v^2\\
&=\kappa v^2\ge0.
\end{aligned}
$$
电磁力的机械功率为 $F_zv=-\kappa v^2$，故
$$
\begin{aligned}
\frac{\mathrm d}{\mathrm dt}
\left(\frac12mv^2+mgz\right)
&=mv\dot v+mgv\\
&=v(-mg-\kappa v)+mgv\\
&=-\kappa v^2\\
&=-P_{\mathrm J}.
\end{aligned}
$$
符号完全闭合：机械能减少，焦耳热增加。若推导得到 $F_z=+\kappa v$，机械能会凭空增加，而同一电流仍产生正焦耳热；这说明受力或电动势正向写错，不能只改最后一行去掩盖。

**第16步：核对初值、量纲和弱阻尼极限。**

直接代入得到 $v(0)=v_0$、$z(0)=0$。再求初始加速度：
$$
\dot v(0)=-g-\frac{v_0}{\tau},
$$
它比仅受重力时更向下，与刚开始上升即受向下阻力的图像一致。

从量纲看，$2\pi rB_rv$ 是电动势，除以 $R$ 是电流，再乘 $2\pi rB_r$ 是力。因此 $\kappa$ 的量纲是质量除以时间，$\tau=m/\kappa$ 是时间；$\pi^2r^3B_r\bar B_z/R$ 是冲量，除以 $m$ 是速度。用力、冲量、速度逐层检查，比只检查最终指数是否无量纲更容易定位错误。

若仅为检查方程而保持初速度 $v_0$ 固定，让阻尼趋弱、$\tau\to\infty$，展开
$$
e^{-t/\tau}=1-\frac t\tau+\frac{t^2}{2\tau^2}+O(\tau^{-3}).
$$
代回可得
$$
v(t)\to v_0-gt,
\qquad z(t)\to v_0t-\frac12gt^2,
\qquad z_{\max}\to\frac{v_0^2}{2g}.
$$
其中位置式的一次大项相消，必须保留指数展开至二阶才看到正确的重力位移。这是“固定初速度检查”而不是同时改变电阻、仍声称启动初速度不变的真实实验；本题 $v_0$ 本身也含 $R$。

**第17步：判断直流选项A、B。**

启动阶段 $F_{z,\mathrm s}>0$，其冲量可使环获得 $v_0>0$，有限启动只需峰值受力超过重力就可能离开桌面。因此A正确。

建场完成后，铁环的运动电磁力为 $-\kappa v$。环的上升速度持续减小，在有限的 $t_*$ 变为零；最高点无电流支持，随后向下运动。因此在题设的直流感应模型下，B正确。

若考虑有限自感，启动电流能在一段时间内衰减而继续向上作用，但非零电阻会使纯直流定高环中的电流最终消失。这不改变“不能凭直流感应电流永久定高托住环”的结论。该说明不把主解的 $L=0$ 初速度公式用于 $L\ne0$ 的启动过程。

**第18步：纯电阻正弦交流中，逐项计算定高平均力。**

在一个周期内环位置变化可忽略。用 $\widehat B_z$ 与 $\widehat B_r$ 表示交流场分量的峰值，写为
$$
\bar B_z(t)=\widehat B_z\cos\omega t,
\qquad B_r(t)=\widehat B_r\cos\omega t.
$$
两个分量由同一线圈电流产生，具有同一时间因子；不能给径向场和竖直场任意指定互不相关的相位。磁通为 $\pi r^2\widehat B_z\cos\omega t$，所以
$$
\begin{aligned}
\mathcal E(t)&=\omega\pi r^2\widehat B_z\sin\omega t,\\
I(t)&=\frac{\omega\pi r^2\widehat B_z}{R}\sin\omega t,\\
F_z(t)&=-\frac{2\pi^2r^3\widehat B_r\widehat B_z\omega}{R}
\sin\omega t\cos\omega t.
\end{aligned}
$$
设周期 $\mathcal T=2\pi/\omega$，周期平均为
$$
\begin{aligned}
\langle F_z\rangle
&=-\frac{2\pi^2r^3\widehat B_r\widehat B_z\omega}{R\mathcal T}
\int_0^{\mathcal T}\sin\omega t\cos\omega t\,\mathrm dt\\
&=-\frac{2\pi^2r^3\widehat B_r\widehat B_z\omega}{R\mathcal T}
\left[\frac{\sin^2\omega t}{2\omega}\right]_0^{\mathcal T}\\
&=0.
\end{aligned}
$$
环虽然有电流，也有瞬时安培力，但此定高纯电阻模型没有平衡 $mg$ 的平均升力。C错误。此处的零平均结论使用了题面说明的定高周期近似；若要讨论大幅度的受迫位置振动，必须联立含位置的电路与运动方程，不能把本式未经审查推广到任意运动。

**第19步：保留自感，说明交流为何可能产生平均升力。**

令磁通峰值 $A=\pi r^2\widehat B_z$。定高环的电路方程为
$$
L\dot I+RI=\omega A\sin\omega t.
$$
稳定周期解设为 $I=p\cos\omega t+q\sin\omega t$。逐项求导并比较余弦、正弦系数：
$$
\begin{aligned}
RI+L\dot I
&=(Rp+\omega Lq)\cos\omega t
+(Rq-\omega Lp)\sin\omega t,\\
Rp+\omega Lq&=0,\\
Rq-\omega Lp&=\omega A.
\end{aligned}
$$
由第一式 $p=-\omega Lq/R$，代入第二式：
$$
\begin{aligned}
Rq+\frac{\omega^2L^2}{R}q&=\omega A,\\
(R^2+\omega^2L^2)q&=\omega AR,\\
q&=\frac{\omega AR}{R^2+\omega^2L^2},\\
p&=-\frac{\omega^2AL}{R^2+\omega^2L^2}.
\end{aligned}
$$
于是
$$
I(t)=\frac{\omega AR\sin\omega t-\omega^2AL\cos\omega t}
{R^2+\omega^2L^2}.
$$
瞬时力为 $-2\pi r\widehat B_r\cos\omega t\,I(t)$。用 $\langle\sin\omega t\cos\omega t\rangle=0$、$\langle\cos^2\omega t\rangle=1/2$ 得
$$
\begin{aligned}
\langle F_z\rangle
&=-2\pi r\widehat B_r\frac p2\\
&=\boxed{\frac{\pi^2r^3\widehat B_r\widehat B_z\omega^2L}
{R^2+\omega^2L^2}}.
\end{aligned}
$$
在 $\widehat B_r\widehat B_z>0$、$L>0$ 时平均力向上。若其大小能达到重力，并具有适当的高度依赖，就可能出现悬浮。$L\to0$ 时此平均力趋于零，恰好回到第18步，不能一面完全忽略自感一面保留由自感产生的同相电流分量。

**第20步：判断质量改变时的电压比例，完成选项D。**

保持几何、频率、电阻、自感和场的线性响应不变，电源电压幅值 $U$ 增大 $k$ 倍，线圈产生的两个磁场峰值都增大 $k$ 倍。因此
$$
\widehat B_r\mapsto k\widehat B_r,
\qquad\widehat B_z\mapsto k\widehat B_z,
\qquad\langle F_z\rangle\mapsto k^2\langle F_z\rangle.
$$
原平衡要求 $\langle F_z\rangle=mg$。只把质量变为 $2m$，保持原高度的平均受力平衡需要
$$
k^2mg=2mg,
\qquad k=\sqrt2.
$$
电压幅值应变为原来的 $\sqrt2$ 倍，而非 $2$ 倍；若变为 $2$ 倍，平均升力会变成 $4$ 倍。因此D的整体叙述错误。若通过改变环材料或尺寸来增加质量，$R,L$ 也可能变化，电压比例需重新计算，不能仅凭“质量翻倍”断言某个普适比例。

第（1）问最终选择为
$$
\boxed{\mathrm{A},\mathrm{B}}.
$$

**第21步：整理运动答案，分开启动量、机械时间和有效范围。**

在已说明的快速共同建场、忽略自感、启动位置不变和随后局部径向场模型下：
$$
\begin{aligned}
v_0&=\frac{\pi^2r^3B_r\bar B_z}{mR},\\
\tau&=\frac{mR}{4\pi^2r^2B_r^2},\\
v(t)&=(v_0+g\tau)e^{-t/\tau}-g\tau,\\
z(t)&=\tau(v_0+g\tau)(1-e^{-t/\tau})-g\tau t,\\
t_*&=\tau\ln\left(1+\frac{v_0}{g\tau}\right),\\
z_{\max}&=\tau v_0-g\tau^2\ln\left(1+\frac{v_0}{g\tau}\right).
\end{aligned}
$$
图4-5以 $\eta=1$ 为例，将有符号速度的唯一零点和位移的最高点画在相同的无量纲时间轴上；任意正的 $\eta$ 都有相同的先上升后下降关系，但具体刻度值不同。图中负的速度不表示“负速率”，而表示向下运动；位移返回零时的速度已为负。

![图4-5 启动后速度递减、唯一最高点与下降回程的对应关系。](../figures/graphs-04.png){width=82%}

先上升、再下降是明确的动力学结果，不是额外假定。以上各式的时间零点都是启动结束；若记录从开关闭合起的总时间，还需加上小的启动时长。图中的长时终端线仅展示局部常场模型的数学趋势，不把线圈附近的近似延伸为真实无限空间。

## 六、关键洞察

**1. 磁通负责产生电流，径向场负责把电流转成竖直力。**

启动时必须同时使用 $\bar B_z$ 和 $B_r$。前者来自环面的积分，后者来自环上导线的受力。若只用竖直场计算竖直安培力，导线与竖直场的叉积只能指向水平，无法使环的质心升起；若只用径向场计算穿过水平环面的磁通，其法向分量又为零。

这一区别与“同一个场有多个分量”相容。图4-3的磁通闭合关系将两个分量联系起来，但不是把它们数值相等。一个可直接检验的局部轴对称场是
$$
B_z(\rho,z)=B_0-kz,
\qquad B_\rho(\rho,z)=\frac{k\rho}{2}.
$$
它满足
$$
\nabla\cdot\boldsymbol B
=\frac1\rho\frac{\partial(\rho B_\rho)}{\partial\rho}
+\frac{\partial B_z}{\partial z}
=k-k=0.
$$
在半径 $r$ 的环上，$B_r=kr/2$ 对高度不变，而 $\bar B_z=B_0-kz$ 随高度变化，恰好给出 $\mathrm d\bar B_z/\mathrm dz=-2B_r/r$。这是局部恒定径向场与运动感应可以同时成立的具体例子，不是关于真实螺线圈全球场型的猜测。

**2. 共同建场的半系数来自两种场的乘积，不来自时间平均。**

把 $a=2\pi rB_r$、$\Phi_0=\pi r^2\bar B_z$ 记为启动终值。启动力为
$$
F_{z,\mathrm s}=\frac{a\Phi_0}{R}s\dot s,
$$
冲量为 $a\Phi_0/(2R)$。$\bar B_z$ 的横线只是空间面积平均，绝不自动提供一个时间上的 $1/2$。真正的半系数由 $\mathrm d(s^2)/\mathrm dt=2s\dot s$ 得到。

共同建场可换成缓急不同的 $s(t)$，冲量不变，但瞬时力峰值、接触脱离时刻和焦耳热都可能变。若改变的是径向场与竖直磁通的相对建立顺序，积分变为 $\int B_r\,\mathrm d\bar B_z$，冲量就未必仍是同一半系数。不能把结论从“共同函数”扩大到“只要终值相同”。

**3. 快速启动、忽略自感和位置固定是三件不同的事。**

若真实环有很小但非零的 $L$，用纯电阻启动近似至少需要电响应时间 $L/R$ 小于建场时间；而建场时间又应小于环的机械变化尺度。例如可要求
$$
\frac LR\ll T_{\mathrm s},
\qquad gT_{\mathrm s}\ll v_0,
\qquad T_{\mathrm s}\ll\tau,
\qquad v_0T_{\mathrm s}\ll \ell_B,
$$
其中 $\ell_B$ 是场变化的空间尺度。前两类分别约束电响应、重力/阻尼和位移。真实有限 $L$ 下不能无限缩短 $T_{\mathrm s}$ 仍声称满足第一条。

位置固定的启动电流为 $I=-\Phi_0\dot s/R$，电阻热为
$$
Q_{\mathrm s}=\frac{\Phi_0^2}{R}
\int_0^{T_{\mathrm s}}\dot s^{\,2}\,\mathrm dt.
$$
线性建场 $s=t_{\mathrm s}/T_{\mathrm s}$ 给出 $Q_{\mathrm s}=\Phi_0^2/(RT_{\mathrm s})$。冲量在快启动近似中为有限值，而纯电阻模型的热却随启动时间缩短而增长，说明“瞬时建场”只是理想极限，不是对实际电源电流和热的无限制预测。

<!-- KEEP_TOGETHER_START -->

**4. 最高点的零电磁力比终端速度更能揭示不能悬停。**

对任意局部场函数，只要外场已经直流稳定、环的自感可忽略，运动电动势都与速度成正比。令环面外磁通为 $\Phi(z)$，则
$$
\mathcal E=-\Phi'(z)v,
\qquad I=-\frac{\Phi'(z)}R v,
\qquad F_z=I\Phi'(z)=-\frac{[\Phi'(z)]^2}{R}v.
$$

<!-- KEEP_TOGETHER_END -->

最后一个等式使用磁通梯度与环上竖直安培力的同一几何关系。即使 $B_r$ 随高度变化，$v=0$ 时仍有 $F_z=0$，因此无法以这一电磁力平衡非零重力。定量终端速度需场近似，不能定高悬停的判断却不依赖于场在任意高度都是同一个常数。

这条推论只针对感应电流安培力，不包含永久磁体、超导持久电流、铁磁磁化吸引或另一个机械支承。改变物理机制后必须重新建模。

**5. 同样写成指数，机械时间常数和电路时间常数不能混用。**

主解的 $\tau=mR/a^2$ 随 $R$ 增大而增大：较大的电阻使运动电流更小、阻尼更弱。有限自感定高电流的衰减时间 $L/R$ 却随 $R$ 增大而减小。两个时间都可出现在指数中，但它们的物理对象、来源和参数趋势完全不同。

主解机械能减少为 $RI^2$；有限自感时还需把环的自磁场能 $LI^2/2$ 加入。若保留 $L$ 但仍使用主解的单一一阶速度方程，会漏掉电流作为独立状态变量，既不能正确描述启动，也不能解释交流平均升力。

## 七、易错点

**1. 把感应电流一直当作正值。** 启动建场产生负电流，上升运动产生正电流，下降运动又产生负电流。用绝对值代替 $I$ 后再套同一受力式，会至少错掉一个阶段。

**2. 只看环与线圈电流相反而不检查径向场。** “相反”可帮助建立排斥直觉，但竖直合力仍由环上径向场决定，须用微元叉积说明。

**3. 启动积分用最终的 $B_r$。** 径向场和竖直场共同增长，力含 $s\dot s$。忘掉 $s$ 会把 $v_0$ 多算一倍，继而使最高点与回程时间全部错误。

**4. 将 $\bar B_z$ 理解为时间平均。** 它是环面的空间平均磁场，用于外磁通 $\pi r^2\bar B_z$；正确的启动半系数需另做时间积分。

**5. 认为直流建场后就永远没有电流。** 定高静止环的电流可为零，但移动环仍有运动电动势。必须区分显含时间的场变化和位置引起的磁通变化。

**6. 把局部恒定 $B_r$ 与处处恒定磁通同时使用。** 二者不相容。图4-3的闭合磁通关系要求竖直面积平均场随高度变化。

**7. 把电磁力全程画成一个固定方向。** $F_z=-\kappa v$，上升向下、下降向上；最高点为零。符号规则比“阻力向下”的口头印象更可靠。

**8. 用加速度为零求最高点。** 最高点速度为零，加速度仍为 $-g$；加速度趋于零对应向下终端运动，不是最高点。

**9. 位移少写 $-g\tau t$。** 这会制造假悬停。对位移式求导必须恢复有符号速度。

**10. 回程求根选到 $t=0$。** 回到初始高度方程含初始根和另一正根。必须结合最高点之后下降的时间区间筛选。

**11. 只要交流就认定有正平均升力。** 纯电阻电流与外场相差四分之一周期，定高平均力为零。电流有效值不为零，不能据此把有正负的力平均成正值。

**12. 把电压翻倍等同于升力翻倍。** 电流和产生力的外场都随电压变化，乘积呈平方比例；只改变质量时需 $\sqrt2$ 倍而非 $2$ 倍。

**13. 混用峰值和有效值。** 第19步采用磁场峰值，周期平均带 $1/2$；若改用有效值，两场各带 $1/\sqrt2$，表达式中不能再额外重复乘同一个 $1/2$。

**14. 把 $\tau=mR/a^2$ 当成 $L/R$。** 前者是质量—运动感应形成的机械时间，后者是自感—电阻形成的电响应时间；参数变化趋势也不同。

**15. 将固定初速度弱阻尼检验当成同时改电阻的实验。** 原题启动 $v_0$ 也依赖电阻。极限检验必须先说明保持哪个量不变。

**16. 在有自感时漏掉自磁场能。** 此时电磁力的机械功率不等于全部电阻热的负值，还包含 $LI^2/2$ 的变化。能量缺项会导致错误的阻力或电流结论。

## 八、课堂讲解建议

课堂先展示图4-1与图4-2，不立即给出阻尼方程。让学生规定俯视逆时针为正，然后在环的近侧和远侧分别画出 $\mathrm d\boldsymbol l\times\boldsymbol B$。两侧的竖直力同向、水平力相消，是从局部受力过渡到整体运动的第一道知识台阶，不宜用一句“线圈排斥铁环”替代。

板书将时间分成“建场阶段”和“建场结束后”两栏。前一栏写 $I\propto-\dot s$、$F\propto s\dot s$、$J\propto\int s\,\mathrm ds$，后一栏写 $I\propto v$、$F\propto-v$。先把各栏正负号核对一致，再计算大小。教师应强调半系数的来源是正在增长的径向场，不是横线符号代表平均值。

用图4-3连接法拉第磁通法与运动电动势法。课堂可问：“若径向场向外穿出薄圆柱，两个水平底面的竖直磁通能完全相同吗？”让学生先用闭合面磁通守恒判断上底更小，再写 $\Phi'(z)=-2\pi rB_r$。这样后续 $\mathcal E=2\pi rB_rv$ 有两条独立依据，不是背一个周长乘速度公式。

求微分方程时，板书保留乘积求导、积分上下限及初值。对初学竞赛的学生而言，直接写出“解得指数式”会掩盖积分因子为何成立，也容易漏掉速度常量项。求位移后立即让学生求导检验，再比较图4-5的速度零点与位移最高点；最高点加速度为 $-g$ 是区分“停一下”与“保持静止”的有效问题。

交流部分先只画纯电阻的场—电流相位图，逐个四分之一周期判断力的正负，然后实际平均 $\sin\omega t\cos\omega t$。学生理解平均为零后，教师再引入 $L\dot I+RI=\mathcal E$，说明自感使电流出现与场同相的分量。板书不只给电流振幅，也应保留决定平均力的余弦系数。

结束时用功率恒等式作整题审查：机械能减少率与 $RI^2$ 一一对应。教师可让学生定位三类错误：初速度倍数错误来自启动积分，电磁力方向错误来自叉积，假悬停来自位移漏项。每类错误都有明确的检查入口，而不是仅凭最后数值是否熟悉来判断。

## 九、变式训练

**变式1：相同终值，不同建场速度或不同步建场。**

保持环的位置不变、自感可忽略。令径向场建立函数为 $f(u)$，竖直磁通建立函数为 $h(u)$，其中 $u=t_{\mathrm s}/T_{\mathrm s}$、$0\le u\le1$，并且两个函数均从 $0$ 变到 $1$。求启动冲量；比较共同建场与 $f=u^p,h=u^q$ 的情形，其中 $p,q>0$。

**解：** 仍记 $a=2\pi rB_r$、$\Phi_0=\pi r^2\bar B_z$。电流与力分别为
$$
I=-\frac{\Phi_0}{RT_{\mathrm s}}h'(u),
\qquad F_z=\frac{a\Phi_0}{RT_{\mathrm s}}f(u)h'(u).
$$
用 $\mathrm dt_{\mathrm s}=T_{\mathrm s}\,\mathrm du$，得到
$$
J_z=\frac{a\Phi_0}{R}\int_0^1f(u)h'(u)\,\mathrm du.
$$
若 $f=h=s$，积分为 $[s^2/2]_0^1=1/2$，无论 $s=u$、$s=u^2$ 还是 $s=(1-\cos\pi u)/2$，冲量都等于 $a\Phi_0/(2R)$。

但共同终值不保证共同过程。若 $f=u^p,h=u^q$，则
$$
\begin{aligned}
\int_0^1 f h'\,\mathrm du
&=\int_0^1u^p\,q u^{q-1}\,\mathrm du\\
&=q\left[\frac{u^{p+q}}{p+q}\right]_0^1\\
&=\frac{q}{p+q},\\
J_z&=\boxed{\frac{a\Phi_0}{R}\frac{q}{p+q}}.
\end{aligned}
$$
$p=q$ 才回到半系数；$p=1,q=3$ 给 $3/4$，$p=3,q=1$ 给 $1/4$。这是数学上不同外场建立历程的比较，不声称单个理想线圈同一电流能够让两个分量任意不同步。

共同建场的焦耳热则为
$$
Q_{\mathrm s}=\frac{\Phi_0^2}{RT_{\mathrm s}}
\int_0^1[s'(u)]^2\,\mathrm du.
$$
线性、二次和半余弦建场的最后一个积分分别是 $1$、$4/3$、$\pi^2/8$。因此相同冲量不等于相同热量：冲量积分含 $ss'$，热量积分含 $(s')^2$。有限启动时，离桌还需检查峰值安培力与重力，不能只看总冲量。

**变式2：给定机械阻尼尺度，求上升时间、高度与落回时间。**

设启动后 $v_0=g\tau$，局部常场模型在全部回程中有效。求最高点、回到启动高度的正时间根，以及上升阶段的焦耳热。

**解：** 此时 $\eta=1$，所以
$$
v(t)=g\tau(2e^{-t/\tau}-1),
\qquad z(t)=g\tau^2[2(1-e^{-t/\tau})-t/\tau].
$$
最高点速度为零，故
$$
\boxed{t_*=\tau\ln2,\qquad
z_{\max}=g\tau^2(1-\ln2)}.
$$
回程令 $u=t/\tau$，求 $2(1-e^{-u})=u$。零根是初始状态，另一根可在区间 $(1,2)$ 内求得
$$
u_{\text{回}}\approx1.5936242600,
\qquad t_{\text{回}}\approx1.5936242600\,\tau.
$$
利用根方程 $2e^{-u}=2-u$，落回速度不需再重复算指数：
$$
v_{\text{回}}=g\tau[(2-u_{\text{回}})-1]
=g\tau(1-u_{\text{回}})
\approx-0.5936242600\,g\tau.
$$
负号说明环向下，且落回速率小于初始向上速率，符合机械能部分耗散。

上升阶段最高点动能为零，机械能损失全部转成焦耳热：
$$
\begin{aligned}
Q_{\text{上}}
&=\frac12mv_0^2-mgz_{\max}\\
&=mg^2\tau^2\left[\frac12-(1-\ln2)\right]\\
&=\boxed{mg^2\tau^2\left(\ln2-\frac12\right)>0}.
\end{aligned}
$$
一般 $\eta>0$ 时，同理得到
$$
Q_{\text{上}}
=mg^2\tau^2\left[\frac{\eta^2}{2}-\eta+\ln(1+\eta)\right].
$$
括号在 $\eta=0$ 为零，其导数为 $\eta^2/(1+\eta)>0$，所以所有正初速度的上升过程中均有正热量。这一检查同时核对最大高度公式和能量符号。

**变式3：有限自感交流环的升力与频率。**

环固定在一个给定高度，电阻为 $R>0$、自感为 $L>0$。该高度外磁通为 $A\cos\omega t$，竖直受力系数为 $-C\cos\omega t$，即 $F_z=-C\cos\omega t\,I$，其中 $A,C>0$。求稳态电流、平均升力与平均发热功率；在外磁场峰值固定时讨论低频、高频及 $L\to0$ 的极限。

**解：** 电动势为 $\omega A\sin\omega t$。解析第19步的系数比较给出
$$
I(t)=\frac{\omega AR\sin\omega t-\omega^2AL\cos\omega t}
{R^2+\omega^2L^2}.
$$
同相余弦电流的系数为负，因此与 $-C\cos\omega t$ 相乘后贡献正平均力：
$$
\boxed{\langle F_z\rangle
=\frac{CA\omega^2L}{2(R^2+\omega^2L^2)}}.
$$
求平均热时需要电流平方的平均，而不是电流本身的平均。由于正弦、余弦平方各平均为 $1/2$，交叉项平均为零，
$$
\begin{aligned}
\langle I^2\rangle
&=\frac12\left[
\left(\frac{\omega AR}{R^2+\omega^2L^2}\right)^2
+\left(\frac{\omega^2AL}{R^2+\omega^2L^2}\right)^2\right]\\
&=\frac{\omega^2A^2(R^2+\omega^2L^2)}
{2(R^2+\omega^2L^2)^2}\\
&=\frac{\omega^2A^2}{2(R^2+\omega^2L^2)},\\
\langle P_{\mathrm J}\rangle
&=\boxed{\frac{R\omega^2A^2}{2(R^2+\omega^2L^2)}}.
\end{aligned}
$$
在给定 $A,C,R,L$ 下，低频 $\omega L\ll R$ 时
$$
\langle F_z\rangle\approx\frac{CA L}{2R^2}\omega^2,
\qquad
\langle P_{\mathrm J}\rangle\approx\frac{A^2}{2R}\omega^2.
$$
高频 $\omega L\gg R$ 时
$$
\langle F_z\rangle\to\frac{CA}{2L},
\qquad
\langle P_{\mathrm J}\rangle\to\frac{RA^2}{2L^2}.
$$
升力并不随频率无限增大；保持外场峰值固定时会趋于饱和值。此“固定场峰值”不是固定电源电压：改变频率可改变线圈阻抗，若电源电压固定，$A,C$ 自身也可能随频率变化，须先求主线圈响应。

对任意固定的非零 $R,\omega$，$L\to0$ 使平均升力趋于零，但热功率趋于 $A^2\omega^2/(2R)$。这再次说明有热、有电流不等于有平均支持力。悬浮高度的稳定性还需要 $A(z),C(z)$ 的导数；只给该高度的幅值不能唯一判断空间稳定性。

**变式4：直流启动若保留自感，为什么不能沿用冲量初速度？**

在局部常场中记 $a=2\pi rB_r>0$，启动后外磁通随高度为 $\Phi_{\mathrm{ext}}(z)=\Phi_0-az$。环具有电阻 $R>0$、自感 $L>0$。外磁通从零快速跳变为 $\Phi_0$，环位置近似不动。求启动电流、离桌条件与其后电流—速度的耦合方程；说明长期运动与能量检查。

**解：** 先在极短的建场时间内对完整回路方程积分：
$$
L\dot I+RI=-\dot\Phi_{\mathrm{ext}}.
$$
在有限电流下电阻项的时间积分趋于零，故
$$
L[I(0^+)-I(0^-)]=-[\Phi_0-0].
$$
初始电流为零，因此
$$
\boxed{I(0^+)=-\frac{\Phi_0}{L}}.
$$
电流发生有限跳变，安培力 $-aI$ 是有限阶跃，不是力的狄拉克冲量。故环的位置和速度在瞬时建场时连续，取 $z(0)=0,v(0)=0$；不能使用主解 $v_0=a\Phi_0/(2mR)$，因为那是另一种 $L=0$ 快速但有限建场模型。

启动结束时向上力为 $a\Phi_0/L$。从桌面离开需要
$$
\boxed{\frac{a\Phi_0}{L}>mg}.
$$
若不满足该条件，环可能一直保持桌面接触，不能把无支持力的自由运动方程套到初始接触阶段。下面只讨论满足该条件而离桌的分支。

建场后显含时间的外场变化为零，但运动外磁通变化为 $\dot\Phi_{\mathrm{ext}}=-av$。完整耦合方程是
$$
\boxed{
\begin{aligned}
m\dot v&=-mg-aI,\\
L\dot I+RI&=av,\\
\dot z&=v.
\end{aligned}}
$$
其中第一式是环的动力学，第二式是环的电路。电流不再由瞬时速度单独决定，必须作为独立状态变量。

形式上的长时匀速解满足 $\dot v=\dot I=0$，所以
$$
\begin{aligned}
I_\infty&=-\frac{mg}{a},\\
v_\infty&=\frac{R}{a}I_\infty
=-\frac{mgR}{a^2}.
\end{aligned}
$$
终端速度仍向下，有限自感并未提供永久的直流定高悬浮。该解仍只用于局部常场数学模型，不延长到真实线圈远场。

为了看清瞬态，令 $u=v-v_\infty$、$j=I-I_\infty$，有
$$
m\dot u=-aj,
\qquad L\dot j+Rj=au.
$$
对第一式求导，用第二式消去 $\dot j$，再由 $j=-m\dot u/a$ 消去 $j$：
$$
\begin{aligned}
m\ddot u&=-a\dot j
=-\frac{a^2}{L}u+\frac{aR}{L}j\\
&=-\frac{a^2}{L}u-\frac{mR}{L}\dot u,\\
\ddot u+\frac RL\dot u+\frac{a^2}{mL}u&=0.
\end{aligned}
$$
特征根为
$$
\lambda_\pm=\frac{-R\pm\sqrt{R^2-4La^2/m}}{2L}.
$$
两根实部都为负；根为复数时速度与电流可出现衰减振荡，不能再称为主解的一条单调指数。初值为
$$
u_0=\frac{mgR}{a^2},
\qquad \dot u_0=-g+\frac{a\Phi_0}{mL}.
$$
不同根时令
$$
c_+=\frac{\dot u_0-\lambda_-u_0}{\lambda_+-\lambda_-},
\qquad c_-=u_0-c_+,
$$
则完整解为
$$
\begin{aligned}
v(t)&=v_\infty+c_+e^{\lambda_+t}+c_-e^{\lambda_-t},\\
z(t)&=v_\infty t+
c_+\frac{e^{\lambda_+t}-1}{\lambda_+}
+c_-\frac{e^{\lambda_-t}-1}{\lambda_-},\\
I(t)&=I_\infty-\frac m a
\left(c_+\lambda_+e^{\lambda_+t}
+c_-\lambda_-e^{\lambda_-t}\right).
\end{aligned}
$$
共轭根和系数的和为实数。临界重根时，令 $\gamma=R/(2L)$、$b=\dot u_0+\gamma u_0$，改用
$$
\begin{aligned}
u(t)&=(u_0+bt)e^{-\gamma t},\\
z(t)&=v_\infty t+
\frac{u_0}{\gamma}(1-e^{-\gamma t})
+\frac b{\gamma^2}[1-(1+\gamma t)e^{-\gamma t}],
\end{aligned}
$$
而不是在 $\lambda_+=\lambda_-$ 的式中除以零。以上解只适用于离桌后尚未再次接触桌面的阶段；接触事件需另加支持力条件。

最后核对能量。将机械方程乘 $v$、电路方程乘 $I$：
$$
\begin{aligned}
\frac{\mathrm d}{\mathrm dt}\left(\frac12mv^2+mgz\right)
&=-aIv,\\
\frac{\mathrm d}{\mathrm dt}\left(\frac12LI^2\right)
&=aIv-RI^2.
\end{aligned}
$$
相加消去环与电磁场之间的交换功率，得到
$$
\boxed{\frac{\mathrm d}{\mathrm dt}
\left(\frac12mv^2+mgz+\frac12LI^2\right)=-RI^2.}
$$
自磁场能是保留自感后必须新增的项。电路、动力学与能量三条路线相互一致，才说明自感变式真正成立；不能只把主解指数中的时间常数改为 $L/R$。

<!-- draft-content-complete: 014-04; 21步完整核心、四个带解变式；五图已绘，实际PDF及分题验收另存，不计整套完成。 -->
