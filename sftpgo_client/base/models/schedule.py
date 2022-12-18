from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Schedule")


@attr.s(auto_attribs=True)
class Schedule:
    """
    Attributes:
        hour (Union[Unset, str]):
        day_of_week (Union[Unset, str]):
        day_of_month (Union[Unset, str]):
        month (Union[Unset, str]):
    """

    hour: Union[Unset, str] = UNSET
    day_of_week: Union[Unset, str] = UNSET
    day_of_month: Union[Unset, str] = UNSET
    month: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hour = self.hour
        day_of_week = self.day_of_week
        day_of_month = self.day_of_month
        month = self.month

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hour is not UNSET:
            field_dict["hour"] = hour
        if day_of_week is not UNSET:
            field_dict["day_of_week"] = day_of_week
        if day_of_month is not UNSET:
            field_dict["day_of_month"] = day_of_month
        if month is not UNSET:
            field_dict["month"] = month

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hour = d.pop("hour", UNSET)

        day_of_week = d.pop("day_of_week", UNSET)

        day_of_month = d.pop("day_of_month", UNSET)

        month = d.pop("month", UNSET)

        schedule = cls(
            hour=hour,
            day_of_week=day_of_week,
            day_of_month=day_of_month,
            month=month,
        )

        schedule.additional_properties = d
        return schedule

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
