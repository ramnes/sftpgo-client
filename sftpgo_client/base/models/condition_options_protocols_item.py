from enum import Enum


class ConditionOptionsProtocolsItem(str, Enum):
    SFTP = "SFTP"
    SCP = "SCP"
    SSH = "SSH"
    FTP = "FTP"
    DAV = "DAV"
    HTTP = "HTTP"
    HTTPSHARE = "HTTPShare"
    OIDC = "OIDC"

    def __str__(self) -> str:
        return str(self.value)
