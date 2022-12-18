from enum import Enum


class ProviderEventObjectType(str, Enum):
    USER = "user"
    FOLDER = "folder"
    GROUP = "group"
    ADMIN = "admin"
    API_KEY = "api_key"
    SHARE = "share"
    EVENT_ACTION = "event_action"
    EVENT_RULE = "event_rule"
    ROLE = "role"

    def __str__(self) -> str:
        return str(self.value)
