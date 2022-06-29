from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.filesystem_config import FilesystemConfig
from ..models.group_mapping import GroupMapping
from ..models.user_filters import UserFilters
from ..models.user_oidc_custom_fields import UserOidcCustomFields
from ..models.user_permissions import UserPermissions
from ..models.user_status import UserStatus
from ..models.virtual_folder import VirtualFolder
from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@attr.s(auto_attribs=True)
class User:
    """
    Attributes:
        id (Union[Unset, int]):
        status (Union[Unset, UserStatus]): status:
              * `0` user is disabled, login is not allowed
              * `1` user is enabled
        username (Union[Unset, str]): username is unique
        email (Union[Unset, str]):
        description (Union[Unset, str]): optional description, for example the user full name
        expiration_date (Union[Unset, int]): expiration date as unix timestamp in milliseconds. An expired account
            cannot login. 0 means no expiration
        password (Union[Unset, str]): password or public key/SSH user certificate are mandatory. If the password has no
            known hashing algo prefix it will be stored, by default, using bcrypt, argon2id is supported too. You can send a
            password hashed as bcrypt ($2a$ prefix), argon2id, pbkdf2 or unix crypt and it will be stored as is. For
            security reasons this field is omitted when you search/get users
        public_keys (Union[Unset, List[str]]): Public keys in OpenSSH format. A password or at least one public key/SSH
            user certificate are mandatory.
        home_dir (Union[Unset, str]): path to the user home directory. The user cannot upload or download files outside
            this directory. SFTPGo tries to automatically create this folder if missing. Must be an absolute path
        virtual_folders (Union[Unset, List[VirtualFolder]]): mapping between virtual SFTPGo paths and virtual folders.
            If one or more of the specified folders are not inside the dataprovider they will be automatically created. You
            have to create the folder on the filesystem yourself
        uid (Union[Unset, int]): if you run SFTPGo as root user, the created files and directories will be assigned to
            this uid. 0 means no change, the owner will be the user that runs SFTPGo. Ignored on windows
        gid (Union[Unset, int]): if you run SFTPGo as root user, the created files and directories will be assigned to
            this gid. 0 means no change, the group will be the one of the user that runs SFTPGo. Ignored on windows
        max_sessions (Union[Unset, int]): Limit the sessions that a user can open. 0 means unlimited
        quota_size (Union[Unset, int]): Quota as size in bytes. 0 means unlimited. Please note that quota is updated if
            files are added/removed via SFTPGo otherwise a quota scan or a manual quota update is needed
        quota_files (Union[Unset, int]): Quota as number of files. 0 means unlimited. Please note that quota is updated
            if files are added/removed via SFTPGo otherwise a quota scan or a manual quota update is needed
        permissions (Union[Unset, UserPermissions]): hash map with directory as key and an array of permissions as
            value. Directories must be absolute paths, permissions for root directory ("/") are required Example: {'/':
            ['*'], '/somedir': ['list', 'download']}.
        used_quota_size (Union[Unset, int]):
        used_quota_files (Union[Unset, int]):
        last_quota_update (Union[Unset, int]): Last quota update as unix timestamp in milliseconds
        upload_bandwidth (Union[Unset, int]): Maximum upload bandwidth as KB/s, 0 means unlimited
        download_bandwidth (Union[Unset, int]): Maximum download bandwidth as KB/s, 0 means unlimited
        upload_data_transfer (Union[Unset, int]): Maximum data transfer allowed for uploads as MB. 0 means no limit
        download_data_transfer (Union[Unset, int]): Maximum data transfer allowed for downloads as MB. 0 means no limit
        total_data_transfer (Union[Unset, int]): Maximum total data transfer as MB. 0 means unlimited. You can set a
            total data transfer instead of the individual values for uploads and downloads
        used_upload_data_transfer (Union[Unset, int]): Uploaded size, as bytes, since the last reset
        used_download_data_transfer (Union[Unset, int]): Downloaded size, as bytes, since the last reset
        created_at (Union[Unset, int]): creation time as unix timestamp in milliseconds. It will be 0 for users created
            before v2.2.0
        updated_at (Union[Unset, int]): last update time as unix timestamp in milliseconds
        last_login (Union[Unset, int]): Last user login as unix timestamp in milliseconds. It is saved at most once
            every 10 minutes
        filters (Union[Unset, UserFilters]):
        filesystem (Union[Unset, FilesystemConfig]): Storage filesystem details
        additional_info (Union[Unset, str]): Free form text field for external systems
        groups (Union[Unset, List[GroupMapping]]):
        oidc_custom_fields (Union[Unset, UserOidcCustomFields]): This field is passed to the pre-login hook if custom
            OIDC token fields have been configured. Field values can be of any type (this is a free form object) and depend
            on the type of the configured OIDC token fields
    """

    id: Union[Unset, int] = UNSET
    status: Union[Unset, UserStatus] = UNSET
    username: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
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
    upload_data_transfer: Union[Unset, int] = UNSET
    download_data_transfer: Union[Unset, int] = UNSET
    total_data_transfer: Union[Unset, int] = UNSET
    used_upload_data_transfer: Union[Unset, int] = UNSET
    used_download_data_transfer: Union[Unset, int] = UNSET
    created_at: Union[Unset, int] = UNSET
    updated_at: Union[Unset, int] = UNSET
    last_login: Union[Unset, int] = UNSET
    filters: Union[Unset, UserFilters] = UNSET
    filesystem: Union[Unset, FilesystemConfig] = UNSET
    additional_info: Union[Unset, str] = UNSET
    groups: Union[Unset, List[GroupMapping]] = UNSET
    oidc_custom_fields: Union[Unset, UserOidcCustomFields] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        username = self.username
        email = self.email
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
        upload_data_transfer = self.upload_data_transfer
        download_data_transfer = self.download_data_transfer
        total_data_transfer = self.total_data_transfer
        used_upload_data_transfer = self.used_upload_data_transfer
        used_download_data_transfer = self.used_download_data_transfer
        created_at = self.created_at
        updated_at = self.updated_at
        last_login = self.last_login
        filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        filesystem: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filesystem, Unset):
            filesystem = self.filesystem.to_dict()

        additional_info = self.additional_info
        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()

                groups.append(groups_item)

        oidc_custom_fields: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.oidc_custom_fields, Unset):
            oidc_custom_fields = self.oidc_custom_fields.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if username is not UNSET:
            field_dict["username"] = username
        if email is not UNSET:
            field_dict["email"] = email
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
        if upload_data_transfer is not UNSET:
            field_dict["upload_data_transfer"] = upload_data_transfer
        if download_data_transfer is not UNSET:
            field_dict["download_data_transfer"] = download_data_transfer
        if total_data_transfer is not UNSET:
            field_dict["total_data_transfer"] = total_data_transfer
        if used_upload_data_transfer is not UNSET:
            field_dict["used_upload_data_transfer"] = used_upload_data_transfer
        if used_download_data_transfer is not UNSET:
            field_dict["used_download_data_transfer"] = used_download_data_transfer
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if last_login is not UNSET:
            field_dict["last_login"] = last_login
        if filters is not UNSET:
            field_dict["filters"] = filters
        if filesystem is not UNSET:
            field_dict["filesystem"] = filesystem
        if additional_info is not UNSET:
            field_dict["additional_info"] = additional_info
        if groups is not UNSET:
            field_dict["groups"] = groups
        if oidc_custom_fields is not UNSET:
            field_dict["oidc_custom_fields"] = oidc_custom_fields

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

        email = d.pop("email", UNSET)

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

        upload_data_transfer = d.pop("upload_data_transfer", UNSET)

        download_data_transfer = d.pop("download_data_transfer", UNSET)

        total_data_transfer = d.pop("total_data_transfer", UNSET)

        used_upload_data_transfer = d.pop("used_upload_data_transfer", UNSET)

        used_download_data_transfer = d.pop("used_download_data_transfer", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

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

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = GroupMapping.from_dict(groups_item_data)

            groups.append(groups_item)

        _oidc_custom_fields = d.pop("oidc_custom_fields", UNSET)
        oidc_custom_fields: Union[Unset, UserOidcCustomFields]
        if isinstance(_oidc_custom_fields, Unset):
            oidc_custom_fields = UNSET
        else:
            oidc_custom_fields = UserOidcCustomFields.from_dict(_oidc_custom_fields)

        user = cls(
            id=id,
            status=status,
            username=username,
            email=email,
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
            upload_data_transfer=upload_data_transfer,
            download_data_transfer=download_data_transfer,
            total_data_transfer=total_data_transfer,
            used_upload_data_transfer=used_upload_data_transfer,
            used_download_data_transfer=used_download_data_transfer,
            created_at=created_at,
            updated_at=updated_at,
            last_login=last_login,
            filters=filters,
            filesystem=filesystem,
            additional_info=additional_info,
            groups=groups,
            oidc_custom_fields=oidc_custom_fields,
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
