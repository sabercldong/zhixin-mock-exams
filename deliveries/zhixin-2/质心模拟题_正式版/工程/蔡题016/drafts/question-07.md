<!-- question-start -->
# 第7题

上好的新鲜牛肉有时会呈现偏绿色的反射光。题设将这一现象解释为牛肉纹理构成的反射光栅：某些方向上的绿光因干涉而得到增强。设相邻纹理层之间的厚度为 $a$，切面与纹理层面的夹角为 $\theta$，每段露出的纹理可视为一小段平面镜。入射光垂直于切面；在满足这些小平面镜反射定律的方向上，最容易观察到反射光。

要使波长为 $\lambda$ 的绿光在上述方向上相干加强，切角 $\theta$ 应满足什么条件？

![图7-1 周期纹理、切面与入射和反射光的空间关系。](../figures/question-07.png){width=80%}

## 一、题型定位

本题属于周期结构的反射干涉与几何光学联合建模问题。单个小平面镜决定反射光的主要方向，多个周期排列的小平面镜决定该方向上哪些波长能够同相叠加。前者是反射定律，后者是相位条件，两个条件必须同时满足。

所给的 $a$ 是沿纹理层面法线测量的层间距离，并不等于切面上相邻纹理的间距。若直接把 $a$ 当作光栅常数，后面的光程差就会错误。另一个关键区别是：光垂直于整体切面，并不意味着垂直于每个倾斜的小平面镜。

解答采用题设的理想周期小平面镜模型，不借此判断某一块真实食物的状态。纹理的真实光学性质、反射强弱和颜色饱和度没有给出，不由干涉条件推造这些信息。

## 二、知识点

1. 平行层面的法向距离与斜截面的截距满足投影关系。切面上相邻周期为 $d$ 时，有 $a=d\sin\theta$。

2. 入射角和反射角均相对于实际反射面的法线测量。若小镜面法线偏离切面法线 $\theta$，垂直切面的入射光相对于小镜面法线的入射角为 $\theta$。

3. 相干叠加比较的是到同一观察方向、同一参考波前的总相位，不能比较两条光线上随意选取的端点。正常入射时，相邻同高反射点的入射相位相同，差异来自出射方向上的路程投影。

4. 波长为 $\lambda$ 的光，光程差大小 $\Delta$ 与相位差满足 $|\delta|=2\pi\Delta/\lambda$。各周期反射性质相同，公共反射相位不影响相邻光的相位差。

5. 多个等振幅周期单元同相时，振幅相加，强度按合振幅的平方计算。相长条件是 $\Delta=q\lambda$，其中 $q$ 为整数级次，而不是折射率。

6. 整数级次、角度定义域和可观察方向需要共同筛选。公式有实数角度，不等于该角度对应的反射光一定离开切面上方。

## 三、物理图像

取垂直于纹理延伸方向的截面来分析。用 $x$ 表示切面内沿周期排列的方向，用 $z$ 表示垂直切面并指向外部的方向，切面为 $z=0$。纹理延伸方向另记为 $y$，沿 $y$ 不改变周期关系，所以核心光路可在 $xz$ 截面中建立。

为固定符号，将纹理层面在 $xz$ 截面中的迹线画成向右下方倾斜，与 $x$ 轴成锐角 $\theta$。纹理层面向外的单位法向量为

$$
\boldsymbol n=(\sin\theta,\,\cos\theta).
$$

入射光的传播方向向下，单位向量为 $\boldsymbol s_i=(0,-1)$。反射光朝右上方传播时，用 $r$ 表示它与切面外法线 $+z$ 的夹角，则

$$
\boldsymbol s_o=(\sin r,\,\cos r).
$$

图7-1中的斜线表示周期层面的延伸关系，不能将整张切面的法线当成每个小镜面的法线。切面上的相邻对应反射点记为 $P$、$Q$，两点均在 $z=0$，间距为 $d$。每个小反射单元的细节无需完全相同到原子尺度，但理想模型要求周期位置和反射相位能保持足够一致。

对于直接从切面上方观察的情况，出射方向必须满足 $\cos r>0$。这一几何要求将在求得反射方向后使用，不能在最开始把所有锐角切角都当成可见。

## 四、解题入口

先把空间层面关系投影到一个法截面，建立 $a$ 与 $d$ 的直角三角形。随后仅分析一个小镜面，求出该镜面的反射方向；这一阶段不使用干涉条件。

最后取相邻两个同高对应点，画出垂直于出射光的参考波前。利用同一入射波前到两点等长、两点到同一出射波前不等长，得到相邻反射光的总路程差。代入前面求得的 $d$ 与反射方向，便可把相干条件完全改写为题目所给的 $a,\lambda,\theta$。

## 五、解析

**步骤1：明确层厚是法向距离，建立周期截距。**

在图7-2中，过相邻两个切面交点 $P,Q$ 的纹理迹线平行。设 $PQ=d$，从 $Q$ 向过 $P$ 的迹线作垂线，垂足为 $H$。$QH$ 就是相邻层面的法向距离，因此 $QH=a$。

![图7-2 层间法向距离与切面周期构成的直角三角形。](../figures/geometry-07.png){width=66%}

图7-2中的 $PH$ 位于纹理迹线上，所以 $\angle QPH=\theta$；$PQ$ 是直角三角形 $PQH$ 的斜边。根据正弦定义，

$$
\begin{aligned}
\sin\theta&=\frac{QH}{PQ}=\frac ad,\\
d\sin\theta&=a,\\
\boxed{d=\frac a{\sin\theta}}.
\end{aligned}
$$

这里的 $a$ 既不是层面在竖直方向的间距，也不是从一层到下一层沿切面的距离。切角较小时，同样厚度的纹理在切面上铺得更疏，$d$ 更大，符合该公式的趋势。

**步骤2：用坐标方程独立复核投影关系。**

过 $P=(0,0)$ 的纹理迹线写为

$$
x\sin\theta+z\cos\theta=0.
$$

其法向量长度为 $1$。与它相距 $a$ 的下一条平行迹线为

$$
x\sin\theta+z\cos\theta=a.
$$

切面上 $z=0$，所以第二条迹线与切面的交点满足 $x\sin\theta=a$，即 $Q=(a/\sin\theta,0)$。两点间距仍为 $d=a/\sin\theta$。这是用“单位法向量点乘坐标等于有符号距离”复核几何，不是再给 $a$ 添加另一个定义。

<!-- KEEP_TOGETHER_START -->
**步骤3：分别画出两条法线，确定实际入射角。**

对一个小镜面进行反射分析，如图7-3。竖直虚线是切面法线；倾斜虚线是小镜面法线。镜面迹线相对切面转过 $\theta$，其法线也相对切面法线转过 $\theta$，因为两条线同时旋转一个直角不会改变它们的夹角。

![图7-3 小镜面法线、切面法线及两种角度的区别。](../figures/angles-07.png){width=65%}
<!-- KEEP_TOGETHER_END -->

从反射点指向光源的入射线沿 $+z$。它与小镜面外法线的夹角为 $\theta$，故小镜面的入射角是 $\theta$，而不是 $0$。反射定律要求出射线与同一条小镜面法线的夹角也为 $\theta$，并位于法线另一侧。因此

$$
\boxed{r=\theta+\theta=2\theta}.
$$

这里 $r$ 相对于整体切面法线测量，$\theta$ 相对于局部小镜面法线测量。这两个角不可直接互换。图7-3中出射线两侧的两个 $\theta$ 相加，正是后面光程投影必须使用 $2\theta$ 的原因。

**步骤4：用反射向量复核方向和正负号。**

平面反射使入射向量的法向分量反号，切向分量不变。将入射单位向量分解为

$$
\boldsymbol s_i=
\big[\boldsymbol s_i-(\boldsymbol s_i\cdot\boldsymbol n)\boldsymbol n\big]
+(\boldsymbol s_i\cdot\boldsymbol n)\boldsymbol n.
$$

括号内是切向分量。反射后只需把后一项变号，因此

$$
\boldsymbol s_o
=\boldsymbol s_i-2(\boldsymbol s_i\cdot\boldsymbol n)\boldsymbol n.
$$

由于 $\boldsymbol s_i\cdot\boldsymbol n=-\cos\theta$，逐项计算得

$$
\begin{aligned}
\boldsymbol s_o
&=(0,-1)+2\cos\theta(\sin\theta,\cos\theta)\\
&=(2\sin\theta\cos\theta,\;2\cos^2\theta-1)\\
&=(\sin2\theta,\;\cos2\theta).
\end{aligned}
$$

第二行到第三行使用正弦和余弦的二倍角公式。该向量长度为 $1$，且法向分量确实由 $-\cos\theta$ 变为 $+\cos\theta$。这既验证 $r=2\theta$，也避免将向右出射误画成向左出射。

**步骤5：选择共同波前，确认入射部分没有光程差。**

令相邻反射点为 $P=(0,0)$、$Q=(d,0)$。正常入射光的波前平行于切面。选一个共同的入射波前 $z=H_i>0$，两条竖直入射线从此波前到 $P$、$Q$ 的距离均为 $H_i$，因此入射路程差为零。

反射后的两条光线平行，但起点不同。不能在两条线上各量出相同长度，就据此说总光程差为零，因为那样的两个终点一般不在同一个波前上。图7-4用垂直于出射方向的共同参考波前消除这一歧义。

![图7-4 同高反射点到共同出射波前的路程差。](../figures/path-07.png){width=69%}

图7-4中，过 $Q$ 作垂直于 $\boldsymbol s_o$ 的线，与从 $P$ 出发的反射线相交于 $K$。于是两条光线到这个参考波前时，$Q$ 处的光已到达波前，$P$ 处的光还须传播 $PK$。两点来自同一个入射波前，因此 $PK$ 就是相邻光的总路程差大小。

**步骤6：由正投影求出射光程差。**

由 $QK\perp PK$，$P,Q,K$ 构成直角三角形。$PQ$ 沿 $+x$，出射方向与 $+x$ 的夹角为 $\pi/2-r$，所以

$$
\begin{aligned}
PK&=PQ\cos\left(\frac{\pi}{2}-r\right)\\
&=d\sin r\\
&=d\sin2\theta.
\end{aligned}
$$

也可以直接用正投影计算：

$$
PK=(\overrightarrow{PQ}\cdot\boldsymbol s_o)
=(d,0)\cdot(\sin r,\cos r)=d\sin r.
$$

因此定义光程差的非负大小为

$$
\boxed{\Delta=d\sin2\theta}.
$$

两光路相减的次序决定有符号差为 $+\Delta$ 或 $-\Delta$，但相长条件不依赖这个选择。此处的 $\lambda$ 是传播介质中的波长，题设未加入介质折射和内部传播，按其小镜面反射模型使用同一外部传播介质。

**步骤7：消去辅助量，补全三角化简。**

将步骤1得到的 $d=a/\sin\theta$ 代入步骤6的路程差：

$$
\begin{aligned}
\Delta
&=\frac a{\sin\theta}\sin2\theta\\
&=\frac a{\sin\theta}\big(2\sin\theta\cos\theta\big)\\
&=2a\cos\theta.
\end{aligned}
$$

此处先使用二倍角公式，再约去 $\sin\theta$。这一约分要求 $\sin\theta\ne0$，所以平行于纹理层面切割的 $\theta=0$ 不能直接包含在该周期截距模型中。所求切角非零时，

$$
\boxed{\Delta=2a\cos\theta}.
$$

式中的因子 $2$ 来自实际反射方向偏转为 $2\theta$，不是因为两相邻反射点有一个深度为 $a$ 的来回传播路程。两点本来就在同一切面上；解释为“上下两层往返 $2a$”会错误地抹去角度依赖。

**步骤8：从波的相位建立相干加强条件。**

设每个周期对应的反射振幅相同，反射产生的公共相位为 $\phi_R$。由点 $P,Q$ 出发的光到共同参考波前的相位差，除去公共初相和 $\phi_R$ 后，仅剩传播引起的差：

$$
|\delta|=\frac{2\pi\Delta}{\lambda}.
$$

相邻光同相的条件是相位差为 $2\pi$ 的整数倍，即

$$
\begin{aligned}
|\delta|&=2\pi q,\\
\frac{2\pi\Delta}{\lambda}&=2\pi q,\\
\Delta&=q\lambda.
\end{aligned}
$$

代入步骤7得

$$
\boxed{2a\cos\theta=q\lambda}.
$$

在非退化锐角范围内，$\Delta>0$，故以正整数 $q=1,2,3,\ldots$ 表示级次。不同波长之间不是彼此相干叠加；这里比较的是同一波长的绿光在不同周期单元上产生的反射波。

**步骤9：解释为什么相邻同相足以保证多层同相。**

若相邻周期的相位差为 $\delta$，从第一个单元算起，第 $j$ 个单元的相位相对第一个为 $j\delta$。当 $\delta=2\pi q$ 时，对每个整数 $j$ 都有

$$
j\delta=2\pi jq,
$$

所以所有单元同相。图7-5比较四个等振幅单元的相位箭头：同相时四箭头同向首尾相接；当相邻相位依次转过 $\pi/2$ 时，它们构成闭合正方形，合振幅为零。

![图7-5 四个周期单元的同相叠加与相位抵消。](../figures/phasors-07.png){width=79%}

用复数把这一点写清楚。设单个单元的振幅为 $A_0$，则 $N$ 个单元的合复振幅为

$$
\mathcal A=A_0\sum_{j=0}^{N-1}\exp(\mathrm ij\delta).
$$

同相时，每一项 $\exp(\mathrm ij2\pi q)=1$，故 $\mathcal A=NA_0$。若 $I_1$ 表示单个单元沿该方向的强度，则

$$
\boxed{I_{\max}=N^2I_1}.
$$

这个平方关系是沿指定方向、等振幅且保持相干时的结果，不是说整个空间的反射能量凭空变为 $N^2$ 倍。增强方向的峰更窄，其他方向可能抵消；完整能量分布还取决于单个小镜面的角度包络。

<!-- KEEP_TOGETHER_START -->
**步骤10：给出切角解族，筛选真实的几何范围。**

由步骤8，

$$
\boxed{\theta_q=\arccos\frac{q\lambda}{2a}}.
$$
<!-- KEEP_TOGETHER_END -->

首先，题设的斜截纹理要求 $0<\theta<\pi/2$，因此仅按干涉代数条件，应有

$$
0<\frac{q\lambda}{2a}<1,
\qquad
1\leqslant q<\frac{2a}{\lambda}.
$$

其次，步骤4给出的出射竖直分量为 $\cos2\theta$。若要求反射光直接离开切面上方，应有

$$
\begin{aligned}
\cos2\theta&>0,\\
0<2\theta&<\frac{\pi}{2},\\
0<\theta&<\frac{\pi}{4}.
\end{aligned}
$$

在这个区间内 $\cos\theta>1/\sqrt2$，于是可见支的正整数级次须满足

$$
\boxed{\frac{\sqrt2\,a}{\lambda}<q<\frac{2a}{\lambda}}.
$$

左端取等时，光沿切面掠射；右端取等时，切面与层面平行，离散交点周期不存在。两种都是边界退化，不能混入正常的上方观察解。这个可见性限制来自出射方向，不改变相干条件本身。若讨论开放的小反射单元阵列并允许从另一侧收光，仍须结合那一侧的几何重新判断，不能把本段的上方条件普遍套用。

**步骤11：进行有单位的计算和逐项回代。**

作为计算示例，取层厚 $a=0.320\,\mu\mathrm m$、目标波长 $\lambda=0.540\,\mu\mathrm m$，考虑 $q=1$。先统一单位，得

$$
\begin{aligned}
\cos\theta&=\frac{0.540}{2\times0.320}
=\frac{27}{32}=0.84375,\\
\theta&=\arccos(0.84375)\approx32.4617^\circ,\\
r&=2\theta\approx64.9235^\circ.
\end{aligned}
$$

反射角小于 $90^\circ$，满足上方观察条件。再独立计算周期：

$$
\begin{aligned}
\sin\theta
&=\sqrt{1-\left(\frac{27}{32}\right)^2}
=\frac{\sqrt{295}}{32},\\
d&=\frac{0.320\times32}{\sqrt{295}}\,\mu\mathrm m
\approx0.596196\,\mu\mathrm m,\\
d\sin r
&=\frac a{\sin\theta}\,2\sin\theta\cos\theta\\
&=2\times0.320\times\frac{27}{32}\,\mu\mathrm m\\
&=0.540\,\mu\mathrm m=\lambda.
\end{aligned}
$$

这里同时检查层间投影、局部反射、光程差与目标波长，不只把角度代回同一个余弦式。若误把整体反射角取成 $\theta$，就会得到 $d\sin\theta=a=0.320\,\mu\mathrm m$，与目标波长不符。

这个例子并非题目额外给定的数值，也不证明实际纹理厚度必为这个值；它仅演示怎样完整计算一个允许的级次并检查单位。

**步骤12：汇总答案并核对量纲和边界。**

本题所求相干加强条件为

$$
\boxed{
2a\cos\theta=q\lambda,\qquad
\theta=\arccos\frac{q\lambda}{2a},\qquad
q\in\mathbb N^+.
}
$$

其中 $a$ 是层间法向距离，$\lambda$ 是同一传播介质中的目标绿光波长，$\theta$ 是切面与层面的夹角。若按直接在切面上方观察的几何，附加 $0<\theta<\pi/4$，即上一步得到的整数区间。

量纲上，$d,a,\lambda,\Delta$ 都是长度，$\sin\theta,\cos\theta,q$ 无量纲，两个核心关系均一致。若整体长度同时放大，而波长也按同比例放大，满足条件的角度不变，符合几何相似性。

当 $\theta\to0^+$ 时，$d\to\infty$，但形式上的 $d\sin2\theta\to2a$。这只是斜截模型的连续极限；有限照明宽度内周期数会变少，$\theta=0$ 本身不再形成这里所用的多周期光栅。不能仅看有限的光程极限就宣布零切角也是相长解。相长条件为特定方向的理想相位匹配，是否明显偏绿还需足够多的有效纹理周期、相干性和合适的单元反射强度。

## 六、关键洞察

**洞察1：反射定律与光栅条件各管一个问题。**

小镜面法线决定单元反射最强的方向；周期平移决定相邻单元的相位差。不能只用“入射角等于反射角”判断颜色，也不能只把 $d\sin r=q\lambda$ 当作方向完整答案。单个单元的反射包络较强，同时阵列因子处于主极大，才是本题要匹配的状态。

将两条路线并列写为

$$
r=2\theta,\qquad d=\frac a{\sin\theta},
\qquad d\sin r=q\lambda.
$$

三个方程的未知辅助量是 $d,r$，消去后二倍角中的 $\sin\theta$ 正好约去。最终结果简洁，不意味着中间两个几何关系可以省略。

**洞察2：波前投影和远处观察点给出同一个相位差。**

另取有限距离的共同观察点 $R=L\boldsymbol s_o$，两反射点仍为 $P=(0,0)$、$Q=(d,0)$。正常入射至两点的路程相同，而出射路程差为

$$
\begin{aligned}
|R-P|-|R-Q|
&=L-\sqrt{L^2-2Ld\sin r+d^2}.
\end{aligned}
$$

在 $L\gg d$ 时，把平方根提出 $L$ 并展开：

$$
\begin{aligned}
|R-Q|
&=L\sqrt{1-\frac{2d\sin r}{L}+\frac{d^2}{L^2}}\\
&=L-d\sin r+\frac{d^2\cos^2r}{2L}
+O\!\left(\frac{d^3}{L^2}\right),\\
|R-P|-|R-Q|
&=d\sin r-\frac{d^2\cos^2r}{2L}
+O\!\left(\frac{d^3}{L^2}\right).
\end{aligned}
$$

此处采用 $\sqrt{1+u}=1+u/2-u^2/8+\cdots$，保留到距离修正的二阶。波前作图得到的 $d\sin r$ 是远场领先项，不是到任意近处点都精确成立的距离差。

对宽度约为 $D=(N-1)d$ 的整个阵列，远场相位误差要小，量级条件是 $D^2/(L\lambda)\ll1$，通常比只要求 $L\gg d$ 更严格。这是阵列整体的远场要求；用准直入射和远场方向进行分析时，才可用同一个相位步长描述所有相邻单元。

**洞察3：有限层数给出窄峰，而不是只有一个离散颜色。**

当 $\exp(\mathrm i\delta)\ne1$ 时，用等比数列求和：

$$
\begin{aligned}
S_N&=1+u+\cdots+u^{N-1},\qquad u=\exp(\mathrm i\delta),\\
uS_N&=u+u^2+\cdots+u^N,\\
(1-u)S_N&=1-u^N,\\
S_N&=\frac{1-\exp(\mathrm iN\delta)}
{1-\exp(\mathrm i\delta)}.
\end{aligned}
$$

将分子分母各提出半角相位，并使用
$e^{-\mathrm ix}-e^{\mathrm ix}=-2\mathrm i\sin x$，得

$$
S_N=
\exp\left[\frac{\mathrm i(N-1)\delta}{2}\right]
\frac{\sin(N\delta/2)}{\sin(\delta/2)}.
$$

前面的指数模长为 $1$，故

$$
I=I_1
\left[\frac{\sin(N\delta/2)}{\sin(\delta/2)}\right]^2.
$$

在主极大 $\delta=2\pi q$ 处，原始有限和直接给 $S_N=N$。商式出现的 $0/0$ 是可去奇点，不是强度发散。图7-6用直接复振幅求和计算 $N=8$ 的局部峰，横坐标是 $u=\Delta/\lambda-q$。

![图7-6 八个等振幅周期单元的主峰及相邻零点。](../figures/peak-07.png){width=66%}

图7-6中峰值为 $I/(N^2I_1)=1$，第一零点在 $u=\pm1/N$。取 $\delta=2\pi q+\varepsilon$，主极大两侧第一零点满足

$$
\frac{N\varepsilon}{2}=\pm\pi,
\qquad
\varepsilon=\pm\frac{2\pi}{N}.
$$

在固定结构、改变观察方向时，

$$
\begin{aligned}
\delta(r)&=\frac{2\pi d\sin r}{\lambda},\\
\delta(r)-\delta(r_q)
&\approx\frac{2\pi d\cos r_q}{\lambda}(r-r_q),\\
|r-r_q|_{\text{first zero}}
&\approx\frac{\lambda}{Nd|\cos r_q|}.
\end{aligned}
$$

这里的角差用弧度，且要求峰不贴近掠射、角宽足够小。两侧零点之间的全宽约为上述半宽的两倍，不可把全宽与单侧宽度混淆。若宽度不小，直接用 $\sin r_\pm=(q\pm1/N)\lambda/d$ 求两个边界，而不强套线性近似。

<!-- KEEP_TOGETHER_START -->
**洞察4：倾斜入射时必须计入入射光程差。**

若入射传播单位向量改为
$\boldsymbol s_i=(\sin\alpha,-\cos\alpha)$，$\alpha$ 是相对于向下切面法线的有符号角，正值表示光向右下方传播。小镜面的向外法线仍为 $(\sin\theta,\cos\theta)$。
<!-- KEEP_TOGETHER_END -->

从反射点反向看入射线，它偏向左侧。因此局部入射角在当前支上是 $\theta+\alpha$。向量反射式给

$$
\begin{aligned}
\boldsymbol s_i\cdot\boldsymbol n
&=\sin\alpha\sin\theta-\cos\alpha\cos\theta\\
&=-\cos(\theta+\alpha),\\
\boldsymbol s_o
&=(\sin\alpha,-\cos\alpha)
+2\cos(\theta+\alpha)(\sin\theta,\cos\theta)\\
&=(\sin(2\theta+\alpha),\;\cos(2\theta+\alpha)).
\end{aligned}
$$

故当前可见支 $r=2\theta+\alpha$。对于平移向量
$\boldsymbol D=(d,0)$，共同观察方向上的相位步长为
$k(\boldsymbol s_i-\boldsymbol s_o)\cdot\boldsymbol D$，其中 $k=2\pi/\lambda$。取其路程差大小，

$$
\begin{aligned}
\Delta
&=d|\sin r-\sin\alpha|\\
&=d\left|\sin(2\theta+\alpha)-\sin\alpha\right|\\
&=2d\sin\theta|\cos(\theta+\alpha)|\\
&=2a|\cos(\theta+\alpha)|.
\end{aligned}
$$

此处使用两正弦之差公式。在受光侧有 $\cos(\theta+\alpha)>0$ 时，相长条件为

$$
2a\cos(\theta+\alpha)=q\lambda.
$$

令 $\alpha=0$ 恢复本题。此处不是直接记忆不同教材的“正弦相加”或“正弦相减”；两者的外形取决于角的符号约定，必须从传播向量与平移向量的点积出发核对。

**洞察5：相同反射相位与交替反射相位不是同一个模型。**

若相邻周期的反射系数相同，设为 $R_0e^{\mathrm i\phi_R}$，公共相位只给整个合振幅乘上一个模长不变的因子。即使每次反射都共同改变 $\pi$，也不会把本题条件改成半整数级次。

若另一个问题明确给出相邻反射单元系数交替变号，则每相邻项还多出 $\pi$，同相条件应为

$$
\delta+\pi=2\pi q
\quad\Longrightarrow\quad
\Delta=\left(q-\frac12\right)\lambda.
$$

本题没有交替反射材料，也不是两种介质边界间的薄膜干涉，不能擅自增加这一相位。对于随机的反射相位，甚至不一定存在一个统一的整数平移条件。

<!-- KEEP_TOGETHER_START -->
**洞察6：颜色匹配存在级次歧义与结构稳定性要求。**

固定 $\theta,a$ 后，允许波长为

$$
\lambda_q=\frac{2a\cos\theta}{q}.
$$
<!-- KEEP_TOGETHER_END -->

因此一个方向的周期相位匹配不只对应一个数学波长。只有结合入射光谱、单元反射包络和有效周期数，才可说明某波段为什么明显。反过来，测得一个峰的 $\theta,\lambda$，若级次未知，也不能唯一反推出层厚，因为

$$
a_q=\frac{q\lambda}{2\cos\theta}
$$

对不同正整数给出不同厚度。

对已固定的级次做微分，

$$
q\,\mathrm d\lambda
=2\cos\theta\,\mathrm da-2a\sin\theta\,\mathrm d\theta.
$$

两边除以 $q\lambda=2a\cos\theta$，得

$$
\frac{\mathrm d\lambda}{\lambda}
=\frac{\mathrm da}{a}-\tan\theta\,\mathrm d\theta.
$$

角度微小变化用弧度。若层厚不变，增大切角使同一级次峰向短波移动；若角度不变，层厚增大则峰向长波移动。该一阶关系只用于小扰动，不把随机间距误差完全等同于整体厚度一致增加。

## 七、易错点

1. 将层厚 $a$ 当作光栅常数 $d$。一个是垂直纹理层面的距离，一个是沿切面的周期；用图7-2的直角三角形确定二者，再进入光程式。

2. 将“垂直切面入射”理解成“垂直小镜面入射”。图7-3中两条法线不重合，局部入射角为 $\theta$，整体出射角为 $2\theta$。

3. 将光程差写成 $d\sin\theta$。这等于 $a$，错在把相对于小镜面法线的角代入相对于切面法线的投影。应使用 $d\sin2\theta$。

4. 把相邻单元比较成薄膜上下界面的往返反射，直接写 $2a$ 或额外加半波损失。两反射点同高，路程差来自横向平移的出射投影；共同反射相位不改变相邻差。

5. 分别在两条反射线上取等长线段，从而说光程差为零。比较的终点必须处在同一个参考波前；图7-4中的 $K,Q$ 才满足这一要求。

6. 解出反余弦后不筛选整数级次和上方可见性。比如 $a=0.600\,\mu\mathrm m$、$\lambda=0.550\,\mu\mathrm m$，$q=1$ 的余弦为 $11/24$，虽有锐角解，但 $\theta>\pi/4$，指定小镜面出射方向不在切面上方；$q=2$ 才给上方可见解。

7. 将 $q=0$ 当成正常的偏绿色解。对本题镜面方向，$2a\cos\theta=0$ 只到 $\theta=\pi/2$ 的退化边界；不能将任意普通零级反射和本题的镜面方向匹配混为一谈。

8. 把 $N$ 束非相干光的强度之和 $NI_1$ 与相干峰值 $N^2I_1$ 混淆。前者的交叉项时间平均为零，后者在指定方向保留同相交叉项；二者需要的相位条件不同。

9. 用有限和商式在主峰处直接计算 $0/0$。应回到原始有限和，或取极限；主峰有限，强度不是无穷大。

10. 在角宽和峰移公式中将度数直接代入微分。三角函数导数的标准形式要求弧度；把一度当成数值 $1$ 会使误差放大约 $57.3$ 倍。

11. 把形状相似的层面、切面与镜面边界画成一条线。空间图用于说明不同对象，法截面用于计算，二者互相补充；不能只补文字而不表达实际夹角与前后关系。

## 八、课堂讲解建议

**建议1：先固定距离和角的定义，再写任何干涉公式。**

课堂中先让学生指出图7-1的切面、层面和纹理延伸方向，再在图7-2中寻找真正长度为 $a$ 的垂线。板书同时写出 $a=d\sin\theta$ 与角的定义，要求口头说明为什么 $d$ 不等于 $a$。随后才处理光路，避免将错误几何带入一个熟悉的光栅公式。

**建议2：将局部反射与整体观察分成两个动作。**

讲解图7-3时，先遮住整体角 $r$，让学生只按小镜面法线画出等角的反射线；再恢复切面法线，读出 $r=\theta+\theta$。对于向量基础尚弱者，先完成作图，再用步骤4检验分量；不以向量公式代替反射的直觉来源。

**建议3：以“终点是否同一波前”核对光程，而不是只记投影。**

让学生在图7-4上比较两个候选终点：两条光线各走相同长度的点，与垂直出射方向的线和两条光线的交点。只有第二组才可直接比较到达同一相位面前的路程差。随后用 $PK=d\sin r$ 建式，并明确入射贡献为零的原因是两点同高与正常入射。

**建议4：用短相位和验证最大值，最后筛选边界。**

先按图7-5相加四个等长箭头，建立同相为振幅相加的认识，再引出复数求和和有限峰形。课堂计算采用步骤11的数值，核对 $d\sin r=\lambda$；最后给出一个有反余弦解但出射向下的候选，讨论为什么代数有根仍需物理筛选。图7-6用于区分峰的位置与峰的宽度，不把这两件事合并为一个条件。

## 九、变式训练

**变式1：较厚纹理能否给出多个上方可见级次？**

层厚为 $a=3.00\,\mu\mathrm m$，正常入射绿光波长为 $\lambda=0.550\,\mu\mathrm m$。求所有能在小镜面反射方向直接从切面上方观察到相干主峰的正整数级次及对应切角。

先用可见支的整数区间：

$$
\frac{\sqrt2\times3.00}{0.550}<q<
\frac{2\times3.00}{0.550}.
$$

逐项计算两个端点：

$$
7.71389\ldots<q<10.90909\ldots.
$$

所以只有 $q=8,9,10$。分别代入：

$$
\begin{aligned}
q=8:\quad &\cos\theta_8=\frac{8\times0.550}{6.00}
=\frac{11}{15},&
\theta_8&\approx42.8334^\circ,\\
q=9:\quad &\cos\theta_9=\frac{9\times0.550}{6.00}
=\frac{33}{40},&
\theta_9&\approx34.4115^\circ,\\
q=10:\quad &\cos\theta_{10}=\frac{10\times0.550}{6.00}
=\frac{11}{12},&
\theta_{10}&\approx23.5565^\circ.
\end{aligned}
$$

每个角都在 $0^\circ$ 与 $45^\circ$ 之间，整体出射角分别为 $85.6669^\circ$、$68.8230^\circ$、$47.1129^\circ$。其中第一个较接近掠射，有限孔径、单元遮挡和实际包络可能显著影响观察强度；题设相位匹配仍成立，不能因峰强未知而删除这个数学可见支。

检查其他整数：$q\leqslant7$ 对应 $\theta>\pi/4$，镜面方向向下；$q\geqslant11$ 则 $q\lambda/(2a)>1$，没有实数切角。因此级次列表完整，而不是只找到一组角就停止。

**变式2：由反射方向反求层厚，说明级次歧义。**

正常入射波长 $\lambda=0.550\,\mu\mathrm m$，观察到小镜面方向 $r=60.0^\circ$ 上的主峰，且实验已确定为一级峰。求 $\theta$、$a$ 与 $d$；若级次未确定，层厚有哪些可能？

局部反射给

$$
\theta=\frac r2=30.0^\circ.
$$

一级峰 $q=1$ 的相干条件为

$$
\begin{aligned}
a&=\frac{\lambda}{2\cos30^\circ}
=\frac{0.550}{\sqrt3}\,\mu\mathrm m
\approx0.317543\,\mu\mathrm m,\\
d&=\frac a{\sin30^\circ}
=2a\approx0.635085\,\mu\mathrm m.
\end{aligned}
$$

独立光程回代：

$$
d\sin60^\circ
=\frac{1.100}{\sqrt3}\frac{\sqrt3}{2}\,\mu\mathrm m
=0.550\,\mu\mathrm m.
$$

若峰的级次未知，角度仍给 $\theta=30^\circ$，但

$$
a_q=q\frac{0.550}{\sqrt3}\,\mu\mathrm m,
\qquad
d_q=2a_q,
\qquad q=1,2,\ldots.
$$

因此 $0.317543\,\mu\mathrm m$ 只是最小正厚度，不是没有级次信息时的唯一厚度。还需另外的谱峰、独立结构测量或级次标定才能消除歧义。

**变式3：有限纹理数量怎样决定峰宽？**

取 $a=0.600\,\mu\mathrm m$，目标波长 $\lambda_0=0.550\,\mu\mathrm m$，正常入射，采用 $q=2$ 的可见切角，有 $N=40$ 个等振幅周期。求主峰角、固定方向下两侧第一零点波长，以及固定波长下两侧第一零点方向；同时给出线性近似与精确值的比较。

先求结构和主峰：

$$
\begin{aligned}
\cos\theta&=\frac{2\times0.550}{2\times0.600}
=\frac{11}{12},\\
\sin\theta&=\frac{\sqrt{23}}{12},\\
d&=\frac{7.200}{\sqrt{23}}\,\mu\mathrm m
\approx1.501304\,\mu\mathrm m,\\
r_0&=2\theta\approx47.1129^\circ,\\
\Delta_0&=d\sin r_0=2\lambda_0=1.100\,\mu\mathrm m.
\end{aligned}
$$

在固定方向下，路程差 $\Delta_0$ 不随波长改变，相位周期数为 $\Delta_0/\lambda$。第一零点满足

$$
\frac{\Delta_0}{\lambda}=q\pm\frac1N.
$$

故短波侧和长波侧分别为

$$
\begin{aligned}
\lambda_{\mathrm{short}}
&=\frac{q\lambda_0}{q+1/N}
=\frac{1.100}{2.025}\,\mu\mathrm m
\approx0.54320988\,\mu\mathrm m,\\
\lambda_{\mathrm{long}}
&=\frac{q\lambda_0}{q-1/N}
=\frac{1.100}{1.975}\,\mu\mathrm m
\approx0.55696203\,\mu\mathrm m.
\end{aligned}
$$

两侧距 $\lambda_0$ 约为 $6.79012\,\mathrm{nm}$ 与 $6.96203\,\mathrm{nm}$，并不严格对称。全宽约 $13.75215\,\mathrm{nm}$。一阶近似的单侧宽度是 $\lambda_0/(qN)=6.875\,\mathrm{nm}$，对称性只是微小偏移近似的结果。

在固定波长下，第一零点满足

$$
\sin r_\pm=\frac{(q\pm1/N)\lambda_0}{d}.
$$

取上方可见且靠近主峰的反正弦支：

$$
r_-\approx46.34734^\circ,\qquad
r_+\approx47.88969^\circ.
$$

<!-- KEEP_TOGETHER_START -->
精确全宽约 $1.54235^\circ$。线性全宽为

$$
\Delta r_{\mathrm{lin}}
\approx\frac{2\lambda_0}{Nd\cos r_0}
\approx0.0269154\,\mathrm{rad}
\approx1.54214^\circ.
$$

这个近似与精确结果接近，因为本例 $N$ 较大且 $r_0$ 未贴近 $90^\circ$。波长零点求的是固定观察方向下的相位变化，角度零点求的是固定波长下的方向变化，二者不能在同一个计算中混用。
<!-- KEEP_TOGETHER_END -->

**变式4：改变入射方向后重新匹配绿光。**

纹理切角为 $\theta=25.0^\circ$，入射传播方向相对于向下切面法线取 $\alpha=-10.0^\circ$，即光向左下方传播。要使 $\lambda=0.550\,\mu\mathrm m$ 的二级主峰与小镜面反射方向匹配，求局部入射角、整体反射角、所需层厚及切面周期。

在本题符号约定下，局部入射角为

$$
i=\theta+\alpha=15.0^\circ,
$$

整体反射方向为

$$
r=2\theta+\alpha=40.0^\circ.
$$

两个角都满足受光及上方出射条件。由相位匹配式，

$$
\begin{aligned}
2a\cos15^\circ&=2\times0.550\,\mu\mathrm m,\\
a&=\frac{0.550}{\cos15^\circ}\,\mu\mathrm m
\approx0.569402\,\mu\mathrm m,\\
d&=\frac a{\sin25^\circ}
\approx1.347320\,\mu\mathrm m.
\end{aligned}
$$

再分别计算两个传播方向在周期平移上的投影。由于 $\sin\alpha<0$，不能把它当成一个不带符号的正角：

$$
\begin{aligned}
\Delta
&=d\big[\sin40^\circ-\sin(-10^\circ)\big]\\
&=d\big[\sin40^\circ+\sin10^\circ\big]\\
&\approx1.100000\,\mu\mathrm m
=2\lambda.
\end{aligned}
$$

如果漏掉入射贡献，只计算 $d\sin40^\circ$，便不会得到 $2\lambda$。最后将 $\alpha$ 置零，整个推导返回正常入射的本题关系；这同时检查了倾斜入射公式的符号约定。

<!-- question-complete -->
<!-- question-end -->
