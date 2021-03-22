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

```python
from sftpgo_client import Client

client = Client(
    base_url="http://localhost:8080/api/v2", user="admin", password="password"
)
users = client.get_users()
for user in users:
    print(user.username)
```

Using the asynchronous client:

```python
import asyncio

from sftpgo_client import AsyncClient


async def print_usernames():
    client = AsyncClient(
        base_url="http://localhost:8080/api/v2", user="admin", password="password"
    )
    users = await client.get_users()
    for user in users:
        print(user.username)


asyncio.run(print_usernames())
```

Development
-----------

You can fetch the latest version of the [SFTPGo][] OpenAPI specification and
update `sftpgo_client.base` with:

```
./generator/run.sh
```
