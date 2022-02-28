from enum import Enum


class SSHAuthentications(str, Enum):
    PUBLICKEY = "publickey"
    PASSWORD = "password"
    KEYBOARD_INTERACTIVE = "keyboard-interactive"
    PUBLICKEYPASSWORD = "publickey+password"
    PUBLICKEYKEYBOARD_INTERACTIVE = "publickey+keyboard-interactive"

    def __str__(self) -> str:
        return str(self.value)
