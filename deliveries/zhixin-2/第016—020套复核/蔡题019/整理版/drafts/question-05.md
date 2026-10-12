# 第5题

<!-- question-start -->

点电荷$q$固定在惯性系$S$的原点。另一惯性系$S'$相对$S$以速度$u$沿$S$的$X$轴正方向运动，两系坐标轴平行，并在原点重合事件处取$t=t'=0$。设$|u|<c$，其中$c$为真空光速。在$S'$系的$t'=0$时刻，求下列位置的电场强度：

（1）$A(0,y)$；（2）$B(x,0)$。

这里$x,y$是$S'$系中的坐标，场点均不与电荷重合。电荷量$q$及非零坐标可带正负号；若只讨论正半轴，可再取$x>0,y>0$。

<!-- question-end -->

## 一、题型定位

本题是静电场在另一惯性系中的表示问题。电荷在$S$系中静止，已知库仑场；在$S'$系中电荷匀速运动，电场发生方向相关的变化，还通常伴随磁场。解题包含两个不同的变换：先确定同一测量事件在两系中的坐标，再变换该事件处的场分量。只做其中一个，不能得到正确答案。

两问分别选择垂直于相对运动的方向和沿相对运动的方向，利用轴线上电场只有一个非零分量，把一般变换化成可逐项检查的结果。横向场的增强与纵向场的减弱并不矛盾，因为对应事件到静止电荷的距离也不同。

## 二、知识点

设$\beta=u/c$、$\gamma=(1-\beta^2)^{-1/2}$、$k=1/(4\pi\varepsilon_0)$，其中$\varepsilon_0$是真空介电常数。$\gamma$无量纲，$kq/r^2$的单位为$\mathrm{N/C}$，等于$\mathrm{V/m}$。使用国际单位制时，磁场变换中出现$u/c^2$，不能把其他单位制的系数直接抄入。

对同一时空事件，标准洛伦兹变换为$x=\gamma(X-ut)$、$t'=\gamma(t-uX/c^2)$，横向坐标不变。这里大写$X,Y,Z$属于$S$，小写$x,y,z$属于$S'$。时间坐标必须与空间坐标一并转换；两系的同时面一般不同。

在静止电荷系中，$\boldsymbol E=kq\boldsymbol R/R^3$、$\boldsymbol B=\boldsymbol0$。向沿$+X$运动的$S'$变换时，平行分量$E'_x=E_X$，垂直分量在本题中为$E'_y=\gamma E_Y$、$E'_z=\gamma E_Z$。这些等式比较的是同一事件，不是两个任意选定的同名空间点。

电场是矢量。$q/y^2$只在已经说明$y>0$时才能代表带符号的$y$分量；任意非零$y$应写成$qy/|y|^3$。同理，纵向分量应保留$x/|x|^3$，不以场强大小代替方向。

## 三、物理图像

在$S'$系的$t'=0$同时面上，运动电荷恰经过原点。$A$在横轴之外的$y$轴上，$B$在$x$轴上。图5-1以$q>0,x>0,y>0$示意方向；图中两侧是相同测量事件的空间坐标表示，左侧不是所有点都在同一个$S$时刻拍摄的快照。

图5-2进一步展示为什么$B$的事件在$S$系中不满足$t=0$。$t'=0$是一条倾斜的同时线，$B$在该线上；$A$因为$X=0$而恰有$t=0$。静止电荷的场不随$t$改变，因此这个时间差不会妨碍使用库仑场，但它必须先被正确识别。

图5-3比较相同$S'$距离处、不同方向的电场大小。它画的是场强相对库仑值的比值，不是电荷密度图，也不是把静电场简单做几何压缩后的图。角度$\theta$的定义及比值将直接用于两轴结果的复核。

## 四、解题入口

先写逆洛伦兹变换，把题给的$(x,y,t'=0)$转换成$(X,Y,t)$。第一问得到$(0,y,0)$，第二问得到$(\gamma x,0,\gamma ux/c^2)$。随后各自计算库仑场的非零分量，最后分别使用垂直或平行场变换。

纵向场不变，准确含义是$E'_x=E_X$；右边必须在$X=\gamma x$处计算。它绝不意味着$E'_x=kq/x^2$。把这条区别写清后，两问的系数便有明确来源，不需要依靠记忆“横向乘什么、纵向除什么”。

## 五、解析

（1）建立两系坐标约定，确定所求同时面。

记$S$中事件坐标为$(X,Y,Z,t)$，$S'$中为$(x,y,z,t')$。标准变换与逆变换分别为

$$
\begin{aligned}
x&=\gamma(X-ut),& t'&=\gamma\left(t-\frac{uX}{c^2}\right),\\
y&=Y,&z&=Z,\\
X&=\gamma(x+ut'),&t&=\gamma\left(t'+\frac{ux}{c^2}\right),\\
Y&=y,&Z&=z.
\end{aligned}
$$

这里$S'$的原点满足$x=0$，故在$S$中有$X=ut$，确实沿$+X$运动，符号约定与题意一致。原点重合只规定两系的一个共同事件为零时刻，不要求每个空间位置都同时满足$t=t'=0$。按题意取所求事件$t'=0$，逆变换成为

$$
X=\gamma x,\qquad Y=y,\qquad Z=z,\qquad
t=\gamma\frac{ux}{c^2}.
$$

由此可以逐点查明测量事件，而不是用非相对论关系$X=x+ut$代替。

（2）沿电荷世界线核对$S'$中电荷的位置与运动方向。

电荷在$S$中始终满足$X=Y=Z=0$。代入正变换得$x_q=-\gamma ut$、$t'_q=\gamma t$，消去$t$，于是

$$
x_q(t')=-ut',\qquad y_q=z_q=0.
$$

所以$S'$中电荷的速度为$-u\boldsymbol e'_x$，在$t'=0$处于原点。不要把$S'$相对$S$的速度$+u$，误当成电荷在$S'$中的速度。图5-1分别标出场点坐标与这一运动方向，以$u=0.60c$、$\gamma=1.25$示意距离和场箭头的相对比例：两侧对应同一$B$事件，因此纵向箭头等长；横向箭头则增强$1.25$倍。这里只画正电荷及正半轴方向，负号情况用后续矢量公式处理。

![图5-1 相同测量事件的空间坐标与两轴电场方向。](../figures/geometry-05.png){width=70%}

（3）写出静止电荷的库仑场，明确距离的所属坐标系。

在$S$系中电荷静止，令$R=\sqrt{X^2+Y^2+Z^2}$，则

$$
\begin{aligned}
\boldsymbol E(X,Y,Z,t)&=kq\frac{X\boldsymbol e_X+Y\boldsymbol e_Y+Z\boldsymbol e_Z}{(X^2+Y^2+Z^2)^{3/2}},\\
\boldsymbol B(X,Y,Z,t)&=\boldsymbol0.
\end{aligned}
$$

该场不随$t$变化。即使某一测量事件对应$t\ne0$，只要空间位置转换正确，仍可在该时刻使用相同的库仑表达式。分母是$S$系中的$R^3$，不能在变换空间坐标之前就把它换成$S'$的距离。

（4）列出同一事件的电磁场变换，并化成本题所需形式。

沿$X$轴的标准变换在国际单位制中为

$$
\begin{aligned}
E'_x&=E_X, &B'_x&=B_X,\\
E'_y&=\gamma(E_Y-uB_Z), &B'_y&=\gamma\left(B_Y+\frac{uE_Z}{c^2}\right),\\
E'_z&=\gamma(E_Z+uB_Y), &B'_z&=\gamma\left(B_Z-\frac{uE_Y}{c^2}\right).
\end{aligned}
$$

因为原系$\boldsymbol B=\boldsymbol0$，电场式分别简化为$E'_x=E_X$、$E'_y=\gamma E_Y$、$E'_z=\gamma E_Z$。磁场则为$B'_x=0$、$B'_y=\gamma uE_Z/c^2$、$B'_z=-\gamma uE_Y/c^2$。原系磁场为零，不代表变换后的磁场也为零。

这些变换反映电磁场作为整体在不同惯性系中的表示。若暂不使用一般磁场公式，核心两问仍只需三个电场式；磁场式在下面用于检查方向和相对论一致性。

（5）求第一问：先转换$A$事件，再计算横向电场。

$A$的$S'$坐标是$x=0,y\ne0,z=0,t'=0$。把每个坐标代入逆变换，得到

$$
X=\gamma(0+u\times0)=0,\quad Y=y,\quad Z=0,\quad
t=\gamma\left(0+\frac{u\times0}{c^2}\right)=0.
$$

因此$R_A=|y|$，库仑场为$E_X=E_Z=0$、$E_Y=kqy/|y|^3$。这个非零分量垂直于运动方向，应使用$E'_y=\gamma E_Y$，于是

$$
\boxed{\boldsymbol E'_A
=\gamma kq\frac{y}{|y|^3}\boldsymbol e'_y}.
$$

若$y>0$，可写成$\boldsymbol E'_A=\gamma kq\boldsymbol e'_y/y^2$；若$y<0$而$q>0$，场沿负$y$方向。两种写法的大小相同，方向相反。若$q<0$，所有电场方向再反向。场强大小为$|\boldsymbol E'_A|=\gamma k|q|/y^2$，不能把大小公式里的$|q|$与带方向的分量公式混用。

同时由场变换得到

$$
\boldsymbol B'_A=-\frac{u}{c^2}E'_y\boldsymbol e'_z.
$$

对$u>0,q>0,y>0$，电荷沿$-x$运动，$\boldsymbol B'$指向$-z$。这一负号与$\boldsymbol v_q\times\boldsymbol E'/c^2$一致；它不是第一问所求电场的额外因子。

（6）用同时线理解第二问事件的时间与位置。

在$S'$系同时面$t'=0$上，正变换的时间式给出$t=uX/c^2$。图5-2采用纵轴$ct$、横轴$X$，故同时线的斜率为$\beta$。$B$位于$X=\gamma x$处，其纵坐标为$ct_B=\gamma\beta x$。图中$A$的$X=0$投影在原点；它仍具有横向坐标$Y=y$，不是说$A$与电荷重合。

![图5-2 测量事件的同时线与洛伦兹坐标关系。](../figures/simultaneity-05.png){width=52%}

由图中的$X_B=\gamma x$和$ct_B=\beta X_B$恢复

$$
X_B=\gamma x,\qquad t_B=\frac{\beta X_B}{c}
=\gamma\frac{ux}{c^2}.
$$

当$u\ne0,x\ne0$时，$B$事件在$S$中的时间不为零。不能为了让两边都“此时”，再把$t$强行设成零；那样选择的是另一个事件。

（7）求第二问：在正确的纵向距离处计算库仑场。

$B$事件在$S$中有$(X,Y,Z)=(\gamma x,0,0)$，到电荷的距离为$R_B=|\gamma x|=\gamma|x|$，因为$\gamma>0$。所以

$$
\begin{aligned}
E_X(B)&=kq\frac{\gamma x}{(\gamma^2x^2)^{3/2}}\\
&=kq\frac{\gamma x}{\gamma^3|x|^3}
=\frac{kq}{\gamma^2}\frac{x}{|x|^3},\\
E_Y(B)&=E_Z(B)=0.
\end{aligned}
$$

此处是正数的分数次幂运算：$(\gamma^2x^2)^{3/2}=\gamma^3|x|^3$，不能写成$\gamma^3x^3$后无条件消去负号。纵向场变换不另乘$\gamma$，故

$$
\boxed{\boldsymbol E'_B
=\frac{kq}{\gamma^2}\frac{x}{|x|^3}\boldsymbol e'_x
=(1-\beta^2)kq\frac{x}{|x|^3}\boldsymbol e'_x}.
$$

若$x>0$，结果就是$kq\boldsymbol e'_x/(\gamma^2x^2)$。此时各横向分量均为零，磁场变换也给出$\boldsymbol B'_B=\boldsymbol0$。运动电荷会产生磁场并不意味着每个空间点的磁场都非零；在运动轴上，速度与电场平行或反平行，叉积恰为零。

（8）区分“场分量不变”与“相同数值坐标处场强相同”。

第二问先把距离从$x$变成$\gamma|x|$，库仑场因此带来$1/\gamma^2$；随后平行分量的变换系数是$1$。第一问距离始终为$|y|$，但垂直场变换带来$\gamma$。将两个环节分别写出：

$$
\begin{aligned}
A:&\quad |y|\ \longrightarrow\ |y|,
\qquad E_Y\ \longrightarrow\ \gamma E_Y,\\
B:&\quad |x|\ \longrightarrow\ \gamma|x|,
\qquad E_X\ \longrightarrow\ E_X.
\end{aligned}
$$

若只背“纵向不变”，漏掉第一环节就会错误得到$kq/x^2$。若把运动方向误判为电荷的$+u$，则磁场方向错误；电场中的$\gamma$只含$u^2$，不能靠两个电场大小察觉这一方向错误。

（9）求一般位置的场，代回两轴作独立的代数检查。

在$t'=0$时，任意点$(x,y,z)$对应$S$中的$(\gamma x,y,z)$。记$D=\gamma^2x^2+y^2+z^2>0$。先计算库仑分量，再变换：

$$
\begin{aligned}
E_X&=\frac{kq\gamma x}{D^{3/2}},
&E_Y&=\frac{kqy}{D^{3/2}},
&E_Z&=\frac{kqz}{D^{3/2}},\\
E'_x&=\frac{kq\gamma x}{D^{3/2}},
&E'_y&=\frac{kq\gamma y}{D^{3/2}},
&E'_z&=\frac{kq\gamma z}{D^{3/2}}.
\end{aligned}
$$

因此三个分量具有相同前因子，可合并为

$$
\boldsymbol E'(x,y,z,0)=
\frac{kq\gamma(x\boldsymbol e'_x+y\boldsymbol e'_y+z\boldsymbol e'_z)}{(\gamma^2x^2+y^2+z^2)^{3/2}}.
$$

这个式子的纵向分子含$\gamma$来自坐标$X=\gamma x$，不是说$E'_x=\gamma E_X$。令$x=z=0$得到第一问，令$y=z=0$得到第二问，正负方向都自动保留。在这个瞬间，电场与相对于电荷当前位置的位矢平行，但大小随角度变化。

（10）把一般式改成角度形式，检查图5-3与两轴结论。

令$r'=\sqrt{x^2+y^2+z^2}$，取$\cos\theta=x/r'$、$\sin^2\theta=(y^2+z^2)/r'^2$。因为$\gamma^2-1=\gamma^2\beta^2$，分母中的距离因子逐步化为

$$
\begin{aligned}
D&=r'^2(\gamma^2\cos^2\theta+\sin^2\theta)\\
&=\gamma^2r'^2\bigl(\cos^2\theta+(1-\beta^2)\sin^2\theta\bigr)\\
&=\gamma^2r'^2(1-\beta^2\sin^2\theta).
\end{aligned}
$$

所以

$$
\boldsymbol E'=\frac{kq}{r'^2}
\frac{1-\beta^2}{(1-\beta^2\sin^2\theta)^{3/2}}\boldsymbol e'_r.
$$

![图5-3 同一距离处电场大小的方向依赖。](../figures/angular-05.png){width=47%}

图中纵坐标为$f(\theta)=|\boldsymbol E'|/(k|q|/r'^2)$。在纵轴方向$\theta=0,\pi$，$f=1-\beta^2=1/\gamma^2$；在横向平面$\theta=\pi/2$，

$$
f\left(\frac\pi2\right)
=\frac{1-\beta^2}{(1-\beta^2)^{3/2}}
=\frac1{\sqrt{1-\beta^2}}=\gamma.
$$

于是图的端点与顶点分别对应$B$和$A$。角度依赖由同一事件的坐标变换和场变换共同给出。

（11）检查单位、低速极限与磁场不变量。

两轴结果分别为$kq/y^2$与$kq/x^2$乘无量纲系数，单位均正确。$u\to0$时$\gamma\to1$，同时线趋于$t=0$，两个结果都恢复库仑场。对$|\beta|\ll1$，利用二项式展开

$$
\gamma=1+\frac{\beta^2}{2}+O(\beta^4),\qquad
\frac1{\gamma^2}=1-\beta^2.
$$

横向增强从二阶开始，纵向减弱也从二阶开始；电场大小不因$u$反向而改变，但磁场随$u$反向。不能凭经验补入一个与$\beta$成正比的电场修正。

以$A$为例，$B'_z=-uE'_y/c^2$，所以

$$
E_A'^2-c^2B_A'^2
=E_A'^2(1-\beta^2)
=\gamma^2E_Y^2(1-\beta^2)=E_Y^2.
$$

它等于$S$中该事件的$E^2-c^2B^2$。对$B$则$B'=0$、$E'_x=E_X$，不变量也直接相等。这里比较的静止系纵向场仍是在$X=\gamma x$处的场，不是$X=x$处的场。

（12）代入一组数值，复核每一个系数。

取$q=1.0\times10^{-9}\,\mathrm C$、$u=0.60c$，并取$x=y=0.20\,\mathrm m$的两个轴上点。使用$k=8.98755\times10^9\,\mathrm{N\,m^2/C^2}$，先算

$$
\gamma=\frac1{\sqrt{1-0.60^2}}=1.25,\qquad
\frac{kq}{(0.20)^2}=224.689\,\mathrm{V/m}.
$$

第一问直接乘$1.25$，得到$E'_y=280.861\,\mathrm{V/m}$。第二问先算$X_B=1.25\times0.20=0.25\,\mathrm m$，再算$kq/(0.25)^2=143.801\,\mathrm{V/m}$；与$0.64\times224.689$相等。使用$c=2.99792458\times10^8\,\mathrm{m/s}$，第一问的磁场为$B'_z=-5.62111\times10^{-7}\,\mathrm T$，第二问为零。这个算例分别检查距离、分量变换与磁场方向，未用大小检查替代符号检查。

<!-- KEEP_STUDENT_START -->

（13）写出适用范围，避免把当前位矢误解为瞬时传递。

上述结论适用于电荷始终匀速运动、两个惯性系之间的标准洛伦兹变换，且场点不位于电荷本身。在$S'$的一般时刻，电荷位置为$-ut'$，令$d=x+ut'$，则相对于电荷当前位置的位矢为$(d,y,z)$，相同推导给出

$$
\boldsymbol E'(x,y,z,t')=
\frac{kq\gamma(d\boldsymbol e'_x+y\boldsymbol e'_y+z\boldsymbol e'_z)}{(\gamma^2d^2+y^2+z^2)^{3/2}},\qquad d=x+ut'.
$$

它是匀速运动迟滞场化简后的表示，不表示电磁作用可以瞬时传播。电荷若加速，不能把这一式的$u$直接换成时变速度，遗漏加速场。$|u|\to c$也只能作为极限检查，不能把光速运动的参考系当作可建立的惯性系。最后两问的答案均以$t'=0$为取值条件，不额外把$S$中所有空间点设为$t=0$。

<!-- KEEP_STUDENT_END -->

## 六、关键洞察

两问可以用一个固定流程统一：测量事件的$S'$坐标，转换成$S$坐标，计算库仑场，变换同一事件的场，最后报告$S'$分量。空间坐标变换与场分量变换不是两个可以任选其一的解法；它们是同一次计算中必须依次完成的环节。

还可从四维力验证本题的电场变换，而不只把它当作一组记忆公式。在$S'$中放置瞬时静止、足够小而不改变源场的试探电荷$Q$；它在$S$中速度为$u\boldsymbol e_X$。因为$S$中磁场为零，三维力为$\boldsymbol F=Q\boldsymbol E$。四维力定义为动量四矢量对固有时的导数，若三维速度为$\boldsymbol w$，其分量为$K^0=\gamma_w\boldsymbol F\cdot\boldsymbol w/c$、$\boldsymbol K=\gamma_w\boldsymbol F$。本情形$\boldsymbol w=u\boldsymbol e_X$，故

$$
K^0=\gamma\beta F_X,\qquad
K^X=\gamma F_X,\qquad K^Y=\gamma F_Y,\qquad K^Z=\gamma F_Z.
$$

沿$X$轴做洛伦兹变换，逐项得到

$$
\begin{aligned}
K'^x&=\gamma(K^X-\beta K^0)
=\gamma^2(1-\beta^2)F_X=F_X,\\
K'^y&=K^Y=\gamma F_Y,\qquad K'^z=K^Z=\gamma F_Z,\\
K'^0&=\gamma(K^0-\beta K^X)=0.
\end{aligned}
$$

在试探电荷瞬时静止的$S'$中，它的洛伦兹因子为$1$，故$\boldsymbol K'=\boldsymbol F'=Q\boldsymbol E'$。电荷量$Q$不随惯性系改变，两侧约去$Q$，就得到$E'_x=E_X$、$E'_y=\gamma E_Y$、$E'_z=\gamma E_Z$。$K'^0=0$也与瞬时静止时功率为零一致。该推导使用相对论四维力，而非错误地假设三维力在各系中相同；它验证的是本题$\boldsymbol B=0$的特殊情形，不取代一般电磁场变换的全部分量。

横向增强不改变包围电荷的总通量。以$S'$中电荷当前位置为球心，取半径$r'$的球面；按角度表达式，径向电场乘面积元为

$$
\Phi_E=2\pi kq(1-\beta^2)
\int_0^\pi\frac{\sin\theta\,\mathrm d\theta}
{(1-\beta^2\sin^2\theta)^{3/2}}.
$$

令$\mu=\cos\theta$，则$\sin\theta\,\mathrm d\theta=-\mathrm d\mu$，上下限由$1$变为$-1$。记$a=1-\beta^2>0$、$b=\beta^2$，有$a+b=1$。利用求导检查原函数：

$$
\begin{aligned}
\frac{\mathrm d}{\mathrm d\mu}
\left[\frac{\mu}{a\sqrt{a+b\mu^2}}\right]
&=\frac1{a\sqrt{a+b\mu^2}}
-\frac{b\mu^2}{a(a+b\mu^2)^{3/2}}\\
&=\frac{a+b\mu^2-b\mu^2}{a(a+b\mu^2)^{3/2}}
=\frac1{(a+b\mu^2)^{3/2}}.
\end{aligned}
$$

因此

$$
\begin{aligned}
\Phi_E&=2\pi kq\,a
\left[\frac{\mu}{a\sqrt{a+b\mu^2}}\right]_{-1}^{1}\\
&=2\pi kq\,a\frac2a
=4\pi kq=\frac q{\varepsilon_0}.
\end{aligned}
$$

这项积分同时检查角度因子的分子、分母幂次和总归一化。只检查两个轴上特殊值，不能排除一个在中间角度错误、却恰在两轴正确的表达式。

迟滞场提供另一条真正独立的数值路线。在$S'$中，令当前位置到场点的位矢为$\boldsymbol r=(d,y,z)$，源速度为$\boldsymbol v_q=-u\boldsymbol e'_x$。若发射与接收相隔$\tau>0$，迟滞源到场点的向量为$\boldsymbol R_{\mathrm{ret}}=\boldsymbol r+\boldsymbol v_q\tau$，必须满足光锥条件$c\tau=|\boldsymbol R_{\mathrm{ret}}|$。平方并展开后

$$
(c^2-u^2)\tau^2+2ud\tau-(d^2+y^2+z^2)=0.
$$

以正时间根确定发射事件，再令$\boldsymbol n=\boldsymbol R_{\mathrm{ret}}/R_{\mathrm{ret}}$、$\boldsymbol\beta_q=\boldsymbol v_q/c$。匀速电荷的速度场为

$$
\boldsymbol E'_{\mathrm{ret}}=
\frac{kq(1-\beta^2)(\boldsymbol n-\boldsymbol\beta_q)}
{(1-\boldsymbol n\cdot\boldsymbol\beta_q)^3R_{\mathrm{ret}}^2}.
$$

数值程序不是把主解析的闭式代回主解析，而是直接求光锥的正根后计算这个迟滞场。两路线在轴上、非轴上、负电荷、反向速度及非零接收时间的20组情形一致；同时检查$\boldsymbol B'=\boldsymbol n\times\boldsymbol E'/c$与$\boldsymbol v_q\times\boldsymbol E'/c^2$相等。匀速情形可写成当前位矢，不会取消迟滞条件。

## 七、易错点

在全空间同时设$t=t'=0$。由$t'=\gamma(t-uX/c^2)$可见，除$uX=0$的特殊点外这不可能；两个零时刻约定共享的是原点重合事件。应先指定所求$S'$同时面，再转换每个场点事件。

把$X=\gamma x$误写成$X=x/\gamma$。所谓长度收缩比较的是特定同时性条件下两个端点的测量，不能直接取代单个时空事件的坐标变换。对$t'=0$必须使用逆变换并逐项代入。

由$E'_x=E_X$推出第二问与$kq/x^2$相同。平行场分量不变，但右侧的库仑场是在$X=\gamma x$处。遗漏这个距离变化会丢掉整个$1/\gamma^2$。

横向场把两个$\gamma$相乘。本题$A$的横向距离不变，只有场分量变换带来一个$\gamma$；不能再给$y$套一个长度收缩因子。

把运动速度写成$+u$。源在$S'$中沿$-x$运动，电场大小含$u^2$可能暂时看不出错误，磁场方向立即出现反号。应从源的世界线求$x_q=-ut'$，再检查叉积。

用$y^2$或$x^2$写矢量答案却不说明坐标正负。负半轴和负电荷必须通过$qy/|y|^3$、$qx/|x|^3$或明确的单位方向保留；大小与带符号分量不能混用。

把不同单位制的磁场公式混写。本题用国际单位制，$uE/c^2$有磁感应强度单位；若写成$uE/c$而没有改变场量定义，量纲不正确。欧姆、光速、介电常数等符号应各自在正确数学环境中使用。

把匀速场改写成当前距离，就认为电磁作用瞬时传播；或者对加速电荷直接代入瞬时$u$。迟滞场已包含源的历史信息，匀速运动才允许上述化简；加速场还有不能省略的贡献。

## 八、课堂讲解建议

教师先让学生画两个坐标系，只标“谁静止、谁沿哪边运动”。课堂应先从电荷世界线得到$S'$中的$-u$，再引入场变换，避免学生把坐标系速度与源速度混在一起。

板书采用四栏：所求事件的$S'$坐标、对应$S$事件、库仑场、变换后分量。教师先填$A$，再让学生填写$B$；最值得停顿的是$B$的时间不为零，以及距离为$\gamma|x|$。两个中间结果不应被一句“考虑相对论效应”略过。

课堂结合图5-2提问：“哪一个系的同时线经过两个测量事件？”让学生由斜率写出$ct=\beta X$，再回到时间变换。图5-3用于核查最终答案，不作为未经推导的起点。教师可让学生说明图上的横向峰值为什么是$\gamma$、两端为什么是$1/\gamma^2$。

核心两问完成后，课堂再用负半轴、反向速度检验符号，并用给定数值检验距离。四维力与通量积分适合在已有相对论基础后展开；教师仍应保留完整计算，使备课时能追溯系数和单位的来源。

## 九、变式训练

变式一：$q=1.0\,\mathrm{nC}$，$u=0.60c$。在$S'$的$t'=0$时刻，求$P(0.12\,\mathrm m,0.16\,\mathrm m)$处的电场和磁场，并与相同距离的库仑场比较。

$\gamma=1.25$，该事件在$S$中对应$X=1.25\times0.12=0.15\,\mathrm m$、$Y=0.16\,\mathrm m$。所需距离平方为$D=0.15^2+0.16^2=0.0481\,\mathrm{m^2}$，而$S'$距离为$r'=\sqrt{0.12^2+0.16^2}=0.20\,\mathrm m$。依一般式分别计算

$$
\begin{aligned}
E'_x&=\frac{(8.98755)(1.25)(0.12)}{(0.0481)^{3/2}}
\simeq127.795\,\mathrm{V/m},\\
E'_y&=\frac{(8.98755)(1.25)(0.16)}{(0.0481)^{3/2}}
\simeq170.394\,\mathrm{V/m},\\
E'_z&=0.
\end{aligned}
$$

电场与$(0.12,0.16)$平行，因为$E'_y/E'_x=4/3$；大小为$\sqrt{127.795^2+170.394^2}\simeq212.992\,\mathrm{V/m}$。同距离库仑场为$224.689\,\mathrm{V/m}$，所以这个斜向点的场略减弱，不能把“有横向坐标”误解成“必增强”。磁场为$B'_z=-uE'_y/c^2\simeq-3.41024\times10^{-7}\,\mathrm T$，其他分量为零。角度$\sin\theta=0.16/0.20=0.8$，代入图5-3对应的角度表达式，也得到相同大小。

变式二：改取$q=-1.0\,\mathrm{nC}$、$u=-0.60c$，求$A(0,-0.20\,\mathrm m)$与$B(-0.20\,\mathrm m,0)$的带方向电场和磁场。

$\gamma$仍为$1.25$。两个电场分量中的$qy$与$qx$都为正，因此

$$
\boldsymbol E'_A=280.861\boldsymbol e'_y\,\mathrm{V/m},\qquad
\boldsymbol E'_B=143.801\boldsymbol e'_x\,\mathrm{V/m}.
$$

这与负电荷的场指向电荷相符：场点位于负半轴，电荷在原点。此时源在$S'$中的速度为$-u=+0.60c$，故$\boldsymbol B'_A=+5.62111\times10^{-7}\boldsymbol e'_z\,\mathrm T$，$\boldsymbol B'_B=\boldsymbol0$。对$B$事件，$t_B=\gamma ux/c^2>0$，因为$u,x$都为负；时间变换的符号也须单独核对，不能由“负速度”直接判断时间负号。

<!-- KEEP_TOGETHER_START -->

变式三：在电荷经过原点的$S'$时刻，分别测量距原点同为$r'$的正$y$轴点（垂直运动方向）与正$x$轴点（平行运动方向）的场强大小，发现前者与后者的比值为$8$。求速度大小及洛伦兹因子；若$|q|=2.0\,\mathrm{nC}$、$r'=0.10\,\mathrm m$，计算两个场强大小。

因为两个距离相同，电荷量及距离因子相消，比值为

$$
\mathcal R=\frac{\gamma k|q|/r'^2}{k|q|/(\gamma^2r'^2)}=\gamma^3.
$$

由$\mathcal R=8$得$\gamma=\sqrt[3]{8}=2$，继而

$$
|\beta|=\sqrt{1-\gamma^{-2}}=\frac{\sqrt3}{2},\qquad
|u|=\frac{\sqrt3}{2}c.
$$

大小比不能区分$u$的正负，须另测磁场方向或源运动方向。场强计算保留未舍入的中间值，最后统一取小数：

$$
\begin{aligned}
E_0&=\frac{k|q|}{r'^2}
\simeq1797.51036\,\mathrm{V/m},\\
E'_{\perp}&=2E_0\simeq3595.021\,\mathrm{V/m},\\
E'_{\parallel}&=E_0/4\simeq449.378\,\mathrm{V/m}.
\end{aligned}
$$

比值仍为$8$。一般测量比值必须满足$\mathcal R\geq1$；若小于$1$，不能强行开根求一个虚速度，应检查距离是否相同、方向是否正确或模型是否适用。

<!-- KEEP_TOGETHER_END -->

变式四：在$S'$的$t'=0$同时面，取以电荷当前位置为球心、半径为$r$的球面。电场沿运动轴方向减弱、横向增强，球面的总电通量是否仍为$q/\varepsilon_0$？用积分证明。

令$\theta$为场点位置矢量与$x$轴的夹角。主问的一般场给出径向分量

$$
E'_r=\frac{kq(1-\beta^2)}{r^2(1-\beta^2\sin^2\theta)^{3/2}},
\qquad \beta=u/c,\quad k=\frac1{4\pi\varepsilon_0}.
$$

球面面积元为$r^2\sin\theta\,d\theta\,d\phi$，故

$$
\mathcal F=2\pi kq(1-\beta^2)
\int_0^\pi\frac{\sin\theta\,d\theta}
{(1-\beta^2\sin^2\theta)^{3/2}}.
$$

作$t=\cos\theta$，积分变为$\int_{-1}^1(1-\beta^2+\beta^2t^2)^{-3/2}dt$。利用

$$
\frac{d}{dt}\frac{t}{\sqrt{1-\beta^2+\beta^2t^2}}
=\frac{1-\beta^2}{(1-\beta^2+\beta^2t^2)^{3/2}},
$$

积分值为$2/(1-\beta^2)$，从而$\boxed{\mathcal F=4\pi kq=q/\varepsilon_0}$。沿轴和横向的变化在角度积分中正好补偿。$\beta\to0$时恢复均匀库仑场的通量；任意$|\beta|<1$都满足同一高斯定律。

球面必须取在一个明确的同时面上，半径也在该系中定义。电荷在此系运动不会改变总电荷；磁场的存在并不在电通量积分中另加一项。该积分验证场的整体约束，不能把总通量不变误解成各方向场强都不变。

<!-- question-complete -->
