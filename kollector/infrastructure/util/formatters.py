import re
from datetime import datetime, timezone


def labelize_string(s):
    """
    Converts a string to a snake case or "labelized" entry.
    """
    s = s.strip().lower()
    s = re.sub(r"\W+", "_", s)
    return s


def strip_python_types_from_definitions(constants):
    """
    Strips the "python_type" field from the given list
    of constants and returns a new list.
    """
    return [
        {k: v for k, v in constant.items() if k != "python_type"}
        for constant in constants
    ]


def get_current_utc_time_as_str():
    return datetime.now(timezone.utc).isoformat()
