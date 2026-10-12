# 第2题

<!-- question-start -->

质量为$m$、半径为$r$、长度为$l$的均匀圆柱体放在倾角为$\theta$的粗糙斜面上。固定在圆柱上的矩形导线框由两端面上的直径和连接端点的两条母线组成，通以恒定电流$I$。匀强磁场大小为$B$，方向竖直向上。初始线框平面水平，圆柱由静止释放，求使其不沿无限长斜面滚下的最小电流。

取初始磁矩竖直向上，即初始线框与磁场同向；斜面足够粗糙，圆柱作纯滚动。若电流反向使初始磁矩向下，下述阻止滚下的势垒模型不适用。

![图2-1 矩形线框随圆柱转动，初始磁矩竖直向上。](../figures/question-02.png){width=88%}

<!-- question-end -->

## 一、题型定位

这是保守力矩作用下的滚动与临界势垒问题。要求“不无限滚下”不是要求释放瞬间平衡，也不是只要求某处存在静态平衡点，而是要求初始机械能不能跨越沿下坡方向的第一道势垒。

恒定重力驱动力矩与周期性的磁力矩竞争，形成向下倾斜的周期势能。临界电流由一个非零超越方程确定，圆柱转动惯量影响到达势垒的时间，却不影响临界能量条件。

## 二、知识点

线框面积为两端直径与圆柱长度的乘积，磁矩大小为

$$
\mu=2rlI.
$$

匀强磁场中闭合线框的总磁力为零，但磁力矩一般不为零。相对初始位置转过$\varphi$后，磁势能变化为

$$
U_B=\mu B(1-\cos\varphi).
$$

纯滚动使沿斜面位移为$s=r\varphi$。重力势能变化为$-mgr\sin\theta\,\varphi$。

均匀圆柱绕轴转动惯量$J=mr^2/2$，总动能包含平动和转动：

$$
K=\frac12(J+mr^2)\dot\varphi^2
=\frac34mr^2\dot\varphi^2.
$$

静摩擦维持纯滚动而不耗散机械能。只要题设的纯滚动条件成立，机械能守恒可以用于从释放位置到转折点的整个过程。

## 三、物理图像

重力势能沿下坡转角线性降低，磁势能则周期起伏。它们相加后，起点附近势能先下降，圆柱一定先向下加速。

![图2-2 重力与磁作用形成倾斜周期势能，临界曲线与初始能量相切。](../figures/potential-02.png){width=92%}

磁力矩达到最大时，仍可能不足以追回圆柱之前积累的动能。因此“最大磁力矩大于重力力矩”只是产生平衡点的必要条件。

![图2-3 静态力矩门槛与阻挡初始轨迹的能量门槛不同。](../figures/threshold-02.png){width=88%}

临界状态下，圆柱无限缓慢地接近一个不稳定平衡点。更大的电流使初始轨迹在势垒之前转向，随后在有限区间内往复滚动。

![图2-4 临界点位于磁力矩下降区，是不稳定平衡位置。](../figures/torque-02.png){width=88%}

## 四、解题入口

以起点势能为零，写出总势能：

$$
U(\varphi)=\mu B(1-\cos\varphi)-C\varphi,
\qquad C=mgr\sin\theta.
$$

定义无量纲强度

$$
\lambda=\frac{\mu B}{C}
=\frac{2lIB}{mg\sin\theta}.
$$

临界势垒必须同时满足$U(\varphi_*)=0$和$U'(\varphi_*)=0$。前者是能量条件，后者是与初始能量线相切的条件。

应排除$\varphi=0$这个形式解，因为释放位置的势能斜率为$-C$，它不是阻挡下坡运动的势垒。

## 五、解析

（1）机械能与允许区间。

初始静止、$U(0)=0$，因此

$$
\frac34mr^2\dot\varphi^2+
\mu B(1-\cos\varphi)-C\varphi=0.
$$

所以

$$
\dot\varphi^2=
\frac{4C}{3mr^2}
\left[\varphi-\lambda(1-\cos\varphi)\right].
$$

只有方括号非负的区域能够到达。若第一周期的势垒顶仍低于零，圆柱会越过第一道势垒；以后各周期的势垒再降低$2\pi C$，因而再也无法阻挡它。

最小电流对应第一道势垒恰好达到初始能量。用$0<\varphi<2\pi$表示第一周期，势垒达到零需要

$$
\lambda\geq\frac{\varphi}{1-\cos\varphi}
$$

在某个非零转角成立。因此

$$
\lambda_{\min}=\min_{0<\varphi<2\pi}
\frac{\varphi}{1-\cos\varphi}.
$$

（2）求临界转角。

对上式求导：

$$
\frac{d}{d\varphi}
\frac{\varphi}{1-\cos\varphi}
=\frac{1-\cos\varphi-\varphi\sin\varphi}
{(1-\cos\varphi)^2}.
$$

极小值满足

$$
1-\cos\varphi_*=\varphi_*\sin\varphi_*.
$$

使用半角恒等式并排除零解，化为

$$
\boxed{\tan\frac{\varphi_*}{2}=\varphi_*},
\qquad 0<\varphi_*<\pi.
$$

数值解为

$$
\varphi_*=2.3311223704\ \mathrm{rad}
\simeq133.563^\circ.
$$

于是

$$
\lambda_{\min}=
\frac{\varphi_*}{1-\cos\varphi_*}
=\frac1{\sin\varphi_*}
=1.3800501397.
$$

（3）最小电流。

将$\mu=2rlI$与$C=mgr\sin\theta$代回：

$$
\boxed{I_{\min}=0.6900250698\,
\frac{mg\sin\theta}{Bl}}.
$$

半径$r$消去，是因为线框磁力矩和重力滚动力矩都与$r$成正比。转动惯量没有出现在临界电流中，是因为释放状态与临界势垒处均无动能。

如果把磁力矩最大值恰等于重力驱动力矩作为答案，会得到$I=mg\sin\theta/(2Bl)$，比正确值偏小约$27.54\%$。在这个值下仅出现一个水平切线，势垒仍低于初始机械能。

（4）临界电流是否真正能阻止无限滚下。

在临界点，

$$
U''(\varphi_*)=\mu B\cos\varphi_*<0.
$$

令$\delta=\varphi_* -\varphi>0$，临近势垒时

$$
U(\varphi)\simeq
\frac12\mu B\cos\varphi_*\,\delta^2.
$$

因此$\dot\varphi\propto\delta$，到达临界点的时间满足

$$
t\propto\int\frac{d\varphi}{\varphi_* -\varphi},
$$

对数发散。圆柱沿下坡方向的位移渐近于$r\varphi_*$，不会无限增大。故在严格理想模型中，临界值本身已满足“不无限滚下”。

若要求在有限时间内停住并回滚，则需要$I>I_{\min}$；这一要求比原问题更强。

（5）纯滚动所需的粗糙程度。

令$f$表示向上的摩擦力大小，平动方程为

$$
ma=mg\sin\theta-f.
$$

下坡转动为正，转动方程为

$$
J\frac ar=fr-\mu B\sin\varphi.
$$

消元后得

$$
a=\frac23g\sin\theta-
\frac{2\mu B}{3mr}\sin\varphi,
$$

$$
f=\frac13mg\sin\theta+
\frac{2\mu B}{3r}\sin\varphi.
$$

在临界轨迹从零到$\varphi_*$的区间，$\sin\varphi$达到1，法向力为$mg\cos\theta$。因此临界纯滚动至少要求

$$
\boxed{\mu_s\geq\frac{1+2\lambda_{\min}}3\tan\theta
=1.2533667598\tan\theta}.
$$

题设“粗糙”在这里应理解为摩擦足以支持上述纯滚动，而不是引入耗散性的滑动摩擦。

## 六、关键洞察

阻止一段已经开始的运动需要足够高的势垒，而仅仅出现一个平衡点不够。临界问题的两条方程$U=E_0$与$U'=0$，分别约束能量和势垒几何形状。

![图2-5 势垒判据同时检查能量相切及释放轨迹的可达性。](../figures/check-02.png){width=92%}

临界电流与转动惯量无关；动态过程却与惯量有关。更换空心圆柱会改变滚动的速度与摩擦需求，但在同样磁矩和重力条件下不会改变能量势垒的临界值。

## 七、易错点

将线框面积写成$\pi r^2$会误用端面圆的面积；本题矩形面积是$2rl$。将均匀磁场对线框的力矩误作对质心的净力，也会导致错误的平动方程。

只用$\mu B\geq mgr\sin\theta$会漏掉从初始水平线框转到势垒之前积累的动能。求超越方程时保留$\varphi=0$则会混淆释放位置和真正势垒。

把临界状态描述为“有限时间达到势垒后停住”，不符合保守系统中不稳定平衡点的渐近运动。

## 八、课堂讲解建议

教师先画倾斜的周期势能，标出释放能量线。让学生分别求静态门槛与能量门槛，再解释为何后者更大。

板书保留$U=0$和$U'=0$两式并列，通过相除得到半角方程。课堂讨论可用空心圆柱比较“临界条件不变、运动时间改变”的两种结论。

## 九、变式训练

<!-- KEEP_TOGETHER_START -->

变式一：将圆柱换为同质量、同半径的薄壁圆筒，线框保持不变，最小电流如何变化？

解：$J$由$mr^2/2$变为$mr^2$，但初态与临界点的动能仍为零，总势能不变。因此$I_{\min}$不变；运动方程中的有效惯量由$3mr^2/2$变为$2mr^2$，同一允许位置的角速度降低到原来的$\sqrt{3/4}$。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式二：仅要求存在静态平衡位置，电流至少多大？

解：由$\mu B\sin\varphi=C$，存在平衡点的条件是$\lambda\geq1$，故$I\geq mg\sin\theta/(2Bl)$。$\lambda>1$时，$\varphi_s=\arcsin(1/\lambda)$是稳定点，而$\pi-\varphi_s$是不稳定点；释放状态是否被势垒阻挡还需能量判据。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式三：取$\lambda=2$，求从静止释放后的第一个转折角。

解：求$2(1-\cos\varphi_t)=\varphi_t$的第一个正根，得$\varphi_t\simeq1.10914418\ \mathrm{rad}$。该角小于$\pi/2$，圆柱在磁力矩上升区已失去全部动能并回滚；位移上界是$1.10914418r$。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式四：在稳定平衡点附近作小振动，求均匀圆柱的角频率。

解：写$\varphi=\varphi_s+\eta$，线性化得$(J+mr^2)\ddot\eta+\mu B\cos\varphi_s\eta=0$，故

$$
\boxed{\Omega=\sqrt{\frac{2\mu B\cos\varphi_s}{3mr^2}}}.
$$

$\lambda\downarrow1$时$\cos\varphi_s\to0$，振动频率趋于零；不能把不稳定平衡点的负曲率代入后仍解释为实频率振动。

<!-- KEEP_TOGETHER_END -->

<!-- question-complete -->
