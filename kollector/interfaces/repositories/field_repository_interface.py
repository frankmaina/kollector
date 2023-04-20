from abc import ABC, abstractmethod


class FieldRepositoryInterface(ABC):
    @abstractmethod
    def get_field(self, field_id):
        pass

    @abstractmethod
    def get_fields(self):
        pass
