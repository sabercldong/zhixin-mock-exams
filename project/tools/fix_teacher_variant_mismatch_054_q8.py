from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "蔡题054" / "整理版" / "markdown" / "蔡题054_教师备课.md"

REPLACEMENT = r"""## 九、变式训练

**变式.** 若两根长直导线的电流改为同向，重新判断 $\phi=0$ 与 $\phi=\pi/2$ 的稳定性，并说明小振动是否仍然存在。

**解答.** 不能只把原结果的符号整体反转，因为改变一根长直导线的电流方向后，原来相加的两组力矩改为相减。下面逐组取矩。

沿线框平面的半宽方向取单位矢量
$$
\boldsymbol u=(\sin\phi,\cos\phi).
$$
用 $\varepsilon=\pm1$ 标记线框的两条竖边，用 $\sigma=\pm1$ 标记两根长直导线，则它们的俯视位置分别为
$$
\boldsymbol r_\varepsilon=\varepsilon b\boldsymbol u,
\qquad
\boldsymbol R_\sigma=\sigma a\boldsymbol e_y.
$$
两者距离满足
$$
\rho_{\varepsilon\sigma}^2
=|\boldsymbol R_\sigma-\boldsymbol r_\varepsilon|^2
=a^2+b^2-2\varepsilon\sigma ab\cos\phi. \tag{23}
$$

线框两条竖边的电流必然反向，可记为 $I_\varepsilon=\varepsilon I$；现在两根长直导线的电流均取 $+I$。平行电流之间的力沿两导线的连线，因此第 $(\varepsilon,\sigma)$ 组对 $z$ 轴的力矩为
$$
\tau_{\varepsilon\sigma}
=\frac{\mu_0I^2abd}{2\pi}
\frac{\sigma\sin\phi}{\rho_{\varepsilon\sigma}^2}. \tag{24}
$$
这里 $\varepsilon$ 在两处出现：一处来自线框竖边电流的方向，另一处来自位置矢量 $\boldsymbol r_\varepsilon$，两者相乘后消去。

对固定的 $\sigma$ 先把两条竖边求和：
$$
\begin{aligned}
\sum_{\varepsilon=\pm1}
\frac1{\rho_{\varepsilon\sigma}^2}
&=\frac1{a^2+b^2-2\sigma ab\cos\phi}
+\frac1{a^2+b^2+2\sigma ab\cos\phi}\\
&=\frac{2(a^2+b^2)}
{(a^2+b^2)^2-4a^2b^2\cos^2\phi}.
\end{aligned} \tag{25}
$$
式（25）与 $\sigma$ 无关，而式（24）的分子仍有一个 $\sigma$。再对两根长直导线求和，得
$$
\begin{aligned}
\tau_z
&=\sum_{\sigma=\pm1}
\sum_{\varepsilon=\pm1}
\tau_{\varepsilon\sigma}\\
&\propto(+1)+(-1)=0.
\end{aligned}
$$
所以
$$
\boxed{\tau_z(\phi)\equiv0}. \tag{26}
$$
线框上下两条横边所受安培力沿 $z$ 方向，它们对 $z$ 轴的力矩分量为零，不会改变式（26）。

因此 $\phi=0$ 和 $\phi=\pi/2$ 都不是有回复刚度的稳定平衡，而是中性平衡；事实上任意 $\phi$ 都是中性平衡。线性化方程只剩
$$
J_z\ddot\phi=0,
$$
其解为
$$
\phi(t)=\phi(0)+\dot\phi(0)t.
$$
系统没有简谐回复项，故
$$
\boxed{\omega_0=0},
$$
不存在有限周期的小振动；形式上可说 $T\to\infty$。
"""


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    match = re.search(r"(?m)^# 第 8 题$", text)
    if match is None:
        raise RuntimeError("找不到第 8 题")
    ninth = text.find("\n## 九、变式训练\n", match.start())
    if ninth < 0:
        raise RuntimeError("第 8 题缺少变式训练")
    updated = text[: ninth + 1] + REPLACEMENT.rstrip() + "\n"
    SOURCE.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
