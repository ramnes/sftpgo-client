from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuotaUsage")


@attr.s(auto_attribs=True)
class QuotaUsage:
    """ """

    used_quota_size: Union[Unset, int] = UNSET
    used_quota_files: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        used_quota_size = self.used_quota_size
        used_quota_files = self.used_quota_files

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if used_quota_size is not UNSET:
            field_dict["used_quota_size"] = used_quota_size
        if used_quota_files is not UNSET:
            field_dict["used_quota_files"] = used_quota_files

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        used_quota_size = d.pop("used_quota_size", UNSET)

        used_quota_files = d.pop("used_quota_files", UNSET)

        quota_usage = cls(
            used_quota_size=used_quota_size,
            used_quota_files=used_quota_files,
        )

        quota_usage.additional_properties = d
        return quota_usage

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
