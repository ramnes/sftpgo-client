from enum import Enum


class EventConditionsProviderEventsItem(str, Enum):
    ADD = "add"
    UPDATE = "update"
    DELETE = "delete"

    def __str__(self) -> str:
        return str(self.value)
