# 第3题

<!-- question-start -->
平行板电容器的两板水平放置，面积为 $S$、间距为 $l$，接在恒压电源 $U_0$ 上，上板带正电，忽略边缘效应。质量为 $m$、带电量为 $+q$ 的小球，用长为 $h$ 的轻绝缘绳系在上板的点 $O$。小球初始在水平面内做圆周运动，绳与竖直方向夹角为 $\theta$。

把电容器下板缓缓下移 $\Delta l$，假定小球始终近似保持水平圆周运动，求绳角变化 $\Delta\theta$，保留一阶小量。重力加速度为 $g$。

原题提示“不考虑角动量不守恒的问题”。本解按无外加轴向力矩的轴对称模型处理：竖直轴角动量守恒，角速度可缓慢变化，不能额外假设角速度恒定。小球须始终位于两板之间，即 $h\cos\theta<l$。

![图3-1 上正下负的电场向下，电力与重力同向，绳的倾角从竖直量起。](../figures/question-03.png)

<!-- question-end -->

## 一、题型定位

这是带电圆锥摆的准静态参数变化题。恒定电压使极板间距改变时电场也改变，圆锥摆的平衡角随之调整。求角度变化既要用瞬时圆周运动方程，也要用控制不同瞬时状态之间的约束。

圆周运动方程本身只给出角速度与角度的关系，并不能单独确定二者如何同时变化。本题没有施加绕竖直轴的力矩，因此守恒的是轴向角动量。缓慢移板使垂直方向的平衡近似成立，并不把角速度锁在初始值。

## 二、知识点

理想平行板电场的大小为

$$
E=\frac{U_0}{l}.
$$

电场向下，正电小球所受电力也向下。记总的向下恒力为

$$
W(l)=mg+\frac{qU_0}{l}.
$$

这里 $W$ 是力，不是势能。设绳张力为 $T$，小球绕竖直轴的角速度为 $\omega$，轨道半径为 $a=h\sin\theta$，则

$$
T\cos\theta=W,
\qquad T\sin\theta=m\omega^2h\sin\theta.
$$

对非退化圆锥摆 $0<\theta<\pi/2$，有

$$
T=mh\omega^2,
\qquad \omega^2=\frac{W}{mh\cos\theta}.
$$

轴向角动量为

$$
J=m a^2\omega=mh^2\sin^2\theta\,\omega.
$$

重力、电力均沿竖直方向，绳张力指向悬点，三者对竖直轴的力矩均为零。因此即使电场随时间缓慢改变，$J$ 仍守恒。

![图3-2 竖直平衡决定张力，水平分量提供向心力，轨道半径为h乘sin theta。](../figures/forces-03.png)

## 三、物理图像

下板下移后，两板间距增加；电压不变，电场减弱，总向下力 $W$ 减小。轴向角动量固定时，小球不能维持原角度和原角速度同时不变。它会缓慢向外展开，水平轨道半径增大，角速度相应减小。

绳角增大并不表示小球受到新的水平电力。电力始终向下，变化的是张力与圆周运动的平衡条件。小球调整到新的圆锥角时，绳张力的水平分量和轨道半径也一起变化。

“始终做圆周运动”是准静态近似：移板的时间尺度远长于摆的内部调整时间。严格的运动会有微小的倾角振动，但在一阶缓慢变化计算中可将其忽略。这个近似与机械能守恒没有直接关系，外部电源和移板机构可以交换能量。

## 四、解题入口

将瞬时圆周关系代入 $J^2$，消去 $\omega$，得到仅含 $\theta$ 和 $W$ 的方程。因为 $J$ 不变，对它作对数微分；这样既保留 $\sin^4\theta$ 的导数，也保留 $1/\cos\theta$ 的导数。

再由 $W=mg+qU_0/l$ 求 $\Delta W$。如果先把电场写成 $U_0/(l+\Delta l)$，也须展开到一阶。最后检查结果的符号、量纲及 $q\to0$ 极限。

这一方法不需要电容 $C=\varepsilon_0S/l$ 的能量计算。面积 $S$ 影响极板电荷和电源做功，但在恒压、忽略边缘效应的局部电场模型中，不进入小球的角度响应。

## 五、解析

（1）建立相邻平衡状态的约束。

利用圆锥摆关系，

$$
J^2=m^2h^4\sin^4\theta\,\omega^2
=mh^3W\frac{\sin^4\theta}{\cos\theta}.
$$

因此沿着准静态过程，

$$
\boxed{W\frac{\sin^4\theta}{\cos\theta}
=\frac{J^2}{mh^3}=\text{常量}}.
$$

函数 $\sin^4\theta/\cos\theta$ 在 $0<\theta<\pi/2$ 单调增加。$W$ 减小时，它必须增大，所以 $\theta$ 增大。这个不使用微分的判断可先确定答案符号。

（2）对平衡关系微分。

对上述等式取对数并微分，

$$
\frac{dW}{W}+(4\cot\theta+\tan\theta)d\theta=0.
$$

将角函数通分，得到

$$
4\cot\theta+\tan\theta
=\frac{4\cos^2\theta+\sin^2\theta}{\sin\theta\cos\theta}
=\frac{1+3\cos^2\theta}{\sin\theta\cos\theta}.
$$

故角度对力的响应为

$$
d\theta=-\frac{dW}{W}
\frac{\sin\theta\cos\theta}{1+3\cos^2\theta}.
$$

分母中的 $4\cot\theta$ 来自轴向角动量含有轨道半径平方，并在平方后产生 $\sin^4\theta$。若只对 $W/\cos\theta$ 微分，就等于未经说明地固定了角速度。

（3）代入电场变化。

恒压条件下，

$$
dW=-\frac{qU_0}{l^2}dl.
$$

因此一阶结果为

$$
\boxed{\Delta\theta
=\frac{qU_0\,\Delta l}{l^2(mg+qU_0/l)}
\frac{\sin\theta\cos\theta}{1+3\cos^2\theta}}.
$$

也可引入电力占比

$$
\eta=\frac{qU_0/l}{mg+qU_0/l},\qquad0<\eta<1,
$$

把答案写为

$$
\boxed{\Delta\theta
=\eta\frac{\Delta l}{l}
\frac{\sin\theta\cos\theta}{1+3\cos^2\theta}}.
$$

角度以弧度表示。$\eta$、$\Delta l/l$ 和角函数都是无量纲的，因此结果具有正确量纲。

![图3-3 固定轴向角动量时，电场减弱使倾角增大、角速度减小。](../figures/response-03.png)

（4）求角速度与张力的变化作核对。

由 $J=mh^2\sin^2\theta\,\omega$ 守恒，

$$
\frac{\Delta\omega}{\omega}
=-2\cot\theta\,\Delta\theta
=-\eta\frac{\Delta l}{l}
\frac{2\cos^2\theta}{1+3\cos^2\theta}.
$$

所以小球角速度降低。张力 $T=mh\omega^2$ 的变化为

$$
\frac{\Delta T}{T}
=2\frac{\Delta\omega}{\omega}
=-\eta\frac{\Delta l}{l}
\frac{4\cos^2\theta}{1+3\cos^2\theta}.
$$

另从 $T=W/\cos\theta$ 微分，则

$$
\frac{\Delta T}{T}
=\frac{\Delta W}{W}+\tan\theta\,\Delta\theta.
$$

代入 $\Delta W/W=-\eta\Delta l/l$ 后得到同一结果，验证了角度响应的分母。

（5）有限变化时怎样求解。

如果下板位移不再足够小，可保留平衡状态关系，不作一阶展开。令 $l_f=l+\Delta l$，新角度 $\theta_f$ 满足

$$
\left(mg+\frac{qU_0}{l_f}\right)
\frac{\sin^4\theta_f}{\cos\theta_f}
=\left(mg+\frac{qU_0}{l}\right)
\frac{\sin^4\theta}{\cos\theta}.
$$

由于角函数单调，允许区间内解唯一。求出 $\theta_f$ 后用 $\omega_f/\omega=\sin^2\theta/\sin^2\theta_f$ 求新角速度。这是原一阶答案的数值检查方式，也显示大位移时不能直接把 $\Delta l$ 代入线性公式。

![图3-4 精确平衡曲线单调，一阶公式是初始状态处的切线。](../figures/equilibrium-03.png)

（6）检查缓慢调整的稳定性。

在固定 $J$ 下，倾角的有效势为

$$
V(\theta)=\frac{J^2}{2mh^2\sin^2\theta}-Wh\cos\theta.
$$

第一项是绕轴转动的动能所形成的有效项，第二项是向下恒力的势能。求 $V'=0$ 恢复前面的平衡方程；在平衡点有

$$
V''=\frac{Wh}{\cos\theta}(1+3\cos^2\theta)>0.
$$

倾角微振动的惯性系数为 $mh^2$，故

$$
\nu^2=\frac{W}{mh\cos\theta}(1+3\cos^2\theta)
=\omega^2(1+3\cos^2\theta).
$$

平衡稳定。如果移板时间远大于 $1/\nu$，小球有足够时间跟随这一平衡支。这里的稳定性推导解释了“缓缓”所控制的物理条件，而不要求机械能在整个外部操作期间保持不变。

（7）与另一种人为约束比较。

若有外部驱动器维持 $\omega$ 恒定，则 $W=mh\omega^2\cos\theta$ 给出另一答案：

$$
\Delta\theta\big|_{\omega\,\text{固定}}
=\eta\frac{\Delta l}{l}\cot\theta.
$$

这需要外加轴向力矩以改变 $J$，不是本题无驱动圆锥摆的条件。如果既不采用轴向角动量守恒，又不指定角速度或驱动力矩，题目就缺少约束，无法唯一确定 $\Delta\theta$。

![图3-5 固定电压与固定极板电荷会给出不同的场强变化。](../figures/check-03.png)

（8）极限检查。

当 $q\to0$ 或 $U_0\to0$ 时，$\eta\to0$，移板不改变小球受力，故 $\Delta\theta\to0$。电力远大于重力时 $\eta\to1$，角度响应仍有限，不会因小球质量趋小而无限放大。

当 $\theta\to0$，响应约为 $\eta(\Delta l/l)\theta/4$。当 $\theta\to\pi/2$，响应也趋零；不过此极限要求很高的转动能量，并不能从小角状态靠有限移板直接达到。上述极限只是对公式的局部检查。

<!-- KEEP_STUDENT_START -->

（9）角度响应的最大系数。

为判断任何初始角度下响应会有多大，记

$$
A(\theta)=\frac{\sin\theta\cos\theta}{1+3\cos^2\theta}.
$$

令 $x=\cos^2\theta$，则 $A^2=x(1-x)/(1+3x)^2$，并有

$$
\frac{dA^2}{dx}=\frac{1-5x}{(1+3x)^3}.
$$

因此最大值在 $x=1/5$，即 $\theta\simeq63.435^\circ$，此时 $A=1/4$。所有允许角度均满足

$$
0<\Delta\theta\le\frac\eta4\frac{\Delta l}{l}
\quad (\Delta l>0).
$$

这个上限也是数量级检查：例如间距只增加百分之一，即使电力主导，一阶角度变化也不超过 $0.0025\,\mathrm{rad}$。若计算得到几十度，必然超出了小位移近似或用了错误的过程约束。

<!-- KEEP_STUDENT_END -->

## 六、关键洞察

圆锥摆中瞬时平衡与过程守恒承担不同任务。前者描述“现在如何运动”，后者连接“初态与末态”。将二者一起使用，才有唯一的角度变化。

整个角动量矢量并不守恒，因为重力和电力对悬点可产生水平力矩；守恒的是竖直轴分量。轴对称性使这个分量即便在场强缓慢变化时也保持不变。

固定电压和固定电荷必须区分。理想孤立极板的电荷不变时，$E=Q/(\varepsilon_0S)$ 不随间距变化，移板不会改变本题的局部受力。

## 七、易错点

上板带正电时电场向下，正电小球的电力和重力相加。写成 $mg-qU_0/l$ 会改变平衡甚至产生不存在的失重条件。

把绳长 $h$ 当成水平轨道半径，会漏掉 $\sin^2\theta$ 的角动量因子。水平半径是 $h\sin\theta$，高度差是 $h\cos\theta$。

移板缓慢不等于角速度恒定，也不等于机械能守恒。两种额外假设都会改变结果。

题给面积 $S$ 不应强行塞入答案。它属于电容和电源能量描述，在本题恒压均匀电场的角度响应中自然消去。

## 八、课堂讲解建议

教师先让学生分别指出三个力对竖直轴的力矩，再确认守恒量是哪个分量。板书把 $\omega$ 消去后再微分，避免学生同时对多个运动量作无约束的微分。

课堂讨论可把电容器改成断开电源的孤立极板：让学生先判断场是否改变，再讨论绳角。随后比较外部固定角速度的情况，说明过程条件如何改变同一瞬时力学方程的解。

## 九、变式训练

<!-- KEEP_TOGETHER_START -->

变式一：$\theta=30^\circ$、$\eta=1/2$、$\Delta l/l=0.02$，估算倾角和角速度的变化。

解：角度响应系数为

$$
\frac{\sin\theta\cos\theta}{1+3\cos^2\theta}
=\frac{\sqrt3}{13}.
$$

所以 $\Delta\theta=0.01\sqrt3/13\simeq0.00133235\,\mathrm{rad}$，约 $0.0763^\circ$。固定轴向角动量又给出

$$
\frac{\Delta\omega}{\omega}
=-2\sqrt3\Delta\theta=-\frac{0.06}{13}
\simeq-0.00461538.
$$

角速度约减小百分之 $0.462$。两个变化都小，符合一阶准静态计算的量级。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式二：下板向上移一小段，$\Delta l<0$，说明倾角、轨道半径、角速度如何变化。

解：电场增强使 $\Delta W>0$。固定 $J$ 的平衡式给出

$$
\Delta\theta=-\frac{\Delta W}{W}
\frac{\sin\theta\cos\theta}{1+3\cos^2\theta}<0.
$$

水平半径 $a=h\sin\theta$ 的相对变化为 $\Delta a/a=\cot\theta\Delta\theta<0$。由 $J=ma^2\omega$，

$$
\frac{\Delta\omega}{\omega}=-2\frac{\Delta a}{a}>0.
$$

所以轨道收缩、角速度增大。此过程还须保证新间距大于小球离上板的竖直距离，不能让小球撞上下板后仍使用圆锥摆模型。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式三：断开电源后极板电荷 $Q$ 固定，缓慢移板，倾角和电压分别如何变化？

解：忽略边缘效应，板间场为

$$
E=\frac{Q}{\varepsilon_0S},
$$

它不依赖间距，故 $W=mg+qE$ 不变。固定 $J$ 的单调平衡关系决定相同的 $\theta$，所以 $\Delta\theta=0$、$\Delta\omega=0$。但电压并不恒定：

$$
U=El,\qquad\frac{\Delta U}{U}=\frac{\Delta l}{l}.
$$

这说明同一移板操作在恒压和恒电荷两种电路条件下有不同效果。此结论仍要求小球始终位于理想均匀场区。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

变式四：用驱动器维持角速度不变，求一阶倾角变化；在 $\theta=30^\circ$ 时与无驱动结果比较。

解：固定 $\omega$ 时，$W=mh\omega^2\cos\theta$ 微分给出

$$
\Delta\theta=\eta\frac{\Delta l}{l}\cot\theta.
$$

与固定 $J$ 结果的比值为

$$
\frac{1+3\cos^2\theta}{\sin^2\theta}.
$$

在 $30^\circ$ 时该比值为13。按变式一的数据，驱动情况下的变化为 $0.0173205\,\mathrm{rad}$。驱动器还必须使 $J\propto\sin^2\theta$ 改变，轴向角动量不再守恒，因而这不是原题的无外加力矩过程。

<!-- KEEP_TOGETHER_END -->

<!-- question-complete -->
