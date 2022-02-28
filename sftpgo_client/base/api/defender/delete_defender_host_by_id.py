from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.api_response import ApiResponse
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
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ApiResponse]]:
    if response.status_code == 200:
        response_200 = ApiResponse.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ApiResponse]]:
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
) -> Response[Union[Any, ApiResponse]]:
    """Removes a host from the defender lists

     Unbans the specified host or clears its violations

    Args:
        id (str):

    Returns:
        Response[Union[Any, ApiResponse]]
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
) -> Optional[Union[Any, ApiResponse]]:
    """Removes a host from the defender lists

     Unbans the specified host or clears its violations

    Args:
        id (str):

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
) -> Response[Union[Any, ApiResponse]]:
    """Removes a host from the defender lists

     Unbans the specified host or clears its violations

    Args:
        id (str):

    Returns:
        Response[Union[Any, ApiResponse]]
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
) -> Optional[Union[Any, ApiResponse]]:
    """Removes a host from the defender lists

     Unbans the specified host or clears its violations

    Args:
        id (str):

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
