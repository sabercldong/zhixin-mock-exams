# 第7题


<!-- question-complete -->
<!-- question-start -->

（1）老式的 $3\mathrm D$ 眼镜的两个镜片分别是透光方向互相垂直的验偏器，即只允许电场沿一个方向振动的线偏振光通过的薄膜。在自然光照射下，戴上这种眼镜观察镜中的自己，左眼闭着、右眼睁开。由于偏振选择，只能看见其中一只眼睛的像。能够看见的是睁开的眼睛，还是闭着的眼睛？

（2）新式的 $3\mathrm D$ 眼镜，在每个验偏器前方再放置一块四分之一波片。波片是单轴晶体薄片，光轴平行于片面。垂直于片面入射时，电场分别沿光轴、垂直于光轴振动的两种线偏振光的折射率为 $n_e$、$n_o$；通过厚度 $d$ 后，两分量的相位差为 $\pi/2$。若入射线偏振光的振动方向与光轴成 $45^\circ$，出射光变为圆偏振光。

根据这些信息，分析左右镜片的验偏方向与波片光轴应如何配置，以及左右投影镜头的出射光应处于什么偏振态。戴上这种新眼镜重复第（1）问的实验，会得到什么结果？

<!-- question-end -->

## 一、题型定位

这是偏振选择与往返光路叠加的问题。第一问只有两个互相垂直的线偏振方向；第二问在同一束光的往返路径中加入波片，使两次相位积累共同改变最后的线偏振方向。镜中的像是否可见，必须用光在最后一次通过睁开眼睛前的镜片时能否透过来判断，不能只凭“镜子左右颠倒”判断。

以下将物理上的右眼记为 $R$，左眼记为 $L$，即使画出镜像也不交换这两个源点的名称。右眼睁开，因此唯一观察通道是返回光通过右镜片进入右眼；左眼闭合并不表示左眼皮不反射环境光，它仍能作为被观察物发出或散射光。

采用题设的理想模型：验偏器理想、波片无吸收且在设计波长具有所给相位差，镜面近轴反射不使光退偏，其对两个固定横向分量的作用相同。实际宽光谱、较大斜入射和非理想器件产生的漏光，另在明确条件下讨论，不把理想的“完全消光”当作任意现实眼镜的精确性能。

## 二、知识点

线偏振方向是电场的振动方向，而不是光的传播方向。若一个线偏振场的振幅为 $E_m$，与验偏器透光轴的夹角为 $\theta$，通过后只留下平行于透光轴的投影，
$$
E_{\rm out}=E_m\cos\theta.
$$
在同一介质中光强与电场振幅平方成正比，因此
$$
I_{\rm out}=I_{\rm in}\cos^2\theta.
$$
这就是马吕斯定律。两个互相垂直的理想验偏器依次通过同一束光时，第二个所取的投影为零。

波片不靠吸收其中一个分量来选偏振。它将入射电场沿两条正交主轴分解，两个分量在晶体中的传播相位不同，出射后再叠加。等振幅且相位差为 $\pm\pi/2$ 的正交分量产生圆偏振；等振幅且相位差为 $0$ 或 $\pi$ 时仍是线偏振；其余一般产生椭圆偏振。

偏振态的判断只依赖两分量之间的相对相位。给两个分量同时加上同一相位，只改变它们在时间上的共同起点，不改变线、圆或椭圆的类别。相反，只给其中一个分量再增加 $\pi/2$，会改变相对相位，必须在每次通过波片时累积。

描述往返光路时可以一直使用同一组实验室横向坐标。若中途改为“沿传播方向看”的局部坐标，返回时某一坐标方向会改变，必须连同场分量一并变换；不能既翻转传播方向，又在没有说明的情况下再翻转圆偏振符号。

## 三、物理图像

自然光照亮脸部，脸部散射出的光先穿过所在眼前的镜片，再被镜面反射，最后穿过观察眼前的镜片。要判断哪只眼睛的像可见，就分别追踪来自 $R$ 和来自 $L$ 的光束，而不是假定所有反射光都回到原来那只眼。

在老式镜片中，右眼附近的光被右验偏器变为一种线偏振，左眼附近的光被左验偏器变为与之垂直的线偏振。近轴镜面保留这个横向振动方向，因此进入右眼的最后一个验偏器可以直接作方向筛选。

在新式镜片中，“波片在验偏器前方”指波片位于朝向镜子或银幕的一侧。来自脸部的光向外传播时先过验偏器、再过波片；投影光或镜面返回光向眼睛传播时先过波片、再过验偏器。两种方向的器件顺序相反，这是第二问最重要的几何关系。

当每片的验偏轴与波片的两条主轴成 $45^\circ$ 时，向外的线偏振经第一次波片变为圆偏振。反射后的光再过波片，两个主轴分量的相位差累计为 $\pi$，变成与向外出发时垂直的线偏振。最后由观察眼前的验偏器决定这束返回光能否被看见。

## 四、解题入口

先把左右验偏轴设成两个正交方向，固定右眼为唯一接收端。对每一个源点写出“源点—所在镜片—镜面—右镜片—右眼”的顺序，逐次记录电场方向。

第二问不直接背诵圆偏振的左右手名称，而是在波片主轴上写出两个振动分量。把第一次波片、镜面共同相位以及第二次波片逐项相加，得到返回后的线偏振方向，再与右验偏轴比较。这样可以完整保留相位法的正确路线，又避免把“光路倒走”误认为“相位退回”。

最后再用投影矩阵检验全部通道，并对银幕入射、波片厚度和非理想相位作交叉检查。投影光与来自脸部向外传播的光方向相反，两者的固定坐标圆偏振分量不能不加区别地套用。

## 五、解析

**第1步：固定眼睛名称、接收端和横向坐标。**

设物理右眼 $R$ 睁开、左眼 $L$ 闭合。镜像的位置虽然与实物成镜面对称，源点名称仍由实物决定。设右镜片的透光轴沿 $\boldsymbol e_x$，左镜片的透光轴沿 $\boldsymbol e_y$，满足
$$
\boldsymbol e_x\cdot\boldsymbol e_y=0.
$$
这只是选择坐标，不限制眼镜在空间中的绝对摆放方向。以下的 $x,y$ 是横向电场轴，垂直于近轴传播方向。

图7-1区分物理源点、器件层次和镜面。两条通道均以右眼接收结束；为了显示器件顺序，通道作展开表示，并非声称每束光都严格沿图上同一条水平直线传播。

![图7-1 两个源点到右眼的往返通道及镜片层次。](../figures/path-07.png){width=96%}

图7-1中的 $P_R,P_L$ 表示两片验偏器，$Q_R,Q_L$ 表示外侧波片，$M$ 表示反射。来自 $R$ 的新式通道为
$$
R\longrightarrow P_R\longrightarrow Q_R\longrightarrow M
\longrightarrow Q_R\longrightarrow P_R\longrightarrow R,
$$
来自 $L$ 而最后被右眼接收的通道为
$$
L\longrightarrow P_L\longrightarrow Q_L\longrightarrow M
\longrightarrow Q_R\longrightarrow P_R\longrightarrow R.
$$
判断可见性只在最后的 $P_R$ 进行，两条光路的出发镜片不相同。

**第2步：从电场投影推得验偏器的选择规律。**

设任意入射电场在固定横向坐标下为
$$
\boldsymbol E(t)=E_x(t)\boldsymbol e_x+E_y(t)\boldsymbol e_y.
$$
理想右验偏器只保留 $x$ 分量，因此
$$
\boldsymbol E_R(t)
=\bigl[\boldsymbol E(t)\cdot\boldsymbol e_x\bigr]\boldsymbol e_x
=E_x(t)\boldsymbol e_x.
$$
左验偏器同理只保留 $y$ 分量。若入射场原来沿与 $x$ 轴成 $\theta$ 的方向，则
$$
\begin{aligned}
\boldsymbol E_{\rm in}(t)
&=E_m\cos\omega t\,
(\cos\theta\,\boldsymbol e_x+\sin\theta\,\boldsymbol e_y),\\
\boldsymbol E_R(t)
&=E_m\cos\theta\cos\omega t\,\boldsymbol e_x,\\
\frac{I_R}{I_{\rm in}}
&=\frac{E_m^2\cos^2\theta}{E_m^2}
=\cos^2\theta.
\end{aligned}
$$
这里先对电场投影，再取时间平均光强；不能先把两个场分量的幅值相加，或把投影系数直接当作光强比例。

**第3步：说明自然光经第一片验偏器后的光强。**

自然光没有一个稳定的横向振动方向。可用均匀分布的线偏振方向求平均，也可用两个等强且互不相干的正交分量描述。前一种方法给出
$$
\begin{aligned}
\left\langle\cos^2\theta\right\rangle
&=\frac1{2\pi}\int_0^{2\pi}\cos^2\theta\,d\theta\\
&=\frac1{2\pi}\int_0^{2\pi}
\frac{1+\cos2\theta}{2}\,d\theta\\
&=\frac1{2\pi}\left[
\frac{\theta}{2}+\frac{\sin2\theta}{4}
\right]_0^{2\pi}\\
&=\frac12.
\end{aligned}
$$
此处使用二倍角公式和对偏振方向的统计平均。于是源点的自然光强若为 $I_{R0}$ 或 $I_{L0}$，穿过其第一片理想验偏器后，强度分别为 $I_{R0}/2$、$I_{L0}/2$。这两个源点不必同样明亮；本题只问某个通道是否消光。

第一片验偏器之后，允许通过的光已经有确定的线偏振方向，因此后面可以使用确定电场的相位法。自然光不能在最初就冒充“两分量固定相位相等”的单一相干场。

**第4步：老式眼镜中来自睁开右眼的光能通过。**

来自物理右眼附近的光向外经过 $P_R$ 后成为 $x$ 线偏振。近轴理想镜面给两横向分量同样的反射系数，不把 $x$ 线偏振转成 $y$ 线偏振。返回右验偏器时，其与透光轴的夹角仍为 $0$，所以
$$
I_{R\to R}
=|r|^2\frac{I_{R0}}2\cos^2 0
=|r|^2\frac{I_{R0}}2.
$$
这里 $r$ 是电场反射系数，$|r|^2$ 是该近轴模型中的强度反射率。只要镜面反射与源点亮度非零，这个通道就可见。

镜面引入的共同相位即使是 $\pi$，也只是把整个电场同时变号，不会使原来的横向线偏振转过 $90^\circ$。

**第5步：老式眼镜中来自闭合左眼的光被挡住。**

来自左眼皮附近的自然光向外经过 $P_L$ 后成为 $y$ 线偏振。镜面反射后仍沿同一固定横向方向振动。返回右镜片时，与其 $x$ 透光轴成 $90^\circ$，于是
$$
\begin{aligned}
I_{L\to R}
&=|r|^2\frac{I_{L0}}2\cos^2 90^\circ\\
&=0.
\end{aligned}
$$
这里消失的是“来自左眼而进入右眼”的光通道，不是左眼皮停止散射光。左眼闭合只意味着它不是观察端，不能据此删除左眼这个物体源。

因此第（1）问的答案为：能看见物理上睁开的右眼的像，闭合左眼的像在理想交叉验偏通道中消光。

**第6步：给新式镜片选择一组相容的主轴。**

让左右波片的主轴在同一横向坐标中平行，取
$$
\boldsymbol e_a
=\frac{\boldsymbol e_x+\boldsymbol e_y}{\sqrt2},
\qquad
\boldsymbol e_b
=\frac{-\boldsymbol e_x+\boldsymbol e_y}{\sqrt2}.
$$
两条主轴互相垂直，右验偏轴 $x$ 和左验偏轴 $y$ 各自与它们成 $45^\circ$。图7-2画的是片面内真实的四个方向，不把光轴画成沿传播方向。

![图7-2 片面内的正交验偏轴与波片主轴。](../figures/axes-07.png){width=68%}

由图7-2可以反解
$$
\begin{aligned}
\boldsymbol e_x
&=\frac{\boldsymbol e_a-\boldsymbol e_b}{\sqrt2},\\
\boldsymbol e_y
&=\frac{\boldsymbol e_a+\boldsymbol e_b}{\sqrt2}.
\end{aligned}
$$
所以两种向外线偏振都有相等的主轴分量振幅，但其中一个分量的相对符号不同。这个正负号将决定两束光产生相反的圆偏振，不能只写“两个镜片都是 $45^\circ$”就认为它们的偏振态相同。

上述是一种有效的对称配置，不是唯一的绝对空间朝向。整体转动两片的验偏轴和主轴，仍保持相对角度即可；交换主轴或改变相位符号时，左右投影偏振通道也须相应交换。

**第7步：从光程差推得波片相位，说明正负号。**

采用复振幅约定
$$
\boldsymbol E(t)=\operatorname{Re}
\bigl(\boldsymbol{\mathcal E}\,e^{i\omega t}\bigr).
$$
一束向外传播的单色光经过折射率为 $n$、厚度为 $d$ 的平板，在这一时间约定下获得传播相位 $-2\pi nd/\lambda_0$，其中 $\lambda_0$ 是真空波长。

若 $a,b$ 主轴折射率分别为 $n_a,n_b$，两分量的相位变化为
$$
\begin{aligned}
\phi_a&=-\frac{2\pi n_a d}{\lambda_0},\\
\phi_b&=-\frac{2\pi n_b d}{\lambda_0},\\
\delta\equiv\phi_b-\phi_a
&=\frac{2\pi(n_a-n_b)d}{\lambda_0}.
\end{aligned}
$$
扣除共同相位 $\phi_a$ 后，波片使 $a$ 分量不变、$b$ 分量乘以 $e^{i\delta}$。若把 $a$ 轴选为光轴，则 $n_a=n_e,n_b=n_o$。若选择另一条为光轴，相位符号就反过来。

题设四分之一波片所需的是相位差的大小为 $\pi/2$，而不是在任何主轴命名下都必须取同一个正号。下文具体计算取
$$
\delta=+\frac\pi2.
$$
取 $-\pi/2$ 会交换两种圆偏振的固定坐标表达，但双程后的线偏振正交结论不变。

**第8步：说明等振幅与四分之一周期相位为何产生圆偏振。**

设入射线偏振在主轴上具有相等、同号的分量，振幅参数为 $E_m$。扣除共同相位后，第一次波片的出射场为
$$
\begin{aligned}
E_a(t)&=\frac{E_m}{\sqrt2}\cos\omega t,\\
E_b(t)&=\frac{E_m}{\sqrt2}
\cos\left(\omega t+\frac\pi2\right)
=-\frac{E_m}{\sqrt2}\sin\omega t.
\end{aligned}
$$
平方后相加，
$$
\begin{aligned}
E_a^2+E_b^2
&=\frac{E_m^2}{2}
\left(\cos^2\omega t+\sin^2\omega t\right)\\
&=\frac{E_m^2}{2}.
\end{aligned}
$$
这是电场矢量端点在横向平面上运动的圆，半径为 $E_m/\sqrt2$。图7-3中的圆表示一个固定空间位置处电场端点随时间的轨迹，不是光线沿圆形路径前进。

![图7-3 主轴分量的相位积累与横向偏振轨迹。](../figures/states-07.png){width=96%}

图7-3左侧同号分量对应 $\boldsymbol e_y$ 线偏振，中间相对相位为 $\pi/2$，右侧双程后相对相位为 $\pi$，对应 $\boldsymbol e_x$ 线偏振。圆轨迹只在中间的单程阶段出现，最后不是圆偏振。

若初始分量为异号，旋转方向与同号情况相反。相等振幅是圆而非椭圆的必要条件之一；只有相位差正确、振幅却不相等，仍是椭圆。

**第9步：用连续四阶段相位法追踪来自左眼的光。**

来自左眼的光经 $P_L$ 后沿 $\boldsymbol e_y$，按第6步分解为同号的两个主轴分量。设在这一步选定的时间原点使两分量相位均为零，则原始主轴电场为
$$
\left(
\frac{E_m}{\sqrt2}\cos\omega t,\ 
\frac{E_m}{\sqrt2}\cos\omega t
\right).
$$
第一次经过 $Q_L$，第二分量增加 $\pi/2$，
$$
\left(
\frac{E_m}{\sqrt2}\cos\omega t,\ 
\frac{E_m}{\sqrt2}\cos\left(\omega t+\frac\pi2\right)
\right).
$$
镜面的共同反射相位可记为 $\phi_M$。为了与四阶段相位写法一一对应，先取 $\phi_M=\pi$，则反射后为
$$
\left(
\frac{E_m}{\sqrt2}\cos(\omega t+\pi),\
\frac{E_m}{\sqrt2}\cos\left(\omega t+\frac{3\pi}{2}\right)
\right).
$$
返回通过 $Q_R$ 时，$b$ 分量再次增加 $\pi/2$，于是
$$
\left(
\frac{E_m}{\sqrt2}\cos(\omega t+\pi),\
\frac{E_m}{\sqrt2}\cos(\omega t+2\pi)
\right).
$$
这些相位逐次相加，没有在返回时把前一遍的波片作用减去。

**第10步：将双程后的场化简为确定的线偏振方向。**

利用
$$
\cos(\omega t+\pi)=-\cos\omega t,
\qquad
\cos(\omega t+2\pi)=\cos\omega t,
$$
第9步的最终场成为
$$
\begin{aligned}
\boldsymbol E_{\rm ret}(t)
&=\frac{E_m}{\sqrt2}\cos\omega t
(-\boldsymbol e_a+\boldsymbol e_b)\\
&=-E_m\cos\omega t\,\boldsymbol e_x.
\end{aligned}
$$
最后一个等号使用图7-2给出的
$\boldsymbol e_x=(\boldsymbol e_a-\boldsymbol e_b)/\sqrt2$。
负号是整体相位差 $\pi$，不改变线偏振轴。返回光沿 $x$ 轴，所以能通过右验偏器 $P_R$。

若镜面的共同相位不是 $\pi$，而是任意 $\phi_M$，最终两分量相位为 $\phi_M$ 和 $\phi_M+\pi$，仍有
$$
\begin{aligned}
\boldsymbol E_{\rm ret}(t)
&=\frac{E_m}{\sqrt2}\cos(\omega t+\phi_M)
(\boldsymbol e_a-\boldsymbol e_b)\\
&=E_m\cos(\omega t+\phi_M)\boldsymbol e_x.
\end{aligned}
$$
因此结论不依赖某一特定共同反射相位。真正使偏振轴改变的是两次波片累计产生的相对 $\pi$，不是共同的镜面半波损失。

**第11步：同样完整追踪来自右眼的光。**

来自右眼的光经 $P_R$ 后沿 $\boldsymbol e_x$，其两个主轴分量初始相反：
$$
\boldsymbol E_{\rm start}(t)
=\frac{E_m}{\sqrt2}\cos\omega t
(\boldsymbol e_a-\boldsymbol e_b).
$$
可以把负号保留在振幅中，也可以改写成 $b$ 分量的初始相位为 $\pi$；两种表示不能同时计入这个负号。

保留负振幅，令镜面共同系数为 $r$，双程波片对 $b$ 分量的相位因子为
$$
e^{i(\pi/2+\pi/2)}=e^{i\pi}=-1.
$$
于是初始的主轴复振幅
$$
\frac{E_m}{\sqrt2}
\begin{pmatrix}1\\-1\end{pmatrix}
$$
变为
$$
\frac{rE_m}{\sqrt2}
\begin{pmatrix}1\\(-1)(-1)\end{pmatrix}
=\frac{rE_m}{\sqrt2}
\begin{pmatrix}1\\1\end{pmatrix}.
$$
再用图7-2的 $\boldsymbol e_y$ 分解式，返回光沿 $y$ 轴。它与最后的 $P_R$ 垂直，因此被挡住。来自右眼的通道与第10步的左眼通道相互交换，不是两个通道都通过或都被阻挡。

**第12步：写出新式眼镜的镜中观察结果。**

理想波片不吸收光，因而第一片验偏器之后的强度除镜面反射损耗外不变。最后一次方向筛选给出
$$
\begin{aligned}
I_{L\to R}
&=|r|^2\frac{I_{L0}}2\cos^2 0
=|r|^2\frac{I_{L0}}2,\\
I_{R\to R}
&=|r|^2\frac{I_{R0}}2\cos^2 90^\circ
=0.
\end{aligned}
$$
所以新式眼镜下，物理上闭合左眼的像能够被睁开的右眼看见，而睁开右眼的像消光。这与第（1）问相反。

“能看见闭眼的像”不意味着闭眼成为接收端，也不是把右眼的像改称镜中的左眼。被看见的物体是左眼及其眼皮，观察者仍用右眼接收光。

**第13步：建立投影矩阵，独立核验旧式通道。**

将复振幅按固定 $x,y$ 坐标写成列向量
$$
\boldsymbol{\mathcal E}
=\begin{pmatrix}\mathcal E_x\\\mathcal E_y\end{pmatrix}.
$$
两个理想验偏器分别对应
$$
P_R=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
P_L=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
$$
矩阵作用的顺序从右向左读，即最先经过的器件放在乘积最右边。镜面为 $M=rI$，其中 $I$ 是单位矩阵。旧式两个通道于是为
$$
\begin{aligned}
P_RMP_R&=rP_R^2=rP_R,\\
P_RMP_L&=rP_RP_L
=\begin{pmatrix}0&0\\0&0\end{pmatrix}.
\end{aligned}
$$
这里使用了 $P_R^2=P_R$ 以及 $P_RP_L=0$。第一式允许右源点的 $x$ 分量通过，第二式将左源点已被选成的 $y$ 分量全部消去，与第4、5步相同。

矩阵法不是另一套不同的物理假设，只是把电场投影与相位叠加线性化，适合逐项检查器件先后次序。

**第14步：由主轴分解构造波片矩阵，展开每一个元素。**

设 $a$ 轴与 $x$ 轴的夹角为 $\chi$。由主轴坐标变回实验室坐标的旋转矩阵为
$$
F(\chi)=
\begin{pmatrix}
\cos\chi&-\sin\chi\\
\sin\chi&\cos\chi
\end{pmatrix}.
$$
其两列分别是 $\boldsymbol e_a,\boldsymbol e_b$ 的分量，故先用 $F^{\mathsf T}$ 将入射场投到主轴，再积累相位，最后用 $F$ 变回原坐标：
$$
Q(\chi,\delta)
=F(\chi)
\begin{pmatrix}1&0\\0&e^{i\delta}\end{pmatrix}
F^{\mathsf T}(\chi).
$$
令 $c=\cos\chi$、$s=\sin\chi$，先乘左侧两项，
$$
F
\begin{pmatrix}1&0\\0&e^{i\delta}\end{pmatrix}
=
\begin{pmatrix}
c&-se^{i\delta}\\
s&ce^{i\delta}
\end{pmatrix}.
$$
再右乘 $F^{\mathsf T}$，得到
$$
Q=
\begin{pmatrix}
c^2+s^2e^{i\delta}&cs(1-e^{i\delta})\\
cs(1-e^{i\delta})&s^2+c^2e^{i\delta}
\end{pmatrix}.
$$
这个矩阵没有删掉两条主轴中的任意一条，并且满足 $Q^\dagger Q=I$，表示无吸收波片保持强度；上标 $\dagger$ 表示共轭转置。

取 $\chi=\pi/4,\delta=\pi/2$，由 $c=s=1/\sqrt2$、$e^{i\pi/2}=i$ 得
$$
Q=\frac12
\begin{pmatrix}
1+i&1-i\\
1-i&1+i
\end{pmatrix}.
$$
这一步的复数正负号来自主轴投影，不能用“转 $45^\circ$”替代实际相位计算。

**第15步：计算两次波片的乘积，并说明为什么不是逆矩阵。**

在同一固定横向坐标下，两块波片主轴平行、相位配置相同。光反向通过均匀互易波片时，实际走过的晶体厚度仍为正的 $d$，两主轴的传播光程仍分别为 $n_a d,n_b d$。因此返回时再乘同一个 $Q$，不是乘 $Q^{-1}$。

矩阵中也可直接看出：本模型 $Q^{\mathsf T}=Q$，互易反向传输在固定端口横向基底中的转置仍为同一矩阵。逆矩阵代表把原来的相位真正减回去，需要相反延迟的补偿器件，不能仅靠光路反向实现。

令
$$
a=\frac{1+i}{2},\qquad b=\frac{1-i}{2},
$$
则
$$
Q^2=
\begin{pmatrix}
a^2+b^2&2ab\\
2ab&a^2+b^2
\end{pmatrix}.
$$
逐项计算，
$$
\begin{aligned}
a^2+b^2
&=\frac{(1+i)^2+(1-i)^2}{4}\\
&=\frac{2i-2i}{4}=0,\\
2ab&=\frac{(1+i)(1-i)}2
=\frac{1-i^2}{2}=1.
\end{aligned}
$$
所以
$$
Q^2=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$
双程波片将 $x$ 线偏振映成 $y$，将 $y$ 映成 $x$。镜面共同系数 $r$ 与矩阵可交换，不影响轴交换。

**第16步：将两条新式光路的完整矩阵逐项相乘。**

按照图7-1，来自右眼的乘积是
$$
\begin{aligned}
P_RQMQP_R
&=rP_RQ^2P_R\\
&=r
\begin{pmatrix}1&0\\0&0\end{pmatrix}
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\begin{pmatrix}1&0\\0&0\end{pmatrix}\\
&=\begin{pmatrix}0&0\\0&0\end{pmatrix}.
\end{aligned}
$$
来自左眼、最后进入右眼的乘积为
$$
\begin{aligned}
P_RQMQP_L
&=rP_RQ^2P_L\\
&=r
\begin{pmatrix}1&0\\0&0\end{pmatrix}
\begin{pmatrix}0&1\\1&0\end{pmatrix}
\begin{pmatrix}0&0\\0&1\end{pmatrix}\\
&=r\begin{pmatrix}0&1\\0&0\end{pmatrix}.
\end{aligned}
$$
这个非零矩阵将左源点的 $y$ 分量送到右接收端的 $x$ 分量。它不是把眼睛的位置移走，而是交换光的横向偏振通道。完整乘积再一次得到第12步结果。

**第17步：反求左右投影镜头必须送入的偏振态。**

投影光从银幕侧入射，依次经过 $Q$、$P_R$ 或 $P_L$。因此要让右镜片通过、左镜片阻挡，必须先经 $Q$ 变成 $x$ 线偏振。反求入射态相当于解
$$
Q\boldsymbol{\mathcal E}_{R,\rm in}
\ \parallel\ \begin{pmatrix}1\\0\end{pmatrix}.
$$
定义两种归一化圆偏振复振幅
$$
C_+=\frac1{\sqrt2}\begin{pmatrix}1\\i\end{pmatrix},
\qquad
C_-=\frac1{\sqrt2}\begin{pmatrix}1\\-i\end{pmatrix}.
$$
先算 $QC_+$：
$$
\begin{aligned}
QC_+
&=\frac1{2\sqrt2}
\begin{pmatrix}
(1+i)+i(1-i)\\
(1-i)+i(1+i)
\end{pmatrix}\\
&=\frac1{2\sqrt2}
\begin{pmatrix}2+2i\\0\end{pmatrix}
=e^{i\pi/4}\begin{pmatrix}1\\0\end{pmatrix}.
\end{aligned}
$$
再算 $QC_-$：
$$
\begin{aligned}
QC_-
&=\frac1{2\sqrt2}
\begin{pmatrix}
(1+i)-i(1-i)\\
(1-i)-i(1+i)
\end{pmatrix}\\
&=\frac1{2\sqrt2}
\begin{pmatrix}0\\2-2i\end{pmatrix}
=e^{-i\pi/4}\begin{pmatrix}0\\1\end{pmatrix}.
\end{aligned}
$$
因此在本节明确的固定坐标与 $\delta=+\pi/2$ 约定下，右眼图像的投影光取 $C_+$，左眼图像的投影光取 $C_-$。两者是相反旋转方向的圆偏振，且
$$
C_+^\dagger C_-=0.
$$
两投影通道理想情况下可被完全区分。

图7-4表示银幕光向眼睛入射的路径，与图7-1来自脸部的向外路径不是同一传播方向。

![图7-4 两种圆偏振投影光经波片恢复正交线偏振。](../figures/projectors-07.png){width=92%}

图7-4中的 $C_+$ 经 $Q$ 变成 $x$，通过 $P_R$；$C_-$ 经 $Q$ 变成 $y$，通过 $P_L$。这些符号就是上述矩阵计算所用的场分量，图不是独立于计算的装饰。

**第18步：区分向外圆偏振与银幕入射圆偏振。**

向外从右镜片出发的场是
$$
\begin{aligned}
Q\begin{pmatrix}1\\0\end{pmatrix}
&=\frac12\begin{pmatrix}1+i\\1-i\end{pmatrix}\\
&=e^{i\pi/4}C_-.
\end{aligned}
$$
而银幕送向右眼、能够被选中的场是第17步的 $C_+$。它们在固定实验室 $x,y$ 分量中看起来符号相反，是因为所说的“向外发出”和“向内送入”不是同一个传播方向；不能把前一个结果直接作为投影镜头的入射状态。

在 $\operatorname{Re}(\boldsymbol{\mathcal E}e^{i\omega t})$ 约定下，
$$
\begin{aligned}
C_+:\quad (E_x,E_y)
&\propto(\cos\omega t,-\sin\omega t),\\
C_-:\quad (E_x,E_y)
&\propto(\cos\omega t,\sin\omega t).
\end{aligned}
$$
它们在同一固定横向平面内反向旋转。若使用“左旋、右旋”名称，必须同时说明观察方向和时间约定；本题用显式分量表达可以避免不同命名惯例的歧义。

镜面反射后传播方向反转，按传播方向定义的旋向名称会变，但在固定实验室坐标中共同反射系数不需要另加一次未经说明的横向符号翻转。

**第19步：推得四分之一波片厚度并检查量纲。**

由第7步的光程相位，
$$
|\delta|=\frac{2\pi|n_e-n_o|d}{\lambda_0}.
$$
最低阶四分之一波片取 $|\delta|=\pi/2$，所以
$$
\begin{aligned}
\frac{2\pi|n_e-n_o|d}{\lambda_0}
&=\frac\pi2,\\
4|n_e-n_o|d&=\lambda_0,\\
d&=\frac{\lambda_0}{4|n_e-n_o|}.
\end{aligned}
$$
折射率无量纲，$\lambda_0$ 与 $d$ 都是长度，量纲正确。若 $n_e=n_o$，有限厚度不能产生相对延迟，不能把上式的发散误说成“极厚仍能实现题设”。

更高阶的奇数四分之一周期厚度为
$$
d_m=\frac{(2m+1)\lambda_0}{4|n_e-n_o|},
\qquad m=0,1,2,\ldots.
$$
不同奇数阶的单程相位可能为 $+\pi/2$ 或 $-\pi/2$ 模 $2\pi$，从而交换两投影圆偏振的对应方向；双程的相对相位仍为奇数倍 $\pi$。不能只增加整片厚度却完全忽略旋向对应。

**第20步：用一般相位与安装角求实际漏光。**

令波片主轴与右验偏轴成 $\chi$，单程相位为任意 $\delta$。第14步的两个旋转矩阵相邻相消，
$$
\begin{aligned}
Q^2
&=F
\begin{pmatrix}1&0\\0&e^{i\delta}\end{pmatrix}
F^{\mathsf T}F
\begin{pmatrix}1&0\\0&e^{i\delta}\end{pmatrix}
F^{\mathsf T}\\
&=F
\begin{pmatrix}1&0\\0&e^{2i\delta}\end{pmatrix}
F^{\mathsf T}.
\end{aligned}
$$
从 $x$ 出发后转到 $y$ 的复振幅系数为
$$
A_{\perp}=cs(1-e^{2i\delta}).
$$
展开其模平方，
$$
\begin{aligned}
|A_{\perp}|^2
&=c^2s^2(1-e^{2i\delta})(1-e^{-2i\delta})\\
&=c^2s^2(2-2\cos2\delta)\\
&=4c^2s^2\sin^2\delta\\
&=\sin^2(2\chi)\sin^2\delta.
\end{aligned}
$$
此处依次使用复数与其共轭相乘、欧拉公式以及二倍角公式。无吸收时其余强度仍在原来的 $x$ 通道，因此
$$
g_{\perp}=\sin^2(2\chi)\sin^2\delta,
\qquad
g_{\parallel}=1-g_{\perp}.
$$
两个 $g$ 的归一化基准是第一次验偏器之后的强度，不是原来自然光的总强度。自然光往返实际光强还要乘以 $I_0/2$ 与镜面反射率。

图7-5取 $\chi=45^\circ$，画出两种通道随单程相位的变化。

![图7-5 正确安装角下的同轴与交叉通道强度。](../figures/leakage-07.png){width=78%}

按图7-5，$\delta=0$ 时双程不改变线偏振，$g_{\parallel}=1$；$\delta=\pi/2$ 时正交交换，$g_{\perp}=1$；$\delta=\pi$ 时双程相对相位为 $2\pi$，回到原方向。曲线上两强度之和恒为 $1$，符合波片无吸收的能量约束。

**第21步：用极限情况检查器件顺序与旋向。**

在正确安装角下，
$$
g_{\parallel}=\cos^2\delta,\qquad
g_{\perp}=\sin^2\delta.
$$
把 $\delta$ 换为 $-\delta$，两种强度不变，证明改用相反主轴相位约定不会改变“旧式看睁眼、新式看闭眼”的答案。单程圆偏振的旋向对应则必须一起交换，不能据强度不变就忽略其分量符号。

若 $\chi=0$，输入沿波片主轴，只获得共同相位而不产生另一主轴分量，故
$$
g_{\perp}=0.
$$
这说明“具有四分之一相位差的薄片”不意味着对任意入射线偏振都转成圆偏振。题设的 $45^\circ$ 不是可有可无的附属信息。

此外，若将波片放到靠近眼睛的一侧，使向外器件顺序变为 $Q$ 后 $P$，光在离开镜片前已被最后的验偏器重新选成线偏振。第（2）问的正交交换论证就不能直接使用，因为最后的验偏器已将第一次波片产生的两个分量重新筛选。器件层次不满足题设时，不能仍套用中间相邻的 $Q^2$ 来代替真实路径。

**第22步：汇总两问并明确适用范围。**

在理想模型下：
$$
\begin{aligned}
\text{老式正交线偏振镜片：}&\quad
I_{R\to R}>0,\qquad I_{L\to R}=0;\\
\text{外侧四分之一波片的新式镜片：}&\quad
I_{R\to R}=0,\qquad I_{L\to R}>0.
\end{aligned}
$$
因此第（1）问看见睁开的右眼；第（2）问看见闭合的左眼。新式眼镜两片验偏轴正交，每片验偏轴与其波片主轴成 $45^\circ$；采用同向主轴、同相位配置时，两投影镜头发出相反旋转方向的圆偏振。具体 $C_+$、$C_-$ 对应须与选定主轴及传播方向一致。

若波片只在某设计波长准确满足四分之一周期，宽光谱中其他波长一般会产生椭圆态与漏光；若镜面斜入射造成两个主轴反射系数不同，还需用实际镜面矩阵替代 $rI$。这些条件改变理想消光程度，不否定上述在题设近轴、单色、理想器件范围内的完整结论。

## 六、关键洞察

**洞察1：镜面不是选择哪只眼睛的最后器件。**

真正的判据是最后一个 $P_R$ 选取哪个电场分量。只说镜子使圆偏振“反手”，没有追踪下一块波片和验偏器，还没有回答可见性问题。图7-1的两个源点、两种出发镜片和同一个接收端必须保持分明。

波片双程主轴延迟从 $\delta$ 变成 $2\delta$。当 $\chi=45^\circ$、$2\delta=\pi$ 时，它等效于将两个线偏振轴交换的半波器件。因此第一问的同源通道与第二问的异源通道互换，是完整路径的线性作用，不是眼睛名称的语言交换。

**洞察2：投影光的设计是一次逆问题，而镜面实验是两次正向相位积累。**

为了给右眼送入图像，必须解 $Q\boldsymbol{\mathcal E}_{\rm in}\parallel x$，因此输入态可通过 $Q^{-1}x$ 求出。但镜面实验中实际第二遍通过晶体，作用是再次乘 $Q$。这里一个逆矩阵来自“反求待定输入”，另一个是否用逆矩阵来自“实际传播”，不能因为二者都含“反”字就混同。

用第17步结果验证，
$$
Q^{-1}\begin{pmatrix}1\\0\end{pmatrix}
=e^{-i\pi/4}C_+,
$$
而第18步的向外场为
$$
Q\begin{pmatrix}1\\0\end{pmatrix}
=e^{i\pi/4}C_-.
$$
两式都正确，描述的任务却不同。对应传播方向与端口明确以后，就不再需要用模糊的左右旋口诀弥补符号问题。

**洞察3：整体相位与相对相位的作用完全不同。**

镜面共同相位 $\phi_M$ 对任意输入只增加因子 $e^{i\phi_M}$。两分量相对相位不变，轨迹类别不变。两次波片只对某一主轴分量增加 $\pi$，却使同号分量变成异号分量。

若光经两遍之后的主轴场是
$$
\begin{pmatrix}A\\Ae^{i\pi}\end{pmatrix}
=\begin{pmatrix}A\\-A\end{pmatrix},
$$
它沿一条固定直线振动。这里的第二分量负号是真正的相对负号；把整个列向量一起变号则只对应共同相位，不能再造成第二次轴旋转。

**洞察4：头部转动对线偏振与圆偏振系统的影响不同。**

老式系统中，银幕上的线偏振轴固定。若整个眼镜转过角 $\alpha$，原来属于右眼的光通过右片的比例变为 $\cos^2\alpha$，漏到左片的比例变为 $\sin^2\alpha$。

新式系统中，让波片与验偏器一起转动、仍保持内部 $45^\circ$。把实验室圆偏振 $C_+$ 写入转动后的局部坐标，
$$
F^{\mathsf T}(\alpha)C_+=e^{i\alpha}C_+.
$$
这只是共同相位，局部圆偏振状态不变。因此理想圆偏振输入的通道选择不因头部转角而改变。这里说明的是银幕入射通道，不是任意斜入射、任意三维头部姿态都保持完美；偏离正常入射仍可能破坏波片设计条件。

**洞察5：退偏与相干相位错误不是同一种效应。**

确定频率、确定方向的波片延迟误差，会把纯偏振态变成另一个纯偏振态，通常是椭圆；其相干信息仍可用复振幅描述。不同波长或不同传播方向的混合光若被一起平均，可能不能再用一个确定的列向量表示，应对各组分强度或相干矩阵统计求和。

自然光入射时的相干矩阵可写作
$$
J_0=\frac{I_0}{2}I.
$$
第一片验偏器之后，
$$
P_RJ_0P_R^\dagger
=\frac{I_0}{2}P_R,
$$
表示只剩一个确定的横向线偏振通道。随后波片保持其强度。这个顺序解释了为何主解可以先处理自然光统计，再对被选出的分量使用相位法，而不是在自然光起点擅自给两分量指定稳定相位。

## 七、易错点

1. 把“镜子里左右相反”当作偏振选择的依据。必须追踪物理源点 $R,L$，最终接收端始终为睁开的右眼。

2. 因左眼闭合就认为左眼完全不反射光。闭合眼皮仍可被照亮并成像，消光是镜片通道筛选，不是源点消失。

3. 把验偏器透光轴与光传播轴混为一谈。图7-2的四条轴都在横向片面内，题设晶体光轴也在片面内。

4. 把“波片在验偏器前”理解为从脸向外仍先过波片。银幕侧为前方，向外顺序是 $P$ 后 $Q$，向内顺序是 $Q$ 后 $P$。

5. 认为反向通过波片必然乘 $Q^{-1}$。真实光程不会因为传播方向反转而变为负厚度；采用同一固定坐标应再次积累相位。

6. 把共同镜面相位 $\pi$ 说成将线偏振轴转过 $90^\circ$。两分量同时变号不改变轴，轴交换来自双程相对相位。

7. 忽略初始异号主轴分量，导致左右眼产生同一种圆偏振。$x=(a-b)/\sqrt2$ 与 $y=(a+b)/\sqrt2$ 的符号必须保留。

8. 在负振幅上又额外添加一次 $\pi$ 初相位。负振幅与相位增加 $\pi$ 是等价表达，不能双重计数。

9. 只满足相位差 $\pi/2$ 就断言圆偏振。两主轴分量还须等振幅；一般方向输入会成为椭圆。

10. 未说明观察方向就把圆偏振称为左旋或右旋。优先使用 $C_\pm$ 的明确分量，再说明时间、传播和观察约定。

11. 把向外 $Q\boldsymbol e_x$ 的结果直接交给投影镜头。银幕的入射态要通过 $Q$ 后成为允许轴，是反求输入，而不是复用相反传播的输出。

12. 混淆场幅比与光强比。漏光比例取复振幅模平方；自然光还要计入第一片验偏器的 $1/2$。

13. 用 $\cos^2\delta$ 的漏光公式时忘记其适用安装角为 $45^\circ$。一般角度必须使用 $1-\sin^2(2\chi)\sin^2\delta$。

14. 认为实际白光镜面实验必然只能看见一只眼睛。实际波片色散、斜入射和有限消光比可能使另一个像有微弱亮度；理想答案需限定题设模型。

## 八、课堂讲解建议

课堂先画图7-1并保持眼睛名称固定。让学生指出每个箭头从哪个物体出发、最后由哪只眼睛接收，再在板书中写两条器件顺序。若尚未读清层次，不宜先宣布新式答案，否则容易把正确结论记成镜像左右互换的口诀。

讲老式系统时，先用一个验偏器的电场投影推得马吕斯定律，再让学生分别计算右源和左源最后的夹角。教师应特别区分“左眼不能观察”与“左眼皮不能被观察”，以免在最早一步就把左源删除。

新式部分先沿图7-2分解 $x,y$ 线偏振。板书保留两组主轴振幅中的正负号，再用图7-3逐列加相位。第一遍的 $\pi/2$、共同镜面相位、第二遍的 $\pi/2$ 分开书写，最后才化简三角函数。这样每一次状态变化都有来源，不靠“反射一次反手一次”的口头计数。

课堂中的核心检验问题可以是：若镜面的共同相位从 $\pi$ 改成任意 $\phi_M$，哪个相对相位改变、哪个不变？再问：若波片主轴与验偏轴重合，是否仍能交换两眼图像？两问分别检验共同相位和等振幅条件，比只复述结论更能揭示理解程度。

矩阵法安排在相位法之后。教师先说明乘积从右向左作用，让学生用矩阵恢复已经理解的两条路径；不要让尚未建立物理图像的学生把多个矩阵相乘当作无意义计算。图7-4随后用来区分正向发出与逆向设计，图7-5用来说明理想消光不是离开设计条件后仍自动成立。

变式讲解应把误差量统一换成弧度，再作二阶展开；安装角误差系数为 $4$、相位误差系数为 $1$ 有明确来源。最后用反装层次的变式检验图7-1是否真正理解，而不是只学会某个固定矩阵答案。

## 九、变式训练

**变式1：设计厚度与非设计波长的完整漏光计算。**

某波片在真空波长 $\lambda_0=550\ \mathrm{nm}$ 时按最低阶四分之一波片设计，主轴折射率之差的大小为 $0.0090$。忽略在 $550$ 至 $650\ \mathrm{nm}$ 内的色散，求厚度。若改用 $650\ \mathrm{nm}$ 光，且安装角仍为 $45^\circ$，求镜面双程后保留原线偏振方向与转到正交方向的强度比例。

先把波长换成米，
$$
\lambda_0=550\times10^{-9}\ \mathrm m.
$$
按第19步，
$$
\begin{aligned}
d&=\frac{550\times10^{-9}}{4\times0.0090}\ \mathrm m\\
&=1.5277778\times10^{-5}\ \mathrm m\\
&=15.277778\ \mathrm{\mu m}.
\end{aligned}
$$
折射率差近似不变时，单程相位大小与真空波长成反比。因此
$$
\begin{aligned}
|\delta_{650}|
&=\frac{2\pi(0.0090)d}{650\times10^{-9}}\\
&=\frac\pi2\frac{550}{650}
=\frac{11\pi}{26}\\
&\approx1.32913535\ \mathrm{rad}.
\end{aligned}
$$
这个值小于设计相位 $\pi/2$，第二遍后相对相位并未达到恰好 $\pi$。在安装角为 $45^\circ$ 的条件下，
$$
\begin{aligned}
g_{\parallel}
&=\cos^2\left(\frac{11\pi}{26}\right)
\approx0.05727199,\\
g_{\perp}
&=\sin^2\left(\frac{11\pi}{26}\right)
\approx0.94272801.
\end{aligned}
$$
所以原方向漏光约 $5.7272\%$，正交转换约 $94.2728\%$。这两个比例以第一片验偏器之后的强度为基准；若原来是强度 $I_0$ 的自然光，则对应返回强度为
$$
|r|^2\frac{I_0}{2}g_{\parallel},
\qquad
|r|^2\frac{I_0}{2}g_{\perp}.
$$
二者相加为 $|r|^2I_0/2$，与无吸收波片的能量要求一致。若材料有色散，须把 $|n_e-n_o|$ 换成该波长实际数值，不能保留这个无色散比例作为精确答案。

**变式2：安装角误差以及两种小误差的二阶展开。**

保持波片相位为 $\pi/2$，但主轴与右验偏轴夹角从 $45^\circ$ 变成 $40^\circ$。求原方向漏光。再设一般小误差
$$
\chi=\frac\pi4+\varepsilon_\chi,
\qquad
\delta=\frac\pi2+\varepsilon_\delta,
$$
其中误差用弧度表示，求最低非零阶的漏光近似。

安装角为 $40^\circ$ 时，第20步给出
$$
\begin{aligned}
g_{\parallel}
&=1-\sin^2(80^\circ)\sin^2(90^\circ)\\
&=1-\sin^2(80^\circ)
=\cos^2(80^\circ)\\
&\approx0.03015369.
\end{aligned}
$$
漏光约 $3.0154\%$，正交通道约 $96.9846\%$。不要将 $5^\circ$ 的安装角误差直接平方而忘记度与弧度的转换。

对两种小误差，先写出精确式
$$
\begin{aligned}
g_{\parallel}
&=1-\sin^2\left(\frac\pi2+2\varepsilon_\chi\right)
       \sin^2\left(\frac\pi2+\varepsilon_\delta\right)\\
&=1-\cos^2(2\varepsilon_\chi)
       \cos^2\varepsilon_\delta.
\end{aligned}
$$
此处用 $\sin(\pi/2+z)=\cos z$。利用泰勒展开
$$
\cos z=1-\frac{z^2}{2}+O(z^4),
$$
平方后为
$$
\cos^2z=1-z^2+O(z^4).
$$
分别代入，
$$
\begin{aligned}
\cos^2(2\varepsilon_\chi)
&=1-4\varepsilon_\chi^2+O(\varepsilon_\chi^4),\\
\cos^2\varepsilon_\delta
&=1-\varepsilon_\delta^2+O(\varepsilon_\delta^4).
\end{aligned}
$$
再乘并保留总二阶，
$$
\begin{aligned}
g_{\parallel}
&=1-
(1-4\varepsilon_\chi^2)
(1-\varepsilon_\delta^2)
+O\!\left(
\varepsilon_\chi^4+\varepsilon_\delta^4
+\varepsilon_\chi^2\varepsilon_\delta^2
\right)\\
&=4\varepsilon_\chi^2+\varepsilon_\delta^2
+O\!\left(
\varepsilon_\chi^4+\varepsilon_\delta^4
+\varepsilon_\chi^2\varepsilon_\delta^2
\right).
\end{aligned}
$$
没有一次项，说明理想安装点是消光极小值。也没有二阶混合项 $\varepsilon_\chi\varepsilon_\delta$，两种误差的最低阶贡献相加；四阶才出现两者乘积。

**变式3：头部转动 $30^\circ$ 时的线偏振串扰与圆偏振不变性。**

银幕为右眼发送固定 $x$ 线偏振。老式眼镜绕近轴传播方向转过 $\alpha=30^\circ$，求右、左通道比例。新式眼镜中波片与验偏器作为整体转动、内部相对夹角仍为 $45^\circ$，对于右眼圆偏振 $C_+$ 是否也产生同样串扰？

老式右验偏轴与银幕 $x$ 夹角为 $\alpha$，左验偏轴与其正交，故
$$
\begin{aligned}
g_R&=\cos^2\alpha=\cos^2 30^\circ=\frac34,\\
g_L&=\sin^2\alpha=\sin^2 30^\circ=\frac14.
\end{aligned}
$$
这是入射已为线偏振的投影光，不应再乘自然光的 $1/2$。右眼目标图像有 $25\%$ 理想偏振泄漏进入错误通道。

新式中先把 $C_+$ 写入随眼镜转动的局部坐标。展开旋转矩阵，
$$
\begin{aligned}
F^{\mathsf T}(\alpha)C_+
&=\frac1{\sqrt2}
\begin{pmatrix}
\cos\alpha&\sin\alpha\\
-\sin\alpha&\cos\alpha
\end{pmatrix}
\begin{pmatrix}1\\i\end{pmatrix}\\
&=\frac1{\sqrt2}
\begin{pmatrix}
\cos\alpha+i\sin\alpha\\
-\sin\alpha+i\cos\alpha
\end{pmatrix}\\
&=\frac{e^{i\alpha}}{\sqrt2}
\begin{pmatrix}1\\i\end{pmatrix}
=e^{i\alpha}C_+.
\end{aligned}
$$
第二行的第二分量可写为
$i(\cos\alpha+i\sin\alpha)$，所以确实得到共同因子，而不是两个不同相位因子。

局部波片仍按相同 $Q$ 工作，
$$
QF^{\mathsf T}(\alpha)C_+
=e^{i(\alpha+\pi/4)}
\begin{pmatrix}1\\0\end{pmatrix}.
$$
右验偏器允许其全部通过，左验偏器取零。于是
$$
g_R=1,\qquad g_L=0.
$$
在这一正常入射、纯圆偏振且两层一起转动的模型中，头部横向转角只改变共同相位，不造成旧式的串扰。若只有验偏器单独转、波片不随动，或者头部转动改变了入射倾角，模型已变，不能使用这个结论。

**变式4：将波片反装到靠眼侧，能否保持原效果？**

仍取相同正交验偏轴和理想四分之一波片，但把层次交换：波片靠眼睛、验偏器靠镜面或银幕。求镜面实验看见哪只眼睛，并检查这种反装眼镜能否区分两种投影圆偏振。

图7-6只比较层次，波片主轴与相位数值保持不变。

![图7-6 正确层次与反装层次的传播顺序比较。](../figures/order-07.png){width=75%}

按图7-6，反装后来自源点 $s$ 的向外顺序为 $Q_s$ 后 $P_s$，返回进入右眼时为 $P_R$ 后 $Q_R$。因此完整乘积为 $T_{s\to R}=Q_RP_RMP_sQ_s$。
镜面 $M=rI$、两片 $Q$ 相同时，
$$
\begin{aligned}
T_{R\to R}&=rQP_RP_RQ=rQP_RQ,\\
T_{L\to R}&=rQP_RP_LQ=0.
\end{aligned}
$$
所以左源点被相邻的正交验偏器直接阻断。右源点虽然经过波片改变偏振，但之后最后没有第二个验偏器再次筛选，进入眼睛的非零光仍可看见。结果恢复为看见睁开的右眼。

还须确定自然光的强度，而不能把 $QP_RQ$ 当成无吸收的单位矩阵。设源自然光相干矩阵为 $J_0=I_0I/2$，由于 $Q$ 幺正，有 $QJ_0Q^\dagger=(I_0/2)I$。外侧 $P_R$ 选出强度 $I_0/2$；返回再过同轴 $P_R$ 不再损失这已被选出的分量，最后的无吸收波片也不改变强度。因此
$$
\begin{aligned}
I_{R\to R}&=|r|^2\frac{I_{R0}}2,\\
I_{L\to R}&=0.
\end{aligned}
$$

对于银幕圆偏振，反装后先到达外侧验偏器。在右镜片中，
$$
P_RC_+=\frac1{\sqrt2}\begin{pmatrix}1\\0\end{pmatrix},
\qquad
P_RC_-=\frac1{\sqrt2}\begin{pmatrix}1\\0\end{pmatrix}.
$$
两输入都先失去相同的一半强度，其原先用于区别通道的相对相位已经被筛掉。后面的 $Q$ 对两者作相同作用，不可能凭空恢复被验偏器丢弃的信息。

左镜片的投影也逐项计算，而不只依据对称性断言结果：
$$
\begin{aligned}
P_LC_+&=\frac1{\sqrt2}
\begin{pmatrix}0&0\\0&1\end{pmatrix}
\begin{pmatrix}1\\i\end{pmatrix}
=\frac{i}{\sqrt2}\begin{pmatrix}0\\1\end{pmatrix},\\
P_LC_-&=\frac1{\sqrt2}
\begin{pmatrix}0&0\\0&1\end{pmatrix}
\begin{pmatrix}1\\-i\end{pmatrix}
=-\frac{i}{\sqrt2}\begin{pmatrix}0\\1\end{pmatrix}.
\end{aligned}
$$
它们只相差共同的负号，不是两种可被后续线性器件区分的偏振方向。再经过无吸收的 $Q$，
$$
\begin{aligned}
\|QP_LC_+\|^2
&=\frac12\|Q\boldsymbol e_y\|^2=\frac12,\\
\|QP_LC_-\|^2
&=\frac12\|Q\boldsymbol e_y\|^2=\frac12.
\end{aligned}
$$
右镜片的两通道强度也都是 $1/2$，故反装系统对两种投影态的透射比例完全相同。若在某一镜片处用等强的两种输入测量分离对比度，定义
$$
\mathcal V=\frac{I_{\rm target}-I_{\rm other}}
{I_{\rm target}+I_{\rm other}},
$$
则反装后为
$$
\mathcal V=\frac{1/2-1/2}{1/2+1/2}=0,
$$
而正确理想层次对应目标透射 $1$、另一通道透射 $0$，得到 $\mathcal V=1$。这个量化检验说明问题不只是整体图像变暗：两眼收到的目标图像和串扰图像一样强，偏振分离本身已经失效。

这说明 $QP$ 与 $PQ$ 不能随意交换。第（2）问指定的“外侧波片、内侧验偏器”不仅影响镜中现象，也是圆偏振投影系统能够工作的必要层次。
