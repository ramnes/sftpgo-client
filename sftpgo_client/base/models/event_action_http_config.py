from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.event_action_http_config_method import EventActionHTTPConfigMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_part import HTTPPart
    from ..models.key_value import KeyValue
    from ..models.secret import Secret


T = TypeVar("T", bound="EventActionHTTPConfig")


@attr.s(auto_attribs=True)
class EventActionHTTPConfig:
    """
    Attributes:
        endpoint (Union[Unset, str]): HTTP endpoint Example: https://example.com.
        username (Union[Unset, str]):
        password (Union[Unset, Secret]): The secret is encrypted before saving, so to set a new secret you must provide
            a payload and set the status to "Plain". The encryption key and additional data will be generated automatically.
            If you set the status to "Redacted" the existing secret will be preserved
        headers (Union[Unset, List['KeyValue']]): headers to add
        timeout (Union[Unset, int]): Ignored for multipart requests with files as attachments
        skip_tls_verify (Union[Unset, bool]): if enabled the HTTP client accepts any TLS certificate presented by the
            server and any host name in that certificate. In this mode, TLS is susceptible to man-in-the-middle attacks.
            This should be used only for testing.
        method (Union[Unset, EventActionHTTPConfigMethod]):
        query_parameters (Union[Unset, List['KeyValue']]):
        body (Union[Unset, str]): HTTP POST/PUT body
        parts (Union[Unset, List['HTTPPart']]): Multipart requests allow to combine one or more sets of data into a
            single body. For each part, you can set a file path or a body as text. Placeholders are supported in file path,
            body, header values.
    """

    endpoint: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    password: Union[Unset, "Secret"] = UNSET
    headers: Union[Unset, List["KeyValue"]] = UNSET
    timeout: Union[Unset, int] = UNSET
    skip_tls_verify: Union[Unset, bool] = UNSET
    method: Union[Unset, EventActionHTTPConfigMethod] = UNSET
    query_parameters: Union[Unset, List["KeyValue"]] = UNSET
    body: Union[Unset, str] = UNSET
    parts: Union[Unset, List["HTTPPart"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        endpoint = self.endpoint
        username = self.username
        password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.password, Unset):
            password = self.password.to_dict()

        headers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = headers_item_data.to_dict()

                headers.append(headers_item)

        timeout = self.timeout
        skip_tls_verify = self.skip_tls_verify
        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        query_parameters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.query_parameters, Unset):
            query_parameters = []
            for query_parameters_item_data in self.query_parameters:
                query_parameters_item = query_parameters_item_data.to_dict()

                query_parameters.append(query_parameters_item)

        body = self.body
        parts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.parts, Unset):
            parts = []
            for parts_item_data in self.parts:
                parts_item = parts_item_data.to_dict()

                parts.append(parts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if headers is not UNSET:
            field_dict["headers"] = headers
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if skip_tls_verify is not UNSET:
            field_dict["skip_tls_verify"] = skip_tls_verify
        if method is not UNSET:
            field_dict["method"] = method
        if query_parameters is not UNSET:
            field_dict["query_parameters"] = query_parameters
        if body is not UNSET:
            field_dict["body"] = body
        if parts is not UNSET:
            field_dict["parts"] = parts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.http_part import HTTPPart
        from ..models.key_value import KeyValue
        from ..models.secret import Secret

        d = src_dict.copy()
        endpoint = d.pop("endpoint", UNSET)

        username = d.pop("username", UNSET)

        _password = d.pop("password", UNSET)
        password: Union[Unset, Secret]
        if isinstance(_password, Unset):
            password = UNSET
        else:
            password = Secret.from_dict(_password)

        headers = []
        _headers = d.pop("headers", UNSET)
        for headers_item_data in _headers or []:
            headers_item = KeyValue.from_dict(headers_item_data)

            headers.append(headers_item)

        timeout = d.pop("timeout", UNSET)

        skip_tls_verify = d.pop("skip_tls_verify", UNSET)

        _method = d.pop("method", UNSET)
        method: Union[Unset, EventActionHTTPConfigMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = EventActionHTTPConfigMethod(_method)

        query_parameters = []
        _query_parameters = d.pop("query_parameters", UNSET)
        for query_parameters_item_data in _query_parameters or []:
            query_parameters_item = KeyValue.from_dict(query_parameters_item_data)

            query_parameters.append(query_parameters_item)

        body = d.pop("body", UNSET)

        parts = []
        _parts = d.pop("parts", UNSET)
        for parts_item_data in _parts or []:
            parts_item = HTTPPart.from_dict(parts_item_data)

            parts.append(parts_item)

        event_action_http_config = cls(
            endpoint=endpoint,
            username=username,
            password=password,
            headers=headers,
            timeout=timeout,
            skip_tls_verify=skip_tls_verify,
            method=method,
            query_parameters=query_parameters,
            body=body,
            parts=parts,
        )

        event_action_http_config.additional_properties = d
        return event_action_http_config

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
