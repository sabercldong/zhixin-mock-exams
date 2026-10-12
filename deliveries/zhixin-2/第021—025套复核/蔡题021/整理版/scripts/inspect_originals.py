"""原件中的细小网络图追加高清裁切；所有原件只读。"""
from pathlib import Path
import fitz
ROOT=Path(__file__).resolve().parents[1]
with fitz.open(ROOT.parent/'试卷.pdf') as doc:
    page=doc[0];w=page.rect.width;h=page.rect.height
    print(w,h)
    page.get_pixmap(matrix=fitz.Matrix(6,6),clip=fitz.Rect(w*.54,h*.46,w*.86,h*.57),alpha=False).save(ROOT/'preview/originals/tetra-detail.png')
