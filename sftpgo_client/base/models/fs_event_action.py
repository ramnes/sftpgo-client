from enum import Enum


class FsEventAction(str, Enum):
    DOWNLOAD = "download"
    UPLOAD = "upload"
    FIRST_UPLOAD = "first-upload"
    FIRST_DOWNLOAD = "first-download"
    DELETE = "delete"
    RENAME = "rename"
    MKDIR = "mkdir"
    RMDIR = "rmdir"
    SSH_CMD = "ssh_cmd"

    def __str__(self) -> str:
        return str(self.value)
