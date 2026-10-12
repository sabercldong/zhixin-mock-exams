# 第4题

<!-- question-start -->

一根轻质细弹簧的初始伸长量为 $\Delta l_1$，两端固定在桌面上的 $A,B$ 两点。在弹簧正中间安置一个小球，使它分别作小幅横向振动和小幅纵向振动，横向振动周期与纵向振动周期之比为 $n_1=4$。将弹簧的伸长量增加 $\Delta x=3.5\,\mathrm{cm}$ 后，周期之比变为 $n_2=3$。

求弹簧原长 $l_0$、第一种情况下的伸长量 $\Delta l_1$ 和第二种情况下的伸长量 $\Delta l_2$。设实验中弹簧满足胡克定律；横向和纵向的定义如图4-1所示。

![图4-1 桌面内垂直与平行于弹簧轴线的两种振动。](../figures/question-04.png){width=88%}

<!-- question-end -->

## 一、题型定位

这是由两个小振动周期反求弹簧几何参数的问题。纵向振动改变两半弹簧的伸长量，横向振动主要改变两半拉力的方向；后者的线性回复力由已有预张力产生。先从真实受力或势能求两个等效劲度，再取周期比，质量和弹簧劲度才会消去。

本题的“原长”是弹簧没有受力时的长度 $l_0$，不是第一次实验中两固定端点的距离。增加的 $\Delta x$ 是两次总伸长量之差，也就是两次端点距离之差，不是小球振动的振幅。

## 二、知识点

均匀弹簧截取一半后劲度加倍；串联弹簧的柔度相加；小球的左右弹簧力与净回复力；小振幅简谐运动；斜向拉力的方向投影；平方根的二阶展开；势能的二次项与等效劲度；预张力引起的横向线性刚度；周期比消元；两次测量的正值条件与回代检验。

采用均匀、左右对称的轻质弹簧模型，忽略弹簧质量、阻尼和桌面内摩擦。桌面支承抵消小球重力，横向振动仍在桌面内，并不是在重力方向上振动。小球质量记作 $m$，整根弹簧的劲度记作 $k$；它们不需要由题目给出，因为周期比中会同时消去。

## 三、物理图像

在平衡位置，两半弹簧都受到预拉伸，向左和向右的力相等。小球沿 $AB$ 向右移动时，左半段进一步拉长，右半段缩短；左拉力增加，右拉力减小，两种变化共同形成向左回复力。

小球在桌面内垂直于 $AB$ 移动时，两半段长度相同，拉力的水平分量相互抵消，垂直于 $AB$ 的分量却同向指向平衡轴线。很小的横向位移只使长度增加一个二阶小量，但原来已有的张力乘上一个一阶小角度，就能给出一阶回复力。因此不能因长度变化小就把横向回复力判为零。

增加预伸长时，纵向线性劲度不变，横向线性劲度增大。横向周期随之缩短，所以周期比由 $4$ 降为 $3$ 与物理趋势一致。

## 四、解题入口

用 $\Delta l$ 暂时表示任意一次实验中的总伸长量，并记

$$
L=l_0+\Delta l,\qquad a=\frac L2,\qquad b=\frac{l_0}{2}.
$$

$L$ 是两个固定端点的距离，$a$ 是平衡时每半段的长度，$b$ 是每半段的原长。先分别求 $T_\parallel$ 和 $T_\perp$，再写 $n=T_\perp/T_\parallel$；不能把频率比与周期比颠倒。

求出一个关于 $l_0/\Delta l$ 的关系后，对两次实验各列一式，并补上 $\Delta l_2-\Delta l_1=\Delta x$。这样恰有三个独立方程求三个长度，不需要另猜小球质量或弹簧劲度。

## 五、解析

**第1步：建立坐标、几何长度与预伸长的统一记号。**

令 $O$ 为两端点的中点，沿 $AB$ 从 $A$ 指向 $B$ 为 $+x$，在桌面内垂直于 $AB$ 取 $+y$。平衡位置小球在 $O$，端点坐标为 $(-a,0)$、$(a,0)$。当前整根原长为 $l_0$，端点距为 $L=l_0+\Delta l$，且 $\Delta l>0$。

每半根的平衡长度为 $a=L/2$，原长为 $b=l_0/2$，所以每半根平衡伸长为

$$
a-b=\frac{L-l_0}{2}=\frac{\Delta l}{2}.
$$

两次实验分别将 $\Delta l$ 换成 $\Delta l_1,\Delta l_2$。小球振动位移 $x,y$ 与端点拉开量 $\Delta x$ 是三种不同的量；在每一次测量周期时，端点不随小球移动。

**第2步：证明每半根的劲度是整根的两倍。**

图4-2将均匀弹簧分为相同的两半。先不讨论振动，对整根施加轴向拉力 $F$。两半串联，因此各自传递的力都为 $F$，不是每半根只受到 $F/2$。

![图4-2 相同半弹簧的长度、劲度与平衡预张力。](../figures/halves-04.png){width=68%}

记每半根劲度为 $k_h$。两半伸长量相加：

$$
\begin{aligned}
\Delta l&=\frac F{k_h}+\frac F{k_h}
=\frac{2F}{k_h},\\
F&=k\Delta l,\\
\frac1k&=\frac2{k_h},\\
\boxed{k_h=2k}.
\end{aligned}
$$

半根原长较短，达到相同相对变形所需的绝对伸长较小，所以劲度较大。后面小球受到左右两半的力，各半都要使用 $2k$；不能把整根劲度 $k$ 分成两个 $k/2$。

**第3步：求平衡预张力，并说明其作用。**

由图4-2每半根伸长 $\Delta l/2$，其平衡拉力为

$$
T_0=k_h\frac{\Delta l}{2}
=2k\frac{\Delta l}{2}
=\boxed{k\Delta l}.
$$

小球受到左、右大小均为 $T_0$ 的相反拉力，合力为零。合力为零不表示每根弹簧没有力；这份已有张力将在横向偏转后产生回复分量。

在纵向运动中，$T_0$ 的相反部分会抵消；在横向运动中，两个 $T_0$ 的投影却会相加。这个差别是两种周期不同的根源。

**第4步：对纵向位移逐项列出左右拉力。**

先令小球向右移动 $x$，保持 $y=0$。图4-3左半长度为 $a+x$、右半长度为 $a-x$。只要小球仍在端点之间，两式就是精确的几何长度。

![图4-3 纵向位移引起的两半长度变化与小球受力。](../figures/longitudinal-04.png){width=92%}

左、右半段的伸长分别为

$$
\begin{aligned}
\delta_L&=a+x-b=\frac{\Delta l}{2}+x,\\
\delta_R&=a-x-b=\frac{\Delta l}{2}-x.
\end{aligned}
$$

左力指向 $A$，右力指向 $B$。按 $+x$ 向右写代数分量：

$$
\begin{aligned}
T_L&=2k\left(\frac{\Delta l}{2}+x\right)
=k\Delta l+2kx,\\
T_R&=2k\left(\frac{\Delta l}{2}-x\right)
=k\Delta l-2kx,\\
F_x&=T_R-T_L\\
&=(k\Delta l-2kx)-(k\Delta l+2kx)\\
&=\boxed{-4kx}.
\end{aligned}
$$

负号表示回复方向与位移相反。取 $x<0$ 时，同一式给正向回复力，不需要为左移另换符号约定。两个弹簧力的变化量各为 $2kx$，总回复量是 $4kx$。

**第5步：由运动方程识别纵向角频率和周期。**

由牛顿第二定律

$$
\begin{aligned}
m\ddot x&=-4kx,\\
\ddot x+\frac{4k}{m}x&=0.
\end{aligned}
$$

与简谐运动标准形式 $\ddot x+\omega_\parallel^2x=0$ 比较：

$$
\begin{aligned}
\omega_\parallel^2&=\frac{4k}{m},\\
T_\parallel&=\frac{2\pi}{\omega_\parallel}
=\boxed{2\pi\sqrt{\frac{m}{4k}}}.
\end{aligned}
$$

例如初始位移 $A_x$、初速度为零时，解为 $x=A_x\cos(\omega_\parallel t)$；相位增加 $2\pi$ 后重复初始状态，所以周期不是 $\pi/\omega_\parallel$。

这里的等效劲度为 $4k$，与预伸长 $\Delta l$ 无关。对只能保持受拉形态的细弹簧，取 $A_x<\Delta l/2$，便可保证两半在整个周期内都有正伸长，避免一侧松弛而破坏上述模型。

**第6步：建立横向位移的真实几何。**

再令小球沿 $+y$ 移到 $P=(0,y)$，保持 $x=0$。图4-4中两半弹簧长度相同，记作 $\ell$；端点、中点和 $P$ 构成两个直角三角形。

![图4-4 横向偏转的三角几何与两斜向拉力的回复分量。](../figures/transverse-04.png){width=92%}

由勾股定理及斜边投影，

$$
\ell=\sqrt{a^2+y^2},
\qquad
\sin\alpha=\frac y\ell,
\qquad
\cos\alpha=\frac a\ell.
$$

对 $y>0$，两拉力分别向左下、右下，两沿图中 $x$ 轴的分量相互抵消，沿 $y$ 轴的分量均向 $-y$。$\alpha$ 是弹簧与平衡轴线的夹角，不是小球的振动相位。

实际长度增加量为 $\ell-a$，不是 $y$。小位移时 $\ell-a$ 为二阶小量，因此不能把每半弹簧的总伸长直接写成 $\Delta l/2+y$。

**第7步：先求横向精确回复力，再作小幅线性化。**

每半段张力大小为 $T=2k(\ell-b)$。图4-4两个 $x$ 分量抵消，两个 $y$ 分量相加：

$$
\begin{aligned}
F_y&=-2T\sin\alpha\\
&=-2\,[2k(\ell-b)]\frac y\ell\\
&=-4ky\left(1-\frac b\ell\right)\\
&=\boxed{-4ky\left(1-\frac{l_0}
{\sqrt{L^2+4y^2}}\right)}.
\end{aligned}
$$

最后一步同时将 $\ell$ 和 $b$ 乘二，使用 $2\ell=\sqrt{L^2+4y^2}$、$2b=l_0$。此式尚未假设 $y$ 很小；$y$ 的正负已经包含在代数分量里。

在固定的 $\Delta l>0$ 下取 $y\to0$，括号的一阶回复系数为

$$
\begin{aligned}
1-\frac{l_0}{L}
&=\frac{L-l_0}{L}
=\frac{\Delta l}{L},\\
F_y&=-\frac{4k\Delta l}{L}\,y+O(y^3).
\end{aligned}
$$

因此横向小振动的等效劲度为

$$
\boxed{K_\perp=\frac{4k\Delta l}{l_0+\Delta l}}.
$$

几何捷径是取 $T\simeq T_0$、$\sin\alpha\simeq y/a$，于是 $F_y\simeq-2T_0y/a$，得到相同系数。但它只保留线性项；上面的精确式说明省略项从三次回复力开始，而不是凭直觉直接指定等效劲度。

**第8步：用完整势能展开核对横纵两个劲度。**

每半段劲度为 $2k$，弹性势能是该半段伸长量平方乘 $\frac12(2k)$。纵向势能为

$$
\begin{aligned}
U_\parallel
&=k\left(\frac{\Delta l}{2}+x\right)^2
+k\left(\frac{\Delta l}{2}-x\right)^2\\
&=k\left[\frac{(\Delta l)^2}{4}
+\Delta l\,x+x^2
+\frac{(\Delta l)^2}{4}
-\Delta l\,x+x^2\right]\\
&=\frac{k(\Delta l)^2}{2}+2kx^2.
\end{aligned}
$$

两一次交叉项抵消。与 $U=U_0+\frac12Kx^2$ 比较，$K_\parallel=4k$；常数 $U_0$ 不产生回复力。

横向两半长度均为 $\ell$，故

$$
\begin{aligned}
U_\perp
&=2\cdot\frac12(2k)(\ell-b)^2\\
&=2k\left(\frac{\sqrt{L^2+4y^2}-l_0}{2}\right)^2\\
&=\frac k2\left(\sqrt{L^2+4y^2}-l_0\right)^2.
\end{aligned}
$$

使用 $\sqrt{1+u}=1+\frac u2+O(u^2)$，令 $u=4y^2/L^2$，得到

$$
\begin{aligned}
\sqrt{L^2+4y^2}
&=L\sqrt{1+\frac{4y^2}{L^2}}\\
&=L+\frac{2y^2}{L}+O(y^4),\\
\sqrt{L^2+4y^2}-l_0
&=\Delta l+\frac{2y^2}{L}+O(y^4).
\end{aligned}
$$

再平方并保留到 $y^2$：

$$
\begin{aligned}
U_\perp
&=\frac k2\left[(\Delta l)^2
+2\Delta l\frac{2y^2}{L}+O(y^4)\right]\\
&=\frac{k(\Delta l)^2}{2}
+\frac{2k\Delta l}{L}y^2+O(y^4).
\end{aligned}
$$

二次项来自“已有伸长 $\Delta l$”与“几何长度的二阶变化”的交叉乘积。若提前把 $\ell$ 完全替换为 $a$，这一项就被误删；若把二次项的系数直接当劲度，又会少一个因子二。

将二次项写成 $\frac12K_\perp y^2$，仍得 $K_\perp=4k\Delta l/L$；再由 $F_y=-\mathrm dU_\perp/\mathrm dy$，得到第7步同一线性回复力。受力法与能量法独立吻合。

**第9步：求横向周期，正确形成周期比。**

横向运动方程为

$$
m\ddot y=-K_\perp y.
$$

因此

$$
\begin{aligned}
\omega_\perp^2&=\frac{4k\Delta l}{mL},\\
T_\perp&=2\pi\sqrt{\frac{mL}{4k\Delta l}}.
\end{aligned}
$$

横向周期除以纵向周期，不是反过来：

$$
\begin{aligned}
n=\frac{T_\perp}{T_\parallel}
&=\frac{2\pi\sqrt{mL/(4k\Delta l)}}
{2\pi\sqrt{m/(4k)}}\\
&=\sqrt{\frac L{\Delta l}}\\
&=\boxed{\sqrt{1+\frac{l_0}{\Delta l}}}.
\end{aligned}
$$

质量 $m$、整根劲度 $k$ 与 $2\pi$ 均消去。由于 $l_0,\Delta l>0$，$n>1$：横向劲度较小，横向周期较长，与图4-4的斜向力投影一致。

**第10步：将两次测量逐式转成长度关系。**

第一次 $n_1=4$，先平方而不是直接令长度比等于 $4$：

$$
\begin{aligned}
16&=1+\frac{l_0}{\Delta l_1},\\
\frac{l_0}{\Delta l_1}&=15,\\
\Delta l_1&=\frac{l_0}{15}.
\end{aligned}
$$

第二次 $n_2=3$，同理

$$
\begin{aligned}
9&=1+\frac{l_0}{\Delta l_2},\\
\frac{l_0}{\Delta l_2}&=8,\\
\Delta l_2&=\frac{l_0}{8}.
\end{aligned}
$$

增加的伸长为两次总伸长之差：

$$
\begin{aligned}
\Delta l_2-\Delta l_1
&=\Delta x=3.5\,\mathrm{cm},\\
\left(\frac18-\frac1{15}\right)l_0
&=3.5\,\mathrm{cm},\\
\frac{15-8}{120}l_0&=3.5\,\mathrm{cm},\\
l_0&=3.5\frac{120}{7}\,\mathrm{cm}
=\boxed{60\,\mathrm{cm}}.
\end{aligned}
$$

通分得到 $7/120$，再乘倒数 $120/7$。厘米在同一组长度关系中可以统一使用，不必先改为米；若后面计算力或能量，才统一改用国际单位。

恢复两个伸长量：

$$
\boxed{
\Delta l_1=\frac{60}{15}\,\mathrm{cm}=4.0\,\mathrm{cm},
\qquad
\Delta l_2=\frac{60}{8}\,\mathrm{cm}=7.5\,\mathrm{cm}}.
$$

**第11步：将答案代回几何、周期比和增量。**

第一、第二次端点距离分别为

$$
L_1=60+4=64\,\mathrm{cm},
\qquad
L_2=60+7.5=67.5\,\mathrm{cm}.
$$

检验三个独立测量条件：

$$
\begin{aligned}
\sqrt{\frac{L_1}{\Delta l_1}}
&=\sqrt{\frac{64}{4}}=\sqrt{16}=4,\\
\sqrt{\frac{L_2}{\Delta l_2}}
&=\sqrt{\frac{67.5}{7.5}}=\sqrt9=3,\\
\Delta l_2-\Delta l_1
&=7.5-4.0=3.5\,\mathrm{cm}.
\end{aligned}
$$

三式同时成立。两个伸长均为正，第二次比第一次大，符合两半均受拉及端点进一步拉开的条件。

由两个等效劲度还可检验趋势：

$$
\frac{K_{\perp,1}}{K_\parallel}=\frac1{16},
\qquad
\frac{K_{\perp,2}}{K_\parallel}=\frac19.
$$

第二次横向劲度更大、纵向劲度不变，所以横向周期缩短。长度反求不依赖 $m/k$，但两次绝对周期仍依赖 $m/k$；题目没有给出它，不能再编出某个唯一的秒数。

**第12步：检查线性化的边界，不暗中增加“小伸长”假设。**

本题在振动位移 $x,y$ 上取小幅极限，并没有对 $\Delta l/l_0$ 作小量展开。因而求得的公式不要求 $\Delta l\ll l_0$。横向精确力展开到三次为

$$
F_y=-\frac{4k\Delta l}{L}y
-\frac{8kl_0}{L^3}y^3+O(y^5).
$$

若横向振幅为 $A_y$，除几何上 $A_y/L\ll1$ 外，还应使三次力相对一次力足够小：

$$
\frac{2l_0A_y^2}{\Delta l\,L^2}\ll1.
$$

在固定正预伸长下，把振幅取得足够小即可。若让预伸长趋零而振幅不相应缩小，线性化不再均匀有效；不能把 $T_\perp\to\infty$ 理解成任意有限幅横向运动都永远不返回。

量纲上，$k$ 与 $K_\perp$ 都为 $\mathrm{N\,m^{-1}}$，$\Delta l/L$ 是纯数，$\sqrt{m/k}$ 的单位为时间；$n$ 则无量纲。强预拉伸极限 $\Delta l/l_0\to\infty$ 时 $K_\perp\to4k$、$n\to1^+$，两方向趋于同一线性劲度。若变形已超出胡克定律有效范围，便不属于本题假设，不能仅靠这个数学极限推断真实弹簧任意拉长后的性质。

## 六、关键洞察

纵向线性劲度来自两个半弹簧拉力大小的反向变化；横向线性劲度来自已有张力的方向变化。横向的额外拉伸从 $y^2$ 才开始，并不妨碍回复力从 $y$ 开始，因为势能中的预伸长与几何二阶量会形成二次交叉项。

可以在同一个二维势能中同时识别两个模式，而不分两次猜回复力。小球位置为 $(x,y)$ 时，两半真实长度为

$$
\ell_L=\sqrt{(a+x)^2+y^2},
\qquad
\ell_R=\sqrt{(a-x)^2+y^2}.
$$

完整势能为

$$
U(x,y)=k(\ell_L-b)^2+k(\ell_R-b)^2.
$$

其在 $(0,0)$ 附近的二次展开是

$$
U=U_0+\frac12(4k)x^2
+\frac12\left(\frac{4k\Delta l}{L}\right)y^2
+\text{高阶项}.
$$

混合二次项 $xy$ 为零，因为几何和弹性势能分别关于 $x\to-x$、$y\to-y$ 对称；二阶展开不能出现奇于某一坐标的项。两个正二次系数说明正预伸长下平衡稳定，并给出已经求得的两个正交小振动模式。

对一般测量数据 $n_1>n_2>1$、伸长增加 $d>0$，由

$$
\Delta l_1=\frac{l_0}{n_1^2-1},
\qquad
\Delta l_2=\frac{l_0}{n_2^2-1}
$$

相减，不能跳过分母通分：

$$
\begin{aligned}
d
&=l_0\left[\frac1{n_2^2-1}-\frac1{n_1^2-1}\right]\\
&=\frac{l_0(n_1^2-n_2^2)}
{(n_1^2-1)(n_2^2-1)}.
\end{aligned}
$$

因此

$$
\begin{aligned}
l_0&=\frac{d(n_1^2-1)(n_2^2-1)}{n_1^2-n_2^2},\\
\Delta l_1&=\frac{d(n_2^2-1)}{n_1^2-n_2^2},\\
\Delta l_2&=\frac{d(n_1^2-1)}{n_1^2-n_2^2}.
\end{aligned}
$$

正分母和 $n_i>1$ 同时保证三个长度为正。若 $d>0$ 却测得 $n_2\ge n_1$，数据不符合本理想模型；若 $n_1,n_2$ 太接近，分母很小，周期比的小测量误差就会使反求长度有较大误差。它是实验反求的条件性问题，不应靠删去数字或随意四舍五入隐藏。

半根劲度加倍还依赖均匀、左右相同的弹簧。对不均匀弹簧，整根劲度只给出串联柔度；若两半劲度不同，纵向总劲度是两半劲度之和，不能直接等同于 $4k$。因此结构对称与预张力条件都是模型的一部分。

## 七、易错点

把小球在桌面内的横向振动画成竖直升降，会引入不属于本题的重力和悬挂平衡。图4-1的 $x,y$ 都在桌面内；重力与支承力在垂直于桌面的方向抵消。

把半根劲度写成 $k/2$，或者给左右半根各分配 $F/2$，混淆串联与并联。切成一半的均匀弹簧劲度为 $2k$，串联时两半传递相同的力；小球纵向运动时两回复变化又同时作用于小球。

把右移时两半伸长都写成 $\Delta l/2+x$，会误以为力仍抵消。左半增加、右半减少，且净力必须按 $T_R-T_L$ 写出正负号。

认为横向伸长是 $y$，误将斜边增量等于直角边。真实长度为 $\sqrt{a^2+y^2}$；必须先通过几何算长度，再用胡克定律求张力并投影。

因为横向长度变化只有二阶就令横向劲度为零，漏掉预张力方向变化。已有 $T_0$ 乘小角度产生一阶回复力，或由势能交叉项产生二次势能，两种解释一致。

把势能中 $Cy^2$ 的系数 $C$ 直接当劲度，少一个因子二。应比较 $\frac12Ky^2$，或者直接对势能求负导数。

把周期比 $n$ 当频率比，或把 $\sqrt{L/\Delta l}=4$ 写成 $L/\Delta l=4$，都会使反求长度错误。先平方得到 $16$、$9$，再扣除式中的常数一。

把增加的 $\Delta x$ 当作横向振幅，或仅让每半根增加 $\Delta x$，使总伸长的差多出一倍。本题 $\Delta x=\Delta l_2-\Delta l_1$ 是整根端点距离的增量。

把小幅条件偷换成小伸长条件，或在零预伸长时仍使用有限的横向简谐频率。解析不要求 $\Delta l/l_0$ 很小；真正需要控制的是位移及高阶力相对线性力的比例。

## 八、课堂讲解建议

课堂先在图4-1上明确两个方向都在桌面内，让学生区分端点拉开量与小球位移。教师先写 $l_0,L,\Delta l,a,b$ 的长度对应，再讲半根劲度；板书用同一个串联拉力 $F$ 证明 $k_h=2k$，不直接给结论。

纵向讲解时，让学生分别说出左半与右半究竟变长还是变短。教师在图4-3自由体图上先规定 $+x$，再逐行写 $T_R-T_L$。此处保留预张力相消的两项，帮助学生看见纵向劲度为何不随伸长改变。

横向课堂先观察图4-4，要求学生指出长度变化与方向变化各从哪一阶开始。教师以精确斜边与力投影作为主路线，再用能量展开交叉核验；板书特别框出 $\Delta l\cdot y^2$ 的交叉项及 $\frac12K$ 的系数，避免仅背周期公式。

最后课堂用三条件回代检查 $60,4,7.5\,\mathrm{cm}$，并让学生先预测增加预伸长后哪一个周期会变。教师可再讨论零预张力及有限幅变式，说明“小振动”是围绕给定平衡的局部近似，而不是把所有几何长度都当作小量。

## 九、变式训练

**变式1：测得纵向绝对周期后，求劲度和预张力。**

在本题条件下，小球质量 $m=0.050\,\mathrm{kg}$，纵向小振动周期为 $0.250\,\mathrm s$。求整根和半根劲度，两次预张力及两次横向周期。

由 $T_\parallel^2=\pi^2m/k$，得到

$$
\begin{aligned}
k&=\frac{\pi^2m}{T_\parallel^2}
=\frac{\pi^2(0.050)}{(0.250)^2}\\
&=0.8\pi^2\,\mathrm{N\,m^{-1}}
\approx7.8957\,\mathrm{N\,m^{-1}},\\
k_h&=2k\approx15.7914\,\mathrm{N\,m^{-1}}.
\end{aligned}
$$

先把伸长改为米，再求预张力：

$$
\begin{aligned}
T_{0,1}&=k\Delta l_1
=(0.8\pi^2)(0.040)
\approx0.31583\,\mathrm N,\\
T_{0,2}&=k\Delta l_2
=(0.8\pi^2)(0.075)
\approx0.59218\,\mathrm N.
\end{aligned}
$$

相应横向周期为

$$
T_{\perp,1}=4(0.250)=1.000\,\mathrm s,
\qquad
T_{\perp,2}=3(0.250)=0.750\,\mathrm s.
$$

纵向总劲度是 $4k$，不是这里求出的半根劲度 $2k$。把它们再代入 $\sqrt{m/K}$ 可独立复算三个周期。

**变式2：改变周期比的测量数据。**

某同类弹簧第一次周期比为 $6$，增加伸长 $1.1\,\mathrm{cm}$ 后周期比为 $5$。求原长及两个伸长量，并判断三个长度是否满足正值条件。

由平方周期比分别得

$$
\Delta l_1=\frac{l_0}{35},
\qquad
\Delta l_2=\frac{l_0}{24}.
$$

相减并通分：

$$
\begin{aligned}
1.1\,\mathrm{cm}
&=\left(\frac1{24}-\frac1{35}\right)l_0\\
&=\frac{35-24}{840}l_0
=\frac{11}{840}l_0,\\
l_0&=1.1\frac{840}{11}\,\mathrm{cm}
=84\,\mathrm{cm}.
\end{aligned}
$$

所以

$$
\Delta l_1=2.4\,\mathrm{cm},
\qquad
\Delta l_2=3.5\,\mathrm{cm}.
$$

回代 $L_1=86.4\,\mathrm{cm}$、$L_2=87.5\,\mathrm{cm}$，得到 $L_1/\Delta l_1=36$、$L_2/\Delta l_2=25$，取正平方根分别为 $6,5$。三个长度均正，且差为 $1.1\,\mathrm{cm}$，满足测量与几何条件。

<!-- KEEP_TOGETHER_START -->

**变式3：有限横向振幅会怎样改变周期？**

仍采用本题第一次条件，令横向振幅为 $A$。求横向周期的首个非线性修正；再取 $m=0.050\,\mathrm{kg}$、$k=0.8\pi^2\,\mathrm{N\,m^{-1}}$、$A=6.4\,\mathrm{mm}$，估计周期并与精确能量积分比较。

<!-- KEEP_TOGETHER_END -->

将平方根展开到 $y^4$，或者将第7步精确力展开到 $y^3$：

$$
\begin{aligned}
U_\perp-U_0
&=\frac{2k\Delta l}{L}y^2
+\frac{2kl_0}{L^3}y^4+O(y^6),\\
\ddot y+\omega_0^2y+\beta y^3&=0,\\
\omega_0^2&=\frac{4k\Delta l}{mL},
\qquad
\beta=\frac{8kl_0}{mL^3}>0.
\end{aligned}
$$

正三次回复力使振动随振幅增大而变硬。用首阶谐波 $y\simeq A\cos(\omega t)$，并利用

$$
\cos^3u=\frac34\cos u+\frac14\cos3u,
$$

保留基频系数得到

$$
\begin{aligned}
(-\omega^2+\omega_0^2)A
+\frac34\beta A^3&=0,\\
\omega^2&=\omega_0^2+\frac34\beta A^2.
\end{aligned}
$$

三倍频项影响波形，但在这一阶不改变所求基频修正。对频率的平方根与周期的倒数依次作展开：

$$
\begin{aligned}
\omega
&=\omega_0\left(1+\frac{3\beta A^2}{8\omega_0^2}
+O(A^4)\right),\\
\frac{T(A)}{T(0)}
&=1-\frac{3\beta A^2}{8\omega_0^2}+O(A^4)\\
&=\boxed{1-\frac{3l_0A^2}{4\Delta l\,L^2}+O(A^4)}.
\end{aligned}
$$

本例 $l_0=0.60\,\mathrm m$、$\Delta l=0.040\,\mathrm m$、$L=0.640\,\mathrm m$，三次力与一次力的幅值比为

$$
\frac{2(0.60)(0.0064)^2}{(0.040)(0.640)^2}=0.003.
$$

线性周期为 $1.000\,\mathrm s$，首阶相对减量为

$$
\frac{3(0.60)(0.0064)^2}{4(0.040)(0.640)^2}
=0.001125,
\qquad
T(A)\simeq0.998875\,\mathrm s.
$$

还可不作小幅展开，由能量守恒进行独立核验。转折点速度为零，设 $D_A=\sqrt{L^2+4A^2}$、$D_y=\sqrt{L^2+4y^2}$，则

$$
\frac12m\dot y^2=U(A)-U(y).
$$

用平方差分解势能差，避免直接相减两相近数：

$$
\begin{aligned}
U(A)-U(y)
&=\frac k2(D_A-D_y)(D_A+D_y-2l_0),\\
D_A-D_y
&=\frac{D_A^2-D_y^2}{D_A+D_y}
=\frac{4(A^2-y^2)}{D_A+D_y},\\
U(A)-U(y)
&=2k(A^2-y^2)
\frac{D_A+D_y-2l_0}{D_A+D_y}.
\end{aligned}
$$

四分之一周期由平衡点积分到转折点，令 $y=A\sin\psi$ 消去端点的平方根因子：

$$
\begin{aligned}
T(A)
&=4\sqrt{\frac m2}
\int_0^A\frac{\mathrm dy}{\sqrt{U(A)-U(y)}}\\
&=2\sqrt{\frac mk}
\int_0^{\pi/2}
\sqrt{\frac{D_A+\sqrt{L^2+4A^2\sin^2\psi}}
{D_A+\sqrt{L^2+4A^2\sin^2\psi}-2l_0}}
\,\mathrm d\psi.
\end{aligned}
$$

代入数值，精确几何模型给 $T(A)\approx0.99887728\,\mathrm s$，直接用两半弹簧矢量力积分运动方程也得到同值。首阶近似差约 $2.28\times10^{-6}\,\mathrm s$；因此给定振幅下近似良好，但周期已不严格等于小幅极限值。

**变式4：完全没有预伸长时，横向还能振动吗？**

令 $\Delta l=0$，保留对称横向运动，问平衡点附近的回复力和势能从哪一阶开始，并求小而有限振幅 $A$ 下周期的主阶关系。这里只讨论横向模式，不将零预拉伸直接套入两半始终受拉的纵向模型。

此时 $L=l_0$，平方根展开为

$$
\sqrt{l_0^2+4y^2}-l_0
=\frac{2y^2}{l_0}+O(y^4).
$$

平方后，

$$
\begin{aligned}
U_\perp
&=\frac k2\left(\frac{2y^2}{l_0}+O(y^4)\right)^2
=\frac{2k}{l_0^2}y^4+O(y^6),\\
F_y&=-\frac{\mathrm dU_\perp}{\mathrm dy}
=-\frac{8k}{l_0^2}y^3+O(y^5).
\end{aligned}
$$

二次势能和一次回复力都为零，但离开平衡点后两半都会拉长，仍产生三次回复力。故它是非线性振动，不是具有非零线性角频率的简谐运动。

<!-- KEEP_TOGETHER_START -->

保留四次势能并在振幅 $A$ 处写总能量：

$$
\begin{aligned}
\frac12m\dot y^2
&=\frac{2k}{l_0^2}(A^4-y^4),\\
|\dot y|
&=\frac{2}{l_0}\sqrt{\frac km}\sqrt{A^4-y^4}.
\end{aligned}
$$

利用对称性，周期为四倍从平衡点到转折点的时间；令 $y=Au$：

$$
\begin{aligned}
T(A)
&\simeq2l_0\sqrt{\frac mk}
\int_0^A\frac{\mathrm dy}{\sqrt{A^4-y^4}}\\
&=\frac{2l_0}{A}\sqrt{\frac mk}
\int_0^1\frac{\mathrm du}{\sqrt{1-u^4}}\\
&\approx\boxed{\frac{2.62205755\,l_0}{A}\sqrt{\frac mk}}.
\end{aligned}
$$

<!-- KEEP_TOGETHER_END -->

积分为 $1.311028777$，其端点虽有可积平方根奇点，积分值有限。$T$ 随振幅按 $1/A$ 增大，说明 $A\to0$ 时周期趋无穷；对任何给定的小正振幅，周期仍有限。

例如 $l_0=0.60\,\mathrm m$、$k=8.0\,\mathrm{N\,m^{-1}}$、$m=0.050\,\mathrm{kg}$、$A=3.0\,\mathrm{mm}$，主阶周期为 $41.4584\,\mathrm s$；用原几何精确力积分得到 $41.4596\,\mathrm s$。这一理想数值忽略阻尼，并非宣称真实桌面实验能在极小预张力下无损振动；它用来说明正预伸长的线性极限与零预伸长的四次势能模型不能混用。

<!-- question-complete -->
