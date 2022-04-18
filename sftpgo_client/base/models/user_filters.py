from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.bandwidth_limit import BandwidthLimit
from ..models.data_transfer_limit import DataTransferLimit
from ..models.hooks_filter import HooksFilter
from ..models.login_methods import LoginMethods
from ..models.mfa_protocols import MFAProtocols
from ..models.patterns_filter import PatternsFilter
from ..models.recovery_code import RecoveryCode
from ..models.supported_protocols import SupportedProtocols
from ..models.user_filters_tls_username import UserFiltersTlsUsername
from ..models.user_totp_config import UserTOTPConfig
from ..models.user_type import UserType
from ..models.web_client_options import WebClientOptions
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserFilters")


@attr.s(auto_attribs=True)
class UserFilters:
    """Additional user options

    Attributes:
        allowed_ip (Union[Unset, List[str]]): only clients connecting from these IP/Mask are allowed. IP/Mask must be in
            CIDR notation as defined in RFC 4632 and RFC 4291, for example "192.0.2.0/24" or "2001:db8::/32" Example:
            ['192.0.2.0/24', '2001:db8::/32'].
        denied_ip (Union[Unset, List[str]]): clients connecting from these IP/Mask are not allowed. Denied rules are
            evaluated before allowed ones Example: ['172.16.0.0/16'].
        denied_login_methods (Union[Unset, List[LoginMethods]]): if null or empty any available login method is allowed
        denied_protocols (Union[Unset, List[SupportedProtocols]]): if null or empty any available protocol is allowed
        file_patterns (Union[Unset, List[PatternsFilter]]): filters based on shell like file patterns. These
            restrictions do not apply to files listing for performance reasons, so a denied file cannot be
            downloaded/overwritten/renamed but it will still be in the list of files. Please note that these restrictions
            can be easily bypassed
        max_upload_file_size (Union[Unset, int]): maximum allowed size, as bytes, for a single file upload. The upload
            will be aborted if/when the size of the file being sent exceeds this limit. 0 means unlimited. This restriction
            does not apply for SSH system commands such as `git` and `rsync`
        tls_username (Union[Unset, UserFiltersTlsUsername]): defines the TLS certificate field to use as username. For
            FTP clients it must match the name provided using the "USER" command. For WebDAV, if no username is provided,
            the CN will be used as username. For WebDAV clients it must match the implicit or provided username. Ignored if
            mutual TLS is disabled
        hooks (Union[Unset, HooksFilter]): User specific hook overrides
        disable_fs_checks (Union[Unset, bool]): Disable checks for existence and automatic creation of home directory
            and virtual folders. SFTPGo requires that the user's home directory, virtual folder root, and intermediate paths
            to virtual folders exist to work properly. If you already know that the required directories exist, disabling
            these checks will speed up login. You could, for example, disable these checks after the first login
        web_client (Union[Unset, List[WebClientOptions]]): WebClient/user REST API related configuration options
        allow_api_key_auth (Union[Unset, bool]): API key authentication allows to impersonate this user with an API key
        user_type (Union[Unset, UserType]): This is an hint for authentication plugins. It is ignored when using SFTPGo
            internal authentication
        totp_config (Union[Unset, UserTOTPConfig]):
        recovery_codes (Union[Unset, List[RecoveryCode]]):
        bandwidth_limits (Union[Unset, List[BandwidthLimit]]):
        data_transfer_limits (Union[Unset, List[DataTransferLimit]]):
        external_auth_cache_time (Union[Unset, int]): Defines the cache time, in seconds, for users authenticated using
            an external auth hook. 0 means no cache
        start_directory (Union[Unset, str]): Specifies an alternate starting directory. If not set, the default is "/".
            This option is supported for SFTP/SCP, FTP and HTTP (WebClient/REST API) protocols. Relative paths will use this
            directory as base.
        field_2fa_protocols (Union[Unset, List[MFAProtocols]]): Defines protocols that require two factor authentication
    """

    allowed_ip: Union[Unset, List[str]] = UNSET
    denied_ip: Union[Unset, List[str]] = UNSET
    denied_login_methods: Union[Unset, List[LoginMethods]] = UNSET
    denied_protocols: Union[Unset, List[SupportedProtocols]] = UNSET
    file_patterns: Union[Unset, List[PatternsFilter]] = UNSET
    max_upload_file_size: Union[Unset, int] = UNSET
    tls_username: Union[Unset, UserFiltersTlsUsername] = UNSET
    hooks: Union[Unset, HooksFilter] = UNSET
    disable_fs_checks: Union[Unset, bool] = UNSET
    web_client: Union[Unset, List[WebClientOptions]] = UNSET
    allow_api_key_auth: Union[Unset, bool] = UNSET
    user_type: Union[Unset, UserType] = UNSET
    totp_config: Union[Unset, UserTOTPConfig] = UNSET
    recovery_codes: Union[Unset, List[RecoveryCode]] = UNSET
    bandwidth_limits: Union[Unset, List[BandwidthLimit]] = UNSET
    data_transfer_limits: Union[Unset, List[DataTransferLimit]] = UNSET
    external_auth_cache_time: Union[Unset, int] = UNSET
    start_directory: Union[Unset, str] = UNSET
    field_2fa_protocols: Union[Unset, List[MFAProtocols]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allowed_ip: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allowed_ip, Unset):
            allowed_ip = self.allowed_ip

        denied_ip: Union[Unset, List[str]] = UNSET
        if not isinstance(self.denied_ip, Unset):
            denied_ip = self.denied_ip

        denied_login_methods: Union[Unset, List[str]] = UNSET
        if not isinstance(self.denied_login_methods, Unset):
            denied_login_methods = []
            for denied_login_methods_item_data in self.denied_login_methods:
                denied_login_methods_item = denied_login_methods_item_data.value

                denied_login_methods.append(denied_login_methods_item)

        denied_protocols: Union[Unset, List[str]] = UNSET
        if not isinstance(self.denied_protocols, Unset):
            denied_protocols = []
            for denied_protocols_item_data in self.denied_protocols:
                denied_protocols_item = denied_protocols_item_data.value

                denied_protocols.append(denied_protocols_item)

        file_patterns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.file_patterns, Unset):
            file_patterns = []
            for file_patterns_item_data in self.file_patterns:
                file_patterns_item = file_patterns_item_data.to_dict()

                file_patterns.append(file_patterns_item)

        max_upload_file_size = self.max_upload_file_size
        tls_username: Union[Unset, str] = UNSET
        if not isinstance(self.tls_username, Unset):
            tls_username = self.tls_username.value

        hooks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hooks, Unset):
            hooks = self.hooks.to_dict()

        disable_fs_checks = self.disable_fs_checks
        web_client: Union[Unset, List[str]] = UNSET
        if not isinstance(self.web_client, Unset):
            web_client = []
            for web_client_item_data in self.web_client:
                web_client_item = web_client_item_data.value

                web_client.append(web_client_item)

        allow_api_key_auth = self.allow_api_key_auth
        user_type: Union[Unset, str] = UNSET
        if not isinstance(self.user_type, Unset):
            user_type = self.user_type.value

        totp_config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.totp_config, Unset):
            totp_config = self.totp_config.to_dict()

        recovery_codes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.recovery_codes, Unset):
            recovery_codes = []
            for recovery_codes_item_data in self.recovery_codes:
                recovery_codes_item = recovery_codes_item_data.to_dict()

                recovery_codes.append(recovery_codes_item)

        bandwidth_limits: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.bandwidth_limits, Unset):
            bandwidth_limits = []
            for bandwidth_limits_item_data in self.bandwidth_limits:
                bandwidth_limits_item = bandwidth_limits_item_data.to_dict()

                bandwidth_limits.append(bandwidth_limits_item)

        data_transfer_limits: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data_transfer_limits, Unset):
            data_transfer_limits = []
            for data_transfer_limits_item_data in self.data_transfer_limits:
                data_transfer_limits_item = data_transfer_limits_item_data.to_dict()

                data_transfer_limits.append(data_transfer_limits_item)

        external_auth_cache_time = self.external_auth_cache_time
        start_directory = self.start_directory
        field_2fa_protocols: Union[Unset, List[str]] = UNSET
        if not isinstance(self.field_2fa_protocols, Unset):
            field_2fa_protocols = []
            for field_2fa_protocols_item_data in self.field_2fa_protocols:
                field_2fa_protocols_item = field_2fa_protocols_item_data.value

                field_2fa_protocols.append(field_2fa_protocols_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_ip is not UNSET:
            field_dict["allowed_ip"] = allowed_ip
        if denied_ip is not UNSET:
            field_dict["denied_ip"] = denied_ip
        if denied_login_methods is not UNSET:
            field_dict["denied_login_methods"] = denied_login_methods
        if denied_protocols is not UNSET:
            field_dict["denied_protocols"] = denied_protocols
        if file_patterns is not UNSET:
            field_dict["file_patterns"] = file_patterns
        if max_upload_file_size is not UNSET:
            field_dict["max_upload_file_size"] = max_upload_file_size
        if tls_username is not UNSET:
            field_dict["tls_username"] = tls_username
        if hooks is not UNSET:
            field_dict["hooks"] = hooks
        if disable_fs_checks is not UNSET:
            field_dict["disable_fs_checks"] = disable_fs_checks
        if web_client is not UNSET:
            field_dict["web_client"] = web_client
        if allow_api_key_auth is not UNSET:
            field_dict["allow_api_key_auth"] = allow_api_key_auth
        if user_type is not UNSET:
            field_dict["user_type"] = user_type
        if totp_config is not UNSET:
            field_dict["totp_config"] = totp_config
        if recovery_codes is not UNSET:
            field_dict["recovery_codes"] = recovery_codes
        if bandwidth_limits is not UNSET:
            field_dict["bandwidth_limits"] = bandwidth_limits
        if data_transfer_limits is not UNSET:
            field_dict["data_transfer_limits"] = data_transfer_limits
        if external_auth_cache_time is not UNSET:
            field_dict["external_auth_cache_time"] = external_auth_cache_time
        if start_directory is not UNSET:
            field_dict["start_directory"] = start_directory
        if field_2fa_protocols is not UNSET:
            field_dict["2fa_protocols"] = field_2fa_protocols

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        allowed_ip = cast(List[str], d.pop("allowed_ip", UNSET))

        denied_ip = cast(List[str], d.pop("denied_ip", UNSET))

        denied_login_methods = []
        _denied_login_methods = d.pop("denied_login_methods", UNSET)
        for denied_login_methods_item_data in _denied_login_methods or []:
            denied_login_methods_item = LoginMethods(denied_login_methods_item_data)

            denied_login_methods.append(denied_login_methods_item)

        denied_protocols = []
        _denied_protocols = d.pop("denied_protocols", UNSET)
        for denied_protocols_item_data in _denied_protocols or []:
            denied_protocols_item = SupportedProtocols(denied_protocols_item_data)

            denied_protocols.append(denied_protocols_item)

        file_patterns = []
        _file_patterns = d.pop("file_patterns", UNSET)
        for file_patterns_item_data in _file_patterns or []:
            file_patterns_item = PatternsFilter.from_dict(file_patterns_item_data)

            file_patterns.append(file_patterns_item)

        max_upload_file_size = d.pop("max_upload_file_size", UNSET)

        _tls_username = d.pop("tls_username", UNSET)
        tls_username: Union[Unset, UserFiltersTlsUsername]
        if isinstance(_tls_username, Unset):
            tls_username = UNSET
        else:
            tls_username = UserFiltersTlsUsername(_tls_username)

        _hooks = d.pop("hooks", UNSET)
        hooks: Union[Unset, HooksFilter]
        if isinstance(_hooks, Unset):
            hooks = UNSET
        else:
            hooks = HooksFilter.from_dict(_hooks)

        disable_fs_checks = d.pop("disable_fs_checks", UNSET)

        web_client = []
        _web_client = d.pop("web_client", UNSET)
        for web_client_item_data in _web_client or []:
            web_client_item = WebClientOptions(web_client_item_data)

            web_client.append(web_client_item)

        allow_api_key_auth = d.pop("allow_api_key_auth", UNSET)

        _user_type = d.pop("user_type", UNSET)
        user_type: Union[Unset, UserType]
        if isinstance(_user_type, Unset):
            user_type = UNSET
        else:
            user_type = UserType(_user_type)

        _totp_config = d.pop("totp_config", UNSET)
        totp_config: Union[Unset, UserTOTPConfig]
        if isinstance(_totp_config, Unset):
            totp_config = UNSET
        else:
            totp_config = UserTOTPConfig.from_dict(_totp_config)

        recovery_codes = []
        _recovery_codes = d.pop("recovery_codes", UNSET)
        for recovery_codes_item_data in _recovery_codes or []:
            recovery_codes_item = RecoveryCode.from_dict(recovery_codes_item_data)

            recovery_codes.append(recovery_codes_item)

        bandwidth_limits = []
        _bandwidth_limits = d.pop("bandwidth_limits", UNSET)
        for bandwidth_limits_item_data in _bandwidth_limits or []:
            bandwidth_limits_item = BandwidthLimit.from_dict(bandwidth_limits_item_data)

            bandwidth_limits.append(bandwidth_limits_item)

        data_transfer_limits = []
        _data_transfer_limits = d.pop("data_transfer_limits", UNSET)
        for data_transfer_limits_item_data in _data_transfer_limits or []:
            data_transfer_limits_item = DataTransferLimit.from_dict(
                data_transfer_limits_item_data
            )

            data_transfer_limits.append(data_transfer_limits_item)

        external_auth_cache_time = d.pop("external_auth_cache_time", UNSET)

        start_directory = d.pop("start_directory", UNSET)

        field_2fa_protocols = []
        _field_2fa_protocols = d.pop("2fa_protocols", UNSET)
        for field_2fa_protocols_item_data in _field_2fa_protocols or []:
            field_2fa_protocols_item = MFAProtocols(field_2fa_protocols_item_data)

            field_2fa_protocols.append(field_2fa_protocols_item)

        user_filters = cls(
            allowed_ip=allowed_ip,
            denied_ip=denied_ip,
            denied_login_methods=denied_login_methods,
            denied_protocols=denied_protocols,
            file_patterns=file_patterns,
            max_upload_file_size=max_upload_file_size,
            tls_username=tls_username,
            hooks=hooks,
            disable_fs_checks=disable_fs_checks,
            web_client=web_client,
            allow_api_key_auth=allow_api_key_auth,
            user_type=user_type,
            totp_config=totp_config,
            recovery_codes=recovery_codes,
            bandwidth_limits=bandwidth_limits,
            data_transfer_limits=data_transfer_limits,
            external_auth_cache_time=external_auth_cache_time,
            start_directory=start_directory,
            field_2fa_protocols=field_2fa_protocols,
        )

        user_filters.additional_properties = d
        return user_filters

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
