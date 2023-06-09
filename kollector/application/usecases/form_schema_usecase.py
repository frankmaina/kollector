from kollector.application.entities.formSchema.form_schema import FormSchema
from kollector.application.entities.formSchema.form_schema_request import (
    FormSchemaRequest,
)
from kollector.interfaces.repositories.form_schema_repository_interface import (
    FormSchemaRepositoryInterface,
)
from kollector.interfaces.usecases.form_schema_usecase_interface import (
    FormSchemaUseCaseInterface,
)


class FormSchemaUseCase(FormSchemaUseCaseInterface):
    def __init__(self, form_schema_repository: FormSchemaRepositoryInterface):
        self.form_schema_repository = form_schema_repository

    def get_form_schema(self, form_schema_id: str) -> FormSchema:
        pass

    def get_form_schemas(self) -> list[FormSchema]:
        form_schemas = self.form_schema_repository.get_form_schemas()
        return form_schemas

    def create_form_schema(self, form_schema: FormSchemaRequest) -> FormSchema:
        form_schema = self.form_schema_repository.create_form_schema(form_schema)
        return form_schema

    def update_form_schema(self, form_schema: FormSchema) -> FormSchema:
        pass

    def delete_form_schema(self, form_schema_id: str) -> None:
        pass
