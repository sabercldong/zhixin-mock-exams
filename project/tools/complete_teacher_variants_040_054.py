from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


V: dict[str, dict[int, str]] = {
    "040": {
        1: r"""**变式.** 立方体八个顶点放六个 $+q$ 与两个 $-3q$，求中心场强的最大值。

**解答.** 令顶点符号向量为 $\bm s_i=(\pm1,\pm1,\pm1)$，中心到顶点的距离为 $\sqrt3l/2$。八个顶点都放 $+q$ 时向量和为零；把其中两个电荷由 $+q$ 换成 $-3q$，每个顶点的电荷变化为 $-4q$。因此
$$
\bm E=\frac{16k_eq}{3\sqrt3l^2}(\bm s_1+\bm s_2).
$$
两个不同顶点中，相邻顶点的 $|\bm s_1+\bm s_2|=2\sqrt2$ 最大，故
$$
\boxed{E_{\max}=\frac{32\sqrt2\,k_eq}{3\sqrt3\,l^2}}.
$$
最大值对应两个 $-3q$ 位于同一条棱的两端。""",
        2: r"""**变式.** 求圆环自转角速度满足什么条件时，最低点左侧乘员加速度的摆臂方向分量为零。

**解答.** 正文已得
$$
\bm a_L=(2\Omega\omega r-\Omega^2l)\bm e_r-\omega^2r\bm e_k.
$$
令 $\bm e_r$ 方向系数为零：
$$
2\Omega\omega r-\Omega^2l=0.
$$
当 $\Omega\ne0$ 时，
$$
\boxed{\omega=\frac{\Omega l}{2r}}.
$$
这里 $\omega$ 与 $\Omega$ 必须按同一右手定则取有符号值；异号时科里奥利项与摆臂向心项同向，不可抵消。此时总加速度仍为 $-\omega^2r\bm e_k$，大小不为零。""",
        3: r"""**变式.** 轴线场改为 $B_z=Cz^{-n}$（$z>0,n>0$），求平衡高度和轴向小振动频率。

**解答.** 轴对称无源条件在轴旁给出
$$
B_\rho=-\frac{\rho}{2}\frac{dB_z}{dz}
=\frac{nC\rho}{2z^{n+1}}.
$$
圆环轴向磁力大小为
$$
F_z=2\pi rI B_\rho(r,z)
=\frac{\pi nICr^2}{z^{n+1}}.
$$
选电流方向使磁力向上，平衡条件 $F_z(a)=mg$ 给出
$$
\boxed{a=\left(\frac{\pi nICr^2}{mg}\right)^{1/(n+1)}}.
$$
令 $z=a+\xi$，一阶展开得
$$
m\ddot\xi=-\frac{(n+1)mg}{a}\xi,
$$
所以
$$
\boxed{\omega_s=\sqrt{\frac{(n+1)g}{a}}},
\qquad
\boxed{T_s=2\pi\sqrt{\frac{a}{(n+1)g}}}.
$$""",
        4: r"""**变式.** 当 $OA$ 与 $AB$ 共线同向时，求使剑尖 $B$ 瞬时静止所需的相对角速度 $\omega_2$。

**解答.** $A$ 点速度为 $\omega_1l_1\bm e_\perp$，剑相对地面的绝对角速度为 $\omega_1+\omega_2$，故
$$
\bm v_B=
\left[\omega_1l_1+(\omega_1+\omega_2)l_2\right]\bm e_\perp.
$$
令方括号为零，得
$$
\boxed{\omega_2=-\omega_1\left(1+\frac{l_1}{l_2}\right)}.
$$
负号表明剑必须相对手臂反向转动；且 $|\omega_2|>|\omega_1|$，因为它不仅要消去剑自身随转的速度，还要消去 $A$ 点的平动速度。""",
        5: r"""**变式.** 令两薄透镜焦距相等，即 $f_1=f_2=f$，化简往返成像所需的镜后距离 $h'$。

**解答.** 把 $f_1=f_2=f$ 代入正文的一般式：
$$
h'=\frac{f_2l(2l-3f_1)}
{f_1f_2-3f_1l-f_2l+2l^2},
$$
逐项合并分母，得
$$
\boxed{h'=\frac{fl(2l-3f)}{f^2-4fl+2l^2}}.
$$
分母不为零时这是唯一解。若 $f^2-4fl+2l^2=0$，必须回到 ABCD 矩阵的 $M_{12}$ 检查退化情形，不能把上式强行当作无穷大镜距。""",
        6: r"""**变式.** 在与原题相同的磁场中，求 muon 运动 $N$ 周后的存活比例和衰变比例。

**解答.** 相对论回旋周期为
$$
T_{\rm lab}=\frac{2\pi\gamma m}{eB},
$$
而实验室系半衰期同样膨胀为 $\gamma\tau$。原题选取的 $B$ 使
$$
\frac{T_{\rm lab}}{\gamma\tau}=1.
$$
经过 $N$ 周的存活率因而是
$$
\boxed{P_N=2^{-N}},
$$
衰变比例为
$$
\boxed{1-P_N=1-2^{-N}}.
$$
这一结果与 $\gamma$ 无关，原因是实验室周期和实验室半衰期含有相同的时间膨胀因子。""",
        7: r"""**变式.** 传统灰体屋顶只有外表面能向外辐射，内表面不自行发射，求房间平衡温度。

**解答.** 记 $\varepsilon=1-r$。屋顶只向外发射时，屋顶能量平衡为
$$
\varepsilon I_0S+\varepsilon\sigma T_1^4S
=\varepsilon\sigma T_R^4S.
$$
房间接收屋顶反射回来的 $r\sigma T_1^4S$，但不再接收屋顶内表面辐射，因而
$$
r\sigma T_1^4S
=\sigma T_1^4S+K(T_1-T_0)-\varepsilon I_0S.
$$
整理得
$$
K(T_1-T_0)=\varepsilon I_0S,
$$
即
$$
\boxed{T_1=T_0+\frac{(1-r)I_0S}{K}}.
$$
与双面辐射模型相比，向室内的长波回辐射通道被移除，所以平衡式的结构也随之改变。""",
        8: r"""**变式.** 探测器从半径 $r_p=R_E+h$ 的圆形近地轨道出发，仍进入同一条地球至水星转移轨道，求地球附近点火的速度增量。

**解答.** 设日心转移轨道在地球处的速度为 $v_a$，地球公转速度为 $v_E$。向内转移时的地球双曲线余速大小为
$$
v_\infty=v_E-v_a.
$$
地球双曲线在 $r_p$ 处的近地点速度由能量式给出：
$$
v_{p,h}=\sqrt{v_\infty^2+\frac{2GM_E}{r_p}}.
$$
原先停泊圆轨道速度为
$$
v_c=\sqrt{\frac{GM_E}{r_p}}.
$$
切向顺行点火的速度增量因而为
$$
\boxed{\Delta v_E=
\sqrt{(v_E-v_a)^2+\frac{2GM_E}{r_p}}
-\sqrt{\frac{GM_E}{r_p}}}.
$$""",
    },
    "045": {
        1: r"""**变式.** 已知恒星径向速度半振幅 $K$、行星周期 $T$ 和轨道倾角 $i$，在 $M_p\ll M_S$ 时反求行星质量。

**解答.** 圆轨道径向速度振幅为
$$
K=\left(\frac{2\pi G}{T}\right)^{1/3}
\frac{M_p\sin i}{(M_S+M_p)^{2/3}}.
$$
在 $M_p\ll M_S$ 的一阶近似下，分母取 $M_S^{2/3}$，所以
$$
\boxed{M_p\sin i
=K M_S^{2/3}\left(\frac{T}{2\pi G}\right)^{1/3}}.
$$
观测只能给出 $M_p\sin i$；未知 $i$ 时，令 $\sin i=1$ 所得的是真实质量的下限。""",
        2: r"""**变式.** 把实心圆柱换成空心薄环，求其相对斜面的加速度及维持纯滚动所需的最小静摩擦因数。

**解答.** 在随斜面平动的参考系中，沿斜面向下的等效驱动加速度为
$$
A=g\sin\theta-a_0\cos\theta.
$$
对薄环 $I=MR^2$，纯滚动通式 $a_r=A/(1+I/MR^2)$ 给出
$$
\boxed{a_r=\frac12(g\sin\theta-a_0\cos\theta)}.
$$
摩擦力大小为 $|f|=M|A|/2$，法向力为
$$
N=M(g\cos\theta+a_0\sin\theta).
$$
因而
$$
\boxed{\mu_{s,\min}=
\frac{|g\sin\theta-a_0\cos\theta|}
{2(g\cos\theta+a_0\sin\theta)}}.
$$
若分母非正，物体已不能保持与斜面接触，滚动约束先于摩擦条件失效。""",
        3: r"""**变式.** 固定磁体的轴线场改为 $B(h)=Ch^{-p}$（$p>0$），求竖直平衡高度附近的小振动频率。

**解答.** 反向磁矩的势能取 $U_m=mB=mCh^{-p}$，向上磁力大小为
$$
F_m=-\frac{dU_m}{dh}=pmC h^{-(p+1)}.
$$
平衡时
$$
Mg=pmC h_0^{-(p+1)},
\qquad
\boxed{h_0=\left(\frac{pmC}{Mg}\right)^{1/(p+1)}}.
$$
对 $F_m-Mg$ 在 $h_0$ 处线性化：
$$
F_m(h_0+x)-Mg
=-\frac{(p+1)Mg}{h_0}x+O(x^2).
$$
故
$$
\boxed{\omega_z=\sqrt{\frac{(p+1)g}{h_0}}},
\qquad
\boxed{f_z=\frac1{2\pi}\sqrt{\frac{(p+1)g}{h_0}}}.
$$""",
        4: r"""**变式.** 求第 III 种平衡时两绳段长度及顶角 $\angle ACB$。

**解答.** 两绳段张力等大，合力沿 $\angle ACB$ 的角平分线。作用线通过质心 $H$，故角平分线定理给出
$$
\frac{AC}{CB}=\frac{AH}{HB}=\frac{m_2}{m_1}.
$$
再用 $AC+CB=2a$，得
$$
\boxed{AC=\frac{2am_2}{m_1+m_2}},
\qquad
\boxed{CB=\frac{2am_1}{m_1+m_2}}.
$$
由余弦定理，其中 $AB=2c$：
$$
\boxed{
\cos\angle ACB=
\frac{AC^2+CB^2-4c^2}{2AC\,CB}}.
$$
最后必须检查 $|AC-CB|<2c<AC+CB$；这正是第 III 种构型存在的几何条件。""",
        5: r"""**变式.** 圆柱与接地平面保持电势差 $U$，求接地平面对圆柱的单位长度吸引力。

**解答.** 记
$$
u=\operatorname{arccosh}\frac lr,
\qquad
C'=\frac{2\pi\varepsilon}{u}.
$$
在电压由外电源保持不变时，吸引力大小为
$$
\frac FL=-\frac12U^2\frac{dC'}{dl}.
$$
由
$$
\frac{du}{dl}=\frac1{\sqrt{l^2-r^2}},
\qquad
\frac{dC'}{dl}=-\frac{2\pi\varepsilon}{u^2\sqrt{l^2-r^2}},
$$
得
$$
\boxed{
\frac FL=
\frac{\pi\varepsilon U^2}
{\left[\operatorname{arccosh}(l/r)\right]^2\sqrt{l^2-r^2}}
}.
$$
方向指向接地平面。若改为固定电荷，必须使用 $W=\lambda^2/(2C')$，不可混用固定电压的势能符号。""",
        6: r"""**变式.** 若每个 $A$ 或 $A_2$ 粒子的平均总动能改为 $3kT/2$，其余解离规律不变，求 $T_0<T<2T_0$ 中以初始 $n_0$ 为基准的 $C_V,C_P$。

**解答.** 总粒子物质的量仍为
$$
n=(1+\lambda)n_0=\frac{T}{T_0}n_0.
$$
因而
$$
U=\frac32nRT
=\frac32n_0R\frac{T^2}{T_0},
$$
所以
$$
\boxed{C_V=\frac1{n_0}\frac{dU}{dT}
=3R\frac{T}{T_0}}.
$$
定压时 $pV=n_0RT^2/T_0$，故
$$
p\frac{dV}{dT}=2n_0R\frac{T}{T_0}.
$$
由 $dQ=dU+p,dV$，
$$
\boxed{C_P=5R\frac{T}{T_0}}.
$$
两式的差不是常数 $R$，因为升温时粒子数本身也随解离程度改变。""",
        7: r"""**变式.** 对两同轴圆环之间的膜面令 $g=0$，求小斜率近似下的形状。

**解答.** 无重力时轴对称膜面的线性化平衡方程为
$$
z''+\frac1x z'=0.
$$
两边乘 $x$：
$$
\frac{d}{dx}(xz')=0.
$$
连续积分两次，
$$
z=A\ln x+B.
$$
若边界为 $z(r_1)=z_1,z(r_2)=z_2$，则
$$
\boxed{
z(x)=z_1+
\frac{z_2-z_1}{\ln(r_2/r_1)}
\ln\frac{x}{r_1}}
.
$$
因为定义域是 $r_1\le x\le r_2$ 且 $r_1>0$，$\ln x$ 处处有限，不能用“轴线处发散”的理由删去对数项。""",
        8: r"""**变式.** 局部流速改为 $u(\rho)=\alpha c\rho^2/\rho_0^2$，求近轴有效折射率并判断会聚还是发散。

**解答.** 将正文的一阶速度展开中 $\beta=\rho^2/\rho_0^2$ 换为 $\alpha\rho^2/\rho_0^2$，得
$$
\boxed{n_{\rm eff}(\rho)=
n-\alpha(n^2-1)\frac{\rho^2}{\rho_0^2}}.
$$
近轴射线方程为
$$
y''+\frac{2\alpha(n^2-1)}{n\rho_0^2}y=0.
$$
当 $\alpha>0$ 时，系数为正，射线作横向简谐振荡，首次焦距为
$$
\boxed{f=\frac{\pi\rho_0}{2}
\sqrt{\frac{n}{2\alpha(n^2-1)}}}.
$$
当 $\alpha<0$ 时，方程变为 $y''-\kappa^2y=0$，离轴射线指数式发散，不存在实焦点。""",
    },
    "046": {
        1: r"""**变式.** 求无限长均匀质量圆柱内部 $r<R$ 的引力场和圆轨道速度。

**解答.** 取半径 $r$ 、长度 $L$ 的同轴高斯柱面。包围质量为 $\rho\pi r^2L$，引力高斯定律给出
$$
g(r),2\pi rL=4\pi G\rho\pi r^2L.
$$
因而
$$
\boxed{g(r)=2\pi G\rho r},
$$
方向指向圆柱轴。圆周运动满足
$$
\frac{v^2}{r}=2\pi G\rho r,
$$
所以
$$
\boxed{v(r)=r\sqrt{2\pi G\rho}},
\qquad
\boxed{\Omega=\sqrt{2\pi G\rho}}.
$$
内部所有圆轨道的角速度相同，类似于谐振子势场；在 $r=R$ 处与外部结果 $v=R\sqrt{2\pi G\rho}$ 连续。""",
        2: r"""**变式.** 车厢向右加速度 $a$ 缓慢增大，墙面光滑，画出静止阶段地面摩擦力和墙面支持力随 $a$ 的变化，并求开始滑动的加速度。

**解答.** 在车厢系中对质心列平动平衡，再对质心列力矩平衡，得
$$
\boxed{f(a)=\frac{mah}{r}},
\qquad
\boxed{N_w(a)=\frac{ma(r-h)}{r}}.
$$
两者在静止阶段都从原点开始随 $a$ 线性增大。竖直方向有 $N=mg$，因此地面静摩擦的极限条件为
$$
\frac{ma_ch}{r}=\mu mg.
$$
所以
$$
\boxed{a_c=\frac{\mu gr}{h}}.
$$
当 $0\le a\le a_c$ 时可保持相对车厢静止；超过 $a_c$ 后应改用动摩擦并重新列平动和转动方程。""",
        3: r"""**变式.** 把两根线电荷改为同号 $+\lambda$，求 $y$ 轴上 $(0,y)$ 点的电场。

**解答.** 通过 $(a,0)$ 的线电荷在该点的电场为
$$
\bm E_+=\frac{\lambda}{2\pi\varepsilon_0}
\frac{-a\bm e_x+y\bm e_y}{a^2+y^2},
$$
通过 $(-a,0)$ 的线电荷贡献为
$$
\bm E_-=\frac{\lambda}{2\pi\varepsilon_0}
\frac{a\bm e_x+y\bm e_y}{a^2+y^2}.
$$
相加后 $x$ 分量抵消，得
$$
\boxed{\bm E(0,y)=
\frac{\lambda y}{\pi\varepsilon_0(a^2+y^2)}\bm e_y}.
$$
$y>0$ 时向上，$y<0$ 时向下；这与原题异号电荷在 $y$ 轴上留下水平分量的情形正好互补。""",
        4: r"""**变式.** 在静止 U 形管中加入与液体体积速度成正比的小黏滞阻力，建立液面差坐标 $x$ 的阻尼振动方程。

**解答.** 管内全部液体以速率 $\dot x$ 运动，等效惯性系数为
$$
M_{\rm eff}=\rho A(3l+h),
$$
两自由液面的重力恢复系数为
$$
K_{\rm eff}=2\rho Ag.
$$
若黏滞广义力写成 $-b\dot x$，则
$$
\boxed{\rho A(3l+h)\ddot x+b\dot x+2\rho Agx=0}.
$$
令
$$
\gamma=\frac{b}{2\rho A(3l+h)},
\qquad
\omega_1^2=\frac{2g}{3l+h},
$$
方程化为 $\ddot x+2\gamma\dot x+\omega_1^2x=0$。欠阻尼时实际角频率为 $\sqrt{\omega_1^2-\gamma^2}$。""",
        5: r"""**变式.** 导轨改为 $y=k|x|^m$（$m>0$），求棒以恒速 $v$ 运动时 $\mathcal E(t)$、$I(t)$ 和外力功率的时间标度。

**解答.** 在 $y=vt$ 处两交点为
$$
x_\pm=\pm\left(\frac{vt}{k}\right)^{1/m},
$$
导体棒长度
$$
L(t)=2\left(\frac{vt}{k}\right)^{1/m}.
$$
由运动电动势
$$
\boxed{\mathcal E(t)=BvL(t)\propto t^{1/m}}.
$$
棒的电阻 $R=\lambda L$，因而
$$
\boxed{I(t)=\frac{Bv}{\lambda}},
$$
仍与时间无关。外力功率等于焦耳热功率：
$$
\boxed{P(t)=\mathcal EI
=\frac{2B^2v^2}{\lambda}
\left(\frac{vt}{k}\right)^{1/m}\propto t^{1/m}}.
$$""",
        6: r"""**变式.** 把球形余弦发光体改为任意光滑凸面，说明远处观察亮度仍均匀的条件。

**解答.** 局部面元向观察方向发出的能量为
$$
dE=I_0\cos\theta,d\Omega,dS,dt.
$$
它在垂直于视线的像平面上投影面积为
$$
dS_\perp=dS\cos\theta.
$$
因而每单位投影面积、单位立体角的能量为
$$
\frac{dE}{d\Omega,dS_\perp,dt}=I_0,
$$
与表面位置和法线倾角无关。成立条件是：表面局部满足余弦定律、从观察方向看每条视线只与可见表面相交一次，且没有额外吸收或遮挡。""",
        7: r"""**变式.** 对水滴折射率 $n=4/3$，求第一级和第二级虹的驻值入射角。

**解答.** 第 $N$ 级虹的驻值条件与斯涅尔定律联立后给出
$$
\sin^2\alpha_{Nm}
=\frac{(N+1)^2-n^2}{N(N+2)}.
$$
对 $N=1$：
$$
\sin^2\alpha_{1m}=\frac{4-16/9}{3}=\frac{20}{27},
$$
故
$$
\boxed{\alpha_{1m}=\arcsin\sqrt{\frac{20}{27}}\approx59.4^\circ}.
$$
对 $N=2$：
$$
\sin^2\alpha_{2m}=\frac{9-16/9}{8}=\frac{65}{72},
$$
故
$$
\boxed{\alpha_{2m}=\arcsin\sqrt{\frac{65}{72}}\approx71.9^\circ}.
$$
两个根都在 $0<\alpha<\pi/2$ 的物理区间内。""",
        8: r"""**变式.** 将质子反应质量流率由 $1\,\mathrm{g,s^{-1}}$ 增大到 $10\,\mathrm{g,s^{-1}}$，求最大推力和低速时的本征加速度。

**解答.** 单次反应的喷射动量不变，反应数率与质子质量流率成正比，所以推力也成正比。利用原题
$$
F_1=3.43244\times10^4\,\mathrm N,
$$
得
$$
\boxed{F_{10}=10F_1
=3.43244\times10^5\,\mathrm N}.
$$
设飞船当时静质量为 $m_0$，在低速极限 $\gamma_v\simeq1$，本征加速度与坐标加速度相同：
$$
\boxed{a_0=\frac{F_{10}}{m_0}
=\frac{3.43244\times10^5}{m_0}\,\mathrm{m,s^{-2}}}.
$$
质量必须用千克代入。""",
    },
    "047": {
        1: r"""**变式.** 保持平衡构型，令两手距离 $L\to4l^-$，求最低点下降量 $h$ 的渐近式及灵敏度 $dh/dL$。

**解答.** 接近完全伸直时 $\theta_1,\theta_2\ll1$，平衡条件 $\tan\theta_1=3\tan\theta_2$ 化为 $\theta_1\simeq3\theta_2$。记 $\delta=4l-L$，由水平投影
$$
\delta=2l\left[2-\cos\theta_1-\cos\theta_2\right]
\simeq l(\theta_1^2+\theta_2^2)
=10l\theta_2^2.
$$
同时
$$
h=l(\sin\theta_1+\sin\theta_2)
\simeq4l\theta_2.
$$
因而
$$
\boxed{h\simeq4\sqrt{\frac{l(4l-L)}{10}}},
$$
$$
\boxed{\frac{dh}{dL}\simeq
-2\sqrt{\frac{l}{10(4l-L)}}}.
$$
当 $L\to4l^-$ 时导数绝对值发散，说明折尺接近伸直时对手间距离极其敏感。""",
        2: r"""**变式.** 求本题中首次到达屋面时间最短的发射角及该最短时间。

**解答.** 交点方程为
$$
\frac12gt^2-v_0
(\sin\theta+\cos\theta\tan\alpha)t+h=0.
$$
要使较小正根最小，应使
$$
\sin\theta+\cos\theta\tan\alpha
=\frac{\sin(\theta+\alpha)}{\cos\alpha}
$$
最大，故
$$
\boxed{\theta_{\min}=\frac\pi2-\alpha=60^\circ}.
$$
此时 $v_0A=40/\cos30^\circ=80/\sqrt3$，取二次方程的较小正根：
$$
\boxed{t_{\min}=
\frac{80/\sqrt3-
\sqrt{(80/\sqrt3)^2-2gh}}{g}
\simeq0.337\,\mathrm s}.
$$
较大根对应抛体若未在首次相交处被屋面截断时的第二交点，不是题求时间。""",
        3: r"""**变式.** 若水侧表面也有有符号曲率半径 $R_1$，眼侧表面半径为 $R_2$，求水中薄透镜的总焦度。

**解答.** 光从折射率 $n_w$ 的水进入折射率 $n$ 的镜片，再进入折射率 $n_e$ 的眼侧介质。薄镜近似下两界面焦度直接相加：
$$
\boxed{\Phi=
\frac{n-n_w}{R_1}+
\frac{n_e-n}{R_2}}.
$$
$R_1,R_2$ 必须按光的传播正方向取有符号值。当水侧表面为平面时 $R_1\to\infty$，第一项消失，便还原原题。这也说明平面界面会改变单条斜光的方向，却不产生光焦度。""",
        4: r"""**变式.** 保留电流环轴线场的首个高阶修正，并说明它为何依赖环半径 $r$。

**解答.** 圆环轴线场的精确式为
$$
B_z=\frac{\mu_0Ir^2}{2(z^2+r^2)^{3/2}}
=\frac{\mu_0p_m}{2\pi z^3}
\left(1+\frac{r^2}{z^2}\right)^{-3/2}.
$$
对 $r^2/z^2\ll1$ 作二项展开：
$$
\boxed{B_z=
\frac{\mu_0p_m}{2\pi z^3}
\left[1-\frac32\frac{r^2}{z^2}
+O\!\left(\frac{r^4}{z^4}\right)\right]}.
$$
首项只含总磁矩 $p_m=I\pi r^2$，是普适偶极远场；次项已能辨认电流分布的有限尺寸，因而必须显式含 $r$。""",
        5: r"""**变式.** 若刚性容器体积随温度缓慢变化为 $V(T)$，推导两相共存时 $dn/dT$ 的一般式。

**解答.** 饱和蒸气满足
$$
n=\frac{p(T)V(T)}{RT}.
$$
对数求导：
$$
\frac1n\frac{dn}{dT}
=\frac1p\frac{dp}{dT}
+\frac1V\frac{dV}{dT}-\frac1T.
$$
克劳修斯—克拉珀龙关系在理想蒸气近似下给出
$$
\frac1p\frac{dp}{dT}=\frac{L}{RT^2}.
$$
因而
$$
\boxed{
\frac{dn}{dT}=n\left[
\frac{L}{RT^2}+\frac1V\frac{dV}{dT}-\frac1T
\right]}.
$$
令 $dV/dT=0$ 就还原原题的定容结果。公式只在液相尚未耗尽、系统始终保持饱和平衡时成立。""",
        6: r"""**变式.** 在顺磁相中加很弱的外场 $h$，求线性磁化率并考察 $T\to T_c^+$ 的行为。

**解答.** 平均场中令
$$
x=\beta(qJm+h).
$$
三态自旋的平均值为
$$
m=\frac{2\sinh x}{1+2\cosh x}.
$$
顺磁相中 $x\ll1$，故
$$
m\simeq\frac23\beta(qJm+h).
$$
解出 $m=\chi h$：
$$
\chi=\frac{2\beta/3}{1-2\beta qJ/3}.
$$
利用 $kT_c=2qJ/3$，得
$$
\boxed{\chi=\frac{2}{3k(T-T_c)}}.
$$
因此 $T\to T_c^+$ 时 $\chi\propto(T-T_c)^{-1}$ 发散，表明临界点附近很弱的外场也能产生很大的磁化响应。""",
        7: r"""**变式.** 在地面接触且不滑动的情形中取 $\lambda=2$，求摩擦力换向时的杆倾角。

**解答.** 正文得到水平摩擦力
$$
f=\frac{mg}{\lambda}\sin\theta(3\cos\theta-2).
$$
在倒下过程 $0<\theta<\pi/2$ 中 $\sin\theta>0$，所以换向点由
$$
3\cos\theta-2=0
$$
确定：
$$
\boxed{\theta_f=\arccos\frac23\approx48.2^\circ}.
$$
这个结果实际上与 $\lambda$ 无关；$\lambda=2$ 只影响摩擦力和支持力的数值比。换向点也不是 $|f|/N$ 最大的最危险点。""",
        8: r"""**变式.** 对 $\lambda>4$ 的非零相对静止位置，求 $\lambda\to\infty$ 时 $\cos\beta_c$ 的渐近式。

**解答.** 物理根为
$$
c=\cos\beta_c=
\frac{\lambda+3-\sqrt{\lambda^2-3\lambda}}{\lambda+1}.
$$
根号作大 $\lambda$ 展开：
$$
\sqrt{\lambda^2-3\lambda}
=\lambda\sqrt{1-\frac3\lambda}
=\lambda-\frac32-\frac{9}{8\lambda}+O(\lambda^{-2}).
$$
代回后
$$
c=\frac{\dfrac92+\dfrac{9}{8\lambda}+O(\lambda^{-2})}
{\lambda+1}.
$$
因而首项为
$$
\boxed{\cos\beta_c\sim\frac{9}{2\lambda}}.
$$
强磁场极限下 $\cos\beta_c\to0^+$，即再次相对静止的位置趋近圆环侧点，与定义域 $0<c\le1$ 相容。""",
    },
    "050": {
        1: r"""**变式.** 若空气分子撞上颗粒后完全吸附，而不是镜面弹回，求圆柱颗粒的新截止半径。

**解答.** 完全弹回时单位质量空气的动量改变为 $2U$；完全吸附时只为 $U$，因而平均力和颗粒减速度都减半。截止条件 $v_0^2/(2a)=h_0$ 表明临界半径与力的形状系数成正比，故
$$
\boxed{r_{0,\rm abs}=\frac12r_0
=\frac{4\eta\rho_0h_0}{\rho}}.
$$
代入题给数据：
$$
\boxed{r_{0,\rm abs}=2.58\times10^{-6}\,\mathrm m
\simeq2.6\,\mu\mathrm m}.
$$""",
        2: r"""**变式.** 把均匀细杆改为质量集中在两端的哑铃，总质量仍为 $M$，求最低位置附近的小振动周期。

**解答.** 长为 $L$ 的弦中点到碗心的距离为
$$
d=\sqrt{R^2-\frac{L^2}{4}}.
$$
哑铃绕质心的转动惯量为 $I_C=ML^2/4$，以构型角 $\theta$ 为广义坐标时的总惯性系数为
$$
I_O=Md^2+\frac14ML^2=MR^2.
$$
重力势能在最低点附近为
$$
U\simeq\frac12Mgd\theta^2.
$$
故
$$
\omega^2=\frac{Mgd}{MR^2}=\frac{gd}{R^2},
$$
$$
\boxed{T=\frac{2\pi R}{\sqrt{gd}}},
\qquad
d=\sqrt{R^2-L^2/4}.
$$""",
        3: r"""**变式.** 若粒子带电量改为 $q<0$，说明环形区临界速度大小和轨迹弯曲方向如何改变。

**解答.** 拉莫尔半径的大小是
$$
\rho_c=\frac{mv_0}{|q|B_0}.
$$
临界内切几何仅涉及 $\rho_c$ 的大小：
$$
\rho_c=\frac{R_2^2-R_1^2}{2R_1}.
$$
因而
$$
\boxed{v_{0\min}=
\frac{|q|B_0}{m}
\frac{R_2^2-R_1^2}{2R_1}},
$$
与正电粒子的速度大小相同。但洛伦兹力 $q\bm v\times\bm B$ 整体反向，轨迹圆心转到入射半径的另一侧，所有带方向的角动量与 $B_x$ 符号结论都应同时重新核对。""",
        4: r"""**变式.** 把越障物体改为半径 $r$、质量 $m$ 的均匀圆盘，求翻过高为 $h$ 的台阶所需的最小入射速度。

**解答.** 碰撞前圆盘纯滚动，$I_C=mr^2/2$、$\omega=v/r$。对台阶棱角 $A$ 取矩，碰撞瞬间角动量守恒：
$$
L_A^-=mv(r-h)+I_C\frac vr
=mv\left(\frac{3r}{2}-h\right).
$$
碰后绕 $A$ 的转动惯量为
$$
I_A=I_C+mr^2=\frac32mr^2.
$$
碰后动能是 $L_A^{-2}/(2I_A)$。临界翻越要求该动能等于 $mgh$，故
$$
\boxed{v_{\min}=
\frac{r\sqrt{3gh}}{\frac32r-h}}.
$$
当 $h\to0$ 时 $v_{\min}\to0$，符合台阶消失的极限。""",
        5: r"""**变式.** 初态改为 $x_1(0)=\varepsilon$、$x_3(0)=-\varepsilon$、$x_2(0)=0$，且三个液柱初速均为零，求全部液面运动。

**解答.** 体积约束为
$$
x_1+2x_2+x_3=0.
$$
给定初态已满足该约束，且属于左右反对称模态，因而中管始终不动：$x_2(t)=0$。两个独立小振动模式都有
$$
\omega=\sqrt{\frac gl}.
$$
结合零初速得
$$
\boxed{x_1(t)=\varepsilon\cos\!\left(\sqrt{\frac gl},t\right)},
$$
$$
\boxed{x_3(t)=-\varepsilon\cos\!\left(\sqrt{\frac gl},t\right)},
\qquad
\boxed{x_2(t)=0}.
$$
任意时刻三式都满足体积约束。""",
        6: r"""**变式.** 求 $t\to0^+$ 时右壁获得的动量速率 $\Delta P/t$ 的极限，并与初始平衡压力比较。

**解答.** 在极短时间内，只有原先就在右壁附近、速度指向右壁的分子发生碰撞。对麦克斯韦分布积分，单位时间、单位面积的法向动量通量正是平衡压强 $p_0$。因而
$$
\boxed{\lim_{t\to0^+}\frac{\Delta P}{t}=p_0S}.
$$
左壁被撤去的信息需要有限的分子飞行时间才能影响右壁，所以初始瞬间的力仍等于原先密闭平衡气体的压力 $p_0S$。""",
        7: r"""**变式.** 保持焦距和距离不变，令 $D_1/D_2=\lambda$，求孔径光阑发生切换的临界 $\lambda$。

**解答.** 对轴上物点发出的近轴光线，两镜允许的初始倾角分别为
$$
|u|\le\frac{D_1}{12f},
\qquad
|u|\le\frac{D_2}{6f}.
$$
切换时两个上限相等：
$$
\frac{\lambda D_2}{12f}=\frac{D_2}{6f}.
$$
因而
$$
\boxed{\lambda_c=2}.
$$
当 $\lambda<2$ 时，$L_1$ 折算到物方的允许角更小，故 $L_1$ 是孔径光阑；当 $\lambda>2$ 时，$L_2$ 是孔径光阑。临界时两镜同时限光。""",
        8: r"""**变式.** 反过来要求火车保持 Born 刚性，求沿车长不同位置所需的本征加速度分布。

**解答.** 令左端的本征加速度为 $a_0$，$\xi$ 是左端瞬时静止系中沿车身向右的本征距离。Born 刚性要求同一瞬时静止截面上各点的固有距离不变，对应 Rindler 加速度分布
$$
\boxed{a(\xi)=\frac{a_0}{1+a_0\xi/c^2}}.
$$
因而车头必须比车尾的本征加速度小。长度为 $l$ 时
$$
a_R=\frac{a_0}{1+a_0l/c^2}.
$$
若两端反而采用相同的地面系坐标加速度，就不满足这一空间分布，因而不能保持 Born 刚性。""",
    },
    "051": {
        1: r"""**变式.** 两带轮的圆锥完整顶角分别为 $\theta_1,\theta_2$，求初始传动比，并说明有限轴距时为何 $d_2'=d_2+x$ 不再严格。

**解答.** 两带轮的工作半径分别是
$$
r_1=\frac{l-d_1}{2}\tan\frac{\theta_1}{2},
\qquad
r_2=\frac{l-d_2}{2}\tan\frac{\theta_2}{2}.
$$
无滑动条件 $\omega_1r_1=\omega_2r_2$ 给出
$$
\boxed{
\frac{\omega_2}{\omega_1}=
\frac{(l-d_1)\tan(\theta_1/2)}
{(l-d_2)\tan(\theta_2/2)}}.
$$
有限轴距 $L$ 时，开式带路长度不只是 $2L+\pi(r_1+r_2)$：两段公切线长度和两轮包角都随 $r_1-r_2$ 改变。因而精确的 $d\mathcal L=0$ 不再等价于 $dr_1+dr_2=0$，只在 $L\gg r_1,r_2$ 的一阶近似下才得 $d_2'=d_2+x$。""",
        2: r"""**变式.** 把吃水深度改为 $\delta r$（$0<\delta<1$），求半圆柱船竖直小振动周期的一般式。

**解答.** 水面到圆心的有符号高度为 $y_w=(\delta-1)r$。水线半弦长为
$$
x_w=\sqrt{r^2-y_w^2}
=r\sqrt{1-(1-\delta)^2},
$$
故单位轴向长度的水线宽度为
$$
b=2r\sqrt{1-(1-\delta)^2}.
$$
浸水截面面积是圆弓面积
$$
A_s=r^2\left[
\arccos(1-\delta)-(1-\delta)
\sqrt{1-(1-\delta)^2}
\right].
$$
竖直位移 $z$ 产生浮力增量 $\rho_0gbz$，而 $M=\rho_0A_s$ 按单位长度计。因而
$$
\boxed{T_1=2\pi\sqrt{\frac{A_s}{gb}}}.
$$
代入 $\delta=8/13$ 即还原正文结果。""",
        3: r"""**变式.** 绳子从顶部对称中点出发，只包覆到方位角 $\alpha_0$ 就离开圆柱，求几何自锁的临界角。

**解答.** 临界状态中摩擦约束处处取等号，切线与轴向的夹角 $\psi$ 满足
$$
\frac{d\psi}{d\alpha}=-\mu\sin\psi.
$$
对称中点的边界条件是 $\psi(0)=\pi/2$，离开点有 $\psi(\alpha_0)=\theta_c$。分离变量积分：
$$
\int_{\pi/2}^{\theta_c}\frac{d\psi}{\sin\psi}
=-\mu\int_0^{\alpha_0}d\alpha.
$$
利用 $\int\csc\psi,d\psi=\ln\tan(\psi/2)$，得
$$
\ln\tan\frac{\theta_c}{2}=-\mu\alpha_0.
$$
因而
$$
\boxed{\theta_c=2\arctan(e^{-\mu\alpha_0})},
$$
可自锁的角度范围为 $\theta_c\le\theta\le\pi/2$。""",
        4: r"""**变式.** 令质量比 $m/M$ 逐渐增大，求三角拉格朗日点稳定性丧失时的临界质量比，并求两支线性振动频率。

**解答.** 记
$$
q=\frac{Mm}{(M+m)^2}.
$$
特征频率为
$$
\boxed{\nu_\pm^2=\frac{\Omega^2}{2}
\left(1\pm\sqrt{1-27q}\right)}.
$$
稳定要求根号内非负，即 $q\le1/27$。令 $\rho=m/M\le1$，临界时
$$
\frac{\rho}{(1+\rho)^2}=\frac1{27},
$$
解得物理根
$$
\boxed{\left(\frac mM\right)_c
=\frac{25-\sqrt{621}}2\approx0.0401}.
$$
当 $q\to0$时，$\nu_+\to\Omega$，而 $\nu_-\simeq\Omega\sqrt{27q/4}\to0$，分别对应快振动与趋慢的漂移模式。""",
        5: r"""**变式.** 把 $H$ 到顶点 $D$ 的电容改为 $2C$，并令匀强磁场绕任意固定轴旋转，判断电容是否充电。

**解答.** 在体心为原点的对称规范中，沿棱 $ij$ 的感应电动势正比于
$$
\mathcal E_{ij}\propto-\dot{\bm B}\cdot(\bm r_i\times\bm r_j).
$$
对任一顶点 $i$，其余三个顶点满足 $\sum_{j\ne i}\bm r_j=-\bm r_i$，所以
$$
\sum_{j\ne i}\mathcal E_{ij}
\propto-\dot{\bm B}\cdot
\left[\bm r_i\times\sum_{j\ne i}\bm r_j\right]=0.
$$
因而节点源向量对任意 $\dot{\bm B}$ 方向都是零。所有顶点与 $H$ 保持等电势是唯一稳态解，即
$$
\boxed{V_A=V_B=V_C=V_D=V_H}.
$$
所以即使一只电容变为 $2C$，各电容电压仍为零，不会充电；改变的只是若有非零节点电压时的瞬态时常。""",
        7: r"""**变式.** 求星形线左下象限从 $A=(-1,0)$ 到 $B=(0,-1)$ 这段弧的弧长。

**解答.** 参数范围是 $\pi\le\varphi\le3\pi/2$。导数为
$$
x'=-3\cos^2\varphi\sin\varphi,
\qquad
y'=3\sin^2\varphi\cos\varphi.
$$
因而
$$
ds=\sqrt{x'^2+y'^2},d\varphi
=3|\sin\varphi\cos\varphi|,d\varphi.
$$
在该象限 $\sin\varphi<0,\cos\varphi<0$，乘积为正，故
$$
\begin{aligned}
s_{AB}
&=3\int_\pi^{3\pi/2}\sin\varphi\cos\varphi,d\varphi\\
&=\frac32\left[\sin^2\varphi\right]_\pi^{3\pi/2}
=\frac32.
\end{aligned}
$$
即
$$
\boxed{s_{AB}=\frac32}.
$$
整条星形线由四象限对称组成，总周长为 $6$。""",
        8: r"""**变式.** 把一块板的边界条件由波节改为波腹，保留 $p$ 个模，求允许波数、总零点能和力的大小。

**解答.** 一端波节、一端波腹时，
$$
\boxed{k_n=\frac{(n+1/2)\pi}{d}},
\qquad n=0,1,\ldots,p-1.
$$
有限和为
$$
\sum_{n=0}^{p-1}\left(n+\frac12\right)=\frac{p^2}{2}.
$$
因而
$$
E=\frac12\sum\hbar ck_n
=\boxed{\frac{\pi\hbar c}{4d}p^2}.
$$
对 $d$ 求导，作用力大小为
$$
\boxed{|F|=\left|-\frac{dE}{dd}\right|
=\frac{\pi\hbar c}{4d^2}p^2}.
$$
符号取决于题目对板间距离增大方向的正方向规定；上式报告其大小。""",
    },
    "053": {
        1: r"""**变式.** 两颗星质量改为 $m_1,m_2$，分别位于 $(x,0)$ 和 $(0,y)$，考察质量加权质心是否仍作严格平方反比中心力运动。

**解答.** 在各自允许的轴向上，
$$
\ddot x=-\frac{Gm_2x}{(x^2+y^2)^{3/2}},
\qquad
\ddot y=-\frac{Gm_1y}{(x^2+y^2)^{3/2}}.
$$
质心坐标是
$$
\bm R=\left(\frac{m_1x}{m_1+m_2},
\frac{m_2y}{m_1+m_2}\right),
$$
其加速度为
$$
\ddot{\bm R}=-\frac{Gm_1m_2}{m_1+m_2}
\frac{(x,y)}{(x^2+y^2)^{3/2}}.
$$
一般时 $(x,y)$ 与 $\bm R$ 不平行，因此这不是关于原点的中心加速度，更不能写成 $-\mu\bm R/R^3$。只有 $m_1=m_2$（或运动始终退化在某一坐标轴上）时，两向量才保持平行，原题的严格开普勒等效才成立。""",
        2: r"""**变式.** 法向力分布为 $dN=k\rho^p,d\rho$（$p>-1$），求干摩擦稳态中滑动换向半径 $\lambda R$ 和圆盘角速度。

**解答.** 摩擦力矩微元为 $d\tau=\mu\rho,dN=\mu k\rho^{p+1}d\rho$。稳态时换向点内外两部分力矩大小相等：
$$
\int_0^{\lambda R}\rho^{p+1}d\rho
=\int_{\lambda R}^{R}\rho^{p+1}d\rho.
$$
因而
$$
2\lambda^{p+2}=1,
\qquad
\boxed{\lambda=2^{-1/(p+2)}}.
$$
换向点的相对速度为零，故
$$
\omega(\lambda R)=\omega_0r=\omega_0nR.
$$
所以
$$
\boxed{\frac\omega{\omega_0}
=\frac n\lambda=n,2^{1/(p+2)}}.
$$
$p$ 增大时压力更集中于外缘，$\lambda\to1$，而 $\omega/\omega_0\to n$。""",
        3: r"""**变式.** 若薄壳是电阻有限的导体，说明电荷运动与能量分配将如何改变。

**解答.** 绝缘壳上的面电荷被束缚在材料上，可与壳刚性共转。导体中的电荷却会在感生切向电场下重新分布，直到由电阻、自感和机械驱动共同决定的瞬态电流；因而不能再直接写 $K=\sigma\omega R$。磁场和附加电磁惯量也会随频率与电阻改变。

能量守恒必须改写为
$$
\boxed{mgH=E_k+E_{\rm em}+Q_J},
$$
其中
$$
Q_J=\int I_s^2(t)R_{\rm eff},dt>0.
$$
因而正文理想绝缘模型中“机械动能 $+$ 电磁场能”的二项闭合不再成立，有一部分势能不可逆地转化为焦耳热。""",
        4: r"""**变式.** 在 $\omega_0=1/\sqrt{LC}$ 下把图（b）中间电阻换成复阻抗 $Z_b$，求干路电流与电源同相的条件。

**解答.** 原方程中只需把桥臂电阻 $R$ 换为 $Z_b$，得
$$
\widetilde I_1=-i\frac r{Z_b}\widetilde I,
\qquad
Z_{\rm in}=R+\frac{r^2}{Z_b}.
$$
干路电流与电源同相要求 $Z_{\rm in}$ 为正实数。由于 $R,r^2$ 都为正实数，被动桥臂中等价条件是
$$
\boxed{Z_b\in\mathbb R_{>0}}.
$$
当 $Z_b\to\infty$ 时，$Z_{\rm in}\to R$、$\widetilde I_1\to0$，桥臂开路；当 $Z_b\to0^+$ 时，$Z_{\rm in}\to\infty$、$\widetilde I\to0$，但
$$
\widetilde I_1\to-i\frac{U_0}{r},
$$
桥臂电流保持有限且滞后电源 $\pi/2$。""",
        5: r"""**变式.** 保留一般 $a,b,c>0$，求正截止速率、内部最概然速率和归一化常数。

**解答.** 概率密度化为
$$
f(v)=A(-av^2+bv+c).
$$
正截止根为
$$
\boxed{v_j=\frac{b+\sqrt{b^2+4ac}}{2a}}.
$$
内部驻点由 $-2av+b=0$ 给出：
$$
\boxed{v_p=\frac b{2a}}.
$$
因 $a,b,c>0$，有 $0<v_p<b/a<v_j$，且 $f''=-2aA<0$，所以它必然是允许区间内的最概然速率。归一化条件给出
$$
1=A\int_0^{v_j}(-av^2+bv+c),dv,
$$
因而
$$
\boxed{A=\left(
-\frac a3v_j^3+\frac b2v_j^2+cv_j
\right)^{-1}}.
$$""",
        8: r"""**变式.** 带电细杆只在 $a<|x|<L/2$ 的两段上有线电荷密度 $\lambda$，求磁场变化过程中的总力矩。

**解答.** 法拉第电场在 $x<r$ 时为 $E_\varphi=-x\dot B/2$，在 $x>r$ 时为 $E_\varphi=-r^2\dot B/(2x)$。两侧杆元的力矩同向，故
$$
M=2\int_a^{L/2}\lambda xE_\varphi(x),dx.
$$
当 $a<r$ 时，
$$
\boxed{M=-\lambda\dot B\left[
\frac{r^3-a^3}{3}+r^2\left(\frac L2-r\right)
\right]}.
$$
当 $a\ge r$ 时，
$$
\boxed{M=-\lambda r^2\dot B
\left(\frac L2-a\right)}.
$$
时间积分后 $\int Mdt$ 只含 $\int(-\dot B)dt=B_0-B_f$，因而最终角速度仍只依赖磁场总变化量，不依赖 $B(t)$ 的具体时间形状。""",
    },
    "054": {
        1: r"""**变式.** 把细丝形状改为 $r=e^{k\theta}$，$0\le\theta\le2\pi$，求一般弧长、转动惯量和切线夹角，并检查 $k\to0$ 极限。

**解答.** $dr/d\theta=kr$，因而
$$
ds=\sqrt{dr^2+r^2d\theta^2}
=\sqrt{1+k^2},e^{k\theta}d\theta.
$$
故
$$
\boxed{l=\frac{\sqrt{1+k^2}}{k}
(e^{2\pi k}-1)}.
$$
质量均匀沿线分布时
$$
I=\frac ml\int_0^{2\pi}r^2ds
=\boxed{\frac m3
\frac{e^{6\pi k}-1}{e^{2\pi k}-1}}
=\boxed{\frac m3(e^{4\pi k}+e^{2\pi k}+1)}.
$$
切向量的径向分量与环向分量之比为 $k$，所以切线与环向夹角
$$
\boxed{\chi=\arctan k}.
$$
当 $k\to0$时，$l\to2\pi$、$I\to m$、$\chi\to0$，正好趋近半径为 $1$ 的完整圆周。""",
        2: r"""**变式.** 将车轮与棱角的法向恢复系数改为 $e$，写出可用于求碰后状态的完整冲量方程组。

**解答.** 设碰撞轮与固定棱角接触点的法向、切向单位矢量为 $\bm n,\bm t$，棱角对车轮的冲量为
$$
\bm J=J_n\bm n+J_t\bm t.
$$
对整车写线冲量和角冲量方程：
$$
M_{\rm tot}(\bm V_C^+-\bm V_C^-)=\bm J,
$$
$$
\bm I_C(\bm\omega^+-\bm\omega^-)
=(\bm r_P-\bm r_C)\times\bm J.
$$
恢复系数条件必须施加在接触点法向相对速度上：
$$
\boxed{\bm v_P^+\cdot\bm n
=-e\,\bm v_P^-\cdot\bm n},
\qquad
\bm v_P=\bm V_C+\bm\omega\times(\bm r_P-\bm r_C).
$$
切向冲量同时满足 $|J_t|\le\mu J_n$。若计算所需值超过此上限，应改取滑动支路
$$
J_t=-\mu J_n\operatorname{sgn}(v_{Pt}^-).
$$
这组方程再与车身刚体约束联立，即可数值求任意 $e$ 的碰后状态。""",
        5: r"""**变式.** 若 $C_1/C_2$ 和 $L_1/L_2$ 都是小参数 $\varepsilon$，求被忽略支路对非退化谐振频率的修正阶数。

**解答.** 把精确谐振条件写成
$$
F(\omega,\varepsilon)
=F_0(\omega)+\varepsilon F_1(\omega)+O(\varepsilon^2)=0.
$$
若理想极限中的根 $\omega_0$ 非退化，即 $F_0(\omega_0)=0$ 且 $F_0'(\omega_0)\ne0$，令 $\omega=\omega_0+\delta\omega$ 并展开：
$$
F_0'(\omega_0)\delta\omega
+\varepsilon F_1(\omega_0)+O(\varepsilon^2)=0.
$$
因而
$$
\boxed{\delta\omega=
-\varepsilon\frac{F_1(\omega_0)}{F_0'(\omega_0)}
+O(\varepsilon^2)},
$$
即一般为相对 $O(\varepsilon)$ 修正。只有电路对称性使 $F_1(\omega_0)=0$ 时，首个非零移频才推迟到 $O(\varepsilon^2)$。若两个理想根退化，则必须在退化子空间内重新对角化，不能套用上式。""",
    },
}


def replace_variants(set_number: str, replacements: dict[int, str]) -> None:
    path = ROOT / f"蔡题{set_number}" / "整理版" / "markdown" / f"蔡题{set_number}_教师备课.md"
    text = path.read_text(encoding="utf-8")
    matches = list(re.finditer(r"(?m)^# 第 (\d+) 题$", text))
    if len(matches) != 8:
        raise AssertionError(f"{set_number}: expected 8 questions")
    pieces: list[str] = []
    cursor = 0
    for index, match in enumerate(matches, start=1):
        end = matches[index].start() if index < len(matches) else len(text)
        block = text[match.start():end]
        if index not in replacements:
            continue
        marker = "## 九、变式训练"
        start = block.index(marker) + len(marker)
        prefix = block[:start]
        starts = prefix.count("<!-- TEACHER_ONLY_START -->")
        ends = prefix.count("<!-- TEACHER_ONLY_END -->")
        if starts - ends not in (0, 1):
            raise AssertionError(f"{set_number} Q{index}: invalid marker depth before module nine")
        # Older source groups differ: some wrap modules six through nine in a
        # teacher-only block, while others keep those modules unwrapped.  Close
        # a block only when one is actually open.
        closing = "<!-- TEACHER_ONLY_END -->\n" if starts - ends == 1 else ""
        new_block = (
            prefix
            + "\n\n"
            + replacements[index].strip()
            + "\n"
            + closing
        )
        pieces.append(text[cursor:match.start()])
        pieces.append(new_block)
        cursor = end
    pieces.append(text[cursor:])
    path.write_text("".join(pieces), encoding="utf-8")


if __name__ == "__main__":
    for number, mapping in V.items():
        replace_variants(number, mapping)
        print(f"第 {number} 套带解变式已补全：{len(mapping)} 题")
