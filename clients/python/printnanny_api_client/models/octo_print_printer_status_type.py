from enum import Enum


class OctoPrintPrinterStatusType(str, Enum):
    PRINTEROFFLINE = "PrinterOffline"
    PRINTEROPENSERIAL = "PrinterOpenSerial"
    PRINTERCONNECTING = "PrinterConnecting"
    PRINTEROPERATIONAL = "PrinterOperational"
    PRINTERSTARTING = "PrinterStarting"
    PRINTERINPROGRESS = "PrinterInProgress"
    PRINTERCANCELLING = "PrinterCancelling"
    PRINTERPAUSING = "PrinterPausing"
    PRINTERPAUSED = "PrinterPaused"
    PRINTERRESUMING = "PrinterResuming"
    PRINTERFINISHING = "PrinterFinishing"
    PRINTERERROR = "PrinterError"

    def __str__(self) -> str:
        return str(self.value)
