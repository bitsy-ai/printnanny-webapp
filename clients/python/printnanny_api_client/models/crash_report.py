import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.crash_report_status_enum import CrashReportStatusEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="CrashReport")


@attr.s(auto_attribs=True)
class CrashReport:
    """
    Attributes:
        id (str):
        url (str):
        created_dt (datetime.datetime):
        updated_dt (datetime.datetime):
        description (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        os_version (Union[Unset, None, str]):
        os_logs (Union[Unset, None, str]):
        browser_version (Union[Unset, None, str]):
        browser_logs (Union[Unset, None, str]):
        serial (Union[Unset, None, str]):
        posthog_session (Union[Unset, None, str]):
        status (Union[Unset, CrashReportStatusEnum]):
        support_comment (Union[Unset, None, str]):
        user (Union[Unset, None, int]):
        pi (Union[Unset, None, int]):
    """

    id: str
    url: str
    created_dt: datetime.datetime
    updated_dt: datetime.datetime
    description: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    os_version: Union[Unset, None, str] = UNSET
    os_logs: Union[Unset, None, str] = UNSET
    browser_version: Union[Unset, None, str] = UNSET
    browser_logs: Union[Unset, None, str] = UNSET
    serial: Union[Unset, None, str] = UNSET
    posthog_session: Union[Unset, None, str] = UNSET
    status: Union[Unset, CrashReportStatusEnum] = UNSET
    support_comment: Union[Unset, None, str] = UNSET
    user: Union[Unset, None, int] = UNSET
    pi: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        url = self.url
        created_dt = self.created_dt.isoformat()

        updated_dt = self.updated_dt.isoformat()

        description = self.description
        email = self.email
        os_version = self.os_version
        os_logs = self.os_logs
        browser_version = self.browser_version
        browser_logs = self.browser_logs
        serial = self.serial
        posthog_session = self.posthog_session
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        support_comment = self.support_comment
        user = self.user
        pi = self.pi

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "url": url,
                "created_dt": created_dt,
                "updated_dt": updated_dt,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if email is not UNSET:
            field_dict["email"] = email
        if os_version is not UNSET:
            field_dict["os_version"] = os_version
        if os_logs is not UNSET:
            field_dict["os_logs"] = os_logs
        if browser_version is not UNSET:
            field_dict["browser_version"] = browser_version
        if browser_logs is not UNSET:
            field_dict["browser_logs"] = browser_logs
        if serial is not UNSET:
            field_dict["serial"] = serial
        if posthog_session is not UNSET:
            field_dict["posthog_session"] = posthog_session
        if status is not UNSET:
            field_dict["status"] = status
        if support_comment is not UNSET:
            field_dict["support_comment"] = support_comment
        if user is not UNSET:
            field_dict["user"] = user
        if pi is not UNSET:
            field_dict["pi"] = pi

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        url = d.pop("url")

        created_dt = isoparse(d.pop("created_dt"))

        updated_dt = isoparse(d.pop("updated_dt"))

        description = d.pop("description", UNSET)

        email = d.pop("email", UNSET)

        os_version = d.pop("os_version", UNSET)

        os_logs = d.pop("os_logs", UNSET)

        browser_version = d.pop("browser_version", UNSET)

        browser_logs = d.pop("browser_logs", UNSET)

        serial = d.pop("serial", UNSET)

        posthog_session = d.pop("posthog_session", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CrashReportStatusEnum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CrashReportStatusEnum(_status)

        support_comment = d.pop("support_comment", UNSET)

        user = d.pop("user", UNSET)

        pi = d.pop("pi", UNSET)

        crash_report = cls(
            id=id,
            url=url,
            created_dt=created_dt,
            updated_dt=updated_dt,
            description=description,
            email=email,
            os_version=os_version,
            os_logs=os_logs,
            browser_version=browser_version,
            browser_logs=browser_logs,
            serial=serial,
            posthog_session=posthog_session,
            status=status,
            support_comment=support_comment,
            user=user,
            pi=pi,
        )

        crash_report.additional_properties = d
        return crash_report

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
