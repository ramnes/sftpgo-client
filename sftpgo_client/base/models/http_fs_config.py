from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.http_fs_config_equality_check_mode import HTTPFsConfigEqualityCheckMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.secret import Secret


T = TypeVar("T", bound="HTTPFsConfig")


@attr.s(auto_attribs=True)
class HTTPFsConfig:
    """
    Attributes:
        endpoint (Union[Unset, str]): HTTP/S endpoint URL. SFTPGo will use this URL as base, for example for the `stat`
            API, SFTPGo will add `/stat/{name}`
        username (Union[Unset, str]):
        password (Union[Unset, Secret]): The secret is encrypted before saving, so to set a new secret you must provide
            a payload and set the status to "Plain". The encryption key and additional data will be generated automatically.
            If you set the status to "Redacted" the existing secret will be preserved
        api_key (Union[Unset, Secret]): The secret is encrypted before saving, so to set a new secret you must provide a
            payload and set the status to "Plain". The encryption key and additional data will be generated automatically.
            If you set the status to "Redacted" the existing secret will be preserved
        skip_tls_verify (Union[Unset, bool]):
        equality_check_mode (Union[Unset, HTTPFsConfigEqualityCheckMode]): Defines how to check if this config points to
            the same server as another config. If different configs point to the same server the renaming between the fs
            configs is allowed:
             * `0` username and endpoint must match. This is the default
             * `1` only the endpoint must match
    """

    endpoint: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    password: Union[Unset, "Secret"] = UNSET
    api_key: Union[Unset, "Secret"] = UNSET
    skip_tls_verify: Union[Unset, bool] = UNSET
    equality_check_mode: Union[Unset, HTTPFsConfigEqualityCheckMode] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        endpoint = self.endpoint
        username = self.username
        password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.password, Unset):
            password = self.password.to_dict()

        api_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.api_key, Unset):
            api_key = self.api_key.to_dict()

        skip_tls_verify = self.skip_tls_verify
        equality_check_mode: Union[Unset, int] = UNSET
        if not isinstance(self.equality_check_mode, Unset):
            equality_check_mode = self.equality_check_mode.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if api_key is not UNSET:
            field_dict["api_key"] = api_key
        if skip_tls_verify is not UNSET:
            field_dict["skip_tls_verify"] = skip_tls_verify
        if equality_check_mode is not UNSET:
            field_dict["equality_check_mode"] = equality_check_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
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

        _api_key = d.pop("api_key", UNSET)
        api_key: Union[Unset, Secret]
        if isinstance(_api_key, Unset):
            api_key = UNSET
        else:
            api_key = Secret.from_dict(_api_key)

        skip_tls_verify = d.pop("skip_tls_verify", UNSET)

        _equality_check_mode = d.pop("equality_check_mode", UNSET)
        equality_check_mode: Union[Unset, HTTPFsConfigEqualityCheckMode]
        if isinstance(_equality_check_mode, Unset):
            equality_check_mode = UNSET
        else:
            equality_check_mode = HTTPFsConfigEqualityCheckMode(_equality_check_mode)

        http_fs_config = cls(
            endpoint=endpoint,
            username=username,
            password=password,
            api_key=api_key,
            skip_tls_verify=skip_tls_verify,
            equality_check_mode=equality_check_mode,
        )

        http_fs_config.additional_properties = d
        return http_fs_config

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
