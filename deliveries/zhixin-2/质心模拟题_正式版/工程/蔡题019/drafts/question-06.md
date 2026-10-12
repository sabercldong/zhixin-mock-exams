# 第6题

<!-- question-start -->

测量一大块均匀薄金属板的电导率$\sigma$，但只能接触板角附近的一小部分。板的厚度为$t$，沿相邻两条边依次取接触点$A,B,C,D$，角点记为$O$。其中$OA=OD=l$，$OB=OC=\lambda l$。恒流源从$A$向板内输入电流$I$，从$D$引出同样大小的电流，用电压表测得$B,C$之间的电压差$U$。

（1）计算金属板的电导率。

（2）改用厚度仍为$t$、半径为$r$的均匀薄圆盘，四个接触点$A,B,C,D$依次位于圆周上，且$\angle AOB=\angle BOC=\angle COD=\pi/3$。从$A$输入电流$I$，从$D$引出电流$I$，测得$B,C$间电压差$U$，求圆盘的电导率。

约定$I>0$，电压表正端接$B$、负端接$C$，即$U=V_B-V_C$。接触点按图中次序排列，故$0<\lambda<1$。电压表输入电阻足够大，$B,C$两端不分流；除电流接触处外，板边不向外导电。第（1）问的角部两条边互相垂直，实际内角为$\omega=\pi/2$；角部结果采用远离其他板边的局部大板近似。两边垂直，跨边距离按平面直角几何计算；一般夹角仅作为改变几何条件时的对照。

![图6-1 薄板角部的电流接触、电压接触与厚度。](../figures/corner-06.png){width=74%}

<!-- question-end -->

## 一、题型定位

本题是二维稳恒导电场的四端测量问题。电流端决定板内电势分布，电压端读取两个位置的电势差；两组端子并不是串联的四个电阻。由于电流在板面内扩散，通常不能直接套用一段直导线的$R=\rho L/S$，必须先求扩散电流的场，再把电势差与电导率联系起来。

角部和圆盘的共同核心是无电流穿过绝缘边界。角部可通过同号镜像使法向电流相消；圆盘可构造在整个圆周上满足无流边界的对数电势。计算中最敏感的不是积分本身，而是边缘接触的电流系数、真实几何距离和电压正负端。

第一问还包含模型辨析：平面图的投影夹角不能自动当作物理夹角。直角和直边给出不同几何因子，仅凭相同的四个沿边距离并不能混用两种公式。一般夹角结果能明确指出该差别的来源。

## 二、知识点

均匀各向同性金属满足局部欧姆定律$\boldsymbol J=\sigma\boldsymbol E$，其中$\boldsymbol J$是体电流密度，单位为$\mathrm{A/m^2}$。稳恒电场满足$\boldsymbol E=-\nabla V$。薄板厚度方向近似均匀时，定义面电流密度$\boldsymbol K=t\boldsymbol J$，其单位为$\mathrm{A/m}$，于是$\boldsymbol K=-\sigma t\nabla V$。厚度$t$不能省略，否则最终得到的是面电导而非体电导率。

在没有注入或抽出电流的板内小区域，电荷不积累，故$\nabla\cdot\boldsymbol K=0$。当$\sigma,t$为常量时，它成为二维拉普拉斯方程$\nabla^2V=0$。绝缘板边满足$\boldsymbol K\cdot\boldsymbol n=0$，亦即$\partial V/\partial n=0$；这里$\boldsymbol n$是板面内指向外部的单位法向量。

点接触产生的二维电势随距离的对数变化。全平面电流源$Q$的电场大小为$Q/(2\pi\sigma t\rho)$，其电势可写成$-Q\ln(\rho/\rho_0)/(2\pi\sigma t)$。相应电流汇的符号相反。$\rho_0$只用于让对数自变量无量纲，测量电势差时它消去。

面电阻记为$R_{\square}=1/(\sigma t)$，单位为$\Omega$。测得的四端电阻$R_4=U/I$等于面电阻乘一个无量纲几何因子。几何因子一经正确求出，$\sigma$由$\sigma=1/(tR_{\square})$得到，而不能把$R_4$直接当作$R_{\square}$。

## 三、物理图像

图6-1保留薄板的厚度和两个可接触边缘的空间关系，电流从$A$进入、从$D$离开；蓝色引线只接$B,C$及电压表。板内电流由源端向汇端扩散，并非沿图中的边线流成一根导线。电压引线不参与承载$I$，其接触位置却决定被测的电势差。

在直角模型中，可把板面转到正视平面，选$A,B$在$x$正半轴上，$C,D$在$y$正半轴上，真实金属占第一象限。为使两条边都不漏电，把源和汇按边界反射延拓到全平面。这些镜像是求解工具，不是另加的实际电极；图6-3中的等效电流为$2I$，实际电流端仍只有$I$。

圆盘模型的边界是封闭圆周，但所有板内点都位于同一个平面。其电势可由源点到场点、汇点到场点两条弦长的比值表示。图6-4中的$r$和$\sqrt3r$随后分别进入$V_B,V_C$，而不是只作为图中标签。

## 四、解题入口

先由一个电流端的截流面积推导电势系数，分清全圆与半圆的二倍差别。然后在直角板中写出四个等效源、汇的位置，计算它们到$B,C$的实际距离。沿同一条边的距离可相减；跨两条垂直边的距离必须用勾股定理，不能也写成$(1\pm\lambda)l$。

圆盘不宜把所有边界粗略当成直线后照搬角部镜像。应先检验候选对数电势在圆周上的法向导数为零，再计算四条弦长。最后统一检查$U$的正负、厚度量纲、尺度消去及接触点靠近时的极限。

## 五、解析

（1）从电流守恒建立薄板导电方程。

取板内不含电流接触点的一小块面积，稳恒状态下流入电流等于流出电流。对任意这类区域，散度定理给出$\nabla\cdot\boldsymbol K=0$。再代入$\boldsymbol K=t\sigma\boldsymbol E=-\sigma t\nabla V$，得到

$$
\begin{aligned}
0&=\nabla\cdot(-\sigma t\nabla V),\\
0&=-\sigma t\nabla^2V,\\
\nabla^2V&=0\qquad\text{（非接触区域）}.
\end{aligned}
$$

第一步使用电流守恒，第二步使用均匀厚度与均匀电导率，第三步除以非零的$\sigma t$。若板材不均匀，第二步不能把$\sigma t$移出散度，本题的对数势也不再普遍适用。边缘处除了$A,D$，没有外部导电通道，故另外必须满足

$$
\boldsymbol K\cdot\boldsymbol n=0
\quad\Longleftrightarrow\quad
\frac{\partial V}{\partial n}=0.
$$

电势只确定到一个任意加法常数；这个自由度不会影响电场或$U$。

（2）推导全平面点源的电场与对数电势。

先考虑一张无限薄板，某内点向板内注入电流$Q$。以接触点为圆心取半径为$\rho$的圆，电流径向穿过的面积不是$\pi\rho^2$，而是圆周长度乘厚度，即$2\pi\rho t$。对称性使该圆周上的径向电流密度相同，因此

$$
\begin{aligned}
Q&=J_\rho\,(2\pi\rho t),\\
J_\rho&=\frac{Q}{2\pi\rho t},\\
E_\rho&=\frac{J_\rho}{\sigma}
=\frac{Q}{2\pi\sigma t\rho}.
\end{aligned}
$$

对于源端$Q>0$，电场向外，沿增大的$\rho$电势降低。由$E_\rho=-dV/d\rho$，对径向坐标积分：

$$
\begin{aligned}
V(\rho)-V(\rho_0)
&=-\int_{\rho_0}^{\rho}
\frac{Q}{2\pi\sigma t s}\,ds\\
&=-\frac{Q}{2\pi\sigma t}
\left[\ln s\right]_{\rho_0}^{\rho}\\
&=-\frac{Q}{2\pi\sigma t}
\ln\frac{\rho}{\rho_0}.
\end{aligned}
$$

这里利用$\int ds/s=\ln s$并先保留两个积分端点。电流汇可取$Q<0$，于是电场指向汇端、电势随远离汇端而升高。源、汇电流等大反向时，叠加后可以写成距离之比的对数，任意的$\rho_0$随之消去。

（3）由半圆截流检查边缘接触的二倍系数。

接触点位于一条平直绝缘边缘时，电流只能流入板内的一侧。图6-2左侧的半圆截流面积为$\pi\rho t$，右侧的全圆面积为$2\pi\rho t$。为了在半板内真实输入$I$，左侧接触附近的径向场为$I/(\pi\sigma t\rho)$；把它延拓到全平面，必须使用等效源$2I$。

![图6-2 边缘半圆截流与全平面等效电流的对应。](../figures/flux-06.png){width=86%}

于是图中两种描述具有相同的板内电场：

$$
\frac{I}{\pi\rho t\sigma}
=\frac{2I}{2\pi\rho t\sigma}.
$$

边缘接触的二倍系数来自可流通的角度减半，而不是“镜像电势再额外乘二”。后面既已使用$2I$作为全平面源强，电势系数就必须是$2I/(2\pi\sigma t)=I/(\pi\sigma t)$，不能重复加倍。

（4）在直角板中逐个确定等效源、汇的位置。

在$\omega=\pi/2$情况下，取$O=(0,0)$，板占$x\geq0,y\geq0$。坐标写为

$$
\begin{aligned}
A&=(l,0),&B&=(\lambda l,0),\\
C&=(0,\lambda l),&D&=(0,l).
\end{aligned}
$$

图6-3给出延拓后的全平面构造：$A$及其镜像$A^*=(-l,0)$均为等效源$+2I$，$D$及其镜像$D^*=(0,-l)$均为等效汇$-2I$。其中$A$已在$y=0$边上，关于该边的同号延拓合并成$2I$；再关于$x=0$反射得到$A^*$。对$D$同理。

![图6-3 直角薄板的绝缘边界延拓与跨边几何距离。](../figures/images-06.png){width=60%}

在$y=0$上，来自$D,D^*$的法向场分量等大反向；$A,A^*$的场在这条线上没有法向分量。在$x=0$上，来自$A,A^*$的法向分量相消；$D,D^*$的场没有法向分量。因此两条边除接触点外都满足$\partial V/\partial n=0$。在真实接触点附近，穿过板内半圆的电流仍是$I$，没有把实际电源变成$2I$或$4I$。

（5）写出四个等效源、汇叠加后的电势。

令$r_A,r_{A^*},r_D,r_{D^*}$分别表示场点$P$到四个点的距离。源势取负的对数、汇势取正的对数，故

$$
\begin{aligned}
V(P)
&=-\frac{I}{\pi\sigma t}\ln\frac{r_A}{\rho_0}
-\frac{I}{\pi\sigma t}\ln\frac{r_{A^*}}{\rho_0}\\
&\quad+\frac{I}{\pi\sigma t}\ln\frac{r_D}{\rho_0}
+\frac{I}{\pi\sigma t}\ln\frac{r_{D^*}}{\rho_0}+V_0\\
&=\frac{I}{\pi\sigma t}
\ln\frac{r_Dr_{D^*}}{r_Ar_{A^*}}+V_0.
\end{aligned}
$$

最后一步使用$\ln a+\ln b=\ln(ab)$，四项中的参考长度恰好抵消。分子、分母都是两个长度的乘积，因此比值无量纲。加法常数$V_0$可任意选取，下面计算$V_B-V_C$时直接消去。

（6）在$B$点计算全部距离，不省略跨边的开方过程。

由图6-3，$B,A,A^*$在同一条水平线上，而$D,D^*$在竖直线上。对$0<\lambda<1$，沿同一直线的距离为

$$
\begin{aligned}
r_A(B)&=|l-\lambda l|=(1-\lambda)l,\\
r_{A^*}(B)&=|\lambda l-(-l)|=(1+\lambda)l.
\end{aligned}
$$

跨两条边的距离则由坐标差平方和决定：

$$
\begin{aligned}
r_D(B)&=\sqrt{(\lambda l-0)^2+(0-l)^2}
=l\sqrt{1+\lambda^2},\\
r_{D^*}(B)&=\sqrt{(\lambda l-0)^2+(0+l)^2}
=l\sqrt{1+\lambda^2}.
\end{aligned}
$$

所以两类距离乘积分别为$l^2(1-\lambda^2)$和$l^2(1+\lambda^2)$。代入电势表达式：

$$
\begin{aligned}
V_B-V_0
&=\frac{I}{\pi\sigma t}
\ln\frac{l^2(1+\lambda^2)}
{(1-\lambda)l(1+\lambda)l}\\
&=\frac{I}{\pi\sigma t}
\ln\frac{1+\lambda^2}{1-\lambda^2}.
\end{aligned}
$$

不能把$r_D(B)$也写成$(1\pm\lambda)l$：它既不是$OB+OD$，也不是$OD-OB$，而是一条连接两条垂直边的斜线段。错误距离会改变最终几何因子，不只是影响图中的标注。

（7）独立计算$C$点并完成第一问直角结果。

$C=(0,\lambda l)$到两个源的距离都为$l\sqrt{1+\lambda^2}$，到$D,D^*$的距离分别为$(1-\lambda)l,(1+\lambda)l$。直接代入，而不只凭对称性猜符号：

$$
\begin{aligned}
V_C-V_0
&=\frac{I}{\pi\sigma t}
\ln\frac{(1-\lambda)l(1+\lambda)l}
{l^2(1+\lambda^2)}\\
&=\frac{I}{\pi\sigma t}
\ln\frac{1-\lambda^2}{1+\lambda^2}\\
&=-\frac{I}{\pi\sigma t}
\ln\frac{1+\lambda^2}{1-\lambda^2}.
\end{aligned}
$$

因此

$$
\begin{aligned}
U&=V_B-V_C
=\frac{2I}{\pi\sigma t}
\ln\frac{1+\lambda^2}{1-\lambda^2},\\
\sigma tU&=\frac{2I}{\pi}
\ln\frac{1+\lambda^2}{1-\lambda^2}.
\end{aligned}
$$

解出电导率，得到

$$
\boxed{\sigma=\frac{2I}{\pi tU}
\ln\frac{1+\lambda^2}{1-\lambda^2}}
\qquad(\omega=\pi/2).
$$

因$0<\lambda<1$，对数为正，与$I>0,U>0$相容。尺度$l$完全消去，并非不需要测量接触位置，而是只需要比例$\lambda=OB/OA=OC/OD$。所有距离同时放大同一倍数时，二维稳恒场的电压比不变。

（8）为圆盘构造候选电势，并核查它的源、汇强度。

圆盘内任一点记为$P$，两电流端在圆周上。候选电势为

$$
V(P)=\frac{I}{\pi\sigma t}
\ln\frac{|P-D|}{|P-A|}+V_0.
$$

它在$A,D$之外满足二维拉普拉斯方程，因为二维$\ln|P-P_0|$在$P\ne P_0$处为调和函数。靠近$A$时，$|P-D|$仍为非零有限量，$V$的奇异项为$-I\ln|P-A|/(\pi\sigma t)$，产生向外的径向场$I/(\pi\sigma t\rho)$。圆周在足够小尺度上近似直线，接触处板内截流角度趋于$\pi$，故输入电流为

$$
\lim_{\rho\to0}
\sigma t\frac{I}{\pi\sigma t\rho}\,\pi\rho=I.
$$

靠近$D$时对数奇异项符号相反，抽出同样大小的$I$。这一步检查的是实际端子电流，而不是只因形式好看便采用候选函数。有限曲率不改变上述局部极限，但候选电势仍须在整个圆周上通过下一步边界检验。

（9）证明圆盘候选电势的法向电流处处为零。

以圆心为坐标原点，令$\boldsymbol p$为圆周上一处非接触点的位置向量，$\boldsymbol a$为圆周上任一接触点的位置向量。两者满足$|\boldsymbol p|=|\boldsymbol a|=r$，单位外法向为$\boldsymbol n=\boldsymbol p/r$。先求一个对数项的法向导数：

$$
\begin{aligned}
\frac{\partial}{\partial n}\ln|\boldsymbol p-\boldsymbol a|
&=\frac{(\boldsymbol p-\boldsymbol a)\cdot\boldsymbol n}
{|\boldsymbol p-\boldsymbol a|^2}\\
&=\frac{r^2-\boldsymbol p\cdot\boldsymbol a}
{r\,[2r^2-2\boldsymbol p\cdot\boldsymbol a]}\\
&=\frac{1}{2r}.
\end{aligned}
$$

第二行分别使用$\boldsymbol n=\boldsymbol p/r$和距离平方展开；第三行在非接触点约去非零因子$r^2-\boldsymbol p\cdot\boldsymbol a$。对$A,D$得到的结果相同，候选电势中两项符号相反，所以

$$
\frac{\partial V}{\partial n}
=\frac{I}{\pi\sigma t}
\left(\frac1{2r}-\frac1{2r}\right)=0.
$$

因此候选函数同时满足内部无源方程、圆周绝缘条件以及正确的输入和输出电流。只差任意常数的电势不会改变$U$，由此可用它计算圆盘的测量结果。

（10）把圆心角逐一转成弦长，再求圆盘的电压。

图6-4取$A$在右端、$D$在左端，$B,C$沿上半圆依次排列。三个相邻圆心角都是$\pi/3$，故$A,D$相隔$\pi$，$B,D$及$A,C$相隔$2\pi/3$。弦长公式为$|PQ|=2r\sin(\angle POQ/2)$。

![图6-4 圆盘四端测量的圆心角与实际弦长。](../figures/disk-06.png){width=62%}

逐项计算：

$$
\begin{aligned}
|BA|=|CD|&=2r\sin\frac\pi6=r,\\
|BD|=|CA|&=2r\sin\frac\pi3=\sqrt3r.
\end{aligned}
$$

代入的必须是场点到电流端的距离，不能把$BC$本身的长度代入源势或汇势。先求两点电势，再相减：

$$
\begin{aligned}
V_B-V_0
&=\frac{I}{\pi\sigma t}\ln\frac{|BD|}{|BA|}
=\frac{I}{\pi\sigma t}\ln\sqrt3,\\
V_C-V_0
&=\frac{I}{\pi\sigma t}\ln\frac{|CD|}{|CA|}
=-\frac{I}{\pi\sigma t}\ln\sqrt3,\\
U&=\frac{2I}{\pi\sigma t}\ln\sqrt3
=\frac{I\ln3}{\pi\sigma t}.
\end{aligned}
$$

这里$2\ln\sqrt3=\ln3$，所以第二问结果也可用两种等价形式写出：

$$
\boxed{\sigma
=\frac{I\ln3}{\pi tU}
=\frac{2I\ln\sqrt3}{\pi tU}}.
$$

半径$r$在弦长比中消去，但板厚$t$仍保留。这是二维几何的尺度性质，不是把圆盘当成零厚度后仍有有限体电导率。

（11）给出一般角部夹角的公式，区分直角与直边。

设金属板局部占极角$0<\varphi<\omega$的楔形，沿$\varphi=0$边取$A$的距离为$l$、$B$为$\lambda l$；沿$\varphi=\omega$边取$D$为$l$、$C$为$\lambda l$。引入复坐标$z=\rho e^{i\varphi}$，令

$$
p=\frac\pi\omega,\qquad
w=\left(\frac zl\right)^p
=\left(\frac\rho l\right)^p e^{ip\varphi}.
$$

该变换把角度区间$(0,\omega)$变成$(0,\pi)$，即把楔形变成上半平面。$z/l$无量纲，避免对有单位的长度直接取任意实数幂。变换在角点之外保持局部夹角；电势沿法线的梯度和沿边界的长度分别按互逆比例变化，故接触处的总电流不变。

![图6-5 楔形角部到上半平面的坐标映射与接触点对应。](../figures/map-06.png){width=88%}

由图6-5中的坐标对应，$A\mapsto1$，$D\mapsto-1$；令$s=\lambda^p$，则$B\mapsto s$、$C\mapsto-s$。上半平面中源、汇在同一直线上，其电势为

$$
V(w)=\frac{I}{\pi\sigma t}
\ln\frac{|w+1|}{|w-1|}+V_0.
$$

因此

$$
\begin{aligned}
V_B-V_0&=\frac{I}{\pi\sigma t}\ln\frac{1+s}{1-s},\\
V_C-V_0&=-\frac{I}{\pi\sigma t}\ln\frac{1+s}{1-s},\\
U&=\frac{2I}{\pi\sigma t}\ln\frac{1+s}{1-s}.
\end{aligned}
$$

把$s=\lambda^{\pi/\omega}$代回并解出电导率：

$$
\boxed{\sigma=\frac{2I}{\pi tU}
\ln\frac{1+\lambda^{\pi/\omega}}
{1-\lambda^{\pi/\omega}}}.
$$

当$\omega=\pi/2$时，$p=2$，恢复第一问直角结果；当$\omega=\pi$时，$p=1$，才得到含$(1+\lambda)/(1-\lambda)$的直边结果。两者的差别来自真实夹角，不是两种等价代数化简。本问已经明确为直角，因此主解取$\omega=\pi/2$；若将实际夹角改变为其他值，就应保留对应的$\omega$，不能沿用直角几何因子。

（12）检查单位、极限与适用条件。

结果中的对数及$\pi$无量纲，而$I/(tU)$的单位为$\mathrm{A/(m\,V)}=\mathrm{S/m}$，正是体电导率。对于固定$\sigma,t,I$，第一问直角电压在$\lambda\to0$时可由对数展开检查：

$$
\begin{aligned}
\ln\frac{1+\lambda^2}{1-\lambda^2}
&=\ln(1+\lambda^2)-\ln(1-\lambda^2)\\
&=\left(\lambda^2-\frac{\lambda^4}{2}
+\frac{\lambda^6}{3}+\cdots\right)
-\left(-\lambda^2-\frac{\lambda^4}{2}
-\frac{\lambda^6}{3}+\cdots\right)\\
&=2\lambda^2+\frac{2\lambda^6}{3}+\cdots,\\
U&=\frac{4I}{\pi\sigma t}\lambda^2
+O(\lambda^6).
\end{aligned}
$$

$B,C$同时靠近角点时电势差趋于零，并且直角情形是二阶小量，不是一阶小量。一般夹角的领先项为$U\sim4I\lambda^{\pi/\omega}/(\pi\sigma t)$。当$\lambda\to1^-$时，测量点分别趋向源、汇接触点，理想点接触电势的对数奇异使$U$增大；真实电极有有限尺寸，不能把发散当成无限可用的实验增益。

电压表应近似开路，金属厚度与接触尺寸应远小于相关接触间距，电导率及厚度在板内近似均匀。角部公式还要求其他板边足够远；若有限边界离接触点不远，则必须重新解其边界问题，不能仍把无限楔形公式当成严格结果。圆盘公式已考虑整个圆周，不需要再作“大圆盘”近似。

（13）用具体数据复核几何因子与数值计算。

取$I=0.010\,\mathrm A$、$t=1.00\times10^{-4}\,\mathrm m$、$U=1.00\times10^{-3}\,\mathrm V$。对直角板取$\lambda=0.500$，则$\lambda^2=0.250$，对数内的比值为$(1.250)/(0.750)=5/3$。保留未舍入中间值：

$$
\begin{aligned}
\sigma_{\rm corner}
&=\frac{0.020}{\pi(1.00\times10^{-4})
(1.00\times10^{-3})}\ln\frac53\\
&\approx6.3661977\times10^4\times0.5108256\\
&\approx3.2520\times10^4\,\mathrm{S/m}.
\end{aligned}
$$

圆盘对应同一组$I,t,U$时，

$$
\begin{aligned}
\sigma_{\rm disk}
&=\frac{0.010\ln3}
{\pi(1.00\times10^{-4})(1.00\times10^{-3})}\\
&\approx3.1830989\times10^4\times1.0986123\\
&\approx3.4970\times10^4\,\mathrm{S/m}.
\end{aligned}
$$

同样的电流与电压并不保证两个不同形状样品有相同电导率，必须带入各自几何因子。反过来，若两种样品都取$\sigma=1.00\times10^6\,\mathrm{S/m}$、厚度及电流不变，则直角板应测得$32.520\,\mu\mathrm V$，圆盘应测得$34.970\,\mu\mathrm V$。这组反算能检查$\sigma$是分母还是分子，以及是否误把$\ln\sqrt3$当成$\ln3$后又多乘一次二。

## 六、关键洞察

四端法把电流引线与测量引线分开，其目的不是消除板内的几何影响，而是尽量避免电压引线接触电阻承载大电流后产生附加压降。即使电压表近似不取电流，$U/I$依然取决于接触位置和板边条件，必须经过几何因子才能换算为$1/(\sigma t)$。

对数势的系数可以仅由接触处的电流通量确定。某点接触在局部可导电角度为$\Theta$时，截流面积为$\Theta\rho t$，因此奇异势的系数为$I/(\Theta\sigma t)$。内点对应$\Theta=2\pi$，光滑边缘点对应$\Theta=\pi$。本题的$A,D$不是角点$O$，即使样品为直角板，它们的局部可导电角度仍为$\pi$，不能错误地用$\pi/2$再加倍。

解的可靠性来自“方程、边界、通量”三项同时满足。以圆盘为例，候选函数内部调和还不够；必须证明圆周法向导数为零，并确认源端输入$I$、汇端抽出$I$。若两个解均满足相同条件，其差$f$在无源区调和且边界法向导数为零。用分部积分可得

$$
\begin{aligned}
\int |\nabla f|^2\,dS
&=\oint f\frac{\partial f}{\partial n}\,ds
-\int f\nabla^2f\,dS\\
&=0.
\end{aligned}
$$

比较时可先剔除接触点附近的小圆弧，并让具有相同奇异强度的差的弧边贡献趋于零。积分非负且总值为零，所以$\nabla f=0$，两解只差常数。这解释了为什么符合全部边界条件的候选对数势已经确定了被测电压。

对于圆盘上任意依次排列的四个接触点，直接由同一候选势相减可得

$$
\begin{aligned}
U
&=\frac{I}{\pi\sigma t}
\left(\ln\frac{|BD|}{|BA|}
-\ln\frac{|CD|}{|CA|}\right)\\
&=\frac{I}{\pi\sigma t}
\ln\frac{|BD|\,|CA|}{|BA|\,|CD|}.
\end{aligned}
$$

因此四端电压由四条弦长的无量纲组合决定，不由圆盘面积或周长单独决定。整块板面在两条互易测量中的积分
$\int\sigma t\nabla V_1\cdot\nabla V_2\,dS$
交换$V_1,V_2$后不变。若第一组从$A$输入$I_1$、从$D$引出，第二组从$B$输入$I_2$、从$C$引出，则边界项分别为
$I_1[V_2(A)-V_2(D)]$和$I_2[V_1(B)-V_1(C)]$。所以

$$
\frac{V_1(B)-V_1(C)}{I_1}
=\frac{V_2(A)-V_2(D)}{I_2}.
$$

这是均匀线性无磁场导电模型的互易检查。它不是交换任意两根线后电压都不变，而是电流端子对与电压端子对成对交换，并保留相同正负次序。

直角结果还可不借助四镜像而通过$w=(z/l)^2$独立得到。在板边上，$B$映到$\lambda^2$、$C$映到$-\lambda^2$，所以直角中的平方幂来自角度加倍。有限网格电阻网络也提供不同于解析公式的数值检查：逐节点解电流平衡，在板边注入和抽出单位电流。固定远边距$16l$、加密网格后，$\lambda=1/2$的$U/(IR_{\square})$趋向$0.325202$；不能把有限网格最后的微小误差称作无限板公式的物理误差。

## 七、易错点

把电流截面写成圆盘面积$\pi\rho^2$，会把二维导电误写成三维点源导电。正确截流面是圆周或半圆弧沿厚度展开的侧面积，$\rho$只出现一次。忽略$t$则得到面电导，不能再把答案单位标为$\mathrm{S/m}$。

边缘点的等效源强已为$2I$，叠加后不再另乘“镜像二倍”。直角图中虽然有四个全平面等效点，但实际第一象限中只接入一个$I$源和一个$I$汇；全平面的扩展电流不是实际电源读数。

跨边距离误用$l\pm\lambda l$是本题实质性几何错误。直角图中$BD$需由勾股定理得$l\sqrt{1+\lambda^2}$；只有同一直线的两点才可直接把到角点的距离相加或相减。另一方面，真实角度为$\pi$时才使用含$\lambda$的直边因子，不能用一张透视图的纸面角度代替实际角度。

对数势的正负号可用靠近源端的极限核查：正电流源附近$V\to+\infty$，汇附近$V\to-\infty$，应有$V\propto\ln(r_D/r_A)$。若写反，正端接$B$时会错误得到负的$U$及负电导率。倒置电压表极性时$U$变号，必须同时调整电压定义，不能把负读数直接代入正读数公式。

圆盘公式中的距离是弦长，而非沿圆周的弧长。$\angle AOB=\pi/3$对应弦长$r$，不是$\pi r/3$。两问尺度消去也不表示任意有限板都可忽略边缘；角部无限模型和完整圆盘模型的成立理由不同。

当$B$无限接近$A$时，点接触势的发散提示接触模型失效，不是可以无代价提高测量灵敏度。真实接触的面积、边缘电流拥挤、样品发热及电压表分流都可能改变结果，应先明确它们可忽略的尺度条件。

## 八、课堂讲解建议

课堂先让学生在一张纸板上指出“沿板面流动”与“穿过厚度方向截流面”的区别。板书画出半圆弧，并沿弧把厚度$t$展开成侧面，要求学生先写$I=J\pi\rho t$，再写$E=J/\sigma$。这一步不急于给出对数积分，以免学生只记住一个二倍系数而不知道从哪里来。

教师随后保留图6-3，只让学生填写$B$到四个点的距离。沿轴的两个距离与跨轴的两个距离应分别列在两行；可以取$l=1,\lambda=1/2$直接比较$1/2,3/2,\sqrt5/2$。板书把错误的“跨边相加”与正确勾股关系并列，错误在求电势之前就能被发现。

圆盘部分可以先让学生猜测$V\propto\ln(|PD|/|PA|)$，再提出“为什么圆周不会漏电”的问题。教师完整展示两个对数项的法向导数都为$1/(2r)$，最后相减为零；这样候选函数有了边界依据，而不是靠图像直觉被默认正确。

一般夹角映射适合在核心直角计算已经掌握后讲解。课堂应明确复坐标只是二维板面的数学记号，不是第三个物理方向。先把角度乘以$p$变成$\pi$，再追踪四个接触点，学生即可看到$\lambda^2$的来源。最后用电流反向和互易测量作为结果自检，不能只核对最后一个小数。

## 九、变式训练

变式一：直角板与圆盘由同一种金属制成，厚度相同，测量电流也相同。直角板取$\lambda=1/2$。求两者电压比；若圆盘测得$70.0\,\mu\mathrm V$，求直角板的电压。

完整解答：两者$\sigma,t,I$相同，公共因子$I/(\pi\sigma t)$约去。直角板电压含$2\ln(5/3)$，圆盘电压含$\ln3$，所以

$$
\begin{aligned}
\frac{U_{\rm corner}}{U_{\rm disk}}
&=\frac{2\ln(5/3)}{\ln3}
\approx0.929947,\\
U_{\rm corner}
&\approx70.0\times0.929947\,\mu\mathrm V
\approx65.1\,\mu\mathrm V.
\end{aligned}
$$

较小电压来自几何因子较小，而不是同一材料的电导率改变。若两块厚度不同，应把厚度因子保留，不能仍直接使用这个比值。

变式二：一般楔形板取$\lambda=1/2$，已知$R_{\square}=1.00\,\Omega$，输入$I=10.0\,\mathrm{mA}$，测得$U=(2I/\pi)\ln(9/7)$。求实际夹角$\omega$，并判断其是否为直角。

完整解答：一般公式给出

$$
\begin{aligned}
\ln\frac{1+s}{1-s}&=\ln\frac97,\qquad s=\lambda^p,\\
\frac{1+s}{1-s}&=\frac97,\\
7+7s&=9-9s,\\
16s&=2,\qquad s=\frac18,\\
\left(\frac12\right)^p&=\frac18
=\left(\frac12\right)^3.
\end{aligned}
$$

因为固定底数$1/2$的实数幂是严格单调函数，$p=3$是唯一解。由$p=\pi/\omega$得$\omega=\pi/3$，为$60^\circ$，不是直角。电压数值为$U\approx1.600\,\mathrm{mV}$。若实际接触比$\lambda$未知，则单次电压不能同时唯一确定$\lambda$和$\omega$。

变式三：圆盘四个接触点等角间隔排列，但相邻圆心角改为$\varphi$，且$0<\varphi<2\pi/3$。$A\to D$通电、$B,C$测压。求几何因子，并计算$\varphi=\pi/2$的结果。

完整解答：四点圆心角可依次取$0,\varphi,2\varphi,3\varphi$。源到$B$、汇到$C$的弦长均为$2r\sin(\varphi/2)$；汇到$B$、源到$C$的弦长均为$2r\sin\varphi$。在所给范围内相关正弦为正，可直接使用弦长比：

$$
\begin{aligned}
U
&=\frac{I}{\pi\sigma t}
\ln\frac{[2r\sin\varphi]^2}
{[2r\sin(\varphi/2)]^2}\\
&=\frac{I}{\pi\sigma t}
\ln\left[\frac{\sin\varphi}{\sin(\varphi/2)}\right]^2\\
&=\frac{I}{\pi\sigma t}
\ln\left[4\cos^2\frac\varphi2\right].
\end{aligned}
$$

第三行使用$\sin\varphi=2\sin(\varphi/2)\cos(\varphi/2)$。当$\varphi=\pi/2$时，$4\cos^2(\pi/4)=2$，因此

$$
U=\frac{I\ln2}{\pi\sigma t},
\qquad
\sigma=\frac{I\ln2}{\pi tU}.
$$

当$\varphi\to2\pi/3$时，$A,D$即将绕圆周重合，几何因子趋于零，此端点不满足四个互不重合电极的条件，不应纳入正式测量构型。本题$\varphi=\pi/3$时则恢复$\ln3$。

变式四：直角板的接触比例存在小误差$\delta\lambda$，$I,t,U$的误差暂忽略。求电导率对$\lambda$的相对灵敏度，并估计$\lambda=1/2$、$\delta\lambda=0.005$造成的相对误差。

完整解答：令$f(\lambda)=\ln[(1+\lambda^2)/(1-\lambda^2)]$，则$\sigma=Cf(\lambda)$，其中$C=2I/(\pi tU)$与$\lambda$无关。先分别求两个对数的导数：

$$
\begin{aligned}
f'(\lambda)
&=\frac{2\lambda}{1+\lambda^2}
+\frac{2\lambda}{1-\lambda^2}\\
&=\frac{2\lambda[(1-\lambda^2)+(1+\lambda^2)]}
{(1+\lambda^2)(1-\lambda^2)}\\
&=\frac{4\lambda}{1-\lambda^4}.
\end{aligned}
$$

在线性误差范围内，

$$
\begin{aligned}
\frac{\delta\sigma}{\sigma}
&\simeq\frac{f'(\lambda)}{f(\lambda)}\,\delta\lambda\\
&=\frac{4\lambda}
{(1-\lambda^4)\ln[(1+\lambda^2)/(1-\lambda^2)]}
\,\delta\lambda.
\end{aligned}
$$

代入$\lambda=1/2$时，$1-\lambda^4=15/16$、$f=\ln(5/3)$，于是

$$
\frac{\delta\sigma}{\sigma}
\simeq\frac{2}{(15/16)\ln(5/3)}\times0.005
\approx0.0209.
$$

即接触比例的绝对误差$0.005$可导致约$2.09\%$的电导率误差，正的$\delta\lambda$使反算电导率偏大。这是固定测量读数下的参数误差传播，不是实际移动电极而仍强行保持$U$不变的物理过程。若还包含独立的$I,t,U$微小系统偏差，一阶关系应补成$\delta\sigma/\sigma\simeq\delta I/I-\delta t/t-\delta U/U+[f'/f]\delta\lambda$。

<!-- question-complete -->
