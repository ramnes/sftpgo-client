from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.api_response import ApiResponse
from ...types import Response


def _get_kwargs(
    username: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/users/{username}/forgot-password".format(
        client.base_url, username=username
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
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
) -> Response[Union[Any, ApiResponse]]:
    """Send a password reset code by email

     You must configure an SMTP server, the account must have a valid email address and must not have the
    \"reset-password-disabled\" restriction, in which case SFTPGo will send a code via email to reset
    the password. If the specified user does not exist, the request will be silently ignored (a success
    response will be returned) to avoid disclosing existing users

    Args:
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
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
) -> Optional[Union[Any, ApiResponse]]:
    """Send a password reset code by email

     You must configure an SMTP server, the account must have a valid email address and must not have the
    \"reset-password-disabled\" restriction, in which case SFTPGo will send a code via email to reset
    the password. If the specified user does not exist, the request will be silently ignored (a success
    response will be returned) to avoid disclosing existing users

    Args:
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    return sync_detailed(
        username=username,
        client=client,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: Client,
) -> Response[Union[Any, ApiResponse]]:
    """Send a password reset code by email

     You must configure an SMTP server, the account must have a valid email address and must not have the
    \"reset-password-disabled\" restriction, in which case SFTPGo will send a code via email to reset
    the password. If the specified user does not exist, the request will be silently ignored (a success
    response will be returned) to avoid disclosing existing users

    Args:
        username (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: Client,
) -> Optional[Union[Any, ApiResponse]]:
    """Send a password reset code by email

     You must configure an SMTP server, the account must have a valid email address and must not have the
    \"reset-password-disabled\" restriction, in which case SFTPGo will send a code via email to reset
    the password. If the specified user does not exist, the request will be silently ignored (a success
    response will be returned) to avoid disclosing existing users

    Args:
        username (str):

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
        )
    ).parsed
