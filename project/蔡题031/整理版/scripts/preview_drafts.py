"""分题工作稿预览，不产生缺题的正式成品。"""
from pathlib import Path
import argparse
import json
import re
import subprocess
import fitz

ROOT=Path(__file__).resolve().parents[1]
COMPILER=Path('/Users/dongxingxi/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py')

def pandoc_source(text):
    # 仅将定义域—临界角—适用条件这个有限逻辑块保持在同页；
    # Markdown保留隐藏标记，正文不增加分页或间距命令。
    assert text.count('<!-- KEEP_TOGETHER_START -->')==text.count('<!-- KEEP_TOGETHER_END -->')
    return text.replace('<!-- KEEP_TOGETHER_START -->',r'\KEEPTOGETHERSTART').replace('<!-- KEEP_TOGETHER_END -->',r'\KEEPTOGETHEREND')

def keep_math_leads(tex):
    blocks=tex.split('\n\n')
    for i in range(len(blocks)-1):
        lead=blocks[i].strip()
        step_intro=bool(re.match(r'^[（(]\d+[）)]',lead))
        math_intro=(blocks[i+1].lstrip().startswith(r'\[') and re.search(r'[\u4e00-\u9fff]',lead)
                    and not lead.startswith('\\') and len(lead.replace('\n',''))<=100)
        if step_intro or math_intro:
            blocks[i]=blocks[i].rstrip()+r'\nopagebreak[4]'
    return '\n\n'.join(blocks).replace(r'\KEEPTOGETHERSTART',r'\begin{logicalblock}').replace(r'\KEEPTOGETHEREND',r'\end{logicalblock}')

def main():
    parser=argparse.ArgumentParser();parser.add_argument('questions',nargs='*')
    args=parser.parse_args();report=[]
    for q in args.questions or ['01']:
        original=(ROOT/f'drafts/question-{q}.md').read_text()
        for version in ['student','teacher']:
            body=original.split('## 六、关键洞察')[0].rstrip()+'\n' if version=='student' else original
            name=f'working-q{q}-{version}';folder=ROOT/'preview'/name;folder.mkdir(parents=True,exist_ok=True)
            md=folder/(name+'.md');md.write_text('---\ntitle: "第031套"\nshorttitle: "第031套"\nauthor: "物理竞赛资料"\n---\n'+body)
            result=subprocess.run(['pandoc','--from=markdown+raw_tex','--to=latex','--standalone',f'--template={ROOT/"latex/template.tex"}','--top-level-division=section'],input=pandoc_source(md.read_text()),check=True,capture_output=True,text=True)
            tex=re.sub(r'\.\./figures/([A-Za-z0-9_-]+)\.png',lambda m:str(ROOT/'figures'/(m.group(1)+'.pdf')),result.stdout)
            tex=tex.replace(r'\begin{figure}',r'\begin{figure}[H]').replace(r'\caption{图',r'\caption*{图');tex=keep_math_leads(tex)
            path=folder/(name+'.tex');path.write_text(tex)
            result=subprocess.run(['python3',str(COMPILER),str(path),'--compiler','texlive','--engine','xelatex'],capture_output=True,text=True)
            (folder/'compile-output.txt').write_text(result.stdout+result.stderr)
            assert result.returncode==0,(name,result.stdout,result.stderr)
            pdf=folder/(name+'.pdf');subprocess.run(['qpdf','--check',str(pdf)],check=True,capture_output=True)
            log=path.with_suffix('.log').read_text(errors='replace')
            warnings=[s for s in log.splitlines() if any(x in s for x in ['Overfull','Missing character','! '])]
            doc=fitz.open(pdf);density=[len(re.sub(r'\s','',p.get_text())) for p in doc][1:]
            item=dict(question=q,version=version,total_pages=len(doc),body_pages=len(doc)-1,body_nonspace=sum(density),per_page_nonspace=density,layout_warnings=warnings)
            report.append(item);print(json.dumps(item,ensure_ascii=False),flush=True)
    (ROOT/'preview'/'working-draft-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

if __name__=='__main__':main()
