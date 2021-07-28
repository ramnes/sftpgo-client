import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DirEntry")


@attr.s(auto_attribs=True)
class DirEntry:
    """ """

    name: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    mode: Union[Unset, int] = UNSET
    last_modified: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        size = self.size
        mode = self.mode
        last_modified: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified, Unset):
            last_modified = self.last_modified.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size
        if mode is not UNSET:
            field_dict["mode"] = mode
        if last_modified is not UNSET:
            field_dict["last_modified"] = last_modified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        size = d.pop("size", UNSET)

        mode = d.pop("mode", UNSET)

        _last_modified = d.pop("last_modified", UNSET)
        last_modified: Union[Unset, datetime.datetime]
        if isinstance(_last_modified, Unset):
            last_modified = UNSET
        else:
            last_modified = isoparse(_last_modified)

        dir_entry = cls(
            name=name,
            size=size,
            mode=mode,
            last_modified=last_modified,
        )

        dir_entry.additional_properties = d
        return dir_entry

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
