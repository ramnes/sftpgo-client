from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransferQuotaUsage")


@attr.s(auto_attribs=True)
class TransferQuotaUsage:
    """
    Attributes:
        used_upload_data_transfer (Union[Unset, int]): The value must be specified as bytes
        used_download_data_transfer (Union[Unset, int]): The value must be specified as bytes
    """

    used_upload_data_transfer: Union[Unset, int] = UNSET
    used_download_data_transfer: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        used_upload_data_transfer = self.used_upload_data_transfer
        used_download_data_transfer = self.used_download_data_transfer

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if used_upload_data_transfer is not UNSET:
            field_dict["used_upload_data_transfer"] = used_upload_data_transfer
        if used_download_data_transfer is not UNSET:
            field_dict["used_download_data_transfer"] = used_download_data_transfer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        used_upload_data_transfer = d.pop("used_upload_data_transfer", UNSET)

        used_download_data_transfer = d.pop("used_download_data_transfer", UNSET)

        transfer_quota_usage = cls(
            used_upload_data_transfer=used_upload_data_transfer,
            used_download_data_transfer=used_download_data_transfer,
        )

        transfer_quota_usage.additional_properties = d
        return transfer_quota_usage

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
