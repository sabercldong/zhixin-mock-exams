# 第 8 题

<!-- question-start -->

考虑真空中平面光波的传播。在地面惯性参考系 $S$ 中，光波传播方向的单位向量为 $(\cos\theta,\sin\theta,0)$，光速为 $c$，角频率为 $\omega$。振动可写为

$$
E(x,y,z,t)=E_0\cos(\omega t-k_xx-k_yy+\phi_0),
$$

其中

$$
k_x=\frac{\omega}{c}\cos\theta,\qquad
k_y=\frac{\omega}{c}\sin\theta.
$$

相位为 $\phi(x,y,z,t)=\omega t-k_xx-k_yy+\phi_0$，波面是等相位面。

参考系 $S'$ 相对 $S$ 以速度 $u$ 沿 $x$ 轴正向运动。相位在参考系变换下不变，时空坐标满足洛伦兹变换。求 $S'$ 中相位满足 $\phi=\phi_0$ 的波面方程；利用速度变换求 $S'$ 中光传播的方向，并验证传播方向仍垂直于波面。

![图 8-1　平面光波的空间波面及其在横截面内的传播方向。](../figures/question-08.png)

<!-- question-end -->

## 一、题型定位

利用相位不变性变换波面，同时利用相对论速度变换求光线方向，再比较二者。这是从“波的等相位面”和“光线的传播运动”两条独立描述验证同一几何性质。

本题不是把一个固定时刻的空间平面单独做长度收缩。不同参考系的同时性不同，必须对时间与空间坐标一起作洛伦兹变换，然后在新参考系中固定 $t'$ 讨论波面。

## 二、知识点

- 相位在同一时空事件处具有不依赖惯性系的值。
- 沿 $x$ 方向的洛伦兹变换同时混合 $x$ 与 $t$，而 $y,z$ 不变。
- 平面方程的空间坐标系数构成其法向量。
- 相对论速度变换应由时空微分之比求出，不能用普通速度相减。
- 证明光线垂直波面，可证明其速度矢量平行于波面法向量。
- 用矢量表达式可避免特殊方向下斜率无穷大或分母为零的问题。
- 真空光速在各惯性系中均为 $c$，可作为独立的代数检查。

## 三、物理图像

两参考系坐标轴平行，$S'$ 的原点沿 $S$ 中的 $+x$ 方向运动。令

$$
\beta=\frac uc,\qquad
\gamma=\frac1{\sqrt{1-\beta^2}},
\qquad 0\le\beta<1.
$$

在 $S$ 中，光线速度为

$$
\boldsymbol c=c(\cos\theta,\sin\theta,0).
$$

虽然波矢没有 $z$ 分量，波面仍是三维空间中的平面：它沿整个 $z$ 方向延伸。图中与 $xy$ 平面的交线只是波面的一个截面，不能将交线本身误当成全部波面。

在固定 $t$ 的截面上，$\phi=\phi_0$ 对应

$$
k_xx+k_yy=\omega t.
$$

其法向量是 $(k_x,k_y,0)$，与给定光线方向相同。本题要证明变换以后这一对应关系仍成立。

## 四、解题入口

先把旧坐标 $x,y,t$ 用新坐标 $x',y',t'$ 表示，代入完整相位，再按 $t',x',y'$ 收集系数。这样会同时得到新角频率与新波矢。

随后对一条光线的相邻两个事件应用正向洛伦兹变换，用 $\mathrm dx'/\mathrm dt'$、$\mathrm dy'/\mathrm dt'$ 求速度。最后把速度写成新波矢的正比例倍数，而不只比较两条直线的斜率。

## 五、解析

（1）确定所需的洛伦兹变换方向。

由 $S$ 到 $S'$ 的正向变换为

$$
\begin{aligned}
x'&=\gamma(x-ut),\\
t'&=\gamma\left(t-\frac{ux}{c^2}\right),\\
y'&=y,\qquad z'=z.
\end{aligned}
$$

例如 $S'$ 原点满足 $x=ut$，代入第一式得到 $x'=0$，这可以检查相对速度的符号。

现在原相位写成旧坐标的函数，若要把它改写为新坐标的函数，应该使用逆变换：

$$
\boxed{
x=\gamma(x'+ut'),\quad
t=\gamma\left(t'+\frac{ux'}{c^2}\right),\quad
y=y',\quad z=z'.
}
$$

逆变换中的 $u$ 项是正号。不能一边把相位中的变量改成带撇符号，一边仍套用旧到新的坐标公式。

（2）把完整相位代入逆变换。

原相位为

$$
\phi=\omega t-k_xx-k_yy+\phi_0.
$$

逐项代入：

$$
\begin{aligned}
\phi
&=\omega\gamma\left(t'+\frac{ux'}{c^2}\right)
-k_x\gamma(x'+ut')-k_yy'+\phi_0\\
&=\gamma\omega t'
+\gamma\frac{\omega u}{c^2}x'
-\gamma k_xx'
-\gamma uk_xt'
-k_yy'+\phi_0\\
&=\gamma(\omega-uk_x)t'
-\gamma\left(k_x-\frac{\omega u}{c^2}\right)x'
-k_yy'+\phi_0.
\end{aligned}
$$

与新参考系中的标准相位形式

$$
\phi=\omega't'-k_x'x'-k_y'y'+\phi_0
$$

逐项比较，得到

$$
\boxed{
\omega'=\gamma(\omega-uk_x),\quad
k_x'=\gamma\left(k_x-\frac{\omega u}{c^2}\right),\quad
k_y'=k_y,\quad k_z'=0.
}
$$

这里 $\omega'$ 是时间系数，$-k_x'$ 是 $x'$ 的系数，比较时不要把相位原有的负号漏掉。$k_y$ 不变并不表示传播角不变，因为 $k_x$ 已经改变。

（3）代入旧波矢，写出显式的新频率与新波矢。

用 $k_x=(\omega/c)\cos\theta$、$k_y=(\omega/c)\sin\theta$：

$$
\begin{aligned}
\omega'
&=\gamma\left(\omega-\frac{u\omega}{c}\cos\theta\right)
=\boxed{\gamma\omega(1-\beta\cos\theta)},\\
k_x'
&=\gamma\left(\frac{\omega}{c}\cos\theta-\frac{\omega u}{c^2}\right)
=\boxed{\frac{\gamma\omega}{c}(\cos\theta-\beta)},\\
k_y'&=\boxed{\frac{\omega}{c}\sin\theta}.
\end{aligned}
$$

由于 $|\beta\cos\theta|<1$，有

$$
1-\beta\cos\theta>0,
$$

因此 $\omega'>0$。这个正性检查不仅保证了频率物理合理，也会用于判断速度与波矢是否同向。

（4）求 $\phi=\phi_0$ 的波面方程。

在新参考系中令相位等于指定常数 $\phi_0$：

$$
\omega't'-k_x'x'-k_y'y'+\phi_0=\phi_0.
$$

消去两侧的 $\phi_0$，得到

$$
\boxed{k_x'x'+k_y'y'=\omega't'.}
$$

代入各系数，再同除正数 $\omega/c$：

$$
\boxed{
\gamma(\cos\theta-\beta)x'
+\sin\theta\,y'
=\gamma c(1-\beta\cos\theta)t'.
}
$$

这就是所求波面方程；$z'$ 不受限制，故每个固定 $t'$ 对应一个沿 $z'$ 延伸的平面。

若 $\sin\theta\ne0$，可把其在 $x'y'$ 平面内的交线改写为

$$
y'=-\frac{\gamma(\cos\theta-\beta)}{\sin\theta}x'
+\frac{\gamma c(1-\beta\cos\theta)}{\sin\theta}t'.
$$

但这只是便于画截面直线的形式。主答案应保留不除以 $\sin\theta$ 的平面方程，因为 $\theta=0,\pi$ 时仍有完全正常的波面，不能因某种斜率写法除零而把它排除。

（5）从两个相邻事件推导光线速度变换。

在旧参考系中，沿一条光线取相邻两个事件，满足

$$
\mathrm dx=c\cos\theta\,\mathrm dt,\qquad
\mathrm dy=c\sin\theta\,\mathrm dt,\qquad
\mathrm dz=0.
$$

对正向洛伦兹变换取微分：

$$
\begin{aligned}
\mathrm dt'
&=\gamma\left(\mathrm dt-\frac{u\,\mathrm dx}{c^2}\right)\\
&=\gamma(1-\beta\cos\theta)\,\mathrm dt,\\
\mathrm dx'
&=\gamma(\mathrm dx-u\,\mathrm dt)\\
&=\gamma(c\cos\theta-u)\,\mathrm dt,\\
\mathrm dy'&=c\sin\theta\,\mathrm dt.
\end{aligned}
$$

新参考系中的速度分量是相应空间微分除以同一个 $\mathrm dt'$。分别相除，得

$$
\boxed{
c_x'=\frac{c\cos\theta-u}{1-\beta\cos\theta}
=c\frac{\cos\theta-\beta}{1-\beta\cos\theta},
}
$$

$$
\boxed{
c_y'=\frac{c\sin\theta}
{\gamma(1-\beta\cos\theta)},\qquad c_z'=0.
}
$$

$x$ 方向的分子、分母中都有 $\gamma$，所以它约去；$y$ 坐标虽然不变，但时间间隔改变，因此 $c_y'$ 不能仍写成 $c\sin\theta$。

（6）先验证速度大小仍为 $c$。

把两个速度分量平方相加：

$$
\frac{c_x'^2+c_y'^2}{c^2}
=\frac{(\cos\theta-\beta)^2+
\sin^2\theta/\gamma^2}
{(1-\beta\cos\theta)^2}.
$$

用 $1/\gamma^2=1-\beta^2$ 展开分子：

$$
\begin{aligned}
&(\cos\theta-\beta)^2
+(1-\beta^2)\sin^2\theta\\
&=\cos^2\theta-2\beta\cos\theta+\beta^2
+\sin^2\theta-\beta^2\sin^2\theta\\
&=1-2\beta\cos\theta
+\beta^2(1-\sin^2\theta)\\
&=1-2\beta\cos\theta+\beta^2\cos^2\theta\\
&=(1-\beta\cos\theta)^2.
\end{aligned}
$$

所以

$$
\boxed{c_x'^2+c_y'^2=c^2}.
$$

这项计算可以排查速度变换中漏掉的 $\gamma$ 或分母。如果只使用普通的 $\boldsymbol c'=\boldsymbol c-u\hat{\boldsymbol x}$，就不会得到这个恒等式。

（7）证明传播方向垂直于新波面。

新波面的空间系数给出一个法向量

$$
\boldsymbol n'
=\bigl(\gamma(\cos\theta-\beta),\,\sin\theta,\,0\bigr).
$$

图8-2把新波面与其法线画在同一空间投影中。箭头所示方向既是新波矢方向，也是下面速度矢量的方向；$z'$ 轴仍位于每个波面内。

![图 8-2　新参考系中波面法线与光线传播方向的一致性。](../figures/solution-08.png)

将速度矢量提取共同正因子：

$$
\begin{aligned}
\boldsymbol c'
&=\left(
\frac{c(\cos\theta-\beta)}{1-\beta\cos\theta},
\frac{c\sin\theta}{\gamma(1-\beta\cos\theta)},
0\right)\\
&=\boxed{
\frac{c}{\gamma(1-\beta\cos\theta)}
\boldsymbol n'}.
\end{aligned}
$$

因为比例因子严格为正，$\boldsymbol c'$ 与波面法向量同向。因此

$$
\boxed{\text{新参考系中的光线传播方向仍垂直于波面。}}
$$

也可以用新波矢写为

$$
\boxed{\boldsymbol c'=\frac{c^2}{\omega'}\boldsymbol k'}.
$$

这个矢量等式直接覆盖 $k_x'=0$ 或 $k_y'=0$ 的情形，比“波面斜率乘光线斜率等于 $-1$”的证明更完整。

（8）求新传播角，并分清象限。

令新传播方向与 $+x'$ 轴的夹角为 $\theta'$。由于速率已经证明为 $c$，

$$
\boxed{
\cos\theta'=\frac{\cos\theta-\beta}{1-\beta\cos\theta},
\qquad
\sin\theta'=
\frac{\sin\theta}{\gamma(1-\beta\cos\theta)}.
}
$$

若 $\cos\theta\ne\beta$，可相除得到

$$
\tan\theta'=
\frac{\sin\theta}{\gamma(\cos\theta-\beta)}.
$$

但仅知道正切值不能唯一确定象限。必须同时使用上面的正弦、余弦，或使用能够识别象限的双参数反正切。

例如 $0<\theta<\pi$ 时，$\sin\theta'>0$。若 $\cos\theta<\beta$，则 $\cos\theta'<0$，所以 $\theta'$ 位于第二象限，而不是对负正切值直接取一个负的小角。

（9）核对特殊方向，确认公式没有遗漏边界。

当 $u=0$ 时，$\beta=0,\gamma=1$，得到 $\omega'=\omega$、$\boldsymbol k'=\boldsymbol k$、$\theta'=\theta$，恢复同一参考系的结果。

当 $\theta=0$，光沿 $+x$ 传播，有

$$
\begin{aligned}
c_x'&=c,\qquad c_y'=0,\\
\omega'&=\gamma\omega(1-\beta)
=\omega\sqrt{\frac{1-\beta}{1+\beta}}.
\end{aligned}
$$

新波面为 $x'=ct'$，仍沿 $+x'$ 传播。参考系追赶光波使频率降低，但不能使光速低于 $c$。

当 $\theta=\pi$，光沿 $-x$ 传播，有

$$
c_x'=-c,\quad c_y'=0,\quad
\omega'=\omega\sqrt{\frac{1+\beta}{1-\beta}},
$$

波面为 $x'=-ct'$。此时参考系与光迎面相遇，频率升高。

当 $\cos\theta=\beta$，新波矢的 $x'$ 分量为零，速度也有 $c_x'=0$。若取 $\sin\theta>0$，则 $\sin\theta=\sqrt{1-\beta^2}=1/\gamma$，代入得到 $c_y'=c$，波面为 $y'=ct'$。虽然旧参考系中光有正的 $x$ 分量，新参考系中它恰沿 $+y'$ 传播。

（10）用一组有明显方向变化的数据检验图与式。

取 $\beta=3/5$、$\theta=60^\circ$，则

$$
\gamma=\frac54,\qquad
1-\beta\cos\theta=1-\frac35\frac12=\frac7{10}.
$$

新频率为

$$
\omega'=\frac54\frac7{10}\omega=\frac78\omega.
$$

新法向量为

$$
\boldsymbol n'
=\left(\frac54\left(\frac12-\frac35\right),
\frac{\sqrt3}{2},0\right)
=\left(-\frac18,\frac{\sqrt3}{2},0\right).
$$

速度分量逐项为

$$
\begin{aligned}
c_x'&=c\,\frac{-1/10}{7/10}=-\frac c7,\\
c_y'&=c\,\frac{\sqrt3/2}{(5/4)(7/10)}
=\frac{4\sqrt3}{7}c.
\end{aligned}
$$

平方和为 $(1+48)c^2/49=c^2$。波面法向量与速度矢量均有负的 $x'$ 分量和正的 $y'$ 分量，与图8-2的方向一致。传播角约为 $98.21^\circ$；这只是方向改变，光速大小并没有变化。

（11）低速相对运动极限的检查。

在 $\beta\ll1$ 时，$\gamma=1+O(\beta^2)$，而

$$
\frac1{1-\beta\cos\theta}
=1+\beta\cos\theta+O(\beta^2).
$$

代入两个速度分量并保留 $\beta$ 的一次项：

$$
\begin{aligned}
c_x'
&\approx c(\cos\theta-\beta)(1+\beta\cos\theta)\\
&\approx c\cos\theta-c\beta(1-\cos^2\theta)\\
&=c\cos\theta-u\sin^2\theta,\\
c_y'
&\approx c\sin\theta(1+\beta\cos\theta)\\
&=c\sin\theta+u\sin\theta\cos\theta.
\end{aligned}
$$

可见即使 $u$ 很小，也不能仅把纵向速度减去 $u$、横向速度保持原值；两分量的一阶修正必须共同维持光速不变。

再设 $\theta'=\theta+\delta\theta$，其中 $\delta\theta$ 是一次小量。由余弦差的展开，

$$
\begin{aligned}
\cos\theta'
&\approx\cos\theta-\delta\theta\sin\theta,\\
\frac{c_x'}c
&\approx\cos\theta-\beta\sin^2\theta.
\end{aligned}
$$

在 $\sin\theta\ne0$ 时比较可得

$$
\boxed{\delta\theta\approx\beta\sin\theta}.
$$

对于 $0<\theta<\pi$，$\beta>0$ 导致传播角增大，与完整方向公式的象限判断一致。$\theta=0,\pi$ 时应直接使用先前的轴向结果，方向保持不变。与此同时 $\omega'\approx\omega(1-\beta\cos\theta)$，给出了与追赶、迎面两种情形一致的频率一阶变化。

## 六、关键洞察

确定新系波面法线，须同时考虑相对同时性和空间坐标的变换。要在新参考系中取一个波面，必须选取相同的 $t'$；这些事件在旧参考系中的时间一般并不相同。如果把旧系某一固定时刻的整张波面直接缩短 $x$ 坐标，就选错了用于组成新波面的事件集合。

相位的时间与空间系数可以组成四维波矢。即使不用四维术语，也可以检验其零范数关系：

$$
\begin{aligned}
\left(\frac{\omega'}c\right)^2-k_x'^2
&=\gamma^2\left[
\left(\frac{\omega}{c}-\beta k_x\right)^2
-\left(k_x-\beta\frac{\omega}{c}\right)^2
\right]\\
&=\gamma^2(1-\beta^2)
\left[\left(\frac{\omega}c\right)^2-k_x^2\right]\\
&=\left(\frac{\omega}c\right)^2-k_x^2.
\end{aligned}
$$

又有 $k_y'=k_y,k_z'=0$，而旧系 $\omega^2/c^2=k_x^2+k_y^2$，所以

$$
\boxed{\frac{\omega'^2}{c^2}=k_x'^2+k_y'^2}.
$$

于是新波面沿法线的移动速率为 $\omega'/|\boldsymbol k'|=c$。这从波面本身的运动再次验证了速度变换给出的光速，不依赖于斜率比较。

还可以用半角形式简化传播角的变换。对非退化角度，

$$
\begin{aligned}
\tan\frac{\theta'}2
&=\frac{\sin\theta'}{1+\cos\theta'}\\
&=\frac{\sin\theta}
{\gamma[(1-\beta\cos\theta)+(\cos\theta-\beta)]}\\
&=\frac{\sin\theta}
{\gamma(1-\beta)(1+\cos\theta)}\\
&=\boxed{
\sqrt{\frac{1+\beta}{1-\beta}}
\tan\frac{\theta}{2}}.
\end{aligned}
$$

在 $0<\theta<\pi$、$\beta>0$ 时，半角正切增大，传播角向远离 $+x'$ 的方向偏转，与正向追赶参考系中的速度分量变化一致。端点方向由正文的矢量式单独处理，不需要用无穷大半角正切硬代入。

## 七、易错点

- 将相位不变误解为电场振幅也不变。本题只利用相位标记同一事件，并未要求变换电场强度。
- 代入相位时使用正向变换却把新旧坐标位置写反。
- 只变换 $x$ 而保留 $t$，忽略相对同时性。
- $x'$ 系数中的负号处理错误，得到 $k_x'=\gamma(k_x+\omega u/c^2)$。
- 认为 $y'=y$ 就有 $c_y'=c_y$，忘记分母中的时间间隔改变。
- 将新频率取成旧频率，导致新波面移动速率与光线速度不一致。
- 只证明速度模为 $c$，却没有证明它与波面法线平行。
- 把二维截面交线称作整个波面，漏掉任意 $z'$ 的空间延伸。
- 用斜率乘积法时遗漏 $\sin\theta=0$ 或 $k_x'=0$ 的情况。
- 只用 $\arctan(c_y'/c_x')$ 判断方向，丢失第二象限信息。

## 八、课堂讲解建议

先让学生写出旧参考系中“同一时刻、同一相位”的平面方程，再提问新参考系中的“同一时刻”是否对应相同的一组事件。用这一问题引出必须同时变换 $x$ 与 $t$。

相位变换与速度变换可以分成两列板书，分别独立完成。直到得到新波矢和新速度后才进行比较，避免学生在中途把“应当垂直”当作已知条件代入，形成循环证明。

证明垂直时，先使用法向量和比例关系，再把斜率乘积作为普通角度下的补充检查。安排 $\cos\theta=\beta$ 这一例子，让学生发现矢量式在特殊方向仍然适用。

最后用 $\beta=3/5,\theta=60^\circ$ 的算例解释负的横向速度：不是光倒退或速度小于零，而是它在新坐标系中的 $x'$ 分量反向，整体速度仍为 $c$。

## 九、变式训练

变式一：在 $S'$ 中观测到光沿 $+y'$ 方向传播，频率为 $\omega'$。$S'$ 仍以速度 $u=\beta c$ 沿 $S$ 的 $+x$ 方向运动。求 $S$ 中光的方向、频率，并用事件速度变换反查。

解：沿 $+y'$ 传播意味着

$$
c_x'=0,\qquad c_y'=c.
$$

由正文方向公式，$c_x'=0$ 要求

$$
\cos\theta-\beta=0,
\qquad \cos\theta=\beta.
$$

因新系的 $y'$ 分量为正，旧系也应取正的 $\sin\theta$，故

$$
\sin\theta=\sqrt{1-\beta^2}=\frac1\gamma.
$$

因此旧系传播方向单位向量为

$$
\boxed{\left(\beta,\frac1\gamma,0\right)}.
$$

频率关系为

$$
\begin{aligned}
\omega'
&=\gamma\omega(1-\beta\cos\theta)\\
&=\gamma\omega(1-\beta^2)\\
&=\frac{\omega}{\gamma}.
\end{aligned}
$$

所以 $\boxed{\omega=\gamma\omega'}$。

再从一对光线事件独立核对。新系中取 $\mathrm dx'=0$、$\mathrm dy'=c\,\mathrm dt'$。对逆变换微分：

$$
\begin{aligned}
\mathrm dx&=\gamma u\,\mathrm dt',\\
\mathrm dt&=\gamma\,\mathrm dt',\\
\mathrm dy&=c\,\mathrm dt'.
\end{aligned}
$$

相除得到旧系速度

$$
c_x=u=\beta c,\qquad
c_y=\frac c\gamma.
$$

两分量的平方和为 $c^2[\beta^2+(1-\beta^2)]=c^2$，与前述方向一致。注意旧系中这束光一般不垂直于 $x$ 轴；“横向”这一描述必须附带参考系，不能在两个参考系中不加区别地同时使用。

变式二：参考系相对速度 $\beta=0.6$，光在原系分别沿 $+x$ 和 $-x$ 传播。求新系频率与方向。

解：频率比为 $\gamma(1-\beta\cos\theta)$，$\gamma=5/4$。前向 $\cos\theta=1$ 给 $\omega'/\omega=1/2$，后向 $\cos\theta=-1$ 给 $\omega'/\omega=2$。方向式

$$
\cos\theta'=\frac{\cos\theta-\beta}{1-\beta\cos\theta}
$$

分别为 $+1,-1$，方向没有翻转。纵向红移与蓝移互为倒数，可用来核对洛伦兹因子。

变式三：取 $\beta=0.6$，原系光沿 $+y$ 方向。求新系方向分量和频率，并检查单位方向矢量。

解：原系 $\cos\theta=0,\sin\theta=1$。代入方向与频率公式，得

$$
\boldsymbol n'=(-0.6,0.8,0),\qquad \omega'=1.25\omega.
$$

平方和 $0.36+0.64=1$，故光仍以 $c$ 沿单位法线传播。原系横向光在新系中已有负 $x'$ 分量，不能把“横向”条件同时放在两个参考系。

变式四：取 $\beta=0.6$，寻找使两系频率完全相同的原系入射角，并求新系角度。

解：令 $\gamma(1-\beta\cos\theta)=1$，有 $\cos\theta=(1-1/\gamma)/\beta=1/3$，即 $\theta\approx70.5288^\circ$。方向变换给

$$
\cos\theta'=\frac{1/3-0.6}{1-0.6/3}=-\frac13,
\qquad \theta'\approx109.4712^\circ.
$$

频率不变没有要求方向不变；相位变换中的空间系数仍随参考系改变。
