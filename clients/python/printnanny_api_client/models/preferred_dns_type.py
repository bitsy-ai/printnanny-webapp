from enum import Enum


class PreferredDnsType(str, Enum):
    MULTICAST = "multicast"
    TAILSCALE = "tailscale"

    def __str__(self) -> str:
        return str(self.value)
