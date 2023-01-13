from enum import Enum


class OctoPrintPrintJobStatusType(str, Enum):
    PRINTPROGRESS = "PrintProgress"
    PRINTSTARTED = "PrintStarted"
    PRINTFAILED = "PrintFailed"
    PRINTDONE = "PrintDone"
    PRINTCANCELLING = "PrintCancelling"
    PRINTCANCELLED = "PrintCancelled"
    PRINTPAUSED = "PrintPaused"
    PRINTRESUMED = "PrintResumed"

    def __str__(self) -> str:
        return str(self.value)
