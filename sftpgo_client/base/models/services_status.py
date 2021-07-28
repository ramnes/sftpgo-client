from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.data_provider_status import DataProviderStatus
from ..models.ftp_service_status import FTPServiceStatus
from ..models.services_status_defender import ServicesStatusDefender
from ..models.ssh_service_status import SSHServiceStatus
from ..models.web_dav_service_status import WebDAVServiceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServicesStatus")


@attr.s(auto_attribs=True)
class ServicesStatus:
    """ """

    ssh: Union[Unset, SSHServiceStatus] = UNSET
    ftp: Union[Unset, FTPServiceStatus] = UNSET
    webdav: Union[Unset, WebDAVServiceStatus] = UNSET
    data_provider: Union[Unset, DataProviderStatus] = UNSET
    defender: Union[Unset, ServicesStatusDefender] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ssh: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ssh, Unset):
            ssh = self.ssh.to_dict()

        ftp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ftp, Unset):
            ftp = self.ftp.to_dict()

        webdav: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.webdav, Unset):
            webdav = self.webdav.to_dict()

        data_provider: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data_provider, Unset):
            data_provider = self.data_provider.to_dict()

        defender: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.defender, Unset):
            defender = self.defender.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ssh is not UNSET:
            field_dict["ssh"] = ssh
        if ftp is not UNSET:
            field_dict["ftp"] = ftp
        if webdav is not UNSET:
            field_dict["webdav"] = webdav
        if data_provider is not UNSET:
            field_dict["data_provider"] = data_provider
        if defender is not UNSET:
            field_dict["defender"] = defender

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _ssh = d.pop("ssh", UNSET)
        ssh: Union[Unset, SSHServiceStatus]
        if isinstance(_ssh, Unset):
            ssh = UNSET
        else:
            ssh = SSHServiceStatus.from_dict(_ssh)

        _ftp = d.pop("ftp", UNSET)
        ftp: Union[Unset, FTPServiceStatus]
        if isinstance(_ftp, Unset):
            ftp = UNSET
        else:
            ftp = FTPServiceStatus.from_dict(_ftp)

        _webdav = d.pop("webdav", UNSET)
        webdav: Union[Unset, WebDAVServiceStatus]
        if isinstance(_webdav, Unset):
            webdav = UNSET
        else:
            webdav = WebDAVServiceStatus.from_dict(_webdav)

        _data_provider = d.pop("data_provider", UNSET)
        data_provider: Union[Unset, DataProviderStatus]
        if isinstance(_data_provider, Unset):
            data_provider = UNSET
        else:
            data_provider = DataProviderStatus.from_dict(_data_provider)

        _defender = d.pop("defender", UNSET)
        defender: Union[Unset, ServicesStatusDefender]
        if isinstance(_defender, Unset):
            defender = UNSET
        else:
            defender = ServicesStatusDefender.from_dict(_defender)

        services_status = cls(
            ssh=ssh,
            ftp=ftp,
            webdav=webdav,
            data_provider=data_provider,
            defender=defender,
        )

        services_status.additional_properties = d
        return services_status

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
