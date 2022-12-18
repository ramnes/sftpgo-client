from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_group_mapping_options import AdminGroupMappingOptions


T = TypeVar("T", bound="AdminGroupMapping")


@attr.s(auto_attribs=True)
class AdminGroupMapping:
    """
    Attributes:
        name (Union[Unset, str]): group name
        options (Union[Unset, AdminGroupMappingOptions]):
    """

    name: Union[Unset, str] = UNSET
    options: Union[Unset, "AdminGroupMappingOptions"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.admin_group_mapping_options import AdminGroupMappingOptions

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _options = d.pop("options", UNSET)
        options: Union[Unset, AdminGroupMappingOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = AdminGroupMappingOptions.from_dict(_options)

        admin_group_mapping = cls(
            name=name,
            options=options,
        )

        admin_group_mapping.additional_properties = d
        return admin_group_mapping

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
