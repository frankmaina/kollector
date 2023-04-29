from kollector.api.controller_implementation.base_controller_implementation import (
    BaseControllerImplementation,
)
from kollector.interfaces.usecases.entry_usecase_interface import EntryUseCaseInterface


class EntryControllerImplementation(BaseControllerImplementation):
    def __init__(self, entry_use_case_interface: EntryUseCaseInterface):
        self.entry_use_case_interface = entry_use_case_interface

    def submit_form_entry(self, form_data: dict):
        return self.entry_use_case_interface.submit_form(form_data)

    def get_form_entries(self, form_schema_id: str = None):
        return self.entry_use_case_interface.get_forms(form_schema_id)
