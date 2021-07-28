from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.secret import Secret
from ..types import UNSET, Unset

T = TypeVar("T", bound="S3Config")


@attr.s(auto_attribs=True)
class S3Config:
    """S3 Compatible Object Storage configuration details"""

    bucket: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    access_key: Union[Unset, str] = UNSET
    access_secret: Union[Unset, Secret] = UNSET
    endpoint: Union[Unset, str] = UNSET
    storage_class: Union[Unset, str] = UNSET
    upload_part_size: Union[Unset, int] = UNSET
    upload_concurrency: Union[Unset, int] = UNSET
    download_part_size: Union[Unset, int] = UNSET
    download_concurrency: Union[Unset, int] = UNSET
    download_part_max_time: Union[Unset, int] = UNSET
    force_path_style: Union[Unset, bool] = UNSET
    key_prefix: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        bucket = self.bucket
        region = self.region
        access_key = self.access_key
        access_secret: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.access_secret, Unset):
            access_secret = self.access_secret.to_dict()

        endpoint = self.endpoint
        storage_class = self.storage_class
        upload_part_size = self.upload_part_size
        upload_concurrency = self.upload_concurrency
        download_part_size = self.download_part_size
        download_concurrency = self.download_concurrency
        download_part_max_time = self.download_part_max_time
        force_path_style = self.force_path_style
        key_prefix = self.key_prefix

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket is not UNSET:
            field_dict["bucket"] = bucket
        if region is not UNSET:
            field_dict["region"] = region
        if access_key is not UNSET:
            field_dict["access_key"] = access_key
        if access_secret is not UNSET:
            field_dict["access_secret"] = access_secret
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if storage_class is not UNSET:
            field_dict["storage_class"] = storage_class
        if upload_part_size is not UNSET:
            field_dict["upload_part_size"] = upload_part_size
        if upload_concurrency is not UNSET:
            field_dict["upload_concurrency"] = upload_concurrency
        if download_part_size is not UNSET:
            field_dict["download_part_size"] = download_part_size
        if download_concurrency is not UNSET:
            field_dict["download_concurrency"] = download_concurrency
        if download_part_max_time is not UNSET:
            field_dict["download_part_max_time"] = download_part_max_time
        if force_path_style is not UNSET:
            field_dict["force_path_style"] = force_path_style
        if key_prefix is not UNSET:
            field_dict["key_prefix"] = key_prefix

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        bucket = d.pop("bucket", UNSET)

        region = d.pop("region", UNSET)

        access_key = d.pop("access_key", UNSET)

        _access_secret = d.pop("access_secret", UNSET)
        access_secret: Union[Unset, Secret]
        if isinstance(_access_secret, Unset):
            access_secret = UNSET
        else:
            access_secret = Secret.from_dict(_access_secret)

        endpoint = d.pop("endpoint", UNSET)

        storage_class = d.pop("storage_class", UNSET)

        upload_part_size = d.pop("upload_part_size", UNSET)

        upload_concurrency = d.pop("upload_concurrency", UNSET)

        download_part_size = d.pop("download_part_size", UNSET)

        download_concurrency = d.pop("download_concurrency", UNSET)

        download_part_max_time = d.pop("download_part_max_time", UNSET)

        force_path_style = d.pop("force_path_style", UNSET)

        key_prefix = d.pop("key_prefix", UNSET)

        s3_config = cls(
            bucket=bucket,
            region=region,
            access_key=access_key,
            access_secret=access_secret,
            endpoint=endpoint,
            storage_class=storage_class,
            upload_part_size=upload_part_size,
            upload_concurrency=upload_concurrency,
            download_part_size=download_part_size,
            download_concurrency=download_concurrency,
            download_part_max_time=download_part_max_time,
            force_path_style=force_path_style,
            key_prefix=key_prefix,
        )

        s3_config.additional_properties = d
        return s3_config

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
