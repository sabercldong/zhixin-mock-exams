# 第014套第3题核验备忘

本文件为内部工作检查点，不进入正式九模块正文。

## 2026-10-10 11:34最新状态

第3题已分题验收通过：question-03.md为完整22步学生核心及九模块教师主稿，5幅TikZ、4个完整带解变式。学生17总/16正文、教师24总/23正文，44符号/176独立数值/39几何及8PDF qpdf、严格日志通过。41工作页/四总览实际审读，25不同高清页直接读取、16同像素公共页复核；最后仅教师20页变化已重读。验收SHA6202a7d993a71a3b17648d68e3d1482a0fe8ed72318c8fa2d23e61b1df0e1e00。下一题第4题，本套3/8仍未整套完成。

以下是10:38初核阶段的数学依据与历史状态，当时没有完整稿；不要从旧待办重新启动第3题。

## 原题与手写路线

2026-10-10 10:34—10:38北京时间，实际重新查看答案第3、第4页两栏与第5页左栏；原题位于已实际阅读的试卷第1页下部。单位质量受恒定大小、沿径向向外的斥力 $g$。$OA=OB=l$，$\angle AOB=2\theta_0$；从 $A$ 以 $v_0=\sqrt{2gl}$ 进入光滑轨道，求到 $B$ 的最短时间轨道。

手写路线含：势能与能量；$n\propto1/v$ 的光学类比；同心圆层的Snell不变量 $nr\sin\alpha$；分离变量积分得到抛物线；辅助牛顿光学粒子的逆平方吸引力类比；直接Euler–Lagrange方程及其降阶。三页不是三道题，不把第5页右栏第4题内容混入。

正式编写须保留正确的Snell与变分路线，补全手写省略的角定义、入出分支、积分常数、代数与端点筛选。不是只用一句“最速线是抛物线”代替计算。

## 能量、坐标及角度

取原点 $O$，$x$ 正轴沿小夹角的平分线，$A=(l\cos\theta_0,-l\sin\theta_0)$，$B=(l\cos\theta_0,+l\sin\theta_0)$。普通几何夹角为 $0<2\theta_0\le\pi$，所以 $0<\theta_0\le\pi/2$；重合点是零时间退化情况，另行说明。

真实斥力为 $\boldsymbol F=mg\boldsymbol e_r$，势能为 $U=-mgr$。光滑固定约束不做功：

$$
\frac12mv_0^2-mgl=0,
\qquad \frac12mv^2-mgr=0,
\qquad v(r)=\sqrt{2gr}.
$$

零的是机械能，不是题设初速度。手写能量行旁的零值标记不能解释成新的 $v_0=0$ 条件，正式正文以清晰的题设初速度和能量式为准。轨道有约束力，真实运动一般不能直接套用关于 $O$ 的角动量守恒；光学类比的辅助粒子是另一模型。

## Snell与第一积分

令 $\alpha$ 是轨道切线与径向线之间的角，取非负 $\sin\alpha$；同心薄层界面的法线为径向。折射率取 $n=k/\sqrt r$，Snell与同心层几何给出 $nr\sin\alpha$ 不变，故

$$
\sqrt r\sin\alpha=\sqrt c,
\quad \sin\alpha=\sqrt{c/r},
\quad \cos\alpha=\pm\sqrt{1-c/r}.
$$

这里 $c$ 是最近半径，$r\ge c>0$。入程的 $\mathrm dr/\mathrm d\varphi<0$，出程大于零，不在全程强行采用正平方根。对于单调角坐标 $\varphi$，

$$
(r')^2=r^2(r/c-1),\qquad
\left|\mathrm d\varphi\right|=
\frac{\sqrt c\,|\mathrm dr|}{r\sqrt{r-c}}.
$$

在转折点令 $r=c$，积分常数由对称端点取 $\varphi=0$。对出程用 $u=\sqrt{r-c}$：$r=c+u^2$，$\mathrm dr=2u\,\mathrm du$，得到

$$
\varphi=2\arctan\sqrt{(r-c)/c},\qquad
r=c\sec^2(\varphi/2).
$$

入程取负角分支，最后同一个偶函数 $r(\varphi)$ 覆盖两段。端点 $r(\pm\theta_0)=l$ 给出 $c=l\cos^2(\theta_0/2)$。手写的 $r=l(1+\cos\theta_0)/(1+\cos\varphi)$ 与此一致。

## 直接变分路线补全

时间泛函为

$$
T=\frac1{\sqrt{2g}}\int_{-\theta_0}^{\theta_0}
\frac{\sqrt{r^2+(r')^2}}{\sqrt r}\,\mathrm d\varphi.
$$

记 $F=\sqrt{r^2+(r')^2}/\sqrt r$。独立微分确认Euler–Lagrange残差为

$$
\frac{\partial F}{\partial r}-\frac{\mathrm d}{\mathrm d\varphi}
\frac{\partial F}{\partial r'}
=\frac{\sqrt r\,[r^2+3(r')^2-2rr'']}
 {2[r^2+(r')^2]^{3/2}}.
$$

所以手写二阶方程 $r^2+3(r')^2-2rr''=0$ 正确。降阶时在单调支上令 $p=r'$、$r''=p\,\mathrm dp/\mathrm dr$，再令 $u=p^2$，得到

$$
\frac{\mathrm du}{\mathrm dr}-\frac3r u=r,
\quad \frac{\mathrm d}{\mathrm dr}(ur^{-3})=r^{-2},
\quad u=Cr^3-r^2.
$$

利用最近点 $p=0,r=c$，有 $C=1/c$，恢复第一积分。此一阶线性方程的积分因子路线比手写的 $x=r^2,y=p^2,w=y/x$ 更清楚；正式解析仍应解释两种路线的对应，而不隐去手写变量代换。

另一直接第一积分为 $F-r'\partial F/\partial r'=r^{3/2}/\sqrt{r^2+(r')^2}=\sqrt c$，可作为代数复核，不取代Euler–Lagrange完整展开。

## 全局最短性的独立证明

Euler–Lagrange只说明驻值，不自动证明全局最短。令

$$
X=\sqrt r\cos(\varphi/2),\qquad
Y=\sqrt r\sin(\varphi/2),
$$

则直接微分得 $\mathrm dX^2+\mathrm dY^2=(\mathrm dr^2+r^2\mathrm d\varphi^2)/(4r)$，交叉项为零，因此 $T=\sqrt{2/g}\int\mathrm ds_w$。映射后的端点为 $(\sqrt l\cos(\theta_0/2),\pm\sqrt l\sin(\theta_0/2))$，最短曲线为竖直线，恰好对应 $r\cos^2(\varphi/2)=c$。

不能不讨论平方根的分支就宣称任意绕行都映成同一端点。先证明没有必要角向回退或绕圈：任意三维路径的单位径向在球面上的累计弧长 $s_\Omega$ 不小于两端小夹角 $\beta=2\theta_0$。保持路径原有 $r(t)$，把角进度改成指定平面内的 $\varphi(t)=-\theta_0+\beta s_\Omega(t)/s_{\Omega,\mathrm{total}}$，其角速度不大于原球面角速度，因而时间不增加。这样得到无绕圈的平面候选，平方根分支连续且固定。再用映射直线长度下界即可证明全局最短。

若路径经过 $O$，速度在那里为零且径向方向奇异，应通过极限路径讨论。映射径向长度经原点至少为 $2\sqrt l$，大于本题最优映射弦长 $2\sqrt l\sin(\theta_0/2)$；最优路线本身 $c\ge l/2>0$，不经过奇点。

原题没有给出阻挡轨道的星体实体半径，且明说任意位置均受同样大小的径向斥力。按给定理想力场求解，不为图中的示意圆猜造实体障碍。若另有实体半径限制，必须另列约束，不能将本结果无条件套用。

## 实际运动与约束力

抛物线的笛卡尔方程是

$$
r+x=2c,\qquad y^2=4c(c-x).
$$

顶点为 $(c,0)$、焦点为 $O$、准线为 $x=2c$，开口朝负 $x$。不能把它画成开口朝正 $x$ 的曲线。取 $q=y/(2c)$，有 $x=c(1-q^2)$、$r=c(1+q^2)$、$\mathrm ds/\mathrm dy=\sqrt{1+q^2}$。由速度式得

$$
\dot y=\sqrt{2gc},\quad
\dot x=-q\sqrt{2gc},\quad
\ddot x=-g,\quad\ddot y=0.
$$

切向从 $A$ 到 $B$，曲率法线 $\boldsymbol n=(-1,-q)/\sqrt{1+q^2}$。真实斥力与约束力相加后才得到上式加速度。约束力为

$$
\boldsymbol N=m\left[(-g,0)-g\frac{(x,y)}r\right]
=\frac{2mg}{\sqrt{1+q^2}}\boldsymbol n.
$$

大小始终为正，且与速度垂直，不做功，与沿轨道内侧接触相容。真实质点有约束力矩，所以不把辅助逆平方粒子的守恒式当作真实角动量守恒。

从 $y_A=-l\sin\theta_0$ 到 $y_B=+l\sin\theta_0$，时间为

$$
T_{\min}=\frac{2l\sin\theta_0}{\sqrt{2gc}}
=2\sqrt{\frac{2l}{g}}\sin\frac{\theta_0}{2}.
$$

时间公式除开半角平方根时，必须使用 $0<\theta_0\le\pi/2$ 下 $\cos(\theta_0/2)>0$。程序第一次保留了绝对值而未化零，已按实际几何角度域正确限定，不通过强行删符号掩盖定义域。

## 后续编写与图稿

正文核心需完整解释势能符号、时间泛函、光学类比、两段积分、端点与转折、抛物线识别、最短性及真实受力。教师进一步解释辅助光学粒子、三维路径的平面化、手写降阶代换与带解变式。

必要图拟为：$O,A,B$ 与最优轨道（不用无数据实体圆阻挡路线）；极坐标弧长微元和Snell径向法线；平方根坐标映射两端点与直线；真实抛物线顶点/焦点/准线；真实斥力、约束力与曲率方向。是否合并图稿以可读性为准，不固定凑图数。

带解变式可选择小夹角展开与圆弧时间比较、实际运动与接触力、不等端点半径的零能量最速线、径向线性斥力下的对数坐标最短圆弧。任何新增变式均须继续独立计算，不把本次初核当作已核验全部变式。

## 10:38初核阶段状态（历史）

已保存初始数学程序，18项符号、108项独立数值检查通过。记录verification/question-03-initial-math.json的SHA为ae131221dd731feeae1f7a9f17fef666cee5cedca8a6ed06518d4a745114c7cf。第3题没有正式九模块主稿、TikZ或PDF，尚未验收。下一步从本备忘的正确路线写完整稿与必要图，不从第2题重启。
