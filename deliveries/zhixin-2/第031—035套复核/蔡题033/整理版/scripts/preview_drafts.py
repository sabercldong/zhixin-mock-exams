"""第033套分题工作稿编译；8题完整前不写正式output。"""
from pathlib import Path
import os, sys
import json
import re
import subprocess
import fitz

ROOT = Path(__file__).resolve().parents[1]
PREVIEW = ROOT / "preview"
_candidates=sorted(Path.home().glob('.codex/plugins/cache/openai-bundled/latex/*/scripts/compile_latex.py'))
COMPILER=Path(os.environ['CODEX_LATEX_COMPILER']) if os.environ.get('CODEX_LATEX_COMPILER') else (_candidates[-1] if _candidates else None)
assert COMPILER is not None and COMPILER.is_file(), 'Set CODEX_LATEX_COMPILER to compile_latex.py'
QUESTIONS = ("01", "02", "03", "04", "05", "06", "07", "08")


def keep_math_leads(tex):
    """短引导句与紧随其后的公式同页，不改变字体、行距或段距。"""
    blocks = tex.split("\n\n")
    for i in range(len(blocks) - 1):
        lead = blocks[i].strip()
        if (blocks[i + 1].lstrip().startswith(r"\[")
                and re.search(r"[\u4e00-\u9fff]", lead)
                and not lead.startswith("\\")
                and len(lead.replace("\n", "")) <= 100):
            blocks[i] = blocks[i].rstrip() + r"\nopagebreak[4]"
    return "\n\n".join(blocks)


def main():
    report = []
    for q in QUESTIONS:
        original = (ROOT / f"drafts/question-{q}.md").read_text()
        for version in ("student", "teacher"):
            body = (original.split("## 六、关键洞察")[0].rstrip() + "\n"
                    if version == "student" else original)
            name = f"working-q{q}-{version}"
            folder = PREVIEW / name
            folder.mkdir(parents=True, exist_ok=True)
            md = folder / (name + ".md")
            md.write_text('---\ntitle: "第033套"\nshorttitle: "第033套"\nauthor: "物理竞赛资料"\n---\n' + body)
            result = subprocess.run([
                "pandoc", str(md), "--from=markdown+raw_tex", "--to=latex", "--standalone",
                f"--template={ROOT / 'latex/template.tex'}", "--top-level-division=section"
            ], check=True, capture_output=True, text=True)
            tex = re.sub(
                r"\.\./figures/([A-Za-z0-9_-]+)\.png",
                lambda m: str(ROOT / "figures" / (m.group(1) + ".pdf")),
                result.stdout,
            )
            tex = tex.replace(r"\begin{figure}", r"\begin{figure}[H]")
            tex = tex.replace(r"\caption{图", r"\caption*{图")
            tex = keep_math_leads(tex)
            path = folder / (name + ".tex")
            path.write_text(tex)
            built = subprocess.run([
                sys.executable, str(COMPILER), str(path),
                "--compiler", "texlive", "--engine", "xelatex"
            ], capture_output=True, text=True)
            (folder / "compile-output.txt").write_text(built.stdout + built.stderr)
            assert built.returncode == 0, (name, built.stdout, built.stderr)
            pdf = folder / (name + ".pdf")
            subprocess.run(["qpdf", "--check", str(pdf)], check=True, capture_output=True)
            log = (folder / (name + ".log")).read_text(errors="replace")
            warnings = [line for line in log.splitlines()
                        if any(key in line for key in ("Overfull", "Missing character", "! "))]
            doc = fitz.open(pdf)
            density = [len(re.sub(r"\s", "", page.get_text())) for page in doc][1:]
            item = {
                "question": q,
                "version": version,
                "total_pages": len(doc),
                "body_pages": len(doc) - 1,
                "body_nonspace": sum(density),
                "per_page_nonspace": density,
                "layout_warnings": warnings,
            }
            report.append(item)
            print(json.dumps(item, ensure_ascii=False), flush=True)
    (PREVIEW / "working-draft-check.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    )


if __name__ == "__main__":
    main()
