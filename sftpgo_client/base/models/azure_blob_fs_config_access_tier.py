from enum import Enum


class AzureBlobFsConfigAccessTier(str, Enum):
    VALUE_0 = ""
    ARCHIVE = "Archive"
    HOT = "Hot"
    COOL = "Cool"

    def __str__(self) -> str:
        return str(self.value)
