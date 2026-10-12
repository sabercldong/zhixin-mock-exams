"""编译当前题的矢量图并保留逐图PDF/PNG；实际审图另行记录。"""
from pathlib import Path
import argparse
import subprocess
import fitz

ROOT = Path(__file__).resolve().parents[1]
import os
_candidates=sorted((Path.home()/'.codex/plugins/cache/openai-bundled/latex').glob('*/scripts/compile_latex.py'))
COMPILER=Path(os.environ['CODEX_LATEX_COMPILER']) if os.environ.get('CODEX_LATEX_COMPILER') else _candidates[-1]
assert COMPILER.is_file()
NAMES = {
    '01': ['question-01', 'geometry-01', 'families-01', 'frequency-01'],
    '02': ['question-02', 'dipoles-02', 'forces-02', 'barrier-02'],
    '03': ['question-03', 'forces-03', 'equilibria-03', 'farfield-03', 'perturbation-03', 'nearstar-03'],
    '04': ['question-04', 'kinematics-04', 'forces-04', 'effective-04'],
    '05': ['question-05', 'section-05', 'decomposition-05', 'fluxlink-05', 'circuit-05'],
    '06': ['geometry-06', 'energyflow-06', 'compression-06', 'energycurve-06'],
    '07': ['question-07', 'curvature-07', 'imaging-07', 'focalrayA-07', 'focalrayB-07', 'intersection-07'],
    '08': ['decay-08', 'boost-08', 'momentum-08', 'section-08', 'anglecases-08'],
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('questions', nargs='*')
    args = parser.parse_args()
    for q in args.questions or NAMES:
        source = ROOT/'figures'/f'题{q}_图稿源文件.tex'
        result = subprocess.run(['python3', str(COMPILER), str(source), '--compiler', 'texlive', '--engine', 'xelatex'], cwd=source.parent, capture_output=True, text=True)
        assert result.returncode == 0, (source, result.stdout, result.stderr)
        bad = [s for s in source.with_suffix('.log').read_text(errors='replace').splitlines() if any(w in s for w in ['Missing character', 'Overfull', 'Undefined control sequence'])]
        assert not bad, (q, bad)
        with fitz.open(source.with_suffix('.pdf')) as doc:
            assert len(doc) == len(NAMES[q]), (q, len(doc), NAMES[q])
            for i, name in enumerate(NAMES[q]):
                dest = source.parent/f'{name}.pdf'
                with fitz.open() as single:
                    single.insert_pdf(doc, from_page=i, to_page=i)
                    single.save(dest)
                doc[i].get_pixmap(matrix=fitz.Matrix(2.5, 2.5), alpha=False).save(dest.with_suffix('.png'))
                subprocess.run(['qpdf', '--check', str(dest)], check=True, capture_output=True)
        print(q, ','.join(NAMES[q]), flush=True)

if __name__ == '__main__':
    main()
