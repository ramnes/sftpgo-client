import pytest

from sftpgo_client import Client


@pytest.fixture
def client():
    return Client("http://localhost:8080/api/v2", "admin", "password")


def test_client_token_reuse(client):
    client.get_users()
    token = client.token
    client.get_users()
    assert client.token == token
