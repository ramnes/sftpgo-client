from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.api_response import ApiResponse
from ...models.backup_data import BackupData
from ...models.dumpdata_indent import DumpdataIndent
from ...models.dumpdata_output_data import DumpdataOutputData
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    output_file: Union[Unset, None, str] = UNSET,
    output_data: Union[Unset, None, DumpdataOutputData] = UNSET,
    indent: Union[Unset, None, DumpdataIndent] = UNSET,
) -> Dict[str, Any]:
    url = "{}/dumpdata".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["output-file"] = output_file

    json_output_data: Union[Unset, None, int] = UNSET
    if not isinstance(output_data, Unset):
        json_output_data = output_data.value if output_data else None

    params["output-data"] = json_output_data

    json_indent: Union[Unset, None, int] = UNSET
    if not isinstance(indent, Unset):
        json_indent = indent.value if indent else None

    params["indent"] = json_indent

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
    *, response: httpx.Response
) -> Optional[Union[Any, Union[ApiResponse, BackupData]]]:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Union[ApiResponse, BackupData]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = ApiResponse.from_dict(data)

                return response_200_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = BackupData.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

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


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, Union[ApiResponse, BackupData]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    output_file: Union[Unset, None, str] = UNSET,
    output_data: Union[Unset, None, DumpdataOutputData] = UNSET,
    indent: Union[Unset, None, DumpdataIndent] = UNSET,
) -> Response[Union[Any, Union[ApiResponse, BackupData]]]:
    """Dump data

     Backups data as data provider independent JSON. The backup can be saved in a local file on the
    server, to avoid exposing sensitive data over the network, or returned as response body. The output
    of dumpdata can be used as input for loaddata

    Args:
        output_file (Union[Unset, None, str]):
        output_data (Union[Unset, None, DumpdataOutputData]):
        indent (Union[Unset, None, DumpdataIndent]):

    Returns:
        Response[Union[Any, Union[ApiResponse, BackupData]]]
    """

    kwargs = _get_kwargs(
        client=client,
        output_file=output_file,
        output_data=output_data,
        indent=indent,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    output_file: Union[Unset, None, str] = UNSET,
    output_data: Union[Unset, None, DumpdataOutputData] = UNSET,
    indent: Union[Unset, None, DumpdataIndent] = UNSET,
) -> Optional[Union[Any, Union[ApiResponse, BackupData]]]:
    """Dump data

     Backups data as data provider independent JSON. The backup can be saved in a local file on the
    server, to avoid exposing sensitive data over the network, or returned as response body. The output
    of dumpdata can be used as input for loaddata

    Args:
        output_file (Union[Unset, None, str]):
        output_data (Union[Unset, None, DumpdataOutputData]):
        indent (Union[Unset, None, DumpdataIndent]):

    Returns:
        Response[Union[Any, Union[ApiResponse, BackupData]]]
    """

    return sync_detailed(
        client=client,
        output_file=output_file,
        output_data=output_data,
        indent=indent,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    output_file: Union[Unset, None, str] = UNSET,
    output_data: Union[Unset, None, DumpdataOutputData] = UNSET,
    indent: Union[Unset, None, DumpdataIndent] = UNSET,
) -> Response[Union[Any, Union[ApiResponse, BackupData]]]:
    """Dump data

     Backups data as data provider independent JSON. The backup can be saved in a local file on the
    server, to avoid exposing sensitive data over the network, or returned as response body. The output
    of dumpdata can be used as input for loaddata

    Args:
        output_file (Union[Unset, None, str]):
        output_data (Union[Unset, None, DumpdataOutputData]):
        indent (Union[Unset, None, DumpdataIndent]):

    Returns:
        Response[Union[Any, Union[ApiResponse, BackupData]]]
    """

    kwargs = _get_kwargs(
        client=client,
        output_file=output_file,
        output_data=output_data,
        indent=indent,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    output_file: Union[Unset, None, str] = UNSET,
    output_data: Union[Unset, None, DumpdataOutputData] = UNSET,
    indent: Union[Unset, None, DumpdataIndent] = UNSET,
) -> Optional[Union[Any, Union[ApiResponse, BackupData]]]:
    """Dump data

     Backups data as data provider independent JSON. The backup can be saved in a local file on the
    server, to avoid exposing sensitive data over the network, or returned as response body. The output
    of dumpdata can be used as input for loaddata

    Args:
        output_file (Union[Unset, None, str]):
        output_data (Union[Unset, None, DumpdataOutputData]):
        indent (Union[Unset, None, DumpdataIndent]):

    Returns:
        Response[Union[Any, Union[ApiResponse, BackupData]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            output_file=output_file,
            output_data=output_data,
            indent=indent,
        )
    ).parsed
