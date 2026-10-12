# 第2题

<!-- question-start -->

一根长度为$l$的柔软导线，两端分别固定在$A(0,0,0)$和$B(l/2,0,0)$处。电流$I$从$A$端流入、从$B$端流出。忽略导线中电流自身产生的磁场，$B_0>0$。

（1）空间中存在均匀磁场$\boldsymbol B=(0,0,B_0)$，求静力平衡时的导线形状及张力大小。

（2）将磁场改为$\boldsymbol B=(B_0,0,0)$，求静力平衡时的导线形状及张力大小。

以下采用不可伸长、可自由弯曲的理想导线模型，只计外磁场安培力、张力和端点约束，不计重力、弯曲刚度及自磁场。求解的是具有正张力的光滑平衡曲线；“静力平衡”本身不等于已证明该形状对任意扰动稳定。

![图2-1 固定端点的位置与两种外磁场方向。](../figures/question-02.png){width=78%}

<!-- question-end -->

## 一、题型定位

这是柔软载流线的连续体静力学。图2-1中端点距离只有导线总长的一半，因此导线不可能在两端之间直接拉成一条直线。局部安培力随导线方向变化，不能把全段安培力简单画成一个恒力后猜测形状。

决定形状的是相邻微元张力方向的变化，而不是张力大小沿线的变化。第一问的磁场垂直端点连线，导线成为同一平面内的一段圆弧；第二问的磁场沿端点连线，切线沿磁场的分量不变，横向分量旋转，形成三维螺旋线。两者的局部平衡方程相同，但端点闭合条件完全不同。

第一问还必须区分所取圆弧是优弧还是劣弧；第二问则必须保留整匝数$n=1,2,\ldots$及绕端点连线旋转的相位自由度。仅给一个未说明匝数的螺旋图，不能构成完整答案。

## 二、知识点

以弧长$s$作为导线参数，$0\le s\le l$。位置为$\boldsymbol r(s)$，单位切向量为$\boldsymbol t=\mathrm d\boldsymbol r/\mathrm ds$，故$|\boldsymbol t|=1$。正向取从$A$到$B$，与电流方向一致。长度微元$\mathrm ds$所受安培力为

$$
\mathrm d\boldsymbol F_{\mathrm B}
=I\,\mathrm d\boldsymbol r\times\boldsymbol B
=I(\boldsymbol t\times\boldsymbol B)\,\mathrm ds.
$$

柔软导线没有弯矩，张力沿局部切线。对同一小段，前端张力为$T(s+\mathrm ds)\boldsymbol t(s+\mathrm ds)$，后端张力为$-T(s)\boldsymbol t(s)$。负号来自后一段拉着微元向后，而不是人为选取相反电流。

单位切向量的导数垂直于切向量：由$\boldsymbol t\cdot\boldsymbol t=1$求导得$\boldsymbol t\cdot\boldsymbol t'=0$。磁力也垂直于切线。这两条关系共同保证张力大小为常数。平面圆弧的曲率为$1/R$；螺旋线绕圆柱轴的半径则不等于其三维曲率半径。

## 三、物理图像

微元图2-2中的两端张力并不共线，其矢量差指向曲线凹侧；安培力指向相反的凸侧。磁场只负责改变张力方向，不能在无其他切向载荷时造成沿线张力大小增加或减少。

![图2-2 导线微元两端张力与安培力的局部平衡。](../figures/element-02.png){width=48%}

第一问的导线位于$xy$平面。按电流从$A$到$B$、磁场沿$+z$的方向，它沿圆周逆时针经过下方优弧。圆心在端点连线的下方，电流在$A$附近先向左下方、在$B$附近向左上方，因此两端切线并不都沿$+x$。这些方向由右手定则和局部平衡共同确定。

第二问不能沿用平面圆弧图。磁场沿$x$，导线沿$x$的切向分量恒为$1/2$，另有大小为$\sqrt3/2$的横向分量。导线绕一条平行于$AB$的轴旋转，但该轴不经过$A$和$B$；两端在圆柱同一条母线上，端点连线是母线，不是圆柱轴。这一区别在三维题图中必须真实表现。

## 四、解题入口

先对微元列矢量平衡，而不是先假设“必然是圆”。点乘切线消去横向载荷，得到$T$为常数；再写切向量的一阶旋转方程。利用磁场方向分别确定平面性或轴向分量，最后才施加两个端点的位置和总长度。

对第一问，把圆弧的总转角记为$2\beta$，弧长$l=2R\beta$，弦长$l/2=2R\sin\beta$，由两者比值得到非零根$\sin\beta/\beta=1/2$。对第二问，横向位移必须同时闭合，要求切线相位转过整数个$2\pi$，这才给出离散的张力分支。

## 五、解析

（1）从微元建立统一的矢量静力方程。

使用图2-2中同一微元的两端张力及安培力，有

$$
\begin{aligned}
& T(s+\mathrm ds)\boldsymbol t(s+\mathrm ds)
-T(s)\boldsymbol t(s)
+I(\boldsymbol t\times\boldsymbol B)\,\mathrm ds=0,\\
& \frac{\mathrm d(T\boldsymbol t)}{\mathrm ds}
+I\boldsymbol t\times\boldsymbol B=0.
\end{aligned}
$$

第二行是第一行除以$\mathrm ds$并取极限，并非将微元张力简单相减成一个标量。展开乘积导数，再与$\boldsymbol t$点乘：

$$
\begin{aligned}
T'\boldsymbol t+T\boldsymbol t'
+I\boldsymbol t\times\boldsymbol B&=0,\\
T'|\boldsymbol t|^2
+T\boldsymbol t\cdot\boldsymbol t'
+I\boldsymbol t\cdot(\boldsymbol t\times\boldsymbol B)&=0,\\
T'&=0.
\end{aligned}
$$

所以沿一条平衡导线$T$处处相等。注意这里结论是大小相等，而张力矢量方向仍随位置变化。剩余方程为

$$
\boxed{\boldsymbol t'
=\frac I T\,\boldsymbol B\times\boldsymbol t}.
$$

把叉乘换序产生了负号：$-\boldsymbol t\times\boldsymbol B=\boldsymbol B\times\boldsymbol t$。它决定后续圆弧和螺旋的旋转方向，不能漏掉。

（2）证明第一问的导线必须位于$xy$平面。

磁场为$B_0\boldsymbol e_z$，令$k=IB_0/T>0$，则分量方程为

$$
t_x'=-kt_y,\qquad t_y'=kt_x,\qquad t_z'=0.
$$

因此$t_z$为常数。两个端点的$z$坐标均为零，而

$$
z_B-z_A=\int_0^l t_z\,\mathrm ds=l t_z=0,
$$

所以$t_z=0$。这不是凭二维图“看出”的，而是局部方程和端点条件的共同结果。又有$t_x^2+t_y^2=1$，可写$t_x=\cos u$、$t_y=\sin u$。代回方程得到$u'=k$：切线沿弧长匀速转动，平面曲率为常量$k$。

于是导线是一段半径为

$$
R=\frac1k=\frac{T}{IB_0}
$$

的圆弧。等价地，微元两端张力的凹向合力大小为$T\,\mathrm ds/R$，安培力大小为$IB_0\,\mathrm ds$，从而$T=IB_0R$。这里每段导线均与磁场垂直，因此没有额外正弦因子。

（3）由长度与端点弦长筛选正确的圆弧。

记沿电流方向的总切线转角为$2\beta$。图2-3中$O$为圆心，端点弦长为$d=l/2$，并画出实际经过的下方优弧。若暂不限制绕行圈数，圆弧的长度与端点距离给出

$$
l=2R\beta,\qquad d=2R|\sin\beta|.
$$

消去$R$后$|\sin\beta|/\beta=1/2$。由于$|\sin\beta|\le1$，必有$\beta\le2<\pi$。因此不存在绕过完整一圈以上的分支，并且这一范围内$\sin\beta>0$，绝对值可以去掉。不能先随意选择短弧，再用错误的弧长公式计算。

![图2-3 垂直磁场中的平面优弧、圆心与端点切线。](../figures/arc-02.png){width=60%}

几何方程最终成为

$$
\boxed{\frac{\sin\beta}{\beta}=\frac12,\qquad 0<\beta<\pi}.
$$

它在该区间只有一个根。证明时对函数求导：

$$
\begin{aligned}
\frac{\mathrm d}{\mathrm d\beta}
\left(\frac{\sin\beta}{\beta}\right)
&=\frac{\beta\cos\beta-\sin\beta}{\beta^2},\\
\frac{\mathrm d}{\mathrm d\beta}
(\sin\beta-\beta\cos\beta)&=\beta\sin\beta>0.
\end{aligned}
$$

因$\sin\beta-\beta\cos\beta$在零点极限为零，在$0<\beta<\pi$为正，故上面的比值严格递减，从$1$降到$0$。又在$\beta=\pi/2$处比值为$2/\pi>1/2$，所以所求根大于$\pi/2$，总弧角大于$\pi$，确实是优弧。

（4）把超越方程的数值求解与张力计算写完整。

令$f(\beta)=\sin\beta-\beta/2$。因为$f(1.8)>0$而$f(2)<0$，可先用二分法把非零根锁定，再用牛顿迭代

$$
\beta_{j+1}
=\beta_j-\frac{\sin\beta_j-\beta_j/2}
{\cos\beta_j-1/2}
$$

求得

$$
\begin{aligned}
\beta&=1.895494267\ldots,\\
2\beta&=3.790988534\ldots,\\
R&=\frac{l}{2\beta}=0.263783\ldots\,l,\\
T&=\boxed{\frac{IB_0l}{2\beta}
=0.263783\ldots\,IB_0l.}
\end{aligned}
$$

这里$\beta=0$虽然使$\sin\beta-\beta/2=0$，却不是原比值方程的解，且会使$R=l/(2\beta)$失去意义，必须排除。数值根若未经这一筛选，很容易被求根程序返回的零根误导。

也可沿用圆心端点锐角$\theta=\pi-\beta$，得到$\pi-\theta=2\sin\theta$。其值是$\theta=1.246098\ldots$弧度，即约$71.396^\circ$；角度数与弧度数不可互相直接代入三角函数。$2\beta$约为$217.208^\circ$，不是一段小于半圆的短弧。

（5）写出圆弧的完整参数方程，检查它确实连接端点。

令$u=ks-\beta$，$k=2\beta/l$。切线为$(\cos u,\sin u,0)$。从$A$出发积分：

$$
\begin{aligned}
x(s)&=R[\sin(ks-\beta)+\sin\beta],\\
y(s)&=R[\cos\beta-\cos(ks-\beta)],\\
z(s)&=0,\qquad 0\le s\le l.
\end{aligned}
$$

在$s=0$处，$x=y=0$；在$s=l$处，$ks-\beta=\beta$，所以$x=2R\sin\beta=l/2$、$y=0$。圆心为

$$
O=(R\sin\beta,R\cos\beta,0)
=(l/4,R\cos\beta,0).
$$

因为$\cos\beta<0$，圆心位于$AB$下方。图2-3中的下方路径与上述$y(s)$一致：中点$s=l/2$处$y=R(\cos\beta-1)<0$。点沿圆周逆时针走过$2\beta$；在局部曲率指向圆心的同时，安培力指向外侧。这也核对了最初叉乘方程的符号。

（6）用全导线的总磁力和端点反力进行独立检查。

均匀磁场中，全段安培力只取决于端点位移：

$$
\begin{aligned}
\boldsymbol F_{\mathrm B,tot}
&=I\int_A^B\mathrm d\boldsymbol r\times\boldsymbol B\\
&=I(\boldsymbol r_B-\boldsymbol r_A)\times\boldsymbol B\\
&=-\frac12IB_0l\,\boldsymbol e_y.
\end{aligned}
$$

支座对导线的端点力分别为$-T\boldsymbol t(0)$和$+T\boldsymbol t(l)$，其和为$2T\sin\beta\,\boldsymbol e_y$。利用$T=IB_0R$与$2R\sin\beta=l/2$，两者恰好抵消。端点水平分量也互相抵消。

这条全局检验不能单独决定圆弧形状，却能查出电流方向、受力方向及张力系数是否错误。若把两端力都写成$+T\boldsymbol t$，即使局部计算正确，全局平衡也不能成立。

（7）第二问先由轴向投影求切线与磁场的夹角。

现在$\boldsymbol B=B_0\boldsymbol e_x$。统一方程给出

$$
t_x'=0,\qquad t_y'=-kt_z,\qquad t_z'=kt_y,\qquad k=\frac{IB_0}{T}.
$$

$t_x$为常数。端点的$x$位移为$l/2$，故

$$
\frac l2=x_B-x_A=\int_0^l t_x\,\mathrm ds=l t_x,
\qquad \boxed{t_x=\frac12}.
$$

由单位切线条件，横向分量大小为

$$
t_\perp=\sqrt{t_y^2+t_z^2}
=\sqrt{1-\frac14}=\frac{\sqrt3}{2}.
$$

因此切线与圆柱轴$x$的夹角$\alpha$满足$\cos\alpha=1/2$，即$\alpha=60^\circ$。若将导线与横向圆周方向的夹角记作$\alpha'$，则$\alpha'=30^\circ$。这两个角互余；不能把$30^\circ$说成与磁场的夹角。

（8）解横向旋转方程，保留任意初始相位。

由$t_y'=-kt_z$、$t_z'=kt_y$，可取

$$
t_y=\frac{\sqrt3}{2}\cos(ks+\delta),\qquad
t_z=\frac{\sqrt3}{2}\sin(ks+\delta).
$$

$\delta$是导线绕$x$方向的初始相位，由端点位置并不能唯一确定。对$s$积分并令起点为$A$，得

$$
\begin{aligned}
x(s)&=\frac s2,\\
y(s)&=\frac{\sqrt3}{2k}
[\sin(ks+\delta)-\sin\delta],\\
z(s)&=\frac{\sqrt3}{2k}
[\cos\delta-\cos(ks+\delta)].
\end{aligned}
$$

横截面中的两个分量都是同一角度的正弦和余弦，所以曲线是圆柱螺旋线，不是平面正弦曲线。由于$x$随$s$严格增加，每个有限匝数分支本身没有交叉重合。

（9）由两个横向端点条件得到整匝数。

在$s=l$处必须同时有$y(l)=0$和$z(l)=0$。它们要求

$$
\sin(kl+\delta)=\sin\delta,\qquad
\cos(kl+\delta)=\cos\delta.
$$

只有正弦等式不能推出完整闭合，必须与余弦等式共同使用。两式等价于角度相差$2\pi$的整数倍，故

$$
\boxed{kl=2\pi n,\qquad n=1,2,3,\ldots}.
$$

$k>0$排除负$n$；$n=0$会要求$k=0$，与有限正张力及非零$IB_0$不相容。若试图直接取直线，它又只能有长度$l/2$，违背既定长度$l$。因此不能添加一个“零匝直线”作为本题的有限张力解。

（10）求每个分支的张力、圆柱半径和螺距。

由$k=IB_0/T=2\pi n/l$得到

$$
\boxed{T_n=\frac{IB_0l}{2\pi n}}.
$$

从参数方程读出圆柱半径$r_n=t_\perp/k$，而一匝导线弧长为$l/n$，其中轴向位移占一半，故

$$
\boxed{r_n=\frac{\sqrt3\,l}{4\pi n},
\qquad p_n=\frac{l}{2n}}.
$$

$p_n$是每匝轴向前进量，不是每匝导线长度。展开图2-5的直角三角形可再次核对：轴向边为$l/(2n)$，圆周边为$2\pi r_n=\sqrt3\,l/(2n)$，斜边为$l/n$。勾股关系与$\cos\alpha=1/2$同时成立。

$n=1$时$T_1=0.159154943\ldots\,IB_0l$，$r_1=0.137832224\ldots\,l$；每增加匝数，张力、半径和螺距均按$1/n$减小。$T_1$是这些平衡分支中的最大张力，不是最小张力。题目没有规定$n$，因此必须列出整个分支族。

（11）明确螺旋轴的位置，避免把轴线错误画在端点连线上。

令$r_n=\sqrt3/(2k)$，则横截面的圆满足

$$
(y+r_n\sin\delta)^2+(z-r_n\cos\delta)^2=r_n^2.
$$

所以圆柱轴是

$$
\mathcal A:\quad
y=-r_n\sin\delta,\qquad z=r_n\cos\delta,
$$

一条平行$x$方向的直线。该轴距端点连线$AB$为$r_n$，不经过两端点。图2-4取$\delta=0$和$n=1$：轴线为$(x,0,r_1)$，而端点为$(0,0,0)$、$(l/2,0,0)$，位于圆柱的同一底部母线。

![图2-4 平行磁场中的一匝三维螺旋与偏置圆柱轴。](../figures/helix-02.png){width=76%}

在这幅图对应的取相下，

$$
y=r_1\sin(2\pi s/l),\qquad
z=r_1[1-\cos(2\pi s/l)].
$$

因此在$x=l/4$处$y=0$、$z=2r_1$，是相对圆柱轴的另一侧，不是沿$AB$来回穿越的正弦波。初始切线的横向分量沿$+y$，曲率指向$+z$，安培力沿$-z$，与图2-2的微元平衡一致。任意$\delta$对应绕端点连线刚性旋转后的同类曲线。

（12）用圆柱展开关系及局部曲率再次核验张力。

图2-5把一匝圆柱面展开成矩形。导线是跨越横向圆周边$2\pi r_n$与轴向边$p_n$的斜线；与轴的夹角为$60^\circ$，与圆周方向的夹角为$30^\circ$。

![图2-5 一匝螺旋的圆柱展开与长度、半径和螺距关系。](../figures/unrolled-02.png){width=54%}

螺旋的单位切线导数大小为$|\boldsymbol t'|=k t_\perp$。因此三维曲率半径为

$$
\begin{aligned}
\rho_{\mathrm h}
&=\frac1{k t_\perp}
=\frac{2}{\sqrt3 k}
=\frac{4r_n}{3},\\
\frac{T}{\rho_{\mathrm h}}
&=IB_0 t_\perp
=IB_0\sin\alpha.
\end{aligned}
$$

代入$\rho_{\mathrm h}$后，$T=IB_0/k=IB_0l/(2\pi n)$，与旋转方程一致。若错误地用圆柱半径$r_n$代替曲率半径，就会得到错误的$\sqrt3/2$系数。

也可以把一小段的张力变化投影到横截面。沿圆周方向的张力分量为$Tt_\perp$，旋转相位增量为$k\,\mathrm ds$，横向合力为$Tt_\perp k\,\mathrm ds$；微元安培力为$IB_0t_\perp\,\mathrm ds$。约去非零$t_\perp\,\mathrm ds$，同样得$Tk=IB_0$。这是投影路线，而非误把整个张力都放在圆周方向。

（13）做全局受力、单位和分支检查，汇总答案。

第二问的端点位移与磁场平行，所以

$$
\boldsymbol F_{\mathrm B,tot}
=I(l\boldsymbol e_x/2)\times(B_0\boldsymbol e_x)=0.
$$

局部各段磁力不为零，但矢量积分相互抵消。整匝闭合又使$\boldsymbol t(l)=\boldsymbol t(0)$，两端支座对导线的力互为相反数。不能由总磁力为零推断各段都没有磁力，更不能据此声称任意松弛形状都能平衡。

$IB_0$的单位为$\mathrm{N/m}$，所以两个答案中的$IB_0l$都具有张力单位。半径、螺距按$l$缩放；形状的无量纲参数由端点距离与总长的比值决定，电流或场强改变时张力成比例改变，而理想形状不变。

最终第一问为唯一的下方平面优弧：

$$
\frac{\sin\beta}{\beta}=\frac12,\quad
R=\frac l{2\beta},\quad T=IB_0R,\quad
\beta=1.895494267\ldots.
$$

第二问为三维螺旋族：

$$
T_n=\frac{IB_0l}{2\pi n},\qquad
r_n=\frac{\sqrt3 l}{4\pi n},\qquad
p_n=\frac l{2n},\qquad n=1,2,\ldots,
$$

并保留任意相位$\delta$。这些是理想柔软、正张力模型下的静力解；实际线材的弯曲刚度、线径、重力及扰动稳定性会进一步限制可实现的形状，但不能在未给相应条件时擅自选择某一个$n$。

## 六、关键洞察

先看方程的结构比先看图更可靠。安培力没有切向分量，使张力大小恒定；均匀磁场又使单位切线以固定角速度绕磁场方向旋转。若切线沿磁场的分量为零，轨迹是平面圆；若该分量非零，轨迹是螺旋。这是同一连续体平衡规律的两种投影，不是两个互不相关的经验结论。

一个更一般的积分关系可以直接从统一方程得到。因为$\boldsymbol B$恒定且$\boldsymbol r'=\boldsymbol t$，

$$
\frac{\mathrm d}{\mathrm ds}
[T\boldsymbol t-I\boldsymbol B\times\boldsymbol r]=0.
$$

因此存在常矢量$\boldsymbol C$使$T\boldsymbol t=I\boldsymbol B\times\boldsymbol r+\boldsymbol C$。第一问在$xy$平面把这个关系投影，即可看到切线总与半径垂直；第二问在$yz$平面则可直接读出偏置轴线。它同时说明圆心或圆柱轴不必与两个固定端点重合。

第二问的整匝数来自两个横向坐标同时闭合，是一个几何边界约束，不是导线长度“约等于若干周长”的近似。螺旋切线中沿轴方向始终占一半，即使$n$很大仍不消失。$n\to\infty$时曲线位置趋近端点连线，但切向量持续快速振荡、实际总弧长保持$l$，所以不能把极限位置曲线的长度$l/2$当作每个有限$n$的长度。

两种端点场方向的总磁力分别为$-IB_0l\boldsymbol e_y/2$和零，而局部形状都需要非零磁力。这很好地区分了“合力为零”“每个微元力为零”和“整体静力平衡”三个不同命题。

## 七、易错点

把安培力写成$I\boldsymbol B\times\mathrm d\boldsymbol r$会反转全部外力方向；正确的是$I\,\mathrm d\boldsymbol r\times\boldsymbol B$。只有将其移到张力方程右边，才得到$\boldsymbol t'=(I/T)\boldsymbol B\times\boldsymbol t$。

把第一问默认为劣弧，遗漏$l/d=2$对弧长的限制，会得到错误圆心、半径和张力。将$\sin\beta-\beta/2=0$的零根当作答案，则完全绕过了原比值方程的定义域。

把第二问的切线与轴夹角写成$30^\circ$，是混淆了轴向与圆周方向；两者正确分别为$60^\circ$与$30^\circ$。将半径$r_n$当作曲率半径，又会使局部力平衡出现错误系数。

三维图的螺旋轴不能直接画在$AB$上：如果两端都落在轴上却半径非零，那根本不是同一个圆柱螺旋。正确轴线与$AB$平行且相距$r_n$，两端落在同一母线上。$x=s/2$还是检验投影图是否错误自交的直接依据。

总磁力为零不代表局部没有磁力，也不代表张力为零。未规定匝数时只写$n=1$不完整；反过来称所有$n$都“稳定”，又超出了静力方程能证明的范围。实际材料是否允许大匝数，需要额外信息，不能在答案中假装已经证明。

## 八、课堂讲解建议

课堂先让学生在微元图上分别画两端张力，再说明前端为$+T\boldsymbol t$、后端为$-T\boldsymbol t$。教师可用两根方向略不同的箭头演示矢量差与标量差的区别，板书展开$\mathrm d(T\boldsymbol t)/\mathrm ds$后点乘$\boldsymbol t$，使恒张力结论有明确出处。

接着将磁场沿$z$与沿$x$的分量方程并排书写。让学生先用端点条件求$t_z=0$或$t_x=1/2$，再命名“圆弧”或“螺旋”。这能避免凭熟悉图形套公式。圆弧部分先问$l/d=2$能否是短弧，再让学生比较半圆的弧弦比$\pi/2$，建立优弧直觉。

螺旋部分应同时展示三维图与展开图。教师明确指出$AB$是母线，不是轴；在圆柱截面画出轴线偏置$r_n$。板书$x=s/2$、$t_\perp=\sqrt3/2$，随后用正弦和余弦两个端点等式推出整匝，不能只靠图上“看起来绕一圈”。

最后让学生分别计算两种磁场中的总磁力，再与两端支座力相加。教师据此检查右手方向、端点力符号和张力系数。稳定性可作为边界说明，不在没有材料和扰动模型的情况下宣布某个分支自然稳定。

## 九、变式训练

变式一：仍令磁场沿端点连线，把端点改为$B(\eta l,0,0)$，其中$0<\eta<1$，求所有正张力平衡螺旋。

完整解答：轴向切线为$t_x=\eta$，横向大小$q=\sqrt{1-\eta^2}$。统一方程仍给$k=IB_0/T$，横向解为$t_y=q\cos(ks+\delta)$、$t_z=q\sin(ks+\delta)$。两个横向位移同时为零要求$kl=2\pi n$。因此

$$
T_n=\frac{IB_0l}{2\pi n},\qquad
r_n=\frac{l\sqrt{1-\eta^2}}{2\pi n},\qquad
p_n=\frac{\eta l}{n}.
$$

轴线仍相对端点连线偏置$r_n$，切线与轴的夹角满足$\cos\alpha=\eta$。一匝展开后，$(2\pi r_n)^2+p_n^2=(l/n)^2$。例如$\eta=3/4$，$r_n=\sqrt7 l/(8\pi n)$、$p_n=3l/(4n)$、$T_n$仍与本题相同，因为固定总弧长的整匝相位条件没有改变。

当$\eta\to1^-$，半径趋于零，但对应的$T_n$仍有限。严格$\eta=1$时切线完全平行磁场，安培力为零，直线导线的张力可由额外预应力决定，不再由上述闭合式唯一确定；这是横向振幅消失后的退化，不能把极限分支误当作全部直线解。严格$\eta=0$则两端重合，轴向分量为零，平衡形状退化为平面圆并可能重绕；本变式限定$0<\eta<1$以免混用这些边界。

变式二：第一问的端点距离改为$d=3l/4$，求圆弧是优弧还是劣弧，并给出张力的求解步骤。

完整解答：由平面曲率与弧长，仍有$l=2R\beta$、$d=2R\sin\beta$，故$\sin\beta/\beta=3/4$。在$\beta=\pi/2$处该比值为$2/\pi<3/4$，而它从零点极限$1$严格递减，故唯一非零根处于$0<\beta<\pi/2$，是劣弧。用二分法或牛顿法求根$\beta=\beta_{3/4}$，得到

$$
R=\frac l{2\beta_{3/4}},\qquad
T=\frac{IB_0l}{2\beta_{3/4}}.
$$

参数式仍可取$x=R[\sin(ks-\beta)+\sin\beta]$、$y=R[\cos\beta-\cos(ks-\beta)]$，$k=2\beta/l$。这一次$\cos\beta>0$，圆心位于端点连线上方，导线走下方劣弧。相同磁场与电流方向下，圆心上下位置的改变来自弧弦比改变，不是叉乘符号反转。代入实际数值根后，须检验$2R\sin\beta=3l/4$与$l=2R\beta$同时成立。

具体数值为$\beta_{3/4}=1.275698109\ldots$、$R=0.391942260\ldots\,l$、$T=0.391942260\ldots\,IB_0l$。所以$2\beta_{3/4}<\pi$。分别代回弦长与弧长条件：

$$
\begin{aligned}
2(0.391942260)\sin(1.275698109)&\simeq0.750000000,\\
2(0.391942260)(1.275698109)&\simeq1.000000000.
\end{aligned}
$$

两者的误差仅来自上述小数截取；使用未经舍入的根和半径时，分别准确满足$d/l=3/4$与总弧长为$l$。

变式三：第一问的端点间距接近导线总长，令$d=l(1-\varepsilon)$，$0<\varepsilon\ll1$，求半径和张力的首阶近似，并解释趋势。

完整解答：几何式为$\sin\beta/\beta=1-\varepsilon$。使用泰勒展开$\sin\beta=\beta-\beta^3/6+O(\beta^5)$，除以非零$\beta$，得到$1-\beta^2/6+O(\beta^4)=1-\varepsilon$。故

$$
\beta=\sqrt{6\varepsilon}\,[1+O(\varepsilon)],\qquad
R=\frac{l}{2\sqrt{6\varepsilon}}\,[1+O(\varepsilon)],\qquad
T=\frac{IB_0l}{2\sqrt{6\varepsilon}}\,[1+O(\varepsilon)].
$$

当端点越接近完全拉直，所允许的曲率越小，而垂直磁场的单位弧长载荷$IB_0$没有减少；由$T/R=IB_0$，张力必须增大。严格$d=l$的不可伸长直线在非零横向磁力下不能靠有限沿线张力维持静力平衡，除非增加分布支承，不能说“完全拉直时张力为零”。

变式四：保持本题几何，把电流方向反转；再把电流和磁场同时反转，分别说明张力和形状变化。

完整解答：安培力含乘积$I\boldsymbol B$。仅反转电流时，局部旋转方程的有向$k$变号。第一问的圆弧关于$x$轴镜像，由下方优弧变成上方优弧，半径和张力大小不变。第二问沿$x$仍需$t_x=1/2$，横向旋转相位随弧长的变化方向反转；轴向螺距大小、圆柱半径和张力大小不变，螺旋旋向反转。若电流与磁场同时反转，$I\boldsymbol B$不变，整套局部方程及端点条件均不变，原形状仍是解。

张力是正的大小，应写$|I|B_0R$或$|I|B_0l/(2\pi n)$；不能因电流符号反转而把张力写成负数，再把“推力”当作柔软导线可以提供的轴向作用。方向改变体现在曲线旋向和受力方向，而非柔软线可以承压。

<!-- question-complete -->
