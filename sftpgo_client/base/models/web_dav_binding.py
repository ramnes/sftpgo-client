from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.tls_versions import TLSVersions
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebDAVBinding")


@attr.s(auto_attribs=True)
class WebDAVBinding:
    """
    Attributes:
        address (Union[Unset, str]): TCP address the server listen on
        port (Union[Unset, int]): the port used for serving requests
        enable_https (Union[Unset, bool]):
        min_tls_version (Union[Unset, TLSVersions]): TLS version:
              * `12` - TLS 1.2
              * `13` - TLS 1.3
        client_auth_type (Union[Unset, int]): 1 means that client certificate authentication is required in addition to
            HTTP basic authentication
        tls_cipher_suites (Union[Unset, List[str]]): List of supported cipher suites for TLS version 1.2. If empty  a
            default list of secure cipher suites is used, with a preference order based on hardware performance
        prefix (Union[Unset, str]): Prefix for WebDAV resources, if empty WebDAV resources will be available at the `/`
            URI
        proxy_allowed (Union[Unset, List[str]]): List of IP addresses and IP ranges allowed to set proxy headers
    """

    address: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    enable_https: Union[Unset, bool] = UNSET
    min_tls_version: Union[Unset, TLSVersions] = UNSET
    client_auth_type: Union[Unset, int] = UNSET
    tls_cipher_suites: Union[Unset, List[str]] = UNSET
    prefix: Union[Unset, str] = UNSET
    proxy_allowed: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address
        port = self.port
        enable_https = self.enable_https
        min_tls_version: Union[Unset, int] = UNSET
        if not isinstance(self.min_tls_version, Unset):
            min_tls_version = self.min_tls_version.value

        client_auth_type = self.client_auth_type
        tls_cipher_suites: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tls_cipher_suites, Unset):
            tls_cipher_suites = self.tls_cipher_suites

        prefix = self.prefix
        proxy_allowed: Union[Unset, List[str]] = UNSET
        if not isinstance(self.proxy_allowed, Unset):
            proxy_allowed = self.proxy_allowed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if port is not UNSET:
            field_dict["port"] = port
        if enable_https is not UNSET:
            field_dict["enable_https"] = enable_https
        if min_tls_version is not UNSET:
            field_dict["min_tls_version"] = min_tls_version
        if client_auth_type is not UNSET:
            field_dict["client_auth_type"] = client_auth_type
        if tls_cipher_suites is not UNSET:
            field_dict["tls_cipher_suites"] = tls_cipher_suites
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if proxy_allowed is not UNSET:
            field_dict["proxy_allowed"] = proxy_allowed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("address", UNSET)

        port = d.pop("port", UNSET)

        enable_https = d.pop("enable_https", UNSET)

        _min_tls_version = d.pop("min_tls_version", UNSET)
        min_tls_version: Union[Unset, TLSVersions]
        if isinstance(_min_tls_version, Unset):
            min_tls_version = UNSET
        else:
            min_tls_version = TLSVersions(_min_tls_version)

        client_auth_type = d.pop("client_auth_type", UNSET)

        tls_cipher_suites = cast(List[str], d.pop("tls_cipher_suites", UNSET))

        prefix = d.pop("prefix", UNSET)

        proxy_allowed = cast(List[str], d.pop("proxy_allowed", UNSET))

        web_dav_binding = cls(
            address=address,
            port=port,
            enable_https=enable_https,
            min_tls_version=min_tls_version,
            client_auth_type=client_auth_type,
            tls_cipher_suites=tls_cipher_suites,
            prefix=prefix,
            proxy_allowed=proxy_allowed,
        )

        web_dav_binding.additional_properties = d
        return web_dav_binding

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
