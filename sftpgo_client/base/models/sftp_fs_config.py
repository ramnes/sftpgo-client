from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.secret import Secret
from ..types import UNSET, Unset

T = TypeVar("T", bound="SFTPFsConfig")


@attr.s(auto_attribs=True)
class SFTPFsConfig:
    """ """

    endpoint: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    password: Union[Unset, Secret] = UNSET
    private_key: Union[Unset, Secret] = UNSET
    fingerprints: Union[Unset, List[str]] = UNSET
    prefix: Union[Unset, str] = UNSET
    disable_concurrent_reads: Union[Unset, bool] = UNSET
    buffer_size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        endpoint = self.endpoint
        username = self.username
        password: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.password, Unset):
            password = self.password.to_dict()

        private_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.private_key, Unset):
            private_key = self.private_key.to_dict()

        fingerprints: Union[Unset, List[str]] = UNSET
        if not isinstance(self.fingerprints, Unset):
            fingerprints = self.fingerprints

        prefix = self.prefix
        disable_concurrent_reads = self.disable_concurrent_reads
        buffer_size = self.buffer_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if private_key is not UNSET:
            field_dict["private_key"] = private_key
        if fingerprints is not UNSET:
            field_dict["fingerprints"] = fingerprints
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if disable_concurrent_reads is not UNSET:
            field_dict["disable_concurrent_reads"] = disable_concurrent_reads
        if buffer_size is not UNSET:
            field_dict["buffer_size"] = buffer_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        endpoint = d.pop("endpoint", UNSET)

        username = d.pop("username", UNSET)

        _password = d.pop("password", UNSET)
        password: Union[Unset, Secret]
        if isinstance(_password, Unset):
            password = UNSET
        else:
            password = Secret.from_dict(_password)

        _private_key = d.pop("private_key", UNSET)
        private_key: Union[Unset, Secret]
        if isinstance(_private_key, Unset):
            private_key = UNSET
        else:
            private_key = Secret.from_dict(_private_key)

        fingerprints = cast(List[str], d.pop("fingerprints", UNSET))

        prefix = d.pop("prefix", UNSET)

        disable_concurrent_reads = d.pop("disable_concurrent_reads", UNSET)

        buffer_size = d.pop("buffer_size", UNSET)

        sftp_fs_config = cls(
            endpoint=endpoint,
            username=username,
            password=password,
            private_key=private_key,
            fingerprints=fingerprints,
            prefix=prefix,
            disable_concurrent_reads=disable_concurrent_reads,
            buffer_size=buffer_size,
        )

        sftp_fs_config.additional_properties = d
        return sftp_fs_config

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
