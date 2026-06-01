"""Generate portfolio evidence reports backed by JSON persistence."""

from __future__ import annotations

import json
from datetime import datetime, UTC
from pathlib import Path

from portfolio.unlock_manager import get_completion_percentage, get_unlocked_features

ROOT = Path(__file__).resolve().parent.parent
REPORTS_PATH = ROOT / 'data' / 'saved_reports.json'


def load_reports():
    if not REPORTS_PATH.exists():
        REPORTS_PATH.write_text('[]\n', encoding='utf-8')
    with REPORTS_PATH.open('r', encoding='utf-8') as handle:
        return json.load(handle)


def save_reports(reports):
    with REPORTS_PATH.open('w', encoding='utf-8') as handle:
        json.dump(reports, handle, indent=2)
        handle.write('\n')


def generate_completion_report():
    unlocked = get_unlocked_features()
    report = {
        'generated_at': datetime.now(UTC).isoformat(),
        'completion_percentage': get_completion_percentage(),
        'unlocked_feature_count': len(unlocked),
        'skills_demonstrated': sorted({feature['skill'] for feature in unlocked}),
        'features': [feature['feature_name'] for feature in unlocked],
    }
    reports = load_reports()
    reports.append(report)
    save_reports(reports)
    return report
