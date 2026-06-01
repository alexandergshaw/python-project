"""Helpers for storing and reading feature unlock status."""

from __future__ import annotations

import json
from pathlib import Path

from portfolio.feature_registry import get_all_features

ROOT = Path(__file__).resolve().parent.parent
APP_STATE_PATH = ROOT / 'data' / 'app_state.json'


def _default_state():
    return {
        'student_name': 'Student Name',
        'course': 'Python Developer Portfolio',
        'weeks': {f"week{feature['week']:02d}": {'completed': False, 'tests_passed': False} for feature in get_all_features()},
    }


def load_app_state():
    if not APP_STATE_PATH.exists():
        save_app_state(_default_state())
    with APP_STATE_PATH.open('r', encoding='utf-8') as handle:
        return json.load(handle)


def save_app_state(state):
    APP_STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with APP_STATE_PATH.open('w', encoding='utf-8') as handle:
        json.dump(state, handle, indent=2)
        handle.write('\n')


def update_week_status(week_number, tests_passed):
    state = load_app_state()
    week_key = f'week{week_number:02d}'
    if week_key not in state['weeks']:
        raise ValueError(f'Unknown week: {week_number}')
    state['weeks'][week_key]['tests_passed'] = bool(tests_passed)
    state['weeks'][week_key]['completed'] = bool(tests_passed)
    save_app_state(state)
    return state


def get_unlocked_features():
    state = load_app_state()
    unlocked = []
    for feature in get_all_features():
        week_key = f"week{feature['week']:02d}"
        if state['weeks'].get(week_key, {}).get('tests_passed'):
            unlocked.append(feature)
    return unlocked


def get_completion_percentage():
    state = load_app_state()
    weeks = list(state['weeks'].values())
    if not weeks:
        return 0
    completed = sum(1 for entry in weeks if entry.get('tests_passed'))
    return round((completed / len(weeks)) * 100, 2)
