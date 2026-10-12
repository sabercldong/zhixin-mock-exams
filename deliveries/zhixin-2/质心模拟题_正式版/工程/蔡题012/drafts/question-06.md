# 第6题　滑套连杆机构的速度与加速度

<!-- question-start -->

平面机构中，杆 $AB$ 以恒定速度 $v$ 水平向右平移。其端点 $B$ 是套在绕固定点 $O$ 转动的杆 $OC$ 上的滑套，$B$ 可沿 $OC$ 滑动。滑块 $E$ 沿过 $O$ 的水平轨道运动，固定长度连杆 $DE$ 连接杆 $OC$ 上的固定铰点 $D$ 与 $E$。$AB$ 与 $OE$ 两水平线的垂直距离为 $b$。

在图示瞬间，$OC$ 与水平夹角 $\alpha=60^\circ$，连杆 $DE$ 向右下方与水平夹角 $\beta=30^\circ$，且 $OD=BD$。求杆 $OC$ 的角速度、角加速度，以及滑块 $E$ 的速度和加速度。取向右为水平正向、逆时针为角度正向。$D$ 是杆上固定材料点，等距关系只在该瞬间成立。

![图 6-1 题目所用的物理模型](../figures/question-06.png)

<!-- question-end -->

## 一、题型定位

滑套 $B$ 有一项沿杆的相对运动，而 $D$ 是杆的固定材料点。这两个点的位置虽然在指定瞬间有 $OD=BD$，但不能在求导时把 $D$ 永远写成 $B$ 的中点。机构加速度题中，瞬时几何关系与全程约束必须区分。

杆 $OC$ 的角运动可先由 $B$ 的水平轨迹确定；再求固定点 $D$ 的速度、加速度；最后通过连杆 $DE$ 的固定长度与 $E$ 的水平约束求输出。这个顺序既便于矢量法，也便于坐标微分法。

## 二、知识点

对绕固定点的杆上材料点，有 $\mathbf v_D=\dot\alpha\,\hat{\mathbf z}\times\mathbf r_D$，$\mathbf a_D=\ddot\alpha\,\hat{\mathbf z}\times\mathbf r_D-\dot\alpha^2\mathbf r_D$。连杆两端的相对速度垂直于连杆：$(\mathbf v_E-\mathbf v_D)\cdot\mathbf r_{ED}=0$。

固定连杆长度还给加速度约束

$$(\mathbf a_E-\mathbf a_D)\cdot\mathbf r_{ED}
+|\mathbf v_E-\mathbf v_D|^2=0.$$

第二项不能省略，它来自对长度平方约束的二次求导。滑块 $E$ 的竖向速度和加速度都为零。角速度与角加速度可以异号，角加速度为正并不表示当时正在逆时针转动。

## 三、物理图像

$B$ 在高度 $b$ 的水平线上向右走，$OB$ 越来越倾斜向右，角度 $\alpha$ 减小，所以杆顺时针转动。转动速度的大小随角度变化；本题瞬间的角加速度为逆时针方向，表示顺时针转动正在减慢。

固定铰点 $D$ 同时向右和向下运动。连杆另一端 $E$ 只能水平走，因此相对速度必须沿连杆法向。加速度中既有连杆转动的法向项，也有杆 $OC$ 的切向与向心项，单凭速度三角形不能得到完整加速度。

## 四、解题入口

令 $x_B=b\cot\alpha$，直接对时间求导，利用 $\dot x_B=v$、$\ddot x_B=0$，先得到 $\dot\alpha$、$\ddot\alpha$。再由瞬时几何求固定长度 $d=OD=b/\sqrt3$、$\ell=DE=b$。

然后保持 $d,\ell$ 为常数写 $x_D=d\cos\alpha$、$y_D=d\sin\alpha$。取 $E$ 位于 $D$ 的右侧，得 $x_E=x_D+\sqrt{\ell^2-y_D^2}$。这是一条可直接两次微分的标量路径，也能用于数值差分检查。

## 五、解析

（1）杆 $OC$ 的角速度。

由套点高度不变，$OB=b/\sin\alpha$、$x_B=b\cot\alpha$。因此

$$v=-b\csc^2\alpha\,\dot\alpha,\qquad
\dot\alpha=-\frac vb\sin^2\alpha.$$

代入 $\alpha=60^\circ$，得到

$$\boxed{\dot\alpha=-\frac{3v}{4b}}.$$

负号表示顺时针。若题目仅问角速度大小，答案为 $3v/(4b)$，但在加速度计算中必须继续使用带符号角速度，尤其是切向项和相对速度方向不能随意改号。


![图 6-2 初始条件与约束关系](../figures/angular-06.png)

（2）角加速度。

对 $\dot\alpha=-v\sin^2\alpha/b$ 求导，利用 $v$ 为常数：

$$\ddot\alpha=-\frac{2v}{b}\sin\alpha\cos\alpha\,\dot\alpha
=\frac{2v^2}{b^2}\sin^3\alpha\cos\alpha.$$

故

$$\boxed{\ddot\alpha=\frac{3\sqrt3v^2}{8b^2}}.$$

这是逆时针角加速度。角速度的绝对值在当前区间随时间减小，与 $B$ 越走越远、杆的方向变化越来越慢一致。角加速度量纲为每秒平方，不能漏掉分母中的 $b^2$。


![图 6-3 核心推导的几何结构](../figures/velocity-06.png)

（3）固定点 $D$ 的几何和速度。

$OD=OB/2=b/(2\sin60^\circ)=b/\sqrt3$。记 $d=b/\sqrt3$，则当前 $\mathbf r_D=(b/(2\sqrt3),b/2)$。连杆 $DE$ 的竖向高度差为 $b/2$，由 $\beta=30^\circ$ 得 $DE=b$，水平投影为 $\sqrt3b/2$。

$D$ 的速度为

$$\mathbf v_D=d\dot\alpha(-\sin\alpha,\cos\alpha)
=\left(\frac{3v}{8},-\frac{\sqrt3v}{8}\right).$$

在 $\mathbf r_{ED}=(\sqrt3b/2,-b/2)$ 方向上，相对速度投影必须为零。令 $\mathbf v_E=(V_E,0)$，得到

$$\frac{\sqrt3b}{2}\left(V_E-\frac{3v}{8}\right)
-\frac b2\left(\frac{\sqrt3v}{8}\right)=0.$$

于是

$$\boxed{\mathbf v_E=\frac v2\hat{\mathbf x}}.$$

两端相对速度为 $(v/8,\sqrt3v/8)$，大小为 $v/4$。这还给连杆 $DE$ 的逆时针角速度 $v/(4b)$；它与杆 $OC$ 的顺时针角速度不是同一个角速度。


![图 6-4 传播、力或运动的过程](../figures/acceleration-06.png)

（4）$D$ 的加速度。

保持 $d$ 固定，对材料点坐标求两次导数：

$$a_{Dx}=-d(\cos\alpha\,\dot\alpha^2+\sin\alpha\,\ddot\alpha),$$

$$a_{Dy}=d(-\sin\alpha\,\dot\alpha^2+\cos\alpha\,\ddot\alpha).$$

代入上述数值，得到

$$\boxed{\mathbf a_D=
\left(-\frac{9\sqrt3v^2}{32b},-\frac{3v^2}{32b}\right)}.$$

水平分量向左，竖直分量向下。向心项与切向项在两个分量上组合不同，不能把 $|\ddot\alpha|d$ 当作总加速度大小，也不能忽略 $d\dot\alpha^2$。


![图 6-5 结果与独立检验](../figures/constraint-06.png)

（5）滑块 $E$ 的加速度。

取 $\mathbf a_E=(A_E,0)$，二阶长度约束给

$$(\mathbf a_E-\mathbf a_D)\cdot\mathbf r_{ED}
=-|\mathbf v_E-\mathbf v_D|^2=-\frac{v^2}{16}.$$

代入 $D$ 的加速度与连杆投影：

$$\frac{\sqrt3b}{2}\left(A_E+\frac{9\sqrt3v^2}{32b}\right)
-\frac b2\left(\frac{3v^2}{32b}\right)=-\frac{v^2}{16}.$$

因此

$$\boxed{\mathbf a_E=-\frac{7\sqrt3v^2}{24b}\hat{\mathbf x}}.$$

输出滑块此时向右运动，却向左加速，即正在减速。不能因为速度向右而把加速度方向也画成右；本题这两个方向恰好相反。

（6）坐标微分的独立路径。

固定 $d=b/\sqrt3$、$\ell=b$，用

$$x_E(\alpha)=d\cos\alpha+\sqrt{\ell^2-d^2\sin^2\alpha}$$

直接求导。也可以把 $x_B$ 作为自变量，写成

$$x_E(x_B)=\frac{dx_B}{\sqrt{x_B^2+b^2}}
+\sqrt{\ell^2-\frac{d^2b^2}{x_B^2+b^2}}.$$

在 $x_B=b/\sqrt3$ 处，$V_E=v\,dx_E/dx_B$、$A_E=v^2d^2x_E/dx_B^2$。数值差分和矢量约束应恢复 $v/2$ 与 $-7\sqrt3v^2/(24b)$。这里不能把 $d$ 写成当前 $OB/2$ 再随 $x_B$ 一同变化，因为 $D$ 是杆上的固定铰点。

（7）为什么瞬时中点不能作全程约束。

如果错误地令 $\mathbf r_D=\mathbf r_B/2$ 全程成立，会得到 $\mathbf v_D=(v/2,0)$ 和 $\mathbf a_D=0$。这与固定材料点必须绕 $O$ 作圆弧运动的事实矛盾，也会把连杆速度三角形整个改变。

本题的等距关系只用于求机构固定尺寸 $OD$，求导后必须保持该尺寸不变。判断约束是否可求导，应先分清它是“任意时刻成立的机构关系”还是“题目指定瞬间的位置数值”。这一规则同样适用于别的滑套、齿轮接触或曲柄机构题。

（8）连杆 $DE$ 的角加速度及向心项。

取 $DE$ 向右下方角为 $-\beta$，则 $y_D=\ell\sin\beta$。一次求导给 $\dot\beta=\dot y_D/(\ell\cos\beta)=-v/(4b)$，因此连杆自身角速度为 $-\dot\beta=v/(4b)$，方向逆时针。

二次求导有

$$a_{Dy}=\ell(\cos\beta\,\ddot\beta-\sin\beta\,\dot\beta^2).$$

使用 $a_{Dy}=-3v^2/(32b)$、$\ell=b$、$\beta=30^\circ$，得到 $\ddot\beta=-v^2/(8\sqrt3b^2)$。所以连杆自身的角加速度为 $\sqrt3v^2/(24b^2)$，同样逆时针。

再写 $\mathbf a_E=\mathbf a_D+\dot\omega_{DE}\hat{\mathbf z}\times\mathbf r_{ED}-\omega_{DE}^2\mathbf r_{ED}$，可恢复输出水平加速度，竖直分量严格相消。这条刚体加速度路径与长度二次约束等价，明确揭示了正文速度平方项对应的连杆向心加速度。

（9）输入速度若随时间变化。

一般输入 $x_B(t)$ 的速度为 $v$、加速度为 $a_{\rm in}$。角运动变成

$$\dot\alpha=-\frac vb\sin^2\alpha,\qquad
\ddot\alpha=-\frac{a_{\rm in}}b\sin^2\alpha
+\frac{2v^2}{b^2}\sin^3\alpha\cos\alpha.$$

输出坐标写作固定尺寸函数 $x_E=g(x_B)$，所以 $V_E=g'v$、$A_E=g'a_{\rm in}+g''v^2$。图示位置 $g'=1/2$、$g''=-7\sqrt3/(24b)$，给出

$$A_E=\frac12a_{\rm in}-\frac{7\sqrt3v^2}{24b}.$$

第一项是输入直接传递的加速度，第二项是机构几何导致的加速度。本题输入匀速只消去第一项，不消去第二项。把“输入加速度为零”理解成所有输出加速度为零，是运动学中常见的错误。

（10）套点 $B$ 的极坐标相对运动检查。

$B$ 的径向坐标为 $\rho=b/\sin\alpha$。速度分解为 $\mathbf v_B=\dot\rho\mathbf e_r+\rho\dot\alpha\mathbf e_\alpha$，其竖直分量必须为零、水平分量为 $v$。由 $\dot\rho=-b\cos\alpha\dot\alpha/\sin^2\alpha=v\cos\alpha$，可以逐项确认这一速度分解。

加速度包含径向 $\ddot\rho-\rho\dot\alpha^2$ 与切向 $\rho\ddot\alpha+2\dot\rho\dot\alpha$。后者中的系数 $2$ 是滑套径向运动与杆转动同时存在的交叉项。代入匀速输入后两个地面分量均为零，与套点直线匀速轨迹一致；漏掉交叉项就会得到虚假的非零加速度。

（11）约束和分支的几何可行性。

输出函数中平方根要求 $\ell^2-d^2\sin^2\alpha\ge0$。题图 $d=b/\sqrt3$、$\ell=b$，在整个第一象限满足该条件。取正平方根表示 $E$ 位于 $D$ 右侧；若改取负根，机构位于另一装配分支，输出速度和加速度也会改变。

因此在代数运算前应确认装配分支，不能把平方根默认选正当成纯数学惯例。固定点半径、连杆长度和滑块位置约束共同决定机构的可行运动区间。


（12）位置约束的残差如何核查。

对任一足够小的角度变化，保持 $d=b/\sqrt3$ 和 $\ell=b$，用位置函数生成 $D,E$ 坐标，距离应满足 $(x_E-x_D)^2+y_D^2=\ell^2$。然后分别求一阶和二阶残差：

$$R_v=(\mathbf v_E-\mathbf v_D)\cdot\mathbf r_{ED},$$

$$R_a=(\mathbf a_E-\mathbf a_D)\cdot\mathbf r_{ED}
+|\mathbf v_E-\mathbf v_D|^2.$$

两者应同时为零。只检查第一条不能保证加速度正确，因为不同的错误加速度仍可能配合同一组正确速度。

使用数值差分时，步长过大有截断误差，过小则受浮点相减影响。可逐次减小步长，观察二阶导数先趋近解析值，再选择稳定区间作为检查。数值方法中的这种变化不能通过修改机构固定尺寸来“补偿”，否则检查的已不是原装配位置。


## 六、关键洞察

$B$ 是滑动点、$D$ 是材料点，这是两类运动学关系的分界。瞬时中点用于定尺寸，不能用于定速度。固定长度约束的二次求导保留相对速度平方项，等价于连杆向心加速度。

矢量法给出每个分量的物理含义，坐标微分则提供独立可计算的检查路径。两者都以全程固定 $OD$ 和 $DE$ 为前提，避免把瞬时几何误当成运动约束。

## 七、易错点

忽略滑套沿杆的相对运动会错算 $OC$ 转速。把 $OD=BD$ 直接求导会把固定点误当成滑套中点。连杆加速度约束若漏掉速度平方项，会少一个法向加速度。

角速度与角加速度、滑块速度与加速度均可异号。只报大小而不画方向，容易在后续代数中制造符号错误。

## 八、课堂讲解建议

教师先用不同颜色区分滑套 $B$ 和固定铰点 $D$，板书哪些尺寸保持不变。课堂先求 $OC$ 角运动，再列 $D$ 分量与 $DE$ 的一阶、二阶约束。用坐标函数微分检查输出，不要求学生只凭加速度多边形猜方向。

## 九、变式训练

<!-- KEEP_TOGETHER_START -->

变式一：取 $b=1\,\mathrm m$、$v=2\,\mathrm{m/s}$，给出四个结果及方向。

解：$\dot\alpha=-1.5\,\mathrm{s^{-1}}$ 为顺时针；$\ddot\alpha=3\sqrt3/2\,\mathrm{s^{-2}}$ 为逆时针。滑块速度 $V_E=1\,\mathrm{m/s}$ 向右，加速度 $A_E=-7\sqrt3/6\,\mathrm{m/s^2}$ 向左。速度的一次比例与加速度的二次比例不同，把 $v$ 增大两倍时前者增两倍、后者增四倍。

代入全部向量结果还能检查连杆二阶约束。这里 $\mathbf v_D=(3/4,-\sqrt3/4)$，$\mathbf a_D=(-9\sqrt3/8,-3/8)$，两端相对速度为 $(1/4,\sqrt3/4)$，平方为 $1/4$。

将 $\mathbf a_E=(-7\sqrt3/6,0)$ 与这些量代入 $(\mathbf a_E-\mathbf a_D)\cdot\mathbf r_{ED}+|\mathbf v_E-\mathbf v_D|^2$ 得零。线加速度向左只是输出速度在当前时刻减小，并不表示滑块已经向左运动；速度和加速度的方向要各自判断。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式二：一般角度 $0<\alpha<\pi/2$ 下，求杆 $OC$ 的角速度与角加速度。

解：仍有 $x_B=b\cot\alpha$、$\dot x_B=v$，所以 $\dot\alpha=-v\sin^2\alpha/b$、$\ddot\alpha=2v^2\sin^3\alpha\cos\alpha/b^2$。在第一象限角速度为负、角加速度为正。$\alpha\to0$ 时二者趋于零，符合远处水平套点越来越难改变杆方向；$\alpha\to\pi/2$ 时角速度大小为 $v/b$，角加速度瞬时为零。

角加速度还可写成 $d\dot\alpha/d\alpha$ 乘 $\dot\alpha$。因为 $d\dot\alpha/d\alpha=-2v\sin\alpha\cos\alpha/b$，两项都为负，乘积为正，说明顺时针角速率正在减小。

套点距离 $OB=b/\sin\alpha$ 随运动变化，其变化率不能当作零；但杆上固定材料点 $D$ 的 $OD$ 必须保持恒定。一个机构同时出现这两类距离，正是用单一瞬时比例图求加速度容易出错的原因。一般角度公式由滑块轨迹得到，不需要假设D仍位于OB中点。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式三：求图示瞬间连杆 $DE$ 的角速度大小和方向。

解：两端相对速度为 $(v/8,\sqrt3v/8)$，长度为 $v/4$；$DE$ 长为 $b$，故连杆转速大小为 $v/(4b)$。从 $D$ 指向 $E$ 的方向是 $(\sqrt3/2,-1/2)$，逆时针转动速度方向为 $(1/2,\sqrt3/2)$，正好与相对速度同向，所以 $DE$ 逆时针转动。这与 $OC$ 的顺时针运动同时发生，不可把两杆转速视作相等。

叉积求角速度能同时给方向：$\Omega_{DE}=(\mathbf r_{ED}\times\mathbf v_{ED})_z/\ell^2$。本例代入得 $v/(4b)>0$。其法向相对加速度为

$$\mathbf a_{{\rm rel},n}=-\Omega_{DE}^2\mathbf r_{ED}.$$

即使DE两端都在运动，这个相对刚体关系仍成立。只比较D与E速度大小不能求杆角速度，必须取两端的向量差。OC的转动与DE的转动以D点相连，却不构成同一刚体，因而没有共同角速度。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式四：若只把机构所有长度乘 $\lambda$，保持输入速度 $v$，各输出如何缩放？

解：$b,d,\ell$ 同乘 $\lambda$，指定角度不变。角速度乘 $1/\lambda$，角加速度乘 $1/\lambda^2$；输出线速度仍为 $v/2$，线加速度乘 $1/\lambda$。固定长度函数的导数也给同样结果：$dx_E/dx_B$ 无量纲，二阶导数量纲为逆长度。这一缩放检验可快速发现角加速度分母写成 $b$ 或线加速度分母写成 $b^2$ 的错误。

时间尺度随尺寸变化也能导出同样结论。选 $t_0=b/v$，所有位置写成 $b$ 乘无量纲几何函数，则一阶时间导数比例为 $b/t_0=v$，二阶为 $b/t_0^2=v^2/b$。

尺寸放大而输入线速度固定，走过相似装配位置需要更长时间；线速度大小不变，线加速度减小。这种推理在未知具体系数时也能先确定量纲，但不能替代求 $1/2$、$7\sqrt3/24$ 等几何系数。若改为保持输入角速度，缩放规律会改变，本变式明确固定的是线速度。

<!-- KEEP_TOGETHER_END -->

<!-- question-complete -->
