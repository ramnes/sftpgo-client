from enum import Enum


class LoginMethods(str, Enum):
    PUBLICKEY = "publickey"
    PASSWORD = "password"
    PASSWORD_OVER_SSH = "password-over-SSH"
    KEYBOARD_INTERACTIVE = "keyboard-interactive"
    PUBLICKEYPASSWORD = "publickey+password"
    PUBLICKEYKEYBOARD_INTERACTIVE = "publickey+keyboard-interactive"
    TLSCERTIFICATE = "TLSCertificate"
    TLSCERTIFICATEPASSWORD = "TLSCertificate+password"

    def __str__(self) -> str:
        return str(self.value)
