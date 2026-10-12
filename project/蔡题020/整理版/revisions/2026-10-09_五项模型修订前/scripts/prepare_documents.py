"""由教师主稿提取学生前五模块及题干；只保留七个题间分页。"""
from pathlib import Path
import hashlib,json,re
from audit_sources import inspect,metrics,MODULES
ROOT=Path(__file__).resolve().parents[1]
HEADER='---\ntitle: "第020套"\nshorttitle: "第020套"\nauthor: "物理竞赛资料"\ntoc: false\n---\n\n'
def assemble(chunks):
    assert len(chunks)==8
    return HEADER+'\n\n\\newpage\n\n'.join(chunk.rstrip() for chunk in chunks)+'\n'
def main():
    drafts=[(ROOT/f'drafts/question-{q:02}.md').read_text().rstrip() for q in range(1,9)]
    for q in range(1,9):assert not inspect(f'{q:02}')['issues']
    folder=ROOT/'markdown';folder.mkdir(exist_ok=True)
    teacher=assemble(drafts);master=folder/'蔡题020_教师备课.md';master.write_text(teacher)
    # 必须从刚写出的教师主文件提取，不能把教师模块八、九改名后拼入学生。
    source=master.read_text()
    parts=re.split(r'(?m)^# 第(\d+)题\n',source)[1:]
    student_chunks=[];paper_chunks=[]
    assert len(parts)==16
    for i in range(0,len(parts),2):
        number=int(parts[i]);body=parts[i+1]
        body=re.sub(r'(?m)^\\newpage\s*$','',body).strip()
        headings=re.findall(r'(?m)^## (.*)$',body);assert headings==MODULES
        student=body.split('## 六、关键洞察',1)[0].rstrip()
        assert re.findall(r'(?m)^## (.*)$',student)==MODULES[:5]
        question=re.search(r'<!-- question-start -->(.*?)<!-- question-end -->',body,re.S).group(1).strip()
        student_chunks.append(f'# 第{number}题\n\n'+student)
        paper_chunks.append(f'# 第{number}题\n\n'+question)
    documents={'教师备课':teacher,'学生详解':assemble(student_chunks),'试卷':assemble(paper_chunks)}
    record={}
    for version,text in documents.items():
        assert text.count(r'\newpage')==7
        path=folder/f'蔡题020_{version}.md';path.write_text(text)
        record[version]=dict(path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),**metrics(text))
    report=dict(paper='020',documents=record,question_count=8,student_modules=5,teacher_modules=9,question_pagebreaks=7,
                accepted=False,pending=['第3题自由偏心初始条件约定待确认','整套实际PDF审读尚未完成'])
    (ROOT/'build/document-source-manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False),flush=True)
if __name__=='__main__':main()

