from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.transfer_operation_type import TransferOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Transfer")


@attr.s(auto_attribs=True)
class Transfer:
    """ """

    operation_type: Union[Unset, TransferOperationType] = UNSET
    path: Union[Unset, str] = UNSET
    start_time: Union[Unset, int] = UNSET
    size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operation_type: Union[Unset, str] = UNSET
        if not isinstance(self.operation_type, Unset):
            operation_type = self.operation_type.value

        path = self.path
        start_time = self.start_time
        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operation_type is not UNSET:
            field_dict["operation_type"] = operation_type
        if path is not UNSET:
            field_dict["path"] = path
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _operation_type = d.pop("operation_type", UNSET)
        operation_type: Union[Unset, TransferOperationType]
        if isinstance(_operation_type, Unset):
            operation_type = UNSET
        else:
            operation_type = TransferOperationType(_operation_type)

        path = d.pop("path", UNSET)

        start_time = d.pop("start_time", UNSET)

        size = d.pop("size", UNSET)

        transfer = cls(
            operation_type=operation_type,
            path=path,
            start_time=start_time,
            size=size,
        )

        transfer.additional_properties = d
        return transfer

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
