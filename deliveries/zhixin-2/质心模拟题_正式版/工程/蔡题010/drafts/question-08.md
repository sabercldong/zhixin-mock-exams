# 第8题

<!-- question-start -->
金属圆盘半径为$r$，中心固定在$C$，距水平金属平面的高度为$r\sin\theta$。圆盘与平面夹角恒为$\theta$，并始终在$A$点无滑动接触。$O$为$C$在平面上的垂足，$OA$与$x$轴夹角$\varphi=\omega t$，初始$\varphi=0$。$\omega$描述接触方向绕$O$的转速，不是圆盘自身绕法线的角速度。

空间有静态匀强磁场$\mathbf B=B\hat y$。由圆盘上$C\to A$、金属平面上$A\to O$及固定引线$O\to C$组成测量回路。

（a）求回路几何磁通$\Phi(t)$。

（b）求圆盘瞬时角速度矢量$\boldsymbol\Omega(t)$。

（c）设圆盘上沿$CA$距$C$为$x$的点$P$带电子$-q$，求由圆盘携带速度造成的磁力。

（d）将单位正电荷沿$CA$从$C$缓慢移到$A$，求为克服上述携带速度造成的磁力所需单位电荷功$W$。

（e）比较回路电动势与$W$、$-d\Phi/dt$，说明理由。

取$0<\theta<\pi/2$。正磁通方向按$C\to A\to O\to C$的有向面积定义；引线及金属平面静止，并采用准静态测量。

![图8-1 中心固定且接触无滑动，接触方向绕轴转动不等于圆盘刚性绕轴转动。](../figures/question-08.png)
<!-- question-end -->

## 一、题型定位

这是无滑动刚体运动与含移动接触点电路的电磁感应问题。几何回路的磁通可能变化，但回路不一定由同一批导体质点围成；只有认清真实导体速度，才能判断磁力产生的电动势。

圆盘中心$C$固定，接触点$A$处圆盘材料的瞬时速度也为零。刚体瞬时转轴就是直线$CA$。因此所选径向导电路径恰好落在零速度线上，这是本题的关键。

## 二、知识点

定义平面内的径向、切向单位矢量

$$\hat e=(\cos\varphi,\sin\varphi,0),\qquad
\hat t=(-\sin\varphi,\cos\varphi,0).$$

位置为

$$\mathbf C=r\sin\theta\,\hat z,\qquad
\mathbf A=r\cos\theta\,\hat e.$$

圆盘上从$C$指向$A$的单位方向为

$$\hat u=\cos\theta\,\hat e-\sin\theta\,\hat z.$$

固定中心刚体任一点速度为$\mathbf v=\boldsymbol\Omega\times(\mathbf P-\mathbf C)$。无滑动要求接触处材料速度为零，因此$\boldsymbol\Omega$平行于$CA$。

电动势的力学定义使用真实导体材料速度：

$$\mathcal E=\oint(\mathbf E+\mathbf v_{\rm mat}\times\mathbf B)\cdot d\boldsymbol\ell.$$

几何轮廓随时间变化的速度，与轮廓所选位置处导体材料速度，必须分别判断。

## 三、物理图像

随着接触方向转动，新的圆盘材料点不断成为接触点，$CA$也不断选取新的圆盘径向材料线。接触位置$A(t)$沿圆周移动，却不意味着正接触的那一个材料点沿圆周滑动。

每个瞬间$C$和接触材料点都静止，二者连线就是瞬时零速度轴。圆盘其他点一般运动，但沿当前$CA$的全部点都静止。金属平面中路径$AO$和固定引线$OC$的材料速度也为零。

![图8-2 接触位置的轨迹在移动，接触材料点的瞬时速度却为零。](../figures/contact-08.png)

## 四、解题入口

磁通先用三角形的有向面积直接算。角速度则从瞬时轴方向和圆盘法线随时间变化的速度确定，不能直接写成$\omega\hat z$。

得到角速度后，沿$CA$逐点求$\mathbf v$。如果该线的材料速度处处为零，携带速度造成的磁力与电动势项就全部为零。最后再解释为何几何磁通导数不适用于这个持续更换材料路径的回路。

## 五、解析

（1）计算回路有向面积及磁通。

按$C\to A\to O\to C$的方向，有向面积为

$$\mathbf S=\frac12(\mathbf A-\mathbf C)\times(\mathbf O-\mathbf C).$$

由于$\mathbf O=0$，有

$$\mathbf S=\frac12r^2\sin\theta\cos\theta\,\hat t.$$

对$\mathbf B=B\hat y$点乘，得

$$\boxed{\Phi(t)=\frac12Br^2\sin\theta\cos\theta\cos(\omega t).}$$

因此

$$\boxed{-\frac{d\Phi}{dt}
=\frac12Br^2\omega\sin\theta\cos\theta\sin(\omega t).}$$

若反转回路取向，两式同时反号。结论是否等于真实电动势不受这种取向约定影响。

（2）确定角速度方向。

由$\mathbf v_C=0$、$\mathbf v_A=0$，有

$$\boldsymbol\Omega\times(\mathbf A-\mathbf C)=0.$$

所以写$\boldsymbol\Omega=\Omega_u\hat u$。圆盘法线可选为

$$\hat n=\sin\theta\,\hat e+\cos\theta\,\hat z.$$

它与$\hat u$正交。因为$\dot{\hat e}=\omega\hat t$，故

$$\dot{\hat n}=\omega\sin\theta\,\hat t.$$

另一方面，刚体法线满足$\dot{\hat n}=\boldsymbol\Omega\times\hat n$。由$\hat u\times\hat n=-\hat t$，得到

$$\Omega_u=-\omega\sin\theta.$$

（3）给出角速度三个分量。

于是

$$\boxed{\boldsymbol\Omega
=-\omega\sin\theta\cos\theta\,\hat e
+\omega\sin^2\theta\,\hat z.}$$

写成固定坐标系分量：

$$\boxed{\begin{aligned}
\Omega_x&=-\omega\sin\theta\cos\theta\cos(\omega t),\\
\Omega_y&=-\omega\sin\theta\cos\theta\sin(\omega t),\\
\Omega_z&=\omega\sin^2\theta.
\end{aligned}}$$

角速度大小为$|\boldsymbol\Omega|=|\omega|\sin\theta$。半径$r$消去，因为无滑动几何决定的是角速度比例，不是某个绝对长度。

![图8-3 瞬时角速度沿CA轴，具有水平和竖直分量。](../figures/axis-08.png)

（4）计算沿$CA$的材料速度与电子磁力。

点$P$位于$\mathbf P-\mathbf C=x\hat u$，故

$$\mathbf v_P=\boldsymbol\Omega\times(x\hat u)=0.$$

由圆盘携带速度产生的洛伦兹力为

$$\boxed{\mathbf F_P=-q\,\mathbf v_P\times\mathbf B=0.}$$

这一结果对$0\le x\le r$都成立，与$t$和磁场方向无关。圆盘其他点一般有非零携带速度，但它们不位于题中选定的瞬时径向导电路径上。

（5）计算单位电荷沿$CA$的磁力功。

携带速度项在整条线上为零，因此

$$\boxed{W=\int_C^A
[-\mathbf v_{\rm mat}\times\mathbf B]\cdot d\boldsymbol\ell=0.}$$

这里$W$按单位正电荷的外力功定义，单位为伏；对电量$Q$，相应外力功为$QW$。测试电荷缓慢移动自身产生的磁力始终垂直其相对运动方向，也不贡献沿路径的功。

（6）求真实回路电动势。

沿$CA$的材料速度为零，沿$AO$的平面材料与$OC$引线都静止，因此

$$\oint(\mathbf v_{\rm mat}\times\mathbf B)\cdot d\boldsymbol\ell=0.$$

外加磁场静态，麦克斯韦—法拉第关系给出$\oint\mathbf E\cdot d\boldsymbol\ell=0$。在题设准静态测量模型下

$$\boxed{\mathcal E=0,\qquad \mathcal E=-W=0.}$$

题目比较大小时，$|\mathcal E|=|W|=0$。由单位正电荷外力功定义，电动势与克服非静电力的外力功符号相反；本题两者都为零，符号不影响数值判断。

![图8-4 沿三段真实导体路径的速度项均为零，几何磁通却一般在变化。](../figures/emf-08.png)

（7）说明为何一般不等于几何磁通变化率。

所选几何三角形随$A(t)$转动，其边界扫过磁场，所以$\Phi(t)$一般变化。但$A(t)$是接触位置，当前接触的导体质点却无滑动；几何$CA$也在圆盘中不断换取不同材料线。

移动回路磁通规则的推导要求用于面积输运的边界速度与电路中产生$\mathbf v\times\mathbf B$的导体材料速度相同。本题这两个速度不相同，不能把几何三角形的$-d\Phi/dt$直接当作电动势。

这不否定麦克斯韦—法拉第方程。外加$\partial\mathbf B/\partial t=0$，它仍给出$\oint\mathbf E\cdot d\boldsymbol\ell=0$；需要修正的是对含更换接触点回路的几何磁通规则的无条件使用。

（8）检查特殊相位。

在$\omega t=0,\pi$等相位，几何磁通处于极值，$d\Phi/dt=0$，此时数值上与零电动势相同。在$\omega t=\pi/2$等相位，几何磁通变化率的大小最大，而真实电动势仍为零。

因此只挑初始时刻检验会看不到差别，必须比较一般时间或磁通斜率非零的相位。

（9）用独立的刚体运动检查。

任取圆盘平面内与$CA$垂直的单位方向$\hat t$，距瞬时轴为$y$的点$Q$满足$\mathbf Q-\mathbf C=x\hat u+y\hat t$。其速度

$$\mathbf v_Q=y\boldsymbol\Omega\times\hat t$$

一般非零，表明圆盘不是整体静止。只有$y=0$的瞬时轴线上速度为零。若误写$\boldsymbol\Omega=\omega\hat z$，接触点速度变成$\omega r\cos\theta\hat t\ne0$，直接违反无滑动条件。

![图8-5 电动势使用材料速度，几何磁通输运使用轮廓速度；移动接触使两者不同。](../figures/check-08.png)

（10）显式比较几何线与材料线的速度。

在每个时刻沿几何半径$CA$取点$\mathbf P_{\rm geom}=\mathbf C+x\hat u(t)$，保持几何参数$x$不变。它的坐标导数为

$$\mathbf v_{\rm geom}
=x\dot{\hat u}=\omega x\cos\theta\hat t.$$

但当前占据这个位置的圆盘材料点，其速度由刚体运动决定：$\mathbf v_{\rm mat}=\boldsymbol\Omega\times(x\hat u)=0$。一个是不断选择新的材料点后形成的几何位置的导数，另一个是追踪同一材料点的导数。无滑动条件约束后者，不能约束前者。

用$\mathbf B=B\hat y$，若误将几何速度代入动生电动势积分，就会得到

$$\int_0^r(\mathbf v_{\rm geom}\times\mathbf B)\cdot\hat u\,dx
=\frac12Br^2\omega\sin\theta\cos\theta\sin\omega t.$$

这恰好等于当前几何三角形的$-\dot\Phi$，说明非零磁通导数反映的是该轮廓如何扫过磁场。把它与真实材料速度积分的零结果并列，能够具体指出差别发生在哪一步，而不只是笼统地说某条公式“失效”。

（11）为什么测试电荷沿CA缓慢移动不会补出这个功。

若测试电荷相对材料以$w\hat u$移动，它的实际速度为$\mathbf v_q=\mathbf v_{\rm mat}+w\hat u$。磁力沿路径的分量满足

$$[(\mathbf v_q\times\mathbf B)\cdot\hat u]
=[(\mathbf v_{\rm mat}\times\mathbf B)\cdot\hat u],$$

因为$(\hat u\times\mathbf B)\cdot\hat u=0$。本题沿轴的材料速度已为零，相对运动产生的磁力也垂直路径，因此缓慢搬运电荷不会增加沿CA的磁力功。需要把磁场力、可能的静电势差与闭合回路电动势按各自定义处理；不能把电子的全部速度简单等同于几何接触位置的速度。

倾角的极限还可以核对向量结构。形式上$\theta\to0$时$|\boldsymbol\Omega|\to0$、几何磁通幅度趋于零；$\theta\to\pi/2$时水平角速度分量趋于零、竖直分量趋于$\omega$，三角形面积又因$\cos\theta\to0$而退化。端点构型的单点接触几何可能退化，因此这些只用作连续公式的极限检查，完整讨论采用$0<\theta<\pi/2$。

最终判断电动势前，应先由接触条件求真实刚体速度，再沿测量路径逐点积分。磁场和几何面积的变化只是另一条检查线，是否能直接合并为磁通规则，需要材料路径与几何路径的速度一致这一条件。

## 六、关键洞察

无滑动接触规定的是接触材料点速度为零，不是接触位置永远不动。位置沿圆周移动，材料点在不断更换。

中心固定与接触点静止共同确定瞬时轴$CA$。选定导电路径在瞬时轴上，携带速度磁力项逐点为零，比先套磁通规则更直接。

一般电动势的定义来自单位电荷绕回路的非静电力积分。几何磁通规则需要额外的材料边界条件，不能把所有移动接触回路都当作同一条材料闭合线。

## 七、易错点

把$\omega$当作圆盘刚体绕$z$轴的角速度，会使接触处滑动。忽略角速度水平分量，同样不能满足两个固定瞬时点的条件。

把$\dot{\mathbf A}(t)$当作接触材料速度，或把不断更换的$CA$当作固定材料径线，都会误算磁力与电动势。

磁通正负取决于回路方向，必须统一。更关键的差别是一般磁通导数非零而真实电动势为零，不是靠改变方向就能消除的符号问题。

## 八、课堂讲解建议

教师先让学生在圆盘模型上标出固定中心与当前无滑动接触材料点，再指出瞬时轴。板书分别列接触位置速度与接触材料速度，用不同符号表示。

课堂讨论先算一般相位的几何磁通，再沿$CA$求真实材料速度，比较两种结果。最后选择$\omega t=\pi/2$检验，让学生说明哪一步需要材料回路条件，以及麦克斯韦方程为何仍然成立。

## 九、变式训练

<!-- KEEP_TOGETHER_START -->

变式一：取圆盘倾角$\theta=30^\circ$，写角速度与几何磁通。

解：$\sin\theta=1/2$、$\cos\theta=\sqrt3/2$，所以

$$\boldsymbol\Omega=-\frac{\sqrt3}{4}\omega\hat e
+\frac14\omega\hat z,\quad |\boldsymbol\Omega|=\frac{|\omega|}{2},$$

$$\Phi=\frac{\sqrt3}{8}Br^2\cos\omega t.$$

角速度仍平行于$CA$，而不是等于$\omega\hat z$；沿$CA$真实材料速度为零，电动势仍为零。

在这个倾角下，角速度水平分量与竖直分量之比为

$$\frac{|\Omega_{\rm horizontal}|}{|\Omega_z|}=\sqrt3.$$

水平分量不能忽略；若仅留下竖直分量，就会使接触材料点产生非零速度，破坏本题的无滑动条件。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式二：在$\omega t=\pi/2$时比较几何磁通、磁通变化率与真实电动势。

解：此时$\Phi=0$，但$-d\Phi/dt=Br^2\omega\sin\theta\cos\theta/2$，一般非零。真实电动势仍$\mathcal E=0$，因为当前$CA$是瞬时零速度轴，其他两段材料静止。磁通为零不意味着其变化率为零，初始磁通极值处的偶然相等也不能用于验证一般时间的规则。

该相位的几何接触速度仍为

$$\dot{\mathbf A}_{\rm geom}=\omega r\cos\theta\hat t,$$

而接触材料速度为零。相位选择只是让磁通导数的差别最明显，并没有改变真实路径的运动学或电动势。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式三：磁场方向改为$B\hat z$，保持无滑动运动，求几何磁通与电动势。

解：三角形有向面积$\mathbf S$沿水平切向$\hat t$，故$B\hat z\cdot\mathbf S=0$，几何磁通始终为零。沿测量路径的材料速度仍逐点为零，因此动生电动势也为零。此时磁通导数与电动势数值相同，但不能据此证明任意磁场方向下移动接触回路都满足同一几何磁通规则。

有向面积为

$$\mathbf S=\tfrac12r^2\sin\theta\cos\theta\hat t,
\qquad \hat t\cdot\hat z=0.$$

它始终水平，所以竖直磁场不穿过该三角形。这是磁场与所选几何面积的正交性，与真实零电动势的无滑动原因分别成立。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式四：取消无滑动条件，圆盘改为整体以$\boldsymbol\Omega=\omega\hat z$绕固定中心旋转，接触处允许滑动，仍取$\mathbf B=B\hat y$。求沿$CA$的动生电动势。

解：沿线距中心$x$处材料速度为$\mathbf v=\omega x\cos\theta\hat t$，路径方向为$\hat u$。由$(\hat t\times\hat y)\cdot\hat u=\sin\varphi\sin\theta$，得到

$$\mathcal E_{CA}=\int_0^r(\mathbf v\times\mathbf B)\cdot\hat u\,dx
=\frac12Br^2\omega\sin\theta\cos\theta\sin\omega t.$$

对当前横向磁场，它等于$-d\Phi/dt$。这个非零结果来自改变了真实材料速度与接触条件，不能移回本题的无滑动圆盘。

允许滑动后，接触材料速度直接成为

$$\mathbf v_A=\omega r\cos\theta\hat t\ne0.$$

这一步明确展示变式改变了哪个题设条件。尽管当前横向场中恢复磁通导数数值，仍须沿真实导体路径计算，不能只凭几何轮廓相同就沿用原结论。

<!-- KEEP_TOGETHER_END -->

<!-- question-complete -->
