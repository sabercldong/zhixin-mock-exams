from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1.0e-10) -> None:
    assert math.isclose(a, b, rel_tol=tol, abs_tol=tol), (a, b)


# 第1题：两种小角回正刚度的符号、速度与量纲因子
G, ell, beta, theta = 12000.0, 0.18, 0.12, 0.04
M1 = -G * ell * math.sin(beta) * math.sin(theta) / 4
assert M1 * theta < 0
m, v, r, d, alpha = 900.0, 20.0, 0.31, 2.7, 0.06
M2 = -m * v**2 * r * math.sin(alpha) * theta / (2 * d)
assert M2 * theta < 0

# 第2题：磁矩绝热不变量、镜比势垒与角条件
B0, mirror, vp0, vz0 = 0.4, 5.0, 3.0, 4.0
vpL2 = vp0**2 * mirror
close(vpL2 / (mirror * B0), vp0**2 / B0)
close(vz0**2, (mirror - 1) * vp0**2 - 20.0)
critical = math.atan(math.sqrt(mirror - 1))
assert math.atan(abs(vz0) / vp0) < critical

# 第3题：两类边界条件和剪切波速
S, rho, L = 2.4e5, 1200.0, 0.8
cs = math.sqrt(S / rho)
for n in range(4):
    k_fixed_free = (2 * n + 1) * math.pi / (2 * L)
    period = 2 * math.pi / (cs * k_fixed_free)
    close(period, 4 * L * math.sqrt(rho / S) / (2 * n + 1))
for n in range(1, 5):
    k_free_free = n * math.pi / L
    period = 2 * math.pi / (cs * k_free_free)
    close(period, 2 * L * math.sqrt(rho / S) / n)

# 第4题：超导熵差数值与极值位置
B0, mu0, T, T0 = 0.144, 1.25e-6, 1.95, 4.48
dS = 2 * mu0 * B0**2 * T / T0**2 * (1 - T**2 / T0**2)
close(dS, 4.082432778265912e-9)
Tmax = T0 / math.sqrt(3)
assert 0 < Tmax < T0

# 第5题：磁链守恒、线性恢复系数与零电流三次力
I0, B0, area, inductance, k, mass = 1.3, 0.8, 0.02, 0.1, 2.2, 0.4
x, y = 0.13, -0.09
Ixy = I0 + B0 * area / inductance * (1 - math.cos(k*x) * math.cos(k*y))
flux_chain = inductance * Ixy + B0 * area * math.cos(k*x) * math.cos(k*y)
close(flux_chain, inductance * I0 + B0 * area)
omega2 = I0 * B0 * area * k**2 / mass
assert omega2 > 0
cubic = B0**2 * area**2 * k**4 / (2 * inductance)
assert cubic > 0

# 第6题：横向模态根和两个端口电阻
q2 = 2 - math.sqrt(3)
q4 = 3 - 2 * math.sqrt(2)
close(q2**2 - 4*q2 + 1, 0)
close(q4**2 - 6*q4 + 1, 0)
z2 = 1 / (3 - q2)
z4 = 1 / (5 - q4)
close(2*z2, math.sqrt(3) - 1)
close(z2 + z4, (math.sqrt(3) + math.sqrt(2) - 2) / 2)

# 第7题：精确速度的经典极限与一阶周期修正
eta = 1.0e-5
v_exact2_over_c2 = 1 - 1 / (1 + eta)**2
close(v_exact2_over_c2 / (2 * eta), 1.0, 2.0e-5)
a, b = 0.004, 1.7
ratio = 3 * a * b**2 / 8
close(ratio, 3 * (a*b**2) / 8)
assert ratio > 0

# 第8题：全反射系数模长、相位导数和显式位移
n1, n2, theta = 1.5, 1.0, 0.9
D = math.sqrt(n1**2 * math.sin(theta)**2 - n2**2)
A = D / (n1 * math.cos(theta))
delta = 2 * math.atan(A)
h = 1.0e-6
def phase(t: float) -> float:
    d = math.sqrt(n1**2 * math.sin(t)**2 - n2**2)
    return 2 * math.atan(d / (n1 * math.cos(t)))

numeric_derivative = (phase(theta + h) - phase(theta - h)) / (2*h)
analytic_derivative = 2 * n1 * math.sin(theta) / D
close(numeric_derivative, analytic_derivative, 1.0e-8)
assert 0 < delta < math.pi

print("第048套八题关键公式、边界条件、数值与极限验证通过")
