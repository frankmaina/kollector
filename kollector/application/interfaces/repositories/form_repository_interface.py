from abc import ABC, abstractmethod


class FormRepositoryInterface(ABC):
    @abstractmethod
    def submit_form(self, form_data: dict):
        pass
