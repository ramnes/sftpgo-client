from enum import Enum


class FolderQuotaUpdateUsageDeprecatedMode(str, Enum):
    ADD = "add"
    RESET = "reset"

    def __str__(self) -> str:
        return str(self.value)
