# 第7题

<!-- question-start -->

理想电容直接接到内阻可忽略、电压为$U$的电源上时，会迅速充电。充电完成后电容储能为$CU^2/2$，而电源做功为$CU^2$；其差额即使没有显式电阻，也可通过辐射等机制耗散。

图示电路的电源电动势为$\varepsilon$，两电阻均为$R$，三电容均为$C$。开始电容不带电。闭合开关后，电容先迅速充电，再缓慢达到最终平衡。

（1）求从合闸到电荷分布稳定，两电阻上产生的总热量。

（2）画出每个电阻两端电压与流过该电阻的电荷量之间的关系图；当电阻累计热量达到其最终值的一半时，求各电容电压。

规定下导线为零电势，上导线合闸后为$\varepsilon$。左中间节点为$A$、右中间节点为$B$。三电容分别记为$C_L$、$C_R$、$C_M$，位置见图。

![图7-1 两电阻、三电容构成的电桥及节点命名。](../figures/question-07.png){width=75%}

<!-- question-end -->

## 一、题型定位

本题的关键是把合闸过程分为两个时间尺度。最初的快速过程经三电容串联路径完成，电容并非等到电阻电流流过后才开始带电；随后两电阻驱动电荷重新分配，才产生题目所求的有限电阻热。

计算不能把初始条件设为$a(0)=b(0)=0$。若三个电容电压都为零，右电容要求$b=\varepsilon$，左电容要求$a=0$，中间电容又要求$a=b$，三者与合闸后的非零电源电压矛盾。

## 二、知识点

电容两极板的电荷由两端电势差决定。浮置节点在瞬时电容调整中总自由电荷守恒；有限电阻在零时间间隔内不能输送有限电荷。电阻缓慢过程满足节点电流守恒与
$$
dQ_R=u_R\,dq_R,\qquad
\frac{dQ_R}{dt}=Ri^2.
$$
电容电压可以正负变化，储能始终为$Cu^2/2$。求热量所用的电压—电荷图应画电阻自身的$u_R(q_R)$，其面积才是该电阻发热。

## 三、物理图像

快速阶段，忽略经过有限$R$输送的电荷，三个$C$形成从上导线到下导线的串联电容链。中间两个节点原净电荷为零，因而每个串联电容获得相同的电荷量$C\varepsilon/3$。

![图7-2 合闸瞬间的三电容串联路径与浮置节点电荷守恒。](../figures/initial-07.png){width=81%}

慢过程开始后，两电阻电流相等并逐渐衰减。节点$A$由$\varepsilon/3$升到$\varepsilon$，节点$B$由$2\varepsilon/3$降到零。中间电容的电压$a-b$从$-\varepsilon/3$变到$+\varepsilon$，会经过零并反向充电。

![图7-3 两节点的共同模式与差动模式；原题只激发差动衰减。](../figures/modes-07.png){width=84%}

## 四、解题入口

先由浮置节点净电荷得到$a(0^+),b(0^+)$。再列完整的两节点电容方程，通过和、差变量找到时间常数。由单个电阻的$i(t)$积分得到$q_R(t)$，消去时间获得$u_R(q_R)$，用三角形面积求热量。

最后将“累计热量一半”转成电压—电荷图上的面积条件，或转成指数平方条件。两种方法将得到相同的电容电压，并可用电源功与电容储能作第三条核验。

## 五、解析

（1）合闸瞬间，浮置节点的净电荷守恒。

设节点电势为$a,b$。节点$A$连接左电容上极板和中间电容左极板，其总电荷为
$$
Q_A=Ca+C(a-b)=C(2a-b).
$$
节点$B$连接右电容下极板和中间电容右极板，其总电荷为
$$
Q_B=C(b-\varepsilon)+C(b-a)
=C(2b-a-\varepsilon).
$$
在极短时间内，有限电阻输送的电荷趋零，两节点均保持初始净电荷零。因此
$$
2a_0-b_0=0,\qquad 2b_0-a_0-\varepsilon=0.
$$
解得
$$
\boxed{a_0=\frac{\varepsilon}{3},
\qquad b_0=\frac{2\varepsilon}{3}}.
$$
下标0表示快速阶段结束、慢过程开始的$0^+$状态。

（2）给出快速阶段的三个电容电压。

规定左电容电压$u_L=a$，右电容电压$u_R^{(C)}=\varepsilon-b$，中间电容有向电压$u_M=a-b$。则
$$
u_L(0^+)=u_R^{(C)}(0^+)=\frac{\varepsilon}{3},
\qquad u_M(0^+)=-\frac{\varepsilon}{3}.
$$
三者电压大小相等，但中间电容相对于约定方向为负。这一点决定其后是否发生电压反转。

三电容串联的等效电容为$C/3$，快速阶段后的储能为
$$
\boxed{W_{C,0}=3\times\frac12C
\left(\frac{\varepsilon}{3}\right)^2
=\frac{C\varepsilon^2}{6}}.
$$
源供电量为$C\varepsilon/3$，供能为$C\varepsilon^2/3$，二者差额$C\varepsilon^2/6$属于快速充电路径的耗散，不计入图中两个有限电阻的慢过程热量。

（3）写慢过程的节点电流方程。

左电阻从上导线向$A$供电，电流为
$$
i_L=\frac{\varepsilon-a}{R}.
$$
右电阻从$B$流向下导线，电流为
$$
i_R=\frac bR.
$$
由节点自由电荷的变化率，
$$
\boxed{
C(2\dot a-\dot b)=\frac{\varepsilon-a}{R}
},
$$
$$
\boxed{
C(2\dot b-\dot a)=-\frac bR
}.
$$
右节点的右边为负，因为电流离开节点$B$。电容电流包含中间电容的耦合项，不能各自把两个支路当作独立的单电容$RC$电路。

（4）将两节点方程相加，确定和变量。

令$s=a+b$，两式相加：
$$
C\dot s=\frac{\varepsilon-s}{R}.
$$
故
$$
s(t)=\varepsilon+(s_0-\varepsilon)e^{-t/(RC)}.
$$
原题$s_0=a_0+b_0=\varepsilon$，因此
$$
\boxed{a(t)+b(t)=\varepsilon}.
$$
这一恒等式说明两个电阻电流始终相等，而不是仅在最终状态相等。

（5）将两节点方程相减，确定差变量。

令$d=a-b$，第一式减第二式：
$$
3C\dot d=\frac{\varepsilon-d}{R}.
$$
原题$d_0=-\varepsilon/3$，所以
$$
d(t)=\varepsilon-\frac{4\varepsilon}{3}e^{-t/(3RC)}.
$$
定义
$$
\tau=3RC,\qquad z=e^{-t/\tau},
$$
则
$$
d=\varepsilon\left(1-\frac43z\right).
$$
时间常数是$3RC$而非$RC$，源于差动时中间电容两端电压变化为单节点变化的两倍。

（6）恢复节点电势及电容电压。

由$a=(s+d)/2,b=(s-d)/2$，
$$
\boxed{
a(t)=\varepsilon-\frac{2\varepsilon}{3}z,\qquad
b(t)=\frac{2\varepsilon}{3}z
}.
$$
因此
$$
\boxed{
u_L=u_R^{(C)}
=\varepsilon\left(1-\frac23z\right)
},
$$
$$
\boxed{
u_M=\varepsilon\left(1-\frac43z\right)
}.
$$
$t\to\infty$时三个电容的电压均为$\varepsilon$，总储能为$3C\varepsilon^2/2$。两个电阻电压则都趋零，不能与电容的最终电压混淆。

（7）求每个电阻的电流和通过电荷。

由$\varepsilon-a=b$，有
$$
i_L=i_R=i(t)=\frac{2\varepsilon}{3R}z.
$$
定义$q_R(t)$为慢过程开始后累计流过任一个电阻的电荷，不包括源在快速阶段经过纯电容路径提供的电荷。积分得
$$
\begin{aligned}
q_R(t)
&=\int_0^t i(t')\,dt'\\
&=\frac{2\varepsilon}{3R}\tau
(1-e^{-t/\tau})\\
&=2C\varepsilon(1-z).
\end{aligned}
$$
所以
$$
\boxed{q_{R,\infty}=2C\varepsilon}.
$$
左右电阻的通过电荷相等，但两者不是串联连接；这是原题对称初始条件下的动态结果。

（8）消去时间，给出电压—电荷图。

任一电阻沿电流方向的电压降为
$$
u_R^{(\text{阻})}=Ri
=\frac{2\varepsilon}{3}z.
$$
由$z=1-q_R/(2C\varepsilon)$，
$$
\boxed{
u_R^{(\text{阻})}
=\frac{2\varepsilon}{3}-\frac{q_R}{3C},
\quad 0\le q_R\le2C\varepsilon
}.
$$
图像为从$(0,2\varepsilon/3)$到$(2C\varepsilon,0)$的直线。横轴是通过某一个电阻的累计电荷，纵轴是该电阻电压；不能把两个电阻的电荷相加后仍使用同一条直线。

![图7-4 电阻电压对通过电荷的直线，面积给出热量。](../figures/charge-07.png){width=79%}

（9）由图像面积求最终电阻热量。

每个电阻的热量为
$$
Q_{R,\infty}
=\int_0^{2C\varepsilon}u_R^{(\text{阻})}\,dq_R
=\frac12(2C\varepsilon)
\left(\frac{2\varepsilon}{3}\right)
=\frac23C\varepsilon^2.
$$
两个电阻总热量为
$$
\boxed{Q_\infty=\frac43C\varepsilon^2}.
$$
也可直接积分功率：
$$
Q_\infty
=2R\int_0^\infty
\left(\frac{2\varepsilon}{3R}e^{-t/\tau}\right)^2dt
=\frac{8\varepsilon^2}{9R}\frac{\tau}{2}
=\frac43C\varepsilon^2.
$$
有限$R$改变耗散速度，不改变总热量。

（10）累计热量一半时，指数因子为多少？

累计总热量为
$$
\begin{aligned}
Q(t)
&=2R\int_0^t i(t')^2dt'\\
&=Q_\infty(1-e^{-2t/\tau})
=Q_\infty(1-z^2).
\end{aligned}
$$
令$Q(t_*)=Q_\infty/2$，
$$
z_*^2=\frac12,\qquad z_*=\frac1{\sqrt2}.
$$
因此
$$
\boxed{t_*=\frac{3RC}{2}\ln2}.
$$
这里电流衰减指数与热量剩余指数相差一倍；直接将电流降至一半当作半热量时刻，会得到错误时间。

（11）代入求三电容电压。

$$
\boxed{
u_L(t_*)=u_R^{(C)}(t_*)
=\varepsilon\left(1-\frac{\sqrt2}{3}\right)
},
$$
$$
\boxed{
u_M(t_*)=\varepsilon\left(1-\frac{2\sqrt2}{3}\right)
}.
$$
数值分别为
$$
u_L=u_R^{(C)}\simeq0.528595\,\varepsilon,\qquad
u_M\simeq0.057191\,\varepsilon.
$$
中间电容在这一时刻已经反向，但其电压仍很小。若只问电压大小，中间值就是上述正数；全过程中则应保留其有向电压。

![图7-5 电容电压随时间的变化，标出反向时刻和半热量时刻。](../figures/voltage-07.png){width=85%}

（12）用几何面积核验半热量状态。

图7-4中剩余热量是右侧未经过部分的三角形面积。相对于全三角形，其底边比和高比都为$z$，因此剩余面积比是$z^2$。

剩余面积一半要求$z=1/\sqrt2$，不是$1/2$。此时
$$
q_R(t_*)=2C\varepsilon
\left(1-\frac1{\sqrt2}\right),
$$
$$
u_R^{(\text{阻})}(t_*)
=\frac{\sqrt2}{3}\varepsilon.
$$
由$a=\varepsilon-u_R^{(\text{阻})}$、$b=u_R^{(\text{阻})}$，立即恢复第（11）步的电容电压。这条路线无需先求$t_*$。

（13）从慢过程电源功与储能变化核验总热量。

慢过程电源正端供电有两条路径：左电阻电流$i$，以及右电容上极板电荷增加率$-C\dot b$。所以源电流为
$$
i_{\text{源}}=i-C\dot b.
$$
积分得慢过程供电量
$$
q_{\text{源,慢}}
=2C\varepsilon+C(b_0-b_\infty)
=\frac83C\varepsilon.
$$
慢过程电源做功为
$$
W_{\text{源,慢}}=\frac83C\varepsilon^2.
$$
储能增加量为
$$
\Delta W_C=\frac32C\varepsilon^2-\frac16C\varepsilon^2
=\frac43C\varepsilon^2.
$$
于是
$$
W_{\text{源,慢}}-\Delta W_C
=\frac43C\varepsilon^2=Q_\infty.
$$
源电流与电阻电流不同，因此源供电量不能只取$2C\varepsilon$。

（14）核验任意中间时刻的能量收支。

令$z=e^{-t/\tau}$，三个电容总储能为
$$
\begin{aligned}
W_C(z)
&=\frac C2\left[2u_L^2+u_M^2\right]\\
&=C\varepsilon^2
\left(\frac32-\frac83z+\frac43z^2\right).
\end{aligned}
$$
慢过程电源截至此刻的供能为
$$
W_{\text{源,慢}}(z)
=\frac83C\varepsilon^2(1-z).
$$
相减得到
$$
W_{\text{源,慢}}(z)
-\bigl[W_C(z)-W_C(1)\bigr]
=\frac43C\varepsilon^2(1-z^2),
$$
正是$Q(t)$。此式同时核对初始条件、指数系数和热量系数。

（15）区分电阻热和全过程总耗散。

快速阶段电源做功$C\varepsilon^2/3$，慢过程做功$8C\varepsilon^2/3$，总电源做功为$3C\varepsilon^2$。最终储能为$3C\varepsilon^2/2$，全过程总耗散为
$$
Q_{\text{全耗散}}=\frac32C\varepsilon^2.
$$
分拆为
$$
\boxed{
\frac32C\varepsilon^2
=\frac16C\varepsilon^2+\frac43C\varepsilon^2
}.
$$
前一项来自题干说明的快速电容充电耗散，后一项才是两个有限电阻上的热。若用微小源内阻描述快速过程，令其趋零，快速热量仍有限，而两个$R$在该极短阶段的热量趋零。

## 六、关键洞察

电容耦合矩阵为
$$
\boldsymbol C=C
\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
$$
其共同模式$(1,1)$对应电容本征值$C$，差动模式$(1,-1)$对应$3C$。电导矩阵则是$(1/R)$乘单位矩阵，因此两个衰减时间分别为$RC$与$3RC$。

原题快速阶段恰好给出$s_0=\varepsilon$，共同模式已经位于最终值，只剩差动模式变化。这是两电阻电流相等、两外侧电容电压相等、单一指数出现的共同原因。

中间电容反向时$z=3/4$，有$t_{\text{反}}=\tau\ln(4/3)$。此时已产生的热量比例为
$$
1-\left(\frac34\right)^2=\frac7{16}<\frac12.
$$
因此反向发生在半热量时刻之前，图7-5与数值解相符。

## 七、易错点

将三电容初始电压仍设为零，会与非零电源阶跃不相容。应先用浮置节点电荷守恒求快速阶段的状态。

将两外侧电容各当作一个$RC$充电，漏掉中间电容耦合，会得到错误时间常数和电阻热量。

用“半热量”推出通过电荷一半，或推出电流一半，都把三角形面积与线性长度混淆。剩余热量与剩余电压平方成正比。

把全过程总耗散$3C\varepsilon^2/2$回答为有限电阻热，会混入快速充电路径的耗散。原题明确问电阻，答案是$4C\varepsilon^2/3$。

## 八、课堂讲解建议

课堂先遮住电阻，仅沿三电容串联路径确认快速初态。让学生在$A,B$两节点逐极板写出电荷，借此看清节点净电荷守恒与单个电容极板电荷变化的区别。

教师先保留两节点微分方程，再引导相加、相减。板书将$s$和$d$两条方程并列，随后代入初值说明为什么共同模式没有被激发，避免将对称性当成无条件成立的结论。

热量计算先用$u_R(q_R)$图像，后用时间积分。课堂讨论半热量时应使用哪块面积，并用电源功核验。快速耗散单列，强调源电流包含右电容极板的电荷变化，不能等同于任一电阻电流。

## 九、变式训练

<!-- KEEP_TOGETHER_START -->

变式1：三电容均变为$kC$，电阻不变。求总电阻热量、半热量时间与此时电压。

电荷与储能按$k$倍缩放，时间常数也按$k$倍缩放：
$$
Q_\infty'=\frac43kC\varepsilon^2,\qquad
t_*'=\frac{3RkC}{2}\ln2.
$$
半热量状态仍满足$z=1/\sqrt2$，故三电容电压与原题相同。改变容量改变电荷、能量和时间，不改变这一无量纲状态的电压比例。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式2：两电阻均变为$kR$，三电容不变。求最终电阻热与半热量时间。

电流初值降为原来的$1/k$，持续时间增为$k$倍，积分$Ri^2dt$不变：
$$
Q_\infty'=\frac43C\varepsilon^2,\qquad
t_*'=\frac{3kRC}{2}\ln2.
$$
这解释了电阻趋小时为何总电阻热不趋零；热量集中在更短时间内产生。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式3：求中间电容电压刚过零时，另外两电容电压、每电阻通过电荷及已产生的热量。

$u_M=0$要求$z=3/4$，于是
$$
u_L=u_R^{(C)}=\frac{\varepsilon}{2},
\qquad
q_R=2C\varepsilon\left(1-\frac34\right)
=\frac12C\varepsilon.
$$
此时
$$
Q=\frac7{16}Q_\infty
=\frac7{12}C\varepsilon^2,
\qquad t=\tau\ln\frac43.
$$
电压反向不对应热量的一半。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式4：不要求三个电容初始不带电。慢过程开始时两节点为$a_0,b_0$，求之后的节点电势。

记$s_0=a_0+b_0,d_0=a_0-b_0$，由两模式方程，
$$
s(t)=\varepsilon+(s_0-\varepsilon)e^{-t/(RC)},
$$
$$
d(t)=\varepsilon+(d_0-\varepsilon)e^{-t/(3RC)}.
$$
因此
$$
a(t)=\varepsilon+\frac12(s_0-\varepsilon)e^{-t/(RC)}
+\frac12(d_0-\varepsilon)e^{-t/(3RC)},
$$
$$
b(t)=\frac12(s_0-\varepsilon)e^{-t/(RC)}
-\frac12(d_0-\varepsilon)e^{-t/(3RC)}.
$$
一般初态含两个指数，两电阻电流不再相等。代入$a_0=\varepsilon/3,b_0=2\varepsilon/3$即还原原题。

<!-- KEEP_TOGETHER_END -->

<!-- question-complete -->
