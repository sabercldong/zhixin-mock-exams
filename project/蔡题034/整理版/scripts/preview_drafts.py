"""分题工作稿编译：不写正式 output，不把缺题试卷标记为完成。"""
from pathlib import Path
import json
import re
import subprocess
import fitz
ROOT=Path(__file__).resolve().parents[1]
PREVIEW=ROOT/"preview"
COMPILER=Path("/Users/dongxingxi/.codex/plugins/cache/openai-bundled/latex/0.2.6/scripts/compile_latex.py")

def keep_math_leads(tex):
    """Keep a short explanation with its equation; do not alter spacing or type size."""
    blocks=tex.split("\n\n")
    for i in range(len(blocks)-1):
        lead=blocks[i].strip()
        if (blocks[i+1].lstrip().startswith(r"\[")
            and re.search(r"[\u4e00-\u9fff]",lead)
            and not lead.startswith("\\")
            and len(lead.replace("\n",""))<=100):
            blocks[i]=blocks[i].rstrip()+r"\nopagebreak[4]"
    return "\n\n".join(blocks)

def main():
    report=[]
    for q in ("01","03","04","05","06","07","08"):
        original=(ROOT/f"drafts/question-{q}.md").read_text()
        for version in ("student","teacher"):
            body=original.split("## 六、关键洞察")[0].rstrip()+"\n" if version=="student" else original
            name=f"working-q{q}-{version}"
            folder=PREVIEW/name
            folder.mkdir(parents=True,exist_ok=True)
            md=folder/(name+".md")
            md.write_text('---\ntitle: "第034套"\nshorttitle: "第034套"\nauthor: "物理竞赛资料"\n---\n'+body)
            result=subprocess.run(["pandoc",str(md),"--from=markdown+raw_tex","--to=latex","--standalone",
                                  f"--template={ROOT/'latex/template.tex'}","--top-level-division=section"],
                                  check=True,capture_output=True,text=True)
            tex=re.sub(r"\.\./figures/([A-Za-z0-9_-]+)\.png",
                       lambda m:str(ROOT/"figures"/(m.group(1)+".pdf")),result.stdout)
            tex=tex.replace(r"\begin{figure}",r"\begin{figure}[H]")
            tex=tex.replace(r"\caption{图",r"\caption*{图")
            tex=keep_math_leads(tex)
            path=folder/(name+".tex")
            path.write_text(tex)
            build=subprocess.run(["python3",str(COMPILER),str(path),"--compiler","texlive","--engine","xelatex"],
                                 capture_output=True,text=True)
            (folder/"compile-output.txt").write_text(build.stdout+build.stderr)
            assert build.returncode==0,(name,build.stdout,build.stderr)
            pdf=folder/(name+".pdf")
            subprocess.run(["qpdf","--check",str(pdf)],check=True,capture_output=True)
            log=(folder/(name+".log")).read_text(errors="replace")
            warnings=[s for s in log.splitlines() if any(x in s for x in ["Overfull","Missing character","! "])]
            document=fitz.open(pdf)
            density=[len(re.sub(r"\s","",page.get_text())) for page in document][1:]
            item=dict(question=q,version=version,total_pages=len(document),body_pages=len(document)-1,
                      body_nonspace=sum(density),per_page_nonspace=density,layout_warnings=warnings)
            report.append(item)
            print(json.dumps(item,ensure_ascii=False),flush=True)
    (PREVIEW/"working-draft-check.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
if __name__=="__main__":main()
