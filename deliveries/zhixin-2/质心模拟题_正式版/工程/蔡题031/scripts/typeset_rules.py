import re

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
