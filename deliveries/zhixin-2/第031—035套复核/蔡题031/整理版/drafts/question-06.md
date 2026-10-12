# 第 6 题

实验基地中有一种信号火箭，以速率$v$飞行，信号发生器发出固定频率$f_0$的声音信号。基地处声速为$c=330\,\mathrm{m\,s^{-1}}$。按题设忽略声音的绝对传播时间对轨迹相位定位的影响。

（1）火箭沿直线朝静止接收器飞来时，接收器收到的声音频率是多少？

（2）火箭距离接收器较远，飞行方向与从火箭指向接收器的连线方向夹角为$\varphi$时，接收频率是多少？

（3）火箭在较低高度以相同速率$v$沿半径$r$的圆周飞行。两台静止接收器记录到的频率—时间关系如图，求两接收器之间的距离。

![图 6-1　两台接收器的周期频率曲线；曲线标号与接收器标号对应。](../figures/question-06.png){width=92%}

## 一、题型定位

这是运动声源的多普勒效应和周期轨迹反演。频率并不直接给出声源与接收器的距离，而是给出声源速度在指向接收器方向上的投影；极值发生的时刻又给出圆周位置的几何约束。

第三问需要同时使用三个独立信息：曲线的极值幅度确定速率，周期确定轨道半径，极值之间的时间间隔和两曲线的相位差确定接收器位置。只读出周期和速率，还不足以求两台接收器的距离。

这里采用静止空气、静止接收器和经典声学多普勒公式。不把声速$c$当作真空光速，也不引入相对论时间膨胀。图上读数有限，最终距离应报告近似数值，而不是许多位小数的“精确实测值”。

## 二、知识点

- 运动声源朝接收器运动时，相邻波前的间距缩小，接收频率增大。
- 进入公式的是朝向接收器的速度分量$u=v\cos\varphi$，而不是始终取总速率$v$。
- 静止接收器的频率为$f=f_0c/(c-u)$。
- 圆周运动满足$v=\omega r$、$\omega=2\pi/T$。
- 外部接收器的最大视线速度可等于$v$；内部接收器的最大视线速度小于$v$。
- 极值条件必须同时考虑投影分子与视线长度分母的变化。
- 圆心到两个接收器的距离及夹角确定后，用余弦定理求接收器间距。

## 三、物理图像

设轨道圆心为$O$，火箭位置为$P$。固定接收器$Q$距圆心$b$。令$\psi$为$OP$相对于$OQ$的角度，火箭逆时针运动时$\dot\psi=\omega>0$。

朝向接收器的视线速度分量为正时，频率高于$f_0$；背离时为负，频率低于$f_0$。火箭“正在绕圈”不意味着朝某台接收器始终接近或始终远离。

将曲线1对应的接收器记为$B$，曲线2对应的接收器记为$A$。曲线1的频率变化范围较大，曲线2较小。后面的极值推导会说明$B$位于轨道外，$A$位于轨道内，而不是仅凭图形高低直接猜测位置。

## 四、解题入口

先从一对相邻波前求出

$$
f=\frac{cf_0}{c-u}.
$$

再对圆周运动建立

$$
D^2=r^2+b^2-2rb\cos\psi,\qquad
u=-\frac{vb\sin\psi}{D}.
$$

对$u^2$求极值，选择几何允许的根。结合图上约$24\,\mathrm s$的周期、约$6\,\mathrm s$的最大频率到最小频率间隔，以及两曲线最大值约$8\,\mathrm s$的错开，求$OA,OB,\angle AOB$。

## 五、解析

（1）用相邻波前推导直线接近时的频率。

源的发声周期为

$$
\Delta t_{\mathrm e}=\frac1{f_0}.
$$

这段时间中，先发出的波前向前传播距离$c\Delta t_{\mathrm e}$；声源自身向接收器移动距离$v\Delta t_{\mathrm e}$。所以前方相邻波前的距离为

$$
\lambda=(c-v)\Delta t_{\mathrm e}
=\frac{c-v}{f_0}.
\tag{1}
$$

接收器在空气中静止，波前以速度$c$经过它，因此

$$
\boxed{
f=\frac c\lambda=\frac c{c-v}f_0
}.
\tag{2}
$$

因为$c-v<c$，接收频率大于$f_0$。若声源直接远离，将朝向接收器的速度分量改为$-v$，得到$f=cf_0/(c+v)$，低于源频率。

图6-2把两次发声位置和相邻波前画在同一传播方向上。图中“波前传播距离”与“源向前移动距离”相减，正是分母$c-v$的来源。

![图 6-2　静止接收器方向上相邻波前间距的形成。](../figures/wavefront-06.png){width=80%}

（2）推广到有夹角的瞬时运动。

声源速度在从声源指向接收器方向上的分量为

$$
u=v\cos\varphi.
$$

相邻发声时刻足够接近时，视线方向变化可以按微分近似处理。用$u$代替式（1）中的$v$，得

$$
\lambda=\frac{c-v\cos\varphi}{f_0}.
$$

第二问答案为

$$
\boxed{
f=\frac c{c-v\cos\varphi}f_0
}.
\tag{3}
$$

当$\varphi=0$，恢复式（2）；当$\varphi=\pi$，为远离情形；当$\varphi=\pi/2$，此经典模型的频率等于$f_0$，没有声学的相对论横向多普勒项。

“忽略传播时间”在本题中的用法是：将频率曲线的时间近似对应到火箭当前轨道位置，不另加绝对路程$D/c$修正相位。它不是删掉相邻波前因源运动造成的间距差；若连这个间距差也删掉，就根本不会有多普勒频移。

（3）提取周期及极值读数，先确定可用精度。

两条曲线重复周期均约为

$$
T\simeq24\,\mathrm s.
\tag{4}
$$

曲线1的极值约为

$$
f_{1,\max}\simeq1.33\,\mathrm{kHz},
\qquad
f_{1,\min}\simeq0.89\,\mathrm{kHz}.
$$

以图中刻度允许的简洁读数计算，可取

$$
f_{1,\max}\simeq\frac43\,\mathrm{kHz},
\qquad
f_{1,\min}\simeq\frac89\,\mathrm{kHz}.
\tag{5}
$$

最大值到随后最小值的短时间间隔约为$6\,\mathrm s$；两曲线对应最大值的错开约为$8\,\mathrm s$。这些时间应从同一周期的对应位置读出，不能将一条曲线的最大值与另一条曲线的最小值当作同类事件。

接下来先证明曲线1为何能用总速率$v$代入极值公式，再用式（5）求数值。

（4）建立任意接收器的视线速度。

将某台接收器置于$Q=(b,0)$，火箭位置写成

$$
P=(r\cos\psi,r\sin\psi).
$$

圆周运动的速度为

$$
\boldsymbol v_P
=(-v\sin\psi,v\cos\psi).
\tag{6}
$$

从火箭指向接收器的矢量及距离为

$$
\begin{aligned}
\boldsymbol D
&=Q-P=(b-r\cos\psi,-r\sin\psi),\\
D^2
&=(b-r\cos\psi)^2+r^2\sin^2\psi\\
&=b^2+r^2-2rb\cos\psi.
\end{aligned}
\tag{7}
$$

速度沿视线的分量为$\boldsymbol v_P\cdot\boldsymbol D/D$。将点积逐项展开：

$$
\begin{aligned}
u
&=\frac{(-v\sin\psi)(b-r\cos\psi)
+(v\cos\psi)(-r\sin\psi)}D\\
&=\frac{-vb\sin\psi
+vr\sin\psi\cos\psi-vr\cos\psi\sin\psi}D\\
&=\boxed{-\frac{vb\sin\psi}D}.
\end{aligned}
\tag{8}
$$

含$r\sin\psi\cos\psi$的两项抵消。$\psi<0$时通常对应接近，$u>0$；$\psi>0$时对应远离，$u<0$。

（5）完整求极值，区分内、外接收器。

因为$f=cf_0/(c-u)$随$u$单调增加，最大、最小频率与最大、最小$u$对应。平方后

$$
\frac{u^2}{v^2}
=\frac{b^2\sin^2\psi}{r^2+b^2-2rb\cos\psi}.
$$

令$z=\cos\psi$，可写成

$$
F(z)=\frac{b^2(1-z^2)}{r^2+b^2-2rbz}.
\tag{9}
$$

对$z$用商法则：

$$
\begin{aligned}
F'(z)
&=\frac{
b^2[-2z(r^2+b^2-2rbz)+2rb(1-z^2)]
}{(r^2+b^2-2rbz)^2}\\
&=\frac{
2b^2[rbz^2-(r^2+b^2)z+rb]
}{(r^2+b^2-2rbz)^2}.
\end{aligned}
\tag{10}
$$

分子二次式可因式分解：

$$
rbz^2-(r^2+b^2)z+rb
=(rz-b)(bz-r).
$$

因此候选根为

$$
z=\frac br,\qquad z=\frac rb.
\tag{11}
$$

当$b>r$，$b/r>1$不可能为余弦，保留$z=r/b$。代入式（9）：

$$
\begin{aligned}
D^2&=b^2-r^2,\\
b^2\sin^2\psi&=b^2-r^2,\\
u_{\max}&=v,\qquad u_{\min}=-v.
\end{aligned}
\tag{12}
$$

当$0<b<r$，$r/b>1$不可能，保留$z=b/r$。此时

$$
\begin{aligned}
D^2&=r^2-b^2,\\
b^2\sin^2\psi&=\frac{b^2}{r^2}(r^2-b^2),\\
u_{\max}&=v\frac br,\qquad
u_{\min}=-v\frac br.
\end{aligned}
\tag{13}
$$

图6-3分别画出外接收器的切线极值和内接收器的垂直视线几何。外部极值时$OP\perp PQ$；内部极值时$OQ\perp PQ$。两个直角所在位置不同，正是$r/b$与$b/r$互为倒数而不能混用的原因。

![图 6-3　外部与内部接收器的频率极值位置及直角几何。](../figures/extrema-06.png){width=88%}

同一速率的声源对任何外部接收器都有完整的$\pm v$极值。曲线2的频移幅度明显小于曲线1，故曲线1对应外部$B$、曲线2对应内部$A$。不能只把曲线2的较小最大值解释为更远的外部接收器。

（6）用曲线1的两个极值求源频率与速率。

由式（12），

$$
f_{1,\max}=\frac{cf_0}{c-v},
\qquad
f_{1,\min}=\frac{cf_0}{c+v}.
\tag{14}
$$

对两式分别取倒数再相加、相减，可以消去$f_0$：

$$
\begin{aligned}
\frac1{f_{1,\min}}+\frac1{f_{1,\max}}
&=\frac{2}{f_0},\\
\frac1{f_{1,\min}}-\frac1{f_{1,\max}}
&=\frac{2v}{cf_0}.
\end{aligned}
$$

两式相除，得

$$
\boxed{
\frac vc
=\frac{f_{1,\max}-f_{1,\min}}
{f_{1,\max}+f_{1,\min}}
}.
\tag{15}
$$

代入式（5）：

$$
\begin{aligned}
\frac vc
&\simeq
\frac{4/3-8/9}{4/3+8/9}\\
&=\frac{12/9-8/9}{12/9+8/9}\\
&=\frac4{20}=\frac15,\\
v&\simeq\frac{330}{5}
=\boxed{66\,\mathrm{m\,s^{-1}}}.
\end{aligned}
\tag{16}
$$

源频率由倒数相加求得：

$$
\begin{aligned}
f_0
&=\frac{2f_{1,\max}f_{1,\min}}
{f_{1,\max}+f_{1,\min}}\\
&\simeq\frac{2(4/3)(8/9)}{4/3+8/9}\,\mathrm{kHz}\\
&=\frac{16}{15}\,\mathrm{kHz}.
\end{aligned}
\tag{17}
$$

这是调和平均形式，不是两个极值的算术平均。用算术平均会高估$f_0$，因为频率对视线速度是分式关系。

（7）由周期求轨道半径。

一周期走过的路程为$2\pi r$，故

$$
\begin{aligned}
2\pi r&=vT,\\
r&=\frac{vT}{2\pi}\\
&\simeq\frac{66\times24}{2\pi}\,\mathrm m\\
&=\frac{792}{\pi}\,\mathrm m\\
&\simeq\boxed{252\,\mathrm m}.
\end{aligned}
\tag{18}
$$

频率曲线的周期是完成一圈的时间，不是最大值到最小值的时间。由于视线几何不对称，后者通常并非半周期，本题约$6\,\mathrm s$也不是$12\,\mathrm s$。

（8）用约6秒的下降段求两接收器到圆心的距离。

令$\delta$表示极值位置的正角。声源从接近极值$\psi=-\delta$走到远离极值$\psi=+\delta$，频率由最大值下降至最小值，转过$2\delta$。按题设时间近似，

$$
2\delta=\omega\Delta t_{\mathrm{fall}},
\qquad
\delta=\frac{\pi\Delta t_{\mathrm{fall}}}{T}.
\tag{19}
$$

曲线1有$\Delta t_{\mathrm{fall},1}\simeq6\,\mathrm s$，所以

$$
\delta_B\simeq\frac{\pi\cdot6}{24}
=\frac\pi4.
$$

外部接收器的极值条件是$\cos\delta_B=r/OB$，因而

$$
\boxed{
OB=\frac r{\cos\delta_B}\simeq\sqrt2\,r
}.
\tag{20}
$$

曲线2也有约$6\,\mathrm s$的极值下降段，得到$\delta_A\simeq\pi/4$。内部接收器使用的是$\cos\delta_A=OA/r$，所以

$$
\boxed{
OA=r\cos\delta_A\simeq\frac r{\sqrt2}
}.
\tag{21}
$$

外部与内部两个距离不能交换。外部必须满足$OB>r$，内部必须满足$OA<r$，可立即筛掉把根选择反了的答案。

由式（13），内部接收器的极值投影速度为$v/\sqrt2$，据此预期

$$
\begin{aligned}
f_{2,\max}
&\simeq\frac{f_0}{1-v/(\sqrt2c)}
\approx1.24\,\mathrm{kHz},\\
f_{2,\min}
&\simeq\frac{f_0}{1+v/(\sqrt2c)}
\approx0.935\,\mathrm{kHz}.
\end{aligned}
\tag{22}
$$

与图中曲线2的范围相符，这是对位置分类和半径比的独立幅度检查。

（9）用两曲线约8秒的峰值错开求夹角。

设$OB$的方位角为$\alpha_B$，$OA$的方位角为$\alpha_A$。两台接收器的最大频率均发生在

$$
\theta_P=\alpha_Q-\delta_Q,
$$

其中$\theta_P$是火箭的地面轨道方位角。由于本题$\delta_A=\delta_B=\pi/4$，两个峰值之间的声源方位角变化就是两个接收器方位角的差：

$$
\begin{aligned}
\alpha_A-\alpha_B
&=\omega(t_{A,\max}-t_{B,\max})\\
&\simeq\frac{2\pi}{24}\times8\\
&=\frac{2\pi}{3}.
\end{aligned}
\tag{23}
$$

因此较小夹角为

$$
\boxed{\angle AOB\simeq120^\circ}.
$$

若选择相反的绕行方向或镜像坐标，会得到相反有向角，但余弦和两接收器间距不变。不能把峰值错开的$8\,\mathrm s$误用作某台接收器最大到最小的$6\,\mathrm s$。

图6-4按$OA=r/\sqrt2$、$OB=\sqrt2r$、$\angle AOB=120^\circ$重建位置。轨道和两点按这些比例绘制，$AB$是最后要求的连线，不是某一段轨道弦长。

![图 6-4　由极值时间和相位差重建的轨道、内外接收器及其距离。](../figures/receivers-06.png){width=75%}

（10）用余弦定理求最终距离。

在三角形$AOB$中，

$$
AB^2=OA^2+OB^2-2\,OA\,OB\cos120^\circ.
\tag{24}
$$

逐项代入：

$$
\begin{aligned}
AB^2
&=\left(\frac r{\sqrt2}\right)^2
+(\sqrt2r)^2
-2\left(\frac r{\sqrt2}\right)(\sqrt2r)
\left(-\frac12\right)\\
&=\frac12r^2+2r^2+r^2\\
&=\frac72r^2.
\end{aligned}
\tag{25}
$$

第三项为正，是因为夹角为钝角，$\cos120^\circ=-1/2$。不能把这个负余弦再漏掉一次符号。

故

$$
\begin{aligned}
AB
&=\sqrt{\frac72}\,r\\
&\simeq\sqrt{\frac72}\frac{792}{\pi}\,\mathrm m\\
&\approx\boxed{4.72\times10^2\,\mathrm m}.
\end{aligned}
\tag{26}
$$

距离约为$472\,\mathrm m$。图上刻度和曲线线宽只支持近似结论，应保留“约”，而不是报告许多位小数。

（11）边界、量纲与回代检查。

最终位置满足$OA\simeq178\,\mathrm m<r$、$OB\simeq357\,\mathrm m>r$。三角形两边之差约为$178\,\mathrm m$，两边之和约为$535\,\mathrm m$，而$AB\simeq472\,\mathrm m$在两者之间，满足三角形不等式。

取$OB=\sqrt2r$，极值角为$\arccos(r/OB)=45^\circ$；取$OA=r/\sqrt2$，极值角为$\arccos(OA/r)=45^\circ$。两者最大到最小均走过$90^\circ$，占$24\,\mathrm s$周期的四分之一，即$6\,\mathrm s$。两接收器方位相差$120^\circ$，对应峰值错开$8\,\mathrm s$，时间关系完整恢复。

取$r=vT/(2\pi)$的单位为长度，余弦定理中的每项单位为长度平方；多普勒式中的$v/c$无量纲，频率单位由$f_0$提供。若把周期误用成频率或漏掉$2\pi$，会在这一步显示量纲或回代时序的不一致。

## 六、关键洞察

内部、外部接收器的极值时刻都有一个直角几何，但直角不在同一点。外部接收器的极值发生在从接收器向轨道作切线的位置，视线与火箭速度平行，得到完整$\pm v$；内部接收器无法与圆周切线相交，最大投影只有$v\,OA/r$。

圆心接收器是一个直接极限检查：令$b\to0$，由式（8）得$u\to0$，因此$f\to f_0$恒定，即使声源速率始终非零。频移观察的是径向接近速度，不是运动本身。

对一般两接收器，峰值相位差还包含极值偏角差。由$\theta_P=\alpha_Q-\delta_Q$，

$$
\alpha_A-\alpha_B
=\omega\Delta t_{\max}+\delta_A-\delta_B.
$$

本题因为两个下降段相同，$\delta_A-\delta_B=0$才直接由$8/24$得到$120^\circ$。不能把这种简化当作任意内外接收器的通用公式。

## 七、易错点

- 用固定接收器、运动声源的题目套上运动接收器公式$f=f_0(c+v)/c$。
- 不定义视线方向，正负投影混乱。
- 用两个频率极值的算术平均代替源频率。
- 看见圆周运动就把最大到最小时间取为$T/2$。
- 极值条件只对$\sin\psi$求最大，遗漏分母$D$也变化。
- 不筛选余弦根，使内部距离大于轨道半径、外部距离小于轨道半径。
- 混用6秒下降段和8秒两曲线错开，得到错误的半径比或夹角。
- 把忽略绝对传播延迟理解为取消多普勒效应。
- 对读图题报告不合理的高精度距离，或把近似模型说成精确定位。

## 八、课堂讲解建议

先让学生在直线传播图上标出两个发声点与相邻波前，推导$c-v$，教师再引入视线投影。随后让学生比较“接收器在圆心”和“接收器在很远处”两种频率范围，建立内部和外部的直觉。

图像审读时，板书分三列记录周期、下降段和峰值错开，要求学生说明每个时间对应的几何事件。极值推导保留商法则和两个候选根，让学生用$\cos\psi\le1$自主筛选，而不直接给出切线结果。

最终余弦定理前，让学生先画按比例的内外位置图并判断钝角。教师用回代的6秒、8秒和曲线2极值范围检查整个几何链，而不只检查最后一个距离数值。

## 九、变式训练

变式一：保留有限声传播时间，其余几何半径比仍由同一台接收器的极值间隔得到。若两台接收器记录的峰值错开仍为$\Delta t_{\mathrm{rec}}$，求真实方位角差的修正。

声音到达时刻为

$$
t_{\mathrm{rec}}=t_{\mathrm e}+\frac{D(t_{\mathrm e})}{c}.
$$

本题$v<c$，映射单调，频率极值的发射位置仍由式（11）确定。每台接收器自身的最大和最小位置关于$OQ$对称，其视线长度相同，所以该台最大到最小的传播延迟差为零，原来的6秒角度判断仍成立。

在峰值位置，外部与内部视线长度分别为

$$
D_B=\sqrt{OB^2-r^2}=r,\qquad
D_A=\sqrt{r^2-OA^2}=\frac r{\sqrt2}.
$$

两台峰值的发射时间差为

$$
\Delta t_{\mathrm e}
=\Delta t_{\mathrm{rec}}-\frac{D_A-D_B}{c}.
$$

故真实方位角差为

$$
\begin{aligned}
\Delta\alpha
&=\omega\Delta t_{\mathrm e}
+\delta_A-\delta_B\\
&=\frac{2\pi}{T}\Delta t_{\mathrm{rec}}
+\frac{v}{c}\left(1-\frac1{\sqrt2}\right).
\end{aligned}
$$

代入$\Delta t_{\mathrm{rec}}=8\,\mathrm s$和$v/c=1/5$，得

$$
\Delta\alpha
=\frac{2\pi}{3}+\frac15\left(1-\frac1{\sqrt2}\right)
\approx123.36^\circ.
$$

相应距离为

$$
AB_{\mathrm{ret}}
=r\sqrt{\frac52-2\cos\Delta\alpha}
\approx4.78\times10^2\,\mathrm m.
$$

它是改变“忽略传播延迟”这一条件后的变式结果，不替代主问题按题设近似得到的$472\,\mathrm m$。修正的角度约为$3.36^\circ$；有限读图误差也会影响定位，不能用这组近似曲线宣称毫米级精度。

变式二：一匀速转动声源，外部静止接收器测得最高、最低频率分别为 $1200\,\mathrm{Hz}$、$1000\,\mathrm{Hz}$。声速为 $330\,\mathrm{m/s}$，求源频率与线速度。

解：外接收器的两条切线对应径向速度 $\pm v$，于是 $f_+=f_0c/(c-v)$、$f_-=f_0c/(c+v)$。将两式分别取倒数再相加、相减，得

$$
v=c\frac{f_+-f_-}{f_++f_-}=30\,\mathrm{m/s},\quad
f_0=\frac{2f_+f_-}{f_++f_-}=\frac{12000}{11}\,\mathrm{Hz}.
$$

源频率是这两个极值的调和平均；算术平均只有低速的一阶近似意义。

变式三：把接收器放在圆轨道中心，声源以速率 $v<c$、半径 $r$ 匀速转动。求接收频率和传播时延，解释为什么没有周期性频移。

解：声源到中心的距离恒为 $r$，每个波包到达时刻都是 $t_{\rm rec}=t_e+r/c$。对相邻发射时刻作差，$\Delta t_{\rm rec}=\Delta t_e$，因此

$$
f_{\rm rec}=f_0,\qquad t_{\rm delay}=r/c.
$$

速度始终与传播方向垂直，经典声学多普勒公式中的径向速度为零。这里仍采用题目的非相对论声学模型；不能另外加入真空光的横向多普勒因子。

变式四：外部接收器测得相邻同类频率峰的间隔为 $T$，源的线速度已知为 $v$。有限声传播时间是否影响由 $r=vT/(2\pi)$ 求半径？给出证明。

解：同一峰在相邻两周对应相同发射位置、速度方向和源—接收器距离 $D$。发射时间相差一周 $T_e=2\pi r/v$，到达时间分别为 $t_e+D/c$ 和 $t_e+T_e+D/c$。因此

$$
T_{\rm rec}=T_e,\qquad r=\frac{vT_{\rm rec}}{2\pi}.
$$

跨不同接收器比较峰相位时，传播距离差需要修正；同一接收器的相邻同类峰则没有这项差值。
