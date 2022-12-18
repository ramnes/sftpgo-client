from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.api_response import ApiResponse
from ...models.base_virtual_folder import BaseVirtualFolder
from ...types import Response


def _get_kwargs(
    name: str,
    *,
    client: Client,
    json_body: BaseVirtualFolder,
) -> Dict[str, Any]:
    url = "{}/folders/{name}".format(client.base_url, name=name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ApiResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiResponse.from_dict(response.json())

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
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, ApiResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: Client,
    json_body: BaseVirtualFolder,
) -> Response[Union[Any, ApiResponse]]:
    """Update folder

     Updates an existing folder

    Args:
        name (str):
        json_body (BaseVirtualFolder): Defines the filesystem for the virtual folder and the used
            quota limits. The same folder can be shared among multiple users and each user can have
            different quota limits or a different virtual path.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        name=name,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: Client,
    json_body: BaseVirtualFolder,
) -> Optional[Union[Any, ApiResponse]]:
    """Update folder

     Updates an existing folder

    Args:
        name (str):
        json_body (BaseVirtualFolder): Defines the filesystem for the virtual folder and the used
            quota limits. The same folder can be shared among multiple users and each user can have
            different quota limits or a different virtual path.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    return sync_detailed(
        name=name,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: Client,
    json_body: BaseVirtualFolder,
) -> Response[Union[Any, ApiResponse]]:
    """Update folder

     Updates an existing folder

    Args:
        name (str):
        json_body (BaseVirtualFolder): Defines the filesystem for the virtual folder and the used
            quota limits. The same folder can be shared among multiple users and each user can have
            different quota limits or a different virtual path.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        name=name,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: Client,
    json_body: BaseVirtualFolder,
) -> Optional[Union[Any, ApiResponse]]:
    """Update folder

     Updates an existing folder

    Args:
        name (str):
        json_body (BaseVirtualFolder): Defines the filesystem for the virtual folder and the used
            quota limits. The same folder can be shared among multiple users and each user can have
            different quota limits or a different virtual path.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            json_body=json_body,
        )
    ).parsed
