from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.filesystem_action_types import FilesystemActionTypes
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_action_fs_compress import EventActionFsCompress
    from ..models.key_value import KeyValue


T = TypeVar("T", bound="EventActionFilesystemConfig")


@attr.s(auto_attribs=True)
class EventActionFilesystemConfig:
    """
    Attributes:
        type (Union[Unset, FilesystemActionTypes]): Supported filesystem action types:
              * `1` - Rename
              * `2` - Delete
              * `3` - Mkdis
              * `4` - Exist
        renames (Union[Unset, List['KeyValue']]):
        mkdirs (Union[Unset, List[str]]):
        deletes (Union[Unset, List[str]]):
        exist (Union[Unset, List[str]]):
        compress (Union[Unset, EventActionFsCompress]):
    """

    type: Union[Unset, FilesystemActionTypes] = UNSET
    renames: Union[Unset, List["KeyValue"]] = UNSET
    mkdirs: Union[Unset, List[str]] = UNSET
    deletes: Union[Unset, List[str]] = UNSET
    exist: Union[Unset, List[str]] = UNSET
    compress: Union[Unset, "EventActionFsCompress"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        renames: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.renames, Unset):
            renames = []
            for renames_item_data in self.renames:
                renames_item = renames_item_data.to_dict()

                renames.append(renames_item)

        mkdirs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.mkdirs, Unset):
            mkdirs = self.mkdirs

        deletes: Union[Unset, List[str]] = UNSET
        if not isinstance(self.deletes, Unset):
            deletes = self.deletes

        exist: Union[Unset, List[str]] = UNSET
        if not isinstance(self.exist, Unset):
            exist = self.exist

        compress: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.compress, Unset):
            compress = self.compress.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if renames is not UNSET:
            field_dict["renames"] = renames
        if mkdirs is not UNSET:
            field_dict["mkdirs"] = mkdirs
        if deletes is not UNSET:
            field_dict["deletes"] = deletes
        if exist is not UNSET:
            field_dict["exist"] = exist
        if compress is not UNSET:
            field_dict["compress"] = compress

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event_action_fs_compress import EventActionFsCompress
        from ..models.key_value import KeyValue

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, FilesystemActionTypes]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = FilesystemActionTypes(_type)

        renames = []
        _renames = d.pop("renames", UNSET)
        for renames_item_data in _renames or []:
            renames_item = KeyValue.from_dict(renames_item_data)

            renames.append(renames_item)

        mkdirs = cast(List[str], d.pop("mkdirs", UNSET))

        deletes = cast(List[str], d.pop("deletes", UNSET))

        exist = cast(List[str], d.pop("exist", UNSET))

        _compress = d.pop("compress", UNSET)
        compress: Union[Unset, EventActionFsCompress]
        if isinstance(_compress, Unset):
            compress = UNSET
        else:
            compress = EventActionFsCompress.from_dict(_compress)

        event_action_filesystem_config = cls(
            type=type,
            renames=renames,
            mkdirs=mkdirs,
            deletes=deletes,
            exist=exist,
            compress=compress,
        )

        event_action_filesystem_config.additional_properties = d
        return event_action_filesystem_config

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
