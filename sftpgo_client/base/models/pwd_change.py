from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PwdChange")


@attr.s(auto_attribs=True)
class PwdChange:
    """
    Attributes:
        current_password (Union[Unset, str]):
        new_password (Union[Unset, str]):
    """

    current_password: Union[Unset, str] = UNSET
    new_password: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_password = self.current_password
        new_password = self.new_password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_password is not UNSET:
            field_dict["current_password"] = current_password
        if new_password is not UNSET:
            field_dict["new_password"] = new_password

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current_password = d.pop("current_password", UNSET)

        new_password = d.pop("new_password", UNSET)

        pwd_change = cls(
            current_password=current_password,
            new_password=new_password,
        )

        pwd_change.additional_properties = d
        return pwd_change

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
