from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_response import ApiResponse
from ...models.upload_to_share_multipart_data import UploadToShareMultipartData
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadToShareMultipartData,
) -> Dict[str, Any]:
    url = "{}/shares/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
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
    id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadToShareMultipartData,
) -> Response[Union[Any, List["ApiResponse"]]]:
    """Upload one or more files to the shared path

     The share must be defined with the write scope and the associated user must have the upload
    permission

    Args:
        id (str):
        multipart_data (UploadToShareMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ApiResponse']]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadToShareMultipartData,
) -> Optional[Union[Any, List["ApiResponse"]]]:
    """Upload one or more files to the shared path

     The share must be defined with the write scope and the associated user must have the upload
    permission

    Args:
        id (str):
        multipart_data (UploadToShareMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ApiResponse']]]
    """

    return sync_detailed(
        id=id,
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadToShareMultipartData,
) -> Response[Union[Any, List["ApiResponse"]]]:
    """Upload one or more files to the shared path

     The share must be defined with the write scope and the associated user must have the upload
    permission

    Args:
        id (str):
        multipart_data (UploadToShareMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ApiResponse']]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    multipart_data: UploadToShareMultipartData,
) -> Optional[Union[Any, List["ApiResponse"]]]:
    """Upload one or more files to the shared path

     The share must be defined with the write scope and the associated user must have the upload
    permission

    Args:
        id (str):
        multipart_data (UploadToShareMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ApiResponse']]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
