from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.totp_config import TOTPConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="MFAStatus")


@attr.s(auto_attribs=True)
class MFAStatus:
    """
    Attributes:
        is_active (Union[Unset, bool]):
        totp_configs (Union[Unset, List[TOTPConfig]]):
    """

    is_active: Union[Unset, bool] = UNSET
    totp_configs: Union[Unset, List[TOTPConfig]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_active = self.is_active
        totp_configs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.totp_configs, Unset):
            totp_configs = []
            for totp_configs_item_data in self.totp_configs:
                totp_configs_item = totp_configs_item_data.to_dict()

                totp_configs.append(totp_configs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if totp_configs is not UNSET:
            field_dict["totp_configs"] = totp_configs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_active = d.pop("is_active", UNSET)

        totp_configs = []
        _totp_configs = d.pop("totp_configs", UNSET)
        for totp_configs_item_data in _totp_configs or []:
            totp_configs_item = TOTPConfig.from_dict(totp_configs_item_data)

            totp_configs.append(totp_configs_item)

        mfa_status = cls(
            is_active=is_active,
            totp_configs=totp_configs,
        )

        mfa_status.additional_properties = d
        return mfa_status

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
