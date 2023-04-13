from kollector.application.interfaces.repositories.form_schema_repository_interface import (
    FormSchemaRepositoryInterface,
)
from kollector.application.entities.formSchema import (
    FormSchema,
    FormSchemaCreate,
    FieldSchema,
)
from kollector.infrastructure.database import get_schema_collection
from kollector.infrastructure.util.formatters import labelize_string


class FormSchemaRepository(FormSchemaRepositoryInterface):
    def get_form_schema(self, form_id: str) -> FormSchema:
        pass

    def get_form_schemas(self) -> list[FormSchema]:
        schema_collection = get_schema_collection()
        schemas = schema_collection.find()

        formSchemas = []
        for schema in schemas:
            obj_id = str(schema["_id"])
            name = schema["name"]
            fields = [FieldSchema(**field) for field in schema["fields"]]
            formSchemas.append(FormSchema(id=obj_id, name=name, fields=fields))

        return formSchemas

    def create_form_schema(self, form_schema: FormSchemaCreate) -> FormSchema:
        schema_collection = get_schema_collection()

        request = form_schema.dict()
        for field in request["fields"]:
            field["field_label"] = labelize_string(field["field_title"])
        result = schema_collection.insert_one(request)
        savedSchema = schema_collection.find_one({"_id": result.inserted_id})

        id = str(savedSchema["_id"])
        name = savedSchema["name"]
        fields = [FieldSchema(**field) for field in savedSchema["fields"]]
        return FormSchema(id=id, name=name, fields=fields)

    def update_form_schema(self, form_schema: FormSchema) -> FormSchema:
        pass

    def delete_form_schema(self, form_id: str) -> None:
        pass
