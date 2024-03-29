from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetpropsUserFileJsonBody")


@attr.s(auto_attribs=True)
class SetpropsUserFileJsonBody:
    """
    Attributes:
        modification_time (Union[Unset, int]): File modification time as unix timestamp in milliseconds
    """

    modification_time: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        modification_time = self.modification_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if modification_time is not UNSET:
            field_dict["modification_time"] = modification_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        modification_time = d.pop("modification_time", UNSET)

        setprops_user_file_json_body = cls(
            modification_time=modification_time,
        )

        setprops_user_file_json_body.additional_properties = d
        return setprops_user_file_json_body

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
