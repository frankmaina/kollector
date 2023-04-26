import mongomock

from kollector.application.entities.formSchema.form_schema import FormSchema
from kollector.application.repositories.form_schema_repository import (
    FormSchemaRepository,
)
from kollector.infrastructure.util.formatters import labelize_string
from tests.entity_factory.entities import FormSchemaRequestFactory

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


# @mongomock.patch(servers=(("localhost", 27017),))
# def test_create_form_schema_with_repository():
#     """
#     This is a sample test case, to demonstrate the usage of the test client
#     and mongomock
#     """
#     request = FormSchemaRequestFactory.build()
#
#     form_schem_repository = FormSchemaRepository()
#     response: FormSchema = form_schem_repository.create_form_schema(request)
#
#     assert response.name == request.name
#     for field in response.fields:
#         assert field.field_label == labelize_string(field.field_title)
#
#     client_response = client.post("/api/v1/formSchema", json=request.dict())
#     assert client_response.status_code == 201


@mongomock.patch(servers=(("localhost", 27017),))
def test_create_form_schema_api(form_schema_url):
    request = FormSchemaRequestFactory.build()

    client_response = client.post(form_schema_url, json=request.dict())
    assert client_response.status_code == 201
    assert request.name == client_response.json()["name"]
    for field in client_response.json()["fields"]:
        assert field["field_label"] == labelize_string(field["field_title"])


@mongomock.patch(servers=(("localhost", 27017),))
def test_get_form_schema_api(form_schema_url):
    for _ in range(1, 11):
        request = FormSchemaRequestFactory.build()
        response = client.post(form_schema_url, json=request.dict())
        assert response.status_code == 201

    response = client.get(form_schema_url)
    assert response.status_code == 200
    assert len(response.json()) == 11  # 10 form schemas created, 1 from  above testcase
