from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventActionEmailConfig")


@attr.s(auto_attribs=True)
class EventActionEmailConfig:
    """
    Attributes:
        recipients (Union[Unset, List[str]]):
        subject (Union[Unset, str]):
        body (Union[Unset, str]):
        attachments (Union[Unset, List[str]]): list of file paths to attach. The total size is limited to 10 MB
    """

    recipients: Union[Unset, List[str]] = UNSET
    subject: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    attachments: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        recipients: Union[Unset, List[str]] = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = self.recipients

        subject = self.subject
        body = self.body
        attachments: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if recipients is not UNSET:
            field_dict["recipients"] = recipients
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body is not UNSET:
            field_dict["body"] = body
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        recipients = cast(List[str], d.pop("recipients", UNSET))

        subject = d.pop("subject", UNSET)

        body = d.pop("body", UNSET)

        attachments = cast(List[str], d.pop("attachments", UNSET))

        event_action_email_config = cls(
            recipients=recipients,
            subject=subject,
            body=body,
            attachments=attachments,
        )

        event_action_email_config.additional_properties = d
        return event_action_email_config

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
