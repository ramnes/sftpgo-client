from enum import Enum


class BaseUserFiltersTlsUsername(str, Enum):
    NONE = "None"
    COMMONNAME = "CommonName"

    def __str__(self) -> str:
        return str(self.value)
