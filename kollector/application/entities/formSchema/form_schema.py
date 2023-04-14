"""
FormSchema entity
"""
from kollector.application.entities.base import BaseEntityModel
from kollector.application.entities.field_schema.field_schema import FieldSchema


class FormSchema(BaseEntityModel):
    """
    FormSchema entity
    """

    name: str
    fields: list[FieldSchema]
