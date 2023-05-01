from enum import Enum


class FieldEnum(str, Enum):
    text = "text"
    number = "number"
    date = "date"
    time = "time"
    datetime = "datetime"
    boolean = "boolean"
