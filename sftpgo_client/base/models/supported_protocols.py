from enum import Enum


class SupportedProtocols(str, Enum):
    SSH = "SSH"
    FTP = "FTP"
    DAV = "DAV"
    HTTP = "HTTP"

    def __str__(self) -> str:
        return str(self.value)
