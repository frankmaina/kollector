from pydantic import BaseModel


class FieldSchemaCreate(BaseModel):
    type: str
    field_title: str
    required: bool
    rules: list[str] = None


class FormSchemaCreate(BaseModel):
    name: str
    fields: list[FieldSchemaCreate]


class FieldSchema(BaseModel):
    type: str
    field_title: str
    field_label: str
    required: bool
    rules: list[str] = None


class FormSchema(BaseModel):
    id: str
    name: str
    fields: list[FieldSchema]
