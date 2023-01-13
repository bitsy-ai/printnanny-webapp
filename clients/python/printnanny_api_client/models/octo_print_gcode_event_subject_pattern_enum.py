from enum import Enum


class OctoPrintGcodeEventSubjectPatternEnum(str, Enum):
    PI_PI_ID_OCTOPRINT_GCODE = "pi.{pi_id}.octoprint.gcode"

    def __str__(self) -> str:
        return str(self.value)
