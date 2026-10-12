# 第1题

<!-- question-start -->

一个质量均匀分布的椭圆薄片，半长轴为$a$，半短轴为$b=\sqrt6\,a/3$，竖立在水平桌面上后由静止释放。开始时长轴竖直；薄片与桌面间无摩擦。设重力加速度为$g$。

（1）当长轴相对初始竖直方向转过$\theta=\pi/3$时，求上方焦点$F_1$的速度和椭圆薄片的角速度。

（2）求同一时刻$F_1$的加速度和椭圆薄片的角加速度。

（3）将接触条件改为纯滚动，重新求前两问中的各量。

约定向右倾倒，$x$轴向右、$y$轴向上，$\theta$沿顺时针增加；角速度和角加速度的标量均以顺时针为正。精确竖立、严格静止的理想状态是一个不稳定平衡，不会自行离开；题设通常所指的倾倒过程，应按向右无初速微小偏角释放的$\theta_0\to0^+$极限理解。严格不加扰动时不存在到达$\pi/3$的时刻。以下同时说明这个适用条件，不凭空给予初始动能。

![图1-1 椭圆薄片的初始竖立位置与向右倾倒位置。](../figures/question-01.png){width=82%}

<!-- question-end -->

## 一、题型定位

图1-1给出初始位置与所求位置。本题是具有移动接触点的平面刚体动力学。椭圆并非圆盘，质心到桌面的高度随转角变化，质心的水平位置又取决于接触是否滑动。光滑接触和纯滚动的势能变化相同，但平动动能不同，因而角速度、焦点速度及加速度都不同。

第一层是几何：确定质心高度、接触点、焦点相对质心的向量和转动惯量。第二层是运动学：依据实际约束写质心速度，随后用刚体速度叠加求焦点速度。第三层是动力学：能量只直接确定速度，还需对运动方程求导或列力与力矩方程求角加速度；最后必须同时保留切向和法向加速度。

最敏感的区别在于“接触材料点”与“接触位置”。接触位置不断改变材料身份。纯滚动只要求当前接触材料点的速度为零，不要求它的加速度为零，更不意味着薄片绕一个固定地面点一直转动。

## 二、知识点

均匀椭圆薄片绕质心、垂直片面的转动惯量为$I_G=m(a^2+b^2)/4$。焦距参数$c=\sqrt{a^2-b^2}$，两个焦点分别位于质心沿长轴正、负方向距离$c$处。这里$m$仅用于列动力学方程，最后所求运动量均与$m$无关。

机械能守恒必须以整个薄片为研究对象。光滑面法向力作用处的竖直速度为零，不做功；纯滚动时静摩擦和法向力所作用的当前材料点瞬时静止，也不做功。因此两种接触都可用机械能守恒，却不能由此认为它们的动能表达式相同。

若刚体上固定材料点$F$相对质心的位置为$\boldsymbol r$，则

$$
\begin{aligned}
\boldsymbol v_F&=\boldsymbol v_G+\boldsymbol\Omega\times\boldsymbol r,\\
\boldsymbol a_F&=\boldsymbol a_G+\dot{\boldsymbol\Omega}\times\boldsymbol r
+\boldsymbol\Omega\times(\boldsymbol\Omega\times\boldsymbol r).
\end{aligned}
$$

本题$\boldsymbol\Omega=-\omega\boldsymbol e_z$，$\dot{\boldsymbol\Omega}=-\alpha\boldsymbol e_z$。最后一项为$-\omega^2\boldsymbol r$，不能漏掉或改成向外的项。对某一瞬间的接触材料点也可用同样公式，但不可把该点当作以后每一瞬间的同一接触点。

## 三、物理图像

设$G$为质心，当前接触点为$Q$，质心高度记$h(\theta)$。长轴向上单位向量和短轴向右单位向量分别为

$$
\boldsymbol e=(\sin\theta,\cos\theta),\qquad
\boldsymbol e_\perp=(\cos\theta,-\sin\theta).
$$

上焦点是相对薄片固定的$F_1=G+c\boldsymbol e$。它的$x$坐标会随转动改变，即使光滑接触时$G$的$x$坐标不变，$F_1$也不只做竖直运动。相反，纯滚动时$G$还向右平移，焦点的水平速度包含这项平动贡献。

在$\theta=\pi/3$处，图1-2中接触点位于质心竖直投影的左侧，$GQ$不是竖直半径。两焦点到接触点的距离分别为$4a/3$、$2a/3$；质心高度为$\sqrt3 a/2$，质心与接触点的水平距离为$a/6$。这些几何量分别进入力矩、平动速度、动能和焦点加速度，不能只用一个“等效半径”替代。

![图1-2 转角为六十度时的焦点、接触点与质心高度。](../figures/support-01.png){width=66%}

## 四、解题入口

先从椭圆最低点求$h(\theta)$，同时得到接触点相对质心的横坐标。随后将$\dot h=h'\omega$代入动能：光滑面没有质心水平动能，纯滚动则另有$\dot X=h\omega$。把两种动能写成$mD(\theta)\omega^2/2$，就能用统一的能量式求速度，但求导时必须保留$D'(\theta)$。

求焦点加速度宜用固定的地面直角坐标。先写$F_1$的坐标，再连续求导两次，能够逐项对应平动、切向和法向项。最后用接触力、质心力矩、曲率与量纲检验核对符号。把瞬时转动中心直接当固定铰链求角加速度，是本题最需要避免的入口。

## 五、解析

（1）明确质量分布并从面积积分求转动惯量。

薄片面内取长轴坐标$u=a r\cos\varphi$、短轴坐标$v=b r\sin\varphi$，$0\le r\le1$、$0\le\varphi<2\pi$。坐标变换的面积元为$\mathrm dS=ab r\,\mathrm dr\,\mathrm d\varphi$。均匀面密度为$m/(\pi ab)$，因此

$$
\begin{aligned}
I_G&=\int(u^2+v^2)\,\mathrm dm\\
&=\frac m\pi\int_0^1 r^3\,\mathrm dr
\int_0^{2\pi}(a^2\cos^2\varphi+b^2\sin^2\varphi)\,\mathrm d\varphi\\
&=\frac m\pi\cdot\frac14\cdot\pi(a^2+b^2)
=\frac m4(a^2+b^2)=\frac5{12}ma^2.
\end{aligned}
$$

这里利用了$\int_0^{2\pi}\cos^2\varphi\,\mathrm d\varphi=\int_0^{2\pi}\sin^2\varphi\,\mathrm d\varphi=\pi$。不能套用均匀椭圆细线框的惯量，二者的质量分布不同。记$j=I_G/m=5a^2/12$，并有$c=a/\sqrt3$。

（2）从旋转椭圆的最低点建立高度函数。

任一边界材料点相对$G$的坐标可写成

$$
\begin{aligned}
x_{ \mathrm{rel}}&=a\cos\varphi\sin\theta+b\sin\varphi\cos\theta,\\
y_{ \mathrm{rel}}&=a\cos\varphi\cos\theta-b\sin\varphi\sin\theta.
\end{aligned}
$$

第二式是形如$A\cos\varphi+B\sin\varphi$的线性组合，最小值为$-\sqrt{A^2+B^2}$。这是振幅合成，也可由柯西不等式并检查取等条件证明。桌面高度为零，故最低点相对质心的$y$坐标为$-h$，得到

$$
\boxed{h(\theta)=\sqrt{a^2\cos^2\theta+b^2\sin^2\theta}}.
$$

取到最低值时，$\cos\varphi=-a\cos\theta/h$、$\sin\varphi=b\sin\theta/h$。代入边界点的$x$坐标，得到

$$
\begin{aligned}
(Q-G)_x
&=-\frac{a^2\sin\theta\cos\theta}{h}
+\frac{b^2\sin\theta\cos\theta}{h}\\
&=\frac{(b^2-a^2)\sin\theta\cos\theta}{h}=h'(\theta),\\
\boldsymbol r_{Q/G}&=(h',-h).
\end{aligned}
$$

于是图1-2中的水平偏置为$x_0=-h'>0$。$h'$的单位仍是长度，因为转角采用无量纲弧度；它不是一段时间内的下降速度。

（3）保留二阶几何导数并代入目标转角。

记$\Delta=b^2-a^2=-a^2/3$。对$h$求导两次，使用商法则得到

$$
\begin{aligned}
h'&=\frac{\Delta\sin\theta\cos\theta}{h},\\
h''&=\frac{\Delta\cos2\theta}{h}
-\frac{\Delta^2\sin^2\theta\cos^2\theta}{h^3}
=\frac{\Delta\cos2\theta-(h')^2}{h}.
\end{aligned}
$$

在$\theta=\pi/3$处，$\sin\theta=\sqrt3/2$、$\cos\theta=1/2$、$\cos2\theta=-1/2$，所以

$$
\begin{aligned}
h^2&=\frac{a^2}4+\frac{2a^2}3\cdot\frac34=\frac34a^2,
\qquad h=\frac{\sqrt3}2a,\\
h'&=\frac{(-a^2/3)(\sqrt3/4)}{\sqrt3 a/2}=-\frac a6,\\
h''&=\frac{a^2/6-a^2/36}{\sqrt3 a/2}
=\frac{5a}{18\sqrt3},\\
h+h''&=\frac{\sqrt3}2a+\frac{5a}{18\sqrt3}
=\frac{16a}{9\sqrt3}.
\end{aligned}
$$

尤其$h''>0$；它反映高度随转角的下降速率正逐渐减小，但不单独决定质心的竖直加速度。实际加速度还包含$h'\alpha$。

（4）用焦点几何交叉核对接触位置。

图1-2中，水平切线的法线平分两个焦点连线在$Q$处形成的角。结合焦距$c=a/\sqrt3$和转角，可得到$\triangle F_2QF_1$在$F_2$处为直角，$\angle QF_1F_2=30^\circ$。因此$QF_1=2QF_2$。椭圆定义给出$QF_1+QF_2=2a$，故

$$
QF_1=\frac43a,\qquad QF_2=\frac23a.
$$

反过来也可直接检查：取$G=(0,\sqrt3 a/2)$、$Q=(-a/6,0)$，则$F_1=(a/2,2a/\sqrt3)$、$F_2=(-a/2,a/\sqrt3)$。分别计算平方距离得$|QF_1|^2=16a^2/9$、$|QF_2|^2=4a^2/9$；$(F_1-F_2)\cdot(Q-F_2)=0$，确实为上述直角三角形。

质心是焦点连线的中点。由三角形中线公式

$$
\begin{aligned}
GQ^2&=\frac{2(QF_1)^2+2(QF_2)^2-(F_1F_2)^2}{4}\\
&=\frac{2(16a^2/9)+2(4a^2/9)-4a^2/3}{4}
=\frac79a^2,\\
x_0^2&=GQ^2-h^2=\frac79a^2-\frac34a^2=\frac1{36}a^2.
\end{aligned}
$$

这里的$a/6$是水平力臂，不是$GQ$的长度；后者是$\sqrt7 a/3$。

（5）分别建立光滑接触和纯滚动的质心速度。

光滑面只有重力和竖直法向力，如图1-3左侧，薄片的水平合外力为零。初始水平动量为零，故$\dot X=0$，而$\dot h=h'\omega$，即

$$
\boldsymbol v_G^{\mathrm s}=(0,h'\omega).
$$

纯滚动时有静摩擦，如图1-3右侧，质心水平动量不守恒。用当前接触材料点的刚体速度公式计算

$$
\begin{aligned}
\boldsymbol v_Q
&=(\dot X,h'\omega)+(-\omega\boldsymbol e_z)\times(h',-h)\\
&=(\dot X-h\omega,0).
\end{aligned}
$$

无滑动要求$\boldsymbol v_Q=\boldsymbol0$，所以

$$
\boxed{\dot X=h\omega},\qquad
\boldsymbol v_G^{\mathrm r}=(h\omega,h'\omega).
$$

![图1-3 光滑接触与纯滚动时的法向力、重力和静摩擦力。](../figures/forces-01.png){width=87%}

图中力均作用于真实材料接触点$Q$或质心$G$。后续力矩的水平力臂使用$x_0=-h'$；摩擦力的力臂使用$h$。图中纯滚动摩擦向右是本题该时刻的计算结果，不是“滚动摩擦总与运动方向相反”的经验判断。

（6）用完整动能求光滑接触的角速度。

机械能守恒为$T+mg h=mg a$，其中$mg a$是微扰释放极限的初始能量。光滑面只有质心竖直平动动能和绕质心转动动能：

$$
T_{\mathrm s}=\frac m2(h')^2\omega^2+\frac{I_G}2\omega^2
=\frac m2D_{\mathrm s}\omega^2,
\qquad D_{\mathrm s}=j+(h')^2.
$$

在目标转角，$D_{\mathrm s}=5a^2/12+a^2/36=4a^2/9$，因此

$$
\begin{aligned}
\frac12\cdot\frac49a^2\omega_{\mathrm s}^2
&=g\left(a-\frac{\sqrt3}2a\right),\\
\omega_{\mathrm s}^2&=\frac94(2-\sqrt3)\frac ga,\\
\boxed{\omega_{\mathrm s}=\frac32\sqrt{(2-\sqrt3)\frac ga}}.
\end{aligned}
$$

正根对应向右顺时针倾倒。没有负初始动能，也没有把法向力作的虚功计入真实机械能。

（7）用坐标连续求导求光滑面焦点速度。

焦点坐标为$x_F=X+c\sin\theta$、$y_F=h+c\cos\theta$。连续求导一次得

$$
\begin{aligned}
v_{Fx}&=\dot X+c\cos\theta\,\omega,\\
v_{Fy}&=h'\omega-c\sin\theta\,\omega.
\end{aligned}
$$

光滑面$\dot X=0$，故在目标转角

$$
\begin{aligned}
v_{Fx}^{\mathrm s}&=\frac a{2\sqrt3}\cdot\frac32
\sqrt{(2-\sqrt3)\frac ga}
=\frac{\sqrt3}4\sqrt{(2-\sqrt3)ga},\\
v_{Fy}^{\mathrm s}&=\left(-\frac a6-\frac a2\right)\omega_{\mathrm s}
=-\sqrt{(2-\sqrt3)ga},\\
|\boldsymbol v_F^{\mathrm s}|&=\sqrt{\frac3{16}+1}\sqrt{(2-\sqrt3)ga}
=\frac{\sqrt{19}}4\sqrt{(2-\sqrt3)ga}.
\end{aligned}
$$

焦点向右下方运动。图1-4中的光滑面质心只向下，但焦点还有绕质心转动的水平速度，两者并不矛盾。

（8）用统一能量微分求角加速度，保留几何系数变化。

两种情况都可以写成$mD\omega^2/2=mg(a-h)$。对时间求导时，$D$是$\theta$的函数，故

$$
\begin{aligned}
\frac12mD'\dot\theta\,\omega^2+mD\omega\dot\omega
&=-mg h'\dot\theta,\\
\frac12D'\omega^3+D\omega\alpha&=-g h'\omega,\\
\boxed{D\alpha+\frac12D'\omega^2+g h'=0}.
\end{aligned}
$$

约去$\omega$用于已经转动的目标时刻；初始$\omega=0$处应使用连续延拓或牛顿方程，不能以“除以零”推导初始动力学。光滑面的$D'_{\mathrm s}=2h'h''$，于是

$$
\alpha_{\mathrm s}=-\frac{h'(g+h''\omega_{\mathrm s}^2)}{j+(h')^2}.
$$

先化简括号中的全部项：

$$
\begin{aligned}
h''\omega_{\mathrm s}^2
&=\frac{5a}{18\sqrt3}\cdot\frac94(2-\sqrt3)\frac ga
=\frac5{8\sqrt3}(2-\sqrt3)g,\\
g+h''\omega_{\mathrm s}^2
&=\left(1-\frac58+\frac5{4\sqrt3}\right)g
=\frac{9+10\sqrt3}{24}g,\\
\alpha_{\mathrm s}
&=\frac{a/6}{4a^2/9}\cdot\frac{9+10\sqrt3}{24}g
=\boxed{\frac{9+10\sqrt3}{64}\frac ga}.
\end{aligned}
$$

它为正，约为$0.411258g/a$，即在该时刻顺时针角速度仍在增大。式中必须是$9+10\sqrt3$，符号可由下面的接触力独立检验。

（9）用牛顿方程独立检查角加速度和接触保持。

质心竖直加速度为$a_{Gy}=h''\omega^2+h'\alpha$。光滑面的受力与绕质心力矩为

$$
N-mg=m a_{Gy},\qquad I_G\alpha=x_0N=-h'N.
$$

代入$N=m(g+h''\omega^2+h'\alpha)$并消元，得到$(j+(h')^2)\alpha=-h'(g+h''\omega^2)$，与能量微分完全相同。再逐项代入可得

$$
\begin{aligned}
a_{Gy}^{\mathrm s}
&=\frac{5(2-\sqrt3)}{8\sqrt3}g
-\frac{9+10\sqrt3}{384}g\\
&=\frac{50\sqrt3-83}{128}g\simeq0.02814485g,\\
N_{\mathrm s}&=\frac{45+50\sqrt3}{128}mg>0.
\end{aligned}
$$

注意质心仍向下运动，但此时竖直加速度已经向上，是下降逐渐变慢；不能把“速度向下”当成“加速度必向下”。正法向力说明目标时刻仍与桌面接触。

（10）完整求出光滑面焦点加速度。

在光滑面$\ddot X=0$。对第（7）步的速度再求导，使用乘积法则：

$$
\begin{aligned}
a_{Fx}^{\mathrm s}&=c\cos\theta\,\alpha_{\mathrm s}
-c\sin\theta\,\omega_{\mathrm s}^2,\\
a_{Fy}^{\mathrm s}&=(h''-c\cos\theta)\omega_{\mathrm s}^2
+(h'-c\sin\theta)\alpha_{\mathrm s}.
\end{aligned}
$$

第一式分别是切向和法向贡献；第二式另外包含质心加速度。在目标转角化简系数为

$$
\begin{aligned}
a_{Fx}^{\mathrm s}&=\frac a{2\sqrt3}\alpha_{\mathrm s}-\frac a2\omega_{\mathrm s}^2,\\
a_{Fy}^{\mathrm s}&=-\frac{2a}{9\sqrt3}\omega_{\mathrm s}^2-\frac{2a}3\alpha_{\mathrm s}.
\end{aligned}
$$

逐项通分后得到

$$
\begin{aligned}
\frac{a_{Fx}^{\mathrm s}}g
&=\frac{9+10\sqrt3}{128\sqrt3}-\frac98(2-\sqrt3)\\
&=\frac{3\sqrt3+10-288+144\sqrt3}{128}
=\frac{147\sqrt3-278}{128},\\
\frac{a_{Fy}^{\mathrm s}}g
&=-\frac{2-\sqrt3}{2\sqrt3}-\frac{9+10\sqrt3}{96}\\
&=\frac{48-32\sqrt3-9-10\sqrt3}{96}
=\frac{13-14\sqrt3}{32}.
\end{aligned}
$$

因此

$$
\boxed{\boldsymbol a_F^{\mathrm s}
=\frac{147\sqrt3-278}{128}g\boldsymbol e_x
+\frac{13-14\sqrt3}{32}g\boldsymbol e_y}.
$$

两分量约为$-0.182723g$、$-0.351522g$。焦点速度向右下方，却加速向左下方，不应把加速度方向画成与速度方向必然相同。

（11）重新计算纯滚动动能和角速度。

纯滚动时质心速度平方为$(h^2+(h')^2)\omega^2$，所以

$$
T_{\mathrm r}=\frac m2D_{\mathrm r}\omega^2,
\qquad D_{\mathrm r}=j+h^2+(h')^2.
$$

也可用瞬时接触材料点的平行轴惯量$I_Q=I_G+mGQ^2$计算瞬时动能，两者一致。在目标转角

$$
\begin{aligned}
D_{\mathrm r}&=\frac5{12}a^2+\frac34a^2+\frac1{36}a^2
=\frac{43}{36}a^2,\\
\frac12\cdot\frac{43}{36}a^2\omega_{\mathrm r}^2
&=\frac{2-\sqrt3}{2}ga,\\
\boxed{\omega_{\mathrm r}=6\sqrt{\frac{2-\sqrt3}{43}\frac ga}}.
\end{aligned}
$$

相同势能下降还要供给水平平动，故$\omega_{\mathrm r}<\omega_{\mathrm s}$。准确的比值为$\omega_{\mathrm r}/\omega_{\mathrm s}=4/\sqrt{43}$，不是凭“摩擦耗能”判断：本题理想静摩擦没有耗散机械能。

（12）用纯滚动速度关系求焦点速度。

将$\dot X=h\omega$代入第（7）步，有

$$
\begin{aligned}
v_{Fx}^{\mathrm r}&=(h+c\cos\theta)\omega_{\mathrm r}
=\frac{2a}{\sqrt3}\omega_{\mathrm r},\\
v_{Fy}^{\mathrm r}&=(h'-c\sin\theta)\omega_{\mathrm r}
=-\frac{2a}3\omega_{\mathrm r},\\
\boxed{\boldsymbol v_F^{\mathrm r}}
&=\boxed{4\sqrt{\frac{2-\sqrt3}{43}ga}
(\sqrt3\boldsymbol e_x-\boldsymbol e_y)},\\
|\boldsymbol v_F^{\mathrm r}|&=\frac{4a}3\omega_{\mathrm r}
=8\sqrt{\frac{2-\sqrt3}{43}ga}.
\end{aligned}
$$

![图1-4 质心与焦点的瞬时速度，以及纯滚动的零速接触点。](../figures/velocity-01.png){width=88%}

图1-4中的纯滚动焦点速度垂直$QF_1$。因为当前接触材料点零速，此瞬间可以用$|\boldsymbol v_F|=\omega QF_1$；$QF_1=4a/3$使几何路线与坐标路线完全一致。这种瞬时速度关系不能未经检查延伸成固定点转动的加速度关系。

（13）完整求纯滚动角加速度。

对$D_{\mathrm r}$求导时，必须连$h^2$也求导：

$$
D'_{\mathrm r}=2hh'+2h'h''=2h'(h+h'').
$$

代入统一能量微分式，得到

$$
\alpha_{\mathrm r}
=-\frac{h'[g+(h+h'')\omega_{\mathrm r}^2]}{j+h^2+(h')^2}.
$$

按顺序保留全部中间运算：

$$
\begin{aligned}
(h+h'')\omega_{\mathrm r}^2
&=\frac{16a}{9\sqrt3}\cdot\frac{36}{43}(2-\sqrt3)\frac ga
=\frac{64(2-\sqrt3)}{43\sqrt3}g,\\
g+(h+h'')\omega_{\mathrm r}^2
&=\frac{43\sqrt3+128-64\sqrt3}{43\sqrt3}g
=\frac{128-21\sqrt3}{43\sqrt3}g,\\
\alpha_{\mathrm r}
&=\frac{a/6}{43a^2/36}\cdot\frac{128-21\sqrt3}{43\sqrt3}g\\
&=\boxed{\frac{2(128\sqrt3-63)}{1849}\frac ga}.
\end{aligned}
$$

这里$1849=43^2$，有理化用$6/\sqrt3=2\sqrt3$。结果约为$0.171663g/a$，顺时针为正。不能只对$\omega^2$中势能下降求导，而把分母惯量当作常数。

（14）求纯滚动焦点加速度，明确新增平动项。

质心水平加速度来自$\dot X=h\omega$的乘积求导，$a_{Gx}=h'\omega^2+h\alpha$。将这一项加到第（10）步，或直接对纯滚动焦点速度求导，得到

$$
\begin{aligned}
a_{Fx}^{\mathrm r}&=(h'-c\sin\theta)\omega_{\mathrm r}^2
+(h+c\cos\theta)\alpha_{\mathrm r}\\
&=-\frac{2a}3\omega_{\mathrm r}^2+\frac{2a}{\sqrt3}\alpha_{\mathrm r},\\
a_{Fy}^{\mathrm r}&=(h''-c\cos\theta)\omega_{\mathrm r}^2
+(h'-c\sin\theta)\alpha_{\mathrm r}\\
&=-\frac{2a}{9\sqrt3}\omega_{\mathrm r}^2-\frac{2a}3\alpha_{\mathrm r}.
\end{aligned}
$$

水平分量的两项分别为$[-24(2-\sqrt3)/43]g$与$[4(128\sqrt3-63)/(1849\sqrt3)]g$；竖直分量的两项分别为$[-8(2-\sqrt3)/(43\sqrt3)]g$与$[-4(128\sqrt3-63)/(3\cdot1849)]g$。将分母统一为$1849$，有

$$
\begin{aligned}
\frac{a_{Fx}^{\mathrm r}}g
&=\frac{-1032(2-\sqrt3)+512-84\sqrt3}{1849}
=\frac{948\sqrt3-1552}{1849},\\
\frac{a_{Fy}^{\mathrm r}}g
&=\frac{344-\frac{688}3\sqrt3+84-\frac{512}3\sqrt3}{1849}
=\frac{428-400\sqrt3}{1849}.
\end{aligned}
$$

所以

$$
\boxed{\boldsymbol a_F^{\mathrm r}
=\frac{948\sqrt3-1552}{1849}g\boldsymbol e_x
+\frac{428-400\sqrt3}{1849}g\boldsymbol e_y}.
$$

分量约为$+0.0486664g$、$-0.143224g$，方向为右下方。其水平符号与光滑面不同，正是水平平动贡献不能省略的直接证据。

（15）用接触材料点的非零加速度独立复核。

图1-5中的$K$是椭圆在$Q$处的曲率中心，$\rho=QK$。由参数曲线曲率公式，若未旋转椭圆为$(b\sin\varphi,a\cos\varphi)$，有

$$
\rho=\frac{(b^2\cos^2\varphi+a^2\sin^2\varphi)^{3/2}}{ab}.
$$

接触参数满足$\cos^2\varphi=1/3$、$\sin^2\varphi=2/3$，故分子中的平方为$8a^2/9$，从而

$$
\rho=\frac{(8a^2/9)^{3/2}}{\sqrt{2/3}a^2}
=\frac{16a}{9\sqrt3}=h+h''.
$$

![图1-5 纯滚动瞬间的接触材料点与局部曲率中心。](../figures/contact-01.png){width=56%}

使用图中同一瞬间的固定材料点$Q$，刚体加速度公式给出

$$
\begin{aligned}
a_{Qx}&=a_{Gx}-h\alpha-h'\omega^2=0,\\
a_{Qy}&=a_{Gy}-h'\alpha+h\omega^2
=(h+h'')\omega^2=\rho\omega^2>0.
\end{aligned}
$$

因此它零速而有向上的加速度。绕该瞬间材料点列转动方程，必须计入参考点加速度项，得到$I_Q\alpha=m x_0(g+a_{Qy})$。代入$x_0=a/6$、$I_Q=43ma^2/36$及$a_{Qy}=\rho\omega^2$，正好重现第（13）步；若误设$a_Q=0$，将漏掉曲率项。

（16）求实际接触力，检查纯滚动约束的物理可实现性。

由图1-3中的实际作用点，取顺时针力矩为正，完整牛顿方程为

$$
f=m a_{Gx},\qquad N=m(g+a_{Gy}),\qquad
I_G\alpha=-h'N-hf.
$$

将$a_{Gx}=h'\omega^2+h\alpha$、$a_{Gy}=h''\omega^2+h'\alpha$代入，所有$\alpha$项移到左侧后为

$$
(j+h^2+(h')^2)\alpha=-h'[g+(h+h'')\omega^2],
$$

与前两条路线一致。在目标转角的结果为

$$
\begin{aligned}
f&=\frac{195\sqrt3-132}{1849}mg\simeq0.1112763mg>0,\\
N&=\frac{1440+244\sqrt3}{1849}mg\simeq1.0073664mg>0,\\
\frac{|f|}{N}&=\frac{195\sqrt3-132}{1440+244\sqrt3}\simeq0.1104626.
\end{aligned}
$$

因此接触点摩擦向右，法向力向上。纯滚动要求静摩擦足够提供所需$f$；$0.1104626$只是该时刻的系数需求，并不自动保证此前整个过程都未滑动。

（17）统一最终答案、单位和释放条件。

光滑面结果为

$$
\begin{aligned}
\omega_{\mathrm s}&=\frac32\sqrt{(2-\sqrt3)g/a},\qquad
\alpha_{\mathrm s}=\frac{9+10\sqrt3}{64}\frac ga,\\
\boldsymbol v_F^{\mathrm s}&=\sqrt{(2-\sqrt3)ga}
\left(\frac{\sqrt3}4\boldsymbol e_x-\boldsymbol e_y\right),\\
\boldsymbol a_F^{\mathrm s}&=g\left(
\frac{147\sqrt3-278}{128}\boldsymbol e_x
+\frac{13-14\sqrt3}{32}\boldsymbol e_y\right).
\end{aligned}
$$

纯滚动结果为

$$
\begin{aligned}
\omega_{\mathrm r}&=6\sqrt{(2-\sqrt3)g/(43a)},\qquad
\alpha_{\mathrm r}=\frac{2(128\sqrt3-63)}{1849}\frac ga,\\
\boldsymbol v_F^{\mathrm r}&=4\sqrt{(2-\sqrt3)ga/43}
(\sqrt3\boldsymbol e_x-\boldsymbol e_y),\\
\boldsymbol a_F^{\mathrm r}&=g\left(
\frac{948\sqrt3-1552}{1849}\boldsymbol e_x
+\frac{428-400\sqrt3}{1849}\boldsymbol e_y\right).
\end{aligned}
$$

$\sqrt{g/a}$的单位为$\mathrm{s^{-1}}$，$g/a$为$\mathrm{s^{-2}}$，$\sqrt{ga}$为速度，$g$为加速度，四类结果量纲正确。两种能量路线都约去了$m$。若向左倾倒，速度和加速度的水平分量反号，竖直分量不变；相应角矢量反向，不能只改焦点水平运动而保持角矢量方向不变。

若从实际有限偏角$\theta_0>0$无初速释放，应将能量式右侧的$a$换为$h(\theta_0)$，再由对应$D$求$\omega^2$和$\alpha$。本文所列数值是$\theta_0\to0^+$的极限；到达时刻在该极限下趋于无穷，并不等于精确不稳定平衡能在有限时间自行开始运动。

## 六、关键洞察

几何高度函数统一了四个看似无关的量：质心高度$h$、接触点横偏置$h'$、几何竖直加速度系数$h''$及接触曲率$\rho=h+h''$。其中$x_0=-h'$决定法向力的转动力矩，纯滚动约束$\dot X=h\omega$决定新增水平动能。只记一个接触半径，会使几何、动能和角加速度三处同时出错。

纯滚动动能可以按当前材料接触点计算，但动力学不能照搬固定转轴公式。一般绕加速材料点$Q$有$\boldsymbol\tau_Q=I_Q\dot{\boldsymbol\Omega}+\boldsymbol r_{G/Q}\times m\boldsymbol a_Q$。本题$\boldsymbol a_Q$向上，$G$在$Q$右侧，所以该项与重力矩在移项后共同增大顺时针角加速度。这是能量中$D'$项在受力语言中的对应物，不是额外人为加上的力矩。

质心竖直加速度的符号独立于下降速度。在目标角度两种接触的$a_{Gy}$都为正，尽管$\dot h<0$；而上焦点的$a_{Fy}$仍为负。不同材料点的加速度由同一转动叠加到不同位置向量上，没有理由必须同向。

用拉格朗日方程可把两条能量求导路线进一步核对。消去约束后$L=mD(\theta)\dot\theta^2/2-mg h(\theta)$，分别计算

$$
\begin{aligned}
\frac{\partial L}{\partial\dot\theta}&=mD\dot\theta,\\
\frac{\mathrm d}{\mathrm dt}\frac{\partial L}{\partial\dot\theta}
&=mD\ddot\theta+mD'\dot\theta^2,\\
\frac{\partial L}{\partial\theta}
&=\frac m2D'\dot\theta^2-mg h'.
\end{aligned}
$$

二者相减给出$D\alpha+D'\omega^2/2+g h'=0$。它在$\omega=0$处也成立，不需要除以角速度；因此是补充初始时刻严谨性的有效路线。

还可定量解释释放等待时间。记$d=a^2-b^2=a^2/3$，小角度时$h=a-d\theta^2/(2a)+O(\theta^4)$、$h'=-d\theta/a+O(\theta^3)$。光滑面的$D_0=j$，纯滚动的$D_0=j+a^2$，线性化得

$$
\ddot\theta=\lambda^2\theta,\qquad
\lambda^2=\frac{gd}{aD_0}.
$$

由$\theta(0)=\theta_0$、$\dot\theta(0)=0$得到$\theta=\theta_0\cosh(\lambda t)$；到达一个固定小角$\theta_*$的时间为$\lambda^{-1}\operatorname{arcosh}(\theta_*/\theta_0)$，当$\theta_0\to0^+$时按对数发散。精确$\theta_0=0$则始终为零，微扰极限的速度结果和等待时间发散能够同时成立。

## 七、易错点

把$GQ$、$QF_1$和曲率半径$\rho$混为一个“滚动半径”。本题分别为$\sqrt7 a/3$、$4a/3$、$16a/(9\sqrt3)$，用途不同；$h=\sqrt3 a/2$又是另一个几何量。代入前必须说明所取哪条长度。

光滑面误用$v_G=\omega GQ$。光滑时质心水平速度为零，接触材料点有沿桌面的速度；瞬时转动中心不在$Q$。反过来，纯滚动若继续用光滑面的动能，漏掉$m h^2\omega^2/2$，会给出错误角速度。

误把接触点零速求导为零加速度。零速条件关联一系列不同材料点，并非同一材料点整段时间都静止。第（15）步的$a_{Qy}=\rho\omega^2$直接反证这一跳步。

求导漏掉$D'$，或者将$h''\omega^2+h'\alpha$写成$h''\omega^2-h'\alpha$。应分别列出链式求导的中间行，$h'<0$的负号已经包含在$h'$自身，不能再凭下降方向额外添负号。

把某时刻法向力当作$mg$。本题目标时刻$N$稍大于$mg$，因为$a_{Gy}>0$。设$N=mg$会同时破坏平动和转动方程；检查$I_G\alpha=x_0N$即可发现矛盾。

不注明顺时针角标量约定，却在叉积中仍用$+\omega\boldsymbol e_z$。该写法会把焦点速度和切向加速度的方向反转。最稳妥的核对是用坐标求导与矢量叉积得到同一分量。

只验最终时刻的静摩擦系数，不检查此前滑动与法向力。$\mu_s\ge0.1104626$是该点的必要条件，并不保证全程纯滚动。应沿整个转角区间检验$N>0$和$|f|\le\mu_sN$。

## 八、课堂讲解建议

课堂先让学生指出图1-2中五条不同长度，教师用颜色只标接触点、质心和上焦点，不先给一个统一“半径”。板书将$h,h',h''$放在一列，并在另一列写明每项进入哪条运动关系，使学生能追踪每个符号的来源。

教师先处理光滑面，要求学生从水平合力为零解释$\dot X=0$，再推焦点两分量。随后保留原几何不变，只把接触改为纯滚动，让学生从$v_Q=0$独立推出$\dot X=h\omega$。课堂对照动能时，应明确静摩擦不耗能，却改变平动分配。

板书的加速度部分不以“类似可得”结束。教师先完整微分焦点坐标，再完整微分能量系数$D$，最后用$N-mg=ma_{Gy}$与质心力矩逐项复核。让学生解释“质心下落且加速度向上”和“焦点速度向右而加速度向左”两个现象，能够检验是否真的区分速度与加速度。

课堂最后使用图1-5提问当前材料点下一瞬间是否仍接触桌面。教师应把移动接触位置和固定材料点的不同写清，再由$a_Q$修正转动方程。释放条件宜在开始和结束各说明一次，避免学生把不稳定平衡误解成无扰动也会自动运动。

## 九、变式训练

变式一：将倾倒方向改为向左，但仍保留地面$x$轴向右、$y$轴向上。求两种接触条件下的焦点速度及加速度方向，并说明角矢量如何改变。

完整解答：对右倾轨迹做镜像$x\mapsto-x$。椭圆几何、重力与水平桌面均保持不变，故$h,|\omega|,|\alpha|$和$y$分量不变。光滑面焦点速度变为$\sqrt{(2-\sqrt3)ga}(-\sqrt3\boldsymbol e_x/4-\boldsymbol e_y)$，加速度水平分量变为$(278-147\sqrt3)g/128>0$、竖直分量仍为$(13-14\sqrt3)g/32<0$。纯滚动速度变为$4\sqrt{(2-\sqrt3)ga/43}(-\sqrt3\boldsymbol e_x-\boldsymbol e_y)$，加速度水平分量变为$(1552-948\sqrt3)g/1849<0$，竖直分量仍为$(428-400\sqrt3)g/1849$。角矢量从$-\omega\boldsymbol e_z$、$-\alpha\boldsymbol e_z$变为正$z$方向，两个顺时针标量则均为负。

变式二：将半短轴改为任意$0<b<a$，给出两种接触的角速度通式，并检查$b\to a$的圆形极限。

完整解答：面积积分仍给$j=(a^2+b^2)/4$，最低点仍给$h=\sqrt{a^2\cos^2\theta+b^2\sin^2\theta}$及$h'=(b^2-a^2)\sin\theta\cos\theta/h$。将真实两种质心速度代入能量得

$$
\omega_{\mathrm s}^2=\frac{2g(a-h)}{j+(h')^2},\qquad
\omega_{\mathrm r}^2=\frac{2g(a-h)}{j+h^2+(h')^2}.
$$

两种角加速度分别为$-h'(g+h''\omega_{\mathrm s}^2)/(j+(h')^2)$及$-h'[g+(h+h'')\omega_{\mathrm r}^2]/(j+h^2+(h')^2)$。焦点速度由$c=\sqrt{a^2-b^2}$代入主解析的坐标求导式即可，不另改变约束。当$b\to a$时$h\to a$、$h'\to0$、$c\to0$，无初始动能则两种$\omega$均趋于零；圆盘的姿态改变不降低质心，不能从静止仅靠重力自行滚动。这个极限同时检查势能与惯量的分母。

变式三：开始时长轴精确竖直，但给顺时针初始角速度$\omega_0>0$。分别求任意转角的角速度，并求初始接触保持的速度上限。

完整解答：光滑面初始$h'=0$且$\dot X=0$，故初始动能$mj\omega_0^2/2$。纯滚动初始$\dot X=a\omega_0$，初始动能$m(j+a^2)\omega_0^2/2$。两种情况能量给出

$$
\begin{aligned}
\omega_{\mathrm s}^2&=\frac{j\omega_0^2+2g(a-h)}{j+(h')^2},\\
\omega_{\mathrm r}^2&=\frac{(j+a^2)\omega_0^2+2g(a-h)}{j+h^2+(h')^2}.
\end{aligned}
$$

初始$h'=0$使角加速度为零，但$h''=(b^2-a^2)/a=-a/3$，所以$a_{Gy}(0)=-a\omega_0^2/3$。由$N=m(g+a_{Gy})$得$N(0)=m(g-a\omega_0^2/3)$。要保持接触，须$\omega_0^2\le3g/a$；若大于该值，约束会要求负法向力而桌面不能向下拉，薄片立即离开，此后不能沿用接触运动公式。等号为临界，还需后续检验。虽然初始角加速度为零，初始非零角速度使系统确实开始运动，不再存在上一种无扰动静止的歧义。

变式四：确定从微扰竖立位置滚到六十度全程不滑所需的最小静摩擦系数，并说明只检查末时刻为什么不足。

完整解答：令$H=h/a$、$J=5/12$、$W=a\omega^2/g$、$A=a\alpha/g$，撇号均对$\theta$求导。由主解析

$$
\begin{aligned}
W&=\frac{2(1-H)}{J+H^2+(H')^2},\\
A&=-\frac{H'[1+(H+H'')W]}{J+H^2+(H')^2},\\
\frac f{mg}&=H'W+HA,\qquad
\frac N{mg}=1+H''W+H'A.
\end{aligned}
$$

因此$\mu_{s,\min}=\max_{0\le\theta\le\pi/3}|H'W+HA|/[1+H''W+H'A]$。该区间法向力为正，直接代入给$0^\circ,15^\circ,30^\circ,45^\circ,60^\circ$处系数需求分别为$0,0.059358,0.105204,0.124779,0.110463$。45度已经大于末时刻，足以排除只用末值的做法。对上述连续函数作一维极值求解，驻点为$\theta\simeq46.348035^\circ$，与两端值比较得

$$
\boxed{\mu_{s,\min}\simeq0.1249200}.
$$

核验时先求$H'$、$H''$及动力学量，再计算摩擦比，不以末时刻的单个公式假定其单调。所得阈值只针对微扰释放至六十度，不声称足以保证之后更大转角全程纯滚动。

<!-- question-complete -->
