from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="HooksFilter")


@attr.s(auto_attribs=True)
class HooksFilter:
    """User specific hook overrides

    Attributes:
        external_auth_disabled (Union[Unset, bool]): If true, the external auth hook, if defined, will not be executed
        pre_login_disabled (Union[Unset, bool]): If true, the pre-login hook, if defined, will not be executed
        check_password_disabled (Union[Unset, bool]): If true, the check password hook, if defined, will not be executed
    """

    external_auth_disabled: Union[Unset, bool] = UNSET
    pre_login_disabled: Union[Unset, bool] = UNSET
    check_password_disabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        external_auth_disabled = self.external_auth_disabled
        pre_login_disabled = self.pre_login_disabled
        check_password_disabled = self.check_password_disabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if external_auth_disabled is not UNSET:
            field_dict["external_auth_disabled"] = external_auth_disabled
        if pre_login_disabled is not UNSET:
            field_dict["pre_login_disabled"] = pre_login_disabled
        if check_password_disabled is not UNSET:
            field_dict["check_password_disabled"] = check_password_disabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        external_auth_disabled = d.pop("external_auth_disabled", UNSET)

        pre_login_disabled = d.pop("pre_login_disabled", UNSET)

        check_password_disabled = d.pop("check_password_disabled", UNSET)

        hooks_filter = cls(
            external_auth_disabled=external_auth_disabled,
            pre_login_disabled=pre_login_disabled,
            check_password_disabled=check_password_disabled,
        )

        hooks_filter.additional_properties = d
        return hooks_filter

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
