import pytest

from sftpgo_client import AsyncClient, Client, User


@pytest.fixture
def client():
    return Client("http://localhost:8080/api/v2", "admin", "password")


@pytest.fixture
def async_client():
    return AsyncClient("http://localhost:8080/api/v2", "admin", "password")


@pytest.fixture(autouse=True)
def clean_users(client):
    for user in client.get_users():
        client.delete_user(user.username)


@pytest.fixture
def user(request, client):
    user = User.from_dict(
        {
            "username": request.node.name,
            "password": "password",
            "permissions": {"/": ["*"]},
        }
    )
    return user


def test_client_token_reuse(client):
    client.get_users()
    token = client.token
    client.get_users()
    assert client.token == token


def test_client_add_user(request, client, user):
    client.add_user(json_body=user)
    user = client.get_users()[0]
    assert isinstance(user, User)
    assert user.username == request.node.name


async def test_async_client_add_user(request, async_client, user):
    await async_client.add_user(json_body=user)
    user = (await async_client.get_users())[0]
    assert isinstance(user, User)
    assert user.username == request.node.name


def test_client_delete_user(client, user):
    client.add_user(json_body=user)
    assert len(client.get_users()) == 1

    response = client.delete_user(user.username)
    assert response.message == "User deleted"
    assert len(client.get_users()) == 0

    response = client.delete_user(user.username)
    assert response is None


async def test_async_client_delete_user(async_client, user):
    await async_client.add_user(json_body=user)
    assert len(await async_client.get_users()) == 1

    response = await async_client.delete_user(user.username)
    assert response.message == "User deleted"
    assert len(await async_client.get_users()) == 0

    response = await async_client.delete_user(user.username)
    assert response is None
