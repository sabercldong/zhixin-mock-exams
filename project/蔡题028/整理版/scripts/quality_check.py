"""第028套正式成品严格验收：页数、真实正文、核心一致与物理核验。"""
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
from tools.document_pipeline import quality_check,split_front_matter,split_questions,STUDENT_TEACHER_LANGUAGE


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
    quality_check('028')
    report=dict(status='technical_acceptance_pass_pending_visual_review',documents={})
    originals={'试卷.pdf':'3c413675107668a7f2f50ea2bcdc562bc28e495f143aa5e8c247086f2c1ef37d'}
    for name,expected_hash in originals.items():
        assert hashlib.sha256((ROOT.parent/name).read_bytes()).hexdigest()==expected_hash,('原始资料发生变化',name)
    report['original_integrity']={'status':'pass','sha256':originals}
    for kind,label,minimum in (('paper','试卷',8),('student','学生详解',56),('teacher','教师备课',71)):
        path=ROOT/'output'/f'第028套_{label}版.pdf'
        current=stats(path)
        if kind!='paper':
            check_page_density(path)
            check_step_leads(path)
            benchmark=stats(PROJECT/'蔡题101/整理版/output/pdf'/f'蔡题101_{label}.pdf')
            assert current['body_pages']>=minimum,(kind,current['body_pages'])
            assert current['body_net_chars']>=benchmark['body_net_chars'],(kind,'正文净字符低于101',current,benchmark)
            current['benchmark101']={k:v for k,v in benchmark.items() if k!='per_question'}
        current['sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
        tex=(ROOT/'build'/f'蔡题028_{label}.tex').read_text()
        fixed_layout=(r'\documentclass[12pt,a4paper,UTF8]{ctexart}',
                      r'\usepackage[a4paper,top=22mm,bottom=22mm,left=22mm,right=22mm,headheight=15pt]{geometry}',
                      r'\setstretch{1.24}',r'\setlength{\parskip}{0.35em}')
        assert all(tex.count(item)==1 for item in fixed_layout),('固定版式参数被改变',kind)
        body=tex.split(r'\end{titlepage}')[1]
        assert not re.search(r'\\(?:setstretch|vspace|linespread|fontsize|enlargethispage)',body)
        assert body.count(r'\newpage')==7
        expected=8 if kind=='paper' else 31
        blocks=re.findall(r'\\begin\{figure\}\[H\](.*?)\\end\{figure\}',tex,re.S)
        assert len(blocks)==expected and all(r'\centering' in b for b in blocks)
        assert tex.count(r'\caption*{图')==expected
        report['documents'][kind]=current
    for md in (ROOT/'markdown').glob('*.md'):
        content=md.read_text()
        assert not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',content),('不可见控制字符',md.name)
        assert not re.search(r'(?<!\\)\b(?:left|right|frac|sqrt|qquad|quad|mathcal|mathrm)\b',content),('裸写数学命令',md.name)
    teacher=(ROOT/'markdown/蔡题028_教师备课.md').read_text()
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
    report['tikz_figures']=31
    report['original_model_limitations']={
        'question01':'2v疑误已经用户确认按2f；准静态近轴；真实物距须正且有限。',
        'question02':'筒碰前固定、碰后解除；持续滚动摩擦阈值高于冲量阈值；支撑域检验。',
        'question03':'平面内仅线性阻力；终态与有限时间瞬时零速分别给出。',
        'question04':'滑动摩擦等于最大静摩擦为明确补充模型；原给条件不保证唯一循环。',
        'question05':'零初始电流与零初始加速度；三种阻尼及无电阻极限完整。',
        'question06':'动量分量非完整总力；旁路保留长度参数；总纤维数44%与单位长度20%区分。',
        'question07':'坐标事件时间与光信号接收时刻分别计算。',
        'question08':'均匀体电荷；有q/无q分别处理；theta从+x到+z；远场非全空间精确等效。'}
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


