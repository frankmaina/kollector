from polyfactory.factories.pydantic_factory import ModelFactory

from kollector.application.entities.formSchema.form_schema_request import (
    FormSchemaRequest,
)


class FormSchemaRequestFactory(ModelFactory):
    __model__ = FormSchemaRequest
