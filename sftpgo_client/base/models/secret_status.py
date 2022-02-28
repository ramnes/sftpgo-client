from enum import Enum


class SecretStatus(str, Enum):
    PLAIN = "Plain"
    AES_256_GCM = "AES-256-GCM"
    SECRETBOX = "Secretbox"
    GCP = "GCP"
    AWS = "AWS"
    VAULTTRANSIT = "VaultTransit"
    AZUREKEYVAULT = "AzureKeyVault"
    REDACTED = "Redacted"

    def __str__(self) -> str:
        return str(self.value)
