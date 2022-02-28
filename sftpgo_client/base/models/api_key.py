from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.api_key_scope import APIKeyScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="APIKey")


@attr.s(auto_attribs=True)
class APIKey:
    """
    Attributes:
        id (Union[Unset, str]): unique key identifier
        name (Union[Unset, str]): User friendly key name
        key (Union[Unset, str]): We store the hash of the key. This is just like a password. For security reasons this
            field is omitted when you search/get API keys
        scope (Union[Unset, APIKeyScope]): Options:
              * `1` - admin scope. The API key will be used to impersonate an SFTPGo admin
              * `2` - user scope. The API key will be used to impersonate an SFTPGo user
        created_at (Union[Unset, int]): creation time as unix timestamp in milliseconds
        updated_at (Union[Unset, int]): last update time as unix timestamp in milliseconds
        last_use_at (Union[Unset, int]): last use time as unix timestamp in milliseconds. It is saved at most once every
            10 minutes
        expires_at (Union[Unset, int]): expiration time as unix timestamp in milliseconds
        description (Union[Unset, str]): optional description
        user (Union[Unset, str]): username associated with this API key. If empty and the scope is "user scope" the key
            can impersonate any user
        admin (Union[Unset, str]): admin associated with this API key. If empty and the scope is "admin scope" the key
            can impersonate any admin
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    key: Union[Unset, str] = UNSET
    scope: Union[Unset, APIKeyScope] = UNSET
    created_at: Union[Unset, int] = UNSET
    updated_at: Union[Unset, int] = UNSET
    last_use_at: Union[Unset, int] = UNSET
    expires_at: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    user: Union[Unset, str] = UNSET
    admin: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        key = self.key
        scope: Union[Unset, int] = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        created_at = self.created_at
        updated_at = self.updated_at
        last_use_at = self.last_use_at
        expires_at = self.expires_at
        description = self.description
        user = self.user
        admin = self.admin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if key is not UNSET:
            field_dict["key"] = key
        if scope is not UNSET:
            field_dict["scope"] = scope
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if last_use_at is not UNSET:
            field_dict["last_use_at"] = last_use_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if description is not UNSET:
            field_dict["description"] = description
        if user is not UNSET:
            field_dict["user"] = user
        if admin is not UNSET:
            field_dict["admin"] = admin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        key = d.pop("key", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: Union[Unset, APIKeyScope]
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = APIKeyScope(_scope)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        last_use_at = d.pop("last_use_at", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        description = d.pop("description", UNSET)

        user = d.pop("user", UNSET)

        admin = d.pop("admin", UNSET)

        api_key = cls(
            id=id,
            name=name,
            key=key,
            scope=scope,
            created_at=created_at,
            updated_at=updated_at,
            last_use_at=last_use_at,
            expires_at=expires_at,
            description=description,
            user=user,
            admin=admin,
        )

        api_key.additional_properties = d
        return api_key

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
