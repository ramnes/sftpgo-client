from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtensionsFilter")


@attr.s(auto_attribs=True)
class ExtensionsFilter:
    """ """

    path: Union[Unset, str] = UNSET
    allowed_extensions: Union[Unset, List[str]] = UNSET
    denied_extensions: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        allowed_extensions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allowed_extensions, Unset):
            allowed_extensions = self.allowed_extensions

        denied_extensions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.denied_extensions, Unset):
            denied_extensions = self.denied_extensions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if allowed_extensions is not UNSET:
            field_dict["allowed_extensions"] = allowed_extensions
        if denied_extensions is not UNSET:
            field_dict["denied_extensions"] = denied_extensions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path", UNSET)

        allowed_extensions = cast(List[str], d.pop("allowed_extensions", UNSET))

        denied_extensions = cast(List[str], d.pop("denied_extensions", UNSET))

        extensions_filter = cls(
            path=path,
            allowed_extensions=allowed_extensions,
            denied_extensions=denied_extensions,
        )

        extensions_filter.additional_properties = d
        return extensions_filter

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
