# 第2题

<!-- question-start -->
本题用简化模型讨论洛伦兹共振。中心天体质量为 $M$，引力常量为 $G$，初始自转角速度为 $\omega_0$。小颗粒质量为 $m$、电荷量为 $q$，在赤道附近与天体同向绕行。

（1）求不带电颗粒的同步轨道半径 $r_0$。

（2）从北极看天体逆时针自转，赤道处磁场由北向南，场强大小为 $B$。设 $|qB/m|\ll\omega_0$，求带电颗粒同步轨道半径 $r_1$ 相对 $r_0$ 的一阶偏差。

（3）在均匀且不随时间变化的磁场中，颗粒发生微小径向扰动，位置记为 $(\rho,\theta)$。机械角动量 $L$ 不再守恒。求修正项 $L_r$，使 $L+L_r$ 守恒。

（4）若均匀磁场缓慢变化为 $B(t)$，求修正项 $L'_r$，并给出 $\dot\theta$ 关于 $\rho(t)$ 的关系。

（5）颗粒在圆轨道附近有径向振动 $\rho=r_1(1+\alpha\cos\omega_0t)$，$\alpha\ll1$。天体转速变为 $\omega_1$，磁场随其旋转，南向磁场大小为 $B_0-\Delta B\cos\theta$，$|\Delta B|\ll B_0$。在惯性系中，定性表示附近的磁场时间变化率及感生电场方向。

（6）设 $r_1$ 附近的感生电场可写为 $\mathbf E=E_0\cos\theta\,\hat{\mathbf r}$。写出颗粒在一个公转周期内的平均功率积分，给出一个使颗粒持续吸收能量的 $\omega_0,\omega_1$ 条件，并说明理由。

为避免本题第（5）问角度记号与前面混淆，解答用 $\phi$ 表示惯性系方位角，用 $\psi=\phi-\omega_1t+\psi_0$ 表示磁场图样中的相位。磁场取 $\mathbf B=-B\hat{\mathbf z}$，$+z$ 指向北极，$q$ 为带符号电荷。

![图2-1 北极视角下颗粒逆时针运行，南向磁场指向纸内。](../figures/question-02.png)

<!-- question-end -->

## 一、题型定位

本题连用圆轨道动力学、磁力矩、法拉第电磁感应和周期平均功率。最容易混淆的是三种频率：公转频率 $\omega_0$、磁场图样的转动频率 $\omega_1$，以及颗粒实际遇到图样的频率 $\omega_0-\omega_1$。

前四问的磁场在空间均匀，最后两问则有方位角变化。均匀场中的角动量修正可以直接推导，不能不加判断地沿用到任意非轴对称场。最后的共振条件从电场做功求出，而不是仅凭“两个周期比为整数”判定。

## 二、知识点

在柱坐标中，速度为

$$
\mathbf v=\dot\rho\,\hat{\mathbf r}
+\rho\dot\phi\,\hat{\boldsymbol\phi}.
$$

因 $\mathbf B=-B\hat{\mathbf z}$，磁力的两分量为

$$
F_{B,r}=-qB\rho\dot\phi,\qquad
F_{B,\phi}=qB\dot\rho.
$$

机械角动量的轴向分量为 $L=m\rho^2\dot\phi$，转动方程是

$$
\dot L=\rho F_\phi.
$$

磁力始终与速度垂直，因此 $\mathbf F_B\cdot\mathbf v=0$。机械角动量可以变化而动能不由磁力直接增加，二者没有矛盾。能量增长必须通过电场功率 $q\mathbf E\cdot\mathbf v$ 来判断。

均匀南向磁场变化时，沿半径为 $\rho$ 的圆周使用法拉第定律。以逆时针为正向，其磁通量为 $-\pi\rho^2B$，从而有

$$
E_\phi=\frac\rho2\dot B.
$$

这里用于求场的圆周是固定的空间回路，不能把颗粒轨道半径的变化误算成感生电场的一部分。

## 三、物理图像

正电颗粒逆时针绕行时，南向磁场给出向内磁力。若公转角速度仍等于天体自转角速度，磁力分担一部分向心力，颗粒可在更大的半径保持同步。负电颗粒的磁力向外，同步半径则减小。

径向速度会产生切向磁力，因而径向扰动伴随机械角动量交换。均匀场中把与磁通有关的一项并入角动量，可以得到守恒量。若场强还随时间变化，切向感生电场恰好补上这个守恒量所需的时间导数。

最后两问的旋转图样则产生随方位变化的径向电场。颗粒向外运动时若电场也推动其向外，向内运动时电场也推动其向内，一个周期就能获得净能量。能否做到这一点取决于频率和相位，两者缺一不可。

![图2-2 惯性方位角phi与图样相位psi不同，遇场频率是两角速度之差。](../figures/phase-02.png)

## 四、解题入口

第（1）、（2）问先在径向列向心力方程，并将 $\omega_c=qB/m$ 作为带符号的小参数。第（3）问求 $\dot L$，把它识别成一个全时间导数。第（4）问先求感生电场，再把磁力矩与电力矩相加。

第（5）问必须区分空间固定点处的 $\partial\mathbf B/\partial t$ 与颗粒沿轨道遇到的 $d\mathbf B/dt$。法拉第定律使用前者。第（6）问再把 $\psi(t)\simeq(\omega_0-\omega_1)t+\psi_0$ 代入电场，与径向速度相乘。

这个顺序还有一项核对作用：如果最终共振功率与初相位无关，或者由磁场直接做功得到，就应返回检查速度、电场方向与相位定义。

## 五、解析

（1）纯引力同步半径。

圆轨道角速度等于 $\omega_0$ 时，

$$
\frac{GMm}{r_0^2}=m\omega_0^2r_0,
\qquad
\boxed{r_0=\left(\frac{GM}{\omega_0^2}\right)^{1/3}}.
$$

质量 $m$ 消去，因为引力和惯性均与颗粒质量成正比。$GM$ 的量纲为长度三次除以时间平方，表达式开立方后确为长度。

（2）弱磁场中的同步半径。

本小问按题设只计引力和磁力，不另加恒定的共转电场。径向平衡为

$$
\frac{GMm}{r_1^2}+qB\omega_0r_1
=m\omega_0^2r_1.
$$

于是

$$
r_1^3=\frac{GM}{\omega_0(\omega_0-\omega_c)},
\qquad \omega_c=\frac{qB}{m}.
$$

在 $|\omega_c/\omega_0|\ll1$ 时展开，

$$
\frac{r_1}{r_0}
=\left(1-\frac{\omega_c}{\omega_0}\right)^{-1/3}
=1+\frac{\omega_c}{3\omega_0}
+O\!\left(\frac{\omega_c^2}{\omega_0^2}\right).
$$

一阶结果为

$$
\boxed{\frac{r_1-r_0}{r_0}=\frac{qB}{3m\omega_0}}.
$$

这也说明为什么不能把磁力项一律写成正数：负电荷给出的偏移方向与正电荷相反。精确圆轨道表达式还要求 $\omega_0(\omega_0-\omega_c)>0$；弱场假设自动满足它。

（3）恒定均匀场中的角动量修正。

引力没有轴向力矩，只有径向运动产生的切向磁力有力矩，故

$$
\dot L=qB\rho\dot\rho
=\frac{d}{dt}\left(\frac{qB\rho^2}{2}\right).
$$

因此

$$
\boxed{L_r=-\frac{qB\rho^2}{2}},\qquad
\boxed{J=L-\frac{qB\rho^2}{2}=\text{常量}}.
$$

向外运动的正电荷受到逆时针切向磁力，机械角动量增大，而负号修正项减小。两者之和保持不变，这个方向检查可独立确定修正项的符号。

![图2-3 径向速度产生切向磁力，机械角动量与磁通修正项相互补偿。](../figures/momentum-02.png)

（4）随时间变化的均匀场。

电力矩为 $q\rho E_\phi=q\rho^2\dot B/2$。将它与磁力矩合并，得到

$$
\dot L=qB\rho\dot\rho+\frac q2\rho^2\dot B
=\frac q2\frac{d}{dt}(B\rho^2).
$$

因此修正项仍有同样形式，只须把场强换为即时值：

$$
\boxed{L'_r=-\frac{qB(t)\rho(t)^2}{2}},
\qquad J=m\rho^2\dot\phi-\frac q2B(t)\rho^2.
$$

角速度的关系式为

$$
\boxed{\dot\phi(t)=\frac{J}{m\rho(t)^2}
+\frac{qB(t)}{2m}}.
$$

若初始半径、角速度、场强分别为 $\rho_i,\omega_i,B_i$，则 $J=m\rho_i^2\omega_i-qB_i\rho_i^2/2$，可直接代入。不知道初始条件时应保留积分常量，不能擅自令 $J=0$。

场随时间变化时机械能通常不守恒，因为感生电场会做功；上面的轴向守恒量依赖空间轴对称性，其守恒不意味着机械能也守恒。

（5）旋转图样中的磁场变化。

写南向场强为

$$
B(\phi,t)=B_0-\Delta B\cos\psi,
\quad\psi=\phi-\omega_1t+\psi_0.
$$

固定 $\phi$ 求时间偏导，得到

$$
\frac{\partial B}{\partial t}
=-\omega_1\Delta B\sin\psi,
\qquad
\frac{\partial B_z}{\partial t}
=+\omega_1\Delta B\sin\psi.
$$

对于题给的径向形式 $E_r=E_0\cos\psi$，其旋度为

$$
(\boldsymbol\nabla\times\mathbf E)_z
=-\frac1\rho\frac{\partial E_r}{\partial\phi}
=\frac{E_0}{\rho}\sin\psi.
$$

用 $\boldsymbol\nabla\times\mathbf E=-\partial\mathbf B/\partial t$，在 $\rho=r_1$ 附近得到一个相容的特解

$$
\boxed{E_0=-r_1\omega_1\Delta B}.
$$

若 $\omega_1\Delta B>0$，$\psi=0$ 处电场向内，$\psi=\pi$ 处向外；$\psi=\pi/2,3\pi/2$ 处径向电场为零，磁场时间变化率的绝对值最大。法拉第定律只约束电场旋度，还可以叠加无旋电场；本式采用题给的径向电场模型，而不是宣称所有边界条件下电场都唯一如此。

![图2-4 图样相位决定固定点的磁场变化率和径向电场方向。](../figures/induction-02.png)

（6）写平均功率并选一个共振。

径向速度为

$$
\dot\rho=-\alpha r_1\omega_0\sin\omega_0t.
$$

令 $T=2\pi/\omega_0$，在一阶振动近似下，

$$
\boxed{\overline P
=-\frac{q\alpha r_1\omega_0E_0}{T}
\int_0^T\sin\omega_0t\,
\cos[(\omega_0-\omega_1)t+\psi_0],dt}.
$$

一般频率下，单个周期的平均不一定等于零，但随后各周期的相位会漂移，不能据一次正功就认定长期持续加速。要得到不会漂移的共振项，可令

$$
|\omega_0-\omega_1|=\omega_0.
$$

两种形式为 $\omega_1=0$ 或 $\omega_1=2\omega_0$。前者在本旋转感应模型中 $E_0=0$，没有感生电场供能。一个非平凡解为

$$
\boxed{\omega_1=2\omega_0}.
$$

此时

$$
\cos[-\omega_0t+\psi_0]
=\cos\omega_0t\cos\psi_0+\sin\omega_0t\sin\psi_0,
$$

所以共振平均功率为

$$
\boxed{\overline P
=-\frac12q\alpha r_1\omega_0E_0\sin\psi_0}.
$$

必须同时取 $qE_0\sin\psi_0<0$，才能吸收能量。例如 $q>0,\Delta B>0,\omega_1>0$ 时 $E_0<0$，选 $\psi_0=\pi/2$ 得正功率；选 $\psi_0=0$ 则平均功率仍为零。频率条件本身不保证能量增长。

（7）检查振动频率的近似。

恒定均匀场的径向有效势可写为

$$
U_{\mathrm{eff}}(\rho)=\frac{J^2}{2m\rho^2}
+\frac{qBJ}{2m}+\frac{q^2B^2\rho^2}{8m}
-\frac{GMm}{\rho}.
$$

在角速度为 $\omega_0$ 的圆轨道附近，二阶展开给出

$$
\kappa^2=\frac1mU_{\mathrm{eff}}''(r_1)
=\omega_0^2-\omega_0\omega_c+\omega_c^2.
$$

弱磁场时 $\kappa\simeq\omega_0$，与题设的径向振动频率一致。若保留这个修正，匹配条件改为 $|\omega_0-\omega_1|=\kappa$。这说明 $2\omega_0$ 属于题设近似，而不是任意真实天体磁场的统一共振比。

![图2-5 共振下只有与速度同相的电场分量贡献正的周期平均功率。](../figures/power-02.png)

（8）结果的适用范围。

正平均功率表示振动能量可在共振近似内持续增长，颗粒会逐渐离开初始小振动轨道。要证明最终逃逸，还需考虑离开线性区后频率的改变、场的空间范围以及能量来源；题设没有给出这些信息，不能由一条频率等式直接推出无条件逃逸。

本题明确可求的是同步半径修正、均匀场的轴向守恒量，以及一种可供能的旋转感应共振条件。真实图样中若加入其他方位谐波，其遇场频率也相应改变，须重新做功率匹配。

（9）一般遇场频率的长期功率检查。

记 $\Omega=\omega_0-\omega_1$，用积化和差公式，做功积分中的函数为

$$
\sin\omega_0t\cos(\Omega t+\psi_0)
=\frac12\sin[(\omega_0+\Omega)t+\psi_0]
+\frac12\sin[(\omega_0-\Omega)t-\psi_0].
$$

若两个组合频率均非零，积分到长时间 $\tau$ 后，每项的积分都是有界的余弦差，再除以 $\tau$，长期平均趋于零。一次公转周期中的正功可由后续周期的负功抵消。

当 $\Omega=-\omega_0$，第一项变成常数 $\sin\psi_0/2$，正是 $\omega_1=2\omega_0$ 的共振项。当 $\Omega=+\omega_0$，第二项变成 $-\sin\psi_0/2$，但对应本模型静止图样，没有旋转感生电场。

这个长期积分说明共振筛选的依据。若 $\omega_1$ 仅接近而未等于 $2\omega_0$，相位缓慢漂移，出现拍频式能量交换。在线性模型中能暂时增长，但不能把这种暂时增长当成无限时长的恒定正功率。

## 六、关键洞察

磁力不做功，但它能传递角动量；感生电场能做功。把两种作用分别写成力矩和功率，角动量修正与能量增长就各有清楚的来源。

“场随天体转动”是关于空间图样的陈述。颗粒沿轨道看到的变化频率由相对角速度决定，而法拉第定律用固定空间点的时间偏导。混用这两个导数会把电场振幅错误地写成含 $\omega_0-\omega_1$ 的量。

共振中频率决定能否形成稳定的平均项，相位决定平均项的正负。图样与颗粒的初始相位必须写入模型。

## 七、易错点

在第（2）问把南向磁场误写成 $+B\hat{\mathbf z}$，会同时反转轨道偏移和角动量修正。应先规定轴向，再使用右手定则。

时间变化的均匀场不能只保留磁力矩。漏掉感生电场时，$J$ 的导数会多出 $-q\rho^2\dot B/2$，守恒量随即失效。

把 $dB/dt$ 沿颗粒的值直接放入法拉第定律，会错配场的旋度。另一方面，算功率时若不用沿轨道的相位，就会漏掉相对频率。

在相位为零的共振示例中宣布正功率，也是不成立的。$\sin\omega_0t\cos\omega_0t$ 的整周期平均为零。

## 八、课堂讲解建议

教师先让学生用速度两个分量逐项计算 $\mathbf v\times\mathbf B$，保留磁场负号。板书并排写 $\dot L$ 与 $q\mathbf E\cdot\mathbf v$，强调它们检验不同的守恒关系。

课堂讨论采用两次相位选择：$\psi_0=0$ 和 $\pi/2$。让学生画出电场和径向速度随时间的曲线，观察同一频率匹配为何可以给出零功或正功，再回到平均功率积分。

## 九、变式训练

<!-- KEEP_TOGETHER_START -->

变式一：颗粒为负电荷，保持同向同步公转，其一阶半径偏差方向如何？

解：以北向 $+z$、南向磁场 $-B\hat{\mathbf z}$ 为约定，同向速度的 $\mathbf v\times\mathbf B$ 向内，但乘负电荷后磁力向外。径向平衡为

$$
\frac{GMm}{r_1^2}+qB\omega_0r_1=m\omega_0^2r_1.
$$

同样展开得到

$$
\frac{r_1-r_0}{r_0}=\frac{qB}{3m\omega_0}<0.
$$

保持同一角速度时，向外磁力要求更强引力，因此轨道半径减小。这个力学判断与代数结果同向，也说明公式中的 $q$ 必须保留符号。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式二：恒定均匀磁场中，颗粒半径由 $a$ 变为 $b$，机械角动量如何变化？磁力是否做功？

解：由 $J=L-qB\rho^2/2$ 守恒，两状态相减，得到

$$
L_b-L_a=\frac{qB}{2}(b^2-a^2).
$$

正电荷向外移动时机械角动量增大，与切向磁力矩一致。不过磁力的功率为

$$
P_B=q(\mathbf v\times\mathbf B)\cdot\mathbf v=0.
$$

所以角动量变化不等于磁场向颗粒提供能量。径向与切向动能可以在力学约束中重新分配；若同时有引力势能变化，也须一起纳入机械能检查。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式三：$\omega_1=2\omega_0$，分别取 $\psi_0=0$ 和 $\psi_0=\pi/2$，比较周期平均功率。

解：相对图样相位为 $\psi=-\omega_0t+\psi_0$，与径向速度相乘后，只有平方正弦项保留整周期平均。因而

$$
\overline P=-\frac12q\alpha r_1\omega_0E_0\sin\psi_0.
$$

相位为零时平均功率为零。相位为 $\pi/2$ 时，

$$
\overline P=-\frac12q\alpha r_1\omega_0E_0.
$$

若 $q>0$、图样正转且 $\Delta B>0$，$E_0=-r_1\omega_1\Delta B<0$，第二个状态吸收能量。两状态频率完全相同，结果差异全部来自相位。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式四：径向振动频率改为 $\kappa$，给出一个正转图样的共振条件，并求弱磁场下的一阶修正。

解：遇场频率仍为 $\omega_0-\omega_1$，需满足

$$
|\omega_0-\omega_1|=\kappa.
$$

可取 $\omega_1=\omega_0+\kappa$。均匀背景磁场给出 $\kappa^2=\omega_0^2-\omega_0\omega_c+\omega_c^2$，故一阶为

$$
\kappa\simeq\omega_0-\frac{\omega_c}{2},
\qquad\omega_1\simeq2\omega_0-\frac{\omega_c}{2}.
$$

这个频率匹配仍须配合使电场与径向速度做正功的相位。它只适用于小振动与弱场条件，不能在振幅增长很大后继续无条件使用。

<!-- KEEP_TOGETHER_END -->

<!-- question-complete -->
