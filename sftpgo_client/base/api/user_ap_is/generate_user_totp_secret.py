from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.generate_user_totp_secret_json_body import GenerateUserTotpSecretJsonBody
from ...models.generate_user_totp_secret_response_200 import (
    GenerateUserTotpSecretResponse200,
)
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: GenerateUserTotpSecretJsonBody,
) -> Dict[str, Any]:
    url = "{}/user/totp/generate".format(client.base_url)

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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, GenerateUserTotpSecretResponse200]]:
    if response.status_code == 200:
        response_200 = GenerateUserTotpSecretResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GenerateUserTotpSecretResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: GenerateUserTotpSecretJsonBody,
) -> Response[Union[Any, GenerateUserTotpSecretResponse200]]:
    """Generate a new TOTP secret

     Generates a new TOTP secret, including the QR code as png, using the specified configuration for the
    logged in user

    Args:
        json_body (GenerateUserTotpSecretJsonBody):

    Returns:
        Response[Union[Any, GenerateUserTotpSecretResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: GenerateUserTotpSecretJsonBody,
) -> Optional[Union[Any, GenerateUserTotpSecretResponse200]]:
    """Generate a new TOTP secret

     Generates a new TOTP secret, including the QR code as png, using the specified configuration for the
    logged in user

    Args:
        json_body (GenerateUserTotpSecretJsonBody):

    Returns:
        Response[Union[Any, GenerateUserTotpSecretResponse200]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: GenerateUserTotpSecretJsonBody,
) -> Response[Union[Any, GenerateUserTotpSecretResponse200]]:
    """Generate a new TOTP secret

     Generates a new TOTP secret, including the QR code as png, using the specified configuration for the
    logged in user

    Args:
        json_body (GenerateUserTotpSecretJsonBody):

    Returns:
        Response[Union[Any, GenerateUserTotpSecretResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: GenerateUserTotpSecretJsonBody,
) -> Optional[Union[Any, GenerateUserTotpSecretResponse200]]:
    """Generate a new TOTP secret

     Generates a new TOTP secret, including the QR code as png, using the specified configuration for the
    logged in user

    Args:
        json_body (GenerateUserTotpSecretJsonBody):

    Returns:
        Response[Union[Any, GenerateUserTotpSecretResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
