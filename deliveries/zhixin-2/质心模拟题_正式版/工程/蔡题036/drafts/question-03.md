# 第 3 题

质量分别为 $m,2m,3m$ 的三个光滑小环套在半径为 $R$ 的光滑轻质大圆环上，相邻小环所对的圆心角均为 $120^\circ$。整个装置放在光滑水平面内。使质量为 $3m$ 的小环获得沿大圆环切向的初速度 $v_0$，其余部分此刻速度为零。

求该瞬间三个小环各自的加速度，以及大圆环圆心的加速度。

![图3-1　三小环在轻质圆环上的初始位置与切向速度](../figures/question-03.pdf){ width=72% }

## 一、题型定位

本题是可移动约束下的瞬时动力学问题。圆环没有固定在地面上，因此不能给有速度的小环直接套用相对地面的向心加速度 $v_0^2/R$。正确关系属于“小环相对圆心”的径向加速度。另一方面，圆环轻质使它所受合力必须为零，从而把三个径向约束力联系起来。

## 二、知识点

1. 光滑约束的法向力与切向无作用力；
2. 轻质刚体的瞬时力平衡；
3. 固定长度约束的一阶、二阶时间导数；
4. 相对速度、相对加速度与向心项；
5. 矢量分量联立及质量加权检验；
6. 区分系统质心与几何圆心。

## 三、物理图像

把质量为 $m,2m,3m$ 的小环分别记为 $A,B,C$。按图示，$C$ 位于圆环顶端，$A$ 在左下，$B$ 在右下。由于接触光滑，每个小环在水平面内只受沿半径的约束力，所以其绝对加速度必沿对应半径，但大小要由整个系统共同决定。

获得速度的 $C$ 倾向沿切线离开原来的圆周。圆环随之发生平移，使原先静止的 $A,B$ 也受到径向力而开始加速。圆心不是一个物质质点，它的加速度可以与各个小环加速度不同；它也不是整个系统的质心。

## 四、解题入口

先由轻环合力为零求三个径向加速度大小的比例。将圆心加速度的两分量分别记为 $a_x$ 和 $a_y$，再对三条半径的定长关系写二阶约束。

前两个小环相对圆心的初速度为零，第三个相对速度为 $v_0$，故第三式多出 $v_0^2/R$。这三条约束加上比例关系即可封闭求解。

## 五、解析

取 $x$ 轴向右、$y$ 轴向上。指向圆心的单位矢量依次为

$$
\begin{aligned}
\mathbf n_A&=\left(\frac{\sqrt3}{2},\frac12\right),\\
\mathbf n_B&=\left(-\frac{\sqrt3}{2},\frac12\right),\\
\mathbf n_C&=(0,-1).
\end{aligned}
$$

设三个加速度的径向大小为 $a_A,a_B,a_C$，先按指向圆心为正写

$$
\mathbf a_A=a_A\mathbf n_A,\qquad
\mathbf a_B=a_B\mathbf n_B,\qquad
\mathbf a_C=a_C\mathbf n_C.
$$

若最终某个 $a_i$ 为负，就表示该加速度实际背离圆心；这样设未知数不预先排除结果。图3-2中的红色箭头代表本题求得的方向，蓝色箭头代表圆心加速度。

![图3-2　径向加速度与运动圆心的二阶约束](../figures/solution-03.pdf){ width=95% }

三个小环的径向力大小分别是 $ma_A,2ma_B,3ma_C$。它们对轻环的反作用力相反，而轻环质量趋于零但加速度有限，故其所受合力为零。等价地，

$$
m a_A\mathbf n_A+2m a_B\mathbf n_B+3m a_C\mathbf n_C=\mathbf0.
$$

分别投影到两轴：

$$
\begin{aligned}
\frac{\sqrt3}{2}ma_A-\frac{\sqrt3}{2}(2m)a_B&=0,\\
\frac12ma_A+\frac12(2m)a_B-3ma_C&=0.
\end{aligned}
$$

第一式约去共同因子，得到

$$
a_A=2a_B.
$$

代入第二式，

$$
\frac12a_A+a_B=3a_C
\quad\Rightarrow\quad a_A=3a_C.
$$

因此可令

$$
a_A=a,\qquad a_B=\frac a2,\qquad a_C=\frac a3.
$$

这里加速度与质量成反比，不是因为三者“运动相同”，而是三个方向相隔 $120^\circ$，轻环平衡要求三个径向力大小相等。其矢量和为零的几何条件产生了这个比例。

下面推导运动约束，避免混用绝对和相对向心加速度。对任一小环，令

$$
\mathbf r=\mathbf r_i-\mathbf r_O,\qquad
\mathbf v_{\rm rel}=\mathbf v_i-\mathbf v_O.
$$

圆环保持半径 $R$，所以

$$
\mathbf r\cdot\mathbf r=R^2.
$$

对时间求一次导数，

$$
2\mathbf r\cdot\mathbf v_{\rm rel}=0.
$$

再求一次导数，

$$
2\mathbf v_{\rm rel}\cdot\mathbf v_{\rm rel}
+2\mathbf r\cdot(\mathbf a_i-\mathbf a_O)=0.
$$

因 $\mathbf r=-R\mathbf n_i$，约去 $2R$ 后得到统一的径向约束：

$$
\boxed{(\mathbf a_i-\mathbf a_O)\cdot\mathbf n_i
=\frac{v_{\rm rel}^2}{R}.}
$$

右侧是相对速度平方，而不是绝对速度平方。左侧也必须是相对加速度的径向分量。这个等式是把熟悉的向心加速度推广到可移动圆心时所需的完整形式。

初瞬间 $\mathbf v_O=\mathbf0$，$A,B$ 也静止，因此它们的 $v_{\rm rel}=0$。记 $\mathbf a_O=(a_x,a_y)$，对 $A$，

$$
\begin{aligned}
(\mathbf a_A-\mathbf a_O)\cdot\mathbf n_A&=0,\\
a-\frac{\sqrt3}{2}a_x-\frac12a_y&=0.
\end{aligned}
$$

即

$$
\frac{\sqrt3}{2}a_x+\frac12a_y=a.
$$

对 $B$ 同理，

$$
-\frac{\sqrt3}{2}a_x+\frac12a_y=\frac a2.
$$

将两式相加，横向项消去：

$$
a_y=\frac32a.
$$

将第一式减去第二式，竖向项消去：

$$
\sqrt3a_x=\frac a2,\qquad
a_x=\frac{a}{2\sqrt3}.
$$

对 $C$，初瞬间相对速度为 $v_0$，且 $\mathbf n_C=(0,-1)$，故

$$
\begin{aligned}
(\mathbf a_C-\mathbf a_O)\cdot\mathbf n_C
&=\frac{v_0^2}{R},\\
\frac a3+a_y&=\frac{v_0^2}{R}.
\end{aligned}
$$

注意这里是相加：$C$ 的加速度向下，而圆心加速度的竖直分量向上，因此相对圆心的向下加速度大小为两者之和。若把这项写成 $a_C-a_y$，将会破坏二阶长度约束。

代入 $a_y=3a/2$，

$$
\begin{aligned}
\left(\frac13+\frac32\right)a&=\frac{v_0^2}{R},\\
\frac{11}{6}a&=\frac{v_0^2}{R},\\
a&=\frac6{11}\frac{v_0^2}{R}.
\end{aligned}
$$

于是三个小环的加速度大小为

$$
\boxed{
a_A=\frac6{11}\frac{v_0^2}{R},\qquad
a_B=\frac3{11}\frac{v_0^2}{R},\qquad
a_C=\frac2{11}\frac{v_0^2}{R}.}
$$

三个结果均为正，验证了它们确实指向圆心。若要求完整矢量，分别乘以对应单位矢量：

$$
\begin{aligned}
\boxed{\mathbf a_A}
&=\boxed{\left(\frac{3\sqrt3}{11},\frac3{11}\right)\frac{v_0^2}{R}},\\
\boxed{\mathbf a_B}
&=\boxed{\left(-\frac{3\sqrt3}{22},\frac3{22}\right)\frac{v_0^2}{R}},\\
\boxed{\mathbf a_C}
&=\boxed{\left(0,-\frac2{11}\right)\frac{v_0^2}{R}}.
\end{aligned}
$$

圆心的分量为

$$
\begin{aligned}
a_x&=\frac1{2\sqrt3}\frac6{11}\frac{v_0^2}{R}
=\frac{\sqrt3}{11}\frac{v_0^2}{R},\\
a_y&=\frac32\frac6{11}\frac{v_0^2}{R}
=\frac9{11}\frac{v_0^2}{R}.
\end{aligned}
$$

因此

$$
\boxed{\mathbf a_O=
\left(\frac{\sqrt3}{11},\frac9{11}\right)\frac{v_0^2}{R}}.
$$

其大小和方向分别为

$$
\begin{aligned}
|\mathbf a_O|
&=\frac{\sqrt{3+81}}{11}\frac{v_0^2}{R}
=\boxed{\frac{2\sqrt{21}}{11}\frac{v_0^2}{R}},\\
\tan\beta&=\frac{a_x}{a_y}=\frac1{3\sqrt3},
\end{aligned}
$$

其中 $\beta$ 为从竖直向上方向向右偏转的角，约为 $10.9^\circ$。图3-2中蓝色圆心加速度应主要向上、略向右，不能画成水平向右，也不能画成向着质量为 $3m$ 的小环以外的任意方向。

用三种方法核验。先检查轻环的合力：三个径向力分别为

$$
ma_A=2ma_B=3ma_C=\frac{6m}{11}\frac{v_0^2}{R}.
$$

大小相等、方向间隔 $120^\circ$，其矢量和恰好为零。再检查 $C$ 的相对向心项：

$$
a_C+a_y=\left(\frac2{11}+\frac9{11}\right)\frac{v_0^2}{R}
=\frac{v_0^2}{R}.
$$

最后检查质心加速度。系统水平外力为零，应有

$$
\mathbf a_G=
\frac{m\mathbf a_A+2m\mathbf a_B+3m\mathbf a_C}{6m}
=\mathbf0.
$$

分量代入时，水平项 $3\sqrt3/11-3\sqrt3/11=0$，竖直项 $3/11+3/11-6/11=0$。圆心 $\mathbf a_O\neq0$ 与质心 $\mathbf a_G=0$ 并不矛盾，因为不等质量小环使系统质心不在几何圆心；而且质心位置随小环在环上的分布变化。

再看初瞬间的功率：$A,B$ 的速度为零，$C$ 的速度水平而约束力竖直，故三个力对小环的总瞬时功率为零。这并不要求各个加速度为零；力垂直于速度时，仍可以改变运动方向。量纲上所有结果都按 $v_0^2/R$ 缩放，符合速度平方和曲率半径决定的加速度尺度。

## 六、关键洞察

固定半径约束应写在珠子相对圆心的位矢上。对其长度平方求两次导数，会同时得到相对加速度投影与相对速度平方项，随后再结合圆环受力求解。

## 七、易错点

直接写 $a_C=v_0^2/R$ 等于偷偷固定了圆心，会导致另外两环“没有速度就没有加速度”的连锁错误。没有速度仅表示此刻不需要相对向心项，不能消去圆心的径向加速度投影。

把圆心当质心，会由水平外力为零误判 $\mathbf a_O=0$。本题三个质量不等，而且小环可滑动，几何中心没有质心定理的资格。

对 $A,B$ 写约束时只写竖直分量，会漏掉 $a_x$ 在斜半径方向上的投影。图中的 $30^\circ$、$60^\circ$ 关系决定了 $\sqrt3/2$ 和 $1/2$，不能交换。

## 八、课堂讲解建议

课堂先提出两个不同问题：“大环半径是否固定”和“大环圆心是否固定”，让学生明确前者成立、后者不成立。教师随后用 $\mathbf r^2=R^2$ 的两次求导建立一般式，再给三个小环分别代入。

板书把四个加速度分开画，特别保留圆心的蓝色箭头。求解结束后让学生用质量加权和检查质心加速度，而不是只检查数值是否与预期接近。这样能同时训练约束、动力学和守恒之间的交叉校验。

## 九、变式训练

变式一：如果三个小环质量都改成 $m$，初始位置与仅顶端小环获得 $v_0$ 的条件不变，求该瞬间圆心及三个小环的加速度。

轻环平衡与三个等夹角方向要求三个径向力相等，因此三个小环径向加速度都为 $a$。左右对称给 $a_x=0$。对任一下方小环，二阶约束变为

$$
\frac12a_y=a,\qquad a_y=2a.
$$

对顶端小环，

$$
a+a_y=\frac{v_0^2}{R},
\qquad 3a=\frac{v_0^2}{R}.
$$

故

$$
\boxed{a=\frac{v_0^2}{3R}},\qquad
\boxed{\mathbf a_O=\left(0,\frac{2v_0^2}{3R}\right)}.
$$

虽然三个质量相同，圆心仍可以加速。初始三个位置的算术平均等于圆心，并不表示整个后续运动中这一等式持续成立，因为小环不再始终相隔 $120^\circ$。不能对只在某一瞬间成立的位置关系直接求两次导数。

变式二：给圆环增加质量 $M=m$，圆环仍能在水平面内自由平动。三个珠子仍为 $m,2m,3m$，仅顶部珠子初速为 $v_0$。求刚释放时圆心加速度和三个珠子的向心加速度。

解：圆环平动满足 $M\boldsymbol a_O=-\sum m_i a_i\boldsymbol n_i$；三个几何约束为 $a_i-\boldsymbol a_O\cdot\boldsymbol n_i=v_{i,\rm rel}^2/R$。取 $\boldsymbol n_a=(\sqrt3/2,1/2)$、$\boldsymbol n_b=(-\sqrt3/2,1/2)$、$\boldsymbol n_c=(0,-1)$，并令 $\delta=M/m$，联立可得分母 $D=4\delta^2+24\delta+33$。在 $\delta=1$ 时

$$
\boldsymbol a_O=\frac{v_0^2}{61R}(3\sqrt3,39),\qquad (a_a,a_b,a_c)=\frac{v_0^2}{61R}(24,15,22).
$$

逐项相减，前两珠的相对向心加速度为零，顶部为 $v_0^2/R$，与初速度条件相符。圆环有质量后，不能继续把环上三个反作用力之和置零。

变式三：给原质量可忽略的圆环及三个珠子共同增加任意水平匀速 $\boldsymbol U$。求刚释放时珠子的加速度是否改变，给出约束方程说明。

解：约束中需要的是珠子相对于圆心的速度 $\boldsymbol v_i-\boldsymbol v_O$。共同加速前后的速度差完全相同，因此 $a_i-\boldsymbol a_O\cdot\boldsymbol n_i=v_{i,\rm rel}^2/R$ 的右端不变。力平衡与质量也不变，解仍为

$$
(a_a,a_b,a_c)=\frac{v_0^2}{11R}(6,3,2),\qquad \boldsymbol a_O=\frac{v_0^2}{11R}(\sqrt3,9).
$$

这是伽利略变换下加速度不变的具体核验。若用珠子的实验室速率平方作为相对向心项，就会错误地产生依赖 $\boldsymbol U$ 的结果。

变式四：原环仍无质量，改为仅质量为 $m$ 的左下珠具有切向初速 $v_0$，其他两珠和圆心初速为零。求三个珠子的向心加速度及圆心加速度。

解：记 $b=v_0^2/R$。由 $\sum m_i a_i\boldsymbol n_i=0$，先得 $a_a=2a_b$、$a_c=(a_a+2a_b)/6=2a_b/3$。顶部约束给 $a_{Oy}=-a_c$，右下珠约束给 $-(\sqrt3/2)a_{Ox}+a_{Oy}/2=a_b$。再代入左下珠约束 $a_a-\boldsymbol a_O\cdot\boldsymbol n_a=b$，得到

$$
(a_a,a_b,a_c)=\frac b{11}(6,3,2),\qquad \boldsymbol a_O=-\frac b{11}\left(\frac8{\sqrt3},2\right).
$$

三个向心加速度数值与本题相同，圆心加速度方向改变。直接检验 $\boldsymbol a_O\cdot\boldsymbol n_a=-5b/11$，所以左珠的相对向心项为 $6b/11+5b/11=b$。
