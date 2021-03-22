from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.extensions_filter import ExtensionsFilter
from ..models.login_methods import LoginMethods
from ..models.patterns_filter import PatternsFilter
from ..models.supported_protocols import SupportedProtocols
from ..models.user_filters_tls_username import UserFiltersTlsUsername
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserFilters")


@attr.s(auto_attribs=True)
class UserFilters:
    """ Additional user restrictions """

    allowed_ip: Union[Unset, List[str]] = UNSET
    denied_ip: Union[Unset, List[str]] = UNSET
    denied_login_methods: Union[Unset, List[LoginMethods]] = UNSET
    denied_protocols: Union[Unset, List[SupportedProtocols]] = UNSET
    file_patterns: Union[Unset, List[PatternsFilter]] = UNSET
    file_extensions: Union[Unset, List[ExtensionsFilter]] = UNSET
    max_upload_file_size: Union[Unset, int] = UNSET
    tls_username: Union[Unset, UserFiltersTlsUsername] = UNSET
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

        file_extensions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.file_extensions, Unset):
            file_extensions = []
            for file_extensions_item_data in self.file_extensions:
                file_extensions_item = file_extensions_item_data.to_dict()

                file_extensions.append(file_extensions_item)

        max_upload_file_size = self.max_upload_file_size
        tls_username: Union[Unset, str] = UNSET
        if not isinstance(self.tls_username, Unset):
            tls_username = self.tls_username.value

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
        if file_extensions is not UNSET:
            field_dict["file_extensions"] = file_extensions
        if max_upload_file_size is not UNSET:
            field_dict["max_upload_file_size"] = max_upload_file_size
        if tls_username is not UNSET:
            field_dict["tls_username"] = tls_username

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

        file_extensions = []
        _file_extensions = d.pop("file_extensions", UNSET)
        for file_extensions_item_data in _file_extensions or []:
            file_extensions_item = ExtensionsFilter.from_dict(file_extensions_item_data)

            file_extensions.append(file_extensions_item)

        max_upload_file_size = d.pop("max_upload_file_size", UNSET)

        tls_username: Union[Unset, UserFiltersTlsUsername] = UNSET
        _tls_username = d.pop("tls_username", UNSET)
        if not isinstance(_tls_username, Unset):
            tls_username = UserFiltersTlsUsername(_tls_username)

        user_filters = cls(
            allowed_ip=allowed_ip,
            denied_ip=denied_ip,
            denied_login_methods=denied_login_methods,
            denied_protocols=denied_protocols,
            file_patterns=file_patterns,
            file_extensions=file_extensions,
            max_upload_file_size=max_upload_file_size,
            tls_username=tls_username,
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
