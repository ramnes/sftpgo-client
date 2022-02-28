from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.api_response import ApiResponse
from ...models.setprops_user_file_json_body import SetpropsUserFileJsonBody
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    json_body: SetpropsUserFileJsonBody,
    path: str,
) -> Dict[str, Any]:
    url = "{}/user/files/metadata".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["path"] = path

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, List[ApiResponse]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ApiResponse.from_dict(response_200_item_data)

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
    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413
    if response.status_code == 500:
        response_500 = cast(Any, None)
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
    json_body: SetpropsUserFileJsonBody,
    path: str,
) -> Response[Union[Any, List[ApiResponse]]]:
    """Set metadata for a file/directory

     Set supported metadata attributes for the specified file or directory

    Args:
        path (str):
        json_body (SetpropsUserFileJsonBody):

    Returns:
        Response[Union[Any, List[ApiResponse]]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        path=path,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: SetpropsUserFileJsonBody,
    path: str,
) -> Optional[Union[Any, List[ApiResponse]]]:
    """Set metadata for a file/directory

     Set supported metadata attributes for the specified file or directory

    Args:
        path (str):
        json_body (SetpropsUserFileJsonBody):

    Returns:
        Response[Union[Any, List[ApiResponse]]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        path=path,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: SetpropsUserFileJsonBody,
    path: str,
) -> Response[Union[Any, List[ApiResponse]]]:
    """Set metadata for a file/directory

     Set supported metadata attributes for the specified file or directory

    Args:
        path (str):
        json_body (SetpropsUserFileJsonBody):

    Returns:
        Response[Union[Any, List[ApiResponse]]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        path=path,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: SetpropsUserFileJsonBody,
    path: str,
) -> Optional[Union[Any, List[ApiResponse]]]:
    """Set metadata for a file/directory

     Set supported metadata attributes for the specified file or directory

    Args:
        path (str):
        json_body (SetpropsUserFileJsonBody):

    Returns:
        Response[Union[Any, List[ApiResponse]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            path=path,
        )
    ).parsed
