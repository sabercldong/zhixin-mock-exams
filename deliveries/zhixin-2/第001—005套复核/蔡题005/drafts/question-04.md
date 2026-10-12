# 第4题

<!-- question-start -->

一细金属圆环，环半径$R=0.10\ \mathrm m$，导线截面半径$r=1.0\ \mathrm{mm}$，电导率$\sigma=3.7\times10^7\ \Omega^{-1}\mathrm m^{-1}$，密度$\rho=2.7\times10^3\ \mathrm{kg/m^3}$，自感$L=6.0\times10^{-7}\ \mathrm H$。圆环位于交流电磁铁上方，电磁铁电流$I_{\rm em}=I_0\cos\omega t$，频率$f=10\ \mathrm{kHz}$。环所在处磁场与竖直方向成$30^\circ$，径向分量向外，磁场大小$B=kI_{\rm em}$，$k=0.2\times10^{-2}\ \mathrm{T/A}$；环内竖直磁场按均匀处理。

判断能否利用感应电流的磁力托起圆环，并求相应电磁铁电流幅值。取$g=9.8\ \mathrm{m/s^2}$。

原题称“细铁环”，但所给电导率、密度与铁的材料常数不符。按题给参数，将其作为不另计铁磁效应的导体圆环，用给定$L$和电阻建立集中参数模型。

![图4-1 径向外磁场与环向感应电流产生竖直磁力。](../figures/question-04.png){width=88%}

<!-- question-end -->

## 一、题型定位

本题是交流感应电路与平均电磁力问题。自感造成感应电流相对于外磁场的额外相位差，正是产生非零平均托举力的关键。

不能只根据楞次定律说“圆环总被排斥”。外磁场增大与减小时感应电流方向会改变，瞬时磁力也会改变；平均值必须用完整电路响应计算。

题给局部磁场可以判断平均力是否够大，却没有给出磁场随高度的分布，所以只能证明局部平均力平衡，不能据此证明竖直位置稳定。

## 二、知识点

圆环导线长$2\pi R$，截面积$\pi r^2$，电阻记作$\mathcal R$以区别环半径：

$$
\mathcal R=\frac{2R}{\sigma r^2}.
$$

圆环质量为

$$
m=2\pi^2\rho Rr^2.
$$

令磁场与竖直夹角为$\alpha=30^\circ$，则$B_z=kI_{\rm em}\cos\alpha$、$B_r=kI_{\rm em}\sin\alpha$。穿过环的外磁通为

$$
\Phi_{\rm ext}=\pi R^2k\cos\alpha\,I_{\rm em}
=\mathcal M I_{\rm em},
$$

其中$\mathcal M=\pi R^2k\cos\alpha$是这个近似模型中的互感系数。

正环向电流取俯视逆时针，产生向上的轴向磁矩。正环向线元与向外径向场叉乘指向下方，故竖直磁力含有负号。

## 三、物理图像

感应电动势与外磁场相差四分之一周期；若仅有电阻，电流也与外场正交，一个周期的托举力平均为零。加入自感后，电流出现与外场反相的分量，产生向上的平均力。

![图4-2 电阻与自感共同决定电流相位，反相分量负责平均托举。](../figures/phase-04.png){width=88%}

托举力正比于外电流与环电流的乘积，含有恒定项和二倍频项。频率远高于机械响应频率时，宏观位移主要由平均力控制。

![图4-3 瞬时力含二倍频起伏，平均值为正。](../figures/force-04.png){width=92%}

提高频率能增强自感在电路中的作用，但平均力并不无界增大：当$\omega L\gg\mathcal R$时，托举能力趋于有限值。

![图4-4 自感不可忽略；高频托举系数趋于饱和值。](../figures/frequency-04.png){width=88%}

## 四、解题入口

从完整环电路方程开始：

$$
L\frac{di}{dt}+\mathcal R i
=-\frac{d\Phi_{\rm ext}}{dt}
=\omega\mathcal M I_0\sin\omega t.
$$

求出周期稳态电流后，用$F_z=-2\pi R iB_r$取周期平均，再令平均力等于$mg$。最后核查$\omega L/\mathcal R$、发热量以及稳定性条件。

没有必要先猜电流方向。把正方向固定并在电路方程中保留负磁通导数，可自动得到正确的相位和磁力符号。

## 五、解析

（1）计算电阻、质量和互感。

代入题给参数：

$$
\mathcal R=\frac{0.20}{3.7\times10^7\times10^{-6}}
=5.4054054\times10^{-3}\ \Omega,
$$

$$
m=2\pi^2\times2700\times0.10\times10^{-6}
=5.3295864\times10^{-3}\ \mathrm{kg}.
$$

重力为$mg=0.0522299465\ \mathrm N$。外磁通系数为

$$
\mathcal M=\pi(0.10)^2(0.002)\cos30^\circ
=5.4413981\times10^{-5}\ \mathrm H.
$$

（2）求交流稳态环电流。

设$i=a\cos\omega t+b\sin\omega t$，代入方程，比较正弦、余弦系数：

$$
\mathcal R a+\omega Lb=0,
$$

$$
\mathcal R b-\omega La=\omega\mathcal M I_0.
$$

解得

$$
a=-\frac{\omega^2L\mathcal M I_0}
{\mathcal R^2+\omega^2L^2},\qquad
b=\frac{\omega\mathcal R\mathcal M I_0}
{\mathcal R^2+\omega^2L^2}.
$$

因此

$$
\boxed{i(t)=\frac{\mathcal M I_0}
{\mathcal R^2+\omega^2L^2}
\left[-\omega^2L\cos\omega t+
\omega\mathcal R\sin\omega t\right]}.
$$

初始条件引入的瞬态项为$C\exp(-\mathcal Rt/L)$，时间常数为

$$
\frac L{\mathcal R}=1.11\times10^{-4}\ \mathrm s.
$$

经过若干时间常数后，以上周期稳态式适用。环电流幅值为

$$
i_0=\frac{\omega\mathcal M I_0}
{\sqrt{\mathcal R^2+\omega^2L^2}}.
$$

（3）平均竖直磁力。

环上一段线元的径向场磁力为$-iB_r\,d\ell$，积分得到

$$
F_z(t)=-2\pi Rk\sin\alpha\,I_0\cos\omega t\,i(t).
$$

使用$\langle\cos^2\omega t\rangle=1/2$及$\langle\sin\omega t\cos\omega t\rangle=0$，得到

$$
\boxed{\langle F_z\rangle=
\frac{\pi^2R^3k^2\sin\alpha\cos\alpha\,
\omega^2L}{\mathcal R^2+\omega^2L^2}I_0^2}.
$$

其符号为正，即向上。竖直场决定外磁通，径向场决定竖直力；缺少任一分量，当前模型都不能托起圆环。

代入$\omega=2\pi\times10^4\ \mathrm{s^{-1}}$，力的系数为

$$
\frac{\langle F_z\rangle}{I_0^2}
=0.0279171551\ \mathrm{N/A^2}.
$$

令其等于重力：

$$
\boxed{I_0=1.3678051\ \mathrm A\simeq1.37\ \mathrm A}.
$$

这是电磁铁电流的峰值；有效值为$I_0/\sqrt2\simeq0.9672\ \mathrm A$。若给出$1.37\ \mathrm A$却称为有效值，就会使预测平均力增加一倍。

（4）检验自感能否忽略。

本题

$$
\frac{\omega L}{\mathcal R}=6.9743357.
$$

自感阻抗约为电阻的七倍，不能忽略。若设$L=0$，环电流仅含正弦项，与电磁铁电流余弦项正交，平均托举力严格为零。

高频极限为

$$
\boxed{\langle F_z\rangle\longrightarrow
\frac{\pi^2R^3k^2\sin\alpha\cos\alpha}{L}I_0^2}.
$$

这也解释了为什么不能把感应电动势正比于频率就简单推成托举力无限增大。

（5）发热与位置稳定性的边界。

在上述平衡电流下，环电流峰值约为

$$
i_0=122.7904\ \mathrm A.
$$

平均焦耳热功率为

$$
\boxed{\langle P_J\rangle=\frac12\mathcal R i_0^2
=40.74996\ \mathrm W}.
$$

因此这个约$5.33\ \mathrm g$的圆环会显著发热。题目没有给出散热与热容条件，不能由机械平均力平衡进一步推出可长期维持题给电导率的状态。

在给定高度$z_0$，$\langle F_z(z_0)\rangle=mg$只是平衡条件。竖直小扰动稳定还需

$$
\left.\frac{d\langle F_z\rangle}{dz}\right|_{z_0}<0.
$$

原题只有局部场强与方向，未给磁场高度梯度，故此条件无法核验。答案应表述为“在集中参数模型中，约$1.37\ \mathrm A$可使平均托举力等于重力”。

按非磁性导体估算趋肤深度，$\delta=\sqrt{2/(\omega\mu_0\sigma)}\simeq0.827\ \mathrm{mm}$，与导线半径相近。上面的电阻采用直流均匀截面近似，适合题给模型估算；若求真实装置的精确电流，需要交流电阻与具体磁场分布。

## 六、关键洞察

平均力来自与外场反相的电流分量，它由自感产生。这个分量在$L=0$时消失，是判别推导是否正确的直接检验。

![图4-5 平均力平衡、发热和位置稳定性是三个不同的检查项目。](../figures/check-04.png){width=92%}

环电流远大于电磁铁电流并不矛盾：二者几何、电感与电阻不同。所求$1.37\ \mathrm A$明确对应电磁铁，不能误报为圆环中的电流。

## 七、易错点

只用$\mathcal Ri=-d\Phi/dt$忽略自感，会得到零平均力，却与题给自感参数不相容。只凭楞次定律把每个时刻的力都画向上，则漏掉相位过程。

磁通应使用$B_z$而托举力应使用$B_r$；把两者都写成$B$会漏掉$\sin\alpha\cos\alpha$。峰值与有效值、环半径与导线半径也必须分别标记。

“力等于重力”不等于“稳定悬浮”。所给材料称谓与数值不一致，计算须清楚说明采用的是题给导体参数，而不是另加入未给出的铁磁响应。

## 八、课堂讲解建议

教师先固定俯视电流正方向，让学生用叉乘判断径向磁场的竖直力符号。板书随后保留电流的正弦、余弦两项，只在最后取周期平均。

课堂讨论用$L=0$与高频极限检验公式，再把$\langle F\rangle=mg$和$d\langle F\rangle/dz<0$并列，区分局部力平衡和稳定性。

## 九、变式训练

<!-- KEEP_TOGETHER_START -->

变式一：忽略自感但保留电阻，求平均托举力。

解：$i=(\omega\mathcal M I_0/\mathcal R)\sin\omega t$，与$I_{\rm em}=I_0\cos\omega t$乘积的平均为零，故$\langle F_z\rangle=0$。瞬时力仍振荡，但不能平均托起圆环。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式二：频率改为$1\ \mathrm{kHz}$，其他条件不变，平均力平衡所需峰值如何变化？

解：平衡电流满足$I_0^2\propto L+\mathcal R^2/(\omega^2L)$，代入新频率得$I_0\simeq2.36686\ \mathrm A$。低频时电阻造成较大的正交电流比例，托举效率下降；不能按频率的平方简单缩放原电流。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式三：磁场完全竖直或完全径向时，本模型能否托起圆环？

解：完全竖直时$B_r=0$，没有竖直磁力；完全径向时$B_z=0$，没有题设磁通感应。两种情况下$\sin\alpha\cos\alpha=0$，平均托举力均为零。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式四：若局部$k$、$L$及电阻固定而磁场倾角可调，哪一倾角使平均力最大？

解：平均力正比于$\sin\alpha\cos\alpha=\tfrac12\sin2\alpha$，在$0<\alpha<90^\circ$内最大值位于$\alpha=45^\circ$。相对原来$30^\circ$，力增大到$2/\sqrt3$倍，所需电流变为原来的$\sqrt{\sqrt3/2}$，约$1.27289\ \mathrm A$。这一比较只适用于所声明的固定局部参数模型。

<!-- KEEP_TOGETHER_END -->

<!-- question-complete -->
