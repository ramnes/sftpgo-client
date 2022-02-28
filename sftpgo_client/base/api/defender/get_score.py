from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.score_status import ScoreStatus
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    ip: str,
) -> Dict[str, Any]:
    url = "{}/defender/score".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["ip"] = ip

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ScoreStatus]]:
    if response.status_code == 200:
        response_200 = ScoreStatus.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ScoreStatus]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    ip: str,
) -> Response[Union[Any, ScoreStatus]]:
    """Get score

     Deprecated, please use '/defender/hosts', '/defender/hosts/{id}' instead

    Args:
        ip (str):

    Returns:
        Response[Union[Any, ScoreStatus]]
    """

    kwargs = _get_kwargs(
        client=client,
        ip=ip,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    ip: str,
) -> Optional[Union[Any, ScoreStatus]]:
    """Get score

     Deprecated, please use '/defender/hosts', '/defender/hosts/{id}' instead

    Args:
        ip (str):

    Returns:
        Response[Union[Any, ScoreStatus]]
    """

    return sync_detailed(
        client=client,
        ip=ip,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    ip: str,
) -> Response[Union[Any, ScoreStatus]]:
    """Get score

     Deprecated, please use '/defender/hosts', '/defender/hosts/{id}' instead

    Args:
        ip (str):

    Returns:
        Response[Union[Any, ScoreStatus]]
    """

    kwargs = _get_kwargs(
        client=client,
        ip=ip,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    ip: str,
) -> Optional[Union[Any, ScoreStatus]]:
    """Get score

     Deprecated, please use '/defender/hosts', '/defender/hosts/{id}' instead

    Args:
        ip (str):

    Returns:
        Response[Union[Any, ScoreStatus]]
    """

    return (
        await asyncio_detailed(
            client=client,
            ip=ip,
        )
    ).parsed
