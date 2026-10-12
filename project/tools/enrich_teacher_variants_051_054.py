#!/usr/bin/env python3
"""为教师版补充已给出完整解答的变式。

正文位于“九、变式训练”内，学生版生成器不会提取该模块。
脚本通过唯一标记保持幂等。
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


ADDITIONS: dict[str, dict[int, str]] = {
    "051": {
        6: r"""**变式的完整解答。** 将气体的定容摩尔热容写成
$$
C_V=\frac f2R.
$$
过程 $a$ 中温度从 $T_0$ 升至 $2T_0$，体积不变，因而
$$
Q_a=nC_VT_0=\frac f2p_0V_0,
\qquad
\boxed{\alpha=\frac f2}.
$$
过程 $b$ 定压，温度从 $2T_0$ 升至 $4T_0$，故
$$
Q_b=n(C_V+R)(2T_0)
=(f+2)p_0V_0,
\qquad
\boxed{\beta=f+2}.
$$

再设回程满足 $p/V^s=K$。由 $p=KV^s$ 与 $pV=nRT$ 得
$$
T=\frac K{nR}V^{s+1}.
$$
对任意一段该过程微分：
$$
(s+1)p\,\mathrm dV=nR\,\mathrm dT,
$$
所以
$$
\mathrm dQ
=nC_V\,\mathrm dT+p\,\mathrm dV
=n\left(C_V+\frac{R}{s+1}\right)\mathrm dT.
$$
因此该路径的摩尔热容为
$$
\boxed{C_s=C_V+\frac R{s+1}}.
$$

不过，本循环的状态 $C$ 由过程 $b$ 确定为
$$
(V_C,p_C,T_C)=(2V_0,2p_0,4T_0).
$$
要使同一条 $p/V^s=\text{const}$ 曲线同时通过 $C$ 与初态 $A$，必须有
$$
\frac{2p_0}{(2V_0)^s}
=\frac{p_0}{V_0^s}
\quad\Longrightarrow\quad
2^{1-s}=1.
$$
故闭合条件唯一给出
$$
\boxed{s=1}.
$$
代入 $s=1$ 和 $T_A-T_C=-3T_0$：
$$
Q_c
=n\left(\frac f2R+\frac R2\right)(-3T_0)
=-\frac32(f+1)p_0V_0,
$$
所以放热系数
$$
\boxed{\gamma=\frac32(f+1)}.
$$
净功由路径决定，仍为 $W_{\rm net}=p_0V_0/2$；总吸热为
$$
Q_{\rm in}
=\left(\frac f2+f+2\right)p_0V_0
=\frac{3f+4}{2}p_0V_0.
$$
因而
$$
\boxed{\eta=\frac1{3f+4}}.
$$
当 $f=5$ 时逐项还原为 $\alpha=5/2$、$\beta=7$、$\gamma=9$、$\eta=1/19$。""",
    },
    "053": {
        6: r"""**变式的完整解答。** 若两面镜以相同速率 $u$ 向中心靠近，镜间距记为 $X$，则
$$
\frac{\mathrm dX}{\mathrm dt}=-2u.
$$
慢变条件是 $u/c\ll1$，一次往返期间 $X$ 的相对变化可忽略。一维腹内光子的绝热不变量给出
$$
\nu X=\nu_0l_0,
$$
所以
$$
\boxed{\nu(X)=\nu_0\frac{l_0}{X}}.
$$
这与只移动右镜时的频率—腔长关系相同；区别只在同一腔长变化所需的时间减半。

光子能量为
$$
E(X)=h\nu_0\frac{l_0}{X}.
$$
对腔长求导，得两镜合计的广义压缩力
$$
-\frac{\mathrm dE}{\mathrm dX}
=\frac{h\nu_0l_0}{X^2}.
$$
这个量就是单面镜所受力的大小，也可由冲量通量复核。每次反射的动量改变约为 $2h\nu/c$，同一面镜的碰撞频率约为 $c/(2X)$，故
$$
F_{\rm one}
=\frac{2h\nu}{c}\frac{c}{2X}
=\frac{h\nu}{X}
=\boxed{\frac{h\nu_0l_0}{X^2}}.
$$
两面镜的力大小相同、方向相反，整个系统的合外力为零，但外界同时推动两镜时的功率为
$$
P_{\rm ext}=2F_{\rm one}u.
$$
另一方面
$$
\frac{\mathrm dE}{\mathrm dt}
=\frac{h\nu_0l_0}{X^2}(2u)
=2F_{\rm one}u,
$$
两者完全一致。""",
        7: r"""**变式的完整解答。** 把水换成折射率为 $n$ 的液体，保留玻璃折射率 $n_G$。透镜在空气中的焦距为 $f$，对平凸薄透镜有
$$
R=(n_G-1)f,
$$
其中 $R$ 是唯一曲面的曲率半径大小。

外贴时，光先通过液体—玻璃平面，该面光焦度为零；再经玻璃—空气曲面，系统光焦度仍为 $1/f$。近轴成像式为
$$
\frac1y=\frac1f-\frac n x.
$$
解得
$$
\boxed{y_{\rm out}=\frac{fx}{x-nf}}.
$$
实、虚像分界在分母为零处：
$$
\boxed{x_{0,\rm out}=nf}.
$$
$x>nf$ 时 $y>0$，为空气侧实像；$0<x<nf$ 时 $y<0$，为物侧虚像。

内贴时，液体中的光先经液体—玻璃曲面，系统光焦度变为
$$
\Phi_{\rm in}
=\frac{n_G-n}{R}
=\frac{n_G-n}{(n_G-1)f}.
$$
随后的玻璃—空气平面不增加光焦度。因而
$$
\frac1{y_{\rm in}}
=\Phi_{\rm in}-\frac n x,
$$
即
$$
\boxed{
y_{\rm in}
=\frac{x(n_G-1)f}
{x(n_G-n)-n(n_G-1)f}
}.
$$
若 $n_G>n$，分界物距为
$$
\boxed{
x_{0,\rm in}
=\frac{n(n_G-1)}{n_G-n}f
}.
$$
若 $n_G\le n$，曲面光焦度非正，对正物距不再存在有限的实像分界。最后取 $n\to1$：
$$
x_{0,\rm out}\to f,
\qquad
x_{0,\rm in}\to f,
$$
两种贴法都退化为空气中普通薄透镜的焦距分界，极限一致。""",
    },
    "054": {
        3: r"""**变式的完整解答。** 将 $AB$ 过程改为
$$
p=\alpha V^s,
$$
其余过程仍为 $BC$ 绝热、$CA$ 在 $T_1$ 等温。由理想气体状态方程，在 $AB$ 上
$$
T=\frac{\alpha}{\nu R}V^{s+1}.
$$
因此
$$
\frac{V_B}{V_A}
=\left(\frac{T_2}{T_1}\right)^{1/(s+1)}.
$$
又因
$$
(s+1)p\,\mathrm dV=\nu R\,\mathrm dT,
$$
所以
$$
\begin{aligned}
\mathrm dQ_{AB}
&=\nu C_V\,\mathrm dT+p\,\mathrm dV\\
&=\nu\left(C_V+\frac R{s+1}\right)\mathrm dT.
\end{aligned}
$$
过程摩尔热容为
$$
\boxed{C_{AB}=C_V+\frac R{s+1}},
$$
且
$$
\boxed{
Q_{AB}
=\nu\left(C_V+\frac R{s+1}\right)(T_2-T_1)
}.
$$
当 $s=-1$ 时上式的分母失效，因为该过程本身就是等温，应单独处理。

在 $BC$ 上使用绝热关系
$$
TV^{\gamma-1}=\text{const},
\qquad
\gamma=1+\frac R{C_V}.
$$
又因 $CA$ 等温且回到 $A$，所以 $T_C=T_A=T_1$。从而
$$
\frac{V_C}{V_B}
=\left(\frac{T_2}{T_1}\right)^{1/(\gamma-1)}.
$$
与 $V_B/V_A$ 相乘：
$$
\boxed{
\frac{V_C}{V_A}
=\left(\frac{T_2}{T_1}\right)^{
\frac1{s+1}+\frac1{\gamma-1}}
}.
$$
本题 $C_V=5R/2$，故 $\gamma=7/5$、$1/(\gamma-1)=5/2$。取 $s=1$ 时
$$
C_{AB}=\frac52R+\frac12R=3R,
$$
且
$$
\frac{V_C}{V_A}
=\left(\frac{T_2}{T_1}\right)^{1/2+5/2}
=\boxed{\left(\frac{T_2}{T_1}\right)^3},
$$
正好还原原题。""",
        4: r"""**变式的完整解答。** 对平面内任意质量元 $\mathrm dm$，到 $z$ 轴的距离满足
$$
r_\perp^2=x^2+y^2.
$$
因此垂直轴定理直接给出
$$
I_z=\int(x^2+y^2)\,\mathrm dm
=I_x+I_y.
$$
代入原题已求得的二阶结果：
$$
I_{2x}=\frac{197}{2880}ML^2,
\qquad
I_{2y}=\frac{199}{2880}ML^2,
$$
得
$$
\begin{aligned}
I_{2z}
&=\frac{197+199}{2880}ML^2\\
&=\frac{396}{2880}ML^2\\
&=\boxed{\frac{11}{80}ML^2}.
\end{aligned}
$$

再用逐段积分独立复核。对端点为 $(x_1,y_1)$、$(x_2,y_2)$ 的均匀线段，令
$$
x(t)=x_1+t(x_2-x_1),
\qquad
y(t)=y_1+t(y_2-y_1),
\quad0\le t\le1.
$$
沿线段的 $r_\perp^2$ 平均值为
$$
\begin{aligned}
\overline{r_\perp^2}
&=\int_0^1[x^2(t)+y^2(t)]\,\mathrm dt\\
&=\frac13\bigl[
x_1^2+x_1x_2+x_2^2
+y_1^2+y_1y_2+y_2^2
\bigr].
\end{aligned}
$$
$H_2$ 共有 15 条等长线段，每段质量为 $M/15$。把原题的 16 个顶点按连线次序代入上式，15 个平均值的和为
$$
\sum_{j=1}^{15}\overline{r_{\perp,j}^2}
=\frac{33}{16}L^2.
$$
所以
$$
I_{2z}
=\frac{M}{15}\frac{33}{16}L^2
=\frac{11}{80}ML^2,
$$
与 $I_x+I_y$ 路线一致。

还可对无穷阶极限做检查。$H_\infty$ 等效为均匀正方形薄片，已知
$$
I_{\infty x}=I_{\infty y}=\frac1{12}ML^2,
$$
因而
$$
\boxed{I_{\infty z}=\frac16ML^2}.
$$
二阶曲线与空间填充极限的比值为
$$
\frac{I_{2z}}{I_{\infty z}}
=\frac{11/80}{1/6}
=\frac{33}{40}<1.
$$
这与 $H_2$ 尚未充分把质量分布到正方形边缘的几何图像一致。""",
        6: r"""**变式的完整解答。** 定义玻尔半径
$$
a_0=\frac{\hbar^2}{mke^2}.
$$
对给定主量子数 $n$，索莫菲尔德轨道的半长轴为
$$
a=n^2a_0,
$$
偏心率为
$$
\varepsilon=\sqrt{1-\frac{l^2}{n^2}},
$$
近、远拱点距离为
$$
r_{\min}=a(1-\varepsilon),
\qquad
r_{\max}=a(1+\varepsilon).
$$

先取 $l=n$。此时 $\varepsilon=0$，所以
$$
\boxed{r_{\min}=r_{\max}=n^2a_0},
$$
轨道为圆。再取 $l=1$：
$$
\varepsilon_1=\sqrt{1-\frac1{n^2}},
$$
$$
\boxed{
r_{\min}=n^2a_0(1-\varepsilon_1),
\qquad
r_{\max}=n^2a_0(1+\varepsilon_1)
}.
$$
为看清大 $n$ 极限，把近拱点式有理化：
$$
\begin{aligned}
r_{\min}
&=n^2a_0
\frac{1-\varepsilon_1^2}{1+\varepsilon_1}\\
&=\frac{a_0}{1+\varepsilon_1}
\longrightarrow\frac{a_0}{2}.
\end{aligned}
$$
而
$$
r_{\max}
=n^2a_0(1+\varepsilon_1)
\longrightarrow2n^2a_0.
$$
因此固定 $l=1$而令 $n\to\infty$ 时，轨道不是“越来越圆”，而是越来越狭长；只有在 $l/n$ 保持接近 $1$ 时才接近圆轨道。

拱点处径向速度为零，角动量 $L=mrv=l\hbar$ 给出
$$
v_{\rm p}=\frac{l\hbar}{mr_{\min}},
\qquad
v_{\rm a}=\frac{l\hbar}{mr_{\max}}.
$$
所以近、远拱点速度之比为
$$
\boxed{
\frac{v_{\rm p}}{v_{\rm a}}
=\frac{r_{\max}}{r_{\min}}
=\frac{1+\varepsilon}{1-\varepsilon}
}.
$$
对 $l=1$、$n\gg1$，有 $1-\varepsilon_1\simeq1/(2n^2)$，因而
$$
\frac{v_{\rm p}}{v_{\rm a}}\simeq4n^2.
$$
这也说明精细结构修正对小 $l$ 轨道更敏感：近拱点速度较大，相对论动能修正更强。""",
        7: r"""**变式的完整解答。** 以左焦点为原点、沿主轴向左的物方坐标记为 $x$。原题四顶点的无量纲纵坐标为
$$
X_D=1,
\quad X_A=\frac34,
\quad X_C=1-\frac{\sqrt3}{4},
\quad X_B=\frac{3-\sqrt3}{4}.
$$
因为
$$
0<X_B<X_C<X_A<X_D,
$$
将正方形整体沿主轴向透镜平移时，$B$ 点最先到达物方焦平面。所需平移距离为
$$
\boxed{
\Delta x_B=fX_B
=\frac{3-\sqrt3}{4}f
}.
$$

设已向透镜平移距离 $\Delta$ ，并记 $\delta=\Delta/f$。$B$ 点新的焦点坐标为
$$
X_B^{\rm new}=X_B-\delta,
$$
而其高度不变：
$$
Y_B=\frac{\sqrt3-1}{4}.
$$
牛顿成像映射给出
$$
\frac{x_B'}f=\frac1{X_B-\delta},
\qquad
\frac{y_B'}f=\frac{Y_B}{X_B-\delta}.
$$
当 $\delta\to X_B^-$ 时，分母为正且趋零：
$$
x_B'\to+\infty,
\qquad y_B'\to+\infty.
$$
物点位于焦点外侧，对应的是无穷远实像极限。当 $\delta\to X_B^+$ 时，分母变为负的无穷小量：
$$
x_B'\to-\infty,
\qquad y_B'\to-\infty.
$$
这表示越过焦平面后像变为物方虚像，坐标从正无穷经无穷远的投影点过渡到负无穷，并非在有限位置不连续跳跃。

两坐标之比始终为
$$
\frac{y_B'}{x_B'}=Y_B,
$$
所以 $B'$ 虽然在越过焦点时走向无穷远，但渐近方向保持不变。这一比值也是检查两个像坐标是否丢掉同一分母的简便方法。""",
        8: r"""**变式的完整解答。** 若不只保留小角一阶项，则可从精确力矩求振幅对周期的首阶修正。将式中的常量组合记为
$$
D=\frac{2\mu_0I^2abd(a^2+b^2)}{\pi},
\quad
A=(a^2-b^2)^2,
\quad
C=4a^2b^2.
$$
有符号力矩为
$$
\tau(\phi)
=-D\frac{\sin\phi}{A+C\sin^2\phi}.
$$
在 $\phi=0$ 附近展开
$$
\sin\phi=\phi-\frac{\phi^3}{6}+O(\phi^5),
$$
以及
$$
\frac1{A+C\sin^2\phi}
=\frac1A\left(1-\frac CA\phi^2+O(\phi^4)\right).
$$
相乘得
$$
\tau(\phi)
=-\kappa\phi
+\kappa q\phi^3+O(\phi^5),
$$
其中
$$
\kappa=\frac DA,
\qquad
q=\frac16+\frac CA
=\frac16+\frac{4a^2b^2}{(a^2-b^2)^2}.
$$
动力学方程因而是一个软化型 Duffing 振子：
$$
J_z\ddot\phi+\kappa\phi-\kappa q\phi^3=0.
$$
线性角频率为
$$
\omega_0=\sqrt{\frac\kappa{J_z}}.
$$
设小振幅为 $\Phi$，并取近似解 $\phi=\Phi\cos\omega t$。利用
$$
\cos^3\omega t
=\frac34\cos\omega t+\frac14\cos3\omega t,
$$
只对基频项做平衡：
$$
-\omega^2+\omega_0^2
-\frac34\omega_0^2q\Phi^2=0.
$$
因而
$$
\omega
\simeq\omega_0
\left(1-\frac38q\Phi^2\right),
$$
周期为
$$
\boxed{
T(\Phi)
\simeq T_0
\left(1+\frac38q\Phi^2\right)
},
\qquad
T_0=2\pi\sqrt{\frac{J_z}{\kappa}}.
$$
$q>0$，所以振幅增大时频率降低、周期增大，与“软化”力矩的几何直觉一致。""",
    },
}


def enrich_set(set_number: str, additions: dict[int, str]) -> None:
    path = (
        ROOT
        / f"蔡题{set_number}"
        / "整理版"
        / "markdown"
        / f"蔡题{set_number}_教师备课.md"
    )
    text = path.read_text(encoding="utf-8")
    matches = list(re.finditer(r"(?m)^# 第 (\d+) 题$", text))
    if [int(match.group(1)) for match in matches] != list(range(1, 9)):
        raise RuntimeError(f"蔡题{set_number}题号异常")

    front = text[: matches[0].start()]
    blocks: list[str] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start() : end].rstrip()
        number = int(match.group(1))
        marker = f"<!-- TEACHER_VARIANT_SOLVED_{set_number}_{number} -->"
        if number in additions and marker not in block:
            if "## 九、变式训练" not in block:
                raise RuntimeError(f"蔡题{set_number}第 {number} 题缺少变式训练模块")
            location = block.rfind("\n\\newpage")
            if location < 0:
                location = len(block)
            addition = additions[number].strip()
            block = (
                block[:location].rstrip()
                + f"\n\n{marker}\n\n{addition}\n"
                + block[location:]
            )
        blocks.append(block)

    path.write_text(front + "\n\n".join(blocks) + "\n", encoding="utf-8")


def main() -> None:
    for set_number, additions in ADDITIONS.items():
        enrich_set(set_number, additions)


if __name__ == "__main__":
    main()
