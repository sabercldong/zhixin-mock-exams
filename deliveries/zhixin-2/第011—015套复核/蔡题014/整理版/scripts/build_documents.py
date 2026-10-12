"""Complete set candidate build; full acceptance remains a separate actual review."""
from pathlib import Path
import hashlib,json,re,shutil,subprocess
import fitz
from preview_drafts import rules,keep_math_leads
from audit_sources import metrics,BANNED
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    output=ROOT/'output/pdf';output.mkdir(parents=True,exist_ok=True);rows=[]
    for version in ['试卷','学生详解','教师备课']:
        name=f'蔡题014_{version}';source=ROOT/'markdown'/f'{name}.md';folder=ROOT/'build'
        md=source.read_text()
        assert len(re.findall(r'(?m)^# 第\d+题$',md))==8 and md.count(r'\newpage')==7
        run=subprocess.run(['pandoc','--from=markdown+raw_tex','--to=latex','--standalone',f'--template={ROOT/"latex/template.tex"}','--top-level-division=section'],input=rules.pandoc_source(md,student=version=='学生详解'),capture_output=True,text=True,check=True)
        tex=re.sub(r'\.\./figures/([A-Za-z0-9_-]+)\.png',lambda m:f'../figures/{m.group(1)}.pdf',run.stdout)
        tex=keep_math_leads(tex.replace(r'\begin{figure}',r'\begin{figure}[H]').replace(r'\caption{图',r'\caption*{图'))
        path=folder/(name+'.tex');path.write_text(tex)
        run=subprocess.run(['python3',str(rules.COMPILER),str(path),'--compiler','texlive','--engine','xelatex'],capture_output=True,text=True)
        (folder/(name+'_compile-output.txt')).write_text(run.stdout+run.stderr)
        assert run.returncode==0,run.stdout+run.stderr
        warnings=[line for line in path.with_suffix('.log').read_text(errors='replace').splitlines() if any(tag in line for tag in ['Underfull','Warning:','Overfull','Missing character','Undefined control sequence','! '])]
        assert not warnings,warnings
        pdf=path.with_suffix('.pdf');subprocess.run(['qpdf','--check',str(pdf)],capture_output=True,check=True)
        dest=output/pdf.name;shutil.copy2(pdf,dest);assert sha(dest)==sha(pdf)
        with fitz.open(pdf) as doc:
            text='\n'.join(page.get_text() for page in doc)
            density=[len(re.sub(r'\s','',p.get_text())) for p in doc][1:]
            assert '\ufffd' not in text and not any(term in text for term in BANNED)
            if version=='学生详解':assert len(doc)-1>=56 and sum(density)>=31218
            if version=='教师备课':assert len(doc)-1>=71 and sum(density)>=45411
            row=dict(version=version,total_pages=len(doc),body_pages=len(doc)-1,pdf_extracted_body_nonspace=sum(density),per_page_nonspace=density,
                     low_density_pages=[i+2 for i,n in enumerate(density) if n<250],qpdf_passed=True,layout_errors=warnings,pdf_sha256=sha(pdf),build_output_identical=True,path=str(dest),source_metrics=metrics(md))
        (folder/(name+'_extracted.txt')).write_text(text);rows.append(row)
        print(json.dumps({k:row[k] for k in ['version','total_pages','body_pages','pdf_extracted_body_nonspace','low_density_pages','pdf_sha256']},ensure_ascii=False),flush=True)
    (ROOT/'build/pdf-build-manifest.json').write_text(json.dumps(dict(documents=rows,accepted=False,actual_visual_review=False,pending=['整套当前PDF实际审读']),ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
