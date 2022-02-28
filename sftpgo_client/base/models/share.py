from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.share_scope import ShareScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="Share")


@attr.s(auto_attribs=True)
class Share:
    """
    Attributes:
        id (Union[Unset, str]): auto-generated unique share identifier
        name (Union[Unset, str]):
        description (Union[Unset, str]): optional description
        scope (Union[Unset, ShareScope]): Options:
              * `1` - read scope
              * `2` - write scope
        paths (Union[Unset, List[str]]): paths to files or directories, for share scope write this array must contain
            exactly one directory. Paths will not be validated on save so you can also create them after creating the share
            Example: ['/dir1', '/dir2/file.txt', '/dir3/subdir'].
        username (Union[Unset, str]):
        created_at (Union[Unset, int]): creation time as unix timestamp in milliseconds
        updated_at (Union[Unset, int]): last update time as unix timestamp in milliseconds
        last_use_at (Union[Unset, int]): last use time as unix timestamp in milliseconds
        expires_at (Union[Unset, int]): optional share expiration, as unix timestamp in milliseconds. 0 means no
            expiration
        password (Union[Unset, str]): optional password to protect the share. The special value "[**redacted**]" means
            that a password has been set, you can use this value if you want to preserve the current password when you
            update a share
        max_tokens (Union[Unset, int]): maximum allowed access tokens. 0 means no limit
        used_tokens (Union[Unset, int]):
        allow_from (Union[Unset, List[str]]): Limit the share availability to these IP/Mask. IP/Mask must be in CIDR
            notation as defined in RFC 4632 and RFC 4291, for example "192.0.2.0/24" or "2001:db8::/32". An empty list means
            no restrictions Example: ['192.0.2.0/24', '2001:db8::/32'].
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    scope: Union[Unset, ShareScope] = UNSET
    paths: Union[Unset, List[str]] = UNSET
    username: Union[Unset, str] = UNSET
    created_at: Union[Unset, int] = UNSET
    updated_at: Union[Unset, int] = UNSET
    last_use_at: Union[Unset, int] = UNSET
    expires_at: Union[Unset, int] = UNSET
    password: Union[Unset, str] = UNSET
    max_tokens: Union[Unset, int] = UNSET
    used_tokens: Union[Unset, int] = UNSET
    allow_from: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        scope: Union[Unset, int] = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        paths: Union[Unset, List[str]] = UNSET
        if not isinstance(self.paths, Unset):
            paths = self.paths

        username = self.username
        created_at = self.created_at
        updated_at = self.updated_at
        last_use_at = self.last_use_at
        expires_at = self.expires_at
        password = self.password
        max_tokens = self.max_tokens
        used_tokens = self.used_tokens
        allow_from: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allow_from, Unset):
            allow_from = self.allow_from

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if scope is not UNSET:
            field_dict["scope"] = scope
        if paths is not UNSET:
            field_dict["paths"] = paths
        if username is not UNSET:
            field_dict["username"] = username
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if last_use_at is not UNSET:
            field_dict["last_use_at"] = last_use_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if password is not UNSET:
            field_dict["password"] = password
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if used_tokens is not UNSET:
            field_dict["used_tokens"] = used_tokens
        if allow_from is not UNSET:
            field_dict["allow_from"] = allow_from

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: Union[Unset, ShareScope]
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = ShareScope(_scope)

        paths = cast(List[str], d.pop("paths", UNSET))

        username = d.pop("username", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        last_use_at = d.pop("last_use_at", UNSET)

        expires_at = d.pop("expires_at", UNSET)

        password = d.pop("password", UNSET)

        max_tokens = d.pop("max_tokens", UNSET)

        used_tokens = d.pop("used_tokens", UNSET)

        allow_from = cast(List[str], d.pop("allow_from", UNSET))

        share = cls(
            id=id,
            name=name,
            description=description,
            scope=scope,
            paths=paths,
            username=username,
            created_at=created_at,
            updated_at=updated_at,
            last_use_at=last_use_at,
            expires_at=expires_at,
            password=password,
            max_tokens=max_tokens,
            used_tokens=used_tokens,
            allow_from=allow_from,
        )

        share.additional_properties = d
        return share

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
