from enum import Enum


class PiCamStatusSubjectPatternEnum(str, Enum):
    PI_PI_ID_STATUS_CAM = "pi.{pi_id}.status.cam"

    def __str__(self) -> str:
        return str(self.value)
