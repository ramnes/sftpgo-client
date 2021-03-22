from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.ssh_binding import SSHBinding
from ..models.ssh_host_key import SSHHostKey
from ..types import UNSET, Unset

T = TypeVar("T", bound="SSHServiceStatus")


@attr.s(auto_attribs=True)
class SSHServiceStatus:
    """  """

    is_active: Union[Unset, bool] = UNSET
    bindings: Union[Unset, None, List[SSHBinding]] = UNSET
    host_keys: Union[Unset, None, List[SSHHostKey]] = UNSET
    ssh_commands: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_active = self.is_active
        bindings: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.bindings, Unset):
            if self.bindings is None:
                bindings = None
            else:
                bindings = []
                for bindings_item_data in self.bindings:
                    bindings_item = bindings_item_data.to_dict()

                    bindings.append(bindings_item)

        host_keys: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.host_keys, Unset):
            if self.host_keys is None:
                host_keys = None
            else:
                host_keys = []
                for host_keys_item_data in self.host_keys:
                    host_keys_item = host_keys_item_data.to_dict()

                    host_keys.append(host_keys_item)

        ssh_commands: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ssh_commands, Unset):
            ssh_commands = self.ssh_commands

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if bindings is not UNSET:
            field_dict["bindings"] = bindings
        if host_keys is not UNSET:
            field_dict["host_keys"] = host_keys
        if ssh_commands is not UNSET:
            field_dict["ssh_commands"] = ssh_commands

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_active = d.pop("is_active", UNSET)

        bindings = []
        _bindings = d.pop("bindings", UNSET)
        for bindings_item_data in _bindings or []:
            bindings_item = SSHBinding.from_dict(bindings_item_data)

            bindings.append(bindings_item)

        host_keys = []
        _host_keys = d.pop("host_keys", UNSET)
        for host_keys_item_data in _host_keys or []:
            host_keys_item = SSHHostKey.from_dict(host_keys_item_data)

            host_keys.append(host_keys_item)

        ssh_commands = cast(List[str], d.pop("ssh_commands", UNSET))

        ssh_service_status = cls(
            is_active=is_active,
            bindings=bindings,
            host_keys=host_keys,
            ssh_commands=ssh_commands,
        )

        ssh_service_status.additional_properties = d
        return ssh_service_status

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
