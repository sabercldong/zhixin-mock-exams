# 第 4 题

水平面上放置两条电阻可忽略的平行光滑导轨，间距$l=0.2\,\mathrm m$，处于方向竖直向上、磁感应强度$B=0.5\,\mathrm T$的匀强磁场中。两导轨的一端接有电阻$R=0.5\,\Omega$。在远离电阻的一侧，垂直于导轨放置一根质量$m=0.1\,\mathrm{kg}$、电阻可忽略的导体棒。

导体棒具有朝电阻方向的初速度$v_0=2\,\mathrm{m\,s^{-1}}$。施加外力$F$，使它以加速度大小$a=2\,\mathrm{m\,s^{-2}}$作匀减速运动；导体棒与导轨之间无摩擦。

（1）求导体棒上电流为零时，导体棒相对初始位置的位移。

（2）求导体棒上电流减为初始值一半时，外力$F$的大小和方向。

（3）求在$0<t<T$的时间内外力$F$所做的功。

![图 4-1　水平导轨、运动导体棒、电阻与竖直向上磁场的空间关系。](../figures/question-04.png){width=79%}

## 一、题型定位

这是规定运动过程的导体棒电磁感应与动力学问题。运动并不是由未知外力自由决定，而是题目先规定$v(t)$必须匀减小，再要求反求实现该运动所需的外力。

导体棒运动产生电流，电流与磁场作用产生反向安培力。匀减速要求总水平力恒为$-ma$，但安培力随速度改变，所以外力一般不是恒力。求外力功时，不能直接用某一个时刻的$F$乘总位移。

忽略回路自感，导轨和导体棒的电阻均不计，全部焦耳热在电阻$R$上产生。题目第三问未给定$T$的数值，因此先保留任意终点$T$的通式；只有额外取$T=v_0/a$时，才代表减速至静止的全过程。

## 二、知识点

- 规定初速度方向为$x$正向，匀减速运动为$v=v_0-at$、$x=v_0t-at^2/2$。
- 导体棒的动生电动势大小为$\mathcal E=Blv$。
- 回路电流为$i=\mathcal E/R$，适用条件是自感可忽略、接触和回路始终完整。
- 安培力方向与运动方向相反，大小为$Bil$。
- 外力不是安培力，牛顿第二定律必须将两者相加。
- 外力功可以由$\int F\,dx$或$\int Fv\,dt$求得。
- 安培力的负功转化为焦耳热，因此外力功满足$W_F=\Delta K+Q_J$。

## 三、物理图像

规定$x$轴沿导轨指向电阻，$y$轴在导轨平面内由下轨指向上轨，$z$轴竖直向上。磁场为$\boldsymbol B=B\boldsymbol e_z$，初始速度为$v_0\boldsymbol e_x$。

在$v>0$阶段，$\boldsymbol v\times\boldsymbol B$指向$-y$，导体棒中正电荷被推向下轨，电流在棒中由上轨流向下轨。这个方向的电流与向上的磁场作用，产生指向$-x$的安培力。

当棒向电阻移动时，回路面积减小，向上的磁通量减小，感应电流应产生向上的磁场；俯视回路，电流为逆时针。这与导体棒中由上向下的方向一致，可作独立符号核对。

以下用$F_x$表示外力在$x$正向上的带符号分量。$F_x<0$表示外力朝远离电阻的方向，不应把负号误解释为力的大小为负。

## 四、解题入口

用速度作为连接运动、电流与力的中间变量：

$$
\begin{aligned}
v(t)&=v_0-at,\\
i(t)&=\frac{Bl}{R}v(t),\\
F_{\mathrm A,x}(t)&=-\frac{B^2l^2}{R}v(t),\\
F_x(t)+F_{\mathrm A,x}(t)&=-ma.
\end{aligned}
$$

第一问由$i=0$求$v=0$，再求时间与位移；第二问由$i=i_0/2$求$v=v_0/2$，再代入动力学；第三问将带符号$F_x(t)$与$v(t)$相乘并积分。

## 五、解析

（1）先写清匀减速过程的时间范围。

初始时刻取$t=0$、$x=0$。规定的加速度为

$$
\frac{dv}{dt}=-a.
$$

积分并用$v(0)=v_0$：

$$
v(t)=v_0-at.
\tag{1}
$$

再次积分并用$x(0)=0$：

$$
\begin{aligned}
x(t)
&=\int_0^t(v_0-a\tau)\,d\tau\\
&=v_0t-\frac12at^2.
\end{aligned}
\tag{2}
$$

“匀减速”在这里是沿原方向运动、速度大小减小，故主要研究区间为

$$
0\le t\le t_{\mathrm s},
\qquad
t_{\mathrm s}=\frac{v_0}{a}=1\,\mathrm s.
\tag{3}
$$

如果把同一个加速度继续作用到$t>t_{\mathrm s}$，导体棒将反向加速，已不是题目所描述的原方向匀减速阶段。

（2）由磁通变化求电流，并核对方向。

设电阻所在位置距棒初始位置为$d$，则回路面积为

$$
\mathcal A(t)=l[d-x(t)].
$$

取回路逆时针为正，对应法向为$+z$，磁通量为

$$
\Phi(t)=Bl[d-x(t)].
$$

法拉第定律给出

$$
\begin{aligned}
\mathcal E
&=-\frac{d\Phi}{dt}\\
&=-Bl\left(-\frac{dx}{dt}\right)\\
&=Blv.
\end{aligned}
\tag{4}
$$

由于$v>0$，$\mathcal E>0$，电流沿规定的逆时针方向。电流大小为

$$
\boxed{
i(t)=\frac{Bl}{R}(v_0-at)
}.
\tag{5}
$$

初始电流为

$$
\begin{aligned}
i_0
&=\frac{Blv_0}{R}\\
&=\frac{0.5\times0.2\times2}{0.5}\,\mathrm A\\
&=0.4\,\mathrm A.
\end{aligned}
\tag{6}
$$

图4-2的俯视回路标出了棒中的向下电流和两条向左的实际水平力。图中磁场用出纸面的符号表示，对应实际竖直向上的磁场，不应误画为向下。

![图 4-2　俯视回路的电流方向、反向安培力及实现匀减速所需的外力。](../figures/forces-04.png){width=77%}

（3）求电流为零时的位移。

在回路电阻有限、$B,l$非零且自感可忽略的条件下，由式（5）可知

$$
i=0\quad\Longleftrightarrow\quad v=0.
$$

故电流为零的时刻是$t_{\mathrm s}=v_0/a=1\,\mathrm s$。代入式（2）：

$$
\begin{aligned}
x_{\mathrm s}
&=v_0\frac{v_0}{a}
-\frac12a\left(\frac{v_0}{a}\right)^2\\
&=\frac{v_0^2}{a}-\frac{v_0^2}{2a}\\
&=\frac{v_0^2}{2a}\\
&=\frac{2^2}{2\times2}\,\mathrm m\\
&=\boxed{1\,\mathrm m}.
\end{aligned}
\tag{7}
$$

方向为初速度方向。用运动学关系$v^2=v_0^2-2ax$直接取$v=0$，也得到相同结果。

这里零电流不是因为磁场消失或导体棒断开，而是棒在该瞬间速度为零，动生电动势也为零。还须默认导轨足够长、初始棒到电阻的距离大于该位移，否则棒会先撞到电阻端部，题设运动无法继续。

（4）由安培力反求外力的带符号表达式。

导体棒中的电流方向是$-y$，所以

$$
\boldsymbol F_{\mathrm A}
=i(-l\boldsymbol e_y)\times(B\boldsymbol e_z)
=-Bil\,\boldsymbol e_x.
$$

将式（5）代入：

$$
F_{\mathrm A,x}
=-Bil
=-\frac{B^2l^2}{R}v.
\tag{8}
$$

为简化计算，定义磁阻尼系数

$$
\begin{aligned}
\kappa
&=\frac{B^2l^2}{R}\\
&=\frac{0.5^2\times0.2^2}{0.5}\\
&=0.02\,\mathrm{kg\,s^{-1}}.
\end{aligned}
\tag{9}
$$

牛顿第二定律的右端是规定的加速度$-a$：

$$
\begin{aligned}
F_x+F_{\mathrm A,x}&=m(-a),\\
F_x-\kappa v&=-ma,\\
\boxed{F_x=\kappa v-ma}.
\end{aligned}
\tag{10}
$$

这一步必须先把安培力的负号写入总力方程，再移项；不能把$F$直接写成$ma$或$Bil$。

代入$v=v_0-at$：

$$
\begin{aligned}
F_x(t)
&=\kappa(v_0-at)-ma\\
&=(0.02\times2-0.1\times2)\,\mathrm N
-(0.02\times2)\,\mathrm{N\,s^{-1}}\,t\\
&=-0.16\,\mathrm N
-(0.04\,\mathrm{N\,s^{-1}})t.
\end{aligned}
\tag{11}
$$

因此整个原方向减速区间内$F_x<0$，外力都向左。随着速度下降，安培制动力减小，为保持相同总减速度，外力的向左大小反而增大。

（5）求半电流时的外力。

式（5）说明电流与速度成正比，因此

$$
\frac{i}{i_0}=\frac{v}{v_0}.
$$

当$i=i_0/2$，

$$
v=\frac{v_0}{2}=1\,\mathrm{m\,s^{-1}}.
\tag{12}
$$

对应时刻与位移为

$$
\begin{aligned}
t_{1/2}
&=\frac{v_0-v_0/2}{a}
=\frac{v_0}{2a}
=0.5\,\mathrm s,\\
x_{1/2}
&=v_0t_{1/2}-\frac12at_{1/2}^2\\
&=2\times0.5-\frac12\times2\times0.5^2\\
&=0.75\,\mathrm m.
\end{aligned}
\tag{13}
$$

安培力分量为

$$
F_{\mathrm A,x}=-\kappa v=-0.02\,\mathrm N.
$$

实现总力$-ma=-0.20\,\mathrm N$还需

$$
\begin{aligned}
F_x
&=-0.20\,\mathrm N-(-0.02\,\mathrm N)\\
&=\boxed{-0.18\,\mathrm N}.
\end{aligned}
\tag{14}
$$

故外力大小为$\boxed{0.18\,\mathrm N}$，方向与初速度相反，即远离电阻。用直接的受力大小检查，两个向左的力相加为$0.18+0.02=0.20\,\mathrm N$，除以$0.1\,\mathrm{kg}$正好给出$2\,\mathrm{m\,s^{-2}}$的减速度。

（6）结合电流—位移关系复查两个时刻。

由$v^2=v_0^2-2ax$，在$v\ge0$的运动支路上取正根：

$$
v(x)=\sqrt{v_0^2-2ax}.
$$

因此

$$
\frac{i(x)}{i_0}
=\sqrt{1-\frac{x}{x_{\mathrm s}}},
\qquad
x_{\mathrm s}=\frac{v_0^2}{2a}.
\tag{15}
$$

图4-3展示电流随位移下降的曲线。半电流不对应半停止距离，而对应

$$
\frac14=1-\frac{x}{x_{\mathrm s}}
\quad\Rightarrow\quad
x=\frac34x_{\mathrm s}.
$$

![图 4-3　电流与位移的非线性关系及半电流、零电流位置。](../figures/current-04.png){width=67%}

这一检查还能排除用“电流随时间线性下降”就误判“随位移也线性下降”的错误。

（7）对外力瞬时功率逐项积分。

外力功取代数值：

$$
W_F(T)=\int_0^T F_x(t)v(t)\,dt.
\tag{16}
$$

将式（10）代入，先分成两类项：

$$
\begin{aligned}
W_F(T)
&=\int_0^T[\kappa(v_0-at)-ma](v_0-at)\,dt\\
&=\kappa\int_0^T(v_0-at)^2\,dt
-ma\int_0^T(v_0-at)\,dt.
\end{aligned}
\tag{17}
$$

第一类积分先展开平方：

$$
\begin{aligned}
\int_0^T(v_0-at)^2dt
&=\int_0^T(v_0^2-2v_0at+a^2t^2)dt\\
&=v_0^2T-v_0aT^2+\frac13a^2T^3.
\end{aligned}
\tag{18}
$$

第二类积分为位移：

$$
\int_0^T(v_0-at)dt=v_0T-\frac12aT^2.
\tag{19}
$$

所以任意终点$0\le T\le v_0/a$对应

$$
\boxed{
W_F(T)=
\kappa\left(v_0^2T-v_0aT^2+\frac{a^2T^3}{3}\right)
-ma\left(v_0T-\frac{aT^2}{2}\right)
}.
\tag{20}
$$

第三问没有给出具体$T$，式（20）就是保留终点时间的答案。若定义无量纲时间$\tau=T/(1\,\mathrm s)$，代入本题数值可写为

$$
\boxed{
W_F(T)=
\left(-0.32\tau+0.12\tau^2+\frac{2}{75}\tau^3\right)\mathrm J
},\qquad 0\le\tau\le1.
\tag{21}
$$

引入$\tau$后数值多项式的系数都乘同一焦耳单位，避免把带量纲的$T$直接塞进“无单位的小数系数”而使各项单位不一致。

图4-4展示了规定的速度、逐渐增强的反向外力及总功随时间变化。外力和速度反向，所以外力功始终非正；停止瞬间速度为零，瞬时功率为零，但已经积累的负功并不消失。

![图 4-4　匀减速过程中速度、外力分量与累计外力功的时间变化。](../figures/timework-04.png){width=84%}

（8）用动能和焦耳热独立验证功的表达式。

电阻的焦耳热为

$$
\begin{aligned}
Q_J(T)
&=\int_0^T i^2R\,dt\\
&=\int_0^T
\left(\frac{Bl}{R}v\right)^2R\,dt\\
&=\kappa\int_0^T v^2\,dt\\
&=\kappa\left(v_0^2T-v_0aT^2+\frac13a^2T^3\right).
\end{aligned}
\tag{22}
$$

安培力做功为

$$
W_{\mathrm A}=\int_0^T(-\kappa v)v\,dt=-Q_J.
$$

对导体棒使用动能定理：

$$
\Delta K=W_F+W_{\mathrm A}=W_F-Q_J.
$$

故

$$
\begin{aligned}
W_F
&=\Delta K+Q_J\\
&=\frac12m(v_0-aT)^2-\frac12mv_0^2\\
&\quad+\kappa\left(v_0^2T-v_0aT^2+\frac13a^2T^3\right).
\end{aligned}
\tag{23}
$$

展开动能变化：

$$
\begin{aligned}
\Delta K
&=\frac12m(v_0^2-2v_0aT+a^2T^2-v_0^2)\\
&=-mv_0aT+\frac12ma^2T^2\\
&=-ma\left(v_0T-\frac12aT^2\right),
\end{aligned}
$$

恰好恢复式（20）。焦耳热虽然为正，却不是外力必做正功的理由；棒原有动能也可以同时向电阻和外力作用系统输出能量。

（9）若终点取停止时刻，给出完整数值核验。

只有额外令$T=t_{\mathrm s}=1\,\mathrm s$，才得到减速至静止的总功。初始动能为

$$
K_0=\frac12mv_0^2
=\frac12\times0.1\times2^2
=0.2\,\mathrm J.
$$

停止前焦耳热为

$$
\begin{aligned}
Q_J(t_{\mathrm s})
&=\frac{\kappa v_0^3}{3a}\\
&=\frac{0.02\times2^3}{3\times2}\\
&=\frac2{75}\,\mathrm J
\approx0.0267\,\mathrm J.
\end{aligned}
\tag{24}
$$

因此

$$
\begin{aligned}
W_F(t_{\mathrm s})
&=-0.2+\frac2{75}\,\mathrm J\\
&=-\frac{15}{75}+\frac2{75}\,\mathrm J\\
&=\boxed{-\frac{13}{75}\,\mathrm J
\approx-0.1733\,\mathrm J}.
\end{aligned}
\tag{25}
$$

能量收支为：棒损失$0.2\,\mathrm J$动能，其中$0.0267\,\mathrm J$成为焦耳热，其余$0.1733\,\mathrm J$通过反向外力被取走。把外力功误写成$-\Delta K+Q_J$会破坏这一收支。

（10）从位置积分再检查功，并判断力的方向边界。

以位置为变量，有

$$
F_x(x)=\kappa\sqrt{v_0^2-2ax}-ma.
$$

对$0\le x\le x_{\mathrm s}$积分，令$u=v_0^2-2ax$、$dx=-du/(2a)$：

$$
\begin{aligned}
W_F(x)
&=-max+\kappa\int_0^x\sqrt{v_0^2-2a\xi}\,d\xi\\
&=-max+\frac{\kappa}{3a}
\left[v_0^3-(v_0^2-2ax)^{3/2}\right].
\end{aligned}
\tag{26}
$$

将$x=v_0T-aT^2/2$代入，根号的正支为$v_0-aT$，再次恢复式（20）。这一变量代换检验了平方根的支路和积分前后的符号。

由式（10），外力方向的临界速度为

$$
v_*=\frac{ma}{\kappa}=10\,\mathrm{m\,s^{-1}}.
$$

本题$v$始终在$0$到$2\,\mathrm{m\,s^{-1}}$之间，故总有$v<v_*$、$F_x<0$。在另一组参数中，即使物体在减速，也可能因磁阻尼足够强而需要一个向前外力；“减速”只限定总力方向，不单独限定每一个力。

## 六、关键洞察

规定运动反求外力与撤去外力后的自然运动不同。这里加速度被保持为$-a$，所以需要主动调节$F_x=\kappa v-ma$。若外力恒定为某个值，则速度一般不能继续严格线性下降。

电磁能量转化可在瞬时层面直接检验：

$$
P_J=i^2R=\kappa v^2,\qquad
P_{\mathrm A}=F_{\mathrm A,x}v=-\kappa v^2.
$$

两者恰好相反。动力学式再乘以$v$：

$$
F_xv-\kappa v^2=m\frac{dv}{dt}v
=\frac{d}{dt}\left(\frac12mv^2\right).
$$

移项即得$P_F=dK/dt+P_J$。这个关系不依赖先把时间积分做完，可用来逐时检查数值计算和受力符号。

在$v=0$瞬间，电流、安培力、焦耳功率和外力功率都为零，但为了继续维持指定加速度，外力仍为$-ma$。因此“功率为零”与“力为零”是不同的判断。

## 七、易错点

- 将竖直向上的磁场误画为入纸面，进而把电流方向反转。
- 把外力当作唯一水平力，直接取$F=ma$。
- 给安培力正确的大小却漏写负方向，使外力大小变为$0.22\,\mathrm N$。
- 半电流时用半位移代替半速度，错误地得到$x=0.5\,\mathrm m$。
- 外力随时间变动却使用单个时刻的力乘总位移。
- 把第三问未指定的终点$T$自动当作停止时刻，只报一个数值而不报通式。
- 在$v^2=v_0^2-2ax$中选负根，混入停止以后的反向运动。
- 认为有焦耳热就必须有正外力功，忽略初始动能提供的能量。

## 八、课堂讲解建议

先让学生通过$\boldsymbol v\times\boldsymbol B$和楞次定律分别判断电流方向，再让学生在同一受力图上画安培力。教师要求写带符号分量式$F_x-\kappa v=-ma$，不要只写力的大小。

半电流问题可先问“电流与哪一个运动量成正比”，再用$x=3x_{\mathrm s}/4$检验学生是否区分时间、速度与位移。板书第三问时保留积分上限$T$，明确停止时刻只是其中一个特例。

功的计算先做$\int Fv\,dt$，再让学生用动能和焦耳热独立核对。停止全过程的三个数值$0.2\,\mathrm J$、$0.0267\,\mathrm J$、$0.1733\,\mathrm J$可以用作能量流向检查，而非只记住外力功的负号。

## 九、变式训练

变式一：在同一装置中撤去外力，导体棒只受磁阻尼，初速度仍为$v_0$。求$v(t)$、$x(t)$、电流减半的时刻、最终位移和总焦耳热。

动力学方程为

$$
m\frac{dv}{dt}=-\kappa v.
$$

分离变量并用$v(0)=v_0$：

$$
\begin{aligned}
\int_{v_0}^{v}\frac{du}{u}
&=-\frac{\kappa}{m}\int_0^t d\tau,\\
\ln\frac v{v_0}&=-\frac{\kappa t}{m},\\
\boxed{v(t)=v_0e^{-\kappa t/m}}.
\end{aligned}
$$

积分位移：

$$
\boxed{
x(t)=\frac{mv_0}{\kappa}
\left(1-e^{-\kappa t/m}\right)
}.
$$

电流也按同一指数下降，半电流时间为

$$
t_{1/2}=\frac m\kappa\ln2=5\ln2\,\mathrm s\approx3.47\,\mathrm s.
$$

当$t\to\infty$，

$$
x_\infty=\frac{mv_0}{\kappa}=10\,\mathrm m.
$$

速度只渐近趋于零，不存在有限时刻的严格零电流。若导轨足够长，总焦耳热为

$$
\begin{aligned}
Q_{J,\infty}
&=\kappa v_0^2\int_0^\infty e^{-2\kappa t/m}dt\\
&=\kappa v_0^2\frac m{2\kappa}\\
&=\boxed{\frac12mv_0^2=0.2\,\mathrm J}.
\end{aligned}
$$

它与主问题在$1\,\mathrm s$内人为匀减速停止不同：自然磁制动的停止更慢、距离更长，且全部初始动能最终转为焦耳热，没有外力取走能量。该对比同时检验了“匀减速”和“力与速度成正比的阻尼”不是同一种运动。

变式二：在同一磁阻尼装置中改施恒定水平拉力 $F_0>0$，棒从静止起动。求速度、位移和达到终端速度一半所需时间。记 $\kappa=B^2l^2/R$。

解：方程 $m\dot v=F_0-\kappa v$ 的稳定解为 $v_\infty=F_0/\kappa$。用初值消去齐次解常数，得

$$
v=v_\infty(1-e^{-\kappa t/m}),\quad
x=v_\infty\left[t-\frac m\kappa(1-e^{-\kappa t/m})\right].
$$

令 $v=v_\infty/2$，有 $t_{1/2}=m\ln2/\kappa$。拉力功等于动能增加与焦耳热之和；终端阶段拉力全部用于补偿磁阻尼。

变式三：棒仍以恒定减速度 $a$ 从 $v_0$ 减速，问电流降为初值的任意比例 $\zeta\in(0,1)$ 时，时间、位移及外力功各为多少。

解：$I=Blv/R$，所以该时刻 $v=\zeta v_0$。运动学给

$$
t_\zeta=\frac{(1-\zeta)v_0}{a},\quad x_\zeta=\frac{v_0^2(1-\zeta^2)}{2a}.
$$

外力为 $F=-ma+\kappa v$。将功写成 $\int Fv\,dt$，用 $dt=-dv/a$ 积分，得到 $W_F=m v_0^2(\zeta^2-1)/2+\kappa v_0^3(1-\zeta^3)/(3a)$。第一项是动能减少，第二项正是焦耳热，符号据二者大小决定。

变式四：要求整个恒减速过程中的外力始终不向前，求减速度 $a$ 的下界。若采用临界值，求停车距离和外力总功。

解：$F(v)=-ma+\kappa v$ 随 $v$ 增大，最大值在初态。故 $F\le0$ 的充要条件为 $a\ge\kappa v_0/m$。临界值时 $t_s=m/\kappa$、$x_s=mv_0/(2\kappa)$。磁热为 $\kappa\int_0^{t_s}v^2dt=mv_0^2/3$，由能量关系

$$
W_F=-\frac12mv_0^2+\frac13mv_0^2=-\frac16mv_0^2.
$$

用原数据 $\kappa=0.02\,\mathrm{kg/s}$，得到 $a=0.4\,\mathrm{m/s^2}$、$x_s=5\,\mathrm m$、$W_F=-1/15\,\mathrm J$。
