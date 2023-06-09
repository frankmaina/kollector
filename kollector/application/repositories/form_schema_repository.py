from bson.objectid import ObjectId

from kollector.application.entities.field_schema.field_schema import FieldSchema
from kollector.application.entities.formSchema.form_schema import FormSchema
from kollector.application.entities.formSchema.form_schema_request import (
    FormSchemaRequest,
)
from kollector.infrastructure.database import get_schema_collection
from kollector.infrastructure.exceptions.not_found_exception import NotFoundException
from kollector.infrastructure.util.formatters import (
    get_current_utc_time_as_str,
    labelize_string,
)
from kollector.interfaces.repositories.form_schema_repository_interface import (
    FormSchemaRepositoryInterface,
)


class FormSchemaRepository(FormSchemaRepositoryInterface):
    def __init__(self):
        self._schema_collection = None

    def _get_schema_collection(self):
        if self._schema_collection is None:
            self._schema_collection = get_schema_collection()
        return self._schema_collection

    def get_form_schema(self, form_id: str, convert_to_entity: bool = True):
        schema = self._get_schema_collection().find_one({"_id": ObjectId(form_id)})
        if schema is None:
            raise NotFoundException(f"The entry schema with id {form_id} was not found")
        if convert_to_entity:
            return self._form_schema_repository_object_to_entity(schema)
        return schema

    def get_form_schemas(self) -> list[FormSchema]:
        schemas = self._get_schema_collection().find(
            {"$or": [{"is_deleted": False}, {"is_deleted": None}]}
        )
        formSchemas = []
        for schema in schemas:
            formSchemas.append(self._form_schema_repository_object_to_entity(schema))

        return formSchemas

    def create_form_schema(self, form_schema: FormSchemaRequest) -> FormSchema:
        create_request = self._form_schema_request_to_repository_object(
            form_schema.dict()
        )
        return self.get_form_schema(
            self._get_schema_collection().insert_one(create_request).inserted_id
        )

    def update_form_schema(self, form_schema: FormSchema) -> FormSchema:
        pass

    def delete_form_schema(self, form_id: str):
        schema = self.get_form_schema(form_id, False)
        schema["is_deleted"] = True
        current_time = get_current_utc_time_as_str()
        schema["updated_at"] = current_time
        schema["deleted_at"] = current_time
        self._get_schema_collection().update_one(schema)

    @staticmethod
    def _form_schema_repository_object_to_entity(form_schema_dto: dict) -> FormSchema:
        """
        Converts a entry schema dto to a entry schema entity
        form_schema_dto: dict
        return: FormSchema
        """
        fields = [FieldSchema(**field) for field in form_schema_dto["fields"]]
        return FormSchema(
            id=str(form_schema_dto["_id"]),
            name=form_schema_dto["name"],
            description=form_schema_dto["description"],
            created_at=form_schema_dto["created_at"],
            updated_at=form_schema_dto["updated_at"],
            fields=fields,
        )

    @staticmethod
    def _form_schema_request_to_repository_object(form_schema: dict) -> dict:
        """
        Converts a entry schema request to a entry schema repository object
        form_schema: dict
        return: dict
        """
        for field in form_schema["fields"]:
            field["field_label"] = labelize_string(field["field_title"])
        current_time = get_current_utc_time_as_str()
        form_schema["created_at"] = current_time
        form_schema["updated_at"] = current_time
        return form_schema
