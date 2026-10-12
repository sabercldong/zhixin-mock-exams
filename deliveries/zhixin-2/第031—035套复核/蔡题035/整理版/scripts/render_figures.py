from pathlib import Path
import subprocess,sys

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
SOURCE = FIGURES / "蔡题035_图稿源文件.tex"
import os
_candidates=sorted((Path.home()/'.codex/plugins/cache/openai-bundled/latex').glob('*/scripts/compile_latex.py'))
COMPILER=Path(os.environ['CODEX_LATEX_COMPILER']) if os.environ.get('CODEX_LATEX_COMPILER') else _candidates[-1]
assert COMPILER.is_file()

def run(args):
    subprocess.run(args, cwd=FIGURES, check=True)

if __name__ == "__main__":
    run([sys.executable, str(COMPILER), str(SOURCE), "--compiler", "texlive", "--engine", "xelatex"])
    names = [f"{kind}-{n:02}" for n in range(1, 9) for kind in ("question", "solution")]
    for page, name in enumerate(names, 1):
        target = FIGURES / f"{name}.pdf"
        if target.exists():target.unlink()
        run(["pdfseparate", "-f", str(page), "-l", str(page), str(SOURCE.with_suffix(".pdf")), str(target)])
        run(["pdftoppm", "-png", "-r", "180", "-singlefile", str(target), str(FIGURES / name)])

    run([sys.executable,str(ROOT / "scripts" / "extract_measurement.py")])
