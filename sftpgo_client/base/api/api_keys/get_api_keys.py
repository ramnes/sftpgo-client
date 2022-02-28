from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.api_key import APIKey
from ...models.get_api_keys_order import GetApiKeysOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
    order: Union[Unset, None, GetApiKeysOrder] = UNSET,
) -> Dict[str, Any]:
    url = "{}/apikeys".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[APIKey]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = APIKey.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[APIKey]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
    order: Union[Unset, None, GetApiKeysOrder] = UNSET,
) -> Response[Union[Any, List[APIKey]]]:
    """Get API keys

     Returns an array with one or more API keys. For security reasons hashed keys are omitted in the
    response

    Args:
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 100.
        order (Union[Unset, None, GetApiKeysOrder]):  Example: ASC.

    Returns:
        Response[Union[Any, List[APIKey]]]
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

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
    order: Union[Unset, None, GetApiKeysOrder] = UNSET,
) -> Optional[Union[Any, List[APIKey]]]:
    """Get API keys

     Returns an array with one or more API keys. For security reasons hashed keys are omitted in the
    response

    Args:
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 100.
        order (Union[Unset, None, GetApiKeysOrder]):  Example: ASC.

    Returns:
        Response[Union[Any, List[APIKey]]]
    """

    return sync_detailed(
        client=client,
        offset=offset,
        limit=limit,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
    order: Union[Unset, None, GetApiKeysOrder] = UNSET,
) -> Response[Union[Any, List[APIKey]]]:
    """Get API keys

     Returns an array with one or more API keys. For security reasons hashed keys are omitted in the
    response

    Args:
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 100.
        order (Union[Unset, None, GetApiKeysOrder]):  Example: ASC.

    Returns:
        Response[Union[Any, List[APIKey]]]
    """

    kwargs = _get_kwargs(
        client=client,
        offset=offset,
        limit=limit,
        order=order,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 100,
    order: Union[Unset, None, GetApiKeysOrder] = UNSET,
) -> Optional[Union[Any, List[APIKey]]]:
    """Get API keys

     Returns an array with one or more API keys. For security reasons hashed keys are omitted in the
    response

    Args:
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 100.
        order (Union[Unset, None, GetApiKeysOrder]):  Example: ASC.

    Returns:
        Response[Union[Any, List[APIKey]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            offset=offset,
            limit=limit,
            order=order,
        )
    ).parsed
