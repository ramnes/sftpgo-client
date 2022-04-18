from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="UserOidcCustomFields")


@attr.s(auto_attribs=True)
class UserOidcCustomFields:
    """This field is passed to the pre-login hook if custom OIDC token fields have been configured. Field values can be of
    any type (this is a free form object) and depend on the type of the configured OIDC token fields

    """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_oidc_custom_fields = cls()

        user_oidc_custom_fields.additional_properties = d
        return user_oidc_custom_fields

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
