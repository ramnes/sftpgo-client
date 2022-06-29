from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.azure_blob_fs_config_access_tier import AzureBlobFsConfigAccessTier
from ..models.secret import Secret
from ..types import UNSET, Unset

T = TypeVar("T", bound="AzureBlobFsConfig")


@attr.s(auto_attribs=True)
class AzureBlobFsConfig:
    """Azure Blob Storage configuration details

    Attributes:
        container (Union[Unset, str]):
        account_name (Union[Unset, str]): Storage Account Name, leave blank to use SAS URL
        account_key (Union[Unset, Secret]): The secret is encrypted before saving, so to set a new secret you must
            provide a payload and set the status to "Plain". The encryption key and additional data will be generated
            automatically. If you set the status to "Redacted" the existing secret will be preserved
        sas_url (Union[Unset, Secret]): The secret is encrypted before saving, so to set a new secret you must provide a
            payload and set the status to "Plain". The encryption key and additional data will be generated automatically.
            If you set the status to "Redacted" the existing secret will be preserved
        endpoint (Union[Unset, str]): optional endpoint. Default is "blob.core.windows.net". If you use the emulator the
            endpoint must include the protocol, for example "http://127.0.0.1:10000"
        upload_part_size (Union[Unset, int]): the buffer size (in MB) to use for multipart uploads. If this value is set
            to zero, the default value (5MB) will be used.
        upload_concurrency (Union[Unset, int]): the number of parts to upload in parallel. If this value is set to zero,
            the default value (5) will be used
        download_part_size (Union[Unset, int]): the buffer size (in MB) to use for multipart downloads. If this value is
            set to zero, the default value (5MB) will be used.
        download_concurrency (Union[Unset, int]): the number of parts to download in parallel. If this value is set to
            zero, the default value (5) will be used
        access_tier (Union[Unset, AzureBlobFsConfigAccessTier]):
        key_prefix (Union[Unset, str]): key_prefix is similar to a chroot directory for a local filesystem. If specified
            the user will only see contents that starts with this prefix and so you can restrict access to a specific
            virtual folder. The prefix, if not empty, must not start with "/" and must end with "/". If empty the whole
            container contents will be available Example: folder/subfolder/.
        use_emulator (Union[Unset, bool]):
    """

    container: Union[Unset, str] = UNSET
    account_name: Union[Unset, str] = UNSET
    account_key: Union[Unset, Secret] = UNSET
    sas_url: Union[Unset, Secret] = UNSET
    endpoint: Union[Unset, str] = UNSET
    upload_part_size: Union[Unset, int] = UNSET
    upload_concurrency: Union[Unset, int] = UNSET
    download_part_size: Union[Unset, int] = UNSET
    download_concurrency: Union[Unset, int] = UNSET
    access_tier: Union[Unset, AzureBlobFsConfigAccessTier] = UNSET
    key_prefix: Union[Unset, str] = UNSET
    use_emulator: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        container = self.container
        account_name = self.account_name
        account_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_key, Unset):
            account_key = self.account_key.to_dict()

        sas_url: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sas_url, Unset):
            sas_url = self.sas_url.to_dict()

        endpoint = self.endpoint
        upload_part_size = self.upload_part_size
        upload_concurrency = self.upload_concurrency
        download_part_size = self.download_part_size
        download_concurrency = self.download_concurrency
        access_tier: Union[Unset, str] = UNSET
        if not isinstance(self.access_tier, Unset):
            access_tier = self.access_tier.value

        key_prefix = self.key_prefix
        use_emulator = self.use_emulator

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if container is not UNSET:
            field_dict["container"] = container
        if account_name is not UNSET:
            field_dict["account_name"] = account_name
        if account_key is not UNSET:
            field_dict["account_key"] = account_key
        if sas_url is not UNSET:
            field_dict["sas_url"] = sas_url
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if upload_part_size is not UNSET:
            field_dict["upload_part_size"] = upload_part_size
        if upload_concurrency is not UNSET:
            field_dict["upload_concurrency"] = upload_concurrency
        if download_part_size is not UNSET:
            field_dict["download_part_size"] = download_part_size
        if download_concurrency is not UNSET:
            field_dict["download_concurrency"] = download_concurrency
        if access_tier is not UNSET:
            field_dict["access_tier"] = access_tier
        if key_prefix is not UNSET:
            field_dict["key_prefix"] = key_prefix
        if use_emulator is not UNSET:
            field_dict["use_emulator"] = use_emulator

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        container = d.pop("container", UNSET)

        account_name = d.pop("account_name", UNSET)

        _account_key = d.pop("account_key", UNSET)
        account_key: Union[Unset, Secret]
        if isinstance(_account_key, Unset):
            account_key = UNSET
        else:
            account_key = Secret.from_dict(_account_key)

        _sas_url = d.pop("sas_url", UNSET)
        sas_url: Union[Unset, Secret]
        if isinstance(_sas_url, Unset):
            sas_url = UNSET
        else:
            sas_url = Secret.from_dict(_sas_url)

        endpoint = d.pop("endpoint", UNSET)

        upload_part_size = d.pop("upload_part_size", UNSET)

        upload_concurrency = d.pop("upload_concurrency", UNSET)

        download_part_size = d.pop("download_part_size", UNSET)

        download_concurrency = d.pop("download_concurrency", UNSET)

        _access_tier = d.pop("access_tier", UNSET)
        access_tier: Union[Unset, AzureBlobFsConfigAccessTier]
        if isinstance(_access_tier, Unset):
            access_tier = UNSET
        else:
            access_tier = AzureBlobFsConfigAccessTier(_access_tier)

        key_prefix = d.pop("key_prefix", UNSET)

        use_emulator = d.pop("use_emulator", UNSET)

        azure_blob_fs_config = cls(
            container=container,
            account_name=account_name,
            account_key=account_key,
            sas_url=sas_url,
            endpoint=endpoint,
            upload_part_size=upload_part_size,
            upload_concurrency=upload_concurrency,
            download_part_size=download_part_size,
            download_concurrency=download_concurrency,
            access_tier=access_tier,
            key_prefix=key_prefix,
            use_emulator=use_emulator,
        )

        azure_blob_fs_config.additional_properties = d
        return azure_blob_fs_config

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
