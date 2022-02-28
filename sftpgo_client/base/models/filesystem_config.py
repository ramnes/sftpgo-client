from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.azure_blob_fs_config import AzureBlobFsConfig
from ..models.crypt_fs_config import CryptFsConfig
from ..models.fs_providers import FsProviders
from ..models.gcs_config import GCSConfig
from ..models.s3_config import S3Config
from ..models.sftp_fs_config import SFTPFsConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="FilesystemConfig")


@attr.s(auto_attribs=True)
class FilesystemConfig:
    """Storage filesystem details

    Attributes:
        provider (Union[Unset, FsProviders]): Filesystem providers:
              * `0` - Local filesystem
              * `1` - S3 Compatible Object Storage
              * `2` - Google Cloud Storage
              * `3` - Azure Blob Storage
              * `4` - Local filesystem encrypted
              * `5` - SFTP
        s3config (Union[Unset, S3Config]): S3 Compatible Object Storage configuration details
        gcsconfig (Union[Unset, GCSConfig]): Google Cloud Storage configuration details. The "credentials" field must be
            populated only when adding/updating a user. It will be always omitted, since there are sensitive data, when you
            search/get users
        azblobconfig (Union[Unset, AzureBlobFsConfig]): Azure Blob Storage configuration details
        cryptconfig (Union[Unset, CryptFsConfig]): Crypt filesystem configuration details
        sftpconfig (Union[Unset, SFTPFsConfig]):
    """

    provider: Union[Unset, FsProviders] = UNSET
    s3config: Union[Unset, S3Config] = UNSET
    gcsconfig: Union[Unset, GCSConfig] = UNSET
    azblobconfig: Union[Unset, AzureBlobFsConfig] = UNSET
    cryptconfig: Union[Unset, CryptFsConfig] = UNSET
    sftpconfig: Union[Unset, SFTPFsConfig] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider: Union[Unset, int] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        s3config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.s3config, Unset):
            s3config = self.s3config.to_dict()

        gcsconfig: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gcsconfig, Unset):
            gcsconfig = self.gcsconfig.to_dict()

        azblobconfig: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.azblobconfig, Unset):
            azblobconfig = self.azblobconfig.to_dict()

        cryptconfig: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cryptconfig, Unset):
            cryptconfig = self.cryptconfig.to_dict()

        sftpconfig: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sftpconfig, Unset):
            sftpconfig = self.sftpconfig.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider is not UNSET:
            field_dict["provider"] = provider
        if s3config is not UNSET:
            field_dict["s3config"] = s3config
        if gcsconfig is not UNSET:
            field_dict["gcsconfig"] = gcsconfig
        if azblobconfig is not UNSET:
            field_dict["azblobconfig"] = azblobconfig
        if cryptconfig is not UNSET:
            field_dict["cryptconfig"] = cryptconfig
        if sftpconfig is not UNSET:
            field_dict["sftpconfig"] = sftpconfig

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, FsProviders]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = FsProviders(_provider)

        _s3config = d.pop("s3config", UNSET)
        s3config: Union[Unset, S3Config]
        if isinstance(_s3config, Unset):
            s3config = UNSET
        else:
            s3config = S3Config.from_dict(_s3config)

        _gcsconfig = d.pop("gcsconfig", UNSET)
        gcsconfig: Union[Unset, GCSConfig]
        if isinstance(_gcsconfig, Unset):
            gcsconfig = UNSET
        else:
            gcsconfig = GCSConfig.from_dict(_gcsconfig)

        _azblobconfig = d.pop("azblobconfig", UNSET)
        azblobconfig: Union[Unset, AzureBlobFsConfig]
        if isinstance(_azblobconfig, Unset):
            azblobconfig = UNSET
        else:
            azblobconfig = AzureBlobFsConfig.from_dict(_azblobconfig)

        _cryptconfig = d.pop("cryptconfig", UNSET)
        cryptconfig: Union[Unset, CryptFsConfig]
        if isinstance(_cryptconfig, Unset):
            cryptconfig = UNSET
        else:
            cryptconfig = CryptFsConfig.from_dict(_cryptconfig)

        _sftpconfig = d.pop("sftpconfig", UNSET)
        sftpconfig: Union[Unset, SFTPFsConfig]
        if isinstance(_sftpconfig, Unset):
            sftpconfig = UNSET
        else:
            sftpconfig = SFTPFsConfig.from_dict(_sftpconfig)

        filesystem_config = cls(
            provider=provider,
            s3config=s3config,
            gcsconfig=gcsconfig,
            azblobconfig=azblobconfig,
            cryptconfig=cryptconfig,
            sftpconfig=sftpconfig,
        )

        filesystem_config.additional_properties = d
        return filesystem_config

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
