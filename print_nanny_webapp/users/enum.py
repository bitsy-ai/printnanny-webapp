from django.db import models


class EmailListInterest(models.TextChoices):
    PRINTNANNY = (
        "printnanny",
        "Subscribe to PrintNanny news and development updates",
    )
    SDWIRE = "sdwire", "Get notified when SDWire is back in stock"
    RPI4_KIT = "rpi4_kit", "Get notified when Raspberry Pi 4 kits are available"
    PRINTNANNY_DEMO = (
        "printnanny_demo",
        "Uploaded image to PrintNanny challenge/demo marketing campaign",
    )
