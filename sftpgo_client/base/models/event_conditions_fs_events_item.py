from enum import Enum


class EventConditionsFsEventsItem(str, Enum):
    UPLOAD = "upload"
    DOWNLOAD = "download"
    DELETE = "delete"
    RENAME = "rename"
    MKDIR = "mkdir"
    RMDIR = "rmdir"
    SSH_CMD = "ssh_cmd"

    def __str__(self) -> str:
        return str(self.value)
