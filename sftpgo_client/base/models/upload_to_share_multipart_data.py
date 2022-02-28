import json
from io import BytesIO
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="UploadToShareMultipartData")


@attr.s(auto_attribs=True)
class UploadToShareMultipartData:
    """
    Attributes:
        filenames (Union[Unset, List[File]]):
    """

    filenames: Union[Unset, List[File]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filenames: Union[Unset, List[FileJsonType]] = UNSET
        if not isinstance(self.filenames, Unset):
            filenames = []
            for filenames_item_data in self.filenames:
                filenames_item = filenames_item_data.to_tuple()

                filenames.append(filenames_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filenames is not UNSET:
            field_dict["filenames"] = filenames

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        filenames: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.filenames, Unset):
            _temp_filenames = []
            for filenames_item_data in self.filenames:
                filenames_item = filenames_item_data.to_tuple()

                _temp_filenames.append(filenames_item)
            filenames = (None, json.dumps(_temp_filenames).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                key: (None, str(value).encode(), "text/plain")
                for key, value in self.additional_properties.items()
            }
        )
        field_dict.update({})
        if filenames is not UNSET:
            field_dict["filenames"] = filenames

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        filenames = []
        _filenames = d.pop("filenames", UNSET)
        for filenames_item_data in _filenames or []:
            filenames_item = File(payload=BytesIO(filenames_item_data))

            filenames.append(filenames_item)

        upload_to_share_multipart_data = cls(
            filenames=filenames,
        )

        upload_to_share_multipart_data.additional_properties = d
        return upload_to_share_multipart_data

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
