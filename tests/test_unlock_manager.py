from portfolio.unlock_manager import get_completion_percentage, load_app_state, save_app_state, update_week_status


def test_update_week_status_unlocks_feature():
    original_state = load_app_state()
    try:
        update_week_status(1, True)
        assert get_completion_percentage() >= 6
    finally:
        save_app_state(original_state)
