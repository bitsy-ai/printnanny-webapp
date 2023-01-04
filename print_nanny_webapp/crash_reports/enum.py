from django.db import models


class CrashReportStatusType(models.TextChoices):

    INVESTIGATING = (
        "Investigating",
        "Your report is being investigated, thank you!",
    )
    FIXED = (
        "Fixed",
        "A fix for your issue has been released. Please submit another crash report if the problem persists.",
    )
