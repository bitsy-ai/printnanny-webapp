import logging
import asyncio
from datetime import timedelta

import django

from django.utils import timezone
from django.apps import apps
from django.db.models import Q
from asgiref.sync import sync_to_async

django.setup()
logger = logging.getLogger(__name__)

PERIOD = 30  # run task every n seconds
FINALIZE_TIME_LIMIT = 20  # time limit on outstanding finalize tasks (minutes)
VideoRecordings = apps.get_model("videos", "VideoRecording")


def get_video_recordings_ready_for_finalization():
    time_threshold = timezone.now() - timedelta(minutes=FINALIZE_TIME_LIMIT)
    # return all VideoRecordings where finalization hasn't been started, or that have execeeded FINALIZE_TIME_LIMIT since being started
    return VideoRecordings.objects.filter(
        Q(recording_start=None, cloud_sync_done=True)
        | Q(recording_start__lt=time_threshold, cloud_sync_done=True)
    )


async def finalize_video_recordings():
    get_recordings = sync_to_async(
        get_video_recordings_ready_for_finalization, thread_sensitive=True
    )
    recordings = await get_recordings()
    get_count = sync_to_async(recordings.count)
    count = await get_count()
    if count > 0:
        logger.info("Found %i VideoRecordings ready for finalization", count)


async def run_periodically(interval, periodic_function):
    while True:
        await asyncio.gather(
            asyncio.sleep(interval),
            periodic_function(),
        )


if __name__ == "__main__":
    logger.info("Initializing finalize_video_recordings.py worker")
    asyncio.run(run_periodically(PERIOD, finalize_video_recordings))
