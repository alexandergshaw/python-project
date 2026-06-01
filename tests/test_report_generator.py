from portfolio.report_generator import generate_completion_report


def test_generate_completion_report_has_required_fields():
    report = generate_completion_report()
    assert 'generated_at' in report
    assert 'completion_percentage' in report
    assert 'skills_demonstrated' in report
