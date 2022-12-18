from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.token import Token
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    x_sftpgo_otp: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/user/token".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_sftpgo_otp, Unset):
        headers["X-SFTPGO-OTP"] = x_sftpgo_otp

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, Token]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Token.from_dict(response.json())

        return response_200
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
) -> Response[Union[Any, Token]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    x_sftpgo_otp: Union[Unset, str] = UNSET,
) -> Response[Union[Any, Token]]:
    """Get a new user access token

     Returns an access token and its expiration

    Args:
        x_sftpgo_otp (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Token]]
    """

    kwargs = _get_kwargs(
        client=client,
        x_sftpgo_otp=x_sftpgo_otp,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    x_sftpgo_otp: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, Token]]:
    """Get a new user access token

     Returns an access token and its expiration

    Args:
        x_sftpgo_otp (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Token]]
    """

    return sync_detailed(
        client=client,
        x_sftpgo_otp=x_sftpgo_otp,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    x_sftpgo_otp: Union[Unset, str] = UNSET,
) -> Response[Union[Any, Token]]:
    """Get a new user access token

     Returns an access token and its expiration

    Args:
        x_sftpgo_otp (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Token]]
    """

    kwargs = _get_kwargs(
        client=client,
        x_sftpgo_otp=x_sftpgo_otp,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    x_sftpgo_otp: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, Token]]:
    """Get a new user access token

     Returns an access token and its expiration

    Args:
        x_sftpgo_otp (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Token]]
    """

    return (
        await asyncio_detailed(
            client=client,
            x_sftpgo_otp=x_sftpgo_otp,
        )
    ).parsed
