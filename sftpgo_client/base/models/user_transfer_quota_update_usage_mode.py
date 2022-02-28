from enum import Enum


class UserTransferQuotaUpdateUsageMode(str, Enum):
    ADD = "add"
    RESET = "reset"

    def __str__(self) -> str:
        return str(self.value)
