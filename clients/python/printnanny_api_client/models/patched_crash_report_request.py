from io import BytesIO
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.crash_report_status_enum import CrashReportStatusEnum
from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="PatchedCrashReportRequest")


@attr.s(auto_attribs=True)
class PatchedCrashReportRequest:
    """
    Attributes:
        description (Union[Unset, None, str]):
        email (Union[Unset, None, str]):
        os_version (Union[Unset, None, str]):
        os_logs (Union[Unset, None, File]):
        browser_version (Union[Unset, None, str]):
        browser_logs (Union[Unset, None, File]):
        serial (Union[Unset, None, str]):
        posthog_session (Union[Unset, None, str]):
        status (Union[Unset, CrashReportStatusEnum]):
        support_comment (Union[Unset, None, str]):
        user (Union[Unset, None, int]):
        pi (Union[Unset, None, int]):
    """

    description: Union[Unset, None, str] = UNSET
    email: Union[Unset, None, str] = UNSET
    os_version: Union[Unset, None, str] = UNSET
    os_logs: Union[Unset, None, File] = UNSET
    browser_version: Union[Unset, None, str] = UNSET
    browser_logs: Union[Unset, None, File] = UNSET
    serial: Union[Unset, None, str] = UNSET
    posthog_session: Union[Unset, None, str] = UNSET
    status: Union[Unset, CrashReportStatusEnum] = UNSET
    support_comment: Union[Unset, None, str] = UNSET
    user: Union[Unset, None, int] = UNSET
    pi: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        email = self.email
        os_version = self.os_version
        os_logs: Union[Unset, None, FileJsonType] = UNSET
        if not isinstance(self.os_logs, Unset):
            os_logs = self.os_logs.to_tuple() if self.os_logs else None

        browser_version = self.browser_version
        browser_logs: Union[Unset, None, FileJsonType] = UNSET
        if not isinstance(self.browser_logs, Unset):
            browser_logs = self.browser_logs.to_tuple() if self.browser_logs else None

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
        field_dict.update({})
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

    def to_multipart(self) -> Dict[str, Any]:
        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )
        email = self.email if isinstance(self.email, Unset) else (None, str(self.email).encode(), "text/plain")
        os_version = (
            self.os_version
            if isinstance(self.os_version, Unset)
            else (None, str(self.os_version).encode(), "text/plain")
        )
        os_logs: Union[Unset, None, FileJsonType] = UNSET
        if not isinstance(self.os_logs, Unset):
            os_logs = self.os_logs.to_tuple() if self.os_logs else None

        browser_version = (
            self.browser_version
            if isinstance(self.browser_version, Unset)
            else (None, str(self.browser_version).encode(), "text/plain")
        )
        browser_logs: Union[Unset, None, FileJsonType] = UNSET
        if not isinstance(self.browser_logs, Unset):
            browser_logs = self.browser_logs.to_tuple() if self.browser_logs else None

        serial = self.serial if isinstance(self.serial, Unset) else (None, str(self.serial).encode(), "text/plain")
        posthog_session = (
            self.posthog_session
            if isinstance(self.posthog_session, Unset)
            else (None, str(self.posthog_session).encode(), "text/plain")
        )
        status: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.status, Unset):
            status = (None, str(self.status.value).encode(), "text/plain")

        support_comment = (
            self.support_comment
            if isinstance(self.support_comment, Unset)
            else (None, str(self.support_comment).encode(), "text/plain")
        )
        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")
        pi = self.pi if isinstance(self.pi, Unset) else (None, str(self.pi).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
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
        description = d.pop("description", UNSET)

        email = d.pop("email", UNSET)

        os_version = d.pop("os_version", UNSET)

        _os_logs = d.pop("os_logs", UNSET)
        os_logs: Union[Unset, None, File]
        if _os_logs is None:
            os_logs = None
        elif isinstance(_os_logs, Unset):
            os_logs = UNSET
        else:
            os_logs = File(payload=BytesIO(_os_logs))

        browser_version = d.pop("browser_version", UNSET)

        _browser_logs = d.pop("browser_logs", UNSET)
        browser_logs: Union[Unset, None, File]
        if _browser_logs is None:
            browser_logs = None
        elif isinstance(_browser_logs, Unset):
            browser_logs = UNSET
        else:
            browser_logs = File(payload=BytesIO(_browser_logs))

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

        patched_crash_report_request = cls(
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

        patched_crash_report_request.additional_properties = d
        return patched_crash_report_request

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
