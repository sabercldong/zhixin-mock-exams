# 第 1 题

<!-- question-start -->
平面内有两座灯塔 $A$、$B$，相距 $l>0$。两座灯塔各发出一束可转动的探照光，交点为 $C$。一个人始终位于交点 $C$，且其速度和加速度大小均有限。令 $\theta=\omega t$，其中 $\omega>0$。灯塔 $A$ 的光束与 $AB$ 正方向的夹角为 $\theta$，灯塔 $B$ 的转角为 $2\theta$。

（1）初态两束光同向。取 $AB$ 向右，随后两束光均逆时针转动，方向角分别为 $\theta$、$2\theta$。求 $t=0$ 与 $t=\pi/(4\omega)$ 时交点到 $B$ 的距离 $r_0,r_1$、速度大小 $v_0,v_1$、加速度大小 $a_0,a_1$。

（2）初态两束光反向。随后 $A$ 光束逆时针转动，$B$ 光束顺时针转动，方向角分别为 $\theta$、$\pi-2\theta$。求同样两个时刻的距离 $r'_0,r'_1$、速度大小 $v'_0,v'_1$、加速度大小 $a'_0,a'_1$。

方向说明：以上转动方向对应两束射线在 $t>0$ 时相交的图示分支。$t=0$ 时两束光共线，交点不由当时的光线单独确定，应由连续运动的极限确定，不任意指定起点。

![图 1-1　同向与反向初始光束的转动方向及交点几何。](../figures/question-01.png)
<!-- question-end -->

## 一、题型定位

由两条旋转射线确定交点的平面运动。已知的是灯塔光束的转动角，而不是人的轨迹、径向速度或加速度；先通过几何求交点位置，才能进行运动学计算。

两种初态在同一个时刻有相同的空间交点，却一般具有不同速度和加速度。判断运动不能仅凭一张位置图，也不能把光束角速度直接当作交点绕某个灯塔匀速转动的充分条件。

## 二、知识点

三角形正弦定理；有向光束与射线参数；极坐标速度及加速度；径向和横向分量的正交合成；复合函数求导；三角恒等式；退化几何的连续极限；Taylor展开；Cartesian坐标交叉检验。

极坐标中的径向坐标会随时间变化，通常有
$$v^2=\dot r^{\,2}+r^2\dot\alpha^{\,2}.$$
即使光束方向角 $\alpha$ 匀速变化，也不意味着 $\dot r=0$，更不意味着加速度只有向心分量。第二种初态恰好需要同时保留径向运动和横向运动。

## 三、物理图像

同向初态下，两束光的交点随后在 $B$ 外侧。$A$ 光束转动较慢，$B$ 光束转动较快，二者与 $AB$ 构成一个外角可直接化成相等内角的三角形。由此交点到 $B$ 的距离保持不变，实际轨迹是一段圆弧。

反向初态下，交点开始在 $A$、$B$ 之间，随后移向上方。交点到 $B$ 的距离不断变化：既有沿光束方向的径向运动，也有垂直于光束方向的运动。极坐标基底本身在顺时针转动，求导时必须计入这一变化。

初始共线时的“交点”看似可在整条直线上任取，但连续运动并不允许任取。后续两个方向角的比例会选出特定极限位置；若把另一个点硬接到轨迹上，会使位移不连续，无法满足有限速度要求。

## 四、解题入口

令 $A=(0,0)$、$B=(l,0)$，取水平向右为 $x$ 正方向、向上为 $y$ 正方向。以 $B$ 为极点，写
$$\boldsymbol r_C=l\boldsymbol e_x+r\boldsymbol e_r(\alpha).$$
先分情况求 $r(\theta)$ 和 $\alpha(\theta)$：
$$
\begin{aligned}
\text{同向初态：}&\quad \alpha=2\theta,\\
\text{反向初态：}&\quad \alpha=\pi-2\theta.
\end{aligned}
$$
随后用 $\dot\theta=\omega$ 将对 $\theta$ 的导数转换为时间导数，求出完整速度、加速度分量，再代入两个时刻。不能先把某个分量的绝对值当成总大小。

## 五、解析

（1）从两条射线的方程确定几何分支。

设交点到 $A$ 的距离为 $s$。沿 $A$ 光束有
$$x=s\cos\theta,\qquad y=s\sin\theta,\qquad s\ge0.$$
同向初态的 $B$ 光束给出
$$x=l+r\cos2\theta,\qquad y=r\sin2\theta,\qquad r\ge0.$$
反向初态则给出
$$x=l-r\cos2\theta,\qquad y=r\sin2\theta,\qquad r\ge0.$$
这里第二组的负号来自 $\cos(\pi-2\theta)=-\cos2\theta$，不是把距离 $r$ 取成负值。

在所求区间 $0<\theta\le\pi/4$，两种情形的射线参数均非负，因此确实是光束的交点，不只是两条无限直线的交点。以后进行极限时，始终使用这两个连续分支。

（2）同向初态的三角形关系。

同向情形中 $\angle A=\theta$，在 $B$ 处三角形内部夹角为 $\pi-2\theta$，故
$$
\angle C=\pi-\theta-(\pi-2\theta)=\theta.
$$
边 $BC=r$ 与边 $AB=l$ 所对内角都为 $\theta$。由正弦定理，
$$
\frac{r}{\sin\theta}=\frac{l}{\sin\theta}.
$$
对 $0<\theta\le\pi/4$，$\sin\theta\ne0$，约去后得到
$$\boxed{r=l.}$$
这一步先在非退化三角形中完成，再取 $\theta\to0$，不能在 $t=0$ 直接写 $0/0=1$。

以 $B$ 为圆心，交点位置为
$$
\boxed{\boldsymbol r_C=l\boldsymbol e_x+l\boldsymbol e_r(2\theta).}
$$
因而
$$x=l+l\cos2\theta,\qquad y=l\sin2\theta.$$
这两式可以直接看出圆方程
$$
(x-l)^2+y^2=l^2.
$$
图 1-2 同时表示反向初态；只有第一种情形的 $r$ 恒定，不能把第二种曲线也按圆周运动处理。

![图 1-2　同向初态的圆弧与反向初态的变半径轨迹。](../figures/opposite-01.png)

（3）推导极坐标的速度和加速度公式。

在固定Cartesian基底中，
$$
\boldsymbol e_r=\cos\alpha\,\boldsymbol e_x+\sin\alpha\,\boldsymbol e_y,
\qquad
\boldsymbol e_\alpha=-\sin\alpha\,\boldsymbol e_x+\cos\alpha\,\boldsymbol e_y.
$$
对时间求导，得到
$$
\dot{\boldsymbol e}_r=\dot\alpha\,\boldsymbol e_\alpha,
\qquad
\dot{\boldsymbol e}_\alpha=-\dot\alpha\,\boldsymbol e_r.
$$
速度不能只对 $r$ 求导。利用乘积求导法则，
$$
\begin{aligned}
\boldsymbol v
&=\frac{d}{dt}\bigl(r\boldsymbol e_r\bigr)\\
&=\dot r\,\boldsymbol e_r+r\dot\alpha\,\boldsymbol e_\alpha.
\end{aligned}
$$
再对两个分量分别求导：
$$
\begin{aligned}
\boldsymbol a
&=\ddot r\,\boldsymbol e_r+\dot r\dot\alpha\,\boldsymbol e_\alpha
+\dot r\dot\alpha\,\boldsymbol e_\alpha
+r\ddot\alpha\,\boldsymbol e_\alpha
-r\dot\alpha^2\,\boldsymbol e_r\\
&=(\ddot r-r\dot\alpha^2)\boldsymbol e_r
+(2\dot r\dot\alpha+r\ddot\alpha)\boldsymbol e_\alpha.
\end{aligned}
$$
两个相同的 $\dot r\dot\alpha$ 分别来自径向分量的基底转动和横向分量的大小变化。漏掉其中一项会使横向加速度少一半。

由于 $\boldsymbol e_r,\boldsymbol e_\alpha$ 正交且为单位矢量，
$$
\begin{aligned}
v&=\sqrt{\dot r^{\,2}+r^2\dot\alpha^2},\\
a&=\sqrt{(\ddot r-r\dot\alpha^2)^2+
(2\dot r\dot\alpha+r\ddot\alpha)^2}.
\end{aligned}
$$

（4）计算同向情形的两个时刻。

由 $r=l$、$\alpha=2\omega t$，
$$
\dot r=0,\quad\ddot r=0,\quad\dot\alpha=2\omega,\quad\ddot\alpha=0.
$$
于是
$$
\boldsymbol v=2l\omega\,\boldsymbol e_\alpha,
\qquad
\boldsymbol a=-4l\omega^2\,\boldsymbol e_r.
$$
大小均为常量：
$$\boxed{v=2l\omega,\qquad a=4l\omega^2.}$$

$t=0$ 时从连续轨迹取极限，$\alpha\to0$，所以
$$
C_0=(2l,0),\quad
\boldsymbol v_0=(0,2l\omega),\quad
\boldsymbol a_0=(-4l\omega^2,0).
$$
$t=\pi/(4\omega)$ 时 $\alpha=\pi/2$，所以
$$
C_1=(l,l),\quad
\boldsymbol v_1=(-2l\omega,0),\quad
\boldsymbol a_1=(0,-4l\omega^2).
$$
因此第一问答案为
$$
\boxed{
r_0=r_1=l,\quad
v_0=v_1=2l\omega,\quad
a_0=a_1=4l\omega^2.
}
$$
加速度方向随时间变化，只有其大小不变。

（5）反向初态的正弦定理与三倍角化简。

反向情形的三角形内角为
$$
\angle A=\theta,\qquad
\angle B=2\theta,\qquad
\angle C=\pi-3\theta.
$$
因此
$$
\frac r{\sin\theta}=\frac l{\sin(\pi-3\theta)}
=\frac l{\sin3\theta},
$$
得到
$$r=l\frac{\sin\theta}{\sin3\theta}.$$
使用三倍角公式，而不是在 $\theta=0$ 直接相除：
$$
\begin{aligned}
\sin3\theta
&=3\sin\theta-4\sin^3\theta\\
&=\sin\theta(3-4\sin^2\theta)\\
&=\sin\theta(1+2\cos2\theta).
\end{aligned}
$$
故在所求区间内，
$$\boxed{r(\theta)=\frac l{1+2\cos2\theta}.}$$
分母在 $0\le\theta\le\pi/4$ 由 $3$ 降到 $1$，始终非零，距离、速度和加速度均有限。更远处 $\theta\to\pi/3$ 会出现交点趋向无穷远，不能把该公式无条件延伸为全时间有限运动。

（6）对变半径作两次求导。

记
$$D(\theta)=1+2\cos2\theta.$$
因 $\dot\theta=\omega$，
$$
\dot D=-4\omega\sin2\theta,\qquad
\ddot D=-8\omega^2\cos2\theta.
$$
第一次求导：
$$
\begin{aligned}
\dot r
&=-lD^{-2}\dot D\\
&=\frac{4l\omega\sin2\theta}{D^2}.
\end{aligned}
$$
第二次求导既要对正弦求导，也要对 $D^{-2}$ 求导：
$$
\begin{aligned}
\ddot r
&=4l\omega\left[
\frac{2\omega\cos2\theta}{D^2}
-\frac{2\sin2\theta\,\dot D}{D^3}\right]\\
&=\frac{8l\omega^2\cos2\theta}{D^2}
+\frac{32l\omega^2\sin^22\theta}{D^3}.
\end{aligned}
$$
反向光束方向为 $\alpha=\pi-2\theta$，故
$$\dot\alpha=-2\omega,\qquad\ddot\alpha=0.$$
负号表示基底顺时针转动。图 1-3 所示的径向与横向分量与以上约定一致；后续速度和加速度的合成正是这两个正交方向的平方和。

![图 1-3　变半径交点的极坐标基底、径向速度及横向速度。](../figures/rates-01.png)

于是
$$
\boxed{
\begin{aligned}
\boldsymbol v&=\dot r\,\boldsymbol e_r-2\omega r\,\boldsymbol e_\alpha,\\
\boldsymbol a&=(\ddot r-4\omega^2r)\boldsymbol e_r
-4\omega\dot r\,\boldsymbol e_\alpha.
\end{aligned}}
$$
后一个横向分量的负号必须保留。虽然求大小时它会被平方，方向分析与Cartesian检验仍需要这个符号。

（7）计算反向情形的初始极限。

$\theta\to0$ 时，
$$D\to3,\qquad\sin2\theta\to0,\qquad\cos2\theta\to1.$$
逐项代入：
$$
r'_0=\frac l3,\qquad
\dot r(0)=0,\qquad
\ddot r(0)=\frac{8l\omega^2}{9}.
$$
速度的径向分量为零，横向分量为 $-2\omega l/3$，因此
$$\boxed{v'_0=\frac{2l\omega}{3}.}$$
加速度的径向分量不能只取 $\ddot r$：
$$
\begin{aligned}
a_r(0)
&=\frac{8l\omega^2}{9}-4\omega^2\frac l3\\
&=-\frac{4l\omega^2}{9},
\qquad a_\alpha(0)=0.
\end{aligned}
$$
故
$$\boxed{a'_0=\frac{4l\omega^2}{9}.}$$
此时 $\boldsymbol e_r=-\boldsymbol e_x$、$\boldsymbol e_\alpha=-\boldsymbol e_y$，所以实际位置和矢量为
$$
C'_0=(2l/3,0),\quad
\boldsymbol v'_0=(0,2l\omega/3),\quad
\boldsymbol a'_0=(4l\omega^2/9,0).
$$
负的径向加速度在此指向右方，不能直接说“加速度向左”。

（8）计算反向情形的第二个时刻。

$t=\pi/(4\omega)$ 时 $\theta=\pi/4$，
$$
D=1,\quad\sin2\theta=1,\quad\cos2\theta=0.
$$
逐项得到
$$
r'_1=l,\qquad\dot r=4l\omega,\qquad\ddot r=32l\omega^2.
$$
于是
$$
v'_1
=\sqrt{(4l\omega)^2+(2l\omega)^2}
=\boxed{2\sqrt5\,l\omega}.
$$
加速度分量为
$$
\begin{aligned}
a_r&=32l\omega^2-4l\omega^2=28l\omega^2,\\
a_\alpha&=-4\omega(4l\omega)=-16l\omega^2.
\end{aligned}
$$
平方和化简：
$$
\begin{aligned}
a'_1
&=l\omega^2\sqrt{28^2+16^2}\\
&=l\omega^2\sqrt{784+256}\\
&=l\omega^2\sqrt{1040}\\
&=\boxed{4\sqrt{65}\,l\omega^2}.
\end{aligned}
$$
此时 $\alpha=\pi/2$，所以
$$
C'_1=(l,l),\quad
\boldsymbol v'_1=(2l\omega,4l\omega),\quad
\boldsymbol a'_1=(16l\omega^2,28l\omega^2).
$$
位置虽然与第一问相同，速度和加速度却不同。

（9）用Cartesian坐标独立核对反向情形。

代入 $r=l/D$，位置为
$$
x=l-\frac{l\cos2\theta}{D},
\qquad
y=\frac{l\sin2\theta}{D}.
$$
第一式写成
$$x=l\frac{1+\cos2\theta}{1+2\cos2\theta}.$$
直接用商法则求导：
$$
\begin{aligned}
\dot x
&=l\frac{(-2\omega\sin2\theta)D
-(1+\cos2\theta)(-4\omega\sin2\theta)}{D^2}\\
&=\frac{2l\omega\sin2\theta}{D^2},\\
\dot y
&=l\frac{2\omega\cos2\theta\,D
+4\omega\sin^22\theta}{D^2}\\
&=\frac{2l\omega(\cos2\theta+2)}{D^2}.
\end{aligned}
$$
最后一步使用 $\cos^22\theta+\sin^22\theta=1$。再求导：
$$
\begin{aligned}
\ddot x
&=\frac{4l\omega^2\cos2\theta}{D^2}
+\frac{16l\omega^2\sin^22\theta}{D^3},\\
\ddot y
&=-\frac{4l\omega^2\sin2\theta}{D^2}
+\frac{16l\omega^2(\cos2\theta+2)\sin2\theta}{D^3}.
\end{aligned}
$$
$t=0$ 时分别为 $(4l\omega^2/9,0)$；$\theta=\pi/4$ 时分别为 $(16l\omega^2,28l\omega^2)$，与极坐标计算一致。

（10）用小时间展开解释唯一连续起点。

反向情形中，
$$
\cos2\theta=1-2\theta^2+O(\theta^4),
\quad
\sin2\theta=2\theta+O(\theta^3).
$$
由
$$
D=3-4\theta^2+O(\theta^4),
\qquad
\frac1D=\frac13+\frac49\theta^2+O(\theta^4),
$$
得
$$
\begin{aligned}
x&=\frac{2l}{3}+\frac{2l}{9}\theta^2+O(\theta^4),\\
y&=\frac{2l}{3}\theta+O(\theta^3).
\end{aligned}
$$
将 $\theta=\omega t$ 代入，与
$$\boldsymbol r(t)=\boldsymbol r(0)+\boldsymbol v(0)t+
\frac12\boldsymbol a(0)t^2+\cdots$$
逐项比较，正好恢复 $C'_0,\boldsymbol v'_0,\boldsymbol a'_0$。这是从初始退化图形到有限运动的具体桥梁，不是任意补一个起点。

同向情形类似：
$$
x=2l-2l\omega^2t^2+O(t^4),
\qquad
y=2l\omega t+O(t^3).
$$
也恢复第一问的初始速度、加速度。图 1-4 将两个初始位置与共同的末位置并置，强调同一末位置不意味着同一运动状态。

![图 1-4　两种连续初态、共同末位置与各自速度方向。](../figures/endpoints-01.png)

（11）汇总结果与量纲检查。

$$
\boxed{
\begin{aligned}
&r_0=r_1=l,\quad v_0=v_1=2l\omega,\quad a_0=a_1=4l\omega^2;\\
&r'_0=l/3,\quad r'_1=l,\\
&v'_0=2l\omega/3,\quad v'_1=2\sqrt5\,l\omega,\\
&a'_0=4l\omega^2/9,\quad a'_1=4\sqrt{65}\,l\omega^2.
\end{aligned}}
$$
$l\omega$ 的量纲是速度，$l\omega^2$ 的量纲是加速度。$\omega\to0$ 时两者分别趋于零；$l$ 加倍而角度变化不变时，全部距离、速度和加速度都加倍。反向情形初始径向速度为零，但径向二阶导数不为零，所以不能凭初始 $\dot r=0$ 判断其以后为定半径运动。

## 六、关键洞察

初态光束共线是几何退化，不是整道运动学问题失去信息。后续方向角随时间的规则仍携带约束，连续性把原本无数个静态交点缩减为唯一运动极限。

两种情形的差别不在两束光转动角的数值，而在初始方向与转动的符号。第一种正弦定理消出恒定 $r$，第二种出现 $\sin3\theta$，产生变半径轨迹。若只记住“角度二比一”而忽略有向射线，会得到错误的圆轨迹。

反向末时刻的 $28$ 和 $16$ 来自两个不同机制：$28$ 是径向二阶导数 $32$ 与基底转动项 $4$ 的差；$16$ 是半径增长与基底转动耦合。不能把光束旋转误当作人的加速度只由向心项决定。

## 七、易错点

把退化时刻的交点任意放在 $A$ 或 $B$；只求光束所在直线、不检查射线正向；混淆 $\angle B$ 的内角与外角；忽略反向情形 $\dot\alpha<0$；把 $\ddot r$ 当成总加速度；漏掉 $2\dot r\dot\alpha$；在正弦比中直接代入零；把两种情形的共同末位置当成共同速度。

求导时对 $D^{-2}$ 的导数为 $-2D^{-3}\dot D$，$\dot D$ 又有负号，两负号使 $\ddot r$ 的第二项为正。把这一项写负会使末时刻的 $32l\omega^2$ 完全改变。速度大小与加速度大小只能在正交分量全部求出后合成。

## 八、课堂讲解建议

先让学生画出两个非零小角度的交点，再向初态逼近，比较“某时刻的几何图”与“整段连续运动”的区别。板书先写两种 $B$ 光束的有向参数式，要求学生明确初始指向，不立即套极坐标公式。

在反向末时刻，先展示图中的 $\boldsymbol e_r,\boldsymbol e_\alpha$，逐项写出 $\dot r,\ddot r,\dot\alpha$。把径向加速度拆为 $32-4$，横向加速度拆为 $2\times4\times(-2)$，之后再合成大小。最后用Cartesian加速度复核符号，让学生看到同一结果可以由另一条路线验证。

## 九、变式训练

（1）同向初态中，将两个光束方向角改为 $\theta$ 和 $p\theta$，其中 $p>1$。求初始连续极限的交点到 $B$ 的距离，以及初始速度大小。

完整解答：三角形在 $C$ 处的内角为 $(p-1)\theta$，故
$$r=l\frac{\sin\theta}{\sin[(p-1)\theta]}.$$
用 $\sin u=u+O(u^3)$，
$$r(0)=\frac l{p-1},\qquad\dot r(0)=0.$$
初始 $\dot\alpha=p\omega$，因此
$$\boxed{r_0=\frac l{p-1},\qquad v_0=\frac{pl\omega}{p-1}.}$$
$p=2$ 恢复 $r_0=l,v_0=2l\omega$。$p\to1^+$ 时交点趋向无穷远，这对应两条几乎平行且转速几乎相同的光束，不是计算异常。

<!-- KEEP_TOGETHER_START -->
（2）反向初态中，$A$ 光束逆时针角速度为 $\omega$，$B$ 光束顺时针角速度为 $p\omega$，其中 $p>0$。求初始连续距离、初始速度及初始加速度大小。

完整解答：$\angle C=\pi-(p+1)\theta$，正弦定理给
$$r=l\frac{\sin\theta}{\sin[(p+1)\theta]},\qquad\alpha=\pi-p\theta.$$
分子、分母均展开至三阶，再对比值展开：
$$
r=\frac l{p+1}\left[1+
\frac{(p+1)^2-1}{6}\theta^2+O(\theta^4)\right].
$$
因此
$$
r_0=\frac l{p+1},\quad
\dot r_0=0,\quad
\ddot r_0=\frac{l\omega^2[(p+1)^2-1]}{3(p+1)}.
$$
$\dot\alpha=-p\omega$，所以
$$
a_{r,0}
=\ddot r_0-r_0p^2\omega^2
=\frac{2lp(1-p)\omega^2}{3(p+1)}.
$$
横向加速度为零，最终
$$
\boxed{
v_0=\frac{pl\omega}{p+1},\qquad
a_0=\frac{2lp|1-p|\omega^2}{3(p+1)}.
}
$$
$p=2$ 恢复本题；$p=1$ 时两个光束对称转动，交点沿中垂线起步，初始加速度为零，但并不保证之后始终零加速度。
<!-- KEEP_TOGETHER_END -->

（3）假设真实质点质量$m$被装置约束，跟随同向转动时的光点轨迹，求装置提供的合力、功率和关于B的角动量。

解：光点关于B作半径$l$、角速度$2\omega$的圆周运动，故
$$\mathbf F=-4m\omega^2\mathbf r,\quad
P=\mathbf F\cdot\mathbf v=0,\quad
L_B=2ml^2\omega,\quad K=2ml^2\omega^2.$$
径向力只改变速度方向。光线交点本身没有质量，不能从其运动学直接推断真实受力；这里的力属于新增的跟随质点及约束装置。

（4）反向转动时求第一次交点发散附近的速率，说明有限速度跟随的范围。

解：$r=l/(1+2\cos2\omega t)$在$t_*=\pi/(3\omega)$首次发散。由分母一阶展开，
$$r\simeq\frac{l}{2\sqrt3\omega(t_*-t)},\qquad
|\mathbf v|\simeq\frac{l}{2\sqrt3\omega(t_*-t)^2}.$$
角向速度项为$r\omega$，阶数低于径向项，故不改变上述主项。真实人员或装置只有有限速度，无法跟随到奇点；发散的是理想延长直线的交点，原光源与转台的速度保持有限。
