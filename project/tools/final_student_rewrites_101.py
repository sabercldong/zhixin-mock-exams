from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


ADDITIONS: dict[str, dict[int, str]] = {
    "045": {
        1: r"""**径向速度的数值链条。** 角速度 $\omega=2\pi/T$，日地间距由
$$
L^3=\frac{G(M_S+M_E)}{\omega^2}
$$
求得。共同质心条件
$$
M_Sr_S=M_Er_E,\qquad r_S+r_E=L
$$
给出
$$
r_S=\frac{M_E}{M_S+M_E}L,\qquad v_S=\omega r_S.
$$
地球轨道速度约 $3.0\times10^4\ \mathrm{m\,s^{-1}}$，质量比约 $3.0\times10^{-6}$，因而太阳速度应为 $9\times10^{-2}\ \mathrm{m\,s^{-1}}$ 量级。光谱仪测到的是 $v_S\sin i$，题问最大值时投影因子取 $1$。""",
        4: r"""**第三种平衡的受力—几何转换。** 销钉 $C$ 两侧绳张力等大，合力沿 $\angle ACB$ 的角平分线。二力平衡要求该作用线通过质心 $H$，故
$$
\frac{AH}{HB}=\frac{AC}{CB}.
$$
左边由质心定义等于 $m_2/m_1$，右边还满足 $AC+CB=2a$。解出绳段后必须检查 $AC>0,CB>0$ 以及与 $AB=2c$ 的三角形不等式，这些条件共同产生质量比的下限。小振动中的重力势能是二阶量，因而杆长和绳长约束也必须展开到二阶。""",
        7: r"""**双表面张力的统一用法。** 肥皂膜有两个表面，有效边界张力为 $2\sigma$。一维微元的横波方程因而是
$$
\rho z_{tt}=2\sigma z_{xx},\qquad c=\sqrt{\frac{2\sigma}{\rho}}.
$$
对半径 $x$ 的水平圆膜内区，圆周上张力的竖直合力为
$$
2\sigma(2\pi x)h'(x),
$$
它平衡膜内重量 $\rho g\pi x^2$。故 $h'(x)=\rho gx/(4\sigma)$，用 $h(r)=0$ 积分得
$$
h(x)=\frac{\rho g}{8\sigma}(r^2-x^2).
$$
波速中的 $\sqrt2$ 和下沉式分母中的 $8$ 都来自双表面，不能在两处重复或遗漏。""",
    },
    "046": {
        6: r"""**亮度式的退化检查。** 正文的亮度表达式中，$J_S$ 负责发光面环带到投影环带的面积变换，$c_i/c$ 负责折射前后立体角变换，$(L'/L)^2$ 负责传播户型面积变换，$\cos\beta$ 则来自亮度定义中的投影面积。当 $n\to1$ 时折射消失，应有
$$
P(q)\to q,\qquad J_S\to1,\qquad L'/L\to1,
$$
整式退化为平面余弦发光体的均匀亮度。若该极限不成立，通常是某个雅可比应取倒数。""",
        8: r"""**从船上时间到地面航程。** 巡航时间 $\tau$ 在飞船固有系中给出，地面系时间为 $t=\gamma\tau$，所以
$$
S=vt=\beta\gamma c\tau.
$$
加速、减速两段共用总质量比 $101$，两段等大快速度给出
$$
2\chi=\frac uc\ln101,
\qquad
\beta=\tanh\chi,\qquad \gamma=\cosh\chi.
$$
因 $\beta\gamma=\sinh\chi$，
$$
S=c\tau\sinh\left(\frac{u}{2c}\ln101\right).
$$
用光年和年为单位时 $c=1\ \mathrm{ly/yr}$，可直接代入 $\tau=15\ \mathrm{yr}$。""",
    },
    "047": {
        7: r"""**离地和滑动都要在全区间检查。** 地面支持力由
$$
N-mg=m\ddot y_C
$$
给出。把 $\ddot y_C$ 改写成 $c=\cos\theta$ 的函数后，$N(c)$ 必须在 $0\le c\le1$ 上始终非负。临界 $\lambda_c$ 是 $N(c)$ 在区间内恰好触零的参数，不能只检查初始点。同理，不滑动要求
$$
\mu\ge
\max_{0\le c\le1}
\frac{|m\ddot x_C|}{m(g+\ddot y_C)}.
$$
分母在接近离地时可变得很小，因而最大值可出现在区间内部，这是 $\mu_2$ 需要真正极值计算的原因。""",
        8: r"""**两组速度根必须成对回代。** 给定 $\beta$ 时，能量守恒是 $\dot x,\dot\beta$ 的二次方程，正则动量守恒是二者的线性方程。消去 $\dot x$ 后会得到两个 $\dot\beta$ 根，每个根都应分别代回
$$
3\dot x-r\dot\beta\cos\beta
=\frac{qBr}{m}\cos\beta
$$
求它自己的 $\dot x$。不能把较大的 $\dot\beta$ 与另一分支的较大 $\dot x$ 交叉配对。小球再次相对圆环静止时 $\dot\beta=0$，两个守恒式消去 $\dot x$ 后才得 $\lambda$ 与 $c=\cos\beta_c$ 的方程。""",
    },
    "048": {
        1: r"""**回正力矩的对称性检查。** 轮架绕倾斜主销转过 $\theta$ 时，车轮中心高度随 $\theta$ 变化。对一个车轮，支持力为 $G/4$，重力势能对 $\theta$ 的负导数给出
$$
M_1=-\frac{Gl}{4}\sin\beta\sin\theta.
$$
当 $\theta=0$ 时力矩必须为零，小角展开为
$$
M_1\simeq-\frac{Gl\sin\beta}{4}\theta,
$$
负号表明它指向中立位置。若误写为 $\cos\theta$，中立位置仍有非零力矩，立即违反左右对称性。""",
        2: r"""**磁矩绝热不变量。** 回旋周期远短于沿 $z$ 方向运动的时标，因而
$$
\mu_m=\frac{mV_\perp^2}{2B_z}=\text{常量}.
$$
这直接给出
$$
V_\perp^2(z)=V_\perp^2(0)\frac{B_z(z)}{B_z(0)}.
$$
磁力不做功，总动能守恒，故
$$
\frac12mV_z^2+\mu_mB_z(z)
=\frac12m[V_z^2(0)+V_\perp^2(0)].
$$
在 $z=\pm L$ 的镜点令 $V_z=0$、$B_z=MB_z(0)$，便得约束与吸收的分界条件。""",
        7: r"""**相对论周期的低能展开。** 设 $\Delta V=V(b)-V(x)$，能量守恒给出 $\gamma=1+\Delta V/(mc^2)$，因而
$$
v(x)=c\sqrt{1-\left(1+\frac{\Delta V}{mc^2}\right)^{-2}}.
$$
对称势中的周期为
$$
T=4\int_0^b\frac{dx}{v(x)}.
$$
对 $V=kx^2/2$ 保留 $1/c^2$ 的最低修正，再用 $x=b\sin u$ 消去端点根式，得
$$
T=2\pi\sqrt{\frac mk}
\left(1+\frac38ab^2\right).
$$
因 $ab^2=E_{k0}/(mc^2)=\eta$，修正项与主项之比为 $3\eta/8$。""",
        8: r"""**反射相位梯度决定横向位移。** 全反射系数的模为 $1$，但相位 $\varphi$ 随入射角变化。由两个相近角度平面波叠加可得包络位移
$$
\Delta=-\frac{d\varphi}{dk_x}
=-\frac{d\varphi/d\theta}
{d(k\sin\theta)/d\theta}
=-\frac1{k\cos\theta}\frac{d\varphi}{d\theta}.
$$
正负号依赖界面坐标和相位约定，但位移大小必须由反射相位对横向波数的导数决定，不能由单条几何光线直接得出。""",
    },
    "050": {
        6: r"""**由初末态动量复核试管终速。** 去掉左壁后，最终离开的分子只保留 $v_x<0$ 半空间分布。麦克斯韦分布给出
$$
\langle|v_x|\rangle
=\sqrt{\frac{2kT}{\pi m}}
=\frac{v_T}{\sqrt\pi}.
$$
气体终态总动量为 $-Nmv_T/\sqrt\pi$，初始总动量为零，因而很重试管的终速为
$$
V=\frac{Nmv_T}{M\sqrt\pi}.
$$
它与有限时间冲量式在 $t\to\infty$ 的极限一致，因而检查了速度积分中的 $\sqrt\pi$ 因子。""",
        8: r"""**同时事件方程的选根条件。** 记 $s=at_A/c$、$\delta=a(t_B-t_A)/c$、$\lambda=al/c^2$。将右端世界线代入左端瞬时共动系的同时条件，会得到关于 $\delta$ 的二次方程。物理根必须满足
$$
\lambda\to0\quad\Longrightarrow\quad\delta\to0,
$$
另一根不与局部同时面连续，应舍去。选根后的共动系长度为
$$
L_A=\frac{c^2}{a}\frac{\delta}{s}\sqrt{1-s^2}.
$$
$c^2/a$ 提供长度量纲，其余因子均无量纲，可用于检查化简过程。""",
    },
    "051": {
        2: r"""**竖直振动与左右摇摆的回复机制不同。** 船体下沉小量 $z$ 时，新增排水体积为水线宽度乘船长再乘 $z$，所以浮力增量 $\Delta F_b=K_zz$ 中的 $K_z$ 由平衡水线宽度决定，周期是 $T_1=2\pi\sqrt{M/K_z}$。左右摇摆时，题设近似使重力与浮力大小相等，但作用线分离形成回复力偶。因此 $T_2$ 必须使用题目指定的绕圆心转动惯量 $I_O$，不能将其当成质心单摆。""",
        4: r"""**科里奥利项决定非共线点的稳定性。** 在 $L_4$ 或 $L_5$ 附近令偏移为 $(u,v)$，线性运动方程必须保留 $\mp2\Omega\dot v$、$\pm2\Omega\dot u$。代入 $e^{\lambda t}$ 并令行列式为零，得
$$
\lambda^4+\Omega^2\lambda^2
+\frac{27}{4}\Omega^4q(1-q)=0.
$$
令 $z=\lambda^2$，稳定要求两个 $z$ 根均为负实数，故判别式给出
$$
1-27q(1-q)\ge0.
$$
即 $q(1-q)\le1/27$。删掉科里奥利项会得到相反的稳定结论。""",
        5: r"""**径向电容无电流不等于棱上无环流。** 对任一顶点，与其相连的三条棱电动势的代数和由正四面体对称性为零。因此没有净电流流入任一顶点，体心与顶点间的电容不会持续充电。但六条棱中仍可形成节点净注入为零的环流。对独立三角面写法拉第回路方程，再与节点方程联立，才能唯一确定 $AD,AB$ 电流。平均功率使用峰值复振幅时应写 $\overline P=R|\widetilde I|^2/2$。""",
        7: r"""**分离点的法向方程。** 参数导数给出
$$
\frac{dy}{dx}=-\tan\varphi,
\qquad
\rho=3|\sin\varphi\cos\varphi|.
$$
从 $A$ 静止释放后，能量守恒给出 $v^2=2g(y_A-y)$。沿曲线法向列方程，在支持力降为零时有重力法向分量恰好提供 $mv^2/\rho$。与三角恒等式联立，得
$$
\cos\varphi_C=-\sqrt{\frac25},
\qquad
\sin\varphi_C=-\sqrt{\frac35}.
$$
时间必须积分 $dt=ds/v$，其中 $ds=\sqrt{x'^2+y'^2}\,d\varphi$，不能把水平位移 $dx$ 当成弧长。""",
    },
    "053": {
        3: r"""**电磁反馈表现为额外惯量。** 壳面电流产生的内部磁场与 $\omega$ 成正比，所以角加速度 $\beta$ 使磁通量变化，再由法拉第定律产生环向电场。该电场对面电荷的总力矩可写成
$$
\tau_{\rm em}=-I_{\rm em}\beta,
\qquad
I_{\rm em}=\frac{\mu_0Q^2R^2}{4\pi l}.
$$
因而机械方程为
$$
(I+mR^2+I_{\rm em})\beta=mgR.
$$
反馈力矩不是恒定阻力，而是使系统表现出更大的有效转动惯量。""",
        4: r"""**两种电桥的对称性不可混用。** 图（a）中上、下 $L$--$C$ 支路完全相同，中点等势，故桥臂无电流。每条支路阻抗
$$
Z_b=i\left(\omega L-\frac1{\omega C}\right),
$$
两支路并联后必须除以 $2$。图（b）在 $\omega_0=1/\sqrt{LC}$ 时有 $Z_L=-Z_C$，但中点不再等势。规定桥臂电流向上，联立节点和回路方程得
$$
\widetilde I_1=-i\frac rR\widetilde I.
$$
因子 $-i$ 表示相位滞后 $\pi/2$，不是简单的电流反向。""",
        8: r"""**感生电场必须按半径分段。** 当 $x<r$，法拉第回路包围磁通量 $\pi x^2B$，故
$$
E_\varphi=-\frac{x}{2}\dot B.
$$
当 $x>r$，包围的变化磁通量固定为 $\pi r^2B$，故
$$
E_\varphi=-\frac{r^2}{2x}\dot B.
$$
杆上 $dq=\lambda dx$，力矩微元 $d\tau=xE_\varphi dq$，所以半杆积分必须在 $x=r$ 拆成两段，再乘两根对称半杆的因子 $2$。对时间积分时 $\int-\dot B,dt=B_0$，因此最终角速度只与磁场总变化量有关。""",
    },
}


def enrich(set_number: str, additions: dict[int, str]) -> None:
    path = ROOT / f"蔡题{set_number}" / "整理版" / "markdown" / f"蔡题{set_number}_教师备课.md"
    text = path.read_text(encoding="utf-8")
    matches = list(re.finditer(r"(?m)^# 第 (\d+) 题$", text))
    front = text[: matches[0].start()]
    blocks: list[str] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start() : end].rstrip()
        question = int(match.group(1))
        marker = f"<!-- CORE_101_FINAL_{set_number}_{question} -->"
        if question in additions and marker not in block:
            sixth = block.find("\n## 六、关键洞察")
            if sixth < 0:
                raise RuntimeError(f"第{set_number}套第{question}题缺少第六模块")
            block = block[:sixth].rstrip() + f"\n\n{marker}\n\n{additions[question].strip()}\n" + block[sixth:]
        blocks.append(block)
    path.write_text(front + "\n\n".join(blocks) + "\n", encoding="utf-8")


def main() -> None:
    for set_number, additions in ADDITIONS.items():
        enrich(set_number, additions)
        print(f"第 {set_number} 套终轮核心解析完成")


if __name__ == "__main__":
    main()
