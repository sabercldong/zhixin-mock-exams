# 第 2 题

一根轻质刚性杆的上、下两端分别固定质量为 $m$ 和 $m'$ 的质点。将杆竖直放在光滑水平桌面上，施加微小扰动后让其倒下。题目提出：当 $m'=0$ 时，底端与桌面之间的作用力立即为零；当 $m'\to\infty$ 时，底端与桌面之间的作用力始终不为零，并据此设想存在临界质量 $m_c$。

（1）求临界质量 $m_c$，以及 $m'=m_c$ 时支持力降为零的杆与桌面的夹角 $\theta_0$。

（2）若空间中存在垂直纸面向外的匀强磁场，磁感应强度为 $B$，两个质点均带正电荷 $+q$，杆长为 $l$，求从竖直状态微扰后、底端离开桌面之前，杆与水平面夹角为 $\theta$ 时两质点的相对速度。

![图 2-1　光滑桌面上轻杆两端的质点及初始竖直位置。](../figures/question-02.png)

## 一、题型定位

刚性杆连接的双质点受约束运动。第一问是可滑动底端的倒杆问题，第二问是在同一约束中加入洛伦兹力。质量集中在两个端点，不能套用均匀杆的转动惯量或离地条件。题目对临界质量的设想需要由支持力的符号检验，而不是把它直接作为已经成立的结论。

## 二、知识点

刚性杆长约束；质心横向运动；机械能守恒；动能中的交叉项及配方；带电粒子的洛伦兹力；机械动量与广义动量的区别；支持力的单侧约束；相对速度和角速度的联系；微扰初态与恰好竖直不动的区别。

## 三、物理图像

杆向右倒下时，上端通常向右下方运动，下端则可以沿桌面向左滑动。桌面光滑意味着没有水平接触力，不意味着底端固定。两质点之间的杆力可以拉伸，也可以压缩，但杆不伸长。磁场力始终垂直各自的速度，所以它改变运动方向而不改变总机械能。磁场可以交换水平动量，因而不能把无磁场时的横向机械动量守恒式原样保留。

## 四、解题入口

先在底端仍贴着桌面的阶段建立两个质点的坐标。无磁场时用水平动量守恒消去底端速度，再由能量求杆角速度，由受力求支持力，并检验是否真的存在正临界质量。有磁场时从总水平受力积分得到新的守恒组合，再与能量联立。第二问的速度公式必须附带“根号非负、支持力非负”的适用条件。

## 五、解析

（1）确定坐标、运动方向及参数的含义。

取桌面为 $x$ 轴，竖直向上为 $y$ 轴，纸面外为 $+z$。以底端质点的位置为 $(X,0)$，以上端在底端右上方的一支运动为例。杆与水平面的夹角为 $\theta$，倒下时 $\theta$ 从接近 $\pi/2$ 减小，故 $\dot\theta<0$。上端和下端的位置分别为

$$\boldsymbol r_u=(X+l\cos\theta,l\sin\theta),\qquad
\boldsymbol r_b=(X,0).$$

将两位置各自对时间求导，得到

$$\begin{aligned}
\boldsymbol v_u&=(\dot X-l\sin\theta\,\dot\theta,\ l\cos\theta\,\dot\theta),\\
\boldsymbol v_b&=(\dot X,0),\\
\boldsymbol v_u-\boldsymbol v_b
&=l\dot\theta(-\sin\theta,\cos\theta).
\end{aligned}$$

相对速度沿杆的垂线，而不是沿杆。图 2-2 中 $\boldsymbol e=(\cos\theta,\sin\theta)$ 沿杆由下端指向上端，$\boldsymbol n=(-\sin\theta,\cos\theta)$ 为逆时针转过 $90^\circ$ 的单位矢量。

![图 2-2　倒下阶段两端速度及沿杆、垂直杆的方向。](../figures/velocities-02.png)

相对速度的矢量和大小分别为

$$\boldsymbol v_{\mathrm{rel}}=l\dot\theta\,\boldsymbol n,\qquad
v_{\mathrm{rel}}=l|\dot\theta|.$$

以下使用 $M=m+m'$、$\mu=m/M$。在 $m>0,m'>0$ 时，有 $0<\mu<1$。这一严格不等式在判定支持力时至关重要；不能先把 $m'=0$ 代入一个除以 $m'$ 得来的受力公式。

（2）无磁场时建立水平动量守恒式。

两端的重力和桌面支持力均竖直，杆力是系统内力，桌面不提供摩擦力。因此系统水平合外力为零。微扰取为无限小的位形扰动，初始水平动量为零，有

$$\begin{aligned}
P_x
&=m(\dot X-l\sin\theta\,\dot\theta)+m'\dot X\\
&=M\dot X-ml\sin\theta\,\dot\theta=0.
\end{aligned}$$

从而

$$\boxed{\dot X=\mu l\sin\theta\,\dot\theta.}$$

因为 $\dot\theta<0$，下端向左运动。上端水平速度为

$$v_{ux}=(\mu-1)l\sin\theta\,\dot\theta>0.$$

底端能移动是本题与“下端铰接的倒杆”的根本差别。若错误地设 $\dot X=0$，不仅能量中的动能项改变，后续杆力与支持力也会全部改变。

（3）展开总动能，消去底端速度。

先不使用任何转动惯量简式，直接写两质点的平动动能：

$$\begin{aligned}
K
&=\frac12m\left[(\dot X-l\sin\theta\,\dot\theta)^2
+l^2\cos^2\theta\,\dot\theta^2\right]
+\frac12m'\dot X^2\\
&=\frac12M\dot X^2
-ml\sin\theta\,\dot X\dot\theta
+\frac12ml^2\dot\theta^2.
\end{aligned}$$

这里将 $\sin^2\theta+\cos^2\theta=1$ 合并进最后一项。将 $\dot X=\mu l\sin\theta\,\dot\theta$ 代入：

$$\begin{aligned}
K
&=\frac12M\mu^2l^2\sin^2\theta\,\dot\theta^2
-m\mu l^2\sin^2\theta\,\dot\theta^2
+\frac12ml^2\dot\theta^2\\
&=\frac12m\mu l^2\sin^2\theta\,\dot\theta^2
-m\mu l^2\sin^2\theta\,\dot\theta^2
+\frac12ml^2\dot\theta^2\\
&=\frac12ml^2(1-\mu\sin^2\theta)\dot\theta^2.
\end{aligned}$$

第二行用了 $M\mu=m$。定义

$$s=\sin\theta,\qquad D=1-\mu s^2.$$

注意 $s$ 是角度的函数，不是固定数。$D>0$，所以约化动能始终为正。这也保证后面的除法在 $m'>0$、$0\le\theta\le\pi/2$ 内合法。

（4）用能量确定角速度，说明微扰极限。

下端高度固定，其重力势能不变；上端高度为 $l\sin\theta$。杆力对两质点的总功为零，桌面支持力与底端水平速度垂直，也不做功。因此总机械能守恒。

若先从 $\theta_i<\pi/2$ 静止释放，则初始势能为 $mgl\sin\theta_i$，精确能量式为

$$\frac12ml^2D\dot\theta^2
=mgl(\sin\theta_i-\sin\theta).$$

题设“竖直状态微扰”取 $\theta_i\to\pi/2$ 的极限，故

$$\boxed{\dot\theta^2=\frac{2g}{l}\frac{1-s}{D}.}$$

下降支应取

$$\dot\theta=-\sqrt{\frac{2g(1-s)}{lD}}.$$

恰好竖直且完全静止的系统可以永远停在不稳定平衡位置。上式描述的是微扰后已经进入倒下过程的极限轨迹，并不表示在完全无扰动的初态会自发运动。

（5）求角加速度，不遗漏角度相关系数。

将能量式写为

$$\frac12ml^2D\dot\theta^2+mgl\sin\theta=mgl.$$

对时间求导，逐项使用乘积法则和链式法则：

$$\begin{aligned}
0&=\frac12ml^2\dot D\,\dot\theta^2
+ml^2D\dot\theta\ddot\theta
+mgl\cos\theta\,\dot\theta,\\
\dot D&=-2\mu\sin\theta\cos\theta\,\dot\theta.
\end{aligned}$$

在已经运动、$\dot\theta\ne0$ 的区间除以 $ml^2\dot\theta$，得

$$D\ddot\theta-\mu\sin\theta\cos\theta\,\dot\theta^2
+\frac gl\cos\theta=0.$$

即

$$\boxed{\ddot\theta=
\frac{\mu s\cos\theta\,\dot\theta^2-(g/l)\cos\theta}{D}.}$$

初始端点的结果由连续极限给出，不能直接在 $\dot\theta=0$ 的瞬间把除法当成合法运算。此式中的第一项来自动能系数随杆角度变化，不能把 $D$ 当常量。

（6）由系统竖直运动求桌面支持力。

图 2-3 中，令杆的轴向力为有符号量 $T$，规定 $T>0$ 时杆拉上端向下端，上端受 $-T\boldsymbol e$，下端受 $+T\boldsymbol e$。$T<0$ 时杆处于压缩状态。杆是刚性杆，不是只能受拉的绳。

![图 2-3　两质点的重力、杆力及桌面支持力。](../figures/forces-02.png)

无磁场时，两质点系统的竖直外力为 $N-Mg$。下端竖直加速度为零，上端的竖直加速度为

$$a_{uy}=l(\cos\theta\,\ddot\theta-\sin\theta\,\dot\theta^2).$$

故

$$N=Mg+ml(\cos\theta\,\ddot\theta-s\dot\theta^2).$$

先将角加速度代入，暂不代入角速度：

$$\begin{aligned}
\frac{N}{Mg}
&=1+\mu\left[
\frac{\mu s\cos^2\theta(l\dot\theta^2/g)-\cos^2\theta}{D}
-s(l\dot\theta^2/g)\right]\\
&=1-\frac{\mu\cos^2\theta}{D}
+\frac{\mu s}{D}\left[\mu\cos^2\theta-D\right]
\frac{l\dot\theta^2}{g}.
\end{aligned}$$

因为

$$\mu\cos^2\theta-D
=\mu(1-s^2)-(1-\mu s^2)=\mu-1,$$

以及

$$1-\frac{\mu\cos^2\theta}{D}
=\frac{1-\mu}{D},$$

所以

$$\frac{N}{Mg}
=\frac{1-\mu}{D}
-\frac{\mu(1-\mu)s}{D}\frac{l\dot\theta^2}{g}.$$

再使用 $l\dot\theta^2/g=2(1-s)/D$，得到

$$\begin{aligned}
\frac{N}{Mg}
&=(1-\mu)\frac{D-2\mu s(1-s)}{D^2}\\
&=(1-\mu)\frac{1-\mu s^2-2\mu s+2\mu s^2}{D^2}\\
&=(1-\mu)\frac{1-\mu(2s-s^2)}{D^2}.
\end{aligned}$$

最后由 $M(1-\mu)=m'$，得

$$\boxed{N=m'g\,
\frac{1-\mu(2s-s^2)}{(1-\mu s^2)^2}.}$$

（7）独立用杆长约束与两端受力核对支持力。

这一核对不重新对能量求导。上端受力为

$$m\boldsymbol a_u=-T\boldsymbol e-mg\boldsymbol e_y.$$

下端的水平、竖直受力分别为

$$m'a_{bx}=T\cos\theta,\qquad
0=N+T\sin\theta-m'g.$$

由 $\boldsymbol r_u-\boldsymbol r_b=l\boldsymbol e$ 连续求两次导数，

$$\boldsymbol a_u-\boldsymbol a_b
=l\ddot\theta\,\boldsymbol n-l\dot\theta^2\boldsymbol e.$$

沿 $\boldsymbol e$ 投影，利用 $\boldsymbol e\cdot\boldsymbol n=0$，得到

$$\boldsymbol e\cdot(\boldsymbol a_u-\boldsymbol a_b)
=-l\dot\theta^2.$$

将受力式代入这个投影：

$$-\frac Tm-g\sin\theta-\frac{T\cos^2\theta}{m'}
=-l\dot\theta^2.$$

于是

$$T=\frac{l\dot\theta^2-gs}{1/m+\cos^2\theta/m'}
=\frac{mm'}{M D}(l\dot\theta^2-gs).$$

这里分母为 $1/m+\cos^2\theta/m'$，不是 $1/m+1/m'$，因为下端不能竖直加速。由下端竖直平衡，

$$\begin{aligned}
N&=m'g-Ts\\
&=m'g\left[1-\frac{\mu s}{D}
\left(\frac{l\dot\theta^2}{g}-s\right)\right]\\
&=\frac{m'g}{D}\left[1-\mu s\frac{l\dot\theta^2}{g}\right]\\
&=m'g\frac{1-\mu(2s-s^2)}{D^2}.
\end{aligned}$$

两条不同路线得到完全相同的结果。杆力由负变正并不等同于支持力变为零；必须比较 $Ts$ 与底端重量 $m'g$。

（8）检验临界质量是否存在，不能预设正根。

对于倒下阶段 $0\le s\le1$，

$$2s-s^2=1-(1-s)^2,\qquad 0\le2s-s^2\le1.$$

因此当 $m'>0$、$0<\mu<1$ 时，

$$1-\mu(2s-s^2)\ge1-\mu>0.$$

分母 $D^2>0$，故

$$\boxed{N>0\quad(m'>0,\ 0\le\theta\le\pi/2).}$$

由此可知，在“轻质杆、质量仅在端点、桌面光滑、从竖直微扰”的题设下，不存在正的临界质量。若直接令 $N=0$，会得到

$$2s-s^2=\frac1\mu>1,$$

而左边在允许区间最多为 $1$，所以这不是可以筛选的物理解。题目由 $m'=0$ 与 $m'\to\infty$ 两个极端推测中间必有正临界值，推测并不成立。

对 $m'\to0^+$，在任意固定 $0\le\theta<\pi/2$ 处有 $N\to0$；但这一极限不能提供唯一的 $\theta_0$。当底端本身没有质量、无磁场、杆端约束只维持几何连接时，杆力和支持力可均为零。若把 $m_c=0$ 称为边界值，则支持力在整个运动区间为零，而不是在某一唯一角度首次归零。因此第一问的严格结论是：没有正临界质量，也没有题设所要求的唯一 $\theta_0$。

两个端点检验为

$$\lim_{\theta\to\pi/2}N=Mg,\qquad N(0)=m'g.$$

上端接近竖直静态时通过杆把自身重量传给底端，因此支持力接近两质点总重；杆水平时杆力没有竖直分量，支持力等于底端重量。这与受力图一致。

（9）加入磁场，先确定洛伦兹力方向。

第二问仍取 $m,m'>0$。令 $\boldsymbol B=B\boldsymbol e_z$、$q>0$。对任意平面速度 $\boldsymbol v=(v_x,v_y,0)$，

$$q\boldsymbol v\times\boldsymbol B
=qB(v_y,-v_x,0).$$

图 2-4 中磁场垂直纸面向外，运动中的正电荷所受磁场力是把速度顺时针转过 $90^\circ$ 后乘以 $qB$。下端水平运动，因此其磁场力竖直；上端的竖直速度则产生水平磁场力。

![图 2-4　向外磁场中两端速度与洛伦兹力的正交关系。](../figures/magnetic-02.png)

磁场力不做功，因为每个质点都满足

$$\boldsymbol F_B\cdot\boldsymbol v
=q(\boldsymbol v\times\boldsymbol B)\cdot\boldsymbol v=0.$$

桌面支持力仍不做功。因此本问的能量守恒式与前问相同；发生变化的是水平动量关系。

（10）从水平合外力积分得到正确的守恒组合。

下端的 $v_{by}=0$，两质点系统的水平磁场力为

$$F_{x,\mathrm{ext}}
=qB(v_{uy}+v_{by})
=qBl\cos\theta\,\dot\theta.$$

于是

$$\frac{dP_x}{dt}=qBl\frac{d(\sin\theta)}{dt}.$$

移项后，

$$\frac d{dt}(P_x-qBl\sin\theta)=0.$$

在竖直静止微扰极限，初始 $P_x=0$、$\sin\theta=1$，故

$$\boxed{P_x-qBl\sin\theta=-qBl.}$$

代入两质点水平动量的表达式：

$$M\dot X-mls\dot\theta=qBl(s-1),$$

即

$$\boxed{\dot X=\mu ls\dot\theta+\frac{qBl}{M}(s-1).}$$

右边第二项是磁场产生的共同横向漂移。它不能被遗漏，也不能把原来的 $P_x=0$ 继续用于带磁场的运动。若从有限初角 $\theta_i$ 静止释放，只需把 $(s-1)$ 换成 $(s-\sin\theta_i)$。

（11）用配方区分共同运动能量与相对运动能量。

动能的未消元表达式仍为

$$K=\frac12M\dot X^2-mls\dot X\dot\theta
+\frac12ml^2\dot\theta^2.$$

此处用平方配方法，而不是把 $\dot X$ 的两项逐项展开后省略交叉项：

$$\begin{aligned}
K
&=\frac12M(\dot X-\mu ls\dot\theta)^2
+\frac12ml^2\dot\theta^2
-\frac12M\mu^2l^2s^2\dot\theta^2\\
&=\frac12M(\dot X-\mu ls\dot\theta)^2
+\frac12ml^2D\dot\theta^2.
\end{aligned}$$

由第（10）步，

$$\dot X-\mu ls\dot\theta=\frac{qBl}{M}(s-1).$$

所以

$$K=\frac{q^2B^2l^2}{2M}(1-s)^2
+\frac12ml^2D\dot\theta^2.$$

第一项是横向共同运动所消耗的动能；第二项对应杆姿态变化。磁场不做功，但它可以使同样的势能下降分配给不同类型的运动。这正是最终相对速度中出现磁场减项的物理原因。

（12）与能量联立，逐项消元得到相对速度。

上端的势能下降为 $mgl(1-s)$，故

$$\frac{q^2B^2l^2}{2M}(1-s)^2
+\frac12ml^2D\dot\theta^2=mgl(1-s).$$

先把第一项移到右边，再乘以 $2/m$：

$$l^2D\dot\theta^2
=2gl(1-s)-\frac{q^2B^2l^2}{mM}(1-s)^2.$$

因为 $v_{\mathrm{rel}}^2=l^2\dot\theta^2$，得到

$$\boxed{
v_{\mathrm{rel}}=
\sqrt{
\frac{2gl(1-\sin\theta)
-\dfrac{q^2B^2l^2}{m(m+m')}(1-\sin\theta)^2}
{1-\dfrac{m}{m+m'}\sin^2\theta}
}.}$$

这给出相对速率。若要求相对速度矢量，在首次倒下的下降支有

$$\boxed{\boldsymbol v_u-\boldsymbol v_b
=-v_{\mathrm{rel}}\,\boldsymbol n.}$$

杆向右倒时，$\boldsymbol n$ 指向左上方，相对速度因而指向右下方。一个是有方向的矢量，另一个是非负速率，不能把二者的负号混写。

（13）核对实根条件和桌面接触条件。

分母 $D>0$。令 $w=1-\sin\theta\ge0$，根号分子为

$$w\left(2gl-\frac{q^2B^2l^2}{mM}w\right).$$

当 $qB\ne0$，要求

$$0\le w\le\frac{2mMg}{q^2B^2l}.$$

若上界小于 $1$，杆可能在到达水平前出现角速度为零的转折；不能把负的根号分子解释成新的倒下速度。转折之后 $\dot\theta$ 的符号需要按实际运动重新选择。

另外，公式的推导假定底端竖直加速度为零，故必须检验支持力。加入磁场后的两端受力为

$$\begin{aligned}
m\boldsymbol a_u&=qB(v_{uy},-v_{ux})
-T\boldsymbol e-mg\boldsymbol e_y,\\
m'a_{bx}&=T\cos\theta,\\
0&=N+T\sin\theta-m'g-qB\dot X.
\end{aligned}$$

沿杆投影相对加速度，逐项计算磁场力的投影：

$$\cos\theta\,v_{uy}-\sin\theta\,v_{ux}
=l\dot\theta-\sin\theta\,\dot X.$$

于是杆力满足

$$\boxed{
T=\frac{
l\dot\theta^2-g\sin\theta
+\dfrac{qB}{m}(l\dot\theta-\sin\theta\,\dot X)}
{1/m+\cos^2\theta/m'}
},$$

支持力为

$$\boxed{N=m'g+qB\dot X-T\sin\theta.}$$

由前面已求出的 $\dot\theta$、$\dot X$ 可逐一计算 $T,N$。只有 $N\ge0$ 的区间才与桌面约束相容。一旦计算要求 $N<0$，说明桌面必须向下“拉住”底端，而普通接触面不能做到，底端应离地；离地以后不能继续使用本题的约化坐标和相对速度公式。

（14）检查量纲、无磁场极限和极重底端极限。

$qB$ 的量纲为 $\mathrm{kg\,s^{-1}}$，故

$$\frac{q^2B^2l^2}{mM}$$

的量纲为 $\mathrm{m^2\,s^{-2}}$，与 $gl$ 一致，整个根号确实给出速度。取 $B\to0$，第二问退化为

$$v_{\mathrm{rel}}^2=\frac{2gl(1-\sin\theta)}
{1-\mu\sin^2\theta},$$

与第一问由能量得到的 $l^2\dot\theta^2$ 相同。取 $m'\to\infty$，则 $\mu\to0$、磁场共同漂移动能趋于零，得到

$$v_{\mathrm{rel}}^2\to2gl(1-\sin\theta).$$

这是上端绕近似固定的下端下降、势能直接变为其动能的结果。两个极限都支持前面的消元路线，但不替代对 $N$ 的实际接触检查。

## 六、关键洞察

一个关于临界值的叙述本身不是证明。本题无磁场支持力可整理成“正的质量因子、正的分母、严格正的括号”三部分，这比解高次方程更直接。先判断允许区间内表达式的符号，可以避免给一个不存在的临界值编造数值。

带磁场时，能量守恒与机械动量不守恒可以同时成立。总水平磁场力是 $qBl\,d(\sin\theta)/dt$，所以真正的常量是 $P_x-qBl\sin\theta$。配方后的动能把磁场引起的共同漂移单独列出，说明它占用势能下降所释放的能量，使角度变化的速率减小。

还可对有限初角检验第一问结论。设 $s_i=\sin\theta_i\le1$，初态静止，则

$$\dot\theta^2=\frac{2g(s_i-s)}{lD}.$$

由独立杆力路线可得

$$N=m'g\frac{D-2\mu s(s_i-s)}{D^2}
=m'g\frac{1+\mu s^2-2\mu ss_i}{D^2}.$$

分子也可写成

$$1-\mu s_i^2+\mu(s-s_i)^2>0.$$

因此从任意第一象限初角静止释放，正质量底端仍不因这一模型而离地。异常不是“微扰极限取错一点点”造成的。

## 七、易错点

把轻杆换成均匀杆，会增加连续质量的惯性和重力作用，已是另一道题。把光滑桌面上的下端当作铰点，会错误地消去底端动能。杆力必须允许正负；一旦把杆当成只能受拉的绳，就会在初始压缩阶段错误地宣布约束失效。

支持力为零与杆力为零不是同一条件。无磁场时 $N=m'g-Ts$，杆力已经变为拉力也可能仍不足以抵消底端重量。带磁场时还有 $qB\dot X$ 项；遗漏底端的竖直磁场力，可能得到正确的相对速度却错误判断离地。

不能将 $m'=0$、$\theta=\pi/2$ 同时硬代入含 $D$ 的约化式：此时 $D$ 可能为零，运动变量选择退化。也不能把 $B\to0$ 与“带电无质量质点”的极限随意交换。第二问的公式适用于两个质量均为正且仍接触桌面的阶段。

## 八、课堂讲解建议

先让学生根据图 2-2 写出两个质点的速度，而不要直接给出转动动能。板书保留 $\dot X$ 与 $\dot\theta$ 两个变量，让学生看见水平动量守恒怎样消掉一个变量，再用平方配方检查动能。

得到支持力公式后，让学生先求 $2s-s^2$ 在 $[0,1]$ 的最大值，再讨论有没有正临界质量。这一步可以训练“先检验问题前提，再计算答案”的习惯，而不是把题干的推测当成不可质疑的定理。

讲第二问时，先画出正电荷速度对应的洛伦兹力，分别指出上端的水平磁场力与下端的竖直磁场力。然后将水平合力写成一个全导数，让学生自己识别守恒组合；最后比较配方后的两种动能，解释磁场不做功却能改变相对速率的原因。

## 九、变式训练

变式一：无磁场，杆从 $\theta_i=\pi/3$ 静止释放，两端质量相等。求杆水平时的相对速率与支持力。

此时 $\mu=1/2$、$s_i=\sqrt3/2$。杆水平时 $s=0,D=1$，能量给出

$$v_{\mathrm{rel}}^2=2gls_i=\sqrt3\,gl,\qquad
v_{\mathrm{rel}}=\sqrt{\sqrt3\,gl}.$$

杆水平时杆力无竖直分量，所以

$$N=m'g=mg.$$

全程是否接触可用有限初角式检查：

$$1-\mu s_i^2+\mu(s-s_i)^2
=\frac58+\frac12\left(s-\frac{\sqrt3}2\right)^2>0.$$

因此从初角到水平期间底端不离地，所求末态公式适用。

变式二：保持第二问的磁场和约束，上端电荷为 $q_u$，下端电荷为 $q_b$，均为有符号电荷。求相对速率是否只与两电荷之和有关。

下端竖直速度为零，其水平洛伦兹力为零。水平总外力因此仍只来自上端：

$$\frac{dP_x}{dt}=q_uBl\cos\theta\,\dot\theta.$$

故

$$P_x-q_uBl\sin\theta=-q_uBl,\qquad
\dot X=\mu ls\dot\theta+\frac{q_uBl}{M}(s-1).$$

两个磁场力各自不做功，同样配方得到

$$v_{\mathrm{rel}}^2=
\frac{2gl(1-s)-q_u^2B^2l^2(1-s)^2/(mM)}{D}.$$

所以在维持桌面接触的阶段，相对速率不是由 $q_u+q_b$ 决定，而只含上端电荷 $q_u$。但接触条件不同：下端竖直平衡变为

$$N=m'g+q_bB\dot X-Ts,$$

其中

$$T=\frac{l\dot\theta^2-gs+
(q_uB/m)(l\dot\theta-s\dot X)}
{1/m+\cos^2\theta/m'}.$$

改变 $q_b$ 会改变支持力及离地角，因此“约束阶段内的速率公式不含 $q_b$”不等于“整个运动完全不受 $q_b$ 影响”。相对速度表达式和它的适用区间必须分开讨论。

例如取 $m=m'=1\,\mathrm{kg}$、$l=1\,\mathrm m$、$g=1\,\mathrm{m\,s^{-2}}$、$q_uB=0.2\,\mathrm{kg\,s^{-1}}$，考察 $\theta=\pi/6$ 的下降支。此时 $s=1/2,D=7/8$，逐项代入得

$$\begin{aligned}
\dot\theta&=-\sqrt{\frac{1-0.005}{0.875}}
=-1.066369\,\mathrm{s^{-1}},\\
\dot X&=\frac14\dot\theta-0.05\,\mathrm{m\,s^{-1}}
=-0.316592\,\mathrm{m\,s^{-1}},\\
T&=\frac{1.137143-0.5+0.2(-1.066369+0.158296)}{1.75}
\,\mathrm N=0.260302\,\mathrm N.
\end{aligned}$$

以 $b=q_bB/(1\,\mathrm{kg\,s^{-1}})$ 表示下端磁场参数的数值，则

$$N=(0.869849-0.316592b)\,\mathrm N.$$

若 $b=0.2$，这一角度处 $N=0.806531\,\mathrm N>0$；若 $b>2.74754$，假定仍接触桌面会算出负支持力，表明实际轨迹已不能继续使用该约束。后一结论只判定该角度处的接触相容性，不把 $2.74754$ 冒称为全程首次离地的临界参数；求首次离地必须沿实际下降轨迹找到最早的 $N=0$。

变式三：无磁场，两端质量相等，杆从近竖直静止状态倒下。求杆与桌面夹角$\theta=\pi/6$时的支持力，并与底端自身重力比较。

解：令$\mu=m/(m+m')=1/2$、$s=\sin\theta=1/2$，已核对的支持力为$N=m'g[1-\mu(2s-s^2)]/(1-\mu s^2)^2$。代入得$N=mg(5/8)/(7/8)^2=40mg/49$，小于$mg$而仍为正。小于自重表示杆对下端有向上的分力，并不表示已经离开桌面。整个倒下区间支持力不为零，所以不能由某个较小的数值推出正临界质量。

变式四：有磁场时上端电荷为$q$，两端总质量为$M=m+m'$。从竖直静止的微扰极限释放，求能到达水平姿态所需的$|qB|$上界。

解：记$k=qB$，下降支的相对速率平方为$[2gl(1-s)-k^2l^2(1-s)^2/(mM)]/[1-(m/M)s^2]$。分母对$m'>0$为正，分子中的额外因子随$1-s$增大而减小。要使全程直到$s=0$仍可达，要求$k^2\leq2gmM/l$，即$|qB|\leq\sqrt{2gmM/l}$。等号时水平姿态相对速度为零；严格小于时到达水平仍有非零速度。接触支持力还须独立检查，这个能量判据本身不保证任意下端电荷时均不离地。
