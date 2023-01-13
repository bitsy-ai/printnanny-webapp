from enum import Enum


class StripePriceTiersMode(str, Enum):
    GRADUATED = "graduated"
    VOLUME = "volume"

    def __str__(self) -> str:
        return str(self.value)
