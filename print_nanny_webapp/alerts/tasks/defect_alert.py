from celery import shared_task

@shared_task
def trigger_defect_alert()