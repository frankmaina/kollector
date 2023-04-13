from fastapi import APIRouter

from kollector.api.controller_implementation.field_controller_implementation import (
    FieldControllerImplementation,
)
from kollector.application.repositories.field_repository import FieldRepository

from kollector.application.usecases.field_usecase import FieldUseCase

router = APIRouter()


@router.get("/fields")
async def get_fields():
    field_repository = FieldRepository()
    field_usecase = FieldUseCase(field_repository)
    return FieldControllerImplementation(field_usecase).get_fields()
