from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.filesystem_config import FilesystemConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="BaseVirtualFolder")


@attr.s(auto_attribs=True)
class BaseVirtualFolder:
    """ Defines the filesystem for the virtual folder and the used quota limits. The same folder can be shared among multiple users and each user can have different quota limits or a different virtual path. """

    id_: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    mapped_path: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    used_quota_size: Union[Unset, int] = UNSET
    used_quota_files: Union[Unset, int] = UNSET
    last_quota_update: Union[Unset, int] = UNSET
    users: Union[Unset, List[str]] = UNSET
    filesystem: Union[Unset, FilesystemConfig] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_ = self.id_
        name = self.name
        mapped_path = self.mapped_path
        description = self.description
        used_quota_size = self.used_quota_size
        used_quota_files = self.used_quota_files
        last_quota_update = self.last_quota_update
        users: Union[Unset, List[str]] = UNSET
        if not isinstance(self.users, Unset):
            users = self.users

        filesystem: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filesystem, Unset):
            filesystem = self.filesystem.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id_ is not UNSET:
            field_dict["id"] = id_
        if name is not UNSET:
            field_dict["name"] = name
        if mapped_path is not UNSET:
            field_dict["mapped_path"] = mapped_path
        if description is not UNSET:
            field_dict["description"] = description
        if used_quota_size is not UNSET:
            field_dict["used_quota_size"] = used_quota_size
        if used_quota_files is not UNSET:
            field_dict["used_quota_files"] = used_quota_files
        if last_quota_update is not UNSET:
            field_dict["last_quota_update"] = last_quota_update
        if users is not UNSET:
            field_dict["users"] = users
        if filesystem is not UNSET:
            field_dict["filesystem"] = filesystem

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id_ = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        mapped_path = d.pop("mapped_path", UNSET)

        description = d.pop("description", UNSET)

        used_quota_size = d.pop("used_quota_size", UNSET)

        used_quota_files = d.pop("used_quota_files", UNSET)

        last_quota_update = d.pop("last_quota_update", UNSET)

        users = cast(List[str], d.pop("users", UNSET))

        filesystem: Union[Unset, FilesystemConfig] = UNSET
        _filesystem = d.pop("filesystem", UNSET)
        if not isinstance(_filesystem, Unset):
            filesystem = FilesystemConfig.from_dict(_filesystem)

        base_virtual_folder = cls(
            id_=id_,
            name=name,
            mapped_path=mapped_path,
            description=description,
            used_quota_size=used_quota_size,
            used_quota_files=used_quota_files,
            last_quota_update=last_quota_update,
            users=users,
            filesystem=filesystem,
        )

        base_virtual_folder.additional_properties = d
        return base_virtual_folder

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
