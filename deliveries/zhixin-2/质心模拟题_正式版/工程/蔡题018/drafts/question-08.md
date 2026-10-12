# 第8题

<!-- question-start -->

考虑两个电荷分别为$+Ze$和$-Ze$、静质量均为$m_0$的微观带电粒子，形成束缚态。采用类似玻尔氢原子模型的描述：两个粒子在质心参考系中绕质心做匀速率圆周运动。不考虑电磁辐射，只考虑静电相互作用。若两粒子的瞬时位置为$\boldsymbol r_+$、$\boldsymbol r_-$，间距为$r=|\boldsymbol r_+-\boldsymbol r_-|$，作用在正电荷上的力为
$$
\boldsymbol F_+=-\frac{KZ^2e^2}{r^3}
(\boldsymbol r_+-\boldsymbol r_-),\qquad
\boldsymbol F_-=-\boldsymbol F_+,
$$
其中$K$为库仑常量，$e$为元电荷，$Z>0$。动力学关系为
$$
\boldsymbol F=\frac{\mathrm d\boldsymbol p}{\mathrm dt},
\qquad
\boldsymbol p=\frac{m_0\boldsymbol v}{\sqrt{1-v^2/c^2}},
$$
$c$为真空光速。在质心参考系中，体系总角动量满足$L=n\hbar$，$n=1$对应基态，$\hbar$为约化普朗克常量。

（1）计算基态两粒子之间的间距$r_0$。

（2）要使上述模型的基态存在，$Z$应满足什么条件？

![图8-1 等质量异号电荷的共同圆轨道、相向作用力与基态间距。](../figures/question-08.png){width=76%}

<!-- question-end -->

## 一、题型定位

本题是等质量二体圆周运动与相对论动量的结合。量子化的是体系关于质心的总角动量，不是某一个粒子的角动量；库仑力的距离是两粒子间距，不是单个粒子的轨道半径。先把这两个“二体因素”分清，再用动量方向变化建立向心方程。

两个关键式分别为$L=rp$和$KZ^2e^2/r^2=2pv/r$。它们先确定速率，再确定动量和间距。第二问不仅要求根号内非负，还要求粒子速率严格小于$c$、间距严格大于零，因此临界等号不属于允许圆轨道。

模型按题设保留瞬时静电力和相对论动量，明确忽略磁相互作用、场的传播延迟及辐射。这是一种半经典模型；本题得到的“基态存在”指$n=1$的有限半径圆轨道存在，不等同于完整量子理论中真实粒子的基态判据。

## 二、知识点

质心静止、质量相等且轨道对称时，两粒子位于同一直径的两端，各自轨道半径为$\rho=r/2$，速率相同，瞬时速度和动量相反。总动量可以为零，但两项关于质心的角动量方向相同，不能由总动量零推断总角动量零。

圆周运动中速率$v$不变，动量大小$p$也不变，但动量矢量的方向不断转动。若角速度为$\omega$，则$|\mathrm d\boldsymbol p/\mathrm dt|=\omega p$。本题$\omega=v/\rho=2v/r$，应使用$\gamma m_0v^2/\rho$，不能使用不含$\gamma$的$m_0v^2/\rho$。

定义无量纲速率和洛伦兹因子
$$
\beta=\frac vc,\qquad
\gamma=\frac{1}{\sqrt{1-\beta^2}},\qquad 0<\beta<1.
$$
静质量$m_0$在计算中保持不变；相对论效应由$p=\gamma m_0v$体现，不另把$\gamma m_0$重复代入。

定义精细结构常量
$$
\alpha=\frac{Ke^2}{\hbar c}.
$$
这里的库仑常量$K$与约化普朗克常量$\hbar$均不可省略。$Ke^2$量纲为能量乘长度，$\hbar c$具有同一量纲，所以$\alpha$无量纲。数值估算可取$\alpha\simeq1/137$。

## 三、物理图像

图8-1中两电荷始终关于$O$对称。正电荷在右端时向上运动，负电荷在左端时向下运动，整个直径逆时针旋转。两个库仑力相向，均指向共同中心；图中一个粒子的半径是$r_0/2$，两粒子的间距才是$r_0$。

当粒子沿圆周前进时，速度大小不变，方向转动。同一时间段内，动量矢量也转过同样的角度。这个几何事实把题设$\boldsymbol F=\mathrm d\boldsymbol p/\mathrm dt$转换为可计算的径向方程，不需凭记忆猜一个“相对论向心力公式”。

引力或吸引库仑力越来越强时，并非任何强度都能由越来越小的圆轨道适应。固定总角动量后，消元会把速率直接锁定为$v=KZ^2e^2/(2L)$。若这个值达到或超过$c$，便不再存在有静质量粒子的允许圆轨道；缩小半径不能绕过速率上限。

## 四、解题入口

取质心为原点$O$，轨道为$x$—$y$平面，逆时针运动对应总角动量沿$+z$方向。设一般量子数$n$时两粒子间距为$r$、单粒子动量大小为$p$、速率为$v$。计算完成后令$n=1$并记$r=r_0$。

为避免反复书写，把正的库仑耦合强度记为
$$
A=KZ^2e^2=\alpha Z^2\hbar c>0.
$$
先从几何导出$\rho=r/2$，再分别建立单粒子向心方程和总角动量方程。两个方程相除时消掉未知动量；确定$v$后再通过相对论动量关系求$r$，这比直接对含根式的方程平方更容易控制正负号。

最后独立检查量纲、严格存在条件、弱耦合极限和二体总能量。仅将最终半径代回同一个已化简公式，不足以检查轨道半径和间距是否混淆。

## 五、解析

（1）建立二体几何与符号。

等质量对称轨道在质心系中满足
$$
\boldsymbol r_-=-\boldsymbol r_+,\qquad
\boldsymbol p_-=-\boldsymbol p_+.
$$
记$|\boldsymbol r_+|=|\boldsymbol r_-|=\rho$，则
$$
r=|\boldsymbol r_+-\boldsymbol r_-|
=|2\boldsymbol r_+|=2\rho,\qquad \rho=\frac r2.
$$
图8-1同时标出$r_0$与两段$r_0/2$，就是为了防止把库仑分母写成$\rho^2$。库仑定律计算两粒子相互作用时使用$r$；圆周运动计算单粒子向心加速度时使用$\rho$。

若取一般时刻相位$\varphi=\omega t$，两位置可写成
$$
\begin{aligned}
\boldsymbol r_+&=\rho(\cos\varphi,\sin\varphi,0),\\
\boldsymbol r_-&=-\rho(\cos\varphi,\sin\varphi,0),\\
\boldsymbol v_+&=\rho\omega(-\sin\varphi,\cos\varphi,0),\\
\boldsymbol v_-&=-\boldsymbol v_+.
\end{aligned}
$$
由此$v=\rho\omega$，所以$\omega=2v/r$。两速度之差的大小$2v$是在同一质心系中的坐标变化率，不是某粒子自身参考系测得的另一粒子速率；此处不使用相对论速度合成公式。

（2）从动量方向变化计算力。

图8-2左侧画实际位置空间，右侧把先后两个动量矢量移到共同起点。动量矢量等长，转角为$\Delta\varphi$；橙色弦是$\Delta\boldsymbol p$，不是沿切向增加的动量大小。

![图8-2 位置空间的向心力与动量空间的方向增量。](../figures/momentum-08.png){width=88%}

右侧两个长度为$p$的动量矢量形成等腰三角形，弦长
$$
|\Delta\boldsymbol p|
=2p\sin\frac{\Delta\varphi}{2}.
$$
取$\Delta t\to0$，并利用小角极限$\sin u/u\to1$：
$$
\begin{aligned}
\left|\frac{\mathrm d\boldsymbol p}{\mathrm dt}\right|
&=\lim_{\Delta t\to0}
\frac{2p\sin(\Delta\varphi/2)}{\Delta t}\\
&=\lim_{\Delta t\to0}
p\frac{\Delta\varphi}{\Delta t}
\frac{\sin(\Delta\varphi/2)}{\Delta\varphi/2}\\
&=p\omega
=\frac{pv}{\rho}
=\frac{2pv}{r}.
\end{aligned}
$$
虽然$p$不变，$\boldsymbol p$仍在变化。把$\mathrm dp/\mathrm dt=0$当成$\mathrm d\boldsymbol p/\mathrm dt=0$，会错误地得到没有向心力。

（3）用矢量微分核对向心方向。

由于$p=\gamma m_0v$且$v$恒定，$\gamma$也恒定。正粒子的动量为
$$
\boldsymbol p_+=p(-\sin\omega t,\cos\omega t,0).
$$
逐分量求导：
$$
\begin{aligned}
\frac{\mathrm d\boldsymbol p_+}{\mathrm dt}
&=p\omega(-\cos\omega t,-\sin\omega t,0)\\
&=-p\omega\frac{\boldsymbol r_+}{\rho}.
\end{aligned}
$$
其方向正好指向$O$。负粒子的结果相反，也指向自己的内侧。这一检查同时确定力的方向和大小，不会把吸引力写成使轨道向外发散的斥力。

也可从乘积微分检查：
$$
\frac{\mathrm d\boldsymbol p}{\mathrm dt}
=m_0\left(\gamma\boldsymbol a+
\frac{\mathrm d\gamma}{\mathrm dt}\boldsymbol v\right),
\qquad
\frac{\mathrm d\gamma}{\mathrm dt}
=\frac{\gamma^3}{c^2}\boldsymbol v\cdot\boldsymbol a=0.
$$
圆周运动中$\boldsymbol v\perp\boldsymbol a$，所以本题径向力为$\gamma m_0\boldsymbol a$。不能把直线加速时出现的$\gamma^3m_0$直接用在横向加速度上。

（4）建立单粒子径向方程。

异号电荷的力是吸引力，大小为$A/r^2$。与图8-2的动量变化率比较：
$$
\boxed{\frac{A}{r^2}=\frac{2pv}{r}}.
$$
两边乘$r^2$：
$$
A=2pvr.
$$
代入$p=\gamma m_0v$，也可写成
$$
\frac{A}{r^2}
=\frac{2\gamma m_0v^2}{r}.
$$
这里方程只针对一个粒子，不要因为体系有两粒子而再将左边乘$2$。另一个粒子满足相同大小的方程，提供的是对称性而不是额外倍数。

（5）计算总角动量而非单粒子角动量。

图8-3中两个位置和两个动量都相反，但每个叉乘同时改变两次符号。因此两个角动量同向，$\odot$表示垂直轨道平面向外。

![图8-3 关于共同质心的两项角动量及同向叠加。](../figures/angular-08.png){width=65%}

两粒子的切向动量均与各自位置垂直：
$$
\begin{aligned}
\boldsymbol L_+&=\boldsymbol r_+\times\boldsymbol p_+,\\
\boldsymbol L_-&=\boldsymbol r_-\times\boldsymbol p_-
=(-\boldsymbol r_+)\times(-\boldsymbol p_+)
=\boldsymbol L_+,\\
L_+&=L_-=\rho p=\frac{rp}{2},\\
L&=L_++L_-=2\rho p=rp.
\end{aligned}
$$
题设要求
$$
\boxed{rp=n\hbar}.
$$
基态$n=1$，因此$rp=\hbar$，每个粒子自己的角动量为$\hbar/2$。不能分别令两个粒子均有$\hbar$，否则总角动量变成$2\hbar$，已经是另一个量子数。

（6）先消去动量并求速率。

把$rp=L$代入单粒子的$A=2pvr$：
$$
\begin{aligned}
A&=2v(rp)=2vL,\\
v&=\frac{A}{2L}=\frac{KZ^2e^2}{2n\hbar},\\
\beta_n&=\frac{v}{c}
=\frac{A}{2n\hbar c}
=\frac{\alpha Z^2}{2n}.
\end{aligned}
$$
这是整题的关键消元：速率不再含$r$或$m_0$。它由耦合强度与指定的总角动量确定，而不是靠调节半径任意选择。若该式已经给出$v\ge c$，随后不能再求一个合法的有限半径来“修复”。

（7）由相对论动量求一般间距。

在$0<\beta_n<1$的合法域内，
$$
p=\frac{m_0c\beta_n}{\sqrt{1-\beta_n^2}}>0.
$$
从$r=L/p$逐步代入：
$$
\begin{aligned}
r_n
&=\frac{L\sqrt{1-\beta_n^2}}{m_0c\beta_n}\\
&=\frac{n\hbar}{m_0c}
\frac{\sqrt{1-\alpha^2Z^4/(4n^2)}}{\alpha Z^2/(2n)}\\
&=\frac{2n^2\hbar}{m_0c\alpha Z^2}
\sqrt{1-\frac{\alpha^2Z^4}{4n^2}}\\
&=\frac{n\hbar}{m_0c\alpha Z^2}
\sqrt{4n^2-\alpha^2Z^4}.
\end{aligned}
$$
最后一步利用$n>0$，把根号中的$4n^2$提出为正的$2n$，不能漏掉外面的$n$。注意$r_n$仍是两粒子间距，单粒子轨道半径是$r_n/2$。

（8）取基态并变换为不含$\alpha$的形式。

令$n=1$：
$$
\boxed{
r_0=\frac{\hbar}{m_0c\alpha Z^2}
\sqrt{4-\alpha^2Z^4}
}.
$$
若直接用题干的$K$、$e$书写，利用$\alpha Z^2=A/(\hbar c)$：
$$
\begin{aligned}
r_0
&=\frac{2\hbar^2}{m_0A}
\sqrt{1-\frac{A^2}{4\hbar^2c^2}}\\
&=\frac{\hbar}{m_0cA}
\sqrt{4\hbar^2c^2-A^2}\\
&=\frac{\sqrt{4c^2\hbar^4-K^2Z^4e^4\hbar^2}}
{m_0cKZ^2e^2}.
\end{aligned}
$$
第二步把根号分母$2\hbar c$提出，并与前面的$2\hbar^2$约分。第三步把正的$\hbar$移入根号。两种表达完全相同，不是两个不同物理解答。

量纲检查可用最简形式：$\hbar/(m_0c)$量纲是长度，$\alpha Z^2$和根号均无量纲。又可检查$2\hbar^2/(m_0A)$：$A$为能量乘长度，所以这个整体仍为长度。

（9）在平方路线中筛选根。

为检查上面的直接消元，也从$L=rp=\hbar$写
$$
\hbar=\frac{rm_0v}{\sqrt{1-v^2/c^2}}.
$$
此式左右为正，平方后得
$$
\begin{aligned}
\hbar^2\left(1-\frac{v^2}{c^2}\right)
&=r^2m_0^2v^2,\\
r^2
&=\frac{\hbar^2}{m_0^2v^2}
-\frac{\hbar^2}{m_0^2c^2}\\
&=\frac{4\hbar^4}{m_0^2A^2}
-\frac{\hbar^2}{m_0^2c^2}.
\end{aligned}
$$
代入$v=A/(2\hbar)$后，只有正的$r$对应间距；负平方根不是“反向转动”的另一个半径。反向转动只改变角动量矢量方向，不改变其大小和间距。

当$v=c$时，相对论动量关系发散，不能代入前一未平方方程；因此即使平方后的式子允许$r^2=0$，也不能将其算成有效圆轨道。平方后的代数条件须与原式定义域合并。

（10）给出严格存在条件。

基态要求$0<v<c$：
$$
\begin{aligned}
0&<\frac{A}{2\hbar}<c,\\
0&<A<2\hbar c,\\
0&<\alpha Z^2<2.
\end{aligned}
$$
因为$Z>0$，得到
$$
\boxed{0<Z<\sqrt{\frac{2}{\alpha}}
=\sqrt{\frac{2\hbar c}{Ke^2}}}.
$$
这与$r_0>0$要求$4-\alpha^2Z^4>0$完全一致。根号内必须严格为正，不能写大于等于零。$\alpha\simeq1/137$时
$$
Z_{\mathrm{crit}}\simeq\sqrt{274}\simeq16.55.
$$
若$Z$限为正整数，则允许$Z=1,2,\ldots,16$，即$Z\le16$；$Z=17$已不满足基态条件。若只把$Z$视作连续的正耦合参数，应保留严格不等式而不写整数上限。

（11）结合阈值图解释临界行为。

定义同一耦合和同一$n$的非相对论间距
$$
r_{\mathrm{NR}}=\frac{2n^2\hbar^2}{m_0A}.
$$
图8-4纵轴是$r_n/r_{\mathrm{NR}}$，不是$r_n$本身；横轴为刚由消元得到的$\beta_n$。图中两端空心点表示极限，不是允许的零电荷轨道或光速轨道。

![图8-4 间距的相对论收缩与严格速率阈值。](../figures/threshold-08.png){width=86%}

由一般间距可得
$$
\frac{r_n}{r_{\mathrm{NR}}}=\sqrt{1-\beta_n^2}.
$$
如图$\beta_n=0.6$处比值为$\sqrt{1-0.36}=0.8$。当$\beta_n\to1^-$，$p\to\infty$、$r_n=L/p\to0$；该轨道族可以接近端点，但端点本身不成立。

当$Z\to0^+$，$\beta_n\to0$，比值趋$1$，但$r_{\mathrm{NR}}\propto1/Z^2$发散，所以$r_n\to\infty$而非趋于有限常量。$Z=0$时没有吸引力，不能把图中的弱耦合极限解读为一个有限半径束缚态。

（12）检查弱耦合和等质量约化质量。

对$\beta_n\ll1$，使用二阶及四阶泰勒展开：
$$
\begin{aligned}
\sqrt{1-\beta_n^2}
&=1-\frac{\beta_n^2}{2}
-\frac{\beta_n^4}{8}+O(\beta_n^6),\\
r_n&=\frac{2n^2\hbar^2}{m_0A}
\left(1-\frac{\alpha^2Z^4}{8n^2}
-\frac{\alpha^4Z^8}{128n^4}+\cdots\right).
\end{aligned}
$$
最低阶$r_n\simeq2n^2\hbar^2/(m_0A)$。这个因子$2$可由独立的非相对论二体路线核对。两等质量的约化质量为
$$
\mu=\frac{m_0m_0}{m_0+m_0}=\frac{m_0}{2}.
$$
相对坐标的圆周速率$u=2v$，非相对论关系为$L=\mu ru$、$A/r^2=\mu u^2/r$。逐步消元：
$$
\begin{aligned}
u&=\frac{L}{\mu r},\\
\frac{A}{r^2}
&=\frac{\mu}{r}\frac{L^2}{\mu^2r^2}
=\frac{L^2}{\mu r^3},\\
r_{\mathrm{NR}}
&=\frac{L^2}{\mu A}
=\frac{2n^2\hbar^2}{m_0A}.
\end{aligned}
$$
相对论主解没有把$2v$塞进单粒子的$\gamma$。约化质量路线在此仅用于非相对论极限；离开低速条件，不能直接照搬这个简化。

（13）用体系能量检查束缚性质。

每粒子总能量为$\gamma m_0c^2$，两粒子静电势能只有一份$-A/r$。因此体系能量
$$
E=2\gamma m_0c^2-\frac Ar.
$$
由径向方程$A/r=2pv=2\gamma m_0v^2$，得到
$$
\begin{aligned}
E&=2\gamma m_0c^2-2\gamma m_0v^2\\
&=2\gamma m_0c^2(1-\beta_n^2)\\
&=2m_0c^2\sqrt{1-\beta_n^2}.
\end{aligned}
$$
在合法域内$0<E<2m_0c^2$。与两粒子相距无限远、均静止的能量$2m_0c^2$比较，本轨道具有正的结合能
$$
B=2m_0c^2-E
=2m_0c^2\left(1-\sqrt{1-\beta_n^2}\right)>0.
$$
不是要求包含静能的$E<0$。用泰勒展开检查弱耦合：
$$
B\simeq m_0c^2\beta_n^2
=\frac{m_0A^2}{4n^2\hbar^2}.
$$
非相对论库仑结合能$\mu A^2/(2L^2)$取$\mu=m_0/2$后与此相同，又一次核对两体因子。这个能量检查不能取代第二问的$v<c$条件，但可以发现漏写一个粒子动能或重复计势能的错误。

（14）核对数值尺度与量子数条件。

为展示计算而非增加本题条件，暂取$m_0$为电子静质量。约化康普顿长度$\bar\lambda_C=\hbar/(m_0c)\simeq3.86159\times10^{-13}\,\mathrm m$，使用$\alpha\simeq0.00729735$。$Z=1$基态：
$$
\begin{aligned}
\beta_1&=\frac{\alpha}{2}\simeq0.00364868,\\
\sqrt{1-\beta_1^2}
&\simeq0.99999334,\\
r_0&=\bar\lambda_C\frac{\sqrt{1-\beta_1^2}}{\beta_1}\\
&\simeq3.86159\times10^{-13}
\times\frac{0.99999334}{0.00364868}\,\mathrm m\\
&\simeq1.05835\times10^{-10}\,\mathrm m,\\
\rho_0&=\frac{r_0}{2}\simeq5.29174\times10^{-11}\,\mathrm m.
\end{aligned}
$$
间距是两倍单粒子半径；本题两粒子等质量，不能将这个$r_0$与固定重核模型的电子半径直接混同。

$Z=16$时：
$$
\begin{aligned}
\beta_1&=\frac{\alpha\,16^2}{2}
=128\alpha\simeq0.934061<1,\\
\sqrt{1-\beta_1^2}&\simeq0.357113,\\
r_0&\simeq3.86159\times10^{-13}
\times\frac{0.357113}{0.934061}\,\mathrm m\\
&\simeq1.47638\times10^{-13}\,\mathrm m.
\end{aligned}
$$
此时非相对论近似明显不合适，仍可在题设模型内使用完整根式。$Z=17$给$\beta_1=144.5\alpha\simeq1.05447>1$，不是将根号取绝对值后继续计算，而是判定$n=1$轨道不存在。

一般量子数的条件是$\alpha Z^2<2n$。基态不存在不等于所有较大$n$的半经典轨道都不存在；本题第二问仅检查$n=1$。近临界的极小尺度和强相对论运动还会使真实体系的忽略磁场、辐射等条件失效，不能把模型的整数上限当成现实中一切带电粒子的普遍限制。

## 六、关键洞察

第一，固定总角动量后，速度先被确定，半径后被确定。若只盯着“库仑力随距离平方增大”，容易以为总能缩小半径补偿强吸引；$v=A/(2L)$说明速率上限与半径缩小无法分开。这是严格阈值的物理来源。

第二，可以用固定$L$的能量函数独立推导圆轨道，并检查其径向稳定性。取相对位置$\boldsymbol r=\boldsymbol r_+-\boldsymbol r_-$，其共轭动量为$\boldsymbol p=\boldsymbol p_+=-\boldsymbol p_-$。这不是把“总动量零”替换成“共轭动量零”。两粒子的正则一形式满足
$$
\boldsymbol p_+\cdot\mathrm d\boldsymbol r_+
+\boldsymbol p_-\cdot\mathrm d\boldsymbol r_-
=\boldsymbol p\cdot\mathrm d\boldsymbol r.
$$
因$\mathrm d\boldsymbol r_\pm=\pm\mathrm d\boldsymbol r/2$，左边两项各为$\boldsymbol p\cdot\mathrm d\boldsymbol r/2$。所以$L=|\boldsymbol r\times\boldsymbol p|=rp_\varphi$，圆轨道$p_\varphi=L/r$。

允许径向动量$p_r$时，题设模型的体系哈密顿量为
$$
H(r,p_r;L)
=2\sqrt{m_0^2c^4+c^2\left(p_r^2+\frac{L^2}{r^2}\right)}
-\frac Ar.
$$
图8-5画$p_r=0$、固定同一个$L$时的能量。蓝线有有限半径最低点；临界和超临界曲线没有正半径最低点。横轴$x=m_0cr/L$，三条曲线的区别只有$A/(cL)$，并非改变横轴单位。

![图8-5 固定总角动量的能量驻点与耦合阈值。](../figures/energy-08.png){width=91%}

记
$$
\mathcal E(r)=\sqrt{m_0^2c^4+\frac{c^2L^2}{r^2}},
\qquad H_0(r)=2\mathcal E(r)-\frac Ar.
$$
圆轨道要求$p_r=0$和$\partial H_0/\partial r=0$。对根式用链式法则：
$$
\begin{aligned}
\mathcal E'(r)
&=\frac{1}{2\mathcal E(r)}
\left(-\frac{2c^2L^2}{r^3}\right)
=-\frac{c^2L^2}{r^3\mathcal E(r)},\\
H_0'(r)
&=-\frac{2c^2L^2}{r^3\mathcal E(r)}
+\frac A{r^2}.
\end{aligned}
$$
驻点方程逐步化为
$$
\begin{aligned}
A r\mathcal E(r)&=2c^2L^2,\\
A\sqrt{m_0^2c^4r^2+c^2L^2}&=2c^2L^2,\\
A^2\left(m_0^2c^4r^2+c^2L^2\right)&=4c^4L^4,\\
r^2&=\frac{L^2(4c^2L^2-A^2)}
{m_0^2c^2A^2},\\
r&=\frac{L\sqrt{4c^2L^2-A^2}}{m_0cA}.
\end{aligned}
$$
取$L=n\hbar$便得到主解。平方前左右为正，仍需$A<2cL$使$r>0$；独立的能量路线没有改变存在条件。

在驻点处，二阶导数是
$$
\begin{aligned}
H_0''(r)
&=\frac{6c^2L^2}{r^4\mathcal E}
-\frac{2c^4L^4}{r^6\mathcal E^3}
-\frac{2A}{r^3}\\
&=\frac{2c^2L^2}{r^4\mathcal E}
-\frac{2c^4L^4}{r^6\mathcal E^3}\\
&=\frac{2c^2L^2}{r^4\mathcal E}
\left(1-\frac{c^2L^2}{r^2\mathcal E^2}\right)\\
&=\frac{2m_0^2c^6L^2}{r^4\mathcal E^3}>0.
\end{aligned}
$$
第二行代入驻点方程$A=2c^2L^2/(r\mathcal E)$；最后一行利用$\mathcal E^2-c^2L^2/r^2=m_0^2c^4$。这说明定$L$的小径向扰动在该静电模型中有恢复趋势，不表示真实辐射体系永远保持轨道。

第三，临界等号可由小半径能量直接辨认。$r\to0^+$时展开根式：
$$
\begin{aligned}
\mathcal E(r)
&=\frac{cL}{r}
\sqrt{1+\frac{m_0^2c^2r^2}{L^2}}\\
&=\frac{cL}{r}
+\frac{m_0^2c^3r}{2L}+O(r^3),\\
H_0(r)&=\frac{2cL-A}{r}
+\frac{m_0^2c^3r}{L}+O(r^3).
\end{aligned}
$$
$A<2cL$时，能量在$r\to0^+$发散为正，在$r\to\infty$趋于$2m_0c^2$，中间可有最低点。$A=2cL$时，小$r$能量趋零但不在任何正半径取得该下确界；它不是一条$r=0$圆轨道。$A>2cL$时能量向负无穷下降，是点粒子模型的失稳方向，而非合法超光速束缚解。

第四，径向小振动与圆周转动频率一般不同。设平衡半径为$r_*$，在$p_r=0$附近有
$$
H_{p_rp_r}=\frac{2c^2}{\mathcal E_*}.
$$
线性哈密顿方程
$$
\delta\dot r=H_{p_rp_r}\delta p_r,\qquad
\delta\dot p_r=-H_{rr}\delta r
$$
给
$$
\begin{aligned}
\delta\ddot r+\kappa^2\delta r&=0,\\
\kappa^2
&=H_{p_rp_r}H_{rr}
=\frac{4m_0^2c^8L^2}{r_*^4\mathcal E_*^4}.
\end{aligned}
$$
圆周角速度由$\partial H/\partial L$得到
$$
\omega=\frac{2c^2L}{r_*^2\mathcal E_*}
=\frac{2v}{r_*}.
$$
因此
$$
\frac{\kappa^2}{\omega^2}
=\frac{m_0^2c^4}{\mathcal E_*^2}
=1-\beta_n^2,\qquad
\boxed{\kappa=\omega\sqrt{1-\beta_n^2}}.
$$
低速极限两频率一致；相对论区径向频率更低。此扩展是在固定$L$的小扰动模型内，不把它当作完整量子跃迁频率，也不将圆周稳定性替代题干量子化规则。

## 七、易错点

把库仑分母写成$(r_0/2)^2$会把相互作用力多算$4$倍；把向心半径写成$r_0$又会少算$2$倍。两错误偶然部分抵消不等于模型正确。必须分别写“粒子间距$r_0$”和“单粒子轨道半径$r_0/2$”。

两个动量矢量相反，总动量为零，但两个角动量同向。量子化的是$rp=n\hbar$；若只写$(r/2)p=n\hbar$，相当于将每个粒子的角动量都量子化为同一$n\hbar$，改变了题设。

动量大小恒定不意味着矢量导数为零。也不能用$m_0v^2/\rho$漏掉$\gamma$，或用$\gamma^3m_0v^2/\rho$误套纵向惯性。根据$\boldsymbol v\cdot\boldsymbol a=0$直接对$\gamma m_0\boldsymbol v$求导最可靠。

对根式平方后只检查非负会误收$r_0=0$。$v=c$使有静质量粒子的动量发散，原式失去定义；基态要求严格$\alpha Z^2<2$。$Z=0$没有吸引力，也不是允许的有限束缚轨道。

总势能只有$-A/r$一项，不因有两个粒子而写成$-2A/r$。总粒子能量却确实有两项；同时写出两个粒子与一对相互作用，才能避免漏项或重复。

总能量包含静能时可以为正，束缚的比较对象是分离静止的$2m_0c^2$，不是零。基态条件是半经典模型条件，不是现实中所有电荷数的限制，更不能借这个近临界计算证明忽略磁场和辐射总是准确。

## 八、课堂讲解建议

课堂先让学生在图8-1上标出粒子间距与两个轨道半径，再询问库仑定律和向心运动分别使用哪个距离。板书保留$r=2\rho$，不要立即把所有半径都简写为$r$。

讲解图8-2时，让学生把两个等长动量矢量的起点移到一起，再连接终点。教师应强调弦表示矢量差，除以时间后才得到力；匀速率只约束大小，不约束方向。先写$\omega p$再写$2pv/r$，比直接给最后公式更便于检查几何因子。

图8-3适合用左右两粒子的叉乘分别判断方向。让学生先判断总动量，再判断总角动量，说明“相反”发生在不同矢量上时不能凭直觉相消。板书两份$rp/2$后相加，再施加题干的$L=n\hbar$。

消元时先由$A=2pvr$和$rp=L$得$v=A/(2L)$，教师在求半径前就提出$v<c$。这样图8-4的空心端点具有明确物理含义，而不是算完根号后临时补一条不等式。

主解完成后可用约化质量核对低速因子$2$，再用总能量核对一份势能、两份粒子能量。备课中的图8-5与二阶导数用于进一步解释严格临界和径向稳定；讲解深度可分层，但不删去学生版的核心运算和根的筛选。

## 九、变式训练

（1）同一电荷的$n=2$轨道。

取$Z=1$，质量不变，比较$n=2$与$n=1$的间距。由一般式：
$$
\begin{aligned}
\beta_1&=\alpha/2,\qquad \beta_2=\alpha/4,\\
r_1&=\frac{2\hbar^2}{m_0A}\sqrt{1-\alpha^2/4},\\
r_2&=\frac{8\hbar^2}{m_0A}\sqrt{1-\alpha^2/16},\\
\frac{r_2}{r_1}
&=4\frac{\sqrt{1-\alpha^2/16}}{\sqrt{1-\alpha^2/4}}
\simeq4.00001997.
\end{aligned}
$$
非相对论最低阶比例是$4$；完整式略大于$4$，因为$n=1$速率更高、相对论收缩更明显。两个轨道均须先检查各自$\beta_n<1$，不能只记$r\propto n^2$而省略定义域。

（2）由收缩比反求耦合。

若某$n$轨道的间距为同一耦合非相对论值的$0.8$倍，求$v/c$、$\gamma$及$\alpha Z^2$。由图8-4：
$$
\begin{aligned}
0.8&=\sqrt{1-\beta_n^2},\\
0.64&=1-\beta_n^2,\\
\beta_n^2&=0.36,\qquad \beta_n=0.6,\\
\gamma&=1/0.8=1.25,\\
\alpha Z^2&=2n\beta_n=1.2n.
\end{aligned}
$$
负的$\beta_n$不表示本题另一速率，因此取正根。若$n=1$，则
$$
Z=\sqrt{1.2/\alpha}\simeq12.82.
$$
该值是连续耦合参数的结果；若额外要求$Z$为整数，题给恰为$0.8$的收缩比通常不能同时精确成立，应保留近似而不强行取整后宣称等式仍成立。

（3）同一轨道的结合能与径向频率。

对上一变式的$\beta_n=0.6$，求体系总能量、结合能及$\kappa/\omega$。完整两粒子结果为
$$
\begin{aligned}
E&=2m_0c^2\sqrt{1-0.6^2}
=1.6m_0c^2,\\
B&=2m_0c^2-E=0.4m_0c^2,\\
\frac{\kappa}{\omega}
&=\sqrt{1-0.6^2}=0.8.
\end{aligned}
$$
若要写$\omega$，先使用固定$L$间距：
$$
\begin{aligned}
r_n&=\frac{n\hbar}{m_0c}\frac{0.8}{0.6}
=\frac{4n\hbar}{3m_0c},\\
\omega&=\frac{2(0.6c)}{r_n}
=\frac{0.9m_0c^2}{n\hbar},\\
\kappa&=0.8\omega
=\frac{0.72m_0c^2}{n\hbar}.
\end{aligned}
$$
二阶能量曲率为正，$\kappa^2>0$，只说明本模型固定$L$的径向小扰动稳定；它不是光子频率，也没有包含辐射耗散。

（4）基态不存在但较大$n$仍存在。

取$Z=20$，求允许圆轨道的最小正整数$n$。一般条件
$$
n>\frac{\alpha Z^2}{2}
=200\alpha\simeq1.45947.
$$
所以最小$n=2$。$n=1$不成立，因为$\beta_1\simeq1.45947>1$；$n=2$则
$$
\begin{aligned}
\beta_2&=\frac{\alpha\,20^2}{4}
=100\alpha\simeq0.729735<1,\\
\sqrt{1-\beta_2^2}&\simeq0.683730,\\
r_2&=\frac{2\hbar}{m_0c}
\frac{\sqrt{1-\beta_2^2}}{\beta_2}.
\end{aligned}
$$
若仍暂取电子静质量，
$$
r_2\simeq2(3.86159\times10^{-13})
\frac{0.683730}{0.729735}\,\mathrm m
\simeq7.236\times10^{-13}\,\mathrm m.
$$
最小允许$n$应由严格不等式筛选；若右侧恰为整数，也须再增$1$，不能用无条件的向上取整收进临界等号。这个变式区别“指定$n=1$不存在”与“所有量子数都不存在”，主问仍以$n=1$定义基态。

<!-- question-complete -->
