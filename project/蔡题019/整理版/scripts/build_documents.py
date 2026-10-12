"""沿用Pandoc—XeLaTeX多文件工程；输出是完整待验收稿，不宣称套卷通过。"""
from pathlib import Path
import hashlib,json,re,shutil,subprocess
import fitz
from preview_drafts import pandoc_source,keep_math_leads
from audit_sources import metrics,BANNED
ROOT=Path(__file__).resolve().parents[1]
COMPILER=Path('/Users/dongxingxi/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py')
def main():
    output=ROOT/'output/pdf';output.mkdir(parents=True,exist_ok=True);report=[]
    for version in ['试卷','学生详解','教师备课']:
        name=f'蔡题019_{version}';source=ROOT/'markdown'/f'{name}.md';folder=ROOT/'build';folder.mkdir(exist_ok=True)
        md=source.read_text()
        assert len(re.findall(r'(?m)^# 第\d+题$',md))==8 and md.count(r'\newpage')==7
        run=subprocess.run(['pandoc','--from=markdown+raw_tex','--to=latex','--standalone',f'--template={ROOT/"latex/template.tex"}','--top-level-division=section'],
                           input=pandoc_source(md,student=version=='学生详解'),capture_output=True,text=True,check=True)
        tex=re.sub(r'\.\./figures/([A-Za-z0-9_-]+)\.png',lambda m:str(ROOT/'figures'/f'{m.group(1)}.pdf'),run.stdout)
        tex=keep_math_leads(tex.replace(r'\begin{figure}',r'\begin{figure}[H]').replace(r'\caption{图',r'\caption*{图'))
        path=folder/f'{name}.tex';path.write_text(tex)
        compile_run=subprocess.run(['python3',str(COMPILER),str(path),'--compiler','texlive','--engine','xelatex'],capture_output=True,text=True)
        (folder/f'{name}_compile-output.txt').write_text(compile_run.stdout+compile_run.stderr);assert compile_run.returncode==0,compile_run.stdout+compile_run.stderr
        log=path.with_suffix('.log').read_text(errors='replace')
        errors=[line for line in log.splitlines() if any(tag in line for tag in ['Overfull','Missing character','Undefined control sequence','! '])]
        assert not errors,errors
        pdf=path.with_suffix('.pdf');subprocess.run(['qpdf','--check',str(pdf)],capture_output=True,check=True)
        dest=output/pdf.name;shutil.copy2(pdf,dest)
        sha=hashlib.sha256(pdf.read_bytes()).hexdigest();assert hashlib.sha256(dest.read_bytes()).hexdigest()==sha
        with fitz.open(pdf) as doc:
            text='\n'.join(page.get_text() for page in doc)
            density=[len(re.sub(r'\s','',p.get_text())) for p in doc][1:]
            assert '\ufffd' not in text
            assert not any(term in text for term in BANNED)
            if version=='学生详解':assert len(doc)-1>=56 and sum(density)>=31218
            if version=='教师备课':assert len(doc)-1>=71 and sum(density)>=45411
            item=dict(version=version,total_pages=len(doc),body_pages=len(doc)-1,pdf_extracted_body_nonspace=sum(density),
                      per_page_nonspace=density,low_density_pages=[i+2 for i,n in enumerate(density) if n<250],qpdf_passed=True,
                      layout_errors=errors,pdf_sha256=sha,build_output_identical=True,path=str(dest),source_metrics=metrics(md))
        (folder/f'{name}_extracted.txt').write_text(text);report.append(item);print(json.dumps(item,ensure_ascii=False),flush=True)
    (ROOT/'build/pdf-build-manifest.json').write_text(json.dumps(dict(documents=report,accepted=False,actual_visual_review=False,
              model_conditions_resolved=True,pending=['整套逐页视觉复审尚未完成']),ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
