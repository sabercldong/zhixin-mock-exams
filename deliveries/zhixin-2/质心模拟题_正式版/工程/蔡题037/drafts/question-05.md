# 第 5 题

木卫一、木卫二、木卫三构成拉普拉斯共振，公转周期近似满足 $T_1:T_2:T_3=1:2:4$，且轨道可视为圆轨道。

（1）求三颗卫星的轨道半径比 $r_1:r_2:r_3$。

木星探测器 Juno 利用地球引力弹弓进入转移轨道。简化认为转移椭圆的近日点、远日点分别位于地球和木星圆轨道，$R_E=1.50\times10^{11}\ \mathrm m$，木星周期 $T_J=11.86\ \mathrm y$，一年取 $365$ 天。

（2）求木星轨道半径 $R_J$；（3）求 Juno 刚进入转移轨道时的速度 $v_1$；（4）已知弹射前 Juno 的日心速度为 $35\ \mathrm{km/s}$，求该速度与地球运行速度的夹角；（5）求 Juno 在转移轨道远日点的速度 $v_3$；（6）求转移轨道的周期。

![题5　Juno 的日心转移椭圆与地球、木星轨道](../figures/question-05.pdf){ width=88% }

## 一、题型定位

本题是开普勒第三定律、活力公式、角动量守恒与引力弹弓速度矢量图的综合题。各小问并非独立：第（2）问给出的 $R_J$ 决定转移椭圆，第（3）问得到的近日点速度又是第（4）问弹弓后的目标速度。

## 二、知识点

1. $T^2\propto r^3$ 与轨道比例；
2. 椭圆半长轴 $a=(r_p+r_a)/2$；
3. 活力公式 $v^2=\mu(2/r-1/a)$；
4. 近日点与远日点的角动量守恒；
5. 地心系中引力弹弓前后相对速度等大；
6. 速度三角形与余弦定理。

## 三、物理图像

转移椭圆与地球轨道相切于近日点，与木星轨道相切于远日点。在近日点，Juno 需要比地球更快的顺行速度；在远日点，它的速度显著减小。弹弓过程中要区分日心速度 $\boldsymbol v$ 和地心相对速度 $\boldsymbol u=\boldsymbol v-\boldsymbol v_E$。

![图5-2　地心系速度矢量与转移轨道关系](../figures/solution-05.pdf){ width=91% }

## 四、解题入口

先用开普勒第三定律把所有轨道尺度化为 $R_E$ 的倍数。再用地球圆轨道消去太阳引力参数 $\mu_\odot=GM_\odot$，这样可不必额外查太阳质量。弹弓问题则画速度三角形，把弹射后的地心速度大小认成 $v_1-v_E$。

## 五、解析

对绕同一中心天体运动的卫星，开普勒第三定律为

$$
\frac{T^2}{r^3}=\text{常量}. \tag{1}
$$

因而

$$
r\propto T^{2/3}. \tag{2}
$$

把 $T_1:T_2:T_3=1:2:4$ 代入：

$$
\boxed{r_1:r_2:r_3=1:2^{2/3}:4^{2/3}
=1:2^{2/3}:2^{4/3}}. \tag{3}
$$

对木星和地球绕太阳的圆轨道，

$$
\left(\frac{T_J}{T_E}\right)^2
=\left(\frac{R_J}{R_E}\right)^3. \tag{4}
$$

$T_E=1\ \mathrm y$，所以

$$
\frac{R_J}{R_E}=11.86^{2/3}=5.20064. \tag{5}
$$

从而

$$
\boxed{R_J=5.20064\times1.50\times10^{11}
\approx7.80\times10^{11}\ \mathrm m}. \tag{6}
$$

地球公转速度可直接由周长除以周期求得：

$$
v_E=\frac{2\pi R_E}{T_E}. \tag{7}
$$

一年的秒数为

$$
T_E=365\times24\times3600=3.1536\times10^7\ \mathrm s. \tag{8}
$$

因此

$$
v_E=\frac{2\pi\times1.50\times10^{11}}{3.1536\times10^7}
=2.9886\times10^4\ \mathrm{m/s}. \tag{9}
$$

转移椭圆半长轴为

$$
a_t=\frac{R_E+R_J}{2}. \tag{10}
$$

地球圆轨道满足

$$
v_E^2=\frac{\mu_\odot}{R_E},
\qquad
\mu_\odot=v_E^2R_E. \tag{11}
$$

在转移椭圆的近日点 $r=R_E$，活力公式给出

$$
v_1^2=\mu_\odot\left(\frac2{R_E}-\frac1{a_t}\right). \tag{12}
$$

代入式（10）、（11）：

$$
\begin{aligned}
v_1^2
&=v_E^2R_E\left(\frac2{R_E}-\frac2{R_E+R_J}\right)\\
&=v_E^2\left(2-\frac{2R_E}{R_E+R_J}\right)\\
&=v_E^2\frac{2R_J}{R_E+R_J}.
\end{aligned} \tag{13}
$$

所以

$$
v_1=v_E\sqrt{\frac{2R_J}{R_E+R_J}}. \tag{14}
$$

代入 $R_J/R_E=5.20064$：

$$
\boxed{v_1\approx38.7\ \mathrm{km/s}}. \tag{15}
$$

由于 $v_1>v_E$，地球弹弓必须为 Juno 增加顺行方向的日心速度。忽略弹弓时间内地球速度的变化，地心系中弹弓前后相对速度大小不变：

$$
|\boldsymbol u_{\rm in}|=|\boldsymbol u_{\rm out}|. \tag{16}
$$

弹射后的目标速度与地球同向，故

$$
u_{\rm out}=v_1-v_E=38.707-29.886=8.821\ \mathrm{km/s}. \tag{17}
$$

令弹射前日心速度大小 $v_{\rm in}=35\ \mathrm{km/s}$，它与 $\boldsymbol v_E$ 夹角为 $\gamma$。由图5-2的速度三角形，

$$
\boldsymbol u_{\rm in}=\boldsymbol v_{\rm in}-\boldsymbol v_E. \tag{18}
$$

对式（18）平方：

$$
u_{\rm in}^2=v_{\rm in}^2+v_E^2-2v_{\rm in}v_E\cos\gamma. \tag{19}
$$

由 $u_{\rm in}=u_{\rm out}$，

$$
\cos\gamma
=\frac{v_{\rm in}^2+v_E^2-u_{\rm out}^2}{2v_{\rm in}v_E}. \tag{20}
$$

代入数值：

$$
\cos\gamma
=\frac{35^2+29.886^2-8.821^2}{2\times35\times29.886}
=0.97531. \tag{21}
$$

因而

$$
\boxed{\gamma\approx12.8^\circ}. \tag{22}
$$

在椭圆近日点和远日点，速度都与径向垂直。角动量守恒给出

$$
v_1R_E=v_3R_J. \tag{23}
$$

所以

$$
v_3=v_1\frac{R_E}{R_J}. \tag{24}
$$

代入数值：

$$
\boxed{v_3=\frac{38.707}{5.20064}\approx7.44\ \mathrm{km/s}}. \tag{25}
$$

转移椭圆也遵守开普勒第三定律。与地球轨道比较：

$$
\frac{T_t}{T_E}=\left(\frac{a_t}{R_E}\right)^{3/2}. \tag{26}
$$

而

$$
\frac{a_t}{R_E}=\frac{1+R_J/R_E}{2}
=\frac{1+5.20064}{2}=3.10032. \tag{27}
$$

因而

$$
\boxed{T_t=(3.10032)^{3/2}\ \mathrm y\approx5.46\ \mathrm y}. \tag{28}
$$

这是整个椭圆周期。从近日点飞到远日点只需半个周期：

$$
t_{E\to J}=\frac{T_t}{2}\approx2.73\ \mathrm y. \tag{29}
$$

可以用轨道比机械能对 $v_1$、$v_3$ 再作一次互相独立的检查。椭圆轨道单位质量的机械能只由半长轴决定：

$$
\varepsilon_t=-\frac{\mu_\odot}{2a_t}.
$$

在近日点，

$$
\varepsilon_t=\frac{v_1^2}{2}-\frac{\mu_\odot}{R_E}.
$$

把 $a_t=(R_E+R_J)/2$ 代入，整理为

$$
\frac{v_1^2}{2}
=\frac{\mu_\odot}{R_E}
-\frac{\mu_\odot}{R_E+R_J}.
$$

两边乘 $2$ 后正好得到式（13）。在远日点，

$$
\varepsilon_t=\frac{v_3^2}{2}-\frac{\mu_\odot}{R_J}.
$$

所以

$$
v_3^2
=2\mu_\odot\left(\frac1{R_J}-\frac1{R_E+R_J}\right)
=\frac{2\mu_\odot R_E}{R_J(R_E+R_J)}.
$$

另一方面，由式（13）和角动量关系 $v_3=v_1R_E/R_J$，

$$
v_3^2
=\left[\frac{2\mu_\odot R_J}{R_E(R_E+R_J)}\right]
\left(\frac{R_E}{R_J}\right)^2
=\frac{2\mu_\odot R_E}{R_J(R_E+R_J)}.
$$

两条路线完全一致。数值上，木星圆轨道速度为

$$
v_J=v_E\sqrt{\frac{R_E}{R_J}}
\approx13.1\ \mathrm{km/s}.
$$

而转移椭圆远日点速度只有 $7.44\ \mathrm{km/s}$。这意味着探测器到达木星轨道半径时仍比木星本身运行得慢，若要真正被木星捕获，还必须依靠木星引力和后续制动改变相对能量；“到达木星轨道”不等于“自动进入绕木星圆轨道”。

地球引力弹弓的数值还可用双曲超越速度作检查。弹射后相对地球的速度大小为

$$
v_\infty=v_1-v_E\approx8.821\ \mathrm{km/s}.
$$

相应的特征能量为

$$
C_3=v_\infty^2.
$$

代入数值：

$$
C_3\approx(8.821)^2
\approx77.8\ \mathrm{km^2/s^2}.
$$

弹射前的日心速度为 $35\ \mathrm{km/s}$，但相对地球的速度不是简单的 $35-29.886$，因为两者并不同向。由求出的 $\gamma=12.8^\circ$，

$$
u_{\rm in}^2
=35^2+29.886^2
-2(35)(29.886)\cos12.8^\circ.
$$

数值上

$$
u_{\rm in}\approx8.82\ \mathrm{km/s},
$$

与 $u_{\rm out}$ 一致。这是对速度夹角的直接回代。如果误把弹射前两速度当作同向，只会得到约 $5.11\ \mathrm{km/s}$，无法与弹射后的 $8.82\ \mathrm{km/s}$ 满足地心系弹性散射条件。

还应区分“探测器在太阳引力场中的机械能增加”和“地心系相对动能不变”。地心系中

$$
\frac12u_{\rm in}^2=\frac12u_{\rm out}^2,
$$

但日心系中速度方向改变后，

$$
\frac12v_{\rm out}^2-\frac12v_{\rm in}^2
=\boldsymbol v_E\cdot
(\boldsymbol u_{\rm out}-\boldsymbol u_{\rm in}).
$$

能量差来自运动中的地球与探测器之间的引力交换；在完整的太阳—地球—探测器系统中，总能量仍然守恒。

## 六、关键洞察

用地球圆轨道关系 $\mu_\odot=v_E^2R_E$ 消去太阳引力参数。飞掠使地心相对速度转向并保持其大小；变回日心系后，由与地球速度的点积得到轨道能量变化。

## 七、易错点

1. 由 $T^2\propto r^3$ 误写成 $r\propto T^{3/2}$。
2. 把转移椭圆半长轴误取为 $R_J-R_E$。
3. 把近日点速度当成地球圆轨道速度。
4. 在日心系中直接认为弹弓前后速度大小不变；真正等大的是地心相对速度。
5. 将椭圆周期 $5.46\ \mathrm y$ 与单程飞行时间 $2.73\ \mathrm y$ 混淆。

## 八、课堂讲解建议

建议以“两个参考系、三条速度边”为主线讲引力弹弓。先让学生在图5-2中标出 $\boldsymbol v_E$、$\boldsymbol v_{\rm in}$、$\boldsymbol u_{\rm in}$，再写余弦定理。数值计算后要回到物理图像：$v_1>v_E$、$v_3<v_1$、单程时间是椭圆周期的一半。

## 九、变式训练

变式一：求转移椭圆远日点处的速度与木星圆轨道速度之比。木星圆轨道速度为

$$
v_J=v_E\sqrt{\frac{R_E}{R_J}}. \tag{30}
$$

由式（14）和式（24），

$$
v_3=v_E\sqrt{\frac{2R_J}{R_E+R_J}}\frac{R_E}{R_J}. \tag{31}
$$

两式相除：

$$
\frac{v_3}{v_J}
=\sqrt{\frac{2R_E}{R_E+R_J}}. \tag{32}
$$

数值为

$$
\boxed{\frac{v_3}{v_J}
=\sqrt{\frac{2}{1+5.20064}}
\approx0.568}. \tag{33}
$$

进一步设想不使用地球引力弹弓，而是在地球圆轨道处沿公转方向瞬时点火，直接进入同一条日心霍曼转移椭圆。求近日点点火速度增量、到达木星轨道处若要变为日心圆轨道所需的第二次速度增量，以及两次速度增量之和。

近日点点火前后的速度分别为 $v_E$、$v_1$，所以第一次速度增量为

$$
\Delta v_E=v_1-v_E. \tag{34}
$$

代入正文数值：

$$
\boxed{\Delta v_E
=38.707-29.886
\approx8.82\ \mathrm{km/s}}. \tag{35}
$$

这次点火造成的单位质量机械能增加为

$$
\Delta\varepsilon_E
=\frac12v_1^2-\frac12v_E^2. \tag{36}
$$

将 $v_1=v_E+\Delta v_E$ 代入：

$$
\Delta\varepsilon_E
=v_E\Delta v_E+\frac12(\Delta v_E)^2. \tag{37}
$$

数值为

$$
\Delta\varepsilon_E
\approx(29.886)(8.821)+\frac12(8.821)^2
\approx302.5\ \mathrm{km^2/s^2}. \tag{38}
$$

在木星轨道半径处，木星的日心圆轨道速度为

$$
v_J=v_E\sqrt{\frac{R_E}{R_J}}. \tag{39}
$$

代入 $R_J/R_E=5.20064$：

$$
v_J\approx13.10\ \mathrm{km/s}. \tag{40}
$$

转移椭圆远日点速度为

$$
v_3\approx7.44\ \mathrm{km/s}. \tag{41}
$$

若理想化地要求探测器在该处变为绕太阳的同向圆轨道，第二次点火必须加速：

$$
\Delta v_J=v_J-v_3. \tag{42}
$$

所以

$$
\boxed{\Delta v_J
\approx13.10-7.44
\approx5.66\ \mathrm{km/s}}. \tag{43}
$$

两次理想脉冲的总速度增量为

$$
\boxed{\Delta v_{\rm total}
=\Delta v_E+\Delta v_J
\approx14.48\ \mathrm{km/s}}. \tag{44}
$$

这里的第二次点火只是在日心两体模型中“圆化”到木星轨道，并不等同于被木星捕获。真实任务到达木星附近时必须转入木星中心参考系，处理木星相对速度、近木点制动和卫星系统摄动。这个变式的价值在于明确区分“霍曼转移到某一轨道半径”和“进入目标行星的绕行轨道”。

变式二：取木星周期为地球的 $11.86$ 倍，两轨道为同心圆。求霍曼转移时间，以及出发时木星相对地球应超前的角度。

解：轨道半径比 $q=11.86^{2/3}$，转移椭圆半长轴为 $a=R_E(1+q)/2$。由开普勒定律，飞行时间为半个转移周期：

$$
\frac{t_H}{T_E}=\frac12\left(\frac{1+q}{2}\right)^{3/2}\approx2.72948.
$$

飞船转过 $\pi$，木星同期转过 $2\pi t_H/T_J$。因此木星出发时需超前 $\phi=\pi-2\pi t_H/T_J\approx97.15^\circ$。相位必须按飞行时间计算，不能把地球与木星出发时放在同一径向线上。

变式三：忽略地球自转，地心相对速度在飞掠前后大小均为 $u$。地球日心速度为 $\boldsymbol v_E$。证明单位质量日心轨道能的变化，并求反向到同向的最大理论增量。

解：飞掠前后日心速度为 $\boldsymbol v_E+\boldsymbol u_{\rm in,out}$，位置变化在局部飞掠近似中忽略，因此势能差忽略。展开动能差并利用两相对速率相同，得

$$
\Delta\epsilon=\boldsymbol v_E\cdot(\boldsymbol u_{\rm out}-\boldsymbol u_{\rm in}).
$$

若可把入射的 $-u\hat{\boldsymbol v}_E$ 完全转为 $+u\hat{\boldsymbol v}_E$，有理论上限 $\Delta\epsilon_{\max}=2v_Eu$。实际转向角受最近距离限制，通常达不到这个 $180^\circ$ 上限。地心系无能量增益，日心系的轨道能却可增加。

变式四：地心双曲线飞掠取 $u_\infty=8.821\,\mathrm{km/s}$、最近地心距离 $r_p=7000\,\mathrm{km}$、地球引力参数 $\mu_E=398600\,\mathrm{km^3/s^2}$。求双曲线偏心率和可实现的转向角。

解：双曲线单位质量能为 $u_\infty^2/2$，半长轴绝对值为 $\mu_E/u_\infty^2$。最近距离关系 $r_p=|a_h|(e_h-1)$ 给

$$
e_h=1+\frac{r_pu_\infty^2}{\mu_E}\approx2.366,
\qquad \delta=2\arcsin\frac1{e_h}\approx50.0^\circ.
$$

这是该最近距离下的转向角。图示中的相对速度箭头必须等长，箭头夹角也应与所需轨道转向比较；只满足速度三角形还不保证地球引力能提供所需偏折。
