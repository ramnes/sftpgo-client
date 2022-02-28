from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.api_response import ApiResponse
from ...types import Response


def _get_kwargs(
    username: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/metadata/users/{username}/check".format(
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ApiResponse]]:
    if response.status_code == 202:
        response_202 = ApiResponse.from_dict(response.json())

        return response_202
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
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
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
) -> Response[Union[Any, ApiResponse]]:
    """Start a metadata check

     Starts a new metadata check for the given user. A metadata check requires a metadata plugin and
    removes the metadata associated to missing items (for example objects deleted outside SFTPGo). If a
    metadata check for this user is already active a 409 status code is returned. Metadata are stored
    for cloud storage backends. This API does nothing for other backends or if no metadata plugin is
    configured

    Args:
        username (str):

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

    return _build_response(response=response)


def sync(
    username: str,
    *,
    client: Client,
) -> Optional[Union[Any, ApiResponse]]:
    """Start a metadata check

     Starts a new metadata check for the given user. A metadata check requires a metadata plugin and
    removes the metadata associated to missing items (for example objects deleted outside SFTPGo). If a
    metadata check for this user is already active a 409 status code is returned. Metadata are stored
    for cloud storage backends. This API does nothing for other backends or if no metadata plugin is
    configured

    Args:
        username (str):

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
    """Start a metadata check

     Starts a new metadata check for the given user. A metadata check requires a metadata plugin and
    removes the metadata associated to missing items (for example objects deleted outside SFTPGo). If a
    metadata check for this user is already active a 409 status code is returned. Metadata are stored
    for cloud storage backends. This API does nothing for other backends or if no metadata plugin is
    configured

    Args:
        username (str):

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    username: str,
    *,
    client: Client,
) -> Optional[Union[Any, ApiResponse]]:
    """Start a metadata check

     Starts a new metadata check for the given user. A metadata check requires a metadata plugin and
    removes the metadata associated to missing items (for example objects deleted outside SFTPGo). If a
    metadata check for this user is already active a 409 status code is returned. Metadata are stored
    for cloud storage backends. This API does nothing for other backends or if no metadata plugin is
    configured

    Args:
        username (str):

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
        )
    ).parsed
