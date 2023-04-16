from fastapi import APIRouter

from kollector.api.controller_implementation.form_controller_implementation import (
    FormControllerImplementation,
)
from kollector.application.repositories.form_repository import FormRepository
from kollector.application.usecases.form_usecase import FormUseCase
from kollector.infrastructure.exceptions.not_found_exception import NotFoundException

router = APIRouter(prefix="/api/v1/form")

form_repository = FormRepository()
form_usecase = FormUseCase(form_repository)


@router.post("/")
async def submit_form(form_data: dict):
    return FormControllerImplementation(form_usecase).submit_form(form_data)
