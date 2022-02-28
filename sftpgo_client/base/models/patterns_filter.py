from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.patterns_filter_deny_policy import PatternsFilterDenyPolicy
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatternsFilter")


@attr.s(auto_attribs=True)
class PatternsFilter:
    """
    Attributes:
        path (Union[Unset, str]): exposed virtual path, if no other specific filter is defined, the filter applies for
            sub directories too. For example if filters are defined for the paths "/" and "/sub" then the filters for "/"
            are applied for any file outside the "/sub" directory
        allowed_patterns (Union[Unset, List[str]]): list of, case insensitive, allowed shell like patterns. Example:
            ['*.jpg', 'a*b?.png'].
        denied_patterns (Union[Unset, List[str]]): list of, case insensitive, denied shell like patterns. Denied
            patterns are evaluated before the allowed ones Example: ['*.zip'].
        deny_policy (Union[Unset, PatternsFilterDenyPolicy]): Deny policies
              * `0` - default policy. Denied files/directories matching the filters are visible in directory listing but
            cannot be uploaded/downloaded/overwritten/renamed
              * `1` - deny policy hide. This policy applies the same restrictions as the default one and denied
            files/directories matching the filters will also be hidden in directory listing. This mode may cause performance
            issues for large directories
    """

    path: Union[Unset, str] = UNSET
    allowed_patterns: Union[Unset, List[str]] = UNSET
    denied_patterns: Union[Unset, List[str]] = UNSET
    deny_policy: Union[Unset, PatternsFilterDenyPolicy] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        allowed_patterns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allowed_patterns, Unset):
            allowed_patterns = self.allowed_patterns

        denied_patterns: Union[Unset, List[str]] = UNSET
        if not isinstance(self.denied_patterns, Unset):
            denied_patterns = self.denied_patterns

        deny_policy: Union[Unset, int] = UNSET
        if not isinstance(self.deny_policy, Unset):
            deny_policy = self.deny_policy.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if allowed_patterns is not UNSET:
            field_dict["allowed_patterns"] = allowed_patterns
        if denied_patterns is not UNSET:
            field_dict["denied_patterns"] = denied_patterns
        if deny_policy is not UNSET:
            field_dict["deny_policy"] = deny_policy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path", UNSET)

        allowed_patterns = cast(List[str], d.pop("allowed_patterns", UNSET))

        denied_patterns = cast(List[str], d.pop("denied_patterns", UNSET))

        _deny_policy = d.pop("deny_policy", UNSET)
        deny_policy: Union[Unset, PatternsFilterDenyPolicy]
        if isinstance(_deny_policy, Unset):
            deny_policy = UNSET
        else:
            deny_policy = PatternsFilterDenyPolicy(_deny_policy)

        patterns_filter = cls(
            path=path,
            allowed_patterns=allowed_patterns,
            denied_patterns=denied_patterns,
            deny_policy=deny_policy,
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
