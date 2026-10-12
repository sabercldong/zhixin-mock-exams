# 第 5 题

<!-- question-start -->
半径为 $R$ 的导体球以坐标原点为球心，处于静电平衡。令 $k_e=1/(4\pi\varepsilon_0)$，电势零点取无穷远。

（1）在 $A=(5R/2,0,0)$ 和 $B=(0,0,3R/2)$ 各放置一个电荷量为 $Q$ 的点电荷。求导体球感应电荷在 $P=(R/2,R/2,R/2)$ 处产生的电场，并求其电势的大小。球的净电荷或接地状态未另行指定；电势数值应说明所采用的状态条件。

（2）另考虑球被理想电源保持在相对于无穷远的电势 $V$，在 $(0,0,d)$ 放一个点电荷 $Q$，其中 $d>R$。求：a）导体球的总电荷量；b）点电荷所受力；c）该力为零时 $d$ 应满足的条件。

![图 5-1　导体球与外部电荷的空间位置及球内观察点。](../figures/question-05.png)
<!-- question-end -->

## 一、题型定位

导体静电平衡与球形边界的镜像法。第一问观察点在导体内部，必须用总电场为零求感应场；第二问观察点在球外，可用满足边界条件的镜像电荷计算。两问的计算区域不同，不能混用同一个点电荷表达式。

## 二、知识点

Coulomb场的矢量形式；电场与电势的叠加；导体内部零电场及等势条件；接地与孤立中性的区别；球的镜像电荷；外部Dirichlet边值问题的唯一性；电源维持电势时的电荷交换；力平衡与稳定性。

镜像电荷是构造边界解的数学工具，不是球内实际存在的点电荷。解的有效范围必须随边界问题一起指定。

## 三、物理图像

$OP=\sqrt3R/2<R$，故 $P$ 位于导体材料内部。外部两个点电荷分别在球外，虽然它们在 $P$ 处产生非零电场，球面电荷会重新分布，使该处总电场精确抵消。

总电势在导体内为常数，但常数值取决于球的净电荷和接地状态；“电场为零”只能推出电势空间上不变，不能推出电势为零。固定电势 $V$ 时，外部电荷位置变化会导致电源向球输送或从球取走电荷，球的总电荷不再固定。

## 四、解题入口

先算 $P-A$、$P-B$ 及其长度，用 $\boldsymbol E_{\mathrm{ind}}=-\boldsymbol E_{\mathrm{ext}}$ 得到感应场。求感应电势时写 $\Phi_{\mathrm{ind}}=\Phi_{\mathrm{sphere}}-\Phi_{\mathrm{ext}}$，补上决定球电势的条件。

第二问先构造接地球的偏轴镜像，再在球心加入电荷使球面电势升至 $V$。从镜像总电荷得到球的实际总电荷，从镜像在外部点产生的场求力，最后讨论零力条件是否有解。

## 五、解析

（1）判断观察点位置。

由直角坐标的距离公式，
$$OP^2=\left(\frac R2\right)^2+\left(\frac R2\right)^2+\left(\frac R2\right)^2=\frac{3R^2}{4}.$$
所以 $P$ 在导体内，而不是球外。静电平衡时，
$$\boldsymbol E_{\mathrm{tot}}(P)=\boldsymbol E_A(P)+\boldsymbol E_B(P)+\boldsymbol E_{\mathrm{ind}}(P)=0.$$
这里 $A,B$ 的场是外加场；感应场是球面电荷的场，两者都可以单独不为零。图 5-2 展示相互抵消关系，后面直接使用此矢量等式，不用镜像表达式去评价球内点。

![图 5-2　导体内部外加场与感应场的精确抵消。](../figures/inside-05.png)

（2）计算电荷 $A$ 在 $P$ 处的场。

从源电荷指向观察点的位移为
$$\boldsymbol s_A=P-A=R(-2,\tfrac12,\tfrac12).$$
距离及三次方为
$$s_A=\sqrt{4R^2+\frac{R^2}4+\frac{R^2}4}=\frac{3R}{\sqrt2},\qquad
s_A^3=\frac{27R^3}{2\sqrt2}.$$
用矢量Coulomb定律而非只写大小：
$$\begin{aligned}
\boldsymbol E_A(P)&=k_eQ\frac{\boldsymbol s_A}{s_A^3}\\
&=\frac{k_eQ}{R^2}\frac{2\sqrt2}{27}(-2,\tfrac12,\tfrac12)\\
&=\frac{k_eQ}{R^2}\frac{\sqrt2}{27}(-4,1,1).
\end{aligned}$$
$x$ 分量为负，是因为 $P$ 位于 $A$ 的左侧；并不是因为 $Q$ 被当成负电荷。

（3）计算电荷 $B$ 在 $P$ 处的场。

位移与距离为
$$\boldsymbol s_B=P-B=R(\tfrac12,\tfrac12,-1),\qquad s_B=\frac{\sqrt6R}{2}.$$
于是
$$\begin{aligned}
s_B^3&=\frac{3\sqrt6R^3}{4},\\
\boldsymbol E_B(P)&=\frac{k_eQ}{R^2}\frac4{3\sqrt6}(\tfrac12,\tfrac12,-1)\\
&=\frac{k_eQ}{R^2}\frac{\sqrt6}{9}(1,1,-2).
\end{aligned}$$
最后一行使用有理化 $2/(3\sqrt6)=\sqrt6/9$。两个电荷距 $P$ 不同，不能因电荷量相同就给它们同样的场强系数。

（4）感应电场的三个分量。

将两场相加再整体取负：
$$\boxed{
\boldsymbol E_{\mathrm{ind}}(P)=\frac{k_eQ}{R^2}
\left(
\frac{4\sqrt2}{27}-\frac{\sqrt6}{9},
-\frac{\sqrt2}{27}-\frac{\sqrt6}{9},
-\frac{\sqrt2}{27}+\frac{2\sqrt6}{9}
\right).
}$$
该式可与原来的 $\boldsymbol E_A+\boldsymbol E_B$ 逐分量相加，全部为零。若要求场强大小，可将三分量平方相加：
$$\begin{aligned}
\left|\frac{R^2\boldsymbol E_{\mathrm{ind}}}{k_eQ}\right|^2
&=18\left(\frac{\sqrt2}{27}\right)^2
+6\left(\frac{\sqrt6}{9}\right)^2
-10\frac{\sqrt2}{27}\frac{\sqrt6}{9}\\
&=\frac4{81}+\frac49-\frac{20\sqrt3}{243}
=\frac{120-20\sqrt3}{243}.
\end{aligned}$$
因此
$$|\boldsymbol E_{\mathrm{ind}}|=\frac{k_e|Q|}{R^2}
\sqrt{\frac{120-20\sqrt3}{243}}.$$
净电荷或接地条件改变时，球内总电场仍为零，所以这里的感应电场抵消关系不变。

（5）求外部电荷在 $P$ 处的电势。

电势是标量，不带位移方向的分量。由两个距离，
$$\begin{aligned}
\Phi_{\mathrm{ext}}(P)
&=k_eQ\left(\frac1{s_A}+\frac1{s_B}\right)\\
&=\frac{k_eQ}{R}\left(\frac{\sqrt2}{3}+\frac2{\sqrt6}\right)\\
&=\frac{k_eQ}{R}\frac{\sqrt2+\sqrt6}{3}.
\end{aligned}$$
设球的恒定电势为 $\Phi_s$，则一般关系为
$$\boxed{\Phi_{\mathrm{ind}}(P)=\Phi_s-\frac{k_eQ}{R}\frac{\sqrt2+\sqrt6}{3}.}$$
到这一步尚不能给出唯一数值，因为 $\Phi_s$ 未由题设确定。以下分别说明最常用的孤立中性状态及接地状态，不把缺失条件隐藏在计算中。

（6）推导一个球外电荷的接地镜像。

外部电荷 $Q$ 位于 $\boldsymbol a$，$|\boldsymbol a|=d>R$。取球内镜像位置
$$\boldsymbol a'=\frac{R^2}{d^2}\boldsymbol a,\qquad q'=-Q\frac Rd.$$
对任意球面点 $\boldsymbol s$，$|\boldsymbol s|=R$，比较两个距离平方：
$$\begin{aligned}
|\boldsymbol s-\boldsymbol a'|^2
&=R^2+\frac{R^4}{d^2}-2\frac{R^2}{d^2}\boldsymbol s\cdot\boldsymbol a\\
&=\frac{R^2}{d^2}\left(d^2+R^2-2\boldsymbol s\cdot\boldsymbol a\right)\\
&=\frac{R^2}{d^2}|\boldsymbol s-\boldsymbol a|^2.
\end{aligned}$$
故 $|\boldsymbol s-\boldsymbol a'|=(R/d)|\boldsymbol s-\boldsymbol a|$，球面电势为
$$k_e\left[\frac Q{|\boldsymbol s-\boldsymbol a|}
+\frac{-QR/d}{(R/d)|\boldsymbol s-\boldsymbol a|}\right]=0.$$
这一构造满足接地边界，且球外区域除真实电荷外无新增奇点，由唯一性定理可用于球外场。镜像处的奇点在导体内，因此绝不能把它解释为实际球内场。

（7）孤立初始中性球的恒定电势。

对 $A,B$ 分别用上述构造，接地镜像为
$$q_A'=-\frac{2Q}{5},\quad \boldsymbol a_A'=(2R/5,0,0),$$
$$q_B'=-\frac{2Q}{3},\quad \boldsymbol a_B'=(0,0,2R/3).$$
两镜像的总量为 $-16Q/15$。为使孤立球净电荷为零，另在球心加入
$$q_c=\frac{16Q}{15}.$$
球心镜像在整个球面产生相同的电势 $k_eq_c/R$，不会破坏等势边界，所以
$$\Phi_s=\frac{16k_eQ}{15R}.$$
从球外远场的 $1/r$ 项或Gauss定律可知，镜像总量等于球的实际总电荷；这里两偏轴镜像与球心镜像之和确为零。图 5-3 的镜像仅用于球外构造和确定 $\Phi_s$。

![图 5-3　孤立中性球的外部等效镜像及总电荷约束。](../figures/images-05.png)

代回第（5）步，
$$\boxed{\Phi_{\mathrm{ind}}(P)=\frac{k_eQ}{R}
\left[\frac{16}{15}-\frac{\sqrt2+\sqrt6}{3}\right].}$$
方括号为负，约为 $-0.2212344$。因此电势的大小为
$$\boxed{|\Phi_{\mathrm{ind}}(P)|=\frac{k_e|Q|}{R}
\left[\frac{\sqrt2+\sqrt6}{3}-\frac{16}{15}\right].}$$
若球接地，则 $\Phi_s=0$，感应电势变为 $-\Phi_{\mathrm{ext}}(P)$。若球有给定净电荷 $Q_s$，球心补偿电荷为 $Q_s+16Q/15$，相应的球电势为 $k_e(Q_s+16Q/15)/R$。这里将球面全部电荷产生的电势计作球面场；若另区分预存电荷与纯诱导重分布，须在定义中注明。

（8）固定电势球的总电荷。

第二问是另一个情景，外部只有一个电荷。其接地镜像为
$$q'=-\frac{QR}{d},\qquad z'=\frac{R^2}{d}.$$
再在球心放置 $q_0$，使球面电势为 $V$：
$$\frac{k_eq_0}{R}=V,\qquad q_0=\frac{RV}{k_e}.$$
两镜像共同给出球外解。因此球的总电荷为
$$\boxed{q_{\mathrm{sphere}}=\frac{RV}{k_e}-\frac{QR}{d}
=4\pi\varepsilon_0RV-\frac{QR}{d}.}$$
其中第二项随 $d$ 变化，是电源维持电势时交换电荷的结果。不能把它固定为 $4\pi\varepsilon_0RV$。

（9）外部点电荷的受力。

取 $+z$ 为由球心指向外部电荷的方向。球心镜像贡献
$$F_0=\frac{k_eQq_0}{d^2}=\frac{QRV}{d^2}.$$
偏轴镜像距真实电荷
$$d-z'=d-\frac{R^2}{d}=\frac{d^2-R^2}{d}>0.$$
其力为
$$\begin{aligned}
F'&=\frac{k_eQq'}{(d-z')^2}\\
&=-\frac{k_eQ^2R}{d}\frac{d^2}{(d^2-R^2)^2}\\
&=-\frac{k_eQ^2Rd}{(d^2-R^2)^2}.
\end{aligned}$$
图 5-4 中 $F'$ 指向球心，恒为吸引；$F_0$ 的方向取决于 $QV$ 的符号。合力为

![图 5-4　球心电荷项与近侧镜像吸引项产生的轴向力。](../figures/force-05.png)

$$\boxed{\boldsymbol F=\left[\frac{QRV}{d^2}
-\frac{k_eQ^2Rd}{(d^2-R^2)^2}\right]\boldsymbol e_z.}$$
电荷本身的自场不计入力，只有球面电荷产生的场；镜像正是这个球外场的等效表达。

（10）零力条件与解的存在性。

对 $Q\ne0$，令括号为零，乘以 $d^2/(QR)$ 得
$$\boxed{V=\frac{k_eQd^3}{(d^2-R^2)^2},\qquad d>R.}$$
右侧因子 $d^3/(d^2-R^2)^2$ 为正，故必须有 $V/Q>0$；若 $V=0$ 或 $V/Q<0$，吸引项不可能被抵消。$Q=0$ 则无力，是应单独列出的平凡情况。

设 $H(d)=d^3/(d^2-R^2)^2$，求导：
$$\begin{aligned}
H'(d)&=\frac{3d^2}{(d^2-R^2)^2}
-\frac{4d^4}{(d^2-R^2)^3}\\
&=-\frac{d^2(d^2+3R^2)}{(d^2-R^2)^3}<0.
\end{aligned}$$
又 $H(R^+)=+\infty$，$H(\infty)=0$。所以对任意给定 $V/Q>0$，恰有一个 $d>R$ 满足零力条件。图 5-5 中的水平线与曲线只有一个交点，正对应这一唯一性。

![图 5-5　零力条件中的单调函数及唯一交点。](../figures/zeros-05.png)

<!-- KEEP_STUDENT_START -->
（11）量纲与极限检查。

感应场量纲为 $k_eQ/R^2$，电势量纲为 $k_eQ/R$；总电荷式中的 $RV/k_e$ 与 $QR/d$ 均为电荷。检查远场时，先将吸引项整理成无量纲小参数：
$$\frac{d}{(d^2-R^2)^2}=\frac1{d^3}
\left(1-\frac{R^2}{d^2}\right)^{-2}.$$
令 $u=R^2/d^2\ll1$，利用二项式展开
$$(1-u)^{-2}=1+2u+3u^2+O(u^3).$$
代回原力式，
$$F=\frac{QRV}{d^2}-\frac{k_eQ^2R}{d^3}
-\frac{2k_eQ^2R^3}{d^5}
+O\left(\frac{k_eQ^2R^5}{d^7}\right).$$
固定非零 $V$ 时最远处由球的基准净电荷项主导；接地 $V=0$ 时始终吸引并按 $d^{-3}$ 衰减。该接地远场规律不同于固定净电荷为零的孤立球，原因是接地球可从外界取得净电荷。

近球面令 $d=R+\eta$，$0<\eta\ll R$。由于
$$d^2-R^2=(d-R)(d+R)\simeq2R\eta,\qquad Rd\simeq R^2,$$
吸引项的首阶为
$$F'\simeq-\frac{k_eQ^2R^2}{(2R\eta)^2}
=-\frac{k_eQ^2}{4\eta^2}.$$
它相当于电荷与距离 $2\eta$ 的反号平面镜像之间的力，验证曲率在很小间隙的首项中消失。固定 $V$ 产生的中心项仍有限，不能抵消这个近表面发散项。

<!-- KEEP_STUDENT_END -->

## 六、关键洞察

球内零场与球外镜像是两个区域中的不同论证。第一问电场不依赖未知常电势，电势却依赖；缺失条件影响的是电势而不是整个题都不可解。

固定电势与固定净电荷是两种不同控制方式。若总电荷固定为零，外部单电荷对应球心镜像 $q_0=QR/d$；若固定电势，则 $q_0=RV/k_e$。它们产生不同远场和受力，不得把中性球的镜像套到电源连接的球上。

在固定 $V$ 下，不能只对 $Q\Phi_{\mathrm{ind}}(d)$ 求导来求力。电荷改变位置时球面电荷随之重新分布，电源还交换能量；镜像自响应的一半因子及电源功都必须正确处理。直接用局部电场计算 $Q\boldsymbol E$ 最稳妥。

零力不等于稳定。令
$$F(d)=\frac{QR}{d^2}[V-k_eQH(d)].$$
在零力点 $d_*$，括号为零，因此
$$F'(d_*)=-\frac{k_eQ^2R}{d_*^2}H'(d_*)>0.$$
向外微移产生向外力，向内微移产生向内力，故轴向平衡不稳定。这里正负 $Q$ 都给相同的失稳结论。

还可从真实球面电荷密度验证镜像与净电荷。对轴上距离 $d$ 的电荷，令球面点的极角为 $\vartheta$，接地球电势由真实电荷与镜像给出。外侧法向场为 $-\partial\Phi/\partial r$，球内场为零，因此 $\sigma=\varepsilon_0E_n$。在 $r=R$ 求导并利用镜像距离比例，得到
$$\sigma_{\mathrm g}(\vartheta)=
-\frac{Q(d^2-R^2)}{4\pi R\,[d^2+R^2-2dR\cos\vartheta]^{3/2}}.$$
为看清该结果的来源，真实电荷势的径向导数为
$$-k_eQ\frac{R-d\cos\vartheta}{s^3},\qquad
s^2=R^2+d^2-2Rd\cos\vartheta.$$
镜像项的径向导数为
$$-k_eq'\frac{R-(R^2/d)\cos\vartheta}{(Rs/d)^3}
=k_eQ\frac{d^2-Rd\cos\vartheta}{R s^3}.$$
两者相加为 $k_eQ(d^2-R^2)/(Rs^3)$，再乘 $-\varepsilon_0$，用 $\varepsilon_0k_e=1/(4\pi)$，得到密度式。球心附加电荷 $q_0$ 对应的球面密度则是均匀项 $q_0/(4\pi R^2)$。

将接地密度积分可检查球的总电荷：
$$\begin{aligned}
q_{\mathrm g}
&=2\pi R^2\int_0^\pi\sigma_{\mathrm g}(\vartheta)\sin\vartheta\,d\vartheta\\
&=-\frac{QR(d^2-R^2)}2\int_{-1}^1
\frac{du}{(d^2+R^2-2dRu)^{3/2}}.
\end{aligned}$$
这里换元 $u=\cos\vartheta$，并将上下限反向与负号一并处理。积分原函数为
$$\frac1{dR\sqrt{d^2+R^2-2dRu}},$$
故定积分为
$$\frac1{dR}\left(\frac1{d-R}-\frac1{d+R}\right)
=\frac2{d(d^2-R^2)}.$$
代回精确得到 $q_{\mathrm g}=-QR/d$。加上均匀项即为 $q_{\mathrm g}+q_0$，与远场镜像总量一致。

第一问的两个外部电荷可分别旋转该密度表达式后叠加，再加 $q_c/(4\pi R^2)$。用真实面电荷积分
$$\Phi_{\mathrm{ind}}(P)=k_e\int_{\partial\mathcal B}
\frac{\sigma(\boldsymbol s)\,dS}{|P-\boldsymbol s|}$$
及其梯度，就能独立核对球内电势与电场。这个积分在球内也有效，因为积分源是真实球面电荷，不是球内虚构镜像；由此再次明确两种计算表达式的有效区域。

## 七、易错点

将 $P$ 当球外点，直接把三个点镜像的势相加，会得到错误的球内场，并可能在镜像处出现不存在的奇点。先算 $OP$ 是避免此错的首要步骤。

“导体内部总电场为零”不意味着外加场或感应场分别为零。电场是矢量，电势是标量；取负号时须对整个场矢量取负，不能对距离取负。

未指定接地或净电荷时，不能默认球电势为零。第二问只说接到电源时，还须解释参考端；本解将球电势 $V$ 定义为相对于无穷远，才对应边值条件。

总电荷与镜像电荷总量相等，不意味着每个镜像代表一个真实球内电荷。求真实外部电荷受力时，不加入其自场，也不再人为乘一半。

## 八、课堂讲解建议

先让学生根据坐标算 $OP$，不急于介绍镜像。板书把总场、外加场、感应场分成三项，用导体平衡条件消去总场，再按坐标逐项核对符号。

课堂讲镜像时保留球面两距离平方的比较，说明位置和电荷量并非凭记忆猜出的。随后用“接地”“孤立中性”“电源固定电势”三个边界条件比较球心镜像，帮助学生理解常电势项的作用。

最后让学生在零力交点两侧各取一个位置，用图 5-5 的单调性判断力方向，先得到不稳定直觉，再通过 $F'(d_*)>0$ 完成证明。

## 九、变式训练

变式一：球接地，外部电荷仍为 $Q$，求球总电荷与力。

解：$V=0$，故 $q_0=0$，
$$q_{\mathrm{sphere}}=-QR/d,\qquad
F=-k_eQ^2Rd/(d^2-R^2)^2<0.$$
接地导体从参考端取得异号净电荷，力恒为吸引；不可能存在有限的零力距离。

<!-- KEEP_TOGETHER_START -->
变式二：球孤立且净电荷为零，求同一个外部电荷的受力，并检查远场。

解：镜像 $q'=-QR/d$ 不变，球心电荷变为 $q_0=QR/d$。因此
$$\begin{aligned}
F&=\frac{k_eQ^2R}{d^3}-\frac{k_eQ^2Rd}{(d^2-R^2)^2}\\
&=-\frac{k_eQ^2R^3(2d^2-R^2)}
{d^3(d^2-R^2)^2}<0.
\end{aligned}$$
合并分式时使用 $(d^2-R^2)^2-d^4=-2d^2R^2+R^4$。在 $d\gg R$ 时，
$$F\simeq-\frac{2k_eQ^2R^3}{d^5}.$$
原来两个 $d^{-3}$ 项互相消去，首项变为中性球的极化吸引。这一结果说明净电荷约束对远场有实质影响，不能与接地情况互换。
<!-- KEEP_TOGETHER_END -->

（3）固定球电势$V$，若外点电荷存在径向零合力位置，判断其稳定性。

解：$F=QRV/d^2-kQ^2Rd/(d^2-R^2)^2$，在$F(d_*)=0$处消去$V$后，
$$F'(d_*)=\frac{kQ^2R(d_*^2+3R^2)}{(d_*^2-R^2)^3}>0.$$
向外微移产生向外力，向内微移产生向内力，故该径向平衡不稳定。质量为$m$的点电荷小扰动增长率为$\sqrt{F'/m}$。此结论只针对固定电势、$d_*>R$及径向运动；改变为固定球总电荷时受力式需重求。

（4）写出固定电势条件下的有效径向势能，并解释像电荷项的系数。

解：取无穷远势能为零，由$F=-dU/dd$积分得
$$U(d)=\frac{QRV}{d}-\frac{kQ^2R}{2(d^2-R^2)}.$$
第二项含$1/2$，因为像电荷的位置和电量随真实电荷改变，且电源维持球电势时交换能量。直接把$Q$乘全部诱导电势会多算该项。对式求导恢复主问的力，适用于将电源能量交换计入后的有效机械势能。
