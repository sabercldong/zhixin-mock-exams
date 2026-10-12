# 第 1 题

质量均为$m$的直角三角形木块$A$与梯形木块$B$如图放置，接触斜面与水平面的夹角为$\theta$，$0<\theta<\pi/2$。木块$A$位于水平地面上，木块$B$受到光滑竖直导向装置约束，只能上下平动。两接触面的摩擦均采用同一库仑系数$\mu$，极限静摩擦与滑动摩擦按该系数处理。取$x$轴水平向右，$y$轴竖直向上，重力加速度为$g$。

（1）若$A$的有符号速度、加速度分别为$v$、$a$，求$B$的速度和加速度。

（2）设无外力时系统能够保持静止。从静止状态对$A$施加恒定水平外力$F$，向右为正。列出静止及滑动分支，以$F$为横轴、$a$为纵轴分析响应图；说明接触失效、分支退化或非唯一时的适用范围。

（3）取$F_0\ge0$，从静止开始施加周期性锯齿力
$$
F(t)=\frac{F_0}{t_0}t\quad(0\le t<t_0),\qquad
F(t+t_0)=F(t).
$$
在接触约束及可确定的摩擦分支有效时，按不同参数情况画出$v(t)$并写出分段关系。

修订说明：明确静、动摩擦模型及有符号外力；“始终保持接触”作为需要检验的约束，不把违反约束或退化的刚性摩擦分支误作确定运动。

![图 1-1　上升斜面木块与竖直导向块的接触。](../figures/question-01.png)

## 一、题型定位

双接触库仑摩擦系统的约束动力学与分段运动。几何约束把两个物体的运动联系起来，竖直导向装置提供水平反力，两处摩擦又通过法向力与加速度相互耦合。恒力响应并非只由一个滑动方程组成，还包括静摩擦允许区间、滑动方向、重新停止、法向力非负及刚性模型的退化情形。

## 二、知识点

相对速度与接触几何；牛顿第二定律的分物体受力；静摩擦的区间约束与滑动摩擦的定值规则；有符号正方向；法向力对加速度的依赖；接触的单边条件；分段积分、速度连续与加速度跃变；周期外力的平均作用及停止事件；刚性摩擦模型的适用边界。

## 三、物理图像

图中的斜面向右升高。$A$向右运动时，固定在同一水平位置的$B$下方遇到的是斜面更靠左、较低的位置，因此$B$下降。$B$相对于$A$沿斜面向左下滑，作用于$B$的滑动摩擦沿斜面向右上。$A$与地面的摩擦向左。

锯齿力在每个周期末从$F_0$突然降到零，但有限的力跳变没有冲量，速度不会突然变为零。此前已经滑动的系统仍按滑动方程减速；真正减到零后，才重新检查静摩擦能否使它停住。周期内既可能“滑动—停止—再次起动”，也可能只触及零速，或者始终向右运动并逐周期增加速度。

## 四、解题入口

先用斜面方程求出$v_B$和$a_B$。再分别对$A$、$B$写受力方程，始终保留接触法向力$N$和地面法向力$Q$，不能预先取$Q=2mg$。在静止时求两个摩擦力各自的允许区间，在滑动时按速度符号消元。最后用起动阈值$F_+$与平均驱动力$F_0/2$分类锯齿响应，每次积分都以实际的起动或停止时刻作为下限。

## 五、解析

（1）由固定水平位置处的斜面高度建立约束。

设$A$沿$x$轴的位移为$X(t)$。记$B$某一固定竖直参考线的水平位置为$x_b$，斜面高度与$B$参考高度之间的常量差为$y_c$。斜面的方程给出
$$
y_B(t)=\bigl[x_b-X(t)\bigr]\tan\theta+y_c.
$$
$x_b$、$y_c$与$\theta$不随时间改变。对时间求导，不需要知道木块的具体边长：
$$
\begin{aligned}
\dot y_B&=-\dot X\tan\theta,\\
\ddot y_B&=-\ddot X\tan\theta.
\end{aligned}
$$
以后以
$$
\xi=\tan\theta>0
$$
简写几何系数。第一问的矢量答案为
$$
\boxed{\boldsymbol v_B=-\xi v\,\boldsymbol e_y,\qquad
\boldsymbol a_B=-\xi a\,\boldsymbol e_y.}
$$
若$v>0$，$B$向下；若$a<0$，即使$B$此时仍向下运动，它的加速度也向上。运动方向由速度决定，不能由加速度的符号代替。

图1-2把两个对应位置画在同一导向线上。$A$向右增加位移$\Delta X$时，$B$下降$\xi\Delta X$；随后所有受力方程中的$a_B$都使用这一关系。

![图 1-2　斜面平移与导向块升降的几何约束。](../figures/constraints-01.png)

（2）明确相对滑动方向，而不是直接猜摩擦方向。

沿斜面向右上的单位矢量为
$$
\boldsymbol\tau=(\cos\theta,\sin\theta),
$$
从$A$指向$B$的法向单位矢量为
$$
\boldsymbol n=(-\sin\theta,\cos\theta).
$$
$A$只有水平平动，$B$只有竖直平动，所以两木块接触材料点的相对速度为
$$
\begin{aligned}
\boldsymbol v_{B/A}
&=\boldsymbol v_B-\boldsymbol v_A\\
&=(-v,-\xi v)\\
&=-\frac{v}{\cos\theta}\boldsymbol\tau.
\end{aligned}
$$
$\cos\theta>0$，故相对速度沿斜面的符号与$v$相反。定义滑动符号
$$
\sigma=\operatorname{sgn}v,\qquad \sigma=\pm1.
$$
作用于$B$的接触摩擦为$+\sigma\mu N\boldsymbol\tau$，其中$N\ge0$为斜面法向力；作用于$A$的地面滑动摩擦为$-\sigma\mu Q\boldsymbol e_x$，其中$Q\ge0$为地面法向力。$v=0$时不能直接使用$\sigma=\pm1$，静摩擦必须另列。

（3）建立两个物体的真实受力方程。

图1-3按$v>0$画出摩擦方向。向左滑动时两摩擦箭头均反向。导向反力$H$取向右为正，由$B$的水平平衡有$H=N(\sin\theta-\mu\cos\theta)$；$H<0$时真实反力向左，图中箭头只规定其正方向。导向反力不进入竖直方程，也不做功。

![图 1-3　向右滑动分支的两物体受力及导向反力。](../figures/forces-01.png)

$B$的竖直方程为
$$
N\cos\theta+\sigma\mu N\sin\theta-mg=-m\xi a.
$$
把$N$的两项合并：
$$
N\cos\theta(1+\sigma\mu\xi)=m(g-\xi a).
$$
若$1+\sigma\mu\xi\ne0$，
$$
\boxed{N_\sigma=
\frac{m(g-\xi a)}
{\cos\theta(1+\sigma\mu\xi)}.}
$$
这一式不仅用于消元，还必须用于检验接触。

$A$无竖直加速度。$B$对$A$的接触力与$A$对$B$的接触力相反，故
$$
Q-mg-N\cos\theta-\sigma\mu N\sin\theta=0.
$$
利用$B$的竖直方程，
$$
\begin{aligned}
Q&=mg+N\cos\theta(1+\sigma\mu\xi)\\
&=mg+m(g-\xi a),
\end{aligned}
$$
从而
$$
\boxed{Q=m(2g-\xi a).}
$$
只有$a=0$时才有$Q=2mg$。$B$下降加速时传给地面的竖直负荷减小，$B$上升加速时负荷增大。

$A$的水平接触力为$N\sin\theta-\sigma\mu N\cos\theta$，所以
$$
ma=F+N\cos\theta(\xi-\sigma\mu)-\sigma\mu Q.
$$
这是最后的水平动力学方程。导向装置能够对整个系统提供水平外力，因此不能把两物体作为系统后误用水平动量守恒。

（4）完整消去$N$与$Q$。

将上一步的两个表达式代入：
$$
a=\frac Fm+
\frac{(g-\xi a)(\xi-\sigma\mu)}
{1+\sigma\mu\xi}
-\sigma\mu(2g-\xi a).
$$
乘以$1+\sigma\mu\xi$，先展开，再分别收集$a$和$g$：
$$
\begin{aligned}
a(1+\sigma\mu\xi)
={}&\frac Fm(1+\sigma\mu\xi)
+g(\xi-\sigma\mu)\\
&-a\xi(\xi-\sigma\mu)
-2\sigma\mu g(1+\sigma\mu\xi)\\
&+\sigma\mu\xi a(1+\sigma\mu\xi).
\end{aligned}
$$
移到左边的$a$系数为
$$
\begin{aligned}
D_\sigma
&=(1+\sigma\mu\xi)+\xi(\xi-\sigma\mu)
-\sigma\mu\xi(1+\sigma\mu\xi)\\
&=1+\sigma\mu\xi+\xi^2-\sigma\mu\xi
-\sigma\mu\xi-\mu^2\xi^2\\
&=\boxed{1+(1-\mu^2)\xi^2-\sigma\mu\xi}.
\end{aligned}
$$
右边的重力系数为
$$
\begin{aligned}
(\xi-\sigma\mu)-2\sigma\mu(1+\sigma\mu\xi)
&=\xi-\sigma\mu-2\sigma\mu-2\mu^2\xi\\
&=(1-2\mu^2)\xi-3\sigma\mu.
\end{aligned}
$$
于是滑动分支满足
$$
\boxed{
D_\sigma a=
(1+\sigma\mu\xi)\frac Fm+
g\bigl[(1-2\mu^2)\xi-3\sigma\mu\bigr].
}
$$
只有$D_\sigma\ne0$时才能除以它求$a$；除完后仍须同时检验$\sigma v>0$、$N_\sigma\ge0$、$Q\ge0$。

（5）静止分支不能把两处摩擦都先取成最大值。

静止时令作用于$B$的斜面摩擦为$f\boldsymbol\tau$，地面对$A$的水平摩擦为$f_G\boldsymbol e_x$。二者是待定反力：
$$
|f|\le\mu N,\qquad |f_G|\le\mu Q.
$$
由$B$的竖直平衡，
$$
N\cos\theta+f\sin\theta=mg.
$$
由$A$的竖直平衡，静止时$Q=2mg$。令
$$
\lambda=\frac fN,\qquad -\mu\le\lambda\le\mu.
$$
还需$N>0$，因此
$$
1+\lambda\xi>0,\qquad
N=\frac{mg}{\cos\theta(1+\lambda\xi)}.
$$
$A$的水平平衡为
$$
0=F+N\cos\theta(\xi-\lambda)+f_G.
$$
整理外力：
$$
\frac F{mg}=
\frac{\lambda-\xi}{1+\lambda\xi}
-\frac{f_G}{mg}.
$$
外力的允许范围由两个区间合成，应求区间端点。

（6）求静摩擦允许的外力端点。

定义
$$
H(\lambda)=\frac{\lambda-\xi}{1+\lambda\xi}.
$$
用商法则求导：
$$
\begin{aligned}
H'(\lambda)
&=\frac{(1+\lambda\xi)-\xi(\lambda-\xi)}
{(1+\lambda\xi)^2}\\
&=\frac{1+\xi^2}{(1+\lambda\xi)^2}>0.
\end{aligned}
$$
所以最大的$F$对应$\lambda=\mu$及$f_G=-2\mu mg$：
$$
\begin{aligned}
F_+
&=mg\left[\frac{\mu-\xi}{1+\mu\xi}+2\mu\right]\\
&=\boxed{mg\frac{3\mu-(1-2\mu^2)\xi}{1+\mu\xi}}.
\end{aligned}
$$
若$\mu\xi<1$，最小的$F$对应$\lambda=-\mu$及$f_G=+2\mu mg$：
$$
\begin{aligned}
F_-
&=mg\left[\frac{-\mu-\xi}{1-\mu\xi}-2\mu\right]\\
&=\boxed{mg\frac{-3\mu-(1-2\mu^2)\xi}{1-\mu\xi}}.
\end{aligned}
$$
$F_-$是有符号的负阈值，不是摩擦力大小。

若$\mu\xi\ge1$，$\lambda$可以从大于$-1/\xi$的一侧逼近$-1/\xi$，此时$H(\lambda)\to-\infty$，而$N\to+\infty$。理想刚性模型给出向左外力下的自锁：
$$
F_-= -\infty.
$$
这表示静止平衡允许任意有限负$F$，不是实际材料能够承受无限法向力。真实装置会先受到变形、强度及导向间隙限制。

图1-4显示有限$F_-$的常规静止区间，以及自锁时向左无界的理想静止分支。它只标静止允许性，并不代替滑动方程。

![图 1-4　静摩擦允许的外力区间及向左自锁。](../figures/static-01.png)

（7）把题设“初态能静止”写成参数条件。

因为$F_-$始终小于零或为$-\infty$，无外力静止的条件就是$F_+\ge0$：
$$
3\mu-(1-2\mu^2)\xi\ge0.
$$
将其改写为关于$\mu$的二次不等式：
$$
2\xi\mu^2+3\mu-\xi\ge0.
$$
两根异号，$\mu\ge0$只需取正根：
$$
\boxed{
\mu\ge\mu_{\mathrm{stat}}
=\frac{\sqrt{9+8\xi^2}-3}{4\xi}.
}
$$
为避免$\xi$很小时两个接近数相减，可以有理化：
$$
\mu_{\mathrm{stat}}
=\frac{2\xi}{\sqrt{9+8\xi^2}+3}.
$$
在小角度极限$\xi\to0$，$\mu_{\mathrm{stat}}\sim\xi/3$。这个条件仅保证初态静止，不保证滑动方程始终正常，更不保证外力任意增大时不失去接触。

（8）正常向右分支的$a(F)$与接触上限。

记
$$
D_+=1+(1-\mu^2)\xi^2-\mu\xi.
$$
先讨论$D_+>0$。定义正的响应系数
$$
\kappa=\frac{1+\mu\xi}{mD_+}>0.
$$
向右滑动方程化为
$$
\boxed{a_+=\kappa(F-F_+).}
$$
这一步使用了$F_+$的定义，没有重新假定两摩擦的方向。从静止起动且$F\ge0$时，
$$
a=
\begin{cases}
0,&0\le F\le F_+,\\
\kappa(F-F_+),&F>F_+,
\end{cases}
$$
但第二行只在接触仍有效时成立。

向右分支中$1+\mu\xi>0$，故$N_+\ge0$要求
$$
a\le \frac g\xi.
$$
此时$Q=m(2g-\xi a)\ge mg>0$，斜面接触先达到边界。把$a=g/\xi$代入$A$的水平方程，此时$N=0$、$Q=mg$，得到
$$
\boxed{F_{\mathrm d}=mg\left(\frac1\xi+\mu\right).}
$$
因此严格接触区间为
$$
F_+<F<F_{\mathrm d}.
$$
$F=F_{\mathrm d}$是$N=0$的边界；超过它不能继续声称两木块始终接触。

两个力端点之差为
$$
\begin{aligned}
F_{\mathrm d}-F_+
&=mg\frac{
(1/\xi+\mu)(1+\mu\xi)
-[3\mu-(1-2\mu^2)\xi]}
{1+\mu\xi}\\
&=mg\frac{1/\xi-\mu+(1-\mu^2)\xi}
{1+\mu\xi}\\
&=\boxed{\frac{mgD_+}{\xi(1+\mu\xi)}}.
\end{aligned}
$$
所以$D_+>0$确实保证接触上限大于起动阈值，这不是图形外观推测。

（9）向左分支与从静止起动的选择。

若$\mu\xi<1$，$D_-=1+(1-\mu^2)\xi^2+\mu\xi>0$。向左起动时
$$
\boxed{
a_-=\frac{1-\mu\xi}{mD_-}(F-F_-).
}
$$
$F<F_-$使$a_-<0$，与由静止向左起动相容，且$N_->0$、$Q>0$。

因此在两侧均为正常分支时，初始恒力响应为
$$
a(F)=
\begin{cases}
\dfrac{1-\mu\xi}{mD_-}(F-F_-),&F<F_-,\\[4pt]
0,&F_-\le F\le F_+,\\[4pt]
\kappa(F-F_+),&F_+<F<F_{\mathrm d}.
\end{cases}
$$
最右侧超过$F_{\mathrm d}$的部分不是本题保持接触的运动。

若$\mu\xi\ge1$，由静止向左起动将要求$a<0$，但向左滑动时$B$的竖直方程左侧接触合力$N\cos\theta(1-\mu\xi)\le0$，使
$$
g-\xi a\le0,\qquad a\ge g/\xi>0.
$$
这与从零速向左起动不相容。因此负外力下静止自锁分支不能随意接成“向左加速”的直线。已经具有负速度的运动是另一个初值问题，不等于本题从静止起动。

（10）$D_+=0$及$D_+<0$时不能机械地画同一种折线。

$D_+$的零点满足
$$
(\mu\xi)^2+\mu\xi-(1+\xi^2)=0.
$$
于是
$$
\mu_{\mathrm P}
=\frac{\sqrt{5+4\xi^2}-1}{2\xi}.
$$
只有$\mu<\mu_{\mathrm P}$才有前述正斜率向右分支。

若$D_+=0$，消元方程成为
$$
0=\frac{1+\mu\xi}{m}(F-F_+).
$$
只有$F=F_+$时滑动受力方程才相容，此时$a$没有由该方程唯一确定；还须保留接触条件$a\le g/\xi$。同时$F_+=F_{\mathrm d}$。不能把“分母为零”写成无限加速度。

若$D_+<0$，向右滑动直线斜率为负。由于$F_{\mathrm d}<F_+$，在
$$
F_{\mathrm d}<F<F_+
$$
内，滑动方程给出$0<a<g/\xi$，同时静摩擦也允许$a=0$。从静止开始的理想刚性方程可出现多种可行分支，不能仅由外力选出唯一轨迹。若$F>F_+$，静止不再允许，而代数滑动分支给$a<0$，又不相容于由静止向右起动；保持接触的模型无相容起动解。

这类情况说明“刚性接触、定值库仑摩擦、始终接触”在部分参数区间不足以确定运动。需要接触柔性、冲击规律等额外模型才能继续；本题不凭空增加这些资料。

图1-5分开画正常、退化和非唯一情形。正常图上的实线只延伸到接触上限，退化图用允许集合而非无穷高直线表示，非唯一图同时保留静止支与滑动支。

![图 1-5　向右响应的正常、退化与非唯一分支。](../figures/response-01.png)

（11）以功率关系独立检查滑动消元式。

在$v\ne0$且接触约束有效时，两木块总动能为
$$
K=\frac12mv^2+\frac12m(\xi v)^2
=\frac12m(1+\xi^2)v^2.
$$
重力对$B$的功率为$(-mg)\dot y_B=mg\xi v$；$A$的重力不做功。地面滑动耗散功率为$-\mu Q|v|$。斜面摩擦的总耗散由相对速度决定：
$$
-\mu N|\boldsymbol v_{B/A}|
=-\mu N\frac{|v|}{\cos\theta}.
$$
导向反力与$B$速度垂直，功率为零。因此
$$
m(1+\xi^2)av
=Fv+mg\xi v-\mu Q|v|-\frac{\mu N|v|}{\cos\theta}.
$$
除以非零$v$，$\lvert v\rvert/v=\sigma$：
$$
m(1+\xi^2)a=
F+mg\xi-\sigma\mu Q-\frac{\sigma\mu N}{\cos\theta}.
$$
代入
$$
Q=m(2g-\xi a),\qquad
\frac N{\cos\theta}
=\frac{m(g-\xi a)(1+\xi^2)}{1+\sigma\mu\xi}.
$$
乘以$1+\sigma\mu\xi$后，$a$的系数为
$$
\begin{aligned}
&(1+\xi^2)(1+\sigma\mu\xi)
-\sigma\mu\xi(1+\xi^2)
-\sigma\mu\xi(1+\sigma\mu\xi)\\
&=1+\xi^2-\sigma\mu\xi-\mu^2\xi^2
=D_\sigma,
\end{aligned}
$$
重力项化为$g[(1-2\mu^2)\xi-3\sigma\mu]$。它与分物体受力路线完全一致。若把斜面耗散错用$\mu N|v|$，就会漏掉$1/\cos\theta$，无法得到同一个方程。

（12）锯齿力分析的适用条件与首个起动时刻。

以下讨论
$$
D_+>0,\qquad F_+\ge0,
$$
并要求峰值没有越过接触上限：
$$
F_0<F_{\mathrm d}.
$$
若只取$F_0=F_{\mathrm d}$，周期末是法向力为零的极限边界，不能替代严格接触。若$F_0>F_{\mathrm d}$，首个周期在达到$F_{\mathrm d}$时就必须切换到离开接触的模型，下面的整周期曲线不再适用。

图1-6标出各周期相位、起动力阈值与力的跳变。它用来确定积分区间，不把周期末的力跳变误作速度跳变。

![图 1-6　周期锯齿力与起动力阈值。](../figures/force-01.png)

令斜率
$$
K_F=\frac{F_0}{t_0}.
$$
若$F_0\le F_+$，每一时刻外力都处于静摩擦允许区间，故
$$
\boxed{v(t)=0\quad\text{对全部 }t\ge0.}
$$
若$F_0>F_+$，首个周期起动时刻为
$$
\boxed{t_1=\frac{F_+}{K_F}=\frac{F_+}{F_0}t_0.}
$$
首周期$t<t_1$仍静止，$t>t_1$时
$$
a(t)=\kappa K_F(t-t_1).
$$
以$v(t_1)=0$为积分下限：
$$
\begin{aligned}
v(t)
&=\int_{t_1}^t\kappa K_F(s-t_1)\,ds\\
&=\frac{\kappa K_F}{2}(t-t_1)^2.
\end{aligned}
$$
首周期结束前的速度为
$$
\boxed{
v_{\mathrm p}
=\frac{\kappa t_0(F_0-F_+)^2}{2F_0}.
}
$$
首周期积分给出这个连续边界值，后续各类运动都要用到它。

（13）力重置后的速度抛物线与是否停止。

在后续周期令相位
$$
u=t-nt_0,\qquad 0\le u<t_0,\qquad n\ge1.
$$
设周期开始速度为$v_n$。只要尚未停住，速度仍正，滑动方程不因外力降到阈值以下就立即停止：
$$
a(u)=\kappa(K_Fu-F_+).
$$
积分得
$$
\boxed{
v(u)=v_n+\kappa\left(\frac{K_Fu^2}{2}-F_+u\right).
}
$$
把平方项配方：
$$
v(u)=v_n-\frac{\kappa F_+^2}{2K_F}
+\frac{\kappa K_F}{2}(u-t_1)^2.
$$
所以这一滑动抛物线的最低点在$u=t_1$。若最低速度为负，不能保留抛物线的负值；它会在前一个根首次停住，然后重新按静摩擦判断。

整个周期都不停止时，周期速度增量为
$$
\begin{aligned}
\Delta v
&=\int_0^{t_0}\kappa(K_Fu-F_+)\,du\\
&=\kappa\left(\frac{F_0t_0}{2}-F_+t_0\right)\\
&=\boxed{\kappa t_0\left(\frac{F_0}{2}-F_+\right)}.
\end{aligned}
$$
$F_0/2$是锯齿力的平均值；$F_+$是向右滑动方程中的常量平衡力。只有没有中途停止时，才可把整周期积分直接用作下一周期的速度增量。

（14）$F_+<F_0<2F_+$：减速到零、等待、再起动。

第一个重置周期的$v_n=v_{\mathrm p}$。最低点为
$$
\begin{aligned}
v_{\min}
&=v_{\mathrm p}-\frac{\kappa F_+^2}{2K_F}\\
&=\frac{\kappa}{2K_F}
\left[(F_0-F_+)^2-F_+^2\right]\\
&=\frac{\kappa}{2K_F}F_0(F_0-2F_+)<0.
\end{aligned}
$$
这是自由延拓抛物线会越过零的信号，不是实际出现向左速度。

令真实停止时刻的相位为$u_s$。将速度方程乘以$2K_F/\kappa$：
$$
(K_Fu_s)^2-2F_+K_Fu_s+(F_0-F_+)^2=0.
$$
用求根公式，
$$
K_Fu_s=F_+\pm\sqrt{F_+^2-(F_0-F_+)^2}.
$$
首次停止取较小根，并化简根号：
$$
\boxed{
u_s=
\frac{t_0}{F_0}
\left[F_+-\sqrt{F_0(2F_+-F_0)}\right].
}
$$
由$F_+<F_0<2F_+$可得$0<u_s<t_1$，停止时外力$K_Fu_s<F_+$，静摩擦可以保持静止。于是每个$n\ge1$的周期都重复
$$
\boxed{
v(nt_0+u)=
\begin{cases}
v_{\mathrm p}+\kappa\left(\dfrac{K_Fu^2}{2}-F_+u\right),
&0\le u\le u_s,\\[5pt]
0,&u_s\le u\le t_1,\\[4pt]
\dfrac{\kappa K_F}{2}(u-t_1)^2,
&t_1\le u<t_0.
\end{cases}
}
$$
在$u_s$处速度连续，原滑动加速度可能为负，停止后改为零；在$t_1$处加速度从零开始增长。后一段积分到$t_0$又得到相同$v_{\mathrm p}$，所以这确实是重复脉冲，而不是只画了一个周期的示意。

（15）$F_0=2F_+$：恰好触及零速，无有限静止时段。

此时
$$
\Delta v=0,\qquad
t_1=\frac{t_0}{2},\qquad
u_s=t_1.
$$
每个重置周期的最低速度恰为零：
$$
v_{\mathrm p}=\frac{\kappa F_+t_0}{4}.
$$
配方后的完整速度为
$$
\boxed{
v(nt_0+u)=
\frac{\kappa K_F}{2}
\left(u-\frac{t_0}{2}\right)^2,\qquad n\ge1.
}
$$
它在周期中点与时间轴相切，随后立即重新增大。没有一段长度非零的等待区间。首周期仍须单列：前半周期静止、后半周期从零起动，不能把后续周期的整条抛物线追溯到$t=0$。

（16）$F_0>2F_+$：不再停住，逐周期增加速度。

第一个重置周期的最低速度已经为正。以后每周期增加
$$
\Delta v=\kappa t_0(F_0/2-F_+)>0,
$$
故最低速度也逐周期增加。记第$n$个重置时刻$t=nt_0$的速度，则
$$
v_n=v_{\mathrm p}+(n-1)\Delta v,\qquad n\ge1.
$$
因而
$$
\boxed{
v(nt_0+u)=
v_{\mathrm p}+(n-1)\Delta v+
\kappa\left(\frac{K_Fu^2}{2}-F_+u\right).
}
$$
每个周期前段仍减速、后段仍加速，但后一段弥补了前段损失并有净增量。因此“持续加速”指周期包络整体上升，不表示每一时刻$a>0$。

图1-7分别画全程静止、脉冲、相切临界和逐周期上升。各图在力重置时保持速度连续，停止后的等待段才贴住时间轴。

![图 1-7　锯齿力作用下四类速度响应。](../figures/pulses-01.png)

（17）检验各分类是否落在接触允许范围内。

最大向右加速度出现在力峰值附近：
$$
a_{\max}=\kappa(F_0-F_+).
$$
$N_+>0$要求$a_{\max}<g/\xi$，恰等价于$F_0<F_{\mathrm d}$。停止后的静摩擦允许性已经在$u_s<t_1$处检查，不能只检查峰值。

持续上升分类还要求存在区间
$$
2F_+<F_0<F_{\mathrm d}.
$$
若$F_{\mathrm d}\le2F_+$，保持严格接触的任何峰值都无法进入该分类。图中的四类曲线是参数分类，并不保证固定的一组$\theta,\mu$能同时实现全部四种。

比较两个端点：
$$
\begin{aligned}
F_{\mathrm d}-2F_+
&=\frac{mg}{1+\mu\xi}
\left[\frac1\xi-4\mu+(2-3\mu^2)\xi\right]\\
&=\frac{mg}{\xi(1+\mu\xi)}
\left[1+2\xi^2-4\mu\xi-3\mu^2\xi^2\right].
\end{aligned}
$$
因此持续上升区间存在，当且仅当
$$
1+2\xi^2-4\mu\xi-3\mu^2\xi^2>0
$$
并同时满足初态静止及$D_+>0$。没有必要用不合接触条件的大$F_0$来强行补画一种速度图。

若$D_+\le0$，周期力下也不能把$\kappa$当正系数套用脉冲公式。此时须回到退化或多分支的受力集合，本题资料不足以选出唯一整周期轨迹；不提供貌似确定、实际上超出模型的$v(t)$。

（18）量纲、边界和速度连续性检查。

$F_\pm$与$F_{\mathrm d}$的量纲为力，$\kappa$的量纲为质量的倒数，所以$\kappa(F-F_+)$为加速度。$K_F$的量纲为力除以时间，$\kappa K_F(t-t_1)^2$为速度；$u_s$中的方括号具有力的量纲，乘$t_0/F_0$后是时间。

令$F_0\to F_+^+$，$t_1\to t_0$且$v_{\mathrm p}\to0$，与全程静止连续接上。令$F_0\to2F_+^-$，根号趋零，$u_s\to t_1$，等待段消失；从$F_0>2F_+$趋近临界，$\Delta v\to0$，最低速度也趋零。三个分支在分类边界相容。

每次外力重置的前后速度相等，但加速度一般由$\kappa(F_0-F_+)$跃为$-\kappa F_+$。这是有限力跳变的结果。若绘图把$v$在周期末竖直降到零，就等于额外添加了未给定的冲量。

## 六、关键洞察

最重要的耦合不是$v_B=-v\tan\theta$本身，而是$N$和$Q$都含有$a$。摩擦力并非“给定质量乘$\mu g$”的常量，法向反力的反馈改变了滑动响应的分母。静摩擦先形成力的允许区间，滑动摩擦再形成两条有方向的动力学分支，二者职责不同。

锯齿力的分类有两个独立阈值：$F_0=F_+$决定是否第一次起动，$F_0=2F_+$决定已滑动系统的整周期净速度变化。还存在第三个接触阈值$F_{\mathrm d}$。这三个阈值不能合并为一句“外力超过摩擦力就一直加速”。

用平均力判断净变化只适用于整周期保持滑动。脉冲分支在停止区间使用静摩擦，实际加速度为零，因此若不先检查停止事件就把负的$\Delta v$逐周期累加，会错误预测向左运动。

$D_+\le0$的异常并不是三角函数算错，也不是惯性质量真的变成负数，而是理想刚性库仑模型的接触反力反馈使代数方程退化或失去唯一性。物理模型的可解性本身必须成为答案的一部分。

## 七、易错点

斜面向右升高却把$v_B$写为$+v\tan\theta$，会使所有后续方向颠倒。判断斜面摩擦时若只看$B$对地的竖直速度，而不看$B$对$A$的相对速度，也容易画反。

把$Q$从头到尾取为$2mg$，或把斜面耗散写为$\mu N|v|$，分别漏掉动态负荷和相对滑动距离。两条错误路线可能给出不同的加速度，功率核验可以及时识别。

在静止区间把$f=\mu N$及$f_G=\mu Q$同时固定，得到的只是边界，不能代表整个静止状态。$v=0$时直接定义$\sigma=0$再代入滑动式，也不能正确恢复静摩擦。

将负斜率滑动支理解为从静止后必定反向加速，忽略速度方向和法向力条件，会掩盖多解或无解。接触约束是单边条件，不能允许$N<0$来拉住两个木块。

在周期末令速度随力跳变、把抛物线的负值保留下来、把首周期与重复周期混为一谈，都属于分段条件错误。图像必须标起动、停止、阈值相切和力重置四类不同事件。

## 八、课堂讲解建议

先让学生在图1-2上画出$A$向右平移后的斜面位置，再判断$B$是升还是降；不急于受力计算。随后在图1-3分别标两木块接触摩擦及地面摩擦，要求学生用相对速度解释方向，并用作用与反作用核对斜面两侧箭头。

板书按“几何约束—两个竖直方程—水平方程—静止区间”四栏展开。在完成$Q=m(2g-\xi a)$之前不让学生代入$2mg$。消元时保留$D_\sigma$，再讨论它的符号，避免提前消去物理适用条件。

周期部分先只讲正常$D_+>0$。将首周期起动抛物线画完整，再把末速度作为下一周期初值；让学生根据最低点是否低于零，自行找停止事件。临界$F_0=2F_+$可用同一配方式解释，不另背一条公式。

最后用功率路线进行独立检查，把导向反力不做功与不守恒水平动量并列比较。进阶讲解再讨论退化分支和接触失效，明确它们是模型边界，不把异常情况省略成“摩擦太大不讨论”。

## 九、变式训练

变式一：取$\theta=\pi/4$、$\mu=2/5$，其余模型不变，$F_0=(3/2)F_+$。求每个重复周期的停止相位、再起动相位、周期末速度，并核验接触。

解：此时$\xi=1$，
$$
\begin{aligned}
D_+&=1+(1-4/25)-2/5=36/25,\\
\kappa&=\frac{7/5}{m(36/25)}=\frac{35}{36m},\\
F_+&=mg\frac{6/5-17/25}{7/5}=\frac{13}{35}mg,\\
F_{\mathrm d}&=(1+2/5)mg=\frac75mg.
\end{aligned}
$$
峰值为$F_0=39mg/70<F_{\mathrm d}$，再起动时刻为
$$
t_1/t_0=F_+/F_0=2/3.
$$
停止相位由小根给出：
$$
\begin{aligned}
u_s/t_0
&=\frac{1-\sqrt{(3/2)(2-3/2)}}{3/2}\\
&=\boxed{\frac{2-\sqrt3}{3}\approx0.0893}.
\end{aligned}
$$
从$u_s$到$2t_0/3$保持静止。周期末速度为
$$
\begin{aligned}
v_{\mathrm p}
&=\frac{\kappa t_0( F_+/2)^2}{3F_+}\\
&=\frac{\kappa F_+t_0}{12}
=\boxed{\frac{13}{432}gt_0}.
\end{aligned}
$$
用$\kappa F_+=13g/36$及$K_F=(3F_+/2)/t_0$写成无量纲相位$\zeta=u/t_0$：
$$
\frac{v}{gt_0}=
\begin{cases}
\dfrac{13}{432}+
\dfrac{13}{36}\left(\dfrac34\zeta^2-\zeta\right),
&0\le\zeta\le(2-\sqrt3)/3,\\[4pt]
0,&(2-\sqrt3)/3\le\zeta\le2/3,\\[4pt]
\dfrac{13}{48}(\zeta-2/3)^2,&2/3\le\zeta<1.
\end{cases}
$$
最大加速度为
$$
a_{\max}=\kappa(F_0-F_+)=\frac{13}{72}g<g.
$$
因此$N>0$；同时$Q=m(2g-a)>0$。首周期只保留等待与后一段起动，不加上前一周期遗留的减速段。

变式二：地面摩擦系数为$\mu_G$，两木块间的摩擦系数为$\nu$，二者不再相等。推导有符号滑动分支，并判断地面完全光滑时是否仍有同一种分母退化。

解：$B$的摩擦换为$\sigma\nu N\boldsymbol\tau$，$A$的地面摩擦换为$-\sigma\mu_GQ\boldsymbol e_x$。两个竖直方程仍给出
$$
N=\frac{m(g-\xi a)}{\cos\theta(1+\sigma\nu\xi)},\qquad
Q=m(2g-\xi a).
$$
$A$的水平式变为
$$
a=\frac Fm+
\frac{(g-\xi a)(\xi-\sigma\nu)}{1+\sigma\nu\xi}
-\sigma\mu_G(2g-\xi a).
$$
乘分母后，$a$系数完整化简为
$$
\begin{aligned}
D_{\sigma,\mathrm{new}}
&=(1-\sigma\mu_G\xi)(1+\sigma\nu\xi)
+\xi(\xi-\sigma\nu)\\
&=1+\sigma\nu\xi-\sigma\mu_G\xi-\mu_G\nu\xi^2
+\xi^2-\sigma\nu\xi\\
&=\boxed{1+(1-\mu_G\nu)\xi^2-\sigma\mu_G\xi}.
\end{aligned}
$$
重力项为
$$
(\xi-\sigma\nu)-2\sigma\mu_G(1+\sigma\nu\xi)
=(1-2\mu_G\nu)\xi-\sigma(\nu+2\mu_G).
$$
所以
$$
\boxed{
a_\sigma=
\frac{(1+\sigma\nu\xi)F/m+
g[(1-2\mu_G\nu)\xi-\sigma(\nu+2\mu_G)]}
{1+(1-\mu_G\nu)\xi^2-\sigma\mu_G\xi}.
}
$$
令$\mu_G=\nu=\mu$恢复主解。若地面完全光滑$\mu_G=0$，
$$
D_{\sigma,\mathrm{new}}=1+\xi^2>0,
$$
故这一分母不会因$\nu$增大而变成零或负。向右分支的起动力为
$$
F_+=mg\frac{\nu-\xi}{1+\nu\xi}.
$$
无外力静止要求$\nu\ge\xi$。滑动仍可能达到$N=0$而失去接触，但原来的双摩擦反馈退化已经消失。这样区分“接触失效”和“代数分母退化”，比仅说摩擦越大越难运动更准确。

变式三：将两处接触都改为光滑，取$\theta=\pi/4$，水平恒力$F=mg/2$。初始速度为零，求仍保持接触且未到达导轨端点时的两木块加速度及支持力。

解：约束给出$a_B=-a_A\tan\theta$。竖直受力为$N\cos\theta-mg=-ma_A\tan\theta$，水平受力为$ma_A=F+N\sin\theta$。消去$N$得
$$a_A=\frac{F+mg\tan\theta}{m(1+\tan^2\theta)}=\frac{3g}{4},\qquad a_B=-\frac{3g}{4}.$$
于是$N=mg/(2\sqrt2)$，地面对下块的支持力为$Q=mg+N\cos\theta=5mg/4$。两支持力为正。结果只适用于接触几何仍成立的有限行程，光滑模型也不能沿用原题的静止阈值。

变式四：取$\theta=\pi/4$、$\mu=2/5$，下块已有向右速度$v_i>0$。求使速度保持不变的恒力和此时两法向力，并判断是否需要摩擦力为零。

解：在正向滑动支，令$a_A=a_B=0$。上块竖直平衡给出$N(\cos\theta+\mu\sin\theta)=mg$，故$N=5\sqrt2mg/7$，$Q=2mg$。下块水平平衡为$F+N(\sin\theta-\mu\cos\theta)-\mu Q=0$，得到$F=13mg/35$。速度恒为$v_i$，但两滑动摩擦均非零；外力、接触力和地面摩擦的合力为零。$v_i=0$时还须使用静摩擦约束，不能据该滑动分支断言自行起动。
