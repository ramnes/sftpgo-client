from enum import Enum


class UserFiltersTlsUsername(str, Enum):
    NONE = "None"
    COMMONNAME = "CommonName"

    def __str__(self) -> str:
        return str(self.value)
