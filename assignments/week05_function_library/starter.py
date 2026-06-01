"""Starter code for week 05: Function Library."""


def normalize_input(value):
    """Return a cleaned lowercase string value."""
    # TODO: Keep this implementation concise and readable.
    if value is None:
        return ''
    return str(value).strip().lower()


def build_feature_summary(name, skill):
    """Create a human-readable feature summary for this week."""
    # TODO: Ensure this formatting remains professional for employer-facing output.
    cleaned_name = normalize_input(name).title()
    cleaned_skill = normalize_input(skill).title()
    return f"{cleaned_name}: Demonstrates {cleaned_skill}"


def validate_payload(payload):
    """Validate assignment payload dictionaries."""
    # TODO: Add any additional validation rules required by your week rubric.
    if not isinstance(payload, dict):
        return False
    required = {'name', 'skill'}
    return required.issubset(payload) and all(normalize_input(payload[key]) for key in required)
