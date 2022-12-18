from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.connection_status_protocol import ConnectionStatusProtocol
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transfer import Transfer


T = TypeVar("T", bound="ConnectionStatus")


@attr.s(auto_attribs=True)
class ConnectionStatus:
    """
    Attributes:
        username (Union[Unset, str]): connected username
        connection_id (Union[Unset, str]): unique connection identifier
        client_version (Union[Unset, str]): client version
        remote_address (Union[Unset, str]): Remote address for the connected client
        connection_time (Union[Unset, int]): connection time as unix timestamp in milliseconds
        command (Union[Unset, str]): Last SSH/FTP command or WebDAV method
        last_activity (Union[Unset, int]): last client activity as unix timestamp in milliseconds
        protocol (Union[Unset, ConnectionStatusProtocol]):
        active_transfers (Union[Unset, List['Transfer']]):
        node (Union[Unset, str]): Node identifier, omitted for single node installations
    """

    username: Union[Unset, str] = UNSET
    connection_id: Union[Unset, str] = UNSET
    client_version: Union[Unset, str] = UNSET
    remote_address: Union[Unset, str] = UNSET
    connection_time: Union[Unset, int] = UNSET
    command: Union[Unset, str] = UNSET
    last_activity: Union[Unset, int] = UNSET
    protocol: Union[Unset, ConnectionStatusProtocol] = UNSET
    active_transfers: Union[Unset, List["Transfer"]] = UNSET
    node: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        connection_id = self.connection_id
        client_version = self.client_version
        remote_address = self.remote_address
        connection_time = self.connection_time
        command = self.command
        last_activity = self.last_activity
        protocol: Union[Unset, str] = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        active_transfers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.active_transfers, Unset):
            active_transfers = []
            for active_transfers_item_data in self.active_transfers:
                active_transfers_item = active_transfers_item_data.to_dict()

                active_transfers.append(active_transfers_item)

        node = self.node

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if client_version is not UNSET:
            field_dict["client_version"] = client_version
        if remote_address is not UNSET:
            field_dict["remote_address"] = remote_address
        if connection_time is not UNSET:
            field_dict["connection_time"] = connection_time
        if command is not UNSET:
            field_dict["command"] = command
        if last_activity is not UNSET:
            field_dict["last_activity"] = last_activity
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if active_transfers is not UNSET:
            field_dict["active_transfers"] = active_transfers
        if node is not UNSET:
            field_dict["node"] = node

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.transfer import Transfer

        d = src_dict.copy()
        username = d.pop("username", UNSET)

        connection_id = d.pop("connection_id", UNSET)

        client_version = d.pop("client_version", UNSET)

        remote_address = d.pop("remote_address", UNSET)

        connection_time = d.pop("connection_time", UNSET)

        command = d.pop("command", UNSET)

        last_activity = d.pop("last_activity", UNSET)

        _protocol = d.pop("protocol", UNSET)
        protocol: Union[Unset, ConnectionStatusProtocol]
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = ConnectionStatusProtocol(_protocol)

        active_transfers = []
        _active_transfers = d.pop("active_transfers", UNSET)
        for active_transfers_item_data in _active_transfers or []:
            active_transfers_item = Transfer.from_dict(active_transfers_item_data)

            active_transfers.append(active_transfers_item)

        node = d.pop("node", UNSET)

        connection_status = cls(
            username=username,
            connection_id=connection_id,
            client_version=client_version,
            remote_address=remote_address,
            connection_time=connection_time,
            command=command,
            last_activity=last_activity,
            protocol=protocol,
            active_transfers=active_transfers,
            node=node,
        )

        connection_status.additional_properties = d
        return connection_status

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
