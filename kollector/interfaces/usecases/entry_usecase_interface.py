from abc import ABC, abstractmethod


class EntryUseCaseInterface(ABC):
    @abstractmethod
    def submit_form(self, form_data: dict):
        pass

    @abstractmethod
    def get_forms(self, schema_id: str = None):
        pass
