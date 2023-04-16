from kollector.application.interfaces.repositories.form_repository_interface import (
    FormRepositoryInterface,
)
from kollector.application.interfaces.usecases.form_usecase_interface import (
    FormUseCaseInterface,
)


class FormUseCase(FormUseCaseInterface):
    def __init__(self, form_repository: FormRepositoryInterface):
        self.form_repository = form_repository

    def submit_form(self, form_data: dict):
        return self.form_repository.submit_form(form_data)
