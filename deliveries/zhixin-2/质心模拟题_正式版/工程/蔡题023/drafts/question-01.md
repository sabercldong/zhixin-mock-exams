# 第 1 题

<!-- question-start -->
圆形顶面的三腿板凳置于水平地面，三条腿竖直，各腿与地面的摩擦系数及支持力均相同。三条腿到圆心 $O$ 的距离均为 $l$，位置按图记为 $A$、$B$、$C$。在距圆心 $\rho$、极角为 $\theta$ 的位置，沿顺时针切向、平行于地面施加力 $F$，缓慢增大 $F$，直至有腿开始滑动。

以 $\rho$、$\theta$ 为极坐标，确定哪些腿先滑动，写出分区边界，作定性图，并说明各区域内 $\rho$、$\theta$ 的极值位置。极角从 $+x$ 轴逆时针计量，“顺时针切向”指施力方向与该处半径垂直。

![图 1-1　三腿的平面位置与顺时针切向施力。](../figures/question-01.png)
<!-- question-end -->

## 一、题型定位

模型说明：等支持力和等摩擦系数规定的是相同的最大静摩擦力，并不直接规定三腿实际静摩擦力的分配。以下先检验原条件，再明确给出相同切向微弹性模型下的条件解；圆形顶面半径若需要使用，另记为 $R_{\rm t}$，不能自动令其等于 $l$。

这是平面刚体在多个摩擦接触点上的静力学问题。破题顺序不是先把最大静摩擦力画在每条腿上，而是先区分“实际摩擦反力”“允许的反力上限”和“接触变形决定的分配规则”。一共有六个水平反力分量，平衡只能提供三个标量方程，因此还必须检查模型是否闭合。

在给定相同各向同性切向刚度后，本题转化为刚体微小平移和转动的叠加；各腿的摩擦大小可唯一计算。这个条件模型的区域图是三个扇区，其边界来自反力模长的比较，不来自猜测力臂最近的腿一定先滑。

## 二、知识点

最大静摩擦力为 $f_{\rm s}=\mu_{\rm s}N$，静止时只有 $|\boldsymbol f_i|\leq f_{\rm s}$，不能总把它写成等号。平面静力平衡为合力零和绕任一点的合力矩零。叉积的竖直分量为 $x f_y-y f_x$，规定逆时针力矩为正。

若接触点有相同切向刚度 $\kappa$，其微小水平位移 $\boldsymbol u_i$ 与反力的关系为 $\boldsymbol f_i=-\kappa\boldsymbol u_i$。刚性板的位移为共同平移加微小转动：
$$
\boldsymbol u_i=\boldsymbol U+\psi\,\boldsymbol e_z\times\boldsymbol r_i.
$$
其中 $\psi$ 的单位为弧度，$\boldsymbol U$ 为平移矢量。极坐标单位矢量分别为
$$
\boldsymbol e_r(\theta)=(\cos\theta,\sin\theta),\qquad
\boldsymbol e_t(\theta)=(-\sin\theta,\cos\theta).
$$
$\boldsymbol e_t$ 是逆时针切向；顺时针施力应为 $-F\boldsymbol e_t$。

## 三、物理图像

施力既有使整块板水平平移的效果，也有使它顺时针转动的效果。各腿需要同时承担抵抗平移的共同反力和抵抗转动的不同方向反力。两种贡献是矢量相加，不能把它们的大小在每条腿上都同号相加。

原条件只限定各反力不能越过同一个半径为 $f_{\rm s}$ 的“摩擦圆”。在圆内如何分配，取决于腿、板和接触面的微小变形。即使三腿摩擦系数相同，刚度仍可能不同；若连刚度模型都没有，首先出现的滑动不是平衡方程唯一决定的量。

## 四、解题入口

先按图取
$$
\boldsymbol r_A=l\left(\frac12,\frac{\sqrt3}{2}\right),\quad
\boldsymbol r_B=l(-1,0),\quad
\boldsymbol r_C=l\left(\frac12,-\frac{\sqrt3}{2}\right).
$$
它们满足 $\sum_i\boldsymbol r_i=\boldsymbol0$、$|\boldsymbol r_i|=l$。施力点为 $\boldsymbol r_P=\rho\boldsymbol e_r(\theta)$，所以外力矩是 $-\rho F$。

接着把三条腿的合力与力矩条件列出，构造不同但同样平衡的反力，检验“先滑区域”是否唯一。只有在明确采用相同微弹性模型后，才比较三个反力平方，得到条件模型的边界。

## 五、解析

（1）明确支持力和摩擦上限。

把每条腿的竖直支持力记为 $N$，则每条腿的最大静摩擦力相同：
$$
f_{\rm s}=\mu_{\rm s}N.
$$
这个量是上限，不是静止时的实际摩擦大小。题设忽略水平施力引起的支持力重新分配；若施力有高度并允许倾覆，还须重新分析竖直支持力，不能直接沿用等 $N$。

（2）建立三个平衡方程。

施力的水平分量为
$$
\boldsymbol F=F(\sin\theta,-\cos\theta).
$$
因此三腿反力必须满足
$$
\begin{aligned}
f_{Ax}+f_{Bx}+f_{Cx}&=-F\sin\theta,\\
f_{Ay}+f_{By}+f_{Cy}&= F\cos\theta,\\
\sum_{i=A,B,C}(x_i f_{iy}-y_i f_{ix})&=\rho F.
\end{aligned}
$$
最后一式的正号来自反力必须平衡顺时针外力矩 $-\rho F$。各反力还须分别满足
$$
f_{ix}^{\,2}+f_{iy}^{\,2}\leq f_{\rm s}^{\,2}.
$$

图 1-2 把共同反力与转动反力分开显示。它们相加才是每条腿的反力；图中 $\boldsymbol e_z\times\boldsymbol r_i$ 的方向会直接进入下面的叉积和模长计算。

![图 1-2　水平反力的合力与合力矩约束。](../figures/equilibrium-01.png)

（3）用自平衡反力证明分配不唯一。

设已经找到一组满足平衡的反力。沿 $AB$ 方向取单位矢量
$$
\boldsymbol t_{AB}
=\frac{\boldsymbol r_A-\boldsymbol r_B}{|\boldsymbol r_A-\boldsymbol r_B|}
=\left(\frac{\sqrt3}{2},\frac12\right).
$$
向这组反力加入
$$
\delta\boldsymbol f_A=\lambda\boldsymbol t_{AB},\quad
\delta\boldsymbol f_B=-\lambda\boldsymbol t_{AB},\quad
\delta\boldsymbol f_C=\boldsymbol0.
$$
合力增量显然为零，力矩增量为
$$
\begin{aligned}
\delta M_z
&=\bigl[(\boldsymbol r_A-\boldsymbol r_B)
\times\lambda\boldsymbol t_{AB}\bigr]_z\\
&=0,
\end{aligned}
$$
因为两矢量平行。只要新增反力仍在各自摩擦圆内，它就是另一组合法静力解。$\lambda$ 可以与 $F$ 成正比，使反力从 $F=0$ 时的零值连续增加，而不必假定存在初始预应力。

（4）在圆心施力时给出具体反例。

取中心施力，并指定外力沿 $-y$ 方向；可把它理解为 $\rho\to0$、$\theta=0$ 的连续极限，圆心本身并没有唯一极角。第一种分配是三腿都向上：
$$
\boldsymbol f_A=\boldsymbol f_B=\boldsymbol f_C
=\left(0,\frac F3\right).
$$
此时三腿同时在 $F=3f_{\rm s}$ 达到上限。

第二种分配在上述反力上取 $\lambda=F/6$，得到
$$
\begin{aligned}
\boldsymbol f_A&=\left(\frac{\sqrt3F}{12},\frac{5F}{12}\right),\\
\boldsymbol f_B&=\left(-\frac{\sqrt3F}{12},\frac F4\right),\\
\boldsymbol f_C&=\left(0,\frac F3\right).
\end{aligned}
$$
逐项平方计算：
$$
\begin{aligned}
|\boldsymbol f_A|^2
&=F^2\frac{3+25}{144}=\frac7{36}F^2,\\
|\boldsymbol f_B|^2
&=F^2\frac{3+9}{144}=\frac1{12}F^2,\\
|\boldsymbol f_C|^2&=\frac19F^2.
\end{aligned}
$$
因而 $A$ 先在 $F=6f_{\rm s}/\sqrt7$ 达到上限，其他两腿仍未达到上限。把 $\lambda$ 改为负值，则可以使 $B$ 先达到上限。这些反力都满足同样的合力与力矩方程。故原条件下不能唯一画出“哪条腿先滑”的区域图。

（5）明确条件解采用的微弹性模型。

现在另加条件：板视作刚性平面，各腿未滑时有相同、各向同性、线性的切向刚度 $\kappa$，从零变形开始缓慢加载，且支持力固定。设板产生平移 $\boldsymbol U$ 和逆时针微小转角 $\psi$，则
$$
\boldsymbol f_i
=-\kappa\left(\boldsymbol U+\psi\boldsymbol e_z\times\boldsymbol r_i\right).
$$
图 1-3 中每个接触点的位移是相同平移与绕 $O$ 的转动位移之和；下面分别用合力求 $\boldsymbol U$，用力矩求 $\psi$。

![图 1-3　刚性板微小平移和转动引起的接触位移。](../figures/elastic-01.png)

合力条件给出
$$
-3\kappa\boldsymbol U=-\boldsymbol F,
\qquad
\boldsymbol U=\frac{\boldsymbol F}{3\kappa}.
$$
这里转动部分之和为零，因为 $\sum_i\boldsymbol r_i=0$。力矩为
$$
\begin{aligned}
\sum_i[\boldsymbol r_i\times\boldsymbol f_i]_z
&=-\kappa\psi\sum_i
[\boldsymbol r_i\times(\boldsymbol e_z\times\boldsymbol r_i)]_z\\
&=-3\kappa l^2\psi.
\end{aligned}
$$
二维矢量恒等式给出方括号为 $|\boldsymbol r_i|^2=l^2$。于是
$$
\psi=-\frac{\rho F}{3\kappa l^2}.
$$
负号表明板顺时针微转，符合外力矩方向。

（6）求出三腿反力的矢量通式。

把 $\boldsymbol U$ 和 $\psi$ 代回：
$$
\boxed{
\boldsymbol f_i
=-\frac{\boldsymbol F}{3}
+\frac{\rho F}{3l^2}\boldsymbol e_z\times\boldsymbol r_i
}.
$$
令
$$
s=\frac{\rho}{l},\quad
\phi_A=\frac\pi3,\quad
\phi_B=\pi,\quad
\phi_C=\frac{5\pi}{3},
$$
则
$$
\boldsymbol f_i
=\frac F3\bigl[\boldsymbol e_t(\theta)+s\boldsymbol e_t(\phi_i)\bigr].
$$
注意 $\kappa$ 已消去：相同刚度的数值影响微小变形大小，但不影响这个对称模型的反力分配比例。若刚度不相同，不能照样把它消去。

（7）完整展开反力平方。

由单位矢量的点积
$$
\boldsymbol e_t(\theta)\cdot\boldsymbol e_t(\phi_i)
=\sin\theta\sin\phi_i+\cos\theta\cos\phi_i
=\cos(\theta-\phi_i),
$$
得到
$$
\boxed{
|\boldsymbol f_i|^2
=\frac{F^2}{9}\left[1+s^2+2s\cos(\theta-\phi_i)\right].
}
$$
平方中的交叉项决定谁先达到上限。不能只按转动力矩贡献来比较，因为该贡献在三条腿上的大小均为 $sF/3$，只有和共同平移贡献的夹角不同。

（8）比较三腿反力并求边界。

当 $s>0$ 时，反力最大者就是 $\cos(\theta-\phi_i)$ 最大者。以 $A$、$B$ 的比较为例：
$$
\begin{aligned}
|\boldsymbol f_A|^2-|\boldsymbol f_B|^2
&=\frac{2sF^2}{9}
\left[\cos\left(\theta-\frac\pi3\right)-\cos(\theta-\pi)\right]\\
&=\frac{2sF^2}{9}
\left(\frac32\cos\theta+\frac{\sqrt3}{2}\sin\theta\right).
\end{aligned}
$$
两者相等时，$\sqrt3\cos\theta+\sin\theta=0$，候选角为 $2\pi/3$、$5\pi/3$。但在 $5\pi/3$ 处，$C$ 的反力更大，所以它不是“$A$、$B$ 先滑”的边界。必须同时比较第三条腿，不能保留所有两两等式作为最终分区线。

对其他两对重复比较，真正边界为
$$
\boxed{\theta=0,\quad \theta=\frac{2\pi}{3},
\quad \theta=\frac{4\pi}{3},\qquad \rho>0.}
$$

（9）给出条件模型下的分区结果。

以 $0\leq\theta<2\pi$ 为一个极角周期：

- $0<\theta<2\pi/3$：$A$ 先达到上限；
- $2\pi/3<\theta<4\pi/3$：$B$ 先达到上限；
- $4\pi/3<\theta<2\pi$：$C$ 先达到上限；
- $\theta=0$：$A$、$C$ 同时达到上限；
- $\theta=2\pi/3$：$A$、$B$ 同时达到上限；
- $\theta=4\pi/3$：$B$、$C$ 同时达到上限；
- $\rho=0$：三腿同时达到上限，且此时极角没有物理意义。

图 1-4 的半径 $R_{\rm t}$ 只是施力点可达区域的边界参数。分区线是上述三条径向线；图中腿的方向 $\phi_i$ 是各扇区中心，不是分区边界。

![图 1-4　相同切向微弹性模型下的先滑扇区。](../figures/regions-01.png)

（10）计算临界施力，检验区域图。

记 $c_{\max}=\max_i\cos(\theta-\phi_i)$，则
$$
\boxed{
F_{\rm cr}(\rho,\theta)
=\frac{3f_{\rm s}}
{\sqrt{1+s^2+2s c_{\max}}}.
}
$$
由于三个腿方向相差 $2\pi/3$，任意方向与最近腿的夹角不超过 $\pi/3$，故
$$
\frac12\leq c_{\max}\leq1.
$$
固定 $\rho$ 时，沿腿的半径方向施力点具有最小临界力：
$$
F_{\rm cr,min}=\frac{3f_{\rm s}}{1+s}.
$$
沿扇区边界时，临界力最大：
$$
F_{\rm cr,max}=\frac{3f_{\rm s}}{\sqrt{1+s+s^2}}.
$$
这两个式子在 $s=0$ 都回到 $3f_{\rm s}$，与三腿共同抵抗平移的结果一致。

<!-- KEEP_STUDENT_START -->
（11）严谨说明极值和边界坐标。

若另给圆面半径 $R_{\rm t}$，允许施力点到达圆面边缘，则各扇区闭包的最大半径都是 $R_{\rm t}$；单腿先滑的开扇区只要求 $0<\rho\leq R_{\rm t}$，其半径下确界是零，但在零点并非单腿先滑。不能把下确界误写成该区域的最小值。

$A$ 区的角度端点为 $0$、$2\pi/3$，$B$ 区为 $2\pi/3$、$4\pi/3$，$C$ 区为 $4\pi/3$、$2\pi$。端点属于两腿同时临界的边界，不属于单腿区域内部。角度端点对应的圆面边缘坐标分别为 $(R_{\rm t},0)$、$(R_{\rm t},2\pi/3)$、$(R_{\rm t},4\pi/3)$；其中 $2\pi$ 与零表示同一条射线。

若比较的是 $F_{\rm cr}$ 的全局极值，因对 $s\geq0$ 有 $s+c_{\max}>0$，分母随 $s$ 增加，故最大值是圆心的 $3f_{\rm s}$；最小值出现在 $(R_{\rm t},\phi_A)$、$(R_{\rm t},\phi_B)$、$(R_{\rm t},\phi_C)$。原条件没有给 $R_{\rm t}$，所以不能输出这些点的唯一数值半径。

<!-- KEEP_STUDENT_END -->

（12）量纲、力矩及适用条件检查。

反力公式第二项的量纲为 $\rho F l/l^2=F$；对三腿求和恢复 $-\boldsymbol F$，对三腿求力矩恢复 $\rho F$。固定 $\theta$ 且 $\rho/l$ 很大时，临界力约为 $3lf_{\rm s}/\rho$，符合最大摩擦力矩有限的趋势。

最终必须区分两层结论：本题给出的三个平衡方程不能唯一决定先滑腿；上述扇区图和临界力则是在相同切向微弹性条件下的完整解答。条件模型忽略接触刚度非线性、支持力变化和倾覆，只描述第一次达到摩擦上限的状态，不自动描述随后的滑动轨迹。

## 六、关键洞察

摩擦系数是接触可承受的反力上限，不是反力分配定律。自平衡的接触力可以改变单腿的负荷，而不改变外部合力和力矩；这正是静力超静定的来源。

相同微弹性模型也可由能量求解：令接触弹性能
$$
W=\frac\kappa2\sum_i|\boldsymbol U+\psi\boldsymbol e_z\times\boldsymbol r_i|^2
=\frac{3\kappa}{2}|\boldsymbol U|^2+\frac{3\kappa l^2}{2}\psi^2.
$$
交叉项因 $\sum_i\boldsymbol r_i=0$ 消失。对 $W-\boldsymbol F\cdot\boldsymbol U-M\psi$ 分别求偏导，得到 $3\kappa\boldsymbol U=\boldsymbol F$、$3\kappa l^2\psi=M=-\rho F$，与解析中的反力完全一致。这是独立的变形能路线，不是把同一平衡式换个名字。

如果问“是否存在一组不超限的静反力”，那是另一个摩擦承载能力问题。所有可能反力组成一个凸可行集；某种实际接触刚度决定加载在该集合中走哪条路径。可行集的极限负荷和某种微弹性路径的首次临界负荷不能未经证明就视为同一个量。

## 七、易错点

把 $\mu N$ 从加载开始就当作每腿的实际摩擦力；只列合力而忘记力矩；把施力极角与施力矢量方向混淆；将顺时针方向的力矩误写为正；把所有两腿等反力线都留下，未检查第三条腿；把腿距 $l$ 与圆面半径混同。

还有两个数学边界容易误判：圆心处 $\theta$ 不唯一；单腿开区域的角度端点是下确界、上确界，并非区域内取得的极小、极大点。最终图应注明采用何种接触模型，不能用漂亮的扇区图掩盖原模型的不足。

## 八、课堂讲解建议

先让学生分别写实际摩擦和最大静摩擦的符号，不立即画三条等长反力。板书六个未知分量、三个平衡方程，再用圆心施力的两组明确反力说明“平衡”与“唯一分配”的区别。

补充微弹性模型后，让学生先把每条腿的位移画成平移加转动，再求反力。分区只比较反力平方，避免不必要的开方。讲两腿边界时保留第三条腿的检验，让学生理解候选边界不是最终边界。

最后把“原条件结论”“明确假设下的条件图”分列，训练模型意识。极值讨论采用扇区闭包与开区域对比，不把极坐标奇点当普通边界点。

## 九、变式训练

（1）相同微弹性模型中，施力点位于 $\rho=l$、$\theta=\pi/3$，求三腿反力大小及首次临界力。

完整解答：此时 $s=1$，对 $A$ 有 $\cos(\theta-\phi_A)=1$，对 $B$、$C$ 均为 $\cos(2\pi/3)=-1/2$。故
$$
|\boldsymbol f_A|=\frac{2F}{3},\quad
|\boldsymbol f_B|=|\boldsymbol f_C|=\frac F3.
$$
首次临界由 $A$ 决定，$F_{\rm cr}=3f_{\rm s}/2$。此时另两腿仅承担 $f_{\rm s}/2$，没有同时滑动。

（2）仍在相同模型中，$\rho=l$、$\theta=0$，求先临界的腿及力。

完整解答：$A$、$C$ 的余弦为 $1/2$，$B$ 的余弦为 $-1$，于是
$$
|\boldsymbol f_A|=|\boldsymbol f_C|=\frac{\sqrt3F}{3},
\qquad |\boldsymbol f_B|=0.
$$
因此 $A$、$C$ 同时临界，$F_{\rm cr}=\sqrt3f_{\rm s}$。$B$ 的平移反力与转动反力恰好抵消。这个例子直接证明“受力点最近的腿”或“转动力矩分摊相同”都不能单独决定实际反力。

（3）仍采用相同各向同性切向刚度，但A腿静摩擦上限为$2f_s$，B、C腿为$f_s$。若力作用于质心投影处，求临界外力。

解：$\rho=0$时无外力矩，三腿位移相同，因此$\mathbf f_i=-\mathbf F/3$。B、C两腿先达到上限，$F_{\rm cr}=3f_s$。不能把三个上限相加成$4f_s$，因为给定刚度决定了载荷分配。一般作用点的结果为
$$F_{\rm cr}=\min_i\frac{3f_{s,i}}{\sqrt{1+s^2+2s\cos(\theta-\phi_i)}},\qquad s=\rho/l.$$
上限只限制可用反力，不替代决定反力的刚度条件。

（4）在主问外力之外另施加逆时针力偶$M_C=\rho F$，抵消原外力的顺时针力矩。求此模型的临界力。

解：合外力矩为零，等切向刚度模型的转动位移为零，三腿只作相同平移，故$\mathbf f_i=-\mathbf F/3$，各腿上限相同时$F_{\rm cr}=3f_s$，与$\rho,\theta$无关。三条反力的合力为$-\mathbf F$，关于质心的力矩因$\sum_i\mathbf r_i=0$而为零。额外力偶必须由独立装置施加；若仍只有原单一外力，不能删去其力矩。
