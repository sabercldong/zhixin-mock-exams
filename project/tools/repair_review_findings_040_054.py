from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SETS = ("040", "045", "046", "047", "048", "050", "051", "053", "054")
GENERIC_FIGURE_SENTENCE = (
    "下图给出与上述推导相对应的解答示意；"
    "图中标出的量、方向和作用点均沿用正文约定，可与前后各式逐项核对。"
)
PLACEHOLDER_RE = re.compile(r"(?m)^<!-- SOLUTION_FIGURE_LINK_\d+ -->\s*$")
SHARED_MARKER_RE = re.compile(
    r"(?m)^<!--\s*(?:TEACHER_ONLY_START|TEACHER_ONLY_END|"
    r"teacher-only-start|teacher-only-end)\s*-->\s*$"
)
SOLUTION_IMAGE_RE = re.compile(
    r"(?m)^!\[[^\]]+\]\(\.\./figures/solution-(\d{2})\.png\)\{[^\n]+\}\s*$"
)


FIGURE_TRANSITIONS: dict[str, dict[int, str]] = {
    "053": {
        1: "按图 1-2 设中点位置矢量为 $\\bm r$，先把两颗星对应坐标分量的加速度写出，再合成径向加速度。",
        2: "图 2-2 将接触区按相对滑动方向分成内、外两部分，下面的合力与力矩积分均使用图示的 $\\rho$ 和分界半径 $\\lambda R$。",
        3: "图 3-2 给出圆柱内外的场区、电场方向和转动正方向，后续安培环路、高斯面及法拉第环路都按该图取向。",
        4: "按图 4-2 规定干路电流 $\\widetilde I$ 与桥臂电流 $\\widetilde I_1$ 的正方向，再从节点电流关系写出四条支路电流。",
        5: "图 5-2 同时标出分布函数的零点 $v_j$、极大值点 $v_p$ 和面积归一化条件，下面依次求这三个量。",
        6: "图 6-2 将每次往返反射、频率递推与单位时间碰撞次数对应起来，以此分别计算瞬时力和时间平均力。",
        7: "图 7-2 中物距、像距和曲率半径均按向右为正取符号，后续折射面成像式直接使用这一符号约定。",
        8: "图 8-2 把感生电场在 $x<R$、$R<x<R+d$ 两区间的分段规律与杆上力矩微元对应起来，因此力矩积分也必须分段。",
    },
    "054": {
        1: "按图 1-2 的切向基矢与正转方向，小物体的绝对速度分为相对螺线的切向速度和螺线整体转动速度。",
        2: "图 2-2 给出前轮碰撞时的法向、切向冲量及碰后后轮轮心轨迹，下面所有冲量方程和几何筛根都按图中方向书写。",
        3: "图 3-2 将 $AB$、$BC$、$CA$ 三个过程的状态量和热量正负号对应起来，后续用状态方程闭合循环。",
        4: "图 4-2 显示低阶线框的质量分布与极限正方形，各线段的坐标平方平均值将直接用于惯量求和。",
        5: "图 5-2 是两个频率尺度下的端口等效网络，先由开路、短路极限确定拓扑，再计算端口导纳。",
        6: "图 6-2 中的近、远转向点满足径向速度为零，因此它们是有效势能方程的两个正根。",
        7: "按图 7-2 的顶点顺序逐点使用牛顿成像映射，再对像多边形使用鞋带公式求面积。",
        8: "图 8-2 以俯视投影标出两根长导线到竖边的距离 $r_1,r_2$ 及磁力的力臂，下面先求磁场，再对两条竖边合成力矩。",
    },
}


def split_document(text: str) -> tuple[str, list[str]]:
    matches = list(re.finditer(r"(?m)^# 第 (\d+) 题\s*$", text))
    if [int(match.group(1)) for match in matches] != list(range(1, 9)):
        raise RuntimeError("题号不是 1—8")
    front = text[: matches[0].start()]
    blocks = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks.append(text[match.start() : end].strip())
    return front, blocks


def migrate_shared_markers(block: str) -> str:
    sixth = block.find("\n## 六、关键洞察")
    if sixth < 0:
        raise RuntimeError("缺少第六模块")
    shared = SHARED_MARKER_RE.sub("", block[:sixth])
    return remove_orphan_markers(shared.rstrip() + block[sixth:])


def remove_orphan_markers(block: str) -> str:
    """删除历史上跨越“解析/关键洞察”边界的孤立标记。

    同一模块内成对的教师专属标记仍保留；只删除在当前文档块中
    没有对应起始标记的结束标记，或没有结束标记的起始标记。
    """
    marker_re = re.compile(
        r"(?m)^<!--\s*(TEACHER_ONLY_START|TEACHER_ONLY_END|"
        r"teacher-only-start|teacher-only-end)\s*-->\s*$"
    )
    matches = list(marker_re.finditer(block))
    stack: list[re.Match[str]] = []
    remove: list[tuple[int, int]] = []
    for match in matches:
        name = match.group(1).lower()
        if name.endswith("start"):
            stack.append(match)
        elif stack:
            stack.pop()
        else:
            remove.append((match.start(), match.end()))
    remove.extend((match.start(), match.end()) for match in stack)
    for start, end in reversed(remove):
        block = block[:start] + block[end:]
    return block


def move_solution_figure(block: str, set_number: str, question: int) -> str:
    matches = list(SOLUTION_IMAGE_RE.finditer(block))
    if len(matches) != 1:
        raise RuntimeError(f"第{set_number}套第{question}题解答图数量为 {len(matches)}")
    match = matches[0]
    fifth = block.find("\n## 五、解析")
    sixth = block.find("\n## 六、关键洞察")
    if fifth < match.start() < sixth:
        return block
    image = match.group(0).strip()
    block = block[: match.start()].rstrip() + "\n\n" + block[match.end() :].lstrip()
    heading = "## 五、解析"
    transition = FIGURE_TRANSITIONS[set_number][question]
    insertion = f"{heading}\n\n{transition}\n\n{image}"
    if block.count(heading) != 1:
        raise RuntimeError(f"第{set_number}套第{question}题第五模块异常")
    return block.replace(heading, insertion, 1)


def repair_set(set_number: str) -> None:
    path = ROOT / f"蔡题{set_number}" / "整理版" / "markdown" / f"蔡题{set_number}_教师备课.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace(GENERIC_FIGURE_SENTENCE, "")
    text = PLACEHOLDER_RE.sub("", text)
    front, blocks = split_document(text)
    repaired = []
    for question, block in enumerate(blocks, start=1):
        block = migrate_shared_markers(block)
        if set_number in FIGURE_TRANSITIONS:
            block = move_solution_figure(block, set_number, question)
        block = re.sub(r"\n{3,}", "\n\n", block).strip()
        repaired.append(block)
    path.write_text(front + "\n\n\\newpage\n\n".join(repaired) + "\n", encoding="utf-8")


def main() -> None:
    for set_number in SETS:
        repair_set(set_number)
        print(f"第 {set_number} 套 Markdown 修复完成")


if __name__ == "__main__":
    main()
