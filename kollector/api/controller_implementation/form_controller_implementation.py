from kollector.api.controller_implementation.base_controller_implementation import (
    BaseControllerImplementation,
)
from kollector.application.interfaces.usecases.form_usecase_interface import (
    FormUseCaseInterface,
)


class FormControllerImplementation(BaseControllerImplementation):
    def __init__(self, form_use_case_interface: FormUseCaseInterface):
        self.form_use_case_interface = form_use_case_interface

    def submit_form(self, form_data: dict):
        return self.form_use_case_interface.submit_form(form_data)
