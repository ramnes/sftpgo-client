from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.get_provider_events_order import GetProviderEventsOrder
from ...models.provider_event import ProviderEvent
from ...models.provider_event_action import ProviderEventAction
from ...models.provider_event_object_type import ProviderEventObjectType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    start_timestamp: Union[Unset, None, int] = 0,
    end_timestamp: Union[Unset, None, int] = 0,
    actions: Union[Unset, None, List[ProviderEventAction]] = UNSET,
    username: Union[Unset, None, str] = UNSET,
    ip: Union[Unset, None, str] = UNSET,
    object_name: Union[Unset, None, str] = UNSET,
    object_types: Union[Unset, None, List[ProviderEventObjectType]] = UNSET,
    instance_ids: Union[Unset, None, List[str]] = UNSET,
    exclude_ids: Union[Unset, None, List[str]] = UNSET,
    role: Union[Unset, None, str] = UNSET,
    csv_export: Union[Unset, None, bool] = False,
    omit_object_data: Union[Unset, None, bool] = False,
    limit: Union[Unset, None, int] = 100,
    order: Union[Unset, None, GetProviderEventsOrder] = UNSET,
) -> Dict[str, Any]:
    url = "{}/events/provider".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["start_timestamp"] = start_timestamp

    params["end_timestamp"] = end_timestamp

    json_actions: Union[Unset, None, List[str]] = UNSET
    if not isinstance(actions, Unset):
        if actions is None:
            json_actions = None
        else:
            json_actions = []
            for actions_item_data in actions:
                actions_item = actions_item_data.value

                json_actions.append(actions_item)

    params["actions"] = json_actions

    params["username"] = username

    params["ip"] = ip

    params["object_name"] = object_name

    json_object_types: Union[Unset, None, List[str]] = UNSET
    if not isinstance(object_types, Unset):
        if object_types is None:
            json_object_types = None
        else:
            json_object_types = []
            for object_types_item_data in object_types:
                object_types_item = object_types_item_data.value

                json_object_types.append(object_types_item)

    params["object_types"] = json_object_types

    json_instance_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(instance_ids, Unset):
        if instance_ids is None:
            json_instance_ids = None
        else:
            json_instance_ids = instance_ids

    params["instance_ids"] = json_instance_ids

    json_exclude_ids: Union[Unset, None, List[str]] = UNSET
    if not isinstance(exclude_ids, Unset):
        if exclude_ids is None:
            json_exclude_ids = None
        else:
            json_exclude_ids = exclude_ids

    params["exclude_ids"] = json_exclude_ids

    params["role"] = role

    params["csv_export"] = csv_export

    params["omit_object_data"] = omit_object_data

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
) -> Optional[Union[Any, List["ProviderEvent"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProviderEvent.from_dict(response_200_item_data)

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
) -> Response[Union[Any, List["ProviderEvent"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    start_timestamp: Union[Unset, None, int] = 0,
    end_timestamp: Union[Unset, None, int] = 0,
    actions: Union[Unset, None, List[ProviderEventAction]] = UNSET,
    username: Union[Unset, None, str] = UNSET,
    ip: Union[Unset, None, str] = UNSET,
    object_name: Union[Unset, None, str] = UNSET,
    object_types: Union[Unset, None, List[ProviderEventObjectType]] = UNSET,
    instance_ids: Union[Unset, None, List[str]] = UNSET,
    exclude_ids: Union[Unset, None, List[str]] = UNSET,
    role: Union[Unset, None, str] = UNSET,
    csv_export: Union[Unset, None, bool] = False,
    omit_object_data: Union[Unset, None, bool] = False,
    limit: Union[Unset, None, int] = 100,
    order: Union[Unset, None, GetProviderEventsOrder] = UNSET,
) -> Response[Union[Any, List["ProviderEvent"]]]:
    """Get provider events

     Returns an array with one or more provider events applying the specified filters. This API is only
    available if you configure an \"eventsearcher\" plugin

    Args:
        start_timestamp (Union[Unset, None, int]):
        end_timestamp (Union[Unset, None, int]):
        actions (Union[Unset, None, List[ProviderEventAction]]):
        username (Union[Unset, None, str]):
        ip (Union[Unset, None, str]):
        object_name (Union[Unset, None, str]):
        object_types (Union[Unset, None, List[ProviderEventObjectType]]):
        instance_ids (Union[Unset, None, List[str]]):
        exclude_ids (Union[Unset, None, List[str]]):
        role (Union[Unset, None, str]):
        csv_export (Union[Unset, None, bool]):
        omit_object_data (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):  Default: 100.
        order (Union[Unset, None, GetProviderEventsOrder]):  Example: DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ProviderEvent']]]
    """

    kwargs = _get_kwargs(
        client=client,
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        actions=actions,
        username=username,
        ip=ip,
        object_name=object_name,
        object_types=object_types,
        instance_ids=instance_ids,
        exclude_ids=exclude_ids,
        role=role,
        csv_export=csv_export,
        omit_object_data=omit_object_data,
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
    start_timestamp: Union[Unset, None, int] = 0,
    end_timestamp: Union[Unset, None, int] = 0,
    actions: Union[Unset, None, List[ProviderEventAction]] = UNSET,
    username: Union[Unset, None, str] = UNSET,
    ip: Union[Unset, None, str] = UNSET,
    object_name: Union[Unset, None, str] = UNSET,
    object_types: Union[Unset, None, List[ProviderEventObjectType]] = UNSET,
    instance_ids: Union[Unset, None, List[str]] = UNSET,
    exclude_ids: Union[Unset, None, List[str]] = UNSET,
    role: Union[Unset, None, str] = UNSET,
    csv_export: Union[Unset, None, bool] = False,
    omit_object_data: Union[Unset, None, bool] = False,
    limit: Union[Unset, None, int] = 100,
    order: Union[Unset, None, GetProviderEventsOrder] = UNSET,
) -> Optional[Union[Any, List["ProviderEvent"]]]:
    """Get provider events

     Returns an array with one or more provider events applying the specified filters. This API is only
    available if you configure an \"eventsearcher\" plugin

    Args:
        start_timestamp (Union[Unset, None, int]):
        end_timestamp (Union[Unset, None, int]):
        actions (Union[Unset, None, List[ProviderEventAction]]):
        username (Union[Unset, None, str]):
        ip (Union[Unset, None, str]):
        object_name (Union[Unset, None, str]):
        object_types (Union[Unset, None, List[ProviderEventObjectType]]):
        instance_ids (Union[Unset, None, List[str]]):
        exclude_ids (Union[Unset, None, List[str]]):
        role (Union[Unset, None, str]):
        csv_export (Union[Unset, None, bool]):
        omit_object_data (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):  Default: 100.
        order (Union[Unset, None, GetProviderEventsOrder]):  Example: DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ProviderEvent']]]
    """

    return sync_detailed(
        client=client,
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        actions=actions,
        username=username,
        ip=ip,
        object_name=object_name,
        object_types=object_types,
        instance_ids=instance_ids,
        exclude_ids=exclude_ids,
        role=role,
        csv_export=csv_export,
        omit_object_data=omit_object_data,
        limit=limit,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    start_timestamp: Union[Unset, None, int] = 0,
    end_timestamp: Union[Unset, None, int] = 0,
    actions: Union[Unset, None, List[ProviderEventAction]] = UNSET,
    username: Union[Unset, None, str] = UNSET,
    ip: Union[Unset, None, str] = UNSET,
    object_name: Union[Unset, None, str] = UNSET,
    object_types: Union[Unset, None, List[ProviderEventObjectType]] = UNSET,
    instance_ids: Union[Unset, None, List[str]] = UNSET,
    exclude_ids: Union[Unset, None, List[str]] = UNSET,
    role: Union[Unset, None, str] = UNSET,
    csv_export: Union[Unset, None, bool] = False,
    omit_object_data: Union[Unset, None, bool] = False,
    limit: Union[Unset, None, int] = 100,
    order: Union[Unset, None, GetProviderEventsOrder] = UNSET,
) -> Response[Union[Any, List["ProviderEvent"]]]:
    """Get provider events

     Returns an array with one or more provider events applying the specified filters. This API is only
    available if you configure an \"eventsearcher\" plugin

    Args:
        start_timestamp (Union[Unset, None, int]):
        end_timestamp (Union[Unset, None, int]):
        actions (Union[Unset, None, List[ProviderEventAction]]):
        username (Union[Unset, None, str]):
        ip (Union[Unset, None, str]):
        object_name (Union[Unset, None, str]):
        object_types (Union[Unset, None, List[ProviderEventObjectType]]):
        instance_ids (Union[Unset, None, List[str]]):
        exclude_ids (Union[Unset, None, List[str]]):
        role (Union[Unset, None, str]):
        csv_export (Union[Unset, None, bool]):
        omit_object_data (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):  Default: 100.
        order (Union[Unset, None, GetProviderEventsOrder]):  Example: DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ProviderEvent']]]
    """

    kwargs = _get_kwargs(
        client=client,
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        actions=actions,
        username=username,
        ip=ip,
        object_name=object_name,
        object_types=object_types,
        instance_ids=instance_ids,
        exclude_ids=exclude_ids,
        role=role,
        csv_export=csv_export,
        omit_object_data=omit_object_data,
        limit=limit,
        order=order,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    start_timestamp: Union[Unset, None, int] = 0,
    end_timestamp: Union[Unset, None, int] = 0,
    actions: Union[Unset, None, List[ProviderEventAction]] = UNSET,
    username: Union[Unset, None, str] = UNSET,
    ip: Union[Unset, None, str] = UNSET,
    object_name: Union[Unset, None, str] = UNSET,
    object_types: Union[Unset, None, List[ProviderEventObjectType]] = UNSET,
    instance_ids: Union[Unset, None, List[str]] = UNSET,
    exclude_ids: Union[Unset, None, List[str]] = UNSET,
    role: Union[Unset, None, str] = UNSET,
    csv_export: Union[Unset, None, bool] = False,
    omit_object_data: Union[Unset, None, bool] = False,
    limit: Union[Unset, None, int] = 100,
    order: Union[Unset, None, GetProviderEventsOrder] = UNSET,
) -> Optional[Union[Any, List["ProviderEvent"]]]:
    """Get provider events

     Returns an array with one or more provider events applying the specified filters. This API is only
    available if you configure an \"eventsearcher\" plugin

    Args:
        start_timestamp (Union[Unset, None, int]):
        end_timestamp (Union[Unset, None, int]):
        actions (Union[Unset, None, List[ProviderEventAction]]):
        username (Union[Unset, None, str]):
        ip (Union[Unset, None, str]):
        object_name (Union[Unset, None, str]):
        object_types (Union[Unset, None, List[ProviderEventObjectType]]):
        instance_ids (Union[Unset, None, List[str]]):
        exclude_ids (Union[Unset, None, List[str]]):
        role (Union[Unset, None, str]):
        csv_export (Union[Unset, None, bool]):
        omit_object_data (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]):  Default: 100.
        order (Union[Unset, None, GetProviderEventsOrder]):  Example: DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['ProviderEvent']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            actions=actions,
            username=username,
            ip=ip,
            object_name=object_name,
            object_types=object_types,
            instance_ids=instance_ids,
            exclude_ids=exclude_ids,
            role=role,
            csv_export=csv_export,
            omit_object_data=omit_object_data,
            limit=limit,
            order=order,
        )
    ).parsed
