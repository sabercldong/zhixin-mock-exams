from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


ADDITIONS: dict[str, dict[int, str]] = {
    "045": {
        1: r"""把各近似的先后次序再写清楚。由两体相对运动
$$
\omega^2L=\frac{G(M_S+M_E)}{L^2}
$$
先得 $L=[G(M_S+M_E)/\omega^2]^{1/3}$，这里尚未使用 $M_E\ll M_S$。质心条件给出
$$
r_S=\frac{M_E}{M_S+M_E}L,
\qquad
v_S=\omega r_S.
$$
只有代入数值时才可令 $M_S+M_E\simeq M_S$。量纲上 $GL/\omega^2$ 的组合最终给出长度，$\omega r_S$ 给出速度；若把质量比漏掉，结果会错误地落在 $10^4\,\mathrm{m,s^{-1}}$ 而不是 $10^{-1}\,\mathrm{m,s^{-1}}$ 量级。""",
        2: r"""地面系答案应由矢量合成得到，而不是把两个标量直接相加。设沿斜面向低端的单位向量为
$$
\hat{\boldsymbol s}=(\cos\theta,-\sin\theta),
$$
斜面系相对加速度为 $a_r\hat{\boldsymbol s}$，斜面本身为 $a_0\hat{\boldsymbol x}$，故
$$
\boldsymbol a_C=a_0\hat{\boldsymbol x}+a_r\hat{\boldsymbol s}.
$$
分别投影即可得到水平、竖直分量。令 $a_0=0$ 时应退化为固定斜面上圆柱的 $a_r=2g\sin\theta/3$；令 $\theta=0$ 时重力无沿面分量，圆柱相对运动只由惯性力决定。这两个极限能同时检查惯性力方向和坐标变换符号。""",
        3: r"""四个自由度必须分别在各自平衡点线性化。竖直方向先写
$$
M\ddot x=F_m(h+x)-Mg,
$$
利用 $F_m(h)=Mg$ 后展开 $F_m(h+x)=F_m(h)+F_m'(h)x$，常数项才会严格相消。角运动中，静磁矩势能的二阶项为负，说明反平行构型本身不稳定；陀螺进动和高频场提供的是附加的正二次项。临界值均由“总二次系数等于零”得到，严格稳定需取使该系数为正的一侧。这样写可避免把竖直频率、进动频率和交变场频率混作同一个量。""",
        4: r"""第 III 种平衡的受力几何可直接验证。销钉两侧绳张力大小相同，其合力沿 $\angle ACB$ 的角平分线；重力作用线通过质心 $H$。平衡要求两条作用线重合，于是角平分线定理给出
$$
\frac{AH}{HB}=\frac{AC}{CB}.
$$
左式由质心定义等于 $m_2/m_1$，右式又受 $AC+CB=2a$ 约束。求得两段长度后还要逐一检查它们为正并满足三角形不等式。第（8）问的本征方程应写成 $\det(K-\omega^2M)=0$；$M$ 的量纲为转动惯量，$K$ 的量纲为力矩，故 $K/M$ 必须具有 $\mathrm{s^{-2}}$ 的量纲。""",
        5: r"""精确几何关系可由等势圆的两个轴上交点建立。若像线电荷位于 $-d$、真线电荷位于 $d$，圆柱表面到两线的距离比固定。把最近点 $x=l-r$ 与最远点 $x=l+r$ 代入同一距离比，消去该比值后得到
$$
d^2=l^2-r^2.
$$
圆柱相对地面的电势差遂为 $U=(\lambda/2\pi\varepsilon)\operatorname{arccosh}(l/r)$。远离平面时令 $x=r/l\ll1$，应先把 $\operatorname{arccosh}(1/x)$ 写成对数再展开；由于几何关于 $r\mapsto-r$ 为偶，修正项不应出现 $x$ 的一次幂。""",
        6: r"""组分计数、热量和循环方向要分三张账。任意温度下
$$
n_{A_2}=(1-\lambda)n_0,
\qquad n_A=2\lambda n_0,
\qquad n=(1+\lambda)n_0.
$$
把 $\lambda=(T-T_0)/T_0$ 代入后再对 $U=3nRT$ 求导，导数包含 $n\,dT$ 与 $T\,dn$ 两项。绝热式必须从 $dU+p\,dV=0$ 逐项代入积分，不能假定常数 $\gamma$。闭合循环最后用 $\sum\Delta U=0$ 检查：各段热量的代数和应等于净功；若所得“效率”超过卡诺上限，应回到题设理想化假定解释，而不能把它宣称为实际热机。""",
        7: r"""圆膜静力式可从环形微元得到。半径 $x$ 处的小斜率为 $h'(x)$，圆周上两层表面张力的竖直合力近似为
$$
2\sigma(2\pi x)h'(x).
$$
它平衡半径 $x$ 内膜的重量 $\rho g\pi x^2$，从而得到 $h'(x)=\rho gx/(4\sigma)$，再用边缘高度条件积分。双圆环问题则不能令对数项自动消失，因为定义域不包含 $x=0$；常数项与 $\ln x$ 项必须由 $z(r_1)$、$z(r_2)$ 两个边界条件同时确定。""",
        8: r"""第一问可用波四矢量的两次变换作闭环检查。入射真空波满足 $k=\omega/c$；变到介质系后得到 $\omega',k'_{\rm in}$，界面在该系静止，故透射频率仍为 $\omega'$，同时 $k'_{\rm tr}=n\omega'/c$。再把 $(\omega'/c,k'_{\rm tr})$ 变回地面系，地面波长由 $2\pi/k_{\rm tr}$ 读取。令 $\beta=0$ 必须得到 $\xi=1/n$，令 $n=1$ 必须得到 $\xi=1$。第二问由 $k(\rho)$ 的二次项得到轴向相位差，再与薄透镜相位 $-k_0\rho^2/(2f)$ 比较，符号应对应会聚而非发散。""",
    },
    "046": {
        1: r"""数值计算先统一单位：$R=6.4\times10^6\,\mathrm m$、$T=27.3\times86400\,\mathrm s$。球形地球阶段
$$
M=\frac43\pi R^3\rho,
\qquad
r^3=\frac{GMT^2}{4\pi^2},
\qquad
v=\frac{2\pi r}{T}.
$$
圆柱阶段取长度为 $L$、半径为 $r>R$ 的高斯面，只有侧面有通量，包围质量恒为 $\rho\pi R^2L$，故
$$
g(r)\,2\pi rL=4\pi G\rho\pi R^2L.
$$
再由 $v^2/r=g(r)$ 可见 $r$ 完全约去。这里若把包围质量误写为 $\rho\pi r^2L$，会得到内部场的表达式，并错误地推出 $v\propto r$。""",
        2: r"""第（2）问三条平衡方程应同时保留：水平方向 $N_w+f=ma$，竖直方向 $N=mg$，关于重心的力矩为
$$
N_wh=f(r-h).
$$
联立而不是猜测摩擦方向，得到 $f=mah/r$、$N_w=ma(r-h)/r$；在 $0<h<r$ 时二者均与预设方向相容。临界滑动由 $f=\mu N$ 给出。第（3）问改成地面光滑后，墙面摩擦同时进入竖直平衡和力矩平衡；应先解出所需比值 $|f_w|/N_w$，再对任意 $a$ 讨论，而不是先把 $a\to\infty$ 代入某一条孤立方程。""",
        3: r"""场线圆的面积应从几何参数完整算出。通过 $(\pm a,0)$ 与 $(0,\eta a)$ 的圆心位于 $y$ 轴，设为 $(0,c)$，则
$$
a^2+c^2=(\eta a-c)^2
$$
给出 $c$ 与半径。上下两条圆弧围成的面积由“扇形减三角形”组成，取反三角函数时必须选择与上弧连续的支路。电流问题中电势仍是若干 $\ln r_i$ 的代数和，电流密度由 $\boldsymbol j=-\sigma_0\nabla U$ 得到。保持电压不变时，源强要按新的电极位置重新归一化；只比较中心场几何因子会漏掉这一因子。""",
        4: r"""液柱动能的质量不是两根竖直柱，而是全管液体：
$$
T=\frac12\rho S(3l+h)\dot x^2.
$$
一侧上升 $x$、另一侧下降 $x$ 时，重力势能增量由两柱分别积分后相加，必须得到与 $x^2$ 成正比而无一次项。恒定转速下，可在旋转系比较两自由液面的 $gz-\omega_0^2s^2/2$；自由转动时则用 $J=I(x)\omega$ 消去 $\omega$，转动动能改写为 $J^2/[2I(x)]$。把 $I(x)$ 展开到二阶前先验证一次项与重力势能相消，才能确认展开点确为平衡点。""",
        5: r"""几何、导电和能量三步可以逐项核对。由 $y=vt=kx_t^2$ 得整棒长度
$$
L(t)=2\sqrt{\frac{vt}{k}}.
$$
所以 $E=BLv$、$R=\lambda L$，电流
$$
I=\frac{Bv}{\lambda}
$$
与时间无关。磁阻力可直接积分 $dF=IB\,dx$ 得 $F=IBL$，外力功率为 $Fv=IBLv=IE=I^2R$。三种写法完全相同，说明回路磁能没有积累且机械功全部变成焦耳热；同时也核对了整棒长度的因子 $2$。""",
        6: r"""亮度变换必须同时追踪面积元和立体角元。对球形余弦发光体，远处同一像面元对应球面投影 $dS\cos\theta$，而发射强度含相同的 $\cos\theta$，两者相除后亮度与位置无关。半球问题中应明确参数链
$$
q=\frac ar\longrightarrow \theta\longrightarrow i
\longrightarrow p(q),
$$
再分别计算环带面积比 $p\,dp/(a\,da)$ 与光束立体角比。轴线处所有看似 $0/0$ 的因子要先作 $q\to0$ 展开；边缘处则用整体极限，不能让单个发散雅可比掩盖最终有限或可积的亮度。""",
        7: r"""统一偏转式写出后再求导：
$$
\Delta_N=N\pi+2\alpha-2(N+1)\theta,
\qquad
\frac{d\theta}{d\alpha}=\frac{\cos\alpha}{n\cos\theta}.
$$
驻值条件首先给出角度关系，再与 $\sin\alpha=n\sin\theta$ 联立消元。所得 $\sin^2\alpha$ 必须位于 $[0,1]$，这一步产生 $n\le N+1$ 的存在条件。后两问先代 $n_0$ 判断一级、二级、三级驻值是否真实存在；不存在的级次没有可比较的虹强度。存在时每多一次内部反射，振幅才多乘一个相应的 $r'$。""",
        8: r"""反应能与喷流动量要使用同一静质量约定。单次反应
$$
Q=(4m_{\rm H}-m_{\rm He}-2m_e)c^2.
$$
若把 $Q$ 全给氦核，则 $\gamma_u m_{\rm He}c^2=m_{\rm He}c^2+Q$，由此先求 $\gamma_u$ 再求 $u$，不能用非相对论式越过数值检查。质子质量流率 $\dot m_{\rm H}$ 对应反应数率 $\dot N=\dot m_{\rm H}/(4m_{\rm H})$，推力为 $F=\dot N\gamma_um_{\rm He}u$。火箭质量比用快速度积分，往返加减速时两段快速度相等、质量比相乘，最后才把总质量比减1换成题目定义的燃料比。""",
    },
    "047": {
        1: r"""约束极值还可用拉格朗日乘子逐项复核。令
$$
\mathcal L=3\sin\theta_1+\sin\theta_2
-\Lambda\left(\cos\theta_1+\cos\theta_2-\frac{L}{2l}\right).
$$
两偏导方程分别为
$$
3\cos\theta_1+\Lambda\sin\theta_1=0,
\qquad
\cos\theta_2+\Lambda\sin\theta_2=0.
$$
消去 $\Lambda$ 就得到 $\tan\theta_1=3\tan\theta_2$，与隐函数求导完全一致。数值方程左端
$$
f(x)=\frac1{\sqrt{1+9x^2}}+\frac1{\sqrt{1+x^2}}
$$
在 $x>0$ 上有 $f'(x)<0$，且 $f(0)=2$、$f(+\infty)=0$，所以当 $0<L/(2l)<2$ 时正根存在且唯一。二分计算可先把根夹在 $x=0.37$ 与 $x=0.38$ 之间，再逐次缩小区间；根的唯一性说明最后得到的不是偶然的数值支路。""",
        2: r"""第一次相交的根应把求根公式完整写出。若
$$
A=v_0(\sin\theta+\cos\theta\tan\alpha),
$$
则
$$
t_{1,2}=\frac{A\mp\sqrt{A^2-2gh}}g.
$$
两根的和为 $2A/g>0$，积为 $2h/g>0$；判别式为正时它们都为正。实体顶棚截断轨迹，故实际碰撞只能取减号对应的较小根。代回位置后还应同时核对
$$
y_1=v_0\sin\theta\,t_1-\frac12gt_1^2
=h-x_1\tan\alpha.
$$
第二问若沿顶棚法线建立坐标，法向距离为 $h\cos\alpha$，初速度法向分量为 $v_0\sin(\theta+\alpha)$，重力法向分量为 $-g\cos\alpha$。于是最短时间等价于最大化初始法向速度，直接得到 $\theta+\alpha=\pi/2$；这也解释了最优角为何不是惯常的 $45^\circ$。""",
        3: r"""逐面折射可以避免把水的折射率误代入曲面公式。第一面曲率半径趋于无穷大，远物又有 $u_1=-\infty$，所以
$$
\frac{n}{v_1}-\frac{n_{\rm out}}{u_1}=0
\quad\Longrightarrow\quad v_1=\infty.
$$
进入玻璃的仍是平行光。第二面才有
$$
\frac1{v_2}-\frac n{-\infty}=\frac{1-n}{R},
$$
因此像方焦度只由 $(1-n)/R$ 决定。“平面无焦度”不等于“单条斜光线不折射”：斜率会按折射定律改变，但一束平行近轴光仍保持平行。用 $R$ 的米制数值计算时，$1/f$ 的单位为 $\mathrm{m^{-1}}$；再乘 $100$ 才得到日常所说的眼镜度数。""",
        4: r"""Gilbert 模型的远场最好从对称位置写起。把磁荷置于 $z=\pm d/2$，则轴线上
$$
B_z=\frac{\mu_0q_m}{4\pi}
\left[\frac1{(z-d/2)^2}-\frac1{(z+d/2)^2}\right]
=\frac{\mu_0q_m}{4\pi}\frac{2zd}{(z^2-d^2/4)^2}.
$$
当 $z\gg d$ 时分母取 $z^4$，便有
$$
B_z\simeq\frac{\mu_0q_md}{2\pi z^3}
=\frac{\mu_0p_m}{2\pi z^3}.
$$
电流环精确式中把 $(z^2+r^2)^{-3/2}$ 写成 $z^{-3}(1+r^2/z^2)^{-3/2}$，保留零阶也得到同一结果。宏观圆柱中 $M=np_m$ 的单位是 $\mathrm{A/m}$；Gilbert 图像留下端面磁荷，Ampere 图像留下侧面束缚电流 $K_b=M$。两种边界源都给出长圆柱内部 $B=\mu_0M$，从单位到方向均一致。""",
        5: r"""汽化过程中不能把潜热全部当作蒸气内能的增加。每摩尔物质从液体变成蒸气时，热力学第一定律给出
$$
L=\Delta U+p\Delta V.
$$
若蒸气近似理想、液体体积忽略，则 $p\Delta V\simeq RT$，所以真正进入内能差的是
$$
\Delta U=L-RT.
$$
压力和物质的量的微分关系也应从理想气体式逐项得到：在体积固定时
$$
pV=nRT
\quad\Longrightarrow\quad
V\,dp=RT\,dn+nR\,dT.
$$
若该小段过程近似等温，才可删去第二项而写成 $dn/n=dp/p$。因此“等温”“定容”和“理想气体”三项条件应在使用比例式之前明确，而不能在结果中倒推。""",
        6: r"""平均场概率式可从能量差逐步得到。单个自旋取 $s=+1,0,-1$ 时的平均场能量为 $\varepsilon_s=-qJms$，故
$$
\frac{P_+}{P_0}=e^{qJm/(kT)},
\qquad
\frac{P_-}{P_0}=e^{-qJm/(kT)}.
$$
归一化后再代入 $m=P_+-P_-$，得到
$$
m=\frac{2\sinh y}{1+2\cosh y},
\qquad y=\frac{qJm}{kT}.
$$
临界点不是把 $m=0$ 直接约去，而是比较右端在原点的斜率。展开 $\sinh y=y+O(y^3)$、$\cosh y=1+y^2/2+O(y^4)$，右端一次项为 $2y/3$，于是 $1=2qJ/(3kT_c)$。高温极限下三态各占 $1/3$，这同时核对了概率归一化和三态而非二态模型。""",
        7: r"""质心加速度式要从坐标连续求导，而不能只写向心项。由
$$
x_C=r_c\sin\theta,
\qquad y_C=r_c\cos\theta
$$
得到
$$
\ddot x_C=r_c(\ddot\theta\cos\theta-\dot\theta^2\sin\theta),
\quad
\ddot y_C=-r_c(\ddot\theta\sin\theta+\dot\theta^2\cos\theta).
$$
再分别代入能量给出的 $\dot\theta^2$ 与力矩方程给出的 $\ddot\theta$，才能得到支持力和摩擦力。全过程约束检查必须按顺序进行：先由 $N\ge0$ 确定仍接触的角区间，再只在该区间最大化 $|f|/N$。当 $N$ 先降到零时，后续“绕固定点转动”的公式已经失效。惯量下界 $\lambda\ge1$ 与接触临界值 $4/3$ 是两个不同概念，不能混用。""",
        8: r"""能量式中的交叉项可由小球速度平方直接核对：
$$
v_P^2=(\dot x-r\dot\beta\cos\beta)^2
+r^2\dot\beta^2\sin^2\beta
=\dot x^2-2r\dot x\dot\beta\cos\beta+r^2\dot\beta^2.
$$
圆环平动和转动各再贡献 $m\dot x^2/2$，所以总动能中 $\dot x^2$ 的系数必为 $3m/2$。磁力虽然不做功，却提供水平冲量，因此能量方程之外还必须保留式（17）的一阶动力学关系。给定 $\beta$ 后把该关系解成 $\dot x$ 关于 $\dot\beta$ 的一次式，再代回能量，就得到关于 $\dot\beta$ 的二次方程；两个实根代表同一位置可能经过的两个速度分支。每个根都要回代求 $\dot x$ 并检查能量，不能把绝对值较大的根凭直觉删去。所谓小球相对圆环静止还必须结合环的纯滚动角速度，按本题符号约定写成 $\dot\beta=\dot x/r$，并非简单令 $\dot\beta=0$。""",
    },
}


ADDITIONS_LATE: dict[str, dict[int, str]] = {
    "048": {
        1: r"""两种回正力矩的建模层次应严格分开。内倾部分先由轴力矩定义
$$
M_{OB}=(\boldsymbol r_{OP}\times\boldsymbol N)\cdot\hat{\boldsymbol e}_{OB}
$$
得到有效力臂 $l\sin\beta\sin\theta$，再乘单轮支持力 $G/4$；只有最后的小角化才令 $\sin\theta\simeq\theta$。后倾部分则先由单轨车辆几何
$$
R=\frac d{\tan\theta}
$$
得到所需总侧向力 $mv^2/R$，按题设对称载荷分给前轮一半，再乘拖距 $r\sin\alpha$。因此较精确的恢复力矩为
$$
M_2=-\frac{mv^2r}{2d}\sin\alpha\tan\theta,
$$
而不是一开始就把 $\alpha$、$\theta$ 的所有三角函数同时删去。令 $v=0$、$\alpha=0$、$\beta=0$ 分别检查，两种机制应按其物理来源独立消失。""",
        2: r"""绝热不变量可以用轨道尺度说明其适用条件。拉莫尔半径和回旋频率分别为
$$
\rho_L=\frac{mV_\perp}{|q|B},
\qquad \omega_c=\frac{|q|B}{m}.
$$
只有满足 $\rho_L|\nabla B|/B\ll1$，且一个回旋周期内导引中心的 $z$ 位移远小于磁场变化尺度时，才可使用
$$
\mu_m=\frac{mV_\perp^2}{2B}=\text{常量}.
$$
在板处令 $V_z=0$ 是临界轨迹；若初始轴向动能更大，到板处仍有 $V_z^2>0$，因而被吸收。角度若相对横截面定义为 $\vartheta$，有 $V_z=V\sin\vartheta$、$V_\perp=V\cos\vartheta$；若改成相对磁轴的角 $\chi$，则两者互余。不先写角度定义，损失锥不等号很容易整体写反。""",
        3: r"""边界条件直接决定允许波数。固定端给 $X(0)=0$，故空间解可取 $X=A\sin kx$；自由端没有切向外力，剪切应力 $S\partial u/\partial x$ 必须为零，所以
$$
X'(L)=Ak\cos kL=0
\quad\Longrightarrow\quad
kL=\left(n+\frac12\right)\pi.
$$
再由 $\omega=ck$、$c=\sqrt{S/\rho}$ 才得到各阶周期。扭转微元的运动方程中，截面极惯性矩 $J_p$ 同时出现在扭转力矩 $SJ_p\partial\varphi/\partial x$ 与质量转动惯量 $\rho J_p\,dx$ 中，因此相消，波速仍为 $\sqrt{S/\rho}$。两端无外力矩给 $\varphi_x(0)=\varphi_x(L)=0$；$k=0$ 是整体刚性转动而非振动，题目要求非零模态时必须删去。""",
        4: r"""超导部分的符号可以不依赖记忆来核对。在 $0<T<T_0$ 内
$$
B_c>0,
\qquad
\frac{dB_c}{dT}=-\frac{2B_0T}{T_0^2}<0.
$$
因此
$$
S_n-S_s=-\mu_0B_c\frac{dB_c}{dT}>0,
$$
说明正常态熵更大，符合超导态更有序的物理图像。代数值时应按
$$
B_c(T)=B_0\left(1-\frac{T^2}{T_0^2}\right),
\quad
-\frac{dB_c}{dT}=\frac{2B_0T}{T_0^2}
$$
分别计算后相乘，这样可避免漏掉一个 $B_0$。最后在 $T\to0$ 时导数趋零，在 $T\to T_0$ 时 $B_c$ 趋零，熵差两端都趋零；这两个边界同时检验函数形式。""",
        5: r"""力的表达式可从受约束能量再核对一次。总磁链
$$
\Phi=L I+SB(x,y)=\Phi_0
$$
固定，所以 $I=(\Phi_0-SB)/L$。消去电流后的磁能等效势可写成
$$
U_{\rm eff}(x,y)=\frac{[\Phi_0-SB(x,y)]^2}{2L},
$$
并有 $\boldsymbol F=-\nabla U_{\rm eff}=IS\nabla B$。在原点沿 $x$ 方向，
$$
B(x,0)=B_0\cos kx
\simeq B_0\left(1-\frac12k^2x^2\right).
$$
电流的位移修正从 $x^2$ 起步，因此求线性恢复力时可把 $I$ 取为 $I_0$，得到
$$
F_x\simeq-I_0B_0Sk^2x.
$$
只有 $I_0B_0>0$ 时原点才是稳定势阱；若符号相反，频率平方为负，物理上是指数离开而不是小振动。""",
        6: r"""端面激励必须先分解成方形截面的本征模态。环上四点的离散拉普拉斯算符具有均匀模态 $\lambda=0$、两重简并模态 $\lambda=2$ 和交错模态 $\lambda=4$。对角注流 $A\to B$ 不含均匀模态，只激发相应的反对称组合；相邻注流 $A\to C$ 则同时投影到 $\lambda=2$ 与 $\lambda=4$。每个模态沿管轴满足
$$
V_{n+1}-(\lambda+2)V_n+V_{n-1}=0,
$$
特征根成倒数对。半无限网络要求电势远处不发散，所以必须取 $0<q_\lambda<1$ 的根。最后把各模态电压降按其投影系数相加；若忘记模态归一化，通常会使等效电阻多出或少掉因子2。""",
        7: r"""周期修正的展开阶数要特别说明。令
$$
\varepsilon=\frac{V(b)-V(x)}{mc^2}.
$$
由于速率平方的最低阶本身就是 $2\varepsilon$，要得到 $1/v$ 的相对一阶修正，必须先把
$$
1-(1+\varepsilon)^{-2}
=2\varepsilon-3\varepsilon^2+O(\varepsilon^3)
$$
保留到绝对二阶，再开方并取倒数。积分
$$
\int_0^b\sqrt{b^2-x^2}\,dx
$$
可令 $x=b\sin u$ 化为 $b^2\int_0^{\pi/2}\cos^2u\,du=\pi b^2/4$。整个轨道上展开成立的条件由 $\varepsilon$ 的最大值给出，即 $ab^2=E_{k0}/(mc^2)\ll1$，而不是只看转向点处 $\varepsilon=0$。""",
        8: r"""横移公式来自包络的驻相条件。反射角谱在界面上的相位可写成
$$
\Phi(k_x)=k_xx+\delta(k_x)-\omega t.
$$
波包中心满足 $\partial\Phi/\partial k_x=0$，所以相对几何反射点
$$
\Delta=-\frac{d\delta}{dk_x}.
$$
又因 $k_x=(n_1\omega/c)\sin\theta$，
$$
\frac{dk_x}{d\theta}=\frac{n_1\omega}{c}\cos\theta,
\qquad
\Delta=-\frac{c}{n_1\omega\cos\theta}\frac{d\delta}{d\theta}.
$$
这个链式求导中的 $\cos\theta$ 不能漏掉。全反射时 $|r|=1$，反射系数只改变相位而不改变每个平面波分量的振幅；若算得 $|r|\ne1$，应先检查 $\cos\theta_2$ 的虚数支路，再继续对相位求导。临界角附近相位变化很快，横移增大，也可作为结果趋势的检查。""",
    },
    "050": {
        1: r"""冲量通量的四个因子应逐一核对：有效质量密度是 $\eta\rho_0$，迎面相对速度是 $U=2v_0$，单位时间扫过体积是 $AU$，完全弹性反射的单位质量动量改变量是 $2U$。所以
$$
F=(\eta\rho_0AU)(2U)=2\eta\rho_0AU^2.
$$
圆柱的迎风面积正比于 $r^2$、质量正比于 $r^3$，故加速度必有 $a\propto1/r$；若结果不含粒径，说明面积或体积取错。球面镜面反射时还要把局部法向动量投影回竖直方向，并在投影圆盘上积分；既不能把整个球面都当作正碰，也不能直接照搬圆柱系数。临界半径由停止距离等于 $h_0$ 给出，算完后应检查所得 $r_0$ 是否远小于装置尺度，从而与局域匀速气流近似相容。""",
        2: r"""杆作为定长弦时，弦中点到圆心的距离恒为
$$
d=\sqrt{R^2-\frac{L^2}{4}}.
$$
因此质心不是沿直线平移，而是以 $O$ 为圆心、$d$ 为半径运动，同时杆本身也随弦转动。关于 $O$ 的等效惯量必须用
$$
I_O=I_G+Md^2
=M\left(R^2-\frac{L^2}{6}\right),
$$
不能只取 $Md^2$。第二问比较支持力时，转折点有 $\dot\theta=0$ 而角加速度不为零；平衡点有角加速度为零而速度最大。应分别代入径向平动方程，再把 $\cos\theta_m$ 和由能量得到的 $\dot\theta_0^2$ 都展开到 $\theta_m^2$，最后才作差。""",
        3: r"""第一问的临界圆几何可再用平方前后的方向检查。轨迹圆心与区域中心距离为 $D=\sqrt{R_2^2+\rho_c^2}$，轨迹能达到的最小半径是 $D-\rho_c$。临界相切给
$$
D-\rho_c=R_1
\quad\Longrightarrow\quad
\rho_c=\frac{R_2^2-R_1^2}{2R_1}>0.
$$
这要求速度越大、曲率半径越大，越容易进入内区。第二问中应把标量符号和矢量方向分开写：若纸外为 $+z$，题设“向里为 $B_0$ 正方向”意味着 $\boldsymbol B_0=-B_0\boldsymbol e_z$。由正则角动量得到的 $B_x<0$ 因而表示内区磁场实际向外。只给绝对值会丢失本问最重要的弯曲方向。""",
        4: r"""三问使用的守恒律处在不同时间段。越阶过程要写成
$$
\text{碰前纯滚动}
\longrightarrow
\text{碰撞瞬间关于棱角守恒角动量}
\longrightarrow
\text{碰后绕棱角上摆时守恒机械能}.
$$
碰撞前关于棱角的角动量含质心平动项 $mv_1(r-h)$ 与自转项 $I_Cv_1/r$，两项方向相同。滚动阻力问中总动能为 $mv^2$，耗散功率为 $-kmg(v/r)$，因此减速度恒定而功率并不恒定。推环问的极值式除求 $D'(\theta)=0$ 外，还要用 $D''(\theta)<0$ 确认分母取最大，并检查所得角位于实际接触区间内。""",
        5: r"""二阶近似的取舍可按量级解释。液柱质量相对平衡值的修正是 $O(x)$，速度平方是 $O(\dot x^2)$，两者相乘为三阶量，所以动能中的质量可取平衡值；势能的一次项则因
$$
x_1+2x_2+x_3=0
$$
严格相消，不是被近似舍弃。消去 $x_2$ 后，质量矩阵与刚度矩阵满足
$$
\boldsymbol K=\frac gl\boldsymbol M,
$$
因此特征方程是
$$
\det(\boldsymbol K-\omega^2\boldsymbol M)
=\det\boldsymbol M\left(\frac gl-\omega^2\right)^2=0.
$$
平方表明两个独立形状同频；这正是任意允许初形都不产生拍频的原因。""",
        6: r"""分段权重 $\min(v_xt/l,1)$ 来自初始位置平均。固定 $v_x>0$ 时，能在 $t$ 前撞壁的初始位置区间长度是 $\min(v_xt,l)$；除以 $l$ 后才对一维麦克斯韦分布积分。第二问每个已撞分子还要乘 $2mv_x$，故积分比计数问题多一个速度因子。结果可用两个极限同时核验：短时总冲量应为 $p_0St$，长时应趋于
$$
\frac{Nmv_T}{\sqrt\pi},
$$
恰等于自由试管最终获得的动量。光子情形使用 $u_\gamma=4\sigma T^4/c$ 与 $\langle|\cos\theta|\rangle=1/2$；前者把出射度换成能量密度，后者把总动量投影到管轴，两项缺一不可。""",
        7: r"""用光线矩阵可以把三处符号一次核对。自由传播与薄透镜分别为
$$
P(d)=\begin{pmatrix}1&d\\0&1\end{pmatrix},
\qquad
L(f)=\begin{pmatrix}1&0\\-1/f&1\end{pmatrix}.
$$
从物屏到第二透镜前的矩阵为 $P(l_2)L(f_1)P(l_1)$。代入 $l_2/f_1=2$、$l_1=2l_2$ 后，第一行给
$$
y_2=-y_0-l_2u_0,
$$
与逐段追迹一致。孔径光阑需对轴上物点比较两透镜允许的初始倾角，不能只比实体直径；可见区域的主光线穿过孔径光阑中心，而题设“明亮”区域使用穿过 $L_1$ 中心的另一条特征光线。两种光线不应混成同一个边界条件。""",
        8: r"""测量长度必须选同一参考系同时的两个事件。左端事件 $A$ 的瞬时静止系满足
$$
\Delta t'=\gamma_A\left(\Delta t-\frac{v_A\Delta x}{c^2}\right)=0,
$$
所以与 $A$ 同时的右端事件 $B$ 一般发生在更晚的地面时刻。将两条抛物线世界线代入后得到关于时间差的二次方程；选根的标准是 $l\to0$ 时应有 $t_B-t_A\to0$。短车近似才给 $L_A\simeq\gamma_Al$，精确有限长度结果还包含加速期间世界线弯曲的修正。低速极限必须回到 $L_A=l$。题设两端具有相同地面坐标加速度，保持的是地面坐标距离而非本征长度，因此不满足 Born 刚性；真正的刚性加速要求前端本征加速度小于后端。""",
    },
}


DEEPENING_ADDITIONS_LATE: dict[str, dict[int, str]] = {
    "048": {
        1: r"""第一问的精确势能可由几何高度直接积分，而不只停在线性力矩。转向角为 $\theta$ 时，轮心沿倾斜主销轴附近运动，单轮相对最低位置的高度变化为
$$
\Delta h=l\sin\beta(1-\cos\theta).
$$
因此
$$
U_1(\theta)=\frac G4l\sin\beta(1-\cos\theta),
$$
有向力矩为
$$
M_1=-\frac{dU_1}{d\theta}
=-\frac{Gl}{4}\sin\beta\sin\theta.
$$
在 $\theta=0$ 附近继续展开：
$$
U_1=\frac{Gl}{8}\sin\beta\,\theta^2
-\frac{Gl}{96}\sin\beta\,\theta^4+\cdots.
$$
二次项系数为正，所以正中位置稳定；四次项说明偏转较大时恢复刚度不再严格常数。第二问中，若不立刻作 $\theta\ll1$，
$$
F_f=\frac12\frac{mv^2}{R}
=\frac{mv^2}{2d}\tan\theta,
$$
从而
$$
M_2=-\frac{mv^2r}{2d}\sin\alpha\tan\theta.
$$
线性化总刚度
$$
K_{\rm eff}
=\frac{Gl}{4}\sin\beta
+\frac{mv^2r}{2d}\sin\alpha.
$$
若轮架绕主销转动惯量为 $J$，小转向振动频率为 $\sqrt{K_{\rm eff}/J}$。这一步把“回正力矩”与“稳定性”明确联系起来。""",
        2: r"""转向点位置可以直接从等效能量式求出。令
$$
\mathcal E=\frac12mV_z^2
+\mu_mB(z),
\qquad
\mu_m=\frac{mV_\perp^2(0)}{2B(0)}.
$$
在原点
$$
\mathcal E
=\frac12mV_z^2(0)+\frac12mV_\perp^2(0).
$$
转向点 $z_t$ 满足 $V_z(z_t)=0$，所以
$$
\frac{B(z_t)}{B(0)}
=1+\frac{V_z^2(0)}{V_\perp^2(0)}.
$$
若右侧小于镜比 $M=B(L)/B(0)$，则 $z_t<L$，粒子在板前反射；若大于 $M$，则整个区间内没有转向点。原点附近若
$$
B(z)=B(0)(1+\kappa z^2+O(z^4)),
$$
则去掉常数后的等效势为
$$
U_{\rm eff}(z)
=\frac12mV_\perp^2(0)\kappa z^2.
$$
与 $\tfrac12m\omega_z^2z^2$ 比较：
$$
\omega_z=V_\perp(0)\sqrt{\kappa}.
$$
这说明磁镜中的纵向慢运动在中心附近近似简谐，而横向回旋频率约为 $|q|B(0)/m$。题设“纵向远慢于横向”正对应 $\omega_z\ll\omega_c$，从而保证绝热不变量在许多回旋周期上缓慢变化。""",
        3: r"""扭转波方程可从圆柱微元完整推出。设截面转角为 $\varphi(x,t)$，单位长度扭转角为 $\partial\varphi/\partial x$。材料力学关系给内力矩
$$
\mathcal M=SJ_p\frac{\partial\varphi}{\partial x},
$$
其中 $J_p=\int r_\perp^2\,dA$ 是截面极惯性矩。厚度 $dx$ 微元两端的力矩差为
$$
d\mathcal M
=SJ_p\frac{\partial^2\varphi}{\partial x^2}dx.
$$
该微元对轴的质量转动惯量为
$$
dI=\rho J_p\,dx.
$$
转动方程
$$
\rho J_pdx\,\frac{\partial^2\varphi}{\partial t^2}
=SJ_p\frac{\partial^2\varphi}{\partial x^2}dx
$$
约去 $J_pdx$：
$$
\frac{\partial^2\varphi}{\partial t^2}
=\frac S\rho\frac{\partial^2\varphi}{\partial x^2}.
$$
两端无外加力矩意味着 $\varphi_x(0)=\varphi_x(L)=0$。取
$$
\varphi=X(x)e^{i\omega t}
$$
后，$X=A\cos kx+B\sin kx$。由 $X'(0)=0$ 得 $B=0$，再由 $X'(L)=0$ 得 $\sin kL=0$，所以
$$
k_n=\frac{n\pi}{L},\qquad n=0,1,2,\ldots.
$$
$n=0$ 是整体等角速度或等角位移的刚性模，不产生弹性回复；非零模才有
$$
T_n=\frac{2L}{n}\sqrt{\frac{\rho}{S}}.
$$
截面面积和半径最终约去，是因为惯性与弹性力矩含同一个 $J_p$。""",
        4: r"""数值计算应保留临界场与导数两条独立中间量。给定
$$
t=\frac{T}{T_0}=\frac{1.95}{4.48}\simeq0.435268,
$$
有
$$
t^2\simeq0.189458,
\qquad
B_c=0.144(1-t^2)\simeq0.116718\,\mathrm T.
$$
另一方面
$$
-\frac{dB_c}{dT}
=\frac{2B_0T}{T_0^2}
=\frac{2(0.144)(1.95)}{(4.48)^2}
\simeq2.798\times10^{-2}\,\mathrm{T/K}.
$$
于是
$$
\begin{aligned}
\Delta S_n
&=\mu_0B_c\left(-\frac{dB_c}{dT}\right)\\
&=(1.25\times10^{-6})(0.116718)
(2.798\times10^{-2})\\
&\simeq4.08\times10^{-9}\,\mathrm{J/K}.
\end{aligned}
$$
按题设量的含义，这里 $M=-\mu_0B$ 已把体系的几何归一化包含在内；若 $M$ 是单位体积磁化强度，则对应结果应解释为熵密度差。微小卡诺循环中 $\Delta M=\mu_0B_c$ 是有限相变跳变量，而 $dB_c$ 是相邻临界点间的一阶小量，所以磁功为二者乘积；不能把两者都当作微分而误判为二阶可略。""",
        5: r"""小振动还可以直接从有效势的二阶导数读取。固定磁链
$$
\Phi_0=LI+SB(x,0)
$$
给
$$
I(x)=\frac{\Phi_0-SB(x,0)}L.
$$
沿 $x$ 轴
$$
B(x,0)=B_0\cos kx
=B_0-\frac12B_0k^2x^2+O(x^4).
$$
因此
$$
I(x)=I_0+\frac{B_0Sk^2}{2L}x^2+O(x^4).
$$
力为
$$
\begin{aligned}
F_x
&=I(x)S\frac{\partial B}{\partial x}\\
&=I(x)S[-B_0k\sin kx]\\
&=-I_0B_0Sk^2x+O(x^3).
\end{aligned}
$$
注意电流的 $x^2$ 修正与场梯度的一阶项相乘后是 $O(x^3)$，所以不进入线性频率。运动方程
$$
m\ddot x+I_0B_0Sk^2x=0
$$
给
$$
\boxed{\omega=k\sqrt{\frac{I_0B_0S}{m}}}.
$$
根号内量纲：
$$
[I_0B_0S]
=\mathrm A\cdot\mathrm{\frac N{A\,m}}\cdot\mathrm{m^2}
=\mathrm{N\,m}=\mathrm J,
$$
再乘 $k^2/m$ 得 $\mathrm{s^{-2}}$。若 $I_0B_0<0$，则 $\omega^2<0$，原点是势垒顶而非稳定点。""",
        6: r"""端口阻抗的模态叠加可用功率正交性检查。设端面四点电势向量分解为
$$
\boldsymbol V
=c_0\boldsymbol e_0+c_{2a}\boldsymbol e_{2a}
+c_{2b}\boldsymbol e_{2b}+c_4\boldsymbol e_4.
$$
四个本征向量可取
$$
\begin{aligned}
\boldsymbol e_0&=(1,1,1,1),\\
\boldsymbol e_{2a}&=(1,0,-1,0),\\
\boldsymbol e_{2b}&=(0,1,0,-1),\\
\boldsymbol e_4&=(1,-1,1,-1).
\end{aligned}
$$
它们分别对应 $\lambda=0,2,2,4$。均匀模态不产生横向或纵向电流，且两端口注入电流总和为零，所以其系数不影响电阻。对每个非均匀模态，衰减根
$$
q_\lambda
=\frac{\lambda+2-\sqrt{\lambda^2+4\lambda}}2
$$
满足
$$
q_\lambda+\frac1{q_\lambda}=\lambda+2.
$$
另一根大于1，若保留会使 $V_n$ 在 $n\to\infty$ 发散。模态端口导纳为
$$
Y_\lambda=\frac{\lambda+1-q_\lambda}{r}.
$$
总耗散功率可写为各正交模态功率之和
$$
P=\sum_\lambda Y_\lambda|c_\lambda|^2,
$$
没有交叉项。由 $P=I^2R_{\rm eq}$ 反算，可核对端口投影系数和因子2。""",
        7: r"""式（5）的二项展开可逐步写成
$$
\left(1-\frac32\varepsilon\right)^{-1/2}
=1+\frac12\left(\frac32\varepsilon\right)
+O(\varepsilon^2)
=1+\frac34\varepsilon+O(\varepsilon^2).
$$
于是
$$
\frac1v
=\frac1{c\sqrt{2a}}
\left[
\frac1{\sqrt{b^2-x^2}}
+\frac34a\sqrt{b^2-x^2}
\right].
$$
四分之一周期中第一项积分为
$$
\frac1{c\sqrt{2a}}\frac\pi2,
$$
修正项为
$$
\frac1{c\sqrt{2a}}\frac34a\frac{\pi b^2}{4}.
$$
乘以4：
$$
T=\frac{2\pi}{c\sqrt{2a}}
\left(1+\frac38ab^2\right).
$$
利用 $a=k/(2mc^2)$，
$$
c\sqrt{2a}
=c\sqrt{\frac{k}{mc^2}}
=\sqrt{\frac km},
$$
故主项确为 $2\pi\sqrt{m/k}$。相对修正
$$
\frac{\Delta T}{T_0}
=\frac38ab^2
=\frac38\frac{kb^2}{2mc^2}
=\frac38\frac{E_{k0}}{mc^2}.
$$
每个等号都保留了相同的无量纲小参数；若最后仍含长度或速度量纲，说明 $a$ 的定义或积分因子有误。""",
        8: r"""反射相位应先把复反射系数化成单位模的标准形式。全反射时令
$$
\kappa=\sqrt{n_1^2\sin^2\theta-n_2^2}>0.
$$
则垂直偏振反射系数可写为
$$
r=\frac{n_1\cos\theta+i\kappa}
{n_1\cos\theta-i\kappa}.
$$
分子、分母互为共轭，所以 $|r|=1$。若令
$$
\tan\psi=\frac{\kappa}{n_1\cos\theta},
$$
则
$$
n_1\cos\theta+i\kappa
=\sqrt{n_1^2\cos^2\theta+\kappa^2}\,e^{i\psi},
$$
分母对应 $e^{-i\psi}$，从而
$$
r=e^{2i\psi},\qquad
\delta(\theta)=2\arctan
\frac{\sqrt{n_1^2\sin^2\theta-n_2^2}}
{n_1\cos\theta}
$$
（整体符号随题目对 $\cos\theta_2$ 的支路约定改变）。横移只依赖相位随切向波数的导数：
$$
\Delta=-\frac{d\delta}{dk_x}
=-\frac{c}{n_1\omega\cos\theta}\frac{d\delta}{d\theta}.
$$
相位若整体加 $2\pi$ 不改变导数；但误选随 $\theta$ 不连续跳变的支路，会在数值求导中制造虚假尖峰，因此应保持 $\delta(\theta)$ 连续。""",
    },
    "050": {
        2: r"""支持力差可由质心径向方程逐状态写出。杆质心距碗心恒为
$$
d=\sqrt{R^2-\frac{L^2}{4}}.
$$
取指向圆心为径向正方向。转折点 $\theta=\theta_m$ 时 $\dot\theta=0$，但切向加速度为
$$
d\ddot\theta=-\frac{Mgd^2}{I_O}\sin\theta_m.
$$
平衡点 $\theta=0$ 时 $\ddot\theta=0$，而由能量
$$
\frac12I_O\dot\theta_0^2
=Mgd(1-\cos\theta_m).
$$
故
$$
\dot\theta_0^2
=\frac{2Mgd}{I_O}(1-\cos\theta_m)
\simeq\frac{Mgd}{I_O}\theta_m^2.
$$
两端支持力的合力可沿质心径向、切向分解；转折点的径向向心项为零，平衡点多出 $Md\dot\theta_0^2$。展开时
$$
\cos\theta_m=1-\frac12\theta_m^2+O(\theta_m^4)
$$
也贡献一个二阶重力分量。因此支持力之差的二阶系数必须同时包含“重力方向改变”和“平衡点向心加速度”两部分；只保留其中一项会使 $\alpha$ 错一项。""",
        3: r"""正则角动量跨边界的处理要区分“守恒量”与“连续量”。在外环区
$$
p_\varphi^{(0)}
=L_z-\frac12qB_0r^2
$$
守恒；在内区
$$
p_\varphi^{(x)}
=L_z-\frac12qB_xr^2
$$
守恒。由于矢势表达式改变，$p_\varphi^{(0)}$ 与 $p_\varphi^{(x)}$ 的数值一般不相等。粒子穿越理想边界时位置和机械速度连续，所以真正用于衔接的是
$$
L_z(R_1^-)=L_z(R_1^+).
$$
外区从径向入射的 $L_z(R_2)=0$ 出发：
$$
L_z(R_1)
=-\frac12qB_0(R_2^2-R_1^2).
$$
内区轨道过原点要求其关于原点的正则角动量为零：
$$
0=L_z(R_1)-\frac12qB_xR_1^2.
$$
联立即得
$$
B_x=-B_0\frac{R_2^2-R_1^2}{R_1^2}.
$$
速度 $v_0$ 在两式中约去不是偶然：只要粒子确实能到达 $R_1$，从 $R_2$ 到 $R_1$ 获得的机械角动量由穿过环带的磁通决定。$v_0$ 只影响到达边界的入射角和能否到达。""",
        4: r"""第一问还可显式求碰撞损失，检验越障阈值。碰前总动能
$$
E_-=\frac12mv_1^2+\frac12mr^2\left(\frac{v_1}{r}\right)^2
=mv_1^2.
$$
碰后绕棱角的角速度
$$
\Omega=\frac{v_1(2r-h)}{2r^2}
$$
给
$$
E_+=\frac12(2mr^2)\Omega^2
=mv_1^2\frac{(2r-h)^2}{4r^2}.
$$
损失比例为
$$
\frac{E_--E_+}{E_-}
=1-\left(1-\frac{h}{2r}\right)^2
=\frac hr-\frac{h^2}{4r^2}.
$$
当 $h\to0$ 时损失趋零，临界速度
$$
v_{\min}=\frac{2r\sqrt{gh}}{2r-h}
$$
也趋零；这两个极限相互一致。第三问中设分母
$$
D(\theta)=A\sin\theta+B\cos\theta-r\mu.
$$
由 $D'=A\cos\theta-B\sin\theta=0$ 得 $\tan\theta=A/B$，再有
$$
D''=-A\sin\theta-B\cos\theta<0,
$$
所以该点使分母最大、推力最小。若 $A/B<0$ 或角度越出接触范围，必须改比较端点。""",
        5: r"""初态可以在两个正交形状模上分解，以验证同频结论。取
$$
\boldsymbol e_s=(1,1),\qquad
\boldsymbol e_a=(1,-1)
$$
分别表示两侧液面同相、反相。题给
$$
(x_1,x_3)=(\varepsilon,-3\varepsilon)
$$
可写为
$$
(\varepsilon,-3\varepsilon)
=-\varepsilon(1,1)+2\varepsilon(1,-1).
$$
若两个模频率不同，运动会出现两种余弦并产生拍频；本题因
$$
\boldsymbol K=\frac gl\boldsymbol M
$$
使二者都满足
$$
\ddot q+\frac glq=0.
$$
所以重新合成后仍为
$$
(x_1,x_3)
=(\varepsilon,-3\varepsilon)
\cos\sqrt{\frac gl}\,t.
$$
中管由约束
$$
x_2=-\frac{x_1+x_3}{2}
=\varepsilon\cos\sqrt{\frac gl}\,t.
$$
把三者代回体积变化：
$$
x_1+2x_2+x_3
=\varepsilon+2\varepsilon-3\varepsilon
$$
乘同一余弦，任意时刻恒为零。该回代同时检查了振幅的符号和中管面积因子2。""",
        6: r"""式（4）的短时极限可用尾积分更精确地核对。当 $a\to\infty$，
$$
f(a)\to\frac{\sqrt\pi}{2},
\qquad e^{-a^2}\to0,
$$
于是
$$
\frac{N_c}{N}
\simeq\frac1{2\sqrt\pi\,a}
=\frac{tv_T}{2\sqrt\pi\,l}.
$$
这等于“单位时间撞壁通量乘面积与时间”除以总粒子数。动量式
$$
\Delta P=\frac{2p_0St}{\sqrt\pi}f(a)
$$
则趋于
$$
\Delta P\simeq p_0St,
$$
故初始平均力 $dP/dt=p_0S$，恰是平衡压强对右壁的力。长时 $a\to0$ 时
$$
f(a)=a-\frac{a^3}{3}+O(a^5),
$$
所以
$$
\Delta P
=\frac{Nmv_T}{\sqrt\pi}
\left(1-\frac{a^2}{3}+\cdots\right),
$$
趋于有限值，因为每个初始 $v_x>0$ 的分子只撞右壁一次，反射后便从开放左端逃出。若积分结果随 $t\to\infty$ 仍线性增长，说明误把右壁当作持续由外界补充的平衡气体压力。""",
        7: r"""两种边界半径可用反向代入检验。可见区域边缘取
$$
r=\frac{3D_2}{2}.
$$
穿过孔径光阑 $L_2$ 中心的主光线初始倾角
$$
u=-\frac r{l_2}.
$$
在 $L_1$ 处
$$
y_1=r+l_1u
=r-2r=-r=-\frac{3D_2}{2}
=-\frac{D_1}{2},
$$
恰擦过 $L_1$ 边缘，而在 $L_2$ 处 $y_2=0$。明亮区域边缘取 $R=D_2$，指定通过 $L_1$ 中心：
$$
u=-\frac R{l_1}.
$$
传播到 $L_2$：
$$
y_2=l_2u
=-\frac{l_2}{l_1}R
=-\frac{D_2}{2},
$$
恰擦过 $L_2$ 边缘。两个边界分别由不同透镜截断，且
$$
R_{\rm bright}=D_2
<r_{\rm visible}=\frac{3D_2}{2}.
$$
外围点仍可能有部分光线通过而“可见”，但题目指定的中心光线已被截去，所以不再属于明亮区。这个大小关系是概念区分的直接物理检查。""",
        8: r"""二次方程的小根可有理化以避免数值消减。正文中
$$
\delta=
\frac{(1-s^2)-\sqrt{(1-s^2)^2-2s^2\lambda}}s
$$
的分子在 $\lambda\ll1$ 时是两个很接近的数。乘以共轭：
$$
\begin{aligned}
\delta
&=\frac{[(1-s^2)^2-
((1-s^2)^2-2s^2\lambda)]/s}
{(1-s^2)+\sqrt{(1-s^2)^2-2s^2\lambda}}\\
&=\boxed{
\frac{2s\lambda}
{(1-s^2)+\sqrt{(1-s^2)^2-2s^2\lambda}}
}.
\end{aligned}
$$
当 $\lambda\to0$，
$$
\delta\simeq\frac{s\lambda}{1-s^2}.
$$
代入
$$
L_A=\frac{c^2}{a}\frac{\delta}{s}\sqrt{1-s^2}
$$
得到
$$
L_A\simeq
\frac{c^2}{a}\frac{\lambda}{\sqrt{1-s^2}}
=\gamma_Al.
$$
这里 $\gamma_Al$ 大于地面长度 $l$，并不违反通常的长度收缩：通常公式假定本征长度固定，而题设运动恰使本征长度随时间增长。判别式
$$
(1-s^2)^2-2s^2\lambda\ge0
$$
还限制了局部瞬时惯性系同时线能否在题设有效世界线段内与车头相交。""",
    },
    "051": {
        1: r"""远轴距近似的误差可以从开式带传动的精确长度看出。设轴距为 $L$、两有效半径为 $r_1,r_2$，公切线与中心线夹角满足
$$
\sin\alpha=\frac{r_1-r_2}{L}.
$$
带长为两段公切线加两段圆弧：
$$
\mathcal L
=2\sqrt{L^2-(r_1-r_2)^2}
+(\pi+2\alpha)r_1+(\pi-2\alpha)r_2.
$$
当 $|r_1-r_2|\ll L$ 时，
$$
\sqrt{L^2-(r_1-r_2)^2}
=L-\frac{(r_1-r_2)^2}{2L}+\cdots,
$$
且
$$
\alpha\simeq\frac{r_1-r_2}{L}.
$$
因此一阶项只剩
$$
\mathcal L=2L+\pi(r_1+r_2)
+O\!\left(\frac{(r_1-r_2)^2}{L}\right).
$$
这就严格说明为何一阶带长约束是 $dr_1+dr_2=0$，而不是凭图假设两处各包半圆。由
$$
dr_i=-\frac12\tan\frac\theta2\,dd_i
$$
进一步得到 $dd_1+dd_2=0$。主动轮间距减少 $x$，从动轮间距必增加 $x$，符号来自总长微分而不是经验判断。""",
        6: r"""过程 $c$ 的热量也可直接求“过程热容量”复核。因
$$
p=\frac{p_0}{V_0}V,
\qquad
pV=nRT,
$$
有
$$
\frac{p_0}{V_0}V^2=nRT.
$$
微分：
$$
2\frac{p_0}{V_0}V\,dV=nR\,dT.
$$
但 $(p_0/V_0)V=p$，所以
$$
p\,dV=\frac12nR\,dT.
$$
第一定律给
$$
dQ=nC_V\,dT+p\,dV
=n\left(C_V+\frac R2\right)dT.
$$
因此过程 $c$ 的摩尔热容量为
$$
C_c=C_V+\frac R2=3R.
$$
从 $4T_0$ 降到 $T_0$：
$$
Q_c=n(3R)(-3T_0)
=-9nRT_0=-9p_0V_0,
$$
与分开计算 $\Delta U_c$ 和 $W_c$ 完全一致。这条路线还解释了为什么过程 $c$ 虽是压缩，$p\,dV<0$，但过程热容量仍为正：降温 $dT<0$，所以 $dQ<0$。""",
        8: r"""求和上限必须在代数开头固定。若严格按 $n<p$ 且 $n$ 为正整数，
$$
n=1,2,\ldots,p-1,
$$
则
$$
\sum_{n=1}^{p-1}n=\frac{p(p-1)}2
$$
并有
$$
E_{<p}(d)
=\frac{\pi\hbar c}{4d}p(p-1),
\qquad
|F|_{<p}
=\frac{\pi\hbar c}{4d^2}p(p-1).
$$
若题目约定“截断到第 $p$ 模”，才改为 $p(p+1)$。对 $p=2000$，
$$
\frac{F_{<p}}{F_{\le p}}
=\frac{1999}{2001}
\simeq0.9990005,
$$
数值只差约 $0.1\%$，但符号答案应注明约定。量纲检查：
$$
[a]=[\hbar c]=\mathrm{J\,m},
\qquad
\left[\frac a{d^2}\right]
=\mathrm{\frac Jm}=\mathrm N.
$$
本题固定的是模序号上限，故最大波数 $k_{\max}=p\pi/d$ 随 $d$ 改变；若固定物理波数截止，保留模数本身会随 $d$ 变化，力的标度也会改变。这正说明有限截断结果不是普适三维卡西米尔常数。""",
    },
    "053": {
        5: r"""各统计量可统一由矩公式得到。对 $n>-1$，
$$
\begin{aligned}
\langle v^n\rangle
&=\int_0^1v^n(-3v^2+2v+1)\,dv\\
&=-\frac3{n+3}+\frac2{n+2}+\frac1{n+1}.
\end{aligned}
$$
取 $n=0$：
$$
-1+1+1=1,
$$
复核归一化；取 $n=1$：
$$
-\frac34+\frac23+\frac12=\frac5{12};
$$
取 $n=2$：
$$
-\frac35+\frac12+\frac13=\frac7{30}.
$$
进一步计算方差：
$$
\begin{aligned}
\operatorname{Var}(v)
&=\langle v^2\rangle-\langle v\rangle^2\\
&=\frac7{30}-\frac{25}{144}\\
&=\frac{168-125}{720}
=\frac{43}{720}>0.
\end{aligned}
$$
所以
$$
v_{\rm rms}^2-\bar v^2=\frac{43}{720}>0,
$$
严格验证 $v_{\rm rms}>\bar v$。最概然值还需与端点比较：
$$
f(0)=1,\quad f(1)=0,\quad
f\!\left(\frac13\right)=\frac43.
$$
因此 $v=1/3$ 确为整个支撑区间的全局最大，而不仅是形式驻点。""",
        6: r"""连续极限可以从精确离散式取出误差阶。每次撞运动镜的频率倍率
$$
q=\frac{1+\beta}{1-\beta}
$$
满足
$$
\ln q
=\ln(1+\beta)-\ln(1-\beta)
=2\beta+\frac23\beta^3+O(\beta^5).
$$
腔长缓慢缩短时，累计碰撞次数的一阶式为
$$
N\simeq\frac1{2\beta}\ln\frac{l_0}{x}.
$$
所以
$$
\ln\frac{\nu}{\nu_0}
=N\ln q
=\left[1+\frac13\beta^2+O(\beta^4)\right]
\ln\frac{l_0}{x}.
$$
在 $\beta\to0$ 的绝热极限恢复
$$
\nu x=\nu_0l_0.
$$
这也说明连续结果的首个相对修正是 $O(\beta^2)$ 而非 $O(\beta)$。力的两种算法闭合：
$$
F=-\frac{d}{dx}
\left(\frac{h\nu_0l_0}{x}\right)
=\frac{h\nu_0l_0}{x^2},
$$
而冲量通量给
$$
F\simeq\left(\frac{2h\nu}{c}\right)
\left(\frac{c}{2x}\right)
=\frac{h\nu}{x}
=\frac{h\nu_0l_0}{x^2}.
$$
前一式检查能量，后一式检查反射冲量和往返时间的两个因子2。""",
    },
}


EXTRA_ADDITIONS: dict[str, dict[int, str]] = {
    "046": {
        2: r"""把第（3）问的极限讨论写成闭合方程组更稳妥。地面光滑时，圆柱只受重力、地面支持力、墙面法向力和墙面摩擦力。先约定墙面摩擦向上为正，分别写
$$
N_w=ma_x,
\qquad
N+f_w-mg=ma_y,
$$
再关于质心写力矩方程
$$
r f_w=I_C\alpha.
$$
接触约束把 $a_x,a_y,\alpha$ 联系起来。联立求出 $f_w/N_w$ 后，静摩擦条件才是
$$
\left|\frac{f_w}{N_w}\right|\le\mu_w.
$$
若算得 $f_w<0$，只表示真实方向与预设相反，不可在中途把摩擦力大小和代数量混写。极限 $a\to0$ 应回到静力平衡；$h\to r$ 时重心与几何中心等高，关于重心的力臂结构应相应简化。""",
        5: r"""长度因子可以从积分而非图形猜测。抛物线 $y=kx^2$ 与水平线 $y=vt$ 的两个交点为
$$
x_\pm=\pm\sqrt{\frac{vt}{k}},
$$
所以切割出的导体总长是
$$
L=x_+-x_-=2\sqrt{\frac{vt}{k}}.
$$
电动势也可逐段积分：
$$
\mathcal E=\int_{x_-}^{x_+}(\boldsymbol v\times\boldsymbol B)\cdot d\boldsymbol l
=Bv(x_+-x_-)=BvL.
$$
由 $R=\lambda L$ 得 $I=Bv/\lambda$，长度恰好约去。随后
$$
F=\int_{x_-}^{x_+}IB\,dx=IBL,
\qquad
Fv=IBLv=I\mathcal E=I^2R.
$$
机械功率、电功率和焦耳热三式完全一致，既检查了因子2，也说明磁场本身不供能；外力克服磁阻力所做的功才转化为热。""",
        6: r"""轴线附近的 $0/0$ 应在组合后取极限。若亮度表达式含
$$
\frac{p\,dp}{a\,da}
$$
与角度雅可比，不应分别把每个因子代 $a=0$。先令 $q=a/r$，将折射关系、像面半径和立体角全部写成 $q$ 的函数，再用
$$
\sin\theta\simeq\theta,
\qquad
\cos\theta\simeq1-\frac12\theta^2
$$
展开到第一个非零阶，分子分母的同阶小量才会正确相消。边缘处同理，单个雅可比可以发散，但环带能量还含面积元；最终应检查总功率积分有限并等于入射功率乘透过率。""",
    },
}


DEEPENING_ADDITIONS: dict[str, dict[int, str]] = {
    "045": {
        1: r"""还可把最终速度化成只含周期与质量的组合，以检查各步是否一致。由
$$
L^3=\frac{G(M_S+M_E)T^2}{4\pi^2},
\qquad
v_S=\frac{2\pi}{T}\frac{M_E}{M_S+M_E}L,
$$
逐项代入得
$$
\begin{aligned}
v_S
&=\frac{M_E}{M_S+M_E}
\frac{2\pi}{T}
\left[\frac{G(M_S+M_E)T^2}{4\pi^2}\right]^{1/3}\\
&=M_EG^{1/3}
\left(\frac{2\pi}{T}\right)^{1/3}
(M_S+M_E)^{-2/3}.
\end{aligned}
$$
第二行中每一项的幂次都来自前一行：$T^{-1}T^{2/3}=T^{-1/3}$，$(M_S+M_E)^{-1}(M_S+M_E)^{1/3}=(M_S+M_E)^{-2/3}$。因此
$$
[v_S]=\mathrm{kg}\,
(\mathrm{m^3\,kg^{-1}\,s^{-2}})^{1/3}
\mathrm{s^{-1/3}}\,
\mathrm{kg^{-2/3}}
=\mathrm{m\,s^{-1}}.
$$
数值上先算质量比
$$
\frac{M_E}{M_S+M_E}
=\frac{6.0\times10^{24}}{2.000006\times10^{30}}
\simeq2.99999\times10^{-6},
$$
再乘地球相对轨道速度 $2\pi L/T\simeq2.98\times10^4\,\mathrm{m/s}$，仍得
$$
v_S\simeq(2.99999\times10^{-6})(2.98\times10^4)
=8.94\times10^{-2}\,\mathrm{m/s}.
$$
这一复算把“太阳的小轨道半径”方法与“质量比乘相对速度”方法闭合起来。若题目所称“往返最大速率”指观测到的径向速度半振幅，则答案为 $v_S\sin i$，其中 $i$ 是轨道法线与视线的夹角；本题未给倾角，默认取边缘朝向 $i=90^\circ$。""",
        2: r"""相对加速度式可由滚动约束与力矩方程逐项消元。取沿斜面向下为正，圆柱质心相对斜面的加速度为 $a_r$，斜面系中的等效沿面驱动力为
$$
F_{\parallel}=mg\sin\theta-ma_0\cos\theta.
$$
设静摩擦力沿斜面向上，平动方程为
$$
ma_r=F_{\parallel}-f.
$$
绕质心取矩：
$$
fr=I_C\alpha.
$$
纯滚动约束给 $a_r=r\alpha$，因而
$$
f=\frac{I_C}{r^2}a_r.
$$
代回平动方程：
$$
\left(m+\frac{I_C}{r^2}\right)a_r
=mg\sin\theta-ma_0\cos\theta.
$$
均匀实心圆柱 $I_C=mr^2/2$，所以
$$
\boxed{
a_r=\frac23(g\sin\theta-a_0\cos\theta)
}.
$$
随后才变换回地面系：
$$
\begin{aligned}
a_x&=a_0+a_r\cos\theta,\\
a_y&=-a_r\sin\theta.
\end{aligned}
$$
把 $a_0=0$ 代回，得到固定斜面上的 $2g\sin\theta/3$；把 $a_0=g\tan\theta$ 代回，得到 $a_r=0$，说明在这一加速度下圆柱可相对斜面静止。还必须检查静摩擦能否提供所需的
$$
f=\frac13m(g\sin\theta-a_0\cos\theta),
$$
即 $|f|\le\mu_sN$。斜面系法向平衡给
$$
N=m(g\cos\theta+a_0\sin\theta),
$$
由此可进一步写出保持纯滚动的摩擦条件。""",
        5: r"""镜像线电荷的强度和位置可以从圆柱表面等势条件同时确定。设真实线电荷为 $+\lambda$，像线电荷为 $-\lambda$，两者到接地平面的距离均为 $d$，则上半平面电势
$$
\varphi(P)=\frac{\lambda}{2\pi\varepsilon}
\ln\frac{r_-}{r_+},
$$
其中 $r_+$、$r_-$ 分别是点 $P$ 到正、负线电荷的距离。等势线满足
$$
\frac{r_-}{r_+}=K,
$$
这是一族阿波罗尼斯圆。把圆心到平面的距离记为 $l$、半径记为 $r$，考察圆上最靠近和最远离平面的两点：
$$
\frac{l-r+d}{l-r-d}=K,
\qquad
\frac{l+r+d}{l+r-d}=K.
$$
消去 $K$：
$$
(l-r+d)(l+r-d)
=(l+r+d)(l-r-d).
$$
展开两边并约去公共项，得到
$$
d^2=l^2-r^2.
$$
因此可令
$$
\cosh u=\frac lr,
\qquad
\sinh u=\frac dr,
$$
从而 $u=\operatorname{arccosh}(l/r)$。圆柱相对平面的电势差为
$$
U=\frac{\lambda}{2\pi\varepsilon}u,
$$
单位长度电容即
$$
\boxed{
C'=\frac{\lambda}{U}
=\frac{2\pi\varepsilon}{\operatorname{arccosh}(l/r)}
}.
$$
远距离 $l\gg r$ 时，
$$
\operatorname{arccosh}\frac lr
=\ln\left(\frac lr+\sqrt{\frac{l^2}{r^2}-1}\right)
=\ln\frac{2l}{r}-\frac{r^2}{4l^2}
+O\!\left(\frac{r^4}{l^4}\right).
$$
于是修正从 $(r/l)^2$ 开始，没有一次项；这与把圆柱半径反号不改变几何的对称性一致。""",
        7: r"""双圆环边界下的积分常数不能沿用单圆膜的中心正则性。若线性化形状方程写成
$$
\frac1x\frac{d}{dx}\left(x\frac{dz}{dx}\right)=C,
$$
先乘以 $x$：
$$
\frac{d}{dx}\left(xz'\right)=Cx.
$$
第一次积分得
$$
xz'=\frac C2x^2+C_1,
\qquad
z'=\frac C2x+\frac{C_1}{x}.
$$
第二次积分：
$$
z(x)=\frac C4x^2+C_1\ln x+C_2.
$$
若定义域包含 $x=0$，有限性迫使 $C_1=0$；但环膜只在 $r_1\le x\le r_2$ 上存在，$\ln x$ 在整个定义域内有限，不能删掉。用
$$
z(r_1)=z_1,\qquad z(r_2)=z_2
$$
相减，先求
$$
C_1=
\frac{z_2-z_1-\frac C4(r_2^2-r_1^2)}
{\ln(r_2/r_1)},
$$
再由任一边界求 $C_2$。单圆膜的斜率式也可由环形微元验证：半径 $x$ 内重量为 $\rho g\pi x^2$，上下两表面的张力竖直分量为 $4\pi x\sigma z'$，故
$$
z'=\frac{\rho g}{4\sigma}x.
$$
左右两边量纲都是无量纲斜率；若漏掉“两表面”的因子2，会使最终下垂量整体大一倍。""",
    },
    "046": {
        1: r"""球形与无限圆柱形引力场的差别可以从高斯定律的包围质量看清。球外半径 $r$ 处
$$
g_r\,4\pi r^2=4\pi GM
\quad\Longrightarrow\quad
g_r=\frac{GM}{r^2},
$$
圆轨道条件 $v^2/r=g_r$ 给
$$
v^2=\frac{GM}{r}.
$$
结合 $v=2\pi r/T$ 后才有
$$
r^3=\frac{GMT^2}{4\pi^2}.
$$
无限实心圆柱外部则取半径 $r$、长度 $\ell$ 的同轴高斯柱：
$$
g_r(2\pi r\ell)
=4\pi G(\rho\pi R^2\ell),
$$
从而
$$
g_r=\frac{2\pi G\rho R^2}{r}.
$$
再代入圆周运动：
$$
\frac{v^2}{r}=\frac{2\pi G\rho R^2}{r}
\quad\Longrightarrow\quad
\boxed{v=R\sqrt{2\pi G\rho}}.
$$
轨道半径约去，意味着所有圆柱外的圆轨道具有同一线速度，而周期 $T=2\pi r/v$ 正比于 $r$。若误把包围质量写成 $\rho\pi r^2\ell$，所得
$$
g_r=2\pi G\rho r
$$
其实是圆柱内部 $r<R$ 的场；这时 $v=r\sqrt{2\pi G\rho}$ 才正比于半径。用 $r=R$ 检查，两侧表达式连续：
$$
g_{\rm in}(R)=g_{\rm out}(R)=2\pi G\rho R.
$$
这一连续性是区分内外场公式的直接判据。""",
        3: r"""场线圆的圆心与半径应从坐标方程算出。设圆过
$$
P_1=(a,0),\quad P_2=(-a,0),\quad P_3=(0,\eta a),
$$
由关于 $y$ 轴对称可设圆心为 $(0,c)$、半径为 $\mathcal R$。于是
$$
\mathcal R^2=a^2+c^2=(\eta a-c)^2.
$$
展开并约去 $c^2$：
$$
a^2=\eta^2a^2-2\eta ac,
$$
所以
$$
c=\frac{\eta^2-1}{2\eta}a,
\qquad
\mathcal R=\frac{\eta^2+1}{2|\eta|}a.
$$
两圆弧围成的面积不能直接写成 $\pi\mathcal R^2$，而应按每一侧的圆心角用
$$
A_{\rm seg}=\frac12\mathcal R^2(\psi-\sin\psi)
$$
计算弓形面积，再依据弧位于弦的哪一侧选择 $\psi$ 的支路。电流部分若电势由二维源组成，
$$
U=\sum_i A_i\ln r_i+C,
$$
则
$$
\boldsymbol j=-\sigma_0\nabla U
$$
中的系数 $A_i$ 由电极电压差重新归一化。移动电极后，既改变 $\nabla\ln r_i$ 的几何因子，也改变满足相同端电压所需的 $A_i$；只比较中心处距离而不重算归一化会漏掉后一项。""",
        4: r"""自由转动问题中，应先用角动量守恒消去角速度，再展开有效势。设液面变量为 $x$，系统转动惯量为
$$
I(x)=I_0+I_1x+I_2x^2+O(x^3),
$$
总角动量 $J=I(x)\omega$ 守恒，因此转动动能不是 $\tfrac12I(x)\omega_0^2$，而是
$$
T_{\rm rot}(x)=\frac{J^2}{2I(x)}.
$$
利用
$$
\frac1{I(x)}
=\frac1{I_0}
\left[
1-\frac{I_1}{I_0}x
+\left(\frac{I_1^2}{I_0^2}-\frac{I_2}{I_0}\right)x^2
+O(x^3)
\right],
$$
得到
$$
T_{\rm rot}
=\frac{J^2}{2I_0}
-\frac{J^2I_1}{2I_0^2}x
+\frac{J^2}{2I_0}
\left(\frac{I_1^2}{I_0^2}-\frac{I_2}{I_0}\right)x^2+\cdots.
$$
重力势能也展开为 $V_g=V_0+V_1x+V_2x^2+\cdots$。平衡点的必要条件是一次项严格相消：
$$
V_1-\frac{J^2I_1}{2I_0^2}=0.
$$
二次项之和才是恢复刚度；若一次项未消失，说明 $x=0$ 并非所选转速下的平衡状态，不能直接从二次项读频率。恒定角速度情形则由外界电机交换角动量，使用旋转系等势量 $gz-\omega_0^2s^2/2$，两种问题的能量约束不同。""",
        7: r"""虹的驻值条件应先对角度映射求导，再做存在性筛选。对经历 $N$ 次内部反射的光线，
$$
\Delta_N=N\pi+2\alpha-2(N+1)\theta,
$$
而折射定律为
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
驻值条件 $d\Delta_N/d\alpha=0$ 给
$$
1-(N+1)\frac{\cos\alpha}{n\cos\theta}=0,
$$
即
$$
n\cos\theta=(N+1)\cos\alpha.
$$
平方并用 $\sin\alpha=n\sin\theta$ 消去 $\theta$：
$$
n^2-\sin^2\alpha=(N+1)^2\cos^2\alpha.
$$
整理得到
$$
\boxed{
\sin^2\alpha
=\frac{(N+1)^2-n^2}{(N+1)^2-1}
}.
$$
右侧必须处于 $[0,1]$，首先要求 $n\le N+1$。若某一级不满足存在条件，就不存在可比较强度的驻值虹。强度比较还要区分振幅反射系数和能量反射率：多一次内部反射时振幅多乘 $r'$，强度则多乘 $|r'|^2$。""",
    },
    "047": {
        1: r"""势能极值还应验证是最大下降量而非不稳定驻点。令约束
$$
g(\theta_1,\theta_2)
=\cos\theta_1+\cos\theta_2-\frac{L}{2l}=0
$$
解出 $\theta_2(\theta_1)$。一阶导数已给
$$
\theta_2'=-\frac{\sin\theta_1}{\sin\theta_2}.
$$
再对约束求导：
$$
-\cos\theta_1
-\cos\theta_2(\theta_2')^2
-\sin\theta_2\theta_2''=0,
$$
所以
$$
\theta_2''
=-\frac{\cos\theta_1+\cos\theta_2(\theta_2')^2}
{\sin\theta_2}.
$$
把它代入
$$
F(\theta_1)=3\sin\theta_1+\sin\theta_2(\theta_1)
$$
的二阶导数
$$
F''=-3\sin\theta_1
-\sin\theta_2(\theta_2')^2
+\cos\theta_2\theta_2''
$$
并代入正根对应的 $0<\theta_1,\theta_2<\pi/2$，各项合成后为负，说明 $F$ 取局部最大、重力势能取局部最小。数值求根也可把式（6）平方两次化为关于 $y=x^2$ 的多项式，但每次平方都会引入额外根，因此仍要回到未平方的
$$
\frac1{\sqrt{1+9x^2}}+\frac1{\sqrt{1+x^2}}=1.6
$$
筛选 $x>0$。二分法没有这一增根问题，并且单调性已保证唯一。""",
        2: r"""第（1）问的数值根可完整复算。取
$$
A=40(\sin35^\circ+\cos35^\circ\tan30^\circ).
$$
分别计算
$$
\sin35^\circ\simeq0.573576,\quad
\cos35^\circ\simeq0.819152,\quad
\tan30^\circ\simeq0.577350,
$$
故
$$
A\simeq40(0.573576+0.472917)
=41.8597\,\mathrm{m/s}.
$$
判别式为
$$
A^2-2gh
\simeq(41.8597)^2-2(10)(15)
\simeq1452.24\,\mathrm{m^2/s^2},
$$
开方得 $38.108\,\mathrm{m/s}$。因此
$$
t_1=\frac{41.8597-38.108}{10}
\simeq0.3752\,\mathrm s.
$$
代入
$$
x_1=40\cos35^\circ\,t_1
\simeq12.29\,\mathrm m,
$$
再由顶棚直线
$$
y_1=15-x_1\tan30^\circ
\simeq7.90\,\mathrm m.
$$
速度分量为
$$
v_x=32.766\,\mathrm{m/s},\qquad
v_y=22.943-3.752=19.191\,\mathrm{m/s}.
$$
机械能检查：
$$
v_x^2+v_y^2
\simeq1442.3,
$$
而
$$
v_0^2+2g(0-y_1)
=1600-158.0=1442.0,
$$
差异只来自舍入。若用较大根，轨迹在代数上再次与无限延长斜线相交，但实体顶棚已在 $t_1$ 处阻断运动，故不能作为第二个实际碰撞。""",
        3: r"""有限物距的反例可以把“平面无焦度”的边界说清。设水中物点距平面第一面为 $s$，第一面半径 $R_1=\infty$。球面折射公式给
$$
\frac{n}{v_1}-\frac{n_w}{-s}=0,
$$
于是
$$
v_1=-\frac{n}{n_w}s.
$$
这表示进入玻璃后的发散束仿佛来自距第一面 $ns/n_w$ 的虚物点。若镜片厚度可忽略，第二曲面的物距不再是无穷大，而是上述有限量，最终成像式变为
$$
\frac1{v_2}-\frac n{u_2}
=\frac{1-n}{R}.
$$
当外界从水换成空气时 $n_w$ 改变，$u_2$ 随之改变，像位一般会变。只有 $s\to\infty$ 时，两种介质都给 $u_2\to-\infty$，水侧平面的差异消失。由此可见，题目第二问的结论依赖“远处物体”而不是“平面界面完全没有折射”。符号方面，若选光从左向右为正，凹面球心位于入射侧时 $R<0$；最终必须满足
$$
\Phi=\frac1f<0,
$$
否则所得镜片成了会聚镜。把 $R$ 用厘米代入 $1/f$ 前要先换成米，再乘 $100$ 转为日常眼镜度数，两个换算步骤不能互相抵消。""",
        4: r"""有限长圆柱的端效应可以由等效端面磁荷估计。磁化强度
$$
\boldsymbol M=np_m\boldsymbol e_z
$$
在侧面满足 $\boldsymbol M\cdot\boldsymbol n=0$，在两端满足
$$
\sigma_m=\boldsymbol M\cdot\boldsymbol n=\pm M.
$$
半径为 $R$、面磁荷密度为 $\sigma_m$ 的圆盘，在轴线上距盘面 $z$ 处产生的场可写成
$$
H_z(z)=\frac{\sigma_m}{2}
\left(1-\frac{z}{\sqrt{z^2+R^2}}\right)
$$
并按观察点位于哪一侧确定方向。圆柱中心到两端的距离均为 $L/2$，两端贡献同向，因此
$$
H_{\rm center}
=M\left[
1-\frac{L/2}{\sqrt{(L/2)^2+R^2}}
\right]
$$
或其与题目几何相应的退磁形式。长圆柱 $L\gg R$ 与薄圆片 $L\ll R$ 的极限不同，说明 $B=\mu_0M$ 只在题设“足够长、中心远离端部”的近似下成立。Ampere 图像中侧面束缚电流
$$
\boldsymbol K_b=\boldsymbol M\times\boldsymbol n
$$
沿环向流动，等效为面电流密度 $K_b=M$ 的螺线管；它与端面磁荷图像给出的端效应必须一致。""",
        5: r"""压强变化引起的汽化量应先由状态方程求出。若容器体积固定、温度在所考察小段内保持为 $T$，
$$
pV=nRT.
$$
微分为
$$
V\,dp=RT\,dn,
$$
所以
$$
dn=\frac{V}{RT}\,dp.
$$
这部分新生成蒸气所需热量为 $L\,dn$，但气体内能增加只含
$$
(L-RT)\,dn,
$$
因为每摩尔汽化还要用 $p\,dV_{\rm phase}\simeq RT$ 对外做膨胀功。若容器整体刚性，这一“相变体积功”体现在液相缩小、气相占据空间的内部功收支中，不能因为外壁不动就把它从摩尔焓与内能的关系中删去。总热量还可能包含原有气体和容器的显热项
$$
dQ_{\rm sensible}=C_{\rm eff}\,dT.
$$
因此完整微分通常写成
$$
dQ=C_{\rm eff}\,dT+L\,dn,
$$
而内能式写成
$$
dU=C_{V,\rm eff}\,dT+(L-RT)\,dn.
$$
使用哪一个取决于题目是直接求吸热还是先列第一定律。令 $dp=0$ 时汽化量增量应为零；令 $L\gg RT$ 时两种热量差异相对较小，这两个极限都与表达式相符。""",
        6: r"""三态平均场的变分可以把约束项完整写出。每格自由能
$$
f=-\frac12qJm^2
+kT(P_+\ln P_++P_0\ln P_0+P_-\ln P_-)
+\Lambda(P_++P_0+P_--1),
$$
其中 $m=P_+-P_-$。对三个概率分别求偏导：
$$
\begin{aligned}
\frac{\partial f}{\partial P_+}
&=-qJm+kT(\ln P_++1)+\Lambda=0,\\
\frac{\partial f}{\partial P_0}
&=kT(\ln P_0+1)+\Lambda=0,\\
\frac{\partial f}{\partial P_-}
&=qJm+kT(\ln P_-+1)+\Lambda=0.
\end{aligned}
$$
第一式减第二式、第三式减第二式，常数 $1$ 与 $\Lambda$ 同时消去：
$$
\ln\frac{P_+}{P_0}=\frac{qJm}{kT},
\qquad
\ln\frac{P_-}{P_0}=-\frac{qJm}{kT}.
$$
这就得到正文的概率比。继续把自洽式展开到三阶：
$$
m=\frac23y-\frac19y^3+O(y^5),
\qquad y=\frac{qJm}{kT}.
$$
对非零 $m$ 移项并除以 $m$：
$$
1-\frac{2qJ}{3kT}
=-\frac19\left(\frac{qJ}{kT}\right)^3m^2+\cdots.
$$
在 $T$ 略低于 $T_c$ 时得到 $m^2\propto T_c-T$，说明非零解连续出现；这也验证临界点应由一次斜率等于1而不是概率突然跳变确定。""",
    },
}


FINAL_STUDENT_ADDITIONS: dict[str, dict[int, str]] = {
    "045": {
        6: r"""四个循环状态可以列成一张代数清单，以避免把两条绝热线的端点配错。记低温等温线两端为
$$
A:(T_0,V_0),\qquad
B:(T_0,2V_0).
$$
绝热关系 $T^2V^{1/3}=\text{常量}$ 给出
$$
\begin{aligned}
B\to C:\quad
T_0^2(2V_0)^{1/3}
&=(2T_0)^2V_C^{1/3},\\
V_C^{1/3}
&=\frac14(2V_0)^{1/3},\\
V_C&=\frac{2V_0}{4^3}
=\frac{V_0}{32}.
\end{aligned}
$$
另一条绝热线 $D\to A$：
$$
\begin{aligned}
(2T_0)^2V_D^{1/3}
&=T_0^2V_0^{1/3},\\
V_D^{1/3}&=\frac14V_0^{1/3},\\
V_D&=\frac{V_0}{64}.
\end{aligned}
$$
所以高温等温压缩确为
$$
\frac{V_C}{V_D}
=\frac{V_0/32}{V_0/64}=2.
$$
在 $T=2T_0$ 时全部解离，总粒子物质的量是 $2n_0$，故
$$
\begin{aligned}
Q_{CD}
&=(2n_0)R(2T_0)
\ln\frac{V_D}{V_C}\\
&=4n_0RT_0\ln\frac12\\
&=-4n_0RT_0\ln2.
\end{aligned}
$$
负号表示系统放热，其大小才是 $Q_2=4n_0RT_0\ln2$。低温段
$$
Q_{AB}=n_0RT_0\ln2>0.
$$
全循环系统吸热代数和为 $Q_1-Q_2<0$，因此系统对外净功也为负；这直接确认题述方向是制冷方向，而不是只根据图形顺逆时针猜测。""",
    },
    "046": {
        8: r"""相对论火箭方程中的快速度形式可由一次微小喷射说明。设火箭瞬时静止系中，喷出静质量 $-dm>0$ 的产物，产物相对火箭的有效喷速为 $u$。在一阶小量下，喷流带走的动量大小与质量损失成正比，火箭获得的微小快速度满足
$$
d\psi=-\frac{u}{c}\frac{dm}{m},
\qquad
\psi=\operatorname{artanh}\beta.
$$
积分时质量从 $m_i$ 减到 $m_f$：
$$
\begin{aligned}
\int_0^{\psi_f}d\psi
&=-\frac uc\int_{m_i}^{m_f}\frac{dm}{m}\\
\psi_f
&=\frac uc\ln\frac{m_i}{m_f}.
\end{aligned}
$$
因此
$$
\boxed{
\frac{m_i}{m_f}
=\exp\left(\frac c u\operatorname{artanh}\beta_f\right)
}.
$$
第（5）问先得到的是总质量比
$$
R=\frac{m_i}{m_f}=5.87203.
$$
若干质量为 $m_f$，燃料质量为 $m_i-m_f$，题目定义的燃料比为
$$
\eta=\frac{m_i-m_f}{m_f}=R-1=4.87203.
$$
第（6）问总质量比为 $101$，加速、减速两阶段的质量比满足
$$
R_1R_2=101.
$$
到站静止要求可获得的两段快速度相等：
$$
\frac uc\ln R_1=\frac uc\ln R_2,
$$
所以
$$
R_1=R_2=\sqrt{101}.
$$
巡航快速度
$$
\psi_c=\frac uc\ln\sqrt{101}
$$
给
$$
\beta_c=\tanh\psi_c,\qquad
\gamma_c=\cosh\psi_c.
$$
飞船钟的 $15\,\mathrm{yr}$ 是固有时，恒星系航程为
$$
S=v_c(\gamma_c\tau)
=\beta_c\gamma_c\,c\tau
=\sinh\psi_c\,c\tau.
$$
这里依次使用了“质量比相乘、快速度相加、固有时换到坐标时”三种不同规则，不能把它们都按普通速度或普通质量差处理。""",
    },
    "047": {
        1: r"""二分法的实际迭代可写成可复核的数表。令
$$
g(x)=
\frac1{\sqrt{1+9x^2}}
+\frac1{\sqrt{1+x^2}}-1.6.
$$
先计算
$$
g(0.37)>0,\qquad g(0.38)<0,
$$
所以根在 $[0.37,0.38]$。依次取中点并保留异号半区间：
$$
\begin{array}{c|c}
\text{试值}&g(x)\text{ 的符号}\\ \hline
0.375&+\\
0.3775&-\\
0.37625&-\\
0.375625&-\\
0.3753125&+
\end{array}
$$
继续迭代得到
$$
x=0.375534\ldots.
$$
单调性
$$
g'(x)
=-\frac{9x}{(1+9x^2)^{3/2}}
-\frac{x}{(1+x^2)^{3/2}}<0
\qquad(x>0)
$$
保证每次异号区间中只有一个根。代回两角：
$$
\tan\theta_2=x,\qquad
\tan\theta_1=3x,
$$
再分别计算正弦，而不是用 $\sin\theta\simeq\tan\theta$：
$$
\sin\theta_2=\frac{x}{\sqrt{1+x^2}},
\qquad
\sin\theta_1=\frac{3x}{\sqrt{1+9x^2}}.
$$
这一步若误用小角近似，外侧角 $\theta_1\simeq48.4^\circ$ 已明显不小，会造成不可忽略的高度误差。""",
        4: r"""远场展开的下一阶也可用于判断近似误差。Gilbert 模型对称放置时
$$
B_z=\frac{\mu_0q_m}{4\pi}
\frac{2zd}{(z^2-d^2/4)^2}.
$$
把分母写成
$$
(z^2-d^2/4)^{-2}
=z^{-4}\left(1-\frac{d^2}{4z^2}\right)^{-2}
$$
并用
$$
(1-y)^{-2}=1+2y+3y^2+\cdots,
$$
得到
$$
B_z=
\frac{\mu_0p_m}{2\pi z^3}
\left[
1+\frac{d^2}{2z^2}
+O\!\left(\frac{d^4}{z^4}\right)
\right].
$$
领先修正的相对量级是 $(d/z)^2$。电流环轴线场
$$
B_z=\frac{\mu_0Ir^2}{2z^3}
\left(1+\frac{r^2}{z^2}\right)^{-3/2}
$$
展开为
$$
B_z=
\frac{\mu_0p_m}{2\pi z^3}
\left[
1-\frac32\frac{r^2}{z^2}
+O\!\left(\frac{r^4}{z^4}\right)
\right].
$$
两模型的领先偶极项相同，下一阶却不同，准确体现“远场等效、近场结构不同”。因此不能用 Gilbert 磁荷模型去预言真实小电流环的近场细节。""",
        5: r"""若温度与压强都缓慢变化，状态方程的全微分必须保留两项。固定容器体积时
$$
V\,dp=RT\,dn+nR\,dT,
$$
所以
$$
dn=\frac{V}{RT}\,dp-\frac nT\,dT.
$$
将其代入显热与相变热的总热量
$$
dQ=C_{\rm eff}\,dT+L\,dn
$$
得到
$$
dQ=
\left(C_{\rm eff}-\frac{nL}{T}\right)dT
+\frac{LV}{RT}\,dp.
$$
只有题设小段等温 $dT=0$ 时，才简化为
$$
dQ=\frac{LV}{RT}\,dp.
$$
若改从内能出发，则相变项使用 $L-RT$：
$$
dU=C_{V,\rm eff}\,dT+(L-RT)\,dn.
$$
再加上第一定律中的功项，必须恢复同一个 $dQ$。这两条路线的相等，是检查潜热究竟作为焓差还是内能差使用的最稳妥方法。""",
        7: r"""第（9）问的极值求导不能省略。令
$$
R^2(c)
=\frac{(1-c^2)(3c-2)^2}
{(1-2c+3c^2)^2},
\qquad0\le c\le1.
$$
通分求导并因式分解：
$$
\frac{dR^2}{dc}
=-\frac{
2(3c-2)(15c^2-14c+1)}
{(3c^2-2c+1)^3}.
$$
分母在 $[0,1]$ 内始终为正。驻点来自
$$
3c-2=0
$$
或
$$
15c^2-14c+1=0.
$$
后一个二次方程给
$$
c_\pm=\frac{7\pm\sqrt{34}}{15},
$$
数值为
$$
c_-\simeq0.0779365,\qquad
c_+\simeq0.855397.
$$
连同端点及绝对值分段点比较：
$$
\begin{array}{c|c}
c&R(c)\\ \hline
0&2\\
c_-&2.0419\\
2/3&0\\
c_+&\text{小于 }2.0419\\
1&0
\end{array}
$$
所以全局最大在 $c_-$，并有
$$
\boxed{\mu_2=R(c_-)\simeq2.04}.
$$
这补全了从“最大化摩擦比”到数值答案之间的求导、因式分解、根筛选和端点比较。""",
        8: r"""数值二次方程的系数可以显式化。取
$$
c_1=\cos1\simeq0.540302306,
\qquad
c_1^2\simeq0.291926582.
$$
式（36）为
$$
\left(\frac12-\frac{c_1^2}{6}\right)w^2
+\frac{c_1^2}{6}-10c_1=0.
$$
两个系数分别是
$$
\frac12-\frac{c_1^2}{6}
\simeq0.451345570,
$$
$$
\frac{c_1^2}{6}-10c_1
\simeq-5.354368625.
$$
因此
$$
w^2=
\frac{5.354368625}{0.451345570}
\simeq11.862,
$$
$$
w_\pm=\pm3.44429\,\mathrm{s^{-1}}.
$$
再用同一个分支代入
$$
u=\frac{c_1(w+1)}3:
$$
$$
\begin{aligned}
w=-3.44429
&\Longrightarrow
u=-0.440218\,\mathrm{s^{-1}},\\
w=+3.44429
&\Longrightarrow
u=+0.800420\,\mathrm{s^{-1}}.
\end{aligned}
$$
因 $r=1\,\mathrm m$，圆心线速度数值等于 $u$ 的数值但单位变为 $\mathrm{m/s}$。最后分别代回
$$
3u-c_1w=c_1
$$
和能量式检查，两支均成立。若先把 $w$ 取绝对值，就会丢失 $u$ 的一负一正配对关系。""",
    },
    "048": {
        4: r"""微小循环面积中的符号可以用循环方向逐边核对。取高温等温线 $T+dT$ 上完成正常态到超导态的转变，再沿临界线返回。两态磁矩差
$$
\Delta M=M_n-M_s=\mu_0B_c>0.
$$
升温时临界场降低：
$$
dB_c=\frac{dB_c}{dT}dT<0.
$$
由 $dW=-B\,dM$，窄循环的有向磁功为
$$
dW=-\Delta M\,dB_c
=-\mu_0B_c\,dB_c>0.
$$
卡诺关系
$$
\frac{dW}{T\Delta S_n}=\frac{dT}{T}
$$
给
$$
\Delta S_n
=-\mu_0B_c\frac{dB_c}{dT}.
$$
这里 $dW$ 和 $dT$ 都是一阶小量，$\Delta M$ 是两相之间的有限跳变量，不能误当成另一阶微分。结果的三个特殊温度为
$$
\Delta S_n(0)=0,\qquad
\Delta S_n(T_0)=0,
$$
以及内部极值由对
$$
T\left(1-\frac{T^2}{T_0^2}\right)
$$
求导得到 $T=T_0/\sqrt3$。这为函数形状提供了额外检查。""",
        6: r"""相邻端口的模态分解可以把系数完整算出。按 $(A,C,B,D)$ 排列，
$$
\boldsymbol j_{AC}=I(1,-1,0,0).
$$
写成
$$
\boldsymbol j_{AC}
=\frac I2(1,0,-1,0)
-\frac I2(0,1,0,-1)
+\frac I2(1,-1,1,-1),
$$
或在一组正交归一化基中投影，最终只有 $\lambda=2$、$\lambda=4$ 两类非均匀模态。每类模态的端面电压响应为 $z_\lambda$ 乘相应电流系数。把端点 $A,C$ 的电势差重新合成，两个简并 $\lambda=2$ 分量合计贡献 $z_2I$，交错 $\lambda=4$ 分量贡献 $z_4I$，所以
$$
V_A-V_C=(z_2+z_4)I.
$$
代入
$$
z_2=\frac{\sqrt3-1}{2}r,
\qquad
z_4=\frac{\sqrt2-1}{2}r:
$$
$$
\begin{aligned}
r_{AC}
&=\frac r2
\left[(\sqrt3-1)+(\sqrt2-1)\right]\\
&=\frac{\sqrt3+\sqrt2-2}{2}r.
\end{aligned}
$$
对角端口则是纯 $\lambda=2$ 型，端点电势一正一负：
$$
V_A-V_B=z_2[I-(-I)]=2z_2I,
$$
故
$$
r_{AB}=(\sqrt3-1)r.
$$
两个结果的模态系数由端点电压差而非仅由向量长度决定。""",
    },
    "050": {
        1: r"""球形颗粒的力应在投影圆盘上积分。取竖直来流方向为轴，投影圆盘上距轴为 $s$ 的环带对应球面法线与来流夹角 $\vartheta$，满足
$$
s=r\sin\vartheta,\qquad
\cos\vartheta=\sqrt{1-\frac{s^2}{r^2}}.
$$
环带投影面积
$$
dA_{\rm proj}=2\pi s\,ds.
$$
入射质量通量仍为 $\eta\rho_0U\,dA_{\rm proj}$。镜面反射时法向速度分量反向，单元空气的动量变化矢量沿法线，大小为 $2U\cos\vartheta$；其竖直分量再乘 $\cos\vartheta$。所以球所受竖直力
$$
\begin{aligned}
F_{\rm sph}
&=2\eta\rho_0U^2
\int_{\rm disk}\cos^2\vartheta\,dA_{\rm proj}\\
&=2\eta\rho_0U^2
\int_0^r\left(1-\frac{s^2}{r^2}\right)2\pi s\,ds\\
&=2\eta\rho_0U^2
\left[\pi r^2-\frac{\pi r^2}{2}\right]\\
&=\eta\rho_0\pi r^2U^2.
\end{aligned}
$$
球质量
$$
m_{\rm sph}=\frac43\pi\rho r^3,
$$
故
$$
a_{\rm sph}
=\frac{3\eta\rho_0U^2}{4\rho r}.
$$
再取 $U=2v_0$ 并用停止距离临界条件，便可与圆柱结果比较。积分中的两个 $\cos\vartheta$ 分别来自法向速度和把法向冲量投影回竖直方向；漏掉任一个都会使球形系数错误。""",
        8: r"""加速度变换也可从速度变换逐步推导。地面系中左端速度为 $v$，取瞬时共动系速度同为 $v$。相邻时刻速度增加 $dv=a\,dt$。一维速度变换
$$
v'=\frac{u-v}{1-uv/c^2}
$$
在考察事件 $u=v$ 附近对 $u$ 微分：
$$
dv'=\frac{du}{1-v^2/c^2}
=\gamma^2dv.
$$
同一事件附近的共动系时间微分
$$
dt'=\gamma\left(dt-\frac{v\,dx}{c^2}\right).
$$
沿左端世界线 $dx=v\,dt$，所以
$$
dt'=\gamma dt(1-\beta^2)
=\frac{dt}{\gamma}.
$$
因此
$$
a'=\frac{dv'}{dt'}
=\gamma^3\frac{dv}{dt}
=\gamma^3a.
$$
这说明 $a'$ 是随车加速度计读出的本征加速度。题设保持 $a$ 恒定，所以
$$
a'=\frac{a}{[1-(at/c)^2]^{3/2}}
$$
随时间增长。真正 Born 刚性的列车不能让所有点具有同一 $a'$ 或同一地面坐标加速度；前端必须按位置减小本征加速度，才能使共动长度不变。""",
    },
    "051": {
        3: r"""临界角积分中的半角关系可以逐步展开。临界时取等号并沿右半支令 $\psi$ 随 $\alpha$ 减小：
$$
\frac{d\psi}{d\alpha}=-\mu\sin\psi.
$$
分离变量：
$$
\frac{d\psi}{\sin\psi}=-\mu\,d\alpha.
$$
利用
$$
\int\csc\psi\,d\psi
=\ln\tan\frac\psi2+C,
$$
从中点 $\alpha=0,\psi=\pi/2$ 积分到任意点：
$$
\ln\tan\frac\psi2
-\ln\tan\frac{\pi}{4}
=-\mu\alpha.
$$
因 $\tan(\pi/4)=1$，
$$
\tan\frac\psi2=e^{-\mu\alpha}.
$$
端点 $\alpha=\pi/2$ 处切线与轴线夹角就是 $\theta$，所以
$$
\tan\frac{\theta_c}{2}
=e^{-\mu\pi/2},
$$
$$
\boxed{\theta_c=2\arctan e^{-\mu\pi/2}}.
$$
再求轨迹。由
$$
\frac{dz}{d\alpha}
=\frac{dz/ds}{d\alpha/ds}
=r\cot\psi.
$$
半角式给
$$
\cot\psi
=\frac{1-\tan^2(\psi/2)}
{2\tan(\psi/2)}
=\sinh(\mu\alpha).
$$
故
$$
z(\alpha)
=r\int_0^\alpha\sinh(\mu a)\,da
=\frac r\mu[\cosh(\mu\alpha)-1].
$$
连同柱面条件 $\rho=r$ 和左支 $z\to-z$，才构成完整三维绳线。""",
    },
    "053": {
        5: r"""累积分布函数还能整体核验所有端点条件。对 $0\le v\le1$，
$$
\begin{aligned}
F(v)
&=\int_0^v(-3s^2+2s+1)\,ds\\
&=-v^3+v^2+v.
\end{aligned}
$$
完整定义为
$$
F(v)=
\begin{cases}
0,&v<0,\\
-v^3+v^2+v,&0\le v\le1,\\
1,&v>1.
\end{cases}
$$
逐项检查：
$$
F(0)=0,\qquad F(1)=1,
$$
且
$$
F'(v)=-3v^2+2v+1=f(v)\ge0
\quad(0\le v\le1).
$$
所以 $F$ 单调不减并正确归一化。若希望核对平均值，还可用非负随机变量的尾积分公式
$$
\bar v=\int_0^\infty[1-F(v)]\,dv.
$$
本题化为
$$
\begin{aligned}
\bar v
&=\int_0^1(1+v^3-v^2-v)\,dv\\
&=\left[v+\frac14v^4-\frac13v^3-\frac12v^2\right]_0^1\\
&=1+\frac14-\frac13-\frac12
=\frac5{12}.
\end{aligned}
$$
这与直接计算 $\int vf(v)\,dv$ 相互独立，能发现平均值积分中漏乘 $v$ 的错误。""",
    },
}


FINAL_STUDENT_ADDITIONS_2: dict[str, dict[int, str]] = {
    "046": {
        8: r"""推力还可从氦核质量流率独立复算。每四个质子产生一个氦核，因此
$$
\dot m_{\rm He}
=\dot m_{\rm H}\frac{m_{\rm He}}{4m_{\rm H}}.
$$
喷流的相对论动量流率为
$$
F=\gamma_u\dot m_{\rm He}u.
$$
代入 $\dot m_{\rm H}=10^{-3}\,\mathrm{kg/s}$、$\gamma_u=1.00662323$ 和
$$
u=3.43338\times10^7\,\mathrm{m/s},
$$
得到
$$
\begin{aligned}
F
&=\gamma_u
\left(\dot m_{\rm H}\frac{m_{\rm He}}{4m_{\rm H}}\right)u\\
&=3.43244\times10^4\,\mathrm N.
\end{aligned}
$$
这与“反应数率乘单核动量”
$$
F=
\left(\frac{\dot m_{\rm H}}{4m_{\rm H}}\right)
(\gamma_um_{\rm He}u)
$$
逐项相同。前者按连续质量流理解，后者按离散反应计数；两式一致可检查是否漏掉每次反应消耗四个质子的因子。若错误使用非相对论动量 $\dot m_{\rm He}u$，会少乘 $\gamma_u$；虽然本题 $\gamma_u-1$ 较小，原则上仍必须保留。""",
    },
    "047": {
        2: r"""最短时间还可直接对较小根求单调性。设
$$
t_-(A)=\frac{A-\sqrt{A^2-2gh}}g,
\qquad A>\sqrt{2gh}.
$$
求导：
$$
\frac{dt_-}{dA}
=\frac1g\left(
1-\frac{A}{\sqrt{A^2-2gh}}
\right)<0,
$$
因为 $\sqrt{A^2-2gh}<A$。所以较小根确实随 $A$ 增大而减小。角度只通过
$$
A(\theta)
=v_0[\sin\theta+\tan\alpha\cos\theta]
=\frac{v_0}{\cos\alpha}\sin(\theta+\alpha)
$$
进入。允许角度内最大值为
$$
A_{\max}=\frac{v_0}{\cos\alpha},
\qquad
\theta=\frac\pi2-\alpha.
$$
相应的最短时间若需要写出，可代回得到
$$
t_{\min}
=\frac{
\frac{v_0}{\cos\alpha}
-\sqrt{\frac{v_0^2}{\cos^2\alpha}-2gh}}
g.
$$
判别式非负还要求
$$
v_0^2\ge2gh\cos^2\alpha.
$$
因此最优角结论之外，还存在“以给定速度是否能碰到顶棚”的可达性条件。""",
        6: r"""三阶展开可以给出临界点下方磁化强度的来路。自洽式为
$$
m=\frac23y-\frac19y^3+O(y^5),
\qquad
y=\frac{qJm}{kT}.
$$
移到同一侧：
$$
m\left[
1-\frac{2qJ}{3kT}
\right]
+\frac19\left(\frac{qJ}{kT}\right)^3m^3
=0.
$$
除零解外，
$$
m^2
=9\left(\frac{kT}{qJ}\right)^3
\left[
\frac{2qJ}{3kT}-1
\right].
$$
利用
$$
kT_c=\frac{2qJ}{3},
$$
并令 $T=T_c-\Delta T$、$\Delta T\ll T_c$，括号的一阶近似为
$$
\frac{T_c}{T}-1
\simeq\frac{\Delta T}{T_c}.
$$
前因子在领先阶可取 $T=T_c$，所以
$$
m^2\propto T_c-T,
\qquad
|m|\propto(T_c-T)^{1/2}.
$$
正负两支对应零外场下的自发对称破缺。这个展开同时证明：在 $T>T_c$ 时右侧不给实的非零小解，只有 $m=0$；在 $T<T_c$ 时成对出现 $\pm m$。""",
        8: r"""能量二次型本身应保持正定。以
$$
u=\frac{\dot x}{r},\qquad w=\dot\beta
$$
表示，动能除以 $mr^2$ 后为
$$
\frac32u^2-uw\cos\beta+\frac12w^2.
$$
对应矩阵
$$
\frac12
\begin{pmatrix}u&w\end{pmatrix}
\begin{pmatrix}
3&-\cos\beta\\
-\cos\beta&1
\end{pmatrix}
\begin{pmatrix}u\\w\end{pmatrix}.
$$
第一顺序主子式为 $3>0$，行列式为
$$
3-\cos^2\beta\ge2>0,
$$
所以除两速度都为零外，动能恒正。这一检查能发现交叉项系数若被误写成 $-2mr\dot x\dot\beta\cos\beta$，矩阵和后续根都会改变。消去 $u$ 后得到的 $w^2>0$ 也必须与正定性和右侧势能降低量 $gr\cos\beta>0$ 同时相容。""",
    },
    "048": {
        3: r"""剪切模态还可用能量守恒检查边界与频率。对任一位移场 $u(x,t)$，
$$
E=\frac12\int_0^L
\left[
\rho A\left(\frac{\partial u}{\partial t}\right)^2
+SA\left(\frac{\partial u}{\partial x}\right)^2
\right]dx.
$$
对时间求导并对第二项分部积分：
$$
\begin{aligned}
\frac{dE}{dt}
&=\int_0^L
\left[
\rho Au_tu_{tt}+SAu_xu_{xt}
\right]dx\\
&=\int_0^L
Au_t(\rho u_{tt}-Su_{xx})\,dx
+SAu_xu_t\Big|_0^L.
\end{aligned}
$$
波动方程使体积分为零。底端固定给 $u_t(0,t)=0$，顶端自由给 $u_x(L,t)=0$，所以边界功率也为零，$dE/dt=0$。这说明“固定端位移为零、自由端应力为零”不仅来自几何名称，还正好保证没有能量穿过边界。若误把自由端写成 $u(L,t)=0$，允许波数会由半整数变成整数，且物理上等于把顶端也固定。""",
    },
    "051": {
        3: r"""临界曲线在中点附近满足
$$
z=\frac r\mu[\cosh(\mu\alpha)-1]
\simeq\frac12r\mu\alpha^2.
$$
因此
$$
\left.\frac{dz}{d\alpha}\right|_{\alpha=0}=0,
\qquad
\left.\frac{d^2z}{d\alpha^2}\right|_{\alpha=0}=r\mu>0.
$$
左右两支用 $z\to-z$ 对称连接时，绳线切向连续，没有尖点；这一局部展开同时检查了积分常数和对称边界。""",
    },
}


FINAL_STUDENT_ADDITIONS_3: dict[str, dict[int, str]] = {
    "047": {
        2: r"""撞击速度还可分解到屋面的切向和法向，这能同时检查屋面几何与速度答案。屋面方程写成
$$
x\sin\alpha+y\cos\alpha=h\cos\alpha,
$$
故从发射点指向屋面的单位法向量与沿屋面向右的单位切向量可取为
$$
\boldsymbol e_n=(\sin\alpha,\cos\alpha),
\qquad
\boldsymbol e_s=(\cos\alpha,-\sin\alpha).
$$
两者满足 $\boldsymbol e_n\cdot\boldsymbol e_s=0$，所以碰撞速度的分量为
$$
\begin{aligned}
v_n&=\boldsymbol v_1\cdot\boldsymbol e_n
=v_x\sin\alpha+v_y\cos\alpha,\\
v_s&=\boldsymbol v_1\cdot\boldsymbol e_s
=v_x\cos\alpha-v_y\sin\alpha.
\end{aligned}
$$
代入 $\alpha=30^\circ$、$v_x\simeq32.77\,\mathrm{m/s}$、$v_y\simeq19.19\,\mathrm{m/s}$：
$$
\begin{aligned}
v_n&\simeq32.77\times0.5+19.19\times0.8660
\simeq33.0\,\mathrm{m/s},\\
v_s&\simeq32.77\times0.8660-19.19\times0.5
\simeq18.8\,\mathrm{m/s}.
\end{aligned}
$$
再做勾股校验：
$$
v_n^2+v_s^2
\simeq(33.0)^2+(18.8)^2
\simeq v_x^2+v_y^2.
$$
碰撞条件也可直接在法向上写成
$$
h\cos\alpha
=v_0\sin(\theta+\alpha)t
-\frac12g\cos\alpha\,t^2.
$$
将式子除以 $\cos\alpha$ 就回到原来的二次方程。这种写法明确显示：常数项 $h$ 来自屋面的法向距离，角度组合 $\sin(\theta+\alpha)$ 则来自初速度的法向投影。""",
    },
    "048": {
        1: r"""第一问的两次正弦投影可用向量力矩逐行算出。取竖直向上为 $z$ 轴，使主销轴位于 $xOz$ 平面，则其单位向量为
$$
\hat{\boldsymbol n}
=(\sin\beta,0,\cos\beta).
$$
正中位置时，$OA$ 既垂直于主销轴，又位于主销轴和竖直方向决定的平面内，故可取
$$
\boldsymbol e_0=(\cos\beta,0,-\sin\beta),
\qquad
\hat{\boldsymbol n}\cdot\boldsymbol e_0=0.
$$
将 $\boldsymbol e_0$ 绕 $\hat{\boldsymbol n}$ 转过 $\theta$，因为两者垂直，Rodrigues 公式简化为
$$
\begin{aligned}
\boldsymbol r_{OA}
&=l\left[
\boldsymbol e_0\cos\theta
+(\hat{\boldsymbol n}\times\boldsymbol e_0)\sin\theta
\right]\\
&=l(\cos\beta\cos\theta,\ \sin\theta,\ -\sin\beta\cos\theta).
\end{aligned}
$$
支持力为 $\boldsymbol N=(0,0,N)$，所以它对主销轴的力矩分量为
$$
\begin{aligned}
M_{OB}
&=(\boldsymbol r_{OA}\times\boldsymbol N)
\cdot\hat{\boldsymbol n}\\
&=Nl\sin\beta\sin\theta.
\end{aligned}
$$
上式是按所选轴向得到的代数分量；若把使车轮偏转增大的方向定为正，重力机构的广义力矩应与偏转相反，因而写为
$$
M_1=-Nl\sin\beta\sin\theta
=-\frac{Gl}{4}\sin\beta\sin\theta.
$$
这一推导同时验证了三个极限：$\beta=0$ 时主销竖直、无回正力矩；$\theta=0$ 时系统处在对称位置、力矩为零；小角度时 $M_1\simeq-(Gl\sin\beta/4)\theta$，为线性恢复力矩。

第二问中前轮侧向力的 $1/2$ 也可从整车的平动与转动平衡推出，不必把它当作无来由的分配。设前、后轮的侧向力分别为 $F_f,F_r$，质心到两轮的水平距离都为 $d/2$。稳定转弯时车身没有绕质心的额外角加速度，故
$$
F_f\frac d2-F_r\frac d2=0
\quad\Longrightarrow\quad
F_f=F_r.
$$
两力合力提供向心力：
$$
F_f+F_r=\frac{mv^2}{R}.
$$
因此
$$
F_f=\frac{mv^2}{2R}.
$$
前轮偏转的几何关系为
$$
\tan\theta=\frac dR
\quad\Longrightarrow\quad
F_f=\frac{mv^2}{2d}\tan\theta.
$$
到这一步还没有对 $\theta$ 作小角近似。

再用向量力矩推出后倾角对应的有效力臂。取 $x$ 轴向前、$y$ 轴沿侧向力、$z$ 轴向上，主销轴单位向量可写成
$$
\hat{\boldsymbol n}=(-\sin\alpha,0,\cos\alpha).
$$
轮胎接地点相对轮心的位置矢量和侧向力分别为
$$
\boldsymbol r_P=(0,0,-r),
\qquad
\boldsymbol F_f=(0,F_f,0).
$$
于是
$$
\begin{aligned}
M_{OB}
&=(\boldsymbol r_P\times\boldsymbol F_f)
\cdot\hat{\boldsymbol n}\\
&=(rF_f,0,0)\cdot(-\sin\alpha,0,\cos\alpha)\\
&=-rF_f\sin\alpha.
\end{aligned}
$$
故在只假设稳定转弯而尚未使用 $\theta\ll1$ 时，结果为
$$
M_2=-\frac{mv^2r}{2d}\sin\alpha\tan\theta.
$$
最后使用 $\tan\theta\simeq\theta$ 才得到题目要求的小角结果。因此 $1/2$、$\sin\alpha$ 和 $\theta$ 分别来自载荷分配、轴向力矩投影和转弯几何，三者不能互相替代。""",
        5: r"""为了检查“线性化时为什么可以用 $I_0$”，可把力完整展开到三阶。沿 $y=0$ 记
$$
a=\frac{B_0S}{L},
\qquad
I(x)=I_0+a(1-\cos kx).
$$
使用
$$
\begin{aligned}
\sin kx&=kx-\frac{k^3x^3}{6}+O(x^5),\\
1-\cos kx&=\frac{k^2x^2}{2}-\frac{k^4x^4}{24}+O(x^6),
\end{aligned}
$$
代入精确力
$$
F_x=-I(x)B_0Sk\sin kx.
$$
先展开括号再按位移次数收集：
$$
\begin{aligned}
F_x
={}&-B_0Sk
\left[I_0+\frac{ak^2x^2}{2}+O(x^4)\right]
\left[kx-\frac{k^3x^3}{6}+O(x^5)\right]\\
={}&-I_0B_0Sk^2x
+B_0Sk^4
\left(\frac{I_0}{6}-\frac{B_0S}{2L}\right)x^3
+O(x^5).
\end{aligned}
$$
可见电流的位移修正确实首次出现在三次力中，不会改变线性角频率。只保留一阶力，才有
$$
m\ddot x+I_0B_0Sk^2x=0.
$$
若要研究较大振幅，则不能丢掉上述 $x^3$ 项；它会导致周期随振幅改变。当 $I_0=0$ 时线性项完全消失，最低阶恢复力为
$$
F_x=-\frac{B_0^2S^2k^4}{2L}x^3+O(x^5),
$$
此时不存在与振幅无关的普通简谐振动频率。""",
    },
}


FINAL_STUDENT_ADDITIONS_4: dict[str, dict[int, str]] = {
    "045": {
        3: r"""竖直小振动还可从总势能的展开中完整复核。令上方磁铁的高度为 $z$，并记
$$
A=\frac{\mu_0m_0m}{2\pi}.
$$
重力势能与反平行磁矩势能之和为
$$
U(z)=Mgz+\frac{A}{z^3}.
$$
平衡条件
$$
U'(h)=Mg-\frac{3A}{h^4}=0
$$
给出
$$
A=\frac13Mgh^4.
$$
令 $z=h+x$、$u=x/h$，并使用二项式展开
$$
(1+u)^{-3}
=1-3u+6u^2-10u^3+15u^4+O(u^5).
$$
则
$$
\begin{aligned}
U(h+x)
={}&Mg(h+x)+\frac{A}{h^3}(1+u)^{-3}\\
={}&U(h)
+\left(Mgx-\frac{3A}{h^4}x\right)
+\frac{6A}{h^5}x^2
-\frac{10A}{h^6}x^3
+\frac{15A}{h^7}x^4+O(x^5).
\end{aligned}
$$
利用 $3A/h^4=Mg$，一阶项严格相消，得
$$
U(h+x)
=U(h)
+\frac{2Mg}{h}x^2
-\frac{10Mg}{3h^2}x^3
+\frac{5Mg}{h^3}x^4+O(x^5).
$$
只保留二次项，与标准简谐振子势能
$$
\frac12M\omega_z^2x^2
$$
比较，立即得到
$$
\frac12M\omega_z^2=\frac{2Mg}{h}
\quad\Longrightarrow\quad
\boxed{\omega_z=2\sqrt{\frac gh}}.
$$
再对势能求导，可得更高阶的合力
$$
F_x
=-\frac{4Mg}{h}x
+\frac{10Mg}{h^2}x^2
-\frac{20Mg}{h^3}x^3+O(x^4).
$$
二次力项表明上、下两侧的回复力并不完全对称；因而振幅不再充分小时，平均位置与周期都会产生修正。题目所求频率只对应二次势能主导的极限。""",
    },
}


def enrich_set(
    set_number: str,
    additions: dict[int, str],
    marker_namespace: str = "CORE_ENRICHMENT",
) -> None:
    path = ROOT / f"蔡题{set_number}" / "整理版" / "markdown" / f"蔡题{set_number}_教师备课.md"
    text = path.read_text(encoding="utf-8")
    matches = list(re.finditer(r"(?m)^# 第 (\d+) 题$", text))
    if [int(match.group(1)) for match in matches] != list(range(1, 9)):
        raise RuntimeError(f"蔡题{set_number} 题号异常")
    blocks: list[str] = []
    front = text[: matches[0].start()]
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start() : end].rstrip()
        number = int(match.group(1))
        marker = f"<!-- {marker_namespace}_{set_number}_{number} -->"
        if number in additions and marker not in block:
            location = block.find("\n## 六、关键洞察")
            if location < 0:
                raise RuntimeError(f"蔡题{set_number}第 {number} 题缺少第六模块")
            addition = additions[number].strip()
            block = block[:location].rstrip() + f"\n\n{marker}\n\n{addition}\n" + block[location:]
        blocks.append(block)
    path.write_text(front + "\n\n".join(blocks) + "\n", encoding="utf-8")


def main() -> None:
    for set_number, additions in ADDITIONS.items():
        if set(additions) != set(range(1, 9)):
            raise RuntimeError(f"蔡题{set_number}补充内容不是 8 题")
        enrich_set(set_number, additions)
    for set_number, additions in ADDITIONS_LATE.items():
        if set(additions) != set(range(1, 9)):
            raise RuntimeError(f"蔡题{set_number}补充内容不是 8 题")
        enrich_set(set_number, additions)
    for set_number, additions in EXTRA_ADDITIONS.items():
        enrich_set(set_number, additions, marker_namespace="CORE_ENRICHMENT_EXTRA")
    for set_number, additions in DEEPENING_ADDITIONS.items():
        enrich_set(set_number, additions, marker_namespace="CORE_DEEPENING")
    for set_number, additions in DEEPENING_ADDITIONS_LATE.items():
        enrich_set(set_number, additions, marker_namespace="CORE_DEEPENING")
    for set_number, additions in FINAL_STUDENT_ADDITIONS.items():
        enrich_set(set_number, additions, marker_namespace="CORE_FINAL_DETAIL")
    for set_number, additions in FINAL_STUDENT_ADDITIONS_2.items():
        enrich_set(set_number, additions, marker_namespace="CORE_FINAL_DETAIL_2")
    for set_number, additions in FINAL_STUDENT_ADDITIONS_3.items():
        enrich_set(set_number, additions, marker_namespace="CORE_FINAL_DETAIL_3")
    for set_number, additions in FINAL_STUDENT_ADDITIONS_4.items():
        enrich_set(set_number, additions, marker_namespace="CORE_FINAL_DETAIL_4")


if __name__ == "__main__":
    main()
