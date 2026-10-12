# 第 4 题

<!-- question-start -->

在水平、无限大且接地的导体平板上，放置一个质量密度为 $\rho$、半径为 $R$ 的导体半圆柱，曲面朝上。半圆柱的长度远大于半径，可忽略端部效应。现施加竖直向上的外加匀强电场，其场强为 $E_0$。

求 $E_0$ 至少多大，才能使半圆柱开始离开平板。已知重力加速度为 $g$，真空介电常数为 $\varepsilon_0$。

![图 4-1　接地平板上的长半圆柱与外加电场。](../figures/question-04.png)

<!-- question-end -->

## 一、题型定位

导体静电平衡与电场力积分相结合的临界平衡问题。外加电场在导体表面诱导电荷，电荷受到其余电荷与外加场的共同作用，从而使曲面产生沿法线方向的电压力。

不能直接用半圆柱的“总电荷乘外加场”求合力，也不能把半圆柱表面场强处处当作 $E_0$。本题的核心是先求导体表面的电荷分布，再排除面元自身电场，最后对电压力的竖直分量积分。

## 二、知识点

- 接地导体表面的电势为零，静电平衡时导体内部电场为零。
- 表面外侧电场只有法向分量，并满足 $E_{\text{外}}=\sigma/\varepsilon_0$。
- 对称延拓可以把接地半圆柱的外部场问题化为完整圆柱的二维场问题。
- 无限长均匀带电圆柱内部场强可由高斯定律求出。
- 表面面元受到的力应使用除去该面元自身贡献的电场。
- 曲面面积元与力的投影分别带来几何因子，不能合并后漏掉余弦。
- 刚要离开支撑面时，支持力降为零。

## 三、物理图像

以半圆柱轴线为 $z$ 轴，取竖直向上为 $y$ 正向。沿轴线取一段长度 $L$，其中 $L\gg R$；最终升力和重量都正比于 $L$，所以 $L$ 会约去。

在垂直轴线的截面中，以底面直径的中点 $O$ 为原点。上半圆曲面的外法线与竖直方向夹角记为 $\theta$，其范围为

$$
-\frac{\pi}{2}\le\theta\le\frac{\pi}{2}.
$$

圆柱顶部对应 $\theta=0$，与平板相接的两侧边缘对应 $\theta=\pm\pi/2$。半圆柱与平板接触时电势相同，整个导体表面为等势面。外部场线在曲面处必须沿法线，而不能保持到处竖直。

长度 $L$ 的半圆柱质量为

$$
m=\rho\left(\frac12\pi R^2L\right).
$$

其底部与平板直接接触，在接触面内没有可供本题电场穿过的真空间隙。临界起离之前，需要积分的是暴露在上半空间的曲面电压力。

## 四、解题入口

先利用接地平面将几何关系向下镜像延拓，得到完整导体圆柱处于横向匀强场的标准边界问题。用两个略有错位、体电荷密度相反的辅助圆柱构造感应电荷，直接从“内部场为零”求出表面电荷密度。

然后取一个足够小的曲面面元。分别写出面元自身电场和其余系统的电场，明确为何作用于面元的场只有总表面场的一半。最后把电压力乘面积元、再取竖直分量，与重力比较。

## 五、解析

（1）说明为何可以补成一个完整圆柱。

图4-2左图中，实线上半圆是真实曲面，虚线下半圆是为了求场而引入的对称延拓。将电势关于接地平面作反对称延拓，下半空间相应地具有与上半空间相反的电势。这样，平面 $y=0$ 上的电势仍为零，圆柱整周也是零电势。

![图 4-2　接地边界的对称延拓与辅助电荷圆柱的错位构造。](../figures/field-04.png)

在远离圆柱的地方，给定外加场为 $E_0\hat{\boldsymbol y}$，对应电势为 $-E_0y$，它本身就满足关于 $y=0$ 的反对称性。因此完整圆柱的解在上半空间同时满足真实题目的接地边界和远处外场条件，可以用来求真实半圆柱的表面电荷。

这里补出的下半圆不是实际又放了一个带质量的半圆柱；它只用于求上半空间的电场。计算重力时仍只能取 $\pi R^2L/2$ 的体积。

（2）求均匀带电长圆柱内部的电场。

为避免与质量密度 $\rho$ 混淆，把辅助体电荷密度记为 $\rho_e$。先考虑半径为 $R$、体电荷密度为 $\rho_e$ 的无限长圆柱。

取半径 $s<R$、长度 $\ell$ 的同轴高斯柱面。对称性保证电场沿径向，侧面上场强大小处处为 $E(s)$；两端面的法向沿轴线，因此电通量为零。高斯定律给出

$$
\begin{aligned}
E(s)\,2\pi s\ell
&=\frac{\rho_e\pi s^2\ell}{\varepsilon_0},\\
E(s)&=\frac{\rho_e s}{2\varepsilon_0}.
\end{aligned}
$$

若辅助圆柱轴线横向位置为 $\boldsymbol a$，内部某点的位置为 $\boldsymbol r$，则矢量表达式为

$$
\boldsymbol E(\boldsymbol r)
=\frac{\rho_e}{2\varepsilon_0}
(\boldsymbol r-\boldsymbol a).
$$

这个内部电场正比于离轴位移，是下一步“两个圆柱叠加后得到匀强场”的原因。

（3）用微小错位的正、负圆柱构造表面电荷。

取半径相同的两个辅助圆柱。正电荷圆柱的轴线向上移动 $\delta/2$，负电荷圆柱的轴线向下移动 $\delta/2$，两轴线间距为 $\delta$，且 $\delta\ll R$。其体电荷密度分别为 $+\rho_e$、$-\rho_e$。

图4-2右图中，正电荷圆柱中心为 $O_+$，负电荷圆柱中心为 $O_-$。两者重叠区域内，体电荷相互抵消；在外缘留下很薄的正、负电荷层。对重叠区域中的任一点，两圆柱产生的电场相加为

$$
\begin{aligned}
\boldsymbol E_{\text{感}}
&=\frac{\rho_e}{2\varepsilon_0}
\left(\boldsymbol r-\frac{\delta}{2}\hat{\boldsymbol y}\right)
-\frac{\rho_e}{2\varepsilon_0}
\left(\boldsymbol r+\frac{\delta}{2}\hat{\boldsymbol y}\right)\\
&=\frac{\rho_e}{2\varepsilon_0}
\left(-\delta\hat{\boldsymbol y}\right)\\
&=-\frac{\rho_e\delta}{2\varepsilon_0}
\hat{\boldsymbol y}.
\end{aligned}
$$

点的位置 $\boldsymbol r$ 消去，因此感应电荷产生的内部场是竖直向下的匀强场。导体内部总场应为零：

$$
\begin{aligned}
E_0\hat{\boldsymbol y}+\boldsymbol E_{\text{感}}&=\boldsymbol0,\\
E_0-\frac{\rho_e\delta}{2\varepsilon_0}&=0,\\
\boxed{\rho_e\delta=2\varepsilon_0E_0}.
\end{aligned}
$$

$\rho_e$、$\delta$ 都是构造辅助量。可以取 $\delta\to0$、$\rho_e\to\infty$，保持乘积 $\rho_e\delta$ 有限，从而得到只有表面电荷而没有内部净体电荷的极限分布。

（4）把辅助薄层转化为表面电荷密度。

在法线与竖直方向夹角为 $\theta$ 的位置，两个圆柱沿竖直方向的错位 $\delta$，投影到局部法线后是 $\delta\cos\theta$。上半圆留下的正电荷薄层厚度就是这一投影的一阶值。

面积为 $\mathrm dS$ 的小面元内，辅助薄层体积为

$$
\mathrm dV_e=\delta\cos\theta\,\mathrm dS.
$$

其中电荷为 $\mathrm dq=\rho_e\,\mathrm dV_e$，故单位面积电荷量为

$$
\begin{aligned}
\sigma(\theta)
&=\frac{\mathrm dq}{\mathrm dS}
=\rho_e\delta\cos\theta\\
&=\boxed{2\varepsilon_0E_0\cos\theta}.
\end{aligned}
$$

这说明顶部电荷密度最大，为 $2\varepsilon_0E_0$；左右边缘的电荷密度趋于零。上半圆各点有 $\cos\theta\ge0$，因而曲面电荷为非负，与向上外场下正电荷聚集在上方的物理图像相符。

注意上式中的 $\cos\theta$ 已经来自“错位厚度的法向投影”。后面计算力的竖直分量时还会出现另一个余弦，两者来源不同，不能只保留一个。

（5）求总表面场，并分离面元自身的电场。

先用跨越导体表面的小高斯柱求总电场的跳变。设面元附近外侧法向场强为 $E_{\text{外}}$，内侧场强为 $E_{\text{内}}=0$。两底面积同为 $\Delta S$，则

$$
\begin{aligned}
(E_{\text{外}}-E_{\text{内}})\Delta S
&=\frac{\sigma\Delta S}{\varepsilon_0},\\
E_{\text{外}}&=\frac{\sigma}{\varepsilon_0}
=2E_0\cos\theta.
\end{aligned}
$$

但这不是直接作用在该面元电荷上的场。原因是 $E_{\text{外}}$ 还包含该面元自身的贡献，而电荷不能通过自身电场给自身提供整体合力。

图4-3右图把足够小的面元局部视为平面电荷片。电荷片在外侧产生沿外法线的场 $\sigma/(2\varepsilon_0)$，在内侧产生反向、等大的场。其余所有电荷与外加场共同产生的场记为 $\boldsymbol E_{\text{余}}$，跨过这一无穷薄面元时连续。

![图 4-3　曲面电压力的方向、竖直投影与局部自场分离。](../figures/solution-04.png)

以外法线为正方向，内侧静电平衡要求

$$
\begin{aligned}
E_{\text{内}}
&=E_{\text{余}}-\frac{\sigma}{2\varepsilon_0}=0,\\
\boxed{E_{\text{余}}}
&=\boxed{\frac{\sigma}{2\varepsilon_0}}.
\end{aligned}
$$

外侧总场因此为

$$
E_{\text{外}}
=E_{\text{余}}+\frac{\sigma}{2\varepsilon_0}
=\frac{\sigma}{\varepsilon_0},
$$

与高斯定律一致。也可以把作用场写为内、外侧场的平均值：

$$
E_{\text{余}}=\frac{E_{\text{外}}+E_{\text{内}}}{2}.
$$

此处的“其余”不仅指最初施加的 $E_0$，还包括导体和接地平板上其他所有感应电荷的场。因此既不能取 $E_0$，也不能取 $E_{\text{外}}$。

（6）计算面元受力及竖直分量。

曲面面元带电量为 $\mathrm dq=\sigma\,\mathrm dS$，沿外法线受到电场力

$$
\begin{aligned}
\mathrm dF
&=\mathrm dq\,E_{\text{余}}\\
&=\sigma\,\mathrm dS\,
\frac{\sigma}{2\varepsilon_0}\\
&=\frac{\sigma^2}{2\varepsilon_0}\,\mathrm dS.
\end{aligned}
$$

故电压力为

$$
p_e(\theta)=\frac{\mathrm dF}{\mathrm dS}
=\frac{\sigma^2}{2\varepsilon_0}
=2\varepsilon_0E_0^2\cos^2\theta.
$$

图4-3左图中的 $\mathrm d\boldsymbol F$ 沿该处半径向外。其竖直分量应再乘法线与竖直方向夹角的余弦：

$$
\mathrm dF_y=p_e(\theta)\cos\theta\,\mathrm dS.
$$

曲面的面积元由截面弧长乘长度 $L$ 给出。弧长为 $R\,\mathrm d\theta$，所以

$$
\mathrm dS=LR\,\mathrm d\theta.
$$

将三者合并：

$$
\begin{aligned}
\mathrm dF_y
&=2\varepsilon_0E_0^2\cos^2\theta
\cdot\cos\theta\cdot LR\,\mathrm d\theta\\
&=\boxed{
2\varepsilon_0E_0^2LR\cos^3\theta\,\mathrm d\theta}.
\end{aligned}
$$

这里三个余弦因子的来源是：电荷密度平方带来两个，力向竖直方向投影再带来一个。面积元本身不含余弦。

（7）对上半圆积分，求总升力。

关于竖直中面对称的两个面元，水平分量大小相等、方向相反，因此水平合力为零。竖直分量相加：

$$
F_y
=2\varepsilon_0E_0^2LR
\int_{-\pi/2}^{\pi/2}\cos^3\theta\,\mathrm d\theta.
$$

下面完整计算积分。利用 $\cos^3\theta=\cos\theta(1-\sin^2\theta)$，令 $s=\sin\theta$，则 $\mathrm ds=\cos\theta\,\mathrm d\theta$，积分上下限变为 $-1$、$1$：

$$
\begin{aligned}
\int_{-\pi/2}^{\pi/2}\cos^3\theta\,\mathrm d\theta
&=\int_{-1}^{1}(1-s^2)\,\mathrm ds\\
&=\left[s-\frac{s^3}{3}\right]_{-1}^{1}\\
&=\left(1-\frac13\right)
-\left(-1+\frac13\right)\\
&=\frac43.
\end{aligned}
$$

因而

$$
\boxed{F_y=\frac83\varepsilon_0E_0^2LR}.
$$

积分只覆盖真实上半圆。如果把补出的下半圆也积分进去，完整圆柱在匀强场中的净竖直力为零，得到的是另一个物体的合力，而不是本题半圆柱的升力。

（8）列临界平衡方程，筛选所需场强。

取半圆柱整体为研究对象，沿竖直方向的力有：向上电场合力 $F_y$、向上平板支持力 $N$、向下重力 $mg$。未起离时静止，因此

$$
N+F_y-mg=0.
$$

平板只能推半圆柱，不能向下拉它，故必须有 $N\ge0$。随着 $E_0$ 增大，$F_y$ 增大、$N$ 减小；开始离开平板的临界条件为 $N=0$，即

$$
F_y=mg.
$$

代入升力与重量：

$$
\begin{aligned}
\frac83\varepsilon_0E_0^2LR
&=\frac12\pi R^2L\rho g,\\
E_0^2
&=\frac{\pi R^2L\rho g}{2}
\frac{3}{8\varepsilon_0LR}\\
&=\frac{3\pi\rho gR}{16\varepsilon_0}.
\end{aligned}
$$

场强大小取非负根，所需最小值为

$$
\boxed{
E_{0,\min}
=\frac14\sqrt{\frac{3\pi\rho gR}{\varepsilon_0}}.
}
$$

题给外场方向为向上。上式回答的是大小至少多大才能刚开始起离，不是离开后任意高度的平衡场强；半圆柱一旦与平板分离，几何边界和接地连接状态都可能改变，不能沿用接触时的表面电荷分布研究全过程。

（9）从量纲、尺度和总电荷检查结果。

由电场能量密度的量纲可知 $\varepsilon_0E_0^2$ 具有压力单位 $\mathrm{N/m^2}$，乘 $LR$ 得到力，故升力表达式量纲正确。另一方面，$\rho gR$ 也是压力量纲，因此临界式中两侧的物理单位一致。

长度 $L$ 约去，表示远离端部的每单位长度具有相同的升力与重量。半径增大时，重量按 $R^2$ 增长，升力在同一外场下仅按 $R$ 增长，所以临界场强正比于 $\sqrt R$。密度增大时，所需场强正比于 $\sqrt\rho$，符合更重物体需要更大升力的判断。

还可计算上半圆的总电荷：

$$
\begin{aligned}
Q_{\text{上}}
&=\int_{-\pi/2}^{\pi/2}\sigma LR\,\mathrm d\theta\\
&=2\varepsilon_0E_0LR
\left[\sin\theta\right]_{-\pi/2}^{\pi/2}\\
&=4\varepsilon_0E_0LR.
\end{aligned}
$$

如果误用 $Q_{\text{上}}E_0$，会得到 $4\varepsilon_0E_0^2LR$，比正确结果大 $3/2$ 倍。差异来自感应电荷之间以及它们与平板电荷之间的相互作用；上半圆并不是一个只受外加匀强场作用、其余外部电荷均可忽略的孤立带电物体。

## 六、关键洞察

局部电压力可以用场能量密度理解：

$$
p_e=\frac12\varepsilon_0E_{\text{外}}^2.
$$

它与上一节的 $\sigma^2/(2\varepsilon_0)$ 完全一致。这个系数 $1/2$ 不是经验修正，而是排除面元自场后自然产生的。即使表面电荷为负，$\sigma$ 与作用场同时反向，其乘积仍为正，所以电压力始终沿导体表面外法线指向真空一侧。

另一条独立求场路线是直接构造电势。用 $s$ 表示离圆柱轴线的距离，$\theta$ 仍从竖直方向量起。外部电势取为

$$
\Phi(s,\theta)
=-E_0\left(s-\frac{R^2}{s}\right)\cos\theta,
\qquad s\ge R.
$$

第一项 $-E_0s\cos\theta=-E_0y$ 是原有匀强场的电势；第二项在远处衰减，描述圆柱感应电荷的影响。圆柱表面 $s=R$ 时，两项相消，电势为零；接地平面 $\theta=\pm\pi/2$ 上也有电势为零；$s\to\infty$ 时恢复给定外加场。

还要验证它在无电荷区域满足拉普拉斯方程，而不能只靠边界“猜对”。在二维极坐标中，对 $f(s)\cos\theta$ 有

$$
\nabla^2[f(s)\cos\theta]
=\left[f''(s)+\frac{f'(s)}s-\frac{f(s)}{s^2}\right]\cos\theta.
$$

取 $f(s)=s$，方括号为 $0+1/s-1/s=0$；取 $f(s)=1/s$，方括号为

$$
\frac2{s^3}-\frac1{s^3}-\frac1{s^3}=0.
$$

所以该电势满足场方程及全部边界条件。由静电边值问题的唯一性，它就是所需外部电势。求法向场：

$$
\begin{aligned}
E_s&=-\frac{\partial\Phi}{\partial s}
=E_0\left(1+\frac{R^2}{s^2}\right)\cos\theta,\\
E_s(R,\theta)&=2E_0\cos\theta.
\end{aligned}
$$

再求切向场以确认导体边界：

$$
E_\theta
=-\frac1s\frac{\partial\Phi}{\partial\theta}
=-E_0\left(1-\frac{R^2}{s^2}\right)\sin\theta,
\qquad E_\theta(R,\theta)=0.
$$

这条电势路线与正文的错位电荷圆柱路线给出同一表面场，构成独立的物理交叉核验。

## 七、易错点

- 把辅助体电荷密度 $\rho_e$ 与题给质量密度 $\rho$ 混用。前者只用于构造静电场，后者只用于计算重量。
- 补全圆柱后，把真实物体重量也翻倍。镜像延拓改变的是求场模型，不是实际质量。
- 把表面总场 $2E_0\cos\theta$ 当成面元受力场。正确受力场是其一半，直接使用总场会使升力增大一倍。
- 把 $\sigma$ 写成与位置无关的常数。顶部和侧边的法线不同，导体表面感应电荷必然重新分布。
- 在 $\mathrm dS$ 中加入 $\cos\theta$，同时又在力的投影中乘余弦。圆柱曲面的实际面积元是 $LR\,\mathrm d\theta$，不是投影面积。
- 把面元力沿竖直方向直接相加。电压力沿局部法线，必须先取竖直分量。
- 积分上下限取整圆。真实半圆柱只对应 $-\pi/2$ 到 $\pi/2$。
- 把“开始离开”当作“已能一直上升”。离开后的电接触和场分布是新的边界问题。
- 认为导体接地就不可能带电。接地固定的是电势，电荷可与大地交换，表面电荷不必为零。

## 八、课堂讲解建议

先展示半圆柱的空间图，再切换到垂直轴线的截面，让学生说明为什么可以只算一段长度 $L$。板书质量和曲面面积元，避免最后把半圆柱当成半球处理。

表面电荷的推导适合分两步讲：先由高斯定律求均匀带电圆柱内部场，再叠加两个错位圆柱。要求学生实际写出两项中的 $\boldsymbol r$ 如何相消，之后才引入表面薄层的厚度投影。

讲面元受力时，将“外侧总场”“面元自场”“其余系统的作用场”分成三列。让学生从内侧总场为零推出自场系数，再用外侧高斯定律核对。不要直接把电压力公式作为一条需要背诵的结论。

最后让学生追踪 $\cos^3\theta$ 的三个因子分别从哪里来，并解释为什么 $L$ 消去而 $R$ 不消去。这两项都能快速检查其是否真正理解了曲面力积分。

## 九、变式训练

变式一：半圆柱材料密度仍为 $\rho$，外半径为 $R$，内部挖去一个同轴半圆柱空腔，内半径为 $a$，其中 $0<a<R$。空腔位于导体内部，且由接地平板封闭，腔内没有电荷。忽略壁厚引起的端部效应，求起离所需外场。

解：空腔内部的边界均为同一接地等势面，且腔内没有电荷，因此腔内电场为零。外部边界的形状和电势未变，所以外曲面的电场、表面电压力及单位长度升力均与实心半圆柱相同：

$$
\frac{F_y}{L}=\frac83\varepsilon_0E_0^2R.
$$

改变的是质量。长度 $L$ 的材料体积为外半圆柱体积减内半圆柱体积：

$$
V_{\text{材}}=\frac12\pi(R^2-a^2)L.
$$

令电场升力等于重量：

$$
\begin{aligned}
\frac83\varepsilon_0E_0^2LR
&=\frac12\pi(R^2-a^2)L\rho g,\\
E_0^2
&=\frac{3\pi\rho g(R^2-a^2)}
{16\varepsilon_0R}.
\end{aligned}
$$

故

$$
\boxed{
E_{0,\min}
=\frac14\sqrt{
\frac{3\pi\rho g(R^2-a^2)}
{\varepsilon_0R}}.
}
$$

检查 $a=0$ 时恢复实心结果；$a\to R$ 时材料质量趋于零，所需临界场也趋于零。在薄壁极限中，令壁厚 $t=R-a\ll R$，则

$$
\begin{aligned}
R^2-a^2&=(R-a)(R+a)=t(2R-t),\\
\frac{R^2-a^2}{R}&=2t-\frac{t^2}{R}\approx2t.
\end{aligned}
$$

保留壁厚的一阶项，得到

$$
\boxed{
E_{0,\min}\approx
\sqrt{\frac{3\pi\rho gt}{8\varepsilon_0}}.
}
$$

薄壁近似中外半径在首阶消去，是因为材料单位长度质量和同一场强下的升力都正比于外半径；并不是把几何尺寸任意忽略。该变式的适用条件是空腔封闭、内部无电荷，并在起离之前保持整个边界等势。

为了量化薄壁近似的适用程度，将近似值与精确值直接相除。由 $R^2-a^2=2Rt-t^2$ 得

$$
\begin{aligned}
\frac{E_{\text{近似}}}{E_{\text{精确}}}
&=\sqrt{\frac{2Rt}{2Rt-t^2}}\\
&=\left(1-\frac{t}{2R}\right)^{-1/2}\\
&\approx1+\frac{t}{4R}.
\end{aligned}
$$

最后一步使用二项式展开，只保留 $t/R$ 的一阶项。因此薄壁公式略微高估临界场强，而不是低估。例如 $t=R/10$，精确比值为 $1/\sqrt{0.95}\approx1.02598$，相对误差约为 $2.60\%$；一阶误差估计给出 $t/(4R)=2.50\%$。

如果要求近似值相对精确值的误差不超过 $5\%$，应从未展开的比值解不等式：

$$
\begin{aligned}
\left(1-\frac{t}{2R}\right)^{-1/2}&\le1.05,\\
1-\frac{t}{2R}&\ge\frac1{1.05^2},\\
\frac tR&\le2\left(1-\frac1{1.05^2}\right)\approx0.18594.
\end{aligned}
$$

这个误差界只针对所用薄壁质量近似；端部效应、材料强度和脱离平板后的场分布仍不在本题模型之内。

变式二：求接地半圆柱曲面上的总电荷，以及曲面顶部的最大电压力，忽略端部。

解：令 $\theta$ 从竖直向上量取，曲面场强 $E_n=2E_0\cos\theta$，电荷密度 $\sigma=2\varepsilon_0E_0\cos\theta$。面积元 $LR\,d\theta$，故

$$
Q=\int_{-\pi/2}^{\pi/2}\sigma LR\,d\theta=4\varepsilon_0E_0LR.
$$

电压力 $p_e=\varepsilon_0E_n^2/2=2\varepsilon_0E_0^2\cos^2\theta$，最大值在顶部，为 $2\varepsilon_0E_0^2$。该电荷可由接地电源提供，不能附加曲面净电荷为零的条件。

变式三：求顶部角区 $|\theta|\le\pi/6$ 提供的竖直电力占总竖直电力的比例。

解：竖直微元力为 $dF_y=2\varepsilon_0E_0^2LR\cos^3\theta\,d\theta$。原总积分为 $\int_{-\pi/2}^{\pi/2}\cos^3\theta d\theta=4/3$。顶部区积分利用原函数 $\sin\theta-\sin^3\theta/3$，为 $2(1/2-1/24)=11/12$。所以

$$
\frac{F_{\rm top}}{F_{\rm all}}=\frac{11}{16}.
$$

顶部只有曲面角宽的三分之一，却承担超过一半的竖直电力；投影因子和电压力分布共同产生这个结果。

变式四：将外半径增为四倍，密度、重力和长度不变，仍满足长圆柱近似。求起离电场及给定外场时电力、重力的变化倍数。

解：$F_e=8\varepsilon_0E_0^2LR/3\propto R$，重力 $G=\pi R^2L\rho g/2\propto R^2$。半径四倍使同场电力四倍、重力十六倍。由两者相等得

$$
E_{\rm crit}=\sqrt{\frac{3\pi\rho gR}{16\varepsilon_0}}\propto\sqrt R,
$$

故临界场变为两倍。长度约去，原因是两种力都与长度成正比；这仍要求 $L\gg4R$，否则端部效应不能忽略。
