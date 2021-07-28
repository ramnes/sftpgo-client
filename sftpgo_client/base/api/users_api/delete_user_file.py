from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.api_response import ApiResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    path: str,
) -> Dict[str, Any]:
    url = "{}/user/files".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "path": path,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, List[ApiResponse]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ApiResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
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
) -> Response[Union[Any, List[ApiResponse]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    path: str,
) -> Response[Union[Any, List[ApiResponse]]]:
    kwargs = _get_kwargs(
        client=client,
        path=path,
    )

    response = httpx.delete(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    path: str,
) -> Optional[Union[Any, List[ApiResponse]]]:
    """Delete a file for the logged in user."""

    return sync_detailed(
        client=client,
        path=path,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    path: str,
) -> Response[Union[Any, List[ApiResponse]]]:
    kwargs = _get_kwargs(
        client=client,
        path=path,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.delete(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    path: str,
) -> Optional[Union[Any, List[ApiResponse]]]:
    """Delete a file for the logged in user."""

    return (
        await asyncio_detailed(
            client=client,
            path=path,
        )
    ).parsed
