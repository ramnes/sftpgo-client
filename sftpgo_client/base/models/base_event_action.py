from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.event_action_types import EventActionTypes
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_event_action_options import BaseEventActionOptions


T = TypeVar("T", bound="BaseEventAction")


@attr.s(auto_attribs=True)
class BaseEventAction:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]): unique name
        description (Union[Unset, str]): optional description
        type (Union[Unset, EventActionTypes]): Supported event action types:
              * `1` - HTTP
              * `2` - Command
              * `3` - Email
              * `4` - Backup
              * `5` - User quota reset
              * `6` - Folder quota reset
              * `7` - Transfer quota reset
              * `8` - Data retention check
              * `9` - Filesystem
        options (Union[Unset, BaseEventActionOptions]):
        rules (Union[Unset, List[str]]): list of event rules names associated with this action
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    type: Union[Unset, EventActionTypes] = UNSET
    options: Union[Unset, "BaseEventActionOptions"] = UNSET
    rules: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        type: Union[Unset, int] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        rules: Union[Unset, List[str]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if type is not UNSET:
            field_dict["type"] = type
        if options is not UNSET:
            field_dict["options"] = options
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.base_event_action_options import BaseEventActionOptions

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, EventActionTypes]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = EventActionTypes(_type)

        _options = d.pop("options", UNSET)
        options: Union[Unset, BaseEventActionOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = BaseEventActionOptions.from_dict(_options)

        rules = cast(List[str], d.pop("rules", UNSET))

        base_event_action = cls(
            id=id,
            name=name,
            description=description,
            type=type,
            options=options,
            rules=rules,
        )

        base_event_action.additional_properties = d
        return base_event_action

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
