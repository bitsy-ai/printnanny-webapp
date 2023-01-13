from enum import Enum


class PiBootStatusType(str, Enum):
    SYSTEMCTLSHOW = "SystemctlShow"
    REBOOTSTARTED = "RebootStarted"
    REBOOTERROR = "RebootError"
    SHUTDOWNSTARTED = "ShutdownStarted"
    SHUTDOWNERROR = "ShutdownError"
    BOOTSTARTED = "BootStarted"
    BOOTSUCCESS = "BootSuccess"
    BOOTDEGRADED = "BootDegraded"
    SYNCSETTINGSSTARTED = "SyncSettingsStarted"
    SYNCSETTINGSSUCCESS = "SyncSettingsSuccess"
    SYNCSETTINGSERROR = "SyncSettingsError"

    def __str__(self) -> str:
        return str(self.value)
