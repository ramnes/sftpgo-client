from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.api_response import ApiResponse
from ...models.create_user_files_multipart_data import CreateUserFilesMultipartData
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    multipart_data: CreateUserFilesMultipartData,
    path: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/user/files".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "path": path,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
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
    multipart_data: CreateUserFilesMultipartData,
    path: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List[ApiResponse]]]:
    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        path=path,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    multipart_data: CreateUserFilesMultipartData,
    path: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List[ApiResponse]]]:
    """Upload one or more files for the logged in user"""

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
        path=path,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    multipart_data: CreateUserFilesMultipartData,
    path: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List[ApiResponse]]]:
    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        path=path,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    multipart_data: CreateUserFilesMultipartData,
    path: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List[ApiResponse]]]:
    """Upload one or more files for the logged in user"""

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
            path=path,
        )
    ).parsed
