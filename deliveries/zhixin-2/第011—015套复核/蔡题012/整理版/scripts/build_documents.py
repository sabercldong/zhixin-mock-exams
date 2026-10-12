"""完整套卷需要八题；--working 只输出已核验分题的工作预览。"""
from pathlib import Path
import argparse,importlib.util,json,re,subprocess,hashlib
import fitz
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('rules',ROOT/'scripts/preview_drafts.py');rules=importlib.util.module_from_spec(spec);spec.loader.exec_module(rules)
HEADS=['一、题型定位','二、知识点','三、物理图像','四、解题入口','五、解析','六、关键洞察','七、易错点','八、课堂讲解建议','九、变式训练']
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--working',action='store_true');args=ap.parse_args()
 files=sorted((ROOT/'drafts').glob('question-[0-9][0-9].md'))
 files=[p for p in files if '<!-- question-complete -->' in p.read_text()]
 if not args.working:assert len(files)==8,'正式套卷必须有全部八题；当前仅允许--working预览'
 assert files
 sections=[p.read_text() for p in files]
 for p,s in zip(files,sections):
  assert re.findall(r'^## (.+)$',s,re.M)==HEADS,p
  assert s.count('<!-- question-start -->')==s.count('<!-- question-end -->')==1,p
  assert not any(x in s for x in ['数字化重构','完成本题','继续下一题','原卷图','http://','https://'])
  assert not re.search(r'(?<!\\)\b(?:sqrt|quad|qquad|frac|begin|end)\b',re.sub(r'<!--.*?-->','',s,flags=re.S))
  for name in re.findall(r'\(\.\./figures/([\w-]+)\.png\)',s):assert (ROOT/'figures'/f'{name}.pdf').exists()
  for part in s.split('## ')[1:]:
   if not part.startswith('八、课堂讲解建议'):assert not any(x in part for x in ['让学生','教师先','课堂先','板书','课堂讨论']),p
 teacher='\n\n\\newpage\n\n'.join(sections)
 students=[];papers=[]
 for s in sections:
  student=s.split('## 六、关键洞察')[0].rstrip()+'\n';students.append(student)
  papers.append(s[:s.index('<!-- question-end -->')+len('<!-- question-end -->')].rstrip()+'\n')
 base=ROOT/'preview/first-two' if args.working else ROOT
 md_dir=base/'markdown';build=base/'build';out=base/'output/pdf'
 for d in [md_dir,build,out]:d.mkdir(parents=True,exist_ok=True)
 bodies={'试卷':'\n\n\\newpage\n\n'.join(papers),'学生详解':'\n\n\\newpage\n\n'.join(students),'教师备课':teacher}
 report=[]
 for label,body in bodies.items():
  name=f'蔡题012_{label}';md=md_dir/f'{name}.md';text='---\ntitle: "第012套"\nshorttitle: "第012套"\nauthor: "物理竞赛资料"\n---\n\n'+body
  md.write_text(text)
  student=label=='学生详解'
  proc=subprocess.run(['pandoc','--from=markdown+raw_tex','--to=latex','--standalone',f'--template={ROOT/"latex/template.tex"}','--top-level-division=section'],input=rules.pandoc_source(text,student=student),capture_output=True,text=True,check=True)
  tex=re.sub(r'\.\./figures/([\w-]+)\.png',lambda m:f'../figures/{m.group(1)}.pdf',proc.stdout)
  tex=rules.keep_math_leads(tex.replace(r'\begin{figure}',r'\begin{figure}[H]').replace(r'\caption{图',r'\caption*{图'))
  target=build/f'{name}.tex';target.write_text(tex)
  run=subprocess.run(['python3',str(rules.COMPILER),str(target),'--compiler','texlive','--engine','xelatex'],capture_output=True,text=True)
  (build/f'{name}_compile.txt').write_text(run.stdout+run.stderr);assert run.returncode==0,run.stdout+run.stderr
  log=target.with_suffix('.log').read_text(errors='replace');bad=[s for s in log.splitlines() if any(x in s for x in ['Overfull','Missing character','Undefined control sequence','! '])];assert not bad,bad
  pdf=target.with_suffix('.pdf');subprocess.run(['qpdf','--check',str(pdf)],capture_output=True,check=True)
  dest=out/pdf.name;dest.write_bytes(pdf.read_bytes());assert hashlib.sha256(dest.read_bytes()).digest()==hashlib.sha256(pdf.read_bytes()).digest()
  with fitz.open(pdf) as doc:
   density=[len(re.sub(r'\s','',p.get_text())) for p in doc][1:];pages=len(doc)
   for p in doc:assert '\ufffd' not in p.get_text()
  if not args.working and label!='试卷':assert pages-1>=({'学生详解':56,'教师备课':71}[label])
  report.append(dict(version=label,question_count=len(files),total_pages=pages,body_pages=pages-1,body_nonspace=sum(density),per_page_nonspace=density,layout_warnings=bad,sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),path=str(dest)))
 result=dict(build_complete=not args.working,full_set_complete=False,working_preview=args.working,questions=[p.stem for p in files],template_sha256=hashlib.sha256((ROOT/'latex/template.tex').read_bytes()).hexdigest(),documents=report)
 (base/'build_report.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(result,ensure_ascii=False),flush=True)
if __name__=='__main__':main()
