from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.filesystem_config import FilesystemConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualFolder")


@attr.s(auto_attribs=True)
class VirtualFolder:
    """A virtual folder is a mapping between a SFTPGo virtual path and a filesystem path outside the user home directory.
    The specified paths must be absolute and the virtual path cannot be "/", it must be a sub directory. The parent
    directory for the specified virtual path must exist. SFTPGo will try to automatically create any missing parent
    directory for the configured virtual folders at user login.

        Attributes:
            virtual_path (str):
            id (Union[Unset, int]):
            name (Union[Unset, str]): unique name for this virtual folder
            mapped_path (Union[Unset, str]): absolute filesystem path to use as virtual folder
            description (Union[Unset, str]): optional description
            used_quota_size (Union[Unset, int]):
            used_quota_files (Union[Unset, int]):
            last_quota_update (Union[Unset, int]): Last quota update as unix timestamp in milliseconds
            users (Union[Unset, List[str]]): list of usernames associated with this virtual folder
            filesystem (Union[Unset, FilesystemConfig]): Storage filesystem details
            quota_size (Union[Unset, int]): Quota as size in bytes. 0 menas unlimited, -1 means included in user quota.
                Please note that quota is updated if files are added/removed via SFTPGo otherwise a quota scan or a manual quota
                update is needed
            quota_files (Union[Unset, int]): Quota as number of files. 0 menas unlimited, , -1 means included in user quota.
                Please note that quota is updated if files are added/removed via SFTPGo otherwise a quota scan or a manual quota
                update is needed
    """

    virtual_path: str
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    mapped_path: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    used_quota_size: Union[Unset, int] = UNSET
    used_quota_files: Union[Unset, int] = UNSET
    last_quota_update: Union[Unset, int] = UNSET
    users: Union[Unset, List[str]] = UNSET
    filesystem: Union[Unset, FilesystemConfig] = UNSET
    quota_size: Union[Unset, int] = UNSET
    quota_files: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        virtual_path = self.virtual_path
        id = self.id
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

        quota_size = self.quota_size
        quota_files = self.quota_files

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "virtual_path": virtual_path,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
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
        if quota_size is not UNSET:
            field_dict["quota_size"] = quota_size
        if quota_files is not UNSET:
            field_dict["quota_files"] = quota_files

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        virtual_path = d.pop("virtual_path")

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        mapped_path = d.pop("mapped_path", UNSET)

        description = d.pop("description", UNSET)

        used_quota_size = d.pop("used_quota_size", UNSET)

        used_quota_files = d.pop("used_quota_files", UNSET)

        last_quota_update = d.pop("last_quota_update", UNSET)

        users = cast(List[str], d.pop("users", UNSET))

        _filesystem = d.pop("filesystem", UNSET)
        filesystem: Union[Unset, FilesystemConfig]
        if isinstance(_filesystem, Unset):
            filesystem = UNSET
        else:
            filesystem = FilesystemConfig.from_dict(_filesystem)

        quota_size = d.pop("quota_size", UNSET)

        quota_files = d.pop("quota_files", UNSET)

        virtual_folder = cls(
            virtual_path=virtual_path,
            id=id,
            name=name,
            mapped_path=mapped_path,
            description=description,
            used_quota_size=used_quota_size,
            used_quota_files=used_quota_files,
            last_quota_update=last_quota_update,
            users=users,
            filesystem=filesystem,
            quota_size=quota_size,
            quota_files=quota_files,
        )

        virtual_folder.additional_properties = d
        return virtual_folder

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
