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
    url = "{}/user/dirs".format(client.base_url)

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
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = ApiResponse.from_dict(response_201_item_data)

            response_201.append(response_201_item)

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

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    path: str,
) -> Optional[Union[Any, List[ApiResponse]]]:
    """Create a directory for the logged in user"""

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
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    path: str,
) -> Optional[Union[Any, List[ApiResponse]]]:
    """Create a directory for the logged in user"""

    return (
        await asyncio_detailed(
            client=client,
            path=path,
        )
    ).parsed
