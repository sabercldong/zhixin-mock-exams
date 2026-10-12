# 第 1 题

一个内、外半径分别为 $r$ 和 $2r$ 的同轴圆筒放在水平地面上，截面圆心为 $C$。地面上的 $A$ 点铰接一根细杆，杆始终与内圆相切，接触位置记为 $B$。在所考察时刻，杆与地面的夹角为 $45^\circ$，杆顺时针转动的角速度为 $\omega$、角加速度为 $\beta$。杆与内圆接触处不滑动，外圆与地面之间可以滑动。

（1）求接触点 $B$ 沿杆的速度分量 $v_{B\tau}$ 和垂直于杆的速度分量 $v_{Bn}$。

（2）求接触点 $B$ 沿杆的加速度分量 $a_{B\tau}$ 和垂直于杆的加速度分量 $a_{Bn}$。

（3）求圆心 $C$ 的速度 $v_C$ 和加速度 $a_C$。

![图 1-1　圆筒截面、地面铰接杆与内圆的相切位置。](../figures/question-01.png)

## 一、题型定位

带移动接触位置的刚体平面运动。外圆半径确定圆心高度，内圆半径确定杆的切线几何；二者作用不同。内圆与杆无滑动提供材料点的速度约束，外圆与地面可滑动，不能另加纯滚动约束。求加速度时，必须说明 $B$ 是哪一个刚体上的材料点，还是随时间迁移的几何接触位置。

## 二、知识点

相切时半径与切线垂直；转动基矢的时间导数；定轴转动的切向与法向加速度；刚体上两点的速度、加速度关系；无滑动接触的瞬时速度相等；对迁移位置求导与追踪材料点求导的区别；三角函数求导及角速度、角加速度的符号约定。

## 三、物理图像

杆顺时针压低时，圆筒为了维持相切关系向右移动。圆心只能水平运动，但圆筒同时转动。此刻在接触位置相遇的杆材料点与圆筒材料点速度相同；稍后原来的这两个材料点分别离开接触位置，新的材料点在另一位置相遇。几何接触位置并不是持续属于某一个刚体的固定点，因此“接触点速度”和“接触点加速度”不能不加定义地混用。

## 四、解题入口

先以任意夹角 $\theta$ 建立相切几何，求 $C$ 的坐标及其两次时间导数。再使用接触处无滑动条件求圆筒角速度 $\Omega$ 和角加速度 $\alpha$，最后把刚体加速度投影到杆向与法向。全程保留 $\theta$，完成求导后才代入 $\theta=\pi/4$；先代入定值再求导会丢失杆在转动这一事实。

## 五、解析

（1）明确研究对象、坐标和正方向。

取 $A$ 为原点，$x$ 轴水平向右、$y$ 轴竖直向上，$\boldsymbol e_z$ 垂直纸面向外。杆与 $+x$ 轴的夹角为 $\theta$。沿杆由 $A$ 指向 $B$ 的单位矢量以及它左侧的法向单位矢量分别为

$$\boldsymbol\tau=(\cos\theta,\sin\theta),\qquad
\boldsymbol n=(-\sin\theta,\cos\theta).$$

于是 $\boldsymbol e_z\times\boldsymbol\tau=\boldsymbol n$，$\boldsymbol e_z\times\boldsymbol n=-\boldsymbol\tau$。本题的杆沿顺时针转动，因此

$$\dot\theta=-\omega,\qquad \ddot\theta=-\beta.$$

这里 $\omega>0$ 表示顺时针角速率，$\beta$ 是顺时针角加速度的有符号分量；减速时 $\beta$ 可以为负。圆筒的 $\Omega$、$\alpha$ 则按逆时针为正，不能把它们直接等同于杆的 $\omega$、$\beta$。

把圆筒上此刻到达接触位置的材料点记为 $B_c$，杆上此刻在该位置的材料点记为 $B_r$，随时间改变的几何接触位置记为 $B_g$。第（1）问两材料点速度相同，答案没有区别。第（2）问先给出圆筒材料点 $B_c$ 的加速度，再完整列出另两种点定义的结果。

（2）建立几何关系，确定 $AB$ 与圆心横坐标。

令瞬时接触距离 $AB_g=s$。图 1-2 中，$CB_g=r$ 且垂直于杆，圆心位于杆的右下方。故

$$\boldsymbol r_{B_g}=s\boldsymbol\tau,\qquad
\boldsymbol r_C=s\boldsymbol\tau-r\boldsymbol n.$$

![图 1-2　切线距离、内圆半径以及圆心的固定高度。](../figures/geometry-01.png)

外圆接触水平地面，圆心高度恒为 $2r$。将矢量式分别投影到两坐标轴：

$$x_C=s\cos\theta+r\sin\theta,\qquad
y_C=s\sin\theta-r\cos\theta=2r.$$

从竖直式解出 $s$：

$$s\sin\theta=2r+r\cos\theta,\qquad
s=r\frac{2+\cos\theta}{\sin\theta}.$$

再代回水平式，逐步通分：

$$\begin{aligned}
x_C
&=r\frac{(2+\cos\theta)\cos\theta}{\sin\theta}
+r\sin\theta\\
&=r\frac{2\cos\theta+\cos^2\theta+\sin^2\theta}{\sin\theta}\\
&=r\frac{2\cos\theta+1}{\sin\theta}.
\end{aligned}$$

所用数学关系是 $\sin^2\theta+\cos^2\theta=1$。在所考察的时刻，

$$s_0=r(1+2\sqrt2),\qquad x_C=r(2+\sqrt2),\qquad y_C=2r.$$

$s_0$ 是当时的几何接触距离，不意味着随后的接触位置仍固定在杆的这个材料点上。

（3）先对角度求导，再对时间求导，得到圆心速度。

对 $x_C(\theta)$ 使用商法则：

$$\begin{aligned}
\frac{dx_C}{d\theta}
&=r\frac{(-2\sin\theta)\sin\theta-(2\cos\theta+1)\cos\theta}
{\sin^2\theta}\\
&=-r\frac{2\sin^2\theta+2\cos^2\theta+\cos\theta}{\sin^2\theta}\\
&=-r\frac{2+\cos\theta}{\sin^2\theta}.
\end{aligned}$$

由链式法则 $\dot x_C=(dx_C/d\theta)\dot\theta$：

$$\dot x_C=r\omega\frac{2+\cos\theta}{\sin^2\theta}.$$

圆心竖直速度为零。代入 $\sin\theta=\cos\theta=1/\sqrt2$：

$$\boxed{\boldsymbol v_C=r(4+\sqrt2)\omega\,\boldsymbol e_x.}$$

结果向右，符合杆顺时针压低、圆筒右移的几何图像。此处用的是相切约束，不是外圆纯滚动关系 $v_C=2r\Omega$。

（4）求圆心加速度，保留两种来源。

再次对角度求导：

$$\begin{aligned}
\frac{d^2x_C}{d\theta^2}
&=-r\frac{d}{d\theta}\left[(2+\cos\theta)\sin^{-2}\theta\right]\\
&=\frac r{\sin\theta}
+\frac{2r(2+\cos\theta)\cos\theta}{\sin^3\theta}.
\end{aligned}$$

链式法则的二阶形式为

$$\ddot x_C=\frac{d^2x_C}{d\theta^2}\dot\theta^2+
\frac{dx_C}{d\theta}\ddot\theta.$$

第一项来自几何关系对角度的非线性，第二项来自杆角速率本身的变化。即使 $\beta=0$，第一项也不为零。代入 $\dot\theta=-\omega$、$\ddot\theta=-\beta$：

$$\ddot x_C=
r\left[
\frac1{\sin\theta}+
\frac{2(2+\cos\theta)\cos\theta}{\sin^3\theta}
\right]\omega^2
+r\frac{2+\cos\theta}{\sin^2\theta}\beta.$$

在 $\theta=\pi/4$，

$$\frac1{\sin\theta}=\sqrt2,\qquad
\frac{2(2+\cos\theta)\cos\theta}{\sin^3\theta}
=4\left(2+\frac1{\sqrt2}\right)=8+2\sqrt2.$$

所以

$$\boxed{\boldsymbol a_C=
r\big[(8+3\sqrt2)\omega^2+(4+\sqrt2)\beta\big]\boldsymbol e_x.}$$

这也给出第（3）问的完整有符号结果；若只要求加速度大小，应在方括号外取绝对值，而不能预先假设 $\beta$ 必为正。

（5）利用无滑动条件求材料接触点速度。

杆绕固定 $A$ 转动。此刻杆材料点 $B_r$ 距铰点 $s_0$，其速度为

$$\boldsymbol v_{B_r}=\dot\theta\,\boldsymbol e_z\times
(s_0\boldsymbol\tau)=-s_0\omega\boldsymbol n.$$

因此沿杆分量为零、法向分量为负。内圆无滑动要求此刻

$$\boldsymbol v_{B_c}=\boldsymbol v_{B_r},$$

故第（1）问为

$$\boxed{v_{B\tau}=0,\qquad v_{Bn}=-r(1+2\sqrt2)\omega.}$$

负法向指向杆的右下方。这是运动学分量的正负号，不表示接触处发生穿透。两个物体在接触处具有同一法向速度，仍能保持接触。

（6）从圆筒刚体速度关系确定 $\Omega$。

圆筒上 $B_c$ 相对于圆心的位置为 $r\boldsymbol n$。刚体速度关系为

$$\boldsymbol v_{B_c}=\dot x_C\boldsymbol e_x+
\Omega\boldsymbol e_z\times(r\boldsymbol n)
=\dot x_C\boldsymbol e_x-r\Omega\boldsymbol\tau.$$

图 1-3 分别表示接触处材料点的共同速度与几何位置沿杆的迁移速率。沿杆的绿色箭头表示更换接触材料点的速率，不是杆材料点的附加速度；它将在求几何位置的导数时使用。

![图 1-3　同一接触位置的两材料点与沿杆迁移的几何位置。](../figures/materials-01.png)

由于

$$\boldsymbol e_x=\cos\theta\,\boldsymbol\tau-
\sin\theta\,\boldsymbol n,$$

可得

$$v_{B_c,\tau}=\dot x_C\cos\theta-r\Omega,\qquad
v_{B_c,n}=-\dot x_C\sin\theta.$$

无滑动要求第一式为零：

$$\Omega=\frac{\dot x_C\cos\theta}{r}
=\omega\frac{(2+\cos\theta)\cos\theta}{\sin^2\theta}.$$

于是

$$\boxed{\Omega=(1+2\sqrt2)\omega.}$$

这是逆时针转动；它与杆的顺时针转动方向相反。第二式同时核对法向相容性：

$$-\dot x_C\sin\theta
=-r\omega\frac{2+\cos\theta}{\sin\theta}
=-s\omega.$$

无滑动条件与相切几何给出一致的法向速度，说明前面没有把内、外半径用反。

（7）对 $\Omega(\theta,\omega)$ 完整求导，得到圆筒角加速度。

令

$$F(\theta)=\frac{(2+\cos\theta)\cos\theta}{\sin^2\theta},\qquad
\Omega=\omega F(\theta).$$

则乘积与链式法则给出

$$\alpha=\dot\Omega=\beta F(\theta)+\omega F'(\theta)\dot\theta
=\beta F(\theta)-\omega^2F'(\theta).$$

把 $F=(2\cos\theta+\cos^2\theta)\sin^{-2}\theta$ 求导：

$$F'(\theta)=
-\frac{2(1+\cos\theta)}{\sin\theta}
-\frac{2(2\cos\theta+\cos^2\theta)\cos\theta}{\sin^3\theta}.$$

在 $\theta=\pi/4$，两项依次为 $-2\sqrt2-2$ 与 $-4\sqrt2-2$，因此

$$F'(\pi/4)=-4-6\sqrt2,$$

$$\boxed{\alpha=(1+2\sqrt2)\beta+(4+6\sqrt2)\omega^2.}$$

不能把瞬时等式 $\Omega=(1+2\sqrt2)\omega$ 当成在所有时刻系数恒定的关系，再写 $\alpha=(1+2\sqrt2)\beta$。系数来自不断变化的角度，漏掉其导数就漏掉后一项。

（8）用刚体加速度公式求圆筒材料点 $B_c$。

圆筒上的固定材料点满足

$$\boldsymbol a_{B_c}=\boldsymbol a_C+
\alpha\boldsymbol e_z\times(r\boldsymbol n)
+\Omega\boldsymbol e_z\times
\big[\Omega\boldsymbol e_z\times(r\boldsymbol n)\big].$$

第二项为切向加速度，第三项为指向圆心的向心加速度。利用两个叉乘方向：

$$\boldsymbol a_{B_c}=a_C\boldsymbol e_x-r\alpha\boldsymbol\tau
-r\Omega^2\boldsymbol n.$$

图 1-4 将三项分别表示。图中的 $a_C$ 为有符号水平分量，示意箭头对应 $a_C>0$；计算仍使用上一步的有符号表达式。

![图 1-4　圆筒材料点加速度的平动、切向和向心贡献。](../figures/accelerations-01.png)

沿 $\boldsymbol\tau$ 和 $\boldsymbol n$ 投影：

$$a_{B_c,\tau}=a_C\cos\theta-r\alpha,\qquad
a_{B_c,n}=-a_C\sin\theta-r\Omega^2.$$

先算沿杆分量。在 $\theta=\pi/4$，

$$\begin{aligned}
a_C\cos\theta
&=r\big[(4\sqrt2+3)\omega^2+(2\sqrt2+1)\beta\big],\\
r\alpha
&=r\big[(4+6\sqrt2)\omega^2+(1+2\sqrt2)\beta\big].
\end{aligned}$$

相减时 $\beta$ 项抵消：

$$\boxed{a_{B_c,\tau}=-r(1+2\sqrt2)\omega^2.}$$

法向分量则是两项相加后的负号。注意

$$\Omega^2=(1+2\sqrt2)^2\omega^2=(9+4\sqrt2)\omega^2.$$

所以

$$\begin{aligned}
a_{B_c,n}
&=-r\big[(4\sqrt2+3)\omega^2+(2\sqrt2+1)\beta
+(9+4\sqrt2)\omega^2\big]\\
&=\boxed{-r\big[(12+8\sqrt2)\omega^2+(1+2\sqrt2)\beta\big]}.
\end{aligned}$$

这两个分量是第（2）问按“圆筒材料接触点”理解时的答案。它们不是几何接触位置的二阶导数。

（9）给出杆材料点的加速度，解释题目点定义的区别。

杆上此刻到达 $B$ 的固定材料点距 $A$ 为 $s_0$。对这个材料点追踪时距离不变，其加速度是

$$\boldsymbol a_{B_r}=
-s_0\omega^2\boldsymbol\tau-s_0\beta\boldsymbol n.$$

因此

$$\boxed{a_{B_r,\tau}=-r(1+2\sqrt2)\omega^2,\qquad
a_{B_r,n}=-r(1+2\sqrt2)\beta.}$$

两材料点的沿杆加速度相同，法向加速度不同：

$$\boxed{\boldsymbol a_{B_c}-\boldsymbol a_{B_r}
=-r(12+8\sqrt2)\omega^2\boldsymbol n.}$$

这不与速度相同矛盾。“此刻这两个材料点速度相同”是瞬时约束，不是说以后仍由同一对材料点持续接触；不能在忽略材料点更换的情况下对该等式求导。

（10）若求的是几何接触位置 $B_g$，必须保留 $s(t)$ 的变化。

由 $s=r(2+\cos\theta)/\sin\theta$：

$$\frac{ds}{d\theta}=-r\frac{1+2\cos\theta}{\sin^2\theta},$$

$$\dot s=r\omega\frac{1+2\cos\theta}{\sin^2\theta},\qquad
\dot s\big|_{\pi/4}=r(2+2\sqrt2)\omega.$$

对 $\boldsymbol r_{B_g}=s\boldsymbol\tau$ 使用乘积法则：

$$\boldsymbol v_{B_g}=\dot s\boldsymbol\tau+s\dot\theta\boldsymbol n
=\dot s\boldsymbol\tau-s\omega\boldsymbol n.$$

所以几何位置的沿杆速度不为零；该分量正是接触位置沿杆的迁移速率，不是相对滑动速度。

再次求导：

$$\boldsymbol a_{B_g}=(\ddot s-s\omega^2)\boldsymbol\tau
-(2\dot s\omega+s\beta)\boldsymbol n.$$

其中 $2\dot s\omega$ 来自两个乘积项，各贡献一次 $\dot s\omega$。在本时刻，

$$\ddot s=r\big[(4+6\sqrt2)\omega^2+(2+2\sqrt2)\beta\big].$$

得到第三种点定义的结果：

$$\boxed{\begin{aligned}
v_{B_g,\tau}&=r(2+2\sqrt2)\omega,\\
v_{B_g,n}&=-r(1+2\sqrt2)\omega,\\
a_{B_g,\tau}&=r\big[(3+4\sqrt2)\omega^2+(2+2\sqrt2)\beta\big],\\
a_{B_g,n}&=-r\big[(4+4\sqrt2)\omega^2+(1+2\sqrt2)\beta\big].
\end{aligned}}$$

第（2）问应分别声明两个刚体材料点和几何接触位置的定义，不能把三套结果混合为一个“接触点加速度”。

（11）用量纲、静止瞬间与接触相容性检验。

所有速度项为 $r\omega$，量纲是长度每时间；所有加速度项为 $r\omega^2$ 或 $r\beta$，量纲是长度每时间平方。若 $\omega=0$、$\beta\ne0$，两材料点速度都为零，但加速度仍可非零；此时法向加速度差也为零，因为迁移速率与角速度之积消失。若 $\beta=0$、$\omega\ne0$，圆心仍有加速度，圆筒也有角加速度，说明“杆匀速转动”不等于“整个系统所有速度恒定”。

还可以直接检验外圆底点速度。底点相对圆心的位置为 $-2r\boldsymbol e_y$，故其水平速度为

$$v_{\mathrm{bottom},x}=v_C+2r\Omega
=r(6+5\sqrt2)\omega.$$

它不为零，恰好符合题设外圆在地面滑动。若错误地追加底点静止条件，将与已经满足的内圆相切和无滑动约束发生矛盾。

## 六、关键洞察

“点的位置”与“物体上固定点的位置”是不同的函数。几何接触位置有沿杆迁移速度，材料接触点却可以没有沿杆速度。加速度差来自迁移过程中对速度场的取样变化，而不是来自接触处突然发生滑动。

可从速度场的空间变化再核对加速度差。几何位置相对任一材料速度场的迁移速度都是 $\dot s\boldsymbol\tau$。沿几何接触位置对相同的两个速度场求全导数，得到

$$\boldsymbol a_{B_c}+\Omega\boldsymbol e_z\times(\dot s\boldsymbol\tau)
=\boldsymbol a_{B_r}+\dot\theta\boldsymbol e_z\times(\dot s\boldsymbol\tau).$$

因此

$$\boldsymbol a_{B_c}-\boldsymbol a_{B_r}
=-(\omega+\Omega)\dot s\,\boldsymbol n.$$

代入 $\omega+\Omega=2(1+\sqrt2)\omega$、$\dot s=2r(1+\sqrt2)\omega$，得到 $-4r(1+\sqrt2)^2\omega^2\boldsymbol n=-r(12+8\sqrt2)\omega^2\boldsymbol n$，与刚体加速度路线一致。两条路线的出发点不同，因而是有效的交叉检验。

## 七、易错点

把地面可滑动改成纯滚动，会多加一个不存在的约束。把内半径 $r$ 写成外半径 $2r$，会同时破坏切线关系和圆筒接触点的转动速度。把顺时针 $\omega$ 当成逆时针有符号角速度，会使速度、角加速度和法向分量的符号相互冲突。

先把 $\theta$ 固定为 $45^\circ$ 再求导，相当于错误地宣布杆不再转动。对瞬时比例 $\Omega=(1+2\sqrt2)\omega$ 直接求导会漏掉几何系数变化。最隐蔽的错误是把 $\boldsymbol v_{B_c}=\boldsymbol v_{B_r}$ 当成同一对材料点在一个时间区间内的等式，从而断言加速度也相同。

## 八、课堂讲解建议

先在图1-1上用两种颜色各标一个接触材料点，让学生说明短时间后这两个点是否还相遇，再引入第三个几何点。板书分成几何、圆心平动、材料点转动三列，避免将 $s(t)$ 与固定材料距离混写。

求导前要求学生写出 $\dot\theta=-\omega$ 和 $\ddot\theta=-\beta$。讲解时可先令 $\beta=0$，让学生用图1-4解释为何圆心加速度和接触材料点加速度仍不为零。最后用外圆底点滑动速度检验，帮助学生识别“看见轮子就写纯滚动”的惯性误判。

## 九、变式训练

变式一：内半径仍为 $r$，外半径改为一般的 $R>r$，其余条件不变。求任意夹角 $\theta$ 下圆心速度以及圆筒角速度，并说明几何高度如何进入结果。

解：圆心高度改为 $R$，相切关系成为 $s\sin\theta-r\cos\theta=R$。因此

$$s=\frac{R+r\cos\theta}{\sin\theta},\qquad
x_C=\frac{R\cos\theta+r}{\sin\theta}.$$

商法则给出

$$\frac{dx_C}{d\theta}
=-\frac{R+r\cos\theta}{\sin^2\theta},\qquad
v_C=\omega\frac{R+r\cos\theta}{\sin^2\theta}.$$

材料点无滑动仍要求 $v_C\cos\theta-r\Omega=0$，所以

$$\boxed{\Omega=\omega\frac{(R+r\cos\theta)\cos\theta}{r\sin^2\theta}.}$$

法向速度检验为 $-v_C\sin\theta=-s\omega$。代入 $R=2r$、$\theta=\pi/4$ 恢复本题。外半径仅通过圆心高度及平动几何进入，内半径则同时进入切线偏移和材料点转动臂长；这种角色区别在一般式中更清楚。

变式二：在杆与地面垂直的瞬间，杆顺时针转动且$\beta=0$，内外半径仍为$r,2r$。求圆心、圆筒接触材料点与杆接触材料点的速度和加速度。

解：一般几何为$x_C=r(2\cos\theta+1)/\sin\theta$，圆筒角速度$\Omega=v_C\cos\theta/r$取逆时针为正。代入$\theta=\pi/2$并求时间导数，得$v_C=2r\omega$、$a_C=r\omega^2$、$\Omega=0$、$\dot\Omega=2\omega^2$。接触半径向左，故圆筒材料点加速度为$(r\omega^2,-2r\omega^2)$。杆上此刻接触材料点距铰点$2r$，加速度为$(0,-2r\omega^2)$。两材料点速度均为$(2r\omega,0)$；切向加速度相同，法向加速度可以不同。

变式三：几何位置不变，把杆角速度改为$2\omega$，角加速度改为$4\beta$。求本题各速度与加速度的倍率，解释为什么不能只把加速度乘2。

解：对任一位置函数$\boldsymbol r(\theta)$，速度为$\boldsymbol r_\theta\dot\theta$，加速度为$\boldsymbol r_{\theta\theta}\dot\theta^2+\boldsymbol r_\theta\ddot\theta$。同一几何点处，角速度倍增使速度增为2倍；平方项与角加速度项都增为4倍，因此圆心、各接触材料点和几何接触位置的加速度均增为4倍。这个结论比较的是对应位置的状态，不能把两次运动在同一实验室时刻的不同夹角混为一谈。

变式四：在某瞬间额外要求圆筒与地面也无滑动，杆仍在转动，求该瞬间杆的夹角。说明这个条件能否在夹角持续变化时始终成立。

解：杆侧无滑动给出$\Omega=v_C\cos\theta/r$。圆筒向右纯滚动时，地面无滑动要求$v_C=2r\Omega$。在$v_C\ne0$的瞬间联立得到$2\cos\theta=1$，所以$\theta=\pi/3$。只要杆角速度非零，夹角会离开该值，两条无滑动约束随即不相容。因此本题允许地面滑动是必要的；该瞬时相容点不能被推广成全程纯滚动。
