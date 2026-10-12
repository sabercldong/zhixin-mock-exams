# 第 8 题

质量为 $m$ 的弹性篮球可视为质点，在硬地面上发生完全弹性碰撞，总机械能为 $E$，重力加速度为 $g$，不考虑相对论效应，最大上升高度为 $H$。
（1）若假定 $H=\lambda/2$，其中 $\lambda=h/p_{\max}$，$p_{\max}$ 为最大动量，$h$ 为普朗克常数，求能量 $E$。
（2）题给量子化关系
$$
2\int_0^H p\,dx=\left(n+\frac14\right)h,\qquad n=0,1,2,\ldots
$$
其中 $p$ 为动量。求：a）能级 $E_n$；b）基态能量 $E_0$；c）若粒子是中子，$m_n=1.675\times10^{-27}\,\mathrm{kg}$、$g=10\,\mathrm{m\,s^{-2}}$，求由该关系得到的基态对应高度 $H_0$。
（3）用基态能量 $E_0$ 与经典往返运动的频率 $f$ 相比，求 $E_0/f$，并讨论数量级。取 $h=6.62607015\times10^{-34}\,\mathrm{J\,s}$。
题给量子化关系在下述解析中按题设计算，同时与通常无限高硬壁的边界条件进行区分。

![图 8-1　重力场中的弹性反弹与最大高度。](../figures/question-08.png)

## 一、题型定位

这是从经典反弹轨道建立作用量、再研究重力势中的半经典量子化问题。它包含一个启发式波长猜测、一条指定量子化公式和一个频率尺度比较。三部分的逻辑地位不同：猜测不是严格边界条件，给定公式也不自动等于真实硬壁的正确量子化。
对于通常无限高势垒形成的硬地面，波函数在地面为零，半经典偏移应为 $3/4$，而不是题给的 $1/4$。下面先完整计算题设结果，再独立推导硬壁结果及精确的线性势能解，不混用两套基态数值。

## 二、知识点

经典运动满足 $E=p^2/(2m)+mgz$。顶点 $p=0$、高度 $H=E/(mg)$；地面 $z=0$ 时动量最大。德布罗意关系 $\lambda=h/p$ 随高度改变，不能把地面波长当作整个重力区的恒定波长。
一个完整反弹周期的作用量为相空间闭合轨道面积 $\oint p\,dz$。上升和下降的动量符号相反，但积分方向也相反，因此两段贡献同号。半经典相位偏移来自转向点连接和地面边界。
量子定态能量与经典轨道频率可作尺度比较，但定态不是沿一条经典轨道反复碰撞的小球。相邻量子能级的跃迁频率另由能量差除以 $h$ 定义。

## 三、物理图像

把地面设为 $z=0$，取上方重力势为 $mgz$。经典质点在 $0\le z\le H$ 之间运动，地面瞬时反向，顶点平滑转向。相空间轨道具有上升支 $p>0$、下降支 $p<0$ 和地面瞬时反射的竖直连接。
量子硬壁模型在 $z<0$ 取无限大势，在 $z>0$ 取线性势。顶点以上是经典禁阻区，波函数衰减而非立即消失。所谓 $H_0$ 应理解为基态能量对应的经典转向高度，不是量子位置分布的严格最大值。

## 四、解题入口

所有积分前先写 $p(z)=\sqrt{2m(E-mgz)}$ 和 $H=E/(mg)$，不要把 $p$ 当作常数。用代换 $u=E-mgz$ 完整计算作用量，再统一求解 $E^{3/2}$。
求经典频率时先求上升时间再乘二。最后把指定偏移 $1/4$ 和硬壁偏移 $3/4$ 分开，并以薛定谔方程的艾里函数零点核验物理边界。

## 五、解析

（1）经典能量关系与最大动量。

地面为零势能位置，任意高度
$$
E=\frac{p(z)^2}{2m}+mgz.
$$
顶点 $p(H)=0$，所以
$$
\boxed{H=\frac E{mg}.}
$$
地面处势能最小，动量大小最大：
$$
\boxed{p_{\max}=\sqrt{2mE}.}
$$
上升时 $p$ 为正，下降时为负；$p_{\max}$ 在波长关系中表示大小，不包含方向。

（2）按第（1）问的波长猜测求能量。

题给 $H=\lambda/2$，且 $\lambda=h/p_{\max}$，故
$$
\frac E{mg}=\frac h{2\sqrt{2mE}}.
$$
两边乘以 $2mg\sqrt{2mE}$：
$$
2E\sqrt{2mE}=mgh.
$$
整理平方根：
$$
2\sqrt{2m}\,E^{3/2}=mgh.
$$
两边均为正，只取正能量根：
$$
\begin{aligned}
E^{3/2}&=\frac{mgh}{2\sqrt{2m}},\\
E^3&=\frac{m^2g^2h^2}{8m}
=\frac{mg^2h^2}{8},\\
E_{\rm guess}&=\boxed{\left(\frac{mg^2h^2}{8}\right)^{1/3}.}
\end{aligned}
$$
这里的立方根不是数学上的所有复根，而是机械能的正实根。能量随 $m^{1/3}$ 而非 $m$ 变化，体现此处施加了含 $h$ 的非经典尺度关系。
此猜测只用地面波长，而在顶点 $p\to0$、局部波长趋大；它未满足实际波函数的边界条件，不应称为精确基态能量。

（3）画出势能与动量随高度的关系。

图8-2中的水平能量线与 $mgz$ 相交于 $H$。线性势不意味着动量线性：
$$
p(z)=\sqrt{2m(E-mgz)}
=\sqrt{2mE}\sqrt{1-\frac zH}.
$$
因此靠近顶点时 $p$ 按平方根趋零。

![图 8-2　线性重力势、能量线与经典转向高度。](../figures/potential-08.png)

用 $p_{\max}H$ 粗代积分会漏掉动量下降的面积比例。作用量积分必须沿整个高度计算。

（4）为什么完整周期的作用量有系数二。

上升支从 $0$ 到 $H$，动量 $p_+(z)=+\sqrt{2m(E-mgz)}$。下降支从 $H$ 到 $0$，动量 $p_-(z)=-p_+(z)$。因此
$$
\begin{aligned}
J(E)&=\oint p\,dz\\
&=\int_0^Hp_+(z)\,dz+\int_H^0p_-(z)\,dz\\
&=\int_0^Hp_+(z)\,dz+\int_0^Hp_+(z)\,dz\\
&=2\int_0^H\sqrt{2m(E-mgz)}\,dz.
\end{aligned}
$$
地面瞬时反射在相图中为竖直线，沿它 $dz=0$，故不另加作用量。图8-3的闭合面积由两条平方根支路包围，并不是矩形面积 $2p_{\max}H$。

![图 8-3　反弹相空间轨道及作用量面积。](../figures/action-08.png)

（5）逐步完成作用量积分。

设
$$
u=E-mgz,\qquad dz=-\frac{du}{mg}.
$$
当 $z=0$ 时 $u=E$；当 $z=H=E/(mg)$ 时 $u=0$。因此
$$
\begin{aligned}
J(E)
&=2\sqrt{2m}\int_0^{E/(mg)}(E-mgz)^{1/2}\,dz\\
&=-\frac{2\sqrt{2m}}{mg}\int_E^0u^{1/2}\,du\\
&=\frac{2\sqrt{2m}}{mg}\int_0^Eu^{1/2}\,du\\
&=\frac{2\sqrt{2m}}{mg}\left[\frac23u^{3/2}\right]_0^E\\
&=\boxed{\frac{4\sqrt{2m}}{3mg}E^{3/2}.}
\end{aligned}
$$
代换中的负号由反转上下限消去，最终作用量为正。另用 $s=z/H$ 可独立核验：
$$
J=2p_{\max}H\int_0^1\sqrt{1-s}\,ds
=\frac43p_{\max}H.
$$
因 $\int_0^1\sqrt{1-s}\,ds=2/3$，闭合面积确为对应矩形的 $2/3$。

（6）按题给偏移 $1/4$ 求全能级。

先用统一记号 $\delta$ 表示偏移：
$$
J(E_n)=(n+\delta)h.
$$
联立积分结果：
$$
\begin{aligned}
\frac{4\sqrt{2m}}{3mg}E_n^{3/2}&=(n+\delta)h,\\
E_n^{3/2}&=\frac{3mgh}{4\sqrt{2m}}(n+\delta).
\end{aligned}
$$
平方后
$$
E_n^3=\frac{9m^2g^2h^2}{32m}(n+\delta)^2.
$$
所以
$$
\boxed{E_n(\delta)=
\left[\frac{9mg^2h^2}{32}(n+\delta)^2\right]^{1/3}.}
$$
严格按题给关系取 $\delta=1/4$：
$$
\boxed{E_n^{\rm given}=
\left[\frac{9mg^2h^2}{32}\left(n+\frac14\right)^2\right]^{1/3}.}
$$
$n=0$ 时
$$
\boxed{E_0^{\rm given}=
\left(\frac{9mg^2h^2}{512}\right)^{1/3}.}
$$
它与第一问猜测的比值为
$$
\frac{E_0^{\rm given}}{E_{\rm guess}}
=\left(\frac{9}{64}\right)^{1/3},
$$
两者不相等。不能因为都是量子尺度估算就强行统一系数。

（7）题给关系的中子基态数值。

先写常数：
$$
m_n=1.675\times10^{-27}\,\mathrm{kg},\quad
g=10\,\mathrm{m\,s^{-2}},\quad
h=6.62607015\times10^{-34}\,\mathrm{J\,s}.
$$
计算 $h^2$：
$$
h^2=4.39048056\times10^{-67}\,\mathrm{J^2s^2}.
$$
立方根内量为
$$
\begin{aligned}
\frac9{512}m_ng^2h^2
&=\frac9{512}(1.675\times10^{-27})
(10^2)(4.39048056\times10^{-67})\\
&\simeq1.292\times10^{-93}\,\mathrm{J^3}.
\end{aligned}
$$
开立方后
$$
\boxed{E_0^{\rm given}=1.08935\times10^{-31}\,\mathrm J.}
$$
高度不是再开一次平方根，而是由势能直接除：
$$
\begin{aligned}
H_0^{\rm given}
&=\frac{E_0^{\rm given}}{m_ng}\\
&=\frac{1.08935\times10^{-31}}{1.675\times10^{-26}}\\
&=\boxed{6.50357\times10^{-6}\,\mathrm m
=6.50357\,\mathrm{\mu m}.}
\end{aligned}
$$
这里用的是 $g=10$ 和题给 $1/4$。后面物理硬壁的高度不能再用这个数值代入而改变标签。

（8）完整推导经典往返频率。

对于能量 $E$，地面向上初速度为
$$
v_0=\frac{p_{\max}}m=\sqrt{\frac{2E}{m}}.
$$
上升过程 $v=v_0-gt$，到顶点 $v=0$，所以
$$
t_{\uparrow}=\frac{v_0}g.
$$
下降时间由时反演对称性相同，地面理想瞬时反射时间取零。完整周期与频率：
$$
\begin{aligned}
T_{\rm cl}
&=\frac{2v_0}g
=\frac2g\sqrt{\frac{2E}m}
=2\sqrt{\frac{2H}g},\\
f_{\rm cl}(E)
&=\boxed{\frac g2\sqrt{\frac m{2E}}.}
\end{aligned}
$$
若只用上升时间倒数，会多出一倍频率。本题“单位时间跳跃次数”按地面到地面的一次完整周期计数。

（9）计算 $E/f$，明确频率的意义。

先不使用量子化：
$$
\begin{aligned}
\frac E{f_{\rm cl}(E)}
&=ET_{\rm cl}\\
&=\frac{2\sqrt2}{g\sqrt m}E^{3/2}.
\end{aligned}
$$
再由统一量子化关系代入
$$
E_n^{3/2}
=\frac{3mgh}{4\sqrt{2m}}(n+\delta),
$$
得到
$$
\begin{aligned}
\frac{E_n}{f_{\rm cl}(E_n)}
&=\frac{2\sqrt2}{g\sqrt m}
\frac{3mgh}{4\sqrt{2m}}(n+\delta)\\
&=\boxed{\frac32(n+\delta)h.}
\end{aligned}
$$
严格按题给基态：
$$
\boxed{\frac{E_0^{\rm given}}{f_{\rm cl}(E_0^{\rm given})}
=\frac38h=2.48478\times10^{-34}\,\mathrm{J\,s}.}
$$
对应经典频率约 $438.41\,\mathrm{Hz}$。比值与 $h$ 同数量级且独立于 $m,g$，反映作用量量子尺度；它不是严格的 $E=hf$，因为这里 $f$ 是能量为 $E$ 的经典轨道频率，而非某个量子跃迁频率。

（10）由硬壁边界推导正确的半经典相位。

通常“硬地面”的量子模型是 $z<0$ 势能无限大，故
$$
\psi(0)=0.
$$
在上方平滑转向点 $H$，可衰减的禁阻区解连接到允许区，半经典波函数形式为
$$
\psi(z)\propto\frac1{\sqrt{p(z)}}
\sin\left[\frac1{\hbar}\int_z^Hp(s)\,ds+\frac\pi4\right],
\qquad \hbar=\frac h{2\pi}.
$$
$\pi/4$ 来自一个平滑转向点的连接相位。地面边界要求
$$
\sin\left[\frac1{\hbar}\int_0^Hp(s)\,ds+\frac\pi4\right]=0.
$$
最小允许正作用量对应正整数 $k=1$：
$$
\frac1{\hbar}\int_0^Hp(s)\,ds+\frac\pi4=k\pi.
$$
令 $n=k-1=0,1,\ldots$：
$$
\begin{aligned}
\int_0^Hp(s)\,ds
&=\left(n+\frac34\right)\pi\hbar,\\
J(E_n)&=\boxed{\left(n+\frac34\right)h.}
\end{aligned}
$$
因此题给的 $1/4$ 不能直接代表通常无限高硬壁的狄利克雷边界。反射完全弹性只描述经典速度反向；要把它转成量子问题，还必须明确反射相位或波函数边界。

（11）正确硬壁的半经典结果及数值。

取 $\delta=3/4$：
$$
\boxed{E_n^{\rm WKB}=
\left[\frac{9mg^2h^2}{32}\left(n+\frac34\right)^2\right]^{1/3}.}
$$
基态比题给值增加
$$
\frac{E_0^{\rm WKB}}{E_0^{\rm given}}
=\left(\frac{3/4}{1/4}\right)^{2/3}
=3^{2/3}.
$$
中子对应
$$
\boxed{H_0^{\rm WKB}=13.5280\,\mathrm{\mu m},\qquad
E_0^{\rm WKB}\simeq2.26593\times10^{-31}\,\mathrm J.}
$$
在同一半经典模型内
$$
\boxed{\frac{E_0^{\rm WKB}}{f_{\rm cl}(E_0^{\rm WKB})}
=\frac98h.}
$$
硬壁地面不是第二个平滑转向点，不能套用两个平滑转向点的 $n+1/2$。半经典近似在低能级不精确，基态还需与精确方程比较。

（12）从薛定谔方程独立求线性势的精确解。

在 $z>0$，
$$
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dz^2}+mgz\psi=E\psi.
$$
引入特征长度
$$
\boxed{\ell_g=\left(\frac{\hbar^2}{2m^2g}\right)^{1/3}},
\qquad
u=\frac z{\ell_g}-\frac E{mg\ell_g}.
$$
因为 $d/dz=(1/\ell_g)d/du$，方程成为
$$
-\frac{\hbar^2}{2m\ell_g^2}\frac{d^2\psi}{du^2}
+mg\ell_gu\psi=0.
$$
由 $\ell_g^3=\hbar^2/(2m^2g)$ 得
$$
\frac{\hbar^2}{2m\ell_g^2}=mg\ell_g.
$$
约去系数：
$$
\boxed{\frac{d^2\psi}{du^2}-u\psi=0.}
$$
这是艾里方程。两个独立解中 $\operatorname{Ai}(u)$ 在 $u\to+\infty$ 衰减，$\operatorname{Bi}(u)$ 增长；可归一化要求舍去后者：
$$
\psi(z)=C\operatorname{Ai}\left(\frac z{\ell_g}-\frac E{mg\ell_g}\right).
$$
硬壁边界 $\psi(0)=0$ 给
$$
\operatorname{Ai}\left(-\frac E{mg\ell_g}\right)=0.
$$
令 $a_k>0$ 为 $\operatorname{Ai}(-a_k)=0$ 的第 $k$ 个正参数，则
$$
\boxed{E_n^{\rm exact}=mg\ell_g a_{n+1},\qquad
H_n^{\rm exact}=\ell_g a_{n+1}.}
$$

（13）精确中子基态与半经典误差。

取
$$
a_1=2.3381074105,\qquad
\ell_g=5.83038949\,\mathrm{\mu m},
$$
因此
$$
\boxed{
H_0^{\rm exact}=13.6321\,\mathrm{\mu m},\qquad
E_0^{\rm exact}=2.28337\times10^{-31}\,\mathrm J.}
$$
半经典高度的相对误差
$$
\frac{H_0^{\rm WKB}-H_0^{\rm exact}}{H_0^{\rm exact}}
\simeq-0.764\%.
$$
图8-4的波函数在地面为零，并在各自转向点外衰减。顶点外仍存在位置概率，因此不能把 $H_0^{\rm exact}$ 称为不可越过的高度上界。

![图 8-4　硬壁线性势的低能定态及转向点外的衰减。](../figures/states-08.png)

对于精确基态，再用经典频率作尺度比较时，$E_0/f_{\rm cl}(E_0)$ 略大于半经典的 $9h/8$；不能在精确能量里仍强制代入半经典相位公式。

（14）题给 $1/4$ 对应什么边界，以及应怎样使用答案。

若地面采用另一种理想反射边界 $\psi'(0)=0$，半经典地面条件近似为
$$
\cos\left[\frac1\hbar\int_0^Hp\,dz+\frac\pi4\right]=0,
$$
从而给 $J\simeq(n+1/4)h$。精确条件则是 $\operatorname{Ai}'(-a)=0$。这种诺伊曼反射边界不等于无限高势垒的通常硬壁。
因此本题给定关系可以作为一道指定半经典模型的计算题，但若解释为通常硬地面，应把偏移修正为 $3/4$，且基态只能称半经典近似。正文保留两种结果，是为了明确模型条件，而不是把不同答案并列而不判断。

（15）经典作用量与周期的交叉检验。

对完整作用量求导：
$$
\begin{aligned}
\frac{dJ}{dE}
&=\frac{4\sqrt{2m}}{3mg}\frac32E^{1/2}\\
&=\frac{2\sqrt{2mE}}{mg}\\
&=\frac2g\sqrt{\frac{2E}m}=T_{\rm cl}.
\end{aligned}
$$
这独立恢复了上升加下降的周期。对高量子数，邻近能级差由微分近似：
$$
\Delta E\simeq\frac h{dJ/dE}=hf_{\rm cl}.
$$
所以高能级间的跃迁频率逐渐趋于经典轨道频率，这才是半经典对应关系。基态的 $E_0/h$ 和跃迁频率不必相同。

（16）量纲、非相对论及尺度检查。

$mg^2h^2$ 的量纲为
$$
\mathrm{kg}\,(\mathrm{m\,s^{-2}})^2
(\mathrm{kg\,m^2\,s^{-1}})^2
=\mathrm{kg^3m^6s^{-6}}=\mathrm{J^3}.
$$
开立方确为能量；$E/f$ 的量纲为作用量，与 $h$ 相同。中子微米高度对应地面速度约厘米每秒，远小于光速，非相对论假设自洽。
当 $h\to0$，固定低量子数的能量与高度趋零；当 $n\to\infty$，$E_n\propto n^{2/3}$，相邻间距逐渐减小，而不是等间距。$m$ 增大时能量 $\propto m^{1/3}$、高度 $\propto m^{-2/3}$，宏观篮球的最低量子高度极小，经典可见跳跃含极大量子数。

## 六、关键洞察

作用量比值有一个不依赖量子化的经典关系。因 $J=(4/3)p_{\max}H$，而
$$
ET_{\rm cl}
=mgH\frac{2p_{\max}}{mg}
=2p_{\max}H,
$$
所以
$$
ET_{\rm cl}=\frac32J.
$$
这解释了 $E/f=(3/2)(n+\delta)h$ 的系数来源，而不是一次神秘的消元。

硬壁精确态的期望势能还可通过尺度变换求出。令归一化波函数试探为 $\psi_s(z)=s^{1/2}\psi(sz)$，地面边界保持零。动能变为 $s^2\langle K\rangle$，势能变为 $s^{-1}\langle V\rangle$。定态在 $s=1$ 的一阶变分为零：
$$
2\langle K\rangle-\langle V\rangle=0.
$$
于是
$$
\langle K\rangle=E/3,\quad
\langle V\rangle=2E/3,\quad
\langle z\rangle=\frac{2E}{3mg}=\frac23H.
$$
平均高度不等于经典转向高度；地面处 $z=0$ 使无限势垒的尺度边界项不改变此关系。

精确低两级的能量差给中子跃迁频率
$$
f_{10}=\frac{mg\ell_g(a_2-a_1)}h
\simeq257.90\,\mathrm{Hz},
$$
其中 $a_2=4.08794944$。它与给定偏移下的经典基态频率 $438.41\,\mathrm{Hz}$ 不是同一个模型中的同一个物理量，不能直接比较后声称能量不守恒。

## 七、易错点

在作用量中把 $p$ 提出积分；下降段忘记积分方向也反向；将半周期当周期；把 $h$ 与 $\hbar$ 混用；将本题 $n=0$ 和艾里零点从 $k=1$ 开始的索引混为一谈。

将猜测 $H=\lambda/2$ 说成精确量子化，或照抄 $n+1/4$ 而不讨论硬壁边界，都会把代数正确误当作物理模型正确。硬壁和光滑转向点的相位贡献不同，不能都按同一种反射处理。

把量子基态描述成有确定轨道和周期的微小弹跳，或将转向高度说成量子粒子不可超过的最高位置，会混淆经典对应量与位置概率。以同一标签混用给定模型、正确半经典模型和精确模型的能量数值也应避免。

## 八、课堂讲解建议

先只讲经典部分，让学生把上升和下降两段画到相空间，观察两个负号如何抵消。完整写一次代换积分，再从作用量求导恢复周期，建立两条可互查的路线。

量子部分先把题给公式当计算条件，算出答案后再提出边界问题。用“地面节点”和“顶点外衰减”两件事说明硬壁模型，不要求初学者凭记忆背相位。艾里函数部分可先展示微分方程如何无量纲化，再说明零点由边界筛选能量。

最后将三种高度明确列为猜测、题设半经典值和物理硬壁精确值，强调学习目标是分清模型而不是机械记住几个微米数字。

## 九、变式训练

（1）保持中子质量，将重力加速度从 $10$ 改为 $g'=g/8$，求硬壁精确基态高度、能量和量子跃迁频率的比例。

解：由 $\ell_g\propto g^{-1/3}$，
$$
\frac{\ell_g'}{\ell_g}=2.
$$
零点 $a_k$ 不变，故
$$
H_0'=2H_0=27.2642\,\mathrm{\mu m}.
$$
$E_n=mg\ell_g a_{n+1}\propto g^{2/3}$：
$$
E_0'=E_0/4,\qquad f_{10}'=f_{10}/4\simeq64.476\,\mathrm{Hz}.
$$
低重力使高度增大、能量间隔变小，并非高度与能量同时增加。

（2）在半经典硬壁模型中，求从 $n$ 到 $n+1$ 的能级间距，并证明高能级下跃迁频率趋于经典频率。

解：设
$$
C_E=\left(\frac{9mg^2h^2}{32}\right)^{1/3}.
$$
则精确的半经典差分为
$$
\Delta E_n=C_E\left[
\left(n+\frac74\right)^{2/3}
-\left(n+\frac34\right)^{2/3}\right].
$$
令 $q=n+3/4\gg1$，利用二项展开：
$$
(q+1)^{2/3}
=q^{2/3}\left(1+\frac{2}{3q}
-\frac1{9q^2}+O(q^{-3})\right).
$$
因此
$$
\Delta E_n=\frac23C_Eq^{-1/3}
\left(1-\frac1{6q}+O(q^{-2})\right).
$$
由 $dJ/dE=T_{\rm cl}$ 和 $dJ/dn=h$，
$$
\frac{dE}{dn}=\frac h{T_{\rm cl}}=hf_{\rm cl}.
$$
领先项 $(2/3)C_Eq^{-1/3}$ 正是 $hf_{\rm cl}(E_n)$，相对误差随 $1/n$ 消失。该结果建立对应原理，不能推广为所有低能级都满足 $\Delta E=hf_{\rm cl}$ 的精确恒等式。

（3）采用硬壁精确Airy定态，求平均高度、势能与动能。

解：固定量子数的$E_n=mg\ell_g a_{n+1}\propto g^{2/3}$。参数微分定理$dE_n/dg=m\langle y\rangle$给
$$\langle y\rangle=\frac{2E_n}{3mg},\quad
\langle V\rangle=\frac{2E_n}3,\quad \langle K\rangle=\frac{E_n}3.$$
平均高度是经典转向高度的$2/3$，不能互换。壁面定义域随$g$不变且$\psi(0)=0$允许上述微分；定态概率分布不代表实际经典跳跃轨道。

（4）求精确基态到第一激发态能隙频率，并与基态转向高度对应的经典弹跳频率比较。

解：正Airy零点$a_1=2.3381074105,a_2=4.0879494441$，$\nu_{10}=mg\ell_g(a_2-a_1)/h$，经典频率$f_{\rm cl}=g\sqrt{m/(2E_0)}/2$。利用$\ell_g^3=\hbar^2/(2m^2g)$，
$$\frac{\nu_{10}}{f_{\rm cl}(E_0)}=\frac{(a_2-a_1)\sqrt{a_1}}{\pi}<1.$$
只有高能级才渐近出现能隙与经典频率的一致。该频率只是能隙标度，观测跃迁还需激励机制及相应选择规则。
