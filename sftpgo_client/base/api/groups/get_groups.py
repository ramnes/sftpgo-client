from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.get_groups_order import GetGroupsOrder
from ...models.group import Group
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
    order: Union[Unset, None, GetGroupsOrder] = UNSET,
) -> Dict[str, Any]:
    url = "{}/groups".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["offset"] = offset

    params["limit"] = limit

    json_order: Union[Unset, None, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value if order else None

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, List["Group"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Group.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, List["Group"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
    order: Union[Unset, None, GetGroupsOrder] = UNSET,
) -> Response[Union[Any, List["Group"]]]:
    """Get groups

     Returns an array with one or more groups

    Args:
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 100.
        order (Union[Unset, None, GetGroupsOrder]):  Example: ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['Group']]]
    """

    kwargs = _get_kwargs(
        client=client,
        offset=offset,
        limit=limit,
        order=order,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
    order: Union[Unset, None, GetGroupsOrder] = UNSET,
) -> Optional[Union[Any, List["Group"]]]:
    """Get groups

     Returns an array with one or more groups

    Args:
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 100.
        order (Union[Unset, None, GetGroupsOrder]):  Example: ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['Group']]]
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
    order: Union[Unset, None, GetGroupsOrder] = UNSET,
) -> Response[Union[Any, List["Group"]]]:
    """Get groups

     Returns an array with one or more groups

    Args:
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 100.
        order (Union[Unset, None, GetGroupsOrder]):  Example: ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['Group']]]
    """

    kwargs = _get_kwargs(
        client=client,
        offset=offset,
        limit=limit,
        order=order,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
    order: Union[Unset, None, GetGroupsOrder] = UNSET,
) -> Optional[Union[Any, List["Group"]]]:
    """Get groups

     Returns an array with one or more groups

    Args:
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 100.
        order (Union[Unset, None, GetGroupsOrder]):  Example: ASC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['Group']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            order=order,
        )
    ).parsed
