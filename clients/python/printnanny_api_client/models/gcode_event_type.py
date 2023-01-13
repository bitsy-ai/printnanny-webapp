from enum import Enum


class GcodeEventType(str, Enum):
    M300 = "M300"
    M245 = "M245"
    G4 = "G4"
    M112 = "M112"
    M600 = "M600"
    M701 = "M701"
    M702 = "M702"
    G28 = "G28"
    M81 = "M81"
    M80 = "M80"

    def __str__(self) -> str:
        return str(self.value)
