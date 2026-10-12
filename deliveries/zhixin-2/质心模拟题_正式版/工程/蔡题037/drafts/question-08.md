# 第 8 题

一个半径为 $R$ 的圆盘在水平面内运动。圆盘边缘绕有三条细线，某时刻三条线的切点恰好位于圆周三等分点。三条线的自由端分别沿线方向以速度 $v_1$、$v_2$、$v_3$ 拉动，且该时刻三个自由端沿绳方向的加速度均为零。细线与圆盘之间不打滑。

（1）求此时圆心速度的大小和圆盘角速度的大小；

（2）求此时圆心加速度的大小。

![题8　圆盘边缘三个互差 $120^\circ$ 的切点与拉线速度](../figures/question-08.pdf){ width=70% }

## 一、题型定位

本题是平面刚体运动学中的“三个切向速度约束反求平动与转动”模型。圆盘在平面内只有三个瞬时速度自由度：圆心速度的两个分量和一个角速度。三条无滑动约束恰好可完全确定它们。加速度问题则要在切向投影中识别：向心加速度沿半径方向，对绳的切向长度约束没有直接贡献。

## 二、知识点

1. 平面刚体上一点的速度关系 $\boldsymbol v_P=\boldsymbol v_C+\boldsymbol\omega\times\boldsymbol r$；
2. 切点处绳与圆盘的无滑动条件；
3. 互差 $120^\circ$ 的三个单位向量的对称恒等式；
4. 非正交投影数据中的向量重建；
5. 刚体上一点的切向、向心加速度；
6. 速度和加速度约束的阶次区分。

## 三、物理图像

如图8-2，以圆心为 $C$，第 $i$ 个切点为 $P_i$。取 $\boldsymbol n_i$ 沿第 $i$ 条细线的正速度方向，三个 $\boldsymbol n_i$ 位于同一平面并互差 $120^\circ$。选定圆盘正角速度方向，使得转动在每个切点的切向速度投影都写成 $+\omega R$。

![图8-2　圆心平动、圆盘转动与三个切向约束](../figures/solution-08.pdf){ width=91% }

三条切向在平面内形成对称的“三方向标架”。它们不是两两正交的基，所以不能把三个投影平方直接相加当作速度平方；必须使用 $120^\circ$ 方向的点积关系。

## 四、解题入口

对每个切点都写一次“圆心平动的切向投影 $+$ 圆盘转动的切向速度 $=$ 绳速”。将三式相加，利用 $\boldsymbol n_1+\boldsymbol n_2+\boldsymbol n_3=\boldsymbol0$ 立即得到 $\omega$。再减去三个速度的平均值，留下纯平动投影，由对称向量标架重建 $\boldsymbol v_C$。加速度部分重复同一结构，但右端变为零。

## 五、解析

首先把几何关系写成向量恒等式。三个切向单位向量的模均为 $1$：

$$
\boldsymbol n_i\cdot\boldsymbol n_i=1
\qquad(i=1,2,3). \tag{1}
$$

两两夹角为 $120^\circ$，因而

$$
\boldsymbol n_i\cdot\boldsymbol n_j
=\cos120^\circ=-\frac12
\qquad(i\ne j). \tag{2}
$$

三向量的和为零：

$$
\boldsymbol n_1+\boldsymbol n_2+\boldsymbol n_3=\boldsymbol0. \tag{3}
$$

还可将它们的并矢和写成

$$
\sum_{i=1}^3\boldsymbol n_i\boldsymbol n_i^{\mathsf T}
=\frac32I_2. \tag{4}
$$

式（4）的意义是，对任意平面向量 $\boldsymbol q$，

$$
\sum_{i=1}^3(\boldsymbol q\cdot\boldsymbol n_i)\boldsymbol n_i
=\frac32\boldsymbol q. \tag{5}
$$

现在写切点速度。刚体上 $P_i$ 点的速度为

$$
\boldsymbol v_{P_i}
=\boldsymbol v_C+\boldsymbol\omega\times\boldsymbol r_i. \tag{6}
$$

其中

$$
|\boldsymbol r_i|=R. \tag{7}
$$

将式（6）沿绳方向 $\boldsymbol n_i$ 投影，按图8-2的正向约定，

$$
\boldsymbol v_{P_i}\cdot\boldsymbol n_i
=\boldsymbol v_C\cdot\boldsymbol n_i+\omega R. \tag{8}
$$

绳与圆盘之间不打滑，所以切点的切向速度必须等于相应绳端速度：

$$
\boldsymbol v_C\cdot\boldsymbol n_1+\omega R=v_1. \tag{9}
$$

$$
\boldsymbol v_C\cdot\boldsymbol n_2+\omega R=v_2. \tag{10}
$$

$$
\boldsymbol v_C\cdot\boldsymbol n_3+\omega R=v_3. \tag{11}
$$

将式（9）至（11）相加：

$$
\boldsymbol v_C\cdot
(\boldsymbol n_1+\boldsymbol n_2+\boldsymbol n_3)
+3\omega R=v_1+v_2+v_3. \tag{12}
$$

利用式（3），平动项正好相消：

$$
3\omega R=v_1+v_2+v_3. \tag{13}
$$

所以有符号角速度为

$$
\omega=\frac{v_1+v_2+v_3}{3R}. \tag{14}
$$

题目要求角速度大小，因而

$$
\boxed{|\omega|=\frac{|v_1+v_2+v_3|}{3R}}. \tag{15}
$$

令三个绳速的平均值为

$$
\bar v=\frac{v_1+v_2+v_3}{3}. \tag{16}
$$

由式（13），

$$
\omega R=\bar v. \tag{17}
$$

再定义去平均后的速度

$$
b_i=v_i-\bar v. \tag{18}
$$

显然

$$
b_1+b_2+b_3=0. \tag{19}
$$

用式（9）至（11）分别减去式（17），得

$$
\boldsymbol v_C\cdot\boldsymbol n_i=b_i
\qquad(i=1,2,3). \tag{20}
$$

将式（20）两边乘 $\boldsymbol n_i$ 并对 $i$ 求和：

$$
\sum_{i=1}^3
(\boldsymbol v_C\cdot\boldsymbol n_i)\boldsymbol n_i
=\sum_{i=1}^3b_i\boldsymbol n_i. \tag{21}
$$

由式（5），左边等于 $3\boldsymbol v_C/2$，因而

$$
\frac32\boldsymbol v_C
=\sum_{i=1}^3b_i\boldsymbol n_i. \tag{22}
$$

解得圆心速度向量

$$
\boxed{
\boldsymbol v_C
=\frac23\sum_{i=1}^3(v_i-\bar v)\boldsymbol n_i
}. \tag{23}
$$

为求大小，对式（23）平方：

$$
v_C^2
=\frac49\left|
b_1\boldsymbol n_1+b_2\boldsymbol n_2+b_3\boldsymbol n_3
\right|^2. \tag{24}
$$

展开点积：

$$
v_C^2
=\frac49\left[
\sum_{i=1}^3b_i^2
+2\sum_{i<j}b_ib_j(\boldsymbol n_i\cdot\boldsymbol n_j)
\right]. \tag{25}
$$

代入式（2）：

$$
v_C^2
=\frac49\left(
\sum_{i=1}^3b_i^2-\sum_{i<j}b_ib_j
\right). \tag{26}
$$

由式（19）平方，

$$
(b_1+b_2+b_3)^2=0. \tag{27}
$$

即

$$
\sum_{i=1}^3b_i^2+2\sum_{i<j}b_ib_j=0. \tag{28}
$$

所以

$$
\sum_{i<j}b_ib_j=-\frac12\sum_{i=1}^3b_i^2. \tag{29}
$$

代入式（26）：

$$
v_C^2
=\frac49\left(1+\frac12\right)\sum_{i=1}^3b_i^2. \tag{30}
$$

因而

$$
v_C^2=\frac23\sum_{i=1}^3b_i^2. \tag{31}
$$

现在把 $b_i$ 换回 $v_i$。由式（18），

$$
\sum_{i=1}^3b_i^2
=\sum_{i=1}^3(v_i-\bar v)^2. \tag{32}
$$

展开：

$$
\sum_{i=1}^3b_i^2
=\sum_{i=1}^3v_i^2-2\bar v\sum_{i=1}^3v_i+3\bar v^2. \tag{33}
$$

由 $\sum v_i=3\bar v$，

$$
\sum_{i=1}^3b_i^2
=\sum_{i=1}^3v_i^2-3\bar v^2. \tag{34}
$$

再代入 $\bar v=(v_1+v_2+v_3)/3$：

$$
\sum_{i=1}^3b_i^2
=\sum_{i=1}^3v_i^2-\frac13(v_1+v_2+v_3)^2. \tag{35}
$$

展开后合并：

$$
\sum_{i=1}^3b_i^2
=\frac23\left(
v_1^2+v_2^2+v_3^2-v_1v_2-v_2v_3-v_3v_1
\right). \tag{36}
$$

将式（36）代入式（31）：

$$
v_C^2
=\frac49\left(
v_1^2+v_2^2+v_3^2-v_1v_2-v_2v_3-v_3v_1
\right). \tag{37}
$$

所以圆心速度大小为

$$
\boxed{
v_C=\frac23\sqrt{
v_1^2+v_2^2+v_3^2-v_1v_2-v_2v_3-v_3v_1
}
}. \tag{38}
$$

根号内也可写成差的平方和：

$$
v_1^2+v_2^2+v_3^2-v_1v_2-v_2v_3-v_3v_1
=\frac12\left[(v_1-v_2)^2+(v_2-v_3)^2+(v_3-v_1)^2\right]. \tag{39}
$$

式（39）立即表明根号内恒非负，且只有当 $v_1=v_2=v_3$ 时 $v_C=0$。

下面求加速度。刚体上 $P_i$ 点的加速度为

$$
\boldsymbol a_{P_i}
=\boldsymbol a_C
+\boldsymbol\beta\times\boldsymbol r_i
+\boldsymbol\omega\times(\boldsymbol\omega\times\boldsymbol r_i), \tag{40}
$$

其中

$$
\boldsymbol\beta=\dot{\boldsymbol\omega}. \tag{41}
$$

最后一项是向心加速度，沿半径方向：

$$
\boldsymbol\omega\times(\boldsymbol\omega\times\boldsymbol r_i)
=-\omega^2\boldsymbol r_i. \tag{42}
$$

因为 $\boldsymbol n_i$ 沿切向，

$$
\boldsymbol r_i\cdot\boldsymbol n_i=0. \tag{43}
$$

所以式（42）在绳方向的投影为零：

$$
[-\omega^2\boldsymbol r_i]\cdot\boldsymbol n_i=0. \tag{44}
$$

将式（40）沿 $\boldsymbol n_i$ 投影：

$$
\boldsymbol a_{P_i}\cdot\boldsymbol n_i
=\boldsymbol a_C\cdot\boldsymbol n_i+\beta R. \tag{45}
$$

题目给出三个绳端沿绳方向的加速度都为零，无滑动约束给出

$$
\boldsymbol a_C\cdot\boldsymbol n_1+\beta R=0. \tag{46}
$$

$$
\boldsymbol a_C\cdot\boldsymbol n_2+\beta R=0. \tag{47}
$$

$$
\boldsymbol a_C\cdot\boldsymbol n_3+\beta R=0. \tag{48}
$$

将三式相加：

$$
\boldsymbol a_C\cdot
(\boldsymbol n_1+\boldsymbol n_2+\boldsymbol n_3)
+3\beta R=0. \tag{49}
$$

利用式（3）：

$$
3\beta R=0. \tag{50}
$$

因 $R\ne0$，

$$
\beta=0. \tag{51}
$$

代回式（46）至（48）：

$$
\boldsymbol a_C\cdot\boldsymbol n_1=0. \tag{52}
$$

$$
\boldsymbol a_C\cdot\boldsymbol n_2=0. \tag{53}
$$

$$
\boldsymbol a_C\cdot\boldsymbol n_3=0. \tag{54}
$$

平面内任取两个不平行的 $\boldsymbol n_i$ 就能张成整个平面。一个平面向量同时与它们都垂直，只能是零向量：

$$
\boldsymbol a_C=\boldsymbol0. \tag{55}
$$

因而圆心加速度大小为

$$
\boxed{a_C=0}. \tag{56}
$$

同时还得到了题目未直接询问的结果

$$
\boxed{\dot\omega=\beta=0}. \tag{57}
$$

做三个特殊情形检验。若三条绳等速拉动，

$$
v_1=v_2=v_3=V. \tag{58}
$$

则式（38）给出

$$
v_C=0. \tag{59}
$$

式（14）给出

$$
\omega=\frac VR. \tag{60}
$$

即对称拉动只使圆盘转动。若

$$
v_1+v_2+v_3=0, \tag{61}
$$

则

$$
\omega=0, \tag{62}
$$

此时三个投影中的平均转动成分完全消失，剩下纯平动。若只拉第一条绳，

$$
v_1=V,
\qquad v_2=v_3=0, \tag{63}
$$

则

$$
|\omega|=\frac{|V|}{3R}, \tag{64}
$$

且

$$
v_C=\frac23|V|. \tag{65}
$$

上述结果均符合量纲：$\omega$ 的量纲为速度除以长度，$v_C$ 的根号内为速度平方。

为了独立检验向量标架方法，还可以选取显式直角坐标。令第一条绳沿 $+x$ 方向，则

$$
\boldsymbol n_1=(1,0). \tag{66}
$$

其余两条绳相对它分别转过 $120^\circ$、$240^\circ$：

$$
\boldsymbol n_2=\left(-\frac12,\frac{\sqrt3}{2}\right). \tag{67}
$$

$$
\boldsymbol n_3=\left(-\frac12,-\frac{\sqrt3}{2}\right). \tag{68}
$$

设

$$
\boldsymbol v_C=(V_x,V_y). \tag{69}
$$

由式（20）的第一式，

$$
V_x=b_1. \tag{70}
$$

第二、第三个投影方程分别为

$$
-\frac12V_x+\frac{\sqrt3}{2}V_y=b_2. \tag{71}
$$

$$
-\frac12V_x-\frac{\sqrt3}{2}V_y=b_3. \tag{72}
$$

式（71）减式（72）：

$$
\sqrt3V_y=b_2-b_3. \tag{73}
$$

因而

$$
V_y=\frac{b_2-b_3}{\sqrt3}. \tag{74}
$$

这样圆心速度平方为

$$
v_C^2=b_1^2+\frac{(b_2-b_3)^2}{3}. \tag{75}
$$

由 $b_1+b_2+b_3=0$，可写 $b_1=-(b_2+b_3)$。代入式（75）：

$$
\begin{aligned}
v_C^2
&=(b_2+b_3)^2+\frac{(b_2-b_3)^2}{3}\\
&=\frac43(b_2^2+b_2b_3+b_3^2).
\end{aligned} \tag{76}
$$

另一方面，

$$
\begin{aligned}
\frac23(b_1^2+b_2^2+b_3^2)
&=\frac23[(b_2+b_3)^2+b_2^2+b_3^2]\\
&=\frac43(b_2^2+b_2b_3+b_3^2).
\end{aligned} \tag{77}
$$

式（76）与式（77）完全一致，因而显式坐标法独立验证了式（31）和最终结果式（38）。这一检查也说明，如果不熟悉并矢恒等式（4），仍然可以从两个直角分量稳妥求解，但必须保留三条绳方向的 $120^\circ$ 几何关系。

## 六、关键洞察

三绳速率的平均值给出转动，减去平均值后的三个投影给出圆心平动。切向加速度约束也可按相同方式求解，圆周材料点的向心加速度则须另行保留。

## 七、易错点

1. 忘记圆心也在运动，直接写 $v_i=\omega R$。
2. 将三个 $120^\circ$ 方向当作正交坐标轴，错把 $b_1^2+b_2^2+b_3^2$ 当成 $v_C^2$。
3. 求得有符号的 $\omega$ 后没有按题意对角速度大小取绝对值。
4. 在加速度投影中把 $\omega^2R$ 误加到切向；该项沿半径，与绳方向垂直。
5. 只由三式之和得到 $\beta=0$，却没有将它代回任意两个独立方向证明 $\boldsymbol a_C=0$。
6. 在速度约束中三次使用不一致的绳方向正向，导致某一个 $\omega R$ 符号突然反转。

## 八、课堂讲解建议

先不做代数，让学生数刚体的瞬时自由度，说明三条切向约束为何恰好足够。然后把式（9）至（11）相加，先得到最直观的角速度。对圆心速度，可先用 $\bar v$ 和 $b_i$ 说清“平均决定转动，差异决定平动”，再展开式（24）至（38）。加速度部分应在图8-2上画出向心项与切线垂直，避免学生只凭公式记忆“它为什么消失”。

## 九、变式训练

变式一：若三个绳端沿绳方向的加速度分别为 $a_1$、$a_2$、$a_3$，求圆盘角加速度和圆心加速度。

将式（46）至（48）的右端改为 $a_i$：

$$
\boldsymbol a_C\cdot\boldsymbol n_i+\beta R=a_i. \tag{78}
$$

定义平均加速度

$$
\bar a=\frac{a_1+a_2+a_3}{3}. \tag{79}
$$

三式相加得

$$
3\beta R=a_1+a_2+a_3. \tag{80}
$$

因而

$$
\boxed{\beta=\frac{a_1+a_2+a_3}{3R}=\frac{\bar a}{R}}. \tag{81}
$$

令

$$
c_i=a_i-\bar a. \tag{82}
$$

则

$$
c_1+c_2+c_3=0. \tag{83}
$$

减去 $\beta R=\bar a$ 后，

$$
\boldsymbol a_C\cdot\boldsymbol n_i=c_i. \tag{84}
$$

完全模仿式（21）至（23）的向量重建：

$$
\boxed{
\boldsymbol a_C
=\frac23\sum_{i=1}^3(a_i-\bar a)\boldsymbol n_i
}. \tag{85}
$$

其大小为

$$
\boxed{
a_C=\frac23\sqrt{
a_1^2+a_2^2+a_3^2-a_1a_2-a_2a_3-a_3a_1
}
}. \tag{86}
$$

当 $a_1=a_2=a_3=0$ 时，式（69）和式（74）立即回到本题的 $\beta=0$、$a_C=0$。

变式二：取 $R=1\,\mathrm m$，三条绳的有符号速率为 $(v_1,v_2,v_3)=(3,0,0)\,\mathrm{m/s}$，第一绳方向为 $+x$。求圆心速度与角速度。

解：三个方向取 $\boldsymbol n_1=(1,0)$、$\boldsymbol n_2=(-1/2,\sqrt3/2)$、$\boldsymbol n_3=(-1/2,-\sqrt3/2)$。速率平均值为 $1\,\mathrm{m/s}$，因此

$$
\omega=1\,\mathrm{rad/s},\qquad \boldsymbol v_C=\frac23\sum v_i\boldsymbol n_i=(2,0)\,\mathrm{m/s}.
$$

按图中约定角速度为顺时针。回代第二、三绳约束均为 $-1+1=0$；绳速为零并不表示对应圆盘材料点的完整速度向量为零。

变式三：三绳同向有符号速率都为 $v>0$，且沿绳加速度均为零。求圆盘运动，并判断圆周材料点的加速度是否为零。

解：$\sum\boldsymbol n_i=0$，所以 $\boldsymbol v_C=(2v/3)\sum\boldsymbol n_i=0$，$\omega=v/R$。切向加速度约束给 $\boldsymbol a_C=0$、$\dot\omega=0$，故圆盘瞬时作匀速纯转动。然而材料点仍有向心加速度：

$$
\boldsymbol a_P=-\omega^2\boldsymbol r_P,\qquad |\boldsymbol a_P|=\frac{v^2}{R}.
$$

切向加速度为零与总加速度为零不同。投影时向心项被消去，不能据此在向量式中删除它。

变式四：三绳沿瞬时切向的加速度改为 $(a_1,a_2,a_3)=(2a,-a,-a)$。第一绳取 $+x$，在切向无滑动加速度模型下求圆心加速度和角加速度。

解：将速度约束换为 $\boldsymbol a_C\cdot\boldsymbol n_i+\beta R=a_i$，相加得 $\beta R=(a_1+a_2+a_3)/3=0$。再按三方向重建平动，有

$$
\boldsymbol a_C=\frac23\sum a_i\boldsymbol n_i=2a\hat x,\qquad \beta=0.
$$

回代三个投影依次为 $2a,-a,-a$。圆心有加速度但角速度此刻不变；若还要求绳方向随时间变化，应先写完整的绳长几何关系，不能把瞬时投影式不加条件地外推到一段运动。
