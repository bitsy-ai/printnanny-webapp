from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from django.contrib.postgres.fields import ArrayField

User = get_user_model()

#TFLiteModel = apps.get_model('ml_ops', 'TFLiteModel')

class PrinterProfile(models.Model):

    class Meta:
        unique_together = ('user', 'name',)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    axes_e_inverted = models.BooleanField()
    axes_e_speed = models.IntegerField()

    axes_x_speed = models.IntegerField()
    axes_x_inverted = models.BooleanField()

    axes_y_inverted = models.BooleanField()
    axes_y_speed = models.IntegerField()

    axes_z_inverted = models.BooleanField()
    axes_z_speed = models.IntegerField()

    extruder_count = models.IntegerField()
    extruder_nozzle_diameter = models.FloatField()

    extruder_offsets = ArrayField(
        ArrayField(
            models.FloatField(),
        ),
        null=True
    )
    extruder_shared_nozzle = models.BooleanField()

    heated_bed = models.BooleanField()
    heated_chamber = models.BooleanField()

    model = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)

    volume_custom_box = models.BooleanField()
    volume_depth = models.FloatField()
    volume_formfactor = models.CharField(max_length=255)
    volume_height = models.FloatField()
    volume_origin = models.CharField(max_length=255)
    volume_width = models.FloatField()

class GcodeFile(models.Model):
    class Meta:
        unique_together = ('user', 'file_hash')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


    file = models.FileField(upload_to='uploads/gcode_file/%Y/%m/%d/')
    file_hash = models.CharField(max_length=255)

class PrintJob(models.Model):
    class Meta:
        unique_together = ('user', 'name', 'dt')

    class StatusChoices(models.TextChoices):
        STARTED = 'STARTED', 'Started'
        DONE = 'DONE', 'Done'
        FAILED = 'FAILED', 'Failed'
        CANCELLING = 'CANCELLING', 'Cancelling'
        CANCELLED = 'CANCELLED', 'Cancelled'
        PAUSED = 'PAUSED', 'Paused'
        RESUMED = 'RESUMED', 'Resumed'

    dt = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    printer_profile = models.ForeignKey(PrinterProfile, on_delete=models.RESTRICT)
    name = models.CharField(max_length=255)
    gcode_file_hash = models.CharField(max_length=255, null=True)
    gcode_file = models.ForeignKey(GcodeFile, on_delete=models.RESTRICT, null=True)
    last_status = models.CharField(
        max_length=12,
        choices=StatusChoices.choices,
        default=StatusChoices.STARTED
    )
    last_seen = models.DateTimeField(auto_now=True)

class PredictEventFile(models.Model):

    annotated_image = models.ImageField('uploads/predict_event/%Y/%m/%d/')
    hash = models.CharField(max_length=255)
    original_image = models.ImageField('uploads/predict_event/%Y/%m/%d/')


class PredictEvent(models.Model):

    dt = models.DateTimeField(db_index=True, default=timezone.now)
    #model = models.ForeignKey(TFLiteModel)
    event_data = models.JSONField(null=True)
    predict_data = models.JSONField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    files = models.ForeignKey(PredictEventFile, on_delete=models.CASCADE)
    print_job = models.ForeignKey(PrintJob, on_delete=models.CASCADE)

    plugin_version = models.CharField(max_length=30)
    octoprint_version = models.CharField(max_length=30)

class OctoPrintEvent(models.Model):

    dt = models.DateTimeField(db_index=True)
    event_type = models.CharField(max_length=30, db_index=True)
    event_data = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    plugin_version = models.CharField(max_length=30)
    octoprint_version = models.CharField(max_length=30)
    print_job = models.ForeignKey(PrintJob, null=True, on_delete=models.SET_NULL, db_index=True)

class EmailNotification(models.Model):

    class StatusChoices(models.TextChoices):
        SENT = 'SENT', 'Sent'
        DONE = 'DONE', 'Done'
        FAILED = 'FAILED', 'Failed'
        CANCELLING = 'CANCELLING', 'Cancelling'
        CANCELLED = 'CANCELLED', 'Cancelled'
        PAUSED = 'PAUSED', 'Paused'
        RESUMED = 'RESUMED', 'Resumed'


class AlertMessage(models.Model):
    """
        outgoing message to user
    """
    class Backend(models.TextChoices):
        EMAIL = 'EMAIL', 'Email'
    

    # subsequent alerts will be paused if message exists in the following state:

    # Row created (PENDING) ->
    # Email enqueued for send (SENT) ->
    # Email opened (READ) ->

    class ActionChoices(models.TextChoices):
        WAITING = 'WAITING', 'Waiting'
        RESUMED = 'RESUMED', 'Resumed'
        STOPPED = 'STOPPED', 'Stopped'
    
    created_dt = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_dt = models.DateTimeField(auto_now=True, db_index=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    print_job = models.ForeignKey(PrintJob, on_delete=models.CASCADE, db_index=True)
    video = models.ImageField(upload_to='uploads/alert/%Y/%m/%d/')
    provider_id = models.CharField(max_length=255, null=True, db_index=True)
    last_action = models.CharField(
        max_length=12,
        choices=ActionChoices.choices,
        default=ActionChoices.WAITING
    )

    tags = ArrayField(
        models.CharField(max_length=255),
        default=["default-alert-message"]
    )

    dataframe = models.JSONField()


class AlertEvent(models.Model):
    """
        inbound alert events, like open and click on an email
    """

    class AnymailStatusChoices(models.TextChoices):
        DELIVERED = 'DELIEVERED', 'Delivered'
        REJECTED = 'REJECTED', 'Rejected'
        BOUNCED = 'BOUNCED', 'Bounced',
        COMPLAINED = 'COMPLAINED','Complained',
        UNSUBSCRIBED = 'UNSUBSCRIBED', 'Unsubscribed'
        OPENED = 'OPENED', 'Opened',
        CLICKED = 'CLICKED', 'Clicked'

    event_type = models.CharField(
        max_length=12,
        choices=AnymailStatusChoices.choices,
    )
    dt = models.DateTimeField(db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    alert_message = models.ForeignKey(AlertMessage, on_delete=models.CASCADE)
    provider_id = models.CharField(max_length=255)
    event_data = models.JSONField()
