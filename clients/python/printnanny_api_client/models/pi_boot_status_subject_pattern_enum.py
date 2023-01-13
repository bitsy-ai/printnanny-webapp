from enum import Enum


class PiBootStatusSubjectPatternEnum(str, Enum):
    PI_PI_ID_STATUS_BOOT = "pi.{pi_id}.status.boot"

    def __str__(self) -> str:
        return str(self.value)
