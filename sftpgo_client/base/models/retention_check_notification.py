from enum import Enum


class RetentionCheckNotification(str, Enum):
    HOOK = "Hook"
    EMAIL = "Email"

    def __str__(self) -> str:
        return str(self.value)
