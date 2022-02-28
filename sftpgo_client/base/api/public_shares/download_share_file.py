from typing import Any, Dict, Union

import httpx

from ...client import AuthenticatedClient
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    path: str,
    inline: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/shares/{id}/files".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["path"] = path

    params["inline"] = inline

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    path: str,
    inline: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Download a single file

     Returns the file contents as response body. The share must have exactly one path defined and it must
    be a directory for this to work

    Args:
        id (str):
        path (str):
        inline (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        path=path,
        inline=inline,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    path: str,
    inline: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Download a single file

     Returns the file contents as response body. The share must have exactly one path defined and it must
    be a directory for this to work

    Args:
        id (str):
        path (str):
        inline (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        path=path,
        inline=inline,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
