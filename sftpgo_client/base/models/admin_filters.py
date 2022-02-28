from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.base_totp_config import BaseTOTPConfig
from ..models.recovery_code import RecoveryCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminFilters")


@attr.s(auto_attribs=True)
class AdminFilters:
    """
    Attributes:
        allow_list (Union[Unset, List[str]]): only clients connecting from these IP/Mask are allowed. IP/Mask must be in
            CIDR notation as defined in RFC 4632 and RFC 4291, for example "192.0.2.0/24" or "2001:db8::/32" Example:
            ['192.0.2.0/24', '2001:db8::/32'].
        allow_api_key_auth (Union[Unset, bool]): API key auth allows to impersonate this administrator with an API key
        totp_config (Union[Unset, BaseTOTPConfig]):
        recovery_codes (Union[Unset, List[RecoveryCode]]):
    """

    allow_list: Union[Unset, List[str]] = UNSET
    allow_api_key_auth: Union[Unset, bool] = UNSET
    totp_config: Union[Unset, BaseTOTPConfig] = UNSET
    recovery_codes: Union[Unset, List[RecoveryCode]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allow_list: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allow_list, Unset):
            allow_list = self.allow_list

        allow_api_key_auth = self.allow_api_key_auth
        totp_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.totp_config, Unset):
            totp_config = self.totp_config.to_dict()

        recovery_codes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.recovery_codes, Unset):
            recovery_codes = []
            for recovery_codes_item_data in self.recovery_codes:
                recovery_codes_item = recovery_codes_item_data.to_dict()

                recovery_codes.append(recovery_codes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_list is not UNSET:
            field_dict["allow_list"] = allow_list
        if allow_api_key_auth is not UNSET:
            field_dict["allow_api_key_auth"] = allow_api_key_auth
        if totp_config is not UNSET:
            field_dict["totp_config"] = totp_config
        if recovery_codes is not UNSET:
            field_dict["recovery_codes"] = recovery_codes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        allow_list = cast(List[str], d.pop("allow_list", UNSET))

        allow_api_key_auth = d.pop("allow_api_key_auth", UNSET)

        _totp_config = d.pop("totp_config", UNSET)
        totp_config: Union[Unset, BaseTOTPConfig]
        if isinstance(_totp_config, Unset):
            totp_config = UNSET
        else:
            totp_config = BaseTOTPConfig.from_dict(_totp_config)

        recovery_codes = []
        _recovery_codes = d.pop("recovery_codes", UNSET)
        for recovery_codes_item_data in _recovery_codes or []:
            recovery_codes_item = RecoveryCode.from_dict(recovery_codes_item_data)

            recovery_codes.append(recovery_codes_item)

        admin_filters = cls(
            allow_list=allow_list,
            allow_api_key_auth=allow_api_key_auth,
            totp_config=totp_config,
            recovery_codes=recovery_codes,
        )

        admin_filters.additional_properties = d
        return admin_filters

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
