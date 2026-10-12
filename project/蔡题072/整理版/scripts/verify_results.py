from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1.0e-10) -> None:
    scale = max(1.0, abs(a), abs(b))
    assert abs(a - b) <= tol * scale, (a, b)


def verify_q1() -> None:
    assert math.comb(10, 2) == 45
    mass_big, mass_small = 1.0e6, 1.0e-3
    alpha = math.atan(math.sqrt(mass_small / mass_big))
    ratio = math.pi / alpha
    assert 99345.8 < ratio < 99345.9
    assert math.ceil(ratio) - 1 == 99345

    # 任选一组碰前速度，核验二体弹性碰撞公式同时守恒动量和动能。
    v_big, v_small = -3.0, 1.25
    v_big_after = ((mass_big - mass_small) * v_big
                   + 2.0 * mass_small * v_small) / (mass_big + mass_small)
    v_small_after = (2.0 * mass_big * v_big
                     + (mass_small - mass_big) * v_small) / (mass_big + mass_small)
    close(mass_big * v_big + mass_small * v_small,
          mass_big * v_big_after + mass_small * v_small_after)
    close(mass_big * v_big**2 + mass_small * v_small**2,
          mass_big * v_big_after**2 + mass_small * v_small_after**2)


def verify_q2() -> None:
    sigma, epsilon, h, d = 2.3, 4.7, 10.0, 0.01
    exact = sigma / (2.0 * math.pi * epsilon) * math.log1p(d / h)
    leading = sigma * d / (2.0 * math.pi * epsilon * h)
    assert abs(exact - leading) / exact < 6.0e-4
    # 每个半无限面的竖直积分都等于 pi/2，与高度无关。
    for height in (0.3, 2.0, 17.0):
        close(math.atan(1.0e9 / height), math.pi / 2.0, 2.0e-8)


def verify_q3() -> None:
    half_length, sag = 40.0, 30.0
    a = (half_length**2 - sag**2) / (2.0 * sag)
    close(a, 35.0 / 3.0)
    u = math.acosh(1.0 + sag / a)
    close(u, math.log(7.0))
    close(a * math.sinh(u), half_length)
    span = 2.0 * a * u
    close(span, (70.0 / 3.0) * math.log(7.0))
    close(a, 35.0 / 3.0)  # 最低点曲率半径


def verify_q4() -> None:
    # 对多条过固定点的弦数值求端点切线交点，核验固定极线。
    a, b = 3.0, 2.0
    p, q = 0.6, 0.4
    for angle in (0.13, 0.67, 1.21, 2.02):
        dx, dy = math.cos(angle), math.sin(angle)
        aa = dx * dx / a**2 + dy * dy / b**2
        bb = 2.0 * (p * dx / a**2 + q * dy / b**2)
        cc = p * p / a**2 + q * q / b**2 - 1.0
        disc = bb * bb - 4.0 * aa * cc
        roots = ((-bb - math.sqrt(disc)) / (2.0 * aa),
                 (-bb + math.sqrt(disc)) / (2.0 * aa))
        x1, y1 = p + roots[0] * dx, q + roots[0] * dy
        x2, y2 = p + roots[1] * dx, q + roots[1] * dy
        # 两切线 A/a^2*x+B/b^2*y=1 的交点。
        det = x1 * y2 / (a**2 * b**2) - x2 * y1 / (a**2 * b**2)
        if abs(det) < 1.0e-9:
            continue
        xi = ((y2 / b**2) - (y1 / b**2)) / det
        eta = ((x1 / a**2) - (x2 / a**2)) / det
        close(p * xi / a**2 + q * eta / b**2, 1.0)


def verify_q5() -> None:
    l1, mutual = 2.7, 0.4
    l2 = 2.0 * l1 + 2.0 * mutual
    lc_flux = 3.0 * l1 + 6.0 * mutual
    lc_eliminated = 3.0 * (l2 - l1)
    close(lc_flux, lc_eliminated)
    assert abs(mutual) <= l1


def verify_q6() -> None:
    m, mass_cu = 0.030, 0.0635
    c_cu, c_s, c_l = 24.44, 128.0, 153.0
    t_cu, t_pb, t_m, latent = 300.15, 303.15, 600.61, 2.045e4
    q_heat = c_cu * (t_m - t_cu) + m * c_s * (t_m - t_pb)
    q_full = q_heat + m * latent
    close(q_heat, 8485.4888)
    close(q_full, 9098.9888)

    q_fixed = 0.5 * m * 850.0**2
    t_fixed = t_m + (q_fixed - q_full) / (c_cu + m * c_l)
    close(t_fixed, 660.49671029969)

    reduced = m * mass_cu / (m + mass_cu)
    q_free = 0.5 * reduced * 850.0**2
    t_free = ((q_free + c_cu * t_cu + m * c_s * t_pb)
              / (c_cu + m * c_s))
    entropy_free = (c_cu * math.log(t_free / t_cu)
                    + m * c_s * math.log(t_free / t_pb))
    close(q_free, 7360.227272727273)
    close(t_free, 560.8199884274142)
    close(entropy_free, 17.640136252344917)

    density, epsilon, charge, c_final = 11340.0, 8.8541878128e-12, 4.0e-5, 1.5e-12
    radius = (3.0 * m / (4.0 * math.pi * density)) ** (1.0 / 3.0)
    c_initial = 4.0 * math.pi * epsilon * radius
    q_part = (0.5 * m * 750.0**2
              + charge**2 / (2.0 * c_initial)
              - charge**2 / (2.0 * c_final))
    melted = (q_part - q_heat) / latent
    entropy_part = (c_cu * math.log(t_m / t_cu)
                    + m * c_s * math.log(t_m / t_pb)
                    + melted * latent / t_m)
    close(radius, 8.57972162225161e-3)
    close(c_initial, 9.546227738725547e-13)
    close(q_part, 8742.194023540516)
    close(melted, 0.012552822667017866)
    close(entropy_part, 20.006019766267027)


def verify_q7() -> None:
    a, b, delta, wavelength = 2.4, 3.7, 0.012, 5.5e-7
    source_gap = 2.0 * a * delta
    spacing = wavelength * (a + b) / source_gap
    close(spacing, wavelength * (a + b) / (2.0 * a * delta))
    h = 0.0013
    y0 = -b * h / a
    path_difference = 2.0 * delta * (a * y0 + b * h) / (a + b)
    close(path_difference, 0.0)
    spacing_double = wavelength * (a + b) / (4.0 * a * delta)
    close(spacing_double, spacing / 2.0)


def verify_q8() -> None:
    avogadro, molar_volume = 6.02e23, 22.4e-3
    length = (molar_volume / avogadro) ** (1.0 / 3.0)
    close(length, 3.340240395e-9, 1.0e-8)
    h_planck, mass, d = 6.62607015e-34, 1.6749275e-27, 2.3e-14
    pressure_exact = h_planck**2 / (4.0 * mass * d**5)
    energy = 3.0 * h_planck**2 / (8.0 * mass * d**2)
    # 对 E(d) 与 V(d) 作中心差分，核验虚功导数。
    step = d * 1.0e-5
    ep = 3.0 * h_planck**2 / (8.0 * mass * (d + step)**2)
    em = 3.0 * h_planck**2 / (8.0 * mass * (d - step)**2)
    vp, vm = (d + step)**3, (d - step)**3
    pressure_fd = -(ep - em) / (vp - vm)
    close(pressure_fd, pressure_exact, 1.0e-8)
    assert energy > 0.0 and pressure_exact > 0.0


def main() -> None:
    checks = [verify_q1, verify_q2, verify_q3, verify_q4,
              verify_q5, verify_q6, verify_q7, verify_q8]
    for check in checks:
        check()
        print(f"PASS {check.__name__}")


if __name__ == "__main__":
    main()
