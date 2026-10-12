# 第 6 题

<!-- question-start -->

考虑太空版“植物大战僵尸”。豌豆射手在地面参考系 $S$ 中以速度 $v_s=0.8c$ 沿 $x$ 轴正向运动。在射手静止参考系 $S'$ 中，每隔 $1\,\mathrm s$ 发射一个豌豆，发射方向与 $x$ 轴正向夹角为 $\theta$。豌豆的传播性质与光完全相同。

地面系中，远处铁栅门僵尸以速率 $v_z=0.6c$ 迎着豌豆运动，其速度方向与 $x$ 轴负向的夹角为 $\alpha=30^\circ$。豌豆在地面系中的入射方向与 $x$ 轴正向成 $30^\circ$。取入射方向在 $x$ 轴下方，僵尸迎面运动方向在上方。

（1）求射手系中的发射角 $\theta$。

（2）在僵尸静止参考系中，两次被豌豆击中的时间间隔是多少？

（3）在僵尸系中，豌豆垂直于铁栅门入射，门将豌豆以原速反弹。求地面系中两个反射豌豆到达 $x$ 轴的时间间隔。

![图 6-1　射手系相对地面系的运动，以及地面系中入射和迎面运动的方向。](../figures/question-06.png)

<!-- question-end -->

## 一、题型定位

光速传播中的方向变换、运动平面截获和反射事件时序。发射间隔是射手自身时钟的间隔，击中间隔要转换到僵尸系；反射后问的是两次到达整条 $x$ 轴的事件，不是到达同一个接收器的事件。

不同发射时刻，射手已经移到不同位置，两束光在地面系中相互平行。因此截获模型应将栅门作为能截获两束光的平面，两次击中可发生在门上的不同位置。不能把它们同时当成同一个质点世界线上的击中事件，然后直接套用单钟时间膨胀。

## 二、知识点

- 光在所有惯性系中速率为 $c$，其不同坐标分量仍须按相对论速度变换计算。
- 相对运动中的光行差，即光传播方向的参考系变换。
- 同一运动钟连续发射的固有时与地面坐标时间关系 $\Delta t=\gamma\Delta\tau$。
- Lorentz时间变换同时包含时间项和空间分离项，不能仅凭两系速度就忽略空间项。
- 移动平面的截获条件是光线位置落在当前平面上，不是固定距离除以相对速度。
- 共线反射可通过门的静止系求出，再转换回地面系。
- 两个不同地点的到达事件可能为空间样分离，时间先后并不代表因果先后。

## 三、物理图像

记射手速度比例 $\beta_s=4/5$、僵尸速度比例 $\beta_z=3/5$。对应因子为

$$
\gamma_s=\frac1{\sqrt{1-\beta_s^2}}=\frac53,
\qquad
\gamma_z=\frac1{\sqrt{1-\beta_z^2}}=\frac54.
$$

地面系入射单位向量取为

$$
\boldsymbol n=(\cos\alpha,-\sin\alpha),\qquad \alpha=30^\circ.
$$

僵尸速度为 $-\beta_zc\boldsymbol n$，栅门平面法线平行 $\boldsymbol n$。光沿 $+\boldsymbol n$ 入射，反射后沿 $-\boldsymbol n$ 返回。门平面的切向单位向量可取 $\boldsymbol e_\perp=(\sin\alpha,\cos\alpha)$。

设第一次发射在地面原点、地面时刻为零，第二次发射时刻为 $t_e$，发射点为 $(\beta_sct_e,0)$。栅门很远，两个截获事件均发生在各自发射之后。其初始沿法线距离用 $D>0$ 表示；时间间隔计算中 $D$ 应消去。

## 四、解题入口

第一问用射手系到地面系的光速度分量变换，先解角度，不把发射间隔掺入方向关系。第二问先在地面系分别建立发射事件和截获事件，再对截获事件差做Lorentz变换。

第三问先确认地面系反射方向确为入射方向的反向，再由光线从门返回 $y=0$ 的条件求到达时刻。保留“第二束减第一束”的带符号时间差直到最后，若差为负，应解释先后反转，而不是提前强行改正号。

## 五、解析

（1）用速度变换建立光行差公式。

在射手系中，光的速度分量为

$$
u_x'=c\cos\theta,\qquad u_y'=-c\sin\theta.
$$

射手系相对地面系沿 $+x$ 运动，故从 $S'$ 变换到 $S$：

$$
\begin{aligned}
u_x&=\frac{u_x'+v_s}{1+v_su_x'/c^2}
=c\frac{\cos\theta+\beta_s}{1+\beta_s\cos\theta},\\
u_y&=\frac{u_y'}{\gamma_s(1+v_su_x'/c^2)}
=-\frac{c\sin\theta}{\gamma_s(1+\beta_s\cos\theta)}.
\end{aligned}\tag{1}
$$

地面系光速仍为 $c$，而方向角为 $\alpha$，所以 $u_x=c\cos\alpha$。令式（1）第一式与其相等：

$$
\begin{aligned}
\cos\alpha(1+\beta_s\cos\theta)
&=\cos\theta+\beta_s,\\
(1-\beta_s\cos\alpha)\cos\theta
&=\cos\alpha-\beta_s,\\
\cos\theta&=\frac{\cos\alpha-\beta_s}
{1-\beta_s\cos\alpha}.
\end{aligned}\tag{2}
$$

分母为正，因为 $\beta_s<1$ 且 $\cos\alpha\le1$。代入 $\cos30^\circ=\sqrt3/2$、$\beta_s=4/5$：

$$
\begin{aligned}
\cos\theta
&=\frac{\sqrt3/2-4/5}{1-(4/5)(\sqrt3/2)}\\
&=\frac{5\sqrt3-8}{10-4\sqrt3},\\
\boxed{\theta}
&\boxed{=\arccos\frac{5\sqrt3-8}{10-4\sqrt3}
\approx77.58795^\circ.}
\end{aligned}\tag{3}
$$

角度取 $0<\theta<\pi/2$，对应向右下方发射。射手自身看到较大的倾角，地面看到向前更集中的光束，符合光行差的方向趋势。用式（1）第二式回代，得到 $u_y=-c/2$，即确实为下方 $30^\circ$，不是上方的另一条数学解。

（2）确定地面系两个发射事件的时间和位置差。

射手静止系发射间隔为 $\Delta\tau_e=1\,\mathrm s$。两次发射位于同一射手时钟上，故可直接用时间膨胀：

$$
\Delta t_e=\gamma_s\Delta\tau_e=\frac53\,\mathrm s.
$$

射手在这段地面时间内前进，所以

$$
\Delta x_e=\beta_sc\Delta t_e
=\frac45c\frac53\,\mathrm s
=\frac43c\,\mathrm s,
\qquad \Delta y_e=0.\tag{4}
$$

这里 $c\,\mathrm s$ 是长度，不是速度与时间混写。若只将发射时间取为1秒，却又使用地面系射手位置，就把两个参考系的事件数据混在一起了。

（3）对任意一束光建立移动栅门的截获条件。

栅门在地面系中的平面方程为

$$
\boldsymbol n\cdot\boldsymbol r=D-\beta_zct.
$$

在地面时刻 $t_e$ 从 $\boldsymbol r_e=(\beta_sct_e,0)$ 发出的光，之后位置为

$$
\boldsymbol r(t)=\boldsymbol r_e+c(t-t_e)\boldsymbol n.
$$

令截获时刻为 $t_h$，将光的位置代入门平面方程：

$$
\begin{aligned}
\boldsymbol n\cdot\boldsymbol r_e+c(t_h-t_e)
&=D-\beta_zct_h,\\
\beta_sct_e\cos\alpha+ct_h-ct_e
&=D-\beta_zct_h,\\
(1+\beta_z)t_h
&=\frac Dc+(1-\beta_s\cos\alpha)t_e,\\
t_h&=\frac{D/c+(1-\beta_s\cos\alpha)t_e}{1+\beta_z}.
\end{aligned}\tag{5}
$$

图6-2展示两个不同发射点、两条平行光线及截获时门的位置。后面的 $(1-\beta_s\cos\alpha)$ 不是经验Doppler因子，而是射手位移在图中法线方向的投影产生的。

![图 6-2　两条平行入射光线、运动栅门和分别位于x轴的返回点。](../figures/events-06.png)

将两个 $t_h$ 相减，初始距离消去：

$$
\Delta t_h
=\frac{1-\beta_s\cos\alpha}{1+\beta_z}\Delta t_e.
\tag{6}
$$

代入数值，

$$
\begin{aligned}
\Delta t_h
&=\frac{1-2\sqrt3/5}{8/5}\frac53\,\mathrm s\\
&=\frac{5(5-2\sqrt3)}{24}\,\mathrm s
\approx0.3199788302\,\mathrm s.
\end{aligned}
$$

地面系中第二束仍较晚击中门，因为式（6）全部因子为正。

（4）将截获事件转换到僵尸参考系。

僵尸速度沿 $-\boldsymbol n$，其时间坐标变换为

$$
t_z=\gamma_z\left(t+\frac{\beta_z}{c}
\boldsymbol n\cdot\boldsymbol r\right).
$$

两个击中事件都在门平面上，由平面方程可知

$$
\boldsymbol n\cdot\Delta\boldsymbol r_h
=-\beta_zc\Delta t_h.
$$

因此直接变换事件差，得

$$
\begin{aligned}
\Delta t_{h,z}
&=\gamma_z\left(\Delta t_h+
\frac{\beta_z}{c}\boldsymbol n\cdot\Delta\boldsymbol r_h\right)\\
&=\gamma_z(1-\beta_z^2)\Delta t_h\\
&=\frac{\Delta t_h}{\gamma_z}.
\end{aligned}\tag{7}
$$

这一步不能只引用单钟时间膨胀，因为两个击中点可以有不同的门面切向坐标。正确依据是完整Lorentz变换与平面运动关系。$\Delta t_{h,z}$ 是僵尸静止系由同步时钟定义的坐标时间间隔。

由式（6）、（7），

$$
\begin{aligned}
\Delta t_{h,z}
&=\frac{1-\beta_s\cos\alpha}{(1+\beta_z)\gamma_z}
\gamma_s\Delta\tau_e\\
&=\frac{(5-2\sqrt3)/5}{(8/5)(5/4)}\frac53\,\mathrm s\\
&=\boxed{\frac{5-2\sqrt3}{6}\,\mathrm s
\approx0.2559830641\,\mathrm s.}
\end{aligned}\tag{8}
$$

若栅门被解释为同一个没有空间尺寸的点，两条来自不同发射点的平行光线不能都击中它，题目的截获模型便不成立。本解采用栅门平面模型，保持题设两次截获成立，并将时间测量的含义说清楚。

（5）在门静止系反射，再变换回地面系。

以 $\boldsymbol n$ 方向为一维正方向，门在地面系的速度为 $-\beta_zc$。地面入射光速分量为 $+c$。变换到门静止系，

$$
u_{\rm in,z}
=\frac{c-(-\beta_zc)}{1-c(-\beta_zc)/c^2}
=\frac{(1+\beta_z)c}{1+\beta_z}=c.
$$

门内法向与光线共线，因此反射后在门系速度为 $-c$。变换回地面：

$$
u_{\rm out}
=\frac{-c-\beta_zc}{1+(-c)(-\beta_zc)/c^2}
=\frac{-(1+\beta_z)c}{1+\beta_z}=-c.
$$

垂直于 $\boldsymbol n$ 的速度分量始终为零，所以地面反射方向也正好为 $-\boldsymbol n$。不能使用经典公式给出反射速率 $c+2v_z$；光速不变排除了这种写法。这里求的是方向与事件时间，反射频率改变并不影响传播速率为 $c$。

（6）利用返回到 $x$ 轴的条件求地面到达时刻。

一束光从 $t_e$ 传播到 $t_h$，发射点在 $y=0$，所以击中门的位置纵坐标为

$$
y_h=-c\sin\alpha(t_h-t_e).
$$

反射后向上返回，纵向速度为 $+c\sin\alpha$。设返回 $x$ 轴的时刻为 $t_r$，则

$$
\begin{aligned}
0&=y_h+c\sin\alpha(t_r-t_h),\\
c\sin\alpha(t_r-t_h)&=c\sin\alpha(t_h-t_e),\\
t_r-t_h&=t_h-t_e,\\
\boxed{t_r=2t_h-t_e.}
\end{aligned}\tag{9}
$$

$\sin\alpha=1/2\ne0$，所以约去它合法。返回时间等于去程时间，是因为同一束光沿原直线反向传播、速率同为 $c$，不是因为门在地面静止。

横坐标同样需要检查。击中时

$$
x_h=x_e+c\cos\alpha(t_h-t_e).
$$

返回时

$$
\begin{aligned}
x_r&=x_h-c\cos\alpha(t_r-t_h)\\
&=x_e+c\cos\alpha(t_h-t_e)
-c\cos\alpha(t_h-t_e)=x_e.
\end{aligned}\tag{10}
$$

所以每束光返回它各自的发射位置，而不是返回此时已经前进的射手。两次返回位置差仍为式（4）的 $4c\,\mathrm s/3$。

（7）求带符号到达差，并解释第二束先返回。

用“第二束减第一束”定义时间差。由式（9），

$$
\begin{aligned}
\Delta t_r
&=2\Delta t_h-\Delta t_e\\
&=\left[\frac{2(1-\beta_s\cos\alpha)}{1+\beta_z}-1\right]\Delta t_e\\
&=\frac{1-\beta_z-2\beta_s\cos\alpha}{1+\beta_z}
\gamma_s\Delta\tau_e.
\end{aligned}\tag{11}
$$

代入参数，不提前取绝对值：

$$
\begin{aligned}
\Delta t_r
&=\frac{1-3/5-2(4/5)(\sqrt3/2)}{8/5}
\frac53\,\mathrm s\\
&=\frac{(2-4\sqrt3)/5}{8/5}\frac53\,\mathrm s\\
&=\frac{5(1-2\sqrt3)}{12}\,\mathrm s\\
&\approx-1.0267090063\,\mathrm s.
\end{aligned}
$$

负号表示第二束虽较晚发射，也较晚击中门，却较早返回它自己的 $x$ 轴位置。原因是门在迎面接近，加上第二次发射点沿光线法向更靠近门，第二束的去程和返程均显著缩短。

题目所问“时间间隔”取两次事件时间的正差，即

$$
\boxed{|\Delta t_r|=\frac{5(2\sqrt3-1)}{12}\,\mathrm s
\approx1.0267090063\,\mathrm s.}\tag{12}
$$

应同时注明第二束先到达。图6-3把发射、击中和返回事件放在同一地面时间轴上，后面较早返回的结论对应的是不同横坐标的两点，不能误画成同一接收器先后收到两束光。

![图 6-3　地面时空图中的两次发射、击中与返回x轴事件。](../figures/timeline-06.png)

（8）以具体初始距离重建事件，核验时间先后。

只为核验取 $D/c=6\,\mathrm s$，并令第一次发射 $t_{e0}=0$、第二次 $t_{e1}=5/3\,\mathrm s$。由式（5），

$$
\begin{aligned}
t_{h0}&=\frac6{1.6}=3.75\,\mathrm s,\\
t_{h1}&=t_{h0}+\Delta t_h
\approx4.0699788302\,\mathrm s.
\end{aligned}
$$

两束击中均在各自发射之后。由式（9），

$$
\begin{aligned}
t_{r0}&=7.5\,\mathrm s,\\
t_{r1}&=2(4.0699788302)-\frac53
\approx6.4732909937\,\mathrm s.
\end{aligned}
$$

所以第二束先返回，而 $t_{r1}-t_{r0}$ 正好等于式（11）。改变 $D$ 会共同平移截获和返回时间，但不改变各次事件之差；最终答案不应含未知初始距离。

（9）核验因果性质，区分不同地点的事件与同一接收器。

两个返回事件的空间差为 $\Delta x_r=4c\,\mathrm s/3$，时间差的绝对值约为 $1.026709\,\mathrm s$。比较

$$
\frac{|\Delta x_r|}{c}=\frac43\,\mathrm s
>|\Delta t_r|.
$$

于是

$$
c^2\Delta t_r^2-\Delta x_r^2<0,
$$

两事件为空间样分离，不能互相发出光信号及时影响对方。它们在不同参考系中的时间顺序可以不同，不存在后发光在同一地点超越先发光的因果悖论。

若改为问某个固定接收器或射手收到光的间隔，需要重新检查两条反射光是否经过该接收器，并计算其接收事件。原题仅要求到达 $x$ 轴，式（12）不能直接作为任意接收器的测量间隔。

## 六、关键洞察

三个时间间隔各有不同的数据来源：发射间隔位于同一射手世界线上；截获间隔位于运动门的世界面上；返回间隔位于地面 $y=0$ 平面上不同位置。参考系转换必须针对实际事件，而不是看到某个速度就套一个 $\gamma$。

第二问虽最终出现 $\Delta t_h/\gamma_z$，但正确论证还包含 $\boldsymbol n\cdot\Delta\boldsymbol r_h=-\beta_zc\Delta t_h$。门面切向间距并不为零，由图6-2可算出

$$
\boldsymbol e_\perp\cdot\Delta\boldsymbol r_h
=\boldsymbol e_\perp\cdot\Delta\boldsymbol r_e
=\beta_sc\Delta t_e\sin\alpha
=\frac23c\,\mathrm s.
$$

门系的这两个击中点也相距 $2c\,\mathrm s/3$。因此坐标间隔 $0.255983\,\mathrm s$ 不是同一个位于击中点的时钟经历的固有时。用门面上的同步时钟描述可以回答题问；若只允许一个点状僵尸接收，就需要更改发射指向，不能维持题给相同方向。

返回先后也可不代数字先判断。由式（11），第二束先返回的条件为

$$
2\beta_s\cos\alpha>1-\beta_z.
$$

本题左侧为 $4\sqrt3/5$，右侧为 $2/5$，显然成立。这个判据来源于运动平面截获与往返路径，不是一般Doppler频率公式本身。

## 七、易错点

- 用经典速度相加改变光速，得到大于或小于 $c$ 的传播速率。
- 将射手系1秒直接当作地面两次发射间隔。
- 只变换时间而不计射手位移，使截获时间缺少 $1-\beta_s\cos\alpha$。
- 将门面不同位置的两个击中事件当作单个时钟世界线，不加条件地称为固有时。
- 在反射方向尚未变换前，就默认地面反射角与静止门的普通反射规律相同。
- 把返回 $x$ 轴理解成返回正在运动的射手，改变接收事件。
- 在求差过程中丢掉负号，未说明第二束先返回，或把负的时间差解释成负的传播时间。

## 八、课堂讲解建议

先让学生逐个指出三问要比较的事件在哪里发生，教师在板书上画出发射世界线、栅门世界面和 $x$ 轴返回位置。速度变换阶段只处理方向；间隔阶段再处理事件，避免把多个不同概念堆入一个Doppler公式。

对第二问，先在地面系写平面方程，再要求学生保留Lorentz时间变换中的空间项。教师可以问“两个平行光束从不同发射点出发，是否击中同一位置”，以此解释为什么结果虽像时间膨胀，却不能跳过事件结构。

第三问暂时不取绝对值，让学生依据负号判断先后，再用具体 $D/c=6\,\mathrm s$ 的事件数字确认所有单束传播时间均为正。最后用空间样判据澄清先后反转与因果矛盾的区别。

## 九、变式训练

变式一：保持发射方向和速度不变，改变门的迎面速度比例 $\beta_z$。求两个返回 $x$ 轴事件同时发生的条件；若 $\beta_s=0.2$、$\alpha=30^\circ$，求临界 $\beta_z$，并判断门速度比大于临界时哪束先返回。

解：式（11）仍成立，且分母 $1+\beta_z>0$。返回同时要求分子为零：

$$
1-\beta_z-2\beta_s\cos\alpha=0,
\qquad
\boxed{\beta_{z,c}=1-2\beta_s\cos\alpha.}
$$

它只有在 $0\le\beta_{z,c}<1$ 时才是迎面亚光速运动的可行临界。代入给定参数：

$$
\beta_{z,c}=1-2(0.2)\frac{\sqrt3}{2}
=1-\frac{\sqrt3}{5}\approx0.65358984.
$$

若 $\beta_z>\beta_{z,c}$，分子为负，第二束先返回；若 $\beta_z<\beta_{z,c}$，第一束先返回。在临界处，两束返回不同的 $x$ 坐标，所以“同时”也不表示两束在同一点相遇。

对主问题 $\beta_s=0.8$，临界值 $1-4\sqrt3/5<0$ 不在迎面速度允许区间。因此所有 $0\le\beta_z<1$ 都给第二束先返回，并非0.6c时才偶然出现。

变式二：保持 $\beta_s=0.8$、$\beta_z=0.6$，把发射方向改为 $\alpha=60^\circ$，两次发射本征间隔为 $1\,\mathrm s$。求撞门事件的门系时间差及返回轴事件的实验室时间差。

解：取 $\gamma_s=5/3$、$\gamma_z=5/4$。沿门面传播方向的事件条件给

$$
\Delta t_z=\frac{\gamma_s(1-\beta_s\cos\alpha)}{(1+\beta_z)\gamma_z}\Delta\tau=\frac12\,\mathrm s.
$$

反射后返回 $x$ 轴的事件差为 $\Delta t_r=\gamma_s[1-\beta_z-2\beta_s\cos\alpha]\Delta\tau/(1+\beta_z)=-5/12\,\mathrm s$。后发光束先返回。撞门事件位于不同门面位置，$\Delta t_z$ 是门系坐标时间差，不能称为同一块门上时钟的本征间隔。

变式三：保持非零发射角 $\alpha$ 和门速度 $\beta_z$，反求使两束光同时返回 $x$ 轴所需的发射者速度；给出可行条件。

解：返回时间差的分子为 $1-\beta_z-2\beta_s\cos\alpha$。令其为零，有

$$
\beta_s=\frac{1-\beta_z}{2\cos\alpha}.
$$

对 $0<\alpha<\pi/2$，还须 $0<\beta_s<1$，即 $1-\beta_z<2\cos\alpha$。取 $\alpha=60^\circ,\beta_z=0.6$ 得 $\beta_s=0.4$。发射角严格非零保证“返回轴”的几何定义有效，不能拿退化的轴上光路直接代入。

变式四：在发射者静止的情形 $\beta_s=0$，门仍以 $-\beta_zc$ 运动。求撞门事件及返回 $x$ 轴事件的时间间隔，并比较 $\beta_z\to0$。

解：发射者本征间隔等于实验室间隔 $\Delta\tau$。代入事件方程：

$$
\Delta t_z=\frac{\Delta\tau}{(1+\beta_z)\gamma_z},\qquad
\Delta t_r=\frac{1-\beta_z}{1+\beta_z}\Delta\tau.
$$

二者均为正，故没有返回次序颠倒。门静止极限中两个坐标时间差均恢复 $\Delta\tau$；移动门使后束光需要传播的路程缩短，返回间隔相应缩短。
