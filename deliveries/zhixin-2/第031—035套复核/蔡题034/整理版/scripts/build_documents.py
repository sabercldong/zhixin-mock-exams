"""固定版式的Pandoc—XeLaTeX构建；不添加局部扩页命令。"""
from pathlib import Path
import subprocess
import re
from preview_drafts import keep_math_leads

ROOT=Path(__file__).resolve().parents[1]


def keep_figure_leads(tex):
    """图及其直接说明同页，不增字号、行距或强制分页。"""
    blocks=tex.split('\n\n')
    for i in range(len(blocks)-1):
        lead=blocks[i].strip()
        if (blocks[i+1].lstrip().startswith(r'\begin{figure}[H]')
            and 'network-05.pdf' in blocks[i+1]
            and re.search(r'[\u4e00-\u9fff]',lead)
            and not lead.startswith('\\') and len(lead)<=1000):
            blocks[i]='\\noindent\\begin{minipage}{\\linewidth}\n'+blocks[i]
            blocks[i+1]=blocks[i+1].replace(
                r'\end{figure}',r'\end{figure}'+'\n\\end{minipage}',1)
    return '\n\n'.join(blocks)


def main():
    (ROOT/'build').mkdir(exist_ok=True)
    for label in ('试卷','学生详解','教师备课'):
        stem=f'蔡题034_{label}'
        result=subprocess.run(['pandoc',str(ROOT/'markdown'/f'{stem}.md'),
                               '--from=markdown+raw_tex','--to=latex','--standalone',
                               f'--template={ROOT / "latex/template.tex"}',
                               '--top-level-division=section'],check=True,capture_output=True,text=True)
        tex=re.sub(r'\.\./figures/([A-Za-z0-9_-]+)\.png',
                   lambda m:f'../figures/{m.group(1)}.pdf',result.stdout)
        tex=tex.replace(r'\begin{figure}',r'\begin{figure}[H]').replace(r'\caption{图',r'\caption*{图')
        tex=keep_math_leads(tex)
        tex=keep_figure_leads(tex)
        (ROOT/'build'/f'{stem}.tex').write_text(tex)


if __name__=='__main__':main()
