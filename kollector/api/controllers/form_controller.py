from fastapi import APIRouter

from kollector.api.controller_implementation.form_controller_implementation import (
    FormControllerImplementation,
)

router = APIRouter()


@router.get("/forms")
async def get_forms():
    return FormControllerImplementation().get_forms()
