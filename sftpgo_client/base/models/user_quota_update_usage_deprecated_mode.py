from enum import Enum


class UserQuotaUpdateUsageDeprecatedMode(str, Enum):
    ADD = "add"
    RESET = "reset"

    def __str__(self) -> str:
        return str(self.value)
