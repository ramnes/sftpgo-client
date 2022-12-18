from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.api_response import ApiResponse
from ...models.folder_retention import FolderRetention
from ...models.retention_check_notification import RetentionCheckNotification
from ...types import UNSET, Response, Unset


def _get_kwargs(
    username: str,
    *,
    client: Client,
    json_body: List["FolderRetention"],
    notifications: Union[Unset, None, List[RetentionCheckNotification]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/retention/users/{username}/check".format(
        client.base_url, username=username
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_notifications: Union[Unset, None, List[str]] = UNSET
    if not isinstance(notifications, Unset):
        if notifications is None:
            json_notifications = None
        else:
            json_notifications = []
            for notifications_item_data in notifications:
                notifications_item = notifications_item_data.value

                json_notifications.append(notifications_item)

    params["notifications"] = json_notifications

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, ApiResponse]]:
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = ApiResponse.from_dict(response.json())

        return response_202
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, ApiResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: Client,
    json_body: List["FolderRetention"],
    notifications: Union[Unset, None, List[RetentionCheckNotification]] = UNSET,
) -> Response[Union[Any, ApiResponse]]:
    """Start a retention check

     Starts a new retention check for the given user. If a retention check for this user is already
    active a 409 status code is returned

    Args:
        username (str):
        notifications (Union[Unset, None, List[RetentionCheckNotification]]):
        json_body (List['FolderRetention']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
        json_body=json_body,
        notifications=notifications,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    username: str,
    *,
    client: Client,
    json_body: List["FolderRetention"],
    notifications: Union[Unset, None, List[RetentionCheckNotification]] = UNSET,
) -> Optional[Union[Any, ApiResponse]]:
    """Start a retention check

     Starts a new retention check for the given user. If a retention check for this user is already
    active a 409 status code is returned

    Args:
        username (str):
        notifications (Union[Unset, None, List[RetentionCheckNotification]]):
        json_body (List['FolderRetention']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    return sync_detailed(
        username=username,
        client=client,
        json_body=json_body,
        notifications=notifications,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: Client,
    json_body: List["FolderRetention"],
    notifications: Union[Unset, None, List[RetentionCheckNotification]] = UNSET,
) -> Response[Union[Any, ApiResponse]]:
    """Start a retention check

     Starts a new retention check for the given user. If a retention check for this user is already
    active a 409 status code is returned

    Args:
        username (str):
        notifications (Union[Unset, None, List[RetentionCheckNotification]]):
        json_body (List['FolderRetention']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
        json_body=json_body,
        notifications=notifications,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    username: str,
    *,
    client: Client,
    json_body: List["FolderRetention"],
    notifications: Union[Unset, None, List[RetentionCheckNotification]] = UNSET,
) -> Optional[Union[Any, ApiResponse]]:
    """Start a retention check

     Starts a new retention check for the given user. If a retention check for this user is already
    active a 409 status code is returned

    Args:
        username (str):
        notifications (Union[Unset, None, List[RetentionCheckNotification]]):
        json_body (List['FolderRetention']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiResponse]]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
            json_body=json_body,
            notifications=notifications,
        )
    ).parsed
