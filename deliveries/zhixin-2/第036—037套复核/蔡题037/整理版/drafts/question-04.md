# 第 4 题

先考虑仅含小球 $A$ 的单摆，再在其下连接质量相同的小球 $B$，形成图中的平面双摆。上端细绳长为 $l_1$，下端细绳长为 $l_2$。在参考温度下 $l_1=l_2=l_0$；两绳的线膨胀系数分别为 $\alpha_1$、$\alpha_2$。

（1）在未连接 $B$ 的单摆阶段，若上绳随温度变化，求小振动周期的一阶相对温漂；

（2）对完整双摆，求两个正则模频率；

（3）要使正则模周期在一阶近似下不随温度变化，$\alpha_1$与 $\alpha_2$ 应满足什么关系？

![题4　绳长随温度变化的等质量双摆](../figures/question-04.pdf){ width=58% }

## 一、题型定位

本题将单摆的温度误差与双摆的线性简正模结合在一起。必须先由动能和势能建立质量矩阵、刚度矩阵，再由特征方程求频率，最后对长度的温度微变化作一阶展开。

## 二、知识点

1. 单摆周期对摆长的对数微分；
2. 双摆小角度运动的二次型；
3. 广义特征值问题 $\det(K-\omega^2M)=0$；
4. 正则模的同相、反相物理图像；
5. 对称点附近的一阶摄动。

## 三、物理图像

两个小角位移不是彼此独立的。低频模中两摆大体同向运动，系统形变较小；高频模中上下两段的运动方向相反，相对形变更快。

![图4-2　等长双摆的同相与反相正则模](../figures/solution-04.pdf){ width=86% }

## 四、解题入口

第（1）问直接从 $T\propto\sqrt l$ 取对数微分。第（2）问选两根绳相对竖直方向的小角 $\theta_1,\theta_2$ 作广义坐标，把位置和速度只保留到足以构成二次型的阶数。第（3）问不必对复杂根式盲目全微分，可以先利用 $l_1=l_2$ 处交换对称性。

## 五、解析

第（1）问中，单摆周期为

$$
T=2\pi\sqrt{\frac{l_1}{g}}. \tag{1}
$$

温度变化 $\Delta\Theta$ 后，线膨胀给出

$$
l_1'=l_1(1+\alpha_1\Delta\Theta). \tag{2}
$$

对式（1）取对数：

$$
\ln T=\ln(2\pi)-\frac12\ln g+\frac12\ln l_1. \tag{3}
$$

微分后

$$
\frac{\Delta T}{T}=\frac12\frac{\Delta l_1}{l_1}. \tag{4}
$$

又有

$$
\frac{\Delta l_1}{l_1}=\alpha_1\Delta\Theta, \tag{5}
$$

所以

$$
\boxed{\frac{\Delta T}{T}=\frac12\alpha_1\Delta\Theta}. \tag{6}
$$

下面建立双摆的线性运动方程。小球 $A$、$B$ 的坐标为

$$
\begin{aligned}
x_A&=l_1\sin\theta_1,& y_A&=-l_1\cos\theta_1,\\
x_B&=l_1\sin\theta_1+l_2\sin\theta_2,
&y_B&=-l_1\cos\theta_1-l_2\cos\theta_2.
\end{aligned} \tag{7}
$$

对时间求导，有

$$
v_A^2=l_1^2\dot\theta_1^2. \tag{8}
$$

对 $B$ 球，

$$
v_B^2=l_1^2\dot\theta_1^2+l_2^2\dot\theta_2^2
+2l_1l_2\dot\theta_1\dot\theta_2\cos(\theta_1-\theta_2). \tag{9}
$$

在线性近似中，动能已经是速度的二阶量，因此式（9）中可取 $\cos(\theta_1-\theta_2)\simeq1$。总动能为

$$
\begin{aligned}
K
&=\frac12mv_A^2+\frac12mv_B^2\\
&=\frac12m\left(2l_1^2\dot\theta_1^2+l_2^2\dot\theta_2^2
+2l_1l_2\dot\theta_1\dot\theta_2\right).
\end{aligned} \tag{10}
$$

取竖直向下平衡位置的重力势能为零。由 $1-\cos\theta\simeq\theta^2/2$，

$$
\begin{aligned}
U
&=2mgl_1(1-\cos\theta_1)+mgl_2(1-\cos\theta_2)\\
&\simeq\frac12mg\left(2l_1\theta_1^2+l_2\theta_2^2\right).
\end{aligned} \tag{11}
$$

由拉格朗日方程 $\frac d{dt}(\partial K/\partial\dot\theta_i)+\partial U/\partial\theta_i=0$，得

$$
\begin{aligned}
2ml_1^2\ddot\theta_1+ml_1l_2\ddot\theta_2+2mgl_1\theta_1&=0,\\
ml_1l_2\ddot\theta_1+ml_2^2\ddot\theta_2+mgl_2\theta_2&=0.
\end{aligned} \tag{12}
$$

约去公因子 $m$，并设

$$
\theta_1=Ae^{i\omega t},
\qquad
\theta_2=Be^{i\omega t}. \tag{13}
$$

代入式（12）：

$$
\begin{pmatrix}
2gl_1-2l_1^2\omega^2&-l_1l_2\omega^2\\
-l_1l_2\omega^2&gl_2-l_2^2\omega^2
\end{pmatrix}
\begin{pmatrix}A\\B\end{pmatrix}=0. \tag{14}
$$

要有非零振幅，系数行列式必须为零：

$$
(2gl_1-2l_1^2\omega^2)(gl_2-l_2^2\omega^2)
-l_1^2l_2^2\omega^4=0. \tag{15}
$$

展开后先合并 $\omega^4$ 项：

$$
2g^2l_1l_2-2gl_1l_2(l_1+l_2)\omega^2
+l_1^2l_2^2\omega^4=0. \tag{16}
$$

除以 $l_1l_2$：

$$
l_1l_2\omega^4-2g(l_1+l_2)\omega^2+2g^2=0. \tag{17}
$$

把 $\omega^2$ 看成未知数，用求根公式：

$$
\omega_\pm^2
=\frac{2g(l_1+l_2)\pm
\sqrt{4g^2(l_1+l_2)^2-8g^2l_1l_2}}{2l_1l_2}. \tag{18}
$$

根号中化简为

$$
(l_1+l_2)^2-2l_1l_2=l_1^2+l_2^2. \tag{19}
$$

因而一般绳长下的两个正则模频率为

$$
\boxed{
\omega_\pm^2
=g\frac{l_1+l_2\pm\sqrt{l_1^2+l_2^2}}{l_1l_2}
}. \tag{20}
$$

在参考温度下 $l_1=l_2=l_0$，式（20）给出

$$
\omega_\pm^2
=\frac g{l_0}(2\pm\sqrt2). \tag{21}
$$

所以

$$
\boxed{
\omega_- =\sqrt{\frac g{l_0}(2-\sqrt2)},
\qquad
\omega_+ =\sqrt{\frac g{l_0}(2+\sqrt2)}
}. \tag{22}
$$

相应周期为

$$
T_\pm=\frac{2\pi}{\omega_\pm}. \tag{23}
$$

现在研究温度稳定性。设

$$
l_1=l_0(1+\varepsilon_1),
\qquad
l_2=l_0(1+\varepsilon_2), \tag{24}
$$

其中

$$
\varepsilon_1=\alpha_1\Delta\Theta,
\qquad
\varepsilon_2=\alpha_2\Delta\Theta. \tag{25}
$$

对根号作一阶展开：

$$
\begin{aligned}
\sqrt{l_1^2+l_2^2}
&=l_0\sqrt{(1+\varepsilon_1)^2+(1+\varepsilon_2)^2}\\
&\simeq l_0\sqrt{2+2(\varepsilon_1+\varepsilon_2)}\\
&=\sqrt2l_0\sqrt{1+\varepsilon_1+\varepsilon_2}\\
&\simeq\sqrt2l_0\left[1+\frac12(\varepsilon_1+\varepsilon_2)\right].
\end{aligned} \tag{26}
$$

分子为

$$
l_1+l_2\pm\sqrt{l_1^2+l_2^2}
=(2\pm\sqrt2)l_0+
\left(1\pm\frac1{\sqrt2}\right)l_0(\varepsilon_1+\varepsilon_2). \tag{27}
$$

注意恒等式

$$
\frac{1\pm1/\sqrt2}{2\pm\sqrt2}=\frac12. \tag{28}
$$

因此分子的相对变化对两个分支都是

$$
\frac{\Delta N_\pm}{N_\pm}=\frac12(\varepsilon_1+\varepsilon_2). \tag{29}
$$

分母一阶变化为

$$
l_1l_2=l_0^2(1+\varepsilon_1)(1+\varepsilon_2)
\simeq l_0^2[1+(\varepsilon_1+\varepsilon_2)], \tag{30}
$$

所以

$$
\frac{\Delta(l_1l_2)}{l_1l_2}=\varepsilon_1+\varepsilon_2. \tag{31}
$$

由式（20）的“分子除以分母”结构，

$$
\frac{\Delta\omega_\pm^2}{\omega_\pm^2}
=\frac12(\varepsilon_1+\varepsilon_2)-(\varepsilon_1+\varepsilon_2)
=-\frac12(\varepsilon_1+\varepsilon_2). \tag{32}
$$

由 $T_\pm\propto(\omega_\pm^2)^{-1/2}$，

$$
\frac{\Delta T_\pm}{T_\pm}
=-\frac12\frac{\Delta\omega_\pm^2}{\omega_\pm^2}
=\frac14(\varepsilon_1+\varepsilon_2). \tag{33}
$$

再代入式（25）：

$$
\frac{\Delta T_\pm}{T_\pm}
=\frac14(\alpha_1+\alpha_2)\Delta\Theta. \tag{34}
$$

要使周期的一阶温漂为零，必须

$$
\boxed{\alpha_1+\alpha_2=0,
\qquad\text{即 }\alpha_1=-\alpha_2}. \tag{35}
$$

值得注意的是，在 $l_1=l_2$ 的对称点，两个正则模的一阶温漂具有相同系数。因此式（35）不仅使其中一个周期不变，而使两个周期都在一阶上不变。

高低两支的频率比还可化成一个简洁常数：

$$
\left(\frac{\omega_+}{\omega_-}\right)^2
=\frac{2+\sqrt2}{2-\sqrt2}.
$$

分子、分母同乘 $2+\sqrt2$：

$$
\frac{2+\sqrt2}{2-\sqrt2}
=\frac{(2+\sqrt2)^2}{4-2}
=3+2\sqrt2.
$$

注意

$$
3+2\sqrt2=(1+\sqrt2)^2.
$$

所以

$$
\frac{\omega_+}{\omega_-}=1+\sqrt2.
$$

周期与频率成反比，故

$$
\frac{T_-}{T_+}=1+\sqrt2.
$$

这个比值与 $m$、$g$、$l_0$ 都无关，是等质量、等长度双摆的纯几何特征。若数值求特征频率后得不到这一比值，通常说明质量矩阵的交叉项或势能中上绳承受两个小球重量的因子 $2$ 被漏掉。

为使图4-2中的“同相、反相”不只停留在示意图，还应由线性方程求出振型。等长时取 $l_1=l_2=l_0$，式（14）的第二行化为

$$
-l_0^2\omega^2A+(gl_0-l_0^2\omega^2)B=0.
$$

约去 $l_0$：

$$
-l_0\omega^2A+(g-l_0\omega^2)B=0.
$$

所以

$$
\frac BA=\frac{l_0\omega^2}{g-l_0\omega^2}.
$$

对低频支 $l_0\omega_-^2/g=2-\sqrt2$，

$$
\frac BA
=\frac{2-\sqrt2}{1-(2-\sqrt2)}.
$$

分母为 $\sqrt2-1$，利用

$$
2-\sqrt2=\sqrt2(\sqrt2-1),
$$

得到

$$
\frac BA=\sqrt2.
$$

低频支中 $A$、$B$ 同号，两个角位移同相，且下球角振幅较大。对高频支 $l_0\omega_+^2/g=2+\sqrt2$，

$$
\frac BA
=\frac{2+\sqrt2}{1-(2+\sqrt2)}
=-\sqrt2.
$$

高频支中两个角位移反相。把振型代回式（12）的两行会得到同一个频率条件，这提供了对行列式求根的独立核验。还要区分“角位移同相”与“两个球的水平速度处处完全相等”：下球水平位置含有上、下两段绳的共同贡献，不能只看 $\theta_2$ 的正负就判断绝对速度。

## 六、关键洞察

在等长点，频率的一阶变化只含 $\varepsilon_1+\varepsilon_2$。取 $\alpha_1=-\alpha_2$ 可同时消去两支的一阶温漂，但反对称长度变化仍会产生二阶修正。

模态分解还应核验能量中的正交性。等长时，质量矩阵和刚度矩阵分别为

$$
M=ml_0^2\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad
K=mgl_0\begin{pmatrix}2&0\\0&1\end{pmatrix}.
$$

取 $\boldsymbol u_-=(1,\sqrt2)^{\mathsf T}$、$\boldsymbol u_+=(1,-\sqrt2)^{\mathsf T}$。直接算得 $\boldsymbol u_-^{\mathsf T}M\boldsymbol u_+=0$、$\boldsymbol u_-^{\mathsf T}K\boldsymbol u_+=0$；普通点积却为 $-1$。广义特征向量的正交使用质量矩阵定义的内积，不能直接按两个角坐标的欧氏内积判断。

令角位移为 $q_-\boldsymbol u_-+q_+\boldsymbol u_+$，动能与势能的交叉项同时消失。两个模态惯量是

$$
M_-=ml_0^2(4+2\sqrt2),\qquad M_+=ml_0^2(4-2\sqrt2),
$$

模态刚度都为 $4mgl_0$，因此二者的刚度惯量比给出 $\omega_-^2=(2-\sqrt2)g/l_0$、$\omega_+^2=(2+\sqrt2)g/l_0$。这个能量核验可以直接检出振型符号或上摆质量系数错误。

一阶温漂相同还可以从特征值微扰计算，而不只依赖交换长度的直觉。若 $K\boldsymbol u=\omega^2M\boldsymbol u$，对参数微分并左乘 $\boldsymbol u^{\mathsf T}$，利用对称矩阵消去振型导数，得到

$$
\delta\omega^2=\frac{\boldsymbol u^{\mathsf T}(\delta K-\omega^2\delta M)\boldsymbol u}{\boldsymbol u^{\mathsf T}M\boldsymbol u}.
$$

把 $l_i=l_0(1+\varepsilon_i)$ 代入本题矩阵并保留一阶，两个分支都给出 $\delta\omega^2/\omega^2=-(\varepsilon_1+\varepsilon_2)/2$。取周期的对数微分后，$\delta T/T=(\varepsilon_1+\varepsilon_2)/4$，与正文一致。

若上下球质量不相等，上述结论不能照抄。上球质量为 $m_A$、下球为 $m_B$ 时，质量矩阵左上元为 $(m_A+m_B)l_1^2$、右下元为 $m_Bl_2^2$，交叉元为 $m_Bl_1l_2$；势能系数依次为 $(m_A+m_B)gl_1$、$m_Bgl_2$。特征方程为

$$
m_A l_1l_2\omega^4-(m_A+m_B)g(l_1+l_2)\omega^2+(m_A+m_B)g^2=0.
$$

等长根及振幅比随质量比改变。长度和、积的对称结构仍可用于一阶分析，但图中 $\sqrt2$ 振幅比和 $1+\sqrt2$ 频率比只属于等质量情况。

## 七、易错点

1. 在式（9）中保留了多余的角度高阶项，却在势能中漏掉二阶项。
2. 漏算 $B$ 球随上绳一起运动的动能，使质量矩阵左上元素少一倍。
3. 直接把单摆频率 $\sqrt{g/l_i}$ 当作双摆的正则频率。
4. 对 $\omega$ 和 $\omega^2$ 的相对变化混淆，漏掉因子 $1/2$。
5. 以为只能使一个正则模温度稳定，没有检查另一分支。

## 八、课堂讲解建议

先从单摆的对数微分热身，然后将双摆的动能和势能分开列出。讲到式（14）时，要把“存在非零振幅”与“行列式为零”明确联系起来。最后将 $\varepsilon_1+\varepsilon_2$ 和 $\varepsilon_1-\varepsilon_2$ 分别称为对称、反对称扰动，帮助学生建立摄动思维。

## 九、变式训练

变式一：在等长情形 $l_1=l_2=l_0$ 下，求两个正则模的振幅比 $B/A$。

由式（14）第二行，

$$
\begin{aligned}
-l_0^2\omega^2A+(gl_0-l_0^2\omega^2)B&=0, \tag{36}\\
\frac BA&=\frac{l_0\omega^2}{g-l_0\omega^2}. \tag{37}
\end{aligned}
$$

代入低、高频支并分别化简：

$$
\begin{aligned}
\frac{B}{A}\biggr|_-
&=\frac{2-\sqrt2}{1-(2-\sqrt2)}
=\sqrt2, \tag{38}\\
\frac{B}{A}\biggr|_+
&=\frac{2+\sqrt2}{1-(2+\sqrt2)}
=-\sqrt2. \tag{39}
\end{aligned}
$$

所以

$$
\boxed{(B/A)_-=\sqrt2,\qquad(B/A)_+=-\sqrt2}. \tag{40}
$$

正负号分别对应图4-2中的同相模和反相模。

变式二：等长双摆从 $\theta_1(0)=\varepsilon$、$\theta_2(0)=0$、两角速度均为零释放。用两个简正模写出随时间的角位移。

解：低频振型可取 $(1,\sqrt2)$，高频振型取 $(1,-\sqrt2)$。初位移分解为二者各乘 $\varepsilon/2$，初速度为零使正弦项消失。因此

$$
\theta_1=\frac\varepsilon2(\cos\omega_-t+\cos\omega_+t),\quad \theta_2=\frac{\varepsilon\sqrt2}{2}(\cos\omega_-t-\cos\omega_+t).
$$

其中 $\omega_\pm^2=(2\pm\sqrt2)g/l_0$。回代 $t=0$ 验证两初值，回代运动方程验证质量矩阵交叉项。下摆初始静止仍会随后运动，因为初态同时激发了两个模。

变式三：两根绳的线膨胀系数相同为 $\alpha$，且长度严格按 $l_1=l_2=l_0(1+\alpha\Delta\Theta)$ 变化。求两个模周期的精确比例及二阶温漂。

解：等长时 $\omega_\pm^2=(2\pm\sqrt2)g/l$，所以两个周期都按 $\sqrt l$ 缩放：

$$
\frac{T_\pm(\Theta)}{T_\pm(0)}=\sqrt{1+\alpha\Delta\Theta}=1+\frac12\alpha\Delta\Theta-\frac18\alpha^2\Delta\Theta^2+O(\Delta\Theta^3).
$$

一阶项与单摆相同，频率比始终为 $1+\sqrt2$。这个精确缩放使用两长度相同地变化；只改上绳的完整双摆不能直接套单摆温漂。

变式四：取 $l_1=l_0(1+\varepsilon)$、$l_2=l_0(1-\varepsilon)$，其中 $|\varepsilon|\ll1$。一阶温漂已消失，求两个模周期的二阶相对变化。

解：长度和为 $2l_0$，平方和的根为 $\sqrt2l_0\sqrt{1+\varepsilon^2}$，长度积为 $l_0^2(1-\varepsilon^2)$。代入精确频率式，展开得

$$
\frac{\omega_\pm^2(\varepsilon)}{\omega_\pm^2(0)}=1+\left[1\pm\frac{\sqrt2}{2(2\pm\sqrt2)}\right]\varepsilon^2+O(\varepsilon^4).
$$

再取平方根的倒数，得到 $\Delta T_-/T_-=(\sqrt2-1)\varepsilon^2/4$、$\Delta T_+/T_+=-(\sqrt2+1)\varepsilon^2/4$。低频周期变长、高频周期缩短，二阶系数不同；消去一阶项不能宣称温度影响完全消失。
