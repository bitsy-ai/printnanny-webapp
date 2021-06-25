from celery import shared_task


@shared_task
def update_ghost_member_tag_task(email: str, tag: str):
    pass
