from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.api_response import ApiResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    path: str,
    mkdir_parents: Union[Unset, None, bool] = UNSET,
    x_sftpgo_mtime: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/user/files/upload".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_sftpgo_mtime, Unset):
        headers["X-SFTPGO-MTIME"] = str(x_sftpgo_mtime)

    params: Dict[str, Any] = {}
    params["path"] = path

    params["mkdir_parents"] = mkdir_parents

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, List[ApiResponse]]]:
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = ApiResponse.from_dict(response_201_item_data)

            response_201.append(response_201_item)

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
    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, List[ApiResponse]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    path: str,
    mkdir_parents: Union[Unset, None, bool] = UNSET,
    x_sftpgo_mtime: Union[Unset, int] = UNSET,
) -> Response[Union[Any, List[ApiResponse]]]:
    """Upload a single file

     Upload a single file for the logged in user to an existing directory. This API does not use
    multipart/form-data and so no temporary files are created server side but only a single file can be
    uploaded as POST body

    Args:
        path (str):
        mkdir_parents (Union[Unset, None, bool]):
        x_sftpgo_mtime (Union[Unset, int]):

    Returns:
        Response[Union[Any, List[ApiResponse]]]
    """

    kwargs = _get_kwargs(
        client=client,
        path=path,
        mkdir_parents=mkdir_parents,
        x_sftpgo_mtime=x_sftpgo_mtime,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    path: str,
    mkdir_parents: Union[Unset, None, bool] = UNSET,
    x_sftpgo_mtime: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, List[ApiResponse]]]:
    """Upload a single file

     Upload a single file for the logged in user to an existing directory. This API does not use
    multipart/form-data and so no temporary files are created server side but only a single file can be
    uploaded as POST body

    Args:
        path (str):
        mkdir_parents (Union[Unset, None, bool]):
        x_sftpgo_mtime (Union[Unset, int]):

    Returns:
        Response[Union[Any, List[ApiResponse]]]
    """

    return sync_detailed(
        client=client,
        path=path,
        mkdir_parents=mkdir_parents,
        x_sftpgo_mtime=x_sftpgo_mtime,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    path: str,
    mkdir_parents: Union[Unset, None, bool] = UNSET,
    x_sftpgo_mtime: Union[Unset, int] = UNSET,
) -> Response[Union[Any, List[ApiResponse]]]:
    """Upload a single file

     Upload a single file for the logged in user to an existing directory. This API does not use
    multipart/form-data and so no temporary files are created server side but only a single file can be
    uploaded as POST body

    Args:
        path (str):
        mkdir_parents (Union[Unset, None, bool]):
        x_sftpgo_mtime (Union[Unset, int]):

    Returns:
        Response[Union[Any, List[ApiResponse]]]
    """

    kwargs = _get_kwargs(
        client=client,
        path=path,
        mkdir_parents=mkdir_parents,
        x_sftpgo_mtime=x_sftpgo_mtime,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    path: str,
    mkdir_parents: Union[Unset, None, bool] = UNSET,
    x_sftpgo_mtime: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, List[ApiResponse]]]:
    """Upload a single file

     Upload a single file for the logged in user to an existing directory. This API does not use
    multipart/form-data and so no temporary files are created server side but only a single file can be
    uploaded as POST body

    Args:
        path (str):
        mkdir_parents (Union[Unset, None, bool]):
        x_sftpgo_mtime (Union[Unset, int]):

    Returns:
        Response[Union[Any, List[ApiResponse]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            path=path,
            mkdir_parents=mkdir_parents,
            x_sftpgo_mtime=x_sftpgo_mtime,
        )
    ).parsed
