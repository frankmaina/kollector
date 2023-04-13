from abc import ABC, abstractmethod


class FieldUseCaseInterface(ABC):
    @abstractmethod
    def get_field(self, field_id: str):
        pass

    @abstractmethod
    def get_fields(self):
        pass
