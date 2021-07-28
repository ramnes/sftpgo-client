import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DefenderEntry")


@attr.s(auto_attribs=True)
class DefenderEntry:
    """ """

    id: Union[Unset, str] = UNSET
    ip: Union[Unset, str] = UNSET
    score: Union[Unset, int] = UNSET
    ban_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        ip = self.ip
        score = self.score
        ban_time: Union[Unset, str] = UNSET
        if not isinstance(self.ban_time, Unset):
            ban_time = self.ban_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if ip is not UNSET:
            field_dict["ip"] = ip
        if score is not UNSET:
            field_dict["score"] = score
        if ban_time is not UNSET:
            field_dict["ban_time"] = ban_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        ip = d.pop("ip", UNSET)

        score = d.pop("score", UNSET)

        _ban_time = d.pop("ban_time", UNSET)
        ban_time: Union[Unset, datetime.datetime]
        if isinstance(_ban_time, Unset):
            ban_time = UNSET
        else:
            ban_time = isoparse(_ban_time)

        defender_entry = cls(
            id=id,
            ip=ip,
            score=score,
            ban_time=ban_time,
        )

        defender_entry.additional_properties = d
        return defender_entry

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
