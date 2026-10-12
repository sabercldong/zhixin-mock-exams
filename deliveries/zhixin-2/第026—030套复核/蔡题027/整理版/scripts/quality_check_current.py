"""Current source/PDF checks; no external set directory is required."""
from pathlib import Path
import re,json,hashlib,subprocess
import fitz
from document_pipeline import quality_check
ROOT=Path(__file__).resolve().parents[1]
def main():
 quality_check('027')
 benchmark=json.loads((ROOT/'baseline-review/benchmark101.json').read_text())
 report=dict(technical_passed=True,actual_visual_review=False,documents={},source_sha256={})
 for q in range(1,9):
  path=ROOT/f'drafts/question-{q:02d}.md'
  report['source_sha256'][str(path.relative_to(ROOT))]=hashlib.sha256(path.read_bytes()).hexdigest()
 for v in ['试卷','学生详解','教师备课']:
  p=ROOT/'output'/f'第027套_{v}版.pdf'
  with fitz.open(p) as doc:
   body='\n'.join(page.get_text(clip=fitz.Rect(0,52,page.rect.width,page.rect.height-45)) for page in list(doc)[1:])
   current=dict(total_pages=len(doc),body_pages=len(doc)-1,body_net_chars=len(re.sub(r'\s','',body)),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
   if v!='试卷':
    assert current['body_pages']>=(56 if v=='学生详解' else 71)
    assert current['body_net_chars']>=benchmark[v]['body_net_chars']
   for page in doc:
    assert abs(page.rect.width-595.276)<.1 and abs(page.rect.height-841.89)<.1
    assert '\ufffd' not in page.get_text()
   tex=(ROOT/'build'/f'蔡题027_{v}.tex').read_text()
   assert tex.split(r'\end{titlepage}')[1].count(r'\newpage')==7
   report['documents'][v]=current
 (ROOT/'build/current-quality.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(report['documents'],ensure_ascii=False),flush=True)
if __name__=='__main__':main()
