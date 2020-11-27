# The following enums describe events sent from OctoPrint
# source: OctoPrint/src/octoprint/events.py
# Doc: https://docs.octoprint.org/en/master/events/index.html
# Please respect OctoPrint's AGPL license and do not copy any source code while this webapp is closed source.

from enum import Enum


# Uncomment event to begin tracking it
# Active events are accessed via GET /api/events/
#

class ClientEvents(Enum):
    '''
        OctoPrint javascript client / browser -> OctoPrint server (not Print Nanny webapp)
    '''

	# USER_LOGGED_IN = "UserLoggedIn"
	# USER_LOGGED_OUT = "UserLoggedOut"
	CLIENT_AUTHED = "ClientAuthed"
	CLIENT_CLOSED = "ClientClosed"
	CLIENT_DEAUTHED = "ClientDeauthed"
	CLIENT_OPENED = "ClientOpened"
	SETTINGS_UPDATED = "SettingsUpdated"

class FileEvents(Enum):


	
	# FILE_DESELECTED = "FileDeselected"
	# FILE_SELECTED = "FileSelected"
	# METADATA_ANALYSIS_FINISHED = "MetadataAnalysisFinished"
	# METADATA_STATISTICS_UPDATED = "MetadataStatisticsUpdated"
	FILE_ADDED = "FileAdded"
	FILE_REMOVED = "FileRemoved"
	FOLDER_ADDED = "FolderAdded"
	FOLDER_REMOVED = "FolderRemoved"
	TRANSFER_DONE = "TransferDone"
	TRANSFER_FAILED = "TransferFailed"
	TRANSFER_STARTED = "TransferStarted"
	UPDATED_FILES = "UpdatedFiles"
	UPLOAD = "Upload"
    # from octoprint filesystem -> sd card 
    # METADATA_ANALYSIS_STARTED = "MetadataAnalysisStarted"

class GcodeEvents(Enum):
    pass
	# ALERT = "Alert"
	# CONVEYOR = "Conveyor"
	# COOLING = "Cooling"
	# DWELL = "Dwelling"
	# E_STOP = "EStop"
	# EJECT = "Eject"
	# FIRMWARE_DATA = "FirmwareData"
	# HOME = "Home"
	# POSITION_UPDATE = "PositionUpdate"
	# POWER_OFF = "PowerOff"
	# POWER_ON = "PowerOn"
	# REGISTERED_MESSAGE_RECEIVED = "RegisteredMessageReceived"
	# TOOL_CHANGE = "ToolChange"
	# WAITING = "Waiting"
	# Z_CHANGE = "ZChange"

class PrinterProfileEvents(Enum):

	PRINTER_PROFILE_ADDED = "PrinterProfileAdded"
	PRINTER_PROFILE_DELETED = "PrinterProfileDeleted"
	PRINTER_PROFILE_MODIFIED = "PrinterProfileModified"

class PrintJobEvents(Enum):
	ERROR = "Error"
	PRINT_CANCELLED = "PrintCancelled"
	PRINT_CANCELLING = "PrintCancelling"
	PRINT_DONE = "PrintDone"
	PRINT_FAILED = "PrintFailed"
	PRINT_PAUSED = "PrintPaused"
	PRINT_RESUMED = "PrintResumed"
	PRINT_STARTED = "PrintStarted"

class ServerEvents(Enum):

	# CONNECTIVITY_CHANGED = "ConnectivityChanged"
	SHUTDOWN = "Shutdown"
    STARTUP = "Startup"

class ServerToPrinter(Enum):
    '''
        OctoPrint server (not Print Nanny webapp) -> printer events
    '''

	# CONNECTING = "Connecting"
	# DISCONNECTING = "Disconnecting"
	# PRINTER_STATE_CHANGED = "PrinterStateChanged"
	CONNECTED = "Connected"
	DISCONNECTED = "Disconnected"
	PRINTER_RESET = "PrinterReset"

class SlicerEvents(Enum):

	SLICING_CANCELLED = "SlicingCancelled"
	SLICING_DONE = "SlicingDone"
	SLICING_FAILED = "SlicingFailed"
	SLICING_PROFILE_ADDED = "SlicingProfileAdded"
	SLICING_PROFILE_DELETED = "SlicingProfileDeleted"
	SLICING_PROFILE_MODIFIED = "SlicingProfileModified"
	SLICING_STARTED = "SlicingStarted"

class TimelapseEvents(Enum):
	CAPTURE_DONE = "CaptureDone"
	CAPTURE_FAILED = "CaptureFailed"
	CAPTURE_START = "CaptureStart"
	MOVIE_DONE = "MovieDone"
	MOVIE_FAILED = "MovieFailed"
	MOVIE_RENDERING = "MovieRendering"
	POSTROLL_END = "PostRollEnd"
	POSTROLL_START = "PostRollStart"

class OctolapsePluginEvents(Enum):
    pass

class OctoPrintEvents(
    ClientEvents,
    FileEvents,
    GcodeEvents,
    PrintJobEvents,
    PrinterProfileEvents,
    SlicerEvents,
    TimelapseEvents,
    OctolapsePluginEvents
):
    pass