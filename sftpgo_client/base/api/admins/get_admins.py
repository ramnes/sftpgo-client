from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.admin import Admin
from ...models.get_admins_order import GetAdminsOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetAdminsOrder] = UNSET,
) -> Dict[str, Any]:
    url = "{}/admins".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params: Dict[str, Any] = {
        "offset": offset,
        "limit": limit,
        "order": json_order,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[List[Admin], None, None, None, None]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Admin.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[List[Admin], None, None, None, None]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetAdminsOrder] = UNSET,
) -> Response[Union[List[Admin], None, None, None, None]]:
    kwargs = _get_kwargs(
        client=client,
        offset=offset,
        limit=limit,
        order=order,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetAdminsOrder] = UNSET,
) -> Optional[Union[List[Admin], None, None, None, None]]:
    """Returns an array with one or more admins. For security reasons hashed passwords are omitted in the response"""

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetAdminsOrder] = UNSET,
) -> Response[Union[List[Admin], None, None, None, None]]:
    kwargs = _get_kwargs(
        client=client,
        offset=offset,
        limit=limit,
        order=order,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    offset: Union[Unset, int] = 0,
    limit: Union[Unset, int] = 100,
    order: Union[Unset, GetAdminsOrder] = UNSET,
) -> Optional[Union[List[Admin], None, None, None, None]]:
    """Returns an array with one or more admins. For security reasons hashed passwords are omitted in the response"""

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            order=order,
        )
    ).parsed
