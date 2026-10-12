# 第2题


<!-- question-start -->

压电效应是许多力电转换设备的基础。一类压电晶体的离子模型如图2-1所示：晶胞的八个角点为 $\mathrm{Pb}^{2+}$，六个面心为 $\mathrm O^{2-}$，晶胞内部为一个 $\mathrm{Ti}^{4+}$。角点离子由相邻八个晶胞共享，面心离子由相邻两个晶胞共享。温度高于临界温度 $T_c$ 时，钛离子位于晶胞中心；温度低于 $T_c$ 时，晶胞成为边长为 $a\times a\times b$ 的长方体，钛离子沿长轴正方向偏移，处于上方五个氧离子构成的四棱锥内，正、负电荷中心不再重合。设偏移距离为 $\lambda b$，其中 $0<\lambda<1/2$，$e$ 为元电荷的大小。

![图2-1 两种温度条件下的晶胞结构及长轴极化方向。](../figures/cell-02.png){width=79%}

（1）求晶体的初始极化强度 $P_0$。$P_0$ 定义为单位体积内电偶极矩的大小，用 $a,b,\lambda,e$ 表示。

（2）晶体沿长轴受到微小拉伸，晶胞长轴的长度增量为 $\Delta b$，钛离子的相对偏移参数改变为 $\lambda+\Delta\lambda$，且
$$
\Delta\lambda=\tau\frac{\Delta b}{b},\qquad
\Delta p=Y\frac{\Delta b}{b},
$$
其中 $\tau$ 为已知无量纲常数，$Y$ 为杨氏模量，$\Delta p$ 为沿长轴的拉伸应力增量，取拉伸为正。内部电场沿长轴的有向增量满足 $\Delta E_z=\alpha\Delta p$。用 $Y,P_0,\lambda,\tau,\varepsilon_0$ 表示直接压电响应系数 $\alpha$。

第（2）问的应力关系为 $\Delta p=Y\Delta b/b$。取横向尺寸 $a$ 不变，晶体为法向沿长轴、横向尺寸远大于厚度的均匀极化薄板，处于开路条件；拉伸期间自由表面电荷不交换，外部电边界不改变。忽略边缘场与背景介电响应，采用 $D_z=\varepsilon_0E_z+P$。$E_z$ 是以极化方向为正的电场分量，“直接压电效应”不预先规定 $\alpha$ 的正负。图中离子位移仅作结构示意，不代表 $\lambda$ 的具体数值。

<!-- question-end -->

## 一、题型定位

本题把微观晶胞中的电荷位移与宏观开路电场联系起来。第（1）问是离散电荷的偶极矩计算：先按晶胞共享比例分配电荷，再除以晶胞体积。第（2）问是线性机电响应：把应力变成应变，把应变变成极化增量，最后用指定电边界把极化增量变成电场增量。

核心不是“拉伸后多出了净电荷”，而是中性晶胞内部正、负电荷相对位置变化。晶体仍可整体电中性，但上下表面的束缚电荷发生变化，内部电场随之改变。这里的电荷守恒与偶极矩变化并不矛盾。

需要分别处理两种尺度。$a,b,\lambda b$ 是一个晶胞的几何量；宏观薄板的厚度后文记为 $L$，不把 $b$ 当作整个样品厚度。微观计算决定 $P$，宏观形状和自由电荷条件决定 $E_z$。由晶胞中性直接断言任何样品都具有 $E_z=-P/\varepsilon_0$，会省掉本题最重要的边界判断。

## 二、知识点

离散电荷的电偶极矩定义为
$$
\boldsymbol p_{\mathrm{cell}}=\sum_iq_i\boldsymbol r_i.
$$
其中 $q_i$ 是归属于所研究晶胞的电荷，$\boldsymbol r_i$ 是相对于同一原点的位置向量。若晶胞总电荷为零，改变原点不会改变偶极矩。对同方向排列的相同晶胞，极化强度为单位体积的偶极矩：
$$
\boldsymbol P=\frac{\boldsymbol p_{\mathrm{cell}}}{V_{\mathrm{cell}}}.
$$
单个偶极矩的单位为 $\mathrm{C\,m}$，极化强度的单位为 $\mathrm{C/m^2}$；两者不能使用同一含义的符号。

长轴的工程应变定义为 $\varepsilon=\Delta b/b$。在线性弹性范围内，拉伸应力与应变满足 $\Delta p=Y\varepsilon$。这里用 $\Delta p$ 表示应力，不是一个晶胞的电偶极矩；偶极矩始终带下标 $\mathrm{cell}$。

极化物体表面的束缚电荷密度为
$$
\sigma_{\mathrm b}=\boldsymbol P\cdot\boldsymbol n,
$$
其中 $\boldsymbol n$ 为向外法线。电位移的高斯定律只把自由电荷放在右端：
$$
\oint\boldsymbol D\cdot\mathrm d\boldsymbol S=Q_{\mathrm f}.
$$
本题忽略背景介电响应，因而 $\boldsymbol D=\varepsilon_0\boldsymbol E+\boldsymbol P$。不能在右端再次加入束缚电荷，否则等于重复计算极化的贡献。

小量近似也必须分层说明。$\Delta p=Y\varepsilon$ 与 $\Delta\lambda=\tau\varepsilon$ 是题设给定的线性关系；而在横截面积不变的模型中，极化式里长轴长度的约去是精确代数。后面不把“线性本构近似”与“忽略体积变化”混为一谈。

## 三、物理图像

图2-1中，八个铅离子位于长方体的角点，六个氧离子位于六个面心，后侧棱用虚线表示。上面一个氧离子与四个侧面心氧离子构成上半个八面体，即题干所说的四棱锥；下方面心的第六个氧离子仍然存在。

钛离子向上移动时，对称分布的铅、氧背景没有额外的偶极矩，只有钛离子相对原有中心的位置变化贡献正向偶极矩。图中的极化箭头表示由负电荷中心指向正电荷中心的方向，不是内部电场的方向。

在宏观尺度上，均匀极化的宽薄板上表面具有束缚正电荷，下表面具有束缚负电荷。没有自由电荷补偿的特例中，内部电场由上向下，与 $\boldsymbol P$ 相反。若已经有固定的表面补偿电荷，初始场可以不同，但本题开路拉伸所产生的电场增量仍由极化增量决定。

拉伸时要区分三个量：长轴长度 $b$，无量纲偏移比例 $\lambda$，实际偏移距离 $\delta=\lambda b$。$b$ 变长会使实际位移改变，也会使一个晶胞占据的体积改变；只有同时更新这两个量，才能正确判断单位体积极化的变化。

## 四、解题入口

先取晶胞几何中心为原点，长轴向上为 $z$ 正方向，计算各类离子的归属电荷。确认总电荷为零以后，再利用对称性消去背景离子的偶极矩，不凭“钛离子电荷最大”而忽略其他离子。

第（1）问算出 $p_{\mathrm{cell},z}$ 与 $V_{\mathrm{cell}}$ 后相除。第（2）问先写变形后真实的 $b'$、$\lambda'$ 和 $V'_{\mathrm{cell}}$，再计算 $P'-P_0$，最后用 $\Delta p=Y\varepsilon$ 消去应变。

从 $\Delta P$ 到 $\Delta E_z$ 的负号不来自机械拉伸式，而来自电边界。开路且横向面积不变，使自由面电荷密度不变；外部电边界也固定，所以薄板内部 $D_z$ 的增量为零。将这一条件代入本构式后，再与 $\Delta E_z=\alpha\Delta p$ 比较系数。

## 五、解析

**第1步：确定一个晶胞中的离子归属与坐标。**

以图2-1右侧长方体的几何中心为原点，取三条相互垂直的棱分别平行于 $x,y,z$ 轴。长轴为 $z$ 轴。八个角点的位置为
$$
\left(\pm\frac a2,\ \pm\frac a2,\ \pm\frac b2\right).
$$
符号独立选取，共有 $2\times2\times2=8$ 个角点。六个面心的位置分别为
$$
\left(\pm\frac a2,0,0\right),\quad
\left(0,\pm\frac a2,0\right),\quad
\left(0,0,\pm\frac b2\right).
$$
钛离子的位置为 $(0,0,\lambda b)$。位移方向已经规定为正 $z$，因此本题初始 $P_0$ 是正向极化分量的大小。若把坐标正方向反过来，电场、极化和偏移参数的有向写法必须同时改变，不能只改变一个负号。

**第2步：按共享比例计算电荷，核对晶胞中性。**

一个角点处的铅离子本身带电 $+2e$，但归属于本晶胞的份额只有 $1/8$。八个角点合计贡献
$$
Q_{\mathrm{Pb}}=8\times\frac18\times2e=2e.
$$
一个面心处的氧离子本身带电 $-2e$，归属份额为 $1/2$。六个面心合计贡献
$$
Q_{\mathrm O}=6\times\frac12\times(-2e)=-6e.
$$
钛离子完整位于晶胞内部，贡献 $Q_{\mathrm{Ti}}=4e$。总电荷为
$$
Q_{\mathrm{cell}}=2e-6e+4e=0.
$$
这是电荷归属正确的第一项检验。如果把八个角点的完整铅离子与六个面心的完整氧离子都归入一个晶胞，就会得到错误的净电荷，同时破坏后面的偶极矩计算。

把边界离子的共享电荷看作放在对应边界位置，是均匀周期模型的计数约定。它不是把真实离子电荷削弱了，而是避免相邻晶胞重复计数。宏观样品边缘的额外归属差异不属于本题的均匀体积极化模型。

**第3步：逐类消去对称背景的偶极矩。**

对每一对关于原点对称的角点，其归属电荷都是 $e/4$，位置分别为 $\boldsymbol r$ 与 $-\boldsymbol r$。这一对的偶极矩为
$$
\frac e4\boldsymbol r+\frac e4(-\boldsymbol r)=\boldsymbol0.
$$
八个角点分成四对，所以铅离子的总偶极矩为零。六个面心分成三对，每个归属氧电荷为 $-e$，每对的偶极矩为
$$
(-e)\boldsymbol r+(-e)(-\boldsymbol r)=\boldsymbol0.
$$
因此氧离子的总偶极矩也为零。这里消去的是矢量和，不是消去这些离子的净电荷。铅、氧背景合起来的总电荷为 $-4e$，但以几何中心为原点，其偶极矩为零。

钛离子沿轴偏移后，其偶极矩为 $4e\lambda b\,\boldsymbol e_z$。所以
$$
\begin{aligned}
p_{\mathrm{cell},x}&=0,\\
p_{\mathrm{cell},y}&=0,\\
p_{\mathrm{cell},z}&=4e\lambda b.
\end{aligned}
$$
如图2-2，中心 $O$ 是几何参考点，黑点是移动后的钛离子。图中的上下氧离子给出长轴的端点；此图只表示轴向投影，不把其余四个氧离子从三维晶胞中删除。

![图2-2 钛离子的轴向位移与晶胞偶极矩。](../figures/dipole-02.png){width=46%}

随后直接使用图中的 $\delta=\lambda b$，得到 $p_{\mathrm{cell},z}=4e\delta$。图上的 $O$ 不是一个新增的带电粒子；也没有把背景电荷实际集中到 $O$。使用背景的对称性与把真实结构替换成一对点电荷，是两个不同层次的描述。

**第4步：核对偶极矩为何不依赖原点。**

若把原点平移 $\boldsymbol r_0$，所有位置变成 $\boldsymbol r_i-\boldsymbol r_0$，则
$$
\begin{aligned}
\boldsymbol p'_{\mathrm{cell}}
&=\sum_iq_i(\boldsymbol r_i-\boldsymbol r_0)\\
&=\sum_iq_i\boldsymbol r_i-\boldsymbol r_0\sum_iq_i\\
&=\boldsymbol p_{\mathrm{cell}}-Q_{\mathrm{cell}}\boldsymbol r_0\\
&=\boldsymbol p_{\mathrm{cell}}.
\end{aligned}
$$
最后一行用到了第2步的 $Q_{\mathrm{cell}}=0$。这说明选择几何中心只是让对称项容易抵消，不会改变答案。

若误算出晶胞净电荷不为零，偶极矩就会随原点改变。这个检验能帮助定位共享比例的错误，却仍不能替代宏观样品的电边界条件；“偶极矩与原点无关”不等于“内部电场必为零”。

**第5步：由单胞偶极矩求单位体积极化，完成第（1）问。**

一个长方体晶胞的体积为 $V_{\mathrm{cell}}=a\times a\times b=a^2b$。设含有 $N$ 个同方向极化的晶胞，忽略边缘效应，总偶极矩为 $Np_{\mathrm{cell},z}$，总体积为 $Na^2b$，故
$$
\begin{aligned}
P_0
&=\frac{Np_{\mathrm{cell},z}}{Na^2b}\\
&=\frac{4e\lambda b}{a^2b}\\
&=\boxed{\frac{4e\lambda}{a^2}}.
\end{aligned}
$$
$N$ 与 $b$ 分别约去。$b$ 消失并不表示长轴对单胞偶极矩没有影响，而是长轴同时出现在偶极矩和体积中。固定 $a,\lambda$ 时，较长的晶胞有较大的偶极矩，也占据更大的体积，两种变化恰好抵消。

量纲为 $e/a^2$，即 $\mathrm{C/m^2}$，与极化强度一致。如果写成 $4e\lambda b$，求到的是单胞偶极矩；如果写成 $4e\lambda/(a^2b)$，则多除了一次长度，单位也不正确。

**第6步：明确拉伸后每个几何量的含义。**

定义 $\varepsilon=\Delta b/b$，则
$$
b'=b+\Delta b=b(1+\varepsilon),\qquad
\lambda'=\lambda+\Delta\lambda=\lambda+\tau\varepsilon.
$$
钛离子相对于变形后晶胞中心的实际偏移为
$$
\begin{aligned}
\delta'&=\lambda'b'\\
&=(\lambda+\tau\varepsilon)b(1+\varepsilon)\\
&=\lambda b+b(\lambda+\tau)\varepsilon+b\tau\varepsilon^2.
\end{aligned}
$$
因此一阶位移增量为 $\Delta\delta=b(\lambda+\tau)\varepsilon+O(b\varepsilon^2)$。其中 $\lambda\varepsilon$ 来自原有偏移随晶胞伸长，$\tau\varepsilon$ 来自偏移比例本身改变。这两项不能在单个偶极矩中漏掉。

题设要求的是单位体积极化，不是仅有 $\delta'$。横向尺寸 $a$ 固定，变形后体积也必须写为
$$
V'_{\mathrm{cell}}=a^2b'=a^2b(1+\varepsilon).
$$
上面的展开只是说明实际位移的来源；下一步保留乘积形式做消元，比先截断后相除更直接。

**第7步：同时更新偶极矩与体积，求极化增量。**

拉伸后的铅、氧位置仍关于新的几何中心成对对称，所以它们的偶极矩仍为零。钛离子的偶极矩变为 $p'_{\mathrm{cell},z}=4e\lambda'b'$。于是
$$
\begin{aligned}
P'
&=\frac{p'_{\mathrm{cell},z}}{V'_{\mathrm{cell}}}\\
&=\frac{4e(\lambda+\tau\varepsilon)b(1+\varepsilon)}
        {a^2b(1+\varepsilon)}\\
&=\frac{4e}{a^2}(\lambda+\tau\varepsilon).
\end{aligned}
$$
此处利用分子、分母相同因子的精确约分，只要求 $b'>0$。没有把体积固定，也没有把 $\varepsilon^2$ 项任意删除。模型的线性适用范围仍由给定本构关系决定，不能据此把任意大拉伸视为线性压电响应。

从 $P'$ 减去 $P_0$，得到
$$
\begin{aligned}
\Delta P
&=P'-P_0\\
&=\frac{4e}{a^2}(\lambda+\tau\varepsilon)
 -\frac{4e\lambda}{a^2}\\
&=\frac{4e\tau}{a^2}\varepsilon.
\end{aligned}
$$
实际位移里曾出现的 $\lambda\varepsilon$ 项不再出现在 $\Delta P$ 中，是因为体积也按同一比例伸长。它不是一开始就可以从偶极矩增量中省略的项。

**第8步：用微分形式独立检查长度项的抵消。**

记 $p_{\mathrm{cell}}=4e\lambda b$，$V=a^2b$，固定 $a$。对 $P=p_{\mathrm{cell}}/V$ 求微分，使用商的微分法则：
$$
\mathrm dP=\frac{V\,\mathrm dp_{\mathrm{cell}}-p_{\mathrm{cell}}\,\mathrm dV}{V^2}.
$$
逐项计算
$$
\mathrm dp_{\mathrm{cell}}=4e(b\,\mathrm d\lambda+\lambda\,\mathrm db),
\qquad \mathrm dV=a^2\,\mathrm db.
$$
代回并展开分子：
$$
\begin{aligned}
\mathrm dP
&=\frac{a^2b\cdot4e(b\,\mathrm d\lambda+\lambda\,\mathrm db)
      -4e\lambda b\cdot a^2\,\mathrm db}{a^4b^2}\\
&=\frac{4ea^2b^2\,\mathrm d\lambda
      +4ea^2b\lambda\,\mathrm db
      -4ea^2b\lambda\,\mathrm db}{a^4b^2}\\
&=\frac{4e}{a^2}\,\mathrm d\lambda.
\end{aligned}
$$
两个含 $\mathrm db$ 的项明确互相抵消。若只取 $\mathrm dP=\mathrm dp_{\mathrm{cell}}/V$，就会漏掉体积变化项，并得到错误的额外贡献 $4e\lambda\varepsilon/a^2$。

**第9步：消去应变，建立极化与应力的关系。**

应力式 $\Delta p=Y\varepsilon$ 给出
$$
\varepsilon=\frac{\Delta p}{Y},\qquad
\Delta\lambda=\frac\tau Y\Delta p.
$$
把它代入第7步的极化增量：
$$
\Delta P=\frac{4e\tau}{a^2Y}\Delta p.
$$
再由第（1）问 $P_0=4e\lambda/a^2$，在 $\lambda\ne0$ 时有 $4e/a^2=P_0/\lambda$，故
$$
\boxed{\Delta P=\frac{\tau P_0}{\lambda Y}\Delta p}.
$$
$Y>0$，拉伸应力为正时应变为正。但 $\tau$ 的符号由题设常数决定，不能凭“拉伸”就断言极化一定增大。只有 $\tau>0$ 时，正向拉伸才增大正向极化；$\tau<0$ 时反之。

**第10步：由表面法线确定束缚电荷的正负。**

取宏观薄板上表面外法线为 $+\boldsymbol e_z$，下表面为 $-\boldsymbol e_z$。设板内极化为 $\boldsymbol P=P\boldsymbol e_z$，侧面法线与它垂直，于是
$$
\begin{aligned}
\sigma_{\mathrm b}^{\mathrm{top}}&=+P,\\
\sigma_{\mathrm b}^{\mathrm{bottom}}&=-P,\\
\sigma_{\mathrm b}^{\mathrm{side}}&=0.
\end{aligned}
$$
面积为 $S$ 时，上下两面的束缚电荷分别为 $PS$ 与 $-PS$，总和仍为零。中性并没有消除两面电荷的空间分离。极化增大后，上面增加 $S\Delta P$，下面减少同量电荷，因此两面产生指向负 $z$ 的场增量。

图2-3画出没有自由电荷补偿的特例。它是宏观宽薄板，不是把图2-1的单个晶胞直接当作宏观电场区域。图中厚度 $L$ 沿极化轴，板内蓝色箭头指向负 $z$。

![图2-3 均匀极化薄板的束缚面电荷与内部去极化场。](../figures/slab-02.png){width=79%}

后续方程使用图中的法线与符号：上表面 $\Delta\sigma_{\mathrm b}=+\Delta P$，下表面为 $-\Delta P$，所以两面造成的内部场增量方向相同，均指向负 $z$。若初始有固定自由表面电荷，它们会改变初始场，却不改变这对增量的方向。

**第11步：用电位移边界写清开路条件。**

忽略边缘场后，内部电位移沿 $z$ 方向。跨过上表面取一只薄柱形高斯盒，设上、下底面积都是 $S$。盒侧面不贡献电位移通量，故
$$
(D_{\mathrm{out},z}-D_{\mathrm{in},z})S
=\sigma_{\mathrm f}^{\mathrm{top}}S.
$$
约去 $S$ 得
$$
D_{\mathrm{in},z}=D_{\mathrm{out},z}-\sigma_{\mathrm f}^{\mathrm{top}}.
$$
式中的 $\sigma_{\mathrm f}^{\mathrm{top}}$ 只计自由电荷。束缚电荷已经通过 $P$ 进入 $D_z=\varepsilon_0E_z+P$，不能再次加入右端。

开路意味着没有通过外部回路转移的自由电荷。横向尺寸不变，使表面积 $S$ 不变，因此自由面电荷密度的增量为零。又因为外部电边界固定，$\Delta D_{\mathrm{out},z}=0$，从而
$$
\begin{aligned}
\Delta D_{\mathrm{in},z}
&=\Delta D_{\mathrm{out},z}-\Delta\sigma_{\mathrm f}^{\mathrm{top}}\\
&=0-0=0.
\end{aligned}
$$
不需要初始 $D_{\mathrm{in},z}=0$。无自由电荷、无外部场的特例确实给出 $D_z=0$；初始已有固定补偿电荷的开路样品，$D_z$ 可以不为零，但增量仍为零。真正使用的是“固定电边界下的增量条件”，不是仅凭晶胞中性得出的结论。

**第12步：从本构关系得到电场增量，筛定负号。**

设初始内部场为 $E_{0,z}$，初始电位移为 $D_0$。初、末状态分别满足
$$
\begin{aligned}
D_0&=\varepsilon_0E_{0,z}+P_0,\\
D_0&=\varepsilon_0(E_{0,z}+\Delta E_z)+(P_0+\Delta P).
\end{aligned}
$$
第二式减去第一式，常量 $D_0,E_{0,z},P_0$ 全部消去，得到
$$
0=\varepsilon_0\Delta E_z+\Delta P.
$$
因此
$$
\Delta E_z=-\frac{\Delta P}{\varepsilon_0}.
$$
当 $\Delta P>0$ 时，$\Delta E_z<0$，与图2-3的束缚电荷增量所产生的方向一致。不能因为原有场可能为零或向上，就把电场增量的符号改成正；增量方向与初始场方向是两个不同问题。

“正压电效应”有时用来指由机械作用产生电响应的直接效应，与由电作用产生形变的逆效应相区别。这个名称不意味着沿任意正轴定义的响应系数都大于零。本题必须保留有向分量中的负号。

**第13步：求出所要求的系数，完成第（2）问。**

将第9步的 $\Delta P$ 代入电场增量式：
$$
\begin{aligned}
\Delta E_z
&=-\frac1{\varepsilon_0}\frac{4e\tau}{a^2Y}\Delta p\\
&=-\frac{4e\tau}{\varepsilon_0a^2Y}\Delta p\\
&=-\frac{\tau P_0}{\varepsilon_0\lambda Y}\Delta p.
\end{aligned}
$$
与定义式 $\Delta E_z=\alpha\Delta p$ 比较 $\Delta p$ 的系数，即得
$$
\boxed{\alpha=-\frac{\tau P_0}{\varepsilon_0\lambda Y}}.
$$
也可以保留微观参数形式 $\alpha=-4e\tau/(\varepsilon_0a^2Y)$。这不是两个不同答案，而是利用第（1）问代换后的同一结果。后一形式不含 $1/\lambda$，有助于避免把 $P_0/\lambda$ 的联动变化误判为奇点。

所求系数是小应变响应系数。如果 $\Delta p=0$，定义应理解为相应的线性导数 $\alpha=\mathrm dE_z/\mathrm dp$，不需要在零增量时计算 $0/0$。在线性范围内，任意非零微小应力的比值都会给出同一系数。

**第14步：通过两张带电平面的电场独立复核。**

一张无限均匀带电面在两侧产生的电场大小为 $|\sigma|/(2\varepsilon_0)$，正面向外、负面向内。上表面新增 $+\Delta P$，在板内下侧产生负向场 $-\Delta P/(2\varepsilon_0)$；下表面新增 $-\Delta P$，在板内上侧也产生负向场 $-\Delta P/(2\varepsilon_0)$。两项相加：
$$
\begin{aligned}
\Delta E_z
&=-\frac{\Delta P}{2\varepsilon_0}
  -\frac{\Delta P}{2\varepsilon_0}\\
&=-\frac{\Delta P}{\varepsilon_0}.
\end{aligned}
$$
板外两项方向相反，互相抵消，所以增量场在板外为零。这也说明第11步外部电边界不变与平面薄板模型相容。

这个复核直接从实际电荷和场的方向出发，不沿用电位移公式，因此既能检查负号，也能检查系数。若只算一张面，会少一个因子 $2$；若把正负两面误当成在板内抵消，会错误地得到零响应。

<!-- KEEP_STUDENT_START -->

**第15步：完成单位、极限及适用条件检查。**

由 $\Delta E_z=\alpha\Delta p$，系数单位应为
$$
[\alpha]=\frac{\mathrm{V/m}}{\mathrm{Pa}}
=\frac{\mathrm{V\,m}}{\mathrm N}
=\frac{\mathrm{m^2}}{\mathrm C}.
$$
又因为 $[P_0]=\mathrm{C/m^2}$，$[\varepsilon_0]=\mathrm{C^2/(N\,m^2)}$，$[Y]=\mathrm{N/m^2}$，$\lambda,\tau$ 无量纲，所以
$$
\left[\frac{\tau P_0}{\varepsilon_0\lambda Y}\right]
=\frac{\mathrm{C/m^2}}
       {\mathrm{C^2/m^4}}
=\frac{\mathrm{m^2}}{\mathrm C},
$$
与定义一致。量纲只能判断单位，不会判断正负号，正负号已由两种独立电场路径核对。

令 $\tau=0$，偏移比例不受应变影响，虽然 $b$ 与实际位移一起变长，$P$ 仍不变，所以 $\alpha=0$。令 $Y\to\infty$，固定应力难以产生应变，响应趋于零。令 $\Delta p\to0$，所有增量趋于零，系数保持有限。这些检验分别对应微观响应、机械刚度与线性极限。

若让 $\lambda\to0$，必须同时使用 $P_0=4e\lambda/a^2$，于是 $P_0/\lambda=4e/a^2$；不能固定 $P_0$ 不变后单独令 $\lambda\to0$，那样已经违反第（1）问的关系。此时是否仍有给定的非零 $\tau$，属于材料模型的额外问题，不由本题公式自行决定。

本解答适用于指定的单一方向均匀极化、固定横截面积、开路平面薄板及小应变模型。不同样品形状、短路边界、横向收缩或额外介电响应都会改变电场系数。真实极化结构是否稳定，不由这道简化模型保证；不能把模型结果直接当作任意压电器件的工作参数。

<!-- KEEP_STUDENT_END -->

## 六、关键洞察

**洞察1：长轴消失反映的是密度守恒结构，而不是遗漏几何量。**

沿长轴排一列 $N_z$ 个相同晶胞，每个横截面积为 $a^2$，总长度为 $L=N_zb$。单胞偶极矩为 $4e\lambda b$，于是这一列的偶极矩为 $N_z4e\lambda b=4e\lambda L$，体积为 $a^2L$，二者之比仍为 $4e\lambda/a^2$。

拉伸保持 $N_z$ 与 $a$ 不变，长度变化同时影响总偶极矩与总体积。真正改变极化密度的是离子偏移比例 $\lambda$，而不是轴长本身。这个列模型与第8步商的微分分别从空间计数和局部变化两方面揭示同一抵消，不应把它们当作“体积不变”的论据。

**洞察2：宏观中性只约束总电荷，不能决定去极化系数。**

为了看清边缘条件的作用，取没有自由表面电荷的均匀极化圆柱薄片，半厚度 $h=L/2$，半径 $R$。两端面的束缚电荷密度仍为 $+P$ 与 $-P$。图2-4中，$s$ 是环元的半径，中心 $O$ 到上端面的轴向距离为 $h$。

![图2-4 有限圆盘的轴上电场积分几何。](../figures/disks-02.png){width=62%}

上端面半径为 $s$、宽度为 $\mathrm ds$ 的环元面积为 $2\pi s\,\mathrm ds$，带电量为 $\mathrm dq=P\,2\pi s\,\mathrm ds$。到中心的距离为 $\sqrt{s^2+h^2}$。环元各点的横向场成对抵消，轴向投影因子为 $h/\sqrt{s^2+h^2}$。因此上盘产生
$$
\begin{aligned}
\mathrm dE_z^{\mathrm{top}}
&=-\frac{1}{4\pi\varepsilon_0}
  \frac{P\,2\pi s\,\mathrm ds}{s^2+h^2}
  \frac{h}{\sqrt{s^2+h^2}}\\
&=-\frac{P}{2\varepsilon_0}
  \frac{hs\,\mathrm ds}{(s^2+h^2)^{3/2}}.
\end{aligned}
$$
下盘带负电，场指向下盘，仍为负 $z$，且大小相等。两盘相加后，积分得到
$$
E_z(0)=-\frac P{\varepsilon_0}
\int_0^R\frac{hs}{(s^2+h^2)^{3/2}}\,\mathrm ds.
$$
令 $u=s^2+h^2$，则 $\mathrm du=2s\,\mathrm ds$，积分上下限为 $h^2$ 与 $R^2+h^2$。逐步化简：
$$
\begin{aligned}
\int_0^R\frac{hs}{(s^2+h^2)^{3/2}}\,\mathrm ds
&=\frac h2\int_{h^2}^{R^2+h^2}u^{-3/2}\,\mathrm du\\
&=\frac h2\left[-2u^{-1/2}\right]_{h^2}^{R^2+h^2}\\
&=-\frac h{\sqrt{R^2+h^2}}+\frac h{\sqrt{h^2}}\\
&=1-\frac h{\sqrt{R^2+h^2}},
\end{aligned}
$$
最后一行用了 $h>0$。故
$$
E_z(0)=-\frac P{\varepsilon_0}
\left(1-\frac h{\sqrt{R^2+h^2}}\right).
$$
令 $R/h\to\infty$，括号趋于 $1$，才恢复无限薄板结果。有限圆柱中心的系数不同，其他位置的场也不必相同，但所有这些样品都可以整体中性。不能用中性替代形状条件。

本积分用于核验固定几何下的电场，不直接当作有限圆柱拉伸后的压电系数。若拉伸使 $h$ 改变，括号里的几何因子也会改变，求响应时还需对它求导。只把本题的 $\alpha$ 乘以一个固定几何因子，会遗漏基线极化与形状变化的耦合项。

**洞察3：开路保持的是自由电荷条件，而不是电场为零。**

在本题固定面积与外部边界下，开路给出 $\Delta D_z=0$，所以 $\varepsilon_0\Delta E_z+\Delta P=0$。短路则由连接回路维持电势差为零，在均匀场薄板模型中 $E_z=0$，因而 $\Delta D_z=\Delta P$。两种情况下产生了相同的给定微观极化增量，但外部能否补充自由电荷不同，导致一个表现为场增量，另一个表现为电极电荷转移。

如果既要求短路后的 $E_z=0$，又沿用开路的 $\Delta D_z=0$，就会错误地强迫 $\Delta P=0$。这种矛盾不是压电模型出错，而是把两种互不相同的边界条件同时用了。

## 七、易错点

把共享离子完整归入一个晶胞。诊断方法是先算 $2e-6e+4e$，确认中性；角点与面心的共享份额分别是 $1/8$ 与 $1/2$，不能互换。

把“五个氧形成四棱锥”理解成晶胞总共只有五个氧。上半八面体只描述钛偏移所处的空间区域，下方面心仍有第六个氧。漏掉它既破坏图2-1的对称结构，也破坏电荷核对。

把 $p_{\mathrm{cell}}$ 与应力 $\Delta p$ 混为同一个量。前者单位是 $\mathrm{C\,m}$，后者是 $\mathrm{Pa}$；所有微观偶极矩都保留下标，变形参数 $\lambda$ 无量纲。

更新钛离子实际位移却保留旧体积。这样会留下多余的 $\lambda\varepsilon$ 项。必须计算 $4e\lambda'b'/(a^2b')$，或完整使用商的微分，不能只算分子变化。

认为“开路”意味着电场为零。开路禁止回路中的自由电荷交换；零电势差是短路条件。自由电荷密度固定还依赖面积固定，若横向面积改变，仅有总电荷固定不够。

把总中性当成 $D_z=0$ 的充分条件。中性只意味着整个样品的净电荷为零；$D_z$ 的具体值还需形状、外部场和自由表面电荷。解析只要求 $\Delta D_z=0$，没有强行将初始 $D_0$ 设为零。

漏掉电场增量中的负号或一张面的贡献。按图2-3分别追踪上下两面的场方向：在板内它们同向，在板外反向。$\Delta P>0$ 时 $\Delta E_z<0$，系数中不能写成正号。

把局部单胞高度 $b$ 当成宏观样品厚度。第（1）、（2）问的最终系数不需要宏观厚度；若求端面电势差，应使用 $L=N_zb$，并把拉伸引起的 $L$ 变化计入。

在 $\lambda\to0$ 检验中将 $P_0$ 保持不变，得到虚假的发散。$P_0$ 与 $\lambda$ 由第（1）问绑定，应先换回 $4e\tau/(\varepsilon_0a^2Y)$ 再讨论极限。

## 八、课堂讲解建议

课堂先从一个离散中性体系开始，不先展示最终压电系数。让学生把八个角点、六个面心与一个中心离子的归属电荷分别算清，并指出第六个下方面心氧的位置。教师用三维图2-1检查他们是否把上方四棱锥误读成整个晶胞。

板书分成微观与宏观两栏。微观栏写 $p_{\mathrm{cell}}\to P$，宏观栏写 $\sigma_{\mathrm b}\to E_z$。微观中性与宏观边界各自写在对应栏，不用一条“中性所以电场……”跨过两种尺度。这样可以避免学生把原点不变性当成电场条件。

解析第6至第8步适合保留两种写法。先让学生计算实际位移的一阶增量，注意其中包含 $\lambda$ 与 $\tau$ 两项；再更新体积，把 $\lambda$ 项抵消出来。教师不要提前省略这个看似多余的项，因为它正是理解“单胞偶极矩变大不一定使极化密度变大”的关键。

电场负号的课堂检查用图2-3，不仅让学生背诵 $D=\varepsilon_0E+P$。分别判断上正面、下负面在板内造成的场方向，再回到增量式核对。板书最后把“开路：固定自由电荷”和“短路：固定端面电势差”并排写出，不同时施加两者。

变式按依次改变电边界、横向几何和介电响应的顺序展开。每次只改变一个假设，保留其余条件；让学生指出是哪一步方程要改，而不是直接给最终式添加一个经验系数。端面电势差的变式再练一次乘积求导，检查基线场乘厚度变化的项是否遗漏。

## 九、变式训练

**变式1：同样的微观响应，在理想短路条件下会测到什么？**

保留本题固定 $a$ 的晶胞模型，薄板两端覆盖理想电极并用导线短接，面积为 $S$。忽略边缘场，求电场增量与两电极自由电荷增量。这里电极可交换自由电荷，不再采用开路条件。

短路保持 $U=0$，均匀板内 $E_z=0$，所以 $\Delta E_z=0$。微观极化的给定关系仍为
$$
\Delta P=\frac{4e\tau}{a^2Y}\Delta p.
$$
由本构式，$\Delta D_z=\Delta P$。外部场为零时，上表面边界 $D_z=-\sigma_{\mathrm f}^{\mathrm{top}}$，于是
$$
\begin{aligned}
\Delta Q_{\mathrm f}^{\mathrm{top}}
&=-S\Delta P=-\frac{4e\tau S}{a^2Y}\Delta p,\\
\Delta Q_{\mathrm f}^{\mathrm{bottom}}
&=+S\Delta P=+\frac{4e\tau S}{a^2Y}\Delta p.
\end{aligned}
$$
当 $\tau\Delta p>0$ 时，上电极获得负自由电荷，下电极获得等量正自由电荷，它们分别补偿增加的正、负束缚电荷。通过外部回路转移的电荷量大小为 $S|\Delta P|$，不是两电极变化绝对值之和 $2S|\Delta P|$；同一批电荷在两端各记录了一次。

答案为 $\boxed{\Delta E_z=0}$，两电极自由电荷增量如上。若以转移电荷密度对应力的系数描述短路响应，其大小涉及 $4e|\tau|/(a^2Y)$，单位为 $\mathrm{C/N}$，与本题开路场系数的 $\mathrm{m^2/C}$ 不同，不能混用。

**变式2：横向允许泊松收缩，开路系数如何变化？**

令小应变为 $\varepsilon$，两个横向尺寸变为 $a'=a(1-\nu\varepsilon)$，长轴仍为 $b'=b(1+\varepsilon)$，偏移参数仍为 $\lambda'=\lambda+\tau\varepsilon$。取无自由表面电荷、无外部场的开路宽薄板，$\nu$ 为给定泊松比。求一阶系数。

先算真实体积与偶极矩，相除得
$$
\begin{aligned}
P'
&=\frac{4e(\lambda+\tau\varepsilon)b(1+\varepsilon)}
 {a^2(1-\nu\varepsilon)^2b(1+\varepsilon)}\\
&=\frac{4e(\lambda+\tau\varepsilon)}{a^2(1-\nu\varepsilon)^2}.
\end{aligned}
$$
利用泰勒展开 $(1-x)^{-2}=1+2x+O(x^2)$，得到
$$
\begin{aligned}
P'
&=\frac{4e}{a^2}(\lambda+\tau\varepsilon)
 [1+2\nu\varepsilon+O(\varepsilon^2)]\\
&=P_0+\frac{4e}{a^2}(\tau+2\nu\lambda)\varepsilon
 +O(\varepsilon^2).
\end{aligned}
$$
因此 $\Delta P=P_0(\tau/\lambda+2\nu)\Delta p/Y$。这里无自由表面电荷，使 $D_z=0$ 不受面积变化影响，所以仍有 $\Delta E_z=-\Delta P/\varepsilon_0$，得到
$$
\boxed{\alpha_\nu=-\frac{P_0}{\varepsilon_0Y}
 \left(\frac\tau\lambda+2\nu\right)}.
$$
$2\nu$ 项来自两个横向长度的收缩，不来自长轴项；令 $\nu=0$ 恢复本题。即使 $\tau=0$，横截面积减小仍会增大极化密度，从而产生场增量。

如果初始有非零固定电极电荷，面积收缩会使自由面电荷密度改变，$\Delta D_z$ 就不再为零。本变式特意选无自由表面电荷，避免将“总自由电荷固定”误替换成“自由面电荷密度固定”。

**变式3：计入线性背景介电响应。**

保持本题固定横向尺寸与开路边界，另取与应变无关的背景相对介电常数 $\varepsilon_r$。将位移引起的自发极化记为 $P_{\mathrm{sp}}$，其初始值仍是 $P_0$，增量仍由给定离子模型求出。背景极化为 $P_{\mathrm{bg}}=\varepsilon_0(\varepsilon_r-1)E_z$，求新的开路系数。

总极化为 $P_{\mathrm{sp}}+P_{\mathrm{bg}}$，本构关系变为
$$
\begin{aligned}
D_z
&=\varepsilon_0E_z+P_{\mathrm{sp}}
 +\varepsilon_0(\varepsilon_r-1)E_z\\
&=\varepsilon_0\varepsilon_rE_z+P_{\mathrm{sp}}.
\end{aligned}
$$
开路固定面积与外部边界仍给出 $\Delta D_z=0$，且 $\varepsilon_r$ 为常数，故
$$
\begin{aligned}
0&=\varepsilon_0\varepsilon_r\Delta E_z+\Delta P_{\mathrm{sp}},\\
\Delta E_z&=-\frac{\Delta P_{\mathrm{sp}}}{\varepsilon_0\varepsilon_r}\\
&=-\frac{\tau P_0}{\varepsilon_0\varepsilon_r\lambda Y}\Delta p.
\end{aligned}
$$
答案为
$$
\boxed{\alpha_r=-\frac{\tau P_0}
 {\varepsilon_0\varepsilon_r\lambda Y}}.
$$
令 $\varepsilon_r=1$ 恢复原模型。不能把 $P_0$ 同时当作已经包含背景响应的总极化，又把相同响应计入 $\varepsilon_r$，那会重复计算。若 $\varepsilon_r$ 也随应变改变，还需保留 $\varepsilon_0E_{0,z}\Delta\varepsilon_r$ 的一阶项；本变式只考虑 $\varepsilon_r$ 为常数的情形。

**变式4：拉伸后端面电势差的增量是否等于 $-L\Delta E_z$？**

回到本题固定 $a$ 的模型，取无自由表面电荷的宽薄板，沿厚度排有 $N_z$ 个晶胞。初始厚度 $L_0=N_zb$，拉伸后 $L'=L_0(1+\varepsilon)$。定义电势差 $U=\varphi_{\mathrm{top}}-\varphi_{\mathrm{bottom}}$，求其一阶增量。

均匀场下，由电势差的定义
$$
U=-\int_{\mathrm{bottom}}^{\mathrm{top}}E_z\,\mathrm dz=-E_zL.
$$
无自由表面电荷时，$E_z=-P/\varepsilon_0$，所以 $U=PL/\varepsilon_0$。初始电势差为 $U_0=P_0L_0/\varepsilon_0$。代入拉伸后的极化与厚度：
$$
\begin{aligned}
U'
&=\frac{L_0}{\varepsilon_0}
 \left(P_0+\frac{4e\tau}{a^2}\varepsilon\right)(1+\varepsilon)\\
&=\frac{P_0L_0}{\varepsilon_0}
 +\frac{L_0}{\varepsilon_0}
 \left(P_0+\frac{4e\tau}{a^2}\right)\varepsilon
 +O(U_0\varepsilon^2)\\
&=U_0+U_0\left(1+\frac\tau\lambda\right)\varepsilon
 +O(U_0\varepsilon^2).
\end{aligned}
$$
因此
$$
\boxed{\Delta U=\frac{U_0}{Y}
 \left(1+\frac\tau\lambda\right)\Delta p
+O\!\left(U_0(\Delta p/Y)^2\right)}.
$$
若只需线性导数，$\mathrm dU/\mathrm dp=(U_0/Y)(1+\tau/\lambda)$。也可由乘积微分独立检查：
$$
\mathrm dU=-L_0\,\mathrm dE_z-E_{0,z}\,\mathrm dL.
$$
第一项来自场变，第二项来自长度变。此处 $E_{0,z}=-P_0/\varepsilon_0$，$\mathrm dL=L_0\,\mathrm dp/Y$，两项相加恰好得到上式。

令 $\tau=0$ 时，本题场响应为零，但端面电势差仍按长度增加，$\Delta U=U_0\Delta p/Y$。这不矛盾：场强是单位长度上的电势变化，样品更厚时，总电势差仍可增大。若初始场已被补偿到零，长度变化项才在一阶消失；不能把这个特殊条件推广到所有开路样品。

上述电势差结论采用了初始无补偿自由电荷的条件。若两电极初始带有等量异号、随后固定不变的补偿电荷，保持面积不变时，可令初始内部电位移为任意常数 $D_0$。此时
$$
E_{0,z}=\frac{D_0-P_0}{\varepsilon_0},\qquad
\frac{\mathrm dE_z}{\mathrm dp}
=-\frac{\tau P_0}{\varepsilon_0\lambda Y}.
$$
把两项分别代入乘积微分，得到一般的电势差导数
$$
\begin{aligned}
\frac{\mathrm dU}{\mathrm dp}
&=-L_0\frac{\mathrm dE_z}{\mathrm dp}
 -E_{0,z}\frac{L_0}{Y}\\
&=\frac{L_0}{\varepsilon_0Y}
 \left(\frac{\tau P_0}{\lambda}+P_0-D_0\right).
\end{aligned}
$$
令 $D_0=0$，恢复无自由电荷时的答案；令 $D_0=P_0$，初始场被恰好补偿，厚度变化项消失，只剩 $L_0\tau P_0/(\varepsilon_0\lambda Y)$。这两种初始状态具有同一个开路场系数，却具有不同的电势差系数，差别完全来自已经写明的基线场。


