import pytest
from fastapi.testclient import TestClient
from my_app import app, custom_header


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def response(client):
    return client.get("/")

def test_root_(response):
    assert response.ok
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World'}

@pytest.mark.parametrize("key, value", custom_header.items())
def test_values_at_custom_header(response, key, value):
    assert key in response.headers
    assert response.headers[key] == value
