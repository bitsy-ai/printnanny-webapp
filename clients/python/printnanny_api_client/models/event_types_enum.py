from enum import Enum


class EventTypesEnum(str, Enum):
    PRINTQUALITY = "PrintQuality"
    PRINTSTARTED = "PrintStarted"
    PRINTDONE = "PrintDone"
    PRINTPROGRESS = "PrintProgress"
    PRINTPAUSED = "PrintPaused"
    PRINTCANCELLED = "PrintCancelled"

    def __str__(self) -> str:
        return str(self.value)
