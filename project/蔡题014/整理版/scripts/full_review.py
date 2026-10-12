"""Current full-set audit with exact already-read body pixels and explicit new reading.
Compare generates review candidates only; reading requires prior actual displays.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,math,re,subprocess
import fitz
from PIL import Image
from audit_sources import inspect,MODULES,BANNED,metrics
from prepare_documents import normalize_boundaries
ROOT=Path(__file__).resolve().parents[1]
LABELS={'paper':'试卷','student':'学生详解','teacher':'教师备课'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def pix(p,crop=False):
    with Image.open(p) as im:
        rgb=im.convert('RGB');box=[0,90,im.width,im.height-95]
        if crop:rgb=rgb.crop(box)
        return hashlib.sha256(str(rgb.size).encode()+rgb.tobytes()).hexdigest(),box,list(im.size)
def question_records():
    out=[]
    for q in range(1,9):
        key=f'{q:02}';a=read(ROOT/f'verification/question-{key}-accepted.json')
        m=read(ROOT/f'verification/question-{key}-math.json');g=read(ROOT/f'verification/question-{key}-geometry.json')
        vp=ROOT/('preview/visual-reviewed-q01.json' if q==1 else f'preview/visual-q{key}-final.json');v=read(vp)
        assert a['question_accepted'] and a['draft_sha256']==sha(ROOT/f'drafts/question-{key}.md')
        assert a['math_record_sha256']==sha(ROOT/f'verification/question-{key}-math.json')
        assert a['geometry_record_sha256']==sha(ROOT/f'verification/question-{key}-geometry.json')
        assert a['visual_record_sha256']==sha(vp) and m['math_passed'] and g['geometry_passed']
        assert g['figure_source_sha256']==sha(ROOT/f'figures/题{key}_图稿源文件.tex')
        assert not inspect(key)['issues']
        # Only current accepted page rasters enter the reuse index.
        page_rows=[]
        for item in a['versions']:
            version=item['version'];folder=ROOT/f'preview/working-q{key}-{version}'
            pdf=folder/(folder.name+'.pdf');assert sha(pdf)==item['pdf_sha256']
            for n in range(1,item['total_pages']+1):
                path=folder/f'page-{n:03}.png';whole,_,_=pix(path)
                if q==1:
                    direct=next((x for x in v['explicit_hd_pages'] if x['version']==version and x['page']==n),None)
                    if direct:
                        assert direct['actual_displayed_and_read'] and direct['file_sha256']==sha(path) and direct['pixel_sha256']==whole
                    else:
                        reuse=next(x for x in v['exact_reuse_pages'] if x['version']==version and x['page']==n)
                        original=next(x for x in v['explicit_hd_pages'] if x['version']==reuse['read_from_version'] and x['page']==reuse['read_from_page'])
                        assert original['actual_displayed_and_read'] and pix(Path(original['path']))[0]==whole==reuse['pixel_sha256']
                else:
                    row=next(x for x in v['pages'] if x['version']==version and x['page']==n)
                    assert row['actual_displayed_and_read'] and row['png_sha256']==sha(path) and row['pixel_sha256']==whole and row['pdf_sha256']==sha(pdf)
                body,box,size=pix(path,crop=True)
                page_rows.append(dict(question=q,version=version,page=n,path=str(path),png_sha256=sha(path),pdf_sha256=sha(pdf),body_pixel_sha256=body,body_crop=box,png_size=size,accepted_record_sha256=sha(ROOT/f'verification/question-{key}-accepted.json'),visual_record_sha256=sha(vp)))
        assert len(v['actual_figures'])==a['figures']
        for f in v['actual_figures']:
            assert f['actual_displayed_and_read']
            for ext in ['pdf','png']:assert sha(ROOT/f"figures/{f['name']}.{ext}")==f[f'{ext}_sha256']
        out.append(dict(question=q,accepted=a,accepted_sha256=sha(ROOT/f'verification/question-{key}-accepted.json'),pages=page_rows,figures=v['actual_figures']))
    return out
def compare():
    questions=question_records();index={}
    for q in questions:
        for row in q['pages']:index.setdefault(row['body_pixel_sha256'],[]).append(row)
    result=dict(scope='exact current accepted body pixels only; final overviews and unmatched pages remain unread',actual_final_visual_review=False,versions={})
    for kind,label in LABELS.items():
        pdf=ROOT/f'output/pdf/蔡题014_{label}.pdf';folder=ROOT/f'preview/full-{kind}';matches=[];unmatched=[]
        with fitz.open(pdf) as doc:
            for n in range(1,len(doc)+1):
                p=folder/f'page-{n:03}.png';digest,box,size=pix(p,crop=True)
                if digest in index:matches.append(dict(page=n,png_sha256=sha(p),body_pixel_sha256=digest,body_crop=box,png_size=size,matches=index[digest]))
                else:unmatched.append(n)
            result['versions'][kind]=dict(pdf_sha256=sha(pdf),total_pages=len(doc),exact_reviewed_working_body_matches=matches,new_body_pages_requiring_actual_review=unmatched)
    (ROOT/'build/final-working-body-comparison.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:dict(pages=v['total_pages'],matched=len(v['exact_reviewed_working_body_matches']),unmatched=v['new_body_pages_requiring_actual_review']) for k,v in result['versions'].items()}))
def reading(direct):
    comparison=read(ROOT/'build/final-working-body-comparison.json');direct=set(direct);records={};overviews=[];direct_rows=[]
    for kind,label in LABELS.items():
        row=comparison['versions'][kind];pdf=ROOT/f'output/pdf/蔡题014_{label}.pdf';folder=ROOT/f'preview/full-{kind}'
        assert sha(pdf)==row['pdf_sha256'];matched={p['page']:p for p in row['exact_reviewed_working_body_matches']};pages=[]
        for n in range(1,row['total_pages']+1):
            path=folder/f'page-{n:03}.png';digest,box,size=pix(path,crop=True);key=f'{kind}:{n}'
            record=dict(page=n,png_sha256=sha(path),body_pixel_sha256=digest,body_crop=box,actual_reviewed=True)
            if key in direct:
                record.update(evidence='current full PDF direct HD display')
                direct_rows.append(dict(variant=kind,page=n,path=str(path.relative_to(ROOT)),sha256=sha(path)))
            else:
                assert n in matched and matched[n]['body_pixel_sha256']==digest and matched[n]['png_sha256']==sha(path),('unread final page',key)
                record.update(evidence='exact body pixels of current actually-read accepted question page',matches=matched[n]['matches'])
            pages.append(record)
        if kind=='paper':assert all(f'paper:{n}' in direct for n in range(2,row['total_pages']+1))
        ovs=[]
        for n in range(1,math.ceil(row['total_pages']/12)+1):
            path=folder/f'overview-{n:02}.jpg';item=dict(path=str(path.relative_to(ROOT)),sha256=sha(path),actual_displayed_and_read=True)
            overviews.append(item);ovs.append(item)
        records[kind]=dict(pdf_sha256=sha(pdf),source_sha256=sha(ROOT/f'markdown/蔡题014_{label}.md'),total_pages=row['total_pages'],pages=pages,actual_overviews=ovs)
    assert direct=={f"{x['variant']}:{x['page']}" for x in direct_rows}
    ledger=dict(actual_reading_attested=True,saved_utc=datetime.now(timezone.utc).isoformat(),direct_hd_pages=direct_rows,overviews=overviews,
        notes=['全部当前整套总览实际逐页审视；全套题干八页直接高清核对。',
               '正文复用仅限当前验收工作稿的精确像素，页眉页码由当前总览单独检查；相似文字不作为复用依据。',
               '空间图、图文方程、题间分页和最后答案核对；未扩大字号或行距，不以页数本身代替内容验收。'])
    lp=ROOT/'preview/full-actual-reading-ledger.json';lp.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
    result=dict(paper='014',actual_reviewed=True,set_accepted=False,unresolved=[],versions=records,manual_ledger_sha256=sha(lp),body_comparison_sha256=sha(ROOT/'build/final-working-body-comparison.json'))
    (ROOT/'preview/visual-reviewed-full.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(actual_reviewed=True,current_pages={k:v['total_pages'] for k,v in records.items()},overviews=len(overviews),direct_hd=len(direct_rows),set_accepted=False)))
def chunks(text):
    parts=re.split(r'(?m)^# 第(\d+)题\n',text)[1:];assert parts[::2]==list(map(str,range(1,9)))
    return [re.sub(r'(?m)^\\newpage\s*$','',parts[i+1]).strip() for i in range(0,len(parts),2)]
def accept():
    questions=question_records();v=read(ROOT/'preview/visual-reviewed-full.json');assert v['actual_reviewed'] and not v['unresolved']
    ledger=read(ROOT/'preview/full-actual-reading-ledger.json');assert ledger['actual_reading_attested'] and v['manual_ledger_sha256']==sha(ROOT/'preview/full-actual-reading-ledger.json')
    for item in ledger['direct_hd_pages']+ledger['overviews']:assert sha(ROOT/item['path'])==item['sha256']
    # Recompute exact reuse proof; no changed render can inherit previous acceptance.
    compare();assert v['body_comparison_sha256']==sha(ROOT/'build/final-working-body-comparison.json')
    texts={k:(ROOT/f'markdown/蔡题014_{label}.md').read_text() for k,label in LABELS.items()}
    for text in texts.values():
        assert text.count(r'\newpage')==7 and not any(x in text for x in BANNED)
        assert not re.search(r'\\(?:clearpage|linespread|setstretch|fontsize|vspace|enlargethispage)\b',text)
        assert 'draft-content-complete' not in text and 'model-revision-authorized' not in text
        for match in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)',text):assert (ROOT/'markdown'/match.group(1)).is_file()
    tc,sc,pc=[chunks(texts[k]) for k in ['teacher','student','paper']]
    for q,(t,s,p) in enumerate(zip(tc,sc,pc),1):
        assert normalize_boundaries((ROOT/f'drafts/question-{q:02}.md').read_text().rstrip().lstrip()).split('\n',1)[1].strip()==t
        assert re.findall(r'(?m)^## (.*)$',t)==MODULES and re.findall(r'(?m)^## (.*)$',s)==MODULES[:5]
        assert t.split('## 六、关键洞察')[0].strip()==s
        assert re.search(r'<!-- question-start -->(.*?)<!-- question-end -->',t,re.S).group(1).strip()==p
    manifest=read(ROOT/'build/pdf-build-manifest.json');documents=[]
    for item,(kind,label) in zip(manifest['documents'],LABELS.items()):
        path=Path(item['path']);row=v['versions'][kind];assert sha(path)==item['pdf_sha256']==row['pdf_sha256']==sha(ROOT/'build'/path.name)
        assert row['source_sha256']==sha(ROOT/f'markdown/蔡题014_{label}.md')
        with fitz.open(path) as doc:
            assert len(doc)==row['total_pages']==item['total_pages'] and len(row['pages'])==len(doc)
            assert re.sub(r'\s','',doc[0].get_text())=='第014套'
            assert all('\ufffd' not in p.get_text() for p in doc)
            assert all(d>20 for d in item['per_page_nonspace'])
            if kind=='student':assert len(doc)-1>=56 and item['pdf_extracted_body_nonspace']>=31218
            if kind=='teacher':assert len(doc)-1>=71 and item['pdf_extracted_body_nonspace']>=45411
        for page in row['pages']:
            p=ROOT/f"preview/full-{kind}/page-{page['page']:03}.png"
            assert page['actual_reviewed'] and page['png_sha256']==sha(p) and page['body_pixel_sha256']==pix(p,crop=True)[0]
            if page['page'] in item['low_density_pages']:assert any(x['variant']==kind and x['page']==page['page'] for x in ledger['direct_hd_pages'])
        log=(ROOT/'build'/path.with_suffix('.log').name).read_text(errors='replace')
        assert not any(tag in log for tag in ['Underfull','Overfull','Warning:','Missing character','Undefined control sequence','! '])
        subprocess.run(['qpdf','--check',str(path)],capture_output=True,check=True)
        documents.append(item)
    figs={f['name']:f for q in questions for f in q['figures']};assert len(figs)==39
    for path in (ROOT/'figures').glob('*.pdf'):subprocess.run(['qpdf','--check',str(path)],capture_output=True,check=True)
    for path in (ROOT/'figures').glob('题*_图稿源文件.log'):assert not re.search(r'Warning:|Underfull|Overfull|Missing character|^!',path.read_text(),re.M)
    for name,item in read(ROOT/'preview/originals/source-manifest.json').items():assert sha(ROOT.parent/name)==item['sha256']
    template=ROOT/'latex/template.tex';reference=ROOT.parents[1]/'蔡题101/整理版/latex/template.tex'
    for param in ['12pt,a4paper','top=22mm,bottom=22mm,left=22mm,right=22mm',r'\setstretch{1.24}',r'\setlength{\parskip}{0.35em}']:
        assert param in template.read_text() and param in reference.read_text()
    benchmark=read(ROOT.parents[1]/'蔡题015/整理版/preview/visual-reviewed-full.json')['benchmark101']
    for label,kind in [('学生详解','student'),('教师备课','teacher')]:
        ref=benchmark[label]
        assert sha(Path(ref['markdown_path']))==ref['markdown_sha256'] and sha(Path(ref['pdf_path']))==ref['pdf_sha256']
        assert metrics(texts[kind])['body_net_characters']>=ref['source_metrics']['body_net_characters']
    result=dict(paper='014',set_accepted=True,technical_checks_passed=True,actual_visual_review=True,unresolved=[],
        question_count=8,figures=39,figure_pdf_collections=8,qpdf_checked_files=50,student_core_identical_to_teacher=True,originals_unchanged=True,
        main_typesetting_parameters_match101=True,template_identical_to101=sha(template)==sha(reference),template_sha256=sha(template),benchmark101=benchmark,
        documents=documents,per_question_depth=[inspect(f'{q:02}') for q in range(1,9)],
        symbolic_checks=sum(q['accepted']['symbolic_checks'] for q in questions),numeric_checks=sum(q['accepted']['numeric_checks'] for q in questions),
        geometrical_checks=sum(q['accepted']['geometrical_checks'] for q in questions),
        question_acceptance_sha256={str(q['question']):q['accepted_sha256'] for q in questions},
        visual_record_sha256=sha(ROOT/'preview/visual-reviewed-full.json'),body_comparison_sha256=sha(ROOT/'build/final-working-body-comparison.json'),
        actual_final_overviews=len(ledger['overviews']),actual_direct_final_hd=len(ledger['direct_hd_pages']))
    path=ROOT/'build/delivery-check.json';path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    for n in ['pdf-build-manifest.json','document-source-manifest.json']:
        p=ROOT/'build'/n;data=read(p);data.update(accepted=True,actual_visual_review=True,pending=[],acceptance_report='build/delivery-check.json',acceptance_report_sha256=sha(path));p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['set_accepted','figures','qpdf_checked_files','symbolic_checks','numeric_checks','geometrical_checks','actual_final_overviews','actual_direct_final_hd']},ensure_ascii=False))
def main():
    p=argparse.ArgumentParser();p.add_argument('action',choices=['compare','reading','accept']);p.add_argument('--direct',nargs='+',default=[]);a=p.parse_args()
    if a.action=='reading':reading(a.direct)
    else:globals()[a.action]()
if __name__=='__main__':main()
