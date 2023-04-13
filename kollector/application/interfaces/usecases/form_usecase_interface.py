from abc import ABC, abstractmethod


class FormUseCaseInterface(ABC):
    @abstractmethod
    def get_form(self, form_id: str):
        pass

    @abstractmethod
    def get_forms(self):
        pass

    @abstractmethod
    def create_form(self, form: FormCreate):
        pass

    @abstractmethod
    def update_form(self, form: Form):
        pass

    @abstractmethod
    def delete_form(self, form_id: str):
        pass
