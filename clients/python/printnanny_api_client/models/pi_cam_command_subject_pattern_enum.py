from enum import Enum


class PiCamCommandSubjectPatternEnum(str, Enum):
    PI_PI_ID_COMMAND_CAM = "pi.{pi_id}.command.cam"

    def __str__(self) -> str:
        return str(self.value)
