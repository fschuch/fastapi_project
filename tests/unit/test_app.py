import pytest
from fastapi.testclient import TestClient
from my_app import app, my_header


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def response(client):
    return client.get("/")


@pytest.mark.parametrize("key, value", my_header.items())
def test_custom_key_values_at_header(response, key, value):
    assert response.headers[key] == value
