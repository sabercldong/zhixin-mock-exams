# 第2题

<!-- question-start -->

一个很长的薄壁圆柱筒，半径为 $r$，表面固定有面密度为 $\sigma$ 的电荷。筒壁与电荷的总面质量密度为 $\mu$。圆筒绕中心轴以角速度 $\omega$ 匀速转动，筒壁单位长度能够承受的最大张力为 $\lambda$。

（1）同时考虑牛顿第二定律、静电作用和洛伦兹力，求 $\omega$ 的最大值。

（2）在 $\omega r\ll c$ 的情况下，通过计算说明是否需要考虑洛伦兹力。$c$ 为真空光速。

![图2-1 带电薄壁圆筒的空间结构与转动方向。](../figures/question-02.png){width=58%}

<!-- question-end -->

## 一、题型定位

这是带电旋转薄膜的环向强度问题。静电排斥、环向电流的磁自作用以及维持圆周运动所需的向心合力，共同决定筒壁的张力。先求场，再确定哪些场真正作用于壁面电荷，最后用一个壁带的受力方程求张力，不能直接用“总质量乘向心加速度”代替局部强度分析。

图2-1中轴向为 $z$，$r$ 是筒半径而非壁厚。题目中的 $\mu$ 是包括电荷在内的面质量密度，$\lambda$ 是跨过轴向切边的环向张力上限，按每单位轴向长度计量；两者都不是整个圆筒的质量或总拉力。磁导率另记作 $\mu_0$，不要与 $\mu$ 混淆。

## 二、知识点

圆柱对称电场与高斯定律；面电流密度与安培环路定律；薄壁表面内外场的跃变及剔除自场后的平均场；洛伦兹力的叉乘方向；薄膜环向张力与微元几何；惯性系中的向心加速度；强度约束与实根筛选；近似量级和临界值误差的区别。

使用 SI 制，真空介电常数为 $\varepsilon_0$，真空磁导率为 $\mu_0$，满足 $\varepsilon_0\mu_0=1/c^2$。面电荷密度 $\sigma$ 的单位为 $\mathrm{C\,m^{-2}}$，面质量密度 $\mu$ 的单位为 $\mathrm{kg\,m^{-2}}$，张力 $\lambda$ 的单位为 $\mathrm{N\,m^{-1}}$。电磁压力的单位则是 $\mathrm{N\,m^{-2}}$，比张力多一个长度分母。

## 三、物理图像

固定在壁面上的电荷随筒旋转，形成沿圆周方向的连续面电流。长圆筒的电场在内部为零、外部沿径向；磁场在内部沿轴向、外部在长筒近似下为零。这不表示壁面电荷完全不受某一种力：壁面处不能任选“内侧为零”或“外侧非零”的单侧场，而应取排除了局部电荷或电流自身贡献后的场。

以 $\sigma>0$、$\omega>0$ 为例，从 $+z$ 方向看电流逆时针，内部磁场朝 $+z$。局部速度沿 $\mathbf e_\varphi$，而 $\mathbf e_\varphi\times\mathbf e_z=\mathbf e_r$，所以磁力与静电力都指向筒外。使壁带向内加速的是两边张力的径向合力，不是磁力。轴向电流导线的磁收缩图像不能直接移植到环向电流圆筒上。

## 四、解题入口

把壁面受到的电力、磁力先写成单位面积的向外压力 $p_E,p_B$，再取轴向长 $h$、圆周中心角 $\mathrm d\varphi$ 的小壁带。它的面积为 $r h\,\mathrm d\varphi$，两端拉力大小各为 $T h$，径向合力约为 $-T h\,\mathrm d\varphi$。这里 $T$ 表示实际环向张力，最后才令 $T=\lambda$。

为使小角近似的来源可见，解析还将用中心角为 $2\alpha$ 的有限壁带做一次精确积分。两种取法得到同一张力方程。第二问先算磁力与电力之比，再区分“总自作用力的主阶近似”与“最大角速度的相对精度”，避免在临界强度问题中删掉虽小却影响裕量的项。

## 五、解析

**第1步：明确模型、研究对象与正方向。**

采用题目所要求的牛顿薄壁模型。将圆筒中段近似为无限长筒，忽略端部场和壁厚引起的修正；不施加额外电磁场。电荷固定在表面，不假定电荷可以在导体中任意重新分布。半径 $r$、面密度 $\sigma,\mu$ 均取稳态转动时给定的值，且 $r>0,\mu>0$。

取径向向外为 $\mathbf e_r$，沿正转向的切向为 $\mathbf e_\varphi$，轴向为 $\mathbf e_z$。先取 $\omega\ge0$ 求角速度大小；反向旋转时用 $|\omega|$ 表示同一强度界限。局部运动量为

$$
\mathbf v=\omega r\,\mathbf e_\varphi,
\qquad
\mathbf a=-\omega^2 r\,\mathbf e_r.
$$

实际张力记作 $T$，安全条件是 $T\le\lambda$。轴向长为 $h$ 的切边所承受的总拉力为 $T h$；不能把单位长度张力 $T$ 直接当成牛顿为单位的总力。由于 $\mu$ 已含电荷质量，写质量微元时不再另加一份电荷质量。

**第2步：由高斯定律求圆筒两侧电场。**

用 $s$ 表示观察点到轴的距离，避免与固定的筒半径 $r$ 混用。取半径 $s$、长度 $h$ 的同轴高斯柱面。由圆柱对称性，电场只有径向分量，在侧面大小相同；端面法向沿轴，电场与之垂直，故端面通量为零。

对于 $s<r$，高斯面没有包围壁面电荷：

$$
E(s)\,2\pi s h=0,
\qquad E(s)=0.
$$

对于 $s>r$，包围电荷量为 $\sigma\,2\pi r h$，因而

$$
\begin{aligned}
E(s)\,2\pi s h
&=\frac{\sigma\,2\pi r h}{\varepsilon_0},\\
\mathbf E(s)&=\frac{\sigma r}{\varepsilon_0s}\,\mathbf e_r.
\end{aligned}
$$

这里 $E(s)$ 可作为有符号径向分量，负电荷时方向自动反转。趋近壁面的两侧极限为

$$
\mathbf E_{\text{内}}=0,
\qquad
\mathbf E_{\text{外}}=\frac{\sigma}{\varepsilon_0}\,\mathbf e_r.
$$

图2-2左侧用径向箭头表示外场，用筒内的零场区域与之区分；右侧将用于下一步的环向电流及轴向磁场。

![图2-2 长圆筒的径向电场、环向面电流与轴向磁场。](../figures/fields-02.png){width=92%}

**第3步：从通过切边的电荷求面电流密度。**

沿轴向取一条长 $h$ 的固定观察线。在时间 $\mathrm dt$ 内，电荷沿圆周移动距离 $v\,\mathrm dt=\omega r\,\mathrm dt$。跨过这条线的壁面带面积和电荷分别为

$$
\begin{aligned}
\mathrm dS_{\text{跨}}
&=h\omega r\,\mathrm dt,\\
\mathrm dq_{\text{跨}}
&=\sigma h\omega r\,\mathrm dt.
\end{aligned}
$$

跨线电流是 $\mathrm dq_{\text{跨}}/\mathrm dt$，再除以切边长度 $h$，得到面电流密度

$$
\boxed{\mathbf K=\sigma\omega r\,\mathbf e_\varphi}.
$$

$K$ 的单位为 $\mathrm{A\,m^{-1}}$，不是 $\mathrm A$；截取轴向宽度 $\mathrm dz$，这一圈电流大小为 $K\,\mathrm dz$。图2-2中的环向箭头正表示 $\mathbf K$，它与壁面速度平行；若 $\sigma<0$，常规电流方向与速度相反。

**第4步：由安培环路定律求内外磁场。**

均匀环向电流相当于连续分布的长螺线管电流。由轴向与转动对称性，磁场沿轴向。在不穿过壁面电流的矩形环路上应用安培定律，得到同一侧的轴向场不随径向位置改变。无外加场，并要求远处磁场为零，便有长筒近似下的外场 $\mathbf B_{\text{外}}=0$。

再取一条跨过壁面的矩形环路，长边长 $h$、平行于轴。环路法向选成使穿过环面的面电流为正，故

$$
\begin{aligned}
(B_{\text{内}}-B_{\text{外}})h
&=\mu_0 K h,\\
\mathbf B_{\text{内}}
&=\mu_0\sigma\omega r\,\mathbf e_z,\\
\mathbf B_{\text{外}}&=0.
\end{aligned}
$$

有符号的 $\sigma\omega$ 决定磁场朝向。图2-2右侧的 $\odot$ 对应正电荷按图示逆时针转动时朝向观察者的轴向场；它不是径向磁场，也不是从壁面向外的磁力箭头。

**第5步：剔除局部自场，说明两个二分之一因子。**

洛伦兹力公式中的场必须由其余电荷、电流产生。理想薄壁总场在表面不连续，不能把壁面外场直接乘以壁面电荷，也不能因为内场为零就认为电力为零。将很小壁片局部视作平面，记其自身在两侧产生的场为自场，其余来源的场在该局部两侧连续。

电荷面自场在两侧分别为 $+\sigma\mathbf e_r/(2\varepsilon_0)$ 和 $-\sigma\mathbf e_r/(2\varepsilon_0)$。于是

$$
\begin{aligned}
\mathbf E_{\text{外}}
&=\mathbf E_{\text{其余}}
+\frac{\sigma}{2\varepsilon_0}\mathbf e_r,\\
\mathbf E_{\text{内}}
&=\mathbf E_{\text{其余}}
-\frac{\sigma}{2\varepsilon_0}\mathbf e_r.
\end{aligned}
$$

两式相加消去局部自场：

$$
\boxed{\mathbf E_{\text{有效}}
=\mathbf E_{\text{其余}}
=\frac{\mathbf E_{\text{外}}+\mathbf E_{\text{内}}}{2}
=\frac{\sigma}{2\varepsilon_0}\mathbf e_r}.
$$

局部平面电流片的自场也在两侧反向。对图示 $\mathbf K=K\mathbf e_\varphi$，其内侧自场朝 $+z$，外侧自场朝 $-z$，因此

$$
\begin{aligned}
\mathbf B_{\text{内}}
&=\mathbf B_{\text{其余}}+\frac{\mu_0K}{2}\mathbf e_z,\\
\mathbf B_{\text{外}}
&=\mathbf B_{\text{其余}}-\frac{\mu_0K}{2}\mathbf e_z,\\
\mathbf B_{\text{有效}}
&=\frac{\mathbf B_{\text{内}}+\mathbf B_{\text{外}}}{2}
=\frac{\mu_0\sigma\omega r}{2}\mathbf e_z.
\end{aligned}
$$

图2-3把电、磁两种场的单侧总场放在壁面两边。计算力时使用上式的平均场；“平均”不是把实际壁面电荷量再除以二，电荷仍是 $\mathrm dq=\sigma\,\mathrm dS$。

![图2-3 壁面两侧的总场与剔除局部自场后的有效场。](../figures/mean-02.png){width=92%}

**第6步：分别计算静电、磁自作用的大小与方向。**

面积 $\mathrm dS$ 的壁片带电量为 $\mathrm dq=\sigma\,\mathrm dS$，它受到的电力为

$$
\begin{aligned}
\mathrm d\mathbf F_E
&=\mathrm dq\,\mathbf E_{\text{有效}}\\
&=\sigma\,\mathrm dS\,
\frac{\sigma}{2\varepsilon_0}\mathbf e_r\\
&=p_E\,\mathrm dS\,\mathbf e_r,
\qquad
p_E=\frac{\sigma^2}{2\varepsilon_0}.
\end{aligned}
$$

磁力按叉乘计算，而不是仅根据“电流之间吸引”猜方向：

$$
\begin{aligned}
\mathrm d\mathbf F_B
&=\mathrm dq\,\mathbf v\times\mathbf B_{\text{有效}}\\
&=\sigma\,\mathrm dS\,
(\omega r\,\mathbf e_\varphi)
\times\left(\frac{\mu_0\sigma\omega r}{2}\mathbf e_z\right)\\
&=\frac{\mu_0\sigma^2\omega^2r^2}{2}
\,\mathrm dS\,\mathbf e_r\\
&=p_B\,\mathrm dS\,\mathbf e_r,
\qquad
p_B=\frac{\mu_0\sigma^2\omega^2r^2}{2}.
\end{aligned}
$$

两种压力均非负，均使圆筒向外胀。反转旋转方向时，$\mathbf v$ 与 $\mathbf B$ 同时反转，叉乘不变；反转电荷符号时，$\mathrm dq$ 与 $\mathbf B$ 同时反转，磁力也不变。电力、磁力只依赖 $\sigma^2$，符合这一符号检验。

**第7步：建立壁带几何，求两边张力的径向合力。**

在截面上以壁带中央径向为 $+x$，中央切向为 $+y$。取中心角 $2\alpha$ 的壁带，$0<\alpha<\pi/2$，轴向长仍为 $h$。两个切边在极角 $\pm\alpha$，从其余筒壁传来的拉力沿各端点切线，大小各为 $T h$。图2-4中的两个蓝色箭头是切边实际拉力，红色箭头代表分布在壁带上的向外压力；图上没有额外添加离心力。

![图2-4 有限角壁带的环向张力与向外电磁压力。](../figures/sector-02.png){width=84%}

上端拉力指向左上，下端拉力指向左下。把图中切线方向分解到同一组坐标：

$$
\begin{aligned}
\mathbf F_{T,+}
&=T h(-\sin\alpha\,\mathbf e_x+\cos\alpha\,\mathbf e_y),\\
\mathbf F_{T,-}
&=T h(-\sin\alpha\,\mathbf e_x-\cos\alpha\,\mathbf e_y).
\end{aligned}
$$

切向分量抵消，径向分量相加：

$$
\boxed{\mathbf F_T=-2T h\sin\alpha\,\mathbf e_x}.
$$

不是 $-2T h\cos\alpha\,\mathbf e_x$。当 $\alpha$ 趋于零，两条切线近乎平行且两边拉力近乎反向，向内合力应随壁带宽度趋零；$\sin\alpha$ 才符合此极限。

**第8步：对压力与真实加速度分别积分。**

壁带中的位置角用 $\psi$ 表示，$-\alpha\le\psi\le\alpha$。其面积微元为 $\mathrm dS=r h\,\mathrm d\psi$，径向单位矢量为

$$
\mathbf e_r(\psi)=\cos\psi\,\mathbf e_x+\sin\psi\,\mathbf e_y.
$$

令 $p=p_E+p_B$。压力大小相同，但方向随 $\psi$ 改变，因此不能把有限壁带全部面积直接乘以中央方向。精确积分：

$$
\begin{aligned}
\mathbf F_p
&=\int_{-\alpha}^{\alpha}p\,r h\,\mathbf e_r(\psi)\,\mathrm d\psi\\
&=p r h\left[
\left(\int_{-\alpha}^{\alpha}\cos\psi\,\mathrm d\psi\right)\mathbf e_x
+\left(\int_{-\alpha}^{\alpha}\sin\psi\,\mathrm d\psi\right)\mathbf e_y
\right]\\
&=2p r h\sin\alpha\,\mathbf e_x.
\end{aligned}
$$

这里使用奇函数对称区间积分为零，以及 $\int_{-\alpha}^{\alpha}\cos\psi\,\mathrm d\psi=2\sin\alpha$。

同一位置处 $\mathrm dm=\mu r h\,\mathrm d\psi$，真实加速度是 $-\omega^2r\,\mathbf e_r(\psi)$。牛顿第二定律右边必须用各质量微元加速度的和：

$$
\begin{aligned}
\int\mathbf a\,\mathrm dm
&=\int_{-\alpha}^{\alpha}
(-\omega^2r\,\mathbf e_r(\psi))
(\mu r h\,\mathrm d\psi)\\
&=-2\mu\omega^2r^2 h\sin\alpha\,\mathbf e_x.
\end{aligned}
$$

电磁合力向外，张力合力向内，真实合加速度向内，三者的方向现已在同一个 $x$ 正方向下确定。

**第9步：列牛顿方程，逐项求实际环向张力。**

将第7、8步代入 $\mathbf F_T+\mathbf F_p=\int\mathbf a\,\mathrm dm$，取 $x$ 分量：

$$
-2T h\sin\alpha+2(p_E+p_B)r h\sin\alpha
=-2\mu\omega^2r^2h\sin\alpha.
$$

由于 $h>0,\sin\alpha>0$，除以共同因子 $2h\sin\alpha$：

$$
\begin{aligned}
-T+r(p_E+p_B)&=-\mu\omega^2r^2,\\
T&=\mu\omega^2r^2+r(p_E+p_B),\\
T&=\mu\omega^2r^2
+\frac{r\sigma^2}{2\varepsilon_0}
+\frac{\mu_0\sigma^2\omega^2r^3}{2}.
\end{aligned}
$$

最终

$$
\boxed{
T=\frac{r\sigma^2}{2\varepsilon_0}
+r^2\left(\mu+\frac{\mu_0\sigma^2r}{2}\right)\omega^2}.
$$

三个项依次是静电已占用的张力、向心运动的张力需求，以及磁自作用追加的张力。磁力虽不是向心力，仍影响强度上限：它向外，所以必须再增加向内张力来抵消它。

有限壁带结果与 $\alpha$ 无关。取 $2\alpha=\mathrm d\varphi$，使用 $\sin\alpha\simeq\alpha$，便恢复微元取法：

$$
\begin{aligned}
\mathrm dS&=r h\,\mathrm d\varphi,\\
\mathrm dm&=\mu r h\,\mathrm d\varphi,\\
(p_E+p_B)\mathrm dS-T h\,\mathrm d\varphi
&=-\mathrm dm\,\omega^2r.
\end{aligned}
$$

再除以 $h\,\mathrm d\varphi$，仍得到同一张力式。这个极限明确解释了两边总拉力为何不是 $2T h$ 全部作为向心力。

**第10步：施加强度条件，求最大角速度并筛选可行情形。**

定义静止时的环向张力及随 $\omega^2$ 增加的系数：

$$
T_0=\frac{r\sigma^2}{2\varepsilon_0},
\qquad
A_T=r^2\left(\mu+\frac{\mu_0\sigma^2r}{2}\right)>0.
$$

于是 $T=T_0+A_T\omega^2$。图2-5以 $\Omega=\omega^2$ 为横轴；直线截距是 $T_0$，斜率是 $A_T$，与 $T=\lambda$ 的交点才给出强度边界。

![图2-5 静电张力、转动张力增量与强度边界。](../figures/strength-02.png){width=76%}

若 $\lambda>T_0$，解不等式并取非负角速度：

$$
\begin{aligned}
T_0+A_T\omega^2&\le\lambda,\\
\omega^2&\le
\frac{\lambda-r\sigma^2/(2\varepsilon_0)}
{r^2(\mu+\mu_0\sigma^2r/2)},\\
\omega_{\max}
&=\frac1r\sqrt{
\frac{\lambda-r\sigma^2/(2\varepsilon_0)}
{\mu+\mu_0\sigma^2r/2}}\\
&=\boxed{\frac1r
\sqrt{\frac{2\lambda-r\sigma^2/\varepsilon_0}
{2\mu+\mu_0r\sigma^2}}}.
\end{aligned}
$$

最后一行同时把分子、分母乘以 $2$，并未多加一个二分之一。

若 $\lambda=T_0$，只有 $\omega=0$ 位于强度边界，任何非零转动都会超过它。若 $\lambda<T_0$，连静止圆筒也无法承受给定电荷的排斥，不存在本模型中的可行稳态；不能把负的根号内部继续解释成某个“最大转速”。若材料在达到最大张力时即发生破坏，严格安全范围应取 $T<\lambda$，上式给的是极限值。

<!-- KEEP_TOGETHER_START -->

**第11步：计算低速时磁力与静电力的比。**

对 $\sigma\ne0$，同一壁片面积相同，故力比等于压力比：

$$
\begin{aligned}
\frac{\mathrm dF_B}{\mathrm dF_E}
&=\frac{p_B}{p_E}\\
&=\frac{\mu_0\sigma^2\omega^2r^2/2}
{\sigma^2/(2\varepsilon_0)}\\
&=\mu_0\varepsilon_0\,\omega^2r^2\\
&=\boxed{\left(\frac{\omega r}{c}\right)^2}.
\end{aligned}
$$

<!-- KEEP_TOGETHER_END -->

所以 $\omega r\ll c$ 时，磁自力相对于静电自力是二阶小量。若只求电磁总力的低速主阶，可取

$$
p_E+p_B
=p_E\left[1+\left(\frac{\omega r}{c}\right)^2\right]
\simeq p_E.
$$

这是低速时通常可以忽略磁力的直接计算依据。$\sigma=0$ 时两种自力都为零，不把 $0/0$ 当作力比；此时无需任何电磁修正。

**第12步：说明忽略磁力对临界角速度的精度条件。**

总力中的小修正，不一定是临界转速中的小相对修正，因为静电已经占去张力 $T_0$，用于转动的裕量是 $\lambda-T_0$。仅忽略磁力求得的角速度为

$$
\omega_{\text{无磁}}^2
=\frac{\lambda-T_0}{\mu r^2},
\qquad \lambda>T_0.
$$

保留磁力时，定义无量纲量

$$
\eta=\frac{\mu_0\sigma^2r}{2\mu}
=\frac{T_0}{\mu c^2}.
$$

由第10步直接逐项比较：

$$
\begin{aligned}
\omega_{\max}^2
&=\frac{\lambda-T_0}{\mu r^2(1+\eta)}
=\frac{\omega_{\text{无磁}}^2}{1+\eta},\\
\frac{\omega_{\text{无磁}}-\omega_{\max}}{\omega_{\max}}
&=\boxed{\sqrt{1+\eta}-1}.
\end{aligned}
$$

因此，若要保证“不计磁力”求得的临界转速相对准确，还需 $\eta\ll1$。当这一条件成立，用二项式展开到一阶：

$$
\omega_{\max}
=\omega_{\text{无磁}}(1+\eta)^{-1/2}
\simeq\omega_{\text{无磁}}\left(1-\frac{\eta}{2}\right).
$$

为看清两种小量的差别，再令静电裕量比例

$$
\delta=\frac{\lambda-T_0}{T_0}>0.
$$

则在强度边界

$$
\begin{aligned}
\left(\frac{\omega_{\max}r}{c}\right)^2
&=\frac{\lambda-T_0}{\mu c^2(1+\eta)}\\
&=\boxed{\frac{\delta\eta}{1+\eta}}.
\end{aligned}
$$

$\delta$ 很小时，边界速率可以远低于 $c$，即使 $\eta$ 并不小。此时磁力相对静电确实很小，却可能与用于转动的张力增量相当。在本题牛顿薄壁模型内，第二问的严谨结论是：低速总电磁力的主阶通常不需磁项；若要求最大角速度的相对精度，则必须同时检查 $\eta$，不能单凭 $\omega r/c$ 删去磁项。

**第13步：检查量纲、退化情形与模型有效性。**

张力式三项应全部为 $\mathrm{N\,m^{-1}}$。其中

$$
\begin{aligned}
[\mu\omega^2r^2]
&=\mathrm{kg\,m^{-2}}\,
\mathrm{s^{-2}}\mathrm{m^2}
=\mathrm{N\,m^{-1}},\\
\left[\frac{r\sigma^2}{\varepsilon_0}\right]
&=[r p_E]=\mathrm{N\,m^{-1}},\\
[\mu_0\sigma^2r]&=\mathrm{kg\,m^{-2}}=[\mu].
\end{aligned}
$$

因此根号内“张力除以面质量密度”的量纲为速率平方，外面的 $1/r$ 使结果成为角速度，单位为 $\mathrm{s^{-1}}$。

不带电时，第10步给出

$$
\boxed{\omega_{\max}=\sqrt{\frac{\lambda}{\mu r^2}}},
$$

与纯机械旋转薄筒相符。静止时，$T=T_0=r p_E$，与薄膜圆筒承受均匀向外压力的关系相符。保持其他参数不变，增加 $|\sigma|$ 同时提高静电截距及磁力斜率，故只能降低可行转速；当 $|\sigma|>\sqrt{2\varepsilon_0\lambda/r}$，静态强度已经失效。

式中的电磁作用采用给定面密度的稳恒场，运动方程采用牛顿质量模型。保留磁力能给出这一模型内的完整结果，但并不使牛顿方程自动变成相对论方程。若计算所得 $\omega_{\max}r$ 不再远小于 $c$，必须重新处理质量、应力和电荷密度的相对论关系；不能把高于或接近光速的形式根当作实际可实现转速。

## 六、关键洞察

本题真正控制张力的是“每单位轴向长度的局部壁带”，不是整个圆筒的合力。完整圆筒的向心加速度矢量在周向积分后相互抵消，总合力可以为零，但每一点仍需向心加速度，壁内张力并不为零。选有限壁带后，压力、张力和惯性项都带有相同的 $2h\sin\alpha$，恰好说明这一局部关系与所选壁带宽度无关。

平均场的二分之一可以用有限厚度模型独立检查。令壁厚为 $t$，中面半径仍为 $r$，内外半径 $a=r-t/2,b=r+t/2$。将相同面电荷均匀铺在薄层内，取体电荷密度 $\rho_q=\sigma/t$。由于 $\int_a^b2\pi s\rho_q\,\mathrm ds=2\pi r\sigma$，单位轴长的总电荷不变。薄层中各处以同一角速度旋转，因此 $J_\varphi(s)=\rho_q\omega s$。

高斯定律与安培定律给出层内场

$$
\begin{aligned}
E(s)&=\frac{\rho_q(s^2-a^2)}{2\varepsilon_0s},\\
B(s)&=\frac{\mu_0\rho_q\omega}{2}(b^2-s^2),
\qquad a\le s\le b.
\end{aligned}
$$

换算为中面单位面积的力时，体积微元须带面积比例 $s/r$，而不能只对 $\rho_q E\,\mathrm ds$ 积分。于是

$$
\begin{aligned}
p_E(t)
&=\int_a^b\rho_qE(s)\frac{s}{r}\,\mathrm ds\\
&=\frac{\rho_q^2}{2\varepsilon_0r}
\int_a^b(s^2-a^2)\,\mathrm ds\\
&=\frac{\rho_q^2}{2\varepsilon_0r}
\left[\frac{s^3}{3}-a^2s\right]_a^b\\
&=\frac{\rho_q^2}{2\varepsilon_0r}
\left(\frac{b^3-a^3}{3}-a^2(b-a)\right).
\end{aligned}
$$

用 $b-a=t$，先因式分解，再代入中面半径：

$$
\begin{aligned}
\frac{b^3-a^3}{3}-a^2(b-a)
&=\frac{b-a}{3}(b^2+ab-2a^2)\\
&=\frac{(b-a)^2(b+2a)}{3}\\
&=t^2\left(r-\frac{t}{6}\right),\\
p_E(t)&=\frac{(\sigma/t)^2}{2\varepsilon_0r}
t^2\left(r-\frac{t}{6}\right)\\
&=\frac{\sigma^2}{2\varepsilon_0}
\left(1-\frac{t}{6r}\right).
\end{aligned}
$$

磁力中速度也随 $s$ 改变，故积分还多出一个 $s$，不能直接照搬电力积分：

$$
\begin{aligned}
p_B(t)
&=\int_a^b\rho_q\omega s B(s)\frac{s}{r}\,\mathrm ds\\
&=\frac{\mu_0\rho_q^2\omega^2}{2r}
\int_a^b s^2(b^2-s^2)\,\mathrm ds\\
&=\frac{\mu_0\rho_q^2\omega^2}{2r}
\left[\frac{b^2s^3}{3}-\frac{s^5}{5}\right]_a^b\\
&=\frac{\mu_0\rho_q^2\omega^2}{2r}
\left[\frac{b^2(b^3-a^3)}{3}-\frac{b^5-a^5}{5}\right].
\end{aligned}
$$

为显示多项式化简，记 $u=t/2$，则 $a=r-u,b=r+u$。二项式展开给出

$$
\begin{aligned}
b^3-a^3&=6r^2u+2u^3,\\
b^5-a^5&=10r^4u+20r^2u^3+2u^5,\\
b^2&=r^2+2ru+u^2.
\end{aligned}
$$

代入后，两项中的一次项抵消：

$$
\begin{aligned}
\frac{b^2(b^3-a^3)}{3}
&=2r^4u+4r^3u^2+\frac83r^2u^3
+\frac43ru^4+\frac23u^5,\\
\frac{b^5-a^5}{5}
&=2r^4u+4r^2u^3+\frac25u^5,\\
\frac{b^2(b^3-a^3)}{3}-\frac{b^5-a^5}{5}
&=4r^3u^2-\frac43r^2u^3
+\frac43ru^4+\frac4{15}u^5\\
&=r^3t^2-\frac{r^2t^3}{6}
+\frac{rt^4}{12}+\frac{t^5}{120},\\
p_B(t)
&=\mu_0\sigma^2\omega^2
\left(\frac{r^2}{2}-\frac{rt}{12}
+\frac{t^2}{24}+\frac{t^3}{240r}\right).
\end{aligned}
$$

令 $t\to0$，分别回到 $p_E=\sigma^2/(2\varepsilon_0)$ 和 $p_B=\mu_0\sigma^2\omega^2r^2/2$。这一路线直接积分层内真实电荷所受的力，独立说明“取单侧场”会多算一倍，并不是为了贴合最终张力式而人为加二分之一。

另一个等价检查是用电磁应力。对局部径向法向，电场沿径向、磁场沿轴向时，应力张量的径向分量为

$$
{\cal T}_{rr}=\frac{\varepsilon_0 E_r^2}{2}
-\frac{B_z^2}{2\mu_0}.
$$

壁外只有径向电场，壁内只有轴向磁场。因此

$$
\begin{aligned}
{\cal T}_{rr}^{\text{外}}-{\cal T}_{rr}^{\text{内}}
&=\frac{\varepsilon_0 E_{\text{外}}^2}{2}
+\frac{B_{\text{内}}^2}{2\mu_0}\\
&=\frac{\sigma^2}{2\varepsilon_0}
+\frac{\mu_0\sigma^2\omega^2r^2}{2}
=p_E+p_B.
\end{aligned}
$$

内场磁压力对筒壁是向外推，不因应力式中 $B_z^2$ 前有负号就变成向内拉力；必须做外侧减内侧。不能单独按“磁场能量越小越好”猜运动方向：在改变半径的虚位移中，还需说明固定的是电流、磁通还是角速度，以及维持电流的系统所做的功。

最后，低速判据比较的是 $p_B/p_E$，临界误差比较的却是 $r p_B$ 与静电之外的张力裕量。不同分母对应不同物理问题。$\eta$ 只是在原张力方程中合并两个 $\omega^2$ 项的无量纲系数，不应未经论证解释成一块额外的实际物质面质量。

## 七、易错点

把 $\lambda$ 当作总拉力，或把 $p_E$ 直接与 $\lambda$ 比较，会少一个长度。应先明确切边长 $h$、总拉力 $T h$，以及压力到张力的换算 $r p$。

用 $\sigma E_{\text{外}}$ 或 $K B_{\text{内}}$ 求自作用力会多算一倍；用零内电场求电力则会完全漏掉静电作用。正确场是内外平均场，电荷量和电流量本身不能再任意减半。

将环向电流圆筒误当作轴向电流柱，容易把磁力画成向内。应直接检查 $\mathbf e_\varphi\times\mathbf e_z=\mathbf e_r$。改变 $\sigma$ 的符号后，最终压力仍应不变；含单独一次 $\sigma$ 的压力式应重新检查。

两端拉力几乎反向，向内合力是 $2T h\sin\alpha$，而不是 $2T h$ 或 $2T h\cos\alpha$。有限壁带中的径向方向也不完全相同，压力与加速度都须投影或积分，不能只对其中一个量使用几何因子。

在惯性系方程中再加向外离心力，同时把向心加速度留在右边，会重复计算。若改在转动系计算，必须明确更换方程体系；两种体系不能混写。本解全程使用惯性系。

先写根式再忽略分子符号，会在静电张力已经超过强度时给出没有物理意义的“转速”。应先检查 $\lambda-T_0$，再选取非负角速度的根。

低速时磁力小于静电力，并不证明它小于临界裕量中的其他项。求转速误差应检查 $\eta$，并注明所使用的牛顿薄壁模型；不能声称这一模型已经包含所有同阶相对论效应。

## 八、课堂讲解建议

课堂先只画一个不带电旋转圆环的窄壁带。让学生在两端沿切线画拉力，并先回答“环很窄时，两边拉力为何几乎抵消”。板书用 $\sin\alpha$ 的极限检验排除 $2T h$ 和 $\cos\alpha$，再恢复面质量密度、轴向长与微元面积，避免一开始将力与张力单位混在一起。

随后加入静电，但先不转动。教师在图2-2上写出内外高斯场，接着在图2-3中分别拆出局部片的正负自场。让学生相加两侧方程，亲自得到有效场的二分之一；再用 $T_0=r p_E$ 检查静态强度，建立“还没旋转也可能破坏”的直觉。

第三层加入面电流和磁场。课堂要求逐字写清“通过轴向切边的电荷面积”，由此得到 $K=\sigma\omega r$。在一个正电荷壁片处做速度与轴向磁场的叉乘，再画向外磁力。教师不宜用“电流总相吸”替代这一方向判断，图2-4与后面的三个受力符号必须保持一致。

最后以图2-5区分截距、斜率和允许裕量。学生先比较 $p_B/p_E$，教师再追问临界方程右侧实际上剩下多少张力。若学生认为“低速必定能删磁力”，可用变式4让他计算两个转速并观察差异；同时明确这只是本题牛顿模型内的近似敏感性，不作完整相对论预测。

## 九、变式训练

**变式1：不带电圆筒的机械强度。**

设 $\sigma=0$，$r=0.20\,\mathrm m$，$\mu=0.80\,\mathrm{kg\,m^{-2}}$，$\lambda=320\,\mathrm{N\,m^{-1}}$。求极限角速度、周期和筒壁线速度。

不带电时，两个自作用压力均为零，张力式为 $T=\mu\omega^2r^2$。令 $T=\lambda$，逐项代入：

$$
\begin{aligned}
\omega_{\max}^2
&=\frac{320}{0.80(0.20)^2}
=\frac{320}{0.032}
=10000\,\mathrm{s^{-2}},\\
\omega_{\max}&=100\,\mathrm{s^{-1}},\\
\mathcal P_{\min}
&=\frac{2\pi}{\omega_{\max}}
=\frac{\pi}{50}\,\mathrm s
\approx0.06283\,\mathrm s,\\
v_{\max}&=r\omega_{\max}=20.0\,\mathrm{m\,s^{-1}}.
\end{aligned}
$$

取任意 $h$ 和 $\alpha$，有限带向内张力合力为 $2\lambda h\sin\alpha$，惯性需求为 $2\mu\omega_{\max}^2r^2h\sin\alpha$；代入后两者相等。此例线速度远小于 $c$，牛顿运动模型自洽。

**变式2：静止充电上限与部分充电后的转速。**

圆筒参数 $r,\mu,\lambda$ 给定。求静态允许的最大 $|\sigma|$；若实际 $|\sigma|$ 为该值的 $0.80$ 倍，求转速上限。再判断 $|\sigma|$ 为该值的 $1.10$ 倍时能否稳态转动。

静态张力不得超过 $\lambda$：

$$
\frac{r\sigma^2}{2\varepsilon_0}\le\lambda
\quad\Longrightarrow\quad
\boxed{|\sigma|\le\sigma_c
=\sqrt{\frac{2\varepsilon_0\lambda}{r}}}.
$$

在 $|\sigma|=0.80\sigma_c$ 时，

$$
\begin{aligned}
T_0&=\frac r{2\varepsilon_0}(0.80)^2
\frac{2\varepsilon_0\lambda}{r}
=0.64\lambda,\\
\lambda-T_0&=0.36\lambda,\\
\eta&=\frac{T_0}{\mu c^2}
=\frac{0.64\lambda}{\mu c^2}.
\end{aligned}
$$

因此

$$
\boxed{\omega_{\max}
=\frac1r\sqrt{
\frac{0.36\lambda}
{\mu[1+0.64\lambda/(\mu c^2)]}}}.
$$

它不是把不带电转速简单乘以 $0.80$。在 $|\sigma|=1.10\sigma_c$ 时，$T_0=1.21\lambda>\lambda$；静止状态已超出强度，不存在可行稳态转动。恰有 $|\sigma|=\sigma_c$ 时，只能在 $\omega=0$ 达到强度边界。

<!-- KEEP_TOGETHER_START -->

**变式3：忽略磁力需要怎样的相对误差条件？**

要求忽略磁力算出的最大角速度相对真实模型值的高估不超过 $q$，其中 $q>0$。求对 $\eta$ 的条件，并计算 $q=1\%$ 与 $q=5\%$ 的界限。

第12步已给出高估比例 $\sqrt{1+\eta}-1$。由于两边均非负，可依次变形：

$$
\begin{aligned}
\sqrt{1+\eta}-1&\le q,\\
\sqrt{1+\eta}&\le1+q,\\
1+\eta&\le(1+q)^2,\\
\eta&\le\boxed{2q+q^2}.
\end{aligned}
$$

<!-- KEEP_TOGETHER_END -->

在 $q=0.01$ 时，$\eta\le0.0201$；在 $q=0.05$ 时，$\eta\le0.1025$。例如 $\eta=0.01$ 给出的相对高估为

$$
\sqrt{1.01}-1\approx0.00498756=0.498756\%.
$$

这些是临界转速的误差条件，不是以 $\omega r/c$ 代替 $\eta$ 的条件。还须检查求出的转速确处于原模型的低速适用范围。

**变式4：低速而临界磁修正显著的模型内反例。**

在本题牛顿薄壁模型中，取非零电荷并满足 $\eta=1$，另设 $\lambda=T_0(1+\delta)$，$\delta=2.0\times10^{-6}$。求保留与不保留磁项时的极限线速度，以及临界点的磁、电力比。

由 $\eta=T_0/(\mu c^2)=1$，先得 $T_0=\mu c^2$。强度中可用于转动的裕量为

$$
\lambda-T_0=\delta T_0=\delta\mu c^2.
$$

<!-- KEEP_TOGETHER_START -->

保留磁力与不保留磁力时分别有

$$
\begin{aligned}
v_{\max}^2
&=r^2\omega_{\max}^2
=\frac{\delta\mu c^2}{\mu(1+1)}
=\frac{\delta c^2}{2},\\
v_{\text{无磁}}^2
&=\frac{\delta\mu c^2}{\mu}
=\delta c^2.
\end{aligned}
$$

代入 $\delta$，并选正的速率根：

$$
\begin{aligned}
v_{\max}&=10^{-3}c,\\
v_{\text{无磁}}&=\sqrt2\,10^{-3}c,\\
\frac{p_B}{p_E}\bigg|_{\max}
&=\left(\frac{v_{\max}}c\right)^2=10^{-6},\\
\frac{v_{\text{无磁}}-v_{\max}}{v_{\max}}
&=\sqrt2-1\approx41.4214\%.
\end{aligned}
$$

虽然磁力比静电小一百万倍，强度之外的裕量也只有百万分之二。临界点的机械转动张力与磁力追加张力恰好相等：

$$
\begin{aligned}
\mu v_{\max}^2&=\frac{\delta T_0}{2},\\
r p_B&=T_0\frac{v_{\max}^2}{c^2}
=\frac{\delta T_0}{2}.
\end{aligned}
$$

两项之和才等于 $\lambda-T_0$，删掉磁项就会明显高估根。此例用于检验近似推理：小项必须与同一方程中真正需要比较的量比较。结论只针对题设牛顿薄壁方程的敏感性；若要讨论这样的高电磁应力材料能否实现，或要求全部同阶相对论修正，必须另给材料及相对论应力模型，不能用此计算替代。

<!-- KEEP_TOGETHER_END -->

<!-- question-complete -->
