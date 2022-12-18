from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.admin_permissions import AdminPermissions
from ..models.admin_status import AdminStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.admin_filters import AdminFilters


T = TypeVar("T", bound="Admin")


@attr.s(auto_attribs=True)
class Admin:
    """
    Attributes:
        id (Union[Unset, int]):
        status (Union[Unset, AdminStatus]): status:
              * `0` user is disabled, login is not allowed
              * `1` user is enabled
        username (Union[Unset, str]): username is unique
        description (Union[Unset, str]): optional description, for example the admin full name
        password (Union[Unset, str]): Admin password. For security reasons this field is omitted when you search/get
            admins
        email (Union[Unset, str]):
        permissions (Union[Unset, List[AdminPermissions]]):
        filters (Union[Unset, AdminFilters]):
        additional_info (Union[Unset, str]): Free form text field
        created_at (Union[Unset, int]): creation time as unix timestamp in milliseconds. It will be 0 for admins created
            before v2.2.0
        updated_at (Union[Unset, int]): last update time as unix timestamp in milliseconds
        last_login (Union[Unset, int]): Last user login as unix timestamp in milliseconds. It is saved at most once
            every 10 minutes
    """

    id: Union[Unset, int] = UNSET
    status: Union[Unset, AdminStatus] = UNSET
    username: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    permissions: Union[Unset, List[AdminPermissions]] = UNSET
    filters: Union[Unset, "AdminFilters"] = UNSET
    additional_info: Union[Unset, str] = UNSET
    created_at: Union[Unset, int] = UNSET
    updated_at: Union[Unset, int] = UNSET
    last_login: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        username = self.username
        description = self.description
        password = self.password
        email = self.email
        permissions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.value

                permissions.append(permissions_item)

        filters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        additional_info = self.additional_info
        created_at = self.created_at
        updated_at = self.updated_at
        last_login = self.last_login

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
        if password is not UNSET:
            field_dict["password"] = password
        if email is not UNSET:
            field_dict["email"] = email
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if filters is not UNSET:
            field_dict["filters"] = filters
        if additional_info is not UNSET:
            field_dict["additional_info"] = additional_info
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if last_login is not UNSET:
            field_dict["last_login"] = last_login

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.admin_filters import AdminFilters

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AdminStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AdminStatus(_status)

        username = d.pop("username", UNSET)

        description = d.pop("description", UNSET)

        password = d.pop("password", UNSET)

        email = d.pop("email", UNSET)

        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = AdminPermissions(permissions_item_data)

            permissions.append(permissions_item)

        _filters = d.pop("filters", UNSET)
        filters: Union[Unset, AdminFilters]
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = AdminFilters.from_dict(_filters)

        additional_info = d.pop("additional_info", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        last_login = d.pop("last_login", UNSET)

        admin = cls(
            id=id,
            status=status,
            username=username,
            description=description,
            password=password,
            email=email,
            permissions=permissions,
            filters=filters,
            additional_info=additional_info,
            created_at=created_at,
            updated_at=updated_at,
            last_login=last_login,
        )

        admin.additional_properties = d
        return admin

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
