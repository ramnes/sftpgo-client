from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatternsFilter")


@attr.s(auto_attribs=True)
class PatternsFilter:
    """  """

    path: Union[Unset, str] = UNSET
    allowed_patterns: Union[Unset, List[str]] = UNSET
    denied_patterns: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        allowed_patterns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allowed_patterns, Unset):
            allowed_patterns = self.allowed_patterns

        denied_patterns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.denied_patterns, Unset):
            denied_patterns = self.denied_patterns

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if allowed_patterns is not UNSET:
            field_dict["allowed_patterns"] = allowed_patterns
        if denied_patterns is not UNSET:
            field_dict["denied_patterns"] = denied_patterns

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path", UNSET)

        allowed_patterns = cast(List[str], d.pop("allowed_patterns", UNSET))

        denied_patterns = cast(List[str], d.pop("denied_patterns", UNSET))

        patterns_filter = cls(
            path=path,
            allowed_patterns=allowed_patterns,
            denied_patterns=denied_patterns,
        )

        patterns_filter.additional_properties = d
        return patterns_filter

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
