"""复用已核验的Pandoc规则；只生成017分题工作预览，不冒充完整套卷。"""
from pathlib import Path
import argparse,importlib.util,json,re,subprocess
import fitz
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parents[1]/'蔡题020/整理版/scripts/preview_drafts.py'
spec=importlib.util.spec_from_file_location('rules020',BASE);rules=importlib.util.module_from_spec(spec);spec.loader.exec_module(rules)
pandoc_source,keep_math_leads=rules.pandoc_source,rules.keep_math_leads
COMPILER=rules.COMPILER
def main():
    parser=argparse.ArgumentParser();parser.add_argument('questions',nargs='*');args=parser.parse_args();report=[]
    for q in args.questions or ['01']:
        source=(ROOT/f'drafts/question-{q}.md').read_text();assert '<!-- question-complete -->' in source
        for version in ['student','teacher']:
            body=source.split('## 六、关键洞察')[0].rstrip()+'\n' if version=='student' else source
            name=f'working-q{q}-{version}';folder=ROOT/'preview'/name;folder.mkdir(parents=True,exist_ok=True)
            md=folder/f'{name}.md';md.write_text('---\ntitle: "第017套"\nshorttitle: "第017套"\nauthor: "物理竞赛资料"\n---\n'+body)
            run=subprocess.run(['pandoc','--from=markdown+raw_tex','--to=latex','--standalone',f'--template={ROOT/"latex/template.tex"}','--top-level-division=section'],input=pandoc_source(md.read_text(),version=='student'),capture_output=True,text=True,check=True)
            tex=re.sub(r'\.\./figures/([A-Za-z0-9_-]+)\.png',lambda m:str(ROOT/'figures'/f'{m.group(1)}.pdf'),run.stdout)
            tex=keep_math_leads(tex.replace(r'\begin{figure}',r'\begin{figure}[H]').replace(r'\caption{图',r'\caption*{图'))
            path=folder/f'{name}.tex';path.write_text(tex)
            run=subprocess.run(['python3',str(COMPILER),str(path),'--compiler','texlive','--engine','xelatex'],capture_output=True,text=True)
            (folder/'compile-output.txt').write_text(run.stdout+run.stderr);assert run.returncode==0,run.stdout+run.stderr
            log=path.with_suffix('.log').read_text(errors='replace')
            errors=[s for s in log.splitlines() if any(x in s for x in ['Overfull','Missing character','Undefined control sequence','! '])]
            assert not errors,errors
            pdf=path.with_suffix('.pdf');subprocess.run(['qpdf','--check',str(pdf)],capture_output=True,check=True)
            with fitz.open(pdf) as doc:
                density=[len(re.sub(r'\s','',p.get_text())) for p in doc][1:]
                item=dict(question=q,version=version,total_pages=len(doc),body_pages=len(doc)-1,body_nonspace=sum(density),per_page_nonspace=density,layout_warnings=errors)
            report.append(item);print(json.dumps(item,ensure_ascii=False),flush=True)
    (ROOT/'preview/working-draft-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
