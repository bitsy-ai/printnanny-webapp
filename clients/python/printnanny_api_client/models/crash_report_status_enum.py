from enum import Enum


class CrashReportStatusEnum(str, Enum):
    INVESTIGATING = "Investigating"
    FIXED = "Fixed"

    def __str__(self) -> str:
        return str(self.value)
