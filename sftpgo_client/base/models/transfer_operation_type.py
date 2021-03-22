from enum import Enum


class TransferOperationType(str, Enum):
    UPLOAD = "upload"
    DOWNLOAD = "download"

    def __str__(self) -> str:
        return str(self.value)
