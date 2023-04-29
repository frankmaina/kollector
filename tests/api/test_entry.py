import mongomock
from bson import ObjectId
from faker import Faker
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


@mongomock.patch(servers=(("localhost", 27017),))
def test_submit_form_entry_api(form_schema_url, form_entry_url):
    form_schema_request = {
        "name": f"{Faker().name()} form",
        "fields": [
            {
                "type": "text",
                "field_title": "First Name",
                "required": True,
                "rules": ["min:3", "max:10"],
            },
            {
                "type": "text",
                "field_title": "Last Name",
                "required": True,
                "rules": ["min:3", "max:10"],
            },
        ],
    }

    client_response = client.post(form_schema_url, json=form_schema_request)
    test_form = client_response.json()
    test_form_id = test_form["id"]

    entry_request = {
        "schema_id": test_form_id,
        "first_name": f"{Faker().name()}",
        "last_name": f"{Faker().name()}",
    }
    client_response = client.post(form_entry_url, json=entry_request)
    assert client_response.status_code == 201
    entry_reponse = client_response.json()
    assert entry_reponse["schema_id"] == test_form_id
    assert entry_reponse["first_name"] == entry_request["first_name"]
    assert entry_reponse["last_name"] == entry_request["last_name"]
    assert entry_reponse["id"] is not None
    assert entry_reponse["schema"] == test_form

    entry_request["schema_id"] = str(ObjectId("0123456789ab0123456789ab"))
    client_response = client.post(form_entry_url, json=entry_request)
    assert client_response.status_code == 404

    invalid_entry_request = {
        "schema_id": test_form_id,
        "first_name": f"{Faker().name()}",
    }

    client_response = client.post(form_entry_url, json=invalid_entry_request)
    assert client_response.status_code == 400


@mongomock.patch(servers=(("localhost", 27017),))
def test_get_form_entry_api(form_schema_url, form_entry_url):
    entries = client.get(form_entry_url).json()
    assert len(entries) != 0
