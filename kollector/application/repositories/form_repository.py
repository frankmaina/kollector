import copy

from kollector.application.entities.formSchema.form_schema import FormSchema
from kollector.application.interfaces.repositories.form_repository_interface import (
    FormRepositoryInterface,
)
from kollector.application.repositories.form_schema_repository import (
    FormSchemaRepository,
)
from kollector.infrastructure.database import get_schema_collection, get_form_collection
from kollector.infrastructure.exceptions.validation_exception import ValidationException


class FormRepository(FormRepositoryInterface):
    def __init__(self):
        self._schema_collection = None
        self._form_collection = None

    def _get_form_collection(self):
        if self._form_collection is None:
            self._form_collection = get_form_collection()

        return self._form_collection

    def _validate_form_schema(self, form_schema: FormSchema, form_data: dict):
        for field in form_schema.fields:
            if field.required and field.field_label not in form_data:
                raise ValidationException(f"Field {field.field_label} is required")

    def _clean_form_data(self, form_schema: FormSchema, form_data: dict):
        form_copy = copy.deepcopy(form_data)
        form_field_keys = [field.field_label for field in form_schema.fields]

        for field in list(form_copy.keys()):
            if field not in form_field_keys:
                del form_copy[field]
        return form_copy

    def submit_form(self, form_data) -> dict:
        schema = FormSchemaRepository().get_form_schema(form_data.get("schema_id"))

        self._validate_form_schema(schema, form_data)
        cleaned_form = self._clean_form_data(schema, form_data)

        cleaned_form["schema_id"] = schema.id
        cleaned_form["schema"] = schema.dict()
        result = self._get_form_collection().insert_one(cleaned_form)
        submitted_form = self._get_form_collection().find_one(
            {"_id": result.inserted_id}
        )
        del submitted_form["_id"]
        submitted_form["id"] = str(result.inserted_id)
        return submitted_form
