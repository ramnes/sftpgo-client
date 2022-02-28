from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Token]]:
    if response.status_code == 200:
        response_200 = Token.from_dict(response.json())

        return response_200
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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Token]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
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

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    x_sftpgo_otp: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, Token]]:
    """Get a new user access token

     Returns an access token and its expiration

    Args:
        x_sftpgo_otp (Union[Unset, str]):

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

    Returns:
        Response[Union[Any, Token]]
    """

    kwargs = _get_kwargs(
        client=client,
        x_sftpgo_otp=x_sftpgo_otp,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    x_sftpgo_otp: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, Token]]:
    """Get a new user access token

     Returns an access token and its expiration

    Args:
        x_sftpgo_otp (Union[Unset, str]):

    Returns:
        Response[Union[Any, Token]]
    """

    return (
        await asyncio_detailed(
            client=client,
            x_sftpgo_otp=x_sftpgo_otp,
        )
    ).parsed
