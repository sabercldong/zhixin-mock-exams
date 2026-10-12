# 第 8 题

蔡子昱乘坐一艘火箭。火箭在其瞬时静止参考系中的加速度为恒定值$a$。某时刻从火箭向前发射一枚导弹，导弹相对于火箭的初速度为$v_0$；随后导弹在惯性参考系中自由运动。

求导弹在火箭参考系中的运动情况，并判断火箭长时间后能否追上导弹而相遇。

提示：火箭瞬时静止系中沿火箭世界线的时间为火箭本征时。可使用

$$
\begin{aligned}
\cosh k&=\frac{e^k+e^{-k}}2,&
\sinh k&=\frac{e^k-e^{-k}}2,&
\tanh k&=\frac{\sinh k}{\cosh k},\\
\frac{d}{dk}\cosh k&=\sinh k,&
\frac{d}{dk}\sinh k&=\cosh k,&
\frac{d}{dk}\ln\cosh k&=\tanh k.
\end{aligned}
$$

![图 8-1　持续加速火箭与自由导弹从同一事件出发的时空关系，示意取$v_0=0.6c$。](../figures/question-08.png){width=72%}

## 一、题型定位

这是恒定固有加速度与惯性运动的相对论追及问题。“在瞬时静止系中的加速度恒定”指固有加速度恒为$a$，不是某个固定惯性系中的$dv/dt$恒为$a$。

最简洁的追及判定在发射瞬间与火箭共动的惯性系中进行：导弹匀速，火箭作双曲线运动，两条世界线再次相交就是追上。相遇事件的存在与否不依赖参考系，求出的地面时间和火箭本征时间却不相同。

描述“火箭参考系中的运动”时，还必须说明如何在持续变化的参考系中定义远处导弹的位置。以下采用火箭瞬时静止系的同时面构成的加速坐标，给出导弹距离随火箭本征时的函数，并区分局部相对速度与该坐标距离的变化率。

## 二、知识点

- 一维速度合成为$(V+u)/(1+Vu/c^2)$。
- 固有加速度$a$满足$dV/d\tau=a(1-V^2/c^2)$，其中$\tau$是火箭本征时。
- 洛伦兹因子$\gamma=1/\sqrt{1-V^2/c^2}$，惯性系时间满足$dt=\gamma\,d\tau$。
- 快度$\eta=\operatorname{artanh}(V/c)$使速度合成化为快度相加。
- 恒定固有加速度对应$V=c\tanh(a\tau/c)$，而不是无限增加的$V=a\tau$。
- 相遇必须满足同一事件的时间和位置，而不是只令火箭与导弹速度相等。
- 加速系的远处同时性随本征时变化，不能直接用不同位置的惯性系等时距离代替火箭瞬时静止系距离。
- 初始共同位置给出的零时间根不是发射后追上所要找的根。

## 三、物理图像

选择发射瞬间与火箭共动的惯性系$S$。取发射事件为$t=0,X=0$，火箭初速度为零；导弹初速度为$v_0$，向$+X$运动。假设$a>0$且$0<v_0<c$，火箭始终向前保持固有加速度$a$。

导弹不再受到推力，在$S$中始终满足$X_{\mathrm m}=v_0t$。火箭速度逐渐增加但始终小于$c$，其位移不是简单的$at^2/2$。

以$\tau$表示火箭本征时，另记

$$
\kappa=\frac{a\tau}{c},\qquad
\beta_0=\frac{v_0}{c},\qquad
\ell=\frac{c^2}{a}.
$$

$\kappa,\beta_0$无量纲，$\ell$是恒定固有加速度所对应的长度尺度。所有时间与距离公式都将按这三个量统一组织，避免把$\tau$和$t$混作同一个时间。

## 四、解题入口

先由速度合成得到火箭的微分方程，再积分求惯性系世界线：

$$
\begin{aligned}
V(\tau)&=c\tanh\kappa,\\
t(\tau)&=\frac ca\sinh\kappa,\\
X_{\mathrm R}(\tau)&=\frac{c^2}{a}(\cosh\kappa-1).
\end{aligned}
$$

导弹的惯性系位置为$v_0t(\tau)$。相遇条件是

$$
X_{\mathrm R}(\tau)=v_0t(\tau).
$$

求出非零时间根后，再建立火箭同时面上的导弹坐标$\xi(\tau)$，分析它先远离、后接近的完整运动。

## 五、解析

（1）从瞬时速度合成推导火箭的速度方程。

设某个火箭本征时$\tau$，火箭相对$S$的速度为$V$。在这一瞬间与火箭共动的惯性系内，经过很小本征时间$d\tau$后，火箭获得小速度

$$
du=a\,d\tau.
$$

用相对论速度合成将这个小速度转回$S$：

$$
V+dV=\frac{V+du}{1+Vdu/c^2}.
\tag{1}
$$

对$du$展开至一阶，使用$(1+\varepsilon)^{-1}=1-\varepsilon+O(\varepsilon^2)$：

$$
\begin{aligned}
V+dV
&=(V+du)\left(1-\frac{Vdu}{c^2}\right)+O(du^2)\\
&=V+du-\frac{V^2du}{c^2}+O(du^2).
\end{aligned}
$$

因此

$$
\begin{aligned}
dV&=\left(1-\frac{V^2}{c^2}\right)du,\\
\boxed{
\frac{dV}{d\tau}
=a\left(1-\frac{V^2}{c^2}\right)
}.
\end{aligned}
\tag{2}
$$

式（2）随$V$增加而降低速度增长率，保证$V$不越过$c$。若用$dV=a\,d\tau$，就忽略了速度合成的分母。

（2）分离变量并积分，不省略对数形式。

由式（2），

$$
\frac{dV}{1-V^2/c^2}=a\,d\tau.
$$

将左侧分母因式分解并作部分分式：

$$
\frac1{1-V^2/c^2}
=\frac c2\left(\frac1{c-V}+\frac1{c+V}\right).
\tag{3}
$$

从$V=0,\tau=0$积分：

$$
\begin{aligned}
a\tau
&=\frac c2\int_0^V
\left(\frac1{c-u}+\frac1{c+u}\right)du\\
&=\frac c2[-\ln(c-u)+\ln(c+u)]_0^V\\
&=\frac c2\ln\frac{c+V}{c-V}.
\end{aligned}
\tag{4}
$$

指数化并解出$V$：

$$
\begin{aligned}
\frac{c+V}{c-V}&=e^{2a\tau/c},\\
V(1+e^{2a\tau/c})&=c(e^{2a\tau/c}-1),\\
\boxed{
V(\tau)=c\frac{e^{2\kappa}-1}{e^{2\kappa}+1}
=c\tanh\kappa
}.
\end{aligned}
\tag{5}
$$

初始$\kappa=0$给出$V=0$；$\kappa\to\infty$时$V\to c$但不达到$c$，符合火箭为有质量物体的限制。

（3）求洛伦兹因子与两个时间的关系。

由$\beta_{\mathrm R}=V/c=\tanh\kappa$，恒等式$1-\tanh^2\kappa=1/\cosh^2\kappa$给出

$$
\gamma_{\mathrm R}=\cosh\kappa.
\tag{6}
$$

火箭沿自身世界线的本征时满足

$$
\frac{dt}{d\tau}=\gamma_{\mathrm R}=\cosh\kappa.
$$

用$d\tau=(c/a)\,d\kappa$积分：

$$
\begin{aligned}
t(\tau)
&=\int_0^\tau\cosh\left(\frac{a\sigma}{c}\right)d\sigma\\
&=\frac ca\int_0^\kappa\cosh u\,du\\
&=\boxed{\frac ca\sinh\kappa}.
\end{aligned}
\tag{7}
$$

惯性系时间$t$与火箭本征时$\tau$仅在低速短时间近似相等。后面的相遇时间必须标明是哪一种。

（4）积分火箭位移，建立双曲线世界线。

火箭在惯性系中的速度为$dX_{\mathrm R}/dt=V$，因此

$$
\begin{aligned}
\frac{dX_{\mathrm R}}{d\tau}
&=\frac{dX_{\mathrm R}}{dt}\frac{dt}{d\tau}\\
&=V\gamma_{\mathrm R}\\
&=c\tanh\kappa\cosh\kappa\\
&=c\sinh\kappa.
\end{aligned}
$$

积分并用$X_{\mathrm R}(0)=0$：

$$
\begin{aligned}
X_{\mathrm R}(\tau)
&=\frac{c^2}{a}\int_0^\kappa\sinh u\,du\\
&=\boxed{\frac{c^2}{a}(\cosh\kappa-1)}.
\end{aligned}
\tag{8}
$$

由$\cosh^2\kappa-\sinh^2\kappa=1$，消去$\kappa$可得

$$
\boxed{
(X_{\mathrm R}+\ell)^2-(ct)^2=\ell^2
},\qquad \ell=\frac{c^2}{a}.
\tag{9}
$$

火箭世界线是双曲线。导弹世界线则是直线

$$
X_{\mathrm m}=v_0t.
\tag{10}
$$

图8-2将两者放在同一惯性系时空图中，并画出某一火箭时刻的瞬时同时面。火箭与导弹的再次交点$C$才是追及事件；火箭速度刚等于$v_0$时，两者仍有非零距离。

![图 8-2　惯性导弹、双曲线火箭及瞬时静止系的同时面，示意取$v_0=0.6c$。](../figures/worldlines-08.png){width=75%}

（5）由位置相等建立相遇方程。

将式（7）、（8）代入$X_{\mathrm R}=v_0t$：

$$
\frac{c^2}{a}(\cosh\kappa-1)
=v_0\frac ca\sinh\kappa.
$$

约去$c^2/a$，得到

$$
\cosh\kappa-\beta_0\sinh\kappa=1.
\tag{11}
$$

用指数定义展开：

$$
\begin{aligned}
\frac{e^\kappa+e^{-\kappa}}2
-\beta_0\frac{e^\kappa-e^{-\kappa}}2
&=1,\\
(1-\beta_0)e^\kappa
+(1+\beta_0)e^{-\kappa}
&=2.
\end{aligned}
\tag{12}
$$

令$z=e^\kappa>0$，再乘以$z$：

$$
(1-\beta_0)z^2-2z+(1+\beta_0)=0.
\tag{13}
$$

对$0<\beta_0<1$，判别式为

$$
\Delta=4-4(1-\beta_0)(1+\beta_0)=4\beta_0^2>0.
$$

二次方程根为

$$
\begin{aligned}
z
&=\frac{2\pm2\beta_0}{2(1-\beta_0)}\\
&=1
\quad\text{或}\quad
\frac{1+\beta_0}{1-\beta_0}.
\end{aligned}
\tag{14}
$$

第一根$z=1$对应$\kappa=0$，只是发射瞬间的共同位置。第二根大于一，才是发射后相遇：

$$
\boxed{
\tau_{\mathrm c}
=\frac ca\ln\frac{1+\beta_0}{1-\beta_0}
=\frac ca\ln\frac{c+v_0}{c-v_0}
}.
\tag{15}
$$

因为分子、分母均为正，且比值大于一，$\tau_{\mathrm c}>0$。对任意$a>0$、$0<v_0<c$，这个本征时间有限，所以持续保持固有加速度的火箭能够追上自由导弹。

（6）求惯性系中的相遇时间与位置。

定义导弹快度

$$
\eta_0=\operatorname{artanh}\beta_0
=\frac12\ln\frac{1+\beta_0}{1-\beta_0}.
$$

由式（15），相遇时火箭快度为$\kappa_{\mathrm c}=2\eta_0$。双曲函数倍角公式给出

$$
\sinh(2\eta_0)
=\frac{2\beta_0}{1-\beta_0^2}.
\tag{16}
$$

因此

$$
\begin{aligned}
t_{\mathrm c}
&=\frac ca\sinh\kappa_{\mathrm c}\\
&=\frac ca\frac{2\beta_0}{1-\beta_0^2}\\
&=\boxed{\frac{2v_0}{a(1-v_0^2/c^2)}}.
\end{aligned}
\tag{17}
$$

相遇位置为

$$
\boxed{
X_{\mathrm c}=v_0t_{\mathrm c}
=\frac{2v_0^2}{a(1-v_0^2/c^2)}
}.
\tag{18}
$$

由于沿火箭世界线$\gamma_{\mathrm R}\ge1$，有$t_{\mathrm c}>\tau_{\mathrm c}$，与时间膨胀一致。不能把式（17）直接作为火箭上乘客钟表记录的时间。

（7）建立火箭加速坐标中的远处位置。

在火箭本征时$\tau$，火箭的惯性系事件为$(t_{\mathrm R},X_{\mathrm R})$，速度为$V=c\tanh\kappa$。在它的瞬时静止系中，取同一时刻、距火箭向前$\xi$的事件。

将这个纯空间间隔$(dt'=0,dX'=\xi)$用洛伦兹变换转回$S$，得到

$$
t-t_{\mathrm R}=\gamma_{\mathrm R}\frac{V\xi}{c^2},
\qquad
X-X_{\mathrm R}=\gamma_{\mathrm R}\xi.
\tag{19}
$$

代入$\gamma_{\mathrm R}=\cosh\kappa$、$V\gamma_{\mathrm R}=c\sinh\kappa$及式（7）、（8）：

$$
\boxed{
\begin{aligned}
ct&=(\ell+\xi)\sinh\kappa,\\
X&=(\ell+\xi)\cosh\kappa-\ell.
\end{aligned}
}
\tag{20}
$$

这定义了火箭瞬时同时面上的加速系位置$\xi$。火箭自身始终为$\xi=0$。空间坐标$\xi$在同一同时面上是火箭瞬时静止系量得的距离，而不是简单的$X_{\mathrm m}(t)-X_{\mathrm R}(t)$。

（8）把导弹惯性世界线代入加速坐标，求其距离函数。

导弹满足$X=\beta_0ct$。将式（20）两式代入：

$$
(\ell+\xi)\cosh\kappa-\ell
=\beta_0(\ell+\xi)\sinh\kappa.
$$

移项并提取$\ell+\xi$：

$$
\begin{aligned}
(\ell+\xi)
(\cosh\kappa-\beta_0\sinh\kappa)&=\ell,\\
\ell+\xi
&=\frac{\ell}{\cosh\kappa-\beta_0\sinh\kappa}.
\end{aligned}
$$

因此

$$
\boxed{
\xi(\tau)=\frac{c^2}{a}
\left[
\frac1{\cosh(a\tau/c)-\beta_0\sinh(a\tau/c)}
-1
\right]
}.
\tag{21}
$$

对$0<\beta_0<1$，分母始终为正。用$\beta_0=\tanh\eta_0$和$\gamma_0=\cosh\eta_0$，可化成更容易观察形状的形式：

$$
\begin{aligned}
\cosh\kappa-\beta_0\sinh\kappa
&=\frac{\cosh\kappa\cosh\eta_0
-\sinh\kappa\sinh\eta_0}{\cosh\eta_0}\\
&=\frac{\cosh(\kappa-\eta_0)}{\gamma_0}.
\end{aligned}
$$

于是

$$
\boxed{
\xi(\tau)=\ell
\left[\frac{\gamma_0}{\cosh(\kappa-\eta_0)}-1\right].
}
\tag{22}
$$

图8-3画出$\xi$及局部相对速度随火箭快度的变化。曲线以$\kappa=\eta_0$为距离最大点，$\kappa=2\eta_0$时回到$\xi=0$。

![图 8-3　相遇前火箭加速坐标中的导弹距离及局部相对速度，示意取$v_0=0.6c$。](../figures/accelerated-08.png){width=86%}

（9）求先远离后接近的转折时刻与最大距离。

记$D(\kappa)=\cosh\kappa-\beta_0\sinh\kappa$。对式（21）求导：

$$
\begin{aligned}
\frac{d\xi}{d\tau}
&=-\ell\frac{D'(\kappa)}{D^2(\kappa)}\frac ac\\
&=c\frac{\beta_0\cosh\kappa-\sinh\kappa}{D^2(\kappa)}.
\end{aligned}
\tag{23}
$$

分母为正，所以转折条件是

$$
\beta_0\cosh\kappa-\sinh\kappa=0,
\qquad
\tanh\kappa=\beta_0.
$$

即

$$
\boxed{
\tau_{\mathrm{turn}}
=\frac ca\operatorname{artanh}\beta_0
=\frac12\tau_{\mathrm c}
}.
\tag{24}
$$

在此之前$\xi$增加，导弹在火箭看来向前远离；在此之后$\xi$减小，导弹向火箭靠近。这个转折时刻火箭速度$V=v_0$，但距离仍不为零。

将$\kappa=\eta_0$代入式（22），由于$\cosh0=1$，

$$
\boxed{
\xi_{\max}
=\ell(\gamma_0-1)
=\frac{c^2}{a}
\left(\frac1{\sqrt{1-v_0^2/c^2}}-1\right)
}.
\tag{25}
$$

速度相等表示瞬时相对速度为零，只能判断间距达到极值，不能判断两物体已经相遇。

相遇之后，$\kappa>2\eta_0$，有$\kappa-\eta_0>\eta_0$，故$\cosh(\kappa-\eta_0)>\cosh\eta_0=\gamma_0$。由式（22）立即得到

$$
-\ell<\xi(\tau)<0.
$$

负号表示导弹位于火箭后方，不是出现“负路程”。当火箭继续加速、$\kappa\to\infty$时，分母趋于无穷，因此在这套加速坐标覆盖的分支上

$$
\xi(\tau)\longrightarrow-\ell=-\frac{c^2}{a}.
$$

它趋近的是加速坐标的后方边界，并不会再次回到$\xi=0$。这一结论只描述同一火箭同时性约定下的位置，不能把它误解为固定惯性系中的导弹位移停止增长；在$S$中导弹依旧满足$X_{\rm m}=v_0t$。

（10）给出局部相对速度，并区分坐标距离变化率。

在本征时$\tau$的火箭瞬时静止系中，用一维速度变换：

$$
\begin{aligned}
u_{\mathrm{rel}}(\tau)
&=\frac{v_0-V(\tau)}{1-v_0V(\tau)/c^2}\\
&=c\frac{\beta_0-\tanh\kappa}
{1-\beta_0\tanh\kappa}\\
&=c\frac{\beta_0\cosh\kappa-\sinh\kappa}
{\cosh\kappa-\beta_0\sinh\kappa}\\
&=\boxed{-c\tanh(\kappa-\eta_0)}.
\end{aligned}
\tag{26}
$$

初始$u_{\mathrm{rel}}=v_0$，转折时为零，相遇时$\kappa=2\eta_0$，有

$$
\boxed{u_{\mathrm{rel}}(\tau_{\mathrm c})=-v_0}.
\tag{27}
$$

火箭看到导弹以与发射时大小相同、方向相反的局部相对速度返回；这对应快度从$+\eta_0$变为$-\eta_0$。

式（23）与式（26）并非处处相等，因为$\xi(\tau)$把远处位置都用火箭原点的钟$\tau$作参数。由式（21），

$$
1+\frac{\xi}{\ell}=\frac1D.
$$

所以

$$
\boxed{
\frac{d\xi}{d\tau}
=\left(1+\frac{a\xi}{c^2}\right)u_{\mathrm{rel}}
}.
\tag{28}
$$

在火箭原点$\xi=0$，两者相等；远处的同时面随加速改变，不能直接将速度合成所得$u_{\mathrm{rel}}$对原点本征时积分当作位置。式（21）由明确的同时性变换得到，避免了这个跳步。

（11）用具体无量纲例子复查全部关键事件。

只作为公式核验，取$v_0=0.6c$。此时

$$
\beta_0=\frac35,\qquad
\gamma_0=\frac54,\qquad
\eta_0=\frac12\ln\frac{1+3/5}{1-3/5}
=\ln2.
$$

转折和相遇本征时分别为

$$
\tau_{\mathrm{turn}}=\frac ca\ln2,\qquad
\tau_{\mathrm c}=\frac ca\ln4.
$$

最大距离为

$$
\xi_{\max}=\frac14\frac{c^2}{a}.
$$

相遇惯性系时间和位置为

$$
\begin{aligned}
t_{\mathrm c}
&=\frac{2(3/5)c}{a[1-(3/5)^2]}
=\frac{15}{8}\frac ca,\\
X_{\mathrm c}
&=\frac35c\,t_{\mathrm c}
=\frac98\frac{c^2}{a}.
\end{aligned}
\tag{29}
$$

直接检查火箭世界线：

$$
\sinh(\ln4)=\frac{4-1/4}{2}=\frac{15}{8},
\qquad
\cosh(\ln4)-1=\frac{4+1/4}{2}-1=\frac98.
$$

与导弹位置完全一致。火箭相遇速度为

$$
V_{\mathrm c}
=c\tanh(2\eta_0)
=c\frac{2\beta_0}{1+\beta_0^2}
=\frac{15}{17}c,
$$

大于$v_0=3c/5$而小于$c$，没有出现超光速追赶。

（12）检查低速极限、光速极限和加速度条件。

当$\beta_0\ll1$，使用

$$
\ln\frac{1+\beta_0}{1-\beta_0}
=2\left(\beta_0+\frac{\beta_0^3}{3}+\cdots\right),
$$

相遇本征时为

$$
\tau_{\mathrm c}
=\frac{2v_0}{a}
\left(1+\frac{v_0^2}{3c^2}+\cdots\right).
\tag{30}
$$

最大距离中的洛伦兹因子可用二项式展开。取$z=\beta_0^2$，将$(1-z)^{-1/2}$展开至$z^2$，系数分别为$1/2$与$(-1/2)(-3/2)/2=3/8$：

$$
\begin{aligned}
\gamma_0
&=(1-\beta_0^2)^{-1/2}\\
&=1+\frac12\beta_0^2+\frac38\beta_0^4
+O(\beta_0^6),\\
\xi_{\max}
&=\frac{c^2}{a}(\gamma_0-1)\\
&=\frac{v_0^2}{2a}
+\frac{3v_0^4}{8ac^2}
+O\!\left(\frac{v_0^6}{ac^4}\right).
\end{aligned}
$$

保留最低阶得到

$$
\xi_{\max}
=\frac{v_0^2}{2a}
+O\left(\frac{v_0^4}{ac^2}\right).
\tag{31}
$$

这分别恢复牛顿模型中$\xi=v_0\tau-a\tau^2/2$的追及时间$2v_0/a$与最大间距$v_0^2/(2a)$。低速极限是对整条推导链的重要检查。

当$v_0\to c^-$，式（15）的对数发散，追及时间趋于无穷。若发射的是光信号$v_0=c$，相遇方程只剩初始根，持续加速火箭也不能追上向前发出的光。不能将“能够追上任何低于光速的惯性导弹”误说成“最终能够追上光”。

光速端点也能直接从位置条件核验，不必把发散公式机械代入。此时$\beta_0=1$，式（11）化为

$$
\cosh\kappa-\sinh\kappa
=e^{-\kappa}=1.
$$

对实数$\kappa\ge0$，指数函数严格递减，唯一解为$\kappa=0$，即发射事件；不存在后来的相遇根。

当$a\to0^+$且$v_0>0$固定，追及时间也趋于无穷；若$a=0$，火箭保持初始静止而导弹向前匀速离开，不再相遇。以上结论要求火箭始终保持给定正固有加速度；若途中停止加速，能否追上须另作判断。

总结：对$a>0$、$0<v_0<c$，导弹在火箭加速坐标中先向前远离，达到式（25）的最大距离后返回，并在式（15）的有限本征时相遇。火箭本身在惯性系中始终不超过光速。

## 六、关键洞察

用快度可以直接比较火箭与导弹的速度变化。导弹快度固定为$\eta_0$，火箭快度为$a\tau/c$线性增加，相对快度为$\eta_0-a\tau/c$。相对速度在$\tau_{\mathrm{turn}}$处为零，相遇时相对快度变为$-\eta_0$。

然而“相对快度反号”本身不足以证明相遇；真正的相遇条件仍是世界线交点。这里恰好由位置方程得到$\kappa_{\mathrm c}=2\eta_0$，才使速度关系具有这种对称形式。

火箭加速坐标的时间尺度随位置不同。对式（20）求微分并代入平直时空间隔：

$$
c^2dt^2-dX^2
=\left(1+\frac{a\xi}{c^2}\right)^2c^2d\tau^2-d\xi^2.
$$

这解释式（28）中坐标速度与局部速度的比例。$\xi$不是任意“伪距离”，而是在火箭瞬时同时面上构造的空间距离；坐标时间则使用原点火箭的钟，必须同时说明测量约定。

火箭在惯性系的加速度为

$$
\frac{dV}{dt}
=\frac{dV/d\tau}{dt/d\tau}
=a\,\operatorname{sech}^3\kappa
=\frac a{\gamma_{\mathrm R}^3}.
$$

它随速度增长而减小。把恒定固有加速度误当成恒定惯性系加速度，会既算错世界线，又算错本征时，还可能得到超过光速的速度。

## 七、易错点

- 使用$V=at$描述恒定固有加速度，而不区分固定惯性系与瞬时静止系。
- 对本征时积分时漏乘$\gamma$，把火箭本征时当作地面时间。
- 将$V=v_0$判作追上；这只对应最大间距。
- 解二次方程保留初始零时间根而遗漏发射后第二个根。
- 用$X_{\mathrm m}(t)-X_{\mathrm R}(t)$冒充火箭瞬时静止系中的距离。
- 将局部相对速度直接对原点本征时积分，忽略远处同时性的变化。
- 使用$v_0>c$或把$v_0=c$代入有限时间公式，忘记定义域和极限。
- 推断火箭能追上光，或认为趋近光速意味着所有相对速度都为零。
- 忽略火箭必须持续加速的条件，把中途停止加速的情形也归入同一结论。

## 八、课堂讲解建议

教师先让学生用牛顿方法判断“速度相等”与“位置相等”的区别，再说明相对论中这个区别仍然存在。发射瞬间的共动惯性系应当首先固定下来，板书始终用$V$表示火箭、$v_0$表示自由导弹，避免把两个速度混为同一变量。

速度合成的一阶展开保留到式（2），让学生看到恒定$a$作用在哪个时间和哪个参考系中。世界线积分要求学生明确$dt/d\tau=\gamma$，两次积分的边界都是发射事件。

追及方程先用指数变成二次式，由学生解释两个根的物理含义。加速坐标的距离可在追及判定后讲解，利用同时面图指出不能简单相减同一地面时刻的位置。最后安排$v_0\ll c$和$v_0\to c$两个极限，检验学生是否理解公式而不只是记住对数。

## 九、变式训练

变式一：火箭只保持固有加速度至本征时$\tau_b$，随后不再加速而保持当时的惯性速度。判断能否追上，并求火箭自身记录的追及时间。

记$\kappa_b=a\tau_b/c$。若$\kappa_b\ge2\eta_0$，火箭在停止加速前已追上，时间仍为$\tau_{\mathrm c}=2c\eta_0/a$。

若$\kappa_b<2\eta_0$，停加速时导弹还在火箭前方。取该时刻瞬时静止系作为之后的固定共动惯性系。导弹初位置和相对速度为

$$
\begin{aligned}
\xi_b
&=\ell\left[
\frac1{\cosh\kappa_b-\beta_0\sinh\kappa_b}-1
\right],\\
u_b&=-c\tanh(\kappa_b-\eta_0).
\end{aligned}
$$

如果$\kappa_b<\eta_0$，$u_b>0$，导弹继续远离，无法追上。若$\kappa_b=\eta_0$，$u_b=0$而$\xi_b>0$，两者同速保持非零距离，也不相遇。

只有$\eta_0<\kappa_b<2\eta_0$时，$u_b<0$，导弹在之后的固定共动系中以恒定速度向火箭接近。额外所需本征时间为

$$
\Delta\tau_{\mathrm{coast}}
=\frac{\xi_b}{-u_b}.
$$

因此

$$
\boxed{
\tau_{\mathrm{hit}}
=\tau_b+
\frac{
\ell\left[(\cosh\kappa_b-\beta_0\sinh\kappa_b)^{-1}-1\right]
}{
c\tanh(\kappa_b-\eta_0)
}
}.
$$

这里使用的是停止加速后不再改变的同时性，距离与速度可以直接作匀速追及计算。当$\kappa_b\to\eta_0^+$，分母趋于零而距离非零，追及时间发散；当$\kappa_b\to2\eta_0^-$，距离趋于零，恢复制动前的相遇时间。它说明“火箭速度超过导弹”是停止加速后能继续追上的必要条件，但还需等待间距消失。

变式二：导弹初速度 $v_0=0.6c$，火箭从静止以恒定固有加速度 $a$ 追赶。求追及时的火箭本征时、惯性系时间和位置。

解：导弹快度 $\eta_0=\operatorname{artanh}0.6=\ln2$，位置相等的非零解给 $\kappa_c=2\eta_0=\ln4$。代入双曲世界线：

$$
\tau_c=\frac ca\ln4,\quad
 t_c=\frac ca\sinh(\ln4)=\frac{15c}{8a},\quad
 X_c=\frac{c^2}a[\cosh(\ln4)-1]=\frac{9c^2}{8a}.
$$

核对 $v_0t_c=9c^2/(8a)$，与火箭位置相同。火箭追及速度为 $c\tanh(\ln4)=15c/17$，始终低于光速。

变式三：仍取 $v_0=0.6c$，求火箭瞬时同时面上导弹与火箭的最大距离、对应本征时及该时刻的局部相对速度。

解：令 $\ell=c^2/a$，距离为 $\xi=\ell[(\cosh\kappa-0.6\sinh\kappa)^{-1}-1]$。分母的导数为 $\sinh\kappa-0.6\cosh\kappa$，零点是 $\kappa=\ln2$；分母此处取最小值 $\sqrt{1-0.6^2}=0.8$。故

$$
\xi_{\max}=\frac{c^2}{4a},\qquad \tau_{\max}=\frac ca\ln2.
$$

局部相对速度为 $c\tanh(\eta_0-\kappa)$，该时刻为零。它早于追及时 $2c\ln2/a$，零相对速度不能代替位置相遇条件。

变式四：已知火箭固有加速度 $a$ 和自身记录的追及时间 $\tau_c>0$，反求导弹初速，并取低速极限。

解：由非零世界线交点 $a\tau_c/c=2\operatorname{artanh}\beta_0$，直接得到

$$
v_0=c\tanh\left(\frac{a\tau_c}{2c}\right).
$$

若 $a\tau_c\ll c$，展开 $\tanh z=z-z^3/3+O(z^5)$，有 $v_0=a\tau_c/2-a^3\tau_c^3/(24c^2)+O(c^{-4})$。最低阶恢复牛顿追及时间 $\tau_c\simeq2v_0/a$；完整表达式自动限制 $v_0<c$。
