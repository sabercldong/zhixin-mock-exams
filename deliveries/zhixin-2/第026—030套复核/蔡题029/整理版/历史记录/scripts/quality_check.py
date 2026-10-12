"""第029套正式成品严格验收：页数、真实正文、核心一致与物理核验。"""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
import fitz

ROOT=Path(__file__).resolve().parents[1]
PROJECT=ROOT.parents[1]
sys.path.insert(0,str(PROJECT))
from document_pipeline import quality_check,split_front_matter,split_questions,STUDENT_TEACHER_LANGUAGE


def stats(path):
    doc=fitz.open(path)
    raw=subprocess.check_output(['pdftotext',str(path),'-'],text=True)
    body='\n'.join(p.get_text(clip=fitz.Rect(0,52,p.rect.width,p.rect.height-45)) for p in list(doc)[1:])
    questions=[]
    for page_number,p in enumerate(list(doc)[1:],2):
        text=p.get_text(clip=fitz.Rect(0,52,p.rect.width,p.rect.height-45))
        heading=re.search(r'^\s*第\s*([1-8])\s*题',text)
        if heading:questions.append(dict(question=int(heading.group(1)),first_pdf_page=page_number,body_pages=0,body_net_chars=0))
        assert questions,(path,page_number)
        questions[-1]['body_pages']+=1
        questions[-1]['body_net_chars']+=len(re.sub(r'\s+','',text))
    assert [q['question'] for q in questions]==list(range(1,9))
    return dict(pdf_pages=len(doc),body_pages=len(doc)-1,extracted_chars=len(raw),
                nonwhitespace_chars=len(re.sub(r'\s+','',raw)),
                body_net_chars=len(re.sub(r'\s+','',body)),per_question=questions)


def check_page_density(path):
    for i,p in enumerate(fitz.open(path)):
        if i==0:continue
        blocks=[b for b in p.get_text('blocks') if b[1]>55 and b[3]<p.rect.height-35]
        bottom=max((b[3] for b in blocks),default=0)
        chars=len(re.sub(r'\s+','',p.get_text()))
        assert not(bottom<280 and chars<300),('稀疏页',path.name,i+1,chars,bottom)


def check_step_leads(path):
    for i,p in enumerate(fitz.open(path)):
        if i==0:continue
        blocks=[b for b in p.get_text('blocks') if b[1]>55 and b[3]<p.rect.height-35]
        if not blocks:continue
        last=max(blocks,key=lambda b:b[3])[4].strip()
        assert not(re.match(r'^（[0-9]+）',last) and len(last.splitlines())<=2),('孤立步骤引导句',path.name,i+1,last)


def main():
    quality_check('029')
    report=dict(status='technical_acceptance_pass_pending_visual_review',documents={})
    originals={'试卷.pdf':'06d4734ed4577683a13e6b045d06a7c6d00f805627e3be956f2117d74080a229',
               '答案.pdf':'933bee10b2ddfc322fa00a46f6b45190593728f58408e78a513c1daf2bec1398'}
    for name,expected_hash in originals.items():
        assert hashlib.sha256((ROOT.parent/name).read_bytes()).hexdigest()==expected_hash,('原始资料发生变化',name)
    report['original_integrity']={'status':'pass','sha256':originals}
    for kind,label,minimum in (('paper','试卷',8),('student','学生详解',56),('teacher','教师备课',71)):
        path=ROOT/'output'/f'第029套_{label}版.pdf'
        current=stats(path)
        if kind!='paper':
            check_page_density(path)
            check_step_leads(path)
            benchmark=stats(PROJECT/'蔡题101/整理版/output/pdf'/f'蔡题101_{label}.pdf')
            assert current['body_pages']>=minimum,(kind,current['body_pages'])
            assert current['body_net_chars']>=benchmark['body_net_chars'],(kind,'正文净字符低于101',current,benchmark)
            current['benchmark101']={k:v for k,v in benchmark.items() if k!='per_question'}
        current['sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
        tex=(ROOT/'build'/f'蔡题029_{label}.tex').read_text()
        fixed_layout=(r'\documentclass[12pt,a4paper,UTF8]{ctexart}',
                      r'\usepackage[a4paper,top=22mm,bottom=22mm,left=22mm,right=22mm,headheight=15pt]{geometry}',
                      r'\setstretch{1.24}',r'\setlength{\parskip}{0.35em}')
        assert all(tex.count(item)==1 for item in fixed_layout),('固定版式参数被改变',kind)
        body=tex.split(r'\end{titlepage}')[1]
        assert not re.search(r'\\(?:setstretch|vspace|linespread|fontsize|enlargethispage)',body)
        assert body.count(r'\newpage')==7
        expected=8 if kind=='paper' else 32
        blocks=re.findall(r'\\begin\{figure\}\[H\](.*?)\\end\{figure\}',tex,re.S)
        assert len(blocks)==expected and all(r'\centering' in b for b in blocks)
        assert tex.count(r'\caption*{图')==expected
        report['documents'][kind]=current
    for md in (ROOT/'markdown').glob('*.md'):
        content=md.read_text()
        assert not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',content),('不可见控制字符',md.name)
        assert not re.search(r'(?<!\\)\b(?:left|right|frac|sqrt|qquad|quad|mathcal|mathrm)\b',content),('裸写数学命令',md.name)
    teacher=(ROOT/'markdown/蔡题029_教师备课.md').read_text()
    for q in split_questions(split_front_matter(teacher)[1]):
        parts=re.split(r'(?m)^## (.+)\n',q)
        for i in range(1,len(parts),2):
            if parts[i]!='八、课堂讲解建议':assert not STUDENT_TEACHER_LANGUAGE.search(parts[i+1])
        # 解答图在解析内，其前后正文必须显式使用图中的量。
        for title in ('一、题型定位','二、知识点','三、物理图像','四、解题入口'):
            index=parts.index(title)
            assert '![' not in parts[index+1],('解答图模块错误',q[:10],title)
    for pdf in (ROOT/'figures').glob('*.pdf'):
        subprocess.run(['qpdf','--check',str(pdf)],check=True,capture_output=True)
    for log in (ROOT/'figures').glob('*.log'):
        assert not re.search(r'Overfull|Missing character|LaTeX Error|Undefined control sequence',log.read_text(errors='replace'))
    verifications={}
    for q in range(1,9):
        data=json.loads((ROOT/'build'/f'question{q:02}-verification.json').read_text())
        assert str(data.get('status','')).lower() in ('pass','passed'),('物理核验未通过',q,data)
        verifications[f'{q:02}']=data
    report['verifications']=verifications
    report['tikz_figures']=32
    report['original_model_limitations']={
        'question01':'水平长板、有限厚度力矩忽略；相对速度确定摩擦；返程静摩擦维持恒速的可行性已验证。',
        'question02':'点质量同形收缩；三体ODE在奇异碰撞前终止并补足最后极小间距时间。',
        'question03':'水平绳、相同质量、独立非负张力；严格安全不包括同时临界边界。',
        'question04':'密度按原题手写10^3修正；T0=310K作体温估算；理想相变模型不冒称真实红细胞机制。',
        'question05':'电容毫法；热量有限有效数字；周期稳态与从零电压启动的周期能量分别保留。',
        'question06':'物方x1向左；前焦距f1、后焦距f2；亮度标准解限定为等输入光通量几何压缩，实际辐射模型另辨析。',
        'question07':'两体衰变质量阈值；全角度洛伦兹变换；最小速率含绝对值。',
        'question08':'无限等势板、准静态、弱磁场；常规电流向内，向上为正时力矩为负；奇异磁场整体力矩可积。'}
    report['fixed_layout']=dict(paper='A4',font_pt=12,margins_mm=22,
                                line_spacing=1.24,paragraph_spacing_em=0.35,
                                question_page_breaks=7)
    visual_record=ROOT/'preview/formal/visual-review.json'
    if visual_record.exists():
        visual=json.loads(visual_record.read_text())
        matched=all(visual.get('documents',{}).get(kind,{}).get('sha256')==info['sha256']
                    and visual['documents'][kind].get('overview_pages_reviewed')==info['pdf_pages']
                    for kind,info in report['documents'].items())
        if matched and visual.get('status')=='pass':
            report['status']='acceptance_pass'
            report['visual_review']=visual
    (ROOT/'build/strict-quality.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:{x:v[x] for x in ('pdf_pages','body_pages','extracted_chars','body_net_chars')}
                      for k,v in report['documents'].items()},ensure_ascii=False,indent=2))


if __name__=='__main__':main()

