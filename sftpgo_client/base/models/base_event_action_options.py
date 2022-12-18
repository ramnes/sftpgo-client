from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_action_command_config import EventActionCommandConfig
    from ..models.event_action_data_retention_config import (
        EventActionDataRetentionConfig,
    )
    from ..models.event_action_email_config import EventActionEmailConfig
    from ..models.event_action_filesystem_config import EventActionFilesystemConfig
    from ..models.event_action_http_config import EventActionHTTPConfig
    from ..models.event_action_password_expiration import EventActionPasswordExpiration


T = TypeVar("T", bound="BaseEventActionOptions")


@attr.s(auto_attribs=True)
class BaseEventActionOptions:
    """
    Attributes:
        http_config (Union[Unset, EventActionHTTPConfig]):
        cmd_config (Union[Unset, EventActionCommandConfig]):
        email_config (Union[Unset, EventActionEmailConfig]):
        retention_config (Union[Unset, EventActionDataRetentionConfig]):
        fs_config (Union[Unset, EventActionFilesystemConfig]):
        pwd_expiration_config (Union[Unset, EventActionPasswordExpiration]):
    """

    http_config: Union[Unset, "EventActionHTTPConfig"] = UNSET
    cmd_config: Union[Unset, "EventActionCommandConfig"] = UNSET
    email_config: Union[Unset, "EventActionEmailConfig"] = UNSET
    retention_config: Union[Unset, "EventActionDataRetentionConfig"] = UNSET
    fs_config: Union[Unset, "EventActionFilesystemConfig"] = UNSET
    pwd_expiration_config: Union[Unset, "EventActionPasswordExpiration"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        http_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.http_config, Unset):
            http_config = self.http_config.to_dict()

        cmd_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cmd_config, Unset):
            cmd_config = self.cmd_config.to_dict()

        email_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.email_config, Unset):
            email_config = self.email_config.to_dict()

        retention_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.retention_config, Unset):
            retention_config = self.retention_config.to_dict()

        fs_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fs_config, Unset):
            fs_config = self.fs_config.to_dict()

        pwd_expiration_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pwd_expiration_config, Unset):
            pwd_expiration_config = self.pwd_expiration_config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if http_config is not UNSET:
            field_dict["http_config"] = http_config
        if cmd_config is not UNSET:
            field_dict["cmd_config"] = cmd_config
        if email_config is not UNSET:
            field_dict["email_config"] = email_config
        if retention_config is not UNSET:
            field_dict["retention_config"] = retention_config
        if fs_config is not UNSET:
            field_dict["fs_config"] = fs_config
        if pwd_expiration_config is not UNSET:
            field_dict["pwd_expiration_config"] = pwd_expiration_config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event_action_command_config import EventActionCommandConfig
        from ..models.event_action_data_retention_config import (
            EventActionDataRetentionConfig,
        )
        from ..models.event_action_email_config import EventActionEmailConfig
        from ..models.event_action_filesystem_config import EventActionFilesystemConfig
        from ..models.event_action_http_config import EventActionHTTPConfig
        from ..models.event_action_password_expiration import (
            EventActionPasswordExpiration,
        )

        d = src_dict.copy()
        _http_config = d.pop("http_config", UNSET)
        http_config: Union[Unset, EventActionHTTPConfig]
        if isinstance(_http_config, Unset):
            http_config = UNSET
        else:
            http_config = EventActionHTTPConfig.from_dict(_http_config)

        _cmd_config = d.pop("cmd_config", UNSET)
        cmd_config: Union[Unset, EventActionCommandConfig]
        if isinstance(_cmd_config, Unset):
            cmd_config = UNSET
        else:
            cmd_config = EventActionCommandConfig.from_dict(_cmd_config)

        _email_config = d.pop("email_config", UNSET)
        email_config: Union[Unset, EventActionEmailConfig]
        if isinstance(_email_config, Unset):
            email_config = UNSET
        else:
            email_config = EventActionEmailConfig.from_dict(_email_config)

        _retention_config = d.pop("retention_config", UNSET)
        retention_config: Union[Unset, EventActionDataRetentionConfig]
        if isinstance(_retention_config, Unset):
            retention_config = UNSET
        else:
            retention_config = EventActionDataRetentionConfig.from_dict(
                _retention_config
            )

        _fs_config = d.pop("fs_config", UNSET)
        fs_config: Union[Unset, EventActionFilesystemConfig]
        if isinstance(_fs_config, Unset):
            fs_config = UNSET
        else:
            fs_config = EventActionFilesystemConfig.from_dict(_fs_config)

        _pwd_expiration_config = d.pop("pwd_expiration_config", UNSET)
        pwd_expiration_config: Union[Unset, EventActionPasswordExpiration]
        if isinstance(_pwd_expiration_config, Unset):
            pwd_expiration_config = UNSET
        else:
            pwd_expiration_config = EventActionPasswordExpiration.from_dict(
                _pwd_expiration_config
            )

        base_event_action_options = cls(
            http_config=http_config,
            cmd_config=cmd_config,
            email_config=email_config,
            retention_config=retention_config,
            fs_config=fs_config,
            pwd_expiration_config=pwd_expiration_config,
        )

        base_event_action_options.additional_properties = d
        return base_event_action_options

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
