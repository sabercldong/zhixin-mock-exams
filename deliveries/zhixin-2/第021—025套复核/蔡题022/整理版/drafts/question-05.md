# 第 5 题

中空薄壁圆柱长 $l$、半径 $r$、壁厚 $d$，满足 $l\gg r\gg d$，材料电阻率为 $\rho$。电流沿圆周切向流动，并沿柱长均匀分布；把穿过一条轴向截面的总环向电流记为 $I$。圆柱被固定，忽略外部磁场。
（1）求圆柱内部磁感应强度。
（2）给出沿圆周的感应电动势 $\varepsilon$ 与 $dI/dt$ 的关系。
（3）给出 $\varepsilon$ 与 $I,\rho$ 和圆柱尺寸的关系。
（4）在 $t=0$ 时 $I=I_0$，求以后无外加电源维持时的 $I(t)$。

![图 5-1　薄壁长圆柱、环向电流及轴向磁场。](../figures/question-05.png)

## 一、题型定位

这是长圆柱环向电流的自感衰减问题。电流沿圆周流动。整个柱面相当于沿轴向并联的许多细环，其内部磁场与长螺线管的电流面密度模型相同。
题目第（4）问要求自由衰减，必须取无外加电源的条件。若存在给定时变外电源电动势，单凭初始电流不足以确定以后电流。下面明确采用自感电场驱动导电环向电流、外源已经移除的模型。

## 二、知识点

表面电流密度 $K_\phi$ 的单位是安培每米，均匀分布时 $K_\phi=I/l$。安培环路给出内部轴向磁场。法拉第定律提供环向非静电场，欧姆定律将电场与材料内部电流密度连接。
有效电阻的导电横截面为 $ld$，导电路径长为 $2\pi r$；不能使用空心截面 $\pi r^2$。自感系数与电阻的比值决定衰减时间常数。固定圆柱不产生运动电动势；表面约束可能受力，却不改变固定模型的能量守恒核算。

## 三、物理图像

从柱轴正端观察，选逆时针环向电流为正，它通过右手规则产生沿 $+z$ 的磁场。圆柱很长，内部场近似均匀、外部场近似零，端部长度约为 $r$ 的区域被忽略。
当正向电流自由衰减时，$dI/dt<0$，磁通减小，感应电场仍沿正电流方向，试图维持原电流。导电损耗最终使电流下降，不是感应电场直接反向阻止原电流。这需与建立电流时感应场反向分开。

## 四、解题入口

先取轴向窄带，把总电流 $I$ 分解为面电流和体电流密度。用安培定律得到 $B$，用一个圆周回路得到感应电动势，再用欧姆定律写同一圆周上的电压降，两者相等得到一阶衰减方程。
之后分别用磁场能量和焦耳热独立验证自感与时间常数。长柱控制端效应，薄壁控制穿壁均匀性，缓变允许忽略位移电流及高频趋肤过程，三个条件不可互相替代。

## 五、解析

（1）定义总电流及微带电流。

取沿轴向长度为 $dz$ 的窄带。由于沿长度均匀，窄带环流为
$$
dI=\frac I l\,dz.
$$
面电流密度为
$$
\boxed{K_\phi=\frac Il.}
$$
穿过总电流截面的面积是 $ld$，所以体电流密度为
$$
\boxed{J_\phi=\frac I{ld}.}
$$
检验积分：
$$
\int_0^l J_\phi d\,dz=\int_0^l\frac Il\,dz=I.
$$
这里的 $I$ 是所有并联细环沿某一轴向截面的合计，不是每个细环各自流过同样的总电流 $I$。

（2）建立长柱安培矩形环路。

图5-2的矩形长边沿柱轴，一边在柱内，另一边在柱外，长为 $\Delta z$。选正方向使跨面环向电流为正。忽略端效应，短边不贡献轴向场，故
$$
B_{\rm in}\Delta z-B_{\rm out}\Delta z
=\mu_0K_\phi\Delta z.
$$
外部场取为零后
$$
\boxed{B_{\rm in}=\mu_0K_\phi=\frac{\mu_0I}{l}.}
$$
方向由右手规则确定。结果不含 $r$ 和 $d$，并非遗漏：无限长电流面模型的内部场由每单位长度的环流决定。

![图 5-2　轴向安培环路及内外场的差值。](../figures/ampere-05.png)

如果材料磁导率不是 $\mu_0$ 或存在磁芯，需另给本构关系；本题未给磁性参数，采用非磁性导电薄壁模型。不能把第4题铁磁环的 $\mu$ 搬到这里。

（3）明确圆周回路的定向与磁通。

取接近内壁半径 $r$ 的圆周回路，正方向与正电流相同，法向沿 $+z$。薄壁近似下包围面积为 $\pi r^2$，磁通为
$$
\Phi(t)=\pi r^2B(t)=\frac{\mu_0\pi r^2}{l}I(t).
$$
忽略 $O(d/r)$ 的壁内场能和半径差；选内、外或中间半径只改变高阶修正。
法拉第定律给出有符号感应电动势
$$
\begin{aligned}
\varepsilon_{\rm ind}
&=\oint\boldsymbol E\cdot d\boldsymbol l=-\frac{d\Phi}{dt}\\
&=\boxed{-\frac{\mu_0\pi r^2}{l}\frac{dI}{dt}.}
\end{aligned}
$$
电动势不是静电势差；闭环电场非保守，不能以回到同一点电势差为零否定它。

（4）将环向电场与电动势联系。

轴对称使圆周上的 $E_\phi$ 均匀：
$$
\varepsilon_{\rm ind}=2\pi rE_\phi,\qquad
\boxed{E_\phi=-\frac{\mu_0r}{2l}\dot I.}
$$
图5-3中，电流衰减时 $\dot I<0$，$E_\phi>0$，感应场沿原电流正向。若外源主动增加电流，则感应场沿反向。

![图 5-3　电流衰减时维持原方向的感应电场。](../figures/faraday-05.png)

（5）用局部欧姆定律求材料电压降。

局部欧姆关系为
$$
E_\phi=\rho J_\phi=\frac{\rho I}{ld}.
$$
因此沿正电流方向的闭环电场积分为
$$
\begin{aligned}
\varepsilon_{\rm ohm}
&=2\pi rE_\phi\\
&=\boxed{\frac{2\pi\rho r}{ld}I.}
\end{aligned}
$$
定义有效电阻
$$
\boxed{\mathcal R=\frac{2\pi\rho r}{ld}.}
$$
路径长是 $2\pi r$，导电截面是 $ld$。$\rho l/(\pi r^2)$ 描述沿轴导电的另一个问题，连尺寸依赖都相反。

（6）用并联细环独立验证电阻。

宽为 $dz$ 的细环，导电截面为 $d\,dz$，其电阻为
$$
\mathcal R_{dz}=\frac{2\pi\rho r}{d\,dz}.
$$
各细环受相同的感应电动势，电导应相加：
$$
\begin{aligned}
\frac1{\mathcal R}
&=\int_0^l\frac{d\,dz}{2\pi\rho r}\\
&=\frac{ld}{2\pi\rho r}.
\end{aligned}
$$
取倒数恢复 $\mathcal R=2\pi\rho r/(ld)$。微带电阻随 $dz$ 变小而变大，符合并联细分；不能将它按串联电阻积分。

（7）联立法拉第关系与欧姆关系。

无外加电源时，闭环电场来自变化的自磁通：
$$
-\frac{\mu_0\pi r^2}{l}\dot I
=\frac{2\pi\rho r}{ld}I.
$$
先约去 $\pi/l$，再整理：
$$
-\mu_0r^2\dot I=\frac{2\rho r}{d}I,
$$
$$
\boxed{\dot I+\frac{2\rho}{\mu_0rd}I=0.}
$$
定义
$$
\boxed{\tau_c=\frac{\mu_0rd}{2\rho},}
$$
得 $\dot I+I/\tau_c=0$。$\tau_c>0$，电流衰减；若误加负号会变成无源增长，违背耗散性。

（8）完整求解初值问题。

对 $I_0\ne0$ 分离变量：
$$
\frac{dI}{I}=-\frac{dt}{\tau_c}.
$$
积分：
$$
\ln\left|\frac{I(t)}{I_0}\right|=-\frac t{\tau_c}.
$$
初值正负决定方向，指数不改变符号：
$$
\boxed{I(t)=I_0e^{-t/\tau_c}
=I_0\exp\!\left(-\frac{2\rho t}{\mu_0rd}\right).}
$$
$I_0=0$ 的无源解为零，不需对零取对数。磁场为
$$
B(t)=\frac{\mu_0I_0}{l}e^{-t/\tau_c}.
$$
$t\to\infty$ 时电流与场趋零；有限时间且 $I_0\ne0$ 时不突然变零。

（9）从磁场能推导有效自感。

内部场能密度 $B^2/(2\mu_0)$、体积 $\pi r^2l$，所以
$$
\begin{aligned}
W_B&=\frac{B^2}{2\mu_0}\pi r^2l\\
&=\frac1{2\mu_0}\left(\frac{\mu_0I}{l}\right)^2\pi r^2l\\
&=\frac12\frac{\mu_0\pi r^2}{l}I^2.
\end{aligned}
$$
与 $W_B=\tfrac12\mathcal LI^2$ 比较：
$$
\boxed{\mathcal L=\frac{\mu_0\pi r^2}{l}.}
$$
因此
$$
\frac{\mathcal L}{\mathcal R}
=\frac{\mu_0\pi r^2/l}{2\pi\rho r/(ld)}
=\frac{\mu_0rd}{2\rho}=\tau_c.
$$
自感与电阻都反比于 $l$，时间常数消去柱长；不是柱长不影响任何物理量。

（10）计算焦耳热及初始磁能去向。

导电体积近似 $2\pi rld$，功率为
$$
\begin{aligned}
P_J&=\rho J_\phi^2(2\pi rld)\\
&=\rho\left(\frac I{ld}\right)^2(2\pi rld)\\
&=\frac{2\pi\rho r}{ld}I^2=\mathcal RI^2.
\end{aligned}
$$
能量导数为
$$
\frac{dW_B}{dt}=\mathcal LI\dot I
=-\frac{\mathcal L}{\tau_c}I^2=-\mathcal RI^2.
$$
场能下降等于焦耳热，不需要圆柱运动。积分：
$$
\begin{aligned}
Q_{\rm total}
&=\int_0^\infty\mathcal RI_0^2e^{-2t/\tau_c}\,dt\\
&=\mathcal RI_0^2\frac{\tau_c}{2}\\
&=\frac12\mathcal LI_0^2=W_B(0).
\end{aligned}
$$
图5-4的能量指数为 $2t/\tau_c$，电流指数为 $t/\tau_c$，两者半衰时间不同。

![图 5-4　归一化电流、磁场能与累计焦耳热。](../figures/energy-05.png)

（11）区分电流与能量半衰时间。

电流降到一半时
$$
e^{-t_I/\tau_c}=\frac12,\qquad t_I=\tau_c\ln2.
$$
磁能降到一半时
$$
e^{-2t_W/\tau_c}=\frac12,\qquad t_W=\frac{\tau_c}{2}\ln2.
$$
累计热占比为
$$
\frac{Q(0,t)}{W_B(0)}=1-e^{-2t/\tau_c}.
$$
区别来自能量正比电流平方，不是两种不同的材料衰减机制。

（12）检验薄壁缓变近似。

取特征频率量级 $1/\tau_c$，趋肤长度为
$$
\delta_{\rm skin}\sim\sqrt{\frac{2\rho\tau_c}{\mu_0}}=\sqrt{rd}.
$$
$d\ll r$ 时
$$
\frac{\delta_{\rm skin}}d\sim\sqrt{\frac rd}\gg1,
$$
故主衰减时间尺度上电流穿壁均匀有自洽依据。最早的快速关断仍可能含高频分量，不能保证所有瞬间都无趋肤。
端效应由 $r/l\ll1$ 控制，半径和场能修正由 $d/r\ll1$ 控制。传播及位移电流也需可忽略。圆柱固定排除了运动电动势；若允许变形，磁压力可能改变半径、自感随时间变，常系数指数不再适用。

（13）用能流方向独立解释磁能怎样进入导体。

仅写出 $-dW_B/dt=P_J$ 能检验总量，还可以检查能量传递方向。内壁附近，衰减电流产生正向 $E_\phi$ 和正向 $B_z$，坡印廷矢量为
$$
\boldsymbol S=\frac{\boldsymbol E\times\boldsymbol B}{\mu_0},\qquad
S_r=\frac{E_\phi B_z}{\mu_0}>0.
$$
因为 $\boldsymbol e_\phi\times\boldsymbol e_z=\boldsymbol e_r$，能量从空腔磁场区沿径向向外进入薄壁。空腔侧面积近似 $2\pi rl$，流出空腔的功率
$$
\begin{aligned}
P_{\rm out}
&=2\pi rl\frac{E_\phi B_z}{\mu_0}\\
&=2\pi rl E_\phi\frac I l\\
&=(2\pi rE_\phi)I=\mathcal RI^2.
\end{aligned}
$$
该结果独立恢复焦耳热功率。感应电场和电流同向并不产生无源能量；它们使原先储存在磁场中的能量进入电阻材料。若把感应电场方向误画为反向，能流方向也随之错误。

（14）检验特征尺度，并计算任意时段的热量。

若 $r=0.10\,\mathrm m$、$d=1.0\,\mathrm{mm}$、$l=2.0\,\mathrm m$、$\rho=1.7\times10^{-8}\,\Omega\,\mathrm m$，则
$$
\begin{aligned}
\mathcal R&=\frac{2\pi(1.7\times10^{-8})(0.10)}{2.0(10^{-3})}
=5.34071\times10^{-6}\,\Omega,\\
\mathcal L&=\frac{(4\pi\times10^{-7})\pi(0.10)^2}{2.0}
=1.97392\times10^{-8}\,\mathrm H,\\
\tau_c&=\mathcal L/\mathcal R=3.69599\times10^{-3}\,\mathrm s.
\end{aligned}
$$
这组数值只用于核验公式，并非原题另给条件。趋肤长度为 $\sqrt{rd}=10\,\mathrm{mm}$，是壁厚的十倍；传播时间 $l/c$ 约为 $6.7\,\mathrm{ns}$，远小于毫秒衰减尺度。若改为极低电阻率，时间常数增加；若改为极薄壁，衰减加快，需重新核对传播和初始高频瞬态。

任意 $0\le t_1<t_2$ 的焦耳热为
$$
\begin{aligned}
Q(t_1,t_2)
&=\mathcal RI_0^2\int_{t_1}^{t_2}e^{-2t/\tau_c}\,dt\\
&=\frac12\mathcal LI_0^2
\left(e^{-2t_1/\tau_c}-e^{-2t_2/\tau_c}\right)\\
&=W_B(t_1)-W_B(t_2).
\end{aligned}
$$
该积分同时检查初能去向及任意子时段的能量守恒。

（15）最终答案与量纲。

在非磁性长柱薄壁、均匀环流及无外源缓变模型下：
$$
\boxed{
\begin{aligned}
B&=\frac{\mu_0I}{l},\\
\varepsilon_{\rm ind}&=-\frac{\mu_0\pi r^2}{l}\dot I,\\
\varepsilon_{\rm ohm}&=\frac{2\pi\rho r}{ld}I,\\
I(t)&=I_0e^{-2\rho t/(\mu_0rd)}.
\end{aligned}}
$$
$\mu_0rd/\rho$ 为秒，$\mathcal L$ 为亨利，$\mathcal R$ 为欧姆；$\mathcal L\dot I$ 与 $\mathcal RI$ 都为伏特。电阻率越大衰减越快，壁越厚电阻越小、衰减越慢，符合能量图像。

## 六、关键洞察

磁通和场能路线同时得到 $\mathcal L=\mu_0\pi r^2/l$。把 $I$ 定义为细环合计，磁通是与该广义电流相配的量；互感已包含在共同轴向场中，不能把各细环孤立自感再相加。
柱长增倍、总电流不变，场强、储能和电阻均减半，时间常数不变，提供直接比例检查。
外源提供 $\varepsilon_{\rm ext}(t)$ 时，正确方程为
$$
\mathcal L\dot I+\mathcal RI=\varepsilon_{\rm ext}(t).
$$
无源指数只是右侧为零的初值解，不能用于任意驱动。

## 七、易错点

把电流沿轴向流动；把微带电流当总 $I$；用空心面积当导电截面；衰减时将感应场画成反向；混淆电流与磁能半衰时间，都会导致错误。
$B$ 正比 $I/l$，不是 $I/(2\pi r)$，后者来自另一种模型。圆柱固定不意味着磁能不能变成热，约束无机械功但电场仍对电流做功。

## 八、课堂讲解建议

在图5-1的轴向截面标出合计电流，切出宽 $dz$ 的细环，让学生解释为何并联。用图5-2求场，转到图5-3检查衰减方向。
指数解之后用场能和热独立核验，再读图5-4解释半衰时间。改变柱长，让学生同时追踪场、自感、电阻与时间常数，防止只记没有电流定义的公式。

## 九、变式训练

（1）柱长增倍、壁厚减半，$r,\rho,I_0$ 不变，求初始场、磁能和时间常数的比值。

解：场与自感正比 $1/l$，初始场和能量均减半；电阻正比 $1/(ld)$，保持不变。因此时间常数减半，与 $\tau_c\propto d$ 一致。

（2）外加恒定电动势 $\varepsilon_0$，初态 $I(0)=0$，求建立过程和撤源后衰减。

解：$I_\infty=\varepsilon_0/\mathcal R$，建立方程
$$
\dot I+\frac I{\tau_c}=\frac{I_\infty}{\tau_c}
$$
给出
$$
I(t)=I_\infty(1-e^{-t/\tau_c}).
$$
若在 $t_s$ 撤源，$I_s=I_\infty(1-e^{-t_s/\tau_c})$，此后
$$
I(t)=I_se^{-(t-t_s)/\tau_c},\qquad t\ge t_s.
$$
两段电流连续，变化率随开关改变；不能在撤源时把电流瞬间设零。

（3）撤源后磁能降至一半需多久？此时电流和已释放热量是多少？

解：$U=\mathcal LI_0^2e^{-2t/\tau_c}/2$，因此
$$t_{1/2}=\frac{\tau_c}2\ln2,\quad I=I_0/\sqrt2,\quad Q=U_0/2.$$
直接积分$\mathcal RI^2$也给同一热量，使用$\tau_c=\mathcal L/\mathcal R$。电流减半需$\tau_c\ln2$，与能量减半时间相差一倍。

（4）外部控制电阻率为$\rho(t)=\rho_0(1+t/t_\rho)$，几何和磁导率不变，求电流及累计热量。

解：令$\tau_0=\mu_0rd/(2\rho_0)$，分离变量积分$\dot I=-(1+t/t_\rho)I/\tau_0$，得
$$I=I_0e^{-t/\tau_0-t^2/(2\tau_0t_\rho)},\quad
Q(0,t)=\frac{\mathcal L}{2}[I_0^2-I(t)^2].$$
第二式来自$\dot U=-\mathcal R(t)I^2$，适用于随时间变化的正电阻。这里规定$\rho(t)$，未假设焦耳热自动产生该电阻率变化。
