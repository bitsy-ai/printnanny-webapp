import logging

from print_nanny_webapp.videos.services import finalize_video_recording
from config import celery_app

logger = logging.getLogger(__name__)


@celery_app.task()
def finalize_video_recording_task(video_recording_id: int):
    return finalize_video_recording(video_recording_id)
