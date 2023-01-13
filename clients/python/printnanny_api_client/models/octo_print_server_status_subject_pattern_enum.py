from enum import Enum


class OctoPrintServerStatusSubjectPatternEnum(str, Enum):
    PI_PI_ID_OCTOPRINT_SERVER = "pi.{pi_id}.octoprint.server"

    def __str__(self) -> str:
        return str(self.value)
