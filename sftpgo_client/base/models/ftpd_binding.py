from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.ftpd_binding_active_connections_security import (
    FTPDBindingActiveConnectionsSecurity,
)
from ..models.ftpd_binding_passive_connections_security import (
    FTPDBindingPassiveConnectionsSecurity,
)
from ..models.ftpd_binding_tls_mode import FTPDBindingTlsMode
from ..models.passive_ip_override import PassiveIPOverride
from ..models.tls_versions import TLSVersions
from ..types import UNSET, Unset

T = TypeVar("T", bound="FTPDBinding")


@attr.s(auto_attribs=True)
class FTPDBinding:
    """
    Attributes:
        address (Union[Unset, str]): TCP address the server listen on
        port (Union[Unset, int]): the port used for serving requests
        apply_proxy_config (Union[Unset, bool]): apply the proxy configuration, if any
        tls_mode (Union[Unset, FTPDBindingTlsMode]): TLS mode:
              * `0` - clear or explicit TLS
              * `1` - explicit TLS required
              * `2` - implicit TLS
        min_tls_version (Union[Unset, TLSVersions]): TLS version:
              * `12` - TLS 1.2
              * `13` - TLS 1.3
        force_passive_ip (Union[Unset, str]): External IP address to expose for passive connections
        passive_ip_overrides (Union[Unset, List[PassiveIPOverride]]):
        client_auth_type (Union[Unset, int]): 1 means that client certificate authentication is required in addition to
            FTP authentication
        tls_cipher_suites (Union[Unset, List[str]]): List of supported cipher suites for TLS version 1.2. If empty  a
            default list of secure cipher suites is used, with a preference order based on hardware performance
        passive_connections_security (Union[Unset, FTPDBindingPassiveConnectionsSecurity]): Active connections security:
              * `0` - require matching peer IP addresses of control and data connection
              * `1` - disable any checks
        active_connections_security (Union[Unset, FTPDBindingActiveConnectionsSecurity]): Active connections security:
              * `0` - require matching peer IP addresses of control and data connection
              * `1` - disable any checks
        debug (Union[Unset, bool]): If enabled any FTP command will be logged
    """

    address: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    apply_proxy_config: Union[Unset, bool] = UNSET
    tls_mode: Union[Unset, FTPDBindingTlsMode] = UNSET
    min_tls_version: Union[Unset, TLSVersions] = UNSET
    force_passive_ip: Union[Unset, str] = UNSET
    passive_ip_overrides: Union[Unset, List[PassiveIPOverride]] = UNSET
    client_auth_type: Union[Unset, int] = UNSET
    tls_cipher_suites: Union[Unset, List[str]] = UNSET
    passive_connections_security: Union[
        Unset, FTPDBindingPassiveConnectionsSecurity
    ] = UNSET
    active_connections_security: Union[
        Unset, FTPDBindingActiveConnectionsSecurity
    ] = UNSET
    debug: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address
        port = self.port
        apply_proxy_config = self.apply_proxy_config
        tls_mode: Union[Unset, int] = UNSET
        if not isinstance(self.tls_mode, Unset):
            tls_mode = self.tls_mode.value

        min_tls_version: Union[Unset, int] = UNSET
        if not isinstance(self.min_tls_version, Unset):
            min_tls_version = self.min_tls_version.value

        force_passive_ip = self.force_passive_ip
        passive_ip_overrides: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.passive_ip_overrides, Unset):
            passive_ip_overrides = []
            for passive_ip_overrides_item_data in self.passive_ip_overrides:
                passive_ip_overrides_item = passive_ip_overrides_item_data.to_dict()

                passive_ip_overrides.append(passive_ip_overrides_item)

        client_auth_type = self.client_auth_type
        tls_cipher_suites: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tls_cipher_suites, Unset):
            tls_cipher_suites = self.tls_cipher_suites

        passive_connections_security: Union[Unset, int] = UNSET
        if not isinstance(self.passive_connections_security, Unset):
            passive_connections_security = self.passive_connections_security.value

        active_connections_security: Union[Unset, int] = UNSET
        if not isinstance(self.active_connections_security, Unset):
            active_connections_security = self.active_connections_security.value

        debug = self.debug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if port is not UNSET:
            field_dict["port"] = port
        if apply_proxy_config is not UNSET:
            field_dict["apply_proxy_config"] = apply_proxy_config
        if tls_mode is not UNSET:
            field_dict["tls_mode"] = tls_mode
        if min_tls_version is not UNSET:
            field_dict["min_tls_version"] = min_tls_version
        if force_passive_ip is not UNSET:
            field_dict["force_passive_ip"] = force_passive_ip
        if passive_ip_overrides is not UNSET:
            field_dict["passive_ip_overrides"] = passive_ip_overrides
        if client_auth_type is not UNSET:
            field_dict["client_auth_type"] = client_auth_type
        if tls_cipher_suites is not UNSET:
            field_dict["tls_cipher_suites"] = tls_cipher_suites
        if passive_connections_security is not UNSET:
            field_dict["passive_connections_security"] = passive_connections_security
        if active_connections_security is not UNSET:
            field_dict["active_connections_security"] = active_connections_security
        if debug is not UNSET:
            field_dict["debug"] = debug

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("address", UNSET)

        port = d.pop("port", UNSET)

        apply_proxy_config = d.pop("apply_proxy_config", UNSET)

        _tls_mode = d.pop("tls_mode", UNSET)
        tls_mode: Union[Unset, FTPDBindingTlsMode]
        if isinstance(_tls_mode, Unset):
            tls_mode = UNSET
        else:
            tls_mode = FTPDBindingTlsMode(_tls_mode)

        _min_tls_version = d.pop("min_tls_version", UNSET)
        min_tls_version: Union[Unset, TLSVersions]
        if isinstance(_min_tls_version, Unset):
            min_tls_version = UNSET
        else:
            min_tls_version = TLSVersions(_min_tls_version)

        force_passive_ip = d.pop("force_passive_ip", UNSET)

        passive_ip_overrides = []
        _passive_ip_overrides = d.pop("passive_ip_overrides", UNSET)
        for passive_ip_overrides_item_data in _passive_ip_overrides or []:
            passive_ip_overrides_item = PassiveIPOverride.from_dict(
                passive_ip_overrides_item_data
            )

            passive_ip_overrides.append(passive_ip_overrides_item)

        client_auth_type = d.pop("client_auth_type", UNSET)

        tls_cipher_suites = cast(List[str], d.pop("tls_cipher_suites", UNSET))

        _passive_connections_security = d.pop("passive_connections_security", UNSET)
        passive_connections_security: Union[
            Unset, FTPDBindingPassiveConnectionsSecurity
        ]
        if isinstance(_passive_connections_security, Unset):
            passive_connections_security = UNSET
        else:
            passive_connections_security = FTPDBindingPassiveConnectionsSecurity(
                _passive_connections_security
            )

        _active_connections_security = d.pop("active_connections_security", UNSET)
        active_connections_security: Union[Unset, FTPDBindingActiveConnectionsSecurity]
        if isinstance(_active_connections_security, Unset):
            active_connections_security = UNSET
        else:
            active_connections_security = FTPDBindingActiveConnectionsSecurity(
                _active_connections_security
            )

        debug = d.pop("debug", UNSET)

        ftpd_binding = cls(
            address=address,
            port=port,
            apply_proxy_config=apply_proxy_config,
            tls_mode=tls_mode,
            min_tls_version=min_tls_version,
            force_passive_ip=force_passive_ip,
            passive_ip_overrides=passive_ip_overrides,
            client_auth_type=client_auth_type,
            tls_cipher_suites=tls_cipher_suites,
            passive_connections_security=passive_connections_security,
            active_connections_security=active_connections_security,
            debug=debug,
        )

        ftpd_binding.additional_properties = d
        return ftpd_binding

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
