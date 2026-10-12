# 第3题

<!-- question-start -->

气球膜与液体表面常被用来比较：气球膜是一层弹性膜，肥皂泡膜包含两个气液界面。另一个重要区别是，气液界面的表面张力通常具有各向同性，而弹性薄膜中的张力可以随方向不同。例如，圆柱形香肠因内部压强过大而破裂时，肠衣通常沿圆柱轴向裂开，而不是沿圆周裂开。

（1）将肠衣建模为弹性固体薄膜。圆柱半径为 $r$，长度为 $l\gg r$，内部压强比外部高 $\Delta p$。膜上沿一条切线每单位长度所传递的拉力称为张力。含圆柱中轴线的纵切面与表面交于直线，将跨过这条线的单位长度张力记作 $\sigma_1$；垂直于中轴线的横切面与表面交于圆，将跨过该圆的单位长度张力记作 $\sigma_2$。求 $\sigma_1,\sigma_2$，并解释纵向裂开的原因。

（2）将香肠弯成圆环面：管的横截面为半径 $r$ 的小圆，各小圆圆心构成半径 $R$ 的大圆。考虑小圆横截面上与大圆平面成角 $\theta$ 的点 $A$，角度的起始方向按图3-2取内侧方向。记跨过横截面交线的单位长度张力为 $\sigma_1(\theta)$。通过 $A$ 的外法向且与该横截面垂直的纵截面，与表面在 $A$ 附近相交；记跨过其交线的单位长度张力为 $\sigma_2(\theta)$。压差与两主张力满足

$$
\Delta p=\frac{\sigma_1}{r_1}+\frac{\sigma_2}{r_2},
$$

其中曲率半径须与相应张力的作用方向配对，并保留凹凸曲率的符号。求 $\sigma_1(\theta),\sigma_2(\theta)$，并说明何处最容易裂开。

![图3-1 圆柱薄膜的纵切面与横切面。](../figures/question-03.png){width=68%}

![图3-2 圆环面及从内侧起算的子午角。](../figures/torus-03.png){width=92%}

<!-- question-end -->

## 一、题型定位

这是薄膜容器的局部张力与整体压力平衡问题。圆柱用半筒和闭端截面分别求两个方向的膜力；环面用环形膜带的竖向合力先求一个张力，再用带符号的主曲率平衡求另一个。仅用“压强乘面积”而不指明投影方向、切边及拉力方向，会遗漏系数或把两个张力交换。

这里的 $\sigma_1,\sigma_2$ 是膜张力，单位为 $\mathrm{N\,m^{-1}}$，不是通常按单位截面积计量的材料应力。若膜厚为 $t$，相应的材料正应力才是 $\sigma_i/t$，单位为 $\mathrm{Pa}$。两问中的下标按各自切线定义使用，不凭“纵向”或“横向”两个字猜实际拉力方向。

## 二、知识点

压差作用于薄膜的外法向；曲面分布力的投影与积分；膜张力跨过切线传递、且在切平面内垂直于切线；闭端容器的端面压力载荷；两主方向的曲率与局部法向平衡；内凹曲率的负号；连续极限与除零条件；张力极值和裂缝方向；大环半径极限中的局部圆筒对应。

计算采用薄膜静力学，忽略膜厚、弯曲刚度及自身重力；内部压差均匀，记 $p=\Delta p>0$。环面取 $R>r>0$，以保证中心孔存在且表面光滑。只计算稳态膜力，不自行引入未给出的弹性模量或把给定形状的平衡问题改成形变求解。

## 三、物理图像

压力把薄膜向外推，膜张力沿曲面切向拉邻近膜块。相对的两边张力大小可能相同，但方向会因曲面弯曲而不同，其合力可以沿法向抵抗压力。液体界面的各向同性张力是同一个标量；弹性膜的两个主张力可以不同，不能直接设 $\sigma_1=\sigma_2$。

图3-1中沿轴向的纵切线所传递的力是环向力，沿圆周的横切线所传递的力是轴向力。因此圆柱的 $\sigma_1$ 为环向张力，$\sigma_2$ 为轴向张力。图3-2中小圆所在横截面的交线沿子午方向，跨线的 $\sigma_1$ 沿大圆环向；另一条交线沿平行圈，跨线的 $\sigma_2$ 沿小圆子午方向。力方向与切线方向相互垂直。

环面内侧在子午方向是凸曲率、在大圆环向却是凹曲率。一部分环向膜力的法向合力会向外，而不是抵消压力。因此内侧所需的子午张力较大。这一几何原因必须通过真实空间法向和两切向判断，不能把甜甜圈的二维外轮廓当成两个同向弯曲的圆。

## 四、解题入口

先明确每条截线传递哪一方向的力，再选能隔离未知张力的整体膜块。圆柱横向取半筒，轴向取含闭端的筒段；环面先取某平行圈到顶部平行圈之间的上半膜带，利用顶部子午张力没有竖向分量这一条件。

求得环面的子午张力 $\sigma_2(\theta)$ 后，再建立外法向下的曲率符号，代入法向平衡求环向张力 $\sigma_1(\theta)$。最后比较主张力及其随 $\theta$ 的变化，区分“哪个力最大”“哪个位置先到限”与“裂缝沿哪个方向”三个问题。

## 五、解析

**第1步：明确膜力定义、静力模型与端部条件。**

取任意一条膜面切线，长为 $\mathrm d\ell$，相邻膜块通过它传递的拉力大小为 $\sigma\,\mathrm d\ell$。拉力沿膜面，垂直于这条切线；$\sigma$ 是每单位切线长度的力，所以压力 $p$ 与 $\sigma$ 的量纲相差一个长度。

圆柱采用香肠的闭端模型：端面受到的压差合力由圆柱侧壁的轴向膜力承担。$l\gg r$ 使中段远离端部局部应力变化，但端面总载荷仍传到中段，不可因为圆柱很长而删掉。若另有刚性装置独立承担端力，或者使用开放管段，轴向张力便需要另给边界载荷；下面的 $\sigma_2$ 结论有明确的闭端条件。

膜的质量在静态方程中不出现。压差力为 $p\,\mathrm dS\,\mathbf n$，其中 $\mathbf n$ 是由内部指向外部的单位法向。每一处压力方向沿本处法向，不将整个曲面上的压力都画成同一方向。

**第2步：对半圆柱沿横向投影，求环向张力。**

沿轴向取中段长度 $h$，再沿含轴平面切出半筒。以该半筒中央向外方向为 $+x$，截面周向角为 $\varphi$，保留范围 $-\pi/2\le\varphi\le\pi/2$。图3-3左侧的两条切边平行轴线，各边的总拉力为 $\sigma_1h$；两力在本次投影中均向内。

![图3-3 半筒横向平衡与闭端筒段轴向平衡。](../figures/cylinder-03.png){width=92%}

侧壁面积微元为 $\mathrm dS=rh\,\mathrm d\varphi$，压力的 $x$ 分量为 $p\,\mathrm dS\cos\varphi$。先积分方向，再与两切边拉力比较：

$$
\begin{aligned}
F_{p,x}
&=\int_{-\pi/2}^{\pi/2}prh\cos\varphi\,\mathrm d\varphi\\
&=prh[\sin\varphi]_{-\pi/2}^{\pi/2}\\
&=2prh,\\
F_{\sigma_1,x}&=-2\sigma_1h,\\
F_{p,x}+F_{\sigma_1,x}&=0.
\end{aligned}
$$

除以 $2h$，得到

$$
\boxed{\sigma_1=pr=r\Delta p}.
$$

积分结果也等于压差乘半筒在垂直于 $x$ 平面上的投影面积 $2rh$。不是把半筒实际侧面积 $\pi rh$ 直接乘以同一方向的压力；后者忽略了两侧法向倾斜。

**第3步：保留闭端压差载荷，求轴向张力。**

图3-3右侧取含一端的筒段。端面受压差合力大小为 $p\pi r^2$；侧壁压力方向径向，与轴垂直，不提供轴向分量。横切线是周长 $2\pi r$ 的圆，其各处轴向拉力均指向筒段之外，合力大小为 $2\pi r\,\sigma_2$。

沿轴向静力平衡：

$$
\begin{aligned}
p\pi r^2-2\pi r\,\sigma_2&=0,\\
\sigma_2&=\frac{p\pi r^2}{2\pi r}\\
&=\boxed{\frac{pr}{2}=\frac{r\Delta p}{2}}.
\end{aligned}
$$

式中的 $\pi$ 和一项 $r$ 分别约去。这个二分之一来自“端面面积除以切边周长”，不是肥皂泡的双界面因子。本题弹性膜是单层膜，不额外把张力乘二。

圆柱结果为 $\sigma_1=2\sigma_2$。若膜厚、质量及许用张力处处相同，且两个方向的强度没有显著差别，环向拉力先达到强度上限。裂缝两侧主要被该力向圆周方向拉开，因此裂缝延伸方向与环向力垂直，即沿轴线纵向。并不是“轴向张力最大所以纵裂”。

**第4步：固定环面的角度、空间坐标及两个主方向。**

以大圆平面为 $z=0$，其中心轴为 $z$ 轴。大圆上的周向角记作 $\varphi$，距轴的柱坐标半径记作 $s$。在一个子午小圆中，$\theta=0$ 指向中心孔，$\theta=\pi$ 指向最外侧；上半部 $0<\theta<\pi$，下半部按同一有向角继续。

图3-2中的小圆圆心距轴 $R$，点 $A$ 相对圆心的水平位移为 $-r\cos\theta$，竖向位移为 $r\sin\theta$。因此

$$
\boxed{s(\theta)=R-r\cos\theta,\qquad z(\theta)=r\sin\theta}.
$$

$s$ 是该点所在平行圈的几何半径，不是小圆半径 $r$。在 $\theta=0,\pi/2,\pi$ 时，依次为 $R-r,R,R+r$。

取柱坐标单位矢量 $\mathbf e_\rho,\mathbf e_\varphi,\mathbf e_z$，则子午切向及外法向为

$$
\begin{aligned}
\mathbf e_\theta
&=\sin\theta\,\mathbf e_\rho+\cos\theta\,\mathbf e_z,\\
\mathbf n
&=-\cos\theta\,\mathbf e_\rho+\sin\theta\,\mathbf e_z.
\end{aligned}
$$

二者内积为零，长度均为一；在内侧 $\theta=0$，外法向朝中心孔，即 $-\mathbf e_\rho$，与空间图一致。环面中的 $\sigma_1$ 沿 $\mathbf e_\varphi$，$\sigma_2$ 沿 $\mathbf e_\theta$；下面不会将切线方向当作力方向。

**第5步：取内侧上膜带，精确求压力的竖向投影。**

先考虑 $0\le\theta<\pi/2$。取该平行圈至顶部平行圈 $\theta=\pi/2$ 之间的整圈膜带。图3-4中的下边界半径为 $s=R-r\cos\theta$，顶部边界半径为 $R$。顶部的子午切向水平，故沿顶部传递的 $\sigma_2$ 没有竖向分量；下边界所受相邻膜的子午拉力向下，其竖向分量每单位周长为 $\sigma_2(\theta)\cos\theta$。

![图3-4 上半环形膜带的压力投影与边界子午拉力。](../figures/cap-03.png){width=92%}

为避免仅凭投影图猜面积，设膜带中间子午角为 $\psi$，面积微元为

$$
\mathrm dS=r\,s(\psi)\,\mathrm d\psi\,\mathrm d\varphi.
$$

法向竖向分量为 $n_z=\sin\psi$。对两个角变量积分：

$$
\begin{aligned}
F_{p,z}
&=\int_0^{2\pi}\int_\theta^{\pi/2}
p\sin\psi\,r(R-r\cos\psi)\,\mathrm d\psi\,\mathrm d\varphi\\
&=2\pi pr\int_\theta^{\pi/2}
(R-r\cos\psi)\sin\psi\,\mathrm d\psi.
\end{aligned}
$$

利用 $s(\psi)=R-r\cos\psi$、$\mathrm ds=r\sin\psi\,\mathrm d\psi$ 换元，积分上下限从 $s$ 到 $R$：

$$
\begin{aligned}
F_{p,z}
&=2\pi p\int_s^R s'\,\mathrm ds'\\
&=2\pi p\left[\frac{(s')^2}{2}\right]_s^R\\
&=\pi p(R^2-s^2).
\end{aligned}
$$

此处 $s'$ 是积分变量，不表示导数。结果正是压差乘图3-4中内半径 $s$、外半径 $R$ 的投影环面积，方向向上。下边界总子午拉力的竖向分量为

$$
F_{\sigma_2,z}=-2\pi s\,\sigma_2(\theta)\cos\theta.
$$

上边界的竖向力为零，膜带又无重力，故

$$
\pi p(R^2-s^2)=2\pi s\,\sigma_2(\theta)\cos\theta.
$$

**第6步：逐项化简并求子午张力。**

在本步范围内 $\cos\theta>0$，可以除以它。先对平方差因式分解：

$$
\begin{aligned}
R^2-s^2
&=(R-s)(R+s),\\
R-s&=r\cos\theta,\\
R+s&=2R-r\cos\theta,\\
R^2-s^2
&=r\cos\theta(2R-r\cos\theta).
\end{aligned}
$$

代入第5步平衡式，约去共同的 $\pi\cos\theta$：

$$
\begin{aligned}
\sigma_2(\theta)
&=\frac{p\,r\cos\theta(2R-r\cos\theta)}
{2s\cos\theta}\\
&=\boxed{\frac{pr(2R-r\cos\theta)}
{2(R-r\cos\theta)}}.
\end{aligned}
$$

将分子拆成 $(R-r\cos\theta)+R$，同一结果也可写成

$$
\sigma_2(\theta)=\frac{pr}{2}
+\frac{prR}{2(R-r\cos\theta)}.
$$

拆分式将用于比较两个张力及求最大值。此时还未求 $\sigma_1$，不能仅根据第（1）问的下标习惯提前把该变量改名。

**第7步：处理外侧、顶部与下半部，不把除零隐藏起来。**

对于 $\pi/2<\theta\le\pi$，取顶部至外侧目标圈的上膜带。压力向上合力为 $\pi p(s^2-R^2)$。目标圈的子午拉力沿 $+\mathbf e_\theta$，其竖向分量因 $\cos\theta<0$ 而向下。因此竖向方程为

$$
\pi p(s^2-R^2)+2\pi s\,\sigma_2(\theta)\cos\theta=0.
$$

移项后仍是

$$
2\pi s\,\sigma_2(\theta)\cos\theta=\pi p(R^2-s^2),
$$

两边均为负值。继续用第6步的平方差，得到相同的正张力式。外侧的两个负号是从受力方向产生的，不对压力大小人为取负。

在 $\theta=\pi/2$，原竖向方程退化为 $0=0$，不能直接除以 $\cos\theta$。从相邻光滑膜带取连续极限：

$$
\sigma_2\left(\frac\pi2\right)
=\lim_{\theta\to\pi/2}
\frac{pr(2R-r\cos\theta)}{2(R-r\cos\theta)}
=pr.
$$

下半部由关于大圆平面的镜面对称给出同一分布；其表达式只含 $\cos\theta$，与上下对称一致。底部 $\theta=3\pi/2$ 的连续值同样为 $pr$。后面的局部法向平衡将独立验证顶部、底部的值。

**第8步：按外法向求两个带符号主曲率。**

图3-5分别标出子午切向、大圆环向和外法向。曲率按“切向沿弧长变化所产生的向内法向合力”取正，写成 $\kappa=-\mathbf n\cdot\mathrm d\mathbf e_t/\mathrm d\ell$。切向的法向变化若朝 $-\mathbf n$，曲率为正；若朝 $+\mathbf n$，则为负。

![图3-5 环面的两主方向、外法向与凹凸曲率。](../figures/geometry-03.png){width=92%}

在子午小圆上，$\mathrm d\ell_\theta=r\,\mathrm d\theta$，并且

$$
\begin{aligned}
\frac{\mathrm d\mathbf e_\theta}{\mathrm d\theta}
&=\cos\theta\,\mathbf e_\rho-\sin\theta\,\mathbf e_z
=-\mathbf n,\\
\kappa_\theta
&=-\mathbf n\cdot\frac{-\mathbf n}{r}
=\frac1r.
\end{aligned}
$$

在平行圈上，$\theta$ 固定，$\mathrm d\ell_\varphi=s\,\mathrm d\varphi$。柱坐标切向满足 $\mathrm d\mathbf e_\varphi/\mathrm d\varphi=-\mathbf e_\rho$，而 $\mathbf n\cdot\mathbf e_\rho=-\cos\theta$，因此

$$
\begin{aligned}
\kappa_\varphi
&=-\mathbf n\cdot
\left(-\frac{\mathbf e_\rho}{s}\right)\\
&=-\frac{\cos\theta}{R-r\cos\theta}.
\end{aligned}
$$

这里必须保留负号。内侧 $\cos\theta>0$ 时，环向曲率为负；外侧 $\cos\theta<0$ 时为正；顶部、底部为零。相应的带符号曲率半径在 $\cos\theta\ne0$ 时为 $-s/\cos\theta$，不是直接取平行圈半径 $s$。顶部、底部应使用零曲率，而不是对无限半径进行不明运算。

两相对边张力的法向合力除以膜块面积，是 $-\sigma_i\kappa_i$。因此压力向外、膜力合力向内的局部平衡为

$$
\boxed{
p=\sigma_1\kappa_\varphi+\sigma_2\kappa_\theta
=-\frac{\sigma_1\cos\theta}{s}+\frac{\sigma_2}{r}}.
$$

与题中的 $p=\sigma_1/r_1+\sigma_2/r_2$ 配对时，$1/r_1=\kappa_\varphi$、$1/r_2=\kappa_\theta$。所配对的是张力实际作用方向，不是跨线名称中的“横”或“纵”。

**第9步：代入子午张力，求环向张力并补连续点。**

先计算局部方程中的差：

$$
\begin{aligned}
\frac{\sigma_2}{r}-p
&=\frac{p(2R-r\cos\theta)}{2s}-p\\
&=\frac{p[(2R-r\cos\theta)-2(R-r\cos\theta)]}{2s}\\
&=\frac{pr\cos\theta}{2s}.
\end{aligned}
$$

局部方程给 $\sigma_1\cos\theta/s=\sigma_2/r-p$。在 $\cos\theta\ne0$ 的地方，

$$
\begin{aligned}
\sigma_1
&=\frac{s}{\cos\theta}
\left(\frac{\sigma_2}{r}-p\right)\\
&=\frac{s}{\cos\theta}\frac{pr\cos\theta}{2s}\\
&=\boxed{\frac{pr}{2}}.
\end{aligned}
$$

差式是 $\sigma_2/r-p$，不是 $p-\sigma_2/r$；这一顺序由第8步的负曲率确定。无论内侧或外侧，约去相同的有符号 $\cos\theta$ 后张力均为正。

在 $\cos\theta=0$ 处，局部方程直接给 $\sigma_2=pr$，与第7步一致；它在单独这一点不含 $\sigma_1$，但光滑膜的连续极限给 $\sigma_1=pr/2$。不能因一条局部方程在某点少一个未知量，就宣称该处环向张力任意。

第（2）问两个张力为

$$
\boxed{
\sigma_1(\theta)=\frac{r\Delta p}{2},\qquad
\sigma_2(\theta)
=\frac{r\Delta p(2R-r\cos\theta)}
{2(R-r\cos\theta)}}.
$$

**第10步：比较两主张力并严格求最大位置。**

用第6步拆分式：

$$
\sigma_2-\sigma_1
=\frac{prR}{2(R-r\cos\theta)}>0.
$$

由于 $R>r$，分母处处为正，所以子午张力处处比环向张力大。比较极值可令 $x=\cos\theta$，$-1\le x\le1$：

$$
\begin{aligned}
\frac{\sigma_2}{pr}
&=f(x)=\frac{2R-rx}{2(R-rx)},\\
f'(x)
&=\frac{(-r)\,2(R-rx)-(2R-rx)(-2r)}
{4(R-rx)^2}\\
&=\frac{rR}{2(R-rx)^2}>0.
\end{aligned}
$$

这是商法则；保留分母导数中的负号后，分子化为 $2rR$。因此最大值在 $x=1$，即最内侧 $\theta=0$；最小值在 $x=-1$，即最外侧 $\theta=\pi$：

$$
\begin{aligned}
\sigma_{2,\max}
&=\frac{pr(2R-r)}{2(R-r)},\\
\sigma_{2,\min}
&=\frac{pr(2R+r)}{2(R+r)},\\
\sigma_2\left(\frac\pi2\right)
&=\sigma_2\left(\frac{3\pi}2\right)=pr.
\end{aligned}
$$

图3-6把张力分布与环面内圈位置对应，内圈的子午拉力最大；下标为 $1$ 的张力则在整圈相同。图中的空间形状与曲线取 $R=3r$ 作为示例，所得公式与最大位置对任意 $R>r$ 均成立。后续判别裂缝时使用这两个实际方向，而非只看数值曲线。

![图3-6 两主张力的分布与内圈易裂方向。](../figures/rupture-03.png){width=92%}

在均匀薄膜、各处许用张力相同且两个方向强度相当的模型下，内圈的子午张力最先到限。裂缝垂直于 $\mathbf e_\theta$，沿内圈的 $\mathbf e_\varphi$ 方向延伸，即沿弯成圆环的香肠的局部轴向；不是沿小圆截面的子午线裂开。若材料方向强度不同或已有局部缺陷，破裂位置还须比较局部张力与对应的许用值，不能只凭最大张力作普遍断言。

<!-- KEEP_TOGETHER_START -->

**第11步：检查量纲、局部圆筒极限与几何边界。**

$pr$ 的单位为 $\mathrm{Pa\,m}=\mathrm{N\,m^{-1}}$；张力式中其余因子均为长度比。法向方程的每一项为张力乘曲率，单位为 $\mathrm{N\,m^{-2}}$，与压差一致。内外侧张力均为正，符合受拉薄膜模型。

<!-- KEEP_TOGETHER_END -->

在 $R/r\to\infty$ 时，令 $\epsilon=r/R\to0$。对子午张力把分子、分母同时除以 $R$：

$$
\begin{aligned}
\sigma_2(\theta)
&=\frac{pr}{2}
\frac{2-\epsilon\cos\theta}{1-\epsilon\cos\theta}\\
&\longrightarrow pr,\qquad
\sigma_1=\frac{pr}{2}.
\end{aligned}
$$

此时一小段弯管接近直圆柱，其局部管轴沿 $\mathbf e_\varphi$，绕管小截面方向沿 $\mathbf e_\theta$。故局部轴向张力为 $pr/2$、局部环绕张力为 $pr$，与第（1）问的物理方向完全一致。两问下标对应不同切线定义，不能只看下标就误判极限。

当 $R\to r^+$ 时，内圈半径 $R-r$ 趋零，负环向曲率和 $\sigma_{2,\max}$ 都增大。数学式显示尖接触附近应力集中，正说明不能把 $R=r$ 的退化环面当作普通光滑薄膜处理。$p=0$ 时两张力均退化为零；若另外施加预张力，则应另给边界和形状条件，本解没有暗中加入它。

## 六、关键洞察

本题的下标不是物理方向的永久名称。两问按不同切线定义两个力，正确做法是先写“切线方向—跨线力方向”的对应，再列面积与周长。由圆柱两整体平衡式得到的 $2:1$ 比例，与环面局部圆筒极限中的 $1:2$ 下标比例并不矛盾，实际的环绕管截面张力始终是 $pr$、沿局部管轴的张力始终是 $pr/2$。

环面也可不先取整体膜带，而从空间膜块的完整矢量平衡独立求两张力。取子午角宽 $\mathrm d\theta$、大圆角宽 $\mathrm d\varphi$ 的小膜块，面积为 $r s\,\mathrm d\theta\,\mathrm d\varphi$。$\theta$ 的两边界长度为 $s\,\mathrm d\varphi$，其传递的是 $\sigma_2$；$\varphi$ 的两边界长度为 $r\,\mathrm d\theta$，其传递的是 $\sigma_1$。

子午两边的合力除以面积，在微元极限下为

$$
\begin{aligned}
\frac{\mathrm d\mathbf F_\theta}{\mathrm dS}
&=\frac1{rs}\frac{\mathrm d}{\mathrm d\theta}
(s\sigma_2\mathbf e_\theta)\\
&=\frac{(s\sigma_2)'}{rs}\mathbf e_\theta
-\frac{\sigma_2}{r}\mathbf n.
\end{aligned}
$$

这里撇号表示对 $\theta$ 求导。第一项保留边界周长 $s$ 的变化，不可只对 $\sigma_2$ 求导。第二项使用 $\mathbf e_\theta'=-\mathbf n$，正是子午曲率所对应的向内力。

环向两边合力为

$$
\frac{\mathrm d\mathbf F_\varphi}{\mathrm dS}
=-\frac{\sigma_1}{s}\mathbf e_\rho.
$$

由第4步两个单位矢量式反解

$$
\mathbf e_\rho
=\sin\theta\,\mathbf e_\theta-\cos\theta\,\mathbf n,
$$

故

$$
\frac{\mathrm d\mathbf F_\varphi}{\mathrm dS}
=-\frac{\sigma_1\sin\theta}{s}\mathbf e_\theta
+\frac{\sigma_1\cos\theta}{s}\mathbf n.
$$

加上压差 $p\mathbf n$，分别令切向与法向分量为零，得到两条不同的平衡式：

$$
\begin{aligned}
(s\sigma_2)'&=r\sin\theta\,\sigma_1=s'\sigma_1,\\
p-\frac{\sigma_2}{r}
+\frac{\sigma_1\cos\theta}{s}&=0.
\end{aligned}
$$

法向式与主解析一致；切向式则约束张力的分布，不能只用一条局部法向式就给两个未知张力赋值。

令 $y=s\sigma_2$。在 $\cos\theta\ne0$ 的一段上，由法向式消去 $\sigma_1$：

$$
\begin{aligned}
\sigma_1
&=\frac{s}{\cos\theta}\left(\frac{y}{rs}-p\right),\\
y'
&=r\sin\theta\,
\frac{s}{\cos\theta}\left(\frac{y}{rs}-p\right)\\
&=\tan\theta(y-prs).
\end{aligned}
$$

采用一阶线性方程的积分因子 $\cos\theta$，同时用乘积求导：

$$
\begin{aligned}
(y\cos\theta)'
&=y'\cos\theta-y\sin\theta\\
&=\sin\theta(y-prs)-y\sin\theta\\
&=-pr(R-r\cos\theta)\sin\theta.
\end{aligned}
$$

逐项积分，不跳过两个三角积分：

$$
\begin{aligned}
y\cos\theta
&=-prR\int\sin\theta\,\mathrm d\theta
+pr^2\int\sin\theta\cos\theta\,\mathrm d\theta\\
&=prR\cos\theta-\frac{pr^2}{2}\cos^2\theta+C,\\
y&=pr\left(R-\frac r2\cos\theta\right)
+\frac{C}{\cos\theta}.
\end{aligned}
$$

后一积分使用 $u=\cos\theta$、$\mathrm du=-\sin\theta\,\mathrm d\theta$。在顶部和底部，$s=R>0$；光滑薄膜的有限张力要求 $y$ 有限，故每段中的 $C/\cos\theta$ 项必须消失，即 $C=0$。恢复 $\sigma_2=y/s$ 后，再代回法向式得 $\sigma_1=pr/2$。上下半部的连续接合排除靠不同积分常数制造的虚假支路。

这一路线解释了为什么整体膜带法有效：顶部边界的竖向张力为零，相当于把有限性条件直接写入积分受力式。完整曲面微元法还能独立检验切向平衡，不只是把已经得到的张力再次代入法向方程。

内圈负曲率不表示膜必须受压。内圈的环向张力仍为正，但其法向合力向孔内外法向方向，增加了子午张力必须抵抗的载荷。区分“张力为负”和“受拉膜的某一主曲率为负”，是理解环面应力集中的关键。

## 七、易错点

将膜张力 $\sigma_i$ 当作 $\mathrm{Pa}$ 为单位的材料应力，会使压力平衡少一个膜厚或长度。先写切边总力 $\sigma_i\ell$；若确需材料应力，最后才除以膜厚。

沿纵切线定义的张力不沿纵切线作用。跨线力方向在膜切平面内垂直于切线，圆柱和环面的下标对应也不同。先画切线与力的直角关系，再给两个力命名。

用半筒实际面积 $\pi rh$ 乘以同一方向的 $p$，会得到错误系数。真正的曲面压力是法向分布力，其横向合力等于 $p$ 乘投影面积 $2rh$。环面膜带同样须取环形投影，不是膜带实际面积。

长圆柱并不意味着端面载荷可以忽略。若未说明端部如何封闭或载荷由谁承担，仅靠中段局部曲率只能确定环向张力，不能唯一确定轴向张力。本题采用闭端香肠模型。

把环向曲率写成 $1/s$、或把两个曲率都取正，会在内圈得到不正确甚至为负的张力。应按外法向计算 $\kappa_\varphi=-\cos\theta/s$，特别检查 $\theta=0$、$\theta=\pi$ 和顶部的符号。

在 $\theta=\pi/2$ 直接约去 $\cos\theta=0$，是隐蔽的除零。该处竖向整体方程为 $0=0$，须用连续极限和局部法向式补值。另解微分方程时也要用有限性排除 $C/\cos\theta$。

最大主张力的方向与裂缝方向垂直，不是平行。环面内圈最大力沿子午方向，裂缝沿内圈环向；圆柱最大力沿绕轴圆周方向，裂缝沿直轴方向。

仅由张力最大就宣称任何材料都在该处破裂，忽略了许用强度、厚度和缺陷。正式结论依赖均匀薄膜和方向强度相当的模型；方向强度不同时应比较 $\sigma_i/\Lambda_i$。

## 八、课堂讲解建议

课堂先用一张纸剪出两种切线，让学生在切线两侧画彼此相反、且垂直切线的面内拉力。教师在图3-1和图3-2上逐一写出实际力方向，不先背“纵向张力”或“横向张力”名称。板书保留切线与拉力的两个方向，避免进入环面后沿用错误下标。

随后只讲圆柱。让学生先把半筒分成几个法向不同的小片，再用 $\cos\varphi$ 投影；算出 $2rh$ 后才指出投影面积捷径。教师再取闭端筒段，让学生说明侧壁压力为何没有轴向分量、端面压力为何仍由中段侧壁传递。

环面课堂从真正三维图开始，先找内侧、外侧、顶部和局部管轴，之后才给 $\theta$。在图3-4上询问顶部子午力为何没有竖向分量，把这一边界条件与环形投影一起作为解题入口；板书逐行做平方差并注明何时能够约去 $\cos\theta$。

最后教师在图3-5的内圈分别沿两个主方向走一小段，比较切向变化与外法向，建立一个正曲率、一个负曲率的直觉。让学生在图3-6上先指出最大力方向，再画垂直于它的裂缝。若时间充足，可用关键洞察中的完整微元推导说明切向平衡与积分常数，不以背诵环面张力式代替理解。

## 九、变式训练

**变式1：薄膜张力与材料应力的换算。**

闭端圆柱半径 $r=2.5\times10^{-2}\,\mathrm m$，膜厚 $t=2.0\times10^{-4}\,\mathrm m$，压差 $p=8.0\times10^3\,\mathrm{Pa}$。求两个膜张力及材料正应力；若两个方向的许用材料应力均为 $S=1.6\times10^6\,\mathrm{Pa}$，求压差上限。

首先按膜张力求力，不把材料应力提前代入同一记号：

$$
\begin{aligned}
\sigma_1&=pr
=(8.0\times10^3)(2.5\times10^{-2})
=200\,\mathrm{N\,m^{-1}},\\
\sigma_2&=\frac{pr}{2}
=100\,\mathrm{N\,m^{-1}}.
\end{aligned}
$$

膜的截面积是切边长度乘厚度，所以两个材料正应力为

$$
\begin{aligned}
S_1&=\frac{\sigma_1}{t}
=\frac{200}{2.0\times10^{-4}}
=1.0\times10^6\,\mathrm{Pa},\\
S_2&=\frac{\sigma_2}{t}
=5.0\times10^5\,\mathrm{Pa}.
\end{aligned}
$$

环向先到限，令 $pr/t=S$，得到

$$
p_{\max}=\frac{St}{r}
=\frac{(1.6\times10^6)(2.0\times10^{-4})}
{2.5\times10^{-2}}
=1.28\times10^4\,\mathrm{Pa}.
$$

轴向在此时仅达到 $S/2$。裂缝沿轴向，不是沿最大材料应力方向。给定压差 $8.0\times10^3\,\mathrm{Pa}$ 低于上限，符合安全条件；若达到许用值即视为失效，则上式表示极限压差而非严格安全端点。

**变式2：半径比为四的环面。**

设 $R=4r$，压差为 $p$。求内侧、顶部、外侧的两个主张力，比较内外子午张力之比及内侧子午张力与环向张力之比。

环向张力处处为 $\sigma_1=pr/2$。对子午张力分别代入 $\cos\theta=1,0,-1$：

$$
\begin{aligned}
\sigma_2(0)
&=\frac{pr(8r-r)}{2(4r-r)}
=\frac76pr,\\
\sigma_2\left(\frac\pi2\right)&=pr,\\
\sigma_2(\pi)
&=\frac{pr(8r+r)}{2(4r+r)}
=\frac9{10}pr.
\end{aligned}
$$

因此

$$
\begin{aligned}
\frac{\sigma_2(0)}{\sigma_2(\pi)}
&=\frac{7/6}{9/10}
=\frac{35}{27}\approx1.2963,\\
\frac{\sigma_2(0)}{\sigma_1}
&=\frac{7/6}{1/2}
=\frac73\approx2.3333.
\end{aligned}
$$

外侧子午张力虽小于 $pr$，仍大于 $pr/2$ 的环向张力。内侧局部法向检查为

$$
-\frac{\sigma_1}{R-r}+\frac{\sigma_2(0)}r
=-\frac{p}{6}+\frac{7p}{6}=p,
$$

明确使用内侧负环向曲率。外侧检查为 $+\sigma_1/(R+r)+\sigma_2(\pi)/r=p/10+9p/10=p$，两个位置均平衡。

**变式3：由许用张力求压差上限和最小大环半径。**

环面两个方向的许用张力均为 $\Lambda>0$。先求 $p_{\max}$。再设 $p,r,\Lambda$ 已给定，求使全部膜面不超限的 $R$ 范围。

因为 $\sigma_2$ 处处大于 $\sigma_1$，只需用内圈最大子午张力限制：

$$
\begin{aligned}
\frac{pr(2R-r)}{2(R-r)}&\le\Lambda,\\
p&\le\boxed{\frac{2\Lambda(R-r)}{r(2R-r)}}.
\end{aligned}
$$

因此 $p_{\max}=2\Lambda(R-r)/[r(2R-r)]$。与相同 $r,\Lambda$ 的闭端直圆柱 $p_{\max,\text{柱}}=\Lambda/r$ 比较，

$$
\frac{p_{\max}}{p_{\max,\text{柱}}}
=\frac{2(R-r)}{2R-r}<1.
$$

把管弯成环后，内侧几何使允许压差下降；当 $R/r\to\infty$ 时比值趋于一。

固定 $p$ 求 $R$ 时，因 $R-r>0$，可乘以正分母而不改变不等号：

$$
\begin{aligned}
pr(2R-r)&\le2\Lambda(R-r),\\
2prR-pr^2&\le2\Lambda R-2\Lambda r,\\
2(\Lambda-pr)R&\ge r(2\Lambda-pr).
\end{aligned}
$$

若 $\Lambda>pr$，除以正的 $2(\Lambda-pr)$：

$$
\boxed{
R\ge R_{\min}
=\frac{r(2\Lambda-pr)}{2(\Lambda-pr)}
=r\left[1+\frac{pr}{2(\Lambda-pr)}\right]}.
$$

$R_{\min}>r$ 自动符合环面几何条件。若 $\Lambda=pr$，不等式化为 $0\ge pr^2$，对 $p,r>0$ 不成立；只有无限大 $R$ 的直管极限能够逼近边界。若 $\Lambda<pr$，任意有限环面的内圈张力都大于 $pr>\Lambda$，仍无解，不可把负分母除过去后给出虚假“最小半径”。

<!-- KEEP_TOGETHER_START -->

**变式4：方向强度不同，还一定在内圈沿环向裂开吗？**

环面膜面均匀，但环向、子午向许用张力分别为 $\Lambda_1,\Lambda_2>0$。求压差上限及先失效的方向；说明内圈结论的适用条件。

环向张力为常数，要求 $pr/2\le\Lambda_1$，故 $p\le2\Lambda_1/r$。子午张力最内侧最大，要求

$$
\frac{pr(2R-r)}{2(R-r)}\le\Lambda_2,
\qquad
p\le\frac{2\Lambda_2(R-r)}{r(2R-r)}.
$$

<!-- KEEP_TOGETHER_END -->

两条件须同时成立：

$$
\boxed{
p_{\max}
=\min\left\{
\frac{2\Lambda_1}{r},
\frac{2\Lambda_2(R-r)}{r(2R-r)}
\right\}}.
$$

比较两个上限，均乘以正数后得到分界：

$$
\frac{\Lambda_1}{\Lambda_2}
\ \begin{cases}
<\dfrac{R-r}{2R-r},&\text{环向强度先到限},\\
=\dfrac{R-r}{2R-r},&\text{两种边界同时到达},\\
>\dfrac{R-r}{2R-r},&\text{内圈子午强度先到限}.
\end{cases}
$$

若内圈子午方向先失效，裂缝沿内圈环向，与主解析一致。若环向方向先失效，环向张力本来处处相同；本模型不能从力的大小挑出唯一破裂位置，裂缝趋向子午方向，具体起裂点还由缺陷决定。方向许用张力相同的情况下，比例为一，而 $(R-r)/(2R-r)<1$，因此确实是内圈子午强度先到限。这个变式说明为什么主解析必须写明方向强度相当的条件。

<!-- question-complete -->
