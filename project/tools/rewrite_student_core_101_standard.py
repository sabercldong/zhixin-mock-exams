from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


ADDITIONS: dict[str, dict[int, str]] = {
    "046": {
        1: r"""**球形地球的数值链条。** 先把周期化成秒：
$$
T=27.3\times24\times3600=2.35872\times10^6\ \mathrm s.
$$
地球质量由题给半径和密度算出：
$$
\begin{aligned}
M_E&=\frac43\pi R^3\rho\\
&=\frac43\pi(6.4\times10^6)^3(5.5\times10^3)\\
&\approx6.04\times10^{24}\ \mathrm{kg}.
\end{aligned}
$$
对地、月的相对坐标使用两体开普勒第三定律，不先抛弃月球质量：
$$
\frac{G(M_E+M_M)}{r^2}=\frac{4\pi^2r}{T^2}.
$$
因此
$$
r=\left[\frac{G(M_E+M_M)T^2}{4\pi^2}\right]^{1/3}
\approx3.84\times10^8\ \mathrm m,
$$
月球相对地球的速率为
$$
v=\frac{2\pi r}{T}\approx1.02\times10^3\ \mathrm{m\,s^{-1}}.
$$
这一数值应与直接使用 $v^2=G(M_E+M_M)/r$ 的结果一致。

**无限圆柱的场方程。** 取与地球圆柱同轴、半径为 $r>R$、长为 $L$ 的高斯柱面。两个端面的法向与引力场垂直，通量只来自侧面：
$$
g(r)(2\pi rL)=4\pi G(\rho\pi R^2L).
$$
先约去 $2\pi L$，再得
$$
g(r)=\frac{2\pi G\rho R^2}{r}.
$$
圆轨道条件 $v^2/r=g(r)$ 给出
$$
v^2=2\pi G\rho R^2.
$$
因为场强恰与 $1/r$ 成正比，向心加速度中的 $1/r$ 完全抵消，所以轨道速度与轨道半径无关，但周期 $2\pi r/v$ 仍与 $r$ 成正比。""",
        2: r"""**用未知方向的摩擦力列式。** 在随车向右加速的非惯性系中，质心受向左的惯性力 $ma$。先假设地面摩擦力 $f$ 向右，墙的支持力 $N_w$ 也向右，再让方程决定二者的符号。刚体在车内静止，故
$$
N_w+f-ma=0,
\qquad N-mg=0.
$$
以质心 $C$ 取力矩。惯性力和重力穿过 $C$，不产生力矩；墙力的力臂是 $h$，地面摩擦力的力臂是 $r-h$，二者应反向：
$$
N_wh=f(r-h).
$$
由第一式 $N_w=ma-f$，代入力矩式：
$$
(ma-f)h=f(r-h).
$$
展开后 $mah-fh=fr-fh$，所以
$$
f=\frac{mah}{r},
\qquad
N_w=ma\left(1-\frac hr\right).
$$
静摩擦临界条件是 $f=\mu N=\mu mg$，因此
$$
a_{\min}=\frac{\mu rg}{h}.
$$
这也说明只有向右加速才会使偏心刚体所需摩擦力随 $a$ 增大。

**地面光滑时的墙面摩擦。** 此时地面只给竖直支持力，墙面的水平支持力 $N_w'$ 与竖直摩擦力 $f_w$ 共同维持平衡。水平方程直接给出
$$
N_w'=ma.
$$
以质心取矩，$N_w'$ 的力臂为 $h$，$f_w$ 的力臂为 $r$，故
$$
|f_w|r=N_w'h.
$$
因而所需摩擦比与 $a$ 无关：
$$
\frac{|f_w|}{N_w'}=\frac hr.
$$
要使任意大的 $a$ 都不滑动，必须且只需 $\mu'\ge h/r$。""",
        3: r"""**由圆心和弦端点求场线面积。** 通过 $(\pm a,0)$ 的场线圆的圆心必在 $y$ 轴上。设上方圆弧经过 $(0,\eta a)$，圆心为 $(0,c)$、半径为 $R_c$，则
$$
R_c^2=a^2+c^2=(\eta a-c)^2.
$$
展开并消去 $c^2$ 后
$$
c=\frac{\eta^2-1}{2\eta}a,
\qquad
R_c=\frac{1+\eta^2}{2\eta}a.
$$
若令圆心到弦端的半径与水平方向夹角为 $\alpha$，则
$$
\sin\alpha=\frac a{R_c}=\frac{2\eta}{1+\eta^2}.
$$
一个弓形面积是扇形减三角形：
$$
S_{\rm seg}=R_c^2\alpha-a|c|.
$$
上、下两弓的边界取向相反，合并后再除以 $a^2$ 即得题中 $\xi$。尤其要保留反三角函数所在的连续支路：$\eta=1$ 时边界是一个整圆，必须得到 $\xi=\pi$。

**圆盘电势的距离比。** 二维点源的电势为对数型。源、汇位于 $\bm r_+$、$\bm r_-$ 时，可写成
$$
U(\bm r)=C\ln\frac{|\bm r-\bm r_-|}{|\bm r-\bm r_+|}+U_0.
$$
由 $\bm j=-\sigma_0\nabla U$ 计算圆心场强，用题给 $j_0$ 消去常数 $C$；再将边界点 $(r\cos\theta,r\sin\theta)$ 到两电极的距离代入，便得只含距离比的对数。移动电极而保持电压时，既要比较圆心梯度，又要按新电极间电势差重新归一化；这两个因子分别给出最终 $\chi$ 和 $\chi'$ 中的三角或双曲函数组合。""",
        4: r"""**先确定惯性系数。** 令左液面从平衡位置上升 $x$，右液面就下降 $x$。不可只统计两段竖直液柱，因为底部水平管中液体以同一速率运动。总流体长度为 $3l+h$，故
$$
\mathcal T=\frac12\rho S(3l+h)\dot x^2.
$$
两侧液柱的质量分别改变 $\rho Sx$，将其重力势能相减，或直接积分 $\rho Sg\int z\,dz$，可得与平衡位置相对的势能
$$
V_g=\rho Sgx^2.
$$
拉格朗日方程为
$$
\rho S(3l+h)\ddot x+2\rho Sgx=0,
$$
因而
$$
\omega_1^2=\frac{2g}{3l+h}.
$$

**恒定角速度的平衡高度差。** 在随管转动系中，静液面满足
$$
gz-\frac12\omega_0^2s^2=\text{常量}.
$$
两根竖直管到转轴的距离分别为 $l$ 和 $2l$，液面高度差为 $2\Delta h$，所以
$$
2g\Delta h=\frac12\omega_0^2[(2l)^2-l^2]
=\frac32\omega_0^2l^2.
$$
从而 $\omega_0^2=4g\Delta h/(3l^2)$。在恒 $\omega_0$ 下做小振动时，离心势对 $x$ 的二阶项为零，它只改变平衡点，因此 $\omega_2=\omega_1$。撤去外部驱动后应改用角动量 $J=I(x)\omega$ 守恒，转动能写成 $J^2/[2I(x)]$。把 $I(x)$ 展开至二阶，一阶项与重力势能相消，二阶项才给出 $\omega_3$ 中的额外回复系数。""",
        5: r"""**由面积变化求电动势。** 时刻 $t$ 导体棒位于 $y=vt$，与抛物线 $y=kx^2$ 的交点满足
$$
x_t=\sqrt{\frac{vt}{k}}.
$$
棒长是两交点间的全长，即 $L=2x_t$。回路面积不是矩形，应对棒与抛物线之间的面积积分：
$$
\begin{aligned}
A(t)
&=\int_{-x_t}^{x_t}(vt-kx^2)\,dx\\
&=2vtx_t-\frac23kx_t^3.
\end{aligned}
$$
由 $kx_t^2=vt$ 得
$$
A(t)=\frac43vtx_t
=\frac43\frac{v^{3/2}}{\sqrt k}t^{3/2}.
$$
因而
$$
E=B\frac{dA}{dt}
=2Bv\sqrt{\frac{vt}{k}}
=BLv.
$$
最后一个等号也可由运动电动势 $\int(\bm v\times\bm B)\cdot d\bm l$ 直接得到。

**电阻、电流和功率的同步化简。** 回路电阻全在棒上，故
$$
R(t)=\lambda L(t)=2\lambda\sqrt{\frac{vt}{k}}.
$$
电动势与电阻都正比于 $L$，因此
$$
I=\frac ER=\frac{Bv}{\lambda}
$$
为常量。安培力大小为
$$
F=IBL,
$$
外力功率
$$
P_{\rm ext}=Fv=IBLv=IE=I^2R.
$$
三种写法相同，同时核对了棒长的因子 $2$。$t\to0^+$ 时 $E$ 和 $R$ 同时按 $\sqrt t$ 趋零，其比值仍有有限右极限，不是任意的 $0/0$。""",
        6: r"""**球面余弦发光体的投影抵消。** 设观察方向与球面元法线夹角为 $\theta$。球面元 $dS$ 在像平面的投影面积为
$$
dS_\perp=dS\cos\theta.
$$
该面元沿观察方向的发射强度为 $I_0\cos\theta$。因而每单位投影面积、每单位立体角的能流为
$$
\frac{I_0\cos\theta\,dS}{dS\cos\theta}=I_0,
$$
与球面位置无关。这一步必须同时保留“发光余弦”和“面积投影余弦”，少任何一个都会得到边缘变暗的错误结论。

**半球折射的面积雅可比。** 发光平面上的环带半径记为 $a=qr$，通过球面折射后，远处投影环带半径为 $p=P(q)r$。原环带面积与投影环带面积分别为
$$
dS=2\pi r^2q\,dq,
\qquad
dS'=2\pi r^2P\,dP.
$$
所以
$$
\frac{dS}{dS'}
=\frac qP\left(\frac{dP}{dq}\right)^{-1}.
$$
若正文定义的 $J_S$ 取倒数，便得 $J_S=(P/q)(dP/dq)$。不能在这里把 $P/q$ 和 $dP/dq$ 分开解读：前者控制环周长伸缩，后者控制径向宽度伸缩。再将折射前后的立体角变换、距离比和余弦投影因子逐项乘入，才得正文的 $B(q)$。在 $q=0$ 不可直接代入 $P/q$，而应先用 $P(q)=q/n+O(q^3)$ 取极限。""",
        7: r"""**偏转角的几何计数。** 光线在入射和出射界面各产生一次 $\alpha-\theta$ 型折转，每次内反射产生 $\pi-2\theta$ 的方向改变。累加 $N$ 次内反射后
$$
\Delta_N
=2(\alpha-\theta)+N(\pi-2\theta)
=N\pi+2\alpha-2(N+1)\theta.
$$
斯涅尔定律为
$$
\sin\alpha=n\sin\theta.
$$
对 $\alpha$ 求导：
$$
\cos\alpha
=n\cos\theta\frac{d\theta}{d\alpha},
\qquad
\frac{d\theta}{d\alpha}
=\frac{\cos\alpha}{n\cos\theta}.
$$
驻值条件 $d\Delta_N/d\alpha=0$ 因而是
$$
1-(N+1)\frac{\cos\alpha}{n\cos\theta}=0.
$$
将它平方，再用 $\sin\theta=\sin\alpha/n$ 消去 $\theta$：
$$
n^2-\sin^2\alpha
=(N+1)^2(1-\sin^2\alpha).
$$
整理得
$$
\sin^2\alpha_{Nm}
=\frac{(N+1)^2-n^2}{(N+1)^2-1}.
$$
分子非负要求 $n\le N+1$；若 $n>N+1$，该级偏转函数在物理入射区间没有驻点，所以后面的光强比没有定义，不能把复数角度强行代入菲涅耳系数。

**光强比的次序。** 先判断级次存在，再在各自驻值角计算振幅。一条经 $N$ 次内反射的光线振幅含入射透射、$N$ 次内反射和出射透射，因而有 $tt'(r')^N$。题给 $tt'=1+rr'$ 用于消去透射系数，但它不能代替驻值存在性判断。""",
        8: r"""**反应能与氦核速度。** 忽略中微子静质量，单次反应可供能量为
$$
Q=\bigl(4m_{\rm H}-m_{\rm He}-2m_e\bigr)c^2.
$$
若全部给氦核，则
$$
(\gamma_u-1)m_{\rm He}c^2=Q,
\qquad
\gamma_u=1+\frac{Q}{m_{\rm He}c^2}.
$$
再由
$$
\frac uc=\sqrt{1-\frac1{\gamma_u^2}}
$$
求喷流速度。选择氦核而不是光子的原因可由同能量动量比较看出：光子 $p=Q/c$，有质量粒子则
$$
pc=\sqrt{Q^2+2Qm_{\rm He}c^2}>Q.
$$

**从质量流率到推力。** 质子质量流率为 $\dot m_{\rm H}$ 时，每秒反应次数是
$$
\dot N=\frac{\dot m_{\rm H}}{4m_{\rm H}}.
$$
每个氦核动量为 $\gamma_um_{\rm He}u$，因而飞船系推力
$$
F=\dot N\gamma_um_{\rm He}u.
$$
在地面系中，沿运动方向的三力与本征加速度关系为 $F=\gamma^3m_0a'$ ，所以
$$
a'=\frac{F}{m_0}\left(1-\frac{v^2}{c^2}\right)^{3/2}.
$$

**相对论火箭方程。** 令快速度 $\chi=\operatorname{artanh}(v/c)$，恒定喷流速度的理想火箭满足
$$
d\chi=-\frac uc\frac{dm}{m}.
$$
积分得
$$
\frac{m_i}{m_f}=\exp\left[\frac c u\operatorname{artanh}\left(\frac{v_f}{c}\right)\right].
$$
往返中的加速与减速需要等大快速度，所以总质量比是两段质量比的乘积，不是把两次燃料分数相加。""",
    },
    "050": {
        1: r"""**圆柱颗粒的力与减速距离。** 被挡板反弹的空气分子向上速率约为 $v_0$，颗粒仍向下以 $v_0$ 运动，代表性相对速率为 $2v_0$。每单位时间打在颗粒迎风面上的反弹分子质量级为
$$
\dot m_{\rm air}\sim\eta\rho_0(\pi r^2)(2v_0).
$$
完全弹性碰撞的动量改变再提供一个速率因子，故平均力的数量级为
$$
F\sim4\eta\rho_0\pi r^2v_0^2.
$$
圆柱颗粒质量是
$$
m_p=\rho\pi r^2(2r)=2\pi\rho r^3,
$$
所以
$$
a_p\sim\frac{F}{m_p}
=\frac{2\eta\rho_0v_0^2}{\rho r}.
$$
正文采用的冲量约定将反射前后的相对速率因子完整计入，系数写为 $4$；无论采用哪个一致的数量级约定，都必须保留 $a_p\propto1/r$。

要在厚度 $h_0$ 的有效区内把向下速度降到零，匀减速估算给出
$$
v_0^2\sim2a_ph_0.
$$
代入正文的力系数后，$v_0^2$ 在两边相消，得
$$
r_0=\frac{8\eta\rho_0h_0}{\rho}.
$$
数值上
$$
r_0
=\frac{8(0.1)(1.29)(1.0\times10^{-2})}{2.0\times10^3}
=5.16\times10^{-6}\ \mathrm m.
$$

**球面的三个余弦因子。** 取球面法线与竖直方向夹角为 $\theta$ 的环带。迎风投影提供 $\cos\theta$，法向相对速度提供第二个 $\cos\theta$，法向冲量的竖直投影提供第三个 $\cos\theta$。因此
$$
dF_z\propto\cos^3\theta\,dA,
\qquad
dA=2\pi r^2\sin\theta\,d\theta.
$$
积分
$$
\int_0^{\pi/2}\cos^3\theta\sin\theta\,d\theta=\frac14
$$
给出球形的几何系数，再用球质量 $4\pi\rho r^3/3$ 重复减速距离判据，得 $r_0'=3r_0/4$。""",
        2: r"""**几何约束与质心轨迹。** 细杆两端均在半径 $R$ 的圆上，长度为 $L$ 的弦到圆心的距离为
$$
d=\sqrt{R^2-\frac{L^2}{4}}.
$$
杆为均匀细杆，质心在弦中点，所以当杆相对最低位置转过小角 $\theta$ 时，质心沿半径 $d$ 的圆弧运动。杆方向与半径方向始终垂直，故杆的自转角速度也为 $\dot\theta$。总动能
$$
\begin{aligned}
\mathcal T
&=\frac12Md^2\dot\theta^2
+\frac12\left(\frac1{12}ML^2\right)\dot\theta^2\\
&=\frac12K\dot\theta^2,
\qquad
K=M\left(d^2+\frac{L^2}{12}\right).
\end{aligned}
$$
重力势能相对最低点为
$$
V=Mgd(1-\cos\theta)
\simeq\frac12Mgd\theta^2.
$$
所以
$$
K\ddot\theta+Mgd\theta=0,
\qquad
T=2\pi\sqrt{\frac{K}{Mgd}}.
$$

**支持力差的二阶计算。** 质心的径向加速度为 $-d\dot\theta^2$，切向加速度为 $d\ddot\theta$。转折点 $\theta=\theta_m$ 时 $\dot\theta=0$；通过平衡点时 $\theta=0$，由能量守恒
$$
\frac12K\dot\theta_0^2
=Mgd(1-\cos\theta_m)
\simeq\frac12Mgd\theta_m^2,
$$
即
$$
\dot\theta_0^2=\frac{Mgd}{K}\theta_m^2.
$$
将这两个状态分别投影到径向和切向，可先求出两端支持力的矢量和，再比较其大小。不能把两个支持力的标量和当成合力大小，因为两个法向之间有有限夹角。展开到 $\theta_m^2$ 后，一阶项必须由对称性消失；若仍留下与 $\theta_m$ 成正比的项，表明两个端点或法向取向不对称。""",
        3: r"""**进入内圆的临界圆轨道。** 在环形磁场中，粒子的轨道半径为
$$
\rho=\frac{mv_0}{qB_0}.
$$
粒子从外圆边界沿半径方向入射，速度与初始位置半径垂直方向的偏移决定轨迹圆心。刚好能够触及内圆时，轨迹圆与半径 $R_1$ 的内边界内切。由圆心距离几何可得
$$
R_2^2+\rho^2=(R_1+\rho)^2.
$$
展开消去 $\rho^2$：
$$
2R_1\rho=R_2^2-R_1^2,
\qquad
\rho=\frac{R_2^2-R_1^2}{2R_1}.
$$
乘上 $qB_0/m$ 就得 $v_{0\min}$。临界状态是相切而非相交，这是因为更小速度对应更小的 $\rho$，轨迹将在达到内圆前已经弯回。

**由轴对称求内区磁场。** 取轴对称规范 $A_\varphi=Br/2$，正则角动量为
$$
p_\varphi=mr^2\dot\varphi+qrA_\varphi
=mr^2\dot\varphi+\frac12qBr^2.
$$
在环形区从 $R_2$ 走到 $R_1$ 时，机械角动量的改变只与穿过环带的磁通量有关：
$$
L_z(R_1)-L_z(R_2)
=-\frac12qB_0(R_2^2-R_1^2).
$$
入射时速度沿半径，$L_z(R_2)=0$。在内圆中轨道通过圆心的条件等价于该区正则角动量为零：
$$
L_z(R_1)+\frac12qB_xR_1^2=0.
$$
代入上式得
$$
B_x=-B_0\frac{R_2^2-R_1^2}{R_1^2}.
$$
负号说明内区磁场必须与题目规定的向里正方向相反。""",
        4: r"""**撞台阶时先守恒角动量，后比较能量。** 碰撞时间很短，右上方棱角 $A$ 的冲量对 $A$ 点力矩为零。碰前圆环纯滚，自转角速度 $v_1/r$。圆心速度对 $A$ 点的轨道角动量与自转角动量必须分开写，其和等于碰后绕 $A$ 转动的角动量。由此求出碰后角速度 $\omega_+$ 后，才有资格写
$$
\frac12I_A\omega_+^2\ge mg h.
$$
等号给出刚好翻过台阶的临界速度。碰前能量不守恒；若直接把 $mv_1^2$ 与 $mgh$ 相等，就会漏掉非弹性碰撞损失。

**滚动阻力矩产生恒角减速。** 纯滚时圆环总动能为
$$
E=\frac12mv^2+\frac12mr^2\left(\frac vr\right)^2=mv^2.
$$
滚动阻力偶矩大小为 $kN=kmg$，功率为
$$
\frac{dE}{dt}=-kmg\omega=-kmg\frac vr.
$$
左边 $dE/dt=2mv\dot v$，约去 $mv$得
$$
\dot v=-\frac{kg}{2r}.
$$
从 $v_0$ 匀减速到零的时间为
$$
t_{\rm stop}=\frac{v_0}{kg/(2r)}=\frac{2rv_0}{kg}.
$$

**推环问题中同时使用平动和转动平衡。** 圆环匀速滚动，水平合力为零、对圆心合力矩也为零。铁棍对环的法向力与动摩擦力的合力方向由 $\mu$ 决定；地面摩擦力再与它的水平分量平衡，并为转动平衡提供力矩。消去地面支持和摩擦后，推力是 $\theta$ 的函数；对它求导或把正弦、余弦组合写成单一相位，得
$$
\tan\theta_{\rm opt}=\frac{r-k\mu}{r\mu+k}.
$$
最后还要检查地面支持力为正且所需静摩擦不超过上限。""",
        5: r"""**体积约束先消去一个自由度。** 三管横截面积为 $S,2S,S$，液体体积不变给出
$$
Slx_1+2Slx_2+Slx_3=0,
$$
即
$$
x_2=-\frac{x_1+x_3}{2}.
$$
第 $i$ 管中运动液体的质量在一阶近似中取平衡值 $\rho S_il$，流速为 $l\dot x_i$。因而
$$
\mathcal T
=\frac12\rho Sl^3
(\dot x_1^2+2\dot x_2^2+\dot x_3^2).
$$
代入 $\dot x_2=-(\dot x_1+\dot x_3)/2$：
$$
\begin{aligned}
\mathcal T
&=\frac12\rho Sl^3\left[
\dot x_1^2+\frac12(\dot x_1+\dot x_3)^2+\dot x_3^2
\right]\\
&=\frac{\rho Sl^3}{4}
(3\dot x_1^2+2\dot x_1\dot x_3+3\dot x_3^2).
\end{aligned}
$$

**势能中的一阶项必须消失。** 高度为 $h_i=l(1+x_i)$ 的竖直液柱势能为 $\rho gS_i h_i^2/2$。三管相加后，与 $x_i$ 成正比的项正比于 $x_1+2x_2+x_3$，由体积约束为零。保留二阶项：
$$
V=\frac12\rho gSl^2(x_1^2+2x_2^2+x_3^2)+\text{常量}.
$$
消去 $x_2$ 后
$$
V=\frac{\rho gSl^2}{4}(3x_1^2+2x_1x_3+3x_3^2)+\text{常量}.
$$
动能和势能中的二次型完全相同，只差系数 $g/l$，所以拉格朗日方程直接给出
$$
\ddot x_1+\frac glx_1=0,
\qquad
\ddot x_3+\frac glx_3=0.
$$
初态 $x_1=x_2=\varepsilon$ 与体积约束同时要求 $x_3=-3\varepsilon$。系统初始静止，因此 $x_1$ 只含余弦项，得
$$
x_1(t)=\varepsilon\cos\sqrt{\frac gl}\,t.
$$""",
        6: r"""**在时刻 $t$ 前能撞到右壁的分子。** 设分子初始距右壁为 $x$，则它必须满足 $v_x>x/t$ 才能在 $t$ 前撞壁。对均匀初始位置和麦克斯韦速度分布积分：
$$
N_c(t)=\frac Nl\int_0^l dx
\int_{x/t}^{\infty}
\sqrt{\frac{m}{2\pi kT}}
e^{-mv_x^2/(2kT)}\,dv_x.
$$
更换积分次序更直观：对给定 $v_x>0$，能撞壁的初始长度为 $\min(v_xt,l)$。以
$$
v_T=\sqrt{\frac{2kT}{m}},
\qquad
a=\frac{l}{v_Tt}
$$
无量纲化，分段积分就会自然出现题定义的
$$
f(a)=\int_0^ae^{-u^2}\,du.
$$

**冲量积分多一个速度因子。** 一个分子完全弹性碰撞给壁的冲量为 $2mv_x$，所以总冲量的积分被积函数比碰撞数积分多一个 $v_x$。通过 $p_0=NkT/(Sl)$ 消去 $N$，可得
$$
\Delta P(t)=\frac{2p_0St}{\sqrt\pi}f(a).
$$
短时 $a\to\infty$时 $f(a)\to\sqrt\pi/2$，因此 $\Delta P\simeq p_0St$，初始受力正是 $p_0S$。长时 $a\to0$时 $f(a)\sim a$，结果趋于全部分子离开前给壁的总动量。

**自由试管只需初末动量。** 当 $M\gg Nm$时，试管速度对分子碰撞的反馈是高阶小量。全部气体最终从左侧离开，用系统总动量守恒可直接求试管终速。对光子气体，体积能量密度由黑体出射度得 $u_\gamma=4\sigma T^4/c$，箱内总能量为 $U=u_\gamma Sl$。各向同性角平均与完全反射的因子合并后，试管获得动量 $2\sigma T^4Sl/c^2$，因而
$$
V_\gamma=\frac{2\sigma T^4Sl}{Mc^2}.
$$""",
        7: r"""**先用轴上物点判定孔径光阑。** 设物屏中心发出的光线初始倾角为 $u_0$。到达 $L_1$ 时高度
$$
y_1=l_1u_0.
$$
通过 $L_1$ 后倾角
$$
u_1=u_0-\frac{y_1}{f_1}.
$$
再传播 $l_2$ 到 $L_2$：
$$
\begin{aligned}
y_2
&=y_1+l_2u_1\\
&=(l_1+l_2)u_0-\frac{l_1l_2}{f_1}u_0.
\end{aligned}
$$
代入 $l_1=2l_2$、$l_2=2f_1$，得 $y_2=-l_2u_0$。两透镜对倾角的限制分别为
$$
|u_0|\le\frac{D_1}{2l_1},
\qquad
|u_0|\le\frac{D_2}{2l_2}.
$$
用 $D_1=3D_2$ 和 $l_1=2l_2$ 比较，第二个上限更小，所以 $L_2$ 是孔径光阑。

**离轴物点的光线高度递推。** 设物点高度为 $y_0$，初始倾角为 $u_0$。传到 $L_1$、折射、再传到 $L_2$ 后，
$$
y_2
=\left(1-\frac{l_2}{f_1}\right)y_0
+\left(l_1+l_2-\frac{l_1l_2}{f_1}\right)u_0.
$$
代入题给距离后
$$
y_2=-y_0-l_2u_0.
$$
可见区域要求存在某条光线同时满足 $|y_1|\le D_1/2$ 和 $|y_2|\le D_2/2$。临界时光线恰好通过两孔径的相反边缘，消去 $u_0$ 得
$$
|y_0|_{\max}=\frac{D_1}{2}=\frac{3D_2}{2}.
$$
“明亮”的定义额外指定光线穿过 $L_1$ 中心，即 $y_1=0$。由此 $u_0=-y_0/l_1$，再代入 $y_2$，得 $|y_2|=|y_0|/2$。条件 $|y_2|\le D_2/2$ 给出 $|y_0|\le D_2$，即明亮区域半径 $R=D_2$。""",
        8: r"""**坐标加速度与本征加速度。** 地面系中两端的速度都是 $v=at$，记
$$
\beta=\frac{at}{c},
\qquad
\gamma=\frac1{\sqrt{1-\beta^2}}.
$$
一维运动的本征加速度为
$$
a'=\gamma^3a
=\frac{a}{(1-a^2t^2/c^2)^{3/2}}.
$$
它随时间增大，说明“地面系坐标加速度恒定”不等于车载加速度计读数恒定。

**世界线参数化。** 令 $\sin\phi=at/c$，则
$$
dt=\frac ca\cos\phi\,d\phi,
\qquad
d\tau=dt\sqrt{1-\frac{a^2t^2}{c^2}}
=\frac ca\cos^2\phi\,d\phi.
$$
从 $0$ 积到 $\phi$：
$$
\begin{aligned}
c\tau
&=\frac{c^2}{a}\int_0^\phi\cos^2u\,du\\
&=\frac{c^2}{2a}(\phi+\sin\phi\cos\phi).
\end{aligned}
$$
坐标位置则直接由 $x_L=at^2/2$ 得
$$
x_L=\frac{c^2}{2a}\sin^2\phi.
$$
右端与左端有完全相同的 $t$ 依赖，只是整体平移 $l$，所以 $x_R=l+x_L$，且同一地面时刻两端间距恒为 $l$。

**瞬时静止系的同时线。** 在左端事件 $A(ct_A,x_A)$ 处，瞬时共动系的同时条件是
$$
c^2(t_B-t_A)=v_A(x_B-x_A).
$$
右端事件 $B$ 必须同时满足它自己的世界线
$$
x_B=l+\frac12at_B^2.
$$
这是一个关于 $t_B$ 的二次方程。取与 $l\to0$ 时 $t_B\to t_A$ 连续的物理根，再用洛伦兹变换求两事件的空间间隔，才得正文的 $L_A$。若直接写 $\gamma l$，就默认两端在同一瞬时共动系时刻也有相同速度；对有限长、持续加速的列车，这一假设只在短车极限成立。""",
    },
}


SECOND_ADDITIONS: dict[str, dict[int, str]] = {
    "046": {
        1: r"""**两种场源的极限比较。** 球外引力场 $g=GM/r^2$ 给出 $v=\sqrt{GM/r}$，故轨道半径增大时速率下降；无限圆柱外场 $g=2\pi G\rho R^2/r$ 给出恒定轨道速度。两者在圆柱表面的内外场还应连续。对 $s<R$ 的高斯柱面，
$$
g_{\rm in}(s)2\pi sL=4\pi G(\rho\pi s^2L),
$$
得 $g_{\rm in}=2\pi G\rho s$。令 $s\to R^-$ 得 $2\pi G\rho R$，而外场令 $r\to R^+$ 也得同一值。这一连续性核对了内外高斯面中包围质量的选择。""",
        2: r"""**加速度反向时的运动趋势。** 若车向左加速，惯性力向右。它的作用线位于地面接触点上方 $r-h$，产生的转动趋势使刚体离开左墙，而非更紧地压向墙。墙面法向力不能为负，因此“仍保持墙、地双接触”的方程在这个方向上会失效。正确物理图像是先失去墙面接触，之后再按单一地面接触讨论滚动或滑动。这是选项 B 不能只靠“摩擦变大”一句得出的原因。""",
        3: r"""**第（1）问的矢量相加。** 在 $(0,\eta a)$ 处，到两线电荷的距离均为 $a\sqrt{1+\eta^2}$。一根正线电荷的场强大小为 $\lambda/(2\pi\varepsilon_0d)$，其 $y$ 分量与另一根负线电荷的 $y$ 分量相消，$x$ 分量同向。每根的水平方向余弦为 $1/\sqrt{1+\eta^2}$，因此
$$
E_x=2\frac{\lambda}{2\pi\varepsilon_0a\sqrt{1+\eta^2}}
\frac1{\sqrt{1+\eta^2}}
=\frac{\lambda}{\pi\varepsilon_0a(1+\eta^2)}.
$$
与题设 $E_x=\zeta\lambda/(4\pi\varepsilon_0a)$ 比较，得 $\zeta=4/(1+\eta^2)$。这一算法同时检查了场方向和因子 $2$。""",
        4: r"""**自由转动情形的二阶展开原则。** 设液面位移为 $x$，总转动惯量写成
$$
I(x)=I_0+I_1x+I_2x^2+O(x^3).
$$
撤去驱动后 $J=I\omega$ 守恒，因而
$$
\frac{J^2}{2I(x)}
=\frac{J^2}{2I_0}
\left(-\frac{I_1}{I_0}x
+\frac{I_1^2-I_0I_2}{I_0^2}x^2\right)+O(x^3).
$$
式中一阶系数必须与重力势能的一阶项相消，因为 $x=0$ 是初始平衡位置。保留的二阶系数与重力势能二阶系数相加，再除以动能中的有效质量 $\rho S(3l+h)$，才得 $\omega_3^2$。若直接将 $\omega$ 保持为 $\omega_0$，就把“自由转动”误做成了“恒速电机驱动”。""",
        5: r"""**电流方向的楼次判断。** 导体棒向 $+y$ 运动时，若磁场向 $+z$，正电荷所受洛伦兹力 $q\bm v\times\bm B$ 沿 $+x$，所以棒中电流从左端流向右端。回路面积随时间增大，根据楞次定律，感应电流产生的磁场应反向阻碍原磁通量增加，与上述洛伦兹力判断相同。棒所受安培力方向为 $-y$，恰与运动方向相反，故外力功率为正，电阻焦耳热也为正。这条方向链可防止在 $E=-d\Phi/dt$ 中单独处理负号而与回路取向矛盾。""",
        6: r"""**折射几何的变量顺序。** 对发光平面上的无量纲半径 $q=a/r$，先算球面法线的余弦 $c=\sqrt{1-q^2}$；入射角正弦为 $q$，折射角正弦为 $q/n$，故 $c_i=\sqrt{1-q^2/n^2}$。先由这两个量建立出射方向，再求投影半径 $P(q)$。这个顺序保证每个根号都在其定义域内。当 $q\to1^-$ 时 $c\to0$，单个雅可比因子可能发散，但亮度必须对全部投影和立体角因子的乘积取极限。边缘的中间量发散不能单独当成物理亮度无穷大。""",
        7: r"""**驻值角的回代。** 求得 $\sin^2\alpha_{Nm}$ 后，应在 $0\le\alpha\le\pi/2$ 取正弦为正的主值，然后由
$$
\theta_{Nm}=\arcsin\frac{\sin\alpha_{Nm}}n
$$
得折射角，最后代回
$$
\Delta_{Nm}=N\pi+2\alpha_{Nm}-2(N+1)\theta_{Nm}.
$$
不能只给出 $\sin^2\alpha$ 而忽略角度支路。当 $n=N+1$ 时分子为零，驻值点退到 $\alpha=0$ 的区间端点；当 $n$ 再增大，根号变成负数，这表示物理驻值消失，而非光线角度变成复数。""",
        8: r"""**质量比与燃料比的换算。** 火箭方程给出的 $R=m_i/m_f$ 是初始总质量与燃料用尽后飞船静质量之比。题目若问“燃料质量与飞船本身质量之比”，应写成
$$
\eta=\frac{m_i-m_f}{m_f}=R-1.
$$
因此得到 $R=5.87203$ 时，答案是 $\eta=4.87203$，而不是 $5.87203$。第（6）问给“燃料为飞船质量的 $100$ 倍”，初始总质量因而是 $101m_f$。加速、减速两段的质量比各为 $\sqrt{101}$，两段快速度绝对值相等，才能在终点回到近似静止。""",
    },
    "047": {
        1: r"""**把几何约束化成单变量方程。** 由左右对称，设外侧杆与水平夹角为 $\theta_1$，内侧杆为 $\theta_2$。水平投影之和给出
$$
2l(\cos\theta_1+\cos\theta_2)=L.
$$
系统重力势能中，$\theta_1$ 的高度贡献具有权重 $3$，$\theta_2$ 的权重为 $1$。在约束下取势能驻值，得
$$
\tan\theta_1=3\tan\theta_2.
$$
令 $x=\tan\theta_2$，则
$$
\cos\theta_2=\frac1{\sqrt{1+x^2}},
\qquad
\cos\theta_1=\frac1{\sqrt{1+9x^2}}.
$$
几何约束化为
$$
\frac1{\sqrt{1+9x^2}}+
\frac1{\sqrt{1+x^2}}=\frac{L}{2l}=1.6.
$$
左端在 $x>0$ 上严格单调减小，因此正根唯一。数值求得 $x\approx0.375534$，回代原约束可得 $\cos\theta_1+\cos\theta_2=1.600000$。最低点与两手的高度差是两根杆的竖直投影之和：
$$
h=l(\sin\theta_1+\sin\theta_2)\approx0.550\ \mathrm m.
$$""",
        2: r"""**相交时刻的二次方程。** 轨迹为
$$
x=v_0\cos\theta\,t,
\qquad
y=v_0\sin\theta\,t-\frac12gt^2.
$$
顶棚直线由 $(0,h)$ 出发向右下方，方程为 $y=h-x\tan\alpha$。代入轨迹：
$$
\frac12gt^2-v_0(\sin\theta+\cos\theta\tan\alpha)t+h=0.
$$
记 $A=v_0(\sin\theta+\cos\theta\tan\alpha)$，两根
$$
t_{1,2}=\frac{A\mp\sqrt{A^2-2gh}}g.
$$
实体顶棚会在第一次相交时截断轨迹，故必须取减号的较小正根。代入该时刻后，位置应同时满足抛体方程和顶棚直线方程，速度则为
$$
\bm v=(v_0\cos\theta,\ v_0\sin\theta-gt_1).
$$

**用法向坐标求最短时间。** 发射点到顶棚的垂直距离为 $h\cos\alpha$，初速度法向分量为 $v_0\sin(\theta+\alpha)$，重力法向分量为 $-g\cos\alpha$。固定距离与加速度时，首次到达时间随初始法向速度增大而减小，所以应使 $\sin(\theta+\alpha)=1$，得 $\theta=\pi/2-\alpha$。""",
        3: r"""**逐面使用单球面折射式。** 对从折射率 $n_1$ 进入 $n_2$ 的近轴球面，取光传播方向为正，
$$
\frac{n_2}{v}-\frac{n_1}{u}=\frac{n_2-n_1}{R}.
$$
水侧第一面是平面，$R\to\infty$；物在无穷远，$u\to-\infty$。因而 $1/v=0$，经过第一面后仍是平行光。第二面从玻璃 $n$ 进入空气 $1$，入射仍是平行光：
$$
\frac1f=\frac{1-n}{R}.
$$
眼镜度数按焦度的 $100$ 倍记，所以
$$
\mathcal D=100\frac{1-n}{R}.
$$
回到空气后，第一面的两侧分别是空气和玻璃，但它仍是平面，无穷远物的平行束通过后仍平行；第二曲面的介质组合也未变。因此对轴上远物的焦度不变，仍可看清。""",
        4: r"""**Gilbert 模型的远场展开。** 把磁荷 $+q_m$ 和 $-q_m$ 置于 $z=\pm d/2$。轴上场为
$$
B_z=\frac{\mu_0q_m}{4\pi}
\left[\frac1{(z-d/2)^2}-\frac1{(z+d/2)^2}\right].
$$
通分后分子为 $2zd$，分母为 $(z^2-d^2/4)^2$。当 $z\gg d$，
$$
B_z\simeq\frac{\mu_0q_md}{2\pi z^3}
=\frac{\mu_0p_m}{2\pi z^3}.
$$

**Ampere 模型的远场展开。** 圆电流环轴上精确场为
$$
B_z=\frac{\mu_0Ir^2}{2(z^2+r^2)^{3/2}}.
$$
提出 $z^3$ 并保留 $(r/z)^0$ 主项：
$$
B_z\simeq\frac{\mu_0Ir^2}{2z^3}
=\frac{\mu_0p_m}{2\pi z^3},
$$
与磁荷模型相同。

**宏观圆柱中的两种边界源。** 单位体积磁偶极矩为 $M=np_m$。Gilbert 图像在两端面留下面磁荷 $\sigma_m=\pm M$；Ampere 图像在侧面留下束缚面电流 $K_b=M$。对足够长的圆柱，两种源都给出中心场
$$
B=\mu_0M=\mu_0np_m.
$$
这里的等价是远场及宏观平均的等价，不表示两种微观场在源附近处处相同。""",
        5: r"""**先由饱和蒸气压求蒸发量。** 理想蒸气摩尔体积 $V_m=RT/p$，因此题给关系化为
$$
\frac{dp}{dT}=\frac{Lp}{RT^2}.
$$
刚性容器体积不变，蒸气满足 $pV=nRT$。对它微分：
$$
Vdp=RT\,dn+nR\,dT.
$$
初态 $n=1\ \mathrm{mol}$ 且 $V=RT/p$，代入 $dp/dT$ 后
$$
\frac{dn}{dT}
=\frac{L}{RT^2}-\frac1T.
$$
取 $T_0=373.15\ \mathrm K$、$\Delta T=1\ \mathrm K$，
$$
\Delta n\simeq
\left(\frac{L}{RT_0^2}-\frac1{T_0}\right)\Delta T
\approx0.0326\ \mathrm{mol}.
$$

**热量不能把汽化热和气体内能重复相加。** 容器刚性且绝热，电功全部变成系统内能增量。已存在的1 mol液水和1 mol蒸气的显热分别为 $C\Delta T$ 和 $C_v\Delta T$。新蒸发 $\Delta n$ 摩尔时，摩尔汽化热满足
$$
L=\Delta U_{\rm vap}+p\Delta V
\simeq\Delta U_{\rm vap}+RT,
$$
故真正增加的内能是 $(L-RT)\Delta n$。因而
$$
Q=(C+C_v)\Delta T+(L-RT_0)\Delta n,
$$
代入数值得约 $1.33\ \mathrm{kJ}$。""",
        6: r"""**平均场内能中的因子 $1/2$。** 每个格点有 $q$ 个最近邻，若直接用 $Nq$ 计数会把每对相邻格点数两次。独立平均场近似下 $\langle S_iS_j\rangle=m^2$，所以
$$
\langle H\rangle=-\frac12NqJm^2-Nhm.
$$

**用约束极值求概率。** 三种概率满足
$$
P_++P_0+P_-=1,
\qquad
m=P_+-P_-.
$$
多项式计数和 Stirling 近似给出
$$
S=-Nk\sum_{s=+,0,-}P_s\ln P_s.
$$
在 $F=\langle H\rangle-TS$ 中对三个 $P_s$ 变分，并用拉格朗日乘子处理归一化，得
$$
P_s\propto e^{\beta qJms}
$$
。令 $x=e^{\beta qJm}$，即有
$$
P_+:P_0:P_-=x:1:x^{-1}
=x^2:x:1.
$$
由此得正文三个概率表达式及自洽方程。

**临界温度来自零解的斜率。** 在 $m\to0$ 时，$x=e^{qJm/(kT)}=1+qJm/(kT)+O(m^2)$。将自洽方程在 $x=1$ 附近展开，非零无穷小 $m$ 能出现的条件是
$$
1=\frac{2qJ}{3kT_c},
$$
因而
$$
T_c=\frac{2qJ}{3k}.
$$""",
        7: r"""**用柯西不等式得到 $\lambda$ 下界。** 设杆上质量元到 $O$ 的距离为 $s$，则
$$
mr_c=\int s\,dm,
\qquad
I_O=\int s^2\,dm=\lambda mr_c^2.
$$
由
$$
\left(\int s\,dm\right)^2
\le\left(\int dm\right)\left(\int s^2\,dm\right)
$$
得 $m^2r_c^2\le mI_O$，所以 $\lambda\ge1$。等号只在全部质量集中在质心距离处时取到。均匀细杆长为 $L$时 $r_c=L/2$、$I_O=mL^2/3$，因而 $\lambda=4/3$。

**角速度和角加速度。** 若 $O$ 点保持不动，从竖直位置倒至角 $\theta$ 时质心下降 $r_c(1-\cos\theta)$。能量守恒给出
$$
\frac12\lambda mr_c^2\dot\theta^2
=mgr_c(1-\cos\theta),
$$
即
$$
\dot\theta^2=\frac{2g}{\lambda r_c}(1-\cos\theta).
$$
对 $O$ 取力矩则
$$
\lambda mr_c^2\ddot\theta
=mgr_c\sin\theta,
$$
故 $\ddot\theta=g\sin\theta/(\lambda r_c)$。将质心坐标 $x_C=r_c\sin\theta$、$y_C=r_c\cos\theta$ 求两次导数，再代入上述 $\dot\theta^2,\ddot\theta$，便可逐项得到题中各个加速度为零的角度条件。第（7—9）问还要用 $N=m(g+\ddot y_C)$ 检查离地，用 $|f|/N$ 在整个 $0\le\theta\le\pi/2$ 上取最大值，不能只检查端点。""",
        8: r"""**纯滚约束下的动能。** 圆环圆心速度为 $\dot x$，纯滚给出圆环自转角速度 $\dot x/r$。圆环的平动与转动动能之和为 $m\dot x^2$。小球位置可写成
$$
x_b=x-r\sin\beta,
\qquad
y_b=r+r\cos\beta.
$$
求导并展开 $v_b^2$ 后，与圆环动能相加，得
$$
T=\frac32m\dot x^2
-mr\dot x\dot\beta\cos\beta
+\frac12mr^2\dot\beta^2.
$$
重力势能取初态为零后是 $mgr(\cos\beta-1)$，因此能量守恒与正文的二次型相同。

**磁场不做功，但会改变广义动量。** 坐标 $x$ 在水平方向是循环坐标。磁场的矢势项使与 $x$ 共轭的正则动量守恒，初态静止后可写成
$$
3\dot x-r\dot\beta\cos\beta
=\frac{qBr}{m}\cos\beta.
$$
将这一线性方程与能量的二次方程联立，在给定 $\beta$ 时会产生两组 $(\dot x,\dot\beta)$ 根。较大的 $\dot x$ 必须与对应的 $\dot\beta$ 同组取值，不能从两个方程的根表中交叉拼接。小球再次相对圆环静止时 $\dot\beta=0$，代入两个守恒式消去 $\dot x$，才得 $\lambda$ 与 $c=\cos\beta_c$ 的代数方程及临界值。""",
    },
    "050": {
        1: r"""**把数量级假设与精确模型区分开。** 题中的“估算”允许用代表性相对速度代替颗粒减速过程中的瞬时相对速度。若要写成连续模型，设颗粒向下速度为 $v$，反弹分子向上速度为 $v_0$，则应写
$$
m_p\frac{dv}{dt}=-C\eta\rho_0A(v_0+v)^2,
$$
其中 $C$ 取决于冲量转移约定。同时有 $dy/dt=v$，从 $y=h_0,v=v_0$ 积到 $y=0,v=0$ 会给出与估算式同一量级的截止半径。这说明 $r_0\propto\eta(\rho_0/\rho)h_0$ 是稳定结构，而数值系数依赖题设的简化冲量模型。""",
        2: r"""**几何参数的正值检查。** 由 $R>1.5L$ 可得
$$
d^2=R^2-\frac{L^2}{4}>2L^2>0,
$$
因此质心轨迹半径远离零，等效转动惯量
$$
K=M\left(d^2+\frac{L^2}{12}\right)>0.
$$
小振动角频率 $\omega^2=Mgd/K$ 因而为正，最低位置是稳定平衡。当 $L/R\to0$ 时，$d\to R$、$K\to MR^2$，系统退化为一个沿圆弧运动的质点，得 $\omega^2\to g/R$。这一极限同时检查了平动惯量 $Md^2$ 和杆自转惯量 $ML^2/12$ 的组合方式。""",
        3: r"""**速度不出现在 $B_x$ 中的原因。** 磁力始终与速度垂直，粒子通过两个区域时速率大小保持 $v_0$。但第（2）问并非由轨道半径单独决定，而是由轴对称下的正则角动量决定。环形区累积的机械角动量改变是
$$
\Delta L_z=-\frac q{2\pi}\Delta\Phi,
\qquad
\Delta\Phi=\pi B_0(R_2^2-R_1^2),
$$
只含穿过环带的磁通量，不含粒子速率。内区通过圆心的条件又只比较这一 $L_z$ 与 $B_xR_1^2$ 的磁通项，因此 $v_0$ 消去是对称性的直接结果，不是代数偶然。""",
        4: r"""**第（3）问的方程数目。** 铁棍与圆环接触处有法向力 $P$ 和大小 $\mu P$ 的滑动摩擦力；地面提供支持力 $N$ 和静摩擦力 $f$。圆环匀速纯滚，所以需要水平、竖直两个平动方程以及绕圆心的转动方程。滑动摩擦力的方向必须由接触点相对滑动方向决定，不能用“总是阻碍圆环向右”判断。三个平衡方程消去 $N,f$ 后，将 $P(\theta)$ 的分母写成 $A\cos\theta+B\sin\theta$，最小 $P$ 等价于使该线性组合取最大值，从而得正文的正切条件。""",
        5: r"""**二重简并频率的含义。** 约化坐标 $\bm q=(x_1,x_3)^{\mathsf T}$ 的质量矩阵和刚度矩阵分别为
$$
\bm M_q=\frac{\rho Sl^3}{2}
\begin{pmatrix}3&1\\1&3\end{pmatrix},
\qquad
\bm K_q=\frac{\rho gSl^2}{2}
\begin{pmatrix}3&1\\1&3\end{pmatrix}.
$$
因此 $\bm K_q=(g/l)\bm M_q$，特征方程
$$
\det(\bm K_q-\omega^2\bm M_q)=0
$$
化为
$$
\det\bm M_q\left(\frac gl-\omega^2\right)^2=0.
$$
两个独立模态 $(1,1)$ 和 $(1,-1)$ 具有同一频率 $\sqrt{g/l}$，因而任意初始形状的时间依赖都只含这一频率。这是正文可以直接对 $x_1,x_3$ 各写一个简谐方程的根本原因。""",
        6: r"""**光子气体中的单位检查。** 斯特藩—玻尔兹常量 $\sigma$ 的单位为 $\mathrm{W\,m^{-2}\,K^{-4}}$，因此 $\sigma T^4S$ 是功率，再乘 $l/c$ 得能量。除以 $c$ 得动量，最后除以 $M$ 得速度。所以
$$
\frac{\sigma T^4Sl}{Mc^2}
$$
的量纲确为速度。正文中的系数 $2$ 来自辐射角分布与右壁完全反射的综合动量转移，不能再额外乘一次“反射因子 $2$”。以单位链复核能避免把能量密度 $4\sigma T^4/c$ 和出射度 $\sigma T^4$ 混为同一个量。""",
        7: r"""**可见与明亮是两个不同判据。** 可见区域的问法是：对给定物点，是否存在至少一条光线同时穿过两个有限孔径。因此临界光线通常连接两个孔径的相反边缘。明亮区域则额外指定光线穿过 $L_1$ 中心，不再能自由调整初始倾角，只需检查这条特定光线在 $L_2$ 处是否被截断。因此两个半径分别为 $3D_2/2$ 和 $D_2$，差异并非近轴近似误差，而是光线选择条件不同。""",
        8: r"""**与 Born 刚性的对比。** 若要让火车在瞬时共动系中的本征长度恒定，前、后端的本征加速度必须不同：后端较大，前端较小。本题却规定两端在地面系中始终有同一坐标加速度，因而地面系间距 $l$ 恒定，但瞬时共动系的同时切片会与右端更晚的事件相交，得到增大的本征长度。在 $l$ 远小于加速度长度 $c^2/a$ 时，展开精确结果的一阶项才是熟悉的 $L_A\simeq\gamma l$；二阶项保留了同时线穿过有限长火车期间运动状态继续变化的效应。""",
    },
}


def enrich_set(
    set_number: str,
    additions: dict[int, str],
    marker_namespace: str = "CORE_101_REWRITE",
) -> None:
    path = ROOT / f"蔡题{set_number}" / "整理版" / "markdown" / f"蔡题{set_number}_教师备课.md"
    text = path.read_text(encoding="utf-8")
    matches = list(re.finditer(r"(?m)^# 第 (\d+) 题$", text))
    if [int(match.group(1)) for match in matches] != list(range(1, 9)):
        raise RuntimeError(f"第{set_number}套题号异常")
    front = text[: matches[0].start()]
    blocks: list[str] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start() : end].rstrip()
        question = int(match.group(1))
        marker = f"<!-- {marker_namespace}_{set_number}_{question} -->"
        if question in additions and marker not in block:
            sixth = block.find("\n## 六、关键洞察")
            if sixth < 0:
                raise RuntimeError(f"第{set_number}套第{question}题缺少第六模块")
            content = additions[question].strip()
            block = block[:sixth].rstrip() + f"\n\n{marker}\n\n{content}\n" + block[sixth:]
        blocks.append(block)
    path.write_text(front + "\n\n".join(blocks) + "\n", encoding="utf-8")


def main() -> None:
    for set_number, additions in ADDITIONS.items():
        if set(additions) != set(range(1, 9)):
            raise RuntimeError(f"第{set_number}套未覆盖8题")
        enrich_set(set_number, additions)
        print(f"第 {set_number} 套学生核心解析重写完成")
    for set_number, additions in SECOND_ADDITIONS.items():
        if set(additions) != set(range(1, 9)):
            raise RuntimeError(f"第{set_number}套第二轮未覆盖8题")
        enrich_set(set_number, additions, marker_namespace="CORE_101_SECOND")
        print(f"第 {set_number} 套学生核心解析第二轮重写完成")


if __name__ == "__main__":
    main()
