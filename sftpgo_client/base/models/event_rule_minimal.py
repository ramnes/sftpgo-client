from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.event_trigger_types import EventTriggerTypes
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_action_minimal import EventActionMinimal
    from ..models.event_conditions import EventConditions


T = TypeVar("T", bound="EventRuleMinimal")


@attr.s(auto_attribs=True)
class EventRuleMinimal:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]): unique name
        description (Union[Unset, str]): optional description
        created_at (Union[Unset, int]): creation time as unix timestamp in milliseconds
        updated_at (Union[Unset, int]): last update time as unix timestamp in millisecond
        trigger (Union[Unset, EventTriggerTypes]): Supported event trigger types:
              * `1` - Filesystem event
              * `2` - Provider event
              * `3` - Schedule
              * `4` - IP blocked
              * `5` - Certificate renewal
        conditions (Union[Unset, EventConditions]):
        actions (Union[Unset, List['EventActionMinimal']]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    created_at: Union[Unset, int] = UNSET
    updated_at: Union[Unset, int] = UNSET
    trigger: Union[Unset, EventTriggerTypes] = UNSET
    conditions: Union[Unset, "EventConditions"] = UNSET
    actions: Union[Unset, List["EventActionMinimal"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        created_at = self.created_at
        updated_at = self.updated_at
        trigger: Union[Unset, int] = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value

        conditions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = self.conditions.to_dict()

        actions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()

                actions.append(actions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if actions is not UNSET:
            field_dict["actions"] = actions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event_action_minimal import EventActionMinimal
        from ..models.event_conditions import EventConditions

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _trigger = d.pop("trigger", UNSET)
        trigger: Union[Unset, EventTriggerTypes]
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = EventTriggerTypes(_trigger)

        _conditions = d.pop("conditions", UNSET)
        conditions: Union[Unset, EventConditions]
        if isinstance(_conditions, Unset):
            conditions = UNSET
        else:
            conditions = EventConditions.from_dict(_conditions)

        actions = []
        _actions = d.pop("actions", UNSET)
        for actions_item_data in _actions or []:
            actions_item = EventActionMinimal.from_dict(actions_item_data)

            actions.append(actions_item)

        event_rule_minimal = cls(
            id=id,
            name=name,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            trigger=trigger,
            conditions=conditions,
            actions=actions,
        )

        event_rule_minimal.additional_properties = d
        return event_rule_minimal

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
