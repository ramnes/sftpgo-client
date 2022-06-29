from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.permission import Permission

T = TypeVar("T", bound="GroupUserSettingsPermissions")


@attr.s(auto_attribs=True)
class GroupUserSettingsPermissions:
    """hash map with directory as key and an array of permissions as value. Directories must be absolute paths, permissions
    for root directory ("/") are required

        Example:
            {'/': ['*'], '/somedir': ['list', 'download']}

    """

    additional_properties: Dict[str, List[Permission]] = attr.ib(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for additional_property_item_data in prop:
                additional_property_item = additional_property_item_data.value

                field_dict[prop_name].append(additional_property_item)

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_user_settings_permissions = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for additional_property_item_data in _additional_property:
                additional_property_item = Permission(additional_property_item_data)

                additional_property.append(additional_property_item)

            additional_properties[prop_name] = additional_property

        group_user_settings_permissions.additional_properties = additional_properties
        return group_user_settings_permissions

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> List[Permission]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: List[Permission]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
