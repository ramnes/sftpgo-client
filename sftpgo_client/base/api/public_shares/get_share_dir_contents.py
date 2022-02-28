from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.dir_entry import DirEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    path: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/shares/{id}/dirs".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["path"] = path

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
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
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 500:
        response_500 = cast(Any, None)
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
    id: str,
    *,
    client: AuthenticatedClient,
    path: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, List[DirEntry]]]:
    """Read directory contents

     Returns the contents of the specified directory for the specified share. The share must have exactly
    one path defined and it must be a directory for this to work

    Args:
        id (str):
        path (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, List[DirEntry]]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        path=path,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    path: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, List[DirEntry]]]:
    """Read directory contents

     Returns the contents of the specified directory for the specified share. The share must have exactly
    one path defined and it must be a directory for this to work

    Args:
        id (str):
        path (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, List[DirEntry]]]
    """

    return sync_detailed(
        id=id,
        client=client,
        path=path,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    path: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, List[DirEntry]]]:
    """Read directory contents

     Returns the contents of the specified directory for the specified share. The share must have exactly
    one path defined and it must be a directory for this to work

    Args:
        id (str):
        path (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, List[DirEntry]]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        path=path,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    path: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, List[DirEntry]]]:
    """Read directory contents

     Returns the contents of the specified directory for the specified share. The share must have exactly
    one path defined and it must be a directory for this to work

    Args:
        id (str):
        path (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, List[DirEntry]]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            path=path,
        )
    ).parsed
