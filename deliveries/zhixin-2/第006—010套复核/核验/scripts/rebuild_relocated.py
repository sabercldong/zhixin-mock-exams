"""将交付包整套复制到新目录，实际重建全部图和三版，并比较页面文本与像素。"""
from pathlib import Path
import hashlib, json, re, shutil, subprocess, sys
import fitz

import tempfile
WORK=Path(__file__).resolve().parent
OUT=WORK.parents[1]
SRC=OUT/'蔡题010'
TEST=Path(tempfile.mkdtemp(prefix='caiti010-rebuild-'))/'蔡题010'
assert SRC.is_dir() and not TEST.exists(),TEST
shutil.copytree(SRC,TEST)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
original={str(p.relative_to(TEST)):sha(p) for folder,ext in [('drafts','*.md'),('figures','*.tex')] for p in (TEST/folder).glob(ext)}
logdir=OUT/'核验/迁移重建日志';logdir.mkdir(parents=True,exist_ok=True)
for p in (TEST/'figures').iterdir():
    if p.suffix!='.tex':p.unlink()
shutil.rmtree(TEST/'build');(TEST/'build').mkdir()
shutil.rmtree(TEST/'output');(TEST/'output/pdf').mkdir(parents=True)
stages=[]
for script in ['write_drafts','make_figures','render_figures','build_documents']:
    proc=subprocess.run([sys.executable,str(TEST/f'scripts/{script}.py')],cwd=TEST,capture_output=True,text=True)
    (logdir/f'{script}.txt').write_text(proc.stdout+proc.stderr)
    assert proc.returncode==0,(script,proc.stdout[-4000:],proc.stderr[-4000:])
    stages.append(dict(script=script,exit_code=proc.returncode));print('完成迁移重建',script,flush=True)
assert all(sha(TEST/k)==v for k,v in original.items())
documents=[]
for p in sorted((SRC/'output/pdf').glob('*.pdf')):
    other=TEST/'output/pdf'/p.name
    with fitz.open(p) as d,fitz.open(other) as t:
        assert len(d)==len(t)
        for i,(a,b) in enumerate(zip(d,t),1):
            assert a.get_text()==b.get_text(),(p.name,i,'text')
            ap=a.get_pixmap(matrix=fitz.Matrix(1,1),alpha=False)
            bp=b.get_pixmap(matrix=fitz.Matrix(1,1),alpha=False)
            assert (ap.width,ap.height,ap.samples)==(bp.width,bp.height,bp.samples),(p.name,i,'pixels')
        documents.append(dict(file=p.name,pages=len(d),text_equal=True,all_pages_raster_equal=True,raster_dpi=72,delivered_sha256=sha(p),rebuilt_sha256=sha(other)))
    print('三版页面一致',p.name,flush=True)
figures=[]
for p in sorted((SRC/'figures').glob('*.png')):
    other=TEST/'figures'/p.name;assert sha(p)==sha(other),p.name
    with fitz.open(p.with_suffix('.pdf')) as d,fitz.open(other.with_suffix('.pdf')) as t:
        assert d[0].get_text()==t[0].get_text()
        assert d[0].get_pixmap().samples==t[0].get_pixmap().samples
    figures.append(dict(file=p.name,png_identical=True,vector_pdf_text_and_raster_equal=True))
assert len(figures)==40 and sum(x['pages'] for x in documents)==141
result=dict(all_passed=True,set='010',method='迁移到新目录，删除全部图像和编译产物，由定稿源文件重建40幅图及三版PDF',source_generators_equal=True,stages=stages,documents=documents,figures=figures,document_pages=141,figure_count=40)
(WORK/'relocation_rebuild_report.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(OUT/'核验/迁移重建报告.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print('PASS 40幅图、3份PDF、141页文本与像素一致',flush=True)
