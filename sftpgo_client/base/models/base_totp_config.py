from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.secret import Secret
from ..types import UNSET, Unset

T = TypeVar("T", bound="BaseTOTPConfig")


@attr.s(auto_attribs=True)
class BaseTOTPConfig:
    """
    Attributes:
        enabled (Union[Unset, bool]):
        config_name (Union[Unset, str]): This name must be defined within the "totp" section of the SFTPGo configuration
            file. You will be unable to save a user/admin referencing a missing config_name
        secret (Union[Unset, Secret]): The secret is encrypted before saving, so to set a new secret you must provide a
            payload and set the status to "Plain". The encryption key and additional data will be generated automatically.
            If you set the status to "Redacted" the existing secret will be preserved
    """

    enabled: Union[Unset, bool] = UNSET
    config_name: Union[Unset, str] = UNSET
    secret: Union[Unset, Secret] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enabled = self.enabled
        config_name = self.config_name
        secret: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.secret, Unset):
            secret = self.secret.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if config_name is not UNSET:
            field_dict["config_name"] = config_name
        if secret is not UNSET:
            field_dict["secret"] = secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enabled = d.pop("enabled", UNSET)

        config_name = d.pop("config_name", UNSET)

        _secret = d.pop("secret", UNSET)
        secret: Union[Unset, Secret]
        if isinstance(_secret, Unset):
            secret = UNSET
        else:
            secret = Secret.from_dict(_secret)

        base_totp_config = cls(
            enabled=enabled,
            config_name=config_name,
            secret=secret,
        )

        base_totp_config.additional_properties = d
        return base_totp_config

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
