import mongomock

from kollector.application.entities.formSchema.form_schema import FormSchema
from kollector.application.repositories.form_schema_repository import (
    FormSchemaRepository,
)
from kollector.infrastructure.util.formatters import labelize_string
from tests.EntityFactory.entities import FormSchemaRequestFactory

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

"""
This is a sample test case, to demonstrate the usage of the test client
and mongomock
"""


@mongomock.patch(servers=(("localhost", 27017),))
def test_create_form_schema_with_repository():
    request = FormSchemaRequestFactory.build()

    form_schem_repository = FormSchemaRepository()
    response: FormSchema = form_schem_repository.create_form_schema(request)

    assert response.name == request.name
    for field in response.fields:
        assert field.field_label == labelize_string(field.field_title)

    client_response = client.post("/api/v1/formSchema", json=request.dict())
    assert client_response.status_code == 201
