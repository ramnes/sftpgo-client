from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.admin_filters import AdminFilters
from ..models.admin_permissions import AdminPermissions
from ..models.admin_status import AdminStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Admin")


@attr.s(auto_attribs=True)
class Admin:
    """ """

    id: Union[Unset, int] = UNSET
    status: Union[Unset, AdminStatus] = UNSET
    username: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    permissions: Union[Unset, List[AdminPermissions]] = UNSET
    filters: Union[Unset, AdminFilters] = UNSET
    additional_info: Union[Unset, str] = UNSET
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        status: Union[Unset, AdminStatus] = UNSET
        _status = d.pop("status", UNSET)
        if not isinstance(_status, Unset):
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

        filters: Union[Unset, AdminFilters] = UNSET
        _filters = d.pop("filters", UNSET)
        if not isinstance(_filters, Unset):
            filters = AdminFilters.from_dict(_filters)

        additional_info = d.pop("additional_info", UNSET)

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
