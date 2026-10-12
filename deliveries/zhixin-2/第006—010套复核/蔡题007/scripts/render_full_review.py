"""生成审读图像与页索引；此脚本不把生成图像等同于实际审读。"""
from pathlib import Path
import argparse,re,json,hashlib,importlib.util
import fitz
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'preview/full-review';DEST.mkdir(parents=True,exist_ok=True)
def figures():
 spec=importlib.util.spec_from_file_location('r',ROOT/'scripts/render_figures.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 for q,names in m.NAMES.items():
  sheet=Image.new('RGB',(1800,1500),'#eeeeee');d=ImageDraw.Draw(sheet)
  for i,n in enumerate(names):
   im=Image.open(ROOT/'figures'/f'{n}.png').convert('RGB');im.thumbnail((860,455));x=i%2*900;y=i//2*500
   sheet.paste(im,(x+(900-im.width)//2,y+35+(455-im.height)//2));d.text((x+25,y+12),n,fill='black')
  sheet.save(DEST/f'figures-{q}.jpg')
def documents():
 index=[]
 for label,slug in [('试卷','paper'),('学生详解','student'),('教师备课','teacher')]:
  src=ROOT/'output/pdf'/f'蔡题007_{label}.pdf'
  with fitz.open(src) as doc:
   hashes=hashlib.sha256(src.read_bytes()).hexdigest();items=[];sheets=[]
   for start in range(0,len(doc),6):
    sheet=Image.new('RGB',(1800,2700),'#dddddd');draw=ImageDraw.Draw(sheet)
    for j,page in enumerate(list(doc)[start:start+6]):
     pm=page.get_pixmap(matrix=fitz.Matrix(1.3,1.3),alpha=False);im=Image.frombytes('RGB',[pm.width,pm.height],pm.samples);im.thumbnail((850,840))
     x=j%2*900;y=j//2*900;sheet.paste(im,(x+(900-im.width)//2,y+35));draw.text((x+20,y+10),f'{slug} physical page {start+j+1}',fill='black')
     items.append(dict(physical_page=start+j+1,body_page=start+j if start+j else None,text=page.get_text()[:180],nonspace=len(re.sub(r'\s','',page.get_text())),body_bottom=max((b[3] for b in page.get_text('blocks') if b[1]>58 and b[3]<800),default=0)))
    target=DEST/f'{slug}-{start+1:03d}-{min(start+6,len(doc)):03d}.jpg';sheet.save(target);sheets.append(str(target))
   index.append(dict(version=label,slug=slug,sha256=hashes,pages=len(doc),overview_sheets=sheets,page_index=items))
 (DEST/'rendered-index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps([dict(version=x['version'],pages=x['pages'],sheets=len(x['overview_sheets']),sha256=x['sha256']) for x in index],ensure_ascii=False))
def hd(slug,nums):
 label={'paper':'试卷','student':'学生详解','teacher':'教师备课'}[slug]
 with fitz.open(ROOT/'output/pdf'/f'蔡题007_{label}.pdf') as doc:
  for n in nums:doc[n-1].get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).save(DEST/f'{slug}-hd-{n:03d}.png')
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--figures',action='store_true');a.add_argument('--documents',action='store_true');a.add_argument('--hd',choices=['paper','student','teacher']);a.add_argument('pages',type=int,nargs='*');args=a.parse_args()
 if args.figures:figures()
 if args.documents:documents()
 if args.hd:hd(args.hd,args.pages)
