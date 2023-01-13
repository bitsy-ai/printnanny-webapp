from enum import Enum


class AchievementTypeEnum(str, Enum):
    FREEBETA = "FreeBeta"
    FOUNDINGMEMBER = "FoundingMember"

    def __str__(self) -> str:
        return str(self.value)
