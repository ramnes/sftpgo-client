from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VersionInfo")


@attr.s(auto_attribs=True)
class VersionInfo:
    """
    Attributes:
        version (Union[Unset, str]):
        build_date (Union[Unset, str]):
        commit_hash (Union[Unset, str]):
        features (Union[Unset, List[str]]): Features for the current build. Available features are `portable`, `bolt`,
            `mysql`, `sqlite`, `pgsql`, `s3`, `gcs`, `metrics`. If a feature is available it has a `+` prefix, otherwise a
            `-` prefix
    """

    version: Union[Unset, str] = UNSET
    build_date: Union[Unset, str] = UNSET
    commit_hash: Union[Unset, str] = UNSET
    features: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        build_date = self.build_date
        commit_hash = self.commit_hash
        features: Union[Unset, List[str]] = UNSET
        if not isinstance(self.features, Unset):
            features = self.features

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if build_date is not UNSET:
            field_dict["build_date"] = build_date
        if commit_hash is not UNSET:
            field_dict["commit_hash"] = commit_hash
        if features is not UNSET:
            field_dict["features"] = features

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("version", UNSET)

        build_date = d.pop("build_date", UNSET)

        commit_hash = d.pop("commit_hash", UNSET)

        features = cast(List[str], d.pop("features", UNSET))

        version_info = cls(
            version=version,
            build_date=build_date,
            commit_hash=commit_hash,
            features=features,
        )

        version_info.additional_properties = d
        return version_info

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
