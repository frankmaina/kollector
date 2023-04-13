from kollector.api.controller_implementation.base_controller_implementation import (
    BaseControllerImplementation,
)
from kollector.application.interfaces.usecases.field_usecase_interface import (
    FieldUseCaseInterface,
)


class FieldControllerImplementation(BaseControllerImplementation):
    def __init__(self, field_use_case: FieldUseCaseInterface):
        self.field_use_case = field_use_case

    def get_fields(self):
        return self.field_use_case.get_fields()
