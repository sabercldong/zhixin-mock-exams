from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN = (
    "数字化重构",
    "完成本题",
    "继续下一题",
    "原卷图",
    "参考文件",
    "手写答案",
    "下图给出与上述推导相对应的解答示意",
    "SOLUTION_FIGURE_LINK_",
)
TEACHER_HEADINGS = (
    "一、题型定位",
    "二、知识点",
    "三、物理图像",
    "四、解题入口",
    "五、解析",
    "六、关键洞察",
    "七、易错点",
    "八、课堂讲解建议",
    "九、变式训练",
)
STUDENT_HEADINGS = TEACHER_HEADINGS[:5]
STUDENT_TEACHER_LANGUAGE = re.compile(
    r"教师版|教师|课堂|板书|教学|让学生|要求学生|学生通常|讲解时|演示给学生"
)
STUDENT_EXTRA_LABELS = (
    "解题顺序与直观复盘",
    "进一步思考与自测",
    "进一步推导、边界检验与自测",
)
BARE_TEX_COMMAND = re.compile(
    r"(?<!\\)\b(?:frac|dfrac|tfrac|sqrt|qquad|quad|boxed|begin|end|"
    r"mathrm|mathbf|mathcal|boldsymbol|operatorname|overline|underbrace)\b"
)
LAYOUT_PADDING_COMMAND = re.compile(
    r"(?m)^\s*\\(?:setstretch|linespread|renewcommand\s*\{\\baselinestretch\}|"
    r"vspace\*?|addvspace|smallskip|medskip|bigskip|pagebreak|clearpage|"
    r"enlargethispage|fontsize)\b"
)
TEACHER_ONLY_RE = re.compile(
    r"\n?<!--\s*(?:TEACHER_ONLY_START|teacher-only-start)\s*-->.*?"
    r"<!--\s*(?:TEACHER_ONLY_END|teacher-only-end)\s*-->\n?",
    re.DOTALL,
)
ANY_TEACHER_MARKER_RE = re.compile(
    r"(?m)^<!--\s*(?:TEACHER_ONLY_START|TEACHER_ONLY_END|"
    r"teacher-only-start|teacher-only-end)\s*-->\s*$"
)


def run(command: list[str], cwd: Path | None = None) -> str:
    result = subprocess.run(
        command,
        cwd=cwd or PROJECT_ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if result.returncode:
        raise AssertionError(f"命令失败：{' '.join(command)}\n{result.stdout}")
    return result.stdout


def set_root(set_number: str) -> Path:
    return PROJECT_ROOT / f"蔡题{set_number}" / "整理版"


def split_front_matter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        raise AssertionError("Markdown 缺少 YAML front matter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise AssertionError("Markdown front matter 未闭合")
    return text[: end + 5], text[end + 5 :]


def split_questions(body: str) -> list[str]:
    matches = list(re.finditer(r"(?m)^# 第 (\d+) 题\s*$", body))
    numbers = [int(match.group(1)) for match in matches]
    if numbers != list(range(1, 9)):
        raise AssertionError(f"题号不是 1—8：{numbers}")
    blocks: list[str] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        block = body[match.start() : end].strip()
        block = re.sub(r"(?m)^\s*\\newpage\s*$", "", block)
        block = re.sub(r"\n{3,}", "\n\n", block).strip()
        blocks.append(block)
    return blocks


def assert_teacher_markers_balanced(block: str, question: int) -> None:
    markers = re.findall(
        r"<!--\s*(TEACHER_ONLY_START|TEACHER_ONLY_END|"
        r"teacher-only-start|teacher-only-end)\s*-->",
        block,
    )
    depth = 0
    for marker in markers:
        depth += 1 if marker.lower().endswith("start") else -1
        if depth not in (0, 1):
            raise AssertionError(f"第 {question} 题教师专属标记嵌套或逆序")
    if depth:
        raise AssertionError(f"第 {question} 题教师专属标记未闭合")


def prepare_set(set_number: str) -> None:
    root = set_root(set_number)
    markdown = root / "markdown"
    teacher_path = markdown / f"蔡题{set_number}_教师备课.md"
    student_path = markdown / f"蔡题{set_number}_学生详解.md"
    paper_path = markdown / f"蔡题{set_number}_试卷.md"

    front, body = split_front_matter(teacher_path.read_text(encoding="utf-8"))
    teacher_blocks = split_questions(body)
    student_blocks: list[str] = []
    paper_blocks: list[str] = []

    for question, block in enumerate(teacher_blocks, start=1):
        assert_teacher_markers_balanced(block, question)
        first = block.find("\n## 一、题型定位")
        sixth = block.find("\n## 六、关键洞察")
        eighth = block.find("\n## 八、课堂讲解建议")
        ninth = block.find("\n## 九、变式训练")
        if (
            first < 0
            or sixth < 0
            or eighth < 0
            or ninth < 0
            or not first < sixth < eighth < ninth
        ):
            raise AssertionError(f"第 {question} 题模块边界异常")

        paper = TEACHER_ONLY_RE.sub("\n", block[:first]).strip()
        # 学生版只取教师主文的前五个模块。教师专属内容即使位于
        # 前五模块中，也必须由 TEACHER_ONLY 标记隔离，不得通过
        # 删标题或替换“教师/课堂”等词语混入学生版。
        student = TEACHER_ONLY_RE.sub("\n", block[:sixth])
        student = ANY_TEACHER_MARKER_RE.sub("", student)
        student = re.sub(r"(?m)^\\setstretch\{[^}]+\}\s*$", "", student)
        student = re.sub(r"\n{3,}", "\n\n", student).strip()
        paper_blocks.append(paper)
        student_blocks.append(student)

    separator = "\n\n\\newpage\n\n"
    teacher_path.write_text(front + separator.join(teacher_blocks) + "\n", encoding="utf-8")
    student_path.write_text(front + separator.join(student_blocks) + "\n", encoding="utf-8")
    paper_path.write_text(front + separator.join(paper_blocks) + "\n", encoding="utf-8")


def markdown_math_blocks(text: str) -> list[str]:
    blocks = re.findall(r"\$\$(.*?)\$\$", text, flags=re.DOTALL)
    blocks.extend(re.findall(r"(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)", text, flags=re.DOTALL))
    return blocks


def display_math_block_count(text: str) -> int:
    """统计 Markdown 中的展示数学块，用于识别公式密集型解答。"""
    return len(re.findall(r"\$\$(.*?)\$\$", text, flags=re.DOTALL)) + len(
        re.findall(r"\\\[(.*?)\\\]", text, flags=re.DOTALL)
    )


def check_markdown(path: Path, expected_headings: tuple[str, ...], kind: str) -> None:
    text = path.read_text(encoding="utf-8")
    _, body = split_front_matter(text)
    blocks = split_questions(body)
    headings = re.findall(r"(?m)^## (.+)$", text)
    if headings != list(expected_headings) * 8:
        raise AssertionError(f"{path.name} 模块标题或顺序异常")
    extra_headings = re.findall(r"(?m)^#{3,}\s+(.+)$", text)
    if extra_headings:
        raise AssertionError(
            f"{path.name} 含既定模块之外的下级标题：{extra_headings[:3]}"
        )
    page_break_count = text.count("\\newpage")
    if page_break_count != 7:
        raise AssertionError(f"{path.name} 应恰有 7 个题间分页，实际 {page_break_count}")
    if re.search(r"(?:^\\newpage\s*$\s*){2,}", text, flags=re.MULTILINE):
        raise AssertionError(f"{path.name} 含重复分页")

    layout_command = LAYOUT_PADDING_COMMAND.search(text)
    if layout_command:
        line = text[: layout_command.start()].count("\n") + 1
        raise AssertionError(
            f"{path.name}:{line} 含正文版式补页命令：{layout_command.group(0).strip()}"
        )

    for word in FORBIDDEN:
        if word in text:
            raise AssertionError(f"{path.name} 含禁用语：{word}")
    if re.search(r"https?://|\[[^]]+\]\([^)]*\.pdf(?:[#?][^)]*)?\)", text):
        raise AssertionError(f"{path.name} 含外部或 PDF 参考链接")
    for target in re.findall(r"!\[[^]]*\]\(([^)]+)\)", text):
        clean = target.split("{")[0].strip()
        image = (path.parent / clean).resolve()
        if not image.exists() or image.stat().st_size == 0:
            raise AssertionError(f"{path.name} 图片缺失：{image}")

    for math in markdown_math_blocks(text):
        match = BARE_TEX_COMMAND.search(math)
        if match:
            line = text[: text.find(math)].count("\n") + 1
            raise AssertionError(f"{path.name}:{line} 数学环境疑似裸写 {match.group(0)}")

    if kind == "student":
        language = STUDENT_TEACHER_LANGUAGE.search(text)
        if language:
            line = text[: language.start()].count("\n") + 1
            raise AssertionError(f"{path.name}:{line} 含教师话术：{language.group(0)}")
        for label in STUDENT_EXTRA_LABELS:
            if label in text:
                raise AssertionError(f"{path.name} 含学生版附加标题：{label}")
        if "## 六、" in text or "## 七、" in text or "## 八、" in text or "## 九、" in text:
            raise AssertionError(f"{path.name} 混入教师版模块")


def check_student_matches_teacher_core(root: Path, set_number: str) -> None:
    """确保学生版逐题只由教师版前五模块生成。

    这项检查防止将“关键洞察”“易错点”或“课堂讲解建议”的
    标题删去后，再把正文伪装成学生解答。
    """
    markdown = root / "markdown"
    teacher_path = markdown / f"蔡题{set_number}_教师备课.md"
    student_path = markdown / f"蔡题{set_number}_学生详解.md"
    _, teacher_body = split_front_matter(teacher_path.read_text(encoding="utf-8"))
    _, student_body = split_front_matter(student_path.read_text(encoding="utf-8"))
    teacher_blocks = split_questions(teacher_body)
    student_blocks = split_questions(student_body)
    for question, (teacher, student) in enumerate(zip(teacher_blocks, student_blocks), start=1):
        sixth = teacher.find("\n## 六、关键洞察")
        if sixth < 0:
            raise AssertionError(f"第 {question} 题缺少第六模块")
        expected = TEACHER_ONLY_RE.sub("\n", teacher[:sixth])
        expected = ANY_TEACHER_MARKER_RE.sub("", expected)
        expected = re.sub(r"(?m)^\\setstretch\{[^}]+\}\s*$", "", expected)
        expected = re.sub(r"\n{3,}", "\n\n", expected).strip()
        actual = re.sub(r"\n{3,}", "\n\n", student).strip()
        if actual != expected:
            raise AssertionError(f"第 {question} 题学生版与教师版前五模块不一致")


def pdf_page_count(path: Path) -> int:
    info = run(["pdfinfo", str(path)])
    match = re.search(r"(?m)^Pages:\s+(\d+)$", info)
    if not match:
        raise AssertionError(f"无法读取页数：{path}")
    return int(match.group(1))


def pdf_text(path: Path) -> str:
    return run(["pdftotext", str(path), "-"])


def sparse_pages(path: Path) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    warnings: list[tuple[int, int]] = []
    failures: list[tuple[int, int]] = []
    for page in range(2, pdf_page_count(path) + 1):
        text = run(["pdftotext", "-f", str(page), "-l", str(page), str(path), "-"])
        count = len(re.sub(r"\s+", "", text))
        if count < 120:
            warnings.append((page, count))
        if count < 20:
            failures.append((page, count))
    return warnings, failures


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_pdf(root: Path, set_number: str, kind: str) -> tuple[int, int, list[tuple[int, int]]]:
    stems = {
        "paper": (f"蔡题{set_number}_试卷.pdf", f"第{set_number}套_试卷版.pdf"),
        "student": (f"蔡题{set_number}_学生详解.pdf", f"第{set_number}套_学生详解版.pdf"),
        "teacher": (f"蔡题{set_number}_教师备课.pdf", f"第{set_number}套_教师备课版.pdf"),
    }
    build_name, output_name = stems[kind]
    build = root / "build" / build_name
    output = root / "output" / output_name
    if not build.exists() or not output.exists():
        raise AssertionError(f"{set_number} {kind} 缺少 build 或 output PDF")
    if digest(build) != digest(output):
        raise AssertionError(f"{set_number} {kind} build 与 output 不同步")
    run(["qpdf", "--check", str(output)])
    log = build.with_suffix(".log")
    if not log.exists():
        raise AssertionError(f"编译日志缺失：{log}")
    bad = re.search(
        r"Overfull|Missing character|LaTeX Error|Undefined control sequence|"
        r"Emergency stop|Fatal error",
        log.read_text(encoding="utf-8", errors="replace"),
    )
    if bad:
        raise AssertionError(f"{log.name} 含编译问题：{bad.group(0)}")
    text = pdf_text(output)
    if "�" in text:
        raise AssertionError(f"{output.name} 含乱码替换字符")
    literal = re.search(r"\b(?:sqrt|qquad|quad|frac)\b", text)
    if literal:
        raise AssertionError(f"{output.name} 可见裸写公式命令：{literal.group(0)}")
    warnings, failures = sparse_pages(output)
    if failures:
        raise AssertionError(f"{output.name} 含近空白页：{failures}")
    return pdf_page_count(output), len(text), warnings


def quality_check(set_number: str) -> None:
    root = set_root(set_number)
    markdown = root / "markdown"
    check_markdown(markdown / f"蔡题{set_number}_试卷.md", (), "paper")
    check_markdown(markdown / f"蔡题{set_number}_学生详解.md", STUDENT_HEADINGS, "student")
    check_markdown(markdown / f"蔡题{set_number}_教师备课.md", TEACHER_HEADINGS, "teacher")
    check_student_matches_teacher_core(root, set_number)

    results = {
        kind: check_pdf(root, set_number, kind)
        for kind in ("paper", "student", "teacher")
    }
    student_pages, student_chars, student_sparse = results["student"]
    teacher_pages, teacher_chars, teacher_sparse = results["teacher"]
    if student_pages < 56 or student_chars < 31_218:
        raise AssertionError(
            f"学生版低于第 101 套正式输出基准：{student_pages} 页，{student_chars} 字"
        )
    teacher_source = (
        markdown / f"蔡题{set_number}_教师备课.md"
    ).read_text(encoding="utf-8")
    teacher_source_chars = len(teacher_source)
    teacher_display_math = display_math_block_count(teacher_source)
    # 第 101 套正式教师版为 71 页、45411 个 PDF 可提取字符、
    # 59255 个源文字符和 325 组展示公式。公式密集的套卷在 PDF
    # 文字统计中偏低，因此允许以“源文量 + 展示公式数”证明同等有效深度。
    teacher_depth_passes = teacher_chars >= 45_411 or (
        teacher_source_chars >= 47_000 and teacher_display_math >= 300
    )
    if teacher_pages < 71 or not teacher_depth_passes:
        raise AssertionError(
            f"教师版低于第 101 套有效深度基准："
            f"{teacher_pages} 页，PDF {teacher_chars} 字，"
            f"源文 {teacher_source_chars} 字，展示公式 {teacher_display_math} 组"
        )
    print(f"第 {set_number} 套统一验收通过")
    print(f"学生版：{student_pages} 页，{student_chars} 字，稀疏页提示 {student_sparse}")
    print(
        f"教师版：{teacher_pages} 页，PDF {teacher_chars} 字，"
        f"源文 {teacher_source_chars} 字，展示公式 {teacher_display_math} 组，"
        f"稀疏页提示 {teacher_sparse}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("prepare", "check"))
    parser.add_argument("set_number")
    args = parser.parse_args()
    set_number = f"{int(args.set_number):03d}"
    if args.action == "prepare":
        prepare_set(set_number)
    else:
        quality_check(set_number)


if __name__ == "__main__":
    main()
