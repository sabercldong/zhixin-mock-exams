# 第 6 题

<!-- question-start -->
单原子理想气体满足状态方程 $PV=n\mathcal RT$，其摩尔定容热容为 $C_{V,\mathrm m}=3\mathcal R/2$。其中 $\mathcal R=N_Ak_B$ 为摩尔气体常量。

（1）证明热平衡时，每个原子的平均平动动能为 $\overline E=3k_BT/2$。

（2）考虑 $^{20}\mathrm{Ne}$ 原子束通过周期 $d=0.5\,\mathrm{nm}$ 的光栅。按题设的衍射尺度条件 $d=\lambda$，用第（1）问对应的热运动特征动量估算温度 $T$。说明所采用的特征动量及该估算与完整光栅衍射条件的区别。

![图 6-1　单原子气体及原子束通过周期光栅的情景。](../figures/question-06.png)
<!-- question-end -->

## 一、题型定位

从宏观理想气体定律连接到微观平均动能，再将热运动与de Broglie波长联系。核心是“平均动能”与“代表动量”的对应，不是把每个原子的速度视为相同。

## 二、知识点

弹性碰撞传递动量；气体压强的微观来源；各向同性平均；Avogadro常量；定容热容与内能；能量零点；均方根速度；de Broglie关系；光栅相邻缝的程差；单位换算与有效数字。

气体采用经典、非相互作用的单原子模型，只计三维平动。真实束流若有定向漂移、非热平衡选速或不同能量分布，温度与束流动量还需额外信息。第二问采用由平均平动能定义的均方根动量，给出明确的条件估算。

## 三、物理图像

压强来自原子不断撞击容器壁所传递的动量。某一面墙只响应垂直于它的速度分量；平衡气体三个方向统计等价，使压强表达式中的 $1/3$ 自然出现。

原子通过光栅时表现为波，动量越小，波长越长。对氖这样远重于电子的原子，$0.5\,\mathrm{nm}$ 的波长意味着低的热运动速度和温度。温度给定仍存在速度分布，不对应严格单色物质波。

## 四、解题入口

用一次碰撞的动量变化和连续两次撞同一面墙的时间求单原子平均力；叠加 $N$ 个原子，与状态方程比较。再由 $\overline E=p_{\mathrm{rms}}^2/(2m)$ 选定特征动量，用 $\lambda=h/p_{\mathrm{rms}}$ 消去动量，以SI单位计算温度。

## 五、解析

（1）单个原子碰壁传递的动量。

取边长 $L$ 的立方体容器，$V=L^3$。原子质量为 $m$，速度分量为 $(v_x,v_y,v_z)$。与垂直 $x$ 方向的刚性壁作弹性碰撞时，切向分量不变，法向分量由 $v_x$ 变为 $-v_x$。

原子向右撞墙时，自身动量变化为 $-2mv_x$，传给墙的动量为 $+2mv_x$。任一面墙收到的法向动量大小均为 $2m|v_x|$。两次撞同一面墙要经过从右到左再返回的路程，因此
$$\Delta t=\frac{2L}{|v_x|}.$$
该原子给这面墙的时间平均力为
$$\overline F_x=\frac{2m|v_x|}{2L/|v_x|}=\frac{mv_x^2}{L}.$$
$v_x=0$ 的原子不撞这面墙，贡献为零，与平方形式连续一致。图 6-2 中的 $2L$ 是重复撞同一面墙的往返距离，不能只取两壁间距 $L$。

![图 6-2　原子碰壁动量交换及热平衡速度分量。](../figures/kinetic-06.png)

（2）由大量原子的平均力得到压强。

设总原子数为 $N$，墙面积为 $L^2$。时间及粒子平均后，
$$\begin{aligned}
F_x&=\sum_{i=1}^N\frac{mv_{x,i}^2}{L}
=\frac{Nm}{L}\langle v_x^2\rangle,\\
P&=\frac{F_x}{L^2}=\frac{Nm}{V}\langle v_x^2\rangle.
\end{aligned}$$
平衡且无宏观定向流动时，各方向的速度统计相同：
$$\langle v_x^2\rangle=\langle v_y^2\rangle=\langle v_z^2\rangle.$$
由 $v^2=v_x^2+v_y^2+v_z^2$，有
$$\langle v^2\rangle=3\langle v_x^2\rangle.$$
代回得到
$$\boxed{PV=\frac13Nm\langle v^2\rangle=\frac23N\overline E},\qquad
\overline E=\frac12m\langle v^2\rangle.$$
平均的是速度平方，而不是先平均速度再平方。平衡气体 $\langle\boldsymbol v\rangle=0$，但平均动能与压强并不为零。

（3）与宏观状态方程比较。

总原子数与物质的量的关系是 $N=nN_A$，又 $\mathcal R=N_Ak_B$，所以
$$PV=n\mathcal RT=nN_Ak_BT=Nk_BT.$$
与微观表达式比较，约去正的 $N$：
$$\frac23\overline E=k_BT,\qquad \boxed{\overline E=\frac32k_BT.}$$
因子 $3$ 来自三个平动方向。单原子模型没有需要加入的分子转动、振动自由度。

（4）用定容热容交叉说明内能。

摩尔定容热容定义为
$$C_{V,\mathrm m}=\frac1n\left(\frac{\partial U}{\partial T}\right)_V.$$
题设给出 $dU=(3/2)n\mathcal R\,dT$。从 $T_1$ 积分到 $T_2$，
$$U(T_2)-U(T_1)=\frac32n\mathcal R(T_2-T_1).$$
一般形式为
$$U(T)=\frac32n\mathcal RT+U_{\mathrm{ref}}.$$
热容只确定能量差，不确定积分常数。以静止原子的平动能为零，且只计平动内能，才取 $U_{\mathrm{tr}}=3n\mathcal RT/2$。除以 $N=nN_A$，再次得到平均平动能。

这一路线需要说明内能组成和零点，不能省略积分常数后声称绝对内能由热容本身确定。若将原子基态内部能量也计入，总内能会另有与温度无关的一项，而热运动的平均动能结论不变。

（5）定义热运动特征动量。

均方根速度及动量定义为
$$v_{\mathrm{rms}}=\sqrt{\langle v^2\rangle},\qquad
p_{\mathrm{rms}}=\sqrt{\langle p^2\rangle}=mv_{\mathrm{rms}}.$$
所以
$$\frac{p_{\mathrm{rms}}^2}{2m}=\frac32k_BT,\qquad
\boxed{p_{\mathrm{rms}}=\sqrt{3mk_BT}}.$$
对应 $v_{\mathrm{rms}}=\sqrt{3k_BT/m}$。这没有断言每个原子动量都相同，而是用代表值匹配平均动能。

（6）物质波关系与温度。

de Broglie关系为 $\lambda=h/p$。按题设取特征波长 $h/p_{\mathrm{rms}}=d$：
$$d=\frac h{\sqrt{3mk_BT}}.$$
两边平方并逐步移项，
$$\begin{aligned}
d^2&=\frac{h^2}{3mk_BT},\\
3mk_BT d^2&=h^2,\\
T&=\boxed{\frac{h^2}{3mk_Bd^2}}.
\end{aligned}$$
温度与质量成反比，与周期平方成反比。若采用另一种速度平均，需相应改变这一系数，不能只改名称而保留同一推导。

（7）逐项代入SI数值。

按质量数近似 $m=20u$，采用
$$\begin{aligned}
u&=1.66053906892\times10^{-27}\,\mathrm{kg},\\
m&=3.32107813784\times10^{-26}\,\mathrm{kg},\\
d&=0.5\times10^{-9}\,\mathrm m=5.0\times10^{-10}\,\mathrm m,\\
h&=6.62607015\times10^{-34}\,\mathrm{J\,s},\\
k_B&=1.380649\times10^{-23}\,\mathrm{J\,K^{-1}}.
\end{aligned}$$
先平方：
$$h^2=4.39048056327\times10^{-67}\,\mathrm{J^2s^2},\qquad
d^2=2.5\times10^{-19}\,\mathrm{m^2}.$$
再计算分母：
$$3mk_Bd^2=3(3.32107813784)(1.380649)(2.5)\times10^{-68}
\simeq3.438932\times10^{-67}.$$
约去公共指数后，
$$\boxed{T\simeq1.2767\,\mathrm K\approx1.28\,\mathrm K.}$$
中间位数用于核验，按给定周期有效数字也可报告约 $1.3\,\mathrm K$。精确同位素质量不是严格 $20u$，采用精确质量只产生小的相对修正，不改变数量级。

（8）以速度和动能反算。

先由波长求动量：
$$p=h/d=1.32521403\times10^{-24}\,\mathrm{kg\,m\,s^{-1}}.$$
除以质量得到
$$v=p/m\simeq39.9031\,\mathrm{m\,s^{-1}}.$$
计算动能，
$$\overline E=p^2/(2m)\simeq2.64401\times10^{-23}\,\mathrm J.$$
再以 $T=2\overline E/(3k_B)$ 回算，得到相同的 $1.2767\,\mathrm K$。这一核验可检查动量、速度、能量间是否漏掉质量或系数。

（9）与完整光栅条件的区别。

图 6-3 中入射束垂直光栅，相邻缝距 $d$。向与入射法线夹角 $\beta$ 的方向传播，相邻路径差为 $d\sin\beta$，相长干涉条件为
$$d\sin\beta=j\lambda,\qquad j\in\mathbb Z.$$
该条件涉及出射角和级次。题设 $d=\lambda$ 只指定尺度；若取一级 $j=1$，则 $\sin\beta=1$，为 $\beta=90^\circ$ 的掠射极限，不是所有衍射必须具有这一个波长。

![图 6-3　相邻光栅缝的程差与出射角。](../figures/diffraction-06.png)

故 $1.28\,\mathrm K$ 是题设尺度与均方根动量约定下的条件估算，不能由“看见任意衍射”唯一确定。若给定角度及级次，先由 $\lambda=d\sin\beta/j$ 求波长，再求温度。

（10）量纲及不同平均的辨析。

$[h]=\mathrm{kg\,m^2s^{-1}}$，$[k_B]=\mathrm{kg\,m^2s^{-2}K^{-1}}$，因此 $[h^2/(mk_Bd^2)]=\mathrm K$。同波长下重原子动量相同，动能更小，温度更低；周期减半使动量增倍、温度变四倍，与公式一致。

经典Maxwell分布的三种速率不同：
$$v_{\mathrm{mp}}=\sqrt{\frac{2k_BT}{m}},\quad
\overline v=\sqrt{\frac{8k_BT}{\pi m}},\quad
v_{\mathrm{rms}}=\sqrt{\frac{3k_BT}{m}}.$$
若改用最概然动量匹配波长，分母系数为 $2$ 而非 $3$。另外，$\langle h/p\rangle$ 不等于 $h/\sqrt{\langle p^2\rangle}$，所以本解的“特征波长”也不称为平均波长。真实定向束流还须扣除宏观漂移动能，才可讨论热温度。

## 六、关键洞察

宏观压强含有微观速度的二阶矩。平均速度零与零压强是完全不同的判断。热容路线说明能量的温度变化率，碰壁路线说明平动能与压强的联系，两条路线并非把同一个结论重复代入自身。

还可从速度分布独立检验。令 $\alpha=m/(2k_BT)$，速率分布正比于 $v^2e^{-\alpha v^2}$，则
$$\langle v^2\rangle=
\frac{\int_0^\infty v^4e^{-\alpha v^2}dv}
{\int_0^\infty v^2e^{-\alpha v^2}dv}.$$
利用 $d(e^{-\alpha v^2})=-2\alpha v e^{-\alpha v^2}dv$，分部积分：
$$\begin{aligned}
\int_0^\infty v^4e^{-\alpha v^2}dv
&=-\frac1{2\alpha}\int_0^\infty v^3\,d(e^{-\alpha v^2})\\
&=\frac3{2\alpha}\int_0^\infty v^2e^{-\alpha v^2}dv.
\end{aligned}$$
边界项 $v^3e^{-\alpha v^2}$ 在两端为零，所以 $\langle v^2\rangle=3/(2\alpha)=3k_BT/m$。这条路线用分布积分检查平均能量，可与独立数值积分比较。

## 七、易错点

同墙碰撞周期取 $2L/|v_x|$，一次反射动量变化取 $2m|v_x|$，漏掉任一个 $2$ 都会出错。$n$ 是物质的量，$N$ 是原子数，$\mathcal R$ 与 $k_B$ 不能混写。

$0.5\,\mathrm{nm}$ 若写成 $0.5\times10^{-6}\,\mathrm m$，温度会相差一百万倍。把电子质量用于氖原子也会改变数量级。

习惯称“分子束”不使单原子氖增加转动自由度；平均动量矢量、平均动量大小和均方根动量各不相同。未声明代表值就给温度，会掩盖模型限定。

## 八、课堂讲解建议

先让学生画一个原子反复碰墙的路径，分别指出两倍动量变化和两倍往返路程的来源。板书从一面墙推广为三维统计平均时保留三分之一的推导，不只引用结论。

数值代入将纳米、原子质量单位和指数分别核对。最后让学生在使用物质波关系前声明所取速度平均，并用两条相邻路径解释 $d=\lambda$ 的一级角度，区分尺度估算与真实测温。

## 九、变式训练

变式一：同样 $\lambda=d=0.5\,\mathrm{nm}$，质量改为 $40u$。

解：动量 $h/d$ 不变，质量加倍使动能减半，故 $T_{40u}=T_{20u}/2\simeq0.63835\,\mathrm K$。速度减半，为约 $19.9516\,\mathrm{m\,s^{-1}}$。

变式二：仍用氖原子与原周期，在 $\beta=30^\circ$ 看到一级相长干涉，按均方根动量估算温度。

解：$\lambda=d\sin30^\circ=d/2$，故动量增倍，动能和温度为原来的四倍：
$$T=4(1.2766987)\,\mathrm K\simeq5.10679\,\mathrm K.$$
速度为约 $79.8063\,\mathrm{m\,s^{-1}}$。这里角度改变后不能继续将波长固定为 $d$。

（3）若原子速度服从三维麦克斯韦分布，求德布罗意波长$\lambda\ge d$的比例，并在主问温度处估计。

解：条件对应$p\le h/d$。速度分布积分得
$$P(\lambda\ge d)=\operatorname{erf}x-\frac{2x}{\sqrt\pi}e^{-x^2},\qquad
x=\frac{h}{d\sqrt{2mk_BT}}.$$
主问按均方根动量取$\lambda=d$，即$T=h^2/(3mk_Bd^2)$，所以$x=\sqrt{3/2}$，比例约$60.8\%$。均方根标度并不表示全部原子波长相同；实际定向束的动量筛选须另给条件。

（4）筛选后的定向原子束取$\lambda_0=d/2$，相对动量标准差为$1\%$。估计一级衍射角和角宽。

解：$d\sin\beta=\lambda$给$\beta_0=\pi/6$。由于$\delta\lambda/\lambda=-\delta p/p$，
$$\sigma_\beta\simeq\tan\beta_0\frac{\sigma_p}{p}
=\frac{0.01}{\sqrt3}\ {\rm rad}\simeq5.77\times10^{-3}\ {\rm rad}.$$
该角宽只计窄动量分布的一阶贡献，未计束发散、有限光栅宽度及探测分辨率。它描述已筛选的定向束，不能直接用于各向同性热气体。
