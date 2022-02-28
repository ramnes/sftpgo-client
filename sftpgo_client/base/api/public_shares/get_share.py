from typing import Any, Dict, Union

import httpx

from ...client import AuthenticatedClient
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    compress: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/shares/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["compress"] = compress

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
    compress: Union[Unset, None, bool] = True,
) -> Response[Any]:
    """Download shared files and folders as a single zip file

     A zip file, containing the shared files and folders, will be generated on the fly and returned as
    response body. Only folders and regular files will be included in the zip. The share must be defined
    with the read scope and the associated user must have list and download permissions

    Args:
        id (str):
        compress (Union[Unset, None, bool]):  Default: True.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        compress=compress,
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
    compress: Union[Unset, None, bool] = True,
) -> Response[Any]:
    """Download shared files and folders as a single zip file

     A zip file, containing the shared files and folders, will be generated on the fly and returned as
    response body. Only folders and regular files will be included in the zip. The share must be defined
    with the read scope and the associated user must have list and download permissions

    Args:
        id (str):
        compress (Union[Unset, None, bool]):  Default: True.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        compress=compress,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
