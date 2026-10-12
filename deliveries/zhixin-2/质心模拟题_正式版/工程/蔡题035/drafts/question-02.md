# 第 2 题

<!-- question-start -->
一个绝热、内壁光滑的圆柱形容器水平放置，被固定的导热活塞分成左右两室。右室另由可自由移动的绝热轻活塞与大气隔开。两室各装有一定量的理想氮气，初始均处于平衡态，体积为 $V_0$，压强等于大气压 $p_0$，温度为 $T_0$，定体摩尔热容为 $C_V=5R/2$。

向右室快速输入热量 $Q_0$，加热期间中间活塞来不及传热；加热停止后，两室通过固定导热活塞交换热量，最终达到热平衡。容器和活塞的热容量均忽略，右侧轻活塞的运动可按力学平衡处理。

1. 刚加热结束时，右室气体内能增加量 $\Delta U_1$ 是多少？
2. 最终达到热平衡后，左室气体相对初态的内能增加量 $\Delta U_2$ 是多少？
3. 当中间活塞已经传递的热量达到全过程传热总量的一半时，求两室温差 $\Delta T=T_{\mathrm R}-T_{\mathrm L}$。

![图 2-1　固定导热隔板与右侧可动绝热活塞分隔的两室气体。](../figures/question-02.png)

<!-- question-end -->

## 一、题型定位

两个不同约束气体系统的加热与内部传热。左室定容，右室在外界恒压下体积可变；两室虽有相同的物质的量和相同的内能温度关系，但相同热量引起的温度变化不同。

## 二、知识点

- 理想气体状态方程 $pV=nRT$ 与内能增量 $\Delta U=nC_V\Delta T$。
- 对气体使用 $\Delta U=Q-W$，其中 $W$ 为气体对外做功。
- 理想气体摩尔热容关系 $C_P=C_V+R$。
- 内部交换热量在合并系统中相消，外部大气做功不能相消。
- 固定隔板允许传热而不允许两室交换体积或物质。

## 三、物理图像

左室的体积始终为 $V_0$，温度升高时压强随之升高。中间活塞固定，可以承受左右压强差，不能额外要求左右压强一直相等。

右侧轻活塞面对恒定大气压，忽略其惯性和摩擦，故右室压强始终为 $p_0$。右室升温时膨胀、向大气做功；加热停止后向左室传热，右室降温收缩，大气对右室做功。

“快速”与“等压”并不矛盾：前者是相对于隔板传热时间而言，后者采用轻活塞的力学平衡近似。若同时引入活塞的有限惯性和剧烈压强振荡，题目给出的条件不足以确定瞬态结果。

## 四、解题入口

先把左右两室的热量—温度关系分别写出：

$$
Q_{\mathrm L}=nC_V\Delta T_{\mathrm L},
\qquad
Q_{\mathrm R}=nC_P\Delta T_{\mathrm R}.
$$

然后用已经从右室流向左室的累计热量 $q$ 描述第二阶段。两室温度都能写成 $q$ 的一次函数，最终平衡、传热到一半和任意中间状态便由同一组关系得到。

## 五、解析

（1）确定气体量、热容与功的符号。

两室初态的 $p,V,T$ 完全相同，所以各自物质的量相同：

$$
n=\frac{p_0V_0}{RT_0}.
$$

这里的 $n$ 是每一室的物质的量，整个容器的总量是 $2n$。如果把 $2n$ 代入单室热容，温升会错误地减半。

由迈耶关系，

$$
\begin{aligned}
C_P&=C_V+R\\
&=\frac52R+R\\
&=\frac72R.
\end{aligned}
$$

每室的定容热容量与右室定压热容量分别为

$$
H_V=nC_V=\frac52nR,
\qquad
H_P=nC_P=\frac72nR.
$$

$H_V,H_P$ 的单位是 $\mathrm{J/K}$，不同于单位为 $\mathrm{J/(mol\cdot K)}$ 的摩尔热容。

（2）刚结束加热：计算右室温升、功及内能增加。

图 2-2 把全过程分为初态、快速加热结束和后续传热三个状态。第一阶段固定隔板尚未传热，左室保持初始状态，输入热量全部进入右室。

![图 2-2　两室温度随累计传热量变化及右室等压体积变化。](../figures/solution-02.png)

设加热后右室温度为 $T_{\mathrm R1}$，体积为 $V_{\mathrm R1}$。右室始终等压，因此状态方程相减得

$$
\begin{aligned}
p_0V_{\mathrm R1}&=nRT_{\mathrm R1},\\
p_0V_0&=nRT_0,\\
p_0(V_{\mathrm R1}-V_0)
&=nR(T_{\mathrm R1}-T_0).
\end{aligned}
$$

右室对大气做功为

$$
W_1=\int_{V_0}^{V_{\mathrm R1}}p_0\,\mathrm dV
=p_0(V_{\mathrm R1}-V_0)
=nR(T_{\mathrm R1}-T_0).
$$

将状态方程用于功的计算，是得到定压热容的关键一步。由热力学第一定律，

$$
\begin{aligned}
Q_0
&=\Delta U_1+W_1\\
&=nC_V(T_{\mathrm R1}-T_0)
+nR(T_{\mathrm R1}-T_0)\\
&=n(C_V+R)(T_{\mathrm R1}-T_0)\\
&=nC_P(T_{\mathrm R1}-T_0).
\end{aligned}
$$

因此

$$
T_{\mathrm R1}-T_0
=\frac{Q_0}{nC_P}
=\frac{2Q_0}{7nR}.
$$

所求内能增加量为

$$
\begin{aligned}
\Delta U_1
&=nC_V\frac{Q_0}{nC_P}\\
&=\frac{C_V}{C_P}Q_0\\
&=\frac{5/2}{7/2}Q_0\\
&=\boxed{\frac57Q_0}.
\end{aligned}
$$

另外，

$$
W_1=\frac27Q_0,\qquad
V_{\mathrm R1}-V_0=\frac{2Q_0}{7p_0}.
$$

两项相加确为输入热量：$5Q_0/7+2Q_0/7=Q_0$。这也说明不能把“容器绝热”理解为“加热量全部成为内能”；绝热壁不漏热，但活动边界仍然允许做功。

（3）用累计传热量描述第二阶段。

令 $q\geq0$ 表示加热停止后，已经从右室经过隔板流入左室的热量。左室没有体积变化，所以不做功，内能增加就是 $q$：

$$
\begin{aligned}
q&=nC_V(T_{\mathrm L}-T_0),\\
T_{\mathrm L}(q)&=T_0+\frac{q}{nC_V}.
\end{aligned}
$$

右室向外放热，按“吸热为正”的约定，它的吸热量是 $-q$。右室仍等压，

$$
-q=nC_P(T_{\mathrm R}-T_{\mathrm R1}),
$$

故

$$
T_{\mathrm R}(q)=T_{\mathrm R1}-\frac{q}{nC_P}
=T_0+\frac{Q_0-q}{nC_P}.
$$

右室体积由状态方程得

$$
\begin{aligned}
V_{\mathrm R}(q)
&=\frac{nR}{p_0}T_{\mathrm R}(q)\\
&=V_0+\frac{R}{C_P}\frac{Q_0-q}{p_0}\\
&=V_0+\frac{2(Q_0-q)}{7p_0}.
\end{aligned}
$$

所以随 $q$ 增大，右室温度降低、体积减小。它在第二阶段做的功为负，而不是零：

$$
W_{\mathrm R,2}(q)
=p_0[V_{\mathrm R}(q)-V_{\mathrm R1}]
=-\frac27q.
$$

右室内能变化为

$$
\Delta U_{\mathrm R,2}(q)
=-q-W_{\mathrm R,2}(q)
=-q+\frac27q
=-\frac57q.
$$

负热量 $-q$ 的绝对值大于右室内能减少量，因为大气在收缩过程中对右室补充了能量。

（4）最终达到热平衡，求总传热量与左室内能增加。

设全部传热量为 $q_\infty$，两室最终共同温度为 $T_f$。令前面两条温度直线相等：

$$
T_0+\frac{q_\infty}{nC_V}
=T_0+\frac{Q_0-q_\infty}{nC_P}.
$$

先消去 $T_0$，再乘以 $nC_VC_P$：

$$
\begin{aligned}
C_Pq_\infty&=C_V(Q_0-q_\infty),\\
C_Pq_\infty+C_Vq_\infty&=C_VQ_0,\\
(C_P+C_V)q_\infty&=C_VQ_0.
\end{aligned}
$$

所以

$$
q_\infty
=\frac{C_V}{C_P+C_V}Q_0
=\frac{5/2}{7/2+5/2}Q_0
=\frac5{12}Q_0.
$$

左室从头到尾不做功，故所求

$$
\boxed{\Delta U_2=q_\infty=\frac5{12}Q_0.}
$$

最终共同温升为

$$
\begin{aligned}
T_f-T_0
&=\frac{q_\infty}{nC_V}\\
&=\frac{Q_0}{n(C_P+C_V)}\\
&=\frac{Q_0}{6nR}.
\end{aligned}
$$

左室最终压强、右室最终体积分别为

$$
\begin{aligned}
p_{\mathrm Lf}
&=\frac{nRT_f}{V_0}
=p_0+\frac{Q_0}{6V_0},\\
V_{\mathrm Rf}
&=\frac{nRT_f}{p_0}
=V_0+\frac{Q_0}{6p_0}.
\end{aligned}
$$

而右室压强仍为 $p_0$。两室热平衡只要求温度相等，并不要求固定隔板两侧压强相等；隔板的固定装置提供所需的力。

（5）把两室合并，独立核对最终状态。

由于每室物质的量相同、最终温升相同，每室相对初态的内能增加相同，均为 $5Q_0/12$，所以

$$
\Delta U_{\mathrm{total}}=\frac56Q_0.
$$

全过程对外净功只来自右侧可动活塞：

$$
W_{\mathrm{total}}
=p_0(V_{\mathrm Rf}-V_0)
=\frac16Q_0.
$$

于是

$$
\Delta U_{\mathrm{total}}+W_{\mathrm{total}}
=\frac56Q_0+\frac16Q_0=Q_0,
$$

与全过程外部输入一致。内部传热量 $q_\infty$ 在合并系统的能量账中必须消去，不能在 $Q_0$ 之外再次加上。

还可以从两个阶段核对净功：

$$
\begin{aligned}
W_1+W_{\mathrm R,2}(q_\infty)
&=\frac27Q_0-\frac27\frac5{12}Q_0\\
&=\left(\frac{24}{84}-\frac{10}{84}\right)Q_0\\
&=\frac16Q_0.
\end{aligned}
$$

这一检验同时检查了第二阶段收缩功的负号。

（6）已经传递一半总热量时的温差。

此时

$$
q=\frac12q_\infty=\frac5{24}Q_0.
$$

左室温度为

$$
\begin{aligned}
T_{\mathrm L}
&=T_0+\frac{5Q_0/24}{(5/2)nR}\\
&=T_0+\frac{Q_0}{12nR}.
\end{aligned}
$$

右室温度为

$$
\begin{aligned}
T_{\mathrm R}
&=T_0+\frac{Q_0-5Q_0/24}{(7/2)nR}\\
&=T_0+\frac{19Q_0/24}{(7/2)nR}\\
&=T_0+\frac{19Q_0}{84nR}.
\end{aligned}
$$

相减时统一分母：

$$
\begin{aligned}
\Delta T
&=T_{\mathrm R}-T_{\mathrm L}\\
&=\left(\frac{19}{84}-\frac1{12}\right)\frac{Q_0}{nR}\\
&=\left(\frac{19}{84}-\frac7{84}\right)\frac{Q_0}{nR}\\
&=\frac{Q_0}{7nR}.
\end{aligned}
$$

用初态的 $nR=p_0V_0/T_0$ 消去 $n$：

$$
\boxed{\Delta T=\frac{Q_0T_0}{7p_0V_0}.}
$$

右室仍比左室热，因此按约定 $\Delta T>0$。$Q_0/(p_0V_0)$ 无量纲，结果具有温度量纲。

（7）为什么此时温差恰为初始温差的一半？

把任意 $q$ 时的两室温度相减：

$$
\begin{aligned}
\Delta T(q)
&=\frac{Q_0}{nC_P}
-q\left(\frac1{nC_P}+\frac1{nC_V}\right)\\
&=\frac{Q_0}{nC_P}
\left(1-\frac{q}{q_\infty}\right).
\end{aligned}
$$

它说明温差随累计传热量线性下降。代入 $q=q_\infty/2$：

$$
\Delta T\left(\frac{q_\infty}{2}\right)
=\frac12\frac{Q_0}{nC_P}
=\frac{Q_0}{7nR}.
$$

这个结论来源于热容为常数、两室约束不变，并不意味着经过了“总传热时间的一半”。若传热速率随温差减小，达到严格热平衡甚至需要渐近的无限时间。

## 六、关键洞察

同样的气体在定容和定压约束下，可分别看作热容量为 $H_V$ 和 $H_P$ 的两个储热单元。左室收到的热量全部改变内能，右室放出的热量同时伴随边界功，故它对“交换热量”的响应由 $C_P$ 决定。

设隔板热导为常数 $\mathcal K$，单位为 $\mathrm{W/K}$，则

$$
\frac{\mathrm dq}{\mathrm dt}=\mathcal K\Delta T.
$$

对温差求导，利用两室温度对 $q$ 的斜率，

$$
\frac{\mathrm d\Delta T}{\mathrm dt}
=-\mathcal K\left(\frac1{H_V}+\frac1{H_P}\right)\Delta T.
$$

定义

$$
\tau_{\mathrm th}
=\frac{H_VH_P}{\mathcal K(H_V+H_P)}
=\frac{35nR}{24\mathcal K},
$$

则

$$
\Delta T(t)=\Delta T(0)e^{-t/\tau_{\mathrm th}},
\qquad
q(t)=q_\infty(1-e^{-t/\tau_{\mathrm th}}).
$$

因此传热量达到一半时为 $t=\tau_{\mathrm th}\ln2$。题目没有给出 $\mathcal K$，所以只能求该状态的温差，不能进一步给出数值时间。

## 七、易错点

- 因加热很快就把右室误判为定容，漏掉活动轻活塞的等压约束。
- 用“隔板是活塞”替代“隔板固定”这一条件，错误要求两室压强相等。
- 把右室降温时的放热量写成 $nC_V|\Delta T|$，漏算大气做功。
- 把总传热量认作 $Q_0/2$；输入热量中还有全过程对外净功。
- 将中间温差设为两室各自温升的一半，却没有核对两室不同的有效热容量。
- 把 $n$ 当作两室总物质的量，导致结果整体差一倍。

## 八、课堂讲解建议

先在图上给固定隔板和活动活塞分别标明“无边界功”和“有边界功”，再让学生判断每室应该使用哪一种热容。课堂中保留三个状态的 $T,V,p$，避免把刚加热后的右室温度与最终共同温度混为一谈。

完成第（3）问后，用总能量账回查前两问。板书中把内部热量 $q$ 在左右两式中用相反符号标出，合并时明确划去，而把外部功保留。

## 九、变式训练

变式一：保持两室初态相同，将气体改为单原子理想气体，$C_V=3R/2$。仍向右室快速输入 $Q_0$，求刚加热后右室内能增加、最终左室内能增加以及传热一半时的温差。

此时 $C_P=5R/2$。第一阶段

$$
\Delta U_1=\frac{C_V}{C_P}Q_0=\frac35Q_0.
$$

最终相同温升由

$$
Q_0=n(C_V+C_P)(T_f-T_0)=4nR(T_f-T_0)
$$

确定，所以

$$
\Delta U_{\mathrm Lf}=nC_V(T_f-T_0)=\frac38Q_0.
$$

传热一半时 $q=3Q_0/16$，两室温度分别为

$$
\begin{aligned}
T_{\mathrm L}&=T_0+\frac{Q_0}{8nR},\\
T_{\mathrm R}&=T_0+\frac{13Q_0}{40nR}.
\end{aligned}
$$

故

$$
\boxed{\Delta T=\frac{Q_0}{5nR}
=\frac{Q_0T_0}{5p_0V_0}.}
$$

最终总内能增加 $3Q_0/4$，对大气净功为 $Q_0/4$，两者之和仍为 $Q_0$。热容改变了分配比例，但没有改变能量守恒结构。

变式二：两室摩尔数改为 $\nu_L,\nu_R$，初温相同，左室等容、右室等压，均有 $C_V=cR$。向右室快速输入 $Q_0$。求刚加热后右室内能增量及最终左室内能增量。

解：右室等压热容量 $C_R=\nu_R(c+1)R$，左室等容热容量 $C_L=\nu_LcR$。快速阶段温升为 $Q_0/C_R$，右室内能增加 $cQ_0/(c+1)$。随后共同温升由总能量与右室边界功合并得到 $\Delta T_f=Q_0/(C_L+C_R)$，所以

$$
\Delta U_{L,f}=\frac{\nu_Lc}{\nu_Lc+\nu_R(c+1)}Q_0.
$$

不能按两室摩尔数简单平分热量，左右过程的热容量不同。相等摩尔数且 $c=5/2$ 时恢复 $5Q_0/12$。

变式三：传热隔板的恒定热导为 $\mathcal K$，采用线性传热率 $\dot Q=\mathcal K(T_R-T_L)$，两室过程不变。求温差的时间变化和传完最终传热量一半所需时间。

解：两室方程为 $C_L\dot T_L=\mathcal K\Delta T$、$C_R\dot T_R=-\mathcal K\Delta T$。相减得 $\dot{\Delta T}=-\mathcal K(1/C_L+1/C_R)\Delta T$，所以

$$
\Delta T(t)=\frac{Q_0}{C_R}e^{-t/\tau},\qquad
\tau=\frac{C_LC_R}{\mathcal K(C_L+C_R)}.
$$

积分热流给 $Q_{R\to L}(t)=C_LQ_0[1-e^{-t/\tau}]/(C_L+C_R)$。达到最终量一半时 $t=\tau\ln2$。右室仍须保持准静态等压，隔板传热时标应满足该条件。

变式四：保持原双原子气体、相等摩尔数 $\nu$。当传热量达到最终传热量的四分之三时，求两室温升和温差。

解：总最终传热为 $5Q_0/12$，此时已传 $5Q_0/16$。左室热容量 $5\nu R/2$，所以温升 $Q_0/(8\nu R)$。右室刚加热温升为 $2Q_0/(7\nu R)$，传热时按等压容量 $7\nu R/2$ 降温，得

$$
T_L-T_0=\frac{Q_0}{8\nu R},\quad
T_R-T_0=\frac{11Q_0}{56\nu R},\quad
T_R-T_L=\frac{Q_0}{14\nu R}.
$$

这相当于初始温差的四分之一；不能按内能增量计算右室降温而漏去等压压缩功。
