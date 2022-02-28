from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddApiKeyResponse201")


@attr.s(auto_attribs=True)
class AddApiKeyResponse201:
    """
    Attributes:
        mesage (Union[Unset, str]):  Example: API key created. This is the only time the API key is visible, please save
            it..
        key (Union[Unset, str]): generated API key
    """

    mesage: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mesage = self.mesage
        key = self.key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mesage is not UNSET:
            field_dict["mesage"] = mesage
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mesage = d.pop("mesage", UNSET)

        key = d.pop("key", UNSET)

        add_api_key_response_201 = cls(
            mesage=mesage,
            key=key,
        )

        add_api_key_response_201.additional_properties = d
        return add_api_key_response_201

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
