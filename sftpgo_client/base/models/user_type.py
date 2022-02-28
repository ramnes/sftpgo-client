from enum import Enum


class UserType(str, Enum):
    VALUE_0 = ""
    LDAPUSER = "LDAPUser"
    OSUSER = "OSUser"

    def __str__(self) -> str:
        return str(self.value)
