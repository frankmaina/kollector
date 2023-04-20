from fastapi import APIRouter
from kollector.api.controller_implementation.form_schema_controller_implementation import (
    FormSchemaControllerImplementation,
)
from kollector.application.entities.formSchema.form_schema_request import (
    FormSchemaRequest,
)

from kollector.application.repositories.form_schema_repository import (
    FormSchemaRepository,
)
from kollector.application.usecases.form_schema_usecase import FormSchemaUseCase

router = APIRouter(prefix="/api/v1/formSchema")

form_schema_repository = FormSchemaRepository()
form_schema_usecase = FormSchemaUseCase(form_schema_repository)


@router.post("/", status_code=201)
async def create_form_schema(schema_request: FormSchemaRequest):
    return FormSchemaControllerImplementation(form_schema_usecase).create_form_schema(
        schema_request
    )


@router.get("/", status_code=200)
async def get_form_schemas():
    return FormSchemaControllerImplementation(form_schema_usecase).get_form_schemas()
