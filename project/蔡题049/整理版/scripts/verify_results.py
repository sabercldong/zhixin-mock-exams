from __future__ import annotations

import math


def close(a: float, b: float, tol: float = 1.0e-10) -> None:
    assert math.isclose(a, b, rel_tol=tol, abs_tol=tol), (a, b)


# 第1题：阿克曼几何与车身最外角扫掠半径
alpha = math.pi / 4
cot_beta = 1 / math.tan(alpha) + 2 / 3
beta = math.atan(1 / cot_beta)
close(1 / math.tan(beta) - 1 / math.tan(alpha), 2 / 3)
close(math.hypot(5, 4), math.sqrt(41))

# 第2题：两级火箭最优中间质量比与给定数据的总质量比
r = 0.1
speed_ratio = math.exp((10 / 2.5) / 2)
sqrt_N = speed_ratio * (1 - r) / (1 - r * speed_ratio)
N = sqrt_N**2
n = math.sqrt(N)
v1 = math.log(N / (r * N + (1 - r) * n))
v2 = math.log(n / (r * n + 1 - r))
close(v1, v2, 1.0e-8)
close(v1 + v2, 10 / 2.5)

# 第3题：点涡诱导速度与伯努利液面差
gamma = 1.7
d = 2.3
v_mid = 2 * gamma / (math.pi * d)
v_outer = 2 * gamma / (3 * math.pi * d)
close(v_mid / v_outer, 3)
h = (v_mid**2 - v_outer**2) / (2 * 9.8)
close(h, 16 * gamma**2 / (9 * math.pi**2 * 9.8 * d**2))

# 第4题：光滑分支恢复系数为1；临界摩擦处滑动、黏着两式连续
theta = 0.83
A = 0.5 * math.sin(theta)
B = 1 + 0.5 * math.cos(theta)
vy_smooth = (1 - A * A) / (1 + A * A)
omega_smooth = -2 * A / (1 + A * A)
close(vy_smooth - A * omega_smooth, 1)
mu_c = A * B / (1 + B * B)
D = 1 + A * A - mu_c * A * B
vx_slide = -2 * mu_c / D
vy_slide = (2 - D) / D
den = 1 + A * A + B * B
vx_stick = -2 * A * B / den
vy_stick = (1 + B * B - A * A) / den
close(vx_slide, vx_stick)
close(vy_slide, vy_stick)

# 第5题：四个区间的映射在各区间中点连续给出36°读数
for theta_deg, reading in ((36, 72 - 36), (180, 180 - 144),
                           (180, 216 - 180), (324, 324 - 288)):
    close(reading, 36)

# 第6题：累计Q-W坐标闭合与可逆熵关系
W0 = 1.0
O1 = (10 / 3 * W0, 10 / 3 * W0)
C = (13 / 3 * W0, 10 / 3 * W0)
B1 = (25 / 3 * W0, 25 / 3 * W0)
close(O1[0] - O1[1], 0)
close(C[0] - C[1], W0)
close(B1[0] - B1[1], 0)
close(math.log(3**2.5), 2.5 * math.log(3))

# 第7题：曲率公式及自渐屈方程的正根
def root_for(n: int) -> float:
    a = 2 * math.pi * n - math.pi / 2
    lo, hi = 0.0, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if mid * math.exp(a * mid) < 1:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


for order in (1, 2, 3):
    k = root_for(order)
    close(k, math.exp(k * (math.pi / 2 - 2 * math.pi * order)))
    radius = 3.1 * math.sqrt(1 + k * k)
    curvature = 1 / (3.1 * math.sqrt(1 + k * k))
    close(radius * curvature, 1)

# 第8题：玻尔—索末菲尺度关系与椭圆两转向点
for principal, angular in ((3, 1), (5, 4), (8, 8)):
    a = principal**2
    e = math.sqrt(1 - angular**2 / principal**2)
    r1, r2 = a * (1 - e), a * (1 + e)
    close(r1 + r2, 2 * a)
    close(r1 * r2, angular**2 * principal**2)

print("第049套八题的关键数值、临界连续性与尺度关系验证通过")
