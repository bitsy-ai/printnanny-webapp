from enum import Enum


class PiBootCommandSubjectPatternEnum(str, Enum):
    PI_PI_ID_COMMAND_BOOT = "pi.{pi_id}.command.boot"

    def __str__(self) -> str:
        return str(self.value)
