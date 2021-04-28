from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.azure_blob_fs_config import AzureBlobFsConfig
from ..models.crypt_fs_config import CryptFsConfig
from ..models.filesystem_config_provider import FilesystemConfigProvider
from ..models.gcs_config import GCSConfig
from ..models.s3_config import S3Config
from ..models.sftp_fs_config import SFTPFsConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="FilesystemConfig")


@attr.s(auto_attribs=True)
class FilesystemConfig:
    """Storage filesystem details"""

    provider: Union[Unset, FilesystemConfigProvider] = UNSET
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
        provider: Union[Unset, FilesystemConfigProvider] = UNSET
        _provider = d.pop("provider", UNSET)
        if not isinstance(_provider, Unset):
            provider = FilesystemConfigProvider(_provider)

        s3config: Union[Unset, S3Config] = UNSET
        _s3config = d.pop("s3config", UNSET)
        if not isinstance(_s3config, Unset):
            s3config = S3Config.from_dict(_s3config)

        gcsconfig: Union[Unset, GCSConfig] = UNSET
        _gcsconfig = d.pop("gcsconfig", UNSET)
        if not isinstance(_gcsconfig, Unset):
            gcsconfig = GCSConfig.from_dict(_gcsconfig)

        azblobconfig: Union[Unset, AzureBlobFsConfig] = UNSET
        _azblobconfig = d.pop("azblobconfig", UNSET)
        if not isinstance(_azblobconfig, Unset):
            azblobconfig = AzureBlobFsConfig.from_dict(_azblobconfig)

        cryptconfig: Union[Unset, CryptFsConfig] = UNSET
        _cryptconfig = d.pop("cryptconfig", UNSET)
        if not isinstance(_cryptconfig, Unset):
            cryptconfig = CryptFsConfig.from_dict(_cryptconfig)

        sftpconfig: Union[Unset, SFTPFsConfig] = UNSET
        _sftpconfig = d.pop("sftpconfig", UNSET)
        if not isinstance(_sftpconfig, Unset):
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
