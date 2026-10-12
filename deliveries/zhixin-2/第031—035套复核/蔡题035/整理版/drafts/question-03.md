# 第 3 题

<!-- question-start -->
在竖直平面内取 $x$ 轴水平向右、$y$ 轴竖直向上。一个质量为 $m$、电荷量为 $q$ 的小球从原点以初速度 $\boldsymbol v_i$ 抛出。匀强磁场大小为 $B$，方向垂直平面向里，重力加速度为 $\boldsymbol g=-g\boldsymbol e_y$。小球受到与其相对静止介质速度成正比的阻力 $\boldsymbol f=-k\boldsymbol v$，其中 $k>0$。

1. 求足够长时间后小球的速度 $\boldsymbol v_0$。
2. 若初速度 $\boldsymbol v_i=0$，在以恒定速度 $\boldsymbol v_0$ 相对地面运动、且初始时与地面坐标系原点重合的参考系中，求小球的最终位移。

![图 3-1　带电小球的坐标、磁场与重力方向。](../figures/question-03.png)

<!-- question-end -->

## 一、题型定位

恒力、线性阻力与洛伦兹力共同作用下的二维趋稳运动。先找速度空间的平衡点，再研究相对该速度平衡点的衰减运动。终端速度在地面系中不为零，但减去匀速漂移后，相对速度趋于零，相对位置趋于有限值。

## 二、知识点

- 洛伦兹力 $\boldsymbol F_B=q\boldsymbol v\times\boldsymbol B$ 的分量和方向。
- 终端速度满足合力为零，但不表示小球位置不再改变。
- 平移惯性系中位置与速度的关系，以及阻力所参照介质不能随意更换。
- 矢量微分方程沿时间积分，把速度变化与总位移联系起来。
- 指数衰减与旋转叠加；相对运动能量单调衰减。

## 三、物理图像

对正电荷，若球开始向下运动，磁力向右，因此最后的漂移速度斜向右下。负电荷的横向漂移反向，竖直下落分量仍向下。

终端状态中，阻力与速度反向，磁力与速度垂直，两者的矢量和向上，平衡重力。图 3-2 以 $qB=k>0$ 为示例：左侧给出三力的作用方向，虚线辅助显示两向上分力的合成；右侧给出同一参数条件下相对速度的衰减旋转。一般参数下各力的夹角与相对大小会改变，受力方程和衰减机制不变。

## 四、解题入口

令 $b=qB$ 保留电荷的符号，避免在一开始就把磁力写成无符号大小。先联立两个终态分量方程，再令 $\boldsymbol w=\boldsymbol v-\boldsymbol v_0$，利用终态平衡消去重力等常量项。求最终位移时可以直接对 $\boldsymbol w$ 的方程积分，不必先求完整轨迹。

## 五、解析

（1）逐项写出力的分量。

磁场为

$$
\boldsymbol B=-B\boldsymbol e_z,
$$

速度为 $\boldsymbol v=v_x\boldsymbol e_x+v_y\boldsymbol e_y$。利用右手坐标系的叉积规则，

$$
\begin{aligned}
\boldsymbol v\times\boldsymbol B
&=-Bv_x(\boldsymbol e_x\times\boldsymbol e_z)
-Bv_y(\boldsymbol e_y\times\boldsymbol e_z)\\
&=Bv_x\boldsymbol e_y-Bv_y\boldsymbol e_x.
\end{aligned}
$$

因此运动方程为

$$
\begin{aligned}
m\dot v_x&=-kv_x-bv_y,\\
m\dot v_y&=bv_x-kv_y-mg,
\qquad b=qB.
\end{aligned}
$$

其中 $\dot v_x$ 是 $\mathrm dv_x/\mathrm dt$，不是位置 $x$ 的一阶导数。阻力的两个分量都是负的“相应速度分量乘以 $k$”；如果某分量速度为负，相应阻力分量自然为正。

（2）终端速度。

足够长时间后，速度若收敛为常矢量，则两分量导数都为零：

$$
kv_{0x}+bv_{0y}=0,\qquad
bv_{0x}-kv_{0y}=mg.
$$

用第一式乘以 $b$、第二式乘以 $k$，相减或相加以消元：

$$
\begin{aligned}
kbv_{0x}+b^2v_{0y}&=0,\\
kbv_{0x}-k^2v_{0y}&=kmg.
\end{aligned}
$$

第二式减第一式得

$$
-(k^2+b^2)v_{0y}=kmg,
$$

所以

$$
v_{0y}=-\frac{mkg}{k^2+b^2}.
$$

将其代回第一式，因 $k>0$，

$$
\begin{aligned}
kv_{0x}
&=-bv_{0y}
=\frac{mbkg}{k^2+b^2},\\
v_{0x}&=\frac{mbg}{k^2+b^2}.
\end{aligned}
$$

最终矢量答案为

$$
\boxed{
\boldsymbol v_0
=\frac{mg}{k^2+q^2B^2}
\left(qB\,\boldsymbol e_x-k\,\boldsymbol e_y\right).
}
$$

其大小为

$$
\begin{aligned}
v_0
&=\sqrt{v_{0x}^2+v_{0y}^2}\\
&=\frac{mg\sqrt{b^2+k^2}}{k^2+b^2}\\
&=\boxed{\frac{mg}{\sqrt{k^2+q^2B^2}}}.
\end{aligned}
$$

若 $q>0$，相对竖直向下方向的偏转角 $\theta$ 满足

$$
\tan\theta=\frac{v_{0x}}{-v_{0y}}=\frac{qB}{k}.
$$

不能只给这个速率而不交代方向，因为第二问所用参考系需要一个完整的速度矢量。

![图 3-2　终端受力、矢量合成与相对速度的衰减旋转。](../figures/solution-03.png)

图中阻力大小为 $kv_0$，磁力大小为 $|q|Bv_0$，二者互相垂直。将两个力矢量平移至首尾相接，它们的合力与重力反向等大，因此力三角形给出

$$
(kv_0)^2+(qBv_0)^2=(mg)^2,
$$

同样得到上面的速率。这是分量结果的几何核对，而不是额外假设磁力与重力垂直。

（3）建立平移系中的相对运动方程。

设新参考系原点位置为 $\boldsymbol r_O(t)=\boldsymbol v_0t$，小球的新坐标与相对速度为

$$
\boldsymbol r'=\boldsymbol r-\boldsymbol v_0t,
\qquad
\boldsymbol w=\dot{\boldsymbol r}'=\boldsymbol v-\boldsymbol v_0.
$$

因 $\boldsymbol v_0$ 是常量，两系加速度相同。把 $\boldsymbol v=\boldsymbol v_0+\boldsymbol w$ 代入地面系运动方程：

$$
\begin{aligned}
m\dot{\boldsymbol w}
&=q(\boldsymbol v_0+\boldsymbol w)\times\boldsymbol B
-k(\boldsymbol v_0+\boldsymbol w)+m\boldsymbol g\\
&=q\boldsymbol w\times\boldsymbol B-k\boldsymbol w\\
&\quad+\left(q\boldsymbol v_0\times\boldsymbol B
-k\boldsymbol v_0+m\boldsymbol g\right).
\end{aligned}
$$

括号内就是终端状态合力，等于零，因此

$$
m\dot{\boldsymbol w}
=q\boldsymbol w\times\boldsymbol B-k\boldsymbol w.
$$

特别要注意：这里没有把真实阻力改成 $-k\boldsymbol w$。实际阻力仍为 $-k(\boldsymbol v_0+\boldsymbol w)$；只是常量部分与重力及磁力的常量部分相消以后，剩余方程才有上述形式。

因为小球初始在地面系静止，所以

$$
\boldsymbol w(0)=-\boldsymbol v_0.
$$

（4）证明相对速度确实趋于零。

将相对运动方程点乘 $\boldsymbol w$。磁力与 $\boldsymbol w$ 垂直，点积为零：

$$
\begin{aligned}
m\boldsymbol w\cdot\dot{\boldsymbol w}
&=q\boldsymbol w\cdot(\boldsymbol w\times\boldsymbol B)-kw^2\\
&=-kw^2.
\end{aligned}
$$

利用 $\mathrm d(w^2)/\mathrm dt=2\boldsymbol w\cdot\dot{\boldsymbol w}$，

$$
\frac{\mathrm d(w^2)}{\mathrm dt}
=-\frac{2k}{m}w^2.
$$

分离变量并从 $0$ 积分到 $t$：

$$
\begin{aligned}
\int_{w(0)^2}^{w(t)^2}\frac{\mathrm d\zeta}{\zeta}
&=-\frac{2k}{m}\int_0^t\mathrm dt,\\
\ln\frac{w(t)^2}{w(0)^2}&=-\frac{2kt}{m}.
\end{aligned}
$$

因此

$$
w(t)=w(0)e^{-kt/m}.
$$

只要 $k>0$，相对速度就指数趋于零。相对路程也有界：

$$
\int_0^\infty w(t)\,\mathrm dt=\frac{m}{k}w(0)<\infty.
$$

于是相对位移积分收敛，可以合法地把积分上限取为无穷大。这一证明补足了“足够长时间后达到终态”的数学依据。

（5）积分方程求最终相对位移。

令

$$
\boldsymbol S=\boldsymbol r'(\infty)-\boldsymbol r'(0)
=\int_0^\infty\boldsymbol w(t)\,\mathrm dt.
$$

对相对运动方程积分：

$$
m[\boldsymbol w(\infty)-\boldsymbol w(0)]
=q\boldsymbol S\times\boldsymbol B-k\boldsymbol S.
$$

代入末态 $\boldsymbol w(\infty)=0$ 及初态 $\boldsymbol w(0)=-\boldsymbol v_0$，

$$
m\boldsymbol v_0=q\boldsymbol S\times\boldsymbol B-k\boldsymbol S.
$$

令 $\boldsymbol S=S_x\boldsymbol e_x+S_y\boldsymbol e_y$，得到两个线性方程：

$$
\begin{aligned}
-kS_x-bS_y&=mv_{0x},\\
bS_x-kS_y&=mv_{0y}.
\end{aligned}
$$

第一式乘以 $-k$、第二式乘以 $b$ 后相加，交叉项消去：

$$
(k^2+b^2)S_x
=m(-kv_{0x}+bv_{0y}).
$$

第一式乘以 $-b$、第二式乘以 $-k$ 后相加，得到

$$
(k^2+b^2)S_y
=m(-bv_{0x}-kv_{0y}).
$$

分别代入已经求得的终端速度：

$$
\begin{aligned}
S_x
&=\frac{m}{k^2+b^2}
\left(-k\frac{mbg}{k^2+b^2}
+b\frac{-mkg}{k^2+b^2}\right)\\
&=-\frac{2m^2gkb}{(k^2+b^2)^2},\\
S_y
&=\frac{m}{k^2+b^2}
\left(-b\frac{mbg}{k^2+b^2}
-k\frac{-mkg}{k^2+b^2}\right)\\
&=\frac{m^2g(k^2-b^2)}{(k^2+b^2)^2}.
\end{aligned}
$$

所以完整的最终位移为

$$
\boxed{
\boldsymbol S
=\frac{m^2g}{(k^2+q^2B^2)^2}
\left[-2kqB\,\boldsymbol e_x+(k^2-q^2B^2)\boldsymbol e_y\right].
}
$$

（6）计算位移大小并区别于总路程。

先平方相加：

$$
\begin{aligned}
S^2
&=\frac{m^4g^2}{(k^2+b^2)^4}
\left[4k^2b^2+(k^2-b^2)^2\right]\\
&=\frac{m^4g^2}{(k^2+b^2)^4}
\left[k^4+2k^2b^2+b^4\right]\\
&=\frac{m^4g^2}{(k^2+b^2)^2}.
\end{aligned}
$$

取非负平方根：

$$
\boxed{S=\frac{m^2g}{k^2+q^2B^2}
=\frac{mv_0}{\sqrt{k^2+q^2B^2}}.}
$$

相对总路程则为

$$
\ell'=\frac{mv_0}{k}.
$$

若磁场非零，$\sqrt{k^2+q^2B^2}>k$，因此 $S<\ell'$：相对速度方向不断转动，沿途各段位移部分抵消。不能把衰减速率的积分直接当作最终位移大小。

（7）求出完整衰减运动以复核方向。

设

$$
\kappa=\frac{k}{m},\qquad \Omega=\frac{qB}{m}.
$$

相对速度分量满足

$$
\dot w_x=-\kappa w_x-\Omega w_y,\qquad
\dot w_y=\Omega w_x-\kappa w_y.
$$

解可写成衰减因子乘以转动矩阵：

$$
\begin{aligned}
w_x(t)
&=e^{-\kappa t}\left[-v_{0x}\cos\Omega t+v_{0y}\sin\Omega t\right],\\
w_y(t)
&=e^{-\kappa t}\left[-v_{0x}\sin\Omega t-v_{0y}\cos\Omega t\right].
\end{aligned}
$$

在 $t=0$ 两式给出 $-\boldsymbol v_0$；直接求导也恢复相对运动方程，所以初值和动力学同时满足。

对指数与三角函数的乘积积分，可由两次分部积分消去重复积分，得到

$$
\begin{aligned}
I_c&=\int_0^\infty e^{-\kappa t}\cos\Omega t\,\mathrm dt
=\frac{\kappa}{\kappa^2+\Omega^2},\\
I_s&=\int_0^\infty e^{-\kappa t}\sin\Omega t\,\mathrm dt
=\frac{\Omega}{\kappa^2+\Omega^2}.
\end{aligned}
$$

具体地，分部积分给出 $I_c=1/\kappa-(\Omega/\kappa)I_s$、$I_s=(\Omega/\kappa)I_c$。代回第一式便有
$(\kappa^2+\Omega^2)I_c=\kappa$，然后得到 $I_s$。因此

$$
S_x=-v_{0x}I_c+v_{0y}I_s,\qquad
S_y=-v_{0x}I_s-v_{0y}I_c,
$$

与直接积分矢量方程完全相同。

（8）特殊情况与量纲检查。

当 $B=0$ 或 $q=0$，

$$
\boldsymbol v_0=-\frac{mg}{k}\boldsymbol e_y,
\qquad
\boldsymbol S=\frac{m^2g}{k^2}\boldsymbol e_y.
$$

这表示新参考系从一开始就以终端速度向下运动，而真实小球开始时速度为零，所以球相对新系先向上，最终留在原点上方；符号符合物理直觉。

当 $|q|B=k$，最终相对竖直位移为零，水平位移却不为零。$q$ 变号时 $v_{0x},S_x$ 变号，$v_{0y},S_y$ 不变，整幅运动图关于竖直轴镜像。

$k$ 与 $qB$ 的单位都是 $\mathrm{kg/s}$，因此终端速度与相对位移的量纲分别为 $\mathrm{m/s}$ 和 $\mathrm m$。若令 $k=0$，衰减证明失效；不能把含阻尼终态结果直接解释为无阻尼系统一定会达到的终态。

## 六、关键洞察

减去终端速度后，原非齐次线性方程化为齐次方程，便于积分。重力并未在物理上消失，而是和匀速平移对应的阻力、磁力常量部分共同满足平衡。

更一般地，若初速度为任意 $\boldsymbol v_i$，则相对初速度为 $\boldsymbol w_i=\boldsymbol v_i-\boldsymbol v_0$。积分同样给出

$$
-m\boldsymbol w_i=q\boldsymbol S\times\boldsymbol B-k\boldsymbol S,
$$

所以

$$
\begin{aligned}
S_x&=\frac{m(kw_{ix}-bw_{iy})}{k^2+b^2},\\
S_y&=\frac{m(bw_{ix}+kw_{iy})}{k^2+b^2}.
\end{aligned}
$$

相对位移的大小为

$$
S=\frac{m|\boldsymbol v_i-\boldsymbol v_0|}{\sqrt{k^2+b^2}}.
$$

它不是只由重力决定，而是由初速度偏离终端速度的程度决定；若一开始便以 $\boldsymbol v_0$ 运动，新系中的相对位移始终为零。

在相对变量中，旋转频率为 $|\Omega|$，衰减时间为 $1/\kappa=m/k$。无量纲比值 $|q|B/k$ 衡量“在明显衰减前能转过多少角度”，同时也决定终端速度偏离竖直方向的角度。

## 七、易错点

- 叉积顺序颠倒，导致横向终端漂移方向错误。
- 把“终端速度”写成零，混淆加速度为零与速度为零。
- 更换参考系后直接把介质阻力当作相对新系的速度函数。
- 求位移只积分速率，漏掉速度方向的转动。
- 第二问只给位移大小，不给矢量或方向。
- 未证明积分收敛，就把末态速度为零用于无阻尼极限。

## 八、课堂讲解建议

先让学生用右手规则判断下落正电荷的磁力方向，再列分量式。得到终端速度后，课堂中用两个匀速参考系小图展示“真实球仍下落”和“相对球逐渐停下”的区别。

第二问先给直接积分法，再给衰减旋转法作为交叉验证。板书保留 $\boldsymbol v$、$\boldsymbol v_0$、$\boldsymbol w$ 三种速度的定义，避免用一个字母兼任三种含义。

## 九、变式训练

变式一：令 $qB=k>0$，初速度仍为零，求终端速度、相对最终位移及相对总路程。

代入主结果：

$$
\boldsymbol v_0=\frac{mg}{2k}(\boldsymbol e_x-\boldsymbol e_y),
\qquad v_0=\frac{mg}{\sqrt2k}.
$$

相对位移为

$$
\begin{aligned}
S_x&=-\frac{2m^2gk^2}{(2k^2)^2}
=-\frac{m^2g}{2k^2},\\
S_y&=\frac{m^2g(k^2-k^2)}{(2k^2)^2}=0.
\end{aligned}
$$

所以

$$
\boxed{\boldsymbol S=-\frac{m^2g}{2k^2}\boldsymbol e_x.}
$$

相对总路程为

$$
\boxed{\ell'=\frac{m}{k}v_0=\frac{m^2g}{\sqrt2k^2}=\sqrt2\,S.}
$$

虽然最终竖直相对位移为零，球相对新系并非始终水平运动；其初始相对速度斜向左上，此后持续旋转，竖直位移累计后恰好相消。

变式二：取任意 $b=qB>0$，初速度改为终端速度加水平增量 $w\boldsymbol e_x$，$w>0$。求相对终端系的最终位移及总路程。

解：相对速度满足 $m\dot w_x=-kw_x-bw_y$、$m\dot w_y=bw_x-kw_y$。对全程积分，以初值 $(w,0)$ 和末值零消元，得到

$$
\boldsymbol S=\frac{mw}{k^2+b^2}(k\boldsymbol e_x+b\boldsymbol e_y).
$$

相对速率为 $we^{-kt/m}$，故总路程 $\mathcal L=\int_0^\infty we^{-kt/m}dt=mw/k$，而 $|\boldsymbol S|=mw/\sqrt{k^2+b^2}$。路程与位移比为 $\sqrt{1+b^2/k^2}$，体现旋转造成的曲线长度。

变式三：求相对终端速度的模降为初值一半所需时间，以及这一段相对速度方向的转角。

解：磁力垂直速度，不改变相对速率的衰减；对相对方程点乘速度给 $m\,d|\boldsymbol w|^2/dt=-2k|\boldsymbol w|^2$。所以

$$
t_{1/2}=\frac{m\ln2}{k},\qquad
\Delta\varphi=\frac{b}{m}t_{1/2}=\frac bk\ln2.
$$

取 $b=k$，转角为 $\ln2$ 弧度，约 $39.7144^\circ$。时间只由阻力决定，转角另含磁场；若初始速度正好等于终端速度，则相对速度为零，方向及半衰时刻没有定义。

变式四：令磁场为零，粒子从静止释放。求终端速度、相对终端系最终位移及总路程，并与含磁场的公式核对。

解：方程 $m\dot v_y=-kv_y-mg$ 给 $v_{0y}=-mg/k$。相对初速度向上为 $mg/k$，以后始终沿竖直方向指数衰减，因此

$$
\boldsymbol S=\frac{m^2g}{k^2}\boldsymbol e_y,\qquad
\mathcal L=\frac{m^2g}{k^2}=|\boldsymbol S|.
$$

主结果中取 $b=0$ 后水平位移消失，竖直结果相同。相对系的向上位移不表示粒子在实验室向上运动，而是粒子落后于向下匀速运动的参考原点。
