# 第3题

<!-- question-start -->

设一个以 $O$ 为中心的理想力场使单位质量物体在任意位置受到大小恒为 $g$、方向沿径向向外的斥力。两点 $A,B$ 满足 $OA=OB=l$，较小夹角 $\angle AOB=2\theta_0$，其中 $0<\theta_0\le\pi/2$。在 $A,B$ 之间设置固定光滑轨道，使质点从 $A$ 以初速度 $v_0=\sqrt{2gl}$ 沿轨道内侧滑到 $B$。求运动时间最短时轨道的形状。

![图3-1 等半径端点、夹角及径向斥力方向。](../figures/statement-03.png){width=45%}

<!-- question-end -->

## 一、题型定位

这是变速运动中的最短时间路径问题。轨道长短与到达时间不是同一件事：靠近 $O$ 时质点的速度变小，远离 $O$ 时速度变大；改变轨道既改变弧长，也改变沿程速度。必须先由能量求出速度与位置的关系，再比较时间积分。

本题的特殊条件是初速度 $v_0=\sqrt{2gl}$。在径向斥力的势能取为 $-mgr$ 时，质点的机械能恰好为零，使速度成为简单的平方根函数。这一条件不是可以省略的背景数据；若初速度改变，最速轨道一般不能继续套用本题的抛物线。

计算分成三个层次：确定候选轨道，证明它确实给出全局最短时间，检查真实质点能够在轨道内侧保持接触。光学类比和变分法解决第一层；坐标变换给出第二层；约束力计算完成第三层。把三个层次混在一起，容易把“满足一个微分方程”误认为“已经证明最短且可以实现”。

## 二、知识点

径向保守力与势能的关系为 $F_r=-\mathrm dU/\mathrm dr$。本题径向向外取正，$F_r=mg$，所以势能必须随半径增加而减少。固定光滑轨道的约束力垂直于瞬时速度，不做功，但通常有关于 $O$ 的力矩。

极坐标中的弧长满足
$$
\mathrm ds^2=\mathrm dr^2+r^2\mathrm d\varphi^2.
$$
沿轨道的时间微元为 $\mathrm dt=\mathrm ds/v(r)$。若用角坐标作为参数，必须说明角度单调的范围，以及 $\mathrm dr/\mathrm d\varphi$ 的正负；最近点处不能把两个分支合并成同一个正平方根。

光线的费马泛函是 $\int n\,\mathrm ds$。只要人为选择 $n(r)$ 与 $1/v(r)$ 成正比，光线路径的驻值条件就与运动时间的驻值条件相同。这是数学路径的对应，不是把真实斥力变成某种吸引力，也不是把真实质点的速度解释为光速。

对泛函 $\int F(r,r',\varphi)\,\mathrm d\varphi$，固定端点下的 Euler–Lagrange 方程是
$$
\frac{\partial F}{\partial r}
-\frac{\mathrm d}{\mathrm d\varphi}\frac{\partial F}{\partial r'}=0,
\qquad r'=\frac{\mathrm dr}{\mathrm d\varphi}.
$$
该方程给出驻值的必要条件。若要判定全局最小，仍需额外的比较、下界或等价最短路证明。

曲线运动的法向动力学为 $F_n=mv^2\kappa$，$\kappa$ 是曲率。这里的 $F_n$ 是全部力的法向合量，不是轨道支持力本身。把径向斥力的法向分量漏掉，会使最后的接触力少算一半。

## 三、物理图像

图3-1只画端点和力场方向，没有预先给出最速轨道。取 $x$ 正轴沿小夹角的平分线，$A$ 在轴下方、$B$ 在轴上方。质点先朝较小半径运动，经过最近点后再向外运动；斥力在入程做负功，在出程做正功，最终速度恢复为初速度。

与通常的重力最速降线不同，本题没有固定向下的重力方向。每一点的斥力都沿该点到 $O$ 的连线向外，大小不变。后面最速轨道是一段开口向负 $x$ 的抛物线，$O$ 是其焦点，但这一结论不意味着真实质点只受焦点吸引力。

题设描述的是任意位置均适用的理想力场，没有给出不可穿入的实体半径。不能从示意图中的中心点推定一个额外障碍。求出的轨道始终满足 $r\ge l/2>0$，也不经过径向方向无定义的中心。

在 $\theta_0=\pi/2$ 的对径端点情形，平分线所在的平面与取向可以选择，相应存在等时的旋转轨道。以下选定图中的平面和正 $x$ 方向描述其中一条，不把退化几何下的选择误称为唯一。

## 四、解题入口

研究对象是轨道上的质点，质量记为 $m$。先写出斥力的势能，利用不做功的固定光滑约束求得 $v(r)$；此时暂不需要知道轨道形状。

再把时间写成加权弧长积分。光学类比可以较快得到一个一阶关系，直接变分法则能逐项核对这一关系的来源。两条路线都保留最近半径这个几何常数，最后用两个等半径端点确定它。

得到曲线以后，把它转成直角坐标，明确焦点、准线与开口。随后使用平方根坐标将加权弧长化为普通欧氏长度，证明没有其他轨道更快；最后独立计算沿该抛物线的真实运动和接触力。这一顺序既避免先猜图形，也避免直接套用自由中心力轨道公式。

## 五、解析

**第1步：固定坐标、角度与端点条件。**

以 $O$ 为原点，以图3-1的平分线为 $x$ 正轴，向图中上方为 $y$ 正方向。角坐标 $\varphi$ 从正 $x$ 轴逆时针计量。于是
$$
\begin{aligned}
A&=(l\cos\theta_0,-l\sin\theta_0),&
\varphi_A&=-\theta_0,\\
B&=(l\cos\theta_0,+l\sin\theta_0),&
\varphi_B&=+\theta_0.
\end{aligned}
$$
轨道端点条件为 $r(-\theta_0)=r(+\theta_0)=l$。质量 $m$ 会出现在力与能量方程中，但最终时间和形状不应依赖 $m$，因为题设给定的是单位质量所受的斥力大小。

这里 $2\theta_0$ 是普通几何中的较小夹角，不是允许任意绕圈的累计角。后面会说明绕行或离开此平面的路径不会降低时间，不能只靠画出一个对称图便排除这些候选。

**第2步：由径向斥力确定势能的负号。**

斥力为 $\boldsymbol F_{\mathrm r}=mg\boldsymbol e_r$。当半径增加 $\mathrm dr>0$ 时，斥力做功 $mg\,\mathrm dr>0$，势能减少。因此
$$
\begin{aligned}
\mathrm dU&=-mg\,\mathrm dr,\\
U(r)&=-mgr+U_*.
\end{aligned}
$$
势能零点任取，以下取 $U_*=0$。这不是在说远离 $O$ 时势能不能为负，而是选择了便于使用题设初速度的零点。若误写为 $U=+mgr$，求导得到的力会指向 $O$，已经换成了另一道题。

固定光滑轨道的法向力满足 $\boldsymbol N\cdot\boldsymbol v=0$，所以它虽会改变速度方向，却不改变机械能。能量式中只能把斥力对应的势能计入，不能凭轨道弯曲再加一个所谓“向心势能”。

**第3步：求位置决定的速度，区分零能量与非零初速度。**

在 $A$ 点，$r=l$、$v=v_0=\sqrt{2gl}$，故
$$
\begin{aligned}
E&=\frac12mv_0^2-mgl\\
&=\frac12m(2gl)-mgl\\
&=0.
\end{aligned}
$$
任意轨道位置的能量守恒给出
$$
\begin{aligned}
\frac12mv^2-mgr&=0,\\
v^2&=2gr,\\
v(r)&=\sqrt{2gr}.
\end{aligned}
$$
最后取非负平方根是因为 $v$ 表示速率，而不是某一坐标方向的速度分量。零的是机械能 $E$，题设初速度并不为零。若令 $v_0=0$，正确的速度式会变成 $v^2=2g(r-l)$，入程 $r<l$ 根本不可达。

同一个半径上的速率相同，与轨道如何弯曲无关。因此后续优化只需把路径的弧长与经过的半径配合起来，不必为每一条候选轨道重新求一个独立的速度函数。

**第4步：建立时间泛函，明确弧长中两个正交分量。**

在极坐标中，相邻两点之间的径向位移为 $\mathrm dr$，横向位移的一阶量为 $r\,\mathrm d\varphi$。二者互相垂直，所以
$$
\mathrm ds=\sqrt{\mathrm dr^2+r^2\mathrm d\varphi^2},
\qquad
\mathrm dt=\frac{\sqrt{\mathrm dr^2+r^2\mathrm d\varphi^2}}{\sqrt{2gr}}.
$$
在角度从 $-\theta_0$ 单调增加到 $+\theta_0$ 的候选轨道上，写 $r=r(\varphi)$、$r'=\mathrm dr/\mathrm d\varphi$，则
$$
T[r]=\frac1{\sqrt{2g}}\int_{-\theta_0}^{+\theta_0}
\frac{\sqrt{r^2+(r')^2}}{\sqrt r}\,\mathrm d\varphi.
$$
分子是单位角度对应的实际路程，分母反映越靠近中心越慢的速度。只最小化分子会得到普通最短弦，遗漏分母则无法解决本题。

如图3-2，取出程的一个小段，用向外径向作为局部横轴。斜边方向为轨道切线，与径向的夹角记为 $\alpha$。图中的直角三角形给出下一步使用的角度关系，放大示意不表示微元具有有限折角。

![图3-2 出程的极坐标位移微元与径向法线。](../figures/element-03.png){width=65%}

由图中 $\mathrm dr$、$r\,\mathrm d\varphi$、$\mathrm ds$ 三边直接得到
$$
\sin\alpha=\frac{r\,\mathrm d\varphi}{\mathrm ds}
=\frac r{\sqrt{r^2+(r')^2}},
\qquad
\cos\alpha=\frac{r'}{\sqrt{r^2+(r')^2}}.
$$
出程 $r'>0$ 时 $\alpha$ 为锐角；入程 $r'<0$ 时切线与向外径向夹角为钝角，$\cos\alpha<0$，但 $\sin\alpha$ 仍为正。不能把锐角图中的余弦正号无条件搬到入程。

**第5步：构造等价的光学路径问题。**

选择无量纲折射率
$$
n(r)=\sqrt{\frac lr}.
$$
它与 $1/v(r)$ 成正比，因为
$$
\frac1{v(r)}=\frac{n(r)}{\sqrt{2gl}},
\qquad
T=\frac1{\sqrt{2gl}}\int n(r)\,\mathrm ds.
$$
前面的正比例常数不会改变使积分最小的轨道。这样，只需研究折射率由半径决定的光学最短路。

把连续介质暂时分成很多薄同心圆层，每层内折射率近似常数。相邻层的界面法线就是径向，所以在同一界面半径 $r$ 上，Snell 定律为
$$
n_{\text{入}}\sin\alpha_{\text{入}}
=n_{\text{出}}\sin\alpha_{\text{出}}.
$$
这里的角是与法线的夹角，而不是与圆周切线的夹角。若选后者，应该使用余弦；角的命名变了，三角函数也必须跟着变。

**第6步：补全同心层几何，得到真正的不变量。**

在任意一个均匀薄层里，光线片段是一条直线。设 $O$ 到这条直线的垂距为 $h$。在直线上任取一点 $P$，以该点的径向与直线夹角为 $\alpha$，直角三角形给出 $h=r\sin\alpha$。因此同一层内 $r\sin\alpha$ 不变；跨界面时，界面两侧的 $r$ 相同，Snell 定律又保证 $n\sin\alpha$ 连续。

将“层内直线几何”与“层间折射关系”连起来，才得到全路径不变量
$$
nr\sin\alpha=K.
$$
不能只在一个界面写了 Snell 定律，就把 $n\sin\alpha$ 当成整个径向渐变介质中的常数；不同位置的径向法线在转动，必须保留这个 $r$。

代入 $n=\sqrt{l/r}$ 后，
$$
\sqrt{lr}\sin\alpha=K.
$$
用一个长度常数 $c$ 表示 $K=\sqrt{lc}$，即
$$
\sqrt r\sin\alpha=\sqrt c.
$$
在最近点，切线与径向垂直，$\sin\alpha=1$，所以该处半径恰为 $r=c$。这说明常数 $c$ 的几何含义，不是凭符号预先指定它为焦距。

**第7步：把角度不变量化为轨道的一阶方程。**

使用图3-2中已经确定的 $\sin\alpha=r/\sqrt{r^2+(r')^2}$，有
$$
\begin{aligned}
\sqrt r\,\frac r{\sqrt{r^2+(r')^2}}&=\sqrt c,\\
\frac{r^3}{r^2+(r')^2}&=c,\\
r^3&=cr^2+c(r')^2,\\
(r')^2&=\frac{r^3}{c}-r^2
=r^2\left(\frac rc-1\right).
\end{aligned}
$$
平方后的等式要求 $r\ge c$。它给出导数的大小，但没有保留导数符号。入程与出程应分别写为
$$
r'=-r\sqrt{\frac{r-c}{c}}
\quad\hbox{或}\quad
r'=+r\sqrt{\frac{r-c}{c}}.
$$
在转折点 $r=c$ 两式的导数都趋于零，能光滑衔接。若全程只取正号，轨道半径只能增加，无法连接这两个等半径端点形成所需的对称段。

**第8步：逐项分离变量并积分。**

先处理出程 $r'\ge0$。从上一式得到
$$
\mathrm d\varphi=\frac{\sqrt c\,\mathrm dr}{r\sqrt{r-c}}.
$$
令最近点的角为 $\varphi_c$，从 $r=c$ 积分到当前 $r$。采用根式代换 $u=\sqrt{r-c}$，则 $r=c+u^2$、$\mathrm dr=2u\,\mathrm du$。代入时不能漏掉 $\sqrt{r-c}=u$：
$$
\begin{aligned}
\varphi-\varphi_c
&=\int_c^r\frac{\sqrt c\,\mathrm d\rho}{\rho\sqrt{\rho-c}}\\
&=\int_0^{\sqrt{r-c}}\frac{2\sqrt c\,\mathrm du}{c+u^2}\\
&=\left[2\arctan\frac u{\sqrt c}\right]_0^{\sqrt{r-c}}\\
&=2\arctan\sqrt{\frac{r-c}{c}}.
\end{aligned}
$$
这里使用 $\mathrm d(\arctan z)/\mathrm dz=1/(1+z^2)$。入程从较大半径走向最近点，$\mathrm dr<0$、$\mathrm d\varphi>0$，所以应取
$$
\varphi-\varphi_c=-2\arctan\sqrt{\frac{r-c}{c}}.
$$
两段的统一形式是
$$
r=c\sec^2\frac{\varphi-\varphi_c}{2}.
$$
最近点附近 $r-c$ 与 $(\varphi-\varphi_c)^2$ 成正比，所以积分中看似奇异的 $1/\sqrt{r-c}$ 并不造成轨道尖点。

**第9步：用两个端点确定积分常数，而非只凭对称性猜测。**

在 $A$ 与 $B$ 都有 $r=l$，代入入、出程角式：
$$
\begin{aligned}
-\theta_0-\varphi_c&=-2\arctan\sqrt{\frac{l-c}{c}},\\
+\theta_0-\varphi_c&=+2\arctan\sqrt{\frac{l-c}{c}}.
\end{aligned}
$$
两式相加，得到 $-2\varphi_c=0$，所以 $\varphi_c=0$。相减后有
$$
\tan\frac{\theta_0}{2}=\sqrt{\frac{l-c}{c}},
$$
于是
$$
\begin{aligned}
\tan^2\frac{\theta_0}{2}&=\frac lc-1,\\
\frac lc&=1+\tan^2\frac{\theta_0}{2}
=\sec^2\frac{\theta_0}{2},\\
c&=l\cos^2\frac{\theta_0}{2}.
\end{aligned}
$$
使用半角公式 $2\cos^2(\varphi/2)=1+\cos\varphi$，轨道方程为
$$
\boxed{\displaystyle
r(\varphi)=\frac{l\cos^2(\theta_0/2)}{\cos^2(\varphi/2)}
=\frac{l(1+\cos\theta_0)}{1+\cos\varphi}},
\qquad -\theta_0\le\varphi\le\theta_0.
$$
定义域内分母不为零，最近半径 $c$ 满足 $l/2\le c<l$。至此得到候选曲线，尚未完成全局最短性的证明。

**第10步：直接变分，逐项计算两个偏导数。**

为了独立核对光学路线，回到第4步的时间泛函。正比例因子 $1/\sqrt{2g}$ 不影响驻值方程，令
$$
F(r,r')=\frac{\sqrt{r^2+(r')^2}}{\sqrt r},
\qquad Q=r^2+(r')^2.
$$
偏导时把 $r,r'$ 当作两个独立变量。按乘积法则与链式法则，
$$
\begin{aligned}
F_r
&=\frac{r}{\sqrt r\sqrt Q}-\frac{\sqrt Q}{2r^{3/2}}\\
&=\frac{2r^2-Q}{2r^{3/2}\sqrt Q}
=\frac{r^2-(r')^2}{2r^{3/2}\sqrt Q},\\
F_{r'}&=\frac{r'}{\sqrt r\sqrt Q}.
\end{aligned}
$$
第二式求对 $\varphi$ 的全导数时，分子 $r'$、因子 $r^{-1/2}$ 和因子 $Q^{-1/2}$ 都会变化。由于 $Q'=2rr'+2r'r''$，
$$
\frac{\mathrm dF_{r'}}{\mathrm d\varphi}
=\frac{r''}{\sqrt r\sqrt Q}
-\frac{(r')^2}{2r^{3/2}\sqrt Q}
-\frac{r'(rr'+r'r'')}{\sqrt r\,Q^{3/2}}.
$$
最后一项不能只对 $r^2$ 求导而忘记 $(r')^2$。这是从时间积分到二阶方程时最容易漏掉的链式求导。

**第11步：通分消元，核对二阶方程中每一项系数。**

把 Euler–Lagrange 方程 $F_r-\mathrm dF_{r'}/\mathrm d\varphi=0$ 乘以正数 $2r^{3/2}Q^{3/2}$。记 $p=r'$ 只为缩短本段代数，则左端分子为
$$
\begin{aligned}
&(r^2-p^2)Q-2rQr''+p^2Q+2rp^2(r+r'')\\
&=r^2Q-2rQr''+2r^2p^2+2rp^2r''\\
&=r^2Q+2r^2p^2-2rr''(Q-p^2)\\
&=r^2(r^2+p^2)+2r^2p^2-2r^3r''\\
&=r^2\bigl(r^2+3p^2-2rr''\bigr).
\end{aligned}
$$
因为轨道不经过 $r=0$，可除以 $r^2$，得到
$$
\boxed{r^2+3(r')^2-2rr''=0}.
$$
系数 $3$ 来自弧长与速度权重共同求导，不是普通圆锥曲线的几何公式。若把时间泛函误写成 $\sqrt{r^2+(r')^2}/r$，会得到另一种最速线方程。

**第12步：降阶并解一阶线性方程。**

在最近点两侧的每一条单调支上，可把 $p=r'$ 看作 $r$ 的函数。链式法则给出
$$
r''=\frac{\mathrm dp}{\mathrm d\varphi}
=\frac{\mathrm dp}{\mathrm dr}\frac{\mathrm dr}{\mathrm d\varphi}
=p\frac{\mathrm dp}{\mathrm dr}.
$$
令 $u=p^2$，则 $\mathrm du/\mathrm dr=2p\,\mathrm dp/\mathrm dr=2r''$。代入二阶方程：
$$
\begin{aligned}
r^2+3u-r\frac{\mathrm du}{\mathrm dr}&=0,\\
\frac{\mathrm du}{\mathrm dr}-\frac3r u&=r.
\end{aligned}
$$
这是关于 $u(r)$ 的一阶线性方程。积分因子为
$$
\exp\left(\int-\frac3r\,\mathrm dr\right)=r^{-3}.
$$
两边乘以它后，用乘积求导反向合并：
$$
\begin{aligned}
\frac{\mathrm d}{\mathrm dr}(ur^{-3})&=r^{-2},\\
ur^{-3}&=-r^{-1}+C_1,\\
u&=C_1r^3-r^2.
\end{aligned}
$$
在最近点 $r=c$、$p=0$，连续极限给出 $0=C_1c^3-c^2$，即 $C_1=1/c$。所以
$$
(r')^2=r^2\left(\frac rc-1\right),
$$
与光学路线完全相同。降阶的变量替换在单调支上使用，不在转折点强行除以 $p=0$；转折条件通过连续极限加入。

**第13步：补全另一种降阶代换，确认两种积分常数一致。**

也可以令 $z=r^2$、$w=p^2$。此处 $z,w$ 只是辅助变量，不是图中的直角坐标。由
$$
\frac{\mathrm dw}{\mathrm dz}
=\frac{2p\,\mathrm dp/\mathrm dr}{2r}
=\frac{r''}{r}
$$
得到
$$
z+3w-2z\frac{\mathrm dw}{\mathrm dz}=0.
$$
再设 $\eta=w/z$，即 $w=\eta z$，则
$$
\begin{aligned}
\frac{\mathrm dw}{\mathrm dz}&=\eta+z\frac{\mathrm d\eta}{\mathrm dz},\\
z+3\eta z-2z\left(\eta+z\frac{\mathrm d\eta}{\mathrm dz}\right)&=0,\\
2z\frac{\mathrm d\eta}{\mathrm dz}&=1+\eta,\\
\frac{\mathrm d\eta}{1+\eta}&=\frac{\mathrm dz}{2z}.
\end{aligned}
$$
积分并还原变量：
$$
\begin{aligned}
\ln(1+\eta)&=\frac12\ln z+C_2,\\
1+\eta&=C_3\sqrt z,\\
w&=C_3z^{3/2}-z,\\
p^2&=C_3r^3-r^2.
\end{aligned}
$$
这里 $z>0$、$\eta=p^2/r^2\ge0$，所以对数中的 $1+\eta>0$，不必丢弃一个隐藏的负号分支。最近点仍给出 $C_3=1/c$。这一路线与第12步不是两条不同曲线，只是同一个一阶方程的两种积分写法。

**第14步：用不显含角度的第一积分再作代数检查。**

因 $F$ 不显含 $\varphi$，有 Beltrami 第一积分。其来源可直接检验：
$$
\frac{\mathrm d}{\mathrm d\varphi}(F-r'F_{r'})
=r'(F_r-\mathrm dF_{r'}/\mathrm d\varphi)=0.
$$
因此
$$
\begin{aligned}
F-r'F_{r'}
&=\frac{\sqrt Q}{\sqrt r}-\frac{(r')^2}{\sqrt r\sqrt Q}\\
&=\frac{Q-(r')^2}{\sqrt r\sqrt Q}
=\frac{r^{3/2}}{\sqrt Q}.
\end{aligned}
$$
在最近点 $r=c$、$r'=0$，该常数为 $\sqrt c$。平方还原正是 $r^3/Q=c$。这项检查特别适合发现第10—11步的通分错误，但它仍只是驻值关系，不能替代最小性的判断。

**第15步：转换直角坐标，确定抛物线的开口与准线。**

由 $r(1+\cos\varphi)=2c$ 以及 $x=r\cos\varphi$，立即有
$$
r+x=2c,\qquad r=2c-x.
$$
再使用 $r^2=x^2+y^2$：
$$
\begin{aligned}
x^2+y^2&=(2c-x)^2\\
&=4c^2-4cx+x^2,\\
y^2&=4c(c-x).
\end{aligned}
$$
如图3-3，曲线的顶点为 $C=(c,0)$，开口朝负 $x$，焦点为 $O=(0,0)$，准线为 $x=2c$。

![图3-3 最速候选抛物线的端点、焦点、顶点与准线。](../figures/parabola-03.png){width=55%}

图中任一点 $P=(x,y)$ 到焦点的距离为 $r$，到准线的距离为 $2c-x$，二者相等，正是抛物线的定义。轨道只取 $A$ 到 $B$ 这一段，不把整条无限抛物线都当作运动区间。图中顶点虽位于焦点右方，曲线仍开口向左；顶点位置与开口方向是两个不同判断。

**第16步：将时间度量变成普通平面长度。**

为了证明最短，定义新的坐标
$$
X=\sqrt r\cos\frac{\varphi}{2},
\qquad Y=\sqrt r\sin\frac{\varphi}{2}.
$$
这两个坐标的量纲是 $\sqrt{\text{长度}}$，不是实际空间的位置坐标。实际角 $\varphi$ 在映射中变成半角。直接微分：
$$
\begin{aligned}
\mathrm dX&=\frac{\cos(\varphi/2)}{2\sqrt r}\,\mathrm dr
-\frac{\sqrt r}{2}\sin\frac{\varphi}{2}\,\mathrm d\varphi,\\
\mathrm dY&=\frac{\sin(\varphi/2)}{2\sqrt r}\,\mathrm dr
+\frac{\sqrt r}{2}\cos\frac{\varphi}{2}\,\mathrm d\varphi.
\end{aligned}
$$
平方相加时，交叉项分别为 $-\tfrac12\sin(\varphi/2)\cos(\varphi/2)\,\mathrm dr\,\mathrm d\varphi$ 与相反数，恰好抵消。两个平方项中的三角函数平方和为 $1$，所以
$$
\begin{aligned}
\mathrm dX^2+\mathrm dY^2
&=\frac{\mathrm dr^2}{4r}+\frac r4\,\mathrm d\varphi^2\\
&=\frac{\mathrm dr^2+r^2\mathrm d\varphi^2}{4r}.
\end{aligned}
$$
记映射平面的弧长为 $\mathrm ds_w=\sqrt{\mathrm dX^2+\mathrm dY^2}$，则
$$
\mathrm dt=\sqrt{\frac2g}\,\mathrm ds_w,
\qquad T=\sqrt{\frac2g}\int\mathrm ds_w.
$$
时间不再是位置加权的长度，而是一个常数乘以映射平面的普通长度。这是全局证明的关键，而不只是又得到一次同样的微分方程。

**第17步：明确平方根分支，并排除三维绕行的优势。**

不能直接把任意绕圈轨道代入半角公式而忽略端点分支。先比较一般路径。用任意参数 $\sigma$ 描述轨道，记单位径向为 $\boldsymbol u(\sigma)$，空间弧长满足
$$
\mathrm ds^2=\left(\frac{\mathrm dr}{\mathrm d\sigma}\right)^2\mathrm d\sigma^2
+r^2\left|\frac{\mathrm d\boldsymbol u}{\mathrm d\sigma}\right|^2\mathrm d\sigma^2.
$$
单位径向在单位球面上的累计弧长为
$$
S_\Omega=\int\left|\frac{\mathrm d\boldsymbol u}{\mathrm d\sigma}\right|\mathrm d\sigma
\ge 2\theta_0.
$$
不等式是球面上两端方向的最短距离不超过任意连接曲线的长度。保持每一个参数位置的半径 $r(\sigma)$ 不变，将其角进度改为选定平面内的
$$
\varphi(\sigma)=-\theta_0+
\frac{2\theta_0}{S_\Omega}
\int_{\sigma_A}^{\sigma}
\left|\frac{\mathrm d\boldsymbol u}{\mathrm d\xi}\right|\mathrm d\xi.
$$
它单调从 $-\theta_0$ 到 $+\theta_0$，且
$$
\left|\frac{\mathrm d\varphi}{\mathrm d\sigma}\right|
\le\left|\frac{\mathrm d\boldsymbol u}{\mathrm d\sigma}\right|.
$$
新路径的径向弧长分量不变，角向分量不增；它每处的速度权重 $1/\sqrt{2gr}$ 也不变。因此新路径的时间不大于原路径。这里 $\sigma$ 不是要求改轨后仍保持不变的实际时间，比较的是加权弧长积分。

所以只需在没有角向回退的指定平面路径中求最短，半角分支在 $[-\theta_0,\theta_0]$ 内连续固定。若一条候选经过 $O$，可用极限讨论，其映射长度至少为两段径向距离之和 $2\sqrt l$；这大于随后给出的最优弦长。最优轨道本身从不接近 $r=0$，不会受该奇点影响。

**第18步：使用直线距离下界，证明候选曲线确实最短。**

映射后的端点为
$$
\begin{aligned}
A_w&=\left(\sqrt l\cos\frac{\theta_0}{2},
-\sqrt l\sin\frac{\theta_0}{2}\right),\\
B_w&=\left(\sqrt l\cos\frac{\theta_0}{2},
+\sqrt l\sin\frac{\theta_0}{2}\right).
\end{aligned}
$$
如图3-4，任意连接两端点的映射曲线，其长度不小于竖直线段 $A_wB_w$ 的长度。等号在沿该直线不回退地运动时成立。

![图3-4 平方根坐标中的端点与最短直线。](../figures/map-03.png){width=65%}

图中直线方程为 $X=\sqrt l\cos(\theta_0/2)=\sqrt c$。还原实际坐标：
$$
\sqrt r\cos\frac{\varphi}{2}=\sqrt c
\quad\Longrightarrow\quad
r=c\sec^2\frac{\varphi}{2}.
$$
这恰好是第9步得到的候选轨道。因此，光学和变分给出的驻值曲线不仅局部满足方程，而且达到全局时间下界：
$$
\boxed{\displaystyle
T_{\min}=\sqrt{\frac2g}\,|A_wB_w|
=2\sqrt{\frac{2l}{g}}\sin\frac{\theta_0}{2}}.
$$
证明没有假定所有曲线都能用一个单值 $r(\varphi)$ 表示；一般路径先经第17步压缩角向绕行，再用映射长度下界比较。

**第19步：独立积分候选曲线的运动时间。**

为了检查映射证明中的比例常数，直接对实际轨道积分。由 $r=c\sec^2(\varphi/2)$，
$$
r'=r\tan\frac{\varphi}{2},
\qquad
\sqrt{r^2+(r')^2}=r\sec\frac{\varphi}{2}.
$$
在本题角域内 $\cos(\varphi/2)>0$，不需要额外绝对值。故
$$
\begin{aligned}
T
&=\frac1{\sqrt{2g}}\int_{-\theta_0}^{+\theta_0}
\sqrt r\,\sec\frac{\varphi}{2}\,\mathrm d\varphi\\
&=\sqrt{\frac c{2g}}\int_{-\theta_0}^{+\theta_0}
\sec^2\frac{\varphi}{2}\,\mathrm d\varphi\\
&=\sqrt{\frac c{2g}}\left[2\tan\frac{\varphi}{2}\right]_{-\theta_0}^{+\theta_0}\\
&=4\sqrt{\frac c{2g}}\tan\frac{\theta_0}{2}\\
&=2\sqrt{\frac{2l}{g}}\sin\frac{\theta_0}{2}.
\end{aligned}
$$
最后使用 $\sqrt c=\sqrt l\cos(\theta_0/2)$；正余弦的符号来自已规定的角域，不是默认 $\sqrt{\cos^2 z}=\cos z$ 对所有 $z$ 成立。结果与映射直线时间一致。

**第20步：求真实运动，解释为何合加速度反而恒定。**

令 $q=y/(2c)$，这个无量纲参数随运动从负值增加到正值。由抛物线方程，
$$
x=c(1-q^2),\qquad y=2cq,\qquad r=c(1+q^2).
$$
再由 $\mathrm dx/\mathrm dy=-y/(2c)=-q$，得到 $\mathrm ds/\mathrm dy=\sqrt{1+q^2}$。从 $A$ 到 $B$ 有 $\dot y>0$，因此
$$
\begin{aligned}
\dot y
&=\frac v{\mathrm ds/\mathrm dy}
=\frac{\sqrt{2gc(1+q^2)}}{\sqrt{1+q^2}}
=\sqrt{2gc},\\
\dot x&=-q\sqrt{2gc},\\
\ddot x&=-\frac{\dot y^2}{2c}=-g,\qquad \ddot y=0.
\end{aligned}
$$
真实轨迹与一段恒定向负 $x$ 加速度的平面抛物运动具有同样的坐标随时间变化；但这来自斥力与轨道反力的合力，并非题设斥力本身改成了固定向左的力。

若在 $A$ 取 $t=0$，则
$$
\begin{aligned}
y(t)&=-l\sin\theta_0+\sqrt{2gc}\,t,\\
x(t)&=c-\frac{y(t)^2}{4c}.
\end{aligned}
$$
从第二式求得的初速度分量为
$$
\dot x(0)=\sqrt{2gl}\sin\frac{\theta_0}{2},
\qquad
\dot y(0)=\sqrt{2gl}\cos\frac{\theta_0}{2}.
$$
两分量平方相加正好为 $2gl$。到达 $B$ 时横向速度反号，纵向速度不变，符合入程和出程的镜面对称。

**第21步：根据实际受力检查内侧接触，而不是只看轨道形状。**

如图3-5，在出程上方一点 $P$，径向斥力向右上，轨道凹侧的单位法向指向左下：
$$
\boldsymbol n=\frac{(-1,-q)}{\sqrt{1+q^2}}.
$$
图中的 $\boldsymbol v$ 沿切线，$\boldsymbol N$ 沿 $\boldsymbol n$；两力合成后才产生水平向左的加速度。

![图3-5 出程点的径向斥力、轨道反力与切向速度。](../figures/forces-03.png){width=48%}

由第20步的加速度和斥力，约束力为
$$
\begin{aligned}
\frac{\boldsymbol N}{m}
&=(-g,0)-g\frac{(x,y)}r\\
&=g\left(-1-\frac{1-q^2}{1+q^2},
-\frac{2q}{1+q^2}\right)\\
&=\frac{2g}{1+q^2}(-1,-q).
\end{aligned}
$$
其大小及方向为
$$
\boxed{N=\frac{2mg}{\sqrt{1+q^2}}>0},
\qquad
\boldsymbol N=N\boldsymbol n.
$$
因 $\boldsymbol v=\sqrt{2gc}(-q,1)$，点乘得到
$$
\boldsymbol N\cdot\boldsymbol v
=\frac{2mg\sqrt{2gc}}{1+q^2}\,[(-1)(-q)+(-q)(1)]=0.
$$
轨道反力确实不做功，且全程指向凹侧，无须轨道向外拉住质点。候选最速段符合“沿轨道内侧滑”的接触要求。

还可用曲率单独检查。将曲线写成 $x=x(y)$，由 $\mathrm dx/\mathrm dy=-q$、$\mathrm d^2x/\mathrm dy^2=-1/(2c)$，平面曲率公式给出
$$
\kappa=\frac{|\mathrm d^2x/\mathrm dy^2|}
{[1+(\mathrm dx/\mathrm dy)^2]^{3/2}}
=\frac1{2c(1+q^2)^{3/2}}.
$$
故 $mv^2\kappa=mg/\sqrt{1+q^2}$。斥力的法向分量为
$$
\boldsymbol F_{\mathrm r}\cdot\boldsymbol n
=\frac{mg\,[-(1-q^2)-2q^2]}{(1+q^2)^{3/2}}
=-\frac{mg}{\sqrt{1+q^2}}.
$$
法向动力学因此是 $N-mg/\sqrt{1+q^2}=mg/\sqrt{1+q^2}$，仍得同样的 $N$。

**第22步：汇总结论并作边界、量纲和守恒检查。**

所求轨道是焦点为 $O$、顶点在小夹角平分线上的抛物线段：
$$
\boxed{\displaystyle
y^2=4c(c-x),\qquad c=l\cos^2\frac{\theta_0}{2}},
$$
其中只取连接 $A$ 与 $B$ 的部分。它的最短时间为
$$
\boxed{\displaystyle T_{\min}=2\sqrt{\frac{2l}{g}}\sin\frac{\theta_0}{2}}.
$$
参数 $c$ 的量纲是长度，$y^2$ 与 $4c(c-x)$ 都是长度平方；$\sqrt{l/g}$ 的量纲是时间。质量在形状和时间中消去，在支持力中仍存在，符合不同物理量的预期。

当 $\theta_0\to0$，端点趋于重合，$c\to l$、$T_{\min}\to0$。在 $\theta_0=\pi/2$ 时，$c=l/2$、$T_{\min}=2\sqrt{l/g}$，轨道仍远离 $O$。从 $A$ 到最近点再到 $B$，总势能变化为零，末速等于初速，但中间速率先减小后增大；只比较初、末速度相等而断言匀速是不成立的。

整个推导没有使用真实质点关于 $O$ 的角动量守恒。斥力本身虽为中心力，轨道反力却不总沿径向；它的力矩不可忽略。光学不变量是时间泛函的几何第一积分，不是未经检查就套入的真实机械守恒量。

## 六、关键洞察

**洞察1：初速度选择使问题的时间几何变平。**

若保留一般初速 $v_A$，能量守恒为
$$
v^2=v_A^2+2g(r-l).
$$
只有 $v_A^2=2gl$ 时，常数项消失，时间元为 $\mathrm ds/\sqrt{2gr}$。此时平方根坐标恰好把度量变成平面常数度量。所谓特殊初速度的意义，不只是“代入后方便约掉一项”，而是整个路径优化的几何发生了简化。

这一点也解释了不能把本题结论推广到“任意径向斥力、任意初速都走抛物线”。改变能量常数后，折射率成为与 $[v_A^2+2g(r-l)]^{-1/2}$ 成正比的函数，不再是 $r^{-1/2}$。

**洞察2：辅助逆平方吸引力路线不等于真实质点动力学。**

可以引入一个与真实质点不同的辅助粒子。令其质量为 $\mu$，势能为 $V_{\mathrm a}=-a/r$，其中 $a>0$。取辅助机械能为零，辅助速率便为
$$
u_{\mathrm a}=\sqrt{\frac{2a}{\mu r}},
$$
即与光学折射率 $n(r)$ 成正比。这里必须是 $u_{\mathrm a}\propto n$，不是 $u_{\mathrm a}\propto1/n$；它是辅助力学模型，不是现代介质中光传播速度的定义。

辅助粒子只受中心吸引力，因此角动量 $J=\mu r u_{\mathrm a}\sin\alpha$ 守恒。消去 $u_{\mathrm a}$：
$$
J^2=2\mu a\,r\sin^2\alpha
\quad\Longrightarrow\quad
r\sin^2\alpha=\frac{J^2}{2\mu a}.
$$
令右侧为 $c$，正好恢复光学路线的不变量。由逆平方中心力的轨道方程也可得到相同结果。设 $h=J/\mu$、$\rho=1/r$；此段导数仍对角坐标求导，但实际时间换成辅助时间 $t_{\mathrm a}$。由角动量守恒，
$$
\dot\varphi_{\mathrm a}=h\rho^2,\qquad
\dot r_{\mathrm a}=-h\rho',\qquad
\ddot r_{\mathrm a}=-h^2\rho^2\rho''.
$$
辅助径向方程 $\ddot r_{\mathrm a}-r\dot\varphi_{\mathrm a}^2=-a/(\mu r^2)$ 因而成为
$$
-h^2\rho^2(\rho''+\rho)=-\frac a\mu\rho^2.
$$
除以非零因子后，得到 Binet 方程
$$
\rho''+\rho=\frac{a}{\mu h^2}.
$$
选择近点方向为角度零线后，一般解是 $\rho=\dfrac{a}{\mu h^2}(1+e\cos\varphi)$，$e\ge0$。令 $p_{\mathrm a}=\mu h^2/a=J^2/(\mu a)$，近点半径为 $r_{\mathrm p}=p_{\mathrm a}/(1+e)$，该处径向速度为零。代入辅助能量，得到
$$
\begin{aligned}
E_{\mathrm a}
&=\frac{J^2}{2\mu r_{\mathrm p}^2}-\frac a{r_{\mathrm p}}\\
&=\frac{\mu a^2}{2J^2}\left[(1+e)^2-2(1+e)\right]\\
&=\frac{\mu a^2}{2J^2}(e^2-1).
\end{aligned}
$$
因此 $E_{\mathrm a}=0$ 且 $e\ge0$ 给出 $e=1$，不是仅凭“零能量轨道”这个名称猜测离心率。轨道为
$$
r=\frac{\mu h^2/a}{1+\cos\varphi}
=\frac{2c}{1+\cos\varphi},
\qquad c=\frac{J^2}{2\mu a}.
$$
这可解释为何光学曲线是抛物线，但真实质点并不受 $-a/r$ 的势能，也不守恒这个 $J$。真实速率是 $\sqrt{2gr}$，随半径增大而增大；辅助速率是 $\sqrt{2a/(\mu r)}$，随半径增大而减小。两者只有空间曲线相同，时间参数完全不同。

**洞察3：最短实际弦与最短时间曲线必须分开比较。**

从 $A$ 到 $B$ 的直弦位于 $x=l\cos\theta_0$。当 $\theta_0<\pi/2$ 时，沿弦的时间是
$$
T_{\text{弦}}=\frac1{\sqrt{2g}}
\int_{-l\sin\theta_0}^{+l\sin\theta_0}
\frac{\mathrm dy}{[(l\cos\theta_0)^2+y^2]^{1/4}}.
$$
该弦的普通长度最短，却经过比最速抛物线更小的中间半径，所以速度损失更多。不能从长度比较直接推断两个时间积分的大小；真正的大小由第18步的映射下界保证。

在对径端点情形，直弦通过 $O$，中点速率为零。其时间仍可作可积的极限：
$$
T_{\text{弦}}
=\frac2{\sqrt{2g}}\int_0^l y^{-1/2}\,\mathrm dy
=2\sqrt{\frac{2l}{g}},
$$
大于抛物线的 $2\sqrt{l/g}$。这说明“速度在一点为零”不必然使总时间发散，也说明轨道避开该点确实带来时间优势。

**洞察4：轨道接触和时间最优是两个独立条件。**

数学泛函没有自动限制支持力只能推不能拉。本题必须另算 $N$，才能确认最优曲线可由内侧接触实现。对于其他力场、初速或端点，如果求出的 $N$ 变为负，受单侧约束的实际最速问题就需要重新处理，不能继续沿用无约束泛函的驻值解。

本题中 $N=2mg/\sqrt{1+q^2}$ 始终为正，最近点最大，端点较小。反力的力矩也可明确算出：
$$
\begin{aligned}
\tau_O&=xN_y-yN_x\\
&=c(1-q^2)\frac{-2mgq}{1+q^2}
-(2cq)\frac{-2mg}{1+q^2}\\
&=2mgcq=mgy.
\end{aligned}
$$
因此除中点瞬间外，真实角动量一直在变化。这个具体力矩比一句“有约束力所以不守恒”更能说明辅助路线和真实路线为何不能混用。

**洞察5：从允许的轨道微扰推导变分方程。**

解析第10步使用的 Euler–Lagrange 方程可以从时间的一阶变化直接得到。令一条候选轨道为 $r(\varphi)$，取满足 $\zeta(-\theta_0)=\zeta(+\theta_0)=0$ 的任意光滑函数 $\zeta$，构造
$$
r_\epsilon=r+\epsilon\zeta,\qquad
r_\epsilon'=r'+\epsilon\zeta'.
$$
端点因 $\zeta$ 为零而保持不动，$\epsilon$ 足够小时半径仍为正。时间对微扰强度的导数为
$$
\left.\frac{\mathrm dT[r_\epsilon]}{\mathrm d\epsilon}\right|_{\epsilon=0}
=\frac1{\sqrt{2g}}\int_{-\theta_0}^{+\theta_0}
(F_r\zeta+F_{r'}\zeta')\,\mathrm d\varphi.
$$
对第二项分部积分，边界项为 $[F_{r'}\zeta]_{-\theta_0}^{+\theta_0}=0$，因此
$$
\left.\frac{\mathrm dT[r_\epsilon]}{\mathrm d\epsilon}\right|_{\epsilon=0}
=\frac1{\sqrt{2g}}\int_{-\theta_0}^{+\theta_0}
\left(F_r-\frac{\mathrm dF_{r'}}{\mathrm d\varphi}\right)\zeta\,\mathrm d\varphi.
$$
如果括号内在某个小区间持续为正，便可选择在此区间为负、在其他位置为零的微扰，使一阶时间变化为负；持续为负时同理选正微扰。因此驻值要求括号内处处为零，得到解析使用的方程。端点固定、边界项消失与内部微扰任意，是这条方程成立的三个具体前提。

再计算对斜率的二阶偏导：
$$
F_{r'r'}=\frac1{\sqrt r\sqrt Q}
-\frac{(r')^2}{\sqrt r\,Q^{3/2}}
=\frac{r^{3/2}}{Q^{3/2}}>0.
$$
它说明在半径固定时，时间密度对斜率是严格凸函数，满足局部极小的斜率凸性必要条件。但半径本身也可变，所以单凭这个正值仍不能完成全局最小证明；平方根坐标下的弦长下界才补上了最后一环。

## 七、易错点

第一处错误是势能符号。径向斥力向外，必须对应 $U=-mgr$，不是 $+mgr$。可以用“半径增大时力做正功、势能减少”即时判断，不必依赖记忆公式。

第二处错误是把零机械能误作零初速度。题设 $v_0=\sqrt{2gl}$ 正好抵消初始势能；若在中间步骤擅自令 $v_0=0$，会改变可达区域和整条最速线。

第三处错误是在径向渐变介质中少写一个 $r$。局部 Snell 条件跨同一界面成立，层内直线的几何垂距才把它延伸为 $nr\sin\alpha$。若把 $\alpha$ 改为与圆周切线的夹角，也必须把正弦改为余弦。

第四处错误是平方后丢失入程符号。$r'$ 在 $A$ 到最近点为负，之后为正；$\varphi$ 全程增加。分离变量时把入程的 $\mathrm dr<0$ 与角增量配对，不能全程直接使用出程正根。

第五处错误是变分求导只对分子求导。$F_{r'}=r' r^{-1/2}Q^{-1/2}$ 含三个随角度变化的因子，尤其 $Q'=2rr'+2r'r''$ 的最后一项容易遗漏。最终二阶方程中 $(r')^2$ 的系数应为 $3$。

第六处错误是把驻值等同于最小值。Euler–Lagrange 与 Snell 都给出候选，只有映射平面中直线达到弦长下界才完成全局最短性证明；平方根变换还须先明确绕圈与半角分支。

第七处错误是把抛物线开口画反。$r+x=2c$ 等价于 $y^2=4c(c-x)$，开口朝负 $x$，顶点在 $(c,0)$，准线在 $x=2c$。焦点在原点并不能单独确定开口。

第八处错误是套用真实角动量守恒。只有斥力是中心力，轨道反力一般不是；辅助吸引粒子与真实受约束质点不能使用同一个速度或时间变量。

第九处错误是把支持力直接写成 $mv^2\kappa$。还要计入斥力的法向分量，本题该分量为负，支持力需要同时抵消它并提供曲率加速度，所以是 $2mg/\sqrt{1+q^2}$。

第十处错误是暗中加入实体障碍。题设没有给出中心物体半径；若另外要求 $r\ge R$，那是增加了一个不等式约束，可能使最优线包含贴边圆弧，不能无说明地改变本题答案。

## 八、课堂讲解建议

课堂首先让学生只看图3-1比较圆弧、直弦与稍向外偏的路径，暂不猜曲线。板书同时保留“路程”与“速度”两列，明确本题比较 $\int\mathrm ds/v$，不比较 $\int\mathrm ds$。再让学生用一小段向外位移判断势能符号，随后计算题设初速度对应的机械能。

讲图3-2时，由教师固定一个出程点，先问径向法线在哪里，再问 $\alpha$ 是与哪条线的夹角。让学生分别写出 $\sin\alpha$ 与 $\cos\alpha$，随后将点移到入程，观察余弦反号而正弦不反号。这样可以在积分之前解决符号问题。

第一次讲解可以先用 Snell 路线得到候选抛物线，但不能省略同心层内的垂距几何。第二次完整讲解再处理变分法，板书把 $F_r$、$F_{r'}$、$\mathrm dF_{r'}/\mathrm d\varphi$ 放在三行，让学生指出最后一行用了几次链式求导，之后逐项通分到系数 $3$。

对变分初学者，教师可先解释“固定端点、让中间一小段略微变动，最优轨道的一阶时间变化应为零”，再给出 Euler–Lagrange 方程。不能把该方程当作无需理解的黑箱，也不要把尚未掌握变分法的学生挡在能量、几何与光学路线之外。

图3-4适合承担第二次认知转折：学生已经找到抛物线，但尚不能说明为什么不是其他驻值线。先让学生核对平方根坐标微分的交叉项确实抵消，再用映射直线的长度下界完成证明。半角分支与三维压缩可作为教师补充，重点说明全局证明没有偷偷排除绕行。

最后讲图3-5，教师要求学生分别画斥力、反力和速度，再用坐标运动算出真实合加速度。板书中明确标注“真实质点”与“辅助光学粒子”，并对比两个速率随半径变化的方向。把支持力正值作为最终验收，而不是看到抛物线就结束。

## 九、变式训练

**变式1：求小夹角时的轨道内凹量与圆弧时间差。**

仍取原题条件，设 $\theta_0$ 很小。求最近半径 $c$ 到四阶，比较最速时间与半径为 $l$ 的短圆弧时间，并解释优势最先出现在哪一阶。

解：由 $\cos^2(\theta_0/2)=(1+\cos\theta_0)/2$，使用余弦泰勒展开，
$$
\begin{aligned}
c&=l\left(1-\frac{\theta_0^2}{4}
+\frac{\theta_0^4}{48}+O(\theta_0^6)\right),\\
l-c&=l\left(\frac{\theta_0^2}{4}
-\frac{\theta_0^4}{48}+O(\theta_0^6)\right).
\end{aligned}
$$
在圆弧上 $r=l$，速率恒为 $\sqrt{2gl}$，弧长为 $2l\theta_0$，故
$$
T_{\text{圆}}=\sqrt{\frac{2l}{g}}\,\theta_0.
$$
最速时间的展开为
$$
\begin{aligned}
T_{\min}
&=2\sqrt{\frac{2l}{g}}\left(
\frac{\theta_0}{2}-\frac{\theta_0^3}{48}
+\frac{\theta_0^5}{3840}+O(\theta_0^7)\right)\\
&=\sqrt{\frac{2l}{g}}\left(
\theta_0-\frac{\theta_0^3}{24}
+\frac{\theta_0^5}{1920}+O(\theta_0^7)\right).
\end{aligned}
$$
因此绝对时间差从三阶出现，
$$
T_{\text{圆}}-T_{\min}
=\sqrt{\frac{2l}{g}}\left(
\frac{\theta_0^3}{24}-\frac{\theta_0^5}{1920}
+O(\theta_0^7)\right),
$$
相对改善则从二阶出现：
$$
\frac{T_{\min}}{T_{\text{圆}}}
=1-\frac{\theta_0^2}{24}+\frac{\theta_0^4}{1920}+O(\theta_0^6).
$$
小角度下两条路径确实接近，但“近似相同”不能替代精确最速条件。圆弧内凹量为零，最速轨道的内凹量从二阶开始，时间优势从三阶开始，两者的阶数并不相同。

**变式2：求最速轨道的入射方向、速率和支持力的极值。**

求 $A$ 点速度与正 $x$ 轴的夹角，轨道上的最大与最小速率，以及支持力的最大与最小值。

解：前文求得
$$
\boldsymbol v_A=\sqrt{2gl}
\left(\sin\frac{\theta_0}{2},\cos\frac{\theta_0}{2}\right).
$$
两个分量在允许角域内均非负，所以入射方向为
$$
\beta_A=\frac{\pi}{2}-\frac{\theta_0}{2}.
$$
该方向应相对于固定 $x$ 轴测量，不是相对于 $OA$ 测量。$OA$ 的角为 $-\theta_0$，故速度与向外径向的有向夹角是 $\pi/2+\theta_0/2$，对应入程的钝角；其正弦为 $\cos(\theta_0/2)$，满足 $\sqrt l\sin\alpha_A=\sqrt c$。

半径从端点的 $l$ 减少到中点的 $c$ 再增加。由 $v=\sqrt{2gr}$，
$$
v_{\max}=\sqrt{2gl},
\qquad v_{\min}=\sqrt{2gc}
=\sqrt{2gl}\cos\frac{\theta_0}{2}.
$$
速率最大值在两个端点，最小值在顶点。取 $q=y/(2c)$，端点有
$$
|q_A|=|q_B|=\frac{l\sin\theta_0}{2l\cos^2(\theta_0/2)}
=\tan\frac{\theta_0}{2}.
$$
由于 $N=2mg/\sqrt{1+q^2}$ 随 $|q|$ 增大而减少，
$$
N_{\max}=2mg,\qquad
N_{\min}=2mg\cos\frac{\theta_0}{2}.
$$
支持力的最大值与速率的最小值在同一点，并不矛盾；中点曲率更大，而且斥力在那里恰好反向于曲率法线。只根据速度大小判断支持力极值会漏掉曲率与外力投影。

**变式3：两个端点半径不等时，求零能量最速时间及曲线。**

保留大小恒为 $g$ 的径向斥力，令 $OA=r_A$、$OB=r_B$，较小夹角为 $0<\beta\le\pi$。初速改为 $\sqrt{2gr_A}$，使机械能仍为零。求最速时间，并说明实际轨道段的最小半径是否一定等于整条抛物线的顶点半径。

解：以 $OA$ 为角度零线，平方根平面的两个端点为
$$
\boldsymbol w_A=(\sqrt{r_A},0),
\qquad
\boldsymbol w_B=\left(\sqrt{r_B}\cos\frac\beta2,
\sqrt{r_B}\sin\frac\beta2\right).
$$
映射线段的长度 $D$ 为
$$
D=\sqrt{r_A+r_B-2\sqrt{r_Ar_B}\cos(\beta/2)}.
$$
因时间元仍为 $\sqrt{2/g}\,\mathrm ds_w$，最短时间是
$$
\boxed{\displaystyle T_{\min}=\sqrt{\frac2g}\,D}.
$$
下面具体确定曲线，而非只给出时间。记 $\Delta\boldsymbol w=\boldsymbol w_B-\boldsymbol w_A$，取直线的单位法向
$$
\boldsymbol n_w=\frac{(\Delta Y,-\Delta X)}D,
\qquad
h=\boldsymbol n_w\cdot\boldsymbol w_A
=\frac{\sqrt{r_Ar_B}\sin(\beta/2)}D>0.
$$
设 $\boldsymbol n_w=(\cos\gamma,\sin\gamma)$，映射直线方程为 $\boldsymbol n_w\cdot\boldsymbol w=h$，即
$$
\sqrt r\cos\left(\frac\varphi2-\gamma\right)=h.
$$
还原后
$$
r=\frac{h^2}{\cos^2(\varphi/2-\gamma)}
=\frac{2h^2}{1+\cos(\varphi-2\gamma)}.
$$
因此仍是一条焦点为 $O$ 的抛物线，整条曲线的轴角为 $2\gamma$、顶点半径为 $h^2$。连接端点的实际段对应映射线段，并不一定包含垂足。

设线段参数为 $\boldsymbol w(t)=\boldsymbol w_A+t\Delta\boldsymbol w$，$0\le t\le1$。实际半径等于 $|\boldsymbol w(t)|^2$。求导得
$$
\frac{\mathrm d|\boldsymbol w(t)|^2}{\mathrm dt}
=2\boldsymbol w_A\cdot\Delta\boldsymbol w+2tD^2,
$$
整条直线的垂足参数是
$$
t_*=-\frac{\boldsymbol w_A\cdot\Delta\boldsymbol w}{D^2}
=\frac{r_A-\sqrt{r_Ar_B}\cos(\beta/2)}{D^2}.
$$
若 $0\le t_*\le1$，轨道段包含顶点，最小半径为 $h^2$；若 $t_*<0$，最小半径为 $r_A$；若 $t_*>1$，最小半径为 $r_B$。不能把整条曲线的顶点半径自动当作任意截取段的最小半径。

检验等半径情形 $r_A=r_B=l$、$\beta=2\theta_0$：
$$
D=2\sqrt l\sin\frac{\theta_0}{2},
\qquad
h=\sqrt l\cos\frac{\theta_0}{2},
\qquad t_*=\frac12.
$$
所有结果恢复原题。若 $\beta\to0$ 而两半径不等，映射最短线趋于径向线，时间趋于 $\sqrt{2/g}\,|\sqrt{r_B}-\sqrt{r_A}|$；此退化极限不再应按 $h=0$ 的式子误画一条非退化抛物线。

**变式4：将恒定斥力改为与半径成正比，最速线还是抛物线吗？**

单位质量所受径向斥力改为 $\Omega^2r$，$\Omega>0$。保留等半径端点与夹角，初速取 $v_0=\Omega l$。求最速轨道、最短时间和圆形轨道的内侧支持力。

解：势能为 $U=-\tfrac12m\Omega^2r^2$。题设初速使机械能为零：
$$
\frac12mv_0^2-\frac12m\Omega^2l^2=0,
\qquad v=\Omega r.
$$
于是
$$
\mathrm dt=\frac1\Omega
\sqrt{\left(\frac{\mathrm dr}{r}\right)^2+\mathrm d\varphi^2}.
$$
取 $u=\ln(r/l)$，则 $\mathrm du=\mathrm dr/r$，得到
$$
\mathrm dt=\frac1\Omega\sqrt{\mathrm du^2+\mathrm d\varphi^2}.
$$
新的平面坐标是 $(u,\varphi)$，不是原题的半角平方根坐标。两个端点为 $(0,-\theta_0)$、$(0,+\theta_0)$，最短连线是 $u=0$，对应实际空间中的短圆弧 $r=l$。因此
$$
\boxed{r=l,\qquad T_{\min}=\frac{2\theta_0}{\Omega}}.
$$
绕行增加角域长度；空间绕行仍可按前文角进度压缩来比较。由于圆弧上速率恒为 $\Omega l$，所需向心合力为 $m\Omega^2l$；外力却是同样大小的向外斥力，故
$$
N-m\Omega^2l=m\Omega^2l,
\qquad \boxed{N=2m\Omega^2l}.
$$
支持力指向内侧且为正，轨道可实现。最速线由抛物线变为圆弧，说明轨道形状取决于完整的力场与能量条件，不是“径向斥力”四个字就能决定。

<!-- draft-content-complete: 014-03; 正确Snell与直接变分路线、全局下界及真实接触检查完整；四个变式均给解。 -->
