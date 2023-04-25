from django.db import models


class EmailListInterest(models.TextChoices):
    PRINTNANNY = "printnanny", "Subscribe to PrintNanny news and development updates"
    SDWIRE = "sdwire", "Get notified when SDWire is back in stock"
