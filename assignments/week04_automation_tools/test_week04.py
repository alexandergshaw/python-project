from assignments.week04_automation_tools.starter import (
    build_feature_summary,
    normalize_input,
    validate_payload,
)


def test_normalize_input_handles_basic_values():
    assert normalize_input('  Python  ') == 'python'
    assert normalize_input(123) == '123'


def test_normalize_input_handles_none_edge_case():
    assert normalize_input(None) == ''


def test_build_feature_summary_formats_output():
    summary = build_feature_summary('data toolkit', 'Loops and iteration')
    assert 'Data Toolkit' in summary
    assert 'Demonstrates' in summary


def test_validate_payload_positive_case():
    assert validate_payload({'name': 'Project', 'skill': 'Python'}) is True


def test_validate_payload_negative_and_edge_cases():
    assert validate_payload('not-a-dict') is False
    assert validate_payload({'name': 'only-name'}) is False
    assert validate_payload({'name': '  ', 'skill': 'python'}) is False
