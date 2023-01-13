from enum import Enum


class OctoPrintServerStatusType(str, Enum):
    TEST = "Test"
    STARTUP = "Startup"
    SHUTDOWN = "Shutdown"

    def __str__(self) -> str:
        return str(self.value)
