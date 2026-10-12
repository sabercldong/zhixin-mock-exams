"""Bind explicit manual reading events to source/image hashes. No inferred review."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
# All entries below were explicitly displayed and read in the current main turn.
full=[f'paper-{p:02}.png' for p in range(1,4)]+[f'answer-{p:02}.png' for p in range(1,9)]
details=['q01-paper.png','q01-answer.png','q02-paper.png','q04-paper.png','q04-answer.png','q07-paper.png','q07-answer.png']
entries=[]
for relative in full+[f'details/{name}' for name in details]:
    path=ROOT/'preview/originals'/relative
    entries.append(dict(path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),actual_displayed_and_read=True))
report=dict(paper='014',read_date='2026-10-10',manual_scope='全部11张整页以及7张重点局部；不是成品审读',
            original_manifest=json.loads((ROOT/'preview/originals/source-manifest.json').read_text()),
            entries=entries,formal_pdf_reviewed=False,set_accepted=False)
(ROOT/'preview/originals/actual-reading-ledger.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Explicit source reading entries:',len(entries))
