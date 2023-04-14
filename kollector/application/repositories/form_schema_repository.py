from kollector.application.entities.field_schema.field_schema import FieldSchema
from kollector.application.entities.formSchema.form_schema import FormSchema
from kollector.application.entities.formSchema.form_schema_request import (
    FormSchemaRequest,
)
from kollector.application.interfaces.repositories.form_schema_repository_interface import (
    FormSchemaRepositoryInterface,
)
from kollector.infrastructure.database import get_schema_collection
from kollector.infrastructure.util.formatters import labelize_string


class FormSchemaRepository(FormSchemaRepositoryInterface):
    def __init__(self):
        self._schema_collection = None

    def _get_schema_collection(self):
        if self._schema_collection is None:
            self._schema_collection = get_schema_collection()

        return self._schema_collection

    def get_form_schema(self, form_id: str) -> FormSchema:
        pass

    def get_form_schemas(self) -> list[FormSchema]:
        schemas = self._get_schema_collection().find()

        formSchemas = []
        for schema in schemas:
            formSchemas.append(self._form_schema_repository_object_to_entity(schema))

        return formSchemas

    def create_form_schema(self, form_schema: FormSchemaRequest) -> FormSchema:
        create_request = self._form_schema_request_to_repository_object(
            form_schema.dict()
        )
        schema = self._schema_collection.find_one(
            {"_id": self._schema_collection.insert_one(create_request).inserted_id}
        )
        return self._form_schema_repository_object_to_entity(schema)

    def update_form_schema(self, form_schema: FormSchema) -> FormSchema:
        pass

    def delete_form_schema(self, form_id: str) -> None:
        pass

    @staticmethod
    def _form_schema_repository_object_to_entity(form_schema_dto: dict) -> FormSchema:
        """
        Converts a form schema dto to a form schema entity
        form_schema_dto: dict
        return: FormSchema
        """
        fields = [FieldSchema(**field) for field in form_schema_dto["fields"]]
        return FormSchema(
            id=str(form_schema_dto["_id"]), name=form_schema_dto["name"], fields=fields
        )

    @staticmethod
    def _form_schema_request_to_repository_object(form_schema: dict) -> dict:
        """
        Converts a form schema entity to a form schema dto
        form_schema: FormSchema
        return: dict
        """
        for field in form_schema["fields"]:
            field["field_label"] = labelize_string(field["field_title"])
        return form_schema
