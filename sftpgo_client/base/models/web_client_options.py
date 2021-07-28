from enum import Enum


class WebClientOptions(str, Enum):
    PUBLICKEY_CHANGE_DISABLED = "publickey-change-disabled"
    WRITE_DISABLED = "write-disabled"

    def __str__(self) -> str:
        return str(self.value)
