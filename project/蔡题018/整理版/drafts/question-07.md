# 第7题

<!-- question-start -->

假设太阳为黑体，温度为$T_S$，半径为$R_S$，地球到太阳的距离为$r_E$。在地球轨道附近，垂直于阳光方向放置一个半径为$r$、焦距为$f$的理想透镜。在焦点附近放置一个导热良好的球形小黑体（修订：补充球形条件），其热平衡温度为$T_B$。

（1）求$T_B$可能达到的最高值。

（2）仅通过改变这个透镜的形状，是否可能使$T_B>T_S$？

（3）如果允许使用任意器件，是否可能使$T_B>T_S$？器件自身的状态和熵均不得随时间改变。若可能，请举例；若不可能，请说明理由。

![图7-1 太阳的有限角宽、透镜与焦区球形小黑体的空间位置。](../figures/question-07.png){width=90%}

<!-- question-end -->

## 一、题型定位

本题连接几何光学、热辐射和热力学第二定律。第一问不是把所有阳光集中到一个没有大小的数学点，而是计算有限角宽太阳在像面形成的照明区域，再比较受热物体吸收和散热的功率。第二问讨论被动光学的极限，第三问允许把太阳能先变成功再用于加热，不能混为一谈。

题干修订说明：补充球形条件，以明确受热物体的几何模型。吸收功率取决于沿来光方向的投影面积，散热功率取决于辐射表面积，因此形状影响第一问的系数。主解按题干的球形小黑体计算；随后将形状改为薄圆片，作为模型对照。黑体是一种辐射性质，不是球形的同义词。

## 二、知识点

温度为$T$的黑体，单位表面的总辐射功率称为辐射出射度，等于$\sigma T^4$，$\sigma$是斯忒藩—玻尔兹曼常量。面积为$A$、温度统一的黑表面向外辐射功率为$A\sigma T^4$；这个表面积不同于沿来光方向的投影面积。

辐照度$E$是单位面积接收的入射功率。辐亮度$L$还区分方向：对投影面积$\mathrm dA_\perp$及方向立体角$\mathrm d\Omega$，功率微元是$L\,\mathrm dA_\perp\,\mathrm d\Omega$。黑体遵从朗伯角分布，辐亮度$L=\sigma T^4/\pi$，其中$\pi$来自向外半球的方向积分。

远处太阳的角半径近似为$\theta_S=R_S/r_E$，近轴透镜把这一角宽映射为像面半径$a\simeq f\theta_S$。太阳像是二维圆盘，面积$\pi a^2$，不是向四面辐射的小球。

能量稳态和熵稳态分别要求器件不持续积累能量和熵，但允许这些量流过器件。热机必须同时写能量与熵的收支，不能仅凭能量守恒判断热流能否全部转化为功。

## 三、物理图像

太阳中心与太阳边缘发来的光方向略有不同。中心方向形成轴上像，边缘方向形成偏离光轴的像；所有太阳表面点的像组成一个圆盘，不是同一个焦点。导热良好只使受热物体自身接近均匀温度，不会消除太阳像的有限面积。

球远小于太阳像且位于其内部时，整个迎光投影都处于均匀焦区照明内。背面虽然不直接接受近轴阳光，也因导热而升温并辐射。吸收按一个圆的投影计算，散热按整个球面计算，产生球形模型的面积比$1/4$。

透镜重排光线的位置和方向，不增加太阳本身的黑体辐亮度。增大孔径可使更多方向带来太阳辐射，但方向立体角有限。把近轴公式外推到任意大的$r/f$，算出的超高温已经不属于原来的近轴模型。

主动器件可以在太阳与冷环境之间提取功，再让电功在小球内耗散为热。功不是温度为$T_S$的热流，电炉因此可以维持更高温度，但整个装置仍须向外界排出熵。

## 四、解题入口

主解明确取半径$b$的球形小黑体，$b\ll a$；太阳和透镜满足$r_E\gg R_S$、$r_E\gg f$，主计算采用$r/f\ll1$的近轴模型，忽略环境和透镜自身回辐射。理想无损透镜排除吸收损失，良好导热使球温统一。球与像区尺寸接近时，必须重新计算非均匀照明和遮挡，不能继续使用一个统一的$E\pi b^2$。

先求透镜收集功率，再求太阳圆像面积，由此得像面辐照度。通过球面投影和完整表面积积分建立热平衡。随后另从辐亮度和立体角重算温度，交叉检验面积系数并给出实际光锥表达式。

第二问用被动、互易的灰体交换模型解释上限，并说明适用范围。第三问加入热机、冷源与电炉，核对能量、熵和长期稳态；不能用不断耗尽的电池满足“器件自身状态不变”。

## 五、解析

（1）明确研究对象及形状条件。

图7-1用分段距离表示$r_E$与$f$，不按同一比例；太阳的$R_S$、透镜的$r$与受热物体尺寸也不同。主解将受热物体取为半径$b$的小球，$b$用于追踪两个面积，最后从温度式约去。

修订后的题干已明确球形；下面第一问的温度式还须满足近轴、小尺寸及暗背景条件，不能外推到任意孔径或任意大小的球。热平衡要求整个球的总入射功率等于总出射功率，不要求每一球面点局部吸收与辐射相等；导热在各区域之间输送能量。

（2）从太阳表面求透镜处辐照度。

太阳表面积为$4\pi R_S^2$，总辐射功率
$$
P_S=4\pi R_S^2\sigma T_S^4.
$$
这些能量在远处均匀通过半径$r_E$的球面。忽略透镜尺寸相对于$r_E$的差别，垂直于径向光线的接收面辐照度为
$$
\begin{aligned}
E_E&=\frac{P_S}{4\pi r_E^2}\\
&=\frac{4\pi R_S^2\sigma T_S^4}{4\pi r_E^2}
=\sigma T_S^4\frac{R_S^2}{r_E^2}.
\end{aligned}
$$
两个$4\pi$来自太阳总表面积与传播球面，并在这一步相约。不能因此在后面又把圆像面积写成球面面积。量纲上$\sigma T_S^4$和$E_E$都是功率除以面积，$R_S^2/r_E^2$是无量纲稀释比例。

（3）计算透镜收集功率。

透镜迎光圆孔面积是$\pi r^2$。透镜平面垂直于太阳中心光线，太阳角宽很小，可忽略各来光方向的余弦差别，故
$$
\begin{aligned}
P_L&=E_E\pi r^2\\
&=\pi r^2\sigma T_S^4\frac{R_S^2}{r_E^2}.
\end{aligned}
$$
理想无损透镜只重排光线，传到像区的总功率仍是$P_L$。焦距改变的是已收集光能的分布，不是在入口处产生新能量。

（4）建立太阳圆像的几何关系。

图7-2上半是含光轴的截面，太阳中心和边缘两个方向形成不同像点；下半把像盘与小球的前后位置用空间投影表示。像盘是平面，球是三维物体。

![图7-2 太阳边缘光线的像高、平面圆像与小球尺度。](../figures/image-07.png){width=85%}

图中太阳角半径$\theta_S$满足
$$
\begin{aligned}
\sin\theta_S&=\frac{R_S}{r_E},\\
\theta_S&\simeq\frac{R_S}{r_E},\\
a&\simeq f\tan\theta_S\simeq f\theta_S
=\frac{fR_S}{r_E}.
\end{aligned}
$$
此处使用小角近似$\sin\theta\simeq\tan\theta\simeq\theta$。若保留有限物距的近轴薄透镜关系，像距$q$满足
$$
\begin{aligned}
\frac1f&=\frac1{r_E}+\frac1q,\\
q&=\frac{fr_E}{r_E-f},\\
a&=\frac{qR_S}{r_E}
=\frac{fR_S}{r_E-f}.
\end{aligned}
$$
$f/r_E\ll1$时$q\simeq f$，回到焦区像半径。这个修正仍属于近轴成像，不是任意大孔径无像差成像的证明。太阳表面辐亮度一致，忽略近轴像面渐晕后，圆像内部照明近乎均匀。

（5）把功率除以正确的像面面积。

图7-2中的二维圆盘面积为
$$
A_{\mathrm{im}}=\pi a^2
=\pi\frac{f^2R_S^2}{r_E^2}.
$$
于是
$$
\begin{aligned}
E_{\mathrm{im}}
&=\frac{P_L}{A_{\mathrm{im}}}\\
&=\frac{\pi r^2\sigma T_S^4R_S^2/r_E^2}
{\pi f^2R_S^2/r_E^2}\\
&=\sigma T_S^4\frac{r^2}{f^2}.
\end{aligned}
$$
太阳半径与距离约去，是因为较远的太阳既使入口更暗，也使太阳像同比例缩小。集光功率和像面积都含$R_S^2/r_E^2$，局部辐照度中这一比例抵消。若太阳像与衍射斑或球尺寸接近，仍不能忽略这些尺度约束。

不能除以$4\pi a^2$，因为太阳像不是三维发光球。此处多除一次$4$，再在热平衡使用球的投影与表面积比$1/4$，就是混淆了两个不同几何对象。

（6）通过球面投影积分求吸收截面。

图7-3中球面法向与朝向光源的方向夹角为$\vartheta$。各处吸收功率密度因入射角不同而不同，黑体吸收率仍为一；导热使球温相同，迎光半球的真实面积不能直接当成投影。

![图7-3 球面迎光投影、面元法向与完整散热表面。](../figures/projection-07.png){width=80%}

球面真实面积微元和迎光投影为
$$
\mathrm dS=b^2\sin\vartheta\,\mathrm d\vartheta\,\mathrm d\phi,
\qquad
\mathrm dA_\perp=\cos\vartheta\,\mathrm dS.
$$
只积分$0\le\vartheta\le\pi/2$的迎光半球：
$$
\begin{aligned}
A_{\mathrm{proj}}
&=\int_0^{2\pi}\int_0^{\pi/2}
b^2\cos\vartheta\sin\vartheta\,
\mathrm d\vartheta\,\mathrm d\phi\\
&=2\pi b^2\left[\frac12\sin^2\vartheta\right]_0^{\pi/2}
=\pi b^2.
\end{aligned}
$$
先对极角再对方位角积分，得到圆盘投影，而非半球面积$2\pi b^2$。在$b\ll a$且$r/f\ll1$时，整个投影处于均匀焦区照明内，
$$
P_{\mathrm{abs}}
=E_{\mathrm{im}}\pi b^2
=\pi b^2\sigma T_S^4\frac{r^2}{f^2}.
$$

（7）计算完整球面散热并求温度。

完整表面积需要对全部极角积分：
$$
\begin{aligned}
A_B&=\int_0^{2\pi}\int_0^\pi
b^2\sin\vartheta\,\mathrm d\vartheta\,\mathrm d\phi\\
&=2\pi b^2[-\cos\vartheta]_0^\pi=4\pi b^2.
\end{aligned}
$$
忽略暗环境回辐射，$P_{\mathrm{em}}=4\pi b^2\sigma T_B^4$。无其他传热时，稳态为$P_{\mathrm{abs}}=P_{\mathrm{em}}$，逐项约去正数：
$$
\begin{aligned}
\pi b^2\sigma T_S^4\frac{r^2}{f^2}
&=4\pi b^2\sigma T_B^4,\\
T_B^4&=\frac{r^2}{4f^2}T_S^4,\\
\frac{T_B}{T_S}
&=\left(\frac{r^2}{4f^2}\right)^{1/4}
=\frac1{\sqrt2}\sqrt{\frac rf}.
\end{aligned}
$$
取温度的非负实根，得到球形近轴小尺寸模型的第一问：
$$
\boxed{T_{B,\max}=T_S\sqrt{\frac{r}{2f}}}.
$$
$b$约去，因为吸收与辐射均正比于$b^2$。有附加导热损失、有限尺寸遮挡时，同样约消并不保证同一温度。这个温度比把圆像误写为球面积所得温度大$\sqrt2$；差别是明确的面积错误，不是舍入。

（8）理解焦区最高温位置与平衡稳定性。

球置于太阳圆像内部、远离像盘边缘时，可接收完整的均匀近轴照明。偏离像面会让同一太阳点的光散成更大光斑；靠近或超出像区边缘会失去部分来光方向。不能通过寻找一个“更精确的焦点”，把扩展太阳源变成无面积点源。

若球总热容为$C_B>0$，固定入射功率下
$$
C_B\frac{\mathrm dT}{\mathrm dt}
=P_{\mathrm{abs}}-4\pi b^2\sigma T^4.
$$
令$T=T_B+\delta T$，一阶展开
$$
(T_B+\delta T)^4=T_B^4+4T_B^3\delta T+O(\delta T^2).
$$
利用平衡功率相消，得
$$
\frac{\mathrm d(\delta T)}{\mathrm dt}
=-\frac{16\pi b^2\sigma T_B^3}{C_B}\delta T.
$$
系数为负，略冷则净吸热、略热则净散热，扰动衰减。热平衡温度不是零热容物体瞬间达到的温度；此处没有假定热容消失。

（9）独立建立黑体辐亮度。

对面积$\mathrm dA$的表面，出射方向与外法向夹角$\vartheta$，朗伯辐亮度$L_S$不随方向改变：
$$
\begin{aligned}
\mathrm dP
&=\mathrm dA\int_0^{2\pi}\int_0^{\pi/2}
L_S\cos\vartheta\sin\vartheta\,
\mathrm d\vartheta\,\mathrm d\phi\\
&=\pi L_S\,\mathrm dA.
\end{aligned}
$$
与$\sigma T_S^4\,\mathrm dA$比较，
$$
L_S=\frac{\sigma T_S^4}{\pi}.
$$
它的单位含立体角，不能把$L_S$当成$E_{\mathrm{im}}$。无损被动真空成像保持辐亮度，不能把多个同温光线方向无限叠入同一光学模式，获得更高的黑体辐亮度。

（10）从空间入射光锥求球的吸收。

图7-4从球看见透镜圆孔，圆孔与球心形成有前后关系的三维光锥。实际填充的半角是$\alpha$，立体角是$\Omega$；它不是平面扇形面积。

![图7-4 小球看见的孔径光锥与方向立体角。](../figures/cone-07.png){width=85%}

方向微元$\mathrm d\Omega=\sin\vartheta\,\mathrm d\vartheta\,\mathrm d\phi$，故
$$
\begin{aligned}
\Omega&=\int_0^{2\pi}\int_0^\alpha
\sin\vartheta\,\mathrm d\vartheta\,\mathrm d\phi\\
&=2\pi[-\cos\vartheta]_0^\alpha
=2\pi(1-\cos\alpha).
\end{aligned}
$$
球对每个方向都有投影$\pi b^2$，方向旋转不改变这个积分。若整个光锥被太阳辐亮度填充，
$$
\begin{aligned}
P_{\mathrm{abs}}
&=\int_\Omega L_S\pi b^2\,\mathrm d\Omega
=L_S\pi b^2\Omega\\
&=\sigma T_S^4b^2\Omega.
\end{aligned}
$$
与完整球面出射功率平衡：
$$
\boxed{\frac{T_B^4}{T_S^4}
=\frac{\Omega}{4\pi}
=\frac{1-\cos\alpha}{2}}.
$$
图中的理想孔径—焦点几何可给$\tan\alpha=r/f$，但“大孔径仍无像差且光锥均匀填满”是额外条件。没有该条件，应使用实际$\alpha$和实际被照亮方向，不能只凭焦距宣称全部几何孔径方向均已填满。

（11）检验近轴极限并阻止越界外推。

余弦小角展开至四阶：
$$
\begin{aligned}
\cos\alpha&=1-\frac{\alpha^2}{2}
+\frac{\alpha^4}{24}+O(\alpha^6),\\
\frac{1-\cos\alpha}{2}
&=\frac{\alpha^2}{4}
-\frac{\alpha^4}{48}+O(\alpha^6).
\end{aligned}
$$
$\alpha\simeq r/f$时，最低阶给$T_B^4/T_S^4\simeq r^2/(4f^2)$，正好核对圆像与球面投影路线，而非只把结果代回自身。

一侧透镜最多提供半球方向，$\alpha\le\pi/2$。另一半球暗时，球形模型满足
$$
\frac{T_B^4}{T_S^4}\le\frac12,\qquad
T_B\le2^{-1/4}T_S<T_S.
$$
若用反射腔等被动装置从更多方向提供同样辐亮度，最多覆盖$4\pi$，球温也只能趋于$T_S$。单透镜的$2^{-1/4}$与一般被动装置的$1$是不同覆盖范围的上限。近轴式在$r/f>2$时形式上给超温，但已违反$r/f\ll1$，不是可实现方案。

（12）比较改变受热物体形状的模型。

把小球改成导热良好、两面均黑、边缘面积可忽略的薄圆片，法向沿近轴来光，记一面面积$A$。投影面积$A$，散热面积近似$2A$：
$$
\begin{aligned}
P_{\mathrm{abs}}&=AE_{\mathrm{im}},\\
P_{\mathrm{em}}&=2A\sigma T_{\mathrm{plate}}^4,\\
T_{\mathrm{plate}}^4
&=\frac{E_{\mathrm{im}}}{2\sigma}
=\frac{r^2}{2f^2}T_S^4,\\
T_{\mathrm{plate}}
&=2^{-1/4}T_S\sqrt{\frac rf}.
\end{aligned}
$$
因此
$$
\frac{T_{\mathrm{plate}}}{T_{B,\mathrm{sphere}}}
=\left(\frac{1/2}{1/4}\right)^{1/4}=2^{1/4}.
$$
两物体均是导热良好的小黑体，温度却不同。一般近轴小物体应保留
$$
T^4=\frac{A_{\mathrm{proj}}}{A_{\mathrm{em}}}
\frac{r^2}{f^2}T_S^4.
$$
球形题干对应面积比$1/4$；薄圆片对应另一个面积比，属于改变物体形状后的模型，不是本题第一问的另一答案。这个对照说明球形条件不能省略，但不改变第二问的被动限制和第三问的主动稳态可能性。

（13）以互易交换说明第二问。

图7-5把太阳$S$、小球$B$、冷背景$C$分开，$T_C<T_S$。每条双向连接代表正反向辐射路径，不能只保留太阳到球而漏掉球返回太阳的辐射。

![图7-5 被动互易辐射路径的热源、小球与冷背景。](../figures/passive-07.png){width=80%}

对灰体、几何不随温度改变的被动系统，令从$S$到$B$功率为$C_{SB}T_S^4$，反向为$C_{BS}T_B^4$。互易性和等温平衡给
$$
C_{SB}=C_{BS}\ge0,\qquad C_{CB}=C_{BC}\ge0.
$$
同温时若仍有单向净热交换，会在无其他改变时制造温差，与被动平衡不相容。球的平衡为
$$
\begin{aligned}
C_{BS}T_S^4+C_{BC}T_C^4
&=(C_{BS}+C_{BC})T_B^4,\\
T_B^4&=\frac{C_{BS}T_S^4+C_{BC}T_C^4}
{C_{BS}+C_{BC}}.
\end{aligned}
$$
分母为正，这是非负权重平均。直接求差：
$$
\begin{aligned}
T_S^4-T_B^4&=\frac{C_{BC}(T_S^4-T_C^4)}
{C_{BS}+C_{BC}}\ge0,\\
T_B^4-T_C^4&=\frac{C_{BS}(T_S^4-T_C^4)}
{C_{BS}+C_{BC}}\ge0.
\end{aligned}
$$
故$T_C\le T_B\le T_S$；两连接均非零且冷热不同，则两端严格。改透镜形状只改变被动几何，不制造负交换权重或功源，所以第二问不能。

若系统频率选择性明显，不能对所有温度都写成同一常数$C$乘$T^4$，应逐频率积分。但被动模态辐亮度不能高于热源的限制仍在。这里的灰体式说明机制，不冒充一切滤光器的通式。

（14）区分自身熵恒定与不能排熵。

对第三问的开放稳态装置，热端温度$T_H$、冷端温度$T_C$，吸热率$\dot Q_H$、排热率$\dot Q_C$与输出功率$\dot W$满足
$$
\frac{\mathrm dU_{\mathrm{dev}}}{\mathrm dt}
=\dot Q_H-\dot Q_C-\dot W=0.
$$
熵收支还含产生项：
$$
\begin{aligned}
\frac{\mathrm dS_{\mathrm{dev}}}{\mathrm dt}
&=\frac{\dot Q_H}{T_H}
-\frac{\dot Q_C}{T_C}
+\dot S_{\mathrm{gen}}=0,\\
\dot S_{\mathrm{gen}}
&=\frac{\dot Q_C}{T_C}
-\frac{\dot Q_H}{T_H}\ge0.
\end{aligned}
$$
自身熵不变表示流入、流出、产生相抵，不表示三个都为零，也不表示外界熵不变。机械功或电功不以$\dot W/T$携带热流熵，不能把功直接塞进热流项。

（15）建立太阳热机与电炉的稳态例子。

图7-6区分吸热、排热、功：太阳持续给集热器供能，$T_H$可低于$T_S$；冷环境接收排热，电炉将功耗散于球。三个连接缺一不可，不能换成不断耗尽的电池。

![图7-6 太阳供能、冷源排熵与电功加热小球的稳态装置。](../figures/engine-07.png){width=90%}

令$\eta=\dot W/\dot Q_H$，能量方程给$\dot Q_C=(1-\eta)\dot Q_H$。代入熵产生率：
$$
\begin{aligned}
\frac{(1-\eta)\dot Q_H}{T_C}
-\frac{\dot Q_H}{T_H}&\ge0,\\
\frac{1-\eta}{T_C}&\ge\frac1{T_H},\\
\eta&\le1-\frac{T_C}{T_H}.
\end{aligned}
$$
这是热边界$T_H,T_C$的卡诺效率上限。太阳辐射被集热器吸收成较低温热流时可另有不可逆损失，并不允许热机超出此上限。

电炉的功补偿暗环境中小球散热：
$$
\dot W=4\pi b^2\sigma T_B^4,\qquad
T_B=\left(\frac{\eta\dot Q_H}{4\pi b^2\sigma}\right)^{1/4}.
$$
有足够集热面积时，可选择足够小而黑体/连续介质模型仍有效的球，使$T_B>T_S$。能量来自热机的功，而非透镜增大太阳辐亮度；这就是第三问可行的主动方案。

（16）核对数值例子及唯一热库的相反限制。

选$T_S=6000\,\mathrm K$、$T_H=2000\,\mathrm K$、$T_C=300\,\mathrm K$，$\dot Q_H=200\,\mathrm W$、$\eta=0.70$。这些数字只是存在性例子，不是原题新增已知量：
$$
\begin{aligned}
\eta_{\mathrm{Carnot}}&=1-\frac{300}{2000}=0.85,\\
\dot W&=0.70\times200=140\,\mathrm W,\\
\dot Q_C&=200-140=60\,\mathrm W,\\
\dot S_{\mathrm{gen}}
&=\frac{60}{300}-\frac{200}{2000}
=0.10\,\mathrm{W/K}>0.
\end{aligned}
$$
效率低于卡诺限，能量、熵都合格。取$T_B=7000\,\mathrm K>T_S$，由球面辐射求所需半径：
$$
\begin{aligned}
b^2&=\frac{140}{4\pi\sigma(7000)^4},\\
(7000)^4&=2.401\times10^{15},\\
\sigma&=5.670374419\times10^{-8}\,
\mathrm{W/(m^2K^4)},\\
b&\simeq2.86060\times10^{-4}\,\mathrm m
=0.286060\,\mathrm{mm}.
\end{aligned}
$$
代回$4\pi b^2\sigma T_B^4=140\,\mathrm W$，与电功相符。这个尺寸远大于高温热辐射典型波长。材料耐温与损耗限制实际实现，但不改变理想题的热力学可能性；电炉产生并向外排熵，自身状态仍可稳态。

若只允许唯一$T_S$热库，没有冷源、外功或其他熵出口，就不能套用该方案。将$Q>0$从$T_S$单独送往更热的$T_B$，循环器件自身不变，两个热边界的总熵变
$$
\Delta S=-\frac Q{T_S}+\frac Q{T_B}<0
\qquad(T_B>T_S).
$$
在没有其他变化时违反第二定律。第三问的主动可能性依赖持续供能与外排熵，不是第二定律失效。第一问的形状条件、第二问的被动限制、第三问的开放稳态条件须分别保留。

## 六、关键洞察

第一，太阳有限角宽进入入口辐照度和像面积，距离越远同时变暗和缩像，两因素在局部近轴辐照度抵消。集光总功率仍随距离减小，不能从局部强度的抵消声称太阳距离毫无作用。接近衍射或有限球尺寸时，更不能忽略太阳像的尺度。

第二，辐照度与辐亮度的角权重不同。对法向沿光轴的平面，填充半角$\alpha$的方向锥给
$$
\begin{aligned}
E_{\mathrm{plane}}
&=\int_0^{2\pi}\int_0^\alpha
L_S\cos\vartheta\sin\vartheta\,
\mathrm d\vartheta\,\mathrm d\phi\\
&=\pi L_S\sin^2\alpha
=\sigma T_S^4\sin^2\alpha.
\end{aligned}
$$
球对每个方向的总投影均为$\pi b^2$，不再乘同一个平面法向的$\cos\vartheta$，所以其吸收与$\Omega$成正比。近轴时两者都与$\alpha^2$成正比；大角度时不能用$E_{\mathrm{plane}}\pi b^2$替代球的完整方向积分。

薄圆片两面散热的有限角度温度为$T_{\mathrm{plate}}^4/T_S^4=\sin^2\alpha/2$，因此
$$
\begin{aligned}
\frac{T_{\mathrm{plate}}^4}{T_{\mathrm{sphere}}^4}
&=\frac{\sin^2\alpha}{1-\cos\alpha}\\
&=\frac{(1-\cos\alpha)(1+\cos\alpha)}
{1-\cos\alpha}=1+\cos\alpha.
\end{aligned}
$$
$\alpha\to0$时比例趋于$2$，$\alpha=\pi/2$时为$1$。形状影响不能用“黑体吸收率都为一”抹掉。

第三，对凸形、等温、无相互遮蔽的黑物体，在固定近似平行来光方向$\boldsymbol k$下，闭合面的法向投影正负相消：
$$
\begin{aligned}
\int_S\boldsymbol n\cdot\boldsymbol k\,\mathrm dS&=0,\\
A_{\mathrm{proj}}
&=\int_{\boldsymbol n\cdot\boldsymbol k>0}
\boldsymbol n\cdot\boldsymbol k\,\mathrm dS\\
&=\frac12\int_S|\boldsymbol n\cdot\boldsymbol k|\,\mathrm dS
\le\frac12 A_{\mathrm{em}}.
\end{aligned}
$$
薄平物体两大表面法向近乎沿$\pm\boldsymbol k$，可以趋近面积比$1/2$；球只有$1/4$。这进一步说明题干的球形条件不能省略。该证明不自动适用于深腔、自遮挡或反面保温的装置，那里应重新计算有效对外辐射和吸收。

第四，开放稳态的熵产生不必为零。主解的$0=\dot Q_H/T_H-\dot Q_C/T_C+\dot S_{\mathrm{gen}}$解释了产生熵却不积累自身熵。漏掉产生项，就只剩可逆热机；漏掉冷端，就误判所有太阳电池和电炉均不可稳态。

可由功需求写超温阈值：
$$
\begin{aligned}
T_B>T_S&\Longleftrightarrow
\dot W>4\pi b^2\sigma T_S^4,\\
\text{若 }T_B>T_S,\ \dot W=\eta\dot Q_H,\quad
\eta\le1-\frac{T_C}{T_H}
&\Longrightarrow
4\pi b^2\sigma T_S^4
<\dot Q_H\left(1-\frac{T_C}{T_H}\right).
\end{aligned}
$$
最后一式是可用功的理想上限条件，不保证实际器件达到；实际判断仍用实际$\eta$。增大集热器或减小球均可降低难度，但要保持辐射和材料模型有意义。功转换并非被动焦区热平衡。

## 七、易错点

太阳真实发射表面积$4\pi R_S^2$、球散热表面积$4\pi b^2$都正确，但中间太阳圆像应为$\pi a^2$。把前后两个正确球面积套到平面像，是额外因子$4$的来源。每次约分前先指出面积属于哪个对象。

迎光半球真实面积$2\pi b^2$不是吸收截面。各面元需要乘入射余弦，积分为$\pi b^2$。散热则要积分完整球面，导热好使背面也同温辐射。

不能把“黑体”理解为“小球”。本题已在题干中补充球形条件并注明修订，因此主解使用球的面积比$1/4$；薄圆片计算只是形状改变后的对照，不可混用其系数。近轴、小尺寸等适用条件仍须单独检查。

$r/f$增大不意味着温度无穷。先检查$r/f\ll1$，再判断近轴式能否用；实际方向立体角最多$4\pi$，一侧孔径最多$2\pi$。大角度又不可把平面辐照度的余弦权重误用于球的每方向投影。

自身熵不变不等于熵产生为零。不可逆稳态装置产生熵并排出，不积累自己的熵。相反，只写太阳电池或电炉而不指出冷环境和排熵，也没有完成检查。

耗尽电池的加热例子不符合自身状态不变；把永不耗尽的热库藏在器件内部同样不合格。必须由外界太阳持续供能，由外界接受排热和辐射，并同时验证功率与熵收支。

## 八、课堂讲解建议

课堂先让学生指出太阳表面、透镜圆孔、太阳像盘、球迎光投影、球全部表面，板书五个面积$4\pi R_S^2$、$\pi r^2$、$\pi a^2$、$\pi b^2$、$4\pi b^2$。先对应图7-1至图7-3，再约分计算温度，避免几何对象未明就操作数字。

讲解图7-2时，让学生比较太阳中心与边缘两个方向是否到同一像点，建立扩展源的像盘。教师强调断轴仅压缩尺度，不代表$r_E$只有几个$f$；$a$与$b$必须分别解释，不能都叫“焦斑半径”。

图7-3应先积分投影，再积分完整表面积。即使学生熟悉$\pi b^2$与$4\pi b^2$，也应解释吸收与散热为何选择不同面积，而非只记住温度式的$1/\sqrt2$。

图7-4不是只展示立体效果。课堂在图旁写$\mathrm d\Omega=\sin\vartheta\,\mathrm d\vartheta\,\mathrm d\phi$，积分$\Omega$，使用球的各方向投影，最后比较小角极限，实现两条路线交叉核验。初学者可从球面帽面积除以半径平方理解立体角。

最后对比图7-5被动双向路径与图7-6冷端、功流。让学生分别标能量流与熵流，板书两个稳态等式，说明“自身不变”和“外界也不变”不是同一句话。第三问要求给持续供能、外排熵和非耗尽的例子。

## 九、变式训练

（1）近轴与有限光锥。

取$T_S=6000\,\mathrm K$、$r/f=0.10$，球远小于像盘。另附加实际光锥均匀填充且$\tan\alpha=r/f$，比较两模型温度。近轴：
$$
\begin{aligned}
T_{\mathrm{par}}
&=6000\sqrt{0.10/2}
=6000\sqrt{0.05}\\
&=6000\times0.223606798
\simeq1341.64\,\mathrm K.
\end{aligned}
$$
光锥几何$\cos\alpha=1/\sqrt{1.01}$，因此
$$
\begin{aligned}
\frac{T_{\mathrm{cone}}^4}{T_S^4}
&=\frac12\left(1-\frac1{\sqrt{1.01}}\right),\\
T_{\mathrm{cone}}
&=6000\left[\frac12\left(1-\frac1{\sqrt{1.01}}\right)\right]^{1/4}
\simeq1339.14\,\mathrm K.
\end{aligned}
$$
相差约$2.50\,\mathrm K$来自有限角修正。多除一次$4$则得$6000\sqrt{0.10}/2\simeq948.683\,\mathrm K$，不能用小角修正解释这一巨大差异。

（2）背景回辐射。

球的半角$0.30$方向锥由$6000\,\mathrm K$太阳辐亮度填充，其余方向由$300\,\mathrm K$各向同性背景填充。令$\beta=\Omega/(4\pi)$，则
$$
\begin{aligned}
P_{\mathrm{abs}}
&=\pi b^2\left[
\frac{\sigma T_S^4}{\pi}\Omega
+\frac{\sigma T_C^4}{\pi}(4\pi-\Omega)\right],\\
4\pi b^2\sigma T_B^4
&=b^2\sigma[\Omega T_S^4+(4\pi-\Omega)T_C^4],\\
T_B^4&=\beta T_S^4+(1-\beta)T_C^4.
\end{aligned}
$$
$\beta=(1-\cos0.30)/2\simeq0.0223317554$，所以
$$
\begin{aligned}
T_B&=\left[
0.0223317554(6000)^4
+0.9776682446(300)^4
\right]^{1/4}\\
&\simeq2319.59\,\mathrm K.
\end{aligned}
$$
$\beta=0$得$T_B=T_C$，$\beta=1$得$T_B=T_S$。背景只填余下方向，不能额外再加整个$4\pi$背景而重复计算太阳方向。

（3）形状对比。

$T_S=6000\,\mathrm K$、$r/f=0.05$，比较同样近轴照明、均匀等温的球和两面黑薄圆片：
$$
\begin{aligned}
T_{\mathrm{sphere}}
&=6000\sqrt{0.05/2}
\simeq948.683\,\mathrm K,\\
T_{\mathrm{plate}}
&=6000\left[\frac{(0.05)^2}{2}\right]^{1/4}
=6000(0.00125)^{1/4}\\
&\simeq1128.18\,\mathrm K,\\
\frac{T_{\mathrm{plate}}}{T_{\mathrm{sphere}}}
&=2^{1/4}\simeq1.18921.
\end{aligned}
$$
圆片温度更高是散热面积比例较小，不是吸收率超过一。只涂黑一面或反面保温，已改变两面均黑模型，须重新列两面的发射和传热条件。

（4）主动超温的球尺寸。

太阳$6000\,\mathrm K$；热机$T_H=1200\,\mathrm K$、$T_C=300\,\mathrm K$，$\dot Q_H=1000\,\mathrm W$、实际$\eta=0.50$，全部功加热黑球。先核验：
$$
\begin{aligned}
\eta_{\mathrm{Carnot}}&=1-\frac{300}{1200}=0.75>0.50,\\
\dot W&=0.50\times1000=500\,\mathrm W,\qquad
\dot Q_C=500\,\mathrm W,\\
\dot S_{\mathrm{gen}}
&=\frac{500}{300}-\frac{1000}{1200}
=\frac53-\frac56=\frac56\,\mathrm{W/K}>0.
\end{aligned}
$$
维持$8000\,\mathrm K$的半径与刚好达到太阳温度的半径为
$$
\begin{aligned}
b_{8000}
&=\sqrt{\frac{500}{4\pi\sigma(8000)^4}}
\simeq4.13899\times10^{-4}\,\mathrm m,\\
b_{\mathrm{crit}}
&=\sqrt{\frac{500}{4\pi\sigma(6000)^4}}
\simeq7.35820\times10^{-4}\,\mathrm m.
\end{aligned}
$$
其他热损失忽略且黑体/材料模型成立时，$0<b<b_{\mathrm{crit}}$可超过$6000\,\mathrm K$；等号仅相等。尺寸上限用实际$500\,\mathrm W$功，不能偷偷把实际效率换成卡诺效率夸大功。功、冷端排热及边界温度必须属于同一个热机。

<!-- question-complete -->
