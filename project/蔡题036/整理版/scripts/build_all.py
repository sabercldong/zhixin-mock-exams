"""Rebuild source figures and all three documents without touching input PDFs."""
from pathlib import Path
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
COMPILER=Path("/Users/dongxingxi/.codex/plugins/cache/openai-bundled/latex/0.2.6/scripts/compile_latex.py")

def run(args):
    subprocess.run(args,cwd=ROOT,check=True)

if __name__=="__main__":
    for name in ("verify_results.py","render_figures.py","prepare_documents.py","build_documents.py"):
        run([sys.executable,str(ROOT/"scripts"/name)])
    for suffix,out_suffix in (("试卷","试卷版"),("学生详解","学生详解版"),("教师备课","教师备课版")):
        tex=ROOT/"build"/f"蔡题036_{suffix}.tex"
        run([sys.executable,str(COMPILER),str(tex),"--compiler","texlive","--engine","xelatex",
             "--output-directory",str(ROOT/"build")])
        shutil.copy2(tex.with_suffix(".pdf"),ROOT/"output"/f"第036套_{out_suffix}.pdf")
    run([sys.executable,str(ROOT/"scripts"/"quality_check.py")])
