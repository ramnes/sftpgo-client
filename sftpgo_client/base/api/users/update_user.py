from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.api_response import ApiResponse
from ...models.update_user_disconnect import UpdateUserDisconnect
from ...models.user import User
from ...types import UNSET, Response, Unset


def _get_kwargs(
    username: str,
    *,
    client: Client,
    json_body: User,
    disconnect: Union[Unset, None, UpdateUserDisconnect] = UNSET,
) -> Dict[str, Any]:
    url = "{}/users/{username}".format(client.base_url, username=username)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_disconnect: Union[Unset, None, int] = UNSET
    if not isinstance(disconnect, Unset):
        json_disconnect = disconnect.value if disconnect else None

    params["disconnect"] = json_disconnect

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
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
    username: str,
    *,
    client: Client,
    json_body: User,
    disconnect: Union[Unset, None, UpdateUserDisconnect] = UNSET,
) -> Response[Union[Any, ApiResponse]]:
    """Update user

     Updates an existing user and optionally disconnects it, if connected, to apply the new settings.
    Recovery codes and TOTP configuration cannot be set/updated using this API: each user must use the
    specific APIs

    Args:
        username (str):
        disconnect (Union[Unset, None, UpdateUserDisconnect]):
        json_body (User):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
        json_body=json_body,
        disconnect=disconnect,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: Client,
    json_body: User,
    disconnect: Union[Unset, None, UpdateUserDisconnect] = UNSET,
) -> Optional[Union[Any, ApiResponse]]:
    """Update user

     Updates an existing user and optionally disconnects it, if connected, to apply the new settings.
    Recovery codes and TOTP configuration cannot be set/updated using this API: each user must use the
    specific APIs

    Args:
        username (str):
        disconnect (Union[Unset, None, UpdateUserDisconnect]):
        json_body (User):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    return sync_detailed(
        username=username,
        client=client,
        json_body=json_body,
        disconnect=disconnect,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: Client,
    json_body: User,
    disconnect: Union[Unset, None, UpdateUserDisconnect] = UNSET,
) -> Response[Union[Any, ApiResponse]]:
    """Update user

     Updates an existing user and optionally disconnects it, if connected, to apply the new settings.
    Recovery codes and TOTP configuration cannot be set/updated using this API: each user must use the
    specific APIs

    Args:
        username (str):
        disconnect (Union[Unset, None, UpdateUserDisconnect]):
        json_body (User):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
        json_body=json_body,
        disconnect=disconnect,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: Client,
    json_body: User,
    disconnect: Union[Unset, None, UpdateUserDisconnect] = UNSET,
) -> Optional[Union[Any, ApiResponse]]:
    """Update user

     Updates an existing user and optionally disconnects it, if connected, to apply the new settings.
    Recovery codes and TOTP configuration cannot be set/updated using this API: each user must use the
    specific APIs

    Args:
        username (str):
        disconnect (Union[Unset, None, UpdateUserDisconnect]):
        json_body (User):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            json_body=json_body,
            disconnect=disconnect,
        )
    ).parsed
