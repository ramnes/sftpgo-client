from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.folder_retention import FolderRetention


T = TypeVar("T", bound="EventActionDataRetentionConfig")


@attr.s(auto_attribs=True)
class EventActionDataRetentionConfig:
    """
    Attributes:
        folders (Union[Unset, List['FolderRetention']]):
    """

    folders: Union[Unset, List["FolderRetention"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        folders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.folders, Unset):
            folders = []
            for folders_item_data in self.folders:
                folders_item = folders_item_data.to_dict()

                folders.append(folders_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if folders is not UNSET:
            field_dict["folders"] = folders

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.folder_retention import FolderRetention

        d = src_dict.copy()
        folders = []
        _folders = d.pop("folders", UNSET)
        for folders_item_data in _folders or []:
            folders_item = FolderRetention.from_dict(folders_item_data)

            folders.append(folders_item)

        event_action_data_retention_config = cls(
            folders=folders,
        )

        event_action_data_retention_config.additional_properties = d
        return event_action_data_retention_config

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
