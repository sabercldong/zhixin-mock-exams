"""选择各题题首、图文衔接、公式密集及题末页面，渲染后由实际审图确认。"""
from pathlib import Path
import json
import re
import subprocess
import sys
import fitz
ROOT=Path(__file__).resolve().parents[1]
def main():
    report=json.loads((ROOT/'build/strict-quality.json').read_text())
    targets=[]
    for kind,label in [('paper','试卷'),('student','学生详解'),('teacher','教师备课')]:
        doc=fitz.open(ROOT/'output'/f'第022套_{label}版.pdf')
        if kind=='paper':pages=list(range(1,len(doc)+1))
        else:
            pages=set()
            for q in report['documents'][kind]['per_question']:
                first=q['first_pdf_page'];last=first+q['body_pages']-1
                pages.update([first,(first+last)//2,last])
            # 全部解析图所在页额外选入；保证不是只查看题首图。
            for number,page in enumerate(doc,1):
                text=page.get_text()
                if re.search(r'图\s*[1-8]\s*[-－]\s*[2-6]',text):pages.add(number)
            pages=sorted(pages)
        targets.extend(f'{kind}:{n}' for n in pages)
    subprocess.run([sys.executable,str(ROOT/'scripts/render_review_details.py'),*targets],check=True)
    subprocess.run([sys.executable,str(ROOT/'scripts/review_montages.py')],check=True)
if __name__=='__main__':main()

