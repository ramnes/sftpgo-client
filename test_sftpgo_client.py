import pytest

from sftpgo_client import Client


@pytest.fixture
def client():
    return Client("http://localhost:8080/api/v2", "admin", "password")
