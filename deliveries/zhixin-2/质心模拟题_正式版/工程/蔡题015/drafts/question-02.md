# 第2题


<!-- question-complete -->
<!-- question-start -->

计算下列电流分布产生的磁场。

（1）一个正二十面体的棱长为 $l$，各条棱由电阻相同的导线构成。从相邻的两个顶点分别流入、流出电流 $I$，求中心处的磁场大小。

（2）一根半无限长直导线连接到与它垂直的无限大导电平面上。电流 $I$ 沿导线从无穷远流入，进入平面后向各个方向均匀流向无穷远。以导线为 $z$ 轴，以注入点为原点，求空间中的磁场。

（3）一个半径为 $r$ 的绝缘球，表面均匀涂有电阻率为常数的薄层。以球心为原点，一根导线沿 $z$ 轴将电流 $I$ 从无穷远注入球面；另一根导线位于 $x$—$z$ 平面内，与 $z$ 轴的夹角为 $\theta_0$，将电流从球面引出到无穷远。求球面上
$$
(r\sin\theta\cos\phi,\ r\sin\theta\sin\phi,\ r\cos\theta)
$$
处单位长度所通过的电流大小。先考虑 $\phi=0$ 的情形。

（4）求第（3）问电流分布在任意空间点产生的磁场大小。

<!-- question-end -->

## 一、题型定位

本题把离散电阻网络、平面面电流和球面面电流放在同一个“电流守恒—线性叠加—磁场对称性”的框架内。困难不是写出安培环路定律，而是找到确实具有足够对称性的电流分布。

第（1）问的两电极相邻，不是球心相对的两个顶点；这一实际通电网络并没有绕某一个电极的五重旋转对称性。不能直接把某个顶点的总电流平均分给五条棱。应先把它分解为两个各自对称的辅助网络，再叠加磁场。

第（3）、（4）问的两电极一般不在一条直径的两端，真实面电流也不是轴对称分布。先构造“一个点注入、整个球面均匀流出”的辅助问题，是把球面几何转化为可计算环路的关键。均匀流出是计算中的辅助分布，不是实际球面额外开了许多接线孔。

以下按理想细导线、理想面电流和非磁性介质的模型处理。第（1）问求三十条棱构成的骨架磁场；若外接引线沿顶点与球心的径向布置，它们在中心的贡献也为零。未规定走向的其他外接引线，不属于已经确定的骨架电流分布。

球面两条引线按通过球心方向的径向半无限直引线处理。为统一坐标，取注入点在正 $z$ 轴上，引出点在负 $x$ 半平面。本题只规定第二条引线与 $z$ 轴的夹角，选择 $x$ 轴的这一方向只是明确观察方位。若改取引出点在正 $x$ 半平面，相应的有向角差和方位角也必须一同改变，不能只换一个正负号。

## 二、知识点

稳恒电流的节点守恒、线性电阻网络的叠加、旋转与镜面对称性、毕奥—萨伐尔定律、安培环路定律、薄层面电流、球冠面积、球坐标单位矢量、半角恒等式，以及面电流两侧磁场的切向跃变。

用 $\boldsymbol K$ 表示面电流密度。这里“面”表示电流集中在很薄的层内，不是说 $\boldsymbol K$ 的单位为 $\mathrm{A/m^2}$。若一条曲线位于薄层内，曲线的面内单位法向为 $\boldsymbol m$，则穿过长度元 $\mathrm ds$ 的电流为
$$
\mathrm dI=\boldsymbol K\cdot\boldsymbol m\,\mathrm ds,
\qquad [K]=\mathrm{A/m}.
$$
只有当这条长度元与局部电流方向垂直时，才有 $\mathrm dI=K\,\mathrm ds$。球面上的一条纬圈，其长度为 $2\pi r\sin\theta$，而不是 $2\pi r$。

如果薄层的厚度为 $t$、体电阻率为 $\varrho_{\mathrm e}$，则面电导为
$$
\Sigma=\frac{t}{\varrho_{\mathrm e}},
\qquad
\boldsymbol K=-\Sigma\nabla_{\!s}V.
$$
$\nabla_{\!s}$ 是沿球面的梯度，$\Sigma$ 的单位为西门子。题目固定总电流 $I$，所以均匀改变整个薄层的面电导只会改变电势差，不改变归一化的电流路线。

对真空或非磁性介质中的稳恒电流，
$$
\begin{aligned}
\oint_C\boldsymbol B\cdot\mathrm d\boldsymbol\ell
&=\mu_0 I_{\rm enc},\\
\boldsymbol B(\boldsymbol X)
&=\frac{\mu_0}{4\pi}\int
\frac{\boldsymbol J(\boldsymbol X')\times(\boldsymbol X-\boldsymbol X')}
{|\boldsymbol X-\boldsymbol X'|^3}\,\mathrm d^3X'.
\end{aligned}
$$
第一式必须同时确定环路方向、穿过面的电流正方向以及磁场是否在环路上恒定。第二式可对细导线或薄层改写为线积分或面积分，用来独立核验叠加结果。

## 三、物理图像

图2-1中的 $A$、$B$ 是一条棱的两个端点，电流从 $A$ 进入、从 $B$ 离开。中心为 $O$。空间骨架的前后棱须分开辨认；纸面上两条投影线交叉不代表那里有电学节点。

![图2-1 相邻顶点通电的正二十面体骨架。](../figures/network-02.png){width=65%}

图2-2给出球面两电极和测点的空间关系。定义球心指向注入点、引出点的单位矢量分别为
$$
\boldsymbol a=(0,0,1),\qquad
\boldsymbol b=(-\sin\theta_0,0,\cos\theta_0).
$$
把球面测点写成 $P=r\boldsymbol n$，其中
$$
\boldsymbol n=(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta).
$$
两电极间的球心角满足 $\boldsymbol a\cdot\boldsymbol b=\cos\theta_0$。

![图2-2 球面两径向引线、测点与角度的空间关系。](../figures/sphere-02.png){width=63%}

$\theta$ 是测点从正 $z$ 轴量起的极角，不是电极间的夹角。对 $\phi=0$，测点在正 $x$ 半平面，引出点在负 $x$ 半平面，两个径向的有向角差为 $\theta+\theta_0$。这个加号来自实际位置关系，不能脱离图形把它改成 $\theta-\theta_0$。

球面上的实际电流是从 $A$ 向 $B$ 汇聚的切向流。求电流密度时，应在面内比较方向；求磁场时，还要把两根外部直引线的贡献包括在内。薄层单独产生的磁场，一般不等于完整电流系统的磁场。

## 四、解题入口

先处理叠加能恢复对称性的部分。对离散骨架，将每个电极分成一个点电流与平均分配到十二个顶点的补偿电流。两个辅助网络各有五重旋转和镜面对称性，因此中心磁场可以逐个判定。

对平面问题，先用电流守恒求 $\boldsymbol K$，再在平面两侧分别选择同心圆环路。注入导线只在一侧出现，所以两侧的环路穿过电流不同。这种单侧磁场不是把导电平面当成磁屏蔽板。

对球面问题，先算一个注入点与均匀球面流出的辅助系统。球冠内的总流出量必须从注入电流中扣除；扣除后剩下的电流才穿过纬圈。然后将一个以 $A$ 为轴的辅助系统与另一个以 $B$ 为轴的辅助系统相减，均匀的补偿电流消失。

最后把磁场分成球内、球外及薄层两侧极限。理想面电流处切向磁场不连续，不能给“恰在薄层几何面上”指定一个与两侧都相同的磁场值。

## 五、解析

**第1步：明确计算对象、坐标和正方向。**

第（1）问中令外部注入、流出的总电流为 $I>0$。每条棱电阻相同，记为 $R_{\mathrm e}$。顶点 $i$ 的净注入电流记为 $q_i$，流入网络为正，流出网络为负。若顶点电势为 $U_i$，从顶点 $i$ 指向相邻顶点 $j$ 的电流为
$$
I_{ij}=\frac{U_i-U_j}{R_{\mathrm e}},
\qquad
\sum_{j\sim i}I_{ij}=q_i.
$$
$U_i$ 可同时增加同一个常量，所有电势差与电流都不改变。后面利用的唯一性是节点电流确定后的各棱电流唯一，不是每个绝对电势唯一。

第（2）问把导电平面取为 $z=0$，导线在 $z>0$，电流沿 $-\boldsymbol e_z$ 流向原点。用 $\rho=\sqrt{x^2+y^2}$ 表示到 $z$ 轴的距离；$\boldsymbol e_\phi$ 指向绕正 $z$ 轴的逆时针方向。第（3）、（4）问的球半径仍记为 $r$，空间场点到球心的距离另记为 $R$，避免用同一个字母混淆球面半径与场点位置。

**第2步：把相邻顶点通电分成两个辅助网络。**

设 $N=12$。第一个辅助网络取
$$
q_i^{(A)}=I\left(\delta_{iA}-\frac1{12}\right),
$$
即 $A$ 净注入 $11I/12$，其余十一个顶点各流出 $I/12$。第二个辅助网络取
$$
q_i^{(B)}=-I\left(\delta_{iB}-\frac1{12}\right),
$$
即 $B$ 净流出 $11I/12$，其余十一个顶点各注入 $I/12$。这里 $\delta_{iA}$ 在 $i=A$ 时等于 $1$，在其他顶点等于 $0$。

图2-3只画第一个辅助网络。平均补偿分配于所有顶点，使其在绕 $OA$ 的五重旋转和通过 $OA$ 的镜面反射下均不改变。图中的空间镜面用于配对两侧导线，不是增加一个导电面。

![图2-3 单顶点辅助注入与正二十面体的对称结构。](../figures/symmetry-02.png){width=63%}

逐点相加检验：
$$
\begin{aligned}
i=A:\quad q_A^{(A)}+q_A^{(B)}
&=\frac{11I}{12}+\frac I{12}=I,\\
i=B:\quad q_B^{(A)}+q_B^{(B)}
&=-\frac I{12}-\frac{11I}{12}=-I,\\
i\ne A,B:\quad q_i^{(A)}+q_i^{(B)}
&=-\frac I{12}+\frac I{12}=0.
\end{aligned}
$$
所以两个辅助网络叠加后，与题目的实际各点注入完全相同。

将两组节点电势相加，对每条棱有
$$
\begin{aligned}
I_{ij}^{(A)}+I_{ij}^{(B)}
&=\frac{U_i^{(A)}-U_j^{(A)}}{R_{\mathrm e}}
+\frac{U_i^{(B)}-U_j^{(B)}}{R_{\mathrm e}}\\
&=\frac{(U_i^{(A)}+U_i^{(B)})-(U_j^{(A)}+U_j^{(B)})}{R_{\mathrm e}}.
\end{aligned}
$$
相加后的电流满足实际节点守恒方程，因此就是实际网络电流。这一步使用线性方程的叠加，不是假设真实通电状态仍然五路均分。

**第3步：分别证明两个辅助网络的中心磁场为零。**

先研究以 $A$ 为特殊顶点的第一个辅助网络。绕 $OA$ 旋转 $72^\circ$ 后，导线位置、电阻和所有节点注入都与原来相同。中心 $O$ 不动，所以 $\boldsymbol B_A(O)$ 也必须在此旋转后不变。

任何垂直于 $OA$ 的非零矢量转过 $72^\circ$ 都会改变方向。因此中心磁场只能平行 $OA$。暂写
$$
\boldsymbol B_A(O)=B_{\parallel}\boldsymbol e_A.
$$
这只排除了横向分量，尚未证明 $B_{\parallel}=0$。

再取图2-3中的一个含有 $OA$ 的镜面。镜面两侧的对应导线，其电流方向互为镜像。以镜面为 $x$—$z$ 平面、以 $OA$ 为 $z$ 轴，则镜像变换为
$$
(x,y,z)\longmapsto(x,-y,z).
$$
毕奥—萨伐尔定律中的磁场含两个极矢量的叉积。镜像后，其变换为
$$
(B_x,B_y,B_z)\longmapsto(-B_x,B_y,-B_z).
$$
因此配对导线对 $B_z$ 的贡献大小相等、符号相反；位于镜面上的导线，其贡献本身没有 $z$ 分量。故 $B_{\parallel}=0$，于是
$$
\boldsymbol B_A(O)=\boldsymbol0.
$$
对以 $B$ 为特殊顶点的第二个辅助网络，完全同样的论证给出 $\boldsymbol B_B(O)=\boldsymbol0$。磁场随电流线性叠加，所以
$$
\boxed{\boldsymbol B(O)=\boldsymbol0,\qquad B(O)=0.}
$$
结果不依赖 $l$ 与 $R_{\mathrm e}$ 的数值。若外接引线径向布置，对中心而言 $\mathrm d\boldsymbol\ell$ 与指向中心的矢量平行，叉积为零，因此不改变这个结果。

**第4步：由平面电流守恒求出面电流密度。**

在 $z=0$ 平面内，以原点为圆心取半径 $\rho$ 的圆周。稳恒条件下，全部注入电流 $I$ 都必须穿过这条圆周向外流动。各方向均匀，故 $K_\rho$ 在圆周上相同，并与圆周垂直。

图2-4同时画出平面内的径向电流，以及上、下两个不同高度的圆形磁场环路。上环路的跨越面被注入直导线穿过，下环路的跨越面不被任何实际电流穿过。

![图2-4 径向平面面电流及两侧的安培环路。](../figures/plane-02.png){width=72%}

电流守恒为
$$
\begin{aligned}
I&=\int_0^{2\pi}K_\rho(\rho)\,\rho\,\mathrm d\phi
=2\pi\rho K_\rho(\rho),\\
\therefore\quad
\boldsymbol K(\rho)&=\frac{I}{2\pi\rho}\boldsymbol e_\rho.
\end{aligned}
$$
$K_\rho$ 随距离按 $1/\rho$ 减小。这并不表示电流在远处变少，而是相同总电流分摊到更长的圆周上。

**第5步：先确定平面问题磁场的方向，再用环路定律。**

实际电流分布绕 $z$ 轴轴对称。在经过 $z$ 轴及场点的镜面内，极矢量电流与空间几何不变；磁场作为轴矢量，镜面内的分量反号。因此磁场只能垂直这个镜面，也就是沿 $\boldsymbol e_\phi$：
$$
\boldsymbol B(\rho,z)=B_\phi(\rho,z)\boldsymbol e_\phi.
$$
在固定的 $\rho,z$ 圆周上，$B_\phi$ 又不依赖 $\phi$，因而可以提出环路积分号。

取环路正向为 $+\boldsymbol e_\phi$，相应跨越圆盘的法向为 $+\boldsymbol e_z$。对 $z>0$，注入导线电流沿 $-\boldsymbol e_z$，所以穿过圆盘的有向电流为 $-I$：
$$
\begin{aligned}
2\pi\rho B_\phi(\rho,z)&=-\mu_0 I,\\
B_\phi(\rho,z)&=-\frac{\mu_0 I}{2\pi\rho}.
\end{aligned}
$$
对 $z<0$，同一水平圆盘上没有导线电流，面电流又只在 $z=0$，因此
$$
2\pi\rho B_\phi(\rho,z)=0.
$$
合并得到
$$
\boxed{
\boldsymbol B(\rho,z)=
\begin{cases}
-\dfrac{\mu_0 I}{2\pi\rho}\boldsymbol e_\phi,&z>0,\ \rho>0,\\[4pt]
\boldsymbol0,&z<0.
\end{cases}}
$$
有电流侧的磁场大小为 $\mu_0 I/(2\pi\rho)$，方向由向下注入的电流决定。无电流侧为零，是“方向已由对称性唯一确定”与“环路包围电流为零”共同作用的结果，不是仅凭包围电流为零就能对任何几何判定局部磁场为零。

**第6步：构造球面单源与均匀流出的辅助系统。**

先只从球面点 $A$ 注入电流 $I$，让它以均匀法向密度从整个球面向外流出。球面面积为 $4\pi r^2$，故均匀流出电流每单位面积为
$$
j_{\rm out}=\frac{I}{4\pi r^2}.
$$
它的单位是 $\mathrm{A/m^2}$，与沿薄层的 $K$ 单位不同。均匀流出既用于保持辅助系统的稳恒守恒，也使问题绕 $OA$ 轴对称。

以 $OA$ 为极轴，令 $\gamma$ 为从 $A$ 量起的球心角。图2-5中的球冠从 $\gamma'=0$ 延伸到 $\gamma'=\gamma$，纬圈半径为 $r\sin\gamma$。沿薄层的辅助面电流指向远离 $A$ 的经线方向，记其单位矢量为 $\boldsymbol e_\gamma$。

![图2-5 单点注入、均匀法向流出的球冠电流守恒。](../figures/cap-02.png){width=64%}

球面面积元为
$$
\mathrm dS=r^2\sin\gamma'\,\mathrm d\gamma'\,\mathrm d\phi'.
$$
逐项积分：
$$
\begin{aligned}
S_{\rm cap}(\gamma)
&=\int_0^{2\pi}\!\mathrm d\phi'
  \int_0^\gamma r^2\sin\gamma'\,\mathrm d\gamma'\\
&=2\pi r^2[-\cos\gamma']_0^\gamma\\
&=2\pi r^2(1-\cos\gamma).
\end{aligned}
$$
因此球冠内部已经通过均匀流出通道离开的电流为
$$
I_{\rm cap,out}
=j_{\rm out}S_{\rm cap}
=\frac I2(1-\cos\gamma).
$$

**第7步：扣除球冠流出电流，得到辅助面电流。**

在球冠内输入 $I$，一部分已经法向流出，剩余部分才沿薄层穿过纬圈。由守恒，
$$
\begin{aligned}
2\pi r\sin\gamma\,K_A(\gamma)
&=I-I_{\rm cap,out}\\
&=I-\frac I2(1-\cos\gamma)\\
&=\frac I2(1+\cos\gamma).
\end{aligned}
$$
因此
$$
K_A(\gamma)
=\frac{I}{4\pi r}\frac{1+\cos\gamma}{\sin\gamma}.
$$
利用半角恒等式
$$
1+\cos\gamma=2\cos^2\frac\gamma2,\qquad
\sin\gamma=2\sin\frac\gamma2\cos\frac\gamma2,
$$
得
$$
\boxed{\boldsymbol K_A(\gamma)
=\frac I{4\pi r}\cot\frac\gamma2\,\boldsymbol e_\gamma.}
$$
$\gamma\to0$ 时，它按 $I/(2\pi r\gamma)$ 增大，对应点接触的电流汇聚；$\gamma\to\pi$ 时，穿过纬圈的电流已经趋零，$K_A\to0$。不能把纬圈电流恒写为 $I$，否则得到的是两相对点电极的另一种问题。

**第8步：把辅助电流写成球面切向矢量。**

令 $c_A=\boldsymbol a\cdot\boldsymbol n=\cos\gamma_A$。从电极方向 $\boldsymbol a$ 走向测点 $\boldsymbol n$ 时，增大 $\gamma_A$ 的单位切向量为
$$
\boldsymbol e_{\gamma_A}
=\frac{c_A\boldsymbol n-\boldsymbol a}{\sin\gamma_A}.
$$
这个表达式可直接检验：
$$
\begin{aligned}
\boldsymbol n\cdot(c_A\boldsymbol n-\boldsymbol a)
&=c_A-c_A=0,\\
|c_A\boldsymbol n-\boldsymbol a|^2
&=c_A^2+1-2c_A^2
=1-c_A^2
=\sin^2\gamma_A.
\end{aligned}
$$
所以它确实位于球面切平面，且归一化后为单位长度。在两极的退化位置，可以用极限而不是直接代入分母为零的式子。

再用
$$
\frac{\cot(\gamma_A/2)}{\sin\gamma_A}
=\frac{1+\cos\gamma_A}{\sin^2\gamma_A}
=\frac1{1-\cos\gamma_A},
$$
得到
$$
\boldsymbol K_A(\boldsymbol n)
=\frac I{4\pi r}
\frac{c_A\boldsymbol n-\boldsymbol a}{1-c_A}.
$$
以 $\boldsymbol b$ 为注入轴的另一辅助系统，同理有
$$
\boldsymbol K_B(\boldsymbol n)
=\frac I{4\pi r}
\frac{c_B\boldsymbol n-\boldsymbol b}{1-c_B},
\qquad c_B=\boldsymbol b\cdot\boldsymbol n.
$$

**第9步：相减恢复实际两电极电流，明确两种角度约定。**

将以 $A$ 为注入点的辅助系统减去以 $B$ 为注入点的辅助系统。前者在 $A$ 注入 $I$，后者反向后在 $B$ 引出 $I$；两套均匀法向流出电流大小相同、方向相反，处处抵消。故实际面电流为
$$
\boxed{
\boldsymbol K(\boldsymbol n)=\frac I{4\pi r}
\left[
\frac{c_A\boldsymbol n-\boldsymbol a}{1-c_A}
-\frac{c_B\boldsymbol n-\boldsymbol b}{1-c_B}
\right].}
$$
这一步是两个切向矢量的相减，不是把两个电流密度的正数大小机械相减。

在本题约定的 $\phi=0$ 测点，
$$
\begin{aligned}
\boldsymbol n&=(\sin\theta,0,\cos\theta),\\
\boldsymbol e_\theta&=(\cos\theta,0,-\sin\theta),\\
c_A&=\cos\theta,\qquad
c_B=\cos(\theta+\theta_0).
\end{aligned}
$$
第二个辅助切向矢量在 $\boldsymbol e_\theta$ 方向的投影为
$$
\begin{aligned}
\frac{(c_B\boldsymbol n-\boldsymbol b)\cdot\boldsymbol e_\theta}
{1-c_B}
&=\frac{-\boldsymbol b\cdot\boldsymbol e_\theta}{1-c_B}\\
&=\frac{\sin\theta_0\cos\theta+\cos\theta_0\sin\theta}
{1-\cos(\theta+\theta_0)}\\
&=\frac{\sin(\theta+\theta_0)}
{1-\cos(\theta+\theta_0)}\\
&=\cot\frac{\theta+\theta_0}{2}.
\end{aligned}
$$
第一项的投影为 $\cot(\theta/2)$，两项均没有垂直 $x$—$z$ 平面的分量。所以
$$
\boxed{
\boldsymbol K_{\phi=0}
=\frac I{4\pi r}
\left[
\cot\frac\theta2-\cot\frac{\theta+\theta_0}{2}
\right]\boldsymbol e_\theta.}
$$
若另将引出点放在正 $x$ 半平面，则 $\boldsymbol b=(\sin\theta_0,0,\cos\theta_0)$，相应的有向角差才是 $\theta-\theta_0$。两式使用的是不同的观察方位，不能把一种方位的图与另一种方位的式子混合。

**第10步：从有向分量得到第（3）问要求的大小。**

在本题当前坐标下，取 $0<\theta_0\le\pi$、$0<\theta<\pi$。此时
$$
0<\frac\theta2<\frac{\theta+\theta_0}{2}<\pi,
$$
$\cot u$ 在 $(0,\pi)$ 内严格递减，所以括号内为正。面电流在这一测点沿 $+\boldsymbol e_\theta$。这就是符号筛选的几何与数学依据。

用两个余切的差化简：
$$
\begin{aligned}
\cot u-\cot v
&=\frac{\cos u}{\sin u}-\frac{\cos v}{\sin v}\\
&=\frac{\cos u\sin v-\cos v\sin u}{\sin u\sin v}\\
&=\frac{\sin(v-u)}{\sin u\sin v}.
\end{aligned}
$$
代入 $u=\theta/2$、$v=(\theta+\theta_0)/2$：
$$
\boxed{
K_{\phi=0}
=\frac I{4\pi r}
\frac{\sin(\theta_0/2)}
{\sin(\theta/2)\sin[(\theta+\theta_0)/2]}.}
$$
例如 $\theta=\theta_0=\pi/2$ 时，测点位于正 $x$ 轴、引出点位于负 $x$ 轴，此测点并非引出电极。代入可得
$$
K=\frac I{4\pi r}
\left(\cot\frac\pi4-\cot\frac\pi2\right)
=\frac I{4\pi r}.
$$
所以不能看见 $\theta=\theta_0$ 就断言此处在引出点，坐标方位仍必须检查。

**第11步：补出任意方位的面电流分量与大小。**

任意 $\phi$ 时，
$$
c_B=\cos\theta\cos\theta_0-\sin\theta\cos\phi\sin\theta_0.
$$
球坐标切向基矢为
$$
\begin{aligned}
\boldsymbol e_\theta
&=(\cos\theta\cos\phi,\cos\theta\sin\phi,-\sin\theta),\\
\boldsymbol e_\phi&=(-\sin\phi,\cos\phi,0).
\end{aligned}
$$
分别与第9步的矢量式点乘，得
$$
\begin{aligned}
K_\theta&=\frac I{4\pi r}\left[
\cot\frac\theta2-
\frac{\sin\theta\cos\theta_0+\cos\theta\cos\phi\sin\theta_0}
{1-c_B}\right],\\
K_\phi&=\frac I{4\pi r}
\frac{\sin\theta_0\sin\phi}{1-c_B}.
\end{aligned}
$$
因此真实两电极系统在一般位置有 $K_\phi$，并非所有面电流都沿以 $z$ 轴为极轴的经线。第（3）问的 $\phi=0$ 只是一个简化截面。

为求大小，令
$$
\boldsymbol T_A=\frac{c_A\boldsymbol n-\boldsymbol a}{1-c_A},
\qquad
\boldsymbol T_B=\frac{c_B\boldsymbol n-\boldsymbol b}{1-c_B},
\qquad d=\boldsymbol a\cdot\boldsymbol b=\cos\theta_0.
$$
逐项计算：
$$
\begin{aligned}
|\boldsymbol T_A|^2&=\frac{1+c_A}{1-c_A},\\
|\boldsymbol T_B|^2&=\frac{1+c_B}{1-c_B},\\
\boldsymbol T_A\cdot\boldsymbol T_B
&=\frac{d-c_Ac_B}{(1-c_A)(1-c_B)}.
\end{aligned}
$$
最后一个分子的来源是
$$
(c_A\boldsymbol n-\boldsymbol a)\cdot
(c_B\boldsymbol n-\boldsymbol b)
=c_Ac_B-c_Ac_B-c_Ac_B+d=d-c_Ac_B.
$$
通分后，
$$
\begin{aligned}
|\boldsymbol T_A-\boldsymbol T_B|^2
&=\frac{(1+c_A)(1-c_B)+(1+c_B)(1-c_A)-2(d-c_Ac_B)}
{(1-c_A)(1-c_B)}\\
&=\frac{2-2d}{(1-c_A)(1-c_B)}.
\end{aligned}
$$
所以任意非接触点的面电流大小为
$$
\boxed{
K=\frac I{4\pi r}
\sqrt{\frac{2(1-\cos\theta_0)}
{(1-c_A)(1-c_B)}}.}
$$
用 $\gamma_A,\gamma_B$ 表示测点分别到两电极的球心夹角，还可写成
$$
K=\frac I{4\pi r}
\frac{\sin(\theta_0/2)}
{\sin(\gamma_A/2)\sin(\gamma_B/2)}.
$$
此处的 $\gamma_B\in[0,\pi]$ 是几何夹角；$\phi=0$ 中的 $\theta+\theta_0$ 则是方便确定切向符号的有向角差，两者不应在所有区间混同。

**第12步：为辅助磁场补齐球外的守恒电流。**

辅助系统中的均匀球面流出必须继续流向外部，否则球面会不断积累电荷，不能称为稳恒。令它沿每个径向向无穷远流动，则半径 $R>r$ 处的体电流密度为
$$
\boldsymbol J_{\rm rad}(R)=\frac I{4\pi R^2}\boldsymbol n.
$$
任一球面上积分都给 $I$：
$$
\int \boldsymbol J_{\rm rad}\cdot\boldsymbol n\,\mathrm dS
=\frac I{4\pi R^2}\cdot4\pi R^2=I.
$$
实际系统由两个辅助系统相减，故这些辅助径向流也处处抵消，只留下两根实际引线和实际球面电流。

图2-6中的外环路位于半径 $R$ 的球面上，关于辅助注入轴的极角为 $\gamma$，其圆周半径为 $R\sin\gamma$。环路的跨越面取球冠，不必取水平圆盘；两者对完整稳恒电流给出相同净穿越电流。

![图2-6 单源辅助系统的外部球冠安培环路。](../figures/ampere-02.png){width=66%}

**第13步：先证明辅助系统的球内磁场为零。**

一个辅助系统关于自己的注入轴轴对称，并关于包含该轴的每个镜面保持电流几何不变。因此其磁场只有关于该轴的方位分量，且沿相同半径的纬圈大小恒定：
$$
\boldsymbol B_A(R,\gamma)=B_{\phi_A}(R,\gamma)\boldsymbol e_{\phi_A}.
$$
对 $R<r$，可以在球内取一条关于该轴的圆形环路，其整个跨越圆盘都位于无电流的球内。环路定律给出
$$
2\pi R\sin\gamma\,B_{\phi_A}(R,\gamma)=0.
$$
因此所有非轴线位置均有 $\boldsymbol B_A=\boldsymbol0$；轴线上没有真实线电流穿过球内，磁场由连续性同样为零。

以 $B$ 为注入轴的辅助系统也有同样结论。两个系统相减后，
$$
\boxed{\boldsymbol B_{\rm in}=\boldsymbol0,\qquad R<r.}
$$
这里的零磁场包括了外部引线与球面电流的合成。若只单独保留球面电流而删去引线，不能继续使用这个结论。

**第14步：用外部球冠的有向电流求辅助磁场。**

取第12步的外球冠，法向为向外的 $\boldsymbol n$，环路正向为 $+\boldsymbol e_{\phi_A}$。注入细导线沿径向向内穿入球冠，在该面的有向贡献为 $-I$。

辅助均匀径向流向外穿出，球冠立体角为
$$
\Omega(\gamma)
=\frac{S_{\rm cap}(R,\gamma)}{R^2}
=2\pi(1-\cos\gamma).
$$
其有向穿出电流为 $I\Omega/(4\pi)$。所以
$$
\begin{aligned}
I_{\rm enc}
&=-I+\frac{I\Omega(\gamma)}{4\pi}\\
&=-I+\frac I2(1-\cos\gamma)\\
&=-\frac I2(1+\cos\gamma).
\end{aligned}
$$
环路积分得
$$
\begin{aligned}
2\pi R\sin\gamma\,B_{\phi_A}
&=-\frac{\mu_0 I}{2}(1+\cos\gamma),\\
B_{\phi_A}(R,\gamma)
&=-\frac{\mu_0 I}{4\pi R}\cot\frac\gamma2,
\qquad R>r.
\end{aligned}
$$
负号表示磁场沿负方位方向，与从外部向内注入的电流一致。分母为场点的 $R$，不是固定球半径 $r$。

因为
$$
\boldsymbol e_{\phi_A}
=\frac{\boldsymbol a\times\boldsymbol n}{\sin\gamma_A},
$$
再使用第8步的半角化简，得到
$$
\boldsymbol B_A(R,\boldsymbol n)
=-\frac{\mu_0 I}{4\pi R}
\frac{\boldsymbol a\times\boldsymbol n}{1-c_A}.
$$

**第15步：叠加两套磁场，求任意球外点的结果。**

第二个辅助系统把 $\boldsymbol a$ 替换为 $\boldsymbol b$。实际磁场为 $\boldsymbol B_A-\boldsymbol B_B$，于是
$$
\boxed{
\boldsymbol B_{\rm out}(R,\boldsymbol n)
=\frac{\mu_0 I}{4\pi R}
\left[
\frac{\boldsymbol b\times\boldsymbol n}{1-c_B}
-\frac{\boldsymbol a\times\boldsymbol n}{1-c_A}
\right],
\qquad R>r.}
$$
每一项都与 $\boldsymbol n$ 垂直，因此 $B_R=0$。但一般方位并不关于 $z$ 轴轴对称，不能同时断言 $B_\theta=0$。

用面电流矢量与法向的叉积还可写成
$$
\begin{aligned}
\boldsymbol K\times\boldsymbol n
&=\frac I{4\pi r}
\left[
-\frac{\boldsymbol a\times\boldsymbol n}{1-c_A}
+\frac{\boldsymbol b\times\boldsymbol n}{1-c_B}
\right],\\
\therefore\quad
\boldsymbol B_{\rm out}
&=\mu_0\frac rR\,\boldsymbol K(\boldsymbol n)\times\boldsymbol n.
\end{aligned}
$$
由于 $\boldsymbol K$ 为切向，$|\boldsymbol K\times\boldsymbol n|=K$，所以第（4）问球外磁场的大小为
$$
\boxed{
B_{\rm out}
=\frac{\mu_0 I}{4\pi R}
\sqrt{\frac{2(1-\cos\theta_0)}
{(1-c_A)(1-c_B)}}.}
$$
这条大小公式适用于任意方位，前提是场点不在两条理想细引线及其接触点上。在线电流模型的导线上，磁场奇异，不能直接以有限数值代替。

**第16步：写出球外分量，回到题目要求的简化截面。**

球坐标基矢满足
$$
\boldsymbol e_\theta\times\boldsymbol n=-\boldsymbol e_\phi,
\qquad
\boldsymbol e_\phi\times\boldsymbol n=\boldsymbol e_\theta.
$$
因此第15步与第11步共同给出
$$
B_\theta=\mu_0\frac rR K_\phi,
\qquad
B_\phi=-\mu_0\frac rR K_\theta,
\qquad B_R=0.
$$
在 $\phi=0$ 处，$K_\phi=0$，所以磁场只有 $-\boldsymbol e_\phi$ 方向：
$$
\boxed{
\boldsymbol B_{\rm out,\phi=0}
=-\frac{\mu_0 I}{4\pi R}
\left[
\cot\frac\theta2-\cot\frac{\theta+\theta_0}{2}
\right]\boldsymbol e_\phi.}
$$
在本题负 $x$ 半平面引出的约定下，方括号为正，故大小为
$$
B_{\rm out,\phi=0}
=\frac{\mu_0 I}{4\pi R}
\frac{\sin(\theta_0/2)}
{\sin(\theta/2)\sin[(\theta+\theta_0)/2]}.
$$
任意球内点仍为零。不能把 $\phi=0$ 的“只有方位分量”结论直接推广到 $\phi\ne0$ 的偏置电极系统。

**第17步：区分理想薄层内外两侧的磁场。**

在球面上避开两接触点，取局部面外法向 $\boldsymbol n$。图2-7是薄层的一小段截面，局部面电流用垂直纸面的符号表示；跨层窄矩形只用于推导切向磁场跃变，不是球面的额外导线。

![图2-7 局部面电流与两侧切向磁场的跃变。](../figures/jump-02.png){width=67%}

由跨越薄层的窄矩形安培环路，令短边高度趋零，短边积分消失；两条长边留下两侧切向磁场差。其矢量形式为
$$
\boldsymbol n\times
(\boldsymbol B_{\rm out}-\boldsymbol B_{\rm in})
=\mu_0\boldsymbol K.
$$
当前 $\boldsymbol B_{\rm in}=\boldsymbol0$，而第15步在 $R\to r^+$ 给出
$$
\boldsymbol B(r^+)=\mu_0\boldsymbol K\times\boldsymbol n.
$$
代入并使用三重积：
$$
\begin{aligned}
\boldsymbol n\times\boldsymbol B(r^+)
&=\mu_0\boldsymbol n\times(\boldsymbol K\times\boldsymbol n)\\
&=\mu_0\big[
\boldsymbol K(\boldsymbol n\cdot\boldsymbol n)
-\boldsymbol n(\boldsymbol n\cdot\boldsymbol K)\big]\\
&=\mu_0\boldsymbol K,
\end{aligned}
$$
与环路边界条件一致，说明叉积次序及负方位符号没有弄反。

因此，理想零厚度面上的两侧极限为
$$
\boldsymbol B(r^-)=\boldsymbol0,\qquad
\boldsymbol B(r^+)=\mu_0\boldsymbol K\times\boldsymbol n.
$$
它们不相等，单说“面上磁场”必须明确取哪一侧。若用对称薄层正则化、以中面平均自场作为约定，则
$$
\boldsymbol B_{\rm av}
=\frac{\boldsymbol B(r^+)+\boldsymbol B(r^-)}2
=\frac{\mu_0}{2}\boldsymbol K\times\boldsymbol n.
$$
这个平均值是附加约定，不是对理想电流面连续性的断言；真实有限厚度薄层内部还需给出电流沿厚度的分布。

**第18步：检验特殊角度、量纲和点接触极限。**

相对两极对应 $\theta_0=\pi$，此时
$$
\cot\frac{\theta+\pi}{2}=-\tan\frac\theta2,
$$
所以
$$
\begin{aligned}
K_\theta
&=\frac I{4\pi r}\left(\cot\frac\theta2+\tan\frac\theta2\right)\\
&=\frac I{4\pi r}
\frac{\cos^2(\theta/2)+\sin^2(\theta/2)}
{\sin(\theta/2)\cos(\theta/2)}\\
&=\frac I{2\pi r\sin\theta}.
\end{aligned}
$$
于是穿过每一纬圈的电流均为
$$
2\pi r\sin\theta\,K_\theta=I,
$$
符合北极输入、南极输出而中间无其他流入流出的真实守恒。

球外相应为
$$
B_{\rm out}=\frac{\mu_0 I}{2\pi R\sin\theta}.
$$
$R\sin\theta$ 正是到直径轴的垂距，因此球外结果与一条向下注入、从另一端向下引出的无限直导线在同一位置的磁场大小一致；球内实际没有这根穿心导线，所以球内仍为零。这两个事实不矛盾。

一般电极趋近时，固定远离接触点的测点有
$$
\theta_0\to0:\quad K\to0,\quad B_{\rm out}\to0.
$$
但如果测点也随电极一起靠近，两个极限不一定可以交换。不能将“远处场趋零”解释成点接触附近从此没有电流。

所有面电流式都为 $I/r$ 乘无量纲角函数，单位为 $\mathrm{A/m}$；磁场式为 $\mu_0 I/R$ 乘无量纲角函数，单位为特斯拉。平面式同样为 $\mu_0 I/\rho$。这些量纲检验能够识别漏掉半径、误用面积电流密度及将 $R$ 写成 $r$ 的错误。

<!-- KEEP_STUDENT_START -->

**第19步：汇总四问并说明理想化范围。**

把四问的结论并列写出，便于逐项核对研究对象和适用区域：
$$
\begin{aligned}
\text{（1）}\quad &B(O)=0,\\
\text{（2）}\quad &\boldsymbol B(\rho,z)=
\begin{cases}
-\dfrac{\mu_0 I}{2\pi\rho}\boldsymbol e_\phi,&z>0,\\
0,&z<0,
\end{cases}\\
\text{（3）}\quad &K\big|_{\phi=0}
=\frac I{4\pi r}
\left[\cot\frac\theta2-\cot\frac{\theta+\theta_0}{2}\right]\\
&\hspace{1.9em}=\frac I{4\pi r}
\frac{\sin(\theta_0/2)}
{\sin(\theta/2)\sin[(\theta+\theta_0)/2]},\\
\text{（4）}\quad &B_{\rm in}=0,\qquad
B_{\rm out}=\frac{\mu_0 I}{4\pi R}
\sqrt{\frac{2(1-\cos\theta_0)}
{(1-\boldsymbol a\cdot\boldsymbol n)
 (1-\boldsymbol b\cdot\boldsymbol n)}}.
\end{aligned}
$$
其中第（1）问是骨架的中心场，第（2）问的正 $z$ 侧有注入导线，第（3）问采用已经说明的负 $x$ 侧出线约定，第（4）问的球外式避开理想引线。平面和球面薄层处均取相应单侧极限。
大小、方向与表面跳跃的完整表达已在第15—17步给出，不能用大小公式代替方向信息。

点电极附近面电流发散，并不意味着任何有限宽度截面传送无限大总电流。总电流仍为 $I$，发散来自接触宽度趋零。若要求有限接触电势、耗散功率或接触内部磁场，须使用有限尺寸接触模型；本题所给 $I$ 是维持的总电流，不是由未给出的有限电压直接算出的电流。

<!-- KEEP_STUDENT_END -->

## 六、关键洞察

**洞察1：中心零磁场可由节点电势直接证明，不必先求三十条棱的电流。**

令十二个顶点位置为 $\boldsymbol v_i$，它们位于半径 $R_0$ 的同一球面。任意相邻两点之间的弦长为 $l$。一条棱上取参数
$$
\boldsymbol x(t)=\boldsymbol v_i+t(\boldsymbol v_j-\boldsymbol v_i),
\qquad 0\le t\le1.
$$
在中心，位移矢量为 $-\boldsymbol x(t)$，故
$$
(\boldsymbol v_j-\boldsymbol v_i)\times[-\boldsymbol x(t)]
=\boldsymbol v_i\times\boldsymbol v_j.
$$
它与 $t$ 无关。棱中点到中心的垂距为
$$
d_0=\sqrt{R_0^2-\frac{l^2}{4}},
$$
沿棱参数的距离平方则为
$$
|\boldsymbol x(t)|^2
=d_0^2+l^2(t-\tfrac12)^2.
$$
由于所有棱的 $l,d_0,R_0$ 相同，积分系数相同。完整积分为
$$
\begin{aligned}
G&=\int_0^1
\frac{\mathrm dt}{[d_0^2+l^2(t-\tfrac12)^2]^{3/2}}\\
&=\frac1l\int_{-l/2}^{l/2}
\frac{\mathrm ds}{(d_0^2+s^2)^{3/2}}\\
&=\frac1l\left[
\frac{s}{d_0^2\sqrt{d_0^2+s^2}}
\right]_{-l/2}^{l/2}\\
&=\frac1{d_0^2R_0}.
\end{aligned}
$$
这里使用平移换元与标准根式原函数；最后一步利用端点到球心的距离均为 $R_0$。

每条棱任取一个方向计入一次，中心总磁场为
$$
\boldsymbol B(O)
=\frac{\mu_0 G}{4\pi R_{\mathrm e}}
\sum_{\{i,j\}}(U_i-U_j)\,
\boldsymbol v_i\times\boldsymbol v_j.
$$
将每个 $U_i$ 的项收在一起；无论原来选哪条棱的正方向，属于顶点 $i$ 的系数都是
$$
U_i\,\boldsymbol v_i\times\sum_{j\sim i}\boldsymbol v_j.
$$
所以
$$
\sum_{\{i,j\}}(U_i-U_j)\boldsymbol v_i\times\boldsymbol v_j
=\sum_i U_i\,\boldsymbol v_i\times
\left(\sum_{j\sim i}\boldsymbol v_j\right).
$$
正二十面体中，五个邻点绕 $O\boldsymbol v_i$ 成正五边形排列。横向分量相消，每个邻点沿该轴的投影相同，因此
$$
\sum_{j\sim i}\boldsymbol v_j=\sqrt5\,\boldsymbol v_i.
$$
这个系数的几何来源也可展开核对。令黄金比 $g=(1+\sqrt5)/2$，满足 $g^2=g+1$。正二十面体的一组未缩放顶点坐标为 $(0,\pm1,\pm g)$、$(\pm1,\pm g,0)$、$(\pm g,0,\pm1)$；所有顶点到中心的距离平方都是 $g+2$。取相邻的 $(0,1,g)$ 与 $(1,g,0)$，两者距离平方为
$$
\begin{aligned}
l_*^2&=1+(1-g)^2+g^2\\
&=1+(2-g)+(g+1)=4.
\end{aligned}
$$
它们的点积为 $g$，因此相邻顶点夹角满足
$$
\cos\eta=\frac g{g+2}=\frac1{\sqrt5},
$$
其中最后一步由 $g\sqrt5=g+2$ 验证。整体缩放不改变夹角；绕任一顶点的五重旋转又使五个邻点的轴向投影相同。所以五个投影之和为 $5(1/\sqrt5)\boldsymbol v_i=\sqrt5\boldsymbol v_i$。于是求和中每一项都含 $\boldsymbol v_i\times\boldsymbol v_i=\boldsymbol0$，总磁场为零。

这一证明并没有用到 $A$、$B$ 相邻，只用了等电阻、等弦长和邻点旋转结构。因此任意给定一对顶点的稳恒输入、输出，骨架中心磁场仍为零；真实电流不必具有某个简单轴对称。等电阻条件一旦破坏，上面的公共系数及电势差求和一般就不再成立。

**洞察2：平面下侧的零磁场来自两种实际贡献的抵消。**

在场点 $(\rho,0,z)$，半无限注入线从 $z'=0$ 延伸至 $+\infty$，电流方向向下。其毕奥—萨伐尔积分为
$$
B_{{\rm wire},\phi}
=-\frac{\mu_0 I}{4\pi}
\int_0^\infty
\frac{\rho\,\mathrm dz'}{[\rho^2+(z-z')^2]^{3/2}}.
$$
取 $u=z'-z$，用
$$
\int\frac{\rho\,\mathrm du}{(\rho^2+u^2)^{3/2}}
=\frac{u}{\rho\sqrt{\rho^2+u^2}},
$$
得到
$$
B_{{\rm wire},\phi}
=-\frac{\mu_0 I}{4\pi\rho}
\left(1+\frac z{\sqrt{\rho^2+z^2}}\right).
$$
导线单独在平面下侧也有磁场，绝不是“线电流仅作用于它所在半空间”。

将真实径向面电流的面积分写成
$$
B_{{\rm sheet},\phi}
=-\frac{\mu_0 I}{8\pi^2}
\int_0^\infty\!\mathrm ds\int_0^{2\pi}
\frac{z\cos\alpha\,\mathrm d\alpha}
{[\rho^2+s^2-2\rho s\cos\alpha+z^2]^{3/2}}.
$$
这里面电流为 $I/(2\pi s)$，面积元为 $s\,\mathrm ds\,\mathrm d\alpha$，两个 $s$ 正好约去；不能再多乘或少乘一个 $s$。

可用已独立确定的完整环路解减去导线积分求出面电流项：
$$
\begin{aligned}
B_{{\rm sheet},\phi}
&=B_\phi-B_{{\rm wire},\phi}\\
&=-\frac{\mu_0 I}{4\pi\rho}
\left[
\operatorname{sgn}z-\frac z{\sqrt{\rho^2+z^2}}
\right],\qquad z\ne0.
\end{aligned}
$$
对 $z<0$，方括号为负，面电流贡献沿 $+\boldsymbol e_\phi$，恰好抵消导线贡献。对 $z>0$，两项同向，并合成为高度无关的完整结果。直接对面电流面积分作数值积分，也能独立得到这一表达式，而非只能由相减定义它。

**洞察3：面电流还可由球面电势复核。**

由单源辅助解和 $\boldsymbol K_A=-\Sigma\nabla_s V_A$，在远离接触点处
$$
\frac{\mathrm dV_A}{\mathrm d\gamma}
=-\frac{I}{4\pi\Sigma}\cot\frac\gamma2.
$$
利用
$$
\int\cot\frac\gamma2\,\mathrm d\gamma
=2\ln\sin\frac\gamma2+C,
$$
可取
$$
V_A=-\frac I{2\pi\Sigma}\ln\sin\frac{\gamma_A}{2}+C_A.
$$
两个辅助电势相减后，实际电势为
$$
V=\frac I{2\pi\Sigma}
\ln\frac{\sin(\gamma_B/2)}{\sin(\gamma_A/2)}+C.
$$
将 $1-\cos\gamma=2\sin^2(\gamma/2)$ 代入，等价于
$$
V=\frac I{4\pi\Sigma}
\ln\frac{1-c_B}{1-c_A}+C.
$$
沿球面的微分满足
$$
\nabla_s c_A=\frac{\boldsymbol a-c_A\boldsymbol n}{r}.
$$
所以
$$
\begin{aligned}
-\Sigma\nabla_s V
&=-\frac I{4\pi}\left[
\frac{-\nabla_s c_B}{1-c_B}
-\frac{-\nabla_s c_A}{1-c_A}\right]\\
&=\frac I{4\pi r}\left[
\frac{c_A\boldsymbol n-\boldsymbol a}{1-c_A}
-\frac{c_B\boldsymbol n-\boldsymbol b}{1-c_B}\right],
\end{aligned}
$$
重现主解的面电流，而方向与系数都得到独立检查。

在没有点电极的区域，
$$
\begin{aligned}
\nabla_s^2\ln\sin\frac\gamma2
&=\frac1{r^2\sin\gamma}
\frac{\mathrm d}{\mathrm d\gamma}
\left[\sin\gamma\cdot\frac12\cot\frac\gamma2\right]\\
&=\frac1{r^2\sin\gamma}
\frac{\mathrm d}{\mathrm d\gamma}\left[\frac{1+\cos\gamma}{2}\right]\\
&=-\frac1{2r^2}.
\end{aligned}
$$
电势中两个对数项的常数拉普拉斯量相减为零，所以 $\nabla_s\cdot\boldsymbol K=-\Sigma\nabla_s^2V=0$。实际薄层内部没有沿面均匀丢失电流，均匀流出只属于已经抵消的两个辅助问题。

**洞察4：为什么辅助径向体电流不会额外产生磁场？**

球外的均匀径向体电流分布具有完整球对称性。若只考虑这一个体电流分布，其磁场若非零，由所有转动不变性只能沿场点的径向；但任一个包含该径向的镜面又使径向轴矢量反号，所以该贡献为零。也可以在毕奥—萨伐尔积分中将各方向的对应电流元成对消去。

这个零贡献不意味着可以从守恒方程中删掉径向体电流。它虽然不产生合成磁场，却参与“导线注入—球面铺展—径向流出”的完整稳恒电流守恒，使辅助系统能够合法使用安培环路定律。

以辅助注入轴为极轴，在球外远离轴线处，
$$
B_\phi=-\frac{\mu_0 I}{4\pi R}\cot\frac\gamma2.
$$
它的径向旋度为
$$
\begin{aligned}
(\nabla\times\boldsymbol B)_R
&=\frac1{R\sin\gamma}
\frac{\partial(\sin\gamma B_\phi)}{\partial\gamma}\\
&=-\frac{\mu_0 I}{4\pi R^2\sin\gamma}
\frac{\partial(1+\cos\gamma)}{\partial\gamma}\\
&=\frac{\mu_0 I}{4\pi R^2}.
\end{aligned}
$$
恰好等于辅助径向电流的 $\mu_0J_R$。为什么这并不与“径向体电流单独的磁场为零”矛盾？因为单独截取径向体电流或面内电流，都不是完整闭合稳恒电流；只对完整守恒分布才能逐点使用没有额外项的静磁安培方程。毕奥—萨伐尔贡献可以线性拆分，但不能对每一段开放的非守恒电流分别断言其旋度仅为 $\mu_0\boldsymbol J$。

两辅助系统相减后，均匀径向电流及上式的均匀径向旋度都抵消。实际球外远离两条引线处才有 $\nabla\times\boldsymbol B=\boldsymbol0$。这是区分“积分贡献拆分”与“每个子分布独立满足静磁方程”的关键。

**洞察5：点接触可固定总电流，但电势差与耗散存在奇异性。**

在注入点附近，球面弧长 $s=r\gamma_A$ 很小，
$$
K\sim\frac I{2\pi s},
\qquad
V\sim-\frac I{2\pi\Sigma}\ln s+\text{常量}.
$$
点接触极限中电势对数发散。局部耗散功率元为
$$
\mathrm dP=\frac{K^2}{\Sigma}\,\mathrm dS.
$$
小圆环的面积元约为 $2\pi s\,\mathrm ds$，因此
$$
\begin{aligned}
\mathrm dP
&\sim\frac1\Sigma\frac{I^2}{4\pi^2s^2}\,2\pi s\,\mathrm ds\\
&=\frac{I^2}{2\pi\Sigma}\frac{\mathrm ds}{s}.
\end{aligned}
$$
从接触尺度 $\varepsilon$ 积分到固定宏观尺度 $L$，
$$
P_{\rm near}\sim\frac{I^2}{2\pi\Sigma}\ln\frac L\varepsilon.
$$
$\varepsilon\to0$ 时耗散发散。题目固定 $I$ 的理想点电极数学解仍可描述远离接触点的场，但不能同时声称一个有限电压源能在严格零面积接触处维持有限的非零电流。

第（4）问的远处磁场按 $1/R$ 衰减，而不是按封闭小线圈的 $1/R^3$ 衰减。原因是两条实际引线延伸至无穷远，整个电流系统并非局域的小线圈。不能根据球形薄层的外观直接套用磁偶极远场公式。

## 七、易错点

真实两电极网络不具备单电极辅助网络的五重对称性。若直接把实际输入 $I$ 均分到五条出发棱，会得到错误的各棱电流；中心零磁场的结论不能为错误的中间假设作辩护。

在辅助离散问题中，特殊顶点的净注入为 $11I/12$，不是 $I$；另一个辅助网络在这个顶点仍贡献 $I/12$，相加才恢复实际的 $I$。十二个顶点的补偿分配必须包含特殊顶点自身。

旋转对称只排除轴外磁场，不排除轴向磁场。镜面对称中的磁场是叉积产生的轴矢量，不能把它当普通位移矢量反射。忽略这一点会漏掉证明中心场为零的第二半。

环路电流是有向量。平面上侧以 $+\boldsymbol e_z$ 为跨越面法向时，注入电流为 $-I$；球外球冠以向外为正时，细引线贡献也是 $-I$。先记清这些正负，再求磁场方向，不能最后凭经验补负号。

平面下侧为零不等于半无限导线在下侧没有磁场。球内为零也不等于球面电流单独在球内没有磁场。两种零场都是完整实际分布的叠加结果。

球冠的均匀流出量必须扣除。只有相对两极的真实输入、输出问题，所有中间纬圈才始终传送同一总电流 $I$；单源均匀流出的辅助问题传送量为 $I(1+\cos\gamma)/2$。

$\cot[(\theta+\theta_0)/2]$ 的加号在负 $x$ 半平面引出、正 $x$ 半平面观察的约定下正确。若引出点改到另一侧，应连同 $\boldsymbol b$、$\phi$ 和切向方向一起更改。几何夹角、极角与有向角差不能混用。

实际偏置电极的磁场一般含 $B_\theta$。球内零场、球外 $B_R=0$、特定截面的 $B_\theta=0$ 是三个范围不同的结论，不应缩写成“一切位置只有 $B_\phi$”。

球面磁场的内外极限不同。将 $R=r$ 直接代入球外式得到的是外侧极限，不是自动得到薄层内的平均场。点接触及理想细导线处的奇异性，也不能用普通有限值代入掩盖。

量纲上，$K$ 是 $\mathrm{A/m}$，均匀法向流出密度是 $\mathrm{A/m^2}$，球外场式分母是 $R$；这三处最容易因记号相近而混淆。

## 八、课堂讲解建议

先让学生在立体骨架中指出相邻电极，并判断真实网络能否绕输入顶点旋转后不变。不要先给出“对称所以零”；先让学生发现相邻输出顶点会破坏这一对称性，再引入两套辅助节点注入，逐点板书相加结果。由此建立“给电流守恒条件做叠加”的实际意义。

在辅助网络中心的磁场判断中，分两次提问：“旋转只留下哪个方向？”“镜面中的配对电流对这个分量是什么关系？”把两半推理分开，比把旋转和镜像同时归结为一个对称性口号更容易理解。若学生尚未学轴矢量，直接用一对电流元的叉积比方向，再归纳镜面变换规则。

平面问题先画圆周上的径向电流，让学生将 $K$ 与圆周长度相乘检验单位。再画上、下圆盘，让学生先说包围电流的正负，后算磁场。若误把平面理解成磁屏蔽板，可暂时删去径向面电流，只保留导线，讨论下侧是否还能零场，引出真实贡献的抵消。

球面辅助问题中，先用图2-5区分球冠面积与纬圈长度。板书固定采用“输入量减去冠内流出量等于跨圈量”，并给每个量单独标单位；不要直接写余切结果。做完一个辅助系统后，才把另一个旋转过来相减。

讲解第9步时，用图2-2同时指向正 $x$ 的测点与负 $x$ 的引出点，要求学生在同一大圆上量有向角。之后再展示另一种坐标约定，说明加号与减号都可能正确，但各自必须对应自己的图和方向。这个比较能防止把符号校对变成不看几何的机械操作。

最后用局部图2-7检查外侧场与面电流的右手关系，让学生亲手检验 $\boldsymbol n\times(\boldsymbol K\times\boldsymbol n)=\boldsymbol K$。若主解已经熟悉，可选电势路线或三十棱求和路线深入，而不是重复抄一遍相同结论。

## 九、变式训练

**变式1：把平面两侧零场与非零场拆成实际来源。**

保持第（2）问的通电方式，令 $I=2.00\,\mathrm A$、$\rho=2.00\,\mathrm{cm}$。分别在 $z=3\rho/4$ 和 $z=-3\rho/4$ 求直导线贡献、面电流贡献和合成磁场的有向方位分量。

两点到注入点的距离均为
$$
\sqrt{\rho^2+z^2}=\frac54\rho,
\qquad
\frac z{\sqrt{\rho^2+z^2}}=\pm\frac35.
$$
公共系数为
$$
C=\frac{\mu_0I}{4\pi\rho}
=\frac{(4\pi\times10^{-7})(2.00)}
{4\pi(2.00\times10^{-2})}
=1.00\times10^{-5}\,\mathrm T.
$$
上侧逐项代入：
$$
\begin{aligned}
B_{{\rm wire},\phi}^{(+)}
&=-C(1+\tfrac35)=-1.60\times10^{-5}\,\mathrm T,\\
B_{{\rm sheet},\phi}^{(+)}
&=-C(1-\tfrac35)=-4.00\times10^{-6}\,\mathrm T,\\
B_\phi^{(+)}
&=-2.00\times10^{-5}\,\mathrm T.
\end{aligned}
$$
下侧逐项代入：
$$
\begin{aligned}
B_{{\rm wire},\phi}^{(-)}
&=-C(1-\tfrac35)=-4.00\times10^{-6}\,\mathrm T,\\
B_{{\rm sheet},\phi}^{(-)}
&=-C(-1+\tfrac35)=+4.00\times10^{-6}\,\mathrm T,\\
B_\phi^{(-)}&=0.
\end{aligned}
$$
所有负号均表示负方位方向。下侧两项各非零，只有合成值为零；上侧合成值与第（2）问的 $\mu_0I/(2\pi\rho)$ 一致。

**变式2：将两电极放在球面的南北两极。**

两电极夹角为 $\theta_0=\pi$。给定 $r=0.200\,\mathrm m$、$I=0.800\,\mathrm A$，求 $\theta=\pi/3$ 处的面电流密度；再求同一径向方向、距离球心 $R=0.500\,\mathrm m$ 处的磁场，并说明球内 $R=0.100\,\mathrm m$ 处的结果。

从任一北极球冠的守恒出发，冠内只有北极输入，中间没有分布式流出，南极尚在冠外，所以所有纬圈传送电流 $I$：
$$
2\pi r\sin\theta\,K_\theta=I.
$$
故
$$
\begin{aligned}
K_\theta
&=\frac{0.800}{2\pi(0.200)(\sqrt3/2)}
=\frac4{\pi\sqrt3}\,\mathrm{A/m}\\
&\approx0.7351\,\mathrm{A/m}.
\end{aligned}
$$
方向为朝向南极的 $+\boldsymbol e_\theta$。球外磁场为
$$
\begin{aligned}
B_\phi
&=-\mu_0\frac rR K_\theta\\
&=-\frac{(4\pi\times10^{-7})(0.800)}
{2\pi(0.500)(\sqrt3/2)}\\
&=-\frac{6.4\times10^{-7}}{\sqrt3}\,\mathrm T
\approx-3.695\times10^{-7}\,\mathrm T.
\end{aligned}
$$
负方位方向由实际电流确定。球内 $R=0.100\,\mathrm m<r$，合成场为零，不能把外部表达继续延伸到球内。

再检验外侧面上的边界：$R\to r^+$ 时 $B_\phi=-\mu_0K_\theta$，与切向跃变条件一致。此处面电流有限，因为 $\theta=\pi/3$ 不在两个理想点接触处。

**变式3：在两电极之间的大圆中点求场。**

取电极夹角 $\theta_0=\pi/2$，仍让引出点位于负 $x$ 半平面。求两电极短大圆弧中点的面电流及球外同一方向的磁场。给定 $r=0.100\,\mathrm m$、$I=2.00\,\mathrm A$、外场点 $R=0.300\,\mathrm m$。

中点位于负 $x$ 半平面，故它的球坐标为 $\theta=\pi/4,\phi=\pi$，不是主解先考虑的 $\phi=0$ 测点。到两个电极的球心夹角均为
$$
\gamma_A=\gamma_B=\frac{\theta_0}{2}=\frac\pi4.
$$
从任意方位的大小式代入：
$$
\begin{aligned}
K
&=\frac I{4\pi r}
\frac{\sin(\theta_0/2)}{\sin^2(\theta_0/4)}\\
&=\frac I{4\pi r}
\frac{2\sin(\theta_0/4)\cos(\theta_0/4)}
{\sin^2(\theta_0/4)}\\
&=\frac I{2\pi r}\cot\frac{\theta_0}{4}.
\end{aligned}
$$
$\cot(\pi/8)=1+\sqrt2$，所以
$$
K=\frac{10(1+\sqrt2)}\pi\,\mathrm{A/m}
\approx7.6847\,\mathrm{A/m}.
$$
该点实际电流沿 $\phi=\pi$ 经线上的 $+\boldsymbol e_\theta$，即从注入电极走向引出电极。$\boldsymbol e_\phi=(0,-1,0)$，因此磁场沿 $-\boldsymbol e_\phi=+\boldsymbol e_y$。

球外磁场大小：
$$
\begin{aligned}
B
&=\mu_0\frac rR K\\
&=\frac{\mu_0I}{2\pi R}\cot\frac\pi8\\
&=\frac43(1+\sqrt2)\times10^{-6}\,\mathrm T\\
&\approx3.2190\times10^{-6}\,\mathrm T.
\end{aligned}
$$
由电势式，两种球心夹角相等，故中点电势可选为零。零电势只是参考值，并不意味着电势梯度或面电流为零；本题正好给出一个两者不能混淆的例子。

**变式4：用有限接触帽求球面薄层的电阻。**

把南北两极的点接触改成两块等大小的理想等势球冠接触帽，其边缘极角分别为 $\alpha$ 与 $\pi-\alpha$，$0<\alpha<\pi/2$。球冠接触帽之间的球面带是均匀电阻薄层，面电导为 $\Sigma$；全部电流 $I$ 从北帽流向南帽。求两接触帽之间的电阻。

对中间球面带的任一纬圈，总电流为 $I$，所以
$$
K_\theta=\frac I{2\pi r\sin\theta},
\qquad \alpha<\theta<\pi-\alpha.
$$
由面内欧姆定律，
$$
E_\theta=\frac{K_\theta}{\Sigma},
\qquad
-\frac1r\frac{\mathrm dV}{\mathrm d\theta}=E_\theta.
$$
北帽电势较高。两帽电势差为
$$
\begin{aligned}
\Delta V
&=\int_\alpha^{\pi-\alpha}E_\theta\,r\,\mathrm d\theta\\
&=\frac I{2\pi\Sigma}
\int_\alpha^{\pi-\alpha}\frac{\mathrm d\theta}{\sin\theta}\\
&=\frac I{2\pi\Sigma}
\left[\ln\tan\frac\theta2\right]_\alpha^{\pi-\alpha}\\
&=\frac I{2\pi\Sigma}
\ln\frac{\cot(\alpha/2)}{\tan(\alpha/2)}\\
&=\frac I{\pi\Sigma}\ln\cot\frac\alpha2.
\end{aligned}
$$
因此
$$
\boxed{R_{\rm film}=\frac1{\pi\Sigma}\ln\cot\frac\alpha2.}
$$
球半径 $r$ 在积分中约去，因为纬圈长度与沿经线长度都随 $r$ 同比例变化；接触帽的角大小固定时，薄层电阻不依赖球半径。这不表示固定实际接触半径时电阻也与球半径无关，两种固定条件不同。

例如 $\Sigma=0.0500\,\mathrm S$、$\alpha=10.0^\circ$、$I=0.120\,\mathrm A$：
$$
\begin{aligned}
R_{\rm film}
&=\frac1{\pi(0.0500)}\ln\cot5.0^\circ
\approx15.51\,\Omega,\\
\Delta V&=IR_{\rm film}\approx1.861\,\mathrm V.
\end{aligned}
$$
当 $\alpha\to0$，
$$
\cot\frac\alpha2\sim\frac2\alpha,
\qquad
R_{\rm film}\sim\frac1{\pi\Sigma}\ln\frac2\alpha\to\infty.
$$
这与主解点电极的对数电势、耗散奇异性相符。当 $\alpha\to\pi/2$，两帽边缘相接，电阻带宽趋零，$R_{\rm film}\to0$。两个极限同时检查了积分上下限和电势差的符号。
