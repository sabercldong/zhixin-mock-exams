# 第 1 题

一个轴对称“子弹头”的接触外表面为旋转抛物面，轻质壳内的全部质量 $m$ 集中在中轴线上、距顶点 $h$ 处，绕质心的转动惯量为零。重力加速度 $g$ 竖直向下，接触摩擦足够大。母线的极坐标方程为
$$
\rho=\frac{p}{1+\cos\theta},\qquad p>0.
$$
（1）求子弹头能稳定立在水平桌面上的最小高度 $h_{\min}$，用 $p$ 表示。
（2）取 $h=p/2$，求小扰动下的振动周期 $T$，用 $g,p$ 表示。

![图 1-1　旋转抛物面的顶点、质心及对称轴。](../figures/question-01.png)

## 一、题型定位

这是曲面刚体在水平面上纯滚动的小振动问题。稳定性来自质心高度随倾角的变化，不是单看“质心越低越稳”，更不是把接触点固定成一个永远不动的铰链。接触位置会沿抛物面移动，瞬时转动中心也随之改变。

题目把壳质量和质心转动惯量都取为零，因此全部动能是嵌入质点的平动动能。纯滚动约束仍然存在，不能因此断言物体没有惯性。第（1）问使用“最小高度”，但按照图示顶点朝下、质心位于顶点上方的几何，稳定性给出的是 $h$ 的上限；下面保留题设问法并明确说明实际稳定范围。

## 二、知识点

极坐标到直角坐标的转换使用 $\rho^2=X^2+Y^2$。平面纯滚动时，接触点相对于桌面的瞬时速度为零，任意刚体点的速度可由该瞬时中心计算。稳定平衡要求势能在平衡位置有局部极小；二次项为零时必须继续检查高阶项。

若小振动的动能和势能分别为
$$
K=\frac12 M_{\rm eff}\dot\alpha^2,\qquad
U=U_0+\frac12 k_{\rm eff}\alpha^2,
$$
则运动方程为 $M_{\rm eff}\ddot\alpha+k_{\rm eff}\alpha=0$，周期为 $2\pi\sqrt{M_{\rm eff}/k_{\rm eff}}$。这里的广义坐标是角度，$M_{\rm eff}$ 的量纲为转动惯量，不是质量本身。

## 三、物理图像

把空间中的滚动方向选定后，轴对称性允许在包含该方向和对称轴的竖直截面中分析。桌面接触母线的一点 $Q$，不是任意穿过曲面的点。倾斜后，母线在 $Q$ 的切线水平，法线竖直。质心 $C$ 的高度既受到轴线倾斜影响，也受到顶点被抬起的影响，两部分必须同时保留。

重力产生回复作用的条件可表述为：微小倾斜后质心升高。若质心下降，重力会继续增大倾角。曲率中心只在二阶判断中提供简便直觉；要求周期时仍须计算动能。

## 四、解题入口

先从极坐标母线求出顶点附近曲线的准确表达式，再用“接触处切线水平”确定接触坐标。由接触坐标计算质心高度，展开得到稳定性和势能系数。最后利用纯滚动的瞬时中心求质心速度，从而得到小振动的惯性系数。

本题的参数 $p$ 同时决定顶点曲率半径，但这不是可以直接猜出的定义。必须通过母线方程验证，避免将焦距 $p/2$ 与曲率半径 $p$ 混淆。

## 五、解析

（1）把极坐标方程转成母线直角坐标。

在原极坐标轴方向记坐标为 $X$，垂直方向为 $Y$。由于 $\rho\cos\theta=X$，
$$
\rho+X=p.
$$
移项后平方：
$$
\begin{aligned}
\rho&=p-X,\\
X^2+Y^2&=(p-X)^2
=p^2-2pX+X^2,\\
Y^2&=p^2-2pX.
\end{aligned}
$$
平方前要求 $p-X\ge0$；所得抛物线满足 $X\le p/2$，所以没有引入不合条件的支路。顶点位于 $(p/2,0)$。

以顶点为原点，把沿物体轴线朝壳内部的坐标记为 $z=p/2-X$，横向坐标记为 $s=Y$，则
$$
\boxed{z=\frac{s^2}{2p}.}
$$
质心的体坐标为 $(s_C,z_C)=(0,h)$。曲线的一阶和二阶导数是
$$
z'(s)=\frac{s}{p},\qquad z''(s)=\frac1p.
$$
顶点处的曲率半径为
$$
{\cal R}_0=\frac{[1+z'(0)^2]^{3/2}}{|z''(0)|}=p.
$$
焦点距顶点为 $p/2$，两种长度不可混用。

（2）规定倾角及接触位置。

设体坐标的 $z$ 轴相对竖直向上方向倾斜，采用如下旋转约定：
$$
x=s\cos\alpha-z\sin\alpha,\qquad
y=s\sin\alpha+z\cos\alpha.
$$
这里先忽略平移；平移只改变所有点的共同位置，不改变切线斜率。由母线参数 $s$ 求世界坐标的竖直导数：
$$
\frac{dy}{ds}
=\sin\alpha+\frac{s}{p}\cos\alpha.
$$
在接触点 $Q$，切线水平，故 $dy/ds=0$。在顶点附近 $|\alpha|<\pi/2$，有
$$
\boxed{s_Q=-p\tan\alpha,\qquad
z_Q=\frac p2\tan^2\alpha.}
$$
图1-2中的负号来自本节的旋转约定：正倾角时接触点移到体坐标 $s<0$ 一侧。改变倾角正方向会同时改变 $s_Q$ 的号，但不能只改其中一处。

![图 1-2　倾斜后的水平切线、接触点及质心高度。](../figures/contact-01.png)

（3）由接触点高度归零计算质心高度。

旋转但未平移时，接触点高度为
$$
y_Q=s_Q\sin\alpha+z_Q\cos\alpha.
$$
把整个物体平移使 $Q$ 位于桌面 $y=0$，质心实际高度为
$$
H_C=h\cos\alpha-y_Q.
$$
代入上一步：
$$
\begin{aligned}
H_C
&=h\cos\alpha
+p\tan\alpha\sin\alpha
-\frac p2\tan^2\alpha\cos\alpha\\
&=h\cos\alpha+\frac p2\frac{\sin^2\alpha}{\cos\alpha}\\
&=\left(h-\frac p2\right)\cos\alpha
+\frac p{2\cos\alpha}.
\end{aligned}
$$
第二行把两项共同写为 $\sin^2\alpha/\cos\alpha$；第三行使用 $\sin^2\alpha=1-\cos^2\alpha$。因此
$$
\boxed{H_C(\alpha)=
\left(h-\frac p2\right)\cos\alpha+\frac p2\sec\alpha.}
$$
当 $\alpha=0$ 时恢复 $H_C=h$，几何初态正确。这个高度公式与接触点在桌面上的水平平移无关，纯滚动与否不改变瞬时几何高度。

（4）展开势能，判断通常的小振动稳定性。

使用以弧度计量的泰勒展开：
$$
\cos\alpha=1-\frac{\alpha^2}{2}+\frac{\alpha^4}{24}+O(\alpha^6),
$$
$$
\sec\alpha=1+\frac{\alpha^2}{2}
+\frac{5\alpha^4}{24}+O(\alpha^6).
$$
逐项整理：
$$
\begin{aligned}
H_C-h
&=\left[-\frac12\left(h-\frac p2\right)+\frac p4\right]\alpha^2\\
&\quad+\left[\frac1{24}\left(h-\frac p2\right)+\frac{5p}{48}\right]\alpha^4
+O(\alpha^6)\\
&=\frac{p-h}{2}\alpha^2+\frac{h+2p}{24}\alpha^4+O(\alpha^6).
\end{aligned}
$$
势能为 $U=mgH_C$，所以在 $0<h<p$ 时二次项正，顶点朝下是稳定的小振动平衡；在 $h>p$ 时二次项负，是不稳定平衡。图1-3比较的是质心高度变化，不是不同物体的绝对势能零点。

![图 1-3　质心高度相对变化与稳定、临界及不稳定状态。](../figures/stability-01.png)

（5）单独检查 $h=p$，不能在二次项为零时直接称“不稳定”。

取 $h=p$，有
$$
H_C=\frac p2(\cos\alpha+\sec\alpha).
$$
对于 $|\alpha|<\pi/2$，令 $c_\alpha=\cos\alpha>0$：
$$
\begin{aligned}
H_C-p
&=\frac p2\left(c_\alpha+\frac1{c_\alpha}-2\right)\\
&=\frac p{2c_\alpha}(1-c_\alpha)^2\ge0.
\end{aligned}
$$
除了 $\alpha=0$，邻近角度的势能仍然升高。因此 $h=p$ 也是局部稳定的，但没有线性回复刚度，不能称为通常的简谐小振动。首个非零项为
$$
H_C-p=\frac p8\alpha^4+O(\alpha^6).
$$
稳定范围可写为 $0<h\le p$；若要求非零线性回复系数和有限的振幅无关周期，则为 $0<h<p$。

因此第（1）问实际给出的是稳定上限 $h_{\max}=p$，不是一个正的稳定下限。$h$ 可以任意接近零；其下确界为零，$h=0$ 时嵌入质点就在接触顶点，角向动能退化，不能继续使用下面的普通小振动公式。

（6）用瞬时转动中心建立动能。

无滑动接触使接触材料点的瞬时速度为零。刚体角速度为 $\dot\alpha$，所以
$$
|\boldsymbol v_C|^2
=\dot\alpha^2\,|\boldsymbol{QC}|^2.
$$
体坐标下
$$
\boldsymbol{QC}=(-s_Q,h-z_Q),
$$
长度在旋转前后不变：
$$
D_C^2=s_Q^2+(h-z_Q)^2.
$$
图1-4中的 $\boldsymbol{QC}$ 正是动能中的几何长度，并不是一条固定摆长。

![图 1-4　纯滚动瞬时中心与质心速度的垂直关系。](../figures/velocity-01.png)

全部质量集中于 $C$，绕质心的惯量为零，故
$$
\boxed{K=\frac12 mD_C^2(\alpha)\dot\alpha^2.}
$$
如果壳有不可忽略的绕质心惯量 $I_C$，应额外加 $\tfrac12 I_C\dot\alpha^2$；本题明确不加这一项。摩擦力和支持力作用于瞬时静止接触点，纯滚动时不做功，机械能可守恒。

（7）说明为何小振动只保留 $D_C^2(0)$。

接触坐标展开为
$$
s_Q=-p\alpha+O(\alpha^3),\qquad
z_Q=\frac p2\alpha^2+O(\alpha^4).
$$
所以
$$
\begin{aligned}
D_C^2
&=p^2\alpha^2+
\left(h-\frac p2\alpha^2\right)^2+O(\alpha^4)\\
&=h^2+(p^2-ph)\alpha^2+O(\alpha^4).
\end{aligned}
$$
把角幅和角速度都视为一阶小量，$\alpha^2\dot\alpha^2$ 是四阶，不能进入线性方程。因此二阶动能为
$$
K^{(2)}=\frac12 mh^2\dot\alpha^2.
$$
这不是把接触点长期固定；只是用瞬时中心正确求得的系数在平衡位置取值。与之配对的二阶势能为
$$
U^{(2)}=mgh+\frac12 mg(p-h)\alpha^2.
$$

（8）逐项写出线性运动方程。

由拉格朗日方程
$$
\frac d{dt}\frac{\partial K}{\partial\dot\alpha}
-\frac{\partial K}{\partial\alpha}
+\frac{\partial U}{\partial\alpha}=0
$$
得到
$$
mh^2\ddot\alpha+mg(p-h)\alpha=0.
$$
约去 $m$，再除以 $h^2>0$：
$$
\ddot\alpha+\frac{g(p-h)}{h^2}\alpha=0.
$$
当 $0<h<p$，
$$
\omega^2=\frac{g(p-h)}{h^2},\qquad
\boxed{T=\frac{2\pi h}{\sqrt{g(p-h)}}.}
$$
$h\to p^-$ 时回复二次项趋零，线性周期趋于无穷，与临界状态一致；$h>p$ 时 $\omega^2<0$，不是实周期，而是指数增长或衰减的线性解。

（9）代入 $h=p/2$，保留计算步骤。

此时
$$
h^2=\frac{p^2}{4},\qquad p-h=\frac p2.
$$
于是
$$
\begin{aligned}
\omega^2
&=\frac{g(p/2)}{p^2/4}=\frac{2g}{p},\\
\omega&=\sqrt{\frac{2g}{p}},\\
T&=\boxed{2\pi\sqrt{\frac{p}{2g}}.}
\end{aligned}
$$
直接检查能量也得到
$$
K^{(2)}=\frac{mp^2}{8}\dot\alpha^2,\qquad
U-mgh=\frac{mgp}{4}\alpha^2,
$$
因此 $\omega^2=(mgp/2)/(mp^2/4)=2g/p$。周期量纲为 $\sqrt{\text{长度}/\text{加速度}}$，即时间；质量消去符合重力回复与惯性都正比于 $m$ 的模型。

（10）检查滚动、离地与小振幅条件。

上面的结果只描述顶点附近的纯滚动接触。小振幅下质心加速度连续且趋于零，支持力趋于 $mg>0$，所以不会自动离地；所需摩擦力随幅度趋零，可由题设“足够大摩擦”保证。但有限振幅时仍须另验支持力非负、摩擦力不超过最大静摩擦力，以及接触点是否仍位于实际壳面。

题目没有给出壳的截断边缘，因此不能把无限母线的计算外推到任意倾角。周期仅取 $\alpha\to0$ 的稳定小振动极限；临界 $h=p$、退化 $h=0$ 均须单独处理，不能强行代入为普通有限周期。

## 六、关键洞察

稳定性首先是几何问题。曲面顶点被抬起的二阶高度为 $p\alpha^2/2$，轴线上质点的倾斜降低贡献为 $h\alpha^2/2$；两者差值决定 $p-h$。因此曲率中心的高度 $p$ 是分界，但临界点是否稳定要看四阶项。

保留有限壳惯量时，同一势能不变，小振动变为
$$
(I_C+mh^2)\ddot\alpha+mg(p-h)\alpha=0,
$$
$$
T=2\pi\sqrt{\frac{I_C+mh^2}{mg(p-h)}}.
$$
这条式子提供独立惯性检查：$I_C=0$ 恢复本题，增加壳惯量只增加周期，不改变稳定高度范围。

完整能量方程为
$$
\frac12 mD_C^2\dot\alpha^2+mgH_C={\cal E}.
$$
若要得到有限角度的方程，不能遗漏变系数动能：
$$
D_C^2\ddot\alpha+\frac12\frac{dD_C^2}{d\alpha}\dot\alpha^2
+g\frac{dH_C}{d\alpha}=0.
$$
线性化时第二项是更高阶，有限振幅时却不可删除。这把小振动公式与完整滚动模型联系起来。

## 七、易错点

把焦距 $p/2$ 当曲率半径，会错误地判断 $h=p/2$ 是临界位置。只计算 $h\cos\alpha$ 而忽略接触曲面的抬升，则会把所有状态都误判为不稳定。把瞬时接触点当固定铰链，会在有限角度下得到错误的质心轨迹。

“没有质心转动惯量”不等于没有动能。$\boldsymbol{QC}$ 与角速度产生质心平动，惯性系数 $mh^2$ 不能漏掉。对 $h=p$ 只查看二阶项，会漏掉四阶稳定势阱。对 $h\to0$ 的退化质量分布外推常规周期，则会忽略模型的奇异性。

## 八、课堂讲解建议

先让学生把极坐标方程转成 $z=s^2/(2p)$，在图1-2上指出“水平切线”提供哪一条方程。随后把质心高度拆成顶点抬升与轴线倾斜两部分，要求学生解释两个二阶项的正负号。

板书动能时先画图1-4中的接触瞬时中心，再写 $\boldsymbol v_C\perp\boldsymbol{QC}$，不要先套摆的公式。最后并排比较 $h<p$、$h=p$、$h>p$ 的势能图，说明“二次项为零”与“不稳定”不同，再检查临界点的高阶项。

<!-- KEEP_TOGETHER_START -->

## 九、变式训练

（1）取 $h=p/3$，求稳定小振动周期并与本题比较。

解：$p-h=2p/3$，所以
$$
\omega^2=\frac{g(2p/3)}{p^2/9}=\frac{6g}{p},\qquad
T_1=2\pi\sqrt{\frac p{6g}}.
$$
本题 $h=p/2$ 的周期为 $T_*=2\pi\sqrt{p/(2g)}$，故 $T_1/T_*=1/\sqrt3$。变短既来自更小的惯性系数，也来自更大的回复系数，不能只归因于其中一项。

（2）临界 $h=p$，给定小而非零振幅 $A$，求周期如何依赖 $A$。

解：首项动能为 $\tfrac12 mp^2\dot\alpha^2$，首项势能为 $mgp\alpha^4/8$。转折点 $\alpha=A$ 时
$$
\frac12 mp^2\dot\alpha^2
=\frac{mgp}{8}(A^4-\alpha^4).
$$
因此四分之一周期为
$$
\frac T4
=2\sqrt{\frac pg}\int_0^A\frac{d\alpha}{\sqrt{A^4-\alpha^4}}
=\frac2A\sqrt{\frac pg}\int_0^1\frac{du}{\sqrt{1-u^4}}.
$$
即
$$
T=\frac8A\sqrt{\frac pg}\int_0^1\frac{du}{\sqrt{1-u^4}}.
$$
积分为有限正数，而 $T\propto A^{-1}$，振幅趋零时周期发散。这与 $h=p$ 稳定但没有通常简谐频率的结论一致。

<!-- KEEP_TOGETHER_END -->

（3）测得线性周期$T=2\pi\sqrt{p/g}$，反求稳定区内的$h$。

解：令$\zeta=h/p$，周期式给$\zeta^2+\zeta-1=0$。稳定区$0<\zeta<1$只接受
$$h=\frac{\sqrt5-1}{2}p.$$
一般测量可记$\Lambda=gT^2/(4\pi^2p)$，得$\zeta=(\sqrt{\Lambda^2+4\Lambda}-\Lambda)/2$。$\zeta^2/(1-\zeta)$严格递增，反演唯一；周期很大意味着接近临界高度，不能按普通有限刚度处理。

（4）内部质量重新分布，质心位置不变，但绕质心惯量为$I_C>0$，求新周期。取$h=p/2,I_C=mp^2/4$核算。

解：小角度质心速率为$h|\dot\alpha|$，动能为$(mh^2+I_C)\dot\alpha^2/2$，势能增量$mg(p-h)\alpha^2/2$，所以
$$T=2\pi\sqrt{\frac{mh^2+I_C}{mg(p-h)}}.$$
给定参数得$T=2\pi\sqrt{p/g}$，为原周期的$\sqrt2$倍。惯量改变时间尺度，不改变势能的稳定符号；$h=p$仍需高阶分析。这是新的质量分布，不能同时声称质心惯量为零。
