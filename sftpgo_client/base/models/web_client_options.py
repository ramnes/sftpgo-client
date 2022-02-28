from enum import Enum


class WebClientOptions(str, Enum):
    PUBLICKEY_CHANGE_DISABLED = "publickey-change-disabled"
    WRITE_DISABLED = "write-disabled"
    MFA_DISABLED = "mfa-disabled"
    PASSWORD_CHANGE_DISABLED = "password-change-disabled"
    API_KEY_AUTH_CHANGE_DISABLED = "api-key-auth-change-disabled"
    INFO_CHANGE_DISABLED = "info-change-disabled"
    SHARES_DISABLED = "shares-disabled"
    PASSWORD_RESET_DISABLED = "password-reset-disabled"
    SHARES_WITHOUT_PASSWORD_DISABLED = "shares-without-password-disabled"

    def __str__(self) -> str:
        return str(self.value)
