from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.dir_entry import DirEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    path: Union[Unset, str] = UNSET,
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
) -> Optional[Union[Any, List[DirEntry]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DirEntry.from_dict(response_200_item_data)

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
) -> Response[Union[Any, List[DirEntry]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    path: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List[DirEntry]]]:
    kwargs = _get_kwargs(
        client=client,
        path=path,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    path: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List[DirEntry]]]:
    """Returns the contents of the specified directory for the logged in user"""

    return sync_detailed(
        client=client,
        path=path,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    path: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List[DirEntry]]]:
    kwargs = _get_kwargs(
        client=client,
        path=path,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    path: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List[DirEntry]]]:
    """Returns the contents of the specified directory for the logged in user"""

    return (
        await asyncio_detailed(
            client=client,
            path=path,
        )
    ).parsed
