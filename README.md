[SFTPGo]: https://github.com/drakkan/sftpgo

sftpgo-client
=============

[![PyPI](https://img.shields.io/pypi/v/sftpgo-client.svg)](https://pypi.org/project/sftpgo-client)
[![License](https://img.shields.io/github/license/ramnes/sftpgo-client)](LICENSE)
[![Code style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/ambv/black)

Python client for the [SFTPGo][] API

The `sftpgo_client.base` package is automatically generated from the [OpenAPI
specification](generator/openapi.yaml) provided by [SFTPGo][] using
[openapi-python-client](https://github.com/triaxtec/openapi-python-client).

Installation
------------

```
pip install sftpgo-client
```

Examples
--------

* Creating a client:

```python
from sftpgo_client import Client

client = Client(
    base_url="http://localhost:8080/api/v2", user="admin", password="password"
)
```

In an asyncio environment, use the asynchronous client instead:

```python
from sftpgo_client import AsyncClient

client = AsyncClient(
    base_url="http://localhost:8080/api/v2", user="admin", password="password"
)
```

* Listing users:

```python
users = client.get_users()
for user in users:
    print(user.username)
```

or with the asynchronous client:

```python
users = await client.get_users()
for user in users:
    print(user.username)
```

All API endpoints are available in both the synchronous and asynchronous clients.

* Adding a new user:

```python
from sftpgo_client import User

user = User.from_dict(
    {
        "username": "user",
        "password": "password",
        "permissions": {"/": ["*"]},
    }
)
client.add_user(json_body=user)
```

Development
-----------

You can fetch the latest version of the [SFTPGo][] OpenAPI specification and
update `sftpgo_client.base` with:

```
./generator/run.sh
```

You can run the tests with:

```
pip install -r requirements.txt
docker-compose up -d
pytest
```
