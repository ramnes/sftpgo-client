from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="QuotaScan")


@attr.s(auto_attribs=True)
class QuotaScan:
    """
    Attributes:
        username (Union[Unset, str]): username to which the quota scan refers
        start_time (Union[Unset, int]): scan start time as unix timestamp in milliseconds
    """

    username: Union[Unset, str] = UNSET
    start_time: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        start_time = self.start_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if start_time is not UNSET:
            field_dict["start_time"] = start_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username", UNSET)

        start_time = d.pop("start_time", UNSET)

        quota_scan = cls(
            username=username,
            start_time=start_time,
        )

        quota_scan.additional_properties = d
        return quota_scan

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
