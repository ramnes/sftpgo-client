from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.web_dav_binding import WebDAVBinding


T = TypeVar("T", bound="WebDAVServiceStatus")


@attr.s(auto_attribs=True)
class WebDAVServiceStatus:
    """
    Attributes:
        is_active (Union[Unset, bool]):
        bindings (Union[Unset, None, List['WebDAVBinding']]):
    """

    is_active: Union[Unset, bool] = UNSET
    bindings: Union[Unset, None, List["WebDAVBinding"]] = UNSET
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

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if bindings is not UNSET:
            field_dict["bindings"] = bindings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.web_dav_binding import WebDAVBinding

        d = src_dict.copy()
        is_active = d.pop("is_active", UNSET)

        bindings = []
        _bindings = d.pop("bindings", UNSET)
        for bindings_item_data in _bindings or []:
            bindings_item = WebDAVBinding.from_dict(bindings_item_data)

            bindings.append(bindings_item)

        web_dav_service_status = cls(
            is_active=is_active,
            bindings=bindings,
        )

        web_dav_service_status.additional_properties = d
        return web_dav_service_status

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
