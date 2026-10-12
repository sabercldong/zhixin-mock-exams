# 第2题

<!-- question-start -->

计算下列电流分布在原点附近的磁场，并求磁感线方程。空间取右手直角坐标系，导线均无限长、平行于 $z$ 轴，各导线中的电流大小均为 $I$。导线横截面的布置如图2-1所示。

（1）两根导线分别通过 $xy$ 平面上的 $(+\ell,0)$、$(-\ell,0)$，电流方向分别为 $+z$、$-z$。求 $|x|,|y|\ll\ell$ 的原点附近磁场大小，并写出任意一条磁感线的方程。

（2）四根导线分别通过 $(+\ell,+\ell)$、$(-\ell,+\ell)$、$(-\ell,-\ell)$、$(+\ell,-\ell)$。第一、第三象限的导线中电流沿 $+z$ 方向，第二、第四象限的导线中电流沿 $-z$ 方向。求 $|x|,|y|\ll\ell$ 的原点附近磁场大小，并写出任意一条磁感线的方程。

![图2-1 两导线与四导线的横截面位置及电流方向。](../figures/question-02.png){width=82%}

<!-- question-end -->

## 一、题型定位

这是长直电流磁场的矢量叠加与磁感线微分方程问题。两问的几何布置不同，中心的抵消方式也不同：两根反向电流在两导线之间产生同向磁场，原点的场不为零；四根交替电流在原点恰好抵消，必须再计算离开原点后的一阶变化，才能得到附近的磁场。

“原点附近”限定了结果的精度与范围。两导线的局部主阶是均匀场，四导线的局部主阶是随位置线性变化的场。它们对应的近似磁感线分别是直线和矩形双曲线。若保留位置的全部依赖，两导线的磁感线是圆族加一条中轴直线；四导线的精确磁感线一般是四次曲线。局部近似与精确关系要分开写，不能把一条近似双曲线延伸到导线附近仍当作精确结果。

## 二、知识点

毕奥—萨伐尔定律；无限长直导线的磁场；右手定则；笛卡尔坐标中的矢量分解；带符号分量的线性叠加；分式通分与平方恒等式；多变量函数在原点的展开；对称性与低阶抵消；磁感线的切线条件；微分形式、积分因子和分离变量；对数积分的绝对值；微分方程除法造成的遗漏解；磁零点与分界磁感线；量纲和特殊位置检验。

按理想长直电流模型处理，介质磁导率取 $\mu_0$。$\ell>0$ 表示截面坐标中的长度，不是导线长度。导线自身的位置是磁场公式的奇点，下面的方程都在导线外使用。电流沿 $+z$ 用 $\odot$ 表示，沿 $-z$ 用 $\otimes$ 表示；这两个符号表示垂直截面的电流方向，不是截面中磁场的方向。

## 三、物理图像

四根导线在空间中始终平行，不在 $xy$ 平面内连成正方形回路。图2-1的虚线正方形仅用于表示截面位置关系。图2-2把实际空间导线和一个横截面画在一起，四条竖直方向的电流线分别对应图2-1中的四个编号。

![图2-2 平行空间导线及其与横截面的交点。](../figures/space-02.png){width=60%}

无限长导线沿 $z$ 方向平移后，其电流分布不变。因此磁场不依赖观察点的 $z$ 坐标；每根导线的场都在垂直导线的平面内，所以总场也有 $B_z=0$。后面求磁感线只需研究 $xy$ 截面，各个平行截面具有相同的图形。

两导线时，原点在右侧正电流的左边，该电流的场朝 $-y$；原点在左侧负电流的右边，该电流的场也朝 $-y$。这说明原点的两个场相加而不是抵消。四导线时，原点位于四角的中心，四个场矢量成对抵消；但是沿 $x$ 方向略移，向外的水平分量逐渐显现，沿 $y$ 方向略移，指向中心的竖直分量逐渐显现。这正是双曲线型场的几何图像。

## 四、解题入口

先把一根任意位置的直导线写成统一公式：导线的截面坐标为 $(a,b)$，电流符号为 $s=\pm1$，观察点为 $P(x,y)$。用这个公式逐根代入，可以在同一套符号规则下计算两问，避免临时选夹角造成投影正负号混乱。

两导线先求精确分量，再取原点附近的主阶；保留精确式还可以继续积分，解释圆族和直线近似的关系。四导线先检查原点的零阶场，再逐根求一阶导数并相加。磁感线方程来自曲线切线与总磁场平行，而不是来自“单根导线磁感线为圆”这一事实。

## 五、解析

**第1步：从一根导线建立带方向的磁场公式。**

令

$$
K=\frac{\mu_0 I}{2\pi},\qquad
d_x=x-a,\qquad d_y=y-b,\qquad
\rho^2=d_x^2+d_y^2.
$$

$K$ 为正，电流方向由 $s$ 单独表示。导线上一个源点取 $(a,b,z')$，电流线元为 $s\,\mathrm dz'\,\boldsymbol e_z$。观察点取 $(x,y,0)$，从源点指向观察点的矢量为

$$
\boldsymbol R=d_x\boldsymbol e_x+d_y\boldsymbol e_y-z'\boldsymbol e_z.
$$

用右手坐标的叉乘规则 $\boldsymbol e_z\times\boldsymbol e_x=\boldsymbol e_y$、$\boldsymbol e_z\times\boldsymbol e_y=-\boldsymbol e_x$，得到

$$
\begin{aligned}
s\,\mathrm dz'\,\boldsymbol e_z\times\boldsymbol R
&=s(-d_y\boldsymbol e_x+d_x\boldsymbol e_y)\,\mathrm dz',\\
\boldsymbol B
&=\frac{\mu_0 I s}{4\pi}
(-d_y\boldsymbol e_x+d_x\boldsymbol e_y)
\int_{-\infty}^{+\infty}
\frac{\mathrm dz'}{(\rho^2+z'^2)^{3/2}}.
\end{aligned}
$$

积分上下限来自无限长导线。积分中的 $\rho$ 对源坐标 $z'$ 是常量，不能在积分过程中把它当作沿导线变化的距离。作代换 $z'=\rho\tan\theta$，则

$$
\begin{aligned}
\mathrm dz'&=\rho\sec^2\theta\,\mathrm d\theta,\\
(\rho^2+z'^2)^{3/2}&=\rho^3\sec^3\theta,\\
\int_{-\infty}^{+\infty}
\frac{\mathrm dz'}{(\rho^2+z'^2)^{3/2}}
&=\frac1{\rho^2}\int_{-\pi/2}^{+\pi/2}\cos\theta\,\mathrm d\theta\\
&=\frac1{\rho^2}
\left[\sin\theta\right]_{-\pi/2}^{+\pi/2}
=\frac2{\rho^2}.
\end{aligned}
$$

这里使用三角代换计算广义积分；在 $-\pi/2<\theta<\pi/2$ 中 $\sec\theta>0$，没有额外绝对值符号。代回并整理系数：

$$
\boxed{
\boldsymbol B(a,b;s)
=\frac{Ks}{(x-a)^2+(y-b)^2}
\left[-(y-b)\boldsymbol e_x+(x-a)\boldsymbol e_y\right].
}
$$

向量 $(-d_y,d_x)$ 与径向向量 $(d_x,d_y)$ 垂直，长度为 $\rho$，所以场强大小为 $K/\rho$。这同时核对了方向、距离幂次和长直导线的标准场强式。$s=-1$ 会反转整个矢量，而不仅反转某一个分量。

**第2步：写出两导线到观察点的距离，并逐项叠加。**

右导线记为“$+$”，在 $(\ell,0)$，$s=+1$；左导线记为“$-$”，在 $(-\ell,0)$，$s=-1$。图2-3中的 $r_+$、$r_-$ 是从这两根导线到 $P$ 的距离。每根磁场与其对应径向线垂直，右图表示同一点的场矢量首尾相接，不能把两条距离线直接当成两个磁场方向。

![图2-3 观察点到两导线的距离与磁场矢量叠加。](../figures/vectors-02.png){width=76%}

按图2-3的符号，

$$
\begin{aligned}
r_+^2&=(x-\ell)^2+y^2,\\
r_-^2&=(x+\ell)^2+y^2,\\
\boldsymbol B_+
&=\frac K{r_+^2}(-y,\ x-\ell),\\
\boldsymbol B_-
&=\frac K{r_-^2}(y,\ -x-\ell).
\end{aligned}
$$

后一行的两个符号均由负电流反转而来。总场分量为

$$
B_x=K\left(-\frac y{r_+^2}+\frac y{r_-^2}\right),
\qquad
B_y=K\left(\frac{x-\ell}{r_+^2}
-\frac{x+\ell}{r_-^2}\right).
$$

场强不能写成 $K/r_++K/r_-$，因为在一般 $P$ 处两个场并不平行。只有在两导线之间的 $x$ 轴上，它们才同向。

<!-- KEEP_TOGETHER_START -->

**第3步：展开通分的分子，保留每一个负号。**

定义公共分母 $\Delta=r_+^2r_-^2>0$。先算水平分量：

$$
\begin{aligned}
B_x
&=Ky\frac{r_+^2-r_-^2}{\Delta},\\
r_+^2-r_-^2
&=(x-\ell)^2-(x+\ell)^2\\
&=(x^2-2\ell x+\ell^2)
-(x^2+2\ell x+\ell^2)=-4\ell x,\\
\therefore\quad B_x&=-\frac{4K\ell xy}{\Delta}.
\end{aligned}
$$

<!-- KEEP_TOGETHER_END -->

再算竖直分量。令 $A=x^2+y^2+\ell^2$，则 $r_-^2=A+2\ell x$、$r_+^2=A-2\ell x$，有

$$
\begin{aligned}
B_y&=K\frac{(x-\ell)r_-^2-(x+\ell)r_+^2}{\Delta},\\
(x-\ell)r_-^2-(x+\ell)r_+^2
&=(x-\ell)(A+2\ell x)-(x+\ell)(A-2\ell x)\\
&=-2\ell A+4\ell x^2\\
&=2\ell(x^2-y^2-\ell^2).
\end{aligned}
$$

于是两导线的精确场为

$$
\boxed{
B_x=-\frac{4K\ell xy}{\Delta},\qquad
B_y=\frac{2K\ell(x^2-y^2-\ell^2)}{\Delta}.
}
$$

立即代入 $x=y=0$：

$$
B_x(0,0)=0,\qquad
B_y(0,0)=-\frac{2K}{\ell}
=-\frac{\mu_0 I}{\pi\ell}.
$$

竖直分量为负，与第3模块的右手定则检验一致。若把它算成正数，后续磁感线的几何形状可能仍正确，但所有有向箭头会反转；这不是可以忽略的符号差异。

**第4步：由分量求精确场强，不把矢量相加误写成大小相加。**

平方后提取公共因子：

$$
B^2=B_x^2+B_y^2
=\frac{4K^2\ell^2}{\Delta^2}
\left[4x^2y^2+(x^2-y^2-\ell^2)^2\right].
$$

括号中的表达式可以利用平方差整理。把每一步展开：

$$
\begin{aligned}
4x^2y^2+(x^2-y^2-\ell^2)^2
&=x^4+y^4+\ell^4+2x^2y^2
-2\ell^2x^2+2\ell^2y^2,\\
\Delta
&=(A-2\ell x)(A+2\ell x)\\
&=A^2-4\ell^2x^2\\
&=x^4+y^4+\ell^4+2x^2y^2
-2\ell^2x^2+2\ell^2y^2.
\end{aligned}
$$

两式相同，所以

$$
\begin{aligned}
B^2&=\frac{4K^2\ell^2}{\Delta},\\
B&=\frac{2K\ell}{\sqrt{\Delta}}
=\frac{2K\ell}{r_+r_-}
=\frac{\mu_0 I\ell}{\pi r_+r_-}.
\end{aligned}
$$

此处取正平方根，因为 $B$ 表示大小，$K,\ell,r_+,r_-$ 都为正。分量 $B_y$ 可为负，场强大小 $B$ 却不能为负。公式只排除两根导线本身，不要求观察点一定在它们之间。

**第5步：按照题设取原点附近的主阶，并说明舍弃了什么。**

令 $r=\sqrt{x^2+y^2}$。当 $r/\ell\ll1$ 时，

$$
\begin{aligned}
\Delta
&=\ell^4+2\ell^2(y^2-x^2)+(x^2+y^2)^2,\\
\frac1\Delta
&=\frac1{\ell^4}
\left[1+\frac{2(x^2-y^2)}{\ell^2}
+O\!\left(\frac{r^4}{\ell^4}\right)\right].
\end{aligned}
$$

这里使用 $1/(1+\varepsilon)=1-\varepsilon+O(\varepsilon^2)$，其中 $\varepsilon$ 的最低阶是 $r^2/\ell^2$。代入精确分量，逐项保留至二阶：

$$
\begin{aligned}
B_x
&=-\frac{4Kxy}{\ell^3}
+O\!\left(\frac{Kr^4}{\ell^5}\right),\\
B_y
&=-\frac{2K}{\ell}
\left[1+\frac{x^2-y^2}{\ell^2}
+O\!\left(\frac{r^4}{\ell^4}\right)\right].
\end{aligned}
$$

两式没有一阶项。水平分量的最低非零项是二阶，竖直分量包含一个非零常数。因此题设所需的最低主阶结果为

$$
\boxed{\boldsymbol B\simeq-\frac{\mu_0 I}{\pi\ell}\boldsymbol e_y,
\qquad B\simeq\frac{\mu_0 I}{\pi\ell}.}
$$

它是局部均匀场，磁感线在这一主阶内满足

$$
\boxed{x=C_1,\qquad \text{方向沿 }-y.}
$$

磁感线写成 $x=C_1$ 比 $y=f(x)$ 更合适，因为竖直线不能作为单值函数 $y(x)$。场强的下一阶修正是

$$
B=\frac{2K}{\ell}
\left[1+\frac{x^2-y^2}{\ell^2}
+O\!\left(\frac{r^4}{\ell^4}\right)\right].
$$

在 $y=0$ 轴上，略向任一导线靠近，场强增大；在 $x=0$ 轴上，离开两导线连线，场强减小。这是展开式符号的一次物理检查，不是另加一个近似条件。

<!-- KEEP_TOGETHER_START -->

**第6步：保留精确场，用切线条件建立磁感线微分方程。**

磁感线是一条处处与总磁场平行的曲线。若以参数 $u$ 表示它，满足

$$
\frac{\mathrm dx}{\mathrm du}=\lambda(u)B_x,\qquad
\frac{\mathrm dy}{\mathrm du}=\lambda(u)B_y,
$$

<!-- KEEP_TOGETHER_END -->

其中 $\lambda$ 只影响沿曲线的参数速度。消去 $\lambda$ 得

$$
B_y\,\mathrm dx-B_x\,\mathrm dy=0.
$$

这个微分形式比直接写 $\mathrm dy/\mathrm dx=B_y/B_x$ 更稳妥：在 $B_x=0$ 而 $B_y\ne0$ 时仍能描述竖直切线。把第3步的分量代入，并约去非零公共因子 $2K\ell/\Delta$：

$$
\boxed{(x^2-y^2-\ell^2)\,\mathrm dx+2xy\,\mathrm dy=0.}
$$

这里磁场大小中的 $I$ 和 $\mu_0$ 消失，是因为改变全部电流的共同倍数只改变场强，不改变磁感线形状。

**第7步：展示积分因子的来历，积分后配方。**

在 $x\ne0$ 的区域，观察微分方程中的项，可以试写

$$
F(x,y)=\frac{x^2+y^2+\ell^2}{x}
=x+\frac{y^2+\ell^2}{x}.
$$

对 $x$、$y$ 分别求偏导，再形成全微分：

$$
\begin{aligned}
\frac{\partial F}{\partial x}
&=1-\frac{y^2+\ell^2}{x^2}
=\frac{x^2-y^2-\ell^2}{x^2},\\
\frac{\partial F}{\partial y}&=\frac{2y}{x},\\
\mathrm dF
&=\frac1{x^2}
\left[(x^2-y^2-\ell^2)\,\mathrm dx+2xy\,\mathrm dy\right].
\end{aligned}
$$

因此 $1/x^2$ 正是把原方程变成全微分的积分因子。沿磁感线 $\mathrm dF=0$，积分得到 $F=2x_c$，即

$$
\begin{aligned}
x^2+y^2+\ell^2&=2x_cx,\\
x^2-2x_cx+x_c^2+y^2&=x_c^2-\ell^2,\\
(x-x_c)^2+y^2&=x_c^2-\ell^2.
\end{aligned}
$$

$\boxed{(x-x_c)^2+y^2=x_c^2-\ell^2}$ 是精确圆族的方程。

<!-- KEEP_TOGETHER_START -->

$x_c$ 的量纲为长度，它是沿场线不变的圆心横坐标。实圆须 $x_c^2>\ell^2$，即 $|x_c|>\ell$；半径为

$$
R=\sqrt{x_c^2-\ell^2}.
$$

<!-- KEEP_TOGETHER_END -->

当 $x_c=\ell$ 或 $x_c=-\ell$ 时，公式只剩导线所在的点。那里的磁场奇异，不能把它当成一条“半径为零的磁感线”。

**第8步：补回除法遗漏的中轴，并解释圆族的方向与局部直线。**

第7步除以 $x^2$，所以必须回到原场检查 $x=0$。直接代入两导线场：

$$
B_x(0,y)=0,\qquad
B_y(0,y)=-\frac{2K\ell}{\ell^2+y^2}<0.
$$

所以

$$
\boxed{x=0}
$$

是一条精确的、沿 $-y$ 的直线磁感线。它不能从有限的圆心参数中直接得到。完整的精确图像是左右两族圆加中轴直线，如图2-4；图中 $R$ 与 $x_c$ 正好满足第7步的半径关系。

![图2-4 两导线的精确圆形磁感线与中轴直线。](../figures/circles-02.png){width=68%}

对于右侧圆，$x_c>\ell$，令 $a=x_c-\ell>0$，则

$$
R^2=(\ell+a)^2-\ell^2=a^2+2a\ell=a(a+2\ell).
$$

这是右侧圆族的另一种参数写法；左侧同样取圆心 $x_c<-\ell$，不能只保留右侧。任何右侧有限圆都不经过右导线，因为把 $(\ell,0)$ 代入圆方程会要求 $x_c=\ell$，与非退化条件矛盾。左侧情形相同。

在右侧圆的最左点 $x=x_c-R$ 有 $0<x<\ell$，场朝下，圆上的方向为逆时针；左侧圆的最右点满足 $-\ell<x<0$，场也朝下，其方向为顺时针。圆的局部弧段在很小的中心窗口中近似竖直，这与第5步的 $x=C_1$ 一致，而不是两个彼此矛盾的答案。

<!-- KEEP_TOGETHER_START -->

**第9步：四导线逐根编号，先验证中心场为零。**

按照图2-1和图2-2的编号，

$$
\begin{aligned}
(a_1,b_1;s_1)&=(\ell,\ell;+1),\\
(a_2,b_2;s_2)&=(-\ell,\ell;-1),\\
(a_3,b_3;s_3)&=(-\ell,-\ell;+1),\\
(a_4,b_4;s_4)&=(\ell,-\ell;-1).
\end{aligned}
$$

<!-- KEEP_TOGETHER_END -->

分别记 $r_i^2=(x-a_i)^2+(y-b_i)^2$。直接套用第1步，四根导线的精确分量是

$$
\begin{aligned}
B_x&=K\left[-\frac{y-\ell}{r_1^2}
+\frac{y-\ell}{r_2^2}
-\frac{y+\ell}{r_3^2}
+\frac{y+\ell}{r_4^2}\right],\\
B_y&=K\left[\frac{x-\ell}{r_1^2}
-\frac{x+\ell}{r_2^2}
+\frac{x+\ell}{r_3^2}
-\frac{x-\ell}{r_4^2}\right].
\end{aligned}
$$

分量的叠加始终是 $B_x=\sum_iB_{ix}$、$B_y=\sum_iB_{iy}$。在 $P=O$ 时，每根距离都是 $\sqrt2\ell$，代入上式的单根场得到

$$
\begin{aligned}
\boldsymbol B_1(O)&=\frac K{2\ell}(1,-1),&
\boldsymbol B_2(O)&=\frac K{2\ell}(-1,-1),\\
\boldsymbol B_3(O)&=\frac K{2\ell}(-1,1),&
\boldsymbol B_4(O)&=\frac K{2\ell}(1,1).
\end{aligned}
$$

四个水平分量之和为零，四个竖直分量之和也为零。因此

$$
\boldsymbol B(O)=0.
$$

这只说明一个点的场为零，不说明原点附近整片区域没有磁场。题设要求“附近”，所以下一步必须保留场对位移的一阶变化。

**第10步：逐根求导，写清一阶展开的系数。**

对任意单导线，仍用 $d_x=x-a$、$d_y=y-b$、$r_i^2=d_x^2+d_y^2$。水平分量为 $-Ks\,d_y/r_i^2$。对 $x$ 求导时，$d_y$ 为常量：

$$
\begin{aligned}
\frac{\partial B_{ix}}{\partial x}
&=-Ks\,d_y\frac{\partial}{\partial x}(r_i^{-2})\\
&=-Ks\,d_y\left(-\frac{2d_x}{r_i^4}\right)
=\frac{2Ks\,d_xd_y}{r_i^4}.
\end{aligned}
$$

对 $y$ 求导时，分子与分母都变化，必须使用乘积或商的求导规则：

$$
\begin{aligned}
\frac{\partial B_{ix}}{\partial y}
&=-Ks\left(\frac1{r_i^2}-\frac{2d_y^2}{r_i^4}\right)\\
&=\frac{Ks(d_y^2-d_x^2)}{r_i^4}.
\end{aligned}
$$

同理从 $B_{iy}=Ks\,d_x/r_i^2$ 得

$$
\begin{aligned}
\frac{\partial B_{iy}}{\partial x}
&=\frac{Ks(d_y^2-d_x^2)}{r_i^4},\\
\frac{\partial B_{iy}}{\partial y}
&=-\frac{2Ks\,d_xd_y}{r_i^4}.
\end{aligned}
$$

在原点，$d_x=-a_i$、$d_y=-b_i$、$r_i^4=4\ell^4$，而 $a_i^2=b_i^2=\ell^2$。所以两项交叉导数都为零：

$$
\left.\frac{\partial B_{ix}}{\partial y}\right|_O
=\left.\frac{\partial B_{iy}}{\partial x}\right|_O=0.
$$

各导线的 $s_ia_ib_i$ 都等于 $\ell^2$。例如第二根有 $s_2=-1$、$a_2b_2=-\ell^2$，乘积仍为正；不能因负电流而把这一项也判成负值。于是每根都有

$$
\left.\frac{\partial B_{ix}}{\partial x}\right|_O
=\frac{2Ks_ia_ib_i}{4\ell^4}
=\frac K{2\ell^2},
\qquad
\left.\frac{\partial B_{iy}}{\partial y}\right|_O
=-\frac K{2\ell^2}.
$$

四根相加：

$$
\begin{aligned}
\left.\frac{\partial B_x}{\partial x}\right|_O
&=\frac{2K}{\ell^2},&
\left.\frac{\partial B_x}{\partial y}\right|_O&=0,\\
\left.\frac{\partial B_y}{\partial x}\right|_O
&=0,&
\left.\frac{\partial B_y}{\partial y}\right|_O&=-\frac{2K}{\ell^2}.
\end{aligned}
$$

现在使用原点的一阶泰勒展开，把零阶场与四个导数分别代入：

$$
\begin{aligned}
B_x(x,y)&\simeq B_x(O)
+\left.\frac{\partial B_x}{\partial x}\right|_O x
+\left.\frac{\partial B_x}{\partial y}\right|_O y
=\frac{2K}{\ell^2}x,\\
B_y(x,y)&\simeq B_y(O)
+\left.\frac{\partial B_y}{\partial x}\right|_O x
+\left.\frac{\partial B_y}{\partial y}\right|_O y
=-\frac{2K}{\ell^2}y.
\end{aligned}
$$

引入正的梯度系数

$$
q=\frac{2K}{\ell^2}=\frac{\mu_0 I}{\pi\ell^2},
$$

第（2）问的场矢量和场强大小就是

$$
\boxed{\boldsymbol B\simeq q(x\boldsymbol e_x-y\boldsymbol e_y),
\qquad B\simeq q\sqrt{x^2+y^2}.}
$$

$q$ 的量纲为磁场除以长度，乘以位置才是磁场。在原点 $B=0$，离开原点一个小距离，主阶场强与距离成正比；这与两导线的非零常数场有本质区别。

<!-- KEEP_TOGETHER_START -->

**第11步：由线性场求双曲线，单独处理坐标轴和磁零点。**

图2-5只画原点附近的局部窗口，远处四根导线没有被画入这个窗口。图中正 $x$ 半轴的箭头向外，正 $y$ 半轴的箭头向内，正是 $B_x=qx$、$B_y=-qy$ 的符号；下列方程实际使用这两个分量。

<!-- KEEP_TOGETHER_END -->

![图2-5 线性近似场的局部双曲线及轴线分界。](../figures/quadrupole-02.png){width=52%}

当 $x\ne0$、$y\ne0$ 时，

$$
\begin{aligned}
\frac{\mathrm dy}{\mathrm dx}
&=\frac{B_y}{B_x}=-\frac yx,\\
\frac{\mathrm dy}{y}&=-\frac{\mathrm dx}{x},\\
\ln\frac{|y|}{\ell}&=-\ln\frac{|x|}{\ell}+C,\\
\ln\frac{|xy|}{\ell^2}&=C,\\
|xy|&=\ell^2\mathrm e^C.
\end{aligned}
$$

这里使用分离变量法。对数的真数应为无量纲比值，所以用 $\ell$ 作长度基准；它只改变积分常量，不改变微分方程。$x,y$ 在不穿过坐标轴的连续弧段内符号固定，把正负号及 $\ell^2\mathrm e^C$ 吸收到新的积分常量 $C_2$，得

$$
\boxed{xy=C_2.}
$$

$C_2$ 的量纲是长度平方。$C_2>0$ 对应第一、第三象限的两支，$C_2<0$ 对应第二、第四象限的两支。一条实际有向磁感线取其中的一支，而不是把两个互不相连的支合成一条。

分离变量时除以了 $xy$，需补查坐标轴。$y=0$ 上 $B_y=0$，所以非零的 $x$ 轴部分也是场线；$x=0$ 上 $B_x=0$，所以非零的 $y$ 轴部分也是场线。它们是 $C_2=0$ 的分界支。原点本身 $\boldsymbol B=0$，没有由磁场给出的唯一切线方向，不能说一条普通磁感线“穿过原点后任选方向”。

为进一步确认图中的方向，可在主阶场中取参数 $\sigma$，写

$$
\frac{\mathrm dx}{\mathrm d\sigma}=qx,\qquad
\frac{\mathrm dy}{\mathrm d\sigma}=-qy.
$$

$\sigma$ 是描绘曲线的参数，不是带电粒子的实际时间；可取其量纲为长度除以磁场，使 $q\sigma$ 无量纲。积分得到 $x=x_0\mathrm e^{q\sigma}$、$y=y_0\mathrm e^{-q\sigma}$。沿场方向描绘，$|x|$ 增大、$|y|$ 减小，且乘积不变。这也说明在轴上接近磁零点的过程只是在参数趋于无穷时逼近它，不需要把四条半轴在零点强行连接。

**第12步：给出两问的精度范围与交叉检查。**

第（1）问按题设主阶回答：

$$
B\simeq\frac{\mu_0 I}{\pi\ell},\qquad
\boldsymbol B\parallel-\boldsymbol e_y,\qquad x=C_1.
$$

若要求精确场线，则用第7、8步的圆族与中轴：

$$
(x-x_c)^2+y^2=x_c^2-\ell^2,\quad |x_c|>\ell,
\qquad \text{以及 }x=0.
$$

第（2）问按题设主阶回答：

$$
B\simeq\frac{\mu_0 I}{\pi\ell^2}\sqrt{x^2+y^2},
\qquad xy=C_2,
$$

并保留坐标轴非零部分以及原点磁零点的说明。这些双曲线是局部主阶，不是四导线全空间的精确场线。

量纲检查：$K$ 的量纲为磁场乘长度，第（1）问的 $K/\ell$ 是磁场，第（2）问的 $(K/\ell^2)r$ 也是磁场。电流 $I$ 增大一倍，两问场强都增大一倍，但磁感线的形状不变。全部电流同时反向，两问的场强大小不变，场线箭头全部反转。

在四导线的无电流中心区域，线性场满足

$$
\frac{\partial B_x}{\partial x}
+\frac{\partial B_y}{\partial y}=q-q=0,\qquad
\frac{\partial B_y}{\partial x}
-\frac{\partial B_x}{\partial y}=0-0=0.
$$

前者是磁场无散度的检查，后者是该截面无局部电流的检查。两式说明水平向外与竖直向内的梯度必须成相反号，不能写成 $q(x,y)$。此外，四根导线的场是矢量之和，不是各自磁感线之和；把它们分成两对计算时，仍须先叠加两对场，再对总场建立切线方程。

## 六、关键洞察

**中心的零阶是否抵消，决定第一步要算到哪一阶。**

两导线在原点叠加成非零场，保留零阶就已回答主阶问题。四导线在原点抵消，只算中心值会遗漏整个问题；必须算场的空间梯度。一般地，多源场在对称点附近的结构，由最低没有被对称性抵消的展开项决定。“距离都相等”只能帮助计算每一项的大小，不能决定它们的方向，也不能替代矢量求和。

**磁感线的第一积分可以由一个标量函数直接读出。**

取只有 $z$ 分量的矢势 $\boldsymbol A=A_z(x,y)\boldsymbol e_z$。由旋度定义，

$$
B_x=\frac{\partial A_z}{\partial y},\qquad
B_y=-\frac{\partial A_z}{\partial x}.
$$

于是沿磁感线，

$$
\begin{aligned}
\mathrm dA_z
&=\frac{\partial A_z}{\partial x}\mathrm dx
+\frac{\partial A_z}{\partial y}\mathrm dy\\
&=-B_y\,\mathrm dx+B_x\,\mathrm dy=0.
\end{aligned}
$$

所以非零场处的磁感线是 $A_z$ 的等值线。$A_z$ 在这里是流函数式的辅助量，不是磁场大小，也不是电势；它可以加上任意常量而不改变磁场。

对一根导线，取 $A_{zi}=-Ks_i\ln(r_i/\ell)$。对它求导：

$$
\begin{aligned}
\frac{\partial A_{zi}}{\partial y}
&=-Ks_i\frac{y-b_i}{r_i^2}=B_{ix},\\
-\frac{\partial A_{zi}}{\partial x}
&=Ks_i\frac{x-a_i}{r_i^2}=B_{iy}.
\end{aligned}
$$

对数里的 $r_i/\ell$ 无量纲；不能对有量纲的距离直接取对数而不说明基准。每根的场均被恢复，故把这些 $A_{zi}$ 相加就得到总场的流函数。

两导线时，

$$
A_z=\frac K2\ln\frac{r_-^2}{r_+^2},
\qquad
\frac{r_-^2}{r_+^2}=\kappa,\quad \kappa>0.
$$

将两个距离平方展开：

$$
\begin{aligned}
(x+\ell)^2+y^2
&=\kappa\left[(x-\ell)^2+y^2\right],\\
(1-\kappa)(x^2+y^2+\ell^2)
+2\ell(1+\kappa)x&=0.
\end{aligned}
$$

若 $\kappa\ne1$，则

$$
x^2+y^2+\ell^2
=2\ell\frac{\kappa+1}{\kappa-1}x,
\qquad
x_c=\ell\frac{\kappa+1}{\kappa-1}.
$$

这独立恢复主解析中的圆心关系。$\kappa>1$ 对应右侧圆，$0<\kappa<1$ 对应左侧圆；若 $\kappa=1$，在未作除法的方程中直接得到 $x=0$。这条路线天然保留中轴，能检查积分因子法是否漏解。

**四导线的精确等值线，不需要先把所有分式通成一个庞大分母。**

按第9步的符号，四根相加得到

$$
A_z=-\frac K2\ln\frac{r_1^2r_3^2}{r_2^2r_4^2}.
$$

因此精确磁感线满足

$$
\boxed{\frac{r_1^2r_3^2}{r_2^2r_4^2}=\kappa,\qquad \kappa>0.}
$$

为写出不含距离符号的方程，令 $S=x^2+y^2+2\ell^2$。对角两根距离平方分别是 $S\mp2\ell(x+y)$，另两根分别是 $S\pm2\ell(x-y)$。逐项相乘：

$$
\begin{aligned}
r_1^2r_3^2
&=[S-2\ell(x+y)][S+2\ell(x+y)]\\
&=S^2-4\ell^2(x+y)^2,\\
r_2^2r_4^2
&=[S+2\ell(x-y)][S-2\ell(x-y)]\\
&=S^2-4\ell^2(x-y)^2.
\end{aligned}
$$

所以总场的精确曲线可写为

$$
S^2-4\ell^2(x+y)^2
=\kappa\left[S^2-4\ell^2(x-y)^2\right].
$$

一般含四次项。$\kappa=1$ 时，两乘积之差为

$$
\begin{aligned}
r_1^2r_3^2-r_2^2r_4^2
&=-4\ell^2\left[(x+y)^2-(x-y)^2\right]\\
&=-16\ell^2xy.
\end{aligned}
$$

故 $\kappa=1$ 恰给出坐标轴 $xy=0$。这也证明轴线不只是线性近似的分界线，在精确四导线场中同样保持不变。零点处仍须分支解释，不能把等值线的交叉当作非零场线交叉。

在原点附近，$r_2^2r_4^2\simeq4\ell^4$，故

$$
\begin{aligned}
\frac{r_1^2r_3^2}{r_2^2r_4^2}
&=1-\frac{16\ell^2xy}{r_2^2r_4^2}
=1-\frac{4xy}{\ell^2}
+O\!\left(\frac{r^4}{\ell^4}\right),\\
A_z
&=-\frac K2\ln\left[
1-\frac{4xy}{\ell^2}
+O\!\left(\frac{r^4}{\ell^4}\right)\right]\\
&=\frac{2Kxy}{\ell^2}
+O\!\left(\frac{Kr^4}{\ell^4}\right).
\end{aligned}
$$

最后一步使用 $\ln(1+\varepsilon)=\varepsilon+O(\varepsilon^2)$。这一粗阶展开已经足以恢复 $xy=C_2$；下文再利用四角交替的更强对称性，证明上述余项估计实际上可以改进。误差阶的粗界可用，但不能把粗界误称为“下一项必为四次”。

**四角交替电流的三次场修正完全抵消，近似精度比一般线性场更高。**

这一点可以用复数形式把四个分式同时整理。令 $\zeta=x+\mathrm i y$，导线位置的复数为 $w_i=a_i+\mathrm i b_i$。这里 $\mathrm i$ 是虚数单位，不是电流或导线编号。由单导线场，

$$
B_{iy}+\mathrm iB_{ix}
=Ks_i\frac{(x-a_i)-\mathrm i(y-b_i)}{r_i^2}
=\frac{Ks_i}{\zeta-w_i}.
$$

设 $w=\ell(1+\mathrm i)$，则正电流位于 $w,-w$；设 $v=\ell(-1+\mathrm i)$，则负电流位于 $v,-v$。两对先分别相加：

$$
\begin{aligned}
B_y+\mathrm iB_x
&=K\left[\frac1{\zeta-w}+\frac1{\zeta+w}
-\frac1{\zeta-v}-\frac1{\zeta+v}\right]\\
&=2K\zeta\left[
\frac1{\zeta^2-w^2}-\frac1{\zeta^2-v^2}\right].
\end{aligned}
$$

因为 $w^2=2\mathrm i\ell^2$、$v^2=-2\mathrm i\ell^2$，通分后

$$
\begin{aligned}
B_y+\mathrm iB_x
&=2K\zeta
\frac{4\mathrm i\ell^2}
{(\zeta^2-2\mathrm i\ell^2)(\zeta^2+2\mathrm i\ell^2)}\\
&=\frac{8\mathrm iK\ell^2\zeta}{\zeta^4+4\ell^4}\\
&=\frac{2\mathrm iK\zeta}{\ell^2}
\frac1{1+\zeta^4/(4\ell^4)}.
\end{aligned}
$$

在 $|\zeta|<\sqrt2\ell$ 中，几何级数收敛，展开得

$$
B_y+\mathrm iB_x
=\frac{2\mathrm iK\zeta}{\ell^2}
-\frac{\mathrm iK\zeta^5}{2\ell^6}
+O\!\left(\frac{K|\zeta|^9}{\ell^{10}}\right).
$$

先把一次项分开：$\mathrm i(x+\mathrm i y)=-y+\mathrm i x$，所以其实部为 $B_y=-2Ky/\ell^2$，虚部为 $B_x=2Kx/\ell^2$，与逐根求导法一致。五次幂的实部、虚部分别为

$$
\begin{aligned}
\operatorname{Re}\zeta^5
&=x^5-10x^3y^2+5xy^4,\\
\operatorname{Im}\zeta^5
&=5x^4y-10x^2y^3+y^5.
\end{aligned}
$$

乘以 $-\mathrm i$ 会把后一行变成实部、把前一行的负值变成虚部。因此

$$
\begin{aligned}
B_x&=\frac{2Kx}{\ell^2}
+\frac K{2\ell^6}
(-x^5+10x^3y^2-5xy^4)
+O\!\left(\frac{Kr^9}{\ell^{10}}\right),\\
B_y&=-\frac{2Ky}{\ell^2}
+\frac K{2\ell^6}
(5x^4y-10x^2y^3+y^5)
+O\!\left(\frac{Kr^9}{\ell^{10}}\right).
\end{aligned}
$$

没有三次修正，五次才是下一个非零阶。相应的 $A_z$ 二次项之后，下一非零多项式项为六次，而不是四次。对于 $r>0$，用线性场的大小归一化矢量误差，由精确复数式直接得到

$$
\begin{aligned}
\frac{|\boldsymbol B-\boldsymbol B_{\mathrm{lin}}|}
{|\boldsymbol B_{\mathrm{lin}}|}
&=\left|\frac{\zeta^4}{4\ell^4+\zeta^4}\right|\\
&\leq\frac{r^4}{4\ell^4-r^4},
\qquad r<\sqrt2\ell.
\end{aligned}
$$

此处使用反三角不等式 $|4\ell^4+\zeta^4|\geq4\ell^4-r^4$。因此四导线的线性场相对误差是 $O((r/\ell)^4)$。原点线性场和精确场均为零，不能在那里直接取相对误差的 $0/0$；应说绝对误差为零并取邻近非零点的极限。

**圆族、轴线与远处弱场各有不同的边界含义。**

两导线总有符号电流为零，远处的 $1/r$ 项抵消。从精确场强看，$r_\pm\simeq r$，于是 $B\simeq2K\ell/r^2$。四导线不仅总电流为零，交替几何又进一步抵消较低阶的远场项；由精确复数式，远处 $B\simeq8K\ell^2/r^3$。这些远场行为能检查表达式的长度幂次，但不能用来代替原点附近的展开。

一对导线的圆族参数沿这一对单独产生的磁场保持不变；加入另一对后，一般不再保持。因此“先配对”是计算总矢量的技巧，不是直接把两套圆相交来确定总磁感线的技巧。真正不变的是总 $A_z$，而不是两个单独 $A_z$ 同时保持常数。

## 七、易错点

**把负电流的作用只理解为大小不变。** 大小确实不变，但整个矢量翻转。右导线正电流在左侧的场向下，左导线负电流在右侧的场也向下；原点两导线场不抵消。先画这两个箭头，再写代数式，能直接查出 $B_y$ 的符号。

**把 $K/r_i$ 当成笛卡尔分量。** $K/r_i$ 是单根场的大小；分量要将这个大小投影到相应坐标轴上，投影可以为正，也可以为负。单导线通式的分母出现平方，不是磁场衰减变成 $1/r_i^2$，因为分子中的切向向量长度本身为 $r_i$，约去后仍按距离的一次方衰减。

**通分时漏掉电流方向的负号。** 两导线的竖直分量已在第2步写清，不能把两个带符号的量都改成正数再相加。四导线的 $B_y$ 最后一项必须是第四根的竖直分量。将不同轴分量误加会破坏中心抵消或导数检查。

**只算四导线原点的磁场。** $\boldsymbol B(O)=0$ 不是整个附近的答案。必须保留一阶位移，且水平和竖直梯度等大反号。若写成 $q(x,y)$，其散度为 $2q$，与无磁单极子的磁场不相容。

**把线性近似无限延伸。** 四导线的双曲线只在中心小窗口中成立，接近各导线时场具有奇异的圆周结构。两导线主阶竖直直线也不能替代所有精确圆族。

**把积分常量当成坐标变量。** $x_c$ 沿一条圆不变，$C_2=xy$ 沿一条近似双曲线不变；它们的量纲分别为长度和长度平方。$x$、$y$ 仍沿曲线变化。正负 $C_2$ 不能一律写成正数而漏掉两个象限。

**除法后忘记补解。** 除以 $x^2$ 漏掉两导线中轴 $x=0$；除以 $xy$ 漏掉四导线的坐标轴。补解必须代回磁场或原微分形式，不是机械地把“所有使分母为零的点”都加为解。导线奇点和磁零点各有特殊性质，均不能当普通场线点。

**把等值线的交叉误认为磁感线能在非零场处交叉。** 四导线的 $\kappa=1$ 等值集合含两个坐标轴，它们在原点相交，但原点恰为零场。除零点和奇点外，总场确定唯一切线方向，场线不能任意交叉。

**看到四根对称导线就默认三次修正存在。** 一阶展开只保证主阶，不能凭经验指定下一项。四角交替布局具有特殊抵消，下一非零场项为五次。若要给误差阶，须由精确式或逐阶展开核验。

## 八、课堂讲解建议

先不进行分式运算，让学生只在原点画两根电流各自产生的磁场箭头，检验是否都向下；再在四导线图上画出四个中心场箭头，明确“两个场相加”和“四个场抵消”是不同结论。此阶段保留电流点叉、坐标轴和导线编号即可，不增加无助于判断方向的长标签。

随后用图2-2确认空间关系：导线平行于 $z$，虚线方框不是回路，$xy$ 平面只是截面。板书一根任意位置导线的公式，把它作为每一次代入的共同模板。要求在代入第二根负电流时把两个分量都反号，以此训练矢量符号意识。

计算两导线总场时，将水平通分和竖直通分分栏写，先完成分子再合并公共系数。学生较容易卡在竖直分子，可引入 $A=x^2+y^2+\ell^2$，把四个乘积简化为“$-2\ell A+4\ell x^2$”。接着分别代 $P=O$、$x=0$、$y=0$，让公式接受方向与大小的三次检验。

场线部分先讲切线平行关系，再写微分形式。不要一开始就用斜率商，使学生误以为竖直线没有方程。积分因子可以通过直接验证全微分展示，重点是解释为什么除以 $x^2$ 后必须回头检查 $x=0$。结合图2-4指出圆没有穿过电流导线，且中心小范围中圆弧近似直线。

四导线的一阶展开先由一根场求四个导数，再利用 $a_i^2=b_i^2$ 和 $s_ia_ib_i=\ell^2$ 相加。让学生看到交叉导数为何为零，及每根水平梯度为何同号，而不是把四根完全通分后直接抄线性结果。

图2-5应与 $B_x=qx$、$B_y=-qy$ 同时展示。可提问：“第一象限一点沿场移动时，横坐标和纵坐标分别怎样变化？”再用 $\mathrm d(xy)=y\,\mathrm dx+x\,\mathrm dy=0$ 联系双曲线不变量。强调原点没有非零场方向，不能在这里机械套斜率商。

流函数路线可在主解掌握后展示，帮助学生把复杂场线积分转化为一个等值线问题。复数的精确整理属于进一步深化，逐步讲清实部为何是 $B_y$、虚部为何是 $B_x$，不能只展示结论。需要控制课堂容量时，可将五次修正与误差估计安排为带完整解答的后续研读内容，不删减主解的符号、除法补解和线性展开过程。

## 九、变式训练

<!-- KEEP_TOGETHER_START -->

**变式1：用实际电流与长度计算局部磁场，并估计近似误差。**

取 $\mu_0=4\pi\times10^{-7}\,\mathrm{T\,m/A}$、$I=5.0\,\mathrm A$、$\ell=0.25\,\mathrm m$。分别求两导线原点磁场、四导线的梯度系数，以及四导线在 $P=(0.010\,\mathrm m,0.020\,\mathrm m)$ 处的线性近似场和场强。

<!-- KEEP_TOGETHER_END -->

先计算共同系数：

$$
K=\frac{(4\pi\times10^{-7})(5.0)}{2\pi}
=1.0\times10^{-6}\,\mathrm{T\,m}.
$$

两导线原点：

$$
\boldsymbol B(O)
=-\frac{2K}{\ell}\boldsymbol e_y
=-8.0\times10^{-6}\boldsymbol e_y\,\mathrm T.
$$

四导线梯度：

$$
q=\frac{2K}{\ell^2}
=\frac{2.0\times10^{-6}}{0.0625}
=3.2\times10^{-5}\,\mathrm{T/m}.
$$

再把坐标乘上梯度，保留两分量的符号：

$$
\begin{aligned}
B_x&\simeq(3.2\times10^{-5})(0.010)
=3.2\times10^{-7}\,\mathrm T,\\
B_y&\simeq-(3.2\times10^{-5})(0.020)
=-6.4\times10^{-7}\,\mathrm T,\\
B&\simeq\sqrt{(3.2\times10^{-7})^2+(6.4\times10^{-7})^2}\\
&=\sqrt{51.2}\times10^{-7}\,\mathrm T
\simeq7.1554\times10^{-7}\,\mathrm T.
\end{aligned}
$$

所求方向指向右下，正好对应图2-5的第一象限箭头。该点的 $r^2=0.0005\,\mathrm m^2$，故

$$
\left(\frac r\ell\right)^2=0.008,\qquad
\left(\frac r\ell\right)^4=0.000064.
$$

矢量相对误差上界为

$$
\frac{0.000064}{4-0.000064}
\simeq1.60003\times10^{-5},
$$

约为 $0.00160003\%$。这个界是相对于线性场的矢量误差，不意味着每个极小分量都具有同一相对误差；某个分量恰为零时，应比较绝对误差而不是对该分量做除法。

**变式2：确定经过指定点的两导线精确磁感线。**

两导线仍为本题配置。给定点 $P=(2\ell/5,3\ell/10)$，求经过它的精确场线、圆心、半径，并判断方向。

第7步的第一积分给出

$$
\begin{aligned}
2x_c
&=\frac{x_P^2+y_P^2+\ell^2}{x_P}\\
&=\frac{(4/25+9/100+1)\ell^2}{2\ell/5}\\
&=\frac{(5/4)\ell^2}{2\ell/5}
=\frac{25\ell}{8},\\
x_c&=\frac{25\ell}{16}.
\end{aligned}
$$

半径平方与半径为

$$
\begin{aligned}
R^2
&=\left(\frac{25\ell}{16}\right)^2-\ell^2
=\frac{625-256}{256}\ell^2
=\frac{369}{256}\ell^2,\\
R&=\frac{3\sqrt{41}}{16}\ell.
\end{aligned}
$$

因此

$$
\boxed{
\left(x-\frac{25\ell}{16}\right)^2+y^2
=\frac{369\ell^2}{256}.
}
$$

独立用距离比核对：该点 $r_-^2=41\ell^2/20$、$r_+^2=9\ell^2/20$，故 $\kappa=41/9$，再代 $x_c=\ell(\kappa+1)/(\kappa-1)$ 得 $x_c=25\ell/16$，与积分结果相同。

此圆在右侧，沿场为逆时针。也可在指定点检查：$xy>0$，所以 $B_x<0$；$x^2-y^2-\ell^2=(4/25-9/100-1)\ell^2=-93\ell^2/100<0$，所以 $B_y<0$，切线朝左下，与该圆在左上弧的逆时针方向一致。若给定点改为 $(0,3\ell/10)$，则不能套除以 $x_P$ 的公式，应直接答中轴 $x=0$，方向向下。

**变式3：两反向电流大小不相等时，零场点在哪里？**

右导线在 $(\ell,0)$，电流为 $+I$；左导线在 $(-\ell,0)$，电流为 $-\eta I$，其中 $\eta>0$。求 $\eta\ne1$ 时的有限零场点，说明它位于哪一侧；再说明 $\eta=1$ 为什么没有有限零场点。

场分量为

$$
\begin{aligned}
B_x&=K y\left(-\frac1{r_+^2}+\frac{\eta}{r_-^2}\right),\\
B_y&=K\left(\frac{x-\ell}{r_+^2}
-\frac{\eta(x+\ell)}{r_-^2}\right).
\end{aligned}
$$

假设 $y\ne0$，由 $B_x=0$ 得 $1/r_+^2=\eta/r_-^2$。代入 $B_y$ 后，

$$
B_y=\frac K{r_+^2}
[(x-\ell)-(x+\ell)]
=-\frac{2K\ell}{r_+^2}\ne0.
$$

与零场条件矛盾。因此任何零场点必在 $y=0$。在该轴上且避开导线，$B_y$ 化成

$$
B_y=K\left[\frac1{x-\ell}-\frac{\eta}{x+\ell}\right].
$$

令其为零，逐步移项：

$$
\begin{aligned}
x+\ell&=\eta(x-\ell),\\
(\eta-1)x&=(\eta+1)\ell,\\
x_0&=\frac{\eta+1}{\eta-1}\ell,\qquad y_0=0.
\end{aligned}
$$

若 $\eta>1$，左侧电流更大，$x_0>\ell$，零点在较弱的右导线外侧；若 $0<\eta<1$，$x_0<-\ell$，零点在较弱的左导线外侧。两导线之间两场同向，不会抵消。取 $\eta=2$，有 $x_0=3\ell$，右导线距零点 $2\ell$、左导线距零点 $4\ell$，大小分别为 $K/(2\ell)$ 与 $2K/(4\ell)$，确实相等反向。

$\eta=1$ 时，轴线零场方程变成 $x+\ell=x-\ell$，因 $\ell>0$ 不可能成立；非轴线又已被排除，所以没有有限零场点。$\eta\to1$ 时上式的 $|x_0|\to\infty$，表示抵消点逃向无穷远，不是原点出现一个新零点。

在 $\eta=2$、$x_0=3\ell$ 处，还可判断局部场型。令 $X=x-3\ell$、$Y=y$，在零点求导：

$$
\begin{aligned}
\left.\frac{\partial B_x}{\partial y}\right|_0
&=K\left[-\frac1{(2\ell)^2}
+\frac2{(4\ell)^2}\right]
=-\frac K{8\ell^2},\\
\left.\frac{\partial B_y}{\partial x}\right|_0
&=K\left[-\frac1{(2\ell)^2}
+\frac2{(4\ell)^2}\right]
=-\frac K{8\ell^2},\\
\left.\frac{\partial B_x}{\partial x}\right|_0
&=\left.\frac{\partial B_y}{\partial y}\right|_0=0.
\end{aligned}
$$

因此 $\boldsymbol B\simeq-g(Y,X)$，其中 $g=K/(8\ell^2)>0$。场线满足 $Y\,\mathrm dY=X\,\mathrm dX$，即 $Y^2-X^2=\text{常量}$，分界线为 $Y=\pm X$。这是旋转了的双曲线型零点，不是各个方向都朝中心的汇聚场。

**变式4：怎样为四导线线性近似选定可靠的使用范围？**

要求所有方向上的矢量相对误差都不超过 $\varepsilon=0.1\%=0.001$，求一个保证满足要求的圆形中心区域，并比较半径减半后误差的变化。

由已证明的方向无关上界，只要

$$
\frac{(r/\ell)^4}{4-(r/\ell)^4}\leq\varepsilon
$$

即可。令 $u=(r/\ell)^4$。在收敛区内 $u<4$，分母为正，所以移项不改变不等号：

$$
\begin{aligned}
u&\leq\varepsilon(4-u),\\
(1+\varepsilon)u&\leq4\varepsilon,\\
u&\leq\frac{4\varepsilon}{1+\varepsilon},\\
\frac r\ell&\leq
\left(\frac{4\varepsilon}{1+\varepsilon}\right)^{1/4}.
\end{aligned}
$$

代入 $\varepsilon=0.001$ 得

$$
\frac r\ell\leq
\left(\frac{0.004}{1.001}\right)^{1/4}
\simeq0.25142.
$$

这是保证所有方向的范围，不是说超过这个半径后每个方向都立刻失效。由精确复数式，当 $\zeta^4=-r^4$，也就是与坐标轴成 $\pi/4$ 等方向时，上界恰可取等；因此对要求“全部方向”而言，这个圆形半径界也是锐的。

若把边界半径减半，则 $u$ 变成 $u/16$，误差上界为

$$
\begin{aligned}
E_{\frac12}
&=\frac{u/16}{4-u/16}
=\frac{u}{64-u}\\
&=\frac{\varepsilon}{16+15\varepsilon}
=\frac{0.001}{16.015}
\simeq6.2441\times10^{-5}.
\end{aligned}
$$

百分数约为 $0.0062441\%$，接近原误差的 $1/16$，而不是 $1/4$。这由五次绝对修正相对于一次主阶的四次比值决定。原点处直接以零绝对误差理解，不在零场点计算没有定义的相对比值。

<!-- question-complete -->
