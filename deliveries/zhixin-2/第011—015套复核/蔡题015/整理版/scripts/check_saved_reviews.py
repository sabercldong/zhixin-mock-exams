"""Check saved current review hashes. Never create or infer visual-reading claims."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import subprocess

import fitz

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("questions", nargs="*")
    args = parser.parse_args()
    records = [ROOT / f"preview/visual-reviewed-q{q}.json" for q in args.questions] if args.questions else sorted((ROOT / "preview").glob("visual-reviewed-q*.json"))
    assert records, "No saved actual-reading record"
    rows = []
    for record in records:
        data = json.loads(record.read_text())
        q = f"{data['question']:02d}"
        assert data["actual_visual_reviewed"] and not data["set_accepted"]
        assert not data["remaining_visual_issues"]
        for rel, digest in data["bound_sha256"].items():
            assert sha(ROOT / rel) == digest, rel
        quality = json.loads((ROOT / f"build/source-quality-q{q}.json").read_text())
        assert quality["passed"]
        assert quality["questions"][0]["sha256"] == data["source_sha256"]
        verification = json.loads((ROOT / f"build/question-{q}-verification.json").read_text())
        assert verification["verified_math"] and not verification["set_accepted"]
        assert verification["model_condition_resolved"] == data["model_condition_resolved"]
        for item in verification["bound_files"].values():
            assert sha(Path(item["path"])) == item["sha256"], item["path"]
        if not data["model_condition_resolved"]:
            assert not data["question_accepted"] and data["remaining_model_issues"]
        assert verification["figures"] == data["figures_reviewed"]
        for name, item in data["figures_reviewed"].items():
            for ext in ["pdf", "png"]:
                assert sha(ROOT / f"figures/{name}.{ext}") == item[f"{ext}_sha256"], name
        for rel, digest in data["original_images_actually_reviewed"].items():
            assert sha(ROOT / rel) == digest, rel
        pages = 0
        for version, item in data["pdfs"].items():
            folder = ROOT / f"preview/working-q{q}-{version}"
            pdf = folder / (folder.name + ".pdf")
            assert sha(pdf) == item["pdf_sha256"]
            with fitz.open(pdf) as document:
                n = len(document)
                assert n == item["total_pages"] == item["body_pages"] + 1
                assert item["overview_pages_reviewed"] == list(range(1, n + 1))
                assert item["high_resolution_pages_reviewed"] == list(range(1, n + 1))
                assert set(item["page_png_sha256"]) == {f"page-{p:03d}.png" for p in range(1, n + 1)}
                assert set(item["overview_sha256"]) == {f"overview-{p:02d}.jpg" for p in range(1, (n + 11) // 12 + 1)}
                assert all(len(re.sub(r"\s", "", page.get_text())) > 100 for page in list(document)[1:])
            for key in ["page_png_sha256", "overview_sha256"]:
                for name, digest in item[key].items():
                    assert sha(folder / name) == digest, name
            log = pdf.with_suffix(".log").read_text()
            assert not re.search(r"Warning|Underfull|Overfull|Missing character|^!", log, re.MULTILINE)
            pages += n
        for pair in data["identical_page_reuse"]:
            student = ROOT / f"preview/working-q{q}-student/page-{pair['student_page']:03d}.png"
            teacher = ROOT / f"preview/working-q{q}-teacher/page-{pair['teacher_page']:03d}.png"
            assert sha(student) == sha(teacher) == pair["png_sha256"]
        for item in data["qpdf_checks"]:
            pdf = ROOT / item["path"]
            assert sha(pdf) == item["sha256"]
            subprocess.run(["qpdf", "--check", str(pdf)], capture_output=True, check=True)
        rows.append(dict(question=int(q), current_files_consistent=True,
                         model_condition_resolved=data["model_condition_resolved"],
                         question_accepted=data["question_accepted"],
                         actual_review_record_sha256=sha(record),
                         working_pdf_pages=pages, figures=len(data["figures_reviewed"])))
    report = dict(scope="015 saved conditional/accepted question preview consistency only; not whole-set acceptance",
                  passed=True, set_accepted=False, questions=rows)
    (ROOT / "build/review-consistency.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()

