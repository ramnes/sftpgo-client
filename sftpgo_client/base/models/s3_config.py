from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.secret import Secret
from ..types import UNSET, Unset

T = TypeVar("T", bound="S3Config")


@attr.s(auto_attribs=True)
class S3Config:
    """S3 Compatible Object Storage configuration details

    Attributes:
        bucket (Union[Unset, str]):
        region (Union[Unset, str]):
        access_key (Union[Unset, str]):
        access_secret (Union[Unset, Secret]): The secret is encrypted before saving, so to set a new secret you must
            provide a payload and set the status to "Plain". The encryption key and additional data will be generated
            automatically. If you set the status to "Redacted" the existing secret will be preserved
        role_arn (Union[Unset, str]): Optional IAM Role ARN to assume
        endpoint (Union[Unset, str]): optional endpoint
        storage_class (Union[Unset, str]):
        acl (Union[Unset, str]): The canned ACL to apply to uploaded objects. Leave empty to use the default ACL. For
            more information and available ACLs, see here: https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-
            overview.html#canned-acl
        upload_part_size (Union[Unset, int]): the buffer size (in MB) to use for multipart uploads. The minimum allowed
            part size is 5MB, and if this value is set to zero, the default value (5MB) for the AWS SDK will be used. The
            minimum allowed value is 5.
        upload_concurrency (Union[Unset, int]): the number of parts to upload in parallel. If this value is set to zero,
            the default value (5) will be used
        upload_part_max_time (Union[Unset, int]): the maximum time allowed, in seconds, to upload a single chunk (the
            chunk size is defined via "upload_part_size"). 0 means no timeout
        download_part_size (Union[Unset, int]): the buffer size (in MB) to use for multipart downloads. The minimum
            allowed part size is 5MB, and if this value is set to zero, the default value (5MB) for the AWS SDK will be
            used. The minimum allowed value is 5. Ignored for partial downloads
        download_concurrency (Union[Unset, int]): the number of parts to download in parallel. If this value is set to
            zero, the default value (5) will be used. Ignored for partial downloads
        download_part_max_time (Union[Unset, int]): the maximum time allowed, in seconds, to download a single chunk
            (the chunk size is defined via "download_part_size"). 0 means no timeout. Ignored for partial downloads.
        force_path_style (Union[Unset, bool]): Set this to "true" to force the request to use path-style addressing,
            i.e., "http://s3.amazonaws.com/BUCKET/KEY". By default, the S3 client will use virtual hosted bucket addressing
            when possible ("http://BUCKET.s3.amazonaws.com/KEY")
        key_prefix (Union[Unset, str]): key_prefix is similar to a chroot directory for a local filesystem. If specified
            the user will only see contents that starts with this prefix and so you can restrict access to a specific
            virtual folder. The prefix, if not empty, must not start with "/" and must end with "/". If empty the whole
            bucket contents will be available Example: folder/subfolder/.
    """

    bucket: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    access_key: Union[Unset, str] = UNSET
    access_secret: Union[Unset, Secret] = UNSET
    role_arn: Union[Unset, str] = UNSET
    endpoint: Union[Unset, str] = UNSET
    storage_class: Union[Unset, str] = UNSET
    acl: Union[Unset, str] = UNSET
    upload_part_size: Union[Unset, int] = UNSET
    upload_concurrency: Union[Unset, int] = UNSET
    upload_part_max_time: Union[Unset, int] = UNSET
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

        role_arn = self.role_arn
        endpoint = self.endpoint
        storage_class = self.storage_class
        acl = self.acl
        upload_part_size = self.upload_part_size
        upload_concurrency = self.upload_concurrency
        upload_part_max_time = self.upload_part_max_time
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
        if role_arn is not UNSET:
            field_dict["role_arn"] = role_arn
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if storage_class is not UNSET:
            field_dict["storage_class"] = storage_class
        if acl is not UNSET:
            field_dict["acl"] = acl
        if upload_part_size is not UNSET:
            field_dict["upload_part_size"] = upload_part_size
        if upload_concurrency is not UNSET:
            field_dict["upload_concurrency"] = upload_concurrency
        if upload_part_max_time is not UNSET:
            field_dict["upload_part_max_time"] = upload_part_max_time
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

        role_arn = d.pop("role_arn", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        storage_class = d.pop("storage_class", UNSET)

        acl = d.pop("acl", UNSET)

        upload_part_size = d.pop("upload_part_size", UNSET)

        upload_concurrency = d.pop("upload_concurrency", UNSET)

        upload_part_max_time = d.pop("upload_part_max_time", UNSET)

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
            role_arn=role_arn,
            endpoint=endpoint,
            storage_class=storage_class,
            acl=acl,
            upload_part_size=upload_part_size,
            upload_concurrency=upload_concurrency,
            upload_part_max_time=upload_part_max_time,
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
