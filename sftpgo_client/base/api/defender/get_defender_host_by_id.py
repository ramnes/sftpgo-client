from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.defender_entry import DefenderEntry
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/defender/hosts/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, DefenderEntry]]:
    if response.status_code == 200:
        response_200 = DefenderEntry.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, DefenderEntry]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
) -> Response[Union[Any, DefenderEntry]]:
    """Get host by id

     Returns the host with the given id, if it exists

    Args:
        id (str):

    Returns:
        Response[Union[Any, DefenderEntry]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
) -> Optional[Union[Any, DefenderEntry]]:
    """Get host by id

     Returns the host with the given id, if it exists

    Args:
        id (str):

    Returns:
        Response[Union[Any, DefenderEntry]]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
) -> Response[Union[Any, DefenderEntry]]:
    """Get host by id

     Returns the host with the given id, if it exists

    Args:
        id (str):

    Returns:
        Response[Union[Any, DefenderEntry]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
) -> Optional[Union[Any, DefenderEntry]]:
    """Get host by id

     Returns the host with the given id, if it exists

    Args:
        id (str):

    Returns:
        Response[Union[Any, DefenderEntry]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
