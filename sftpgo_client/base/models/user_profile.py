from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserProfile")


@attr.s(auto_attribs=True)
class UserProfile:
    """
    Attributes:
        email (Union[Unset, str]):
        description (Union[Unset, str]):
        allow_api_key_auth (Union[Unset, bool]): If enabled, you can impersonate this user, in REST API, using an API
            key. If disabled user credentials are required for impersonation
        public_keys (Union[Unset, List[str]]):
    """

    email: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    allow_api_key_auth: Union[Unset, bool] = UNSET
    public_keys: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        description = self.description
        allow_api_key_auth = self.allow_api_key_auth
        public_keys: Union[Unset, List[str]] = UNSET
        if not isinstance(self.public_keys, Unset):
            public_keys = self.public_keys

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if description is not UNSET:
            field_dict["description"] = description
        if allow_api_key_auth is not UNSET:
            field_dict["allow_api_key_auth"] = allow_api_key_auth
        if public_keys is not UNSET:
            field_dict["public_keys"] = public_keys

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email", UNSET)

        description = d.pop("description", UNSET)

        allow_api_key_auth = d.pop("allow_api_key_auth", UNSET)

        public_keys = cast(List[str], d.pop("public_keys", UNSET))

        user_profile = cls(
            email=email,
            description=description,
            allow_api_key_auth=allow_api_key_auth,
            public_keys=public_keys,
        )

        user_profile.additional_properties = d
        return user_profile

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
