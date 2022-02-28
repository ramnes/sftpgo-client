from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidateUserTotpSecretJsonBody")


@attr.s(auto_attribs=True)
class ValidateUserTotpSecretJsonBody:
    """
    Attributes:
        config_name (Union[Unset, str]): name of the configuration to use to validate the passcode
        passcode (Union[Unset, str]): passcode to validate
        secret (Union[Unset, str]): secret to use to validate the passcode
    """

    config_name: Union[Unset, str] = UNSET
    passcode: Union[Unset, str] = UNSET
    secret: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config_name = self.config_name
        passcode = self.passcode
        secret = self.secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config_name is not UNSET:
            field_dict["config_name"] = config_name
        if passcode is not UNSET:
            field_dict["passcode"] = passcode
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        config_name = d.pop("config_name", UNSET)

        passcode = d.pop("passcode", UNSET)

        secret = d.pop("secret", UNSET)

        validate_user_totp_secret_json_body = cls(
            config_name=config_name,
            passcode=passcode,
            secret=secret,
        )

        validate_user_totp_secret_json_body.additional_properties = d
        return validate_user_totp_secret_json_body

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
