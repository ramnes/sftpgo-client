import json
from io import BytesIO
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="CreateUserFilesMultipartData")


@attr.s(auto_attribs=True)
class CreateUserFilesMultipartData:
    """ """

    filename: Union[Unset, List[File]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filename: Union[Unset, List[FileJsonType]] = UNSET
        if not isinstance(self.filename, Unset):
            filename = []
            for filename_item_data in self.filename:
                filename_item = filename_item_data.to_tuple()

                filename.append(filename_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filename is not UNSET:
            field_dict["filename"] = filename

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        filename: Union[Unset, Tuple[None, str, str]] = UNSET
        if not isinstance(self.filename, Unset):
            _temp_filename = []
            for filename_item_data in self.filename:
                filename_item = filename_item_data.to_tuple()

                _temp_filename.append(filename_item)
            filename = (None, json.dumps(_temp_filename), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                key: (None, str(value), "text/plain")
                for key, value in self.additional_properties.items()
            }
        )
        field_dict.update({})
        if filename is not UNSET:
            field_dict["filename"] = filename

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        filename = []
        _filename = d.pop("filename", UNSET)
        for filename_item_data in _filename or []:
            filename_item = File(payload=BytesIO(filename_item_data))

            filename.append(filename_item)

        create_user_files_multipart_data = cls(
            filename=filename,
        )

        create_user_files_multipart_data.additional_properties = d
        return create_user_files_multipart_data

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
