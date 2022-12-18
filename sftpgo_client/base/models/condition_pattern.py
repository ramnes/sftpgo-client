from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConditionPattern")


@attr.s(auto_attribs=True)
class ConditionPattern:
    """
    Attributes:
        pattern (Union[Unset, str]):
        inverse_match (Union[Unset, bool]):
    """

    pattern: Union[Unset, str] = UNSET
    inverse_match: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pattern = self.pattern
        inverse_match = self.inverse_match

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if inverse_match is not UNSET:
            field_dict["inverse_match"] = inverse_match

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pattern = d.pop("pattern", UNSET)

        inverse_match = d.pop("inverse_match", UNSET)

        condition_pattern = cls(
            pattern=pattern,
            inverse_match=inverse_match,
        )

        condition_pattern.additional_properties = d
        return condition_pattern

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
