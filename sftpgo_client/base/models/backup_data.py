from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.admin import Admin
from ..models.api_key import APIKey
from ..models.base_virtual_folder import BaseVirtualFolder
from ..models.share import Share
from ..models.user import User
from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupData")


@attr.s(auto_attribs=True)
class BackupData:
    """
    Attributes:
        users (Union[Unset, List[User]]):
        folders (Union[Unset, List[BaseVirtualFolder]]):
        admins (Union[Unset, List[Admin]]):
        api_keys (Union[Unset, List[APIKey]]):
        shares (Union[Unset, List[Share]]):
        version (Union[Unset, int]):
    """

    users: Union[Unset, List[User]] = UNSET
    folders: Union[Unset, List[BaseVirtualFolder]] = UNSET
    admins: Union[Unset, List[Admin]] = UNSET
    api_keys: Union[Unset, List[APIKey]] = UNSET
    shares: Union[Unset, List[Share]] = UNSET
    version: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()

                users.append(users_item)

        folders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.folders, Unset):
            folders = []
            for folders_item_data in self.folders:
                folders_item = folders_item_data.to_dict()

                folders.append(folders_item)

        admins: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.admins, Unset):
            admins = []
            for admins_item_data in self.admins:
                admins_item = admins_item_data.to_dict()

                admins.append(admins_item)

        api_keys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.api_keys, Unset):
            api_keys = []
            for api_keys_item_data in self.api_keys:
                api_keys_item = api_keys_item_data.to_dict()

                api_keys.append(api_keys_item)

        shares: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.shares, Unset):
            shares = []
            for shares_item_data in self.shares:
                shares_item = shares_item_data.to_dict()

                shares.append(shares_item)

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if users is not UNSET:
            field_dict["users"] = users
        if folders is not UNSET:
            field_dict["folders"] = folders
        if admins is not UNSET:
            field_dict["admins"] = admins
        if api_keys is not UNSET:
            field_dict["api_keys"] = api_keys
        if shares is not UNSET:
            field_dict["shares"] = shares
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = User.from_dict(users_item_data)

            users.append(users_item)

        folders = []
        _folders = d.pop("folders", UNSET)
        for folders_item_data in _folders or []:
            folders_item = BaseVirtualFolder.from_dict(folders_item_data)

            folders.append(folders_item)

        admins = []
        _admins = d.pop("admins", UNSET)
        for admins_item_data in _admins or []:
            admins_item = Admin.from_dict(admins_item_data)

            admins.append(admins_item)

        api_keys = []
        _api_keys = d.pop("api_keys", UNSET)
        for api_keys_item_data in _api_keys or []:
            api_keys_item = APIKey.from_dict(api_keys_item_data)

            api_keys.append(api_keys_item)

        shares = []
        _shares = d.pop("shares", UNSET)
        for shares_item_data in _shares or []:
            shares_item = Share.from_dict(shares_item_data)

            shares.append(shares_item)

        version = d.pop("version", UNSET)

        backup_data = cls(
            users=users,
            folders=folders,
            admins=admins,
            api_keys=api_keys,
            shares=shares,
            version=version,
        )

        backup_data.additional_properties = d
        return backup_data

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
