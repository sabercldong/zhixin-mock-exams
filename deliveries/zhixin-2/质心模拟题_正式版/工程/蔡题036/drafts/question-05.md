# 第 5 题

单极感应器由高速转动的圆盘形永磁体构成。圆盘由磁性合金制成，表面覆盖薄导电层。圆盘转动时，可以用固定电压表通过滑动接触测量转轴与圆周边缘的电势差；在两者之间接入电池，也可以使圆盘像电动机一样转动。

圆盘半径为 $r_0=2\,\mathrm{cm}$，表面磁感应强度 $\mathbf B$ 垂直盘面向上，大小恒为 $B=1\,\mathrm T$。为简化计算，假定导电层中的电流沿轴心与圆周接触点之间的半径流动。最终数值保留两位有效数字。

（1）按图左侧连接电压表。圆盘转速为 $3000\,\mathrm{r/min}$，从上方看沿逆时针方向转动。以上方接线端电势较高为正，求电压表读数。

（2）按图右侧连接电动势 $E=1.5\,\mathrm V$ 的电池，滑动接触良好，圆盘从静止开始转动。忽略摩擦，求可达到的最大转速，并指出从上方看的转动方向。

（3）接上问，设摩擦阻力矩大小为 $M=k\omega$，其中 $\omega$ 为角速度。整个转子质量为 $m$，转动惯量为 $I=\frac12mr_0^2$，电路总内阻为 $R$。求由静止加速时角加速度和角速度的最大值。

（4）接上问，电动机以恒定角速度驱动阻力矩为 $M_0$ 的负载。求使负载获得最大功率的 $M_0$。

![图5-1　单极圆盘的电压测量和电动机接线](../figures/question-05.pdf){ width=95% }

## 一、题型定位

本题把动生电动势、安培力矩、转动方程和负载功率连接在同一个装置中。先建立一个共同的机电耦合系数 $K=Br_0^2/2$：圆盘转动产生电动势 $K\omega$，径向电流产生力矩 $Ki$。两者的一致性保证机械功率和电能转化功率相等。

## 二、知识点

1. 洛伦兹力 $q\mathbf v\times\mathbf B$ 与导体内电荷分离；
2. 动生电动势的径向积分；
3. 径向电流元所受安培力及其力矩；
4. 反电动势、摩擦阻尼与一阶转动动力学；
5. 稳态负载条件下的功率极值；
6. 转速单位换算及能量守恒核验。

## 三、物理图像

规定从上方看逆时针为正转动，故 $\boldsymbol\omega$ 和 $\mathbf B$ 都向上。盘面某点的速度沿正切线方向，$\mathbf v\times\mathbf B$ 指向径向外侧，正电荷被推向圆周，圆周电势高于轴心。上方电压表接线端连接轴心，所以按题定正负读数应为负。

电池长线端接圆周，驱动常规电流从圆周向轴心流动。向内的径向电流在向上的磁场中受到逆时针切向力，使转子加速。转得越快，圆周相对轴心的动生电势差越大，与电池电动势对抗，电流和驱动力矩随之减小。

## 四、解题入口

对半径 $r$ 处的导体元 $dr$ 分别做两个积分：发电时积分 $B\omega r\,dr$，电动时积分 $r\,iB\,dr$。先从物理上得到共同系数 $K$，再写

$$
i=\frac{E-K\omega}{R},\qquad
I\dot\omega=Ki-k\omega-M_0.
$$

无负载加速取 $M_0=0$；匀速驱动负载取 $\dot\omega=0$。不应在这两个阶段使用同一个“净力矩为零”条件。

## 五、解析

（1）用右手基矢明确方向。取 $\mathbf e_r$ 向外，$\mathbf e_\varphi$ 沿逆时针，$\mathbf e_z$ 向上。则

$$
\mathbf v=\omega r\,\mathbf e_\varphi,\qquad
\mathbf B=B\,\mathbf e_z,\qquad
\mathbf e_\varphi\times\mathbf e_z=\mathbf e_r.
$$

于是磁力对正电荷的作用为

$$
q\mathbf v\times\mathbf B=qB\omega r\,\mathbf e_r,
$$

方向向外。开路稳态中电荷分离产生的静电场与之平衡：

$$
q(\mathbf E_{\rm el}+\mathbf v\times\mathbf B)=0,
\qquad E_r=-B\omega r.
$$

由于 $E_r=-dV/dr$，有 $dV/dr=B\omega r$。从轴心 $O$ 积分到圆周 $A$，

$$
\begin{aligned}
V_A-V_O
&=\int_0^{r_0}B\omega r\,dr\\
&=B\omega\left[\frac{r^2}{2}\right]_0^{r_0}\\
&=\frac12B\omega r_0^2.
\end{aligned}
$$

这个正号表示圆周电势更高。题目规定的仪表读数却是上接线端减下接线端，而图中上端接轴、下端接边缘，因此

$$
U_{\rm meter}=V_O-V_A=-\frac12B\omega r_0^2.
$$

转速 $n=3000\,\mathrm{r/min}$ 换算为角速度：

$$
\begin{aligned}
f&=\frac{3000}{60}\,\mathrm{s^{-1}}=50\,\mathrm{s^{-1}},\\
\omega&=2\pi f=100\pi\,\mathrm{rad/s}.
\end{aligned}
$$

半径必须化为米，$r_0=0.020\,\mathrm m$。代入，

$$
\begin{aligned}
U_{\rm meter}
&=-\frac12(1)(100\pi)(0.020)^2\,\mathrm V\\
&=-0.0628318\ldots\,\mathrm V.
\end{aligned}
$$

保留两位有效数字，

$$
\boxed{U_{\rm meter}=-0.063\,\mathrm V=-63\,\mathrm{mV}.}
$$

负号是接线方向的结果，不表示电动势大小为负。若交换仪表接线，读数变正；若在原接线下反转圆盘或反转磁场，读数也变号。

（2）电池驱动与最终空载速度。定义

$$
K=\frac12Br_0^2.
$$

从圆周流向轴心的常规电流取正。其在半径元上的方向为 $-\mathbf e_r$，故

$$
d\mathbf F=i(-dr\,\mathbf e_r)\times(B\mathbf e_z)
=iB\,dr\,\mathbf e_\varphi.
$$

安培力沿逆时针，力矩与正角速度同向。图5-2左侧把半径 $r$、微元 $dr$、向内电流和切向力画在同一平面中。后面的 $r$ 因子来自作用点到轴的力臂，而不是再乘一次导线长度。

![图5-2　径向电流元的安培力矩与转矩—转速关系](../figures/solution-05.pdf){ width=95% }

单个微元的力矩为 $dM=r\,iB\,dr$，全盘有效半径上的积分给出

$$
\begin{aligned}
M_{\rm em}
&=\int_0^{r_0}riB\,dr\\
&=\frac12iBr_0^2=Ki.
\end{aligned}
$$

逆时针转动产生的圆周高电势抵抗电池所驱动的向内电流，因此

$$
Ri=E-K\omega,\qquad
i=\frac{E-K\omega}{R}.
$$

忽略摩擦且没有负载时，只要 $K\omega<E$，电流和力矩就为正，转子继续加速；达到 $K\omega=E$ 的极限时，电流趋于零，净力矩趋于零。因此

$$
\boxed{\omega_{\max}=\frac EK=\frac{2E}{Br_0^2}}.
$$

代入数据，

$$
\omega_{\max}=\frac{2(1.5)}{1(0.020)^2}
=7500\,\mathrm{rad/s}.
$$

转为每分钟转数：

$$
\begin{aligned}
n_{\max}
&=\frac{60}{2\pi}\omega_{\max}\\
&=\frac{60}{2\pi}\times7500
=7.16197\ldots\times10^4\,\mathrm{r/min}.
\end{aligned}
$$

故

$$
\boxed{n_{\max}=7.2\times10^4\,\mathrm{r/min},\quad
\text{从上方看逆时针}.}
$$

在有限电阻和惯量的理想模型中，这个“最大值”是随时间渐近达到的极限速度，不能理解为某一有限时刻突然停止加速。真实装置还可能受机械强度等限制，但题目模型没有包含这些因素。

（3）加入线性摩擦。无负载时，摩擦力矩反向，大小 $k\omega$，所以

$$
I\dot\omega=K\frac{E-K\omega}{R}-k\omega.
$$

展开并整理，

$$
\begin{aligned}
I\dot\omega
&=\frac{KE}{R}-\left(\frac{K^2}{R}+k\right)\omega,\\
\dot\omega
&=\frac{KE}{IR}
-\frac{K^2+kR}{IR}\omega.
\end{aligned}
$$

初始 $\omega=0$，反电动势和题设的线性摩擦力矩均为零，此时加速度最大：

$$
\alpha_{\max}=\frac{KE}{IR}.
$$

代入 $K=Br_0^2/2$ 和 $I=mr_0^2/2$，

$$
\begin{aligned}
\alpha_{\max}
&=\frac{(Br_0^2/2)E}{(mr_0^2/2)R}\\
&=\boxed{\frac{EB}{mR}}.
\end{aligned}
$$

半径消去的原因是驱动力矩和转动惯量都含同一个 $r_0^2$ 因子，不表示所有形状的转子都有这个性质。若质量分布改变，$I$ 的表达式也会改变。

随 $\omega$ 增大，加速度以线性规律减小。稳态由驱动力矩与摩擦平衡：

$$
\frac{KE}{R}-\frac{K^2}{R}\omega_\infty-k\omega_\infty=0.
$$

移项、合并系数，

$$
KE=(K^2+kR)\omega_\infty.
$$

所以

$$
\boxed{\omega_{\max}=\omega_\infty
=\frac{KE}{K^2+kR}
=\frac{2EBr_0^2}{B^2r_0^4+4kR}.}
$$

图5-2右侧的下降直线为电磁力矩，上升直线为摩擦力矩，两者交点对应上述 $\omega_\infty$。不计摩擦时交点退到横轴截距 $E/K$，与第（2）问连续相接。

再解出整个加速过程，以验证最大值所在位置。定义机械—电磁共同时间常量

$$
\tau=\frac{IR}{K^2+kR}.
$$

方程化为

$$
\dot\omega=\frac{\omega_\infty-\omega}{\tau}.
$$

分离变量并使用 $\omega(0)=0$，

$$
\begin{aligned}
\int_0^\omega\frac{d\widetilde\omega}
{\omega_\infty-\widetilde\omega}
&=\int_0^t\frac{dt'}{\tau},\\
-\ln\left(1-\frac{\omega}{\omega_\infty}\right)
&=\frac t\tau.
\end{aligned}
$$

故

$$
\omega(t)=\omega_\infty(1-e^{-t/\tau}),\qquad
\alpha(t)=\frac{\omega_\infty}{\tau}e^{-t/\tau}.
$$

两式分别单调增加和单调减小；又 $\omega_\infty/\tau=KE/(IR)$，与前面由初始状态求出的 $\alpha_{\max}$ 一致。这里隐含题目忽略电路自感，电流由瞬时欧姆关系决定；若另加电感，初始电流与加速度将需要重新求解。

（4）现在接入恒定阻力矩 $M_0$ 的负载，并讨论正向匀速状态。转动方程变为

$$
0=\frac{K(E-K\omega)}R-k\omega-M_0.
$$

乘以 $R$ 并整理，

$$
KE=(K^2+kR)\omega+RM_0.
$$

所以匀速角速度为

$$
\omega=\frac{KE-RM_0}{K^2+kR}.
$$

正向运行要求 $\omega\geq0$，即

$$
0\leq M_0\leq\frac{KE}{R}.
$$

负载得到的机械功率不是 $Ei$，而是

$$
\begin{aligned}
P_{\rm load}
&=M_0\omega\\
&=\frac{KE\,M_0-RM_0^2}{K^2+kR}.
\end{aligned}
$$

分母为正，与 $M_0$ 无关；分子是开口向下的二次函数。可以求导，也可以配方。配方过程为

$$
\begin{aligned}
KE\,M_0-RM_0^2
&=-R\left[M_0^2-\frac{KE}{R}M_0\right]\\
&=-R\left(M_0-\frac{KE}{2R}\right)^2
+\frac{K^2E^2}{4R}.
\end{aligned}
$$

所以最大值位于

$$
\boxed{M_0^*=\frac{KE}{2R}=\frac{EBr_0^2}{4R}}.
$$

它在允许区间的正中，确实是正向运行时的内部最大值，不需要再与无物理意义的负角速度区间比较。相应速度和功率为

$$
\omega_*=\frac{KE}{2(K^2+kR)}=\frac{\omega_\infty}{2},
$$

$$
P_{\max}=\frac{K^2E^2}{4R(K^2+kR)}.
$$

最优负载力矩没有 $k$，但最优速度及最大功率都依赖 $k$。原因是线性摩擦只改变整个功率抛物线的正比例系数，不改变它的横坐标顶点；这不是任意摩擦规律下都成立的结论。

做能量检验。欧姆关系 $E=Ri+K\omega$ 乘以 $i$，得到

$$
Ei=Ri^2+Ki\omega.
$$

转动方程乘以 $\omega$，得到

$$
Ki\omega=I\omega\dot\omega+k\omega^2+M_0\omega.
$$

合并为

$$
\boxed{Ei=Ri^2+\frac{d}{dt}\left(\frac12I\omega^2\right)
+k\omega^2+P_{\rm load}.}
$$

等式逐项对应电源输入、焦耳热、转动动能、摩擦热及负载输出。若电动势积分或力矩积分漏掉因子 $1/2$，这项检验将无法成立。它是两个径向积分应得到同一 $K$ 的根本原因。

最后看极限：$k\to0$ 时空载速度回到 $E/K$；$M_0\to0$ 时负载功率为零但转子可转得很快；$M_0\to KE/R$ 时转子堵转，负载功率仍为零。最大功率只能在二者之间，不能用“力矩越大功率越大”或“速度越大功率越大”单独判断。

在求得的最大功率工作点，还可以把电流明确算出，确认电池确实在供能而不是被反充电。将 $\omega_*=KE/[2(K^2+kR)]$ 代入欧姆关系，

$$
\begin{aligned}
i_*
&=\frac ER-\frac KR\frac{KE}{2(K^2+kR)}\\
&=\frac ER\left[1-\frac{K^2}{2(K^2+kR)}\right]\\
&=\frac{E(K^2+2kR)}{2R(K^2+kR)}>0.
\end{aligned}
$$

当 $k>0$ 时，$i_*>E/(2R)$。同一电源与电阻下，摩擦增加使该工作点需要更大的电流，而不是可以忽略电流变化只从输出功率中简单减去一个常数。

转子在此时匀速，驱动力矩应分成负载和摩擦两部分。把电流乘以 $K$ 后减去最优负载力矩，得到

$$
\begin{aligned}
Ki_*-M_0^*
&=\frac{KE}{2R}
\left[\frac{K^2+2kR}{K^2+kR}-1\right]\\
&=\frac{kKE}{2(K^2+kR)}=k\omega_*.
\end{aligned}
$$

这项直接代回验证说明 $M_0^*=KE/(2R)$ 虽然没有 $k$，但电磁力矩并非与摩擦无关。多出来的力矩恰好抵消摩擦；把 $Ki_*$ 误认成全部负载力矩，将会错误预测更大的负载输出。

## 六、关键洞察

动生电动势为 $K\omega$，电磁转矩为 $Ki$。两式采用同一系数 $K$，才能使电磁输入功率 $Ki\omega$ 与机械功率相等；稳态、起动和带载计算都应保留这对关系。

## 七、易错点

电压表上端接轴心，故本题开路读数为负。仅判断圆周电势高，却没有回到实际接线定义，仍可能把最后符号写错。

半径导体不同位置的速度为 $\omega r$，不能把整条半径都当成边缘速度 $\omega r_0$。这样会把动生电动势算大一倍。力矩积分同样不能把所有力臂取成 $r_0$。

有摩擦时，稳态不等于电流为零。稳态电流需要提供摩擦力矩。仅在完全无摩擦、无负载的空载极限下，电流才趋于零。

## 八、课堂讲解建议

课堂先在俯视图中选一个右侧导体元，让学生用右手法则分别判断发电时正电荷受力和电动时径向电流受力。教师把两个判断用同一个坐标三基矢写下，再进行积分。

板书保留 $K$ 到求完动态方程后再展开，可以让学生看见方程结构；数值换算则单独列出厘米到米、转每分到弧度每秒两步。最后用功率守恒反查两个积分，强化独立核验意识。

## 九、变式训练

变式一：若无摩擦 $k=0$，负载取最大功率时的 $M_0^*$，求电流、转速、输出功率和效率，并求每转一周的输入电能、负载做功和电阻放热。

此时

$$
\omega_*=\frac{E}{2K},\qquad
i_*=\frac{E-K\omega_*}{R}=\frac{E}{2R}.
$$

电源功率和负载功率分别代入电流和转速，效率取两者之比：

$$
\begin{aligned}
P_{\rm in}&=Ei_*=\frac{E^2}{2R},\\
P_{\rm out}&=M_0^*\omega_*=\frac{E^2}{4R},\\
\eta&=\frac{P_{\rm out}}{P_{\rm in}}=\boxed{\frac12}.
\end{aligned}
$$

输入功率的另一半为焦耳热 $Ri_*^2=E^2/(4R)$，所以无机械摩擦并不等于无损耗。

每转一周的时间由角速度确定，输入电能和焦耳热分别由功率乘时间求得，负载做功还可直接用恒定力矩乘转角求出：

$$
\begin{aligned}
T_*&=\frac{2\pi}{\omega_*}=\frac{4\pi K}{E},\\
W_{\rm in}&=P_{\rm in}T_*=\frac{2\pi KE}{R},\\
Q_R&=Ri_*^2T_*=\frac{\pi KE}{R},\\
W_{\rm load}&=2\pi M_0^*=\frac{\pi KE}{R}.
\end{aligned}
$$

每周都满足 $W_{\rm in}=Q_R+W_{\rm load}$。匀速时动能不增加，电能全部成为焦耳热和负载功；转动惯量仅影响到达此工作点的加速过程，不影响稳态能量比例。

变式二：发电圆盘接入恒压电源后从静止起动，无额外负载，阻尼转矩为 $k\omega$。求达到稳态角速度一半的时间与此前电源输入的电荷。记 $K=Br^2/2$、盘惯量为 $J$。

解：$J\dot\omega=K(\mathcal E-K\omega)/R-k\omega$，所以 $\omega_\infty=K\mathcal E/(K^2+kR)$、$\tau=JR/(K^2+kR)$。由 $\omega=\omega_\infty(1-e^{-t/\tau})$ 得 $t_h=\tau\ln2$。电流为 $i=\mathcal E/R-K\omega/R$，积分得

$$
q_h=\frac{\mathcal E\tau}{R}\ln2-\frac{K\omega_\infty\tau}{R}(\ln2-1/2).
$$

后一项是转动产生的反电动势对电流的削减。初态电流最大，达到稳态的过程不能用恒定稳态电流计算电荷。

变式三：将电刷接触位置改为内半径 $a$ 与外半径 $r$，圆盘其余参数不变。求电动势系数与起动角加速度，并比较 $a=r/2$ 时和原轴心电刷的结果。

解：半径 $\rho$ 处速度为 $\omega\rho$，径向动生电动势微元为 $B\omega\rho\,d\rho$。从 $a$ 到 $r$ 积分得

$$
\mathcal E_{\rm mot}=K_a\omega,\qquad K_a=\frac B2(r^2-a^2).
$$

互易的电磁转矩为 $K_ai$。从静止起动时 $i=\mathcal E/R$，$\alpha_0=K_a\mathcal E/(JR)$。取 $a=r/2$，$K_a=3K/4$、$\alpha_0=3\alpha_{0,\rm old}/4$。无机械阻尼时空载极限角速度 $\mathcal E/K_a$ 却增加为 $4/3$ 倍，起动加速度和空载转速不按同一比例变化。

变式四：取 $\beta=kR/K^2=1$，求稳态最大输出功率点与最大效率点的无量纲转速 $x=K\omega/\mathcal E$，并比较两点效率。

解：负载输出功率为 $P=(\mathcal E^2/R)x[1-(1+\beta)x]$，效率为 $\eta=x[1-(1+\beta)x]/(1-x)$。功率是开口向下的二次式，极值在 $x_P=1/4$，$P_{\max}=\mathcal E^2/(8R)$，效率 $\eta_P=1/6$。对效率求导，物理根为

$$
x_\eta=1-\frac1{\sqrt2},\qquad \eta_{\max}=(\sqrt2-1)^2=3-2\sqrt2\approx0.171573.
$$

最大效率点的转速略高于最大功率点，但效率只从 $0.166667$ 提升到 $0.171573$。两类优化的分母不同，不能用一个驻点回答两问。
