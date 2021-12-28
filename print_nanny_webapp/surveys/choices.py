from django.db import models


class PrimaryOS(models.TextChoices):
    MACOS = "macos", "macOS"
    WINDOWS = "windows", "Windows"
    LINUX = "linux", "Linux"


class MobileOS(models.TextChoices):
    MOBILE = "android", "Android"
    IOS = "ios", "iOS"


class NetworkType(models.TextChoices):
    HOME = "home", "Personal home/residential network"
    OFFICE = "office", "Corporate, industrial park, warehouse network"
    SCHOOL = "school", "University, school, maker space network"


class VPNExperience(models.TextChoices):
    VPN_NO = "vpn_no", "I am not interested in remote access"
    VPN_NEWBIE = (
        "vpn_newbie",
        "I have never used a VPN, but am interested in remote printer access",
    )
    VPN_USER = (
        "vpn_user",
        "I currently/recently use a managed VPN service (examples: TailScale, ZeroTier)",
    )
    VPN_ADMIn = (
        "vpn_admin",
        "I manage my own VPN or mesh network at work, home, or school",
    )


class UserScale(models.TextChoices):
    SINGLEUSER = (
        "singleuser",
        "I want personal access to my Raspberry Pi, 3D printers, or home computers from anywhere in the world",
    )
    MULTISITE = (
        "multisite",
        "I want to manage 3D printers across multiple networks or job sites",
    )
    MULTIUSER = "multiuser", "I want to provide access to my employees"
    CRM = "crm", "I want to automatically send status updates to customers"
    SOCIAL = (
        "social",
        "I want to share a camera feed with my followers, classroom, or other large audience",
    )
    TIMESHARE = (
        "timeshare",
        "I want to manage/schedule timeshares for 3D printers, 3D scanners, or other hardware",
    )
    OTHER = "other", "Other"


class PrinterSoftware(models.TextChoices):
    OCTOPRINT = "octoprint", "OctoPrint"
    MAINSAIL = "mainsail", "Mainsail"
    FLUIDD = "fluidd", "Fluidd"
    REPETIER = "repetier", "Repetier"
    CREALITY_BOX = "creality_box", "Creality Box"
    ASTROPRINT = "astroprint", "Astroprint"
    SIMPLIFY3D = "simplify3d", "Simplify 3D"
    PRINTER3DOS = "3dprinteros", "3D Printer OS"
    OTHER = "other", "Other"
