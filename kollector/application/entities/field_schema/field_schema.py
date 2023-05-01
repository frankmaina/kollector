from pydantic import BaseModel

from kollector.application.entities.field.field import FieldEnum


class FieldSchemaBase(BaseModel):
    type: FieldEnum
    field_title: str
    field_description: str = None
    required: bool = False
    rules: list[str] = None


class FieldSchema(FieldSchemaBase):
    """
    FieldSchema entity
    """

    field_label: str
