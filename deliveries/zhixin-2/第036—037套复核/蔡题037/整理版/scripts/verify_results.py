from __future__ import annotations

import math

import sympy as sp


def close(actual: float, expected: float, tolerance: float = 1e-6) -> None:
    assert math.isclose(actual, expected, rel_tol=tolerance, abs_tol=tolerance), (
        actual,
        expected,
    )


def verify_question_1() -> None:
    # Literal normal impact, including translation and rotation; no reset assumption.
    L,g,l,phi,m=2.3,9.8,.12,.04,1.7
    a=l/2; Ic=m*L*L/12; Ip=Ic+m*a*a; eta=m*a*a/Ic
    close(math.sqrt(2*Ip*phi/(m*g*a)),L*math.sqrt(phi/(3*g*l))*math.sqrt(1+eta))
    for e in [0,.4,1]:
        Om=1.3;J=2*m*a*(1+e)*Om/(1+eta)
        vc=-a*Om+J/m;om=-Om+a*J/Ic
        close(vc+a*om,2*e*a*Om)
        kin=.5*(m*a*a+Ic)*Om*Om; kout=.5*m*vc*vc+.5*Ic*om*om
        close((kin-kout)/kin,4*eta*(1-e*e)/(1+eta)**2)
        if e>0: assert vc+a*om>0 and vc-a*om>0


    eta=.03;a=.2;Om=.04;g=9.8;Ic=a*a/eta
    vc=a*Om*(3-eta)/(1+eta);omega=Om*(3*eta-1)/(1+eta)
    tq=4*a*Om/g;tp=8*a*Om*(1-eta)/(g*(1+eta));assert tq<tp
    y=vc*tq-g*tq*tq/2
    close(y+a*omega*tq,0);assert y-a*omega*tq>0
    j=4*a*Om/(1+eta)
    close(omega+a*j/Ic,Om*(7*eta-1)/(1+eta))
    close(vc-g*tq+j,a*Om*(3-5*eta)/(1+eta))


def verify_question_2() -> None:
    mu,I,r=4*math.pi*1e-7,3,.2
    close(mu*(-I)/(2*math.pi*r),-3e-6)  # upper feed wire points down
    # 载流棒力矩的一阶系数和频率系数。
    x, L, d, theta = sp.symbols("x L d theta", positive=True)
    expansion = x / d + x**2 * theta / d**2
    integral = sp.integrate(expansion, (x, -L / 2, L / 2))
    assert sp.simplify(integral - L**3 * theta / (12 * d**2)) == 0

    mu0, I, Ip, m = sp.symbols("mu0 I Ip m", positive=True)
    torque_coefficient = mu0 * I * Ip * L**3 / (24 * sp.pi * d**2)
    inertia = m * L**2 / 12
    omega_squared = sp.simplify(torque_coefficient / inertia)
    expected = mu0 * I * Ip * L / (2 * sp.pi * m * d**2)
    assert sp.simplify(omega_squared - expected) == 0


def verify_question_3() -> None:
    n = sp.symbols("n")
    polynomial = 12948 * n**2 + 7499 * n - 33005
    roots = sp.nroots(polynomial)
    physical = max(float(sp.re(root)) for root in roots)
    close(physical, 1.33303984465660, 1e-10)

    lam = 0.195
    p_over_r = 2 + 1 / (2 * (physical - 1) + 1 / lam)
    v_over_r = -lam / (2 * lam - 1) - 2
    close(1 / p_over_r + physical / v_over_r, 1 - physical, 1e-10)

    variant_roots = sp.solve(4 * n**2 - n - 9, n)
    physical_variant = max(float(root) for root in variant_roots)
    close(physical_variant, (1 + math.sqrt(145)) / 8, 1e-10)


def verify_question_4() -> None:
    l1, l2, g, w2 = sp.symbols("l1 l2 g w2", positive=True)
    characteristic = l1 * l2 * w2**2 - 2 * g * (l1 + l2) * w2 + 2 * g**2
    roots = sp.solve(characteristic, w2)
    expected = [
        g * (l1 + l2 - sp.sqrt(l1**2 + l2**2)) / (l1 * l2),
        g * (l1 + l2 + sp.sqrt(l1**2 + l2**2)) / (l1 * l2),
    ]
    for actual, target in zip(roots, expected):
        assert sp.simplify(actual - target) == 0

    ratio = sp.sqrt((2 + sp.sqrt(2)) / (2 - sp.sqrt(2)))
    assert sp.simplify(ratio - (1 + sp.sqrt(2))) == 0


def verify_question_5() -> None:
    radius_ratio = 11.86 ** (2 / 3)
    earth_radius = 1.50e11
    earth_period = 365 * 24 * 3600
    earth_speed = 2 * math.pi * earth_radius / earth_period
    perihelion_speed = earth_speed * math.sqrt(
        2 * radius_ratio / (1 + radius_ratio)
    )
    aphelion_speed = perihelion_speed / radius_ratio
    transfer_period_years = ((1 + radius_ratio) / 2) ** 1.5
    excess_speed = perihelion_speed - earth_speed
    incoming_speed = 35_000.0
    cosine = (
        incoming_speed**2 + earth_speed**2 - excess_speed**2
    ) / (2 * incoming_speed * earth_speed)

    close(radius_ratio, 5.20063601688, 1e-10)
    close(perihelion_speed / 1000, 38.70701036, 1e-8)
    close(aphelion_speed / 1000, 7.44274551, 1e-8)
    close(transfer_period_years, 5.45895312, 1e-8)
    close(math.degrees(math.acos(cosine)), 12.75929490, 1e-8)


def verify_question_6() -> None:
    c,vx,vz,g,t=sp.symbols('c vx vz g t',positive=True)
    r=sp.Matrix([c*t,vx*t,vz*t-g*t*t/2]);d=r.diff(t);dd=d.diff(t)
    radius=sp.simplify(d.dot(d)**sp.Rational(3,2)/sp.sqrt(d.cross(dd).dot(d.cross(dd))))
    target=(c*c+vx*vx+(vz-g*t)**2)**sp.Rational(3,2)/(g*sp.sqrt(c*c+vx*vx))
    assert sp.simplify(radius-target)==0
    assert sp.simplify(radius.subs(t,vz/g)-(c*c+vx*vx)/g)==0
    # Exact light hit and receiver Doppler agree with equal-height Rindler clocks.
    b=1.;distance=.7;z=distance**2/(2*b);ct=math.hypot(distance,z)
    close(z,math.sqrt(b*b+ct*ct)-b)
    beta=ct/math.sqrt(b*b+ct*ct);gamma=1/math.sqrt(1-beta*beta)
    close(gamma*(1-beta*z/ct),1)


def verify_question_7() -> None:
    x, y = sp.symbols("x y", real=True)
    ellipse = x**2 + y**2 + x * y - x - y
    assert sp.factor(ellipse.subs(y, x)) == x * (3 * x - 2)
    assert sp.factor(ellipse.subs(y, 1 - 2 * x)) == x * (3 * x - 2)

    wx, wy, v0 = sp.symbols("wx wy v0", real=True, nonzero=True)
    disk_expression = sp.expand(
        2 * (wx**2 + wy**2) + (v0 - wx) ** 2 + wy**2 - 2 * v0**2
    )
    completed_square = sp.expand(
        3 * ((wx - v0 / 3) ** 2 + wy**2 - (2 * v0 / 3) ** 2)
    )
    assert sp.simplify(disk_expression - completed_square) == 0


def verify_question_8() -> None:
    # 用一个非对称数值例检验三个切向投影方程。
    v1, v2, v3, radius = 4.0, -1.0, 2.5, 1.7
    mean = (v1 + v2 + v3) / 3
    omega = mean / radius
    b1, b2, b3 = v1 - mean, v2 - mean, v3 - mean
    vx = b1
    vy = (b2 - b3) / math.sqrt(3)
    directions = [
        (1.0, 0.0),
        (-0.5, math.sqrt(3) / 2),
        (-0.5, -math.sqrt(3) / 2),
    ]
    for prescribed, direction in zip((v1, v2, v3), directions):
        projection = vx * direction[0] + vy * direction[1] + omega * radius
        close(projection, prescribed)

    expected_speed = 2 / 3 * math.sqrt(
        v1**2 + v2**2 + v3**2 - v1 * v2 - v2 * v3 - v3 * v1
    )
    close(math.hypot(vx, vy), expected_speed)


def main() -> None:
    verify_question_1()
    print("Q1 PASS")
    verify_question_2()
    print("Q2 PASS")
    verify_question_3()
    print("Q3 PASS")
    verify_question_4()
    print("Q4 PASS")
    verify_question_5()
    print("Q5 PASS")
    verify_question_6()
    print("Q6 PASS")
    verify_question_7()
    print("Q7 PASS")
    verify_question_8()
    print("Q8 PASS")
    print("第 037 套八题符号与数值验证通过")


if __name__ == "__main__":
    main()
