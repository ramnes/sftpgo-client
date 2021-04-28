from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.api_response import ApiResponse
from ...models.backup_data import BackupData
from ...models.loaddata_from_request_body_mode import LoaddataFromRequestBodyMode
from ...models.loaddata_from_request_body_scan_quota import (
    LoaddataFromRequestBodyScanQuota,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: BackupData,
    scan_quota: Union[Unset, LoaddataFromRequestBodyScanQuota] = UNSET,
    mode: Union[Unset, LoaddataFromRequestBodyMode] = UNSET,
) -> Dict[str, Any]:
    url = "{}/loaddata".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_scan_quota: Union[Unset, int] = UNSET
    if not isinstance(scan_quota, Unset):
        json_scan_quota = scan_quota.value

    json_mode: Union[Unset, int] = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode.value

    params: Dict[str, Any] = {
        "scan-quota": json_scan_quota,
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
) -> Optional[Union[ApiResponse, None, None, None, None]]:
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
    if response.status_code == 500:
        response_500 = None

        return response_500
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[ApiResponse, None, None, None, None]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: BackupData,
    scan_quota: Union[Unset, LoaddataFromRequestBodyScanQuota] = UNSET,
    mode: Union[Unset, LoaddataFromRequestBodyMode] = UNSET,
) -> Response[Union[ApiResponse, None, None, None, None]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        scan_quota=scan_quota,
        mode=mode,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: BackupData,
    scan_quota: Union[Unset, LoaddataFromRequestBodyScanQuota] = UNSET,
    mode: Union[Unset, LoaddataFromRequestBodyMode] = UNSET,
) -> Optional[Union[ApiResponse, None, None, None, None]]:
    """Restores SFTPGo data from a JSON backup. Users, folders and admins will be restored one by one and the restore is stopped if a user/folder/admin cannot be added or updated, so it could happen a partial restore"""

    return sync_detailed(
        client=client,
        json_body=json_body,
        scan_quota=scan_quota,
        mode=mode,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: BackupData,
    scan_quota: Union[Unset, LoaddataFromRequestBodyScanQuota] = UNSET,
    mode: Union[Unset, LoaddataFromRequestBodyMode] = UNSET,
) -> Response[Union[ApiResponse, None, None, None, None]]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        scan_quota=scan_quota,
        mode=mode,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: BackupData,
    scan_quota: Union[Unset, LoaddataFromRequestBodyScanQuota] = UNSET,
    mode: Union[Unset, LoaddataFromRequestBodyMode] = UNSET,
) -> Optional[Union[ApiResponse, None, None, None, None]]:
    """Restores SFTPGo data from a JSON backup. Users, folders and admins will be restored one by one and the restore is stopped if a user/folder/admin cannot be added or updated, so it could happen a partial restore"""

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            scan_quota=scan_quota,
            mode=mode,
        )
    ).parsed
