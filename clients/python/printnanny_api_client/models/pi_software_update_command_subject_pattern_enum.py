from enum import Enum


class PiSoftwareUpdateCommandSubjectPatternEnum(str, Enum):
    PI_PI_ID_COMMAND_SWUPDATE = "pi.{pi_id}.command.swupdate"

    def __str__(self) -> str:
        return str(self.value)
