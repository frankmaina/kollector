import pytest


@pytest.fixture
def form_schema_url():
    return "/api/v1/formSchema"


@pytest.fixture
def form_entry_url():
    return "/api/v1/entry"
