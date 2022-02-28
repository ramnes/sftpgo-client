from enum import Enum


class FsEventAction(str, Enum):
    DOWNLOAD = "download"
    PRE_UPLOAD = "pre-upload"
    UPLOAD = "upload"
    DELETE = "delete"
    RENAME = "rename"
    MKDIR = "mkdir"
    RMDIR = "rmdir"
    SSH_CMD = "ssh_cmd"

    def __str__(self) -> str:
        return str(self.value)
