from definitions.query import get_field_definitions

from kollector.infrastructure.util.formatters import strip_python_types_from_definitions
from kollector.interfaces.repositories.field_repository_interface import (
    FieldRepositoryInterface,
)


class FieldRepository(FieldRepositoryInterface):
    def get_field(self, field_id):
        pass

    def get_fields(self):
        native_fields = get_field_definitions()
        return strip_python_types_from_definitions(native_fields)
