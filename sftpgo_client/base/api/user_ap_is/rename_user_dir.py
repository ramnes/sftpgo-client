from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.api_response import ApiResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    path: str,
    target: str,
) -> Dict[str, Any]:
    url = "{}/user/dirs".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["path"] = path

    params["target"] = target

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, List["ApiResponse"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ApiResponse.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, List["ApiResponse"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    path: str,
    target: str,
) -> Response[Union[Any, List["ApiResponse"]]]:
    """Rename a directory

     Rename a directory for the logged in user. The rename is allowed for empty directory or for non
    empty local directories, with no virtual folders inside

    Args:
        path (str):
        target (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ApiResponse']]]
    """

    kwargs = _get_kwargs(
        client=client,
        path=path,
        target=target,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    path: str,
    target: str,
) -> Optional[Union[Any, List["ApiResponse"]]]:
    """Rename a directory

     Rename a directory for the logged in user. The rename is allowed for empty directory or for non
    empty local directories, with no virtual folders inside

    Args:
        path (str):
        target (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ApiResponse']]]
    """

    return sync_detailed(
        client=client,
        path=path,
        target=target,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    path: str,
    target: str,
) -> Response[Union[Any, List["ApiResponse"]]]:
    """Rename a directory

     Rename a directory for the logged in user. The rename is allowed for empty directory or for non
    empty local directories, with no virtual folders inside

    Args:
        path (str):
        target (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ApiResponse']]]
    """

    kwargs = _get_kwargs(
        client=client,
        path=path,
        target=target,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    path: str,
    target: str,
) -> Optional[Union[Any, List["ApiResponse"]]]:
    """Rename a directory

     Rename a directory for the logged in user. The rename is allowed for empty directory or for non
    empty local directories, with no virtual folders inside

    Args:
        path (str):
        target (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ApiResponse']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            path=path,
            target=target,
        )
    ).parsed
