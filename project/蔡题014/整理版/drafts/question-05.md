# 第5题

<!-- question-start -->

如图5-1所示，一块正方形薄金属板的厚度为 $d$，边长为 $l$，且 $l\gg d$。沿两组对边中点的连线，将板面分为四个相等的正方形区域。左上与右下两区的电导率为 $\sigma_1$，左下与右上两区的电导率为 $\sigma_2$，其中 $\sigma_1,\sigma_2>0$。在金属板前、后两个相对的侧面贴上良导电电极，通以直流电，定义两电极之间的等效电阻为 $R$。

![图5-1 棋盘形薄板的四区材料、厚度与相对侧面电极。](../figures/statement-05.png){width=54%}

（1）判断 $R$ 与 $\dfrac{2}{d(\sigma_1+\sigma_2)}$ 的大小关系。

（2）求 $R$。

题面比较式中的厚度符号统一为 $d$。按理想导电模型，两电极分别覆盖所接的完整侧面并保持等势，另两侧面绝缘；材料界面无附加接触电阻，忽略电极引线及接触电阻。电流在板面内流动，厚度方向上的变化忽略。这里的“前、后”指图中贴电极的两条相对边，不指薄板的上、下大表面。

<!-- question-end -->

## 一、题型定位

这是二维非均匀导体的稳恒导电问题，不是四个已知电阻简单串、并联的问题。每一小块虽然是正方形，但它与相邻块的连接面通常既不是完整等势电极，也不是绝缘边界，不能未经证明就把每块替换为一个两端电阻。

第（1）问适合先构造两种可精确计算的改造板：在横向中线上加理想导体，给出电阻下界；沿纵向中线切断横向电流通道，给出电阻上界。改造板能够化成电路，不意味着原板也有相同的串、并联拓扑。

第（2）问的关键是二维对偶。电势的等值线与电流流线在各均匀区域相互垂直，将场与电流旋转 $90^\circ$ 并适当改变比例，可以交换两种材料和电极、绝缘边的角色。棋盘形正方形又恰好在整体旋转 $90^\circ$ 后交换两种材料；这种“局部方程—界面条件—外边界—整体几何”的共同对应，才使精确电阻可求。

## 二、知识点

局部欧姆定律是矢量关系
$$
\boldsymbol j=\sigma\boldsymbol E,\qquad
\boldsymbol E=-\boldsymbol\nabla u,
$$
其中 $u$ 是电势，$\boldsymbol j$ 是体电流密度，单位为 $\mathrm{A/m^2}$。把厚度积分掉，定义片电流和片电导
$$
\boldsymbol K=d\boldsymbol j,\qquad
\kappa=d\sigma,
$$
于是
$$
\boldsymbol K=\kappa\boldsymbol E,\qquad
[\boldsymbol K]=\mathrm{A/m},\qquad[\kappa]=\mathrm S.
$$
这里 $\boldsymbol K$ 是二维电流密度，不是总电流；跨过板面内一段曲线的总电流须对其法向分量沿曲线积分。

稳恒电流不在板内持续积累电荷，因此
$$
\boldsymbol\nabla\cdot\boldsymbol K=0.
$$
静电场满足
$$
(\boldsymbol\nabla\times\boldsymbol E)_z=0.
$$
在材料界面，法向电流连续、切向电场连续：
$$
K_{1n}=K_{2n},\qquad E_{1t}=E_{2t}.
$$
法向电场通常不连续，切向电流也通常不连续。仅仅说“界面上所有场都连续”，会把材料电导率的差别抹去。

均匀长方体的电阻公式 $R=L/(\sigma A)$，只有在电流沿长度方向、横截面等势且电流均匀的条件下才能直接使用。良导电的完整电极提供等势边界，绝缘边提供零法向电流边界；这两类边界不能互换。

电阻大小可用耗散检查。总焦耳功率为
$$
P=\int_\Omega \boldsymbol K\cdot\boldsymbol E\,\mathrm dA
=\int_\Omega\kappa|\boldsymbol\nabla u|^2\,\mathrm dA
=UI=I^2R=\frac{U^2}{R}.
$$
最后三种写法分别适合不同控制条件。比较两个系统时，必须说明固定的是 $U$ 还是 $I$，否则“功率增大所以电阻增大”可能恰好反向。

## 三、物理图像

图5-1是一块有有限厚度的薄板，四个材料区共享完整界面。电极沿前、后侧面的全宽接触，而不是两个只接在中点的点电极。把图中板面展开为图5-2，取 $x$ 向右、$y$ 从前边指向后边；四区的材料编号保持不变。

令后边的电势为 $U>0$，前边为 $0$。总电流 $I>0$ 从后边流向前边，即主要沿负 $y$ 方向；正电流与电势增加方向相反。左右边不向外导电，局部电流可以偏转，但不能穿过这两条外边界。

![图5-2 电极等势边界、侧边绝缘条件与电流函数的边界值。](../figures/layout-05.png){width=57%}

图5-2中的 $\psi$ 是稍后定义的电流函数，单位为安培。两条侧边的 $\psi$ 值相差总电流 $I$，并不是说两条侧边有大小为 $I$ 的电流流出。电势差反映沿电场方向的变化，电流函数差反映横跨流管时累计经过的电流；两者的量纲、方向和边界职责各不相同。

四块中央的交点会使非均匀场的局部求解较复杂，但求总电阻不要求先画出每一条精确流线。所需信息是守恒、界面条件和整体对偶，不把随意弯曲的示意线当作已求得的电场。

## 四、解题入口

先把三维电导率换成片电导 $\kappa_i=d\sigma_i$，避免在电流函数中反复漏掉厚度。再固定电极电压 $U$、把实测总电流记为 $I$，明确 $R=U/I$；这一归一化不会预先假定电流均匀。

比较大小时，不先猜一个平均电导率。在横中线短接与纵中线切开后，分别计算可确认的串、并联电阻，并以耗散原理判定它们相对于原板的上下关系。

求精确值时，先证明电流函数存在，再把旋转后的电流用作新电场，把旋转后的电场用作新电流。尤其要检查四条外边界：原有绝缘边成为新电极，原有电极成为新绝缘边。只有新问题的材料与边界共同等于整体旋转后的原问题，才可以令新、旧等效电阻相等。

## 五、解析

**第1步：定义研究区域、正方向和端口量。**

取前边左端为原点 $O$，展开后的板面为
$$
\Omega=\{(x,y):0<x<l,\ 0<y<l\}.
$$
后电极在 $y=l$、前电极在 $y=0$，故
$$
u(x,l)=U,\qquad u(x,0)=0.
$$
左右两边绝缘，因而
$$
K_x(0,y)=K_x(l,y)=0.
$$
定义正的总电流
$$
I=-\int_0^l K_y(x,y)\,\mathrm dx.
$$
负号来自电流主要向负 $y$。稳恒时这个积分与所取水平截面的高度无关：对两个截面之间的区域应用电流守恒，左右边没有流出量，上、下截面的流入与流出必须相等。因此
$$
R=\frac UI>0.
$$

**第2步：写清分区片电导和实际满足的方程。**

记
$$
\kappa_1=d\sigma_1,\qquad \kappa_2=d\sigma_2.
$$
材料分布为
$$
\kappa(x,y)=
\begin{cases}
\kappa_1,&x<l/2,\ y>l/2,\ \text{或 }x>l/2,\ y<l/2,\\
\kappa_2,&x<l/2,\ y<l/2,\ \text{或 }x>l/2,\ y>l/2.
\end{cases}
$$
由 $\boldsymbol K=-\kappa\boldsymbol\nabla u$ 和电流守恒，得到
$$
\boldsymbol\nabla\cdot(\kappa\boldsymbol\nabla u)=0.
$$
在每个常电导区内部，这化为 $\nabla^2u=0$；跨界面则须同时满足电势连续和法向电流连续。不能把不同材料区分别解出的四个任意电势直接拼接。

**第3步：说明为什么四小块不能直接当作四个两端电阻。**

若一小块两端真的由完整等势电极覆盖，而另外两边绝缘，它的电流才沿一维均匀流动。原板的横中线没有导体将它强制等势，纵中线也没有绝缘裂缝阻止横向电流。原板不能同时拥有这两项并未给出的边界条件。

尤其在横中线的同一个 $x$ 处，上、下材料的电导不同。若强行使用全板均匀的竖直电场，则两侧法向电流分别为 $\kappa_1E_y$ 与 $\kappa_2E_y$，通常不相等，违背稳恒电流连续性。真实场必须调整，不能以“总面积各占一半”免去这一调整。

**第4步：添加横向理想导体，构造可计算的下界板。**

如图5-3左，在 $y=l/2$ 的整条中线上加一个电阻可忽略的窄导体，将中线变成等势线。上半板中的两个小正方形分别跨接后电极与中线，成为两个并联支路；下半板同样形成两个并联支路。

![图5-3 （a）横向短接的下界板；（b）纵向绝缘切缝的上界板。](../figures/bounds-05.png){width=82%}

每个小块的电流路长为 $l/2$，垂直于电流的横截面积为 $d(l/2)$，所以
$$
\begin{aligned}
R_1&=\frac{l/2}{\sigma_1d(l/2)}=\frac1{\kappa_1},\\
R_2&=\frac{l/2}{\sigma_2d(l/2)}=\frac1{\kappa_2}.
\end{aligned}
$$
上半板的并联电导为 $\kappa_1+\kappa_2$，其电阻为 $1/(\kappa_1+\kappa_2)$；下半板相同。两半板串联：
$$
R_{\text{短}}=\frac2{\kappa_1+\kappa_2}
=\frac2{d(\sigma_1+\sigma_2)}.
$$
进一步使用图中的中线电势 $u_m$：上半板流入中线的电流为 $(\kappa_1+\kappa_2)(U-u_m)$，下半板流出的电流为 $(\kappa_1+\kappa_2)u_m$。中线不能持续积累电荷，故
$$
(\kappa_1+\kappa_2)(U-u_m)=(\kappa_1+\kappa_2)u_m,
\qquad u_m=\frac U2.
$$
这个结果属于加了导体的板，不证明原板整条横中线的电势也为 $U/2$。
导体中线仅用于这个改造系统，不能在未改造的原板中也把中线当作等势电极。

**第5步：用固定电压的耗散原理判定下界方向。**

对任一满足两电极电势的连续试探电势 $v$，写
$$
v=u+w,
$$
其中真实解为 $u$，且 $w$ 在两电极为零。展开功率泛函：
$$
\begin{aligned}
\mathcal P[v]
&=\int_\Omega\kappa|\boldsymbol\nabla(u+w)|^2\,\mathrm dA\\
&=\mathcal P[u]
+2\int_\Omega\kappa\boldsymbol\nabla u\cdot\boldsymbol\nabla w\,\mathrm dA
+\int_\Omega\kappa|\boldsymbol\nabla w|^2\,\mathrm dA.
\end{aligned}
$$
中间项用分部积分处理。体积分因真实场满足 $\nabla\cdot(\kappa\nabla u)=0$ 而为零；电极边界因 $w=0$ 而为零；绝缘边因法向电流为零而为零。材料内部界面的两侧边界项由电势及法向通量连续而相消。于是
$$
\mathcal P[v]=\mathcal P[u]
+\int_\Omega\kappa|\boldsymbol\nabla w|^2\,\mathrm dA
\ge\mathcal P[u].
$$
这说明固定电极电压时，真实电势使耗散最小。加理想导体后，导体内电势变化必须为零，试探电势受到额外限制；最小功率不会降低。因两系统电压相同、$P=U^2/R$，得到
$$
R_{\text{短}}\le R.
$$
“最小功率增大”与“电阻减小”并不矛盾，关键是此处固定的是电压。

**第6步：用一个线性试探电势复核下界和等号条件。**

不用真的添加导体，也可令
$$
v(x,y)=\frac Ul y,\qquad
|\boldsymbol\nabla v|^2=\frac{U^2}{l^2}.
$$
两种材料的面积各为 $l^2/2$，所以
$$
\begin{aligned}
\mathcal P[v]
&=\frac{U^2}{l^2}\left(\kappa_1\frac{l^2}2+\kappa_2\frac{l^2}2\right)\\
&=\frac{U^2}{2}(\kappa_1+\kappa_2).
\end{aligned}
$$
由真实功率不超过试探功率，
$$
\frac{U^2}{R}\le\frac{U^2}{2}(\kappa_1+\kappa_2),
\qquad
R\ge\frac2{\kappa_1+\kappa_2}.
$$
若 $\kappa_1\ne\kappa_2$，这个线性电势在横向界面产生不连续的法向电流，不能是真实解，故不等号严格。若 $\kappa_1=\kappa_2$，板为均匀导体，线性电势正是真实解，等号成立。第（1）问的完整结论是
$$
\boxed{
R>\frac2{d(\sigma_1+\sigma_2)}\quad(\sigma_1\ne\sigma_2);
\qquad
R=\frac2{d(\sigma_1+\sigma_2)}\quad(\sigma_1=\sigma_2).
}
$$

**第7步：切断纵向横流，构造电阻上界。**

如图5-3右，沿 $x=l/2$ 加绝缘切缝。每个竖直长条变为独立的串联支路：一块材料 $1$ 与一块材料 $2$ 串联。每支路电阻为
$$
R_{\text{支}}=\frac1{\kappa_1}+\frac1{\kappa_2}
=\frac{\kappa_1+\kappa_2}{\kappa_1\kappa_2}.
$$
左右两条相同支路并联，得
$$
R_{\text{切}}=\frac{\kappa_1+\kappa_2}{2\kappa_1\kappa_2}
=\frac{\sigma_1+\sigma_2}{2d\sigma_1\sigma_2}.
$$
切缝阻止原先可有的横向电流重分配；它是另一个改造系统，不是原板中本来就存在的边界。

固定总电流，以满足电流守恒、外侧绝缘和给定总端口电流的片电流为试探量。真实场使下列泛函取最小值：
$$
\mathcal D[\boldsymbol K]=\int_\Omega
\frac{|\boldsymbol K|^2}{\kappa}\,\mathrm dA
$$
切缝增加零法向电流约束，最小 $\mathcal D$ 不会降低；而 $\mathcal D=I^2R$，所以
$$
R\le R_{\text{切}}.
$$
此处固定的是总电流，不沿用第5步固定电压时的功率比较方向。

**第8步：补出固定电流最小耗散的依据。**

设真实电流为 $\boldsymbol K$，另一个允许电流为 $\boldsymbol K+\delta\boldsymbol K$。两者均满足守恒，且两电极的总电流相同。展开：
$$
\begin{aligned}
\mathcal D[\boldsymbol K+\delta\boldsymbol K]-\mathcal D[\boldsymbol K]
&=2\int_\Omega\frac{\boldsymbol K}{\kappa}\cdot\delta\boldsymbol K\,\mathrm dA
+\int_\Omega\frac{|\delta\boldsymbol K|^2}{\kappa}\,\mathrm dA\\
&=-2\int_\Omega\boldsymbol\nabla u\cdot\delta\boldsymbol K\,\mathrm dA
+\int_\Omega\frac{|\delta\boldsymbol K|^2}{\kappa}\,\mathrm dA.
\end{aligned}
$$
第一项分部积分后，体积分因 $\nabla\cdot\delta\boldsymbol K=0$ 而为零；绝缘外边没有通量；每条电极上 $u$ 为常数，而 $\delta\boldsymbol K$ 的总端口通量为零，边界积分也为零。于是
$$
\mathcal D[\boldsymbol K+\delta\boldsymbol K]-\mathcal D[\boldsymbol K]
=\int_\Omega\frac{|\delta\boldsymbol K|^2}{\kappa}\,\mathrm dA\ge0.
$$
这证明了第7步所需的比较方向，而不是凭“电流走得绕，所以电阻大”的口头印象下结论。

取均匀竖直试探片电流 $\boldsymbol K_{\text{试}}=(0,-I/l)$，它满足电流守恒和外边条件。积分给出
$$
\begin{aligned}
\mathcal D[\boldsymbol K_{\text{试}}]
&=\frac{I^2}{l^2}
\left(\frac{l^2}{2\kappa_1}+\frac{l^2}{2\kappa_2}\right)\\
&=I^2\frac{\kappa_1+\kappa_2}{2\kappa_1\kappa_2},
\end{aligned}
$$
再次得到上界。这条试探电流一般不是实际电流，因为它对应的电场在纵向界面不能满足切向连续。

**第9步：建立电流函数，保留与总电流的量纲关系。**

板面区域无孔洞，且 $\nabla\cdot\boldsymbol K=0$。可以引入电流函数 $\psi(x,y)$，定义
$$
K_x=\frac{\partial\psi}{\partial y},
\qquad
K_y=-\frac{\partial\psi}{\partial x}.
$$
这样
$$
\frac{\partial K_x}{\partial x}+
\frac{\partial K_y}{\partial y}
=\frac{\partial^2\psi}{\partial x\partial y}
-\frac{\partial^2\psi}{\partial y\partial x}=0.
$$
流线是 $\psi$ 的等值线，因为
$$
\boldsymbol K\cdot\boldsymbol\nabla\psi
=\psi_y\psi_x-\psi_x\psi_y=0.
$$
在左右绝缘边，$K_x=\psi_y=0$，所以 $\psi$ 沿每条侧边分别为常数。选择左边常数为零：
$$
\psi(0,y)=0.
$$
由第1步的总电流定义，
$$
\begin{aligned}
I&=-\int_0^lK_y\,\mathrm dx
=\int_0^l\psi_x\,\mathrm dx\\
&=\psi(l,y)-\psi(0,y),
\end{aligned}
$$
故
$$
\psi(l,y)=I.
$$
图5-2右边标出的 $I$ 是电流函数值。它对应所有流管的累计电流，不是右边界流出的电流。

**第10步：把微小流管的关系转为二维局部欧姆定律。**

在某个均匀材料区，沿电场方向移动距离 $\mathrm ds$，电势下降量的大小为 $\mathrm du$；横跨一个流管的宽度为 $\mathrm d\ell$，电流函数差为 $\mathrm d\psi$。于是
$$
E=\left|\frac{\mathrm du}{\mathrm ds}\right|,
\qquad
j=\frac{|\mathrm d\psi|}{d\,\mathrm d\ell}.
$$
由 $j=\sigma E$，
$$
\left|\frac{\mathrm d\psi}{\mathrm d\ell}\right|
=d\sigma\left|\frac{\mathrm du}{\mathrm ds}\right|
=\kappa\left|\frac{\mathrm du}{\mathrm ds}\right|.
$$
这保留了电势线与流线交换的几何依据。但绝对值不能决定新场的正方向；以下用旋转矩阵把所有方向和负号一并固定，避免只交换两组曲线后漏验界面。

**第11步：检查材料界面上的折转关系。**

如图5-4，取界面法线 $\boldsymbol n$ 从材料 $1$ 指向材料 $2$，切向 $\boldsymbol t$ 为将 $\boldsymbol n$ 逆时针转 $90^\circ$ 得到的方向。稳恒条件和静电条件分别给出
$$
K_{1n}=K_{2n}=K_n,\qquad E_{1t}=E_{2t}=E_t.
$$

![图5-4 材料界面两侧的法向电流与切向电场连续。](../figures/interface-05.png){width=55%}

令 $\theta_i$ 为电流方向与界面法线之间的夹角。各材料内电流与电场平行，故
$$
\begin{aligned}
\tan\theta_1&=\frac{K_{1t}}{K_n}
=\frac{\kappa_1E_t}{K_n},\\
\tan\theta_2&=\frac{K_{2t}}{K_n}
=\frac{\kappa_2E_t}{K_n}.
\end{aligned}
$$
在相应分量非零时，
$$
\frac{\tan\theta_2}{\tan\theta_1}=\frac{\kappa_2}{\kappa_1}
=\frac{\sigma_2}{\sigma_1}.
$$
图示取 $\kappa_1>\kappa_2$，所以材料 $1$ 中的电流更偏向切线，进入材料 $2$ 后更靠近法线。零切向分量或零法向分量应直接使用连续条件，不对零量作除法。

**第12步：定义带正确单位和方向的对偶场。**

记逆时针 $90^\circ$ 旋转矩阵为
$$
Q=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\qquad
Q(v_x,v_y)=(-v_y,v_x).
$$
另定义正的片电导尺度
$$
\kappa_0=\sqrt{\kappa_1\kappa_2}.
$$
构造新场、新电流
$$
\boxed{
\boldsymbol E^\star=\frac1{\kappa_0}Q\boldsymbol K,
\qquad
\boldsymbol K^\star=\kappa_0Q\boldsymbol E.
}
$$
$\boldsymbol K/\kappa_0$ 的单位为 $\mathrm{V/m}$，$\kappa_0\boldsymbol E$ 的单位为 $\mathrm{A/m}$，所以不能省去比例尺度而直接把电流密度当作电场。

因为 $\boldsymbol K=\kappa\boldsymbol E$，
$$
\begin{aligned}
\boldsymbol E^\star&=\frac{\kappa}{\kappa_0}Q\boldsymbol E,\\
\boldsymbol K^\star&=\frac{\kappa_0^2}{\kappa}\boldsymbol E^\star.
\end{aligned}
$$
新材料的片电导为
$$
\kappa^\star(x,y)=\frac{\kappa_0^2}{\kappa(x,y)}.
$$
由于 $\kappa_0^2=\kappa_1\kappa_2$，原材料 $1$ 变为材料 $2$，原材料 $2$ 变为材料 $1$。

**第13步：逐项确认新场满足稳恒导电方程。**

新电场的两分量为
$$
E_x^\star=-\frac{K_y}{\kappa_0},
\qquad E_y^\star=\frac{K_x}{\kappa_0}.
$$
其旋度为
$$
\begin{aligned}
(\boldsymbol\nabla\times\boldsymbol E^\star)_z
&=\frac{\partial E_y^\star}{\partial x}
-\frac{\partial E_x^\star}{\partial y}\\
&=\frac1{\kappa_0}
\left(\frac{\partial K_x}{\partial x}+\frac{\partial K_y}{\partial y}\right)=0.
\end{aligned}
$$
新电流两分量为 $K_x^\star=-\kappa_0E_y$、$K_y^\star=\kappa_0E_x$，所以
$$
\begin{aligned}
\boldsymbol\nabla\cdot\boldsymbol K^\star
&=-\kappa_0\frac{\partial E_y}{\partial x}
+\kappa_0\frac{\partial E_x}{\partial y}\\
&=-\kappa_0(\boldsymbol\nabla\times\boldsymbol E)_z=0.
\end{aligned}
$$
原问题的电流守恒变成新问题的无旋电场，原问题的无旋电场变成新问题的电流守恒。这正是二维旋转能发挥作用的原因。

**第14步：确认对偶场在材料界面也能衔接。**

图5-4的法、切向基满足 $Q\boldsymbol n=\boldsymbol t$、$Q\boldsymbol t=-\boldsymbol n$。因此
$$
K_n^\star=-\kappa_0E_t,\qquad
E_t^\star=\frac{K_n}{\kappa_0}.
$$
原来的 $E_t$ 连续，使新 $K_n^\star$ 连续；原来的 $K_n$ 连续，使新 $E_t^\star$ 连续。负号只改变取向，不破坏两侧相等关系。

至此新问题不仅在各小块内部成立，也满足材料界面条件。如果只检查每一小块的欧姆定律而略去界面，就仍可能拼出一个不守恒的假解。

**第15步：检查四条外边界，求新电压。**

由第9步，
$$
Q\boldsymbol K=(\psi_x,\psi_y)=\boldsymbol\nabla\psi.
$$
所以
$$
\boldsymbol E^\star=\frac{\boldsymbol\nabla\psi}{\kappa_0}
=-\boldsymbol\nabla u^\star,
\qquad
u^\star=\frac{I-\psi}{\kappa_0}.
$$
左边 $\psi=0$，右边 $\psi=I$，故
$$
u^\star(0,y)=\frac I{\kappa_0},
\qquad
u^\star(l,y)=0.
$$
两条原绝缘边现在成为等势电极，新端电压为
$$
U^\star=\frac I{\kappa_0}.
$$

原上、下电极上的 $u$ 沿 $x$ 不变，所以 $E_x=0$。而新电流的 $y$ 分量为 $K_y^\star=\kappa_0E_x$，因此新上、下边没有法向电流，成为绝缘边。图5-5把这一次边界交换与材料交换同时画出。

![图5-5 （a）原问题；（b）交换材料与边界后的对偶问题。](../figures/duality-05.png){width=83%}

图中不能仍把新上边标为电极。对偶问题的正电流由左流向右，和原问题由上流向下的方向不同。

**第16步：沿完整截面计算新总电流，不假定局部电流均匀。**

在任意竖直截面上，向右的新总电流为
$$
I^\star=\int_0^lK_x^\star(x,y)\,\mathrm dy.
$$
由 $K_x^\star=-\kappa_0E_y=\kappa_0u_y$，
$$
\begin{aligned}
I^\star
&=\kappa_0\int_0^l\frac{\partial u}{\partial y}\,\mathrm dy\\
&=\kappa_0[u(x,l)-u(x,0)]\\
&=\kappa_0U.
\end{aligned}
$$
中间使用了微积分基本定理；不需要 $u_y$ 在截面上为常数。新电阻为
$$
\begin{aligned}
R^\star
&=\frac{U^\star}{I^\star}
=\frac{I/\kappa_0}{\kappa_0U}\\
&=\frac1{\kappa_0^2}\frac IU
=\frac1{\kappa_0^2R}.
\end{aligned}
$$
从而得到有限板的端口对偶关系
$$
\boxed{RR^\star=\frac1{\kappa_1\kappa_2}}.
$$
到这一步仍没有令 $R^\star=R$；一般材料图案与一般外边界未必允许这样做。

**第17步：将新材料和边界与整体旋转后的原板逐点比较。**

把整个原问题绕板中心逆时针转 $90^\circ$，坐标映射为
$$
T(x,y)=(l-y,x),\qquad T^{-1}(x,y)=(y,l-x).
$$
原上边 $y=l$ 变为新左边 $x=0$，原下边变为新右边；原左右绝缘边分别变为新下、上绝缘边。电流方向由向下转为向右。

原来的左上材料 $1$ 变到左下，右下材料 $1$ 变到右上。因而旋转后，材料 $1$ 位于另一个对角，材料 $2$ 同样互换。对于本题四区，
$$
\kappa(T^{-1}(x,y))
=\frac{\kappa_1\kappa_2}{\kappa(x,y)}
=\kappa^\star(x,y).
$$
图5-5右的材料布局与电极边，正好同时等于这个整体旋转问题，而不是只在面积比例上相同。正方形旋转后区域本身不变，长度和厚度也不变。

**第18步：说明几何对应为什么足以推出新、旧电阻相等。**

对于正片电导和指定的完整电极、绝缘边，稳恒解在给定电极电势后唯一。若 $u_a,u_b$ 是两个解，取 $w=u_a-u_b$，则 $w$ 在两电极为零，且满足同样的守恒与绝缘条件。与第5步相同的分部积分给出
$$
\int_\Omega\kappa|\boldsymbol\nabla w|^2\,\mathrm dA=0.
$$
因 $\kappa>0$，只有 $\boldsymbol\nabla w=0$；再由电极上的零值可知 $w=0$。同一边界问题不能有两种不同的归一化电流分布。

整体旋转不改变电压与总电流之比。对偶问题的电压数值 $U^\star$ 可以与 $U$ 不同，但线性欧姆模型下，将整个电压乘一个常数，整个电流也乘同一个常数，电阻不变。因此
$$
R^\star=R.
$$
这不是预设有效导体“各向同性”，而是本题有限区域及端口的直接旋转对应。

**第19步：代入对偶关系，筛选正的物理解。**

第16步与第18步合并：
$$
R^2=\frac1{\kappa_1\kappa_2}
=\frac1{d^2\sigma_1\sigma_2}.
$$
代数上有正、负两个平方根，但被动导体耗散为正、$U$ 与 $I$ 取同一端口约定，所以 $R>0$。故
$$
\boxed{R=\frac1{d\sqrt{\sigma_1\sigma_2}}}.
$$
平方根必须同时覆盖两种电导率。不能写成 $1/(d\sigma_1\sqrt{\sigma_2})$，也不能漏掉厚度 $d$。

**第20步：将精确值与两条界作完整代数核对。**

用 $\kappa_i$ 表示，先比较下界：
$$
\begin{aligned}
R-\frac2{\kappa_1+\kappa_2}
&=\frac{\kappa_1+\kappa_2-2\sqrt{\kappa_1\kappa_2}}
{(\kappa_1+\kappa_2)\sqrt{\kappa_1\kappa_2}}\\
&=\frac{(\sqrt{\kappa_1}-\sqrt{\kappa_2})^2}
{(\kappa_1+\kappa_2)\sqrt{\kappa_1\kappa_2}}\ge0.
\end{aligned}
$$
再比较上界：
$$
\begin{aligned}
\frac{\kappa_1+\kappa_2}{2\kappa_1\kappa_2}-R
&=\frac{\kappa_1+\kappa_2-2\sqrt{\kappa_1\kappa_2}}
{2\kappa_1\kappa_2}\\
&=\frac{(\sqrt{\kappa_1}-\sqrt{\kappa_2})^2}
{2\kappa_1\kappa_2}\ge0.
\end{aligned}
$$
因此
$$
\boxed{
\frac2{d(\sigma_1+\sigma_2)}
\le\frac1{d\sqrt{\sigma_1\sigma_2}}
\le\frac{\sigma_1+\sigma_2}{2d\sigma_1\sigma_2}.
}
$$
两侧等号均且仅在 $\sigma_1=\sigma_2$ 成立。两种材料不同时，两条界同时严格，不沿用漏掉均匀特例的严格不等号。

**第21步：做量纲、尺度及退化极限检查。**

电导率单位为 $\mathrm{S/m}$，所以 $d\sqrt{\sigma_1\sigma_2}$ 的单位是 $\mathrm S$，其倒数为欧姆。若 $\sigma_1=\sigma_2=\sigma$，结果变为
$$
R=\frac1{d\sigma}
=\frac l{\sigma(dl)},
$$
恰是均匀方板沿两相对边导电的电阻。

边长 $l$ 消去，不是忘记了尺寸：所有平面长度共同缩放，路径长度与有效横向宽度共同缩放，方板的二维电导不变。设 $x=l\xi,\ y=l\eta$，场梯度带 $1/l$，面积带 $l^2$，功率积分中的两个长度因子正好抵消；厚度不参与这个平面缩放，故 $R\propto1/d$。

当 $\sigma_2\to0^+$、$\sigma_1$ 固定时，$R\to\infty$。两个 $\sigma_1$ 区只在中央一个点相遇，不能把零面积点接触当作具有有限截面的金属通道。该极限从严格正的电导率逼近；若直接设某区绝缘，先前正片电导的唯一性证明须另行处理退化，不能把极限中的每个中间步骤无条件照搬。

若改变外形、只用局部点电极或改变四区布局，图5-5的材料与边界对应可能消失。此时对偶关系仍可提供两个不同问题的联系，却不能只凭面积各半就继续使用本题精确值。

## 六、关键洞察

**洞察1：能求总电阻，不等于必须先求全部局部电势。**

本题的局部电势在材料界面折转，并在中央交点附近可能具有较强梯度，直接分区解拉普拉斯方程和全部边界很繁琐。对偶法不假造均匀电流，而是把每一个真实但未知的解转换成另一个真实解，再通过整体几何识别另一个问题的端口电阻。

所以“未知流线形状”不是本题缺少条件，也不是允许画任意流线的理由。精确端口值由完整方程和边界唯一性决定。解题图只要准确表示区域、界面连续及边界转换即可，不需要虚构已精确求出的全场分布。

**洞察2：保留电压、电流的手写归一化路线，可以得到同一结论。**

另一种归一化不预先选择 $\kappa_0$，而直接用未知 $R=U/I$ 构造
$$
\widehat{\boldsymbol E}=R\,Q\boldsymbol K,
\qquad
\widehat{\boldsymbol K}=\frac1R Q\boldsymbol E.
$$
其局部片电导为
$$
\widehat\kappa=\frac1{R^2\kappa}.
$$
重复第15、16步的端口积分，得到
$$
\widehat U=RI=U,\qquad
\widehat I=\frac UR=I.
$$
将这个横向问题再整体转回竖向，两个材料在位置上交换，转回后的片电导在每个原材料区均为原片电导的同一个比例：
$$
\begin{aligned}
\alpha
&=\frac{1/(R^2\kappa_2)}{\kappa_1}
=\frac{1/(R^2\kappa_1)}{\kappa_2}\\
&=\frac1{R^2\kappa_1\kappa_2}.
\end{aligned}
$$
在电极电压不变时，把所有片电导同乘 $\alpha$ 不改变归一化电势方程及其唯一解，但使电流同乘 $\alpha$。构造得到的新总电流又与原总电流相同，故
$$
\alpha I=I,\qquad I>0,
\qquad\alpha=1.
$$
于是 $R^2=1/(\kappa_1\kappa_2)$。这补足了“交换电势线和流线后，电流仍相同”的逻辑：相同的是构造及端口归一化后的总电流；不能在未验证电导率比例与边界前直接宣称所有对应点的电流密度都相同。

若使用体电流密度 $j$，归一化公式必须带 $d$；改用片电流后，$\widehat\kappa$ 的单位和尺度更清楚。两条归一化路线是同一个对偶变换的不同尺度选择，不是两个互相矛盾的物理模型。

**洞察3：加导体和切通道都可用最小耗散，但固定量不同。**

固定 $U$ 的电势原理与固定 $I$ 的电流原理都求一个正二次型的最小值，却分别对应 $U^2/R$ 与 $I^2R$。前者增大意味着 $R$ 减小，后者增大意味着 $R$ 增大。比较改造板时不说明端口固定量，是最容易把上下界颠倒的原因。

从离散电阻网络看，添加零电阻连接与删除导电连接分别是短接节点、删除支路，确有同样的单调性；连续薄板中的电势和电流变分给出它们的依据。改造板的中心短接或切缝必须在图中明确出现，不应拿改造后的两端电阻网络冒充原连续板。

原板的精确电阻还满足
$$
\sqrt{R_{\text{短}}R_{\text{切}}}
=\sqrt{\frac2{\kappa_1+\kappa_2}
\frac{\kappa_1+\kappa_2}{2\kappa_1\kappa_2}}
=\frac1{\sqrt{\kappa_1\kappa_2}}.
$$
它恰好是两个界的几何平均。但“在上下界之间”本身不能确定这个平均值；精确位置仍由对偶证明，不以漂亮的均值形式代替物理依据。

**洞察4：正方形外边界是精确值成立的一部分。**

无限周期材料的有效电导率与本题有限四块板的端口电阻并不是自动同一对象。本题直接建立了有限电极与绝缘边的对偶，并用方形的整体旋转识别新问题，避免借用没有验证外边界的宏观平均公式。

四区面积各半还不够。将同样两种材料改成水平层，电阻为串联平均；改成竖直条，电阻为并联平均。改变接触方式同样会改变端口场。方形棋盘、相对完整边电极及余边绝缘三项共同保证这次自对偶。

真实材料的有限界面接触电阻、很厚的板、局部引线电极或各向异性张量会引入新条件。此时并不是“对偶失效”的笼统理由，而是要逐项重验：局部本构能否按相同比例变换、界面通量是否连续、边界是否仍对应。

**洞察5：中心交点的局部梯度不应被强行当作有限常数。**

两种正的有限片电导使总耗散和端口电流有明确解，但中央四材料交点不必具有处处有界、光滑的电场。把连续电势与法向电流要求解释为“所有梯度在一点也必须相等”，会额外加入不成立的条件。

积分守恒、耗散与对偶关系可按分区积分和弱形式处理。交点附近用很小区域排除后取极限，或用有限能量的变分定义，都不需要给零面积交点安排独立电阻。独立有限元计算应保留真实分区界面，并通过网格加密检查总电流收敛，而不是以粗网格四电阻的输出证明精确公式。

数值计算中，由连续试探电势组成的有限元空间只是所有允许电势的子集，因此固定 $U$ 时离散功率从上方逼近真实功率，离散电阻从下方逼近真实电阻。误差不为零很正常；须同时核节点守恒、两端电流平衡和网格收敛，不能把已知的平方根结果写回计算电流再称为独立验证。

## 七、易错点

**1. 把前、后侧面误认成上、下大表面。** 本题电流主要在板面内，截面积含厚度 $d$；若电流穿过大表面，长度和截面积都会换成另一个问题。

**2. 四个小正方形一律赋值为 $1/(d\sigma_i)$。** 这个值属于完整等势电极、侧面绝缘的一维小块。原板内部界面通常不具备这些条件；只有图5-3改造后才可作相应网络化。

**3. 用两种材料的算术平均代替精确电导率。** 算术平均对应线性试探电势及下界，不是对原场的无条件精确计算。

**4. 忽略 $\sigma_1=\sigma_2$ 的等号。** 均匀板恰好达到两界，不应把 $R>$ 写成对所有正电导率均成立。

**5. 混用体电流密度、片电流和总电流。** $\boldsymbol j$、$\boldsymbol K=d\boldsymbol j$、$I=\int K_n\,\mathrm d\ell$ 的单位不同，漏掉一个厚度会破坏最终电阻量纲。

**6. 把 $\psi$ 误作另一种伏特单位的电势。** 电流函数差是安培，侧边 $\psi=I$ 不表示电流从侧边流出。

**7. 只交换两组曲线而不检查界面。** 新场的法向电流与切向电场必须连续；各块内部欧姆定律成立不足以构成整板真实解。

**8. 只交换材料，不交换电极和绝缘边。** 对偶问题由左向右导电，不能仍保持原上、下电极而直接令新、旧电阻相同。

**9. 省去对偶变换中的比例尺度。** 电场与片电流不能仅凭旋转直接相等，$\kappa_0$ 正是保证正确单位和两相交换的尺度。

**10. 负号由图上箭头临时猜定。** 以 $Q(v_x,v_y)=(-v_y,v_x)$ 固定取向，再推导 $u^\star=(I-\psi)/\kappa_0$；原电流向下对应新电流向右。

**11. 将相同电阻误读为相同电压或逐点相同场。** 对偶端口电压、电流分别为 $I/\kappa_0$ 与 $\kappa_0U$，它们一般不等于原值。比较的是线性端口比值。

**12. 由平方关系取负根。** 被动导体的正耗散筛出正电阻；数学平方根的另一个符号不是可选物理解。

**13. 把边长消去解释成任何外形都不影响电阻。** 仅是相似平面缩放不影响；改变长宽比、材料位置和电极长度会改变问题。

**14. 将两个导电区的点接触当作有限宽的导线。** 当另一材料趋于绝缘时，单点没有有限导电横截面，不能得到有限直流电流通道。

**15. 变分比较不交代固定端口量。** 固定电压的真实功率最小与固定电流的真实功率最小用于不同试探变量，不可随意互换电阻比较方向。

**16. 用粗网格误差否认连续对偶结果，或把误差隐藏。** 中央交点可能导致慢收敛。必须比较真实计算的多个网格，并报告离散误差和守恒残差，不将离散结果替换成已知公式。

## 八、课堂讲解建议

先让学生在三维题图中确认贴电极的两个侧面，再展开成板面图。板书同时写出 $u$、$\boldsymbol j$、$\boldsymbol K$、$I$ 的单位，特别指出两个大表面不是电极。前几步若不先澄清研究对象，后续所有漂亮代数都可能在求另一种电阻。

课堂可先给出“四块分别算电阻”的常见想法，再要求学生标出每块所谓两端的等势依据和另外两边的绝缘依据。学生通常会发现这两项都不能从原图推出。随后在图5-3上实际画出新增的短接线和切缝，说明串、并联计算并非完全错误，而是它准确描述了被改造的两个问题。

教师应把上下界比较与端口控制量放在同一板书行中：固定电压写 $P=U^2/R$，固定电流写 $P=I^2R$。不必先要求学生记忆变分原理名称，但要展开二次型、说明交叉项为何为零；这样可以把边界、电流守恒和分部积分关联起来。第6步的线性试探场还可用于独立检查比较方向。

引入电流函数时，先在水平截面写出 $I=-\int K_y\,\mathrm dx$，再由它确定 $\psi$ 左右边界。学生要看见为什么一个安培单位的标量可以编码流线，而不是把它误作第二种电势。可用一小流管核对 $j\,d\,\mathrm d\ell=\mathrm d\psi$，随后把这种微元图像升级为矩阵旋转，保留取向和比例。

对偶部分的课堂重点是四项逐格核对，不是直接宣布几何平均。板书按“局部本构、守恒方程、界面条件、外边界”列四栏，最后才画整体旋转后的棋盘。两个系统的端口积分必须完整写出，尤其是新电流来自电势沿竖直截面的净变化，而非局部均匀假定。

可提出两个有明确答案的引导问题：若只有四区面积各半，但改成水平层，是否还有本题平方根结果？答案是否，因为材料及外边界不再有同一对偶旋转关系。若整体板边长加倍而厚度不变，为什么电阻不变？答案是长度与横向宽度同时加倍，或功率积分的平面尺度因子消去。两问都能由本题已经推导的关系作答，不留下未解自测凑篇幅。

最后由学生分别完成均匀极限、两条界、量纲和零电导率极限，教师核对时强调这四种检查各发现不同错误。有限元演示只作为独立数值复核，须说明每个网格的误差，不用动画流线的视觉效果取代守恒及端口计算。

## 九、变式训练

**变式1：数值、发热与相似尺寸变化。**

题：保持本题的材料布局和完整边电极，取 $d=1.0\,\mathrm{mm}$、$l=0.10\,\mathrm m$、$\sigma_1=4.0\times10^6\,\mathrm{S/m}$、$\sigma_2=1.0\times10^6\,\mathrm{S/m}$。两电极电压为 $U=1.0\,\mathrm{mV}$。求电阻、总电流、焦耳功率及两界；再求边长加倍或厚度加倍时的变化。

解：先全部换为国际单位，
$$
d=10^{-3}\,\mathrm m,\qquad U=10^{-3}\,\mathrm V.
$$
两种电导率的几何平均为
$$
\sqrt{\sigma_1\sigma_2}
=\sqrt{4.0\times10^{12}}=2.0\times10^6\,\mathrm{S/m}.
$$
因此
$$
\begin{aligned}
R&=\frac1{10^{-3}\times2.0\times10^6}
=5.0\times10^{-4}\,\Omega,\\
I&=\frac{10^{-3}}{5.0\times10^{-4}}=2.0\,\mathrm A,\\
P&=UI=2.0\times10^{-3}\,\mathrm W.
\end{aligned}
$$
下界为
$$
R_{\text{短}}
=\frac2{10^{-3}(5.0\times10^6)}
=4.0\times10^{-4}\,\Omega.
$$
上界为
$$
R_{\text{切}}
=\frac{5.0\times10^6}
{2\times10^{-3}\times4.0\times10^{12}}
=6.25\times10^{-4}\,\Omega.
$$
确有 $0.400<0.500<0.625$，这里三个数的单位均为毫欧；若漏写单位，容易把毫伏与伏混用。

边长加倍、厚度不变，仍为相似方板，$R,I,P$ 均不变。厚度加倍、电压不变时，$R$ 减半、$I$ 加倍、$P$ 加倍。若改为固定总电流，厚度加倍反而使 $P=I^2R$ 减半；不能把固定电压的功率变化照搬到固定电流。

**变式2：弱反差展开和两个材料的灵敏度。**

题：令 $\sigma_1=\sigma_0(1+\varepsilon)$、$\sigma_2=\sigma_0(1-\varepsilon)$，$|\varepsilon|<1$。求 $R$ 关于 $\varepsilon$ 的四阶展开，并比较两界。另求一相电导率小幅变化而另一相不变时的相对电阻变化。

解：两相乘积为 $\sigma_0^2(1-\varepsilon^2)$，记 $R_0=1/(d\sigma_0)$，
$$
R=R_0(1-\varepsilon^2)^{-1/2}.
$$
使用二项式展开至 $\varepsilon^4$，
$$
(1-z)^{-1/2}=1+\frac12z+\frac38z^2+O(z^3),
\qquad z=\varepsilon^2,
$$
所以
$$
\boxed{R=R_0\left(1+\frac12\varepsilon^2
+\frac38\varepsilon^4+O(\varepsilon^6)\right)}.
$$
没有一次项是因为交换材料等同于 $\varepsilon\mapsto-\varepsilon$，电阻应为偶函数，不只是展开中的偶然抵消。

下界与上界分别为
$$
\begin{aligned}
R_{\text{短}}&=R_0,\\
R_{\text{切}}&=\frac{R_0}{1-\varepsilon^2}
=R_0(1+\varepsilon^2+\varepsilon^4+O(\varepsilon^6)).
\end{aligned}
$$
非均匀性引起的真实首项增量为 $\frac12R_0\varepsilon^2$，介于两个改造板的首项增量之间。这个弱反差结果不能用于 $|\varepsilon|$ 接近 $1$ 的强反差极限，那里要使用完整根式。

对精确公式取对数并微分：
$$
\ln R=-\ln d-\frac12\ln\sigma_1-\frac12\ln\sigma_2,
$$
$$
\frac{\mathrm dR}{R}
=-\frac{\mathrm dd}{d}
-\frac12\frac{\mathrm d\sigma_1}{\sigma_1}
-\frac12\frac{\mathrm d\sigma_2}{\sigma_2}.
$$
厚度和另一材料不变时，某一电导率增加 $1\%$，电阻一阶近似降低 $0.5\%$。若两相同时按同一比例增加，电阻按该比例的倒数变化，不把单相的半系数用于整体同乘。

**变式3：面积比例相同，但改成层状和条状材料。**

题：仍有各占一半面积的 $\sigma_1,\sigma_2$，厚度与方形尺寸不变，电极仍在前、后完整边。分别把材料排成上下两个水平层、左右两个竖直条，求电阻并与棋盘形比较。

解：上下水平层垂直于主要电流方向。每层路长 $l/2$、截面积 $dl$，所以
$$
R_{1,\text{层}}=\frac1{2d\sigma_1},
\qquad
R_{2,\text{层}}=\frac1{2d\sigma_2}.
$$
两层串联，
$$
R_{\text{层}}=\frac{\sigma_1+\sigma_2}{2d\sigma_1\sigma_2}
=R_{\text{切}}.
$$
这里横向界面可以成为等势面，由全宽电极、沿 $x$ 均匀的分布和唯一性保证；两层电场一般不同，但法向电流相同。

左右竖条平行于电流方向，每条路长 $l$、截面积 $d(l/2)$，所以
$$
R_{1,\text{条}}=\frac2{d\sigma_1},
\qquad
R_{2,\text{条}}=\frac2{d\sigma_2}.
$$
两条跨在同一对电极间，并联电导为
$$
G_{\text{条}}=\frac{d\sigma_1}2+\frac{d\sigma_2}2,
$$
从而
$$
R_{\text{条}}=\frac2{d(\sigma_1+\sigma_2)}
=R_{\text{短}}.
$$
其纵向界面没有法向电流，线性竖直电势是真实解。不能只因“并排”就判并联，必须核对完整端口电压和零横向流量。

故
$$
R_{\text{条}}\le R_{\text{棋盘}}\le R_{\text{层}},
$$
两相不同则严格。三种结构有完全相同的厚度、两相和面积比例，却有不同电阻，证明几何和边界不能由一个面积平均数取代。

**变式4：矩形棋盘只能确定互补长宽比的电阻乘积。**

题：将板面改为宽 $W$、高 $H$ 的矩形，仍由两条中线分成四块，左上与右下为 $\kappa_1$、另两块为 $\kappa_2$；电极在完整上、下边，左右绝缘。记长宽比 $a=W/H$ 时的竖向电阻为 $R(a)$。证明 $R(a)R(1/a)=1/(\kappa_1\kappa_2)$，并说明为何不能分别断定两者等于 $1/\sqrt{\kappa_1\kappa_2}$。

解：第12—16步的场旋转、界面检查和端口积分不要求正方形。新问题仍在同一个矩形内，但电极变为左右边，材料交换。把这个新问题整体转 $90^\circ$ 后，外形成为宽 $H$、高 $W$，电极恢复为上、下边，材料布局也恢复为原规定的两个对角。平面统一尺度不影响电阻，旋转问题可用互补长宽比 $1/a$ 表示。因此先写端口对偶，再识别旋转问题，最后将两式比较并乘以 $R(a)$，完整计算为
$$
\begin{aligned}
R^\star(a)&=\frac1{\kappa_1\kappa_2R(a)},\\
R^\star(a)&=R(1/a),\\
R(a)R(1/a)&=\boxed{\frac1{\kappa_1\kappa_2}}.
\end{aligned}
$$
矩形在 $90^\circ$ 旋转后不是原来的同一区域，两个长宽比不同，因此没有 $R(a)=R(1/a)$ 的依据。

最直接的反例是 $\kappa_1=\kappa_2=\kappa$。此时
$$
R(a)=\frac H{\kappa W}=\frac1{\kappa a},
\qquad
R(1/a)=\frac a\kappa.
$$
乘积恰为 $1/\kappa^2$，但当 $a\ne1$ 时两者不等。对偶只能给乘积，正方形才额外给相等。

两条试探界也保留形状因子：
$$
\frac1a\frac2{\kappa_1+\kappa_2}
\le R(a)\le
\frac1a\frac{\kappa_1+\kappa_2}{2\kappa_1\kappa_2}.
$$
这是以 $v=Uy/H$ 和 $\boldsymbol K_{\text{试}}=(0,-I/W)$ 分别积分得到的，不是把方板精确式简单乘 $H/W$。非均匀矩形的实际场仍取决于长宽比，不能从这两个界制造不存在的通用精确值。

<!-- draft-content-complete: 014 question 05; 21 core steps, 4 fully solved variations; finite boundary duality, not unverified homogenization -->
