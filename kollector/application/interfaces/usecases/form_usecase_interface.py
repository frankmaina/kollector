from abc import ABC, abstractmethod


class FormUseCaseInterface(ABC):
    @abstractmethod
    def submit_form(self, form_data: dict):
        pass
