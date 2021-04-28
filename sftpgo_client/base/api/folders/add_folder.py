from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.base_virtual_folder import BaseVirtualFolder
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: BaseVirtualFolder,
) -> Dict[str, Any]:
    url = "{}/folders".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[BaseVirtualFolder, None, None, None, None]]:
    if response.status_code == 201:
        response_201 = BaseVirtualFolder.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = None

        return response_400
    if response.status_code == 401:
        response_401 = None

        return response_401
    if response.status_code == 403:
        response_403 = None

        return response_403
    if response.status_code == 500:
        response_500 = None

        return response_500
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[BaseVirtualFolder, None, None, None, None]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: BaseVirtualFolder,
) -> Response[Union[BaseVirtualFolder, None, None, None, None]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: BaseVirtualFolder,
) -> Optional[Union[BaseVirtualFolder, None, None, None, None]]:
    """Adds a new folder. A quota scan is required to update the used files/size"""

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: BaseVirtualFolder,
) -> Response[Union[BaseVirtualFolder, None, None, None, None]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: BaseVirtualFolder,
) -> Optional[Union[BaseVirtualFolder, None, None, None, None]]:
    """Adds a new folder. A quota scan is required to update the used files/size"""

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
