from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminPreferences")


@attr.s(auto_attribs=True)
class AdminPreferences:
    """
    Attributes:
        hide_user_page_sections (Union[Unset, int]): Allow to hide some sections from the user page. These are not
            security settings and are not enforced server side in any way. They are only intended to simplify the user page
            in the WebAdmin UI. 1 means hide groups section, 2 means hide filesystem section, "users_base_dir" must be set
            in the config file otherwise this setting is ignored, 4 means hide virtual folders section, 8 means hide profile
            section, 16 means hide ACLs section, 32 means hide disk and bandwidth quota limits section, 64 means hide
            advanced settings section. The settings can be combined
        default_users_expiration (Union[Unset, int]): Defines the default expiration for newly created users as number
            of days. 0 means no expiration
    """

    hide_user_page_sections: Union[Unset, int] = UNSET
    default_users_expiration: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hide_user_page_sections = self.hide_user_page_sections
        default_users_expiration = self.default_users_expiration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hide_user_page_sections is not UNSET:
            field_dict["hide_user_page_sections"] = hide_user_page_sections
        if default_users_expiration is not UNSET:
            field_dict["default_users_expiration"] = default_users_expiration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hide_user_page_sections = d.pop("hide_user_page_sections", UNSET)

        default_users_expiration = d.pop("default_users_expiration", UNSET)

        admin_preferences = cls(
            hide_user_page_sections=hide_user_page_sections,
            default_users_expiration=default_users_expiration,
        )

        admin_preferences.additional_properties = d
        return admin_preferences

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
