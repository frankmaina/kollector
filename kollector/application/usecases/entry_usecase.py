from kollector.interfaces.repositories.entry_repository_interface import (
    EntryRepositoryInterface,
)
from kollector.interfaces.usecases.entry_usecase_interface import EntryUseCaseInterface


class EntryUseCase(EntryUseCaseInterface):
    def __init__(self, form_repository: EntryRepositoryInterface):
        self.form_repository = form_repository

    def submit_form(self, form_data: dict):
        return self.form_repository.submit_form_entry(form_data)

    def get_forms(self, schema_id: str = None):
        return self.form_repository.get_form_entries(schema_id)
