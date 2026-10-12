from pathlib import Path
import argparse,re,subprocess,json,hashlib,shutil
import fitz
from PIL import Image,ImageDraw

BASE=Path(__file__).resolve().parent
WORK=Path(__file__).resolve().parent
HEADS=['一、题型定位','二、知识点','三、物理图像','四、解题入口','五、解析','六、关键洞察','七、易错点','八、课堂讲解建议','九、变式训练']

def compile_tex(p):
    for _ in range(2):
        run=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error',p.name],cwd=p.parent,capture_output=True,text=True)
        if run.returncode:raise RuntimeError(run.stdout[-3500:])


def split_figures(root,n):
    p=root/f'figures/蔡题{n:03}_图稿源文件.tex'
    names=re.findall(r'(?m)^%\s*\d+\s+([a-zA-Z0-9_-]+)\s*$',p.read_text())
    compile_tex(p)
    with fitz.open(p.with_suffix('.pdf')) as doc:
        assert len(doc)==len(names),(n,len(doc),names)
        for i,name in enumerate(names):
            out=root/'figures'/f'{name}.pdf'
            with fitz.open() as d:d.insert_pdf(doc,from_page=i,to_page=i);d.save(out)
            doc[i].get_pixmap(matrix=fitz.Matrix(2,2)).save(out.with_suffix('.png'))
            subprocess.run(['qpdf','--check',str(out)],capture_output=True,check=True)
    return names

def sync_documents(root,n):
    teacher=root/f'markdown/蔡题{n:03}_教师备课.md'
    s=teacher.read_text();s=re.sub(r'<!-- PAGE_COMPACT_(?:START|END) -->\s*','',s)
    m=list(re.finditer(r'(?m)^# 第\s*(\d+)\s*题\s*\n',s));assert len(m)==8,(n,len(m))
    front=s[:m[0].start()];papers=[];students=[];teachers=[]
    for i,x in enumerate(m):
        num=int(x.group(1));assert num==i+1
        b=s[x.end():m[i+1].start() if i+1<len(m) else len(s)]
        b=re.sub(r'(?m)^\s*\\newpage\s*$','',b).strip()
        assert re.findall(r'(?m)^## (.+)$',b)==HEADS,(n,num)
        q=re.search(r'<!-- question-start -->\s*(.*?)\s*<!-- question-end -->',b,re.S)
        if q:
            paper=q.group(1)
        else:
            q=re.search(r'(?s)^(.*?)\n## 一、题型定位',b)
            assert q,(n,num)
            paper=q.group(1).strip()
        student=b.split('## 六、关键洞察')[0].rstrip()
        student=re.sub(r'<!-- teacher-only-start -->.*?<!-- teacher-only-end -->\s*','',student,flags=re.S)
        teachers.append(f'# 第 {num} 题\n\n{b}')
        students.append(f'# 第 {num} 题\n\n{student}')
        papers.append(f'# 第 {num} 题\n\n{paper}')
    for label,blocks in [('教师备课',teachers),('学生详解',students),('试卷',papers)]:
        p=root/f'markdown/蔡题{n:03}_{label}.md'
        p.write_text(front+'\n\n\\newpage\n\n'.join(blocks)+'\n')
        assert p.read_text().count('\\newpage')==7

def image_sizes(s,root,label=None):
    def sub(m):
        path=m.group(2);pdf=(root/'markdown'/path).with_suffix('.pdf')
        with fitz.open(pdf) as d: w,h=d[0].rect.width,d[0].rect.height
        # Keep physical height below 88 mm while retaining fixed document typography.
        frac=min(.9,88/(166*h/w))
        # Keep the three question illustrations beside their long prompts.
        setno=root.name[-3:]
        key=(setno,Path(path).name)
        caps={('076','question-01.png'):.42,('087','question-05.png'):.43,('091','question-05.png'):.45,('090','question-07.png'):.62,('088','question-08.png'):.60}
        if key in caps:frac=min(frac,caps[key])
        if label=='试卷' and key==('070','question-04.png'):frac=min(frac,.45)
        if label=='试卷' and key==('062','question-07.png'):frac=min(frac,.82)
        old=m.group(3)
        if old:
            v=re.search(r'width=(\d+(?:\.\d+)?)%',old)
            if v:frac=min(frac,float(v.group(1))/100)
        return f'![{m.group(1)}]({path}){{width={frac*100:.1f}%}}'
    return re.sub(r'!\[([^\]]*)\]\((\.\./figures/[\w-]+\.png)\)(\{[^}]*\})?',sub,s)

def build(root,n):
    sync_documents(root,n)
    reports=[]
    for label in ['试卷','学生详解','教师备课']:
        stem=f'蔡题{n:03}_{label}';md=root/f'markdown/{stem}.md'
        text=image_sizes(md.read_text(),root,label)
        tex=root/f'build/{stem}.tex';tex.parent.mkdir(exist_ok=True)
        r=subprocess.run(['pandoc','--from=markdown+raw_tex','--to=latex','--standalone',f'--template={root/"latex/template.tex"}','--top-level-division=section'],input=text,capture_output=True,text=True,check=True)
        source=re.sub(r'\\noindent\s*\n\s*\n\s*\\begin\{minipage\}',lambda m:r'\noindent\begin{minipage}',r.stdout)
        # Keep an unnumbered derivation heading with the start of its explanation.
        source=re.sub(r'(?m)^(\\textbf\{[^\n]+\})\s*\n\n',lambda m:r'\needspace{3\baselineskip}'+'\n'+m.group(1)+'\n\n',source)
        source=source.replace(r'\Needspace{3\baselineskip}'+'\n'+r'\textbf{功率必为非负的检查}',r'\Needspace{8\baselineskip}'+'\n'+r'\textbf{功率必为非负的检查}')
        source=re.sub(r'\.\./figures/([\w-]+)\.png',lambda m:str(root/'figures'/f'{m.group(1)}.pdf'),source)
        source=source.replace(r'\begin{figure}',r'\begin{figure}[H]').replace(r'\caption{图',r'\caption*{图')
        (root/f'latex/{stem}.tex').write_text(source.replace(str(root/'figures')+'/', '../figures/'))
        tex.write_text(source);compile_tex(tex)
        log=tex.with_suffix('.log').read_text(errors='replace')
        bad=[l for l in log.splitlines() if any(k in l for k in ['Overfull','Missing character','Undefined control sequence','! '])]
        out=root/f'PDF/{stem}.pdf';out.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(tex.with_suffix('.pdf'),out)
        subprocess.run(['qpdf','--check',str(out)],capture_output=True,check=True)
        density=[];figpages=[]
        with fitz.open(out) as d:
            for i,p in enumerate(d):
                t=p.get_text();assert '\ufffd' not in t
                density.append(len(re.sub(r'\s','',t)))
                if p.get_image_info() or len(p.get_drawings())>8:figpages.append(i+1)
            pages=len(d)
        reports.append(dict(version=label,pages=pages,body_pages=pages-1,sha256=hashlib.sha256(out.read_bytes()).hexdigest(),warnings=bad,sparse_pages=[i+1 for i,v in enumerate(density) if i and v<90],figure_pages=figpages,per_page_nonspace=density))
        print(n,label,pages,'warnings',len(bad),flush=True)
    (root/'复核构建报告.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2))
    return reports

if __name__=='__main__':
    a=argparse.ArgumentParser(description='从教师Markdown和TikZ图稿重建本批试卷。')
    a.add_argument('sets',nargs='+',type=int,choices=[52,51,50,49,48])
    a.add_argument('--figures',action='store_true');a.add_argument('--documents',action='store_true')
    args=a.parse_args()
    if not (args.figures or args.documents):a.error('指定 --figures 或 --documents')
    for n in args.sets:
        root=BASE/f'蔡题{n:03}'
        if args.figures:split_figures(root,n)
        if args.documents:build(root,n)
