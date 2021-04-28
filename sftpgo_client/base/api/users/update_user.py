from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.api_response import ApiResponse
from ...models.update_user_disconnect import UpdateUserDisconnect
from ...models.user import User
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    username: str,
    json_body: User,
    disconnect: Union[Unset, UpdateUserDisconnect] = UNSET,
) -> Dict[str, Any]:
    url = "{}/users/{username}".format(client.base_url, username=username)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_disconnect: Union[Unset, int] = UNSET
    if not isinstance(disconnect, Unset):
        json_disconnect = disconnect.value

    params: Dict[str, Any] = {
        "disconnect": json_disconnect,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ApiResponse, None]]:
    if response.status_code == 200:
        response_200 = ApiResponse.from_dict(response.json())

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
    if response.status_code == 404:
        response_404 = None

        return response_404
    if response.status_code == 500:
        response_500 = None

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ApiResponse, None]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    username: str,
    json_body: User,
    disconnect: Union[Unset, UpdateUserDisconnect] = UNSET,
) -> Response[Union[ApiResponse, None]]:
    kwargs = _get_kwargs(
        client=client,
        username=username,
        json_body=json_body,
        disconnect=disconnect,
    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    username: str,
    json_body: User,
    disconnect: Union[Unset, UpdateUserDisconnect] = UNSET,
) -> Optional[Union[ApiResponse, None]]:
    """Updates an existing user and optionally disconnects it, if connected, to apply the new settings"""

    return sync_detailed(
        client=client,
        username=username,
        json_body=json_body,
        disconnect=disconnect,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    username: str,
    json_body: User,
    disconnect: Union[Unset, UpdateUserDisconnect] = UNSET,
) -> Response[Union[ApiResponse, None]]:
    kwargs = _get_kwargs(
        client=client,
        username=username,
        json_body=json_body,
        disconnect=disconnect,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    username: str,
    json_body: User,
    disconnect: Union[Unset, UpdateUserDisconnect] = UNSET,
) -> Optional[Union[ApiResponse, None]]:
    """Updates an existing user and optionally disconnects it, if connected, to apply the new settings"""

    return (
        await asyncio_detailed(
            client=client,
            username=username,
            json_body=json_body,
            disconnect=disconnect,
        )
    ).parsed
