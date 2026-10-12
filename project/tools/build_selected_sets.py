from __future__ import annotations

import argparse
import os
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SETS = ("040", "045", "046", "047", "048", "050", "051", "053", "054")
KINDS = (
    ("试卷", "试卷版"),
    ("学生详解", "学生详解版"),
    ("教师备课", "教师备课版"),
)


def run(command: list[str], cwd: Path, stdout: Path | None = None) -> None:
    if stdout is None:
        subprocess.run(command, cwd=cwd, check=True)
        return
    with stdout.open("a", encoding="utf-8") as stream:
        subprocess.run(command, cwd=cwd, stdout=stream, stderr=subprocess.STDOUT, check=True)


def atomic_copy(source: Path, target: Path, cwd: Path) -> None:
    """先复制到同目录的新临时文件，校验大小后再原子替换成品。"""
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{target.name}.", suffix=".tmp", dir=target.parent
    )
    os.close(descriptor)
    temporary = Path(temporary_name)
    temporary.unlink()
    try:
        run(["cp", str(source), str(temporary)], cwd=cwd)
        if temporary.stat().st_size != source.stat().st_size:
            raise RuntimeError(f"PDF 复制后大小不一致: {target.name}")
        os.replace(temporary, target)
    finally:
        if temporary.exists():
            temporary.unlink()


def build_set(set_number: str) -> str:
    root = ROOT / f"蔡题{set_number}" / "整理版"
    build = root / "build"
    output = root / "output"
    output.mkdir(parents=True, exist_ok=True)
    run(["python3", str(root / "scripts" / "build_documents.py")], cwd=root)

    for stem, output_label in KINDS:
        name = f"蔡题{set_number}_{stem}"
        tex = build / f"{name}.tex"
        log = build / f"{name}.compile.stdout"
        log.write_text("", encoding="utf-8")
        command = [
            "xelatex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-file-line-error",
            f"-output-directory={build}",
            str(tex),
        ]
        run(command, cwd=root, stdout=log)
        run(command, cwd=root, stdout=log)
        atomic_copy(
            build / f"{name}.pdf",
            output / f"第{set_number}套_{output_label}.pdf",
            root,
        )
    return set_number


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("sets", nargs="*", default=list(DEFAULT_SETS))
    parser.add_argument("--workers", type=int, default=3)
    args = parser.parse_args()

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = {executor.submit(build_set, set_number): set_number for set_number in args.sets}
        for future in as_completed(futures):
            set_number = futures[future]
            try:
                future.result()
            except Exception as exc:
                raise RuntimeError(f"第 {set_number} 套构建失败") from exc
            print(f"第 {set_number} 套构建完成", flush=True)


if __name__ == "__main__":
    main()
