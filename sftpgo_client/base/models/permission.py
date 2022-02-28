from enum import Enum


class Permission(str, Enum):
    VALUE_0 = "*"
    LIST = "list"
    DOWNLOAD = "download"
    UPLOAD = "upload"
    OVERWRITE = "overwrite"
    DELETE = "delete"
    DELETE_FILES = "delete_files"
    DELETE_DIRS = "delete_dirs"
    RENAME = "rename"
    RENAME_FILES = "rename_files"
    RENAME_DIRS = "rename_dirs"
    CREATE_DIRS = "create_dirs"
    CREATE_SYMLINKS = "create_symlinks"
    CHMOD = "chmod"
    CHOWN = "chown"
    CHTIMES = "chtimes"

    def __str__(self) -> str:
        return str(self.value)
