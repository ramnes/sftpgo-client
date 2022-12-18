from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.api_response import ApiResponse
from ...models.create_user_files_multipart_data import CreateUserFilesMultipartData
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    multipart_data: CreateUserFilesMultipartData,
    path: Union[Unset, None, str] = UNSET,
    mkdir_parents: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/user/files".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["path"] = path

    params["mkdir_parents"] = mkdir_parents

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, List["ApiResponse"]]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = ApiResponse.from_dict(response_201_item_data)

            response_201.append(response_201_item)

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = cast(Any, None)
        return response_413
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, List["ApiResponse"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    multipart_data: CreateUserFilesMultipartData,
    path: Union[Unset, None, str] = UNSET,
    mkdir_parents: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, List["ApiResponse"]]]:
    """Upload files

     Upload one or more files for the logged in user

    Args:
        path (Union[Unset, None, str]):
        mkdir_parents (Union[Unset, None, bool]):
        multipart_data (CreateUserFilesMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ApiResponse']]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        path=path,
        mkdir_parents=mkdir_parents,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    multipart_data: CreateUserFilesMultipartData,
    path: Union[Unset, None, str] = UNSET,
    mkdir_parents: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, List["ApiResponse"]]]:
    """Upload files

     Upload one or more files for the logged in user

    Args:
        path (Union[Unset, None, str]):
        mkdir_parents (Union[Unset, None, bool]):
        multipart_data (CreateUserFilesMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ApiResponse']]]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
        path=path,
        mkdir_parents=mkdir_parents,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    multipart_data: CreateUserFilesMultipartData,
    path: Union[Unset, None, str] = UNSET,
    mkdir_parents: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, List["ApiResponse"]]]:
    """Upload files

     Upload one or more files for the logged in user

    Args:
        path (Union[Unset, None, str]):
        mkdir_parents (Union[Unset, None, bool]):
        multipart_data (CreateUserFilesMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ApiResponse']]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        path=path,
        mkdir_parents=mkdir_parents,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    multipart_data: CreateUserFilesMultipartData,
    path: Union[Unset, None, str] = UNSET,
    mkdir_parents: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, List["ApiResponse"]]]:
    """Upload files

     Upload one or more files for the logged in user

    Args:
        path (Union[Unset, None, str]):
        mkdir_parents (Union[Unset, None, bool]):
        multipart_data (CreateUserFilesMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ApiResponse']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
            path=path,
            mkdir_parents=mkdir_parents,
        )
    ).parsed
