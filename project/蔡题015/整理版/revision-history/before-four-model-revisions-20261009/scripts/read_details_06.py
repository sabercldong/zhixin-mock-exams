"""Render Q6 source details; rendering does not imply actual reading."""
from pathlib import Path
import hashlib
import json

import fitz

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    dest = ROOT / "preview/originals"
    requests = [
        ("试卷.pdf", 1, (.145, .764, .950, .901), "q06-paper-text"),
        ("答案.pdf", 4, (.505, .070, .965, .195), "q06-answer-text"),
        ("答案.pdf", 4, (.515, .183, .968, .350), "q06-answer-energy"),
        ("答案.pdf", 4, (.520, .323, .970, .484), "q06-answer-result"),
    ]
    report = {"actual_reviewed": False, "sources": {}, "crops": {}}
    for name, index, box, label in requests:
        source = ROOT.parent / name
        report["sources"][name] = sha(source)
        with fitz.open(source) as document:
            page = document[index]
            width, height = page.rect.width, page.rect.height
            clip = fitz.Rect(box[0] * width, box[1] * height,
                             box[2] * width, box[3] * height)
            path = dest / (label + ".png")
            page.get_pixmap(matrix=fitz.Matrix(5, 5), clip=clip, alpha=False).save(path)
            report["crops"][label] = {
                "source": name, "page": index + 1, "relative_clip": box,
                "sha256": sha(path),
            }
    (dest / "question-06-detail-manifest.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    )
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
