from flask import Flask, render_template

from portfolio.display_helpers import build_progress_tracker, build_skill_badges
from portfolio.feature_registry import get_all_features
from portfolio.report_generator import generate_completion_report, load_reports
from portfolio.unlock_manager import get_unlocked_features, load_app_state

app = Flask(__name__)


@app.route('/')
def home():
    state = load_app_state()
    return render_template(
        'home.html',
        student_name=state.get('student_name', 'Student Name'),
        course=state.get('course', 'Python Developer Portfolio'),
        progress=build_progress_tracker(),
        overview='Build one assignment per week to unlock portfolio features.',
    )


@app.route('/portfolio')
def portfolio_page():
    unlocked = get_unlocked_features()
    return render_template(
        'portfolio.html',
        unlocked_features=unlocked,
        badges=build_skill_badges(unlocked),
    )


@app.route('/assignments')
def assignments_page():
    state = load_app_state()
    assignments = []
    for feature in get_all_features():
        week_key = f"week{feature['week']:02d}"
        week_state = state['weeks'].get(week_key, {})
        assignments.append(
            {
                **feature,
                'tests_passed': week_state.get('tests_passed', False),
                'completed': week_state.get('completed', False),
            }
        )
    return render_template('assignments.html', assignments=assignments, progress=build_progress_tracker())


@app.route('/skills')
def skills_page():
    unlocked = get_unlocked_features()
    return render_template('skills.html', badges=build_skill_badges(unlocked), progress=build_progress_tracker())


@app.route('/reports')
def reports_page():
    reports = load_reports()
    latest_report = reports[-1] if reports else generate_completion_report()
    return render_template('reports.html', reports=reports, latest_report=latest_report)


if __name__ == '__main__':
    app.run(debug=True)
