from fastapi import APIRouter

from kollector.api.controller_implementation.form_controller_implementation import (
    EntryControllerImplementation,
)
from kollector.application.repositories.entry_repository import EntryRepository
from kollector.application.usecases.form_usecase import FormUseCase

router = APIRouter(prefix="/api/v1/entry")

form_repository = EntryRepository()
form_usecase = FormUseCase(form_repository)


@router.post("/")
async def submit_form(form_data: dict):
    return EntryControllerImplementation(form_usecase).submit_form(form_data)


@router.get("/")
async def get_forms(form_schema_id: str = None):
    return EntryControllerImplementation(form_usecase).get_forms(form_schema_id)
