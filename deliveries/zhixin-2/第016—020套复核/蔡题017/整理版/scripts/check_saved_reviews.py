"""Check saved actual-review hashes; this never creates visual-review claims."""
from pathlib import Path
import argparse,hashlib,json,re,subprocess
import fitz
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    parser=argparse.ArgumentParser();parser.add_argument('questions',nargs='*');args=parser.parse_args()
    records=[ROOT/f'preview/visual-reviewed-q{q}.json' for q in args.questions] if args.questions else sorted((ROOT/'preview').glob('visual-reviewed-q*.json'))
    assert records,'No actual review record'
    rows=[]
    for record in records:
        data=json.loads(record.read_text());q=f"{data['question']:02d}"
        assert data['actual_visual_reviewed'] and data['set_accepted'] is False
        assert not data['remaining_visual_issues']
        assert sha(ROOT/f'drafts/question-{q}.md')==data['source_sha256']
        quality_path=ROOT/f'build/source-quality-q{q}.json'
        assert sha(quality_path)==data['source_quality_sha256'],quality_path
        assert json.loads(quality_path.read_text())['passed']
        for version,item in data['pdfs'].items():
            folder=ROOT/f'preview/working-q{q}-{version}';pdf=folder/(folder.name+'.pdf')
            assert sha(pdf)==item['pdf_sha256'],pdf
            with fitz.open(pdf) as doc:
                assert len(doc)==item['total_pages']==item['body_pages']+1
                assert item['overview_pages_reviewed']==list(range(1,len(doc)+1))
                assert set(item['overview_sha256'])=={
                    f'overview-{i:02d}.jpg' for i in range(1,(len(doc)+11)//12+1)},'Stale overview cannot count as current PDF review'
                assert set(item['page_png_sha256'])=={f'page-{i:03d}.png' for i in range(1,len(doc)+1)}
                assert all(len(re.sub(r'\s','',p.get_text()))>20 for p in list(doc)[1:])
            for key in ['page_png_sha256','overview_sha256']:
                for filename,digest in item[key].items():assert sha(folder/filename)==digest,filename
            log=pdf.with_suffix('.log').read_text(errors='replace')
            assert not any(x in log for x in ['Overfull','Missing character','Undefined control sequence','! '])
            subprocess.run(['qpdf','--check',str(pdf)],capture_output=True,check=True)
        for name,digest in data['figures_reviewed'].items():
            path=ROOT/f'figures/{name}.pdf';assert sha(path)==digest
            subprocess.run(['qpdf','--check',str(path)],capture_output=True,check=True)
        verification_path=ROOT/f'build/verification-q{q}.json'
        assert sha(verification_path)==data['verification_sha256']
        verification=json.loads(verification_path.read_text())
        assert verification['verified_math'] and verification['document_complete'] and not verification['set_accepted']
        for rel,digest in verification['source_sha256'].items():assert sha(ROOT/rel)==digest,rel
        assert verification['figures_sha256']==data['figures_reviewed']
        for name,digest in verification['originals_sha256'].items():assert sha(ROOT.parent/name)==digest,name
        assert sha(ROOT/'latex/template.tex')==data['template_sha256']=='434e4734708ef9c12c4be4629709e370fa5fe9a67a4cc88709ee13ffa571673b'
        rows.append(dict(question=int(q),current_files_consistent=True,
                         actual_review_record_sha256=sha(record),
                         working_pdf_pages=sum(i['total_pages'] for i in data['pdfs'].values()),
                         figures=len(data['figures_reviewed'])))
    quality=json.loads((ROOT/'build/source-quality.json').read_text());assert quality['passed']
    result=dict(scope='017 saved question previews only, not whole-set acceptance',passed=True,set_accepted=False,questions=rows)
    (ROOT/'build/review-consistency.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))
if __name__=='__main__':main()
