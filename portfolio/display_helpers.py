"""Formatting helpers for dashboard display."""

from portfolio.unlock_manager import get_completion_percentage


def build_progress_tracker():
    percentage = get_completion_percentage()
    return {
        'percentage': percentage,
        'label': f'{percentage:.0f}% Complete',
    }


def build_skill_badges(features):
    return [
        {
            'title': feature['feature_name'],
            'skill': feature['skill'],
            'week': feature['week'],
        }
        for feature in features
    ]
