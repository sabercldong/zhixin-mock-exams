# 第6题

<!-- question-start -->

工业中常用高温废水预热低温水。将装置理想化为图6-1所示的同轴逆流换热管：低温水的入口温度为 $T_L$，在内管中从左向右流动；高温水的入口温度为 $T_H$，在外管的环形通道中从右向左流动，且 $T_H>T_L$。管道总长为 $l$。管道足够细，在同一轴向位置，每股水流在其横截面内的温度可视为均匀。

冷、热两股水流的质量流率相同，均为

$$
\alpha=\frac{\Delta m}{\Delta t},
$$

水的比热容为

$$
c=\frac{\Delta Q}{\Delta m\,\Delta T}.
$$

内、外两股水流之间的管壁半径为 $r$，厚度为 $h\ll r$，热导率为 $\kappa$。薄壁导热满足

$$
\Delta Q=\frac{\kappa\,\Delta T}{h}\,\Delta A\,\Delta t,
$$

其中 $\Delta T$ 是壁两侧水流的局部温差，$\Delta A$ 是相应的换热面积。

（1）求内管水温随轴向坐标 $x$ 的分布。

（2）求单位时间内换热过程引起的两股水流总熵变化。

![图6-1 同轴管内冷水与环形通道内热水的逆向流动。](../figures/question-06.png){width=90%}

<!-- question-end -->

## 一、题型定位

本题是稳态逆流换热与不可逆传热的熵分析。需要先对同一小段中的两股水流分别列能量平衡，建立局部温度的联立微分方程，再利用位于不同管端的两个入口条件确定积分常量。

两股水流质量流率及比热相同，是温差沿管长保持不变的关键；“恒定温差”不是由管壁薄自动得到的。管壁薄只决定题设导热系数的形式。第（2）问同时涉及熵随水流的输运和换热产生的熵，必须区分流体熵变化与稳态装置中的熵积累。

## 二、知识点

质量流率与热容流率；薄圆柱壁的换热面积；稳态控制体能量守恒；逆流的入口与出口辨认；统一空间坐标下的温度梯度；联立一阶微分方程及异端边界条件；恒温差与线性温度分布；定比热流体的对数熵变化；局部熵产生与整体熵流平衡；量纲、温差正值及弱、强换热极限。

采用题设的理想热交换模型：水的比热容 $c$ 和热导率 $\kappa$ 不随温度变化；只有两股水流之间的径向换热，不计向环境散热、壁的稳态储热和轴向导热，也不额外加入压降、黏性耗散或机械功引起的熵变化。这些约定限定本题公式的适用范围，不是对实际换热设备所有效应的描述。所有熵公式中的温度必须是绝对温度。

## 三、物理图像

冷水沿 $+x$ 方向流动，越向右越热。热水沿 $-x$ 方向流动，越向左越冷；但若把它的温度也画在同一个向右增加的 $x$ 坐标上，曲线同样向右上升。沿水流方向的降温与沿共同坐标方向的正梯度不是一回事。

每一小段中，热水放出的热量等于冷水吸收的热量。两股水流的热容流率相等，因此同一段内两条温度曲线的增量相同，曲线保持平行。在任何一个位置，热水仍比冷水热；然而两股水流的出口位于相反管端，比较两处出口温度不能代替比较同一位置的温度。

有限温差传热使冷水获得的熵大于热水失去的熵。装置在稳态下并不持续积累这份熵，而是由出流水将产生的熵带走。

## 四、解题入口

从冷水入口取 $x=0$，向右为正方向，右端为 $x=l$。入口温度 $T_L,T_H$ 是给定常数；局部冷、热水温度分别写作 $T_c(x),T_h(x)$，避免把热水入口温度误当作全管恒温。

先定义热容流率和单位管长的导热系数：

$$
C=\alpha c,\qquad
G=\frac{2\pi r\kappa}{h}.
$$

$C$ 的单位为 $\mathrm{W\,K^{-1}}$，$G$ 的单位为 $\mathrm{W\,m^{-1}\,K^{-1}}$。对小段列式后，先相减求 $T_h-T_c$，再用 $T_c(0)=T_L$ 与 $T_h(l)=T_H$；不能把两个入口条件都放在 $x=0$。

## 五、解析

**第1步：明确研究对象、局部温度和两个入口条件。**

图6-1外侧环形流道与内管只通过中间薄壁交换热量，两股水不混合。取任意固定的小段 $[x,x+dx]$ 为研究对象；小段内两股水分别是两个稳态控制体。

冷水从左侧面进入、右侧面流出；热水从右侧面进入、左侧面流出。因此边界条件是

$$
\boxed{T_c(0)=T_L,\qquad T_h(l)=T_H.}
$$

未知的是右端冷水出口 $T_c(l)$ 和左端热水出口 $T_h(0)$。质量流率 $\alpha$ 是每秒通过截面的质量，而不是管中已有水的总质量。后面每个能量方程使用的是单位时间内流入、流出的焓差，不是整段水温随时间的变化。

**第2步：从真实换热面积得到小段的热流率。**

半径为 $r$ 的圆柱壁，在轴向长度 $dx$ 内的面积为周长乘长度：

$$
dA=2\pi r\,dx.
$$

按薄壁模型，壁两侧温差就是同一位置的 $T_h(x)-T_c(x)$。记从热水传给冷水的小段热流率为 $d\dot Q$；点表示“每单位时间”，$d$ 表示“这一小段所占的部分”。由题给导热关系，

$$
\begin{aligned}
d\dot Q
&=\frac{\kappa}{h}[T_h(x)-T_c(x)]\,dA\\
&=\frac{2\pi r\kappa}{h}[T_h(x)-T_c(x)]\,dx\\
&=\boxed{G[T_h(x)-T_c(x)]\,dx}.
\end{aligned}
$$

这里没有再乘水流速度。流速只通过质量流率影响水流携带热量的能力，不能重复计入壁的导热式。有限厚度圆柱壁的精确热阻不同；本题先严格使用已给的薄壁定律。

**第3步：对冷水列出流入、吸热、流出三项。**

图6-2把同一小段中的冷、热水分开显示。先辨认每个箭头是进入还是离开该控制体，再确定能量方程中的符号。

![图6-2 同一空间小段中两股水流的进出方向及径向传热。](../figures/slice-06.png){width=76%}

冷水在时间 $dt$ 内通过的质量为 $\alpha\,dt$。定比热情况下，从 $T_c(x)$ 到 $T_c(x+dx)$ 所需的热量为

$$
\alpha c\,dt\,[T_c(x+dx)-T_c(x)].
$$

吸收的热量为 $d\dot Q\,dt$。稳态没有该段能量积累，故

$$
\begin{aligned}
C\,T_c(x)+d\dot Q&=C\,T_c(x+dx),\\
C[T_c(x+dx)-T_c(x)]&=G[T_h(x)-T_c(x)]\,dx.
\end{aligned}
$$

固定比热时焓基准可以取在任意温度，因为流入和流出的同一基准项抵消；不需要把 $cT$ 理解为从绝对零度积分得到的真实总焓。将温度差除以 $dx$ 并取极限，得到

$$
\boxed{C\,\frac{dT_c}{dx}=G(T_h-T_c).}
$$

这是空间微分方程，不是 $C\,dT_c/dt$。稳态只说明每个固定位置的温度不随时间变化，不说明沿管长处处等温。

**第4步：对热水列式，核对反向流动的符号。**

图6-2中的热水从右侧 $x+dx$ 进入，从左侧 $x$ 离开。热水失去热量 $d\dot Q\,dt$，所以

$$
\begin{aligned}
C\,T_h(x+dx)&=C\,T_h(x)+d\dot Q,\\
C[T_h(x+dx)-T_h(x)]&=G[T_h(x)-T_c(x)]\,dx,\\
C\,\frac{dT_h}{dx}&=G(T_h-T_c).
\end{aligned}
$$

两个导数都为正，这与热水沿自己的流向降温完全一致。若改为沿热水流向的坐标 $s=l-x$，则

$$
\frac{dT_h}{ds}
=\frac{dT_h}{dx}\frac{dx}{ds}
=-\frac{dT_h}{dx}<0.
$$

必须在共同 $x$ 坐标下解联立方程，不能一条方程用向右的 $x$，另一条暗中换成向左的 $s$。

**第5步：相减方程，证明局部温差恒定。**

将第3、4步相减，因为两股水的热容流率都是同一个 $C$，

$$
\begin{aligned}
\frac{dT_h}{dx}-\frac{dT_c}{dx}
&=\frac GC(T_h-T_c)-\frac GC(T_h-T_c)=0,\\
\frac{d}{dx}(T_h-T_c)&=0.
\end{aligned}
$$

因此可以记

$$
T_h(x)-T_c(x)=\delta,
$$

其中 $\delta$ 是待由边界条件确定的常数。它不是两入口温差 $T_H-T_L$，也不是冷水通过全管的升温量。

此时任一温度的导数为 $G\delta/C$，所以曲线是直线。若两流率或比热不同，两个导数不再相同，这个结论便不能直接沿用。

**第6步：逐项积分，再用异端边界求出常数。**

由冷水方程，从 $0$ 积分到任意 $x$：

$$
\begin{aligned}
\int_{T_L}^{T_c(x)}dT
&=\frac{G\delta}{C}\int_0^x d\xi,\\
T_c(x)&=T_L+\frac{G\delta}{C}x.
\end{aligned}
$$

热水温度比它高 $\delta$，因此

$$
T_h(x)=T_L+\delta+\frac{G\delta}{C}x.
$$

将热水入口条件代入 $x=l$，得到

$$
\begin{aligned}
T_H&=T_L+\delta+\frac{G\delta l}{C},\\
T_H-T_L&=\delta\left(1+\frac{Gl}{C}\right),\\
\delta&=\frac{T_H-T_L}{1+Gl/C}
=\frac{\alpha c h(T_H-T_L)}{\alpha c h+2\pi r\kappa l}.
\end{aligned}
$$

分母中 $1$ 不能遗漏。它来自右端两股水仍相差 $\delta$，不是积分中凭空加上的修正常量。因 $G,C,l>0$、$T_H>T_L$，所以 $\delta>0$，每处热流始终从热水指向冷水。

**第7步：给出温度分布，统一长度与无量纲参数。**

定义换热长度和无量纲换热强度

$$
\ell_0=\frac CG=\frac{\alpha c h}{2\pi r\kappa},
\qquad N=\frac l{\ell_0}=\frac{Gl}{C},
\qquad D=T_H-T_L.
$$

$\ell_0$ 表示导热与水流携热相竞争的长度尺度，不是管子的原长。代入上一步，内管冷水分布为

$$
\boxed{\begin{aligned}
T_c(x)&=T_L+D\,\frac{x/\ell_0}{1+l/\ell_0}\\
&=T_L+\frac{2\pi r\kappa(T_H-T_L)}
{\alpha c h+2\pi r\kappa l}\,x,
\quad 0\le x\le l.
\end{aligned}}
$$

同时，为后续熵计算保留热水分布：

$$
\begin{aligned}
T_h(x)
&=T_c(x)+\frac{D}{1+N}\\
&=T_H-D\,\frac{N}{1+N}\left(1-\frac xl\right).
\end{aligned}
$$

后一式在 $x=l$ 自动给出 $T_H$；前一式在 $x=0$ 自动给出 $T_L$。图6-3用同一坐标展示两条平行曲线、两个入口和两个出口；右端的竖直间距为 $\delta$，与左端相同。

![图6-3 共同空间坐标下的平行温度曲线及异端入口条件。](../figures/temperature-06.png){width=68%}

图中每一竖直连线都连接同一个 $x$ 的两股水，故温差为正。后面计算局部熵产生时，使用的正是这样的局部温差，而不是跨管两端的出口温差。

**第8步：求两个出口与总热流率，作能量回代。**

令

$$
\varepsilon=\frac{N}{1+N},\qquad 0<\varepsilon<1.
$$

它表示冷水实际升温占两入口温差的比例。由温度分布，

$$
\begin{aligned}
T_{c,\mathrm{out}}=T_c(l)&=T_L+\varepsilon D=T_H-\delta,\\
T_{h,\mathrm{out}}=T_h(0)&=T_H-\varepsilon D=T_L+\delta.
\end{aligned}
$$

两股出口温度之和为 $T_L+T_H$。每秒冷水获得的热量与热水失去的热量分别为

$$
\begin{aligned}
\dot Q_c&=C[T_c(l)-T_L]=C\varepsilon D,\\
\dot Q_h&=C[T_H-T_h(0)]=C\varepsilon D.
\end{aligned}
$$

从壁面沿管长积分也给出

$$
\dot Q=\int_0^l G\delta\,dx
=Gl\delta
=\frac{GlD}{1+Gl/C}
=C\varepsilon D.
$$

三种计算一致。特别地，$N>1$ 时 $\varepsilon>1/2$，冷水出口可以高于热水出口，但这两个出口分别在右端和左端；每一处仍有 $T_h(x)-T_c(x)=\delta>0$，没有热从冷处自发流向热处。

**第9步：辨认“熵变化”在稳态开放系统中的含义。**

以 $S_{\mathrm{cv}}$ 表示固定管段这一控制体内物质的熵。若研究的是固定管段中的全部物质，稳态时其熵不随时间积累，即

$$
\frac{dS_{\mathrm{cv}}}{dt}=0.
$$

这不表示换热没有熵产生。水不断流入、流出，必须把熵流也计入。无外界传热的理想装置满足

$$
0=\dot S_{\mathrm{in}}-\dot S_{\mathrm{out}}
+\dot S_{\mathrm{gen}},
$$

所以

$$
\boxed{\dot S_{\mathrm{gen}}
=\dot S_{\mathrm{out}}-\dot S_{\mathrm{in}}.}
$$

本题第（2）问所求的是通过装置的两股水流总熵变化率，即上述出、入熵流之差；它等于有限温差换热的熵产生率。不能把这个正值与固定稳态控制体的零积累量混为一谈。

<!-- KEEP_TOGETHER_START -->

**第10步：写出局部水流熵变化并判断正负。**

图6-4以一小段的热交换为对象。该段每秒把 $d\dot Q$ 从局部热水 $T_h$ 传给局部冷水 $T_c$。在本题定比热、无额外机械耗散模型中，水流温度变化的熵可由平衡态关系 $ds=c\,dT/T$ 计算。

<!-- KEEP_TOGETHER_END -->

![图6-4 有限温差传热中两股水流的熵损失、熵获得与熵产生。](../figures/entropy-06.png){width=70%}

将冷水吸热和热水放热分别计入，

$$
\begin{aligned}
d\dot S_c&=\frac{d\dot Q}{T_c},\\
d\dot S_h&=-\frac{d\dot Q}{T_h},\\
d\dot S_{\mathrm{gen}}
&=d\dot Q\left(\frac1{T_c}-\frac1{T_h}\right)\\
&=G(T_h-T_c)
\left(\frac1{T_c}-\frac1{T_h}\right)dx\\
&=\boxed{\frac{G\delta^2}{T_cT_h}\,dx>0.}
\end{aligned}
$$

$dQ/T$ 不是把整个非等温流体当成一个恒温热库；这里在每个微小空间段分别采用其局部温度，然后再积分。由于 $T_h>T_c>0$，热水少失去一些熵，冷水多获得一些熵，两者不抵消。

**第11步：逐项计算熵积分，明确温差因子的消去。**

总熵产生率为

$$
\dot S_{\mathrm{gen}}
=G\delta\int_0^l
\left[\frac1{T_c(x)}-\frac1{T_h(x)}\right]dx.
$$

记两条温度曲线的斜率为

$$
b=\frac{G\delta}{C},
\quad T_c(x)=T_L+bx,
\quad T_h(x)=T_L+\delta+bx.
$$

这里 $b>0$。分别积分两个倒数，数学技巧是线性换元 $u=a+bx$：

$$
\begin{aligned}
\int_0^l\frac{dx}{T_L+bx}
&=\frac1b\left[\ln(T_L+bx)\right]_0^l
=\frac1b\ln\frac{T_c(l)}{T_L},\\
\int_0^l\frac{dx}{T_L+\delta+bx}
&=\frac1b\ln\frac{T_h(l)}{T_h(0)}
=\frac1b\ln\frac{T_H}{T_h(0)}.
\end{aligned}
$$

再代回整体系数，不省略关键约分：

$$
\begin{aligned}
\dot S_{\mathrm{gen}}
&=\frac{G\delta}{b}
\left[\ln\frac{T_c(l)}{T_L}
-\ln\frac{T_H}{T_h(0)}\right],\\
\frac{G\delta}{b}
&=\frac{G\delta}{G\delta/C}=C,\\
\dot S_{\mathrm{gen}}
&=C\left[
\ln\frac{T_H-\delta}{T_L}
-\ln\frac{T_H}{T_L+\delta}
\right].
\end{aligned}
$$

最终对数前的系数只有 $C=\alpha c$，没有额外乘上 $\delta$。若保留额外温差，既没有正确完成换元约分，也会使单位由熵流率变成热功率。

当 $D=0$ 或 $G=0$ 时，上面为积分方便而引入的 $b$ 为零，不能直接除以 $b$；此时原始热流和熵产生均为零，可直接处理或取连续极限。

**第12步：由出、入水流的熵变化独立核对。**

定比热水在温度从 $T_a$ 变为 $T_b$ 时，比熵变化为

$$
s_b-s_a=\int_{T_a}^{T_b}\frac cT\,dT
=c\ln\frac{T_b}{T_a}.
$$

每秒有质量 $\alpha$ 通过，所以冷水、热水的熵流变化分别为

$$
\begin{aligned}
\dot S_c&=\alpha c\ln\frac{T_c(l)}{T_L}>0,\\
\dot S_h&=\alpha c\ln\frac{T_h(0)}{T_H}<0.
\end{aligned}
$$

二者相加，

$$
\begin{aligned}
\dot S_c+\dot S_h
&=C\ln\frac{T_c(l)T_h(0)}{T_LT_H}\\
&=\boxed{
\alpha c\ln\frac{(T_H-\delta)(T_L+\delta)}{T_LT_H}},
\end{aligned}
$$

与局部积分完全一致。这条方法不需要先求熵产生的空间分布，却仍需第（1）问提供两个正确的出口温度。

为了不只凭直觉判断正号，利用 $T_c(l)=T_L+\varepsilon D$、$T_h(0)=T_H-\varepsilon D$ 展开乘积：

$$
\begin{aligned}
&(T_L+\varepsilon D)(T_H-\varepsilon D)\\
&\quad=T_LT_H+\varepsilon D(T_H-T_L)-\varepsilon^2D^2\\
&\quad=T_LT_H+\varepsilon(1-\varepsilon)D^2.
\end{aligned}
$$

故还可写成

$$
\boxed{
\dot S_{\mathrm{gen}}
=C\ln\left[
1+\frac{N}{(1+N)^2}
\frac{(T_H-T_L)^2}{T_LT_H}
\right]\ge0.
}
$$

所有对数的真数均为无量纲正数，且在有限正换热强度、非零入口温差下严格大于 $1$。出口在不同位置“温度交换”并不使熵产生为负。

**第13步：检查弱换热、强换热和无温差极限。**

当 $N\to0$ 时，$\delta\to D$、$\varepsilon\to0$，两股水几乎保持各自入口温度，熵产生趋零。若这个极限由 $G\to0$ 或 $l\to0$ 实现，热流率也趋零。

当固定 $G,l$ 而 $C\to\infty$ 时，虽然 $N\to0$、每股水的温升降趋零，但

$$
\dot Q=\frac{GlD}{1+Gl/C}\longrightarrow GlD,
$$

不必趋零。几乎不变的水温不等于小质量流率下的微小传热量，必须说明参数怎样趋于极限。

<!-- KEEP_TOGETHER_START -->

当固定 $C$ 而 $Gl\to\infty$ 时，$N\to\infty$，

$$
\begin{aligned}
\delta&\to0,\\
T_c(l)&\to T_H,\qquad T_h(0)\to T_L,\\
\dot Q&\to CD,\qquad \dot S_{\mathrm{gen}}\to0.
\end{aligned}
$$

这是无限换热能力的理想极限：相等热容的两股逆流水流几乎交换入口温度，每处温差趋小，可以在有有限总热交换的同时使熵产生趋零。有限正 $N$ 时不能提前把 $\delta$ 设为零。

若强换热比例来自 $C\to0$，则 $\dot Q\le CD\to0$，不是仍有同一有限热功率。最后，当 $T_H=T_L$ 时，两条温度曲线都恒定，热流与熵产生均为零。

**第14步：核对量纲与摄氏温度的使用范围。**

由定义，

$$
\begin{aligned}
[C]&=\mathrm{kg\,s^{-1}}\,
\mathrm{J\,kg^{-1}\,K^{-1}}
=\mathrm{W\,K^{-1}},\\
[G]&=\frac{\mathrm{m}\,
\mathrm{W\,m^{-1}\,K^{-1}}}{\mathrm{m}}
=\mathrm{W\,m^{-1}\,K^{-1}},\\
[\ell_0]&=[C/G]=\mathrm m,\qquad [N]=1,\\
[\dot Q]&=[GlD]=\mathrm W,\\
[\dot S_{\mathrm{gen}}]&=[C]
=\mathrm{J\,K^{-1}\,s^{-1}}.
\end{aligned}
$$

温差和线性温度分布可以用摄氏数值进行温升计算，但熵的对数必须先转成开尔文。不能将 $\ln(T_b/T_a)$ 中的 $T_a,T_b$ 直接换成摄氏温度，因为比例而非温差依赖温标零点。

本题的 $\Delta A$ 是壁面面积，$\Delta S$ 或 $\dot S$ 是熵，二者不能因字母相似而混用。

<!-- KEEP_TOGETHER_END -->

## 六、关键洞察

本题两个温度梯度同号的原因，是两股水的进出面反向，而不是热水也沿 $+x$ 运动。质量流率和比热相等，又使两个正梯度相等，最终给出恒定局部温差。这个推理顺序是“方向确定符号—热容确定系数—相减确定温差”，不能倒过来先猜平行直线。

若将两股热容流率分别记作 $C_c,C_h$，相同小段的能量平衡变为

$$
T_c'=\frac G{C_c}(T_h-T_c),\qquad
T_h'=\frac G{C_h}(T_h-T_c).
$$

相减后令 $\Delta(x)=T_h(x)-T_c(x)$，则

$$
\Delta'=a\Delta,\qquad
a=G\left(\frac1{C_h}-\frac1{C_c}\right).
$$

用分离变量法，

$$
\frac{d\Delta}{\Delta}=a\,dx,\qquad
\Delta(x)=\Delta_0e^{ax}.
$$

再对冷水积分。为了避免 $C_c=C_h$ 时形式上除以零，定义连续函数

$$
E(x)=
\begin{cases}
\dfrac{e^{ax}-1}{a},&a\ne0,\\[4pt]
x,&a=0.
\end{cases}
$$

由于 $E'(x)=e^{ax}$，

$$
\begin{aligned}
T_c(x)&=T_L+\frac{G\Delta_0}{C_c}E(x),\\
T_h(x)&=T_c(x)+\Delta_0e^{ax}.
\end{aligned}
$$

从热水右端入口求出

$$
\begin{aligned}
T_H-T_L
&=\Delta_0\left[e^{al}+\frac G{C_c}E(l)\right],\\
\Delta_0
&=\frac{T_H-T_L}{e^{al}+(G/C_c)E(l)}.
\end{aligned}
$$

分母为正，因为指数为正，而且 $E(l)=\int_0^l e^{ax}dx>0$，不管 $a$ 为何符号。$a\to0$ 时 $E(l)\to l$，正好连续回到本题的 $\delta=D/(1+Gl/C)$。这给出了本题等热容特例的独立结构解释，不宜在不等流率问题中强行使用平行线。

不等热容情况下，总热流率和熵产生仍分别满足

$$
\begin{aligned}
\dot Q&=C_c[T_c(l)-T_L]
=C_h[T_H-T_h(0)]
=G\Delta_0E(l),\\
\dot S_{\mathrm{gen}}
&=C_c\ln\frac{T_c(l)}{T_L}
+C_h\ln\frac{T_h(0)}{T_H}.
\end{aligned}
$$

第二条不能再合并为同一个 $C$ 乘一个温度乘积对数。局部熵积分仍为

$$
\dot S_{\mathrm{gen}}
=G\int_0^l\frac{\Delta(x)^2}{T_c(x)T_h(x)}\,dx\ge0,
$$

因此在适用热模型下，不等热容并不改变局部传热的非负熵产生。

薄壁定律的来源也可通过精确圆柱导热检验。图6-5表示内半径为 $r$、外半径为 $r+h$ 的导热壁及径向坐标 $s$；厚度为辨认结构而放大显示。取单位轴向长度，稳态向内导热的正热流率记作 $q'$，有

![图6-5 圆柱导热壁的径向坐标、内外半径与向内热流。](../figures/wall-06.png){width=54%}

$$
q'=2\pi s\kappa\,\frac{dT}{ds}.
$$

温度由内壁的 $T_c$ 向外壁的 $T_h$ 增加，导数为正，而实际热流向内。径向傅里叶定律的负号已由“向内为正”的热流约定处理，不可再多加一次负号。分离变量、逐项积分：

$$
\begin{aligned}
dT&=\frac{q'}{2\pi\kappa}\frac{ds}{s},\\
T_h-T_c
&=\frac{q'}{2\pi\kappa}\int_r^{r+h}\frac{ds}{s}\\
&=\frac{q'}{2\pi\kappa}\ln\frac{r+h}{r},\\
G_{\mathrm{exact}}
&=\frac{q'}{T_h-T_c}
=\frac{2\pi\kappa}{\ln(1+h/r)}.
\end{aligned}
$$

令 $u=h/r\ll1$，使用 $\ln(1+u)=u-u^2/2+u^3/3+\cdots$，得到

$$
\frac{G_{\mathrm{exact}}}{G}
=\frac{u}{\ln(1+u)}
=1+\frac u2-\frac{u^2}{12}+O(u^3).
$$

所以题设 $G=2\pi r\kappa/h$ 是取内壁半径时的薄壁主阶近似。主解析不能一边使用这个给定模型，一边把高阶修正只加在某个公式中；若采用精确热阻，应在全部温度、出口与熵公式中一致替换 $G$。

## 七、易错点

热水从右向左流动，容易误写 $dT_h/dx<0$；应先标注小段的流入面在 $x+dx$、流出面在 $x$。其沿流向的导数为负，但沿共同向右坐标的导数为正。

把 $T_H$ 同时当作入口温度和每处热水温度，会把真实的两有限热容水流改成一个恒温热库；这样得到指数而不是本题的线性分布。记号 $T_h(x)$ 与 $T_H$ 必须区分。

把壁面面积错写成 $\pi r^2$ 会将换热侧面积换成管口面积。图6-1的轴向长度配圆周 $2\pi r$，所以小段面积是 $2\pi r\,dx$。

直接用 $T_c(0)=T_L,T_h(0)=T_H$ 是将逆流的两入口放在同一端。若如此列边界，求出的并非本题装置。

认为热水一定比“冷水出口”热，容易否定逆流中可能出现的出口温度顺序交换；需要比较图6-3同一个 $x$ 的两点，而非两端各取一个点。

熵积分中的斜率 $b=G\delta/C$ 必须完整带入，$G\delta/b=C$；多留下一个 $\delta$ 会破坏量纲。所有对数均需绝对温度，不用摄氏比值。

稳态的零熵积累不等于零熵产生。有限温差产生的熵由出流水带走；无耗散的温差极限才可能使熵产生趋零。

把 $N\to\infty$ 一概解释为热流趋同一非零值，也忽略了参数路径。固定 $C$ 增加面积与降低 $C$ 是两种不同过程，后者的最大热功率本身趋零。

## 八、课堂讲解建议

课堂先只展示图6-1，请学生分别指出冷、热入口及两个出口，再在图6-2把四个穿过控制面的箭头辨认完整。教师板书先保留“流入加获得等于流出”，然后才整理为微分方程，让学生通过进出方向决定热水方程的正号。

在两条方程写完后，让学生尝试相减；只有看到两个热容流率相等，才宣布温差恒定。随后教师将两个入口条件分别放在图6-3的左下和右上，帮助学生理解异端边界而不是同一端的初值问题。

讲解熵时，先用图6-4比较同一份热量除以两个不同绝对温度所得的熵，再完成空间积分。教师特别展示 $G\delta/(G\delta/C)$ 的约分，避免学生只记住最后对数式而遗漏换元系数。

课堂可设置 $N=2$ 的出口比较，让学生在图6-3分别找出冷水出口和热水出口；教师同时保留任一竖直截线，说明出口顺序交换并不违背局部第二定律。

最后用局部积分与出入熵流两条路线交叉检验，并让学生解释“稳态管内熵不变，但通过它的水流熵增加”。变式中的流率不等和最大熵产生问题可用于检验模型适用条件，不将几何薄壁与等热容两种条件混为一谈。

## 九、变式训练

<!-- KEEP_TOGETHER_START -->

**变式1：按给定参数计算温度、热功率与熵产生。**

取

$$
\begin{aligned}
T_L&=293.15\,\mathrm K,\quad T_H=353.15\,\mathrm K,\\
\alpha&=0.100\,\mathrm{kg\,s^{-1}},\quad
c=4200\,\mathrm{J\,kg^{-1}\,K^{-1}},\\
r&=0.0100\,\mathrm m,\quad h=5.00\times10^{-4}\,\mathrm m,\\
\kappa&=0.600\,\mathrm{W\,m^{-1}\,K^{-1}},\quad l=5.00\,\mathrm m.
\end{aligned}
$$

求两条温度分布、两个出口温度、热功率及熵产生率。

<!-- KEEP_TOGETHER_END -->

先求组合系数，不将所有常量直接堆进最后对数：

$$
\begin{aligned}
C&=0.100\times4200=420\,\mathrm{W\,K^{-1}},\\
G&=\frac{2\pi(0.0100)(0.600)}{5.00\times10^{-4}}
\approx75.3982\,\mathrm{W\,m^{-1}\,K^{-1}},\\
\ell_0&=\frac{420}{75.3982}\approx5.57042\,\mathrm m,\\
N&=\frac5{5.57042}\approx0.897598.
\end{aligned}
$$

入口温差为 $60.00\,\mathrm K$，所以

$$
\delta=\frac{60.00}{1+0.897598}
\approx31.6189\,\mathrm K,
\qquad
b=\frac{G\delta}{C}\approx5.67622\,\mathrm{K\,m^{-1}}.
$$

因此温度分布及出口为

$$
\begin{aligned}
T_c(x)&=(293.15\,\mathrm K)
+(5.67622\,\mathrm{K\,m^{-1}})x,\\
T_h(x)&=(324.76892\,\mathrm K)
+(5.67622\,\mathrm{K\,m^{-1}})x,\\
T_{c,\mathrm{out}}&\approx321.53108\,\mathrm K,\\
T_{h,\mathrm{out}}&\approx324.76892\,\mathrm K.
\end{aligned}
$$

回代 $T_h(5\,\mathrm m)=353.15\,\mathrm K$，且两出口升、降温量均为 $28.38108\,\mathrm K$。热功率为

$$
\dot Q=420(321.53108-293.15)
\approx1.19201\times10^4\,\mathrm W.
$$

熵产生分别由两水流温度比例计算：

$$
\begin{aligned}
\dot S_{\mathrm{gen}}
&=420\left[
\ln\frac{321.53108}{293.15}
+\ln\frac{324.76892}{353.15}\right]\\
&\approx\boxed{3.62494\,\mathrm{W\,K^{-1}}}.
\end{aligned}
$$

第一个对数为正，第二个为负，和仍为正；这里熵不是热功率除以任意“平均温度”。

**变式2：为达到指定预热比例，反求所需管长。**

保持变式1除 $l$ 外的参数不变，要求冷水升温至少达到两入口温差的 $90\%$。求最小管长，并辨认有限厚度导热修正的方向。

令目标比例为 $\varepsilon_*=0.90$。因 $\varepsilon=N/(1+N)$ 随 $N$ 单调增加，最小长度满足等号：

$$
\begin{aligned}
\frac N{1+N}&=\varepsilon_*,\\
N&=\varepsilon_*+\varepsilon_*N,\\
N(1-\varepsilon_*)&=\varepsilon_*,\\
N_*&=\frac{\varepsilon_*}{1-\varepsilon_*}=9.
\end{aligned}
$$

所以

$$
\boxed{l_{\min}=9\ell_0
=9(5.57042\,\mathrm m)
\approx50.1338\,\mathrm m.}
$$

此时冷水出口为 $293.15+0.9(60)=347.15\,\mathrm K$，热水出口为 $353.15-54=299.15\,\mathrm K$。两出口相隔管道两端，每处局部温差仍是 $60/10=6\,\mathrm K$，不能因出口先后颠倒而删去此设计解。

若一致采用精确圆柱导热，$h/r=0.05$，

$$
G_{\mathrm{exact}}
=\frac{2\pi(0.600)}{\ln(1.05)}
\approx77.2679\,\mathrm{W\,m^{-1}\,K^{-1}}>G.
$$

导热能力略大，故所需长度略小：

$$
l_{\min,\mathrm{exact}}
=9\frac{C}{G_{\mathrm{exact}}}
\approx48.9207\,\mathrm m.
$$

这只是超出题设薄壁主阶模型的完整替代计算，不能只换分母而仍保留旧的 $N$ 或出口公式。完全达到 $100\%$ 要求 $N\to\infty$，在本理想模型中没有有限正管长解。

**变式3：两股水的热容流率不相等。**

取 $T_L=290\,\mathrm K$、$T_H=350\,\mathrm K$，$C_c=200\,\mathrm{W\,K^{-1}}$、$C_h=400\,\mathrm{W\,K^{-1}}$，$G=20.0\,\mathrm{W\,m^{-1}\,K^{-1}}$，$l=10.0\,\mathrm m$。求两条温度曲线、出口、热流率和熵产生。

采用第六模块已逐项求出的不等热容方程：

$$
\begin{aligned}
a&=20\left(\frac1{400}-\frac1{200}\right)
=-0.0500\,\mathrm{m^{-1}},\\
e^{al}&=e^{-0.5}\approx0.60653066,\\
E(l)&=\frac{e^{-0.5}-1}{-0.05}
\approx7.8693868\,\mathrm m.
\end{aligned}
$$

初始局部温差不是 $60\,\mathrm K$，而是

$$
\begin{aligned}
\Delta_0
&=\frac{60}{0.60653066+(20/200)(7.8693868)}\,\mathrm K\\
&\approx43.0580\,\mathrm K.
\end{aligned}
$$

对任意 $x$，取 $x$ 以米计，则

$$
\begin{aligned}
E(x)&=\frac{\exp[-(0.0500\,\mathrm{m^{-1}})x]-1}
{-0.0500\,\mathrm{m^{-1}}},\\
T_c(x)&=290\,\mathrm K
+(4.30580\,\mathrm{K\,m^{-1}})E(x),\\
T_h(x)&=T_c(x)+(43.0580\,\mathrm K)
\exp[-(0.0500\,\mathrm{m^{-1}})x].
\end{aligned}
$$

指数中的 $ax$ 是无量纲乘积，$E(x)$ 具有长度单位。两出口及热流率为

$$
\begin{aligned}
T_c(l)&\approx323.8840\,\mathrm K,\\
T_h(0)&\approx333.0580\,\mathrm K,\\
\dot Q&=200(323.8840-290)
\approx6776.80\,\mathrm W.
\end{aligned}
$$

热水放热计算独立给出 $400(350-333.0580)\approx6776.80\,\mathrm W$。两水温改变量不相同，因为各自热容流率不同；不能检查“升温量等于降温量”，应检查热功率相等。

熵产生为

$$
\begin{aligned}
\dot S_{\mathrm{gen}}
&=200\ln\frac{323.8840}{290}
+400\ln\frac{333.0580}{350}\\
&\approx\boxed{2.25430\,\mathrm{W\,K^{-1}}}.
\end{aligned}
$$

温差从 $43.0580\,\mathrm K$ 减小到约 $26.1160\,\mathrm K$，两曲线并不平行，仍始终满足局部热水温度较高。

<!-- KEEP_TOGETHER_START -->

**变式4：熵产生是否随管长一直增大？**

固定 $C,G,T_L,T_H$，只改变 $l$。求最大熵产生率对应的管长，并解释长管极限。

利用主解析已完成的温度乘积展开，

$$
\dot S_{\mathrm{gen}}(N)
=C\ln\left[1+
\frac{D^2}{T_LT_H}\frac{N}{(1+N)^2}\right].
$$

$C>0$ 且对数单调增加，所以只需最大化 $f(N)=N/(1+N)^2$，不能最大化热流率来代替这个问题。商法则给出

$$
\begin{aligned}
f'(N)
&=\frac{(1+N)^2-2N(1+N)}{(1+N)^4}\\
&=\frac{1-N}{(1+N)^3}.
\end{aligned}
$$

在 $0<N<1$ 上导数为正，在 $N>1$ 上为负。因此唯一最大值发生在

$$
\boxed{N=1,\qquad l=\ell_0=\frac CG.}
$$

此时 $\varepsilon=1/2$，两出口均为 $(T_L+T_H)/2$，但仍位于不同管端，局部温差为 $D/2$。最大熵产生为

$$
\boxed{
\dot S_{\max}
=C\ln\frac{(T_L+T_H)^2}{4T_LT_H}.
}
$$

例如 $C=200\,\mathrm{W\,K^{-1}}$、$T_L=280\,\mathrm K$、$T_H=360\,\mathrm K$、$G=30\,\mathrm{W\,m^{-1}\,K^{-1}}$ 时，

$$
\begin{aligned}
l_*&=\frac{200}{30}\,\mathrm m\approx6.66667\,\mathrm m,\\
T_{c,\mathrm{out}}=T_{h,\mathrm{out}}&=320\,\mathrm K,\\
\dot S_{\max}
&=200\ln\frac{320^2}{280\times360}
\approx3.14967\,\mathrm{W\,K^{-1}}.
\end{aligned}
$$

增加管长时，参与换热的壁面积增大，却使每处驱动温差减小；有限温差不可逆性不是单由总热量决定。$N\to\infty$ 时两股等热容逆流水流接近互换入口温度，热流趋 $CD$，熵产生却趋零。因而“更多热交换必然产生更多熵”不成立。

<!-- KEEP_TOGETHER_END -->

<!-- question-complete -->
