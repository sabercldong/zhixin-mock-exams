# 第 7 题

<!-- question-start -->
钠灯发出自然光，经理想窄缝 $S_0$ 后，照射对称的两条理想窄缝 $S_1,S_2$，两缝间距为 $d$。屏到双缝的距离为 $D\gg d$，屏上以对称点为原点取坐标 $z$，观测区域满足 $|z|\ll D$。忽略不同路径长度导致的振幅衰减，波长记为 $\lambda$。

（1）不加偏振片时，零级亮纹中心光强为 $I_0$，求 $I_1(z)$。

（2）在 $S_1,S_2$ 后分别放理想偏振片 $p_1,p_2$，屏前放覆盖两束光的偏振片 $p_3$。在垂直传播方向的偏振平面内，三片透光轴与 $x$ 轴的角度依次为 $0,\theta,2\theta$。以未加偏振片的 $I_0$ 为基准，求 $\theta=0$ 时的 $I_2(z)$ 和对比度 $M_2$。

（3）求 $\theta=\pi/4$ 时的 $I_3(z)$、$M_3$。

（4）求 $0<\theta<\pi/4$ 时的 $I_4(z)$、$M_4$。对比度定义为 $M=(I_{\max}-I_{\min})/(I_{\max}+I_{\min})$。

![图 7-1　双缝、屏前分析片及三个透光轴的方向。](../figures/question-07.png)
<!-- question-end -->

## 一、题型定位

带偏振统计的双缝干涉。双缝出射光来自同一个入射场，具有相同偏振分量间的相关性；“自然光”不意味着两条路径彼此完全不相干。经过不同方向的偏振片后，必须同时计算各束强度与交叉相关，不能仅用Malus定律计算两束强度再假定对比度为一。

## 二、知识点

远场程差；相位差；自然光的正交偏振统计；偏振片的矢量投影；Malus定律；电场叠加与强度时间平均；干涉交叉项；对比度；Cauchy不等式；相位与亮纹位置。

采用理想单色相干路径模型，两个正交分量的平均强度相等且互不相关。偏振片仅投影，不引入额外相位或吸收以外的效应。

## 三、物理图像

不加偏振片时，两个光路的同一偏振分量能够干涉，两组正交偏振的干涉图相同，因此自然光仍产生条纹。加上 $p_1,p_2$ 后，两束光各取共同入射场的不同投影，既改变振幅又改变统计相关。

末片 $p_3$ 使透射光方向相同，却不能把原来不相关的随机分量变成相同随机振幅。特别在 $\theta=\pi/4$ 时，$p_3$ 与 $p_1$ 正交，第一条路完全被阻断，只剩第二条路，因而没有干涉条纹。

## 四、解题入口

先以无偏振片的零级强度 $I_0$ 标定单缝强度 $I_s$。把双缝共同入射场分为 $E_x,E_y$ 两个正交随机分量，依次作两次投影。最后展开两束振幅和的模平方，在平均后得到常数项与 $\cos\delta$ 项，再分别取最大、最小值。

## 五、解析

（1）程差与相位差。

取 $S_1$ 位于 $z=d/2$，$S_2$ 位于 $z=-d/2$，屏上点位于 $z$。两路径为
$$r_1=\sqrt{D^2+(z-d/2)^2},\qquad r_2=\sqrt{D^2+(z+d/2)^2}.$$
在 $|z|,d\ll D$ 下用 $\sqrt{1+\epsilon}\simeq1+\epsilon/2$，
$$\begin{aligned}
r_2-r_1&\simeq\frac{(z+d/2)^2-(z-d/2)^2}{2D}\\
&=\frac{2zd}{2D}=\frac{dz}{D}.
\end{aligned}$$
所以
$$\delta=\frac{2\pi}{\lambda}(r_2-r_1)\simeq\frac{2\pi dz}{\lambda D}.$$
交换两缝命名只会使 $\delta$ 反号，后面的 $\cos\delta$ 不变。条纹周期为 $\Delta z=\lambda D/d$。

（2）用 $I_0$ 确定单路强度。

无偏振片时，两束等强且相干，在 $\delta=0$ 处振幅相加、强度是单束的四倍，故
$$I_s=\frac{I_0}{4}.$$
任意相位下两束叠加给出
$$\begin{aligned}
I_1(z)&=I_s+I_s+2I_s\cos\delta\\
&=\frac{I_0}{2}(1+\cos\delta)\\
&=\boxed{I_0\cos^2\left(\frac{\pi dz}{\lambda D}\right)}.
\end{aligned}$$
因此 $I_{\max}=I_0$、$I_{\min}=0$。如果误取 $I_s=I_0/2$，后面所有带偏振片的光强都会多一倍。

（3）建立自然光的共同随机振幅。

用复振幅 $E_x,E_y$ 表示同一束入射自然光的两个正交分量。将光强比例常数吸收进振幅定义后，
$$\langle|E_x|^2\rangle=\langle|E_y|^2\rangle=\frac{I_s}{2},\qquad
\langle E_xE_y^*\rangle=0.$$
尖括号表示时间或统计平均，星号表示复共轭。两条光路使用同一组 $E_x,E_y$，另乘路径相位；不能给第二条路重新引入完全独立的一组随机量，否则无偏振片时也不会干涉。

（4）第一条路的两次投影。

三个透光轴的单位矢量为
$$\boldsymbol u_1=(1,0),\quad
\boldsymbol u_2=(\cos\theta,\sin\theta),\quad
\boldsymbol u_3=(\cos2\theta,\sin2\theta).$$
过 $p_1$ 后电场为 $E_x\boldsymbol u_1$。再过 $p_3$，只留下在 $\boldsymbol u_3$ 上的投影，标量振幅为
$$a=E_x(\boldsymbol u_1\cdot\boldsymbol u_3)=E_x\cos2\theta.$$
图 7-2 中第一条路径的投影系数是 $\cos2\theta$，不是 $\cos\theta$。

![图 7-2　两条路径经过首片及分析片的矢量投影。](../figures/vectors-07.png)

（5）第二条路的两次投影。

过 $p_2$ 后的标量为
$$\boldsymbol E\cdot\boldsymbol u_2=E_x\cos\theta+E_y\sin\theta.$$
过 $p_3$ 再乘两轴点积
$$\boldsymbol u_2\cdot\boldsymbol u_3=\cos(2\theta-\theta)=\cos\theta.$$
故第二路最终标量振幅为
$$b=\cos\theta(E_x\cos\theta+E_y\sin\theta).$$
两路透射后的矢量方向都为 $\boldsymbol u_3$，但标量 $a,b$ 一般不是同一个随机量的常数倍。

（6）分别计算两路平均强度。

第一路为
$$A=\langle|a|^2\rangle=\frac{I_s}{2}\cos^22\theta.$$
第二路展开后，
$$\begin{aligned}
B&=\cos^2\theta\left[
\cos^2\theta\langle|E_x|^2\rangle
+\sin^2\theta\langle|E_y|^2\rangle
+2\sin\theta\cos\theta\,\operatorname{Re}\langle E_xE_y^*\rangle\right]\\
&=\frac{I_s}{2}\cos^2\theta(\cos^2\theta+\sin^2\theta)\\
&=\frac{I_s}{2}\cos^2\theta.
\end{aligned}$$
这与逐片Malus定律一致：自然光过首片强度减半，再乘相应的余弦平方。

（7）计算两路的交叉相关。

光强叠加还需要
$$\begin{aligned}
\Gamma&=\langle ab^*\rangle\\
&=\cos2\theta\cos\theta\left[
\cos\theta\langle|E_x|^2\rangle+\sin\theta\langle E_xE_y^*\rangle\right]\\
&=\boxed{\frac{I_s}{2}\cos2\theta\cos^2\theta}.
\end{aligned}$$
它为实数。在所求角度区间内为非负。图 7-3 中只有共同的 $E_x$ 分量参与交叉项；第二路的 $E_y$ 贡献仍增加背景强度，却不与第一路相干。

![图 7-3　共同偏振分量产生交叉项，独立分量只增加背景。](../figures/correlation-07.png)

若直接把 $\Gamma$ 写成 $\sqrt{AB}$，会漏掉相关系数 $\cos\theta$。方向相同只是干涉的必要因素，不保证随机振幅完全相关。

（8）得到任意 $\theta$ 的强度。

将路径相位附在第二束，最终标量为 $a+be^{i\delta}$。展开模平方并平均：
$$\begin{aligned}
I_\theta(z)
&=\langle(a+be^{i\delta})(a^*+b^*e^{-i\delta})\rangle\\
&=A+B+\Gamma e^{-i\delta}+\Gamma^*e^{i\delta}\\
&=A+B+2\Gamma\cos\delta.
\end{aligned}$$
代入三项并用 $I_s=I_0/4$，
$$\boxed{
I_\theta(z)=\frac{I_0}{8}
\left[\cos^22\theta+\cos^2\theta
+2\cos2\theta\cos^2\theta\cos\left(\frac{2\pi dz}{\lambda D}\right)\right].
}$$
这同一公式给出第（2）至（4）问，基准始终为不加偏振片时的 $I_0$。

（9）$\theta=0$ 的结果。

三片透光轴均平行，$\cos2\theta=\cos\theta=1$，所以
$$\begin{aligned}
I_2(z)&=\frac{I_0}{8}(2+2\cos\delta)\\
&=\boxed{\frac{I_0}{2}\cos^2\left(\frac{\pi dz}{\lambda D}\right)}.
\end{aligned}$$
亮纹峰值为 $I_0/2$，暗纹仍为零。因此
$$\boxed{M_2=1.}$$
光强减半来自自然光在首片后的损失；后续平行片不再损失所允许的分量。

（10）$\theta=\pi/4$ 的结果。

此时 $\cos2\theta=0$，第一条路在 $p_3$ 完全被挡住；$\cos^2\theta=1/2$，故
$$\boxed{I_3(z)=\frac{I_0}{16},\qquad M_3=0.}$$
该强度不随 $z$ 变化。第二路首片将强度由 $I_0/4$ 减为 $I_0/8$，再过与它相差 $45^\circ$ 的分析片减为 $I_0/16$，与上式一致。

（11）一般区间内的最大、最小及对比度。

令 $H=\cos^22\theta+\cos^2\theta$，$C=2\cos2\theta\cos^2\theta$。对 $0<\theta<\pi/4$，$C>0$，故
$$I_{\max}=\frac{I_0}{8}(H+C),\qquad I_{\min}=\frac{I_0}{8}(H-C).$$
代入定义时公共强度系数消去：
$$\begin{aligned}
M_4&=\frac{(H+C)-(H-C)}{(H+C)+(H-C)}\\
&=\boxed{\frac{2\cos2\theta\cos^2\theta}{\cos^22\theta+\cos^2\theta}}.
\end{aligned}$$
亮纹仍位于 $\delta=2j\pi$，间距不变；偏振片改变背景与调制深度，不改变这里的几何程差。

![图 7-4　三个代表角度的强度分布与条纹调制。](../figures/fringes-07.png)

（12）非负性与极限检验。

由 $|\Gamma|\le\sqrt{AB}$，有
$$A+B-2|\Gamma|\ge A+B-2\sqrt{AB}=(\sqrt A-\sqrt B)^2\ge0.$$
所以暗纹强度不会为负，并有 $0\le M\le1$。在所求区间中还可直接写
$$H-C=(\cos2\theta-\cos^2\theta)^2+\cos^2\theta\sin^2\theta\ge0.$$
将 $\theta\to0$、$\theta\to\pi/4$ 代入一般式，分别恢复 $M=1,0$，以及前两问的光强。各项均为 $I_0$ 乘无量纲三角函数，量纲正确。

## 六、关键洞察

偏振片是对随机矢量场的线性变换。单路强度由二阶矩决定，干涉项由两路互相关决定，两者不能互相替代。

只要两路都非零，归一化相关系数为
$$\gamma=\frac{\Gamma}{\sqrt{AB}}=\cos\theta
\quad(0<\theta<\pi/4).$$
所以对比度也可分解为
$$M=\frac{2\sqrt{AB}}{A+B}\,\gamma.$$
第一个因子是不等强度的影响，第二个是偏振选择引入的部分相关。这一分解说明末片使方向相同仍不足以完全恢复条纹。

若分析片的轴改为任意 $\alpha$，重复投影得到
$$I_\alpha(z)=\frac{I_0}{8}
\left[\cos^2\alpha+\cos^2(\alpha-\theta)
+2\cos\alpha\cos(\alpha-\theta)\cos\theta\cos\delta\right].$$
两束非零时，相关系数大小仍为 $|\cos\theta|$，可调整的是强度平衡因子。取 $\alpha=\theta/2$，两路强度相等，对比度达到该条件下最大值 $|\cos\theta|$。对于正交首片 $\theta=\pi/2$，两路选取的自然光分量互不相关，任何固定分析片都不能恢复交叉项。

## 七、易错点

将 $p_3$ 的角度读成 $\theta$ 会错掉第一路的 $\cos2\theta$。图中两次相邻夹角均为 $\theta$，因此第三片相对于 $p_1$ 为 $2\theta$。

自然光过理想首片的平均强度减半，不是电场振幅固定减半。不能把这个统计因子与第二次投影余弦混在一起。

只算 $A,B$ 后用 $2\sqrt{AB}$ 写干涉振幅，会把部分相关错当成完全相干。反过来，把两缝入射随机场看成独立，又会错误地抹去无偏振片时的条纹。

对比度分母是 $I_{\max}+I_{\min}$，不是最大光强；$I_0$ 是未加片的零级强度，不能在各问中重新定义。

## 八、课堂讲解建议

先让学生核对三个轴角，再分别作第一路、第二路的投影。课堂板书将单路强度和交叉项分三列，在最后一列保留 $\langle E_xE_y^*\rangle=0$，使背景与相干项的来源清楚可见。

讲到末片时追问“方向相同是否意味着随机振幅相同”，用第二路残留的 $E_y$ 分量说明区别。最后比较三条强度曲线，让学生指出周期、峰值和对比度分别由哪些因素决定。

<!-- KEEP_TOGETHER_START -->
## 九、变式训练

变式一：按本题三片轴角取 $\theta=\pi/6$，求光强及对比度。

解：$\cos2\theta=1/2$、$\cos^2\theta=3/4$，故
$$I(z)=\frac{I_0}{8}\left[1+\frac34\cos\delta\right].$$
于是 $I_{\max}=7I_0/32$、$I_{\min}=I_0/32$，
$$M=\frac{(7-1)I_0/32}{(7+1)I_0/32}=\frac34.$$
两路强度不等、相关系数小于一，使对比度低于一。

变式二：首片仍相差 $\theta=\pi/4$，但末片改取中间轴 $\alpha=\theta/2=\pi/8$，求最大对比度。

解：两路最后强度相等，$\cos^2\alpha=\cos^2(\alpha-\theta)=\cos^2(\pi/8)$，因此
$$I(z)=\frac{I_0}{4}\cos^2\frac{\pi}{8}\left(1+\frac1{\sqrt2}\cos\delta\right),\qquad
M=\frac1{\sqrt2}.$$
这大于本题 $\alpha=2\theta=\pi/2$ 的零对比度，但仍小于一。分析片可使两路都透射并平衡强度，不能消去共同入射场的统计相关限制。
<!-- KEEP_TOGETHER_END -->

（3）两路另有复空间相干度$g$，求条纹对比度。取$\theta=\pi/6,|g|=1/2$核算。

解：不相干背景强度不变，交叉项乘$g$，因此
$$\mathcal V=|g|\frac{2\cos2\theta\,\cos^2\theta}{\cos^22\theta+\cos^2\theta}.$$
给定角度时原对比度为$3/4$，故新值为$3/8$；$\arg g$只平移条纹相位。这里相干度表示相同两路对应光场的相关程度，不能同时把相关交叉项按两独立自然光束相加。

（4）第二路进入检偏器前的振幅另乘$t>0$，检偏器角$\alpha$可调。求最大对比度及其实现条件。

解：两路强度正比于$\cos^2\alpha$和$t^2\cos^2(\alpha-\theta)$，原自然光相关系数为$\cos\theta$。因此最大对比度为$|\cos\theta|$，在
$$|\cos\alpha|=t|\cos(\alpha-\theta)|$$
时取得。选择同号投影支路可写$\tan\alpha=(1-t\cos\theta)/(t\sin\theta)$。$\theta=\pi/3,t=1/2$时可取$\alpha=\pi/3$，最大值$1/2$。必须保证共同投影非零；完全遮断两路时对比度没有意义。
