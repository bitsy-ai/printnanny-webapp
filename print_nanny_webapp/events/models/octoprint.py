from django.db import models

from .pi import AbstractPiEvent
from .enum import OctoPrintEventType


# class OctoPrintEvent(AbstractPiEvent):
#     """
#     Events emitted by OctoPrint application
#     """

#     model = "OctoPrintEvent"

#     class Meta:
#         ordering = ["-created_dt"]
#         index_together = (("octoprint_server", "pi", "event_type", "created_dt"),)

#     octoprint_server = models.ForeignKey(
#         "octoprint.OctoPrintServer",
#         on_delete=models.CASCADE,
#         related_name="octoprint_events",
#     )
#     event_type = models.CharField(max_length=32, choices=OctoPrintEventType.choices)
