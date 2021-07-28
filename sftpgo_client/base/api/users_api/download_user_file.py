from typing import Any, Dict

import httpx

from ...client import Client
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    path: str,
) -> Dict[str, Any]:
    url = "{}/user/files".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "path": path,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    path: str,
) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,
        path=path,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    path: str,
) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,
        path=path,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
