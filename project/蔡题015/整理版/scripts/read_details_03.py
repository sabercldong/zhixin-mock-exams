"""Render only question 03 source crops; originals remain untouched."""
from pathlib import Path
import hashlib, json
import fitz

ROOT = Path(__file__).resolve().parents[1]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    dest = ROOT / "preview/originals"
    dest.mkdir(parents=True, exist_ok=True)
    requests = [
        ("试卷.pdf", 0, (.115, .632, .945, .930), "q03-paper-detail"),
        ("答案.pdf", 2, (.020, .045, .503, .958), "q03-answer-left-detail"),
        ("答案.pdf", 2, (.505, .025, .985, .620), "q03-answer-right-detail"),
    ]
    report = {"actual_reviewed": False, "sources": {}, "crops": {}}
    for name, number, box, label in requests:
        source = ROOT.parent / name
        report["sources"][name] = sha(source)
        with fitz.open(source) as doc:
            page = doc[number]
            w, h = page.rect.width, page.rect.height
            clip = fitz.Rect(box[0]*w, box[1]*h, box[2]*w, box[3]*h)
            path = dest / (label + ".png")
            page.get_pixmap(matrix=fitz.Matrix(4, 4), clip=clip, alpha=False).save(path)
            report["crops"][label] = {
                "source": name, "page": number+1, "relative_clip": box,
                "sha256": sha(path),
            }
    (dest / "question-03-detail-manifest.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    )
    print(json.dumps(report, ensure_ascii=False))

if __name__ == "__main__":
    main()

