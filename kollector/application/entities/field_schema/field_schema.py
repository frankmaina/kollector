from pydantic import BaseModel


class FieldSchemaBase(BaseModel):
    type: str
    field_title: str
    required: bool = False
    rules: list[str] = None


class FieldSchema(FieldSchemaBase):
    """
    FieldSchema entity
    """

    field_label: str
