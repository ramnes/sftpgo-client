from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PassiveIPOverride")


@attr.s(auto_attribs=True)
class PassiveIPOverride:
    """
    Attributes:
        networks (Union[Unset, List[str]]):
        ip (Union[Unset, str]):
    """

    networks: Union[Unset, List[str]] = UNSET
    ip: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        networks: Union[Unset, List[str]] = UNSET
        if not isinstance(self.networks, Unset):
            networks = self.networks

        ip = self.ip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if networks is not UNSET:
            field_dict["networks"] = networks
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        networks = cast(List[str], d.pop("networks", UNSET))

        ip = d.pop("ip", UNSET)

        passive_ip_override = cls(
            networks=networks,
            ip=ip,
        )

        passive_ip_override.additional_properties = d
        return passive_ip_override

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
