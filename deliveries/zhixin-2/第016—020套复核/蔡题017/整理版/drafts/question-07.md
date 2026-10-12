# 第7题

<!-- question-start -->

一束平行光沿 $+z$ 方向传播，在垂直于传播方向的平面内放置理想光学元件，如图7-1。$P_1$ 和 $P_2$ 是验偏器，只允许沿各自通光方向的线偏振光通过；其初始通光方向分别为 $x$ 轴和 $y$ 轴。

（1）只有 $P_1,P_2$ 时，最终光强透过率为零。在两者之间加入验偏器 $P_3$，其通光方向与 $x$ 轴的夹角为 $\theta$。求通过 $P_2$ 后的光强与通过 $P_1$ 后的光强之比。

（2）在 $P_1,P_2$ 之间加入厚度为 $l$ 的波片。波片光轴平行于片面，与 $x$ 轴的夹角为 $\theta_3$；沿光轴方向振动和垂直光轴方向振动的光，其折射率分别为 $n_e,n_o$。将 $P_2$ 的通光方向转至与 $x$ 轴成 $\theta_2$ 的方向，且该方向不与 $x$ 轴重合。发现一定条件下光强透过率为 $1$，求 $\theta_3$ 与 $l$ 应满足的条件。真空波长记为 $\lambda$。

（3）在 $P_1,P_2$ 之间放入两片四分之一波片，每片厚度 $l'$ 满足

$$
l'(n_e-n_o)=\frac{\lambda}{4}.
$$

两片波片的光轴分别与 $x$ 轴成 $\beta_1,\beta_2$。$P_2$ 的方向与第（2）问相同，求透过率为 $1$ 的全部 $\beta_1,\beta_2$ 组合条件。

![图7-1 沿传播方向依次排列的验偏器及其横向通光轴。](../figures/question-07.png){width=86%}

<!-- question-end -->

## 一、题型定位

本题比较两种改变偏振状态的操作：验偏器把电场投影到一条通光轴上，波片则对两个互相垂直的分量施加不同相位。前者一般损失光强，后者在理想模型中不损失光强。因此插入第三个验偏器与插入合适波片，都能使原本正交的两验偏器之间出现透射，但两种机制的最高透过率不同。

第（1）问是连续两次投影，第（2）问是单片波片把一种线偏振完整转换为另一种线偏振，第（3）问则要求两片四分之一波片的完整解集。最后一问不能只举出“同轴合成半波片”的一种配置，也不能把两个光轴相差直角与相同混为一谈。

## 二、知识点

电场振幅与时间平均光强；马吕斯定律；偏振轴作为无向直线的角度周期；正交分解中的带符号投影；双折射产生的光程差与相位差；公共相位与相对相位的区别；半波片的线偏振方向变换；四分之一波片产生的椭圆偏振和圆偏振；复振幅的实部、虚部与模平方；理想无损变换的总强度守恒；沿通光轴与被挡轴的两次正交投影；零透射分量的实、虚两条件；分支筛选、退化条件与量纲检查。

采用题设的理想模型：单色光正入射，无吸收、无界面反射损失，两个主轴方向正交，波片只改变相位。实际波片若存在吸收或未消除的反射，即使偏振方向完全匹配，绝对光强也未必达到此理想值。全文以通过 $P_1$ 后的非零光强 $I_1$ 为分母，不额外假设入射光一定是自然光。

## 三、物理图像

经过 $P_1$，电场只沿 $x$ 方向振动。直接遇到沿 $y$ 的 $P_2$，投影为零。加入 $P_3$ 时，先从 $x$ 方向取出沿 $\theta$ 的分量，再从此分量中取出沿 $y$ 的部分，每次都要把投影振幅平方才能得到光强。

波片不是新的验偏器。经过它的两个分量都还存在，但到达出口时的相位关系改变。半波片使两分量相差半个周期，相当于把输入振动方向关于光轴作一次反射；适当选择角平分线，可以让输出方向恰好与转过的 $P_2$ 重合。

两片四分之一波片至少有两种完整转换机制：相同光轴时，相位差叠加成半波片；第一片以合适角度把线偏振变成圆偏振时，第二片可以把圆偏振变为所需的线偏振。第二种机制中，圆偏振的旋向与第一片光轴是哪一条四十五度方向有关，第二片的角度不能随意取相反号。

## 四、解题入口

建立固定的右手坐标系 $\mathbf e_x,\mathbf e_y,\mathbf e_z$，传播方向为 $+\mathbf e_z$。所有横向角度都按从 $x$ 朝 $y$ 的方向为正定义，不在不同图或不同波片处交换观察方向。

任意角度 $\gamma$ 对应两条单位向量：

$$
\mathbf e(\gamma)=
\begin{pmatrix}\cos\gamma\\ \sin\gamma\end{pmatrix},
\qquad
\mathbf q(\gamma)=
\begin{pmatrix}-\sin\gamma\\ \cos\gamma\end{pmatrix}.
$$

$\mathbf e(\gamma)$ 是所选轴，$\mathbf q(\gamma)$ 是沿正方向再转过 $\pi/2$ 的轴。它们的点积为零，模均为 $1$。对波片，前者规定为对应 $n_e$ 的光轴，后者对应 $n_o$；不能只交换轴名而不同时改变相位约定。

验偏器的轴是一条无向直线，所以 $\gamma$ 与 $\gamma+\pi$ 表示同一配置。以下把第（2）、（3）问的非重合目标写为 $\theta_2\not\equiv0\pmod\pi$；这说明“不为零”应对实际轴方向理解。平行目标的退化情形另作完整辨析。

## 五、解析

**第1步：规定光强基准，并从实际振动说明为什么振幅必须平方。**

通过 $P_1$ 后，可在某一横截面写

$$
\mathbf E_1(t)=E_0\cos(\omega t)\,\mathbf e_x.
$$

在同一介质中，光强正比于电场平方的时间平均。设共同的比例系数为 $K>0$，则

$$
\begin{aligned}
I_1&=K\left\langle E_0^2\cos^2(\omega t)\right\rangle\\
&=\frac{K E_0^2}{2}.
\end{aligned}
$$

其中平均是对一个或若干完整周期进行的，

$$
\left\langle\cos^2(\omega t)\right\rangle
=\frac{1}{2\pi}\int_0^{2\pi}\cos^2u\,du=\frac12.
$$

若验偏器通光方向为 $\mathbf e(\gamma)$，投影电场为

$$
\begin{aligned}
\mathbf E_{\rm out}(t)
&=[\mathbf e(\gamma)\cdot\mathbf E_1(t)]\,\mathbf e(\gamma)\\
&=E_0\cos\gamma\cos(\omega t)\,\mathbf e(\gamma).
\end{aligned}
$$

因此 $I_{\rm out}/I_1=\cos^2\gamma$，而不是 $\cos\gamma$。投影振幅为负，只表示振动整体相差 $\pi$，不会使光强为负。

**第2步：分别列两次投影，得到第（1）问的透过率。**

图7-2中，第一幅先从输入 $x$ 方向投影到 $P_3$，第二幅再从 $P_3$ 的方向投影到 $P_2$。两幅都在同一个横向坐标中，虚线表示被投影的几何分量。

![图7-2 从输入偏振到中间通光轴，再到末级通光轴的两次投影。](../figures/malus-07.png){width=80%}

<!-- KEEP_TOGETHER_START -->

通过 $P_3$ 后的振幅为 $E_0\cos\theta$，光强为 $I_1\cos^2\theta$。$P_3$ 与 $y$ 轴之间的夹角为 $\pi/2-\theta$，所以末级振幅和光强分别为

$$
\begin{aligned}
E_2&=E_0\cos\theta\cos\left(\frac{\pi}{2}-\theta\right)
=E_0\cos\theta\sin\theta,\\
I_2&=I_1\cos^2\theta\sin^2\theta.
\end{aligned}
$$

<!-- KEEP_TOGETHER_END -->

利用 $\sin2\theta=2\sin\theta\cos\theta$，得到

$$
\boxed{\frac{I_2}{I_1}=\frac14\sin^2(2\theta).}
$$

分母已经是通过 $P_1$ 后的强度，不能在这里再无条件乘一次 $1/2$。只有另行说明入射光为自然光，并要求相对其原始强度的比值时，才需把理想 $P_1$ 的一半损失计入。

**第3步：核对第（1）问的极值与两个零点。**

因为 $0\le\sin^2(2\theta)\le1$，所以

$$
0\le\frac{I_2}{I_1}\le\frac14.
$$

最大值在 $2\theta=\pi/2+k\pi$ 时取得，即

$$
\theta=\frac{\pi}{4}+\frac{k\pi}{2},\qquad k\in\mathbb Z.
$$

这两类实际通光轴都是输入轴与输出轴的角平分线。若 $\theta=0$，$P_3$ 虽不损失输入光，却不能改变它沿 $x$ 的方向，随后仍被 $P_2$ 全部挡住；若 $\theta=\pi/2$，光在 $P_3$ 处就已全被挡住。两端零值与中间极大值都能由两次投影直接解释。

**第4步：在波片自己的两条主轴上分解输入，并保留负号。**

第（2）问记 $\gamma=\theta_3$。图7-3中蓝色输入矢量沿 $x$，其沿光轴的投影为 $\cos\gamma$，沿正交轴的带符号投影为 $-\sin\gamma$。

![图7-3 输入电场在光轴与其正交主轴上的带符号分解。](../figures/axes-07.png){width=60%}

具体计算为

$$
\begin{aligned}
\mathbf e(\gamma)\cdot\mathbf e_x&=\cos\gamma,\\
\mathbf q(\gamma)\cdot\mathbf e_x&=-\sin\gamma,\\
\mathbf e_x&=\cos\gamma\,\mathbf e(\gamma)
-\sin\gamma\,\mathbf q(\gamma).
\end{aligned}
$$

最后一式可按两个坐标核对：

$$
\begin{aligned}
x:\quad \cos^2\gamma+\sin^2\gamma&=1,\\
y:\quad \cos\gamma\sin\gamma-\sin\gamma\cos\gamma&=0.
\end{aligned}
$$

这里的负号来自定义好的轴方向，不是波片额外给出的相位。改变坐标轴后可以换一种分解写法，但相应的分量和后续相位必须同时变化。

**第5步：由传播光程建立相位差，分清共同相位与相对相位。**

采用复数记号

$$
\mathbf E(t)=E_0\,\operatorname{Re}
[\mathbf F e^{-i\omega t}],
\qquad i^2=-1.
$$

若某分量的复振幅为 $a+ib$，它对应的真实振动是 $a\cos\omega t+b\sin\omega t$；复数没有引入另一种物理电场，只是同时记录余弦和正弦的系数。

真空波数为 $k_0=2\pi/\lambda$。两主轴穿过厚度 $l$ 后分别获得传播相位

$$
\phi_e=k_0n_e l,\qquad \phi_o=k_0n_o l.
$$

定义有符号相位差

$$
\delta=\phi_e-\phi_o
=\frac{2\pi(n_e-n_o)l}{\lambda}.
$$

于是输出复振幅为

$$
\begin{aligned}
\mathbf F_{\rm full}
&=\cos\gamma\,e^{i\phi_e}\mathbf e(\gamma)
-\sin\gamma\,e^{i\phi_o}\mathbf q(\gamma)\\
&=e^{i\phi_e}\left[
\cos\gamma\,\mathbf e(\gamma)
-e^{-i\delta}\sin\gamma\,\mathbf q(\gamma)\right].
\end{aligned}
$$

前面的 $e^{i\phi_e}$ 同时乘在两个分量上，只使全部振动的时间原点改变，不改变偏振状态和时间平均光强，故可略去。括号内的 $e^{-i\delta}$ 不能略去，它决定两个分量能否沿固定直线合成。

**第6步：证明无损波片保持总强度，并把“透过率为一”改写成零被挡分量。**

波片后的归一化复振幅为

$$
\mathbf F=
\cos\gamma\,\mathbf e(\gamma)
-e^{-i\delta}\sin\gamma\,\mathbf q(\gamma).
$$

利用主轴正交，得到

$$
\begin{aligned}
\|\mathbf F\|^2
&=|\cos\gamma|^2+
|e^{-i\delta}\sin\gamma|^2\\
&=\cos^2\gamma+\sin^2\gamma=1.
\end{aligned}
$$

末级验偏器的通光轴为 $\mathbf e(\theta_2)$，被挡轴为 $\mathbf q(\theta_2)$。记两者的复振幅系数为 $A_\parallel,A_\perp$，则

$$
\begin{aligned}
A_\parallel&=\mathbf e(\theta_2)\cdot\mathbf F,\\
A_\perp&=\mathbf q(\theta_2)\cdot\mathbf F,\\
|A_\parallel|^2+|A_\perp|^2&=1.
\end{aligned}
$$

通过 $P_2$ 的强度比为 $|A_\parallel|^2$。因此它等于 $1$ 当且仅当 $A_\perp=0$，即余弦振动和正弦振动在被挡轴上的系数都为零。仅在某一瞬间电场碰巧沿通光轴，不足以保证整个周期没有损失。

**第7步：求单片波片的被挡振幅，严格筛选相位差。**

两个点积分别是

$$
\mathbf q(\theta_2)\cdot\mathbf e(\gamma)
=\sin(\gamma-\theta_2),
\qquad
\mathbf q(\theta_2)\cdot\mathbf q(\gamma)
=\cos(\gamma-\theta_2).
$$

代入第6步得

$$
A_\perp=
\cos\gamma\sin(\gamma-\theta_2)
-e^{-i\delta}\sin\gamma\cos(\gamma-\theta_2).
$$

为看清条件，记两个实数

$$
a=\cos\gamma\sin(\gamma-\theta_2),
\qquad
b=\sin\gamma\cos(\gamma-\theta_2).
$$

若 $a=0$ 且要求 $A_\perp=0$，便还须 $b=0$。分别检查 $\cos\gamma=0$ 或 $\sin(\gamma-\theta_2)=0$，两种情况都迫使 $\theta_2\equiv0\pmod\pi$；反过来从 $b=0$ 检查也相同。所以在本问非重合目标下，$a,b$ 均不为零，可以由 $a=e^{-i\delta}b$ 得

$$
e^{-i\delta}=\frac ab.
$$

右侧为非零实数，左侧模为 $1$，因此只能为 $+1$ 或 $-1$，即 $\delta=m\pi$。若 $\delta=2m\pi$，两主轴的相对相位等效为零，输出仍为输入 $\mathbf e_x$，此时 $A_\perp=-\sin\theta_2\ne0$，必须排除。

剩下的可能只有

$$
\boxed{\delta=(2m+1)\pi.}
$$

这就是半波条件，包括高阶奇数半波条件。不能因“输出是线偏振”就保留整波条件，因为整波片不把非重合的输入轴变成目标轴。

**第8步：在半波条件下求光轴方向，并给出正厚度解。**

半波条件使 $e^{-i\delta}=-1$，所以被挡振幅化为

$$
\begin{aligned}
A_\perp
&=\cos\gamma\sin(\gamma-\theta_2)
+\sin\gamma\cos(\gamma-\theta_2)\\
&=\sin(2\gamma-\theta_2).
\end{aligned}
$$

此处用的是正弦的和角公式。令其为零：

$$
\begin{aligned}
2\gamma-\theta_2&=k\pi,\\
\theta_3=\gamma&=\frac{\theta_2}{2}+\frac{k\pi}{2},
\qquad k\in\mathbb Z.
\end{aligned}
$$

结合相位差定义，厚度条件为

$$
(n_e-n_o)l=\frac{2m+1}{2}\lambda.
$$

如果 $n_e-n_o$ 为正，可以取 $m=0,1,2,\ldots$。若其为负，整数必须使右端同号，确保 $l>0$。不依赖差值符号的写法是

$$
\boxed{
l=\frac{(2j+1)\lambda}{2|n_e-n_o|},
\quad j=0,1,2,\ldots;
\qquad
\theta_3\equiv\frac{\theta_2}{2}\pmod{\pi/2}.
}
$$

若 $n_e=n_o$，没有双折射相位差，不能以有限厚度完成本问所需的非重合方向变换。这里不把分母为零的形式误当成可用解。

**第9步：用真实矢量反射核对半波片的角度因子二。**

如图7-4，把沿光轴的分量保留，把沿正交轴的分量反号。输入 $\mathbf e_x$ 关于光轴反射后，输出偏振轴为 $2\theta_3$。

![图7-4 半波片对两个主轴分量的相对反号与偏振方向变换。](../figures/half-07.png){width=48%}

不依赖图形直觉的坐标验证为

$$
\begin{aligned}
\mathbf F_{\rm H}
&=\cos\gamma\,\mathbf e(\gamma)
+\sin\gamma\,\mathbf q(\gamma)\\
&=
\begin{pmatrix}
\cos^2\gamma-\sin^2\gamma\\
2\sin\gamma\cos\gamma
\end{pmatrix}
=
\begin{pmatrix}\cos2\gamma\\ \sin2\gamma\end{pmatrix}
=\mathbf e(2\gamma).
\end{aligned}
$$

当 $\gamma=\theta_2/2$ 时，$\mathbf F_{\rm H}=\mathbf e(\theta_2)$；当 $\gamma=\theta_2/2+\pi/2$ 时，$\mathbf F_{\rm H}=-\mathbf e(\theta_2)$。两者相差整体相位 $\pi$，实际通光轴相同，强度都完整通过。这解释了为什么轴角条件是模 $\pi/2$，而通常单一轴方向的周期是 $\pi$。

**第10步：对两片四分之一波片逐片分解，不跳过中间偏振。**

第（3）问给出的厚度条件固定了每片有符号相位差 $\delta=\pi/2$，两片符号相同。省略每片自己的共同相位后，沿光轴的分量不变，沿正交轴的分量乘 $e^{-i\pi/2}=-i$。

第一片分解必须使用 $\beta_1$，不能把它的一个分量先写成第二片的角度。通过第一片后

$$
\begin{aligned}
\mathbf F_1
&=\cos\beta_1\,\mathbf e(\beta_1)
-(-i)\sin\beta_1\,\mathbf q(\beta_1)\\
&=\cos\beta_1\,\mathbf e(\beta_1)
+i\sin\beta_1\,\mathbf q(\beta_1).
\end{aligned}
$$

这一状态一般是椭圆偏振，不能马上使用某一条“线偏振方向”再套马吕斯定律。令

$$
d=\beta_1-\beta_2.
$$

对第二片的两条主轴分别求投影，四个几何点积为

$$
\begin{aligned}
\mathbf e(\beta_2)\cdot\mathbf e(\beta_1)&=\cos d,\\
\mathbf e(\beta_2)\cdot\mathbf q(\beta_1)&=-\sin d,\\
\mathbf q(\beta_2)\cdot\mathbf e(\beta_1)&=\sin d,\\
\mathbf q(\beta_2)\cdot\mathbf q(\beta_1)&=\cos d.
\end{aligned}
$$

于是进入第二片的两个复分量分别为

$$
\begin{aligned}
A_e&=\cos\beta_1\cos d-i\sin\beta_1\sin d,\\
A_o&=\cos\beta_1\sin d+i\sin\beta_1\cos d.
\end{aligned}
$$

第二片让 $A_o$ 再乘一次 $-i$，而不改变 $A_e$：

$$
\begin{aligned}
\mathbf F_2&=A_e\mathbf e(\beta_2)-iA_o\mathbf q(\beta_2)\\
&=(\cos\beta_1\cos d-i\sin\beta_1\sin d)\mathbf e(\beta_2)\\
&\quad+(\sin\beta_1\cos d-i\cos\beta_1\sin d)\mathbf q(\beta_2).
\end{aligned}
$$

这里 $(-i)(i)=1$，$(-i)^2=-1$，两个不同的乘积都要区分。每一项都来自先投影、再改变相位，不是假定第二片“抵消掉第一片”而直接写出目标。

**第11步：合并第二片输出的实部和虚部，保留所有方向。**

另记

$$
u=\beta_1+\beta_2.
$$

把第10步的实部、虚部分组：

$$
\begin{aligned}
\operatorname{Re}\mathbf F_2
&=\cos d[\cos\beta_1\,\mathbf e(\beta_2)
+\sin\beta_1\,\mathbf q(\beta_2)],\\
\operatorname{Im}\mathbf F_2
&=-\sin d[\sin\beta_1\,\mathbf e(\beta_2)
+\cos\beta_1\,\mathbf q(\beta_2)].
\end{aligned}
$$

实部括号的两个坐标为

$$
\begin{aligned}
x&=\cos\beta_1\cos\beta_2-\sin\beta_1\sin\beta_2
=\cos u,\\
y&=\cos\beta_1\sin\beta_2+\sin\beta_1\cos\beta_2
=\sin u.
\end{aligned}
$$

虚部括号的两个坐标为

$$
\begin{aligned}
x&=\sin\beta_1\cos\beta_2-\cos\beta_1\sin\beta_2
=\sin d,\\
y&=\sin\beta_1\sin\beta_2+\cos\beta_1\cos\beta_2
=\cos d.
\end{aligned}
$$

因此

$$
\boxed{
\mathbf F_2=\cos d\,\mathbf e(u)
-i\sin d\,\mathbf e\left(\frac{\pi}{2}-d\right).
}
$$

两组实向量分别乘余弦时间项和正弦时间项，不能只把它们的几何方向做一次普通实矢量加法。总强度仍为

$$
\|\mathbf F_2\|^2=\cos^2d+\sin^2d=1,
$$

因为复振幅模平方是各坐标实部平方与虚部平方之和，实、虚两组之间没有这一时间平均交叉项。

**第12步：把满透射条件写成两个实方程。**

投影到 $P_2$ 的被挡轴 $\mathbf q(\theta_2)$。对第11步实部与虚部分别投影：

$$
\begin{aligned}
\mathbf q(\theta_2)\cdot\mathbf e(u)&=\sin(u-\theta_2),\\
\mathbf q(\theta_2)\cdot
\mathbf e\left(\frac{\pi}{2}-d\right)
&=\cos(d+\theta_2).
\end{aligned}
$$

故

$$
A_\perp=\cos d\sin(u-\theta_2)
-i\sin d\cos(d+\theta_2).
$$

模平方必须把实部和虚部分别平方再相加：

$$
\begin{aligned}
|A_\perp|^2
&=\cos^2d\sin^2(u-\theta_2)
+\sin^2d\cos^2(d+\theta_2),\\
\frac{I_2}{I_1}
&=1-\cos^2d\sin^2(u-\theta_2)
-\sin^2d\cos^2(d+\theta_2).
\end{aligned}
$$

两个非负项之和为零，当且仅当它们各自为零，得到完整条件

$$
\boxed{
\cos d\sin(u-\theta_2)=0,
\qquad
\sin d\cos(d+\theta_2)=0.
}
$$

不要把两个实方程改成单个三角方程，也不要直接除去 $\sin d$ 或 $\cos d$；这样会漏掉主要分支。

**第13步：先处理主轴相同与主轴正交的两个特殊分支。**

若 $\sin d=0$，即 $\beta_1-\beta_2=m\pi$，两光轴是同一无向直线。此时 $\cos d=\pm1$，第一个方程要求 $u-\theta_2=k\pi$。结合两式：

$$
\begin{aligned}
\beta_2&\equiv\beta_1\pmod\pi,\\
2\beta_1&\equiv\theta_2\pmod\pi.
\end{aligned}
$$

这给出第一类完整组合：

$$
\boxed{
\beta_2\equiv\beta_1\pmod\pi,\qquad
\beta_1\equiv\frac{\theta_2}{2}\pmod{\pi/2}.
}
$$

它是两片相同轴向的四分之一波片合成半波片，不要求中间状态一定是圆偏振。

若 $\cos d=0$，则两光轴相差 $\pi/2$，第一个方程自动成立。第二个方程还要求 $\cos(d+\theta_2)=0$。代入 $d=\pi/2+m\pi$ 后，这等价于 $\sin\theta_2=0$，与本题非重合目标冲突，因此这一分支排除。

从第11步也可直接核对：$\cos d=0$ 时只有虚部，$\mathbf e(\pi/2-d)$ 沿 $x$，输出仍是输入方向，只多一个公共相位。两个实际光轴相差直角时，第一片的 $e$ 轴正好是第二片的 $o$ 轴，两个相位差抵消，而非叠加成半波片。

**第14步：在两个系数均非零时，解出线偏振—圆偏振—线偏振分支。**

剩下 $\sin d\ne0$ 且 $\cos d\ne0$。此时可分别除去两个非零系数，得到

$$
\begin{aligned}
u-\theta_2&=k\pi,\\
d+\theta_2&=\frac{\pi}{2}+m\pi.
\end{aligned}
$$

把 $u=\beta_1+\beta_2$、$d=\beta_1-\beta_2$ 代入，两式相加消去 $\beta_2,\theta_2$：

$$
\begin{aligned}
2\beta_1&=\frac{\pi}{2}+(k+m)\pi,\\
\beta_1&=\frac{\pi}{4}+\frac{k+m}{2}\pi.
\end{aligned}
$$

再由第一式回代 $\beta_2$，得到第二类组合：

$$
\boxed{
\beta_1\equiv\frac{\pi}{4}\pmod{\pi/2},
\qquad
\beta_2\equiv\theta_2-\beta_1\pmod\pi.
}
$$

具体包含两条不同光轴配置：

$$
\begin{aligned}
\beta_1\equiv\frac{\pi}{4}\pmod\pi
&:\quad\beta_2\equiv\theta_2-\frac{\pi}{4}\pmod\pi,\\
\beta_1\equiv-\frac{\pi}{4}\pmod\pi
&:\quad\beta_2\equiv\theta_2+\frac{\pi}{4}\pmod\pi.
\end{aligned}
$$

第二条对应另一种圆偏振旋向，不能因为都写成“四十五度”而漏去或把两个正负号任意搭配。两式同时整体取复共轭会改变旋向描述，却不改变光强及完整组合条件。

图7-5展示同轴叠加与经过圆偏振的两种机制；中间曲线由真实输出复振幅的实、虚部画出，不是任意椭圆。

![图7-5 相同光轴相位叠加与圆偏振中间态的两条完整转换路线。](../figures/quarter-07.png){width=88%}

同轴路线中，后续使用的是 $\beta_2=\beta_1$ 与 $2\beta_1=\theta_2$；圆偏振路线中，第一片两分量等幅并相差 $\pi/2$，后续使用的是 $\beta_1+\beta_2=\theta_2$。图中第二片轴角因此不能在两条路线之间互换。

<!-- KEEP_TOGETHER_START -->

**第15步：合并完整解集，并说明重复解不应重复计数。**

在 $\theta_2\not\equiv0\pmod\pi$ 下，第（3）问全部解为第13、14步两类的并集。前一类给两种角平分线配置，后一类给两种圆偏振旋向配置，轴角均按模 $\pi$ 识别。

<!-- KEEP_TOGETHER_END -->

以 $\theta_2=\pi/3$ 为例，在 $0\le\beta_1,\beta_2<\pi$ 的基本区间内，四组实际配置是

$$
\begin{aligned}
(\beta_1,\beta_2)
&=\left(\frac{\pi}{6},\frac{\pi}{6}\right),
\quad\left(\frac{2\pi}{3},\frac{2\pi}{3}\right),\\
&\quad\left(\frac{\pi}{4},\frac{\pi}{12}\right),
\quad\left(\frac{3\pi}{4},\frac{7\pi}{12}\right).
\end{aligned}
$$

如图7-6，四个离散点而不是整条角度曲线满足满透射。横坐标是第一片光轴，纵坐标是第二片光轴，交换两片的先后顺序一般不会保留同一输出。

![图7-6 目标通光角为六十度时，两类满透射配置在光轴角平面中的位置。](../figures/branches-07.png){width=65%}

若目标恰好为 $\theta_2=\pi/2$，两类的角度解重合：第一片取 $\pi/4$ 或 $3\pi/4$，第二片取同一方向。物理机制的两种描述在这里指向相同装置，不能把它们当成四组不同解。分支方程先完整保留再求并集，既避免漏解，也避免重复计数。

**第16步：验证第二类确实先产生圆偏振，并在末级保留全部强度。**

以 $\beta_1=\pi/4$ 为例，由第10步

$$
\mathbf F_1=
\begin{pmatrix}
(1-i)/2\\
(1+i)/2
\end{pmatrix}.
$$

两个坐标分量模相同，均为 $1/\sqrt2$，相对相位为 $\pi/2$。对应真实电场为

$$
\begin{aligned}
E_x/E_0&=\tfrac12\cos\omega t-\tfrac12\sin\omega t,\\
E_y/E_0&=\tfrac12\cos\omega t+\tfrac12\sin\omega t.
\end{aligned}
$$

平方相加得

$$
(E_x^2+E_y^2)/E_0^2=\frac12,
$$

所以矢量端点走半径 $E_0/\sqrt2$ 的圆。圆的半径不是 $E_0$，但总光强仍为 $I_1$，因为输入线偏振的电场平方本来就有周期平均的一半。

再取 $\beta_2=\theta_2-\pi/4$。第12步实、虚被挡系数同时为零，第6步总模为 $1$，因而沿通光轴的强度正好是 $I_1$。对于 $\beta_1=-\pi/4$，第一片两坐标相对相位反号，第二片必须取 $\theta_2+\pi/4$。若保留第一片为 $+\pi/4$ 却误把第二片取为 $\theta_2+\pi/4$，输出方向反而与目标正交，透过率为零；这一检查能立即发现符号搭配错误。

**第17步：区分三种看起来相似而结论不同的操作。**

第三个验偏器作真实投影，去掉被挡分量；第（1）问最高只剩 $I_1/4$。无损半波片不去掉分量，只改变相对相位，使输出重新成为目标线偏振，因此可以保留全部 $I_1$。四分之一波片对一般输入产生椭圆偏振，不存在一条固定振动轴可直接再套一次普通线偏振马吕斯定律；必须对两个相差相位的分量投影，再作时间平均或复振幅模平方。

同样，波片光轴转过 $\pi/2$ 与验偏器通光轴转过 $\pi$ 是不同操作。前者交换 $n_e,n_o$ 的几何方向；对单片半波片，两者仅差公共相位，但对单片四分之一波片会反转相对相位意义。两片四分之一波片一同转过 $\pi/2$ 仍可有完整转换，而只把其中一片转过 $\pi/2$ 一般不保留原解。

**第18步：完成量纲、边界、能量和相位约定的交叉检查。**

$\delta=2\pi(n_e-n_o)l/\lambda$ 无量纲，$l,l',\lambda$ 都是长度；三个强度比也均无量纲。波片的归一化模从始至终为 $1$，验偏器把模平方拆成两部分，没有生成额外光能。

单片 $\delta=0$ 时，前述输出恢复 $\mathbf e_x$，目标非重合时不可能满透射；半波片 $\gamma=0$ 时，输入本来沿主轴，只获公共相位，也不能转向。两片光轴相同，则两次 $-i$ 相乘成为 $-1$，回到半波片；两光轴正交，则两个主轴各得到一次相同相位，输出回到输入。第一片光轴沿输入方向时，它不改变线偏振状态；只有第二片四分之一波片，仍不可能把它完整转成非重合线偏振。这些特殊值均与完整分支相符。

若改用 $e^{+i\omega t}$ 表示真实波动，传播因子及全部复振幅取共轭，所有强度比不变。不能只在中间某个步骤改变相位符号，随后仍沿用原旋向和角度搭配。公共相位可以逐片移除，相对相位不能逐片随意改号。

## 六、关键洞察

最直接的满透射判据是“被挡振幅为零”，而不是先猜测输出方向。无损波片使总强度不变，末级验偏器只需检验一条被挡轴。复振幅的实、虚部必须各自满足零条件，这正是最后一问能完整分类的原因。

为用另一条组织方式复核，定义波片的线性作用矩阵

$$
W(\gamma,\delta)
=\mathbf e(\gamma)\mathbf e(\gamma)^{\mathsf T}
+e^{-i\delta}\mathbf q(\gamma)\mathbf q(\gamma)^{\mathsf T}.
$$

每个外积先把任意输入向量投影到相应轴，再把投影矢量还原到横向坐标，因此矩阵不是额外假设。逐项展开为

$$
W(\gamma,\delta)=
\begin{pmatrix}
\cos^2\gamma+e^{-i\delta}\sin^2\gamma&
(1-e^{-i\delta})\sin\gamma\cos\gamma\\
(1-e^{-i\delta})\sin\gamma\cos\gamma&
\sin^2\gamma+e^{-i\delta}\cos^2\gamma
\end{pmatrix}.
$$

因为两投影矩阵彼此正交且平方仍为自身，记 $P_e,P_o$ 后

$$
\begin{aligned}
W^\dagger W
&=(P_e+e^{i\delta}P_o)(P_e+e^{-i\delta}P_o)\\
&=P_e^2+P_o^2+e^{i\delta}P_oP_e
+e^{-i\delta}P_eP_o\\
&=P_e+P_o=\mathbb I.
\end{aligned}
$$

这里 $\dagger$ 表示转置后再取复共轭；这从矩阵角度证明了全部输入偏振的强度守恒。两片作用的顺序是 $W(\beta_2,\pi/2)W(\beta_1,\pi/2)$，右边先作用，不能倒置后仍把第一片的圆偏振条件放在 $\beta_1$。

另一种先判定“输出是线偏振”的方法，可以不预先给定目标。对复矢量 $\mathbf F=\mathbf R+i\mathbf V$，真实场为 $\mathbf R\cos\omega t+\mathbf V\sin\omega t$。只有 $\mathbf R,\mathbf V$ 共线，才沿固定直线振动，二维行列式应为零。第11步给出

$$
\begin{aligned}
R_xV_y-R_yV_x
&=-\cos d\sin d
\sin\left(\frac{\pi}{2}-d-u\right)\\
&=-\cos d\sin d\cos(d+u)\\
&=-\frac12\sin(2d)\cos(2\beta_1).
\end{aligned}
$$

因此线偏振的必要充分条件为

$$
\sin(2d)\cos(2\beta_1)=0.
$$

它把可能性分成同轴、正交轴以及第一片轴在 $\pm\pi/4$。但“输出是线偏振”还不是“通过既定 $P_2$ 无损”，必须继续核对方向：同轴时输出沿 $2\beta_1$，正交轴时沿 $x$，圆偏振分支时沿 $\beta_1+\beta_2$。这一步的方向筛选与主解析的两个零被挡方程完全一致。

平行目标的退化条件也可以完整列出。若 $\theta_2\equiv0\pmod\pi$，第12步变为

$$
\cos d\sin u=0,\qquad \sin d\cos d=0.
$$

后一式要求 $\sin d=0$ 或 $\cos d=0$。如果 $\cos d=0$，两片光轴正交，任意第一片轴角都可使输出回到 $x$；如果 $\sin d=0$，还需 $\sin u=0$，即两片同轴且 $\beta_1\equiv0\pmod{\pi/2}$。没有第三类。单片的平行目标条件则为

$$
\sin\gamma\cos\gamma\,[1-e^{-i\delta}]=0,
$$

对应输入沿某一主轴，或相位差为整波；厚度不再必须为奇数半波。这样既说明了非重合前提的作用，也避免把角度字面上不等于零误当成方向一定不平行。

第（1）问还能推广为连续多个中间验偏器。设从 $x$ 转到 $y$ 共经过 $N$ 个相邻角度间隔，角差为 $\Delta_j$，满足 $0\le\Delta_j<\pi/2$ 且 $\sum_j\Delta_j=\pi/2$。强度比为 $\prod_j\cos^2\Delta_j$。对数函数

$$
f(x)=\ln\cos x,\qquad
f''(x)=-\sec^2x<0
$$

为严格凹函数，在固定角差和下平均分配取得最大值：

$$
\frac1N\sum_{j=1}^N f(\Delta_j)
\le f\left(\frac{\pi}{2N}\right).
$$

于是

$$
T_{\max,N}
=\cos^{2N}\left(\frac{\pi}{2N}\right).
$$

$N=2$ 即本问的 $1/4$。对 $N$ 很大，用 $\ln\cos x=-x^2/2+O(x^4)$：

$$
\begin{aligned}
\ln T_{\max,N}
&=2N\ln\cos\left(\frac{\pi}{2N}\right)\\
&=-\frac{\pi^2}{4N}+O(N^{-3})\longrightarrow0,
\end{aligned}
$$

因此理想连续缓慢投影的总透过率趋近 $1$，但每个有限步骤仍是有损投影，机制与单片无损波片不同。

## 七、易错点

光强基准错放在 $P_1$ 之前，导致额外因子 $1/2$；只乘振幅的余弦而未平方；看见加入元件就以为光能增加；把波片也当成只保留一个投影分量的验偏器。

把第一片波片的两个分解角写成 $\beta_1,\beta_2$ 混用；忘记 $\mathbf q(\gamma)\cdot\mathbf e_x=-\sin\gamma$；第二次投影的两个正弦点积使用同一符号；把 $(-i)(i)=1$ 写成 $-1$。这些错误都可以用零角、同轴和正交轴特殊值立即核对。

只要求输出为线偏振，却不核对它是否与 $P_2$ 重合；把整波片与半波片都留下；求厚度时不筛选正值，或在 $n_e=n_o$ 时直接代入除零公式；遗漏较高阶奇数半波厚度。

在最后一问直接除去 $\sin d$、$\cos d$，漏掉同轴分支；只写一条正四十五度的圆偏振路线，漏另一种旋向；把第二片取角的正负号与第一片任意搭配；把两主轴相差直角的四分之一波片说成半波片，实际这时输出回到输入。

将模 $\pi$ 的实际轴角当成带方向箭头的模 $2\pi$ 角；把半波片输出的整体负号当成方向不匹配；两类解在正交通光目标时重复计数；换观察方向或复时间约定后只改单个相位符号，最终前后不一致。

认为波片产生圆偏振后场矢量圆的半径仍为输入线偏振峰值，误算一倍强度；在一般椭圆偏振中挑某一瞬间方向套马吕斯定律，而未对完整周期平均；把理想无反射、无吸收的满透射结论直接当成实际器件绝对效率。

## 八、课堂讲解建议

课堂先用第7-2图连续做两个带符号电场投影，再对振幅平方，让学生明确第（1）问每一级强度的分母。板书把输入、第一投影、第二投影各列一行，不从最后的倍角公式开始，以免“为何是一第四”只剩记忆。

教师引入波片时，应先说明两个分量都存在，分别沿主轴传播，再用光程除波长得到相位差。先展示零相位、半周期、四分之一周期三个真实振动状态，最后才引入复振幅。对尚不熟悉复数的学生，把实部理解为余弦系数、虚部理解为正弦系数，所有投影都可以分别对这两行完成。

在第7-3图上让学生亲自计算四个坐标点积，特别指出沿正交轴的负投影与波片相位是两种不同来源。讲半波片时先作关于光轴的几何反射，再展开两个坐标验证方向转过两倍轴角；板书同时保留两个角平分线解，并用整体相位解释为何都满透射。

两片波片部分，教师按“第一片输出—第二片两主轴投影—第二次相位—末级被挡轴”四列推进。第10步中每个复项都标清它来自第一片哪一个分量，不先假定输出线偏振。随后以两个非负平方项引导学生分类，先查可能被除掉的零系数，再处理普通分支。

课堂最后比较同轴合成半波片与线—圆—线两条路线，要求学生用第7-6图判断指定目标下有哪些离散解，以及交换两片会怎样。可用变式的角度误差和波长偏离帮助理解理想解的敏感性；不能只检查输出“似乎有光”，还要核验与目标轴的被挡幅是否严格为零。

## 九、变式训练

<!-- KEEP_TOGETHER_START -->

**变式1：第三个验偏器的不同角度与最佳方向。**

通过 $P_1$ 后的强度为 $I_1=8.00\ \mathrm{W\,m^{-2}}$，末级 $P_2$ 沿 $y$。分别取中间轴 $\theta=30^\circ,45^\circ,60^\circ$，求输出强度，再用求导核验最高值的条件。

<!-- KEEP_TOGETHER_END -->

由主解析的两次投影，而非直接猜比值：

$$
\begin{aligned}
\theta=30^\circ:\quad
T&=\left(\frac{\sqrt3}{2}\right)^2
\left(\frac12\right)^2=\frac{3}{16},\\
I_2&=8.00\times\frac{3}{16}
=1.50\ \mathrm{W\,m^{-2}},\\
\theta=45^\circ:\quad
T&=\left(\frac{1}{\sqrt2}\right)^4=\frac14,\\
I_2&=2.00\ \mathrm{W\,m^{-2}},\\
\theta=60^\circ:\quad
T&=\left(\frac12\right)^2
\left(\frac{\sqrt3}{2}\right)^2=\frac{3}{16},\\
I_2&=1.50\ \mathrm{W\,m^{-2}}.
\end{aligned}
$$

两侧角度的结果相同，因为交换两级投影的余弦、正弦因子不改变乘积。对 $T(\theta)=\tfrac14\sin^22\theta$ 求导：

$$
\begin{aligned}
T'(\theta)
&=\tfrac14\cdot2\sin2\theta\cdot\cos2\theta\cdot2
=\frac12\sin4\theta,\\
T''(\theta)&=2\cos4\theta.
\end{aligned}
$$

在 $0<\theta<\pi/2$ 内，唯一驻点为 $\theta=\pi/4$，其二阶导为 $-2<0$。再比较两个边界值零，确认全区间最高值为 $1/4$，而非只确认一个局部驻点。输入若改为 $16.00\ \mathrm{W\,m^{-2}}$ 的自然光，理想 $P_1$ 先给本题的 $8.00$，相对自然入射光的最终最高比才是 $1/8$。

**变式2：半波片的厚度、两个光轴解和小误差。**

设 $\lambda=632.8\ \mathrm{nm}$，$n_e=1.55,n_o=1.54$，目标轴 $\theta_2=60^\circ$。求最薄半波片厚度及光轴条件；再分别讨论光轴多转 $1^\circ$、相位差多出 $5^\circ$ 和两者同时发生时的强度比。

折射率差为 $0.0100$，最薄厚度为

$$
\begin{aligned}
l_{\min}
&=\frac{632.8\times10^{-9}\ \mathrm m}{2(0.0100)}\\
&=31.64\times10^{-6}\ \mathrm m
=31.64\ \mu\mathrm m.
\end{aligned}
$$

两种不同光轴为 $30^\circ$ 和 $120^\circ$，其余按 $180^\circ$ 周期等效。更厚的有效奇数半波片依次为 $3l_{\min},5l_{\min},\ldots$，轴角条件不变。

记实际光轴 $\gamma=\theta_2/2+\varepsilon$、实际相位差 $\delta=\pi+\eta$。第7步两个实系数仍为

$$
a=\cos\gamma\sin(\gamma-\theta_2),
\qquad
b=\sin\gamma\cos(\gamma-\theta_2).
$$

被挡振幅为 $a+e^{-i\eta}b$，因此

$$
\begin{aligned}
L\equiv1-T
&=a^2+b^2+2ab\cos\eta\\
&=(a+b)^2-2ab(1-\cos\eta)\\
&=\sin^2(2\varepsilon)-4ab\sin^2(\eta/2).
\end{aligned}
$$

最后一式中的 $ab$ 仍按实际 $\gamma$ 求，不能在有限光轴误差时直接换成零误差值。若只有光轴误差，$\eta=0$：

$$
T=\cos^2(2\varepsilon)
=\cos^2(2^\circ)\approx0.998782.
$$

若只有相位误差，$\varepsilon=0$，则 $a=-\tfrac12\sin\theta_2$、$b=\tfrac12\sin\theta_2$：

$$
\begin{aligned}
L&=\sin^2\theta_2\sin^2(\eta/2),\\
T&=1-\sin^2(60^\circ)\sin^2(2.5^\circ)
\approx0.998573.
\end{aligned}
$$

两者同时出现时，在完整 $a,b$ 中代入 $\gamma=31^\circ$、$\eta=5^\circ$，得到 $T\approx0.997357$。小误差按弧度展开还可给

$$
L=4\varepsilon^2+\frac{\sin^2\theta_2}{4}\eta^2
+O(\varepsilon^4+\varepsilon\eta^2+\eta^4).
$$

这是二阶近似，误差无一阶项；但它不能代替有限角度的精确表达。轴误差使反射后的方向多转两倍，而相位误差使原本线偏振重新出现椭圆成分，两种损失来源不同。

<!-- KEEP_TOGETHER_START -->

**变式3：列出三十度目标的全部四分之一波片组合。**

目标为 $\theta_2=30^\circ$，两片均满足题设四分之一波厚度。要求在 $0\le\beta_1,\beta_2<180^\circ$ 中列出全部组合，并核对正、负四十五度旋向。

同轴分支满足 $\beta_2=\beta_1$ 且 $2\beta_1\equiv30^\circ\pmod{180^\circ}$，所以

$$
(\beta_1,\beta_2)=(15^\circ,15^\circ),
\quad(105^\circ,105^\circ).
$$

圆偏振分支满足 $\beta_1=45^\circ$ 或 $135^\circ$，$\beta_2\equiv30^\circ-\beta_1\pmod{180^\circ}$：

$$
\begin{aligned}
\beta_1=45^\circ&:\quad
\beta_2=-15^\circ\equiv165^\circ,\\
\beta_1=135^\circ&:\quad
\beta_2=-105^\circ\equiv75^\circ.
\end{aligned}
$$

因此另外两组为 $(45^\circ,165^\circ)$、$(135^\circ,75^\circ)$。后者也可写作 $(-45^\circ,75^\circ)$；不能先把第一片换成等价角，再忘记同时核对第二片的条件。

四组均可在第12步独立检查。第一组 $d=0,u=30^\circ$，被挡两项零；第二组 $d=0,u=210^\circ$，仍有 $\sin(u-\theta_2)=0$。第三组取代表角 $(45^\circ,-15^\circ)$，则 $d=60^\circ,u=30^\circ$，$\cos(d+\theta_2)=\cos90^\circ=0$；第四组取 $(-45^\circ,75^\circ)$，则 $d=-120^\circ,u=30^\circ$，$\cos(d+\theta_2)=\cos(-90^\circ)=0$。所有情况下 $\|\mathbf F_2\|^2=1$，故 $T=1$。

若错误地把第三组第二片取为 $75^\circ=30^\circ+45^\circ$，则 $u=120^\circ,d=-30^\circ$：

$$
\begin{aligned}
1-T
&=\cos^2(-30^\circ)\sin^2(90^\circ)
+\sin^2(-30^\circ)\cos^2(0^\circ)\\
&=\frac34+\frac14=1,
\end{aligned}
$$

即 $T=0$。第二片的完整输出转到了末级被挡轴，因此发生完全消光。

<!-- KEEP_TOGETHER_END -->

<!-- KEEP_TOGETHER_START -->

**变式4：离开设计波长后，同轴与正交轴组合是否仍等效？**

设一片半波片在波长 $\lambda_0$ 处设计为 $\delta_0=\pi$，光轴为 $45^\circ$，目标为沿 $y$ 的末级验偏器。暂忽略折射率差随波长的变化，求 $\lambda=0.9\lambda_0$ 与 $1.1\lambda_0$ 时透过率；再与两片同轴、两片正交轴的四分之一波片比较。

厚度固定时

$$
\delta(\lambda)
=\frac{2\pi(n_e-n_o)l}{\lambda}
=\pi\frac{\lambda_0}{\lambda}.
$$

输入沿两个主轴的振幅分别为 $E_0/\sqrt2$ 和带符号的 $-E_0/\sqrt2$，不是各为原振幅的一半；两个主轴向 $y$ 投影时又各出现一个 $1/\sqrt2$ 因子。由第5步代入 $\gamma=\pi/4$，归一化 $y$ 分量为

$$
\begin{aligned}
F_y&=\cos(\pi/4)\sin(\pi/4)
-e^{-i\delta}\sin(\pi/4)\cos(\pi/4)\\
&=\frac{1-e^{-i\delta}}2.
\end{aligned}
$$

因此

$$
\begin{aligned}
T(\lambda)
&=\frac14|1-e^{-i\delta}|^2\\
&=\frac14[2-2\cos\delta]
=\sin^2\left(\frac{\pi\lambda_0}{2\lambda}\right).
\end{aligned}
$$

代入两种波长：

$$
\begin{aligned}
\lambda=0.9\lambda_0:\quad
T&=\sin^2(5\pi/9)
=\cos^2(\pi/18)\approx0.969846,\\
\lambda=1.1\lambda_0:\quad
T&=\sin^2(5\pi/11)
=\cos^2(\pi/22)\approx0.979746.
\end{aligned}
$$

两片同轴的四分之一波片，在设计波长的单片相位差为 $\pi/2$，偏离后单片相位差为 $\delta(\lambda)/2$。同轴乘积使两条主轴的相位直接相加，合成相位差仍为 $\delta(\lambda)$，所以每个波长的透过率都与上述半波片相同。

若两片实际光轴正交，设第一片两投影为 $P_e,P_o$，单片相位差为 $\rho$，第二片的两投影互换：

$$
\begin{aligned}
W_2W_1
&=(P_o+e^{-i\rho}P_e)(P_e+e^{-i\rho}P_o)\\
&=e^{-i\rho}P_o^2+e^{-i\rho}P_e^2\\
&=e^{-i\rho}\mathbb I.
\end{aligned}
$$

输出只改变公共相位，始终沿 $x$，正交末级透过率始终为零。这不仅在设计波长成立。真实材料存在色散时，应改用 $(n_e(\lambda)-n_o(\lambda))l/\lambda$，不能仍把相位简单按 $\lambda_0/\lambda$ 缩放；本变式的忽略色散前提已明确给出。

<!-- KEEP_TOGETHER_END -->

<!-- question-complete -->
