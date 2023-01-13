from enum import Enum


class PiSoftwareUpdateStatusType(str, Enum):
    SWUPDATESTARTED = "SwupdateStarted"
    SWUPDATESUCCESS = "SwupdateSuccess"
    SWUPDATEERROR = "SwupdateError"

    def __str__(self) -> str:
        return str(self.value)
