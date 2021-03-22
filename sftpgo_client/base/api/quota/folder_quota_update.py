from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.api_response import ApiResponse
from ...models.base_virtual_folder import BaseVirtualFolder
from ...models.folder_quota_update_mode import FolderQuotaUpdateMode
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: BaseVirtualFolder,
    mode: Union[Unset, FolderQuotaUpdateMode] = UNSET,
) -> Dict[str, Any]:
    url = "{}/folder-quota-update".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_mode: Union[Unset, str] = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode.value

    params: Dict[str, Any] = {
        "mode": json_mode,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[ApiResponse, None, None, None, None, None, None]]:
    if response.status_code == 200:
        response_200 = ApiResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = None

        return response_400
    if response.status_code == 401:
        response_401 = None

        return response_401
    if response.status_code == 403:
        response_403 = None

        return response_403
    if response.status_code == 404:
        response_404 = None

        return response_404
    if response.status_code == 409:
        response_409 = None

        return response_409
    if response.status_code == 500:
        response_500 = None

        return response_500
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[ApiResponse, None, None, None, None, None, None]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: BaseVirtualFolder,
    mode: Union[Unset, FolderQuotaUpdateMode] = UNSET,
) -> Response[Union[ApiResponse, None, None, None, None, None, None]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        mode=mode,
    )

    response = httpx.put(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: BaseVirtualFolder,
    mode: Union[Unset, FolderQuotaUpdateMode] = UNSET,
) -> Optional[Union[ApiResponse, None, None, None, None, None, None]]:
    """ Sets the current used quota limits for the given folder """

    return sync_detailed(
        client=client,
        json_body=json_body,
        mode=mode,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: BaseVirtualFolder,
    mode: Union[Unset, FolderQuotaUpdateMode] = UNSET,
) -> Response[Union[ApiResponse, None, None, None, None, None, None]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        mode=mode,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.put(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: BaseVirtualFolder,
    mode: Union[Unset, FolderQuotaUpdateMode] = UNSET,
) -> Optional[Union[ApiResponse, None, None, None, None, None, None]]:
    """ Sets the current used quota limits for the given folder """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            mode=mode,
        )
    ).parsed
