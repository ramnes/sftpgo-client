from enum import Enum


class ConnectionStatusProtocol(str, Enum):
    SFTP = "SFTP"
    SCP = "SCP"
    SSH = "SSH"
    FTP = "FTP"
    DAV = "DAV"

    def __str__(self) -> str:
        return str(self.value)
