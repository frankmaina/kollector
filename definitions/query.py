import datetime
import uuid


def get_field_definitions():
    """Get field definitions

    returns: list[dict]
    """
    return [
        {"type": "string", "label": "Text", "python_type": str},
        {"type": "number", "label": "Number", "python_type": (int, float)},
        {"type": "date", "label": "Date", "python_type": datetime.date},
        {"type": "time", "label": "Time", "python_type": datetime.time},
        {"type": "datetime", "label": "Date & Time", "python_type": datetime.datetime},
        {"type": "boolean", "label": "Boolean", "python_type": bool},
    ]

