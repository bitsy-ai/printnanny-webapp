import uuid
from rest_framework.exceptions import APIException


class UUID4Mixin:
    _uuid = None

    @property
    def uuid(self):
        if self._uuid is None:
            self._uuid = uuid.uuid4()
        return self._uuid


class RegistrationUnavailable(APIException, UUID4Mixin):
    status_code = 503
    default_detail = "Device registration failed."
    default_code = "device_register"

    def __init__(self, user, serial, parent_exception=None):
        self.user = user
        self.serial = serial
        self.parent_exception = parent_exception

        self.message = f"Device registration failed for serial={serial} user={user} log_id={self.uuid}. Please email support@printnanny.ai with this message for assistance."

        super().__init__(self.message)


class DeviceAlreadyExists(APIException, UUID4Mixin):
    status_code = 400
    default_detail = "Device registration failed."
    default_code = "device_register"

    def __init__(self, user, serial, parent_exception=None):
        self.user = user
        self.serial = serial
        self.parent_exception = parent_exception

        self.message = f"Device registration failed for serial={serial} user={user} log_id={self.uuid}. Please email support@printnanny.ai with this message for assistance."

        super().__init__(self.message)
