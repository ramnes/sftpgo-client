from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.admin_reset_password_json_body import AdminResetPasswordJsonBody
from ...models.api_response import ApiResponse
from ...types import Response


def _get_kwargs(
    username: str,
    *,
    client: Client,
    json_body: AdminResetPasswordJsonBody,
) -> Dict[str, Any]:
    url = "{}/admins/{username}/reset-password".format(
        client.base_url, username=username
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ApiResponse]]:
    if response.status_code == 200:
        response_200 = ApiResponse.from_dict(response.json())

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
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ApiResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: Client,
    json_body: AdminResetPasswordJsonBody,
) -> Response[Union[Any, ApiResponse]]:
    """Reset the password

     Set a new password using the code received via email

    Args:
        username (str):
        json_body (AdminResetPasswordJsonBody):

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    username: str,
    *,
    client: Client,
    json_body: AdminResetPasswordJsonBody,
) -> Optional[Union[Any, ApiResponse]]:
    """Reset the password

     Set a new password using the code received via email

    Args:
        username (str):
        json_body (AdminResetPasswordJsonBody):

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    return sync_detailed(
        username=username,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: Client,
    json_body: AdminResetPasswordJsonBody,
) -> Response[Union[Any, ApiResponse]]:
    """Reset the password

     Set a new password using the code received via email

    Args:
        username (str):
        json_body (AdminResetPasswordJsonBody):

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    username: str,
    *,
    client: Client,
    json_body: AdminResetPasswordJsonBody,
) -> Optional[Union[Any, ApiResponse]]:
    """Reset the password

     Set a new password using the code received via email

    Args:
        username (str):
        json_body (AdminResetPasswordJsonBody):

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            json_body=json_body,
        )
    ).parsed
