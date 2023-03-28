from config import celery_app
from uuid import UUID

from print_nanny_webapp.events.services import send_print_job_alert_email


@celery_app.task()
def send_print_job_alert_email_task(print_job_alert_id: UUID):
    return send_print_job_alert_email(print_job_alert_id)
