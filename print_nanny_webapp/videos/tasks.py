import logging
from uuid import UUID

from django.apps import apps
from print_nanny_webapp.videos.services import finalize_video_recording
from config import celery_app

logger = logging.getLogger(__name__)

ChallengeCampaignLead = apps.get_model("videos", "ChallengeCampaignLead")


@celery_app.task()
def finalize_video_recording_task(video_recording_id: UUID):
    return finalize_video_recording(video_recording_id)


@celery_app.task()
def printnanny_challenge_task(challenge_id: int):
    entry = ChallengeCampaignLead.objects.get(id=challenge_id)
    logger.info("Processing ChallengeCampaignLead id=%s", entry.id)
