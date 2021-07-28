from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.secret_status import SecretStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Secret")


@attr.s(auto_attribs=True)
class Secret:
    """The secret is encrypted before saving, so to set a new secret you must provide a payload and set the status to "Plain". The encryption key and additional data will be generated automatically. If you set the status to "Redacted" the existig secret will be preserved"""

    status: Union[Unset, SecretStatus] = UNSET
    payload: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    additional_data: Union[Unset, str] = UNSET
    mode: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        payload = self.payload
        key = self.key
        additional_data = self.additional_data
        mode = self.mode

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if payload is not UNSET:
            field_dict["payload"] = payload
        if key is not UNSET:
            field_dict["key"] = key
        if additional_data is not UNSET:
            field_dict["additional_data"] = additional_data
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _status = d.pop("status", UNSET)
        status: Union[Unset, SecretStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SecretStatus(_status)

        payload = d.pop("payload", UNSET)

        key = d.pop("key", UNSET)

        additional_data = d.pop("additional_data", UNSET)

        mode = d.pop("mode", UNSET)

        secret = cls(
            status=status,
            payload=payload,
            key=key,
            additional_data=additional_data,
            mode=mode,
        )

        secret.additional_properties = d
        return secret

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
