from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.event_conditions_fs_events_item import EventConditionsFsEventsItem
from ..models.event_conditions_provider_events_item import (
    EventConditionsProviderEventsItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.condition_options import ConditionOptions
    from ..models.schedule import Schedule


T = TypeVar("T", bound="EventConditions")


@attr.s(auto_attribs=True)
class EventConditions:
    """
    Attributes:
        fs_events (Union[Unset, List[EventConditionsFsEventsItem]]):
        provider_events (Union[Unset, List[EventConditionsProviderEventsItem]]):
        schedules (Union[Unset, List['Schedule']]):
        options (Union[Unset, ConditionOptions]):
    """

    fs_events: Union[Unset, List[EventConditionsFsEventsItem]] = UNSET
    provider_events: Union[Unset, List[EventConditionsProviderEventsItem]] = UNSET
    schedules: Union[Unset, List["Schedule"]] = UNSET
    options: Union[Unset, "ConditionOptions"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fs_events: Union[Unset, List[str]] = UNSET
        if not isinstance(self.fs_events, Unset):
            fs_events = []
            for fs_events_item_data in self.fs_events:
                fs_events_item = fs_events_item_data.value

                fs_events.append(fs_events_item)

        provider_events: Union[Unset, List[str]] = UNSET
        if not isinstance(self.provider_events, Unset):
            provider_events = []
            for provider_events_item_data in self.provider_events:
                provider_events_item = provider_events_item_data.value

                provider_events.append(provider_events_item)

        schedules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.schedules, Unset):
            schedules = []
            for schedules_item_data in self.schedules:
                schedules_item = schedules_item_data.to_dict()

                schedules.append(schedules_item)

        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fs_events is not UNSET:
            field_dict["fs_events"] = fs_events
        if provider_events is not UNSET:
            field_dict["provider_events"] = provider_events
        if schedules is not UNSET:
            field_dict["schedules"] = schedules
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.condition_options import ConditionOptions
        from ..models.schedule import Schedule

        d = src_dict.copy()
        fs_events = []
        _fs_events = d.pop("fs_events", UNSET)
        for fs_events_item_data in _fs_events or []:
            fs_events_item = EventConditionsFsEventsItem(fs_events_item_data)

            fs_events.append(fs_events_item)

        provider_events = []
        _provider_events = d.pop("provider_events", UNSET)
        for provider_events_item_data in _provider_events or []:
            provider_events_item = EventConditionsProviderEventsItem(
                provider_events_item_data
            )

            provider_events.append(provider_events_item)

        schedules = []
        _schedules = d.pop("schedules", UNSET)
        for schedules_item_data in _schedules or []:
            schedules_item = Schedule.from_dict(schedules_item_data)

            schedules.append(schedules_item)

        _options = d.pop("options", UNSET)
        options: Union[Unset, ConditionOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = ConditionOptions.from_dict(_options)

        event_conditions = cls(
            fs_events=fs_events,
            provider_events=provider_events,
            schedules=schedules,
            options=options,
        )

        event_conditions.additional_properties = d
        return event_conditions

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
