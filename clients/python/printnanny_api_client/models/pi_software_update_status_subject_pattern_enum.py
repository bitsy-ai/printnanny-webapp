from enum import Enum


class PiSoftwareUpdateStatusSubjectPatternEnum(str, Enum):
    PI_PI_ID_STATUS_SWUPDATE = "pi.{pi_id}.status.swupdate"

    def __str__(self) -> str:
        return str(self.value)
