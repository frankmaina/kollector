from kollector.api.controller_implementation.base_controller_implementation import (
    BaseControllerImplementation,
)


class FormControllerImplementation(BaseControllerImplementation):
    # def __init__(self, field_use_case: FormUseCaseInterface):
    #     self.field_use_case = field_use_case

    def get_fields(self):
        return self.field_use_case.get_fields()
