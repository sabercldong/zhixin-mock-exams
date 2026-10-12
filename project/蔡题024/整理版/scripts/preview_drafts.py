"""分题工作稿预览，不产生缺题的正式成品。"""
from pathlib import Path
import argparse
import json
import re
import subprocess
import fitz

ROOT=Path(__file__).resolve().parents[1]
COMPILER=Path('/Users/dongxingxi/.codex/plugins/cache/openai-bundled/latex/0.2.8/scripts/compile_latex.py')

def pandoc_source(text,student=False):
    # 题干边界是源文索引，不应与独立图片形成同一段落。
    # 移除构建时标记，让Pandoc将题图生成有图注的居中figure。
    text=re.sub(r'<!--\s*question-(?:start|end)\s*-->','\n\n',text)
    # 仅将有限逻辑块保持在同页；学生题末的检验段只在学生版保持，
    # 教师版后续还有四模块，允许该段正常跨页，避免推挤其末页。
    assert text.count('<!-- KEEP_STUDENT_START -->')==text.count('<!-- KEEP_STUDENT_END -->')
    if student:
        text=text.replace('<!-- KEEP_STUDENT_START -->','<!-- KEEP_TOGETHER_START -->').replace('<!-- KEEP_STUDENT_END -->','<!-- KEEP_TOGETHER_END -->')
    else:
        text=text.replace('<!-- KEEP_STUDENT_START -->','').replace('<!-- KEEP_STUDENT_END -->','')
    assert text.count('<!-- KEEP_TOGETHER_START -->')==text.count('<!-- KEEP_TOGETHER_END -->')
    return text.replace('<!-- KEEP_TOGETHER_START -->',r'\KEEPTOGETHERSTART').replace('<!-- KEEP_TOGETHER_END -->',r'\KEEPTOGETHEREND')

def keep_math_leads(tex):
    # 显式同页块中的短表用普通 tabular，不让 longtable 在题末拆成残表。
    # 只改变分页机制，不改变字号、行距、正文、公式或列宽。
    def compact_table(match):
        table=match.group(0)
        assert r'\endfirsthead' not in table and table.count(r'\\')<=12
        table=table.replace(r'\begin{longtable}[]',r'\noindent\begin{tabular}')
        table=table.replace(r'\endhead','')
        table=table.replace('\\bottomrule\\noalign{}\n\\endlastfoot','')
        return table.replace(r'\end{longtable}',r'\bottomrule\end{tabular}')
    tex=re.sub(r'\\KEEPTOGETHERSTART.*?\\KEEPTOGETHEREND',
               lambda m:re.sub(r'\\begin\{longtable\}\[\].*?\\end\{longtable\}',
                               compact_table,m.group(0),flags=re.S),tex,flags=re.S)
    blocks=tex.split('\n\n')
    for i in range(len(blocks)-1):
        lead=blocks[i].strip()
        step_intro=bool(re.match(r'^[（(]\d+[）)]',lead))
        math_intro=(blocks[i+1].lstrip().startswith(r'\[') and re.search(r'[\u4e00-\u9fff]',lead)
                    and not lead.startswith('\\') and len(lead.replace('\n',''))<=100)
        if step_intro or math_intro:
            blocks[i]=blocks[i].rstrip()+r'\nopagebreak[4]'
    text='\n\n'.join(blocks).replace(r'\KEEPTOGETHERSTART',r'\begin{logicalblock}').replace(r'\KEEPTOGETHEREND',r'\end{logicalblock}')
    # 模块标题在 minipage 顶部原有的前距会消失，只恢复 ctexset 中
    # 既定的 subsection 前距，不向正文增加额外空白。
    return re.sub(r'\\begin\{logicalblock\}(\s*\\subsection\b.*?)\\end\{logicalblock\}',
                  lambda m:r'\begin{headedlogicalblock}'+m.group(1)+r'\end{headedlogicalblock}',
                  text,flags=re.S)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('questions',nargs='*')
    args=parser.parse_args();report=[]
    for q in args.questions or ['01']:
        original=(ROOT/f'drafts/question-{q}.md').read_text()
        for version in ['student','teacher']:
            body=original.split('## 六、关键洞察')[0].rstrip()+'\n' if version=='student' else original
            name=f'working-q{q}-{version}';folder=ROOT/'preview'/name;folder.mkdir(parents=True,exist_ok=True)
            md=folder/(name+'.md');md.write_text('---\ntitle: "第024套"\nshorttitle: "第024套"\nauthor: "物理竞赛资料"\n---\n'+body)
            result=subprocess.run(['pandoc','--from=markdown+raw_tex','--to=latex','--standalone',f'--template={ROOT/"latex/template.tex"}','--top-level-division=section'],input=pandoc_source(md.read_text(),student=version=='student'),check=True,capture_output=True,text=True)
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

