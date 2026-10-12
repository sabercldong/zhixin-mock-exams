"""第034套第7题：以有限高度光线的精确球面求交和矢量 Snell 定律独立核验。
长度统一用 cm。不是将最终近轴公式重新代入自身。
"""
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parents[1]
R1, R2, N = 20.0, 80.0, 1.5

def add(a, b):
    return tuple(x + y for x, y in zip(a, b))

def scale(s, a):
    return tuple(s * x for x in a)

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def unit(a):
    return scale(1.0 / math.sqrt(dot(a, a)), a)

def subtract(a, b):
    return add(a, scale(-1, b))

def snell(direction, forward_normal, n_in, n_out):
    # forward_normal 指向下一介质；向量切向分量按 n_in/n_out 缩放。
    cosine = dot(direction, forward_normal)
    assert cosine > 0
    tangent = scale(n_in / n_out, subtract(direction, scale(cosine, forward_normal)))
    radicand = 1 - dot(tangent, tangent)
    assert radicand > 0, "发生全反射；测试光线不属于本题近轴范围"
    return unit(add(tangent, scale(math.sqrt(radicand), forward_normal)))

def meet_circle(point, direction, center, radius):
    shift = subtract(point, center)
    b = dot(shift, direction)
    c = dot(shift, shift) - radius * radius
    discriminant = b * b - c
    assert discriminant >= 0
    roots = [-b - math.sqrt(discriminant), -b + math.sqrt(discriminant)]
    roots = [s for s in roots if s > 1e-10]
    assert roots, (point, direction, center)
    hit = add(point, scale(min(roots), direction))
    assert abs(math.dist(hit, center) - radius) < 1e-8
    return hit

def intercept(point, direction):
    return point[0] - point[1] * direction[0] / direction[1]

def trace_left(u, height, thickness):
    c1, c2 = (R1, 0.0), (R2 + thickness, 0.0)
    # 稳定计算 R - sqrt(R^2-y^2)，避免相减消去。
    x = height * height / (R1 + math.sqrt(R1 * R1 - height * height))
    front = (x, height)
    incoming = unit(subtract(front, (-u, 0.0)))
    inside = snell(incoming, unit(subtract(c1, front)), 1.0, N)
    back = meet_circle(front, inside, c2, R2)
    normal = unit(subtract(c2, back))
    transmitted = snell(inside, normal, N, 1.0)
    reflected = subtract(inside, scale(2 * dot(inside, normal), normal))
    front_return = meet_circle(back, reflected, c1, R1)
    returning = snell(reflected, unit(subtract(front_return, c1)), N, 1.0)
    return intercept(back, transmitted), intercept(front_return, returning)

def trace_right(u, height, thickness):
    c1, c2 = (R1, 0.0), (R2 + thickness, 0.0)
    x = thickness + height * height / (R2 + math.sqrt(R2 * R2 - height * height))
    back = (x, height)
    incoming = unit(subtract(back, (thickness + u, 0.0)))
    normal_left = unit(subtract(back, c2))
    reflected = subtract(incoming, scale(2 * dot(incoming, normal_left), normal_left))
    inside = snell(incoming, normal_left, 1.0, N)
    front = meet_circle(back, inside, c1, R1)
    transmitted = snell(inside, unit(subtract(front, c1)), N, 1.0)
    return intercept(front, transmitted), intercept(back, reflected)

def main():
    rows = []
    # 薄透镜极限和近轴极限同时逼近；厚度始终大于本光线处的表面弓高差。
    for h, d in [(0.01, 0.001), (0.003, 0.0001), (0.001, 0.00001)]:
        left = trace_left(64.0, h, d)
        right = trace_right(320.0 / 7, h, d)
        wrong = trace_left(320.0 / 9, h, d)
        rows.append(dict(height=h, thickness=d, left_images=left,
                         right_images=right, handwritten_left_images=wrong))
    last = rows[-1]
    assert max(abs(x - 320) for x in last["left_images"]) < 0.004
    assert max(abs(x - 320) for x in last["right_images"]) < 0.004
    # 旧 u=320/9 时，两束光的像分别趋近 -320/3 和 +64，显然不重合。
    assert abs(last["handwritten_left_images"][0] + 320 / 3) < 0.004
    assert abs(last["handwritten_left_images"][1] - 64) < 0.004
    # 物距微扰的数值差分，核对真实空间 x 坐标中的纵向放大率。
    du = 1e-3
    at_low = trace_right(320 / 7 - du, 0.001, 1e-5)
    at_high = trace_right(320 / 7 + du, 0.001, 1e-5)
    derivatives = [(a - b) / (2 * du) for a, b in zip(at_high, at_low)]
    assert abs(derivatives[0] - 49) < 0.01
    assert abs(derivatives[1] + 49) < 0.01
    report = dict(status="passed", method="精确球面求交、矢量 Snell 折射和镜面反射",
                  convergence=rows, right_longitudinal_signed=derivatives,
                  correction=dict(left_object_cm=64, common_image_x_cm=320,
                                  right_object_cm=320/7, right_signed_image_cm=-320))
    target = ROOT / "build/question07-verification.json"
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()

