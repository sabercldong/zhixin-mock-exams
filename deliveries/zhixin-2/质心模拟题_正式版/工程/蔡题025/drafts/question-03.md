# 第 3 题

<!-- question-start -->
一个物体在 $x$—$y$平面内运动。已知它沿 $x$轴的投影，以及沿 $x$轴与 $y$轴夹角平分线方向的投影，分别作非零振幅的简谐振动。两投影的频率没有规定相等。物体运动轨迹可能属于下列哪些形状？

$\mathrm A$：圆；$\mathrm B$：有限抛物线弧；$\mathrm C$：椭圆；$\mathrm D$：八字形曲线。

图示用于区分形状类别，不额外规定未标出的坐标方向、尺度或平衡点。简谐投影有界，故抛物线选项指有限弧段，而不是整条无界抛物线。

![图 3-1　圆、有限抛物线弧、椭圆和八字形四类候选轨迹。](../figures/question-03.png)
<!-- question-end -->

## 一、题型定位

由两个方向的运动投影判断二维轨迹的构造与反例问题。关键是两个已知方向并非互相垂直，也没有同频条件，因此不能直接套用“两个正交同频简谐振动合成为椭圆”的结论排除其他形状。判断“可能”只需要为每一类给出一条符合全部投影条件的实际运动。

## 二、知识点

向量的正交投影；非正交坐标方向的线性变换；简谐振动的振幅、频率、相位和平衡位置；同频正弦量合成；参数方程消元；二倍角公式；Lissajous曲线；有界运动与闭合轨迹；轨迹自交处位置和速度的区别。

两个方向投影都简谐，并不自动使 $x$、$y$各自简谐，也不自动使合加速度指向某个固定中心。这些只有在额外的同频条件下才成立。

## 三、物理图像

定义角平分线单位向量为 $\boldsymbol e_u=(\boldsymbol e_x+\boldsymbol e_y)/\sqrt2$。该方向的投影是 $u=(x+y)/\sqrt2$，不是 $y$，也不是不除以 $\sqrt2$的几何长度 $x+y$。

可以先在辅助的 $(x,u)$平面中画两种简谐信号的Lissajous轨迹，再通过可逆线性变换 $y=\sqrt2u-x$还原真实平面。这个变换会剪切并缩放图形，但不会把圆锥曲线变为任意高次曲线，也不会消除一条八字形曲线的自交点。

同频时，参数曲线由 $\cos\omega t$与 $\sin\omega t$的线性组合组成，非退化情况下是椭圆，圆是其特例。二倍频时可借二倍角公式形成抛物线弧，也可用正弦相位形成八字形。题目没有排除二倍频，所以这些都应检验。

## 四、解题入口

先把已知条件准确写成

$$x=x_0+A\cos(\omega_1t+\phi_1),$$

$$u=u_0+B\cos(\omega_2t+\phi_2),$$

其中 $A,B>0$、$\omega_1,\omega_2>0$，而 $\omega_1$与 $\omega_2$不必相等。再由

$$y=\sqrt2u-x$$

逐项构造四个例子，直接回算两个投影是否都为单一频率的正弦量。不能只画出像某个选项的曲线而不检查投影，也不能在证明可能性时偷偷把频率改成题目不允许的值。

## 五、解析

（1）建立两个投影与真实坐标的关系。

取 $x$、$y$轴正交，角平分线朝第一象限。位置向量为

$$\boldsymbol r=x\boldsymbol e_x+y\boldsymbol e_y.$$

角平分线单位向量长度必须为 $1$：

$$\left|\frac{\boldsymbol e_x+\boldsymbol e_y}{\sqrt2}\right|^2
=\frac{1+1+2\boldsymbol e_x\cdot\boldsymbol e_y}{2}=1.$$

沿它的标量投影为

$$\begin{aligned}
u
&=\boldsymbol r\cdot\boldsymbol e_u\\
&=(x\boldsymbol e_x+y\boldsymbol e_y)\cdot
\frac{\boldsymbol e_x+\boldsymbol e_y}{\sqrt2}\\
&=\frac{x+y}{\sqrt2}.
\end{aligned}$$

乘以 $\sqrt2$并移项，得到

$$\boxed{y=\sqrt2u-x.}$$

图 3-2 左侧显示同一个位置在两个方向上的投影；右侧展示辅助坐标到真实坐标的剪切关系。随后所有构造都用这个式子回算真实 $y$，不把辅助的 $u$轴当成真实 $y$轴。

![图 3-2　两个投影方向与由 $(x,u)$还原 $(x,y)$的线性关系。](../figures/coordinates-03.png)

（2）证明变换可逆，不丢失轨迹信息。

坐标关系可写为

$$\begin{pmatrix}x\\y\end{pmatrix}
=\begin{pmatrix}1&0\\-1&\sqrt2\end{pmatrix}
\begin{pmatrix}x\\u\end{pmatrix}.$$

矩阵行列式是

$$1\times\sqrt2-0\times(-1)=\sqrt2\ne0.$$

因此不同 $(x,u)$点对应不同真实位置；变换存在唯一逆变换。辅助轨迹中的自交仍是同一个真实位置的自交，辅助轨迹的两条不同分支不会由于投影变换而凭空合成一条直线。

运动的平衡位置为 $(x_0,y_0)$，其中 $y_0=\sqrt2u_0-x_0$。平衡位置只平移图形，不改变圆、椭圆、抛物线或自交的类别。简谐振动可以绕非零平衡位置，不能无依据要求所有选项中心恰好位于原点。

（3）构造圆轨迹并检查两投影。

令真实运动为

$$x=A\cos\omega t,\qquad y=A\sin\omega t,$$

其中 $A>0$、$\omega>0$。直接消去时间：

$$x^2+y^2
=A^2(\cos^2\omega t+\sin^2\omega t)=A^2.$$

所以轨迹是半径 $A$的圆。$x$投影显然简谐；角平分线投影为

$$\begin{aligned}
u
&=\frac{A\cos\omega t+A\sin\omega t}{\sqrt2}\\
&=A\cos\left(\omega t-\frac\pi4\right),
\end{aligned}$$

最后一步利用 $\cos(\xi-\pi/4)=(\cos\xi+\sin\xi)/\sqrt2$。因此 $u$也为非零振幅的简谐振动，选项 $\mathrm A$可能。

（4）构造非圆椭圆并检查两投影。

取

$$x=A\cos\omega t,\qquad y=C\sin\omega t,$$

其中 $A,C>0$且 $A\ne C$。消参得

$$\boxed{\frac{x^2}{A^2}+\frac{y^2}{C^2}=1.}$$

角平分线投影为

$$u=\frac{A\cos\omega t+C\sin\omega t}{\sqrt2}.$$

设

$$U=\frac{\sqrt{A^2+C^2}}{\sqrt2},\qquad
\cos\delta=\frac{A}{\sqrt{A^2+C^2}},\quad
\sin\delta=\frac{C}{\sqrt{A^2+C^2}}.$$

因为两个比值平方和为 $1$，可以选取同一相位 $\delta$。于是

$$\begin{aligned}
U\cos(\omega t-\delta)
&=U\cos\delta\cos\omega t+U\sin\delta\sin\omega t\\
&=\frac{A\cos\omega t+C\sin\omega t}{\sqrt2}=u.
\end{aligned}$$

故 $u$也是单一频率的简谐量，选项 $\mathrm C$可能。不同半轴只改变投影振幅与相位，不会使投影变成多频信号。

（5）同频情况下的一般轨迹，说明结论适用范围。

为了看清常见椭圆结论为何不是全题结论，先假定两个已知投影确实同频，并把平衡位置平移到原点，时间原点选到 $x$最大时：

$$x=A\cos\omega t,\qquad
u=B\cos(\omega t+\delta).$$

由角和公式，真实 $y$为

$$\begin{aligned}
y
&=\sqrt2B\cos(\omega t+\delta)-A\cos\omega t\\
&=(\sqrt2B\cos\delta-A)\cos\omega t
-\sqrt2B\sin\delta\sin\omega t.
\end{aligned}$$

定义 $C_1=\sqrt2B\cos\delta-A$、$C_2=-\sqrt2B\sin\delta$。若 $C_2\ne0$，则

$$\cos\omega t=\frac xA,\qquad
\sin\omega t=\frac{y-C_1x/A}{C_2}.$$

用正弦、余弦平方和为 $1$消参：

$$\boxed{\frac{x^2}{A^2}
+\frac{(y-C_1x/A)^2}{C_2^2}=1.}$$

这是可能倾斜的椭圆。若 $\sin\delta=0$，则 $C_2=0$，轨迹退化为线段 $y=C_1x/A$，不能继续除以 $C_2$。图 3-3将圆、非圆椭圆和退化线段分开；它仅用于同频子问题，不能替代后面的二倍频构造。

![图 3-3　同频投影合成的圆、椭圆及零相位差的退化线段。](../figures/samefreq-03.png)

（6）构造有限抛物线弧。

令两个已知投影为

$$x=A\cos\omega t,\qquad
u=B\cos2\omega t,$$

其中 $A,B>0$。它们的频率分别是 $\omega$与 $2\omega$，都符合简谐条件。利用二倍角恒等式

$$\cos2\omega t=2\cos^2\omega t-1,$$

得到

$$u=B\left(2\frac{x^2}{A^2}-1\right).$$

代入真实坐标关系：

$$\boxed{y=\frac{2\sqrt2B}{A^2}x^2-x-\sqrt2B.}$$

这是关于 $x$的二次函数，而且最高次系数非零，故为抛物线。这里的 $-x$项来自角平分线与 $y$轴不同，不能删掉后声称投影仍是同一个运动。

将它配方，设 $a_p=2\sqrt2B/A^2$，则

$$\begin{aligned}
y
&=a_px^2-x-\sqrt2B\\
&=a_p\left(x^2-\frac{x}{a_p}\right)-\sqrt2B\\
&=a_p\left(x-\frac1{2a_p}\right)^2
-\frac1{4a_p}-\sqrt2B.
\end{aligned}$$

所以顶点为

$$x_v=\frac{A^2}{4\sqrt2B},\qquad
y_v=-\frac{A^2}{8\sqrt2B}-\sqrt2B.$$

改变 $u$振动的相位为 $\pi$，即取 $u=-B\cos2\omega t$，则抛物线开口方向反转，得到向下开口的有限弧，与候选图 $\mathrm B$的类别一致。

因为 $|x|\leq A$，实际只走过抛物线的有限部分。一个周期内 $\cos\omega t$从 $1$降到 $-1$再回到 $1$，所以物体沿同一弧段往返，不要求沿无界抛物线越走越远。

图 3-4左侧用二倍频投影展示消参，右侧在真实平面画弧段，并保留坐标剪切产生的线性项。选项 $\mathrm B$可能。

![图 3-4　二倍频余弦投影对应的辅助抛物线与真实平面有限弧。](../figures/parabola-03.png)

（7）检查抛物线例子的两个投影确实单频。

从所得真实轨迹反算：

$$\begin{aligned}
\frac{x+y}{\sqrt2}
&=\frac{1}{\sqrt2}
\left[x+\frac{2\sqrt2B}{A^2}x^2-x-\sqrt2B\right]\\
&=B\left(2\frac{x^2}{A^2}-1\right)\\
&=B\cos2\omega t.
\end{aligned}$$

两处 $x$精确相消。如果误用通常的正交构造 $x=A\cos\omega t$、$y=B\cos2\omega t$，角平分线投影会包含 $\omega$和 $2\omega$两种频率，不再是单一简谐振动。正确例子必须带有真实 $y$中的 $-x$项。

（8）构造八字形并检查自交。

取已知投影

$$x=A\sin\omega t,\qquad
u=B\sin2\omega t.$$

两个投影仍分别是非零振幅、单一频率的简谐振动。真实运动为

$$\boxed{y=\sqrt2B\sin2\omega t-A\sin\omega t.}$$

先在辅助平面中消参。由

$$\sin2\omega t=2\sin\omega t\cos\omega t,$$

有

$$u=2B\frac xA\cos\omega t.$$

平方后使用 $\cos^2\omega t=1-x^2/A^2$，得到

$$\boxed{u^2=\frac{4B^2x^2}{A^2}
\left(1-\frac{x^2}{A^2}\right).}$$

当 $x=0$时 $u=0$；当 $0<|x|<A$时有正、负两支；当 $x=\pm A$时两支相接。这是左右各一环、在原点交叉的八字形曲线。

在真实平面中用 $u=(x+y)/\sqrt2$替换，得到

$$\boxed{(x+y)^2=
\frac{8B^2x^2}{A^2}
\left(1-\frac{x^2}{A^2}\right).}$$

线性变换可逆，因而两环和自交点保持，形状可以被剪切但仍是八字形。图 3-5同时画辅助八字形与真实轨迹，避免把辅助坐标图直接当作真实 $x$—$y$图。

![图 3-5　二倍频正弦投影形成的八字形及其真实平面剪切像。](../figures/eight-03.png)

（9）自交位置允许有不同速度。

在 $t=0$与 $t=\pi/\omega$两时刻，均有 $x=0$、$u=0$、$y=0$。但速度分别为

$$\begin{aligned}
t=0:&\quad
\dot x=A\omega,\quad
\dot y=2\sqrt2B\omega-A\omega,\\
t=\frac\pi\omega:&\quad
\dot x=-A\omega,\quad
\dot y=2\sqrt2B\omega+A\omega.
\end{aligned}$$

两速度方向通常不同，因此形成穿过同一点的两条分支。这并不违反运动学：同一位置在不同时间可以具有不同速度。本题只给运动投影，没有额外要求力只依赖位置且初态在自交处相同。

回算角平分线投影：

$$\frac{x+y}{\sqrt2}=B\sin2\omega t,$$

正好恢复原构造。选项 $\mathrm D$可能。

（10）汇总答案并说明“可能”的逻辑。

四个构造均满足两个指定方向的简谐投影，因此

$$\boxed{\mathrm A,\ \mathrm B,\ \mathrm C,\ \mathrm D\ \text{均可能}.}$$

这不等于“所有符合投影条件的轨迹只能是这四类”。例如频率比为 $2:3$时还可以得到其他多叶Lissajous曲线；频率比无理时，运动一般不闭合。题目只是在给出的四类候选中判断存在性。

若另外要求两投影同频，那么非退化轨迹是椭圆，圆是其中一类，抛物线弧和八字形都不属于这个同频子问题。这个附加结论不能反过来作为本题未给的条件。

（11）有界性、周期与量纲检查。

由两个已知简谐投影的振幅界可得

$$|x-x_0|\leq A,\qquad
|x+y-\sqrt2u_0|\leq\sqrt2B.$$

两条带状区域的交集是有限平行四边形，因此真实轨迹始终有界。有限抛物线弧符合该条件，整条无限抛物线则不符合。

若 $\omega_2/\omega_1=p/q$为最简有理比，可以取公共周期 $T=2\pi q/\omega_1=2\pi p/\omega_2$；经过这个时间，两个投影与速度都回到初值，真实运动也重复。无理频率比不能找到这样的公共周期，但仍然有界。

抛物线式中 $2\sqrt2B/A^2$量纲为长度的倒数，乘以 $x^2$后为长度；八字形式两侧均为长度平方。所有例子的时间参数都是 $\omega t$，无量纲，相位与频率没有混淆。

## 六、关键洞察

“可能”是构造命题，给出一个严格例子比凭形状直觉排除更可靠。两个非平行投影足以恢复位置，却不足以限定它们的频率关系；可逆线性变换保留了辅助轨迹的许多性质，构造因而十分直接。

同频性质可以从向量方程再证明：将平衡位置平移后，$x$与 $u$同满足 $\ddot x=-\omega^2x$、$\ddot u=-\omega^2u$，因此

$$\ddot y=\sqrt2\ddot u-\ddot x=-\omega^2y.$$

从而 $\ddot{\boldsymbol r}=-\omega^2\boldsymbol r$。这是各向同性二维谐振模型，角动量守恒，非零角动量下轨迹椭圆。不同频率时，上面的同一 $\omega^2$不能提出，真实 $y$一般是双频信号；本题因此允许更多形状。

任意非平行的两个投影方向都可用同样方法。若夹角为 $\chi$，$u=x\cos\chi+y\sin\chi$，则 $y=(u-x\cos\chi)/\sin\chi$。只有 $\sin\chi=0$时信息不足，不能由两投影唯一还原平面运动。

## 七、易错点

把角平分线投影等同于 $y$，会使二倍频例子违反原条件。把投影长度写成 $x+y$则漏掉单位向量的归一化；虽然可以吸收到振幅中，但逐图标注和方程不能前后不一致。

只记得“简谐合成椭圆”而不检查同频条件，会误排除抛物线和八字形。把有限弧段当成整条无界抛物线，会与简谐投影的有界性矛盾。自交并不要求物体同时出现在两个位置，也不要求同一点必须有相同速度。

仅凭草图相似不能证明某个特定朝向、长度范围的曲线就是所给运动。正式判断应使用明确参数方程和投影回算，草图只显示形状类别。退化线段需要另行辨认，不应在 $\sin\delta=0$时继续除以零。

## 八、课堂讲解建议

先让学生在平面中画 $x$轴、$y$轴和45度投影方向，用点积写出 $u$。板书第一行就标注“已知 $x$、$u$，不是已知 $x$、$y$”，之后所有例子都要求学生回算 $(x+y)/\sqrt2$。

按圆、椭圆、抛物线、八字形顺序展示构造。同频两例建立熟悉感，再用二倍频例子指出遗漏条件。在抛物线例子中保留 $-x$项，让学生观察它如何在投影回算时相消；不要为了草图对称而删除这个关键项。

用八字形的两个过原点时刻计算速度，说明位置图不包含全部初态。最后让学生把答案改写为“为每类找到一个满足条件的例子”，形成存在性证明的习惯。

## 九、变式训练

（1）两个已知投影同频，分别为 $x=A\cos\omega t$、$u=B\cos(\omega t+\delta)$。求轨迹成为圆所需的振幅和相位条件。

完整解答：真实 $y=C_1\cos\omega t+C_2\sin\omega t$，其中 $C_1=\sqrt2B\cos\delta-A$、$C_2=-\sqrt2B\sin\delta$。圆要求两个参数基向量 $(A,C_1)$和 $(0,C_2)$等长且正交。正交给 $C_1C_2=0$；非退化圆有 $C_2\ne0$，故 $C_1=0$。等长给 $A^2=C_2^2$，所以

$$\sqrt2B\cos\delta=A,\qquad
2B^2\sin^2\delta=A^2.$$

第一式平方后为 $2B^2\cos^2\delta=A^2$，与第二式相加得 $2B^2=2A^2$。因此 $B=A$，再代回得

$$\boxed{B=A,\qquad \delta=\pm\frac\pi4\pmod{2\pi}.}$$

由于 $A,B$均定义为正振幅，不能把 $\cos\delta=-1/\sqrt2$也当作同一原点和相位约定下的条件。两相位号对应两种相反的绕行方向。

（2）将第二个投影方向改为与 $x$轴夹角 $\chi$，$0<\chi<\pi$。已知 $x=A\cos\omega t$、$u=B\cos2\omega t$，求真实轨迹，并分析 $\chi\to0$为什么不能直接代入。

完整解答：由 $u=x\cos\chi+y\sin\chi$，

$$y=\frac{u-x\cos\chi}{\sin\chi}.$$

用二倍角公式消去时间，得到

$$\boxed{y=
\frac{2B}{A^2\sin\chi}x^2
-x\cot\chi-\frac{B}{\sin\chi},\qquad |x|\leq A.}$$

因 $\sin\chi>0$且 $B>0$，仍是有限抛物线弧。令 $\chi=\pi/4$恢复主解。若 $\chi\to0$，两个投影方向重合，坐标变换的行列式趋于零；两个不同频率的给定投影不可能在重合方向上同时成立。分母发散提示的是条件退化，而不是物体真的可以在同一投影下产生任意无限振幅。

（3）两投影的非零频率比$\omega_u/\omega_x=p/q$，$p,q$互素。求轨迹重复周期，并讨论无理频率比。

解：共同相位恢复需要$\omega_xT=2\pi q$、$\omega_uT=2\pi p$，故完整参数化运动的周期$T=2\pi q/\omega_x$。例如比值$3/2$时为$4\pi/\omega_x$。无理比时相位对稠密覆盖二维环面，而线性关系$y=\sqrt2u-x$把两个有界投影区间映成一个有界平行四边形，轨迹在其中稠密。非周期不意味着无限远运动；特殊零振幅退化情形需单独排除。

（4）两投影同频，$x=A\cos\omega t$、$u=B\cos(\omega t+\delta)$。求椭圆面积及质点绕原点角动量。

解：$y=C_1\cos\omega t+C_2\sin\omega t$，其中$C_1=\sqrt2B\cos\delta-A$、$C_2=-\sqrt2B\sin\delta$。线性映射的行列式为$AC_2$，故
$$S_{\rm ellipse}=\pi\sqrt2AB|\sin\delta|,\qquad
L_z=m(x\dot y-y\dot x)=m\omega AC_2.$$
相位符号决定绕行方向，面积与其绝对值有关。$\delta=0$或$\pi$时面积为零、轨迹退化成线段，不能继续称为非退化椭圆。
