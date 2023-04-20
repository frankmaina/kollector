from kollector.interfaces.repositories.field_repository_interface import (
    FieldRepositoryInterface,
)
from kollector.interfaces.usecases.field_usecase_interface import FieldUseCaseInterface


class FieldUseCase(FieldUseCaseInterface):
    def __init__(self, field_repository: FieldRepositoryInterface):
        self.field_repository = field_repository

    def get_field(self, field_id: str):
        pass

    def get_fields(self):
        return self.field_repository.get_fields()
