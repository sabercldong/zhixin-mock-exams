from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
SOURCE = FIGURES / "蔡题036_图稿源文件.tex"
COMPILER = Path("/Users/dongxingxi/.codex/plugins/cache/openai-bundled/latex/0.2.6/scripts/compile_latex.py")

def run(args):
    subprocess.run(args, cwd=FIGURES, check=True)

if __name__ == "__main__":
    run(["python3", str(COMPILER), str(SOURCE), "--compiler", "texlive", "--engine", "xelatex"])
    names = [f"{kind}-{n:02}" for n in range(1, 9) for kind in ("question", "solution")]
    for page, name in enumerate(names, 1):
        target = FIGURES / f"{name}.pdf"
        run(["pdfseparate", "-f", str(page), "-l", str(page), str(SOURCE.with_suffix(".pdf")), str(target)])
        run(["pdftoppm", "-png", "-r", "180", "-singlefile", str(target), str(FIGURES / name)])
