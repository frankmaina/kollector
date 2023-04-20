from abc import ABC, abstractmethod

from kollector.application.entities.formSchema.form_schema import FormSchema
from kollector.application.entities.formSchema.form_schema_request import (
    FormSchemaRequest,
)


class FormSchemaUseCaseInterface(ABC):
    @abstractmethod
    def get_form_schema(self, form_schema_id: str) -> FormSchema:
        pass

    @abstractmethod
    def get_form_schemas(self) -> list[FormSchema]:
        pass

    @abstractmethod
    def create_form_schema(self, form_schema: FormSchemaRequest) -> FormSchema:
        pass

    @abstractmethod
    def update_form_schema(self, form_schema: FormSchema) -> FormSchema:
        pass

    @abstractmethod
    def delete_form_schema(self, form_schema_id: str) -> None:
        pass
