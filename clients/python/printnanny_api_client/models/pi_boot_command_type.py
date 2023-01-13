from enum import Enum


class PiBootCommandType(str, Enum):
    REBOOT = "Reboot"
    SHUTDOWN = "Shutdown"
    SYNCSETTINGS = "SyncSettings"
    SYSTEMCTLSHOW = "SystemctlShow"

    def __str__(self) -> str:
        return str(self.value)
