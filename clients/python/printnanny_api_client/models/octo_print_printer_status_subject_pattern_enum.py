from enum import Enum


class OctoPrintPrinterStatusSubjectPatternEnum(str, Enum):
    PI_PI_ID_OCTOPRINT_PRINTER = "pi.{pi_id}.octoprint.printer"

    def __str__(self) -> str:
        return str(self.value)
