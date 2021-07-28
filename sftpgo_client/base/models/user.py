from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.filesystem_config import FilesystemConfig
from ..models.user_filters import UserFilters
from ..models.user_permissions import UserPermissions
from ..models.user_status import UserStatus
from ..models.virtual_folder import VirtualFolder
from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@attr.s(auto_attribs=True)
class User:
    """ """

    id: Union[Unset, int] = UNSET
    status: Union[Unset, UserStatus] = UNSET
    username: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    expiration_date: Union[Unset, int] = UNSET
    password: Union[Unset, str] = UNSET
    public_keys: Union[Unset, List[str]] = UNSET
    home_dir: Union[Unset, str] = UNSET
    virtual_folders: Union[Unset, List[VirtualFolder]] = UNSET
    uid: Union[Unset, int] = UNSET
    gid: Union[Unset, int] = UNSET
    max_sessions: Union[Unset, int] = UNSET
    quota_size: Union[Unset, int] = UNSET
    quota_files: Union[Unset, int] = UNSET
    permissions: Union[Unset, UserPermissions] = UNSET
    used_quota_size: Union[Unset, int] = UNSET
    used_quota_files: Union[Unset, int] = UNSET
    last_quota_update: Union[Unset, int] = UNSET
    upload_bandwidth: Union[Unset, int] = UNSET
    download_bandwidth: Union[Unset, int] = UNSET
    last_login: Union[Unset, int] = UNSET
    filters: Union[Unset, UserFilters] = UNSET
    filesystem: Union[Unset, FilesystemConfig] = UNSET
    additional_info: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        username = self.username
        description = self.description
        expiration_date = self.expiration_date
        password = self.password
        public_keys: Union[Unset, List[str]] = UNSET
        if not isinstance(self.public_keys, Unset):
            public_keys = self.public_keys

        home_dir = self.home_dir
        virtual_folders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.virtual_folders, Unset):
            virtual_folders = []
            for virtual_folders_item_data in self.virtual_folders:
                virtual_folders_item = virtual_folders_item_data.to_dict()

                virtual_folders.append(virtual_folders_item)

        uid = self.uid
        gid = self.gid
        max_sessions = self.max_sessions
        quota_size = self.quota_size
        quota_files = self.quota_files
        permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        used_quota_size = self.used_quota_size
        used_quota_files = self.used_quota_files
        last_quota_update = self.last_quota_update
        upload_bandwidth = self.upload_bandwidth
        download_bandwidth = self.download_bandwidth
        last_login = self.last_login
        filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        filesystem: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filesystem, Unset):
            filesystem = self.filesystem.to_dict()

        additional_info = self.additional_info

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if username is not UNSET:
            field_dict["username"] = username
        if description is not UNSET:
            field_dict["description"] = description
        if expiration_date is not UNSET:
            field_dict["expiration_date"] = expiration_date
        if password is not UNSET:
            field_dict["password"] = password
        if public_keys is not UNSET:
            field_dict["public_keys"] = public_keys
        if home_dir is not UNSET:
            field_dict["home_dir"] = home_dir
        if virtual_folders is not UNSET:
            field_dict["virtual_folders"] = virtual_folders
        if uid is not UNSET:
            field_dict["uid"] = uid
        if gid is not UNSET:
            field_dict["gid"] = gid
        if max_sessions is not UNSET:
            field_dict["max_sessions"] = max_sessions
        if quota_size is not UNSET:
            field_dict["quota_size"] = quota_size
        if quota_files is not UNSET:
            field_dict["quota_files"] = quota_files
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if used_quota_size is not UNSET:
            field_dict["used_quota_size"] = used_quota_size
        if used_quota_files is not UNSET:
            field_dict["used_quota_files"] = used_quota_files
        if last_quota_update is not UNSET:
            field_dict["last_quota_update"] = last_quota_update
        if upload_bandwidth is not UNSET:
            field_dict["upload_bandwidth"] = upload_bandwidth
        if download_bandwidth is not UNSET:
            field_dict["download_bandwidth"] = download_bandwidth
        if last_login is not UNSET:
            field_dict["last_login"] = last_login
        if filters is not UNSET:
            field_dict["filters"] = filters
        if filesystem is not UNSET:
            field_dict["filesystem"] = filesystem
        if additional_info is not UNSET:
            field_dict["additional_info"] = additional_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, UserStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UserStatus(_status)

        username = d.pop("username", UNSET)

        description = d.pop("description", UNSET)

        expiration_date = d.pop("expiration_date", UNSET)

        password = d.pop("password", UNSET)

        public_keys = cast(List[str], d.pop("public_keys", UNSET))

        home_dir = d.pop("home_dir", UNSET)

        virtual_folders = []
        _virtual_folders = d.pop("virtual_folders", UNSET)
        for virtual_folders_item_data in _virtual_folders or []:
            virtual_folders_item = VirtualFolder.from_dict(virtual_folders_item_data)

            virtual_folders.append(virtual_folders_item)

        uid = d.pop("uid", UNSET)

        gid = d.pop("gid", UNSET)

        max_sessions = d.pop("max_sessions", UNSET)

        quota_size = d.pop("quota_size", UNSET)

        quota_files = d.pop("quota_files", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, UserPermissions]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = UserPermissions.from_dict(_permissions)

        used_quota_size = d.pop("used_quota_size", UNSET)

        used_quota_files = d.pop("used_quota_files", UNSET)

        last_quota_update = d.pop("last_quota_update", UNSET)

        upload_bandwidth = d.pop("upload_bandwidth", UNSET)

        download_bandwidth = d.pop("download_bandwidth", UNSET)

        last_login = d.pop("last_login", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, UserFilters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = UserFilters.from_dict(_filters)

        _filesystem = d.pop("filesystem", UNSET)
        filesystem: Union[Unset, FilesystemConfig]
        if isinstance(_filesystem, Unset):
            filesystem = UNSET
        else:
            filesystem = FilesystemConfig.from_dict(_filesystem)

        additional_info = d.pop("additional_info", UNSET)

        user = cls(
            id=id,
            status=status,
            username=username,
            description=description,
            expiration_date=expiration_date,
            password=password,
            public_keys=public_keys,
            home_dir=home_dir,
            virtual_folders=virtual_folders,
            uid=uid,
            gid=gid,
            max_sessions=max_sessions,
            quota_size=quota_size,
            quota_files=quota_files,
            permissions=permissions,
            used_quota_size=used_quota_size,
            used_quota_files=used_quota_files,
            last_quota_update=last_quota_update,
            upload_bandwidth=upload_bandwidth,
            download_bandwidth=download_bandwidth,
            last_login=last_login,
            filters=filters,
            filesystem=filesystem,
            additional_info=additional_info,
        )

        user.additional_properties = d
        return user

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
