import re

def pandoc_source(text,student=False):
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
    blocks=tex.split('\n\n')
    for i in range(len(blocks)-1):
        lead=blocks[i].strip()
        step_intro=bool(re.match(r'^[（(]\d+[）)]',lead))
        math_intro=(blocks[i+1].lstrip().startswith(r'\[') and re.search(r'[\u4e00-\u9fff]',lead)
                    and not lead.startswith('\\') and len(lead.replace('\n',''))<=100)
        if step_intro or math_intro:
            blocks[i]=blocks[i].rstrip()+r'\nopagebreak[4]'
    return '\n\n'.join(blocks).replace(r'\KEEPTOGETHERSTART',r'\begin{logicalblock}').replace(r'\KEEPTOGETHEREND',r'\end{logicalblock}')
