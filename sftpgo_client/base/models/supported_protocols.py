from enum import Enum


class SupportedProtocols(str, Enum):
    SSH = "SSH"
    FTP = "FTP"
    DAV = "DAV"

    def __str__(self) -> str:
        return str(self.value)
