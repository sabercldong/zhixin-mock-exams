"""核验既有实际审读证据绑定的文件，不能替代实际看图或生成虚假审读记录。"""
from pathlib import Path
import hashlib,json,subprocess
import fitz
ROOT=Path(__file__).resolve().parents[1]
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    reports=[]
    for q in ['01','02','03','04','05','06','07','08']:
        record=ROOT/f'preview/visual-reviewed-q{q}.json'
        data=json.loads(record.read_text())
        assert data['actual_visual_reviewed'] and not data['set_accepted']
        for version,item in data['pdfs'].items():
            folder=ROOT/f'preview/working-q{q}-{version}'
            pdf=folder/f'working-q{q}-{version}.pdf'
            assert sha(pdf)==item['pdf_sha256'],pdf
            for filename,digest in item.get('page_png_sha256',{}).items():
                assert sha(folder/filename)==digest,folder/filename
            with fitz.open(pdf) as doc:
                assert len(doc)==item['total_pages']==item['body_pages']+1
                assert item['overview_pages_reviewed']==list(range(1,len(doc)+1))
            log=pdf.with_suffix('.log').read_text(errors='replace')
            assert not any(x in log for x in ['Overfull','Missing character','Undefined control sequence','! '])
            subprocess.run(['qpdf','--check',str(pdf)],capture_output=True,check=True)
        for name,digest in data['figures_reviewed'].items():
            path=ROOT/f'figures/{name}.pdf'
            assert sha(path)==digest,path
            subprocess.run(['qpdf','--check',str(path)],capture_output=True,check=True)
        if 'source_sha256' in data:
            assert sha(ROOT/f'drafts/question-{q}.md')==data['source_sha256']
        if q in ['05','06','07','08']:
            verification=json.loads((ROOT/f'build/verification-q{q}.json').read_text())
            assert verification['verified_math'] and verification['document_complete']
            for rel,digest in verification['source_sha256'].items():
                assert sha(ROOT/rel)==digest,rel
            assert verification['figures_sha256']==data['figures_reviewed']
            if 'verification_sha256' in data:
                assert sha(ROOT/f'build/verification-q{q}.json')==data['verification_sha256']
        reports.append(dict(question=int(q),review_record_sha256=sha(record),
                            bound_current_files=True,pdfs_checked=2,figures_checked=len(data['figures_reviewed'])))
    assert sha(ROOT/'latex/template.tex')=='434e4734708ef9c12c4be4629709e370fa5fe9a67a4cc88709ee13ffa571673b'
    assert sha(ROOT.parent/'试卷.pdf')=='1f37604d37c061d72ee99c5af8247df5d8552f3dc82bf63d269206755d1c8cdf'
    assert sha(ROOT.parent/'答案.pdf')=='809e74d95fd68880c1d5ed1a20fb1771619c6e049a102ac88067a561f3cb227d'
    result=dict(scope='018已实际审读分题1—8的当前文件一致性；题7球形条件已获用户确认，不代表整套验收',passed=True,questions=reports)
    (ROOT/'build/review-consistency.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':main()
