from enum import IntEnum


class FilesystemActionTypes(IntEnum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4

    def __str__(self) -> str:
        return str(self.value)
