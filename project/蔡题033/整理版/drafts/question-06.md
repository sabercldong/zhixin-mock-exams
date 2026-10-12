# 第 6 题

<!-- question-start -->

两根平行理想导轨相距 $l$，放在垂直纸面向外的匀强磁场 $B$ 中。质量为 $m$、电阻可忽略的导体棒垂直跨接在导轨上，并可沿导轨无摩擦滑动。导体棒运动时受到与速度成正比、方向相反的阻力

$$
\boldsymbol f=-k\boldsymbol v.
$$

导轨、导体棒和外接非直流电源构成的回路自感为 $L$，其余电阻均忽略。

（1）用一个由电阻 $R_0$、电容 $C_0$、电感 $L_0$ 和原电源组成的纯电路模拟该机电系统，使电源端口的电压和电流在任意时刻均与原系统相同。画出连接方式，并用 $l$、$B$、$m$、$L$、$k$ 表示 $R_0$、$C_0$、$L_0$。

（2）若电源电压为

$$
U(t)=U_0\cos\omega t,
$$

求稳态时导体棒位移振幅 $x_0$。

![图 6-1　磁场中导体棒的机电耦合系统。](../figures/question-06.png)

<!-- question-end -->

## 一、题型定位

本题是电磁感应、含自感电路与受迫运动的机电类比题。导体棒既是电路元件，也是机械运动物体：电流通过导体棒产生安培力，导体棒运动又产生动生电动势。把这两个耦合关系写成同一对端口变量后，质量与阻力可以分别等效为电容和电阻，原回路自感则保持为串联电感。

第（2）问本质上是线性受迫系统的正弦稳态响应。直接从复阻抗求电流再求速度可以完成；把两个一阶方程消元成关于速度的二阶方程，则更容易看清惯性项、阻尼项和电磁“回复项”的来源。

## 二、知识点

- 导体棒的动生电动势 $u_m=Blv$。
- 导体棒所受安培力 $F_B=Bli$。
- 含自感回路的端口电压方程。
- 机械方程与并联 $RC$ 支路的端口类比。
- 串联电感与并联 $RC$ 的复阻抗。
- 正弦稳态、相量法和位移—速度振幅关系 $v_0=\omega x_0$。
- 极限、量纲和平均功率检查。

## 三、物理图像

规定导体棒向右运动的速度 $v$ 为正，选取电流正方向，使正电流对棒产生向右的安培力。导体棒运动时产生的动生电动势反抗外电源驱动，因此电源端电压分成两部分：一部分加在原回路自感上，另一部分等于动生电动势

$$
u_m=Blv.
$$

机械侧的安培力 $Bli$ 一部分使质量产生加速度，另一部分克服线性阻力：

$$
Bli=m\frac{dv}{dt}+kv.
$$

把 $u_m=Blv$ 当作一个电支路的端电压后，右端的惯性项正比于 $du_m/dt$，阻力项正比于 $u_m$，它们正好对应电容电流和电阻电流。图6-2给出端口变量与纯电路的对应关系。

## 四、解题入口

不要从“质量像电感还是电容”的记忆表开始。先定义导体棒端口电压

$$
u_m=Blv,
$$

再把机械方程改写成 $i$ 关于 $u_m$ 和 $du_m/dt$ 的关系。只要所得形式与

$$
i=\frac{u_m}{R_0}+C_0\frac{du_m}{dt}
$$

逐项比较，$R_0$、$C_0$ 就会自然出现。随后由电源电压方程判断 $L_0$ 与这个并联支路是串联还是并联。

求振幅时，先求速度振幅 $v_0$。位移是速度对时间的积分，稳态正弦量的振幅满足 $x_0=v_0/\omega$；若直接把速度振幅当成位移振幅，会少一个 $\omega$。

## 五、解析

图6-2左侧保留导体棒的机械运动及电学端口，右侧将同一端口替换为纯电网络。两侧共用 $u_m$ 和 $i$：下面把机械方程改写成以 $u_m$ 为自变量的电流关系，并据此确定右侧支路是并联还是串联；图中各元件的数值均由这一关系求出。

![图 6-2　导体棒机电端口与串联电感、并联电阻电容的等效关系。](../figures/solution-06.png)

（1）建立原机电系统的两个耦合方程。

电流为 $i$ 时，导体棒受到向右的安培力

$$
F_B=Bli.
$$

线性阻力大小为 $kv$、方向向左。对导体棒列牛顿第二定律：

$$
m\frac{dv}{dt}=Bli-kv.
$$

移项得

$$
Bli=m\frac{dv}{dt}+kv.
\tag{1}
$$

导体棒向右运动产生动生电动势

$$
u_m=Blv.
\tag{2}
$$

因此

$$
v=\frac{u_m}{Bl},
\qquad
\frac{dv}{dt}=\frac1{Bl}\frac{du_m}{dt}.
$$

代入式（1）：

$$
Bli
=m\frac1{Bl}\frac{du_m}{dt}
+k\frac{u_m}{Bl}.
$$

两边再除以 $Bl$：

$$
i
=\frac{m}{B^2l^2}\frac{du_m}{dt}
+\frac{k}{B^2l^2}u_m.
\tag{3}
$$

并联电阻、电容支路的总电流为

$$
i=C_0\frac{du_m}{dt}+\frac{u_m}{R_0}.
\tag{4}
$$

逐项比较式（3）、（4）：

$$
\boxed{C_0=\frac{m}{B^2l^2}},
\qquad
\boxed{R_0=\frac{B^2l^2}{k}}.
$$

再看电源端电压。原回路自感为 $L$，按所定正方向列回路电压方程：

$$
U=L\frac{di}{dt}+u_m.
\tag{5}
$$

这表明电源电压等于电感电压与机电端口电压之和，而且流过两部分的是同一电流 $i$。因此原自感应与并联 $R_0C_0$ 支路串联，并且

$$
\boxed{L_0=L}.
$$

等效电路为：电源先串联电感 $L_0$，再串联一个由 $R_0$ 与 $C_0$ 并联构成的二端网络。

量纲也可直接检查。因为 $Blv$ 的量纲是电压、$Bli$ 的量纲是力，

$$
\frac{B^2l^2}{k}
=\frac{Blv}{Bli}
=\frac{U}{i}
$$

具有电阻量纲；而

$$
\frac{m}{B^2l^2}
=\frac{i}{d(Blv)/dt}
$$

具有电容量纲。

（2）求正弦稳态位移振幅。

为了不在复数相位中遗漏符号，先从时域方程消去电流。由式（1）

$$
i=\frac{m\dot v+kv}{Bl}.
$$

对时间求导：

$$
\frac{di}{dt}
=\frac{m\ddot v+k\dot v}{Bl}.
$$

代入电压方程（5）：

$$
U
=L\frac{m\ddot v+k\dot v}{Bl}+Blv.
$$

两边乘以 $Bl$：

$$
Lm\ddot v+Lk\dot v+B^2l^2v=BlU.
\tag{6}
$$

当 $U=U_0\cos\omega t$ 时，稳态速度可写为

$$
v(t)=\Re\!\left(\widetilde v e^{i\omega t}\right).
$$

于是

$$
\dot v\longrightarrow i\omega\widetilde v,
\qquad
\ddot v\longrightarrow-\omega^2\widetilde v.
$$

把它们代入式（6）：

$$
\left(B^2l^2-Lm\omega^2+iLk\omega\right)\widetilde v
=BlU_0.
$$

所以复速度振幅为

$$
\widetilde v
=\frac{BlU_0}
{B^2l^2-Lm\omega^2+iLk\omega}.
$$

取模得到速度振幅

$$
\boxed{
v_0
=\frac{BlU_0}
{\sqrt{\left(B^2l^2-Lm\omega^2\right)^2+\left(Lk\omega\right)^2}}
}.
$$

稳态位移满足 $v=dx/dt$。对正弦量，速度振幅与位移振幅相差因子 $\omega$：

$$
v_0=\omega x_0.
$$

因此

$$
\boxed{
x_0
=\frac{BlU_0}
{\omega\sqrt{\left(B^2l^2-Lm\omega^2\right)^2+\left(Lk\omega\right)^2}}
}.
$$

位移振幅与速度振幅之间的 $1/\omega$ 也可通过积分直接看出。记

$$
a_\omega=B^2l^2-Lm\omega^2,
\qquad b_\omega=Lk\omega.
$$

把复分母乘以其共轭，得到

$$
\widetilde v
=\frac{BlU_0(a_\omega-ib_\omega)}{a_\omega^2+b_\omega^2}.
$$

展开实部后，速度为

$$
v(t)=\frac{BlU_0}{a_\omega^2+b_\omega^2}
\left(a_\omega\cos\omega t+b_\omega\sin\omega t\right).
$$

逐项积分得到

$$
x(t)-\overline x
=\frac{BlU_0}{\omega(a_\omega^2+b_\omega^2)}
\left(a_\omega\sin\omega t-b_\omega\cos\omega t\right),
$$

其中 $\overline x$ 是由初始位置和暂态过程确定的平均位置。两个正交正弦项的振幅按平方和合成，恰好给出上面的 $x_0$。导轨上的棒没有位置回复力，所以题目能确定振幅，却不能仅凭稳态电压确定 $\overline x$。

若写为 $v=v_0\cos(\omega t-\phi)$，则相位应由

$$
\cos\phi=\frac{a_\omega}{\sqrt{a_\omega^2+b_\omega^2}},
\qquad
\sin\phi=\frac{b_\omega}{\sqrt{a_\omega^2+b_\omega^2}}
$$

联合确定。只写 $\tan\phi=b_\omega/a_\omega$ 会丢失象限；在 $a_\omega<0$ 时，速度滞后角已大于 $\pi/2$，不能仍取反正切的小角主值。

还可以从等效电路反查。并联支路阻抗为

$$
Z_{RC}
=\frac1{1/R_0+i\omega C_0}
=\frac{B^2l^2}{k+i\omega m}.
$$

总阻抗为

$$
Z=i\omega L+Z_{RC}.
$$

并联支路电压就是 $\widetilde u_m=Bl\widetilde v$。由分压关系计算出的 $\widetilde v$ 与上式完全相同，说明纯电路在电源端口的电压、电流关系和原机电系统一致。

平均功率也能核验等效电阻。机械阻力平均耗散功率为

$$
\overline P_{\rm mech}
=k\overline{v^2}
=\frac12kv_0^2.
$$

等效电阻两端电压振幅为 $u_{m0}=Blv_0$，其平均耗散功率为

$$
\overline P_R
=\frac{u_{m0}^2}{2R_0}
=\frac{B^2l^2v_0^2}{2(B^2l^2/k)}
=\frac12kv_0^2.
$$

两者相等，说明 $R_0=B^2l^2/k$ 不仅满足方程形式，也正确保存了能量耗散。

频率极限还可以检查振幅式的物理意义。当 $\omega\to0$ 时，外电压变化很慢，自感项可忽略，电压主要与动生电动势平衡，因而

$$
v_0\longrightarrow\frac{U_0}{Bl}.
$$

位移振幅 $x_0=v_0/\omega$ 随之增大，这表示无弹簧系统在很慢的交变驱动下可在每个半周内移动很长距离，并非公式发散失效。当 $\omega\to\infty$ 时，惯性与自感项占主导，有

$$
v_0\sim\frac{BlU_0}{Lm\omega^2},
\qquad
x_0\sim\frac{BlU_0}{Lm\omega^3}.
$$

高频下位移按 $\omega^{-3}$ 衰减，与“自感抑制电流变化、质量抑制加速度变化”的双重惰性一致。

（3）检查储能与暂态消失条件。

质量对应电容，还应在能量上成立。等效电容的电场能为

$$
W_C=\frac12C_0u_m^2
=\frac12\frac{m}{B^2l^2}(Blv)^2
=\frac12mv^2.
$$

它正好等于棒的动能；串联电感的储能 $Li^2/2$ 则与原回路磁场能相同。将机械方程乘以 $v$、电压方程乘以 $i$，消去功率交换项 $Bli v$，有

$$
\begin{aligned}
Bli v&=\frac{d}{dt}\left(\frac12mv^2\right)+kv^2,\\
Ui&=\frac{d}{dt}\left(\frac12Li^2\right)+Bli v,\\
Ui&=\frac{d}{dt}\left(\frac12Li^2+\frac12mv^2\right)+kv^2.
\end{aligned}
$$

这就是完整的瞬时能量守恒式：电源供给的功率等于储能增长率与阻力耗散之和。进入周期稳态后，储能一周期的净变化为零，对上式取周期平均便得 $\overline{Ui}=kv_0^2/2$。

暂态速度满足式（6）的齐次方程。设 $v_h\propto e^{\lambda t}$，则

$$
Lm\lambda^2+Lk\lambda+B^2l^2=0,
$$

所以

$$
\lambda_\pm=-\frac{k}{2m}
\pm\sqrt{\frac{k^2}{4m^2}-\frac{B^2l^2}{Lm}}.
$$

当 $k>0$ 时，两根为实数的情形下都为负；为复数时实部均为 $-k/(2m)<0$。因此速度和电流暂态最终衰减，上述稳态振幅与初始条件无关。若令 $k=0$，暂态一般不再衰减，且 $\omega=Bl/\sqrt{Lm}$ 时理想模型产生无阻尼共振，此时不能把有限稳态振幅公式用于共振点。

如果初始速度与初始电流分别为 $v(0)=v_i$、$i(0)=i_i$，机械方程还给出初始加速度

$$
\dot v(0)=\frac{Bl i_i-kv_i}{m}.
$$

设稳态解为 $v_s$，在两特征根不相同的情形，完整速度写为

$$
v(t)=v_s(t)+c_+e^{\lambda_+t}+c_-e^{\lambda_-t}.
$$

令 $a=v_i-v_s(0)$、$b=(Bl i_i-kv_i)/m-\dot v_s(0)$，代入两个初始条件得到

$$
c_++c_-=a,\qquad
\lambda_+c_++\lambda_-c_-=b.
$$

消去其中一个系数：

$$
c_+=\frac{b-\lambda_-a}{\lambda_+-\lambda_-},
\qquad
c_-=\frac{\lambda_+a-b}{\lambda_+-\lambda_-}.
$$

因此初态确实影响暂态系数，但 $k>0$ 时这两项衰减以后，只剩前面计算的稳态。重根时齐次解改为 $(c_1+c_2t)e^{-kt/(2m)}$，仍趋于零；这个情况不能把上述含 $\lambda_+-\lambda_-$ 的分式直接代零。

## 六、关键洞察

机电类比取决于选用哪一对端口变量。本题选 $u_m=Blv$ 后，速度对应电压，安培力方程中的质量项变成与 $du_m/dt$ 成正比的电流，所以质量等效为电容，而不是凭印象写成电感。

原回路自感 $L$ 与导体棒端口流过同一电流，电源电压又等于两者电压之和，因此 $L_0$ 必须串联在并联 $R_0C_0$ 网络之前。元件数值正确但拓扑画错，仍不能保证电源端口的电压、电流相同。

式（6）是关于速度而不是位移的受迫二阶方程。电磁项 $B^2l^2v$ 对速度变量起“回复项”作用，因此速度响应存在类似共振的频率结构；最后转换成位移振幅时还要除以 $\omega$。

## 七、易错点

- 把动生电动势在电压方程中写成帮助外电源的方向，导致 $U=L\dot i-Blv$。按本题正方向，动生电动势反抗驱动，电源必须同时提供 $L\dot i$ 与 $Blv$。
- 把安培力写成 $Bil^2$ 或漏掉导轨间距 $l$。导体棒有效长度就是 $l$，故 $F_B=Bli$。
- 直接套“质量对应电感”的另一种类比。本题端口变量选为 $u_m=Blv$，质量对应的是电容 $C_0$。
- 把 $R_0$、$C_0$ 串联。式（3）中两项电流相加，说明它们是同端电压下的并联支路。
- 求出 $v_0$ 后直接当成 $x_0$，漏掉 $x_0=v_0/\omega$。
- 把复数分母的模写成两项直接相加。应使用 $\sqrt{A^2+B^2}$。
- 忽略稳态限定。完整运动还含由初始条件决定的暂态项，题目所求振幅是暂态衰减后的正弦稳态振幅。

## 八、课堂讲解建议

讲解时先在原装置图上圈出两个端口量：棒的动生电动势 $u_m$ 和流过棒的电流 $i$。要求先把机械方程改写成式（3），再让学生识别“同一电压下两项电流相加”对应并联结构。这样比先给机械—电学对应表更不容易画错拓扑。

完成等效电路后，应同时做三项检查：电源端KVL是否与原式相同；$R_0$、$C_0$ 的量纲是否正确；电阻耗散功率是否等于机械阻力耗散功率。三项都成立时，类比才算完整。

第（2）问可分别用时域消元和复阻抗分压求一次。前者突出运动方程，后者突出“端口等效”的含义；两条路线得到同一复速度振幅，是很有价值的交叉核验。

## 九、变式训练

若导体棒除线性阻力 $-kv$ 外，还受到水平轻弹簧的回复力 $-Kx$，其余条件不变。仍取 $u_m=Blv$，说明纯电路中应再加入什么元件，并写出正弦电压驱动下的位移振幅。

机械方程变为

$$
Bli=m\dot v+kv+Kx.
$$

由于 $v=\dot x$ 且 $u_m=Blv$，有

$$
x=\frac1{Bl}\int u_m\,dt.
$$

两边除以 $Bl$：

$$
i
=\frac{m}{B^2l^2}\dot u_m
+\frac{k}{B^2l^2}u_m
+\frac{K}{B^2l^2}\int u_m\,dt.
$$

前两项仍对应 $C_0$ 与 $R_0$。电感支路在端电压为 $u_m$ 时满足

$$
i_L=\frac1{L_K}\int u_m\,dt.
$$

因此还应在 $R_0$、$C_0$ 两端并联一个电感

$$
\boxed{L_K=\frac{B^2l^2}{K}}.
$$

原回路自感 $L_0=L$ 仍与整个并联网络串联。

直接消去电流可得到位移方程。由

$$
i=\frac{m\ddot x+k\dot x+Kx}{Bl}
$$

和 $U=L\dot i+Bl\dot x$，

$$
Lm\dddot x+Lk\ddot x+(LK+B^2l^2)\dot x=BlU.
$$

对频率为 $\omega$ 的稳态，令 $\widetilde v=i\omega\widetilde x$。速度方程的复系数变为

$$
B^2l^2+LK-Lm\omega^2+iLk\omega.
$$

因此位移振幅为

$$
\boxed{
x_0
=\frac{BlU_0}
{\omega\sqrt{\left(B^2l^2+LK-Lm\omega^2\right)^2+\left(Lk\omega\right)^2}}
}.
$$

令 $K\to0$，新增并联电感 $L_K\to\infty$，该支路自动开路，振幅公式也退化为原题结果。

这个并联电感不仅在方程形式上对应弹簧，它储存的能量也恰好对应弹性势能。电感支路满足

$$
u_m=L_K\frac{di_K}{dt}.
$$

又因为 $u_m=Bl\dot x$，并取 $x=0$ 时 $i_K=0$，对时间积分得

$$
L_Ki_K=Blx,
\qquad
i_K=\frac{Bl}{L_K}x=\frac{Kx}{Bl}.
$$

因此电感的磁场能为

$$
\frac12L_Ki_K^2
=\frac12\frac{B^2l^2}{K}
\left(\frac{Kx}{Bl}\right)^2
=\frac12Kx^2,
$$

正好等于弹簧的弹性势能。这一能量检查同时确认了 $L_K=B^2l^2/K$ 的数值和并联位置。

若进一步考察速度振幅，其分母平方为

$$
F(\omega)
=\left(B^2l^2+LK-Lm\omega^2\right)^2
+L^2k^2\omega^2.
$$

记 $A_0=B^2l^2+LK$。对 $\omega$ 逐项求导：

$$
\begin{aligned}
F'(\omega)
&=2(A_0-Lm\omega^2)(-2Lm\omega)+2L^2k^2\omega\\
&=2L\omega[-2m(A_0-Lm\omega^2)+Lk^2].
\end{aligned}
$$

对非零驻点，方括号必须为零。移项得 $2Lm^2\omega^2=2mA_0-Lk^2$，所以

$$
\omega_v^2
=\frac{B^2l^2+LK}{Lm}-\frac{k^2}{2m^2}.
$$

只有右端为正时，速度响应才在非零频率处有极大值。位移振幅还多出 $1/\omega$ 因子，所以它的极值条件不能直接沿用上式。
