# 第8题

<!-- question-start -->

把光源置于原点$O$，飞蛾以恒定速率$v_0$飞行，轨迹位于以$z$轴为轴、半顶角为$\alpha$的圆锥面上。飞蛾的速度与指向光源的方向始终成固定角$\theta$。初始位置为$(L\sin\alpha,0,L\cos\alpha)$，选择初始绕轴速度指向$+y$的分支。

（1）求初始加速度的三个直角坐标分量。（2）求飞蛾的位置随时间的变化。（3）飞蛾能提供的加速度大小不超过$a_0$，求它能够沿上述轨道飞到距光源$L_0$处所要求的$\theta$范围。

取$0<\alpha\leq\pi/2$、$0\leq\theta<\pi/2$、$0<L_0<L$。反向绕轴的分支可由$y$坐标与相关分量反号得到。此处采用题给运动学模型。

![图8-1 恒定追光夹角使圆锥面上的轨道不断向光源收缩。](../figures/question-08.png){width=78%}

<!-- question-end -->

## 一、题型定位

本题是具有几何约束的空间运动学问题。圆锥面确定一个方向角不变，追光夹角确定速度在径向与绕轴方向上的比例，恒速条件则固定这两个分量的大小。

与平面等角螺线相比，圆锥面的法向曲率额外贡献一部分加速度。求轨道位置可以通过展开圆锥面简化，但求真实三维加速度时不能丢掉法向分量。

最后一问把规定的轨道与有限的转向能力联系起来。轨道所需加速度随距光源的距离减小而增大，因此能否到达$L_0$，由这一段中最靠近光源的终点控制。

## 二、知识点

用到光源的距离$\rho$及方位角$\varphi$参数化圆锥面：

$$
\boldsymbol r=(\rho\sin\alpha\cos\varphi,
\rho\sin\alpha\sin\varphi,\rho\cos\alpha).
$$

圆锥面的线元为

$$
ds^2=d\rho^2+\rho^2\sin^2\alpha\,d\varphi^2.
$$

单位径向向量$\boldsymbol e_\rho$从光源指向飞蛾，单位方位向量$\boldsymbol e_\varphi$沿方位角增大的方向。题给夹角是速度与$-\boldsymbol e_\rho$之间的角，因而

$$
\boldsymbol v=-v_0\cos\theta\,\boldsymbol e_\rho
+v_0\sin\theta\,\boldsymbol e_\varphi.
$$

径向速度是负的，表示向光源接近。绕轴分量等于$\rho\sin\alpha\,\dot\varphi$，不能误写成$\rho\dot\varphi$；$\rho$是斜距，绕轴圆的半径为$\rho\sin\alpha$。

即使速度分量在随动基底中保持常数，加速度也不为零，因为基底随方位角改变。求导时必须同时处理分量和基底。

## 三、物理图像

将圆锥面沿母线展开，方位角变成$\chi=\sin\alpha\,\varphi$。展开后线元成为平面极坐标线元，轨迹是与向心径向成固定角的对数螺线。

![图8-2 圆锥展开后，方位角缩放为$\chi$=sin$\alpha$ $\varphi$，轨道成为等角螺线。](../figures/developed-08.png){width=88%}

图8-3表示速度分解。向光源的分量$v_0\cos\theta$恒定，故斜距$\rho$线性减少；绕轴分量$v_0\sin\theta$也恒定，但绕轴半径收缩，角速度逐渐增大。

![图8-3 恒速运动仍需转向加速度，还需圆锥面的法向曲率分量。](../figures/components-08.png){width=88%}

图8-4表示$\varphi$与$\rho$的对数关系。形式上到达顶点的径向时间有限，但非零$\theta$会绕行无限多圈，所需加速度也发散。

![图8-4 距离线性减小，绕轴方位却按负对数增长。](../figures/trajectory-08.png){width=92%}

## 四、解题入口

先将恒速与固定夹角条件转换成两条一阶方程：

$$
\dot\rho=-v_0\cos\theta,
\qquad
\dot\varphi=\frac{v_0\sin\theta}{\rho\sin\alpha}.
$$

先积分$\rho(t)$，再积分$\varphi(t)$，最后代回直角坐标。这样可以直接得到位置，也能检查速率大小确实恒定。

求初始加速度可用两条独立路线：对直角坐标位置求二阶导数，或对随动基底中的速度求导。后者更容易看出三维法向贡献，前者则给出直角坐标分量的直接核查。

把所需加速度写成$C/\rho$后，最后一问只需在$\rho=L_0$检查$C/L_0\leq a_0$。随后用$u=\sin^2\theta$将角度不等式化成二次不等式。

## 五、解析

（1）求径向距离与方位角。

由$\dot\rho=-v_0\cos\theta$和$\rho(0)=L$，得

$$
\boxed{\rho(t)=L-v_0\cos\theta\,t}.
$$

由方位速度方程，

$$
\varphi(t)=\int_0^t
\frac{v_0\sin\theta}{[L-v_0\cos\theta\,t']\sin\alpha}\,dt'.
$$

利用$\varphi(0)=0$，得

$$
\boxed{\varphi(t)=-\frac{\tan\theta}{\sin\alpha}
\ln\frac{L-v_0\cos\theta\,t}{L}}.
$$

所选分支$\dot\varphi\geq0$。若初始绕轴方向相反，方位角整体反号即可；径向距离、速率和加速度大小保持不变。

（2）写出完整位置函数。

记$\rho=L-v_0\cos\theta\,t$，则

$$
\boxed{\begin{aligned}
x(t)&=\rho\sin\alpha\cos\left[
-\frac{\tan\theta}{\sin\alpha}\ln\frac\rho L\right],\\
y(t)&=\rho\sin\alpha\sin\left[
-\frac{\tan\theta}{\sin\alpha}\ln\frac\rho L\right],\\
z(t)&=\rho\cos\alpha.
\end{aligned}}
$$

位置公式适用到模型失效之前，形式上的范围为$0\leq t<L/(v_0\cos\theta)$。距光源$L_0$处对应的时间为

$$
\boxed{t_0=\frac{L-L_0}{v_0\cos\theta}}.
$$

此段绕轴圈数为

$$
\boxed{N=\frac{\tan\theta}{2\pi\sin\alpha}
\ln\frac{L}{L_0}}.
$$

可直接检查轨迹仍在圆锥面：$x^2+y^2=\rho^2\sin^2\alpha$，$z=\rho\cos\alpha$。又有

$$
v^2=\dot\rho^2+\rho^2\sin^2\alpha\,\dot\varphi^2
=v_0^2\cos^2\theta+v_0^2\sin^2\theta=v_0^2.
$$

（3）求初始直角坐标加速度。

取$R_\perp=\rho\sin\alpha$。则$\dot R_\perp=-v_0\cos\theta\sin\alpha$是常数，$\ddot R_\perp=0$。由$x=R_\perp\cos\varphi$、$y=R_\perp\sin\varphi$，在初始$\varphi=0$时，

$$
a_x(0)=\ddot R_\perp-R_\perp\dot\varphi^2
=-\frac{v_0^2\sin^2\theta}{L\sin\alpha}.
$$

另有

$$
\ddot\varphi(0)
=\frac{v_0^2\sin\theta\cos\theta}{L^2\sin\alpha}.
$$

所以

$$
a_y(0)=2\dot R_\perp\dot\varphi
+R_\perp\ddot\varphi
=-\frac{v_0^2\sin\theta\cos\theta}{L}.
$$

$z=\rho\cos\alpha$随时间线性变化，因此$a_z=0$。汇总为

$$
\boxed{\boldsymbol a(0)=\left(
-\frac{v_0^2\sin^2\theta}{L\sin\alpha},
-\frac{v_0^2\sin\theta\cos\theta}{L},0\right)}.
$$

初始速度为$(-v_0\cos\theta\sin\alpha,v_0\sin\theta,-v_0\cos\theta\cos\alpha)$。两者点积为零，验证加速度只改变速度方向，未改变速率。

（4）在随动基底中独立求加速度。

引入增加圆锥半顶角的单位方向$\boldsymbol e_\alpha$，在本题$\alpha$固定的情况下有

$$
\dot{\boldsymbol e}_\rho
=\dot\varphi\sin\alpha\,\boldsymbol e_\varphi,
$$

$$
\dot{\boldsymbol e}_\varphi
=-\dot\varphi(\sin\alpha\,\boldsymbol e_\rho
+\cos\alpha\,\boldsymbol e_\alpha).
$$

对$\boldsymbol v=-v_0\cos\theta\boldsymbol e_\rho
+v_0\sin\theta\boldsymbol e_\varphi$求导，代入$\dot\varphi$，得到

$$
\boxed{\boldsymbol a=
-\frac{v_0^2\sin^2\theta}{\rho}\boldsymbol e_\rho
-\frac{v_0^2\sin\theta\cos\theta}{\rho}\boldsymbol e_\varphi
-\frac{v_0^2\sin^2\theta\cot\alpha}{\rho}\boldsymbol e_\alpha}.
$$

前两项位于圆锥切平面内，第三项是圆锥面的法向曲率贡献。初始$\varphi=0$时，$\boldsymbol e_\rho=(\sin\alpha,0,\cos\alpha)$、$\boldsymbol e_\alpha=(\cos\alpha,0,-\sin\alpha)$，代回后恰好得到上一小问的直角坐标分量。

尤其是$a_z=0$由径向和法向分量抵消产生，不能据此说真实轨道没有法向加速度。

（5）求任意距离处的加速度大小。

三个随动单位方向正交，因此

$$
a^2=\frac{v_0^4}{\rho^2}
\left[\sin^4\theta+\sin^2\theta\cos^2\theta
+\sin^4\theta\cot^2\alpha\right].
$$

整理得

$$
\boxed{a(\rho)=\frac{v_0^2\sin\theta}{\rho}
\sqrt{1+\sin^2\theta\cot^2\alpha}}.
$$

将圆锥展开成平面，只能读出切向加速度大小$v_0^2\sin\theta/\rho$，不能读出最后的平方根修正。该修正反映圆锥嵌入三维空间的法向弯曲。

式中的$v_0^2/\rho$具有加速度单位，其余因子无量纲。在$\theta=0$时，轨迹沿母线直线向内，加速度为零；在$\alpha=\pi/2$时，圆锥退化为平面，平方根修正为1。这两个极限都符合预期。

（6）由最大可用加速度求夹角范围。

由于$\rho$单调从$L$减小到$L_0$，$a(\rho)$单调增大。沿规定轨道到达$L_0$的充要运动学条件是

$$
\frac{v_0^2\sin\theta}{L_0}
\sqrt{1+\sin^2\theta\cot^2\alpha}\leq a_0.
$$

令$q=a_0L_0/v_0^2$、$u=\sin^2\theta$，得

$$
u+u^2\cot^2\alpha\leq q^2.
$$

对$u\geq0$，左侧单调递增。其非负上限可以写成数值稳定且涵盖平面极限的形式：

$$
\boxed{u_*=
\frac{2q^2}{1+\sqrt{1+4q^2\cot^2\alpha}}}.
$$

于是允许范围为

$$
\boxed{0\leq\theta<\frac\pi2,
\qquad \sin^2\theta\leq u_*}.
$$

若$u_*<1$，可写成$0\leq\theta\leq\arcsin\sqrt{u_*}$。若$u_*\geq1$，所有严格小于$90^\circ$的向内角度都满足加速度限制。$\theta=90^\circ$时径向速度为零，无法到达$L_0<L$，始终应排除。

等号表示到达$L_0$时刚好用满$a_0$。若还要求在$L_0$之后继续沿同一轨道飞行，则应要求这里有严格余量，或对更小的目标距离重新检查。

![图8-5 所需加速度与距离成反比，有限能力对应一个临界距离。](../figures/check-08.png){width=90%}

（7）写出临界距离并检查顶点极限。

对给定的非零$\theta$，设$a_0>0$，临界距离为

$$
\boxed{\rho_c=\frac{v_0^2\sin\theta}{a_0}
\sqrt{1+\sin^2\theta\cot^2\alpha}}.
$$

若$\rho_c\leq L_0$，可沿规定轨道到达目标；若$L_0<\rho_c<L$，会在到达目标前用满加速度；若$\rho_c>L$，初态就不能实现所要求的轨道。

形式上$\rho$在有限时间$L/(v_0\cos\theta)$降到零，但$\theta>0$时所需加速度发散，有限$a_0$不允许完整到达顶点。若目标改为$L_0=0$，只有$\theta=0$的直线母线运动可在这个恒速模型中到达。

（8）检验加速度限制的单调性。

在相同$\rho,v_0,\theta$下，$\alpha$越小，$\cot\alpha$越大，所需加速度越大。这是因为绕轴半径变小，保持同一绕轴速度需要更快转向。

对于固定的圆锥和目标距离，增加$a_0$或减小$v_0$会扩大允许角度范围。特别是$v_0$增大两倍，所需加速度增大四倍；不能把恒速误解为转向能力与速率无关。

## 六、关键洞察

固定夹角使径向速度恒定，固定圆锥角使轴向坐标线性变化，因此$a_z=0$。然而运动仍不断绕轴，横向加速度并不为零。这种分量的抵消比只使用“向心加速度”一词更精确。

圆锥展开保持曲面的内在长度，却不保留曲面在三维空间中的法向弯曲。展开图适合求对数轨迹，完整加速度仍需要三维基底或直角坐标求导。

限制不是“全程加速度都等于$a_0$”，而是规定轨道需要的加速度不超过$a_0$。在这一模型中，终点是最严格的检查位置。

## 七、易错点

把绕轴圆半径写成$\rho$；漏掉基底随时间变化；在固定速率下令加速度为零；只计算平面展开图的曲率；在角度上限中接受$90^\circ$，都会违背题给几何或到达条件。

初始方位角是零，但方位角速度并非零。$a_y$含$2\dot R_\perp\dot\varphi$和$R_\perp\ddot\varphi$两项，漏掉前一项会把符号算反。

飞行时间有限不保证所需加速度有限。对数轨迹在顶点附近绕行无限圈，是恒定追光夹角模型在有限转向能力下必然失效的地方。

## 八、课堂讲解建议

教师先板书速度的径向、方位分量，再让学生积分距离和方位角。通过初始速度和位置公式的导数，检查所选绕轴分支的正负号。

将加速度用直角坐标和随动基底分别计算，课堂比较两条路线中$a_z=0$的原因。讨论展开圆锥为什么能给出轨迹，却少了一项真实加速度。

最后把$a(\rho)$画成距离的函数，让学生标出临界距离，并区分“到达$L_0$”与“继续到达顶点”的要求。用平面和直线两个极限检验角度范围。

## 九、变式训练

<!-- KEEP_TOGETHER_START -->

变式一：$\theta=0$时写出轨迹、加速度与到达时间。

解：$\varphi=0$，$(x,y,z)=(L-v_0t)(\sin\alpha,0,\cos\alpha)$，沿母线直线运动。加速度为零，到达$L_0$的时间为$(L-L_0)/v_0$，即使$a_0=0$也可实现。

变式二：$\alpha=90^\circ$时给出轨迹和加速度限制。

解：轨迹在$z=0$平面，$\rho=L-v_0\cos\theta\,t$、$\varphi=-\tan\theta\ln(\rho/L)$，加速度大小为$v_0^2\sin\theta/\rho$。若$q=a_0L_0/v_0^2<1$，允许$\theta\leq\arcsin q$；若$q\geq1$，所有$0\leq\theta<90^\circ$均满足限制。

变式三：$\alpha=30^\circ$、$\theta=30^\circ$、$L=10\ \mathrm m$、$L_0=1\ \mathrm m$、$v_0=2\ \mathrm{m/s}$。求到达时间、绕轴圈数和最小所需$a_0$。

解：$t_0=9/\sqrt3=3\sqrt3\ \mathrm s\simeq5.196\ \mathrm s$；$N=\ln10/(\pi\sqrt3)\simeq0.4232$。终点所需加速度为$4\times(1/2)\sqrt{1+3/4}=\sqrt7\ \mathrm{m/s^2}\simeq2.646\ \mathrm{m/s^2}$。

变式四：$\alpha=30^\circ$且$q=a_0L_0/v_0^2=1$，求最大允许$\theta$，并判断$45^\circ$能否满足限制。

解：$3u^2+u=1$，得$u_*=(-1+\sqrt{13})/6\simeq0.43426$，$\theta_{\max}=\arcsin\sqrt{u_*}\simeq41.22^\circ$。$45^\circ$对应$u=1/2$，左侧$u+3u^2=1.25>1$，故不能满足。其归一化所需加速度为$\sqrt5/2>1$。

<!-- KEEP_TOGETHER_END -->

<!-- question-complete -->
