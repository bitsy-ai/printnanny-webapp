from django.db.models.signals import post_save
from django.dispatch import receiver


from print_nanny_webapp.events.models import PrintJobAlert
from print_nanny_webapp.events.tasks import send_print_job_alert_email_task


@receiver(post_save, sender=PrintJobAlert)
def create_print_job_alert_email_task(sender, instance, created, **kwargs):
    # only send when report is created for the first time
    if created:
        task = send_print_job_alert_email_task(instance.id)
        instance.celery_task_id = task.id
        instance.save()
