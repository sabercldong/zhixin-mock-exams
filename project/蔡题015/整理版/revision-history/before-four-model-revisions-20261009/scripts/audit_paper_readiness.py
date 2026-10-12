"""Read-only cross-question readiness audit. No build or acceptance inference.

Reuse current per-question source/review rules without calling any writer.
Write only a new aggregate technical report. Missing model authorization always
closes the formal-delivery gate; page totals from separate question previews
are never represented as whole-paper pages.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import subprocess
from datetime import datetime, timezone

import fitz

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[1]
SPEC = importlib.util.spec_from_file_location("audit015_readonly", ROOT / "scripts/audit_sources.py")
RULES = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RULES)
EXPECTED_MODULES = RULES.MODULES
EXPECTED_PARTS = {1: 3, 2: 4, 3: 3, 4: 3, 5: 1, 6: 1, 7: 2, 8: 2}
YAML = '---\ntitle: "第015套"\nshorttitle: "第015套"\nauthor: "物理竞赛资料"\n---\n'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read_json(path):
    return json.loads(path.read_text())

def bind(report, path):
    report["bound_sha256"][str(path.relative_to(ROOT))] = digest(path)

def main():
    report = {
        "paper": "015",
        "saved_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "Cross-question technical readiness only; no new physical or visual acceptance",
        "set_accepted": False,
        "actual_whole_pdf_reviewed": False,
        "formal_delivery_allowed": False,
        "whole_pdf_built": False,
        "bound_sha256": {},
        "questions": [],
        "source_integrity_issues": [],
        "unresolved_models": [],
        "all_current_source_and_evidence_consistent": False,
    }
    student_sources, teacher_sources, stem_sources, figure_tags = [], [], [], []
    page_sums = {"student": 0, "teacher": 0}
    body_sums = {"student": 0, "teacher": 0}
    for number in range(1, 9):
        q = f"{number:02d}"
        source_path = ROOT / f"drafts/question-{q}.md"
        source = source_path.read_text()
        inspect = RULES.inspect(q)
        assert not inspect["issues"], (q, inspect["issues"])
        assert source.startswith(f"# 第{number}题\n")
        assert "<!-- question-complete -->" in source
        assert re.findall(r"(?m)^## (.*)$", source) == EXPECTED_MODULES
        student = source.split("## 六、关键洞察")[0].rstrip() + "\n"
        assert re.findall(r"(?m)^## (.*)$", student) == EXPECTED_MODULES[:5]
        assert not re.search(r"课堂|教师|板书|让学生", student)
        stem = source.split("<!-- question-start -->")[1].split("<!-- question-end -->")[0].strip()
        assert not re.search(r"(?m)^#{1,6} ", stem)
        parts = re.findall(r"(?m)^（([1-9])）", stem)
        assert len(parts) == EXPECTED_PARTS[number] if EXPECTED_PARTS[number] > 1 else not parts
        assert parts == [str(k) for k in range(1, EXPECTED_PARTS[number] + 1)] if parts else True
        for match in re.finditer(r"!\[图(\d+-\d+) [^]]*\]\((\.\./figures/[^)]+)\)", source):
            tag, relative = match.groups()
            assert int(tag.split("-")[0]) == number
            assert tag not in figure_tags, tag
            figure_tags.append(tag)
            bind(report, (source_path.parent / relative).resolve())
            bind(report, (source_path.parent / relative).resolve().with_suffix(".pdf"))
        visual_path = ROOT / f"preview/visual-reviewed-q{q}.json"
        visual = read_json(visual_path)
        assert visual["question"] == number and visual["actual_visual_reviewed"]
        assert not visual["set_accepted"] and not visual["remaining_visual_issues"]
        assert visual["source_sha256"] == digest(source_path) == inspect["sha256"]
        assert len(visual["figures_reviewed"]) == inspect["figures"]
        for relative, sha in visual["bound_sha256"].items():
            assert digest(ROOT / relative) == sha, (q, relative)
        for relative, sha in visual["original_images_actually_reviewed"].items():
            assert digest(ROOT / relative) == sha, (q, relative)
        verification = read_json(ROOT / f"build/question-{q}-verification.json")
        assert verification["verified_math"] and not verification["set_accepted"]
        assert verification["model_condition_resolved"] == visual["model_condition_resolved"]
        for item in verification["bound_files"].values():
            assert digest(Path(item["path"])) == item["sha256"], (q, item["path"])
        assert verification["figures"] == visual["figures_reviewed"]
        for name, item in visual["figures_reviewed"].items():
            for ext in ["png", "pdf"]:
                assert digest(ROOT / f"figures/{name}.{ext}") == item[f"{ext}_sha256"]
        for item in visual["qpdf_checks"]:
            pdf = ROOT / item["path"]
            assert digest(pdf) == item["sha256"]
            subprocess.run(["qpdf", "--check", str(pdf)], capture_output=True, check=True)
        for path in [source_path, visual_path, ROOT / f"build/source-quality-q{q}.json",
                     ROOT / f"build/question-{q}-verification.json",
                     ROOT / f"build/question-{q}-figure-geometry.json",
                     ROOT / f"build/question-{q}-work-check.json"]:
            bind(report, path)
        for version, expected in [("student", student), ("teacher", source)]:
            folder = ROOT / f"preview/working-q{q}-{version}"
            md = folder / f"{folder.name}.md"
            assert md.read_text() == YAML + expected, (q, version, "extraction mismatch")
            expected_heads = EXPECTED_MODULES[:5] if version == "student" else EXPECTED_MODULES
            assert re.findall(r"(?m)^## (.*)$", md.read_text()) == expected_heads
            pdf = folder / f"{folder.name}.pdf"
            item = visual["pdfs"][version]
            assert digest(pdf) == item["pdf_sha256"]
            with fitz.open(pdf) as document:
                assert len(document) == item["total_pages"] == item["body_pages"] + 1
                assert item["high_resolution_pages_reviewed"] == list(range(1, len(document) + 1))
                assert item["overview_pages_reviewed"] == list(range(1, len(document) + 1))
                assert all(len(re.sub(r"\s", "", page.get_text())) > 100 for page in list(document)[1:])
            for key in ["page_png_sha256", "overview_sha256"]:
                for image_name, sha in item[key].items():
                    assert digest(folder / image_name) == sha, (q, version, image_name)
            log = pdf.with_suffix(".log").read_text()
            assert not re.search(r"Warning|Underfull|Overfull|Missing character|^!", log, re.MULTILINE)
            page_sums[version] += item["total_pages"]
            body_sums[version] += item["body_pages"]
        if not visual["model_condition_resolved"]:
            assert not visual["question_accepted"] and visual["remaining_model_issues"]
            model_path = ROOT / f"build/question-{q}-模型审查.json"
            model = read_json(model_path)
            assert not model["model_condition_resolved"]
            assert not model.get("human_answer") and not model.get("human_choice_reply")
            assert not model.get("user_reply_received") and not model.get("reply_received")
            bind(report, model_path)
            report["unresolved_models"].append({
                "question": number, "record": str(model_path.relative_to(ROOT)),
                "sha256": digest(model_path), "issues": visual["remaining_model_issues"],
                "must_not_reuse_prior_authorization": True,
            })
        else:
            assert visual["question_accepted"]
        report["questions"].append({
            **inspect, "stem_subquestion_count": EXPECTED_PARTS[number],
            "stem_figure_count": len(re.findall(r"!\[", stem)),
            "student_exactly_first_five_modules": True,
            "teacher_exactly_all_nine_modules": True,
            "current_saved_review_consistent": True,
            "question_accepted": visual["question_accepted"],
            "model_condition_resolved": visual["model_condition_resolved"],
            "working_pages": {v: visual["pdfs"][v]["total_pages"] for v in ["student", "teacher"]},
            "working_body_pages": {v: visual["pdfs"][v]["body_pages"] for v in ["student", "teacher"]},
        })
        student_sources.append(student)
        teacher_sources.append(source)
        stem_sources.append(f"# 第{number}题\n\n" + stem + "\n")
    assert [x["question"] for x in report["questions"]] == list(range(1, 9))
    assert len(figure_tags) == 49
    for label, sources in [("student", student_sources), ("teacher", teacher_sources), ("paper", stem_sources)]:
        assembled = "\n\n\\newpage\n\n".join(sources)
        assert len(re.findall(r"(?m)^# 第\d+题$", assembled)) == 8
        assert assembled.count("\\newpage") == 7
        assert not re.search(r"\\newpage\s*\\newpage", assembled)
        if label == "paper":
            assert not re.search(r"题型定位|知识点|物理图像|解题入口|解析|关键洞察|易错点|课堂讲解建议|变式训练", assembled)
    report["cross_question"] = {
        "questions": 8, "stem_subquestions": sum(EXPECTED_PARTS.values()),
        "unique_figure_tags": 49, "unique_figures": figure_tags,
        "paper_source_extracted_only_from_bound_stem_markers": True,
        "planned_between_question_pagebreaks": 7,
        "planned_versions_structurally_consistent": True,
        "summed_separate_working_total_pages": page_sums,
        "summed_separate_working_body_pages": body_sums,
        "page_sum_is_not_a_whole_paper_page_count": True,
        "summed_question_source_metrics": {
            version: {key: sum(row[version][key] for row in report["questions"])
                      for key in ["raw_with_whitespace", "raw_nonspace", "body_net_characters"]}
            for version in ["student", "teacher"]
        },
    }
    reference = PROJECT / "蔡题101/整理版"
    report["reference101"] = {
        "metrics_note": "Same source algorithm; source counts are not PDF page/text counts, and source/PDF byte sync is not inferred.",
        "minimum_whole_body_pages_required": {"student": 56, "teacher": 71},
        "files": {},
    }
    for version, name in [("student", "学生详解"), ("teacher", "教师备课")]:
        md = reference / f"markdown/蔡题101_{name}.md"
        pdf = reference / f"output/pdf/蔡题101_{name}.pdf"
        subprocess.run(["qpdf", "--check", str(pdf)], capture_output=True, check=True)
        with fitz.open(pdf) as document:
            n = len(document)
        report["reference101"]["files"][version] = {
            "markdown": str(md), "markdown_sha256": digest(md),
            "source_metrics": RULES.metrics(md.read_text()),
            "latest_formal_pdf": str(pdf), "pdf_sha256": digest(pdf),
            "pdf_total_pages": n,
        }
    report["original_sha256"] = {
        "paper": digest(ROOT.parent / "试卷.pdf"),
        "answers": digest(ROOT.parent / "答案.pdf"),
    }
    assert report["original_sha256"] == {
        "paper": "e74012ea35ebe38b9367a88ac99f9aa1f45483b4d2d44ebe5e36ed4315b6ec70",
        "answers": "1fb790700698c4b474fa8d5e50a0a10e178e42ec98378c3572cab1d4e0cca35d",
    }
    bind(report, ROOT / "scripts/audit_paper_readiness.py")
    bind(report, ROOT / "scripts/audit_sources.py")
    bind(report, ROOT / "latex/template.tex")
    report["all_current_source_and_evidence_consistent"] = True
    report["gate_status"] = ("WAIT_FOR_EXISTING_SEPARATE_MODEL_CHOICES" if report["unresolved_models"]
                             else "READY_FOR_WHOLE_BUILD_AND_ACTUAL_REVIEW")
    report["next_after_choices"] = [
        "Apply only the specifically authorized question model revisions and mark them as revisions.",
        "Reverify changed calculations/figures and rebuild only affected working previews, then actually reread changed pages.",
        "Assemble three whole versions, check current whole-PDF pagination and all actual pages, and bind the new evidence.",
        "Only then decide whole-set acceptance; do not substitute separate working-page sums or structural gates.",
    ]
    report["no_new_acceptance_claim"] = True
    target = ROOT / "build/paper-readiness.json"
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({key: report[key] for key in [
        "scope", "set_accepted", "formal_delivery_allowed", "gate_status",
        "all_current_source_and_evidence_consistent", "cross_question", "unresolved_models",
    ]}, ensure_ascii=False))

if __name__ == "__main__":
    main()
