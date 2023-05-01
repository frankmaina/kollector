from fastapi import APIRouter
import time
from kollector.api.controller_implementation.entry_controller_implementation import (
    EntryControllerImplementation,
)
from kollector.application.repositories.entry_repository import EntryRepository
from kollector.application.usecases.entry_usecase import EntryUseCase

router = APIRouter(prefix="/api/v1/entry")

form_repository = EntryRepository()
entry_usecase = EntryUseCase(form_repository)


@router.post("/", status_code=201)
async def submit_form_entry(form_data: dict):
    return EntryControllerImplementation(entry_usecase).submit_form_entry(form_data)


@router.get("/")
async def get_forms(form_schema_id: str = None):
    return EntryControllerImplementation(entry_usecase).get_form_entries(form_schema_id)
