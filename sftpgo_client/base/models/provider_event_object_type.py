from enum import Enum


class ProviderEventObjectType(str, Enum):
    USER = "user"
    ADMIN = "admin"
    API_KEY = "api_key"
    SHARE = "share"

    def __str__(self) -> str:
        return str(self.value)
