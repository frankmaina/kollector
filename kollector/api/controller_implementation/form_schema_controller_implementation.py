from kollector.api.controller_implementation.base_controller_implementation import (
    BaseControllerImplementation,
)
from kollector.application.interfaces.usecases.form_schema_usecase_interface import (
    FormSchemaUseCaseInterface,
)
from kollector.application.entities.formSchema import FormSchemaCreate


class FormSchemaControllerImplementation(BaseControllerImplementation):
    def __init__(self, form_schema_use_case_interface: FormSchemaUseCaseInterface):
        self.form_schema_use_case_interface = form_schema_use_case_interface

    def create_form_schema(self, form_schema: FormSchemaCreate):
        return self.form_schema_use_case_interface.create_form_schema(form_schema)

    def get_form_schemas(self):
        return self.form_schema_use_case_interface.get_form_schemas()
