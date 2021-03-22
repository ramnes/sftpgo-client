from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebDAVBinding")


@attr.s(auto_attribs=True)
class WebDAVBinding:
    """  """

    address: Union[Unset, str] = UNSET
    port: Union[Unset, int] = UNSET
    enable_https: Union[Unset, bool] = UNSET
    client_auth_type: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address
        port = self.port
        enable_https = self.enable_https
        client_auth_type = self.client_auth_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if port is not UNSET:
            field_dict["port"] = port
        if enable_https is not UNSET:
            field_dict["enable_https"] = enable_https
        if client_auth_type is not UNSET:
            field_dict["client_auth_type"] = client_auth_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("address", UNSET)

        port = d.pop("port", UNSET)

        enable_https = d.pop("enable_https", UNSET)

        client_auth_type = d.pop("client_auth_type", UNSET)

        web_dav_binding = cls(
            address=address,
            port=port,
            enable_https=enable_https,
            client_auth_type=client_auth_type,
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
