from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.add_api_key_response_201 import AddApiKeyResponse201
from ...models.api_key import APIKey
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: APIKey,
) -> Dict[str, Any]:
    url = "{}/apikeys".format(client.base_url)

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
) -> Optional[Union[AddApiKeyResponse201, Any]]:
    if response.status_code == 201:
        response_201 = AddApiKeyResponse201.from_dict(response.json())

        return response_201
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
) -> Response[Union[AddApiKeyResponse201, Any]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: APIKey,
) -> Response[Union[AddApiKeyResponse201, Any]]:
    """Add API key

     Adds a new API key

    Args:
        json_body (APIKey):

    Returns:
        Response[Union[AddApiKeyResponse201, Any]]
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
    json_body: APIKey,
) -> Optional[Union[AddApiKeyResponse201, Any]]:
    """Add API key

     Adds a new API key

    Args:
        json_body (APIKey):

    Returns:
        Response[Union[AddApiKeyResponse201, Any]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: APIKey,
) -> Response[Union[AddApiKeyResponse201, Any]]:
    """Add API key

     Adds a new API key

    Args:
        json_body (APIKey):

    Returns:
        Response[Union[AddApiKeyResponse201, Any]]
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
    json_body: APIKey,
) -> Optional[Union[AddApiKeyResponse201, Any]]:
    """Add API key

     Adds a new API key

    Args:
        json_body (APIKey):

    Returns:
        Response[Union[AddApiKeyResponse201, Any]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
