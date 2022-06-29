from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.group_mapping_type import GroupMappingType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupMapping")


@attr.s(auto_attribs=True)
class GroupMapping:
    """
    Attributes:
        name (Union[Unset, str]): group name
        type (Union[Unset, GroupMappingType]): Group type:
              * `1` - Primary group
              * `2` - Secondaru group
    """

    name: Union[Unset, str] = UNSET
    type: Union[Unset, GroupMappingType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, GroupMappingType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = GroupMappingType(_type)

        group_mapping = cls(
            name=name,
            type=type,
        )

        group_mapping.additional_properties = d
        return group_mapping

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
