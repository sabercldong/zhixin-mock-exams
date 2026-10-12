# 第 8 题

总电荷为 $Q$ 的均匀带电实心球，半径为 $R$，球心在原点。沿 $+z$ 方向挖去一个直径为 $R$ 的小球，小球与大球内切于大球顶部。小球半径为 $R/2$，球心位于 $z=R/2$。将被挖去部分的电荷集中成点电荷 $q$，放在该空腔中心。

（a）求 $q$ 的大小。

（b）求有点电荷 $q$ 时，$x$ 轴上的电场强度大小分布。

（c）移走点电荷 $q$，只留下带球形空腔的均匀带电体，求 $z$ 轴上的电场分布。

（d）继续采用无 $q$ 的情形。在 $xz$ 平面内，点 $P$ 距原点为 $r\gg R$，从 $+x$ 轴朝 $+z$ 方向量取角度 $\theta$，求电势 $\phi(r,\theta)$，保留相对于主项的一阶 $R/r$ 修正，取无穷远电势为零。

（e）把该电荷分布的远场表示为原点处的等效点电荷 $Q_s$ 和电偶极子 $\boldsymbol p$ 的叠加，求 $Q_s$ 及 $\boldsymbol p$。

（f）求远处 $P$ 点电场的分量及方向，同样保留相对一阶 $R/r$ 修正。

![图 8-1　球形空腔的空间剖视与xz截面；左图保留中心点电荷。](../figures/question-08.png)

## 一、题型定位

均匀球体场的叠加、非同心球形空腔以及多极远场展开。几何上是一个有空腔的三维带电体，不是带孔的二维圆盘。移去体积可以用同密度负球叠加表示，但有、无补回点电荷的两种模型必须分开。

## 二、知识点

高斯定律；均匀实心球的内外电场；球外场等效于球心点电荷；场与势的叠加；球内空腔的均匀场；分段表达与边界连续性；二项式展开；单极矩与偶极矩；极坐标梯度及矢量分量变换。

## 三、物理图像

完整球加一个同密度的负小球，恰好表示挖去小球的电荷分布。小球外，负小球的场等于球心负点电荷的场；若再在球心放回正点电荷，两者在小球外完全相消。空腔内则不能用球外点电荷公式。移走点电荷后，空腔内留下恒定电场，远处还同时存在净电荷场与偏心产生的偶极修正。

## 四、解题入口

记 $a=R/2$，小球球心为 $\boldsymbol a=a\boldsymbol e_z$，库仑常数为 $K=1/(4\pi\varepsilon_0)$。先求被挖去的电量 $q_h$，再分别计算完整球、负小球和补回点电荷的贡献。轴上按相对于两个球面的内外位置分段，远场则从精确电势进行展开。

## 五、解析

（1）几何、密度与电量。

以下用 $Q>0$ 说明方向；若 $Q<0$，所有场、势和偶极矩整体反向，场强大小使用 $|Q|$。完整球的体电荷密度为

$$\rho=\frac{Q}{(4\pi/3)R^3}.$$

小球半径为 $a=R/2$，不是 $R$。其电量为

$$\begin{aligned}
q_h&=\rho\frac{4\pi}{3}a^3\\
&=Q\left(\frac aR\right)^3=\frac Q8.
\end{aligned}$$

所以补回点电荷为

$$\boxed{q=\frac Q8}.$$

移走该点电荷后，剩余带电体总电荷为 $7Q/8$；保留点电荷时，整个系统总电荷仍为 $Q$。

（2）先推导均匀实心球的内外场公式。

以球心为中心取半径 $s$ 的高斯面。若 $s<R$，包围电量为 $Q s^3/R^3$，由球对称性

$$\begin{aligned}
E\,4\pi s^2&=\frac{Qs^3}{\varepsilon_0R^3},\\
E&=K\frac Q{R^3}s.
\end{aligned}$$

若 $s>R$，包围全部电量，得到 $E=KQ/s^2$。写成矢量：

$$\boxed{\boldsymbol E_{\rm full}(\boldsymbol r)=
\begin{cases}
KQ\boldsymbol r/R^3,&|\boldsymbol r|\leq R,\\
KQ\boldsymbol r/|\boldsymbol r|^3,&|\boldsymbol r|\geq R.
\end{cases}}$$

两式在球面连续。内场线性增长来自包围电量随 $s^3$ 增长，并不是把全部电荷放在球心后仍可向球内延用反平方公式。

（3）用负小球表示被挖去体积。

图 8-2 将完整正球、偏心负球以及可选的补回点电荷分开。负小球电量为 $-Q/8$，球心为 $\boldsymbol a$，密度为 $-\rho$。

![图 8-2　完整正球、偏心负球及中心补回点电荷的叠加。](../figures/superposition-08.png)

设 $\boldsymbol u=\boldsymbol r-\boldsymbol a$。负小球场为

$$\boldsymbol E_h=
\begin{cases}
-K(Q/8)\boldsymbol u/a^3,&|\boldsymbol u|\leq a,\\
-K(Q/8)\boldsymbol u/|\boldsymbol u|^3,&|\boldsymbol u|\geq a.
\end{cases}$$

因 $a^3=R^3/8$，其内场可简化为

$$\boldsymbol E_h=-KQ\frac{\boldsymbol r-\boldsymbol a}{R^3}.$$

有点电荷时再加

$$\boldsymbol E_q=K\frac Q8
\frac{\boldsymbol r-\boldsymbol a}{|\boldsymbol r-\boldsymbol a|^3}.$$

这最后一式在点电荷处奇异，不能将它写成小球内的线性场。

（4）$x$ 轴全部位于小球外或其边界。

$x$ 轴上 $\boldsymbol r=(x,0,0)$，距空腔球心的距离为

$$|\boldsymbol r-\boldsymbol a|=\sqrt{x^2+a^2}\geq a.$$

只有 $x=0$ 时恰在空腔下端边界，其余点均在小球外。因此小球负场和补回点电荷正场在整个 $x$ 轴相消：

$$\boldsymbol E_h+\boldsymbol E_q=0.$$

这里可以使用球外等效，并不是由于它们“总电量相反所以任何地方都相消”；空腔内部一般并不相消。

（5）有 $q$ 时的 $x$ 轴场强大小。

剩下的就是完整大球场：

$$E_x=
\begin{cases}
KQx/R^3,&|x|\leq R,\\
KQx/|x|^3,&|x|\geq R,
\end{cases}
\qquad E_y=E_z=0.$$

题目问大小，故

$$\boxed{|\boldsymbol E(x)|=
\begin{cases}
K|Q|\,|x|/R^3,&|x|\leq R,\\
K|Q|/x^2,&|x|\geq R.
\end{cases}}$$

$x=0$ 的总场为零。单个负球和点电荷在原点都有非零 $z$ 向场，但相加后抵消；不能只检查 $x$ 分量而漏掉这项核对。

（6）移走 $q$ 后，先分清 $z$ 轴的四个区域。

沿 $z$ 轴，大球内部为 $-R\leq z\leq R$。空腔范围为

$$|z-a|\leq a\quad\Longleftrightarrow\quad0\leq z\leq R.$$

因此需要分成 $z<-R$、$-R\leq z<0$、$0\leq z\leq R$、$z>R$。图 8-3 用带符号的 $E_z$ 表示方向，曲线不把负场强错误地画成不存在。

![图 8-3　移去点电荷后z轴上的分段场强；空腔内部为恒定场。](../figures/axis-08.png)

（7）空腔内部场为常量。

在 $0\leq z\leq R$，同时使用两个球的内场：

$$\begin{aligned}
E_z
&=KQ\frac z{R^3}
-KQ\frac{z-a}{R^3}\\
&=KQ\frac a{R^3}
=\frac{KQ}{2R^2}.
\end{aligned}$$

故

$$\boxed{\boldsymbol E_{\rm cavity}
=\frac{KQ}{2R^2}\boldsymbol e_z}.$$

事实上，该常量对整个三维空腔都成立，因为矢量相减为 $KQ\boldsymbol a/R^3$。这是均匀带电绝缘体的空腔，不是静电平衡导体的空腔，不能套用“导体内部电场为零”。

（8）大球内、空腔外的负半轴。

对于 $-R\leq z<0$，大球用内场，负小球用外场。因 $z-a<0$，

$$\begin{aligned}
E_{hz}
&=-K\frac Q8\frac{z-a}{|z-a|^3}\\
&=+\frac{KQ}{8(z-a)^2}.
\end{aligned}$$

于是

$$\boxed{E_z=KQ\left[\frac z{R^3}
+\frac1{8(z-R/2)^2}\right],\quad-R\leq z<0}.$$

第一项指向负 $z$，第二项指向正 $z$，必须代数相加，不能把两项大小直接相加。

（9）大球外的两侧。

$z>R$ 时，两球都使用外场，且 $z-a>0$：

$$E_z=KQ\left[\frac1{z^2}
-\frac1{8(z-R/2)^2}\right].$$

$z<-R$ 时，两球也都使用外场，但完整正球指向负 $z$，负小球指向正 $z$：

$$E_z=KQ\left[-\frac1{z^2}
+\frac1{8(z-R/2)^2}\right].$$

汇总无 $q$ 的完整答案：

$$\boxed{E_z(z)=KQ
\begin{cases}
-\dfrac1{z^2}+\dfrac1{8(z-R/2)^2},&z<-R,\\[4pt]
\dfrac z{R^3}+\dfrac1{8(z-R/2)^2},&-R\leq z<0,\\[4pt]
\dfrac1{2R^2},&0\leq z\leq R,\\[4pt]
\dfrac1{z^2}-\dfrac1{8(z-R/2)^2},&z>R.
\end{cases}}$$

轴对称性保证 $E_x=E_y=0$。若需大小，取 $|E_z|$，不改变上述方向信息。

（10）逐个检查边界与零场点。

在 $z=0$，负半轴式给出 $KQ/[8(R/2)^2]=KQ/(2R^2)$，与空腔场相接。$z=R$ 时，球外式给出

$$KQ\left[\frac1{R^2}-\frac1{8(R/2)^2}\right]
=\frac{KQ}{2R^2}.$$

在 $z=-R$，内外大球公式共同给出 $-17KQ/(18R^2)$。全部边界场连续，符合没有单独面电荷层的均匀体电荷模型。

负半轴大球内还有一处 $E_z=0$。令 $u=z/R$：

$$u+\frac1{8(u-1/2)^2}=0,\qquad-1<u<0.$$

函数导数为 $1-1/[4(u-1/2)^3]>0$，且在 $u=-1$ 为负、在 $u=0$ 为正，所以恰有一个物理解。用二分法逐次保留异号两端区间，可得 $u\approx-0.232786$，即 $z\approx-0.232786R$。把此数代回原方程，两项相抵。其存在解释了图中场方向翻转，而不是全负半轴始终向左。

（11）从精确电势开始远场展开。

无 $q$ 时，球外点距小球球心也大于 $a$，两个球的电势均等效于球心点电荷。图 8-4 中

$$\boldsymbol r=(r\cos\theta,0,r\sin\theta),\qquad
|\boldsymbol r-\boldsymbol a|
=\sqrt{r^2+a^2-2ra\sin\theta}.$$

![图 8-4　远场观测点、角度定义、负z向偶极矩及场的局部方向。](../figures/farfield-08.png)

因此精确球外电势为

$$\boxed{\phi=K\left[
\frac Qr-\frac{Q/8}{\sqrt{r^2+a^2-2ra\sin\theta}}\right]}.$$

$\theta$ 从 $+x$ 轴朝 $+z$ 轴量取，所以偏心项含 $\sin\theta$；若从 $+z$ 轴量角才会出现 $\cos\theta$，不能不改图就更换。

（12）保留相对一阶小量。

令 $\epsilon=a/r=R/(2r)\ll1$：

$$\frac1{|\boldsymbol r-\boldsymbol a|}
=\frac1r(1-2\epsilon\sin\theta+\epsilon^2)^{-1/2}.$$

使用二项式展开 $(1+w)^{-1/2}=1-w/2+O(w^2)$，其中 $w=-2\epsilon\sin\theta+\epsilon^2$，得

$$\frac1{|\boldsymbol r-\boldsymbol a|}
=\frac1r\left[1+\epsilon\sin\theta+O(\epsilon^2)\right].$$

代回：

$$\begin{aligned}
\phi
&=\frac{KQ}{r}
-\frac{KQ}{8r}\left[1+\frac{R}{2r}\sin\theta
+O\!\left(\frac{R^2}{r^2}\right)\right]\\
&=\boxed{\frac{7KQ}{8r}
-\frac{KQR}{16r^2}\sin\theta
+O\!\left(\frac{K|Q|R^2}{r^3}\right)}.
\end{aligned}$$

一阶指相对于 $1/r$ 主项的一阶 $R/r$ 修正，因此必须保留 $1/r^2$ 项，不是只留下电势中的一次幂符号。

（13）识别等效单极矩与偶极矩。

净电荷为

$$\boxed{Q_s=\frac{7Q}{8}}.$$

关于原点的偶极矩定义为 $\boldsymbol p=\int\boldsymbol r\,\mathrm dq$。完整均匀球关于原点的偶极矩因对称性为零；负小球的电荷质心在 $\boldsymbol a$，所以

$$\boxed{\boldsymbol p=-\frac Q8\boldsymbol a
=-\frac{QR}{16}\boldsymbol e_z}.$$

其大小为 $|Q|R/16$，对于 $Q>0$ 方向为负 $z$。偶极电势 $K(\boldsymbol p\cdot\boldsymbol e_r)/r^2$ 正好等于前一步的 $-KQR\sin\theta/(16r^2)$。

这是远场截断表示，不表示整个空间的电场都能由一个点电荷和一个点偶极子精确取代。有限体积在近场、空腔和材料内部的场仍需前面分段公式。

（14）用极坐标梯度求场的径向与角向分量。

在 $xz$ 平面定义

$$\boldsymbol e_r=(\cos\theta,0,\sin\theta),\qquad
\boldsymbol e_\theta=(-\sin\theta,0,\cos\theta).$$

场与势关系为

$$E_r=-\frac{\partial\phi}{\partial r},\qquad
E_\theta=-\frac1r\frac{\partial\phi}{\partial\theta}.$$

对保留的电势逐项求导：

$$\begin{aligned}
E_r&=\frac{7KQ}{8r^2}
-\frac{KQR}{8r^3}\sin\theta
+O\!\left(\frac{K|Q|R^2}{r^4}\right),\\
E_\theta&=\frac{KQR}{16r^3}\cos\theta
+O\!\left(\frac{K|Q|R^2}{r^4}\right).
\end{aligned}$$

径向偶极项的系数增加为电势系数的两倍，角向项则多一个 $1/r$。这两处不能凭“方向差不多”省略。

（15）转成题设直角坐标分量。

由 $\boldsymbol E=E_r\boldsymbol e_r+E_\theta\boldsymbol e_\theta$：

$$E_x=E_r\cos\theta-E_\theta\sin\theta,\qquad
E_z=E_r\sin\theta+E_\theta\cos\theta.$$

代入并合并：

$$\boxed{\begin{aligned}
E_x&=K\left[
\frac{7Q}{8r^2}\cos\theta
-\frac{3QR}{16r^3}\sin\theta\cos\theta\right]
+O\!\left(\frac{K|Q|R^2}{r^4}\right),\\
E_z&=K\left[
\frac{7Q}{8r^2}\sin\theta
+\frac{QR}{16r^3}(1-3\sin^2\theta)\right]
+O\!\left(\frac{K|Q|R^2}{r^4}\right),\\
E_y&=0.
\end{aligned}}$$

其中 $E_z$ 的 $1-3\sin^2\theta$ 来自 $\cos^2\theta-2\sin^2\theta$。写明这一恒等变形，可避免把极坐标分量直接当作直角坐标分量。

（16）场强大小与方向的一阶修正。

对于 $Q>0$，主场径向向外，角向分量相对主场为一阶小量，其平方只影响二阶的大小。因此

$$|\boldsymbol E|
=\frac{7KQ}{8r^2}
\left[1-\frac{R}{7r}\sin\theta
+O\!\left(\frac{R^2}{r^2}\right)\right].$$

场相对于径向偏转的有符号小角 $\delta$ 满足

$$\begin{aligned}
\tan\delta&=\frac{E_\theta}{E_r},\\
\delta&=\frac{R}{14r}\cos\theta
+O\!\left(\frac{R^2}{r^2}\right).
\end{aligned}$$

$\delta>0$ 表示朝 $\theta$ 增大的方向偏转。在 $+x$ 轴远处，场有小的正 $z$ 分量；在正负 $z$ 轴，$\cos\theta=0$，场仍沿轴向。

（17）远场、量纲与两条路线的核对。

电势主项为净电荷 $7Q/8$ 的势，偶极矩量纲为电荷乘长度，偶极场比单极场小约 $R/r$。沿正 $z$ 轴，精确球外式展开为

$$\begin{aligned}
E_z
&=\frac{KQ}{r^2}
-\frac{KQ}{8r^2}\left(1-\frac{R}{2r}\right)^{-2}\\
&=\frac{7KQ}{8r^2}-\frac{KQR}{8r^3}
+O\!\left(\frac{K|Q|R^2}{r^4}\right),
\end{aligned}$$

与极坐标导数在 $\theta=\pi/2$ 的结果一致。若保留点电荷 $q$，整个球外负小球与该点电荷完全相消，远场应恢复净电荷 $Q$、零偶极矩；这再次核对有、无 $q$ 的区分。

## 六、关键洞察

球外等效是空间条件，不是仅由总电量决定的全空间等效。$x$ 轴恰好全部在空腔小球外，所以补回点电荷能恢复整条 $x$ 轴的完整球场；空腔内部不具备这个条件。

非同心同密度球相减，在共同内部区域中线性场的变量项抵消，留下与偏心矢量成正比的常量。这比只沿轴计算更本质，能直接推广到任意偏心球形空腔。

另一条远场路线是直接用点偶极场：

$$\boldsymbol E_{\rm dip}
=\frac K{r^3}\left[3(\boldsymbol p\cdot\boldsymbol e_r)
\boldsymbol e_r-\boldsymbol p\right].$$

代入 $\boldsymbol p=-QR\boldsymbol e_z/16$，得到径向 $-KQR\sin\theta/(8r^3)$、角向 $KQR\cos\theta/(16r^3)$，与求势梯度的路线逐项相同。由于净电荷非零，偶极矩依赖原点选择；本题统一以大球球心为原点，不能另移原点后仍使用同一个 $\boldsymbol p$。

## 七、易错点

小球直径是 $R$，半径是 $R/2$，电量比例是体积的 $1/8$，不是面积的 $1/4$。负小球的内场随相对球心位移线性变化，不能在空腔内使用反平方场。没有点电荷时空腔不含奇点，更不能把 $z=R/2$ 错写成发散点。

$\theta$ 从 $x$ 轴量起，偏心项用 $\sin\theta$；场方向需要角向分量，不能只求径向大小。无 $q$ 的净电荷是 $7Q/8$，不是 $Q$，而偶极矩向负 $z$。轴上分段场应带符号，最后求大小时才取绝对值。

## 八、课堂讲解建议

先用空间剖视和截面图确认小球半径、球心、两个相切点，再让学生在x轴和z轴分别标出哪些点属于小球内部。板书把完整球、负小球、可选点电荷三列贡献分开，避免两种模型混算。

讲解远场时先写精确距离，再做二项式展开，随后把单极和偶极项与几何偏心联系起来。课堂用势梯度和偶极场公式互相核对角向符号，并沿正z轴与精确分段式比较，确保图中的角度真正进入方程。

<!-- KEEP_TOGETHER_START -->

## 九、变式训练

变式一：小球半径改为 $a$，球心改为任意偏心矢量 $\boldsymbol d$，要求 $|\boldsymbol d|+a\leq R$。挖去小球后不补回点电荷，求空腔内场、净电荷与关于大球球心的偶极矩。

解：被挖去电量为 $q_h=Q(a/R)^3$。在空腔内部，

$$\begin{aligned}
\boldsymbol E
&=\frac{\rho}{3\varepsilon_0}\boldsymbol r
-\frac{\rho}{3\varepsilon_0}(\boldsymbol r-\boldsymbol d)\\
&=\boxed{\frac{\rho}{3\varepsilon_0}\boldsymbol d
=\frac{KQ}{R^3}\boldsymbol d}.
\end{aligned}$$

净电荷和偶极矩为

$$\boxed{Q_s=Q\left[1-\left(\frac aR\right)^3\right]},\qquad
\boxed{\boldsymbol p=-Q\left(\frac aR\right)^3\boldsymbol d}.$$

所以远场势为 $KQ_s/r+K(\boldsymbol p\cdot\boldsymbol e_r)/r^2$ 加二阶相对小量。若 $\boldsymbol d=0$，空腔内场为零、偶极矩为零；若 $a\to0$，移去电量和远场修正趋零。空腔内恒定场与 $a$ 无显式关系，但适用区域随 $a$ 改变，不能由此误认为挖孔大小完全没有物理影响。

<!-- KEEP_TOGETHER_END -->

变式二：挖去半径$a$、偏心$\boldsymbol d$的小球后，把全部挖去电量集中于小球中心。求净电荷、偶极矩及空腔外的电场。

解：负小球电量$-q_h$与补回点电荷$+q_h$的总量和偶极矩分别抵消，净电荷为$Q$、偶极矩为零。对$|\boldsymbol r-\boldsymbol d|\geq a$，球对称小球场等于中心点电荷场，两者精确抵消，故外部电场恰等于未挖孔的完整大球场。在空腔内抵消不成立，点电荷仍有奇异场；不能由外场相同推出所有位置场相同。

变式三：没有补回点电荷时，把带球形空腔的整个绝缘体在真空中刚性转动，使偏心矢量由$\boldsymbol d$变为$-\boldsymbol d$。求空腔恒定场及远场偶极项的变化。

解：固定均匀电荷密度时，空腔场$\boldsymbol E=KQ\boldsymbol d/R^3$反向，大小不变。偶极矩$\boldsymbol p=-Q(a/R)^3\boldsymbol d$也反向，故同一观察方向上的$K\boldsymbol p\cdot\boldsymbol e_r/r^2$改变符号；单极项由净电量决定，保持不变。观察方向恰与$\boldsymbol d$垂直时偶极项原本为零，不能仅凭该方向判断偶极矩不存在。

变式四：保留本题无点电荷情形，在远处正、负$z$轴的同一距离$r\gg R$测电势。求两电势之差的最低非零阶。

解：净电量为$7Q/8$，偶极矩为$-QR\boldsymbol e_z/16$。两处单极项相等，偶极项分别为$-KQR/(16r^2)$和$+KQR/(16r^2)$，因此$\phi(+r\boldsymbol e_z)-\phi(-r\boldsymbol e_z)=-KQR/(8r^2)+O(KQR^3/r^4)$。二阶四极项在相反方向相同而抵消；若不利用这一奇偶性，写更宽松的误差界也成立。
