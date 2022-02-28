from enum import Enum


class EventProtocols(str, Enum):
    SSH = "SSH"
    SFTP = "SFTP"
    SCP = "SCP"
    FTP = "FTP"
    DAV = "DAV"
    HTTP = "HTTP"
    HTTPSHARE = "HTTPShare"
    DATARETENTION = "DataRetention"
    OIDC = "OIDC"

    def __str__(self) -> str:
        return str(self.value)
