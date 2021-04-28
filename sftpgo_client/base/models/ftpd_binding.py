from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ftpd_binding_tls_mode import FTPDBindingTlsMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="FTPDBinding")


@attr.s(auto_attribs=True)
class FTPDBinding:
    """ """

    address: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    apply_proxy_config: Union[Unset, bool] = UNSET
    tls_mode: Union[Unset, FTPDBindingTlsMode] = UNSET
    force_passive_ip: Union[Unset, str] = UNSET
    client_auth_type: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address
        port = self.port
        apply_proxy_config = self.apply_proxy_config
        tls_mode: Union[Unset, int] = UNSET
        if not isinstance(self.tls_mode, Unset):
            tls_mode = self.tls_mode.value

        force_passive_ip = self.force_passive_ip
        client_auth_type = self.client_auth_type

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
        if force_passive_ip is not UNSET:
            field_dict["force_passive_ip"] = force_passive_ip
        if client_auth_type is not UNSET:
            field_dict["client_auth_type"] = client_auth_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("address", UNSET)

        port = d.pop("port", UNSET)

        apply_proxy_config = d.pop("apply_proxy_config", UNSET)

        tls_mode: Union[Unset, FTPDBindingTlsMode] = UNSET
        _tls_mode = d.pop("tls_mode", UNSET)
        if not isinstance(_tls_mode, Unset):
            tls_mode = FTPDBindingTlsMode(_tls_mode)

        force_passive_ip = d.pop("force_passive_ip", UNSET)

        client_auth_type = d.pop("client_auth_type", UNSET)

        ftpd_binding = cls(
            address=address,
            port=port,
            apply_proxy_config=apply_proxy_config,
            tls_mode=tls_mode,
            force_passive_ip=force_passive_ip,
            client_auth_type=client_auth_type,
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
