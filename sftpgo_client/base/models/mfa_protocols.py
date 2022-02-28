from enum import Enum


class MFAProtocols(str, Enum):
    SSH = "SSH"
    FTP = "FTP"
    HTTP = "HTTP"

    def __str__(self) -> str:
        return str(self.value)
