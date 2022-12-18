from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.condition_options_protocols_item import ConditionOptionsProtocolsItem
from ..models.condition_options_provider_objects_item import (
    ConditionOptionsProviderObjectsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_pattern import ConditionPattern


T = TypeVar("T", bound="ConditionOptions")


@attr.s(auto_attribs=True)
class ConditionOptions:
    """
    Attributes:
        names (Union[Unset, List['ConditionPattern']]):
        group_names (Union[Unset, List['ConditionPattern']]):
        role_names (Union[Unset, List['ConditionPattern']]):
        fs_paths (Union[Unset, List['ConditionPattern']]):
        protocols (Union[Unset, List[ConditionOptionsProtocolsItem]]):
        provider_objects (Union[Unset, List[ConditionOptionsProviderObjectsItem]]):
        min_size (Union[Unset, int]):
        max_size (Union[Unset, int]):
        concurrent_execution (Union[Unset, bool]): allow concurrent execution from multiple nodes
    """

    names: Union[Unset, List["ConditionPattern"]] = UNSET
    group_names: Union[Unset, List["ConditionPattern"]] = UNSET
    role_names: Union[Unset, List["ConditionPattern"]] = UNSET
    fs_paths: Union[Unset, List["ConditionPattern"]] = UNSET
    protocols: Union[Unset, List[ConditionOptionsProtocolsItem]] = UNSET
    provider_objects: Union[Unset, List[ConditionOptionsProviderObjectsItem]] = UNSET
    min_size: Union[Unset, int] = UNSET
    max_size: Union[Unset, int] = UNSET
    concurrent_execution: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        names: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.names, Unset):
            names = []
            for names_item_data in self.names:
                names_item = names_item_data.to_dict()

                names.append(names_item)

        group_names: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.group_names, Unset):
            group_names = []
            for group_names_item_data in self.group_names:
                group_names_item = group_names_item_data.to_dict()

                group_names.append(group_names_item)

        role_names: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.role_names, Unset):
            role_names = []
            for role_names_item_data in self.role_names:
                role_names_item = role_names_item_data.to_dict()

                role_names.append(role_names_item)

        fs_paths: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fs_paths, Unset):
            fs_paths = []
            for fs_paths_item_data in self.fs_paths:
                fs_paths_item = fs_paths_item_data.to_dict()

                fs_paths.append(fs_paths_item)

        protocols: Union[Unset, List[str]] = UNSET
        if not isinstance(self.protocols, Unset):
            protocols = []
            for protocols_item_data in self.protocols:
                protocols_item = protocols_item_data.value

                protocols.append(protocols_item)

        provider_objects: Union[Unset, List[str]] = UNSET
        if not isinstance(self.provider_objects, Unset):
            provider_objects = []
            for provider_objects_item_data in self.provider_objects:
                provider_objects_item = provider_objects_item_data.value

                provider_objects.append(provider_objects_item)

        min_size = self.min_size
        max_size = self.max_size
        concurrent_execution = self.concurrent_execution

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if names is not UNSET:
            field_dict["names"] = names
        if group_names is not UNSET:
            field_dict["group_names"] = group_names
        if role_names is not UNSET:
            field_dict["role_names"] = role_names
        if fs_paths is not UNSET:
            field_dict["fs_paths"] = fs_paths
        if protocols is not UNSET:
            field_dict["protocols"] = protocols
        if provider_objects is not UNSET:
            field_dict["provider_objects"] = provider_objects
        if min_size is not UNSET:
            field_dict["min_size"] = min_size
        if max_size is not UNSET:
            field_dict["max_size"] = max_size
        if concurrent_execution is not UNSET:
            field_dict["concurrent_execution"] = concurrent_execution

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.condition_pattern import ConditionPattern

        d = src_dict.copy()
        names = []
        _names = d.pop("names", UNSET)
        for names_item_data in _names or []:
            names_item = ConditionPattern.from_dict(names_item_data)

            names.append(names_item)

        group_names = []
        _group_names = d.pop("group_names", UNSET)
        for group_names_item_data in _group_names or []:
            group_names_item = ConditionPattern.from_dict(group_names_item_data)

            group_names.append(group_names_item)

        role_names = []
        _role_names = d.pop("role_names", UNSET)
        for role_names_item_data in _role_names or []:
            role_names_item = ConditionPattern.from_dict(role_names_item_data)

            role_names.append(role_names_item)

        fs_paths = []
        _fs_paths = d.pop("fs_paths", UNSET)
        for fs_paths_item_data in _fs_paths or []:
            fs_paths_item = ConditionPattern.from_dict(fs_paths_item_data)

            fs_paths.append(fs_paths_item)

        protocols = []
        _protocols = d.pop("protocols", UNSET)
        for protocols_item_data in _protocols or []:
            protocols_item = ConditionOptionsProtocolsItem(protocols_item_data)

            protocols.append(protocols_item)

        provider_objects = []
        _provider_objects = d.pop("provider_objects", UNSET)
        for provider_objects_item_data in _provider_objects or []:
            provider_objects_item = ConditionOptionsProviderObjectsItem(
                provider_objects_item_data
            )

            provider_objects.append(provider_objects_item)

        min_size = d.pop("min_size", UNSET)

        max_size = d.pop("max_size", UNSET)

        concurrent_execution = d.pop("concurrent_execution", UNSET)

        condition_options = cls(
            names=names,
            group_names=group_names,
            role_names=role_names,
            fs_paths=fs_paths,
            protocols=protocols,
            provider_objects=provider_objects,
            min_size=min_size,
            max_size=max_size,
            concurrent_execution=concurrent_execution,
        )

        condition_options.additional_properties = d
        return condition_options

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
