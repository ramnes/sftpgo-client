from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.admin_group_mapping_options_add_to_users_as import (
    AdminGroupMappingOptionsAddToUsersAs,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminGroupMappingOptions")


@attr.s(auto_attribs=True)
class AdminGroupMappingOptions:
    """
    Attributes:
        add_to_users_as (Union[Unset, AdminGroupMappingOptionsAddToUsersAs]): Add to new users as:
              * `0` - the admin's group will be added as membership group for new users
              * `1` - the admin's group will be added as primary group for new users
              * `2` - the admin's group will be added as secondary group for new users
    """

    add_to_users_as: Union[Unset, AdminGroupMappingOptionsAddToUsersAs] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        add_to_users_as: Union[Unset, int] = UNSET
        if not isinstance(self.add_to_users_as, Unset):
            add_to_users_as = self.add_to_users_as.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if add_to_users_as is not UNSET:
            field_dict["add_to_users_as"] = add_to_users_as

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _add_to_users_as = d.pop("add_to_users_as", UNSET)
        add_to_users_as: Union[Unset, AdminGroupMappingOptionsAddToUsersAs]
        if isinstance(_add_to_users_as, Unset):
            add_to_users_as = UNSET
        else:
            add_to_users_as = AdminGroupMappingOptionsAddToUsersAs(_add_to_users_as)

        admin_group_mapping_options = cls(
            add_to_users_as=add_to_users_as,
        )

        admin_group_mapping_options.additional_properties = d
        return admin_group_mapping_options

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
