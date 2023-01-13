from enum import Enum


class OctoPrintPrintJobStatusSubjectPatternEnum(str, Enum):
    PI_PI_ID_OCTOPRINT_PRINT_JOB = "pi.{pi_id}.octoprint.print_job"

    def __str__(self) -> str:
        return str(self.value)
