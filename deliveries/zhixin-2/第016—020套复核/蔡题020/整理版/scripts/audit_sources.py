"""源稿结构、数学书写、图片和一致性检查；不替代物理和实际PDF审读。"""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
MODULES=['一、题型定位','二、知识点','三、物理图像','四、解题入口','五、解析','六、关键洞察','七、易错点','八、课堂讲解建议','九、变式训练']
BANNED=['数字化重构','完成本题','继续下一题','原卷图','进一步思考与自测','解题顺序与直观复盘']
def metrics(text):
    no_meta=re.sub(r'\A---\n.*?\n---\n','',text,flags=re.S)
    no_meta=re.sub(r'<!--.*?-->','',no_meta,flags=re.S)
    body=re.sub(r'(?m)^#{1,6} .*\n','',no_meta)
    body=re.sub(r'!\[[^]]*\]\([^)]+\)(?:\{[^}]*\})?','',body)
    body=re.sub(r'\\(?:newpage|begin|end)\b(?:\{[^}]*\})?','',body)
    body=re.sub(r'\\[A-Za-z]+\*?','',body)
    body=re.sub(r'[{}$&\\]','',body)
    return dict(raw_with_whitespace=len(text),raw_nonspace=len(re.sub(r'\s','',text)),body_net_characters=len(re.sub(r'\s','',body)))
def inspect(q):
    path=ROOT/f'drafts/question-{q}.md';text=path.read_text();issues=[]
    modules=re.findall(r'(?m)^## (.*)$',text)
    if modules!=MODULES:issues.append('module_sequence')
    if len(re.findall(r'(?m)^# 第\d+题$',text))!=1:issues.append('question_heading')
    if re.search(r'(?m)^#{3,6} ',text):issues.append('extra_heading')
    if text.count('<!-- question-start -->')!=1 or text.count('<!-- question-end -->')!=1:issues.append('question_boundaries')
    for term in BANNED:
        if term in text:issues.append('banned:'+term)
    if re.search(r'https?://|\]\((?!\.\./figures/)',text):issues.append('reference_link')
    if re.search(r'[\u200b-\u200d\ufeff\ufffd]',text):issues.append('invisible_or_replacement')
    outside=text.split('## 八、课堂讲解建议')[0]+text.split('## 九、变式训练')[-1]
    if re.search(r'课堂|教师|板书|让学生',outside):issues.append('teacher_language_outside_module8')
    if re.search(r'\\(?:newpage|clearpage|setstretch|linespread|fontsize|vspace|enlargethispage|addtolength|setlength)\b',text):issues.append('local_pagination_or_expansion')
    formulas=re.findall(r'\$\$(.*?)\$\$|\$(.*?)\$',text,flags=re.S)
    if re.search(r'(?m)^\s*\$\s*$',text):issues.append('single_dollar_display_delimiter')
    for pairs in formulas:
        math=''.join(pairs)
        if re.search(r'(?<![\\A-Za-z])(?:sqrt|qquad|frac|begin|end|sin|cos|theta|omega|mu|gamma|beta|pi)\b',math):issues.append('bare_math_command')
        braces=re.sub(r'\\[{}]','',math);depth=0
        for char in braces:
            depth+=(char=='{')-(char=='}')
            if depth<0:issues.append('unbalanced_braces');break
        if depth!=0:issues.append('unbalanced_braces')
    remainder=re.sub(r'\$\$.*?\$\$|\$.*?\$','',text,flags=re.S)
    if '$' in remainder:issues.append('unbalanced_dollars')
    figs=re.findall(r'!\[([^]]*)\]\((\.\./figures/[^)]+)\)',text)
    for caption,rel in figs:
        png=(path.parent/rel).resolve();pdf=png.with_suffix('.pdf')
        if not png.exists() or not pdf.exists():issues.append('missing_figure:'+rel)
        tag=re.match(r'图(\d+-\d+)',caption)
        if not tag:issues.append('missing_neutral_caption')
        elif text.count('图'+tag.group(1))<2:issues.append('unreferenced_figure:'+tag.group(1))
    student=text.split('## 六、关键洞察')[0]
    return dict(question=int(q),issues=sorted(set(issues)),student=metrics(student),teacher=metrics(text),figures=len(figs),sha256=hashlib.sha256(path.read_bytes()).hexdigest())
def main():
    rows=[inspect(f'{q:02}') for q in range(1,9)]
    report=dict(scope='draft source only; PDF physics and visual checks required separately',metrics_definition='raw source counts separate; net body removes metadata, comments, headings, image markup, TeX control words and whitespace',questions=rows,passed=all(not row['issues'] for row in rows))
    (ROOT/'build/source-quality.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False),flush=True)
    if not report['passed']:raise SystemExit(1)
if __name__=='__main__':main()
