from enum import Enum


class SbcEnum(str, Enum):
    RPI_4 = "rpi_4"

    def __str__(self) -> str:
        return str(self.value)
