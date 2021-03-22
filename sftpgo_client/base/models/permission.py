from enum import Enum


class Permission(str, Enum):
    VALUE_0 = "*"
    LIST = "list"
    DOWNLOAD = "download"
    UPLOAD = "upload"
    OVERWRITE = "overwrite"
    DELETE = "delete"
    RENAME = "rename"
    CREATE_DIRS = "create_dirs"
    CREATE_SYMLINKS = "create_symlinks"
    CHMOD = "chmod"
    CHOWN = "chown"
    CHTIMES = "chtimes"

    def __str__(self) -> str:
        return str(self.value)
