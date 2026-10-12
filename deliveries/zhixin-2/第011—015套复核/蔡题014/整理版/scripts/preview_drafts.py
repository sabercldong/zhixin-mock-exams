"""014 per-question work previews. Never publish an incomplete formal set."""
from pathlib import Path
import argparse,hashlib,importlib.util,json,re,subprocess
import fitz
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'scripts/rules_shared.py'
spec=importlib.util.spec_from_file_location('rules020',BASE)
rules=importlib.util.module_from_spec(spec);spec.loader.exec_module(rules)
def keep_math_leads(tex):
    tex=rules.keep_math_leads(tex)
    blocks=tex.split('\n\n')
    for i in range(len(blocks)-1):
        lead=blocks[i].strip()
        if (re.match(r'^\\textbf\{(?:第\s*\d+\s*步|洞察\d+|变式\d+)',lead) and lead.endswith('}') and len(lead)<360):
            blocks[i]=blocks[i].rstrip()+r'\nopagebreak[4]'
    return '\n\n'.join(blocks)
def main():
    parser=argparse.ArgumentParser();parser.add_argument('questions',nargs='*');args=parser.parse_args();report=[]
    questions=args.questions or ['01']
    for q in questions:
        source=(ROOT/f'drafts/question-{q}.md').read_text()
        assert '<!-- model-clarification-pending:' not in source
        assert '<!-- draft-content-complete:' in source
        expected=['一、题型定位','二、知识点','三、物理图像','四、解题入口','五、解析','六、关键洞察','七、易错点','八、课堂讲解建议','九、变式训练']
        assert re.findall(r'(?m)^## (.*)$',source)==expected
        for version in ['student','teacher']:
            body=source.split('## 六、关键洞察')[0].rstrip()+'\n' if version=='student' else source
            name=f'working-q{q}-{version}'
            folder=ROOT/'preview'/name;folder.mkdir(parents=True,exist_ok=True)
            md=folder/f'{name}.md'
            md.write_text('---\ntitle: "第014套"\nshorttitle: "第014套"\nauthor: "物理竞赛资料"\n---\n'+body)
            run=subprocess.run(['pandoc','--from=markdown+raw_tex','--to=latex','--standalone',f'--template={ROOT/"latex/template.tex"}','--top-level-division=section'],input=rules.pandoc_source(md.read_text(),version=='student'),capture_output=True,text=True,check=True)
            tex=re.sub(r'\.\./figures/([A-Za-z0-9_-]+)\.png',lambda m:str(ROOT/'figures'/f'{m.group(1)}.pdf'),run.stdout)
            tex=keep_math_leads(tex.replace(r'\begin{figure}',r'\begin{figure}[H]').replace(r'\caption{图',r'\caption*{图'))
            path=folder/f'{name}.tex';path.write_text(tex)
            run=subprocess.run(['python3',str(rules.COMPILER),str(path),'--compiler','texlive','--engine','xelatex'],capture_output=True,text=True)
            (folder/'compile-output.txt').write_text(run.stdout+run.stderr)
            assert run.returncode==0,run.stdout+run.stderr
            log=path.with_suffix('.log').read_text(errors='replace')
            errors=[line for line in log.splitlines() if any(x in line for x in ['Overfull','Underfull','Missing character','Undefined control sequence','! ','Warning:'])]
            assert not errors,errors
            pdf=path.with_suffix('.pdf');subprocess.run(['qpdf','--check',str(pdf)],capture_output=True,check=True)
            with fitz.open(pdf) as doc:
                density=[len(re.sub(r'\s','',p.get_text())) for p in doc][1:]
                item=dict(question=q,version=version,total_pages=len(doc),body_pages=len(doc)-1,body_nonspace=sum(density),per_page_nonspace=density,layout_warnings=errors,pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),draft_sha256=hashlib.sha256((ROOT/f'drafts/question-{q}.md').read_bytes()).hexdigest(),actual_reviewed=False,accepted=False)
            report.append(item);print(json.dumps(item,ensure_ascii=False),flush=True)
    key='-q'.join(questions)
    (ROOT/f'preview/working-draft-check-q{key}.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':main()
