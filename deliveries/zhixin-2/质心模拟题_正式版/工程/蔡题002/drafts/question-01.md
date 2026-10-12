# 第1题

<!-- question-start -->

如图1-1，电路中有电容$C$、电感$L$和两个电动势均为$\varepsilon_0$的电池。二极管均为理想二极管：正向导通时压降为零，反向加电压时电流为零。初始电容电压为$U_0$，规定左极板为正；初始电流为零，规定电感中从左向右流动的电流$I$为正。

（1）对于$U_0=4\varepsilon_0$，以$I$为横轴、$U$为纵轴，画出系统随时间变化的轨迹。

（2）求系统稳定后电容电压$U_1$随初始电压$U_0$的变化关系。

![图1-1 电流的正方向与电容电压的正方向沿用题设。](../figures/question-01.png){width=78%}

<!-- question-end -->

## 一、题型定位

这是由理想二极管控制的分段LC运动。每一段导通状态中，电感和电容仍遵循线性微分方程，但电池在两个电流方向上都吸收能量，方程的常数项随电流方向改变。电流第一次变成零时，必须重新判断哪条支路能导通；不能把同一条正弦曲线一直延长。

本题的“稳定”是电流最终为零、二极管阻止电流继续启动的静止状态。电容终态电压可以不为零。满足静止的电压形成一个区间，而不是唯一一个点，这正是最终电压呈三角折线的原因。

题设规定左极板电势较高时$U>0$，但电感的正电流向右。按原电路连接，正电流流入电容左极板所在的节点，因此$C\dot U=I$。初始正电压放电时$I$实际为负。相图左右半平面的选择必须由这个符号关系决定。

## 二、知识点

令电容左极板及下方导线的电势为零，电容右极板电势就是$-U$。电感左端连接该右极板，右端连接$a$点。两支路的二极管和电池共同给出$a,b$端口的特性：有正电流时$V_a-V_b=\varepsilon_0$，有负电流时$V_a-V_b=-\varepsilon_0$；零电流时，端口电压可以处于$[-\varepsilon_0,\varepsilon_0]$而保持截止。

导通时由电感电压关系得

$$
C\dot U=I,\qquad
L\dot I=-U-\varepsilon_0\operatorname{sgn}I.
$$

第二式只用于$I\ne0$的导通段。在$I=0$处应使用支路导通判据，不能把$\operatorname{sgn}0=0$代入后误判所有非零电压都会启动。

设$\omega=1/\sqrt{LC}$、$u=U/\varepsilon_0$、$j=I\sqrt{L/C}/\varepsilon_0$、$\tau=\omega t$，则

$$
\frac{du}{d\tau}=j,\qquad
\frac{dj}{d\tau}=-u-\operatorname{sgn}j.
$$

物理相图以$I,U$为坐标时是椭圆；采用$j,u$后变成圆。两种图形描述同一条轨迹，横轴的电流单位已经包含$\sqrt{C/L}$，不可直接用电压单位标电流。

## 三、物理图像

图1-2画出零电流状态的判据。当$u>1$时，只有负电流可以启动；当$u<-1$时，只有正电流可以启动；当$|u|\le1$时，系统保持$I=0$。

![图1-2 零电流时的启动方向和静止区间。](../figures/switch-01.png){width=82%}

导通后，电池电压把LC相圆的中心平移。$j<0$的圆心在$(j,u)=(0,1)$，$j>0$的圆心在$(0,-1)$。两者都不以原点为圆心。系统先在左半平面走半圈，再在右半平面走半圈，是否还有下一段取决于端点是否落入静止区间。

![图1-3 $U_0=4\varepsilon_0$时的两段有向相轨迹，箭头标出时间方向。](../figures/phase-01.png){width=74%}

图中第一段从$(0,4)$到$(0,-2)$，第二段从$(0,-2)$到$(0,0)$。到原点后停止；两条圆不能补成完整闭合圆。圆心和静止端点必须分开标注，圆心一般不是该段实际终态。

## 四、解题入口

先分析电流为零时能否启动，再在每个电流符号固定的阶段解方程。第一问只需两段半周期；第二问把“一个转折电压如何映射到下一个转折电压”作为递推规则，再确定何时递推终止。

分段计算有三个连续条件：电容电压不能突变，电感电流不能突变，每段起点与终点的电流都是零。二极管状态可以在零电流转折处改变，电压导数随电流连续归零，而电流导数通常会改变。

## 五、解析

（1）推导负电流段的相轨迹。

负电流时，电池端口电压为$-\varepsilon_0$。由方程

$$
L\dot I=-U+\varepsilon_0,
$$

两边乘$I$，并用$I=C\dot U$，有

$$
LI\dot I+C(U-\varepsilon_0)\dot U=0.
$$

因此该段守恒的是移位后的二次式：

$$
\boxed{\frac12LI^2+\frac12C(U-\varepsilon_0)^2=\text{常数}}.
$$

这不表示实际电磁能量守恒。常数式中含线性项$-C\varepsilon_0U$，它记入了电池的能量交换。真实电磁能$CU^2/2+LI^2/2$会减少。

（2）代入第一段初值。

取$U(0)=4\varepsilon_0$、$I(0)=0$，得到

$$
LI^2+C(U-\varepsilon_0)^2=9C\varepsilon_0^2,
$$

即无量纲圆方程

$$
\boxed{j^2+(u-1)^2=9,\qquad j\le0}.
$$

完整参数解为

$$
\begin{aligned}
U(t)&=\varepsilon_0+3\varepsilon_0\cos\omega t,\\
I(t)&=-3\varepsilon_0\sqrt{\frac CL}\sin\omega t,
\qquad 0\le t\le\frac\pi\omega.
\end{aligned}
$$

起点处$\dot I=-3\varepsilon_0/L<0$，说明轨迹确实进入左半平面。到$t=\pi/(2\omega)$时，$U=\varepsilon_0$，电流为最小值$-3\varepsilon_0\sqrt{C/L}$；到$t=\pi/\omega$时，$I=0$且$U=-2\varepsilon_0$。

（3）判断第一转折处是否停止。

$-2\varepsilon_0$在静止区间之外，负电压仍有足够幅度推动正电流。因此此处不是稳定终态，而是切换到另一支路。此时电感右端端口电压变为$+\varepsilon_0$，方程相应成为

$$
L\dot I=-U-\varepsilon_0.
$$

在$U=-2\varepsilon_0$处，新段初始$\dot I=+\varepsilon_0/L>0$，与进入右半平面一致。

（4）求第二段完整轨迹。

令$t'=t-\pi/\omega$，以$U=-2\varepsilon_0,I=0$为新初值。正电流段相椭圆为

$$
LI^2+C(U+\varepsilon_0)^2=C\varepsilon_0^2,
$$

即

$$
\boxed{j^2+(u+1)^2=1,\qquad j\ge0}.
$$

参数解为

$$
\begin{aligned}
U(t)&=-\varepsilon_0-\varepsilon_0\cos\omega t',\\
I(t)&=\varepsilon_0\sqrt{\frac CL}\sin\omega t',
\qquad0\le t'\le\frac\pi\omega.
\end{aligned}
$$

到$t'=\pi/\omega$时，$U=0,I=0$。端点落入静止区间，二极管截止，之后不再振荡。于是第一问的停止时间为

$$
\boxed{t_s=2\pi\sqrt{LC},\qquad U_1=0}.
$$

（5）把相图与时间波形对应起来。

图1-4采用同一无量纲时间轴，横轴的$\pi$和$2\pi$对应两个转折。电压第一段从4下降至$-2$，第二段从$-2$升至0；电流第一段为负半正弦，第二段为正半正弦，两段幅值相差三倍。

![图1-4 电压、电流的两段时间波形，$2\pi$之后保持静止。](../figures/time-01.png){width=88%}

每段长度相同来自相同的$LC$，幅值缩小来自电池吸收能量。不能以“幅值三倍”推断第一段历时也三倍，也不能把两个半正弦画成幅值相同的阻尼正弦。

（6）推广一个零电流转折的映射。

假设某段起点电压为$A>\varepsilon_0$。负电流段圆心在$\varepsilon_0$，半周期前后电压关于圆心对称，因此下一个零电流电压为

$$
\boxed{A'=2\varepsilon_0-A}.
$$

若$A<-\varepsilon_0$，正电流段圆心在$-\varepsilon_0$，同理

$$
\boxed{A'=-2\varepsilon_0-A}.
$$

合写为$A'=2\varepsilon_0\operatorname{sgn}A-A$，前提是$|A|>\varepsilon_0$。每一步都从零电流出发，不能把它用于半周期中间的任意状态。

（7）求小初始电压的终态。

对$0\le U_0\le\varepsilon_0$，系统始终不启动，$U_1=U_0$。对$\varepsilon_0<U_0\le3\varepsilon_0$，一次映射即可进入静止区间，因此

$$
U_1=2\varepsilon_0-U_0.
$$

对$3\varepsilon_0<U_0\le5\varepsilon_0$，第一次端点仍低于$-\varepsilon_0$，需要第二段。两次映射给

$$
U_1=-2\varepsilon_0-(2\varepsilon_0-U_0)
=U_0-4\varepsilon_0.
$$

各区间交界处的表达式一致，例如$U_0=3\varepsilon_0$给$U_1=-\varepsilon_0$。该点一次半周期就停止，不能因两式都能代入而多算一次运动。

（8）写出任意初始电压的统一关系。

两个连续半周期使初始转折幅值减少$4\varepsilon_0$，最终结果对$U_0$以$4\varepsilon_0$为周期。负初值由电路的正负对称性得到$U_1(-U_0)=-U_1(U_0)$。图1-5即为完整三角折线。

![图1-5 终态电压是周期为4$\varepsilon_0$、幅值为$\varepsilon_0$的三角折线。](../figures/map-01.png){width=87%}

一种紧凑写法为

$$
\boxed{U_1=\frac{2\varepsilon_0}{\pi}
\arcsin\!\left[\sin\!\left(\frac{\pi U_0}{2\varepsilon_0}\right)\right]},
$$

其中反正弦取$[-\pi/2,\pi/2]$主值。若希望避免反三角函数的分支理解，对非负初值可令

$$
k=\left\lceil\frac{U_0/\varepsilon_0-1}{2}\right\rceil
\quad(U_0>\varepsilon_0),
$$

则经过$k$个半周期停止，并有

$$
\boxed{\frac{U_1}{\varepsilon_0}=(-1)^k
\left(\frac{U_0}{\varepsilon_0}-2k\right)}.
$$

对负初值先使用其绝对值求结果再取反；对$|U_0|\le\varepsilon_0$，取$k=0$。最终$|U_1|\le\varepsilon_0$，而停止时间为$k\pi\sqrt{LC}$。

（9）用电磁能与电池功检验。

直接对真实能量求导，

$$
\begin{aligned}
\frac{d}{dt}\left(\frac12CU^2+\frac12LI^2\right)
&=UI+I(-U-\varepsilon_0\operatorname{sgn}I)\\
&=-\varepsilon_0|I|\le0.
\end{aligned}
$$

电池吸收的总能量为

$$
\boxed{W_{\rm bat}=\varepsilon_0\int_0^{t_s}|I|dt
=\frac C2(U_0^2-U_1^2)}.
$$

理想二极管压降为零，不能把这个能量一概称为二极管发热。对于第一问，两段通过的电荷量分别为$6C\varepsilon_0$和$2C\varepsilon_0$，电池总吸收$8C\varepsilon_0^2$，恰等于初始电场能。

（10）检验静止边界与极限。

在$U_0=\pm\varepsilon_0$时，电流初始加速度为零，可以保持静止；在边界稍外侧才发生一次完整的半周期。因而$U_1(U_0)$连续，而停止时间在这些阈值处可以跳变。这并不矛盾：有限半周期内的电流幅值可以趋于零。

当$\varepsilon_0>0$而初值有限时，运动总在有限次切换后停止。当$\varepsilon_0=0$时，电池吸能机制消失，成为理想LC的持续振荡；不能把终态三角公式中的$\varepsilon_0$直接置零来描述这一运动。

## 六、关键洞察

静止条件和运动方程是两个不同层次。运动阶段的二极管具有固定端口电压，静止阶段的端口电压则可以在一定范围内变化。正是这个区间使许多终态电压都合法。

半周期映射由相圆中心决定，周期由$LC$决定，终态由映射的停止条件决定。把三者分开，才能同时解释时间波形、相图和输入输出折线。

这里的电池作用与恒大小、反向于速度的阻力在数学上相似。类比有助于识别分段简谐结构，但能量的实际去向是电池吸收，不能借类比把电池替换成电阻。

## 七、易错点

电流初始方向最易画反。题图的正电流从电容右极板经电感流出，正电流使左极板的正电荷增加；故$C\dot U=I$，正初始电压的第一段位于相图左半平面。

不能把负电流段的圆心也放在$-\varepsilon_0$。圆心由$L\dot I=-U+\varepsilon_0$确定，应在$+\varepsilon_0$。第二段才以$-\varepsilon_0$为中心。

只要转折电压落入静止区间就必须终止递推。继续延长第二段到负电流，会违反二极管导通条件。终态为零只适用于若干特定初值，例如$U_0=2n\varepsilon_0$，不适用于所有初值。

## 八、课堂讲解建议

课堂先从图1-1指定一个正电流，判断电容哪块极板的电荷增加，再写$C\dot U=I$。让学生据初始$\dot I$决定相轨迹左右半平面，这比直接提供相圆更能暴露符号错误。

板书先保留两段的圆心、半径和起终点，再加入时间参数。教师先问$U=-2\varepsilon_0,I=0$能否停止，随后比较$U=-\varepsilon_0,I=0$，突出零电流不等于稳定。

最后让学生用$U_0=0.5\varepsilon_0,2\varepsilon_0,3.5\varepsilon_0,6\varepsilon_0$逐个构造终态，连接成图1-5，再归纳周期式。反三角函数表达式放在分段关系之后。

## 九、变式训练

<!-- KEEP_TOGETHER_START -->

变式一：初始电压为$6\varepsilon_0$，求全部零电流转折电压、停止时间及最大电流。

解：递推依次为$6\varepsilon_0\to-4\varepsilon_0\to2\varepsilon_0\to0$，前三个起点均在静止区间外，末点在区间内。故有三个半周期，$t_s=3\pi\sqrt{LC}$。第一段半径$5\varepsilon_0$最大，因此$\max|I|=5\varepsilon_0\sqrt{C/L}$，第一峰为负。电池吸能$18C\varepsilon_0^2$，与初始能量一致。

变式二：$U_0=-3.6\varepsilon_0$，求$U_1$及两段电池吸能。

解：第一段正电流，转折为$1.6\varepsilon_0$；第二段负电流，转折为$0.4\varepsilon_0$，停止。因此$U_1=0.4\varepsilon_0$。两段绝对电荷量为$5.2C\varepsilon_0$和$1.2C\varepsilon_0$，吸能分别为$5.2C\varepsilon_0^2$和$1.2C\varepsilon_0^2$。总量$6.4C\varepsilon_0^2=C(3.6^2-0.4^2)\varepsilon_0^2/2$。

变式三：保持$U_0=4\varepsilon_0$和$C$不变，将电感增大到$9L$。相图和终态如何改变？

解：半周期增至原来的三倍，停止时间为$6\pi\sqrt{LC}$。电流幅值均缩至原来的三分之一，第一段峰值为$-\varepsilon_0\sqrt{C/L}$，第二段为$\varepsilon_0\sqrt{C/L}/3$。电压转折仍为$4,-2,0$倍$\varepsilon_0$，终态仍为零；在实际$I,U$图中椭圆变窄，在归一化$j,u$图中轨迹不变。吸收能量也不变。

变式四：两方向的电池电压改为$\varepsilon_+>0$和$\varepsilon_->0$，正电流端口电压为$\varepsilon_+$，负电流为$-\varepsilon_-$。求静止区间及$U_0=4\varepsilon,\varepsilon_+=2\varepsilon,\varepsilon_-=\varepsilon$的终态。

解：正电流启动要求$U<-\varepsilon_+$，负电流启动要求$U>\varepsilon_-$，故静止区间为$[-\varepsilon_+,\varepsilon_-]$。负段转折$A'=2\varepsilon_--A$，正段转折$A'=-2\varepsilon_+-A$。指定初值先从$4\varepsilon$到$-2\varepsilon$，恰好抵达新区间左端，故只经历一个半周期即停止，$U_1=-2\varepsilon$。电池吸能$\varepsilon\,C(4\varepsilon+2\varepsilon)=6C\varepsilon^2$，等于电磁能减少。原对称三角公式不再直接适用。

<!-- KEEP_TOGETHER_END -->

<!-- question-complete -->
