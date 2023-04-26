from abc import ABC, abstractmethod


class EntryRepositoryInterface(ABC):
    @abstractmethod
    def submit_form_entry(self, form_data: dict):
        pass

    @abstractmethod
    def get_form_entries(self, form_schema_id: str = None):
        pass
