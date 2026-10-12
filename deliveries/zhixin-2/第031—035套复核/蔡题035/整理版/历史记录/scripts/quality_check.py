"""Strict additive acceptance gate for the 035--021 batch; legacy rules unchanged."""
from pathlib import Path
import sys
import re
import json
import subprocess
import fitz

ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT.parents[1]
sys.path.insert(0,str(PROJECT))
from document_pipeline import quality_check, split_front_matter, split_questions, display_math_block_count, STUDENT_TEACHER_LANGUAGE

def statistics(path):
    doc=fitz.open(path)
    text=subprocess.check_output(["pdftotext",str(path),"-"],text=True)
    body=[]
    for p in list(doc)[1:]:
        body.append(p.get_text(clip=fitz.Rect(0,52,p.rect.width,p.rect.height-45)))
    body_text="\n".join(body)
    return {"pdf_pages":len(doc),"body_pages":len(doc)-1,
            "extracted_chars":len(text),
            "nonwhitespace_chars":len(re.sub(r"\s+","",text)),
            "body_net_chars":len(re.sub(r"\s+","",body_text))}

def per_question_pdf(path):
    """Count rendered body text, not Markdown/LaTeX source or line breaks."""
    doc=fitz.open(path)
    groups=[]
    for number,page in enumerate(list(doc)[1:],2):
        t=page.get_text(clip=fitz.Rect(0,52,page.rect.width,page.rect.height-45))
        head=re.search(r"^\s*第\s*([1-8])\s*题",t)
        if head:
            groups.append({"question":int(head.group(1)),"first_pdf_page":number,
                           "body_net_chars":0,"body_pages":0})
        assert groups,("missing first question",path,number)
        groups[-1]["body_pages"]+=1
        groups[-1]["body_net_chars"]+=len(re.sub(r"\s+","",t))
    assert [g["question"] for g in groups]==list(range(1,9)),groups
    return groups

def reject_sparse_tails(path):
    doc=fitz.open(path)
    for index,page in enumerate(doc):
        if index==0:continue
        blocks=page.get_text("blocks")
        body=[b for b in blocks if b[1]>55 and b[3]<page.rect.height-35]
        bottom=max((b[3] for b in body),default=0)
        chars=len(re.sub(r"\s+","",page.get_text()))
        assert not (bottom<280 and chars<300),("稀疏正文尾页",path.name,index+1,chars,bottom)

if __name__=="__main__":
    quality_check("035")
    report={}
    for kind,label,minimum in (("student","学生详解",56),("teacher","教师备课",71)):
        current=statistics(ROOT/"output"/f"第035套_{label}版.pdf")
        reject_sparse_tails(ROOT/"output"/f"第035套_{label}版.pdf")
        base=statistics(PROJECT/"蔡题101"/"整理版"/"output"/"pdf"/f"蔡题101_{label}.pdf")
        report[kind]={"current":current,"benchmark101":base}
        report[kind]["per_question_rendered"]=per_question_pdf(
            ROOT/"output"/f"第035套_{label}版.pdf")
        assert current["body_pages"]>=minimum,(kind,current)
        assert current["body_net_chars"]>=base["body_net_chars"],(kind,"正文净字符低于101",current,base)
        md=(ROOT/"markdown"/f"蔡题035_{label}.md").read_text()
        _,body=split_front_matter(md)
        report[kind]["questions"]=[]
        for i,q in enumerate(split_questions(body),1):
            report[kind]["questions"].append({
                "question":i,"source_chars":len(q),
                "display_math_blocks":display_math_block_count(q),
                "figures":re.findall(r"!\[[^\]]*\]\(([^)]+)\)",q)})
    teacher=(ROOT/"markdown"/"蔡题035_教师备课.md").read_text()
    for q in split_questions(split_front_matter(teacher)[1]):
        parts=re.split(r"(?m)^## (.+)\n",q)
        for i in range(1,len(parts),2):
            if parts[i]!="八、课堂讲解建议":
                assert not STUDENT_TEACHER_LANGUAGE.search(parts[i+1]),("teacher-language",parts[i])
    for label,count in (("试卷",9),("学生详解",17),("教师备课",17)):
        tex=(ROOT/"build"/f"蔡题035_{label}.tex").read_text()
        assert tex.count(r"\includegraphics")==count,(label,"image count")
        assert tex.count(r"\begin{figure}[H]")==count,(label,"inline image detected")
        assert tex.count(r"\caption*{图")==count,(label,"missing caption")
        figure_blocks=re.findall(r"\\begin\{figure\}\[H\](.*?)\\end\{figure\}",tex,re.S)
        assert all(r"\centering" in block for block in figure_blocks)
        body=tex.split(r"\end{titlepage}",1)[1]
        assert not re.search(r"\\(?:setstretch|vspace|linespread|fontsize|enlargethispage)",body)
    figures=list((ROOT/"figures").glob("question-*.pdf"))+list((ROOT/"figures").glob("solution-*.pdf"))
    assert len(figures)==16
    for path in (ROOT/"figures").glob("*.pdf"):
        subprocess.run(["qpdf","--check",str(path)],check=True,capture_output=True)
    figlog=(ROOT/"figures"/"蔡题035_图稿源文件.log").read_text()
    assert not re.search(r"Overfull|Missing character|LaTeX Error|Undefined control sequence",figlog)
    report["tikz_figures"]=16
    report["retained_measurement_images"]=1
    (ROOT/"build"/"strict-quality.json").write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps(report,ensure_ascii=False,indent=2))
