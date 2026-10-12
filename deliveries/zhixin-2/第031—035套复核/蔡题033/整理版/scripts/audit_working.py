"""验收第033套现有分题工作稿；8题不全时绝不返回整套通过。"""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
import fitz

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[1]
sys.path.insert(0, str(PROJECT))
from document_pipeline import STUDENT_TEACHER_LANGUAGE, BARE_TEX_COMMAND

HEADINGS = ["一、题型定位", "二、知识点", "三、物理图像", "四、解题入口", "五、解析",
            "六、关键洞察", "七、易错点", "八、课堂讲解建议", "九、变式训练"]
FORBIDDEN = ["数字化重构", "完成本题的输出", "继续下一题", "原卷图", "解题顺序与直观复盘", "进一步思考与自测"]

def pdf_stats(path):
    doc = fitz.open(path)
    raw = subprocess.check_output(["pdftotext", str(path), "-"], text=True)
    body = "\n".join(p.get_text(clip=fitz.Rect(0,52,p.rect.width,p.rect.height-45)) for p in list(doc)[1:])
    return dict(pdf_pages=len(doc), body_pages=len(doc)-1, extracted_chars=len(raw),
                nonwhitespace_chars=len(re.sub(r"\s+","",raw)),
                body_net_chars=len(re.sub(r"\s+","",body)))

def main():
    rows = []
    expected = ["01", "02", "03", "04", "05", "06", "07", "08"]
    figure_names = set()
    for q in expected:
        source = (ROOT/f"drafts/question-{q}.md").read_text()
        assert re.findall(r"(?m)^## (.+)$", source) == HEADINGS
        assert len(re.findall(r"(?m)^# ", source)) == 1
        assert not re.search(r"(?m)^###", source)
        assert source.count("<!-- question-start -->") == source.count("<!-- question-end -->") == 1
        assert not any(word in source for word in FORBIDDEN)
        clean_source = re.sub(r"<!--.*?-->", "", source, flags=re.S)
        assert not BARE_TEX_COMMAND.search(clean_source), (q, BARE_TEX_COMMAND.search(clean_source))
        parts = re.split(r"(?m)^## (.+)\n", source)
        for i in range(1, len(parts), 2):
            if parts[i] != "八、课堂讲解建议":
                assert not STUDENT_TEACHER_LANGUAGE.search(parts[i+1]), (q, parts[i])
        names = re.findall(r"!\[[^\]]*\]\(\.\./figures/([^)]*)\.png\)", source)
        for name in names:
            assert (ROOT/f"figures/{name}.png").exists()
            assert (ROOT/f"figures/{name}.pdf").exists()
            figure_names.add(name)
        core = source.split("## 六、关键洞察")[0].rstrip()
        for version in ("student", "teacher"):
            stem = f"working-q{q}-{version}"
            folder = ROOT/"preview"/stem
            path = folder/(stem+".pdf")
            tex = (folder/(stem+".tex")).read_text()
            md = (folder/(stem+".md")).read_text().split("---\n", 2)[2].strip()
            expected_md = core if version == "student" else source.strip()
            assert md == expected_md
            assert tex.count(r"\begin{figure}[H]") == len(names)
            assert tex.count(r"\caption*{图") == len(names)
            figures = re.findall(r"\\begin\{figure\}\[H\](.*?)\\end\{figure\}", tex, re.S)
            assert all(r"\centering" in f for f in figures)
            texbody = tex.split(r"\end{titlepage}")[1]
            assert not re.search(r"\\(?:setstretch|vspace|linespread|fontsize|enlargethispage|newpage)", texbody)
            log = (folder/(stem+".log")).read_text(errors="replace")
            assert not re.search(r"Overfull|Missing character|LaTeX Error|Undefined control sequence", log)
            subprocess.run(["qpdf","--check",str(path)], check=True, capture_output=True)
            doc = fitz.open(path)
            for index, page in enumerate(doc):
                assert "�" not in page.get_text()
                if index == 0:
                    continue
                blocks = [x for x in page.get_text("blocks") if x[1]>55 and x[3]<page.rect.height-35]
                bottom = max((x[3] for x in blocks), default=0)
                chars = len(re.sub(r"\s+","",page.get_text()))
                assert not (bottom<280 and chars<300), ("sparse",q,version,index+1,chars,bottom)
            rows.append(dict(question=q,version=version,statistics=pdf_stats(path),
                             figures=len(names),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                             qpdf="pass",layout="pass",student_core_exact="pass"))
    checked = []
    for path in sorted((ROOT/"figures").glob("*.pdf")):
        subprocess.run(["qpdf","--check",str(path)],check=True,capture_output=True)
        checked.append(path.name)
    for path in sorted((ROOT/"figures").glob("*.log")):
        log = path.read_text(errors="replace")
        assert not re.search(r"Overfull|Missing character|LaTeX Error|Undefined control sequence",log),path
    benchmark = {}
    for version, label in (("student","学生详解"),("teacher","教师备课")):
        benchmark[version] = pdf_stats(PROJECT/f"蔡题101/整理版/output/pdf/蔡题101_{label}.pdf")
    report = dict(status="working_drafts_technical_checks_pass_set_NOT_accepted",
                  unresolved_questions=[],completed_working_questions=expected,
                  benchmark101=benchmark,documents=rows,unique_tikz_figures=len(figure_names),
                  figure_pdf_checks=checked,
                  acceptance_note="第1—8题工作稿技术检查通过；整套正式成品须单独构建并通过严格验收，分题页数不替代整套检查。")
    (ROOT/"build/working-quality.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__ == "__main__":
    main()
