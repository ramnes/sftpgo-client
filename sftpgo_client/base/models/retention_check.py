from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.folder_retention import FolderRetention
from ..models.retention_check_notification import RetentionCheckNotification
from ..types import UNSET, Unset

T = TypeVar("T", bound="RetentionCheck")


@attr.s(auto_attribs=True)
class RetentionCheck:
    """
    Attributes:
        username (Union[Unset, str]): username to which the retention check refers
        folders (Union[Unset, List[FolderRetention]]):
        start_time (Union[Unset, int]): check start time as unix timestamp in milliseconds
        notifications (Union[Unset, List[RetentionCheckNotification]]):
        email (Union[Unset, str]): if the notification method is set to "Email", this is the e-mail address that
            receives the retention check report. This field is automatically set to the email address associated with the
            administrator starting the check
    """

    username: Union[Unset, str] = UNSET
    folders: Union[Unset, List[FolderRetention]] = UNSET
    start_time: Union[Unset, int] = UNSET
    notifications: Union[Unset, List[RetentionCheckNotification]] = UNSET
    email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        folders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.folders, Unset):
            folders = []
            for folders_item_data in self.folders:
                folders_item = folders_item_data.to_dict()

                folders.append(folders_item)

        start_time = self.start_time
        notifications: Union[Unset, List[str]] = UNSET
        if not isinstance(self.notifications, Unset):
            notifications = []
            for notifications_item_data in self.notifications:
                notifications_item = notifications_item_data.value

                notifications.append(notifications_item)

        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if folders is not UNSET:
            field_dict["folders"] = folders
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if notifications is not UNSET:
            field_dict["notifications"] = notifications
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username", UNSET)

        folders = []
        _folders = d.pop("folders", UNSET)
        for folders_item_data in _folders or []:
            folders_item = FolderRetention.from_dict(folders_item_data)

            folders.append(folders_item)

        start_time = d.pop("start_time", UNSET)

        notifications = []
        _notifications = d.pop("notifications", UNSET)
        for notifications_item_data in _notifications or []:
            notifications_item = RetentionCheckNotification(notifications_item_data)

            notifications.append(notifications_item)

        email = d.pop("email", UNSET)

        retention_check = cls(
            username=username,
            folders=folders,
            start_time=start_time,
            notifications=notifications,
            email=email,
        )

        retention_check.additional_properties = d
        return retention_check

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
