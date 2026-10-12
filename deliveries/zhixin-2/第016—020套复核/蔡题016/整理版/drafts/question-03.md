# 第3题

<!-- question-start -->

如图3-1所示，有一个光滑的固定圆锥，顶角为 $2\theta$，其轴线竖直。用光滑、轻质、柔软且不可伸长的绳子绕在锥面上，连接两个质量均为 $m$ 的重物 $A$、$B$。重力加速度为 $g$。求图示静力平衡时各段绳子的张力。

（1）采用一个绳套连接两个重物，如图3-1左图所示。

（2）采用两根绳子，每根绳子的一个端点设有轻环；两根绳子分别穿过对方端点的环，再连接重物，如图3-1右图所示。

题干修订：两个重物保持与光滑锥面接触，可以在锥面上滑动；第（2）问连接重物的末段绳沿锥面母线，端点轻环光滑且质量忽略。绳与环均无摩擦。讨论绳绷紧、连接点位于锥面内部而未触及顶点或下缘的平衡，不把重物改为自由悬空模型。

![图3-1 绳套连接与交叉过环连接的锥面空间绳路。](../figures/question-03.png){width=88%}

<!-- question-end -->

## 一、题型定位

本题属于光滑曲面上的绳系静力平衡。先求绳在圆锥侧面上的真实形状，确定端点拉力方向，再列竖直方向的平衡式。圆锥顶角决定锥面展开角；展开后的直绳方向，又决定张力沿母线的分量。三维空间角、绕轴的方位角和展开面的平面角必须分开。

两种连接不能用同一个受力图替代。第（1）问的连接点承受重力与两条绳弧的拉力。第（2）问的轻环不承受重物的重力，而是承受两条锥面绳弧和一条下行尾段的三股拉力；自由端重物的受力另列。第（2）问还必须先判断平衡是否存在，不能把一个张力表达式当成任意锥角下都能成立的答案。

## 二、知识点

圆锥的母线、水平截面半径和竖直高度；曲面等距展开；光滑轻绳的恒定张力；绳端拉力沿实际绳路切线；力在切平面、母线和法线方向的分解；光滑轻环上的过绳与张力连续；静力平衡的研究对象选择；余弦定理及半角公式；微分与虚功；绳长约束；三角方程的分支筛选；接触反力的非负条件和边界条件。

圆锥顶角为 $2\theta$，故母线与竖直轴的夹角为 $\theta$，取 $0<\theta<\pi/2$。在绳端对称几何中，定义两条相对母线展开后的夹角

$$
\alpha=\pi\sin\theta,\qquad
\beta=\frac{\alpha}{2}.
$$

因此 $0<\alpha<\pi$、$0<\beta<\pi/2$。$\alpha$ 不是 $2\theta$，$\beta$ 也不是重力与母线之间的夹角。质量为零的环不能提供额外切向支承力；圆锥对贴面物体的支承力只能沿法线。两根绳的总长度没有规定相等，后面用 $L_A$、$L_B$ 分别表示，不额外加上等长条件。

## 三、物理图像

圆锥尖顶记为 $O$。由顶点沿母线向下的距离记为 $r$。该点到轴线的水平距离是 $r\sin\theta$，低于顶点的竖直距离是 $r\cos\theta$。图3-1上的曲绳不是水平纬圆：半圈绳的中间部分更接近顶点，映回空间后也更高。后侧虚线表示遮挡的同一根绳，而不是断开的绳端。

第（1）问采用两个连接点位于相对母线上的对称平衡构型。每个连接点的两侧绳弧向上拉，它们绕轴方向的分量相互抵消，沿上行母线的分量相加。重物受到的重力只有 $mg\cos\theta$ 沿母线向下，其余法向分量由锥面支承力抵消。

第（2）问将两只轻环记为 $P$、$Q$。通过 $P$ 后连接重物 $A$ 的连续绳，其张力记为 $T_A$；通过 $Q$ 后连接重物 $B$ 的连续绳，其张力记为 $T_B$。在 $P$ 处，一条锥面弧属于绳 $A$，另一条属于绳 $B$，尾段属于绳 $A$；在 $Q$ 处则互换。绳在图中视觉交会，不等于增加了一个绳结，真正改变绳路的只有固定端和轻环。

## 四、解题入口

先沿母线把圆锥侧面剪开并展开，利用同一水平圆周在展开前后的弧长相同，求出相对母线的展开夹角 $\alpha$。再把一段半圈绳化成展开面内的直线弦，求弦长以及弦与母线的夹角。这个几何结果随后进入两种连接各自的母线方向力平衡。

第（1）问在重物上列式。第（2）问先在末端重物上求 $T_A$、$T_B$，再在两个轻环上列三股拉力的平衡式，筛选允许的 $\theta$。最后保留势能路线作独立核对：绳长减少的量不等于竖直下降量，必须先算母线距离，再乘 $\cos\theta$。这条路线同时检查负号和两根绳的长度口径。

## 五、解析

<!-- KEEP_TOGETHER_START -->

**第1步：说明轻绳张力与曲面绳路的关系。**

绳子质量忽略，取没有外加集中力的一小段绳。它两端的张力和锥面的支承力必须平衡。锥面光滑，支承力垂直于锥面，不提供沿绳的切向摩擦；所以同一根连续绳在经过光滑锥面和光滑环后，张力大小保持不变。

<!-- KEEP_TOGETHER_END -->

张力恒定不意味着绳在空间中处处沿同一方向。绳会沿锥面转弯，支承力改变张力方向，而不改变其大小。将锥面等距展开后，绳路在平面内没有使其转弯的切向力，因而成为直线。这个结论只适用于两个集中连接点之间的绷紧绳段，不把整个含重物或过环转折的绳系画成一根无拐点直线。

绳在空间中必须贴着锥面；展开后的直弦是用来求曲面上的距离和端点切线，不能将平面直弦直接画成穿过锥体内部的空间直绳。

**第2步：由弧长不变求展开角。**

取距顶点母线距离为 $x$ 的水平圆周。它的水平半径为

$$
R=x\sin\theta.
$$

整个圆周长为 $2\pi R=2\pi x\sin\theta$。展开后它成为半径为 $x$ 的扇形圆弧。若整个扇形的圆心角为 $\Omega$，弧长是 $x\Omega$，于是

$$
\begin{aligned}
x\Omega&=2\pi x\sin\theta,\\
\Omega&=2\pi\sin\theta.
\end{aligned}
$$

相对母线在空间中绕轴相差半圈，即方位差为 $\pi$。它对应展开扇形的一半，故

$$
\boxed{\alpha=\frac{\Omega}{2}=\pi\sin\theta.}
$$

如图3-2所示，空间母线角 $\theta$ 决定水平半径 $R$，圆周弧长再决定展开角 $\alpha$。这两次几何变换不能合并成“展开角等于顶角”。

![图3-2 母线距离、水平半径与半圈锥面展开角。](../figures/unfold-03.png){width=78%}

图中用于弧长换算的是半径 $x$ 的参考圆弧，实际绳段是内部的直弦 $PQ$。参考圆弧长度为 $\pi x\sin\theta=x\alpha$，并不是实际半圈绳长。

**第3步：求半圈绳长和端点张力方向。**

在展开面内，两个等高连接点满足 $OP=OQ=x$、$\angle POQ=\alpha=2\beta$。由余弦定理，实际半圈绳长 $d$ 满足

$$
\begin{aligned}
d^2
&=x^2+x^2-2x^2\cos(2\beta)\\
&=2x^2[1-\cos(2\beta)]\\
&=2x^2\cdot2\sin^2\beta\\
&=4x^2\sin^2\beta.
\end{aligned}
$$

此处使用半角恒等式 $1-\cos(2\beta)=2\sin^2\beta$。因为 $x>0$、$\sin\beta>0$，取正长度根，得到

$$
\boxed{d=2x\sin\beta.}
$$

等腰三角形 $OPQ$ 的两底角相同，故

$$
\angle OPQ=\angle OQP
=\frac{\pi-2\beta}{2}
=\frac{\pi}{2}-\beta.
$$

在 $P$ 点，拉力沿 $P\to Q$ 的绳切线，而上行母线是 $P\to O$。两者夹角为 $\pi/2-\beta$，所以单股张力沿上行母线的分量为

$$
T\cos\left(\frac{\pi}{2}-\beta\right)=T\sin\beta.
$$

另一侧半圈绳的母线分量也是 $T\sin\beta$，绕轴分量却相反。因此两股绳的合力为沿上行母线的 $2T\sin\beta$。这里应当使用 $\sin\beta$，不是 $\sin\theta$ 或 $\cos\beta$。

**第4步：建立重物所在点的切向、法向受力图。**

取沿母线向下的单位矢量为 $\boldsymbol e_r$，绕轴正方向的单位矢量为 $\boldsymbol e_\varphi$，锥面朝外法向为 $\boldsymbol n$，竖直向上的单位矢量为 $\boldsymbol e_z$。重力在母线方向的分量是向下的 $mg\cos\theta$，在法向的分量是向内的 $mg\sin\theta$。

将端点处锥面切平面单独展开，得到图3-3。左侧两根蓝色箭头是绳切线，红色箭头只表示重力在切平面内的投影；右侧子图才是实际空间的重力与支承力分解。不能在同一个平面投影图中把重力全矢量和它的切向分量重复算作两股力。

![图3-3 两股绳的母线合力与重物重力的切向、法向分解。](../figures/forces-03.png){width=72%}

按图3-3的方向，两个绳端单位切线可以写成

$$
\begin{aligned}
\boldsymbol t_+
&=-\sin\beta\,\boldsymbol e_r
+\cos\beta\,\boldsymbol e_\varphi,\\
\boldsymbol t_-
&=-\sin\beta\,\boldsymbol e_r
-\cos\beta\,\boldsymbol e_\varphi.
\end{aligned}
$$

相加时 $\boldsymbol e_\varphi$ 的系数抵消，而 $\boldsymbol e_r$ 的系数都是负值，表示沿母线向上。重力分解为

$$
-mg\boldsymbol e_z
=mg\cos\theta\,\boldsymbol e_r
-mg\sin\theta\,\boldsymbol n.
$$

后面的每个力平衡式都采用这组同一方向约定。

**第5步：完成第（1）问的张力和接触检查。**

对质量为 $m$ 的一个重物列母线方向平衡式。两股绳向上，重力切向分量向下，故

$$
\begin{aligned}
-2T\sin\beta+mg\cos\theta&=0,\\
2T\sin\beta&=mg\cos\theta,\\
T&=\frac{mg\cos\theta}{2\sin\beta}.
\end{aligned}
$$

代入 $\beta=\pi\sin\theta/2$，第（1）问为

$$
\boxed{
T_{(1)}
=\frac{mg\cos\theta}
{2\sin\!\left(\dfrac{\pi\sin\theta}{2}\right)}.
}
$$

两股绳都沿锥面切线，对该点没有法向分量，因此法向平衡为

$$
N-mg\sin\theta=0,\qquad
\boxed{N=mg\sin\theta>0.}
$$

支承力为正，说明圆锥是在向外推物体，这符合接触力只能推不能拉的性质。另一重物由于质量相同、几何对称，得到相同张力和支承力。

也可用完整矢量检查，而不另加新的力：

$$
\begin{aligned}
\boldsymbol F_{\rm total}
&=T(\boldsymbol t_++\boldsymbol t_-)
-mg\boldsymbol e_z+N\boldsymbol n\\
&=(-2T\sin\beta+mg\cos\theta)\boldsymbol e_r
+(N-mg\sin\theta)\boldsymbol n\\
&=\boldsymbol0.
\end{aligned}
$$

**第6步：把第一问绳长与张力的作用分开。**

若整个绳套长度为 $S$，两条半圈弧长度都是 $d$，所以

$$
\begin{aligned}
S&=2d=4x\sin\beta,\\
x&=\frac{S}{4\sin\beta}.
\end{aligned}
$$

给定绳长主要确定平衡构型的尺度 $x$，张力由角度和质量确定。将 $S$ 增大，只会把相似绳路整体向下放大；在不触及下缘的范围内，并不改变端点绳与母线的夹角，所以不改变上述张力。

这不是说“任何绳长都无条件可用”。若有限圆锥的母线长为 $H$，应满足 $x<H$，即

$$
S<4H\sin\beta.
$$

顶点与下缘都被排除在本题的内部平衡之外。还应有正的绳张力，不能把 $\theta=\pi/2$ 的退化平面直接作为有张力的锥面绳系。

**第7步：第（2）问先在重物上确定每根连续绳的张力。**

第（2）问每个重物只由一个沿母线的末段绳向上拉，另受重力和锥面支承力。取重物 $A$：

$$
\begin{aligned}
-T_A+mg\cos\theta&=0,\\
N_A-mg\sin\theta&=0.
\end{aligned}
$$

因此

$$
T_A=mg\cos\theta,\qquad
N_A=mg\sin\theta.
$$

同理，重物 $B$ 满足

$$
T_B=mg\cos\theta,\qquad
N_B=mg\sin\theta.
$$

因为两重物质量相同，得到 $T_A=T_B\equiv T$；因为每根绳经光滑轻环无摩擦通过，尾段和相应半圈绳弧的张力大小相同。这里的结论来自重物沿母线的平衡，而不是直接把 $T$ 写成 $mg$。

如图3-4所示，同一颜色表示同一根连续绳。一个固定端、一个过环处和一个重物端之间的连接顺序必须读清；图中的第三股下行拉力不能漏掉。

![图3-4 两根连续绳的固定端、过环位置及轻环三股拉力。](../figures/rings-03.png){width=86%}

**第8步：在轻环上列三股拉力的平衡式。**

取轻环 $P$。两条锥面绳弧向上母线的分量分别为 $T_A\sin\beta$、$T_B\sin\beta$；通过 $P$ 后的尾段沿母线向下，拉力为 $T_A$。轻环自身没有质量，也没有沿锥面方向的外加支承，故

$$
(T_A+T_B)\sin\beta-T_A=0.
$$

轻环 $Q$ 的下行尾段属于另一根绳，因而

$$
(T_A+T_B)\sin\beta-T_B=0.
$$

将 $T_A=T_B=T>0$ 代入，两式都成为

$$
2T\sin\beta-T=0.
$$

这里没有重力项 $mg$，因为研究对象是质量忽略的轻环，不是重物。重物的重力已经通过尾段张力作用到环上，再补一个 $mg$ 会把同一作用重复计算。

<!-- KEEP_TOGETHER_START -->

**第9步：筛选锥角，得到第（2）问的存在条件。**

由 $T>0$ 可以约去张力：

$$
\begin{aligned}
2\sin\beta&=1,\\
\sin\beta&=\frac12.
\end{aligned}
$$

<!-- KEEP_TOGETHER_END -->

本题已有 $0<\beta<\pi/2$，在这一范围内 $\sin\beta$ 严格增加。因此只保留

$$
\begin{aligned}
\beta&=\frac{\pi}{6},\\
\alpha&=2\beta=\frac{\pi}{3},\\
\pi\sin\theta&=\frac{\pi}{3},\\
\sin\theta&=\frac13.
\end{aligned}
$$

不能取 $5\pi/6$，因为它超出了展开半角的允许范围；也不能在解三角方程时加上任意整数周，使绳额外绕圈。题目给定的是图示的一圈连接拓扑。

随后计算

$$
\begin{aligned}
\cos\theta
&=\sqrt{1-\sin^2\theta}\\
&=\sqrt{1-\frac19}\\
&=\sqrt{\frac89}
=\frac{2\sqrt2}{3}.
\end{aligned}
$$

取正根是因为 $0<\theta<\pi/2$。所以

$$
\boxed{
T_{(2)}=\frac{2\sqrt2}{3}mg,
\qquad
\theta=\arcsin\frac13.
}
$$

第（2）问的张力不是一般 $\theta$ 的表达式。若 $\sin\theta\ne1/3$，则尾段已规定的张力无法同时使两轻环平衡，图示内部静止构型不存在。

**第10步：补出两个轻环等高的几何依据。**

上面的对称图用两个轻环到顶点距离都为 $x$。为核对这不是任意省略一个位置变量，先把两相对母线上的距离分别写成 $a$、$b$。一条半圈绳展开后的弦长为

$$
d=\sqrt{a^2+b^2-2ab\cos\alpha}.
$$

如图3-5，弦从 $P$ 指向 $Q$ 的方向在 $P$ 的上行母线上的投影系数为 $c_P$，在 $Q$ 的上行母线上的投影系数为 $c_Q$。把平面坐标选成 $P=(a,0)$、$Q=(b\cos\alpha,b\sin\alpha)$，由端点位移直接计算：

$$
\begin{aligned}
c_P
&=\frac{a-b\cos\alpha}{d},\\
c_Q
&=\frac{b-a\cos\alpha}{d}.
\end{aligned}
$$

![图3-5 不同母线距离的两个端点及弦方向投影。](../figures/asymmetric-03.png){width=40%}

两股半圈绳的张力都为 $T$，两条尾段张力也为 $T$。两个轻环分别要求

$$
2Tc_P=T,\qquad 2Tc_Q=T.
$$

于是 $c_P=c_Q=1/2$。两系数相减：

$$
\begin{aligned}
c_P-c_Q
&=\frac{a-b\cos\alpha-b+a\cos\alpha}{d}\\
&=\frac{(a-b)(1+\cos\alpha)}{d}
=0.
\end{aligned}
$$

由于 $d>0$，且 $0<\alpha<\pi$ 给出 $1+\cos\alpha>0$，只能有 $a=b$。因此两个轻环等高是力平衡所要求的结果；回代 $a=b=x$，才恢复 $c_P=c_Q=\sin(\alpha/2)$。

两重物的高度却不必相同，因为两根绳未必等长。不要把“两个轻环等高”误扩大成“两个末端重物也一定等高”。

**第11步：沿势能路线展开两根绳的完整长度约束。**

分别用 $L_A$、$L_B$ 表示通过 $P$、$Q$ 并连接重物 $A$、$B$ 的两根绳总长度。每根连续绳都含一段半圈弧，其长度为 $d=2x\sin\beta$。因此末段母线绳长为

$$
\ell_A=L_A-d,\qquad \ell_B=L_B-d.
$$

重物 $A$ 从顶点到轻环 $P$ 已走母线距离 $x$，再沿同一母线向下走 $\ell_A$；重物 $B$ 同理。所以它们到顶点的母线距离为

$$
\begin{aligned}
r_A&=x+\ell_A=x+L_A-d,\\
r_B&=x+\ell_B=x+L_B-d.
\end{aligned}
$$

竖直坐标不能直接用 $r_A$、$r_B$，而必须为

$$
z_A=-r_A\cos\theta,\qquad
z_B=-r_B\cos\theta.
$$

以顶点水平面为重力势能零面，总势能是两重物相加：

$$
\begin{aligned}
U
&=mgz_A+mgz_B\\
&=-mg\cos\theta[(x+L_A-d)+(x+L_B-d)]\\
&=-mg\cos\theta(2x+L_A+L_B-2d)\\
&=-mg\cos\theta[2x+L_A+L_B-4x\sin\beta].
\end{aligned}
$$

此处先保持两个独立绳长，再将它们并入常数项；因此没有偷偷使用等长条件，也没有漏计第二个重物。若恰好 $L_A=L_B=L$，才可化为

$$
U=-2mg\cos\theta[x+L-2x\sin\beta].
$$

这个形式中的因子 $2$ 对应两个等质量重物，不是弦长的另一个因子 $2$。

**第12步：从允许的虚位移求平衡，核对重力势能的符号。**

两轻环沿各自母线同时下移小量 $\mathrm dx$，保持 $\theta$、$L_A$、$L_B$ 不变。圆锥是相似曲面，弦长变化为

$$
\mathrm dd=2\sin\beta\,\mathrm dx.
$$

因此两末段绳各缩短 $\mathrm dd$，每个重物的母线位移为

$$
\begin{aligned}
\mathrm dr_A
&=\mathrm dx-\mathrm dd
=(1-2\sin\beta)\mathrm dx,\\
\mathrm dr_B
&=(1-2\sin\beta)\mathrm dx.
\end{aligned}
$$

这里用的是绳长微分，不是令重物和轻环始终移动相同距离。将其转成竖直位移，得 $\mathrm dz_i=-\cos\theta\,\mathrm dr_i$。于是

$$
\begin{aligned}
\mathrm dU
&=mg(\mathrm dz_A+\mathrm dz_B)\\
&=-2mg\cos\theta(1-2\sin\beta)\,\mathrm dx,\\
\frac{\mathrm dU}{\mathrm dx}
&=-2mg\cos\theta(1-2\sin\beta).
\end{aligned}
$$

在没有端点限位、摩擦或其他切向外力的内部平衡中，允许的正负虚位移均不能产生一阶势能变化，所以 $\mathrm dU/\mathrm dx=0$。因为 $m>0$、$g>0$、$\cos\theta>0$，再次得到 $2\sin\beta=1$，与轻环三股拉力法完全相同。

负号还有直接物理解释。若 $2\sin\beta<1$，轻环下移时重物也下移，重力势能降低，原构型不可能静止；若 $2\sin\beta>1$，轻环下移反而使重物上移，势能增加。仅当二者恰好抵消时，这种尺度方向的虚位移才无一阶势能代价。

**第13步：检查接触、尺度、量纲与最终答案。**

临界角下 $d=x$，故

$$
\ell_A=L_A-x,\quad \ell_B=L_B-x,\qquad
r_A=L_A,\quad r_B=L_B.
$$

要有两条正长度尾段，须 $0<x<\min(L_A,L_B)$。如果有限圆锥母线长为 $H$，还须 $\max(L_A,L_B)<H$，使两个末端重物仍在侧面内部。两环的尺度 $x$ 在这个范围内不是唯一的；只有锥角和张力被平衡条件确定，不能从未给出的绳长编造一个数值位置。

第（2）问每个重物的支承力为

$$
N_A=N_B=mg\sin\theta=\frac{mg}{3}>0.
$$

轻环的三股拉力都在锥面切平面内，平衡后无需法向力，所以轻环自身的支承力为零。它和重物的 $mg/3$ 是不同研究对象的反力，不能相互移用。

<!-- KEEP_STUDENT_START -->

两张力式都是 $mg$ 乘无量纲角函数，量纲为力。第（1）问在细锥极限 $\theta\to0$ 时，

$$
\begin{aligned}
\sin\theta&\sim\theta,\\
\sin\left(\frac{\pi\sin\theta}{2}\right)&\sim\frac{\pi\theta}{2},\\
T_{(1)}&\sim\frac{mg}{\pi\theta}.
\end{aligned}
$$

两根绳越来越接近绕轴方向，能用于向上母线支承的分量越来越小，因此张力增大，符合受力图像。$\theta\to\pi/2$ 时重力沿母线的分量趋零，公式给出张力趋零；这是几何退化的极限检验，不是把退化端点纳入正常绷紧平衡。

最终，第（1）问按允许的图示对称构型，

$$
\boxed{
T_{(1)}
=\frac{mg\cos\theta}
{2\sin\!\left(\dfrac{\pi\sin\theta}{2}\right)}.
}
$$

第（2）问只有在 $\sin\theta=1/3$ 时具有上述内部静力平衡，此时各段连续绳的张力均为

$$
\boxed{T_A=T_B=\frac{2\sqrt2}{3}mg.}
$$

势能沿尺度方向无变化仅说明这一方向中性，不保证所有扰动都稳定；若将“能静止”进一步讨论成“稳定平衡”，还须检查允许的环向扰动。

<!-- KEEP_STUDENT_END -->

## 六、关键洞察

**曲面展开保留的是内在距离和切线夹角，不是空间中的直线。**

可以从三维参数式独立验证展开。取

$$
\boldsymbol R(r,\varphi)
=\bigl(r\sin\theta\cos\varphi,\,
r\sin\theta\sin\varphi,\,-r\cos\theta\bigr).
$$

对两个参数分别求导：

$$
\begin{aligned}
\boldsymbol R_r
&=(\sin\theta\cos\varphi,\sin\theta\sin\varphi,-\cos\theta),\\
\boldsymbol R_\varphi
&=(-r\sin\theta\sin\varphi,r\sin\theta\cos\varphi,0).
\end{aligned}
$$

利用 $\sin^2\varphi+\cos^2\varphi=1$，有

$$
\boldsymbol R_r^2=1,\qquad
\boldsymbol R_r\cdot\boldsymbol R_\varphi=0,\qquad
\boldsymbol R_\varphi^2=r^2\sin^2\theta.
$$

所以曲面线元为

$$
\mathrm d\ell^2
=\mathrm dr^2+r^2\sin^2\theta\,\mathrm d\varphi^2.
$$

令 $\psi=\sin\theta\,\varphi$，则

$$
\mathrm d\ell^2=\mathrm dr^2+r^2\,\mathrm d\psi^2,
$$

恰好是平面极坐标的线元。将 $(r,\psi)$ 映到 $(r\cos\psi,r\sin\psi)$，才能把曲面绳路变成平面直线。这里没有把圆锥当平面，而是先证明该展开保留弧长。

以半圈绳的中间方位为 $\varphi_{\rm c}$，展开弦到顶点的最短距离为 $h=x\cos\beta$。直线弦在平面极坐标中的方程是 $r\cos(\psi-\psi_{\rm c})=h$，故空间绳路满足

$$
r(\varphi)
=\frac{x\cos\beta}
{\cos[\sin\theta(\varphi-\varphi_{\rm c})]}.
$$

绳两端 $\varphi-\varphi_{\rm c}=\pm\pi/2$，分母为 $\cos\beta$，恢复 $r=x$；绳中部 $\varphi=\varphi_{\rm c}$，得到 $r=x\cos\beta<x$。因此绳中部相对两端抬高

$$
\Delta z=x(1-\cos\beta)\cos\theta>0.
$$

这就是图3-1必须画成高低变化空间曲线的理由，水平圆圈无法提供同一个受力夹角。

**接触是否成立，还可从绳微元法向力独立检查。**

以实际弧长 $\ell$ 为参数，绳单位切线为 $\boldsymbol t=\mathrm d\boldsymbol R/\mathrm d\ell$。因为展开弦的平面角动量为 $r^2\,\mathrm d\psi/\mathrm d\ell=h$，有

$$
\frac{\mathrm d\varphi}{\mathrm d\ell}
=\frac{h}{r^2\sin\theta}.
$$

圆锥的母线方向法曲率为零，环向的法曲率为 $-\cot\theta/r$。直接对三维切线求导也给出相同法向分量：

$$
\boldsymbol n\cdot\frac{\mathrm d\boldsymbol t}{\mathrm d\ell}
=-r\sin\theta\cos\theta
\left(\frac{\mathrm d\varphi}{\mathrm d\ell}\right)^2
=-\frac{\cos\theta\,h^2}{\sin\theta\,r^3}<0.
$$

轻绳微元平衡为 $T\,\mathrm d\boldsymbol t/\mathrm d\ell+q_n\boldsymbol n=\boldsymbol0$，其中 $q_n$ 是锥面对绳每单位弧长的反力。因此

$$
q_n
=\frac{T\cos\theta\,h^2}{\sin\theta\,r^3}>0.
$$

这个正号说明实体锥面确实可以由内向外支承绳，不需要虚构吸附力。$q_n$ 的量纲为力每长度；重物支承力 $N$ 的量纲为力，二者不能混为一项。

**可以通过长度偏导求绳端投影，而不必记忆一张角度图。**

一般端点弦长为 $d(a,b,\alpha)=\sqrt{a^2+b^2-2ab\cos\alpha}$。固定另一端与展开角，对 $a$ 求导：

$$
\begin{aligned}
\frac{\partial d}{\partial a}
&=\frac{1}{2d}(2a-2b\cos\alpha)
=\frac{a-b\cos\alpha}{d}=c_P,\\
\frac{\partial d}{\partial b}
&=\frac{b-a\cos\alpha}{d}=c_Q.
\end{aligned}
$$

端点向下母线位移 $\mathrm da$ 会增加绳长 $c_P\,\mathrm da$，所以绳张力对该位移作功 $-Tc_P\,\mathrm da$。长度偏导与绳端力投影是同一个虚功关系。这也解释为何用势能与用轻环三股力求出的临界角必须相同。

<!-- KEEP_TOGETHER_START -->

**相对母线的对称性也可以由平衡推出。**

暂令两个环方位差为 $\delta$，两侧弧分别展开成夹角

$$
\alpha_1=\delta\sin\theta,\qquad
\alpha_2=(2\pi-\delta)\sin\theta.
$$

<!-- KEEP_TOGETHER_END -->

两条弧都不经过尖顶、能展开成普通直弦时，取 $0<\alpha_1,\alpha_2<\pi$。各弦长度为 $d_1,d_2$。由于等质量末端给出相同张力，两环母线平衡相减，得到

$$
T(a-b)\left[
\frac{1+\cos\alpha_1}{d_1}
+\frac{1+\cos\alpha_2}{d_2}
\right]=0.
$$

方括号严格为正，因此 $a=b=x$。此时两条弦的端点母线分量是 $\sin(\alpha_i/2)$，环向分量大小是 $\cos(\alpha_i/2)$，方向相反。环向平衡给

$$
\cos\frac{\alpha_1}{2}
=\cos\frac{\alpha_2}{2}.
$$

两个半角都在 $(0,\pi/2)$，余弦严格下降，所以 $\alpha_1=\alpha_2$，从而 $\delta=\pi$。图示相对母线、等高轻环的对称构型并不是单靠观察就假定的；它与允许的两段测地线和全切向平衡一致。

**静力平衡存在、尺度中性与稳定性是三个不同结论。**

第（2）问临界角时，总势能与 $x$ 无关，故允许尺度方向存在一族平衡。现在保持两环等高，令其方位差变成 $\delta=\pi+\varepsilon$。两个展开夹角为 $\alpha\pm\varepsilon\sin\theta$，两条弧总长

$$
\begin{aligned}
D(\varepsilon)
&=2x\sin\left(\beta+\frac{\varepsilon\sin\theta}{2}\right)
+2x\sin\left(\beta-\frac{\varepsilon\sin\theta}{2}\right)\\
&=4x\sin\beta\cos\left(\frac{\varepsilon\sin\theta}{2}\right).
\end{aligned}
$$

此处使用和差化积，而不是把两段长度误写成同一段。两重物总母线距离为 $2x+L_A+L_B-D$，因而

$$
U(\varepsilon)-U(0)
=mg\cos\theta[D(\varepsilon)-D(0)].
$$

利用 $\cos u=1-u^2/2+O(u^4)$，得到

$$
\begin{aligned}
\Delta U
&=-\frac{mg\cos\theta}{2}
x\sin\beta\,\sin^2\theta\,\varepsilon^2+O(\varepsilon^4)\\
&=-\frac{mg\cos\theta}{36}x\varepsilon^2+O(\varepsilon^4)<0
\end{aligned}
$$

最后一行代入临界角 $\sin\theta=1/3$、$\sin\beta=1/2$。存在能降低势能的允许环向小扰动，所以不额外限制方位时，该静止构型环向不稳定。仅在图中写“平衡”是正确的，写成“稳定平衡”则没有依据。

## 七、易错点

**把圆锥顶角当展开角。** 顶角 $2\theta$ 是空间母线角；展开全扇角是 $2\pi\sin\theta$，半圈展开角是 $\pi\sin\theta$。最可靠的检查是回到 $x\Omega=2\pi x\sin\theta$，确保两边使用同一参考圆周。

**把参考圆弧当实际绳长。** 同高度圆弧长度 $\pi x\sin\theta$ 只用于确定展开角；实际绳弦长度为 $2x\sin(\pi\sin\theta/2)$。绳中部会上升，不应在空间图中画水平纬圈，更不能把展开弦放进锥体内部。

**张力分量用错三角函数。** 绳与上行母线夹角为 $\pi/2-\beta$，所以沿母线为 $T\sin\beta$。$T\cos\beta$ 是环向分量，两股相互抵消。$\theta$ 则用于重力投影，不能用它代替绳端角。

**在第（2）问的轻环上再次加入重力。** 重物和环不是一个研究对象。重物确定尾段 $T=mg\cos\theta$；环上的下行力已经是该尾段张力，再列重物重力会重复。环上有三股绳力，不是只看见两条弧便漏掉尾段。

**把接触重物改成自由悬挂。** 自由悬空、静止重物只受重力和单根绳力时必有 $T=mg$；本题已注明锥面接触，法向反力抵消重力的法向分量，母线张力才是 $mg\cos\theta$。从实体圆锥侧面直接向下画竖直尾绳还会进入锥体，不能用一根错误连线掩盖模型改变。

**认为两根不同绳必定有不同张力，或必定等长。** 本题张力相同来自两末端质量相同和同一锥角，而不是来自绳长相同。$L_A\ne L_B$ 时两环仍可等高，重物却在不同高度；两根绳必须分别写长度约束。

**只给张力而不检查存在条件。** 第（2）问首先要求 $2T\sin\beta=T$，在给定锥角不满足 $\sin\theta=1/3$ 时，不存在图示内部平衡。不能在一般锥角下照搬第（1）问的表达式作为第二问答案。

**求导漏掉两重物或写错势能负号。** 母线距离增加意味着竖直坐标 $z=-r\cos\theta$ 减小，重力势能降低。总势能应为 $mgz_A+mgz_B$；即便少一个整体常数因子没有改变驻点，也不能在完整能量式里省略一个物体。

**把轻环、重物和绳微元的支承反力混用。** 临界接触模型的轻环反力为零，重物反力为 $mg/3$，连续曲绳的反力密度为 $q_n>0$。这三项的位置、量纲和作用对象不同。

**驻点自动写成稳定。** 尺度方向 $U$ 为常数，只说明该方向中性；环向扰动有负二阶势能变化，说明另一方向不稳定。若要额外固定相对母线，就改变了允许位移和模型，不能默加导槽或固定杆。

## 八、课堂讲解建议

课堂先用纸制圆锥演示半圈展开：让学生标出同一母线距离的水平圆周，测其圆周长，再剪开铺平。板书只保留 $R=x\sin\theta$、$x\Omega=2\pi R$、$\alpha=\Omega/2$ 三个连续关系。教师此时应追问展开图的弧与绳是否是同一条曲线，避免学生还没有分清参考圆周就套用张力式。

随后沿图3-2的两端连直线，在图3-1上对应描出绳的真实升降。让学生判断绳中部是比端点高还是低，再由 $r_{\min}=x\cos\beta$ 检查直觉。这样空间图与展开图相互核对，不能只记“圆锥展开成扇形”而忽略实际绳路。

受力环节采用三张对象图：第一问的重物、第二问的末端重物、第二问的轻环。教师可让学生逐一数绳力，并标明每股力属于哪一根连续绳。板书先写 $T_A=mg\cos\theta$、$T_B=mg\cos\theta$，再写轻环的 $(T_A+T_B)\sin\beta=T_A$；不要先公布 $\sin\theta=1/3$ 再反向拼式。

计算环节让学生先保留 $L_A$、$L_B$，在每根绳上标出半圈段 $d$ 和尾段 $L_i-d$，从顶点沿母线逐段走到对应重物。课堂应特别核对 $r_i=x+L_i-d$ 到 $z_i=-r_i\cos\theta$ 这一转换，随后由允许的小位移解释势能导数，不把虚功法讲成未经说明的“求导等于零”口令。

基础课堂到两问张力、存在条件和接触反力即可；教师备课可进一步准备不等高环的消元和完整三维力检查。若讨论稳定性，应先让学生指出允许的是母线尺度变化还是环向相对变化，只有研究过对应势能二阶项后再下结论。变式可按几何数值、长度边界、质量不等和张力上限四个层次顺序使用，每个都完整回代，不留未作答自测题替代主解析。

## 九、变式训练

**变式1：用具体锥角同时检查绳长、空间高度和张力。**

采用第（1）问连接，给定 $\theta=30^\circ$、$m=0.20\,\mathrm{kg}$、$g=9.80\,\mathrm{m\,s^{-2}}$，绳套长度 $S=1.20\,\mathrm m$，圆锥母线长 $H=0.80\,\mathrm m$。求两个连接点的母线距离、水平半径、半圈绳中部抬高量及张力，检查该构型是否触及下缘。

先转换展开角：

$$
\alpha=\pi\sin30^\circ=\frac{\pi}{2},\qquad
\beta=\frac{\pi}{4},\qquad
\sin\beta=\cos\beta=\frac{\sqrt2}{2}.
$$

由绳套总长求母线距离：

$$
\begin{aligned}
x
&=\frac{S}{4\sin\beta}
=\frac{1.20}{2\sqrt2}\,\mathrm m
=0.4242641\,\mathrm m,\\
R&=x\sin30^\circ=0.2121320\,\mathrm m,\\
-z_A
&=x\cos30^\circ=0.3674235\,\mathrm m.
\end{aligned}
$$

一条半圈绳的长度为 $d=S/2=0.60\,\mathrm m$，其展开弦中部母线距离

$$
r_{\min}=x\cos\beta=0.3000000\,\mathrm m.
$$

因此空间绳中部抬高

$$
\begin{aligned}
\Delta z
&=(x-r_{\min})\cos30^\circ\\
&=(0.4242641-0.3000000)\frac{\sqrt3}{2}\,\mathrm m\\
&=0.1076159\,\mathrm m.
\end{aligned}
$$

张力为

$$
\begin{aligned}
T
&=\frac{mg\cos30^\circ}{2\sin45^\circ}\\
&=\frac{\sqrt6}{4}mg
=\frac{\sqrt6}{4}(0.20)(9.80)\,\mathrm N\\
&=1.20024997\,\mathrm N.
\end{aligned}
$$

支承力 $N=mg\sin30^\circ=0.980\,\mathrm N>0$。$x=0.4242641<H=0.80$，整条绳的母线距离不超过端点 $x$，所以既不触及下缘也不触及顶点。回代 $2T\sin45^\circ=1.6974098\,\mathrm N=mg\cos30^\circ$，母线方向平衡成立。

**变式2：两绳不等长时，平衡位置是否唯一？**

采用第（2）问连接，锥角满足 $\sin\theta=1/3$，$m=0.30\,\mathrm{kg}$、$g=9.80\,\mathrm{m\,s^{-2}}$。两根绳长分别为 $L_A=0.80\,\mathrm m$、$L_B=1.10\,\mathrm m$，锥面母线长 $H=1.50\,\mathrm m$。求张力、两个重物位置和环位置允许范围；比较 $x=0.20\,\mathrm m$、$x=0.50\,\mathrm m$ 两个构型。

临界角给出 $\beta=\pi/6$、$d=x$，所以

$$
\begin{aligned}
T_A=T_B
&=mg\cos\theta
=(0.30)(9.80)\frac{2\sqrt2}{3}\,\mathrm N\\
&=2.77185858\,\mathrm N,\\
N_A=N_B&=\frac{mg}{3}=0.980\,\mathrm N.
\end{aligned}
$$

每个重物的母线距离 $r_i=x+L_i-d=L_i$，因此

$$
\begin{aligned}
r_A&=0.80\,\mathrm m,\qquad r_B=1.10\,\mathrm m,\\
z_A&=-0.80\frac{2\sqrt2}{3}\,\mathrm m=-0.7542472\,\mathrm m,\\
z_B&=-1.10\frac{2\sqrt2}{3}\,\mathrm m=-1.0370900\,\mathrm m.
\end{aligned}
$$

两个重物都在 $H=1.50\,\mathrm m$ 以内，但不等高。正长度尾段要求

$$
0<x<\min(0.80,1.10)\,\mathrm m=0.80\,\mathrm m.
$$

当 $x=0.20\,\mathrm m$ 时，$(\ell_A,\ell_B)=(0.60,0.90)\,\mathrm m$；当 $x=0.50\,\mathrm m$ 时，$(\ell_A,\ell_B)=(0.30,0.60)\,\mathrm m$。两组均满足 $x+\ell_A=0.80$、$x+\ell_B=1.10$，所以环下移，尾段等量缩短，重物位置和势能不变。两组张力相同，尺度位置不唯一；这不意味着它们对环向扰动稳定。

**变式3：末端质量不相同时，临界锥角和两环高度怎样改变？**

采用交叉过环连接，重物仍与锥面接触，但 $m_A=3m$、$m_B=m$。另加两条沿相对母线的光滑细导槽，两个轻环分别只能沿对应导槽滑动；导槽能够提供环向约束力，但不提供沿母线的力。允许两环母线距离 $a$、$b$ 不同，绳长足够使末段保持正长度且未触边。求静力平衡的 $\theta$、$a/b$、两根绳张力以及导槽约束力。

末端重物先给出

$$
T_A=3mg\cos\theta,\qquad T_B=mg\cos\theta.
$$

两条半圈弦几何相同，端点的母线投影分别为 $c_P$、$c_Q$。环上两弧合张力系数为 $T_A+T_B=4mg\cos\theta$，尾段在 $P$ 为 $T_A$、在 $Q$ 为 $T_B$。因此

$$
c_P=\frac{T_A}{T_A+T_B}=\frac34,\qquad
c_Q=\frac{T_B}{T_A+T_B}=\frac14.
$$

在展开三角形 $OPQ$ 内，令底角为 $\gamma_P$、$\gamma_Q$，其余弦正是端点上行母线的投影系数，故

$$
\gamma_P=\arccos\frac34,\qquad
\gamma_Q=\arccos\frac14.
$$

三角形内角和给顶角

$$
\begin{aligned}
\alpha
&=\pi-\gamma_P-\gamma_Q\\
&=\pi-\arccos\frac34-\arccos\frac14\\
&=1.1007423341\,\mathrm{rad}.
\end{aligned}
$$

由于 $\alpha=\pi\sin\theta$，

$$
\begin{aligned}
\sin\theta&=\frac{\alpha}{\pi}=0.3503771671,\\
\theta&=0.3579737677\,\mathrm{rad}
=20.51038607^\circ,\\
\cos\theta&=0.9366086914.
\end{aligned}
$$

由正弦定理，$a=OP$ 对着 $\gamma_Q$，$b=OQ$ 对着 $\gamma_P$，所以

$$
\begin{aligned}
\frac ab
&=\frac{\sin\gamma_Q}{\sin\gamma_P}\\
&=\frac{\sqrt{1-(1/4)^2}}{\sqrt{1-(3/4)^2}}\\
&=\frac{\sqrt{15}/4}{\sqrt7/4}
=\sqrt{\frac{15}{7}}
=1.4638501094.
\end{aligned}
$$

与较重末端相连的 $P$ 环具有更大的母线距离，即位置更低。最后

$$
\boxed{
T_A=2.8098260742\,mg,\qquad
T_B=0.9366086914\,mg.
}
$$

这里 $mg$ 的 $m$ 是较轻重物质量，两张力不再相等。将比值 $a/b$ 代回弦长式和 $c_P,c_Q$，分别恢复 $3/4$、$1/4$；因此不能继续使用等质量时的 $\sin\theta=1/3$。

还必须完成环向平衡。两个半圈弧在同一环处的环向分量方向相反，但因为张力不等，它们不会自行抵消。导槽反力必须反向抵消剩余分量，其大小分别为

$$
\begin{aligned}
F_P
&=|T_A-T_B|\sqrt{1-c_P^2}
=2mg\cos\theta\,\frac{\sqrt7}{4}
=\frac{\sqrt7}{2}mg\cos\theta,\\
F_Q
&=|T_A-T_B|\sqrt{1-c_Q^2}
=2mg\cos\theta\,\frac{\sqrt{15}}4
=\frac{\sqrt{15}}2mg\cos\theta.
\end{aligned}
$$

这些反力只约束环向，不对沿母线的允许虚位移作功。若删除本变式明确增加的导槽，却保留两环位于相对母线、两弧夹角相同的构型，环向净力不能平衡；仅求出上面的 $\theta$ 和 $a/b$ 还不能称为完整静力解。

**变式4：绳的承载上限如何限制允许的锥角？**

采用第（1）问连接，$m=0.20\,\mathrm{kg}$、$g=9.80\,\mathrm{m\,s^{-2}}$，绳的允许张力为 $T_{\max}=2.00\,\mathrm N$。只讨论几何长度能够容纳绳套的范围。求不超过承载上限的锥角条件，并说明求得的阈值是否唯一。

由主解，

$$
T(\theta)
=\frac{mg\cos\theta}{2\sin\beta(\theta)},\qquad
\beta(\theta)=\frac{\pi}{2}\sin\theta.
$$

对无量纲正量 $T/(mg)$ 取对数再求导，避免复杂商法则：

$$
\begin{aligned}
\frac{\mathrm d}{\mathrm d\theta}\ln\frac{T}{mg}
&=\frac{\mathrm d}{\mathrm d\theta}
[\ln(1/2)+\ln\cos\theta-\ln\sin\beta]\\
&=-\tan\theta-\cot\beta\frac{\mathrm d\beta}{\mathrm d\theta}\\
&=-\tan\theta-\frac{\pi}{2}\cos\theta\cot\beta<0.
\end{aligned}
$$

严格负号来自 $0<\theta<\pi/2$、$0<\beta<\pi/2$。因此 $T(\theta)$ 严格下降；又有 $\theta\to0$ 时 $T\to+\infty$、$\theta\to\pi/2$ 时 $T\to0$，承载等式必有唯一根。不能只找到一个数值驻点而不检查唯一性。

<!-- KEEP_TOGETHER_START -->

解阈值方程

$$
\frac{(0.20)(9.80)\cos\theta_{\min}}
{2\sin[(\pi/2)\sin\theta_{\min}]}
=2.00.
$$

用弧度计算三角函数，逐步缩小有符号残差区间，得到

$$
\begin{aligned}
\theta_{\min}&=0.3137879436\,\mathrm{rad},\\
&=17.97872483^\circ.
\end{aligned}
$$

作邻近回代检验：$\theta=18.00^\circ$ 时 $T=1.99765546\,\mathrm N<2.00\,\mathrm N$；$\theta=17.90^\circ$ 时张力超过上限。故承载条件为

$$
\boxed{
17.97872483^\circ\leq\theta<90^\circ,
}
$$

同时仍须满足主解的绳长、锥面边界和正常绷紧条件。此处求的是第一种连接的承载限制，不与第二种连接只有单一临界锥角的平衡存在条件混用。

<!-- KEEP_TOGETHER_END -->

<!-- question-complete -->
