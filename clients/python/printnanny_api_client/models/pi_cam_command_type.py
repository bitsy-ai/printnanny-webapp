from enum import Enum


class PiCamCommandType(str, Enum):
    CAMSTART = "CamStart"
    CAMSTOP = "CamStop"

    def __str__(self) -> str:
        return str(self.value)
