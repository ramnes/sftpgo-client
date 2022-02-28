from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataTransferLimit")


@attr.s(auto_attribs=True)
class DataTransferLimit:
    """
    Attributes:
        sources (Union[Unset, List[str]]): Source networks in CIDR notation as defined in RFC 4632 and RFC 4291 for
            example `192.0.2.0/24` or `2001:db8::/32`. The limit applies if the defined networks contain the client IP
        upload_data_transfer (Union[Unset, int]): Maximum data transfer allowed for uploads as MB. 0 means no limit
        download_data_transfer (Union[Unset, int]): Maximum data transfer allowed for downloads as MB. 0 means no limit
        total_data_transfer (Union[Unset, int]): Maximum total data transfer as MB. 0 means unlimited. You can set a
            total data transfer instead of the individual values for uploads and downloads
    """

    sources: Union[Unset, List[str]] = UNSET
    upload_data_transfer: Union[Unset, int] = UNSET
    download_data_transfer: Union[Unset, int] = UNSET
    total_data_transfer: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sources: Union[Unset, List[str]] = UNSET
        if not isinstance(self.sources, Unset):
            sources = self.sources

        upload_data_transfer = self.upload_data_transfer
        download_data_transfer = self.download_data_transfer
        total_data_transfer = self.total_data_transfer

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sources is not UNSET:
            field_dict["sources"] = sources
        if upload_data_transfer is not UNSET:
            field_dict["upload_data_transfer"] = upload_data_transfer
        if download_data_transfer is not UNSET:
            field_dict["download_data_transfer"] = download_data_transfer
        if total_data_transfer is not UNSET:
            field_dict["total_data_transfer"] = total_data_transfer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sources = cast(List[str], d.pop("sources", UNSET))

        upload_data_transfer = d.pop("upload_data_transfer", UNSET)

        download_data_transfer = d.pop("download_data_transfer", UNSET)

        total_data_transfer = d.pop("total_data_transfer", UNSET)

        data_transfer_limit = cls(
            sources=sources,
            upload_data_transfer=upload_data_transfer,
            download_data_transfer=download_data_transfer,
            total_data_transfer=total_data_transfer,
        )

        data_transfer_limit.additional_properties = d
        return data_transfer_limit

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
