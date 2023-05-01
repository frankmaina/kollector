from pydantic import BaseModel

from kollector.application.entities.field_schema.field_schema_request import (
    FieldSchemaRequest,
)


class FormSchemaRequest(BaseModel):
    """
    FormSchemaRequest entity
    """

    name: str
    description: str
    fields: list[FieldSchemaRequest]
