import re


def labelize_string(s):
    """
    Converts a string to a snake case or "labelized" form.
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
