from django.db import models

##
# Python enum-based types required a custom Metaclass to support multi-inheritance
# Instead, I've just duplicated event types where inheritance is needed

# Example:
# TelemetryEventTypes is the Union of [OctoprintPluginEventTypes, OctoprintEventTypes, PrintJobEventTypes] etc
# but TelemetryEventTypes cannot be defined as inheriting from multiple enums with members defined
#
# I think the best long-term approach is to use Protobuf as the source of truth for schemas
# The data pipelines already use gRPC for inter-proc comms and django-db-model would make it easy to reference protobufs in Django model definitions
# django-db-model makes it easy to
##


class EventSource(models.TextChoices):
    OCTOPRINT = ("octoprint", "Events originating from octoprint")
    PRINT_NANNY_PLUGIN = (
        "plugin_octoprint_nanny",
        "Events originating from Print Nanny octoprint plugin",
    )
    REMOTE_COMMAND = (
        "remote_command",
        "Events originating from a remote control command",
    )


# Catch-all for all event types
class TelemetryEventType(models.TextChoices):

    ##
    #   source: OctoprintPluginEventType
    ##
    ##
    # emitted by Print Nanny Octoprint Plugin
    ##
    MONITORING_START = (
        "plugin_octoprint_nanny_monitoring_start",
        "Print Nanny Monitoring started",
    )
    MONITORING_STOP = (
        "plugin_octoprint_nanny_monitoring_stop",
        "Print Nanny Monitoring stopped",
    )
    MONITORING_RESET = (
        "plugin_octoprint_nanny_monitoring_reset",
        "Print Nanny Monitoring reset",
    )

    DEVICE_REGISTER_START = (
        "plugin_octoprint_nanny_device_register_start",
        "Device registration started",
    )
    DEVICE_REGISTER_DONE = (
        "plugin_octoprint_nanny_device_register_done",
        "Device registration succeeded",
    )
    DEVICE_REGISTER_FAILED = (
        "plugin_octoprint_nanny_device_register_failed",
        "Device registration failed",
    )
    DEVICE_RESET = "plugin_octoprint_nanny_device_reset", "Device identity reset"

    PRINTER_PROFILE_SYNC_START = (
        "plugin_octoprint_nanny_printer_profile_sync_start",
        "Printer profile sync started",
    )
    PRINTER_PROFILE_SYNC_DONE = (
        "plugin_octoprint_nanny_printer_profile_sync_done",
        "Printer profile sync succeeded",
    )
    PRINTER_PROFILE_SYNC_FAILED = (
        "plugin_octoprint_nanny_printer_profile_sync_failed",
        "Printer profile sync failed",
    )

    CONNECT_TEST_REST_API = (
        "plugin_octoprint_nanny_connect_test_rest_api",
        "Test connection to REST API",
    )
    CONNECT_TEST_REST_API_FAILED = (
        "plugin_octoprint_nanny_connect_test_rest_api_failed",
        "Test connection to REST API failed",
    )
    CONNECT_TEST_REST_API_SUCCESS = (
        "plugin_octoprint_nanny_connect_test_rest_api_success",
        "Test connection to REST API success",
    )

    CONNECT_TEST_MQTT_PING = (
        "plugin_octoprint_nanny_connect_test_mqtt_ping",
        "Test connection to REST API",
    )
    CONNECT_TEST_MQTT_PING_FAILED = (
        "plugin_octoprint_nanny_connect_test_mqtt_ping_failed",
        "Test connection to REST API failed",
    )
    CONNECT_TEST_MQTT_PING_SUCCESS = (
        "plugin_octoprint_nanny_connect_test_mqtt_ping_success",
        "Test connection to REST API success",
    )

    CONNECT_TEST_MQTT_PONG = (
        "plugin_octoprint_nanny_connect_test_mqtt_pong",
        "Test connection to REST API",
    )
    CONNECT_TEST_MQTT_PONG_FAILED = (
        "plugin_octoprint_nanny_connect_test_mqtt_pong_failed",
        "Test connection to REST API failed",
    )
    CONNECT_TEST_MQTT_PONG_SUCCESS = (
        "plugin_octoprint_nanny_connect_test_mqtt_pong_success",
        "Test connection to REST API success",
    )

    ##
    # Source: OctoprintEventType
    ##

    # OctoPrint javascript client / browser -> OctoPrint server (not Print Nanny webapp)
    CLIENT_AUTHED = "ClientAuthed", "ClientAuthed"
    CLIENT_CLOSED = "ClientClosed", "ClientClosed"
    CLIENT_DEAUTHED = "ClientDeauthed", "ClientDeauthed"
    CLIENT_OPENED = "ClientOpened", "ClientOpened"
    SETTINGS_UPDATED = "SettingsUpdated", "SettingsUpdated"

    USER_LOGGED_IN = "UserLoggedIn"
    USER_LOGGED_OUT = "UserLoggedOut"

    # file events
    # FILE_DESELECTED = "FileDeselected"
    # FILE_SELECTED = "FileSelected"
    # METADATA_ANALYSIS_FINISHED = "MetadataAnalysisFinished"
    # METADATA_STATISTICS_UPDATED = "MetadataStatisticsUpdated"
    FILE_ADDED = "FileAdded", "FileAdded"
    FILE_REMOVED = "FileRemoved", "FileRemoved"
    FOLDER_ADDED = "FolderAdded", "FolderAdded"
    FOLDER_REMOVED = "FolderRemoved", "FolderRemoved"
    TRANSFER_DONE = "TransferDone", "TransferDone"
    TRANSFER_FAILED = "TransferFailed", "TransferFailed"
    TRANSFER_STARTED = "TransferStarted", "TransferStarted"
    UPDATED_FILES = "UpdatedFiles", "UpdatedFiles"
    UPLOAD = "Upload", "Upload"

    # timelapse
    CAPTURE_DONE = "CaptureDone", "CaptureDone"
    CAPTURE_FAILED = "CaptureFailed", "CaptureFailed"
    CAPTURE_START = "CaptureStart", "CaptureStart"
    MOVIE_DONE = "MovieDone", "MovieDone"
    MOVIE_FAILED = "MovieFailed", "MovieFailed"
    MOVIE_RENDERING = "MovieRendering", "MovieRendering"
    POSTROLL_END = "PostRollEnd", "PostRollEnd"
    POSTROLL_START = "PostRollStart", "PostRollStart"

    # slicer
    SLICING_CANCELLED = "SlicingCancelled", "SlicingCancelled"
    SLICING_DONE = "SlicingDone", "SlicingDone"
    SLICING_FAILED = "SlicingFailed", "SlicingFailed"
    SLICING_PROFILE_ADDED = "SlicingProfileAdded", "SlicingProfileAdded"
    SLICING_PROFILE_DELETED = "SlicingProfileDeleted", "SlicingProfileDeleted"
    SLICING_PROFILE_MODIFIED = "SlicingProfileModified", "SlicingProfileModified"
    SLICING_STARTED = "SlicingStarted", "SlicingStarted"

    # octoprint server <-> printer telemetry
    CONNECTED = "Connected", "Connected"
    DISCONNECTED = "Disconnected", "Disconnected"
    PRINTER_RESET = "PrinterReset", "PrinterReset"
    FIRMWARE_DATA = "FirmwareData", "FirmwareData"

    # printer profile
    PRINTER_PROFILE_ADDED = "PrinterProfileAdded", "PrinterProfileAdded"
    PRINTER_PROFILE_DELETED = "PrinterProfileDeleted", "PrinterProfileDeleted"
    PRINTER_PROFILE_MODIFIED = "PrinterProfileModified", "PrinterProfileModified"

    # print progress
    PRINT_PROGRESS = "PrintProgress", "PrintProgress"

    # pi throttle state
    # @todo (not sure why this event is formatted different by octoprint)
    PI_THROTTLE_STATE = (
        "plugin_pi_support_throttle_state",
        "plugin_pi_support_throttle_state",
    )

    # octoprint server
    # CONNECTIVITY_CHANGED = "ConnectivityChanged"
    SHUTDOWN = "Shutdown", "Shutdown"
    STARTUP = "Startup", "Startup"

    ##
    #   source: RemoteCommandEventType
    ##

    REMOTE_COMMAND_RECEIVED = (
        "remote_command_received",
        "Command was received by device",
    )

    REMOTE_COMMAND_FAILED = (
        "remote_command_failed",
        "Command failed. Please download your Octoprint logs and open a Github issue to get this fixed.",
    )

    REMOTE_COMMAND_SUCCESS = (
        "remote_command_success",
        "Command succeeded",
    )

    ##
    # source: PrintJobEventType
    ##

    PRINT_CANCELLED = "PrintCancelled", "PrintCancelled"
    PRINT_CANCELLING = "PrintCancelling", "PrintCancelling"
    PRINT_DONE = "PrintDone", "PrintDone"
    PRINT_FAILED = "PrintFailed", "PrintFailed"
    PRINT_PAUSED = "PrintPaused", "PrintPaused"
    PRINT_RESUMED = "PrintResumed", "PrintResumed"
    PRINT_STARTED = "PrintStarted", "PrintStarted"
    PRINTER_STATE_CHANGED = "PrinterStateChanged", "PrinterStateChanged"


class PrintNannyPluginEventType(models.TextChoices):
    """
    Enumerates all plugin_octoprint_nanny_* event_type values
    """

    ##
    # emitted by Print Nanny Octoprint Plugin
    ##
    MONITORING_START = (
        "plugin_octoprint_nanny_monitoring_start",
        "Print Nanny Monitoring started",
    )
    MONITORING_STOP = (
        "plugin_octoprint_nanny_monitoring_stop",
        "Print Nanny Monitoring stopped",
    )
    MONITORING_RESET = (
        "plugin_octoprint_nanny_monitoring_reset",
        "Print Nanny Monitoring reset",
    )

    DEVICE_REGISTER_START = (
        "plugin_octoprint_nanny_device_register_start",
        "Device registration started",
    )
    DEVICE_REGISTER_DONE = (
        "plugin_octoprint_nanny_device_register_done",
        "Device registration succeeded",
    )
    DEVICE_REGISTER_FAILED = (
        "plugin_octoprint_nanny_device_register_failed",
        "Device registration failed",
    )
    DEVICE_RESET = "plugin_octoprint_nanny_device_reset", "Device identity reset"

    PRINTER_PROFILE_SYNC_START = (
        "plugin_octoprint_nanny_printer_profile_sync_start",
        "Printer profile sync started",
    )
    PRINTER_PROFILE_SYNC_DONE = (
        "plugin_octoprint_nanny_printer_profile_sync_done",
        "Printer profile sync succeeded",
    )
    PRINTER_PROFILE_SYNC_FAILED = (
        "plugin_octoprint_nanny_printer_profile_sync_failed",
        "Printer profile sync failed",
    )

    CONNECT_TEST_REST_API = (
        "plugin_octoprint_nanny_connect_test_rest_api",
        "Test connection to REST API",
    )
    CONNECT_TEST_REST_API_FAILED = (
        "plugin_octoprint_nanny_connect_test_rest_api_failed",
        "Test connection to REST API failed",
    )
    CONNECT_TEST_REST_API_SUCCESS = (
        "plugin_octoprint_nanny_connect_test_rest_api_success",
        "Test connection to REST API success",
    )

    CONNECT_TEST_MQTT_PING = (
        "plugin_octoprint_nanny_connect_test_mqtt_ping",
        "Test connection to REST API",
    )
    CONNECT_TEST_MQTT_PING_FAILED = (
        "plugin_octoprint_nanny_connect_test_mqtt_ping_failed",
        "Test connection to REST API failed",
    )
    CONNECT_TEST_MQTT_PING_SUCCESS = (
        "plugin_octoprint_nanny_connect_test_mqtt_ping_success",
        "Test connection to REST API success",
    )

    CONNECT_TEST_MQTT_PONG = (
        "plugin_octoprint_nanny_connect_test_mqtt_pong",
        "Test connection to REST API",
    )
    CONNECT_TEST_MQTT_PONG_FAILED = (
        "plugin_octoprint_nanny_connect_test_mqtt_pong_failed",
        "Test connection to REST API failed",
    )
    CONNECT_TEST_MQTT_PONG_SUCCESS = (
        "plugin_octoprint_nanny_connect_test_mqtt_pong_success",
        "Test connection to REST API success",
    )


class OctoprintEventType(models.TextChoices):
    # OctoPrint javascript client / browser -> OctoPrint server (not Print Nanny webapp)
    CLIENT_AUTHED = "ClientAuthed", "ClientAuthed"
    CLIENT_CLOSED = "ClientClosed", "ClientClosed"
    CLIENT_DEAUTHED = "ClientDeauthed", "ClientDeauthed"
    CLIENT_OPENED = "ClientOpened", "ClientOpened"
    SETTINGS_UPDATED = "SettingsUpdated", "SettingsUpdated"

    USER_LOGGED_IN = "UserLoggedIn"
    USER_LOGGED_OUT = "UserLoggedOut"

    # file events
    # FILE_DESELECTED = "FileDeselected"
    # FILE_SELECTED = "FileSelected"
    # METADATA_ANALYSIS_FINISHED = "MetadataAnalysisFinished"
    # METADATA_STATISTICS_UPDATED = "MetadataStatisticsUpdated"
    FILE_ADDED = "FileAdded", "FileAdded"
    FILE_REMOVED = "FileRemoved", "FileRemoved"
    FOLDER_ADDED = "FolderAdded", "FolderAdded"
    FOLDER_REMOVED = "FolderRemoved", "FolderRemoved"
    TRANSFER_DONE = "TransferDone", "TransferDone"
    TRANSFER_FAILED = "TransferFailed", "TransferFailed"
    TRANSFER_STARTED = "TransferStarted", "TransferStarted"
    UPDATED_FILES = "UpdatedFiles", "UpdatedFiles"
    UPLOAD = "Upload", "Upload"

    # timelapse
    CAPTURE_DONE = "CaptureDone", "CaptureDone"
    CAPTURE_FAILED = "CaptureFailed", "CaptureFailed"
    CAPTURE_START = "CaptureStart", "CaptureStart"
    MOVIE_DONE = "MovieDone", "MovieDone"
    MOVIE_FAILED = "MovieFailed", "MovieFailed"
    MOVIE_RENDERING = "MovieRendering", "MovieRendering"
    POSTROLL_END = "PostRollEnd", "PostRollEnd"
    POSTROLL_START = "PostRollStart", "PostRollStart"

    # slicer
    SLICING_CANCELLED = "SlicingCancelled", "SlicingCancelled"
    SLICING_DONE = "SlicingDone", "SlicingDone"
    SLICING_FAILED = "SlicingFailed", "SlicingFailed"
    SLICING_PROFILE_ADDED = "SlicingProfileAdded", "SlicingProfileAdded"
    SLICING_PROFILE_DELETED = "SlicingProfileDeleted", "SlicingProfileDeleted"
    SLICING_PROFILE_MODIFIED = "SlicingProfileModified", "SlicingProfileModified"
    SLICING_STARTED = "SlicingStarted", "SlicingStarted"

    # octoprint server <-> printer telemetry
    CONNECTED = "Connected", "Connected"
    DISCONNECTED = "Disconnected", "Disconnected"
    PRINTER_RESET = "PrinterReset", "PrinterReset"
    FIRMWARE_DATA = "FirmwareData", "FirmwareData"

    # printer profile
    PRINTER_PROFILE_ADDED = "PrinterProfileAdded", "PrinterProfileAdded"
    PRINTER_PROFILE_DELETED = "PrinterProfileDeleted", "PrinterProfileDeleted"
    PRINTER_PROFILE_MODIFIED = "PrinterProfileModified", "PrinterProfileModified"

    # print progress
    PRINT_PROGRESS = "PrintProgress", "PrintProgress"

    # pi throttle state
    # @todo (not sure why this event is formatted different by octoprint)
    PI_THROTTLE_STATE = (
        "plugin_pi_support_throttle_state",
        "plugin_pi_support_throttle_state",
    )

    # octoprint server
    # CONNECTIVITY_CHANGED = "ConnectivityChanged"
    SHUTDOWN = "Shutdown", "Shutdown"
    STARTUP = "Startup", "Startup"


class RemoteCommandEventType(models.TextChoices):

    REMOTE_COMMAND_RECEIVED = (
        "remote_command_received",
        "Command was received by device",
    )

    REMOTE_COMMAND_FAILED = (
        "remote_command_failed",
        "Command failed. Please download your Octoprint logs and open a Github issue to get this fixed.",
    )

    REMOTE_COMMAND_SUCCESS = (
        "remote_command_success",
        "Command succeeded",
    )


class PrintJobEventType(models.TextChoices):

    # print job
    PRINT_CANCELLED = "PrintCancelled", "PrintCancelled"
    PRINT_CANCELLING = "PrintCancelling", "PrintCancelling"
    PRINT_DONE = "PrintDone", "PrintDone"
    PRINT_FAILED = "PrintFailed", "PrintFailed"
    PRINT_PAUSED = "PrintPaused", "PrintPaused"
    PRINT_RESUMED = "PrintResumed", "PrintResumed"
    PRINT_STARTED = "PrintStarted", "PrintStarted"
    PRINTER_STATE_CHANGED = "PrinterStateChanged", "PrinterStateChanged"


class PrinterEventType(models.TextChoices):
    OPERATIONAL = "Operational", "Printer Connected"
    PAUSED = "Paused", "Paused"
    CANCELLING = "Cancelling", "Cancelling"
    PRINTING = "Printing", "Printing"
    PAUSING = "Pausing", "Pausing"
    SD_READY = "sdReady", "SD Card Available"
    ERROR = "Error", "Error"
    READY = "Ready" "Printer Ready"
    CLOSED_OR_ERROR = "closedOrError", "Printer Connection Closed"
    OFFLINE = "Offline", "Printer Offline"
    OPEN_SERIAL = "Opening serial connection", "Opening serial connection"
    CONNECTING = "Connection", "Establishing printer connection"
    RESUMING = "Resuming", "Resuming"
    FINISHING = "Finishing", "Finishing"
