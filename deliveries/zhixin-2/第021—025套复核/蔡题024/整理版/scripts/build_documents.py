"""固定版式的Pandoc—XeLaTeX构建；不添加局部扩页命令。"""
from pathlib import Path
import subprocess
import re
from preview_drafts import keep_math_leads,pandoc_source

ROOT=Path(__file__).resolve().parents[1]


def main():
    (ROOT/'build').mkdir(exist_ok=True)
    for label in ('试卷','学生详解','教师备课'):
        stem=f'蔡题024_{label}'
        result=subprocess.run(['pandoc',
                               '--from=markdown+raw_tex','--to=latex','--standalone',
                               f'--template={ROOT / "latex/template.tex"}',
                               '--top-level-division=section'],input=pandoc_source((ROOT/'markdown'/f'{stem}.md').read_text(),student=label=='学生详解'),check=True,capture_output=True,text=True)
        tex=re.sub(r'\.\./figures/([A-Za-z0-9_-]+)\.png',
                   lambda m:f'../figures/{m.group(1)}.pdf',result.stdout)
        tex=tex.replace(r'\begin{figure}',r'\begin{figure}[H]').replace(r'\caption{图',r'\caption*{图')
        tex=keep_math_leads(tex)
        (ROOT/'build'/f'{stem}.tex').write_text(tex)


if __name__=='__main__':main()

