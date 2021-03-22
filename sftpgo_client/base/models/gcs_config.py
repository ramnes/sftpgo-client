from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.gcs_config_automatic_credentials import GCSConfigAutomaticCredentials
from ..models.secret import Secret
from ..types import UNSET, Unset

T = TypeVar("T", bound="GCSConfig")


@attr.s(auto_attribs=True)
class GCSConfig:
    """ Google Cloud Storage configuration details. The "credentials" field must be populated only when adding/updating a user. It will be always omitted, since there are sensitive data, when you search/get users """

    bucket: Union[Unset, str] = UNSET
    credentials: Union[Unset, Secret] = UNSET
    automatic_credentials: Union[Unset, GCSConfigAutomaticCredentials] = UNSET
    storage_class: Union[Unset, str] = UNSET
    key_prefix: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bucket = self.bucket
        credentials: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        automatic_credentials: Union[Unset, int] = UNSET
        if not isinstance(self.automatic_credentials, Unset):
            automatic_credentials = self.automatic_credentials.value

        storage_class = self.storage_class
        key_prefix = self.key_prefix

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if automatic_credentials is not UNSET:
            field_dict["automatic_credentials"] = automatic_credentials
        if storage_class is not UNSET:
            field_dict["storage_class"] = storage_class
        if key_prefix is not UNSET:
            field_dict["key_prefix"] = key_prefix

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bucket = d.pop("bucket", UNSET)

        credentials: Union[Unset, Secret] = UNSET
        _credentials = d.pop("credentials", UNSET)
        if not isinstance(_credentials, Unset):
            credentials = Secret.from_dict(_credentials)

        automatic_credentials: Union[Unset, GCSConfigAutomaticCredentials] = UNSET
        _automatic_credentials = d.pop("automatic_credentials", UNSET)
        if not isinstance(_automatic_credentials, Unset):
            automatic_credentials = GCSConfigAutomaticCredentials(
                _automatic_credentials
            )

        storage_class = d.pop("storage_class", UNSET)

        key_prefix = d.pop("key_prefix", UNSET)

        gcs_config = cls(
            bucket=bucket,
            credentials=credentials,
            automatic_credentials=automatic_credentials,
            storage_class=storage_class,
            key_prefix=key_prefix,
        )

        gcs_config.additional_properties = d
        return gcs_config

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
