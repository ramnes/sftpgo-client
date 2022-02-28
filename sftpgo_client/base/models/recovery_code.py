from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.secret import Secret
from ..types import UNSET, Unset

T = TypeVar("T", bound="RecoveryCode")


@attr.s(auto_attribs=True)
class RecoveryCode:
    """Recovery codes to use if the user loses access to their second factor auth device. Each code can only be used once,
    you should use these codes to login and disable or reset 2FA for your account

        Attributes:
            secret (Union[Unset, Secret]): The secret is encrypted before saving, so to set a new secret you must provide a
                payload and set the status to "Plain". The encryption key and additional data will be generated automatically.
                If you set the status to "Redacted" the existig secret will be preserved
            used (Union[Unset, bool]):
    """

    secret: Union[Unset, Secret] = UNSET
    used: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        secret: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.secret, Unset):
            secret = self.secret.to_dict()

        used = self.used

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if secret is not UNSET:
            field_dict["secret"] = secret
        if used is not UNSET:
            field_dict["used"] = used

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _secret = d.pop("secret", UNSET)
        secret: Union[Unset, Secret]
        if isinstance(_secret, Unset):
            secret = UNSET
        else:
            secret = Secret.from_dict(_secret)

        used = d.pop("used", UNSET)

        recovery_code = cls(
            secret=secret,
            used=used,
        )

        recovery_code.additional_properties = d
        return recovery_code

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
