from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.event_protocols import EventProtocols
from ...models.fs_event import FsEvent
from ...models.fs_event_action import FsEventAction
from ...models.fs_event_status import FsEventStatus
from ...models.fs_providers import FsProviders
from ...models.get_fs_events_order import GetFsEventsOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    start_timestamp: Union[Unset, None, int] = 0,
    end_timestamp: Union[Unset, None, int] = 0,
    actions: Union[Unset, None, List[FsEventAction]] = UNSET,
    username: Union[Unset, None, str] = UNSET,
    ip: Union[Unset, None, str] = UNSET,
    ssh_cmd: Union[Unset, None, str] = UNSET,
    fs_provider: Union[Unset, None, FsProviders] = UNSET,
    bucket: Union[Unset, None, str] = UNSET,
    endpoint: Union[Unset, None, str] = UNSET,
    protocols: Union[Unset, None, List[EventProtocols]] = UNSET,
    statuses: Union[Unset, None, List[FsEventStatus]] = UNSET,
    instance_ids: Union[Unset, None, List[str]] = UNSET,
    exclude_ids: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = 100,
    order: Union[Unset, None, GetFsEventsOrder] = UNSET,
) -> Dict[str, Any]:
    url = "{}/events/fs".format(client.base_url)

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

    params["ssh_cmd"] = ssh_cmd

    json_fs_provider: Union[Unset, None, int] = UNSET
    if not isinstance(fs_provider, Unset):
        json_fs_provider = fs_provider.value if fs_provider else None

    params["fs_provider"] = json_fs_provider

    params["bucket"] = bucket

    params["endpoint"] = endpoint

    json_protocols: Union[Unset, None, List[str]] = UNSET
    if not isinstance(protocols, Unset):
        if protocols is None:
            json_protocols = None
        else:
            json_protocols = []
            for protocols_item_data in protocols:
                protocols_item = protocols_item_data.value

                json_protocols.append(protocols_item)

    params["protocols"] = json_protocols

    json_statuses: Union[Unset, None, List[int]] = UNSET
    if not isinstance(statuses, Unset):
        if statuses is None:
            json_statuses = None
        else:
            json_statuses = []
            for statuses_item_data in statuses:
                statuses_item = statuses_item_data.value

                json_statuses.append(statuses_item)

    params["statuses"] = json_statuses

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[FsEvent]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FsEvent.from_dict(response_200_item_data)

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[FsEvent]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    start_timestamp: Union[Unset, None, int] = 0,
    end_timestamp: Union[Unset, None, int] = 0,
    actions: Union[Unset, None, List[FsEventAction]] = UNSET,
    username: Union[Unset, None, str] = UNSET,
    ip: Union[Unset, None, str] = UNSET,
    ssh_cmd: Union[Unset, None, str] = UNSET,
    fs_provider: Union[Unset, None, FsProviders] = UNSET,
    bucket: Union[Unset, None, str] = UNSET,
    endpoint: Union[Unset, None, str] = UNSET,
    protocols: Union[Unset, None, List[EventProtocols]] = UNSET,
    statuses: Union[Unset, None, List[FsEventStatus]] = UNSET,
    instance_ids: Union[Unset, None, List[str]] = UNSET,
    exclude_ids: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = 100,
    order: Union[Unset, None, GetFsEventsOrder] = UNSET,
) -> Response[Union[Any, List[FsEvent]]]:
    """Get filesystem events

     Returns an array with one or more filesystem events applying the specified filters. This API is only
    available if you configure an \"eventsearcher\" plugin

    Args:
        start_timestamp (Union[Unset, None, int]):
        end_timestamp (Union[Unset, None, int]):
        actions (Union[Unset, None, List[FsEventAction]]):
        username (Union[Unset, None, str]):
        ip (Union[Unset, None, str]):
        ssh_cmd (Union[Unset, None, str]):
        fs_provider (Union[Unset, None, FsProviders]): Filesystem providers:
              * `0` - Local filesystem
              * `1` - S3 Compatible Object Storage
              * `2` - Google Cloud Storage
              * `3` - Azure Blob Storage
              * `4` - Local filesystem encrypted
              * `5` - SFTP
              * `6` - HTTP filesystem
        bucket (Union[Unset, None, str]):
        endpoint (Union[Unset, None, str]):
        protocols (Union[Unset, None, List[EventProtocols]]):
        statuses (Union[Unset, None, List[FsEventStatus]]):
        instance_ids (Union[Unset, None, List[str]]):
        exclude_ids (Union[Unset, None, List[str]]):
        limit (Union[Unset, None, int]):  Default: 100.
        order (Union[Unset, None, GetFsEventsOrder]):  Example: DESC.

    Returns:
        Response[Union[Any, List[FsEvent]]]
    """

    kwargs = _get_kwargs(
        client=client,
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        actions=actions,
        username=username,
        ip=ip,
        ssh_cmd=ssh_cmd,
        fs_provider=fs_provider,
        bucket=bucket,
        endpoint=endpoint,
        protocols=protocols,
        statuses=statuses,
        instance_ids=instance_ids,
        exclude_ids=exclude_ids,
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
    client: Client,
    start_timestamp: Union[Unset, None, int] = 0,
    end_timestamp: Union[Unset, None, int] = 0,
    actions: Union[Unset, None, List[FsEventAction]] = UNSET,
    username: Union[Unset, None, str] = UNSET,
    ip: Union[Unset, None, str] = UNSET,
    ssh_cmd: Union[Unset, None, str] = UNSET,
    fs_provider: Union[Unset, None, FsProviders] = UNSET,
    bucket: Union[Unset, None, str] = UNSET,
    endpoint: Union[Unset, None, str] = UNSET,
    protocols: Union[Unset, None, List[EventProtocols]] = UNSET,
    statuses: Union[Unset, None, List[FsEventStatus]] = UNSET,
    instance_ids: Union[Unset, None, List[str]] = UNSET,
    exclude_ids: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = 100,
    order: Union[Unset, None, GetFsEventsOrder] = UNSET,
) -> Optional[Union[Any, List[FsEvent]]]:
    """Get filesystem events

     Returns an array with one or more filesystem events applying the specified filters. This API is only
    available if you configure an \"eventsearcher\" plugin

    Args:
        start_timestamp (Union[Unset, None, int]):
        end_timestamp (Union[Unset, None, int]):
        actions (Union[Unset, None, List[FsEventAction]]):
        username (Union[Unset, None, str]):
        ip (Union[Unset, None, str]):
        ssh_cmd (Union[Unset, None, str]):
        fs_provider (Union[Unset, None, FsProviders]): Filesystem providers:
              * `0` - Local filesystem
              * `1` - S3 Compatible Object Storage
              * `2` - Google Cloud Storage
              * `3` - Azure Blob Storage
              * `4` - Local filesystem encrypted
              * `5` - SFTP
              * `6` - HTTP filesystem
        bucket (Union[Unset, None, str]):
        endpoint (Union[Unset, None, str]):
        protocols (Union[Unset, None, List[EventProtocols]]):
        statuses (Union[Unset, None, List[FsEventStatus]]):
        instance_ids (Union[Unset, None, List[str]]):
        exclude_ids (Union[Unset, None, List[str]]):
        limit (Union[Unset, None, int]):  Default: 100.
        order (Union[Unset, None, GetFsEventsOrder]):  Example: DESC.

    Returns:
        Response[Union[Any, List[FsEvent]]]
    """

    return sync_detailed(
        client=client,
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        actions=actions,
        username=username,
        ip=ip,
        ssh_cmd=ssh_cmd,
        fs_provider=fs_provider,
        bucket=bucket,
        endpoint=endpoint,
        protocols=protocols,
        statuses=statuses,
        instance_ids=instance_ids,
        exclude_ids=exclude_ids,
        limit=limit,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    start_timestamp: Union[Unset, None, int] = 0,
    end_timestamp: Union[Unset, None, int] = 0,
    actions: Union[Unset, None, List[FsEventAction]] = UNSET,
    username: Union[Unset, None, str] = UNSET,
    ip: Union[Unset, None, str] = UNSET,
    ssh_cmd: Union[Unset, None, str] = UNSET,
    fs_provider: Union[Unset, None, FsProviders] = UNSET,
    bucket: Union[Unset, None, str] = UNSET,
    endpoint: Union[Unset, None, str] = UNSET,
    protocols: Union[Unset, None, List[EventProtocols]] = UNSET,
    statuses: Union[Unset, None, List[FsEventStatus]] = UNSET,
    instance_ids: Union[Unset, None, List[str]] = UNSET,
    exclude_ids: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = 100,
    order: Union[Unset, None, GetFsEventsOrder] = UNSET,
) -> Response[Union[Any, List[FsEvent]]]:
    """Get filesystem events

     Returns an array with one or more filesystem events applying the specified filters. This API is only
    available if you configure an \"eventsearcher\" plugin

    Args:
        start_timestamp (Union[Unset, None, int]):
        end_timestamp (Union[Unset, None, int]):
        actions (Union[Unset, None, List[FsEventAction]]):
        username (Union[Unset, None, str]):
        ip (Union[Unset, None, str]):
        ssh_cmd (Union[Unset, None, str]):
        fs_provider (Union[Unset, None, FsProviders]): Filesystem providers:
              * `0` - Local filesystem
              * `1` - S3 Compatible Object Storage
              * `2` - Google Cloud Storage
              * `3` - Azure Blob Storage
              * `4` - Local filesystem encrypted
              * `5` - SFTP
              * `6` - HTTP filesystem
        bucket (Union[Unset, None, str]):
        endpoint (Union[Unset, None, str]):
        protocols (Union[Unset, None, List[EventProtocols]]):
        statuses (Union[Unset, None, List[FsEventStatus]]):
        instance_ids (Union[Unset, None, List[str]]):
        exclude_ids (Union[Unset, None, List[str]]):
        limit (Union[Unset, None, int]):  Default: 100.
        order (Union[Unset, None, GetFsEventsOrder]):  Example: DESC.

    Returns:
        Response[Union[Any, List[FsEvent]]]
    """

    kwargs = _get_kwargs(
        client=client,
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        actions=actions,
        username=username,
        ip=ip,
        ssh_cmd=ssh_cmd,
        fs_provider=fs_provider,
        bucket=bucket,
        endpoint=endpoint,
        protocols=protocols,
        statuses=statuses,
        instance_ids=instance_ids,
        exclude_ids=exclude_ids,
        limit=limit,
        order=order,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    start_timestamp: Union[Unset, None, int] = 0,
    end_timestamp: Union[Unset, None, int] = 0,
    actions: Union[Unset, None, List[FsEventAction]] = UNSET,
    username: Union[Unset, None, str] = UNSET,
    ip: Union[Unset, None, str] = UNSET,
    ssh_cmd: Union[Unset, None, str] = UNSET,
    fs_provider: Union[Unset, None, FsProviders] = UNSET,
    bucket: Union[Unset, None, str] = UNSET,
    endpoint: Union[Unset, None, str] = UNSET,
    protocols: Union[Unset, None, List[EventProtocols]] = UNSET,
    statuses: Union[Unset, None, List[FsEventStatus]] = UNSET,
    instance_ids: Union[Unset, None, List[str]] = UNSET,
    exclude_ids: Union[Unset, None, List[str]] = UNSET,
    limit: Union[Unset, None, int] = 100,
    order: Union[Unset, None, GetFsEventsOrder] = UNSET,
) -> Optional[Union[Any, List[FsEvent]]]:
    """Get filesystem events

     Returns an array with one or more filesystem events applying the specified filters. This API is only
    available if you configure an \"eventsearcher\" plugin

    Args:
        start_timestamp (Union[Unset, None, int]):
        end_timestamp (Union[Unset, None, int]):
        actions (Union[Unset, None, List[FsEventAction]]):
        username (Union[Unset, None, str]):
        ip (Union[Unset, None, str]):
        ssh_cmd (Union[Unset, None, str]):
        fs_provider (Union[Unset, None, FsProviders]): Filesystem providers:
              * `0` - Local filesystem
              * `1` - S3 Compatible Object Storage
              * `2` - Google Cloud Storage
              * `3` - Azure Blob Storage
              * `4` - Local filesystem encrypted
              * `5` - SFTP
              * `6` - HTTP filesystem
        bucket (Union[Unset, None, str]):
        endpoint (Union[Unset, None, str]):
        protocols (Union[Unset, None, List[EventProtocols]]):
        statuses (Union[Unset, None, List[FsEventStatus]]):
        instance_ids (Union[Unset, None, List[str]]):
        exclude_ids (Union[Unset, None, List[str]]):
        limit (Union[Unset, None, int]):  Default: 100.
        order (Union[Unset, None, GetFsEventsOrder]):  Example: DESC.

    Returns:
        Response[Union[Any, List[FsEvent]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            actions=actions,
            username=username,
            ip=ip,
            ssh_cmd=ssh_cmd,
            fs_provider=fs_provider,
            bucket=bucket,
            endpoint=endpoint,
            protocols=protocols,
            statuses=statuses,
            instance_ids=instance_ids,
            exclude_ids=exclude_ids,
            limit=limit,
            order=order,
        )
    ).parsed
