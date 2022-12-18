from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.secret import Secret


T = TypeVar("T", bound="CryptFsConfig")


@attr.s(auto_attribs=True)
class CryptFsConfig:
    """Crypt filesystem configuration details

    Attributes:
        passphrase (Union[Unset, Secret]): The secret is encrypted before saving, so to set a new secret you must
            provide a payload and set the status to "Plain". The encryption key and additional data will be generated
            automatically. If you set the status to "Redacted" the existing secret will be preserved
    """

    passphrase: Union[Unset, "Secret"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        passphrase: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.passphrase, Unset):
            passphrase = self.passphrase.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if passphrase is not UNSET:
            field_dict["passphrase"] = passphrase

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.secret import Secret

        d = src_dict.copy()
        _passphrase = d.pop("passphrase", UNSET)
        passphrase: Union[Unset, Secret]
        if isinstance(_passphrase, Unset):
            passphrase = UNSET
        else:
            passphrase = Secret.from_dict(_passphrase)

        crypt_fs_config = cls(
            passphrase=passphrase,
        )

        crypt_fs_config.additional_properties = d
        return crypt_fs_config

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
