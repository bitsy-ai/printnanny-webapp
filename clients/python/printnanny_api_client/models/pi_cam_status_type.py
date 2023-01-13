from enum import Enum


class PiCamStatusType(str, Enum):
    CAMSTARTED = "CamStarted"
    CAMSTARTSUCCESS = "CamStartSuccess"
    CAMERROR = "CamError"
    CAMSTOPPED = "CamStopped"

    def __str__(self) -> str:
        return str(self.value)
