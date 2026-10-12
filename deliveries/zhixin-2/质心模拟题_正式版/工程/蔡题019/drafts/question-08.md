# 第8题

<!-- question-start -->

在三角形$ABC$的三个顶点分别坐有一人，三人到火锅内一点$O$的伸筷长度之和用$AO+BO+CO$表示。

（1）点$O$可以在三角形区域内自由选择。确定使$AO+BO+CO$最小的点的位置，可以用角度关系描述，并用物理方法说明理由。

（2）在三角形内设置一条线段支架$AD$，其中$D$位于边$BC$的内部，点$O$只能在线段$AD$上移动。求最短总长度所对应的角$\alpha=\angle BOD$、$\beta=\angle COD$需要满足的三角函数条件。

（3）设$ABC$为正三角形，且$\angle BAD=15^\circ$。用计算器求满足第（2）问要求的角度。

三角形非退化。第（1）问先讨论最优点位于内部的情形，再说明大角和边界情形；第（2）问的角度只在$O$不与$A,D$重合时定义，端点必须另外筛选。

![图8-1 自由选点、线段约束和正三角形内的偏置支架。](../figures/question-08.png){width=100%}

<!-- question-end -->

## 一、题型定位

本题是距离和的极小值问题，同时可以转化为等大绳张力的平衡问题。三条距离不是沿同一直线的三个标量；移动$O$时，它们的变化分别取决于该移动在三条连线方向上的投影。将距离和当作势能，或者直接求距离的方向导数，都会得到同一个平衡条件。

两种选点方式的差别是允许的位移不同。第（1）问允许在平面内沿任意方向移动，两个方向的一阶变化都必须为零；第（2）问只允许沿$AD$移动，因此只要求沿支架方向的一阶变化为零。支架可以承担垂直方向的力，不可把有支架的平衡也写成只有三条等大张力的平衡。

第（3）问除了列方程，还要证明求到的数值确实是线段上的最小值。必须检查角度的几何范围、两端点的一侧导数，以及中间解是否唯一。仅给出$34.1^\circ$而不说明这些筛选，不能排除错误分支或边界解。

## 二、知识点

对固定点$X$，距离$r_X=|\boldsymbol r-\boldsymbol r_X|$的梯度为$(\boldsymbol r-\boldsymbol r_X)/r_X$。梯度方向由$X$指向动点，恰与绳子对动点的拉力方向相反。这个符号必须在使用势能和受力两种方法时保持一致。

设动点沿单位方向$\boldsymbol u$位移$ds$。距离的一阶变化是两点连线在该方向上的投影，写成$dr_X/ds=(\boldsymbol r-\boldsymbol r_X)\cdot\boldsymbol u/r_X$。如果$\theta$是由动点指向$X$的方向与$\boldsymbol u$的夹角，那么$dr_X/ds=-\cos\theta$；向固定点靠近时，距离减少，这正是负号的物理含义。

三条等大、共点、在同一平面内的力平衡时，其方向两两相差$120^\circ$。这个结论来自矢量和为零，不是“有三条线便均分周角”。如果存在第四个支架反力，或者三条力大小不等，角度一般不再是$120^\circ$。

一个函数的导数为零只给出驻点。若在区间内二阶导数严格为正，导数便严格递增，区间内至多有一个驻点；再结合端点的一侧导数，可以判断该点是唯一最小值，或最小值落在端点。距离和的凸性为本题提供了这一判断依据。

正弦定理适用于每一个实际三角形：边长除以其对角的正弦相等。代入前必须先确定哪条边与哪一个角相对。第（3）问中$\angle ADB=105^\circ$、$\angle ADC=75^\circ$，这两个角在直线上互补，不能因为图画得倾斜而交换。

## 三、物理图像

图8-1的三幅题图依次区分自由区域、支架约束和正三角形条件。橙色线段是真实允许位置$AD$，蓝色三条连线表示计入距离和的$AO,BO,CO$；后两幅中的$O$必须位于$AD$上，不能沿其他蓝线移动。

可以把三条距离换成水平板上三条绳段的长度。三根轻绳在动点$O$打结，分别通过固定于$A,B,C$的光滑小孔，再在板下各悬挂质量为$m$的物体。每根绳总长固定，板上绳段越短，对应的板下绳段就越长，悬物位置越低，重力势能越小。

这个模型只用于建立势能和静力平衡的等价关系。理想无阻尼装置从任意初态释放后未必自动停在最低点，因此不能把“最后停在哪里”作为不加条件的证明。应考察稳定平衡位置；若要通过实验寻找该位置，可引入很弱的阻尼，而不改变平衡的几何条件。

图8-2的板下竖直绳段与板上斜绳段在三个小孔处相连。虚线只表示绳段被板遮住，不是板面内多加的一条绳。三个悬物质量相同，因此平衡时三个张力都等于$mg$，不要求三根绳的总长度相同。

受限模型仍有三根绳，却多了一条无摩擦支架。图8-6中的反力$\boldsymbol R$垂直$AD$，沿$AD$没有分量。于是自由点的二维矢量平衡，变成支架方向上的一维投影平衡。

## 四、解题入口

先建立重力势能与$AO+BO+CO$之间的对应，说明为什么最短总长度对应最低势能。接着对自由点列三条张力的矢量平衡，得到$120^\circ$，并补充该条件何时能在三角形内部实现。用一次$60^\circ$旋转把三段长度接成折线，还可以从三角不等式直接证明全局最小。

对受限点，不必求支架反力的大小便能先求位置。选从$A$指向$D$为正方向：向$D$移动时$AO$增加，而$BO,CO$的变化由$\cos\alpha,\cos\beta$决定。写出一阶变化为零的条件，再用几何关系补足角度方程。

最后针对正三角形建立沿$AD$的单一坐标$s=AO$，把三条距离全部写成$s$的函数。这个坐标方法既可直接数值求根，也能检验正弦定理所得两角方程，并清楚处理两端点和唯一性。

## 五、解析

（1）将最短总长度严格转化为最低重力势能。

记三条绳总长度为$L_A,L_B,L_C$，三个固定导向位置的高度相同。忽略小孔内不随$O$变化的绳长，板下悬挂长度分别为

$$
\begin{aligned}
h_A&=L_A-AO,\\
h_B&=L_B-BO,\\
h_C&=L_C-CO.
\end{aligned}
$$

取竖直向上的高度为正，三个悬物高度可写成$z_A=z_0-h_A$、$z_B=z_0-h_B$、$z_C=z_0-h_C$。图8-2展示了这一空间连接，板上每减短一段绳，板下就增加同样的长度。

![图8-2 三条距离与等质量悬物重力势能的空间对应。](../figures/weights-08.png){width=65%}

由图中的三个等质量悬物，总重力势能为

$$
\begin{aligned}
U_g
&=mg(z_A+z_B+z_C)\\
&=mg\bigl[3z_0-(h_A+h_B+h_C)\bigr]\\
&=mg\bigl[3z_0-(L_A+L_B+L_C)
 +(AO+BO+CO)\bigr]\\
&=U_0+mg(AO+BO+CO).
\end{aligned}
$$

$U_0$不随$O$改变，$mg>0$，所以两者的最小位置完全相同。这里的正号不是任意指定：距离变长时，悬物上升，势能增加；距离变短时，悬物下降，势能减少。绳长只需足够容许所研究的移动范围，固定绳长的具体数值不进入最优点条件。

（2）对自由内部点列矢量平衡，推出三角度均为$120^\circ$。

令$\boldsymbol e_A,\boldsymbol e_B,\boldsymbol e_C$分别为从$O$指向$A,B,C$的单位矢量。三个悬物静止时，每根绳的张力大小为$G=mg$。板对结点的竖直支持抵消其他竖直作用，板面内只剩三条绳的拉力，如图8-3所示。

![图8-3 自由内部点的三条等大张力及平衡夹角。](../figures/freeforces-08.png){width=50%}

平衡方程除以非零的$G$，得到

$$
\boldsymbol e_A+\boldsymbol e_B+\boldsymbol e_C=0.
$$

将前两项移到一起并取模平方：

$$
\begin{aligned}
\boldsymbol e_A+\boldsymbol e_B&=-\boldsymbol e_C,\\
|\boldsymbol e_A+\boldsymbol e_B|^2&=|\boldsymbol e_C|^2,\\
|\boldsymbol e_A|^2+|\boldsymbol e_B|^2
 +2\boldsymbol e_A\cdot\boldsymbol e_B&=1,\\
2+2\cos\angle AOB&=1,\\
\cos\angle AOB&=-\frac12,\\
\angle AOB&=120^\circ.
\end{aligned}
$$

交换$A,B,C$的地位，同样得到$\angle BOC=\angle COA=120^\circ$。因此内部最优点满足

$$
\boxed{\angle AOB=\angle BOC=\angle COA=120^\circ.}
$$

反过来，三个单位方向彼此相差$120^\circ$时，它们的矢量和为零，故该角度条件也足以保证一阶平衡。接下来仍须证明它不是极大值或鞍点，以及该内部位置是否存在。

（3）由距离的支持不等式证明内部平衡点是全局最小值。

记距离和为$F(P)=PA+PB+PC$。对任意固定顶点$X$，以及不与$X$重合的候选点$O$，把$\boldsymbol v_X=(O-X)/OX$作为由$X$指向$O$的单位矢量。任意矢量的模不小于它在单位方向上的投影，因此

$$
\begin{aligned}
PX=|P-X|
&\geq\boldsymbol v_X\cdot(P-X)\\
&=\boldsymbol v_X\cdot(O-X)
 +\boldsymbol v_X\cdot(P-O)\\
&=OX+\boldsymbol v_X\cdot(P-O).
\end{aligned}
$$

这里使用柯西不等式的投影形式，不是对距离作近似展开。对$X=A,B,C$相加：

$$
F(P)\geq F(O)
 +(\boldsymbol v_A+\boldsymbol v_B+\boldsymbol v_C)
 \cdot(P-O).
$$

由于$\boldsymbol v_X=-\boldsymbol e_X$，平衡条件使括号内的矢量为零，因而$F(P)\geq F(O)$。这对任意$P$成立，所以平衡点给出全局最小，而不只是附近最小。

等号要求对三个顶点分别满足投影等号，即$P-X$都与$O-X$同向。若$P\ne O$，这会要求三个不共线顶点同时位于同一条直线上，非退化三角形不可能满足。因此内部最优点唯一。这个结论也是距离和严格凸性的具体体现。

（4）说明$120^\circ$结论的适用范围与边界情形。

若某一顶角，例如$\angle BAC=\Theta$，达到或超过$120^\circ$，最短点在$A$，不能再要求一个内部点形成三个$120^\circ$。下面不依赖图形猜测，直接证明这一点。

设$\boldsymbol a_B=(B-A)/AB$、$\boldsymbol a_C=(C-A)/AC$，任意$P$相对于$A$的位移为$\boldsymbol d=P-A$。对$PB,PC$分别使用距离的支持不等式，得

$$
\begin{aligned}
PB&\geq AB-\boldsymbol a_B\cdot\boldsymbol d,\\
PC&\geq AC-\boldsymbol a_C\cdot\boldsymbol d,\\
F(P)&\geq AB+AC+|\boldsymbol d|
 -(\boldsymbol a_B+\boldsymbol a_C)\cdot\boldsymbol d\\
&\geq AB+AC+
 \bigl(1-|\boldsymbol a_B+\boldsymbol a_C|\bigr)|\boldsymbol d|.
\end{aligned}
$$

两个单位矢量夹角为$\Theta$，所以

$$
\begin{aligned}
|\boldsymbol a_B+\boldsymbol a_C|^2
&=2+2\cos\Theta
=4\cos^2\frac\Theta2,\\
|\boldsymbol a_B+\boldsymbol a_C|
&=2\cos\frac\Theta2.
\end{aligned}
$$

当$\Theta\geq120^\circ$，有$2\cos(\Theta/2)\leq1$，故$F(P)\geq AB+AC=F(A)$。当$\Theta>120^\circ$时，只要$P\ne A$，下界就严格大于$F(A)$；等于$120^\circ$时，仍由三个顶点不共线及前面的等号条件得到唯一最小点$A$。

若三个顶角均小于$120^\circ$，在每个顶点都能沿相邻两边单位方向的和移动，使距离和减少，因此顶点不可能最优。边的内部点也不可能最优：向三角形内部作一个垂直于该边的微小移动，到该边两个端点的距离只产生二阶增加，而到对面顶点的距离产生一阶减少。闭三角形上的连续距离和必有最小值，排除全部边界后，最小值必在内部，于是满足三个$120^\circ$。

所以第（1）问的完整结论是：最大顶角小于$120^\circ$时，唯一内部费马点满足三个$120^\circ$；最大顶角不小于$120^\circ$时，最小点是该大角顶点。如果“内部”被严格解释为不包含边界，那么后一种情况下不能取到最小值，只能通过趋近该顶点得到下确界$AB+AC$。

（5）补全$60^\circ$旋转几何法，保留其最短折线依据。

将图置于$A$在$BC$上方的方向，绕$B$顺时针旋转$60^\circ$，把$O,C$分别变成$O^*,C^*$。旋转保持长度，且$\triangle BOO^*$是正三角形，所以$OO^*=BO$，同时$O^*C^*=OC$。图8-4以正三角形示意这一连接；旋转等距关系本身对一般三角形也成立。

![图8-4 六十度旋转把三条距离连接为一条折线。](../figures/rotation-08.png){width=67%}

因此原来的距离和成为折线$A\to O\to O^*\to C^*$的长度：

$$
\begin{aligned}
AO+BO+CO
&=AO+OO^*+O^*C^*\\
&\geq AC^*.
\end{aligned}
$$

这里连续使用三角不等式。等号要求$A,O,O^*,C^*$按该次序共线，不能只说“四点在同一直线上”而不检查先后顺序。内部费马点的$120^\circ$条件恰使折线拉直：正三角形$BOO^*$在$O$处提供$60^\circ$，与$\angle AOB=120^\circ$互补；旋转后的$120^\circ$条件又使$O^*C^*$接着沿同一直线延伸。

于是内部可行时达到下界$AC^*$。大角不小于$120^\circ$时，这条直线构造不能在三角形内部给出所需次序，应改用上一段的顶点解，不能把不可行的折线等号继续当作内部答案。

（6）对受限点建立支架方向的长度变化和张力投影。

令$\boldsymbol u$沿$A\to D$，取$s=AO$，因此$O=A+s\boldsymbol u$，且$0<s<AD$。沿支架向$D$移动$ds>0$时，$AO$精确增加$ds$。另外两段的变化不是直接减去$ds$，而是连线投影给出的$-\cos\alpha\,ds$和$-\cos\beta\,ds$。故

$$
\begin{aligned}
\frac{d(AO)}{ds}&=1,\\
\frac{d(BO)}{ds}&=-\cos\alpha,\\
\frac{d(CO)}{ds}&=-\cos\beta,\\
F'(s)&=1-\cos\alpha-\cos\beta.
\end{aligned}
$$

在内部最小点，一阶导数为零，得到第（2）问所需条件

$$
\boxed{\cos\alpha+\cos\beta=1.}
$$

同一条件可从图8-6的受力投影得到。$OA$方向的张力沿$-\boldsymbol u$，贡献$-G$；$OB,OC$方向贡献$G\cos\alpha,G\cos\beta$；支架反力垂直$\boldsymbol u$，贡献为零。因而$-G+G\cos\alpha+G\cos\beta=0$。这里即使某角为钝角，也应保留其余弦的负值，而不擅自用绝对值改成正数。

（7）证明受限距离和严格凸，并筛选线段端点。

对$X=B$或$C$，记$p_X=(X-A)\cdot\boldsymbol u$，记$h_X$为$X$到直线$AD$的垂距。勾股分解给出

$$
r_X(s)=\sqrt{(s-p_X)^2+h_X^2}.
$$

逐次求导并通分，得到

$$
\begin{aligned}
r_X'(s)&=\frac{s-p_X}{r_X(s)},\\
r_X''(s)
&=\frac{r_X(s)-(s-p_X)r_X'(s)}{r_X^2(s)}\\
&=\frac{r_X^2(s)-(s-p_X)^2}{r_X^3(s)}\\
&=\frac{h_X^2}{r_X^3(s)}.
\end{aligned}
$$

$D$位于$BC$内部且三角形非退化，故$B,C$均不在$AD$直线上，$h_B,h_C>0$。$AO=s$的二阶导数为零，于是

$$
F''(s)=\frac{h_B^2}{BO^3}+\frac{h_C^2}{CO^3}>0.
$$

因此$F'(s)$严格递增。令$\phi=\angle BAD$、$\psi=\angle CAD$，从$A$端朝支架内部移动的一侧导数为

$$
F'(0^+)=1-\cos\phi-\cos\psi.
$$

到达$D$的极限中，由$D$指向$B,C$的单位方向互相相反，其在$\boldsymbol u$方向的投影和为零；$AO$项仍贡献$1$，故$F'(AD^-)=1>0$。由单调性得：若$F'(0^+)<0$，线段内部存在且只存在一个导数零点，它就是唯一最小点；若$F'(0^+)\geq0$，最小点在$A$，不能再使用未定义的$\angle BOD,\angle COD$来描述它。

这个判断还说明，在$D$位于$BC$内部的本题条件下，$D$不是最小点。若把$D$改成$B$或$C$，垂距和距离的可微性发生变化，必须重新处理该特殊情形，不能直接沿用以上严格凸证明。

（8）建立正三角形中的真实角度关系。

设正三角形边长为$a$。图8-5中$\angle BAC=60^\circ$、$\angle BAD=15^\circ$，所以$\angle DAC=45^\circ$。在$\triangle ABD$中，$\angle ABD=60^\circ$，由内角和得$\angle ADB=105^\circ$。由于$B,D,C$共线，另一侧角$\angle ADC=180^\circ-105^\circ=75^\circ$。

![图8-5 正三角形内支架方向与受限角度的几何关系。](../figures/geometry-08.png){width=62%}

现在令图中$\alpha=\angle BOD$、$\beta=\angle COD$。因为$A,O,D$依次共线，$OA$与$OD$方向相反，所以$\angle AOB=180^\circ-\alpha$、$\angle AOC=180^\circ-\beta$。在$\triangle BOD$和$\triangle COD$内分别计算剩余角：

$$
\begin{aligned}
\angle OBD&=180^\circ-105^\circ-\alpha
=75^\circ-\alpha,\\
\angle OCD&=180^\circ-75^\circ-\beta
=105^\circ-\beta.
\end{aligned}
$$

从$A$端趋近时，$\alpha\to15^\circ$、$\beta\to45^\circ$；沿线段向$D$移动，它们分别增大至$75^\circ$和$105^\circ$。因此内部可行角必须满足

$$
15^\circ<\alpha<75^\circ,\qquad
45^\circ<\beta<105^\circ.
$$

这些范围既保证有关三角形非退化，也限定了反三角函数的正确分支。

（9）逐项使用正弦定理，补足两角方程。

在$\triangle AOB$中，$OB$对角为$15^\circ$，$AB=a$对角为$180^\circ-\alpha$。利用$\sin(180^\circ-\alpha)=\sin\alpha$，得到

$$
\frac{OB}{\sin15^\circ}
=\frac{a}{\sin\alpha}
\quad\Longrightarrow\quad
OB=\frac{a\sin15^\circ}{\sin\alpha}.
$$

在$\triangle AOC$中同理，$OC$对角为$45^\circ$，$AC=a$对角为$180^\circ-\beta$，故

$$
OC=\frac{a\sin45^\circ}{\sin\beta}.
$$

再转到$\triangle BOC$：$OB$对角是$\angle BCO=105^\circ-\beta$，$OC$对角是$\angle CBO=75^\circ-\alpha$。正弦定理给出

$$
\frac{OB}{\sin(105^\circ-\beta)}
=\frac{OC}{\sin(75^\circ-\alpha)}.
$$

代入上面两条边长式并约去非零边长$a$，得

$$
\boxed{
\frac{\sin15^\circ}
{\sin\alpha\sin(105^\circ-\beta)}
=\frac{\sin45^\circ}
{\sin\beta\sin(75^\circ-\alpha)}.}
$$

这是几何相容条件；$\cos\alpha+\cos\beta=1$是最短条件。两式必须同时满足，只有后一式不能决定两个角。所有分母在可行角范围内均为正，故交叉相乘没有遗漏分母为零的内部解。求根过程中若用平方消去根号，则必须回代两条原式和角度范围，排除平方引入的伪根。

（10）用单一坐标重建方程，独立核验角度求根。

取$B=(0,0)$、$C=(a,0)$、$A=(a/2,\sqrt3a/2)$。从$A$沿$AD$的单位方向为

$$
\boldsymbol u=(-\sin15^\circ,-\cos15^\circ).
$$

它的横分量为负，说明支架向左下方倾斜；不能仅画一条任意向下的线段。点$O$的坐标由$O=A+s\boldsymbol u$给出：

$$
x_O=\frac a2-s\sin15^\circ,\qquad
y_O=\frac{\sqrt3a}{2}-s\cos15^\circ.
$$

令$D$的纵坐标为零，得到线段长度和底边分点

$$
\begin{aligned}
AD&=\frac{\sqrt3a}{2\cos15^\circ}
=0.8965754722a,\\
BD&=\frac a2-\frac{\sqrt3a}{2}\tan15^\circ\\
&=\frac a2-\frac{\sqrt3a}{2}(2-\sqrt3)\\
&=(2-\sqrt3)a.
\end{aligned}
$$

这里利用$\tan15^\circ=\tan(45^\circ-30^\circ)=2-\sqrt3$，并展开$\sqrt3(2-\sqrt3)=2\sqrt3-3$。$BD\approx0.267949a$，确在底边内部。

距离平方可以从坐标直接展开，也可从余弦定理得到。保留每条线段与$s$的夹角后，有

$$
\begin{aligned}
AO&=s,\\
BO&=\sqrt{s^2-2as\cos15^\circ+a^2},\\
CO&=\sqrt{s^2-2as\cos45^\circ+a^2},\\
F(s)&=s+\sqrt{s^2-2as\cos15^\circ+a^2}
 +\sqrt{s^2-2as\cos45^\circ+a^2}.
\end{aligned}
$$

逐项求导：根号内导数分别为$2s-2a\cos15^\circ$、$2s-2a\cos45^\circ$，再除以对应的两倍根号，得

$$
\begin{aligned}
F'(s)=1
&+\frac{s-a\cos15^\circ}
 {\sqrt{s^2-2as\cos15^\circ+a^2}}\\
&+\frac{s-a\cos45^\circ}
 {\sqrt{s^2-2as\cos45^\circ+a^2}}.
\end{aligned}
$$

这就是不借助未知角度的单变量求根式。与此同时，从矢量投影读出

$$
\cos\alpha=\frac{a\cos15^\circ-s}{BO},\qquad
\cos\beta=\frac{a\cos45^\circ-s}{CO},
$$

可见它与$1-\cos\alpha-\cos\beta=0$完全一致。式中每个分子、分母都有长度量纲，余弦和$F'(s)$无量纲；若数值求解时令$a=1$，只是选择长度单位，并未改变角度答案。

（11）先判断端点，再给出唯一内部解及数值计算。

在本题$\phi=15^\circ$、$\psi=45^\circ$，所以

$$
\begin{aligned}
F'(0^+)
&=1-\cos15^\circ-\cos45^\circ\\
&=1-\frac{\sqrt6+\sqrt2}{4}
 -\frac{\sqrt2}{2}\\
&=-0.6730326075<0.
\end{aligned}
$$

而$F'(AD^-)=1>0$。结合前面已证明的$F''(s)>0$，可知必有唯一内部零点，且该零点是整条支架上的最小值。用$a$归一化，令$q=s/a$，把上面的导数式写成只含$q$的无量纲函数。计算器逐步缩小区间得到

$$
\begin{aligned}
q=0.58&:\quad F'=-0.00744287,\\
q=0.59&:\quad F'= 0.01294831,\\
q=0.583&:\quad F'=-0.00137431,\\
q=0.584&:\quad F'= 0.00065777,\\
q=0.5836&:\quad F'=-0.00015562,\\
q=0.5837&:\quad F'= 0.00004766.
\end{aligned}
$$

每次取一负一正的两端，再在区间内求根；单调性保证不会错过另一内部解。继续迭代得到

$$
\begin{aligned}
AO&=0.5836765561a,\\
BO&=0.4616295080a,\\
CO&=0.7177987326a.
\end{aligned}
$$

用这些未过早舍入的长度回代余弦式：

$$
\begin{aligned}
\alpha
&=\arccos\frac{0.9659258263-0.5836765561}
 {0.4616295080}\\
&=34.10173000^\circ,\\
\beta
&=\arccos\frac{0.7071067812-0.5836765561}
 {0.7177987326}\\
&=80.09840092^\circ.
\end{aligned}
$$

故按一位小数回答第（3）问为

$$
\boxed{\alpha\approx34.1^\circ,\qquad\beta\approx80.1^\circ.}
$$

求解两条角度方程也得到同一结果，且两角均落在可行范围内。回代应使用未舍入的角度；将仅保留一位小数的角度代入时，出现小的残差属于舍入误差，不能要求机器显示严格等于$1$。

（12）比较最小长度、端点及自由点，检查结果的物理意义。

受限最短总长度为

$$
F_{\min}
=(0.5836765561+0.4616295080+0.7177987326)a
=1.7631047967a.
$$

两端点分别给出$F(A)=AB+AC=2a$，$F(D)=AD+BD+CD=AD+BC=1.8965754722a$。受限内部值比两端都小，与导数筛选一致。正三角形的无约束费马点是中心，三个距离各为$a/\sqrt3$，所以自由最小值为$\sqrt3a\approx1.7320508076a$。增加支架约束后最小值增大，也符合允许位置集合缩小不会降低最小值的基本判断。

本题受限点位于$(x_O,y_O)\approx(0.3489333911a,0.3022371441a)$，并不是正三角形中心。由角度可见$\angle AOB=145.89827^\circ$、$\angle AOC=99.90160^\circ$、$\angle BOC=\alpha+\beta=114.20013^\circ$，三者相加为$360^\circ$，但不相等。

<!-- KEEP_STUDENT_START -->
（13）补算支架反力，解释为何三条张力不必互成$120^\circ$。

在图8-6中选$\boldsymbol n$为垂直$\boldsymbol u$、指向右下方的单位法向量。$OB$方向位于$-\boldsymbol n$一侧，$OC$方向位于$+\boldsymbol n$一侧，所以两条张力在法向上的分量分别为$-G\sin\alpha$和$G\sin\beta$。$OA$张力没有法向分量。

![图8-6 支架约束下的切向平衡与法向反力。](../figures/restrictedforces-08.png){width=35%}

沿图中两个正交方向分别列平衡方程：

$$
\begin{aligned}
\boldsymbol u\text{方向}:&\quad
 -G+G\cos\alpha+G\cos\beta=0,\\
\boldsymbol n\text{方向}:&\quad
 -G\sin\alpha+G\sin\beta+R_n=0.
\end{aligned}
$$

第二式给出$R_n=G(\sin\alpha-\sin\beta)$，故

$$
\boldsymbol R=-G(\sin\beta-\sin\alpha)\boldsymbol n.
$$

本题$\sin\beta>\sin\alpha$，所以反力指向左上方，大小为$0.4244405304G$。图中的红色箭头方向与这个负的法向分量一致。它补偿了三根绳在法向上的不平衡，而没有改变切向最短条件；这正是受限解与自由解角度不同的原因。

<!-- KEEP_STUDENT_END -->

## 六、关键洞察

距离和的极小值并非只能用几何技巧猜点。每一条距离的梯度都是一个单位矢量，因而等权距离和天然对应等大拉力。几何角度、微分条件和最低势能其实描述同一件事：允许位移方向上的一阶变化消失。

“允许方向”比“有几条力”更根本。自由点需要二维梯度为零；直线约束只需要梯度在切向的投影为零，剩余法向由约束承担。极小值条件不能脱离允许位置集合，而$120^\circ$不是加了任何约束后仍然不变的普适答案。

旋转法还能给出内部费马点的最小长度。令$a=BC$、$b=CA$、$c=AB$，三角形面积为$\Delta$，$B$处顶角记为$\Theta_B$。在上述旋转方向中，$\angle ABC^*=\Theta_B+60^\circ$，因此余弦定理给出

$$
\begin{aligned}
F_{\min}^2=AC^{*2}
&=a^2+c^2-2ac\cos(\Theta_B+60^\circ)\\
&=a^2+c^2-ac\cos\Theta_B
 +\sqrt3ac\sin\Theta_B.
\end{aligned}
$$

由$b^2=a^2+c^2-2ac\cos\Theta_B$，可得$ac\cos\Theta_B=(a^2+c^2-b^2)/2$；由面积公式$\Delta=ac\sin\Theta_B/2$，可得$ac\sin\Theta_B=2\Delta$。依次代入并合并同类项：

$$
\begin{aligned}
F_{\min}^2
&=a^2+c^2-\frac{a^2+c^2-b^2}{2}+2\sqrt3\Delta\\
&=\frac{a^2+b^2+c^2+4\sqrt3\Delta}{2},\\
F_{\min}
&=\sqrt{\frac{a^2+b^2+c^2+4\sqrt3\Delta}{2}}.
\end{aligned}
$$

这个式子的成立前提仍是三个顶角均小于$120^\circ$。正三角形代入$\Delta=\sqrt3a^2/4$后，根号内为$3a^2$，故得到$\sqrt3a$；若大角超过阈值，则应改用邻边和，不能无条件使用面积式。

受限情形可以用局部曲率看出稳定性。在任意非顶点处，一条距离的二阶变化沿单位方向$\boldsymbol v$为

$$
\frac{1-(\widehat{OX}\cdot\boldsymbol v)^2}{OX}
=\frac{\sin^2\angle(\widehat{OX},\boldsymbol v)}{OX}\geq0.
$$

沿$AD$时，$B,C$的垂直距离非零，两项中都有严格的正贡献。这不仅说明零点唯一，也说明偏离它时距离和按二阶增加。二阶导数是$1/\text{长度}$量纲；若错误地漏掉分母的三次方，就无法通过这个量纲检查。

## 七、易错点

第一类错误是把三个$120^\circ$写成无条件结论。大角三角形的最优点位于顶点，顶点处有一条距离为零，不能直接对这条距离用普通梯度公式。应采用一侧变化或支持不等式，明确不可微点的判断办法。

第二类错误是只把支架画进图，却仍对$O$列三力平衡。沿支架投影时可以略去反力，完整矢量平衡却不能略去。若三个张力的矢量和不为零，这不说明最短点计算错了；应检查法向分量是否恰由支架反力抵消。

第三类错误是把距离变化写成$ds$而不作投影。只有$AO$与移动方向同线且同向增加，才有$d(AO)/ds=1$。$BO,CO$的变化是$-\cos\alpha$、$-\cos\beta$；使用$\sin$会相当于投影到了错误方向，符号写反则会预言靠近固定点时距离反而增长。

第四类错误是交换$105^\circ$、$75^\circ$，或者在$\triangle BOC$中把$OB$对角误写成$75^\circ-\alpha$。应先在两个含$D$的小三角形中求余角，再写每条边的对角；两个正弦定理必须在各自三角形中保持一致。

第五类错误是求到一个角方程的根便宣布完成。必须同时回代几何相容方程和最短方程，并检查两角范围、$0<s<AD$及导数符号。使用反余弦时需明确角度制；在程序中用弧度计算，再转换为度，不能把数值$15$直接当作弧度代入。

第六类错误是认为相等悬物自动意味着相等绳长，或认为无阻尼释放必定静止在最低点。前者不是势能对应所需条件，后者忽略了持续运动的可能。应区分张力相等、总绳长固定、稳定平衡和运动耗散四个不同命题。

## 八、课堂讲解建议

课堂先让学生尝试把点$O$沿一条短箭头移动，只判断三条距离分别变长还是变短，再引出投影。教师可在板书中并排写出$dr/ds=-\cos\theta$和张力投影$G\cos\theta$，使学生看到同一个几何投影为何在长度变化与拉力中呈相反符号。

展示悬物模型时，先让学生说清板上绳段变短后悬物上升还是下降，再写势能式。教师应当把“理想装置的平衡位置”与“释放后是否会停住”分开，否则学生容易把能量最低与任何运动的最终状态混同。板下绳段的遮挡虚线只用来表达空间位置，不引入额外连接。

接着教师在板书中逐行展开两个单位矢量和的模平方，推得$120^\circ$。可以询问学生：若一根绳张力变为两倍，三个角还会均分吗？这一提问为加权距离和建立联系，随后再用一个$130^\circ$顶角反例限制费马点条件的适用范围。

进入支架问题后，教师让学生先画反力，再选择沿$AD$投影。不要先告诉学生“余弦之和等于一”，而让其从$AO$增加、另外两段的投影减少写出导数。课堂可用正三角形中线的$\alpha=\beta=60^\circ$作即时检查，再转向偏置$15^\circ$支架。

数值计算环节可让学生分别使用角度联立方程和单变量距离函数，核对两种答案。教师需要保留端点导数与严格凸性两行板书，说明“计算器找到了一个根”和“证明只有这个最小值”是不同层次。课堂最后把受限最小长度与自由最小长度比较，让学生解释为什么增加约束不会带来更小的最小值。

## 九、变式训练

（1）正三角形的支架改为中线，求受限最优点和最短总长度。

设边长为$a$、高为$H=\sqrt3a/2$。取$B=(-a/2,0)$、$C=(a/2,0)$、$A=(0,H)$，令$O=(0,z)$，$0\leq z\leq H$。三条距离为$AO=H-z$、$BO=CO=\sqrt{a^2/4+z^2}$，故

$$
F(z)=H-z+2\sqrt{\frac{a^2}{4}+z^2}.
$$

求导并令其为零，逐步消元：

$$
\begin{aligned}
F'(z)&=-1+\frac{2z}{\sqrt{a^2/4+z^2}}=0,\\
2z&=\sqrt{a^2/4+z^2},\\
4z^2&=a^2/4+z^2,\\
3z^2&=a^2/4,\\
z&=\frac{a}{2\sqrt3}.
\end{aligned}
$$

平方前要求$z\geq0$，负根不在几何范围内。于是$AO=H-z=a/\sqrt3$、$BO=CO=a/\sqrt3$，最短总长度为$\sqrt3a$。由$\cos\alpha=\cos\beta=z/BO=1/2$，得到$\alpha=\beta=60^\circ$，其和满足两余弦等于$1$；由于中线经过自由费马点，增加此约束并没有改变最小值。

（2）三角形满足$AB=AC=a$、$\angle BAC=130^\circ$，求自由最短点。

在顶点$A$处，相邻两边的单位方向和的模为$2\cos65^\circ\approx0.8452365<1$。对任意位移$\boldsymbol d=P-A$，支持不等式给出

$$
F(P)\geq2a+
 \bigl(1-2\cos65^\circ\bigr)|\boldsymbol d|.
$$

括号为$0.1547635>0$，所以$P\ne A$时严格有$F(P)>2a$。故唯一最优点是$A$，最小长度为$2a$。若要求严格内部，则没有能取到这个值的点，但任意靠近$A$的内部点可使距离和趋近$2a$；这就是最小值与下确界的区别。

（3）在正三角形中将总长度成本改为$2AO+BO+CO$，求最优点，并解释$120^\circ$为何失效。

权重$2$意味着与$A$连接的绳张力改为$2mg$，另外两条仍为$mg$。在$A$处，$B,C$方向单位矢量和的模是$2\cos30^\circ=\sqrt3$。对任意$P$，支持不等式给出

$$
\begin{aligned}
2PA+PB+PC
&\geq2a+2|\boldsymbol d|
 -(\boldsymbol a_B+\boldsymbol a_C)\cdot\boldsymbol d\\
&\geq2a+(2-\sqrt3)|\boldsymbol d|.
\end{aligned}
$$

由于$2-\sqrt3>0$，唯一最优点为$A$，最小成本为$2a$。一般权重$w_A,w_B,w_C>0$时，只要$w_A\geq|w_B\boldsymbol a_B+w_C\boldsymbol a_C|$，顶点$A$就满足相应的全局下界条件。此时等权力的$120^\circ$结论不能使用，原因是平衡多边形的边长已不相等，不是几何图形画得不对。

<!-- KEEP_TOGETHER_START -->
（4）正三角形中点$O$只能在线段$AB$上，求最短总长度。

此时$AO+BO=AB=a$为常数，问题只剩使$CO$最小。设$x=BO$，$0\leq x\leq a$，$C$在$AB$上的垂足为中点，垂距为$\sqrt3a/2$，所以

$$
\begin{aligned}
CO&=\sqrt{(x-a/2)^2+3a^2/4},\\
F(x)&=a+\sqrt{(x-a/2)^2+3a^2/4},\\
F'(x)&=\frac{x-a/2}{\sqrt{(x-a/2)^2+3a^2/4}}.
\end{aligned}
$$

导数在$x<a/2$时为负、$x>a/2$时为正，故最优点是$AB$中点，最短总长度为$(1+\sqrt3/2)a$。这一情形相当于$D=B$，不能直接套用“$D$在$BC$内部”的端点导数结论；重新利用$AO+BO$恒定，反而得到更简单而完整的解法。
<!-- KEEP_TOGETHER_END -->

<!-- question-complete -->
