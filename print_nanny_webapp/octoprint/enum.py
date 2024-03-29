from django.db import models


class OctoprintEventSubjectPattern(models.TextChoices):
    OctoPrintServerStatus = "pi.{pi_id}.octoprint.server"
    OctoPrintPrinterStatus = "pi.{pi_id}.octoprint.printer"
    OctoPrintPrintJobStatus = "pi.{pi_id}.octoprint.print_job"
    OctoPrintGcodeEvent = "pi.{pi_id}.octoprint.gcode"


class OctoPrintServerStatusType(models.TextChoices):
    SERVER_TEST = "Test", "Test Event"
    SERVER_STARTUP = "Startup", "Server Startup"  # server
    SERVER_SHUTDOWN = "Shutdown", "Server Shutdown"  # server


class OctoPrintPrintJobStatusType(models.TextChoices):
    PRINT_PROGRESS = "PrintProgress", "Print Progress"  # printer comms
    PRINT_JOB_STARTED = "PrintStarted", "Print Job Started"  # print job
    PRINT_JOB_FAILED = "PrintFailed", "Print Job Failed"  # print job
    PRINT_JOB_DONE = "PrintDone", "Print Job Done"  # print job
    PRINT_JOB_CANCELLING = "PrintCancelling", "Print Job Cancelling"  # print job
    PRINT_JOB_CANCELLED = "PrintCancelled", "Print Job Cancelled"  # print job
    PRINT_JOB_PAUSED = "PrintPaused", "Print Job Paused"  # print job
    PRINT_JOB_RESUMED = "PrintResumed", "Print Job Resumed"  # print job


class OctoPrintPrinterStatusType(models.TextChoices):
    OFFLINE = "PrinterOffline", "Printer is offline"
    OPEN_SERIAL = "PrinterOpenSerial", "Opening serial connection"
    CONNECTING = "PrinterConnecting", "Printer connecting"
    OPERATIONAL = "PrinterOperational", "Printer is ready to use"
    STARTING = "PrinterStarting", "Printer is starting job"
    PRINTING = "PrinterInProgress", "Printer is running job"
    CANCELLING = (
        "PrinterCancelling",
        "Printer is cancelling job",
    )
    PAUSING = (
        "PrinterPausing",
        "Printer is pausing job",
    )
    PAUSED = (
        "PrinterPaused",
        "Printer paused job",
    )
    RESUMING = (
        "PrinterResuming",
        "Printer is resuming job",
    )
    FINISHING = (
        "PrinterFinishing",
        "Printer is finishing job",
    )
    ERROR = "PrinterError", "Printer connection error"
