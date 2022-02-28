from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FolderRetention")


@attr.s(auto_attribs=True)
class FolderRetention:
    """
    Attributes:
        path (Union[Unset, str]): exposed virtual directory path, if no other specific retention is defined, the
            retention applies for sub directories too. For example if retention is defined for the paths "/" and "/sub" then
            the retention for "/" is applied for any file outside the "/sub" directory Example: /.
        retention (Union[Unset, int]): retention time in hours. All the files with a modification time older than the
            defined value will be deleted. 0 means exclude this path Example: 24.
        delete_empty_dirs (Union[Unset, bool]): if enabled, empty directories will be deleted
        ignore_user_permissions (Union[Unset, bool]): if enabled, files will be deleted even if the user does not have
            the delete permission. The default is "false" which means that files will be skipped if the user does not have
            permission to delete them. File patterns filters will always be silently ignored
    """

    path: Union[Unset, str] = UNSET
    retention: Union[Unset, int] = UNSET
    delete_empty_dirs: Union[Unset, bool] = UNSET
    ignore_user_permissions: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        path = self.path
        retention = self.retention
        delete_empty_dirs = self.delete_empty_dirs
        ignore_user_permissions = self.ignore_user_permissions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if retention is not UNSET:
            field_dict["retention"] = retention
        if delete_empty_dirs is not UNSET:
            field_dict["delete_empty_dirs"] = delete_empty_dirs
        if ignore_user_permissions is not UNSET:
            field_dict["ignore_user_permissions"] = ignore_user_permissions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("path", UNSET)

        retention = d.pop("retention", UNSET)

        delete_empty_dirs = d.pop("delete_empty_dirs", UNSET)

        ignore_user_permissions = d.pop("ignore_user_permissions", UNSET)

        folder_retention = cls(
            path=path,
            retention=retention,
            delete_empty_dirs=delete_empty_dirs,
            ignore_user_permissions=ignore_user_permissions,
        )

        folder_retention.additional_properties = d
        return folder_retention

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
