import json

from portfolio import report_generator


def test_generate_completion_report_has_required_fields():
    tmp_reports_path = report_generator.ROOT / "data" / "test_saved_reports.json"
    original_path = report_generator.REPORTS_PATH
    try:
        tmp_reports_path.write_text(json.dumps([], indent=2) + "\n", encoding="utf-8")
        report_generator.REPORTS_PATH = tmp_reports_path
        report = report_generator.generate_completion_report()
    finally:
        report_generator.REPORTS_PATH = original_path
        if tmp_reports_path.exists():
            tmp_reports_path.unlink()
    assert 'generated_at' in report
    assert 'completion_percentage' in report
    assert 'skills_demonstrated' in report
