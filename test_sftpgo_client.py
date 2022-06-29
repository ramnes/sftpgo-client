import pytest

from sftpgo_client import AsyncClient, Client, User


@pytest.fixture
def client():
    return Client("http://localhost:8080/api/v2", "admin", "password")


@pytest.fixture
def async_client():
    return AsyncClient("http://localhost:8080/api/v2", "admin", "password")


def test_client_token_reuse(client):
    client.get_users()
    token = client.token
    client.get_users()
    assert client.token == token


def test_client_add_user(client):
    user = User.from_dict(
        {
            "username": "user",
            "password": "password",
            "permissions": {"/": ["*"]},
        }
    )
    client.add_user(json_body=user)

    user = client.get_users()[0]
    assert isinstance(user, User)
    assert user.username == "user"


async def test_async_client_add_user(async_client):
    user = User.from_dict(
        {
            "username": "user",
            "password": "password",
            "permissions": {"/": ["*"]},
        }
    )
    await async_client.add_user(json_body=user)

    user = (await async_client.get_users())[0]
    assert isinstance(user, User)
    assert user.username == "user"
