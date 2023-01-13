from enum import Enum


class PiSoftwareUpdateCommandType(str, Enum):
    SWUPDATE = "Swupdate"
    SWUPDATEROLLBACK = "SwupdateRollback"

    def __str__(self) -> str:
        return str(self.value)
