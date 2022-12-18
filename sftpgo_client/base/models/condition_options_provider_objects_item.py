from enum import Enum


class ConditionOptionsProviderObjectsItem(str, Enum):
    USER = "user"
    GROUP = "group"
    ADMIN = "admin"
    API_KEY = "api_key"
    SHARE = "share"
    EVENT_ACTION = "event_action"
    EVENT_RULE = "event_rule"

    def __str__(self) -> str:
        return str(self.value)
