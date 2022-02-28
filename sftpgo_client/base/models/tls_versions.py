from enum import IntEnum


class TLSVersions(IntEnum):
    VALUE_12 = 12
    VALUE_13 = 13

    def __str__(self) -> str:
        return str(self.value)
