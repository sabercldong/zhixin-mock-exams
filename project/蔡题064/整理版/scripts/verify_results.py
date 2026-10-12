from __future__ import annotations

from fractions import Fraction


def check_equal(name: str, actual: Fraction, expected: Fraction) -> None:
    if actual != expected:
        raise AssertionError(f"{name}: {actual} != {expected}")
    print(f"[PASS] {name}: {actual}")


def main() -> None:
    # 第 2 题：特征多项式的常数项在 Omega^2=ag 时变号。
    # 令 A=ag, W=Omega^2，常数项为 (W-A)(W+A/2)。
    A = Fraction(6)
    below = (Fraction(5) - A) * (Fraction(5) + A / 2)
    above = (Fraction(7) - A) * (Fraction(7) + A / 2)
    assert below < 0 < above
    print("[PASS] 第 2 题稳定性分界：Omega^2=ag")

    # 第 3 题：过渡段与双圆柱段的功分别为 1/2 和 1 个 mu*m*g*l。
    energy_gain = Fraction(1, 2) + 1
    check_equal("第 3 题总功系数", energy_gain, Fraction(3, 2))

    # 第 7 题：用 R0=rl, E=kl^2 作无量纲系数核验。
    r_diag_child = Fraction(5, 21)
    r_middle = Fraction(1, 3)
    emf_eff = Fraction(1) - 4 * Fraction(1, 18)
    r_top = 4 * (r_middle + r_diag_child)
    i_coeff = emf_eff / r_top
    check_equal("第 7 题中段电流系数", i_coeff, Fraction(49, 144))

    p2_coeff = 4 * (r_middle + r_diag_child) * i_coeff**2
    check_equal("第 7 题顶层环流功率系数", p2_coeff, Fraction(343, 1296))

    p_total_coeff = p2_coeff / (1 - Fraction(4, 27))
    check_equal("第 7 题总功率系数", p_total_coeff, Fraction(343, 1104))

    # 第 8 题：公共支路中电流为 (a+b)I1，折算电阻必为正。
    a, b = Fraction(2), Fraction(4)
    r1, r2, r3, rp = map(Fraction, (3, 5, 7, 11))
    denominator = rp + a * a * r2 + b * b * r3 + (a + b) ** 2 * r1
    assert denominator > 0
    print(f"[PASS] 第 8 题折算分母为正：{denominator}")


if __name__ == "__main__":
    main()
