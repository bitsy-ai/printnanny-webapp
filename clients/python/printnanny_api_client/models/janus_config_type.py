from enum import Enum


class JanusConfigType(str, Enum):
    CLOUD = "cloud"
    EDGE = "edge"

    def __str__(self) -> str:
        return str(self.value)
