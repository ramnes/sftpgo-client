import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BanStatus")


@attr.s(auto_attribs=True)
class BanStatus:
    """
    Attributes:
        date_time (Union[Unset, None, datetime.datetime]): if null the host is not banned
    """

    date_time: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_time: Union[Unset, None, str] = UNSET
        if not isinstance(self.date_time, Unset):
            date_time = self.date_time.isoformat() if self.date_time else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_time is not UNSET:
            field_dict["date_time"] = date_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _date_time = d.pop("date_time", UNSET)
        date_time: Union[Unset, None, datetime.datetime]
        if _date_time is None:
            date_time = None
        elif isinstance(_date_time, Unset):
            date_time = UNSET
        else:
            date_time = isoparse(_date_time)

        ban_status = cls(
            date_time=date_time,
        )

        ban_status.additional_properties = d
        return ban_status

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
