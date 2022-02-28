from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ftp_passive_port_range import FTPPassivePortRange
from ..models.ftpd_binding import FTPDBinding
from ..types import UNSET, Unset

T = TypeVar("T", bound="FTPServiceStatus")


@attr.s(auto_attribs=True)
class FTPServiceStatus:
    """
    Attributes:
        is_active (Union[Unset, bool]):
        bindings (Union[Unset, None, List[FTPDBinding]]):
        passive_port_range (Union[Unset, FTPPassivePortRange]):
    """

    is_active: Union[Unset, bool] = UNSET
    bindings: Union[Unset, None, List[FTPDBinding]] = UNSET
    passive_port_range: Union[Unset, FTPPassivePortRange] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_active = self.is_active
        bindings: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.bindings, Unset):
            if self.bindings is None:
                bindings = None
            else:
                bindings = []
                for bindings_item_data in self.bindings:
                    bindings_item = bindings_item_data.to_dict()

                    bindings.append(bindings_item)

        passive_port_range: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.passive_port_range, Unset):
            passive_port_range = self.passive_port_range.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if bindings is not UNSET:
            field_dict["bindings"] = bindings
        if passive_port_range is not UNSET:
            field_dict["passive_port_range"] = passive_port_range

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_active = d.pop("is_active", UNSET)

        bindings = []
        _bindings = d.pop("bindings", UNSET)
        for bindings_item_data in _bindings or []:
            bindings_item = FTPDBinding.from_dict(bindings_item_data)

            bindings.append(bindings_item)

        _passive_port_range = d.pop("passive_port_range", UNSET)
        passive_port_range: Union[Unset, FTPPassivePortRange]
        if isinstance(_passive_port_range, Unset):
            passive_port_range = UNSET
        else:
            passive_port_range = FTPPassivePortRange.from_dict(_passive_port_range)

        ftp_service_status = cls(
            is_active=is_active,
            bindings=bindings,
            passive_port_range=passive_port_range,
        )

        ftp_service_status.additional_properties = d
        return ftp_service_status

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
