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
    description: str
    is_active: bool = True
    previous_version: str = None
    version_hash: str = None
    fields: list[FieldSchema]
