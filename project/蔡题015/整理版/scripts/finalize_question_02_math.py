"""Refresh Q2 independent mathematical evidence; never infer visual acceptance."""
from pathlib import Path
import hashlib,json
import verify_question_02 as physics
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    physics.main()
    pre=json.loads((ROOT/'build/question-02-preverification.json').read_text())
    geo=json.loads((ROOT/'build/question-02-figure-geometry.json').read_text())
    quality=json.loads((ROOT/'build/source-quality-q02.json').read_text())
    assert pre['verified_math'] and geo['passed'] and quality['passed']
    paths={'manuscript':ROOT/'drafts/question-02.md','figure_source':ROOT/'figures/题02_图稿源文件.tex',
           'geometry':ROOT/'build/question-02-figure-geometry.json','geometry_data':ROOT/'build/question-02-figure-data.json',
           'quality':ROOT/'build/source-quality-q02.json','math_script':ROOT/'scripts/verify_question_02.py',
           'finalizer':Path(__file__),'geometry_script':ROOT/'scripts/check_figures_02.py',
           'figure_generator':ROOT/'scripts/draw_figures_02.py',
           'original_paper':ROOT.parent/'试卷.pdf','original_answers':ROOT.parent/'答案.pdf',
           'source_detail_manifest':ROOT/'preview/originals/question-02-detail-manifest.json'}
    for name in geo['figures']:
        for ext in ['pdf','png']:paths[name+'_'+ext]=ROOT/f'figures/{name}.{ext}'
    report=dict(pre)
    report.update(scope='Complete Q2 mathematical/source verification; actual PDF/visual acceptance recorded separately',
                  document_complete=True,model_condition_resolved=True,
                  model_scope='All 4 parts use stated ideal thin currents and nonmagnetic media. Sphere leads are radial semi-infinite rays in the handwritten geometry; arbitrary extra nonradial leads are explicitly excluded, current-sheet one-sided limits distinguished.',
                  question_accepted=False,set_accepted=False,figures_rendered=True,
                  figures=geo['figures'],
                  bound_files={k:dict(path=str(p),sha256=sha(p)) for k,p in paths.items()})
    (ROOT/'build/question-02-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(verified_math=True,document_complete=True,model_condition_resolved=True,question_accepted=False,figures=len(geo['figures'])),ensure_ascii=False))
if __name__=='__main__':main()

